"""
test_teklif_degerlendirme.py — TUR 3.25 §12/§13 TESTLERI

===========================================================================
 KAPSAM
===========================================================================
  A) SINIFLANDIRMA   : FIRM_QUOTE dogrulama kurali (QV-1..QV-6) — 10 vektor
  B) FX KOPRUSU      : ayni teklif DORT EKSENDE ayri sonuc verir — 4x4 hucre
  C) TEK YONLU KARAR : kopru eksikken YALNIZCA ABOVE_CEILING kararlastirilabilir
  D) RET YASAGI      : REJECTED/KILL/VIABLE URETILEMEZ (koda gomulu)
  E) INTERNAL_ONLY   : dosya adi kilidi + sizinti taramasi
  F) ENTEGRASYON     : gercek CSV bandi + gercek makro.yaml dort ekseni

===========================================================================
 ⛔ TEST_FIXTURE DISIPLINI
===========================================================================
  - Sentetik degerler YALNIZCA `inputs/TEST_FIXTURE-teklif-vektorleri.yaml`
    dosyasindan, `TEST_FIXTURE_*` on ekli degiskenlere okunur.
  - `guvenli_girdi_yukle()` bu dosyayi REDDEDER (uretim yolu kapali);
    burada BILEREK ve TEK BIR yerde `yaml.safe_load` ile okunur.
  - Fixture tedarikci adlari UYDURMADIR; havuzdaki SUP-### ile eslesmez.
  - Fixture kurlari GERCEK KUR DEGILDIR: gercek kur `ttl 7d`'dir, testler
    ona baglanirsa haftalik kirilir. Gercek okuma AYRI (F) testlerinde.

Calistirma:  python3 80-model/engine/test_teklif_degerlendirme.py
"""

from __future__ import annotations

import sys
from datetime import date
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml  # noqa: E402

import teklif_degerlendirme as TD  # noqa: E402
from kalem_defteri import DAMGA_BLOCKED, FixtureSizintisi, guvenli_girdi_yukle  # noqa: E402

D = Decimal
INPUTS = Path(__file__).resolve().parent.parent / "inputs"
TEST_FIXTURE_DOSYASI = INPUTS / "TEST_FIXTURE-teklif-vektorleri.yaml"

BUGUN = date(2026, 8, 10)

SONUCLAR: list[tuple[str, str, str, bool]] = []


def kaydet(kod: str, beklenen: str, gerceklesen: str, ok: bool) -> None:
    SONUCLAR.append((kod, beklenen, gerceklesen, ok))


# ---------------------------------------------------------------------------
# FIXTURE — TEK NOKTA, ACIK AD
# ---------------------------------------------------------------------------

def TEST_FIXTURE_yukle() -> dict:
    """⛔ SENTETIK. Uretim kodu bu fonksiyonu CAGIRAMAZ."""
    with TEST_FIXTURE_DOSYASI.open("r", encoding="utf-8") as f:
        veri = yaml.safe_load(f)
    assert veri.get("TEST_FIXTURE") is True, "Fixture dosyasi TEST_FIXTURE: true tasimali"
    assert veri.get("uretim_girdisi_mi") is False
    assert veri.get("status") == "TEST_FIXTURE"
    return veri


TEST_FIXTURE = TEST_FIXTURE_yukle()
TEST_FIXTURE_VEKTORLER = {v["kod"]: v for v in TEST_FIXTURE["vektorler"]}
TEST_FIXTURE_BAND_HAM = TEST_FIXTURE["TEST_FIXTURE_band"]
TEST_FIXTURE_FX_HAM = TEST_FIXTURE["TEST_FIXTURE_fx_eksenleri"]
TEST_FIXTURE_KOPRU_TAM = TEST_FIXTURE["TEST_FIXTURE_kopru_tam"]
TEST_FIXTURE_KOPRU_YOK = TEST_FIXTURE["TEST_FIXTURE_kopru_yok"]
ENTEGRASYON_CAPALARI = TEST_FIXTURE["entegrasyon_capalari"]

SEMA = guvenli_girdi_yukle(INPUTS / "quote-ingestion-schema.yaml")


def TEST_FIXTURE_band() -> TD.TavanBandi:
    h = TEST_FIXTURE_BAND_HAM
    return TD.TavanBandi(
        hedef_id=h["hedef_id"], kanal=h["kanal"], mense_grubu=h["mense_grubu"],
        X_try=D(str(h["X_try"])), Y_try=D(str(h["Y_try"])),
        kaynak="TEST_FIXTURE (SENTETIK)", blocked_input_count=0,
    )


def TEST_FIXTURE_eksenler() -> dict[str, TD.FXEkseni]:
    out: dict[str, TD.FXEkseni] = {}
    for kod in TD.FX_EKSEN_SIRASI:
        e = TEST_FIXTURE_FX_HAM[kod]
        out[kod] = TD.FXEkseni(
            kod=kod, eur_try=D(str(e["eur_try"])), usd_try=D(str(e["usd_try"])),
            status="SENSITIVITY_AXIS", kaynak="TEST_FIXTURE (SENTETIK)",
            kur_tipi="TEST_FIXTURE",
        )
    return out


def TEST_FIXTURE_kopru(secim: str) -> TD.Kopru:
    if secim == "YOK":
        return TD.Kopru()
    ham = TEST_FIXTURE_KOPRU_TAM
    k = TD.Kopru()
    for kk in ham["fob_cif"]:
        k.fob_cif.append(TD.KopruKalemi(
            ad=kk["ad"], tutar=D(str(kk["tutar"])), currency=kk["currency"],
            evidence_id=kk["evidence_id"], status=kk["status"]))
    if secim == "TAM":
        for kk in ham["exw_fob"]:
            k.exw_fob.append(TD.KopruKalemi(
                ad=kk["ad"], tutar=D(str(kk["tutar"])), currency=kk["currency"],
                evidence_id=kk["evidence_id"], status=kk["status"]))
    return k


def teklif_of(kod: str) -> TD.Teklif:
    v = TEST_FIXTURE_VEKTORLER[kod]
    t = TD.teklif_kur(dict(v["teklif"]))
    t.kopru = TEST_FIXTURE_kopru(v.get("kopru", "YOK"))
    return t


def degerlendir(kod: str) -> list[TD.Degerlendirme]:
    t = teklif_of(kod)
    band = TEST_FIXTURE_band()
    out: list[TD.Degerlendirme] = []
    for k in t.kademeler:
        out += TD.kademe_degerlendir(
            t, k, band, TEST_FIXTURE_eksenler(), SEMA, BUGUN,
            hedef_id="TGT_799", kanal="CHAIN_RETAIL",
        )
    return out


# ===========================================================================
# A) SINIFLANDIRMA
# ===========================================================================

def _sinif_testi(kod: str) -> None:
    v = TEST_FIXTURE_VEKTORLER[kod]
    bek = v["beklenen"]
    t = teklif_of(kod)
    sinif, zorlanan, ihlaller = TD.sinif_belirle(t, t.kademeler[0], SEMA, BUGUN)
    ok = True
    parca: list[str] = [f"sinif={sinif}"]
    if "etkin_sinif" in bek:
        ok = ok and sinif == bek["etkin_sinif"]
    if "sonuc" in bek:
        sonuclar = {d.sonuc for d in degerlendir(kod)}
        parca.append(f"sonuclar={sorted(sonuclar)}")
        ok = ok and sonuclar == {bek["sonuc"]}
    if "ihlal_kural" in bek:
        kidler = {i.kural_id for i in ihlaller}
        parca.append(f"ihlaller={sorted(kidler)}")
        ok = ok and bek["ihlal_kural"] in kidler
    kaydet(kod, str(bek), " ".join(parca), ok)


def a_siniflandirma() -> None:
    for kod in ("TQV-1", "TQV-2", "TQV-3", "TQV-4", "TQV-5", "TQV-6",
                "TQV-12", "TQV-13", "TQV-14", "TQV-15"):
        _sinif_testi(kod)


# ===========================================================================
# B) FX KOPRUSU — DORT EKSEN, DORT AYRI SONUC
# ===========================================================================

def _fx_testi(kod: str) -> None:
    bek = TEST_FIXTURE_VEKTORLER[kod]["beklenen"]
    gercek = {d.fx_ekseni: d.sonuc for d in degerlendir(kod)}
    ok = all(gercek.get(e) == b for e, b in bek.items())
    kaydet(kod, " ".join(f"{e}={b}" for e, b in bek.items()),
           " ".join(f"{e}={gercek.get(e)}" for e in TD.FX_EKSEN_SIRASI), ok)


def b_fx_eksenleri() -> None:
    for kod in ("TQV-7A", "TQV-7B", "TQV-9", "TQV-10", "TQV-11"):
        _fx_testi(kod)


def b_tek_teklif_iki_sonuc() -> None:
    """AYNI teklif, ayni gun, FARKLI eksende FARKLI sonuc -> tek kur ile tek
    sonuc uretmek YANLIS olurdu."""
    s = {d.fx_ekseni: d.sonuc for d in degerlendir("TQV-7A")}
    ok = len(set(s.values())) > 1
    kaydet("FX::EKSEN_AYRISMASI", "ayni teklif -> en az iki farkli sonuc",
           str(sorted(set(s.values()))), ok)


def b_band_fx_araligindan_genis() -> None:
    """
    YAPISAL BULGU: X->Y bandi (x1,4455) FX ekseninin acikligindan (1,20/0,90
    = x1,3333) GENISTIR. Bu nedenle TEK bir teklif, salt FX hareketiyle
    STRONG'dan ABOVE_CEILING'e GECEMEZ.
    """
    band = TEST_FIXTURE_band()
    band_orani = band.Y_try / band.X_try
    fx_orani = TD.FX_EKSEN_CARPANLARI["FX_UP_20"] / TD.FX_EKSEN_CARPANLARI["FX_DOWN_10"]
    ok = band_orani > fx_orani
    kaydet("FX::BAND_GENISLIGI", "band orani > fx ekseni acikligi",
           f"band={band_orani:.4f} fx={fx_orani:.4f}", ok)


# ===========================================================================
# C) TEK YONLU KARAR
# ===========================================================================

def c_tek_yonlu() -> None:
    d9 = degerlendir("TQV-9")
    d10 = degerlendir("TQV-10")
    ok = (
        all(x.sonuc == TD.SONUC_ABOVE and x.karar_yolu == TD.KARAR_YOLU_TEK_YONLU
            for x in d9)
        and all(x.sonuc == TD.SONUC_INCOMPLETE for x in d10)
        and all(x.sonuc != TD.SONUC_STRONG for x in d10)
    )
    kaydet("C::TEK_YONLU",
           "kopru yok: yalniz ABOVE_CEILING kararlastirilabilir, STRONG ASLA",
           f"TQV-9={ {x.sonuc for x in d9} } TQV-10={ {x.sonuc for x in d10} }", ok)


def c_katman_ayrimi() -> None:
    """EXW (L0) teklifi, EXW->FOB koprusu olmadan CIF ile KARSILASTIRILAMAZ."""
    ds = degerlendir("TQV-11")
    ok = all(d.sonuc == TD.SONUC_INCOMPLETE for d in ds) and all(
        d.teklif_katmani == "L0" for d in ds)
    kaydet("C::KATMAN_L0_L1", "EXW teklifi kopru olmadan INCOMPLETE",
           f"katman={ {d.teklif_katmani for d in ds} } sonuc={ {d.sonuc for d in ds} }", ok)


# ===========================================================================
# D) RET YASAGI
# ===========================================================================

def d_ret_yasagi() -> None:
    hatalar: list[str] = []
    for yasak in ("REJECTED", "KILL", "NOT_VIABLE", "VIABLE", "APPROVED", "RED"):
        try:
            TD._sonuc_dogrula(yasak)
            hatalar.append(f"{yasak} GECTI")
        except TD.YasakliSonuc:
            pass
    try:
        TD.retmek("herhangi bir teklif")
        hatalar.append("retmek() GECTI")
    except TD.YasakliSonuc:
        pass
    try:
        TD.Degerlendirme(supplier="X", tier_code="V1", fx_ekseni="FX_0",
                         sonuc="REJECTED")
        hatalar.append("Degerlendirme(REJECTED) GECTI")
    except TD.YasakliSonuc:
        pass
    ok = not hatalar and len(TD.SONUC_DEGERLERI) == 4
    kaydet("D::RET_YASAGI", "REJECTED/KILL/VIABLE uretilemez; 4 sonuc degeri",
           f"ihlal={hatalar or 'YOK'} n={len(TD.SONUC_DEGERLERI)}", ok)


def d_above_ceiling_ret_degil() -> None:
    """ABOVE_CEILING satirinda RET olmadigini soyleyen bayrak BULUNMALI."""
    ds = [d for d in degerlendir("TQV-7B") if d.sonuc == TD.SONUC_ABOVE
          and d.karar_yolu == TD.KARAR_YOLU_TAM]
    ok = bool(ds) and all(
        any("RET DEGILDIR" in b for b in d.bayraklar) for d in ds)
    kaydet("D::ABOVE_RET_DEGIL", "ABOVE_CEILING satirinda 'RET DEGILDIR' bayragi",
           f"{len(ds)} satir, bayrak={'VAR' if ok else 'YOK'}", ok)


# ===========================================================================
# E) INTERNAL_ONLY
# ===========================================================================

def e_dosya_adi_kilidi() -> None:
    hatalar: list[str] = []
    try:
        TD.internal_rapor_yaz(TD.OUTPUTS / "gizli-olmayan.md", "x")
        hatalar.append("on eksiz ad GECTI")
    except TD.IcerideKalmaliHatasi:
        pass
    try:
        TD.internal_rapor_yaz(
            Path(TD.MODEL_KOK).parent / "50-sourcing" / "INTERNAL_ONLY-x.md", "x")
        hatalar.append("50-sourcing/ GECTI")
    except TD.IcerideKalmaliHatasi:
        pass
    kaydet("E::DOSYA_ADI", "on ek zorunlu + yasak dizin reddedilir",
           f"ihlal={hatalar or 'YOK'}", not hatalar)


def e_sizinti_taramasi() -> None:
    hatalar: list[str] = []
    yasak_metinler = [
        "Tavanimiz 290,51 TRY/sise",
        "Bu teklif ABOVE_CEILING olarak degerlendirildi",
        "MAX_CIF hesabimiza gore",
        "FX_UP_20 ekseninde bakildiginda",
    ]
    for m in yasak_metinler:
        try:
            TD.disari_giden_metin_denetle(m)
            hatalar.append(f"SIZDI: {m[:30]}")
        except TD.IcerideKalmaliHatasi:
            pass
    # temiz metin GECMELI
    try:
        TD.disari_giden_metin_denetle("Lutfen teslim yerini belirtiniz.")
    except TD.IcerideKalmaliHatasi:
        hatalar.append("temiz metin REDDEDILDI")
    kaydet("E::SIZINTI", "4 sizintili metin reddedilir, temiz metin gecer",
           f"ihlal={hatalar or 'YOK'}", not hatalar)


def e_tedarikci_metni_temiz() -> None:
    ds = degerlendir("TQV-4")
    metin = TD.tedarikciye_giden_metin(teklif_of("TQV-4"), ds)
    ok = ("290" not in metin and "CEILING" not in metin.upper()
          and "INCOMPLETE" not in metin.upper())
    kaydet("E::TEDARIKCI_METNI", "tedarikciye giden metinde tavan/sonuc YOK",
           f"{len(metin)} karakter, temiz={ok}", ok)


def e_fixture_sizintisi() -> None:
    hatalar: list[str] = []
    try:
        guvenli_girdi_yukle(TEST_FIXTURE_DOSYASI)
        hatalar.append("fixture URETIM YOLUNDAN OKUNDU")
    except FixtureSizintisi:
        pass
    kaydet("E::TEST_FIXTURE", "TEST_FIXTURE dosyasi uretim girdisi olarak OKUNAMAZ",
           f"ihlal={hatalar or 'YOK'}", not hatalar)


def e_kademe_tekilligi() -> None:
    ham = dict(TEST_FIXTURE_VEKTORLER["TQV-1"]["teklif"])
    ham["kademeler"] = list(ham["kademeler"]) + list(ham["kademeler"])
    hatalar: list[str] = []
    try:
        TD.teklif_kur(ham)
        hatalar.append("cift kademe GECTI")
    except TD.KademeCiftKayit:
        pass
    kaydet("E::KADEME_TEKILLIGI", "ayni tier_code iki kez -> KademeCiftKayit",
           f"ihlal={hatalar or 'YOK'}", not hatalar)


def e_metadata_kalemi() -> None:
    """Teklif kalemi TUR 3A defterine BLOCKED_INPUT olarak girer (tutar TL degil)."""
    t = teklif_of("TQV-1")
    kalem = TD.teklif_kalemi(t, t.kademeler[0], SEMA)
    damga, eksik = kalem.damga()
    ok = damga == DAMGA_BLOCKED and "tutar_try" in eksik
    kaydet("E::METADATA_KALEMI",
           "teklif kalemi BLOCKED_INPUT (TL'ye cevrilerek saklanmaz)",
           f"damga={damga} eksik={eksik}", ok)


# ===========================================================================
# F) ENTEGRASYON — GERCEK CSV + GERCEK makro.yaml
# ===========================================================================

def f_tavan_csv() -> None:
    c = ENTEGRASYON_CAPALARI
    p = TD.tavan_bandi_oku("TGT_799", "CHAIN_RETAIL", "P")
    n = TD.tavan_bandi_oku("TGT_799", "CHAIN_RETAIL", "N")
    ok = (
        p.X_try == D(str(c["TGT_799_CHAIN_P_X"]))
        and p.Y_try == D(str(c["TGT_799_CHAIN_P_Y"]))
        and n.X_try == D(str(c["TGT_799_CHAIN_N_X"]))
        and n.Y_try == D(str(c["TGT_799_CHAIN_N_Y"]))
    )
    kaydet("F::TAVAN_CSV", "P: 200,9780/290,5134 · N: 200,9780/256,3354",
           f"P={p.X_try}/{p.Y_try} N={n.X_try}/{n.Y_try}", ok)


def f_v2_tavani_yok() -> None:
    """V2 = 10.000 sise TUR 3.25'te EKLENDI; CSV'de o hacim satiri YOK."""
    t10, not10 = TD.hacim_tavani_oku("TGT_799", "CHAIN_RETAIL", "P", 10000)
    t25, not25 = TD.hacim_tavani_oku("TGT_799", "CHAIN_RETAIL", "P", 25000)
    ok = t10 is None and "HACIM_KADEMESI_TAVANI_YOK" in not10 and t25 is not None
    kaydet("F::V2_TAVANI", "10.000 -> None (T-865, interpolasyon YOK); 25.000 -> deger",
           f"10k={t10}/{not10}  25k={t25}", ok)


def f_fx_dort_eksen() -> None:
    makro = guvenli_girdi_yukle(TD.MAKRO_DOSYASI)
    eksenler, eksik = TD.fx_eksenleri_oku(makro, BUGUN)
    hazir = [k for k in TD.FX_EKSEN_SIRASI if eksenler[k].hazir_mi()]
    fx0 = eksenler["FX_0"]
    ok = (
        len(hazir) == 4
        and fx0.status == "OBSERVED"
        and fx0.kur_tipi == "doviz_satis"
        and not any(e.startswith("CONFLICT") for e in eksik)
    )
    kaydet("F::FX_DORT_EKSEN",
           "4 eksen hazir, FX_0=OBSERVED, kur_tipi=doviz_satis, carpan tutarli",
           f"hazir={len(hazir)} fx0={fx0.status}/{fx0.kur_tipi} "
           f"eur={fx0.eur_try} usd={fx0.usd_try} eksik={len(eksik)}", ok)


def f_fx_carpan_tutarliligi() -> None:
    """Yazilan eksen degerleri, eksen ADININ tanimladigi carpanla uyusmali."""
    makro = guvenli_girdi_yukle(TD.MAKRO_DOSYASI)
    eksenler, _ = TD.fx_eksenleri_oku(makro, BUGUN)
    taban = eksenler["FX_0"].eur_try
    sapmalar = []
    for kod in TD.FX_EKSEN_SIRASI:
        bek = taban * TD.FX_EKSEN_CARPANLARI[kod]
        var = eksenler[kod].eur_try
        if var is None or abs(var - bek) > D("0.001"):
            sapmalar.append(f"{kod}: {var} != {bek}")
    kaydet("F::FX_CARPAN", "yazilan eksen degerleri carpan tanimiyla uyusuyor",
           f"sapma={sapmalar or 'YOK'}", not sapmalar)


def f_max_fob_ust_siniri() -> None:
    """fx geldi -> MAX_FOB/MAX_EXW UST SINIRI artik hesaplanabilir."""
    makro = guvenli_girdi_yukle(TD.MAKRO_DOSYASI)
    eksenler, _ = TD.fx_eksenleri_oku(makro, BUGUN)
    band = TD.tavan_bandi_oku("TGT_799", "CHAIN_RETAIL", "P")
    satirlar = TD.max_alim_tavani(band, eksenler)
    eur = {r["fx_ekseni"]: r["MAX_FOB_UST_SINIR_Y"]
           for r in satirlar if r["para_birimi"] == "EUR"}
    hepsi_var = all(v is not None for v in eur.values())
    # TL zayifladikca EUR cinsinden tavan DUSMELI (monotonluk)
    monoton = (
        hepsi_var
        and eur["FX_DOWN_10"] > eur["FX_0"] > eur["FX_UP_10"] > eur["FX_UP_20"]
    )
    kaydet("F::MAX_FOB_UST_SINIR",
           "4 eksende de hesaplanir ve fx artarken MONOTON DUSER",
           f"hepsi_var={hepsi_var} monoton={monoton} FX_0={eur['FX_0']:.4f} EUR",
           hepsi_var and monoton)


def f_sema_kurallari_okundu() -> None:
    """Kurallar SEMADAN gelir: semadan silinen kural CALISMAZ."""
    kurallar = SEMA.get("dogrulama_kurallari") or []
    kimlikler = {k["kural_id"] for k in kurallar}
    bekleniyor = {"QV-1", "QV-1B", "QV-1C", "QV-1D", "QV-2", "QV-3", "QV-4", "QV-5", "QV-6"}
    # kural silinirse ihlal de kaybolmali (davranissal kanit)
    kirpik = dict(SEMA)
    kirpik["dogrulama_kurallari"] = [k for k in kurallar if k["kural_id"] != "QV-1"]
    t = teklif_of("TQV-2")
    with_qv1, _, _ = TD.sinif_belirle(t, t.kademeler[0], SEMA, BUGUN)
    without_qv1, _, _ = TD.sinif_belirle(t, t.kademeler[0], kirpik, BUGUN)
    ok = (bekleniyor <= kimlikler and with_qv1 == TD.SINIF_B2B
          and without_qv1 == TD.SINIF_FIRM)
    kaydet("F::SEMA_KURALLARI",
           "9 kural semada; QV-1 silinince davranis DEGISIR (kural=veri)",
           f"kurallar={len(kimlikler)} QV1_ile={with_qv1} QV1_siz={without_qv1}", ok)


def f_epistemik_asimetri() -> None:
    ds = degerlendir("TQV-7A")
    ok = all("ASIMETRIK" in d.epistemik_not and "MODEL_DERIVED" in d.epistemik_not
             for d in ds)
    kaydet("F::EPISTEMIK_ASIMETRI",
           "her satir teklif(gozlem) vs tavan(MODEL_DERIVED) ayrimini tasir",
           f"{len(ds)} satirin hepsinde={'EVET' if ok else 'HAYIR'}", ok)


# ===========================================================================
# ANA
# ===========================================================================

def main() -> int:
    for f in (
        a_siniflandirma,
        b_fx_eksenleri, b_tek_teklif_iki_sonuc, b_band_fx_araligindan_genis,
        c_tek_yonlu, c_katman_ayrimi,
        d_ret_yasagi, d_above_ceiling_ret_degil,
        e_dosya_adi_kilidi, e_sizinti_taramasi, e_tedarikci_metni_temiz,
        e_fixture_sizintisi, e_kademe_tekilligi, e_metadata_kalemi,
        f_tavan_csv, f_v2_tavani_yok, f_fx_dort_eksen, f_fx_carpan_tutarliligi,
        f_max_fob_ust_siniri, f_sema_kurallari_okundu, f_epistemik_asimetri,
    ):
        try:
            f()
        except Exception as exc:
            kaydet(f.__name__, "istisna YOK",
                   f"ISTISNA: {type(exc).__name__}: {exc}", False)

    gecen = sum(1 for *_r, ok in SONUCLAR if ok)
    print("=" * 130)
    print("TUR 3.25 §12/§13 — QUOTE INGESTION + EVALUATION TESTLERI")
    print("FIXTURE: inputs/TEST_FIXTURE-teklif-vektorleri.yaml  (SENTETIK — URETIM GIRDISI DEGIL)")
    print("SEMA   : inputs/quote-ingestion-schema.yaml (dogrulama_kurallari VERI olarak calisir)")
    print("=" * 130)
    print(f"{'TEST':<24}{'BEKLENEN':<58}{'GERCEKLESEN':<62}{'GECTI'}")
    print("-" * 130)
    for kod, b, g, ok in SONUCLAR:
        print(f"{kod:<24}{b[:56]:<58}{g[:60]:<62}{'EVET' if ok else 'HAYIR'}")
    print("-" * 130)
    print(f"SONUC: {gecen}/{len(SONUCLAR)} gecti")
    print("=" * 130)
    return 0 if gecen == len(SONUCLAR) else 1


if __name__ == "__main__":
    sys.exit(main())
