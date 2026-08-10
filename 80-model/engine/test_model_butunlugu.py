"""
test_model_butunlugu.py — TUR 3A MODEL BÜTÜNLÜK TESTLERİ

===========================================================================
 KAPSAM
===========================================================================
  A) ANA ROUND-TRIP     : target shelf -> ters model -> MAX_CIF -> İLERİ
                          YENİDEN KURULUM -> aynı shelf price (tolerans içinde)
  B) `R8-K` KANAL       : `T-619`'un DOĞRU çözümü + `T-942`'nin BİREBİR
                          spesifikasyonunun TERSTEN çalıştığının KALICI kanıtı
  C) 16 BİRİM VEKTÖR    : `TVK-1`..`TVK-P6` (`kanal-bacagi-hata-listesi.md`)
  D) INVARIANT'LAR      : ZERO_PARITY (K3) · LEDGER_UNIQUENESS (K6) ·
                          SCALE_MONOTONICITY (K7) · KARMA_UNKNOWN (K9c)
  E) METADATA MİMARİSİ  : BLOCKED_INPUT / EXCLUDED_WITH_REASON damgaları

===========================================================================
 ⛔ TEST_FIXTURE DİSİPLİNİ
===========================================================================
  - Sentetik değerler YALNIZCA `inputs/TEST_FIXTURE-kanal-test-vektorleri.yaml`
    dosyasından, `TEST_FIXTURE_*` ön ekli değişkenlere okunur.
  - `kalem_defteri.guvenli_girdi_yukle()` bu dosyayı REDDEDER (üretim yolu
    kapalıdır); burada BİLEREK `yaml.safe_load` ile ve TEK BİR yerde okunur.
  - `status: TEST_FIXTURE` taşıyan bir değer üretim defterine giremez
    (`FixtureSizintisi`).

Çalıştırma:  python3 80-model/engine/test_model_butunlugu.py
"""

from __future__ import annotations

import sys
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml  # noqa: E402

import kanal_bacagi as KB  # noqa: E402
from kalem_defteri import (  # noqa: E402
    DAMGA_BLOCKED,
    DAMGA_EXCLUDED,
    DAMGA_OK,
    DefterCiftKayit,
    FixtureSizintisi,
    KalemDefteri,
    MaliyetKalemi,
    blocked_envanterinden_kalemler,
    guvenli_girdi_yukle,
    zero_parity,
)
from ters_model import ileri_l4_econ, r7_adim_sirasini_oku, r7_coz  # noqa: E402

INPUTS = Path(__file__).resolve().parent.parent / "inputs"
TEST_FIXTURE_DOSYASI = INPUTS / "TEST_FIXTURE-kanal-test-vektorleri.yaml"

D = Decimal
TOL = D("0.0001")
TOL_TL = D("0.01")

SONUCLAR: list[tuple[str, str, str, bool]] = []


def kaydet(kod: str, beklenen: str, gerceklesen: str, ok: bool) -> None:
    SONUCLAR.append((kod, beklenen, gerceklesen, ok))


# ---------------------------------------------------------------------------
# FIXTURE YÜKLEME — TEK NOKTA, AÇIK AD
# ---------------------------------------------------------------------------

def TEST_FIXTURE_yukle() -> dict:
    """⛔ SENTETİK. Üretim kodu bu fonksiyonu ÇAĞIRAMAZ."""
    with TEST_FIXTURE_DOSYASI.open("r", encoding="utf-8") as f:
        veri = yaml.safe_load(f)
    assert veri.get("TEST_FIXTURE") is True, "Fixture dosyasi TEST_FIXTURE: true tasimali"
    assert veri.get("uretim_girdisi_mi") is False
    return veri


TEST_FIXTURE = TEST_FIXTURE_yukle()
TEST_FIXTURE_VEKTORLER = {v["kod"]: v for v in TEST_FIXTURE["vektorler"]}
TEST_FIXTURE_MAXCIF = TEST_FIXTURE["max_cif_donusumu"]

L5_TOPLAM = D(str(TEST_FIXTURE_MAXCIF["L5_kalemleri_toplami"]["value"]))
OTV = D(str(TEST_FIXTURE_MAXCIF["otv_per_sise"]["value"]))
GV = D(str(TEST_FIXTURE_MAXCIF["gv_orani"]["value"]))


def par(kod: str, **ek) -> KB.KanalParametreleri:
    """Vektör girdisinden `KanalParametreleri` kurar (beklenen değere BAKMAZ)."""
    v = TEST_FIXTURE_VEKTORLER[kod]
    g = v.get("girdi") or {}
    p = KB.KanalParametreleri(
        kanal_kodu=v.get("kanal", "CHAIN_RETAIL"),
        v=D(str(g.get("v", "0.20"))),
        m=D(str(g["m"])) if g.get("m") is not None else None,
        k=D(str(g["k"])) if g.get("k") is not None else None,
        d_var=D(str(g.get("d_var", 0))),
        mu=D(str(g.get("mu", 0))),
        mu_matrahi=g.get("mu_matrahi"),
        dagitim_modeli=g.get("dagitim_modeli", "MODEL_B"),
        d_kimde=g.get("d_kimde"),
    )
    # f: fixture'da `f_per_bottle` verilmişse, K7 gereği F_total = f*Q olarak
    # TÜREVE çevrilir — engine `f_per_bottle`'ı GİRDİ olarak KABUL ETMEZ.
    if g.get("f_per_bottle") is not None:
        p.Q_ithal = D("1")
        p.F_total = D(str(g["f_per_bottle"]))
        p.F_total_kdv_dahil_mi = "HARIC"
    if g.get("TEST_FIXTURE_F_total") is not None:
        p.F_total = D(str(g["TEST_FIXTURE_F_total"]))
        p.F_total_kdv_dahil_mi = g.get("F_total_kdv_dahil_mi")
        if g.get("Q_ithal"):
            p.Q_ithal = D(str(g["Q_ithal"]))
    if g.get("Q_ithal") is not None:
        p.Q_ithal = D(str(g["Q_ithal"]))
    if g.get("TEST_FIXTURE_r") is not None:
        p.r_iade = D(str(g["TEST_FIXTURE_r"]))
    if g.get("TEST_FIXTURE_m_dist") is not None:
        p.m_dist = D(str(g["TEST_FIXTURE_m_dist"]))
    if g.get("odeme_vadesi_gun") is not None:
        p.odeme_vadesi_gun = D(str(g["odeme_vadesi_gun"]))
    for kk, vv in ek.items():
        setattr(p, kk, vv)
    return p


def l8(kod: str) -> Decimal:
    return D(str(TEST_FIXTURE_VEKTORLER[kod]["girdi"]["L8_gross"]))


def bek(kod: str) -> dict:
    return TEST_FIXTURE_VEKTORLER[kod]["beklenen"]


def max_cif(l5_max: Decimal) -> Decimal:
    return (l5_max - L5_TOPLAM - OTV) / (D("1") + GV)


# ===========================================================================
# C) BİRİM VEKTÖRLER — POZİTİF
# ===========================================================================

def tvk_1() -> None:
    p, b = par("TVK-1"), bek("TVK-1")
    s = KB.kanal_ileri(l8("TVK-1"), p)
    ok = (
        abs(s.l8_net - D(str(b["L8_net"]))) < TOL
        and abs(s.l7_eff - D(str(b["L7_eff"]))) < TOL
        and abs(s.l6 - D(str(b["L6"]))) < TOL
        and abs(s.l5_max - D(str(b["L5_max"]))) < TOL
    )
    kaydet("TVK-1", f"L7_eff={b['L7_eff']} L6={b['L6']}",
           f"L7_eff={s.l7_eff:.4f} L6={s.l6:.4f} L5_max={s.l5_max:.4f}", ok)


def tvk_2() -> None:
    p, b = par("TVK-2"), bek("TVK-2")
    s = KB.kanal_ileri(l8("TVK-2"), p)
    okr, fark, _adim, _t = KB.r8k_roundtrip(l8("TVK-2"), s.l5_max, p)
    ok = okr and fark < D(str(b["tolerans"]))
    kaydet("TVK-2", f"L8_geri={b['L8_geri']} |d|<{b['tolerans']}",
           f"gecti={okr} fark={fark}", ok)


def tvk_3() -> None:
    p, b = par("TVK-3"), bek("TVK-3")
    s = KB.kanal_ileri(l8("TVK-3"), p)
    ok = (abs(s.l7_eff - D(str(b["L7_eff"]))) < TOL
          and abs(s.l6 - D(str(b["L6"]))) < TOL)
    # HoReCa geri inşa `*k` ile olmalı (T-619 kriter #3)
    okr, _f, _a, _t = KB.r8k_roundtrip(l8("TVK-3"), s.l5_max, p)
    ok = ok and okr
    kaydet("TVK-3", f"L7_eff=L6={b['L7_eff']} + R8-K(HoReCa,*k) gecer",
           f"L7_eff={s.l7_eff:.4f} L6={s.l6:.4f} R8K={okr}", ok)


def tvk_4() -> None:
    p = par("TVK-4")
    s = KB.kanal_ileri(l8("TVK-4"), p)
    ok = s.l6 == s.l7_eff
    kaydet("TVK-4", "L6 == L7_eff (TAM ESIT)", f"L6-L7_eff={s.l6 - s.l7_eff}", ok)


def tvk_p123() -> None:
    for kod in ("TVK-P1", "TVK-P2", "TVK-P3"):
        p, b = par(kod), bek(kod)
        s = KB.kanal_ileri(l8(kod), p)
        mc = max_cif(s.l5_max)
        ok = (abs(s.l5_max - D(str(b["L5_max"]))) < TOL
              and abs(mc - D(str(b["MAX_CIF"]))) < D("0.001"))
        # her matrah icin R8-K de kapanmali (mu != 0 kolu)
        okr, _f, _a, _t = KB.r8k_roundtrip(l8(kod), s.l5_max, p)
        ok = ok and okr
        kaydet(kod, f"L5_max={b['L5_max']} MAX_CIF={b['MAX_CIF']}",
               f"L5_max={s.l5_max:.4f} MAX_CIF={mc:.4f} R8K={okr}", ok)
    # UCU DE FARKLI OLMALI
    l5ler = []
    for kod in ("TVK-P1", "TVK-P2", "TVK-P3"):
        l5ler.append(KB.kanal_ileri(l8(kod), par(kod)).l5_max)
    ok = len({str(x) for x in l5ler}) == 3
    kaydet("TVK-P1/2/3-AYRIM", "uc matrah UC FARKLI sonuc",
           f"{[f'{x:.4f}' for x in l5ler]}", ok)


def tvk_p4() -> None:
    """SCALE_MONOTONICITY (K7) — f TÜREVDİR, f*Q SABİTTİR."""
    b = bek("TVK-P4")
    F = D(str(TEST_FIXTURE_VEKTORLER["TVK-P4"]["girdi"]["TEST_FIXTURE_F_total"]))
    qs = [D(str(q)) for q in TEST_FIXTURE_VEKTORLER["TVK-P4"]["girdi"]["Q_listesi"]]
    fler = []
    for q in qs:
        p = par("TVK-P4")
        p.Q_ithal, p.F_total, p.F_total_kdv_dahil_mi = q, F, "HARIC"
        s = KB.kanal_ileri(l8("TVK-P4"), p)
        fler.append(s.f_per_bottle)
    sabit = all(f * q == F for f, q in zip(fler, qs))
    monoton = fler[0] > fler[-1]        # hacim buyudukce sise basi f DUSER
    ok = (sabit and monoton
          and abs(fler[0] - D(str(b["f_at_5000"]))) < TOL
          and abs(fler[-1] - D(str(b["f_at_100000"]))) < TOL)
    kaydet("TVK-P4", f"f@5k={b['f_at_5000']} f@100k={b['f_at_100000']} f*Q SABIT",
           f"f={[f'{x:.2f}' for x in fler]} f*Q_sabit={sabit} monoton={monoton}", ok)


def tvk_p5() -> None:
    """K11 — Q_ithal != Q_satilan; sabitler Q_ithal'e bölünür."""
    p, b = par("TVK-P5"), bek("TVK-P5")
    s = KB.kanal_ileri(l8("TVK-P5"), p)
    ok = (s.q_satilan == D(str(b["Q_satilan"]))
          and p.Q_ithal == D(str(b["sabit_bolen"]))
          and s.iade_kaybi > 0
          and "IADE_GERI_KAZANIM_UST_SINIR" in s.bayraklar)
    # r=0 halinde FIRE_SIFIR_VARSAYILDI bayragi basilmali
    p0 = par("TVK-P5")
    p0.r_iade = None
    s0 = KB.kanal_ileri(l8("TVK-P5"), p0)
    ok = ok and "FIRE_SIFIR_VARSAYILDI" in s0.bayraklar
    kaydet("TVK-P5", f"Q_satilan={b['Q_satilan']} + FIRE_SIFIR_VARSAYILDI(r=None)",
           f"Q_satilan={s.q_satilan} iade_kaybi={s.iade_kaybi:.4f} "
           f"bayrak_r0={'FIRE_SIFIR_VARSAYILDI' in s0.bayraklar}", ok)


def tvk_p6() -> None:
    """K12 — alacak matrahı L6_gross; finansman yoksa uyarı."""
    p, b = par("TVK-P6"), bek("TVK-P6")
    s = KB.kanal_ileri(l8("TVK-P6"), p)
    ok = (abs(s.l6_gross - D(str(b["L6_gross"]))) < TOL
          and s.l6_gross == s.l6 * (D("1") + p.v)
          and b["bayrak"] in s.bayraklar)
    kaydet("TVK-P6", f"L6_gross={b['L6_gross']} + {b['bayrak']}",
           f"L6_gross={s.l6_gross:.4f} L6={s.l6:.4f} bayraklar={s.bayraklar}", ok)


# ===========================================================================
# C) BİRİM VEKTÖRLER — NEGATİF
# ===========================================================================

def tvk_n1() -> None:
    """naif R5 (`L5_max = L6`) -> DOĞRU `R8-K` REDDETMELİ."""
    p, b = par("TVK-N1"), bek("TVK-N1")
    s = KB.kanal_ileri(l8("TVK-N1"), p)
    naif_l5 = s.l6                      # K1 hatasi: L6'yi net hasilat sanmak
    okr, fark, _a, _t = KB.r8k_roundtrip(l8("TVK-N1"), naif_l5, p)
    l8_geri, _a2, _e = KB.kanal_geri_insa(naif_l5, p)
    ok = (okr is False
          and abs(l8_geri - D(str(b["L8_geri"]))) < TOL_TL
          and abs(fark - D(str(b["sapma"]))) < TOL_TL)
    kaydet("TVK-N1", f"REDDEDILMELI; L8_geri={b['L8_geri']} sapma={b['sapma']}",
           f"reddedildi={not okr} L8_geri={l8_geri:.4f} sapma={fark:.4f}", ok)


def tvk_n1b() -> None:
    """
    ⛔⛔ `T-619` — `T-942`'nin BİREBİR spesifikasyonu TERSTEN ÇALIŞIR.
    Bu vektör KALICIDIR: aynı spesifikasyon bir daha yazılırsa test KIRILIR.
    """
    p, b = par("TVK-N1b"), bek("TVK-N1b")
    hedef = l8("TVK-N1b")
    s = KB.kanal_ileri(hedef, p)
    dogru_l5 = s.l5_max                 # = L7_eff  (R5 duzeltmesi)
    naif_l5 = s.l6                      # = L6      (K1 hatasi)

    t942_dogru, t942_l8_dogru = KB.R8K_T942_BIREBIR_HATALI_ASLA_URETIMDE_KULLANMA(
        hedef, dogru_l5, p)
    t942_naif, _t942_l8_naif = KB.R8K_T942_BIREBIR_HATALI_ASLA_URETIMDE_KULLANMA(
        hedef, naif_l5, p)
    dogru_ok, _f1, _a1, _x1 = KB.r8k_roundtrip(hedef, dogru_l5, p)
    naif_ok, _f2, _a2, _x2 = KB.r8k_roundtrip(hedef, naif_l5, p)

    ok = (
        t942_dogru is bool(b["T942_dogru_formulu_kabul_eder_mi"])          # False
        and t942_naif is bool(b["T942_naif_formulu_kabul_eder_mi"])        # True
        and dogru_ok is bool(b["dogru_R8K_dogru_formulu_kabul_eder_mi"])   # True
        and naif_ok is bool(b["dogru_R8K_naif_formulu_kabul_eder_mi"])     # False
        and abs(t942_l8_dogru - D(str(b["T942_dogru_formulde_urettigi_L8"]))) < TOL_TL
    )
    kaydet(
        "TVK-N1b",
        "T-942: dogru=RED / naif=KABUL  (TERSTEN)  ;  DOGRU R8-K: dogru=KABUL / naif=RED",
        f"T942(dogru)={t942_dogru} L8={t942_l8_dogru:.2f} ; T942(naif)={t942_naif} ; "
        f"R8K(dogru)={dogru_ok} ; R8K(naif)={naif_ok}",
        ok,
    )


def tvk_n2() -> None:
    """margin<->markup karışıklığı -> `R8-K` REDDETMELİ."""
    p, b = par("TVK-N2"), bek("TVK-N2")
    hedef = l8("TVK-N2")
    l8_net = hedef / (D("1") + p.v)
    l7_yanlis = l8_net / (D("1") + p.m)          # K2 hatasi
    okr, fark, _a, _t = KB.r8k_roundtrip(hedef, l7_yanlis, p)
    l8_geri, _a2, _e = KB.kanal_geri_insa(l7_yanlis, p)
    ok = (okr is False
          and abs(l8_geri - D(str(b["L8_geri"]))) < TOL_TL
          and abs(fark - D(str(b["sapma"]))) < TOL_TL)
    kaydet("TVK-N2", f"REDDEDILMELI; L8_geri={b['L8_geri']} sapma={b['sapma']}",
           f"reddedildi={not okr} L8_geri={l8_geri:.4f} sapma={fark:.4f}", ok)


def tvk_n3() -> None:
    """K10 — mutlak tutarlı kalemde `kdv_dahil_mi` boşsa UNKNOWN."""
    p, b = par("TVK-N3"), bek("TVK-N3")
    s = KB.kanal_ileri(l8("TVK-N3"), p)
    ok = (s.status == b["status"]
          and any("kdv_dahil_mi" in x for x in s.bloke_girdiler)
          and s.l5_max is None)
    # ayrica MaliyetKalemi seviyesinde de yakalanmali
    k = MaliyetKalemi("f_test", payer="ithalatci", receiver="perakendeci", layer="L6->L7",
                      currency="TRY", fixed_or_variable="FIXED",
                      per_bottle_or_total="PER_BOTTLE", tax_treatment="hizmet faturasi",
                      evidence_id="EV-2026-08-10-610", status="ASSUMPTION",
                      tutar_try=D("60"), kdv_dahil_mi=None)
    damga, eksik = k.damga()
    ok = ok and damga == DAMGA_BLOCKED and "kdv_dahil_mi" in eksik
    kaydet("TVK-N3", "engine UNKNOWN + BLOCKED_INPUT(kdv_dahil_mi)",
           f"status={s.status} kalem_damgasi={damga} eksik={eksik}", ok)


def tvk_n4() -> None:
    """K5 — `mu != 0` ve matrah `null` -> UNKNOWN (varsayılana DÜŞMEZ)."""
    p, b = par("TVK-N4"), bek("TVK-N4")
    s = KB.kanal_ileri(l8("TVK-N4"), p)
    ok = (s.status == b["status"]
          and any("importer_katki_matrahi" in x for x in s.bloke_girdiler)
          and s.l5_max is None)
    # mu = 0 iken matrah null OLSA BILE calismali (uc matrah aynidir)
    p0 = par("TVK-N4")
    p0.mu = D("0")
    s0 = KB.kanal_ileri(l8("TVK-N4"), p0)
    ok = ok and s0.l5_max is not None
    kaydet("TVK-N4", "mu!=0 & matrah null -> UNKNOWN ; mu=0 -> CALISIR",
           f"status(mu=0.20)={s.status} l5_max(mu=0)={s0.l5_max:.4f}", ok)


def tvk_n5() -> None:
    """K3 / ZERO_PARITY — kanallar karşılaştırılabilir mi."""
    a = KalemDefteri(kanal_kodu="CHAIN_RETAIL")
    b_ = KalemDefteri(kanal_kodu="INDEPENDENT_TEKEL")
    ortak = ["f_listeleme", "D_fix", "iade_orani"]
    for ad in ortak:
        a.ekle(MaliyetKalemi(f"CHAIN::{ad}", tutar_try=None, status="UNKNOWN"))
        b_.ekle(MaliyetKalemi(f"TEKEL::{ad}", tutar_try=None, status="UNKNOWN"))
    for ad in KB.kanala_ozgu_bloke_kalemler("INDEPENDENT_TEKEL"):
        b_.ekle(MaliyetKalemi(f"TEKEL::{ad.split(':')[0]}", tutar_try=None, status="UNKNOWN"))
    esit, mesaj = zero_parity(a, b_)
    ok = esit is False and "KANALLAR_KARSILASTIRILAMAZ" in mesaj
    kaydet("TVK-N5", "KANALLAR_KARSILASTIRILAMAZ bayragi",
           f"esit={esit} chain_sifir={a.sifir_sayisi()} tekel_sifir={b_.sifir_sayisi()}", ok)


def tvk_n6() -> None:
    """K6d — MODEL A'da `d_kimde` boşsa UNKNOWN."""
    p, b = par("TVK-N6"), bek("TVK-N6")
    s = KB.kanal_ileri(l8("TVK-N6"), p)
    ok = s.status == b["status"] and any("d_kimde" in x for x in s.bloke_girdiler)
    # A2 (d distributorde) + d_var>0 -> CIFT SAYIM yakalanmali
    p2 = par("TVK-N6")
    p2.d_kimde = "DISTRIBUTORDE"
    s2 = KB.kanal_ileri(l8("TVK-N6"), p2)
    ok = ok and s2.status == "UNKNOWN" and any("CIFT_SAYIM" in x for x in s2.bloke_girdiler)
    # A1 (d bizde) -> calisir
    p1 = par("TVK-N6")
    p1.d_kimde = "BIZDE"
    s1 = KB.kanal_ileri(l8("TVK-N6"), p1)
    ok = ok and s1.l5_max is not None
    kaydet("TVK-N6", "d_kimde bos -> UNKNOWN ; A2+d>0 -> CIFT_SAYIM ; A1 -> calisir",
           f"bos={s.status} A2={s2.status} A1_l5={s1.l5_max is not None}", ok)


def tvk_n7() -> None:
    """K9c — `kanal_karmasi` eksikse birleşik çıktı ÜRETİLMEZ."""
    kanal_yaml = guvenli_girdi_yukle(INPUTS / "kanal.yaml")
    gecerli, mesaj = KB.karma_gecerli_mi(kanal_yaml)
    ok = gecerli is False and "KARMA_UNKNOWN" in mesaj
    # pozitif kontrol: paylar dolarsa gecmeli
    sahte = {"kanal_karmasi": {
        "zincir_market_pay_pct": {"value": 50},
        "tekel_bayi_pay_pct": {"value": 30},
        "horeca_pay_pct": {"value": 20}}}
    g2, _m2 = KB.karma_gecerli_mi(sahte)
    ok = ok and g2 is True
    kaydet("TVK-N7", "KARMA_UNKNOWN + birlesik cikti YOK",
           f"gercek_yaml_gecerli={gecerli} pozitif_kontrol={g2}", ok)


# ===========================================================================
# A) ANA ROUND-TRIP — target shelf -> MAX_CIF -> İLERİ -> target shelf
# ===========================================================================

def ana_roundtrip() -> None:
    """
    ZİNCİRİN TAMAMI kapanıyor mu:
      L8 -> (kanal) -> L5_max -> (L5 kalemleri) -> L4_econ -> (R7) -> MAX_CIF
      MAX_CIF -> (ileri vergi) -> L4_econ -> (+L5) -> L5_max -> (R8-K) -> L8

    ⛔ `T-619`: geri inşa `L6`'dan GEÇMEZ. `L5_max`'in karşılığı `L7_eff`'tir.
    """
    vergi = guvenli_girdi_yukle(INPUTS / "vergi.yaml")
    r7_sira, _ = r7_adim_sirasini_oku(vergi)

    for kod in ("TVK-1", "TVK-P1", "TVK-P2", "TVK-P3", "TVK-3"):
        p = par(kod)
        hedef = l8(kod)
        s = KB.kanal_ileri(hedef, p)
        if s.l5_max is None:
            kaydet(f"ROUNDTRIP::{kod}", "L8 -> ... -> L8", "kanal cozulmedi", False)
            continue
        l4 = s.l5_max - L5_TOPLAM
        cif, bolundu = r7_coz(l4, OTV, D("0"), D("0"), GV, r7_sira)
        # --- İLERİ YENİDEN KURULUM (bagimsiz) ---
        l4_geri = ileri_l4_econ(cif, GV, D("0"), OTV, D("0"))
        l5_geri = l4_geri + L5_TOPLAM
        l8_geri, _adim, _hata = KB.kanal_geri_insa(l5_geri, p)
        fark = abs(l8_geri - hedef)
        ok = bolundu and fark < TOL_TL
        kaydet(f"ROUNDTRIP::{kod}", f"L8_geri = {hedef} (|d| < 0,01)",
               f"MAX_CIF={cif:.4f} L8_geri={l8_geri:.6f} fark={fark:.8f}", ok)


# ===========================================================================
# D/E) INVARIANT'LAR VE METADATA MİMARİSİ
# ===========================================================================

def inv_ledger_uniqueness() -> None:
    """K6 — aynı kalem iki kez düşülemez."""
    d = KalemDefteri(kanal_kodu="CHAIN_RETAIL")
    d.ekle(MaliyetKalemi("L5::tr_lojistik", tutar_try=D("3.99"), status="ESTIMATE"))
    yakalandi = False
    try:
        d.ekle(MaliyetKalemi("L5::tr_lojistik", tutar_try=D("3.99"), status="ESTIMATE"))
    except DefterCiftKayit:
        yakalandi = True
    kaydet("INV::LEDGER_UNIQUENESS", "ayni kalem_kimligi -> CIFT_SAYIM istisnasi",
           f"yakalandi={yakalandi}", yakalandi)


def inv_metadata_zorunlulugu() -> None:
    """GÖREV 1 — eksik alan SESSİZ GEÇMEZ."""
    tam = MaliyetKalemi(
        "L5::bandrol", payer="ithalatci", receiver="Hazine/TAPDK", layer="L5",
        currency="TRY", fixed_or_variable="VARIABLE", per_bottle_or_total="PER_BOTTLE",
        tax_treatment="KDV haric; ithalat vergi matrahina GIRMEZ",
        evidence_id="EV-X", status="FACT", tutar_try=D("2.36073"),
        kdv_dahil_mi="HARIC")
    eksikli = MaliyetKalemi("L5::antrepo_bekleme", currency="TRY", status="UNKNOWN")
    haric = MaliyetKalemi(
        "KANAL::markup_karsiligi_k", status="DERIVED",
        haric_gerekce="m ve k AYNI gercegin iki ifadesidir; ikisi birden "
                      "dusulurse CIFT SAYIMDIR (kanal.yaml markup_basis."
                      "modele_girme_kurali = ENGINE_OKUMAZ)")
    d1, _ = tam.damga()
    d2, e2 = eksikli.damga()
    d3, _ = haric.damga()
    ok = (d1 == DAMGA_OK and d2 == DAMGA_BLOCKED and d3 == DAMGA_EXCLUDED
          and eksikli.dusulecek_tutar() == 0 and len(e2) >= 7)
    kaydet("INV::METADATA", "OK / BLOCKED_INPUT / EXCLUDED_WITH_REASON",
           f"{d1} / {d2}(eksik={len(e2)}) / {d3}", ok)


def inv_fixture_sizintisi() -> None:
    """TEST_FIXTURE bir üretim girdisi olarak OKUNAMAZ."""
    a = False
    try:
        guvenli_girdi_yukle(TEST_FIXTURE_DOSYASI)
    except FixtureSizintisi:
        a = True
    b = False
    try:
        MaliyetKalemi("X", status="TEST_FIXTURE", tutar_try=D("1")).damga()
    except FixtureSizintisi:
        b = True
    kaydet("INV::TEST_FIXTURE", "dosya adi REDDEDILIR + status TEST_FIXTURE REDDEDILIR",
           f"dosya={a} status={b}", a and b)


def inv_blocked_envanteri() -> None:
    """`kanal.yaml`'daki 15 kalemlik envanterin 15'i de GÖRÜNÜR olmalı."""
    kanal_yaml = guvenli_girdi_yukle(INPUTS / "kanal.yaml")
    kalemler = blocked_envanterinden_kalemler(kanal_yaml)
    d = KalemDefteri(kanal_kodu="CHAIN_RETAIL")
    d.ekle_hepsi(kalemler)
    bloke = d.bloke_kalemler()
    ok = len(kalemler) == 15 and len(bloke) == 15 and d.toplam_dusulen() == 0
    kaydet("INV::BLOCKED_ENVANTERI", "15 kalem -> 15 BLOCKED_INPUT (0 SAYILMAZ)",
           f"kalem={len(kalemler)} blocked={len(bloke)} toplam_dusulen={d.toplam_dusulen()}", ok)


def inv_scale_monotonicity() -> None:
    """K7 — f_per_bottle GİRDİ olarak KABUL EDİLMEZ; yalnız F_total+Q."""
    p = KB.KanalParametreleri(kanal_kodu="CHAIN_RETAIL", v=D("0.20"), m=D("0.25"),
                              d_var=D("0.08"), F_total=None, Q_ithal=D("5000"))
    s = KB.kanal_ileri(D("799"), p)
    bloke_var = any("f_listeleme_bedeli" in x for x in s.bloke_girdiler)
    ok = bloke_var and s.f_per_bottle == 0 and s.status == "DRAFT_BLOCKED_INPUT"
    kaydet("INV::SCALE_MONOTONICITY", "F_total yok -> f BLOCKED_INPUT (sessiz 0 DEGIL)",
           f"blocked={bloke_var} status={s.status}", ok)


def inv_l6_kullanilmadi() -> None:
    """
    ⛔ `T-619` KİLİDİ — `R8-K` geri inşası `L6`'yı ASLA kullanmamalı.
    Kanıt: `d_var` ve `F_total` değiştirilse bile (yani `L6` değişse bile)
    `L5_max` -> `L8` dönüşümü `mu=m_dist=r=0` iken DEĞİŞMEZ.
    """
    hedef = D("799")
    sonuclar = []
    for d_var, f_tot in ((D("0"), None), (D("0.08"), None), (D("0.18"), D("6"))):
        p = KB.KanalParametreleri(kanal_kodu="CHAIN_RETAIL", v=D("0.20"), m=D("0.25"),
                                  d_var=d_var, F_total=f_tot, Q_ithal=D("1"),
                                  F_total_kdv_dahil_mi="HARIC")
        l8_geri, _a, _e = KB.kanal_geri_insa(D("499.375"), p)
        sonuclar.append(l8_geri)
    ok = len({str(x) for x in sonuclar}) == 1 and abs(sonuclar[0] - hedef) < TOL_TL
    kaydet("INV::L6_ZINCIRDE_YOK",
           "L5_max sabitken d/f degisse de L8_geri DEGISMEZ (=799)",
           f"{[f'{x:.4f}' for x in sonuclar]}", ok)


# ===========================================================================
# ANA
# ===========================================================================

def main() -> int:
    for f in (
        tvk_1, tvk_2, tvk_3, tvk_4, tvk_p123, tvk_p4, tvk_p5, tvk_p6,
        tvk_n1, tvk_n1b, tvk_n2, tvk_n3, tvk_n4, tvk_n5, tvk_n6, tvk_n7,
        ana_roundtrip,
        inv_ledger_uniqueness, inv_metadata_zorunlulugu, inv_fixture_sizintisi,
        inv_blocked_envanteri, inv_scale_monotonicity, inv_l6_kullanilmadi,
    ):
        try:
            f()
        except Exception as exc:  # test altyapisi hatasi da BIR HATADIR
            kaydet(f.__name__, "istisna YOK", f"ISTISNA: {type(exc).__name__}: {exc}", False)

    gecen = sum(1 for *_r, ok in SONUCLAR if ok)
    print("=" * 120)
    print("TUR 3A — MODEL BUTUNLUK TESTLERI  (round-trip + invariant + 16 birim vektor)")
    print("KAYNAK: 70-kanal/kanal-bacagi-hata-listesi.md · kanal-katman-matrah-haritasi.md · T-619")
    print("FIXTURE: inputs/TEST_FIXTURE-kanal-test-vektorleri.yaml  (SENTETIK — URETIM GIRDISI DEGIL)")
    print("=" * 120)
    print(f"{'TEST':<26}{'BEKLENEN':<62}{'GERCEKLESEN':<62}{'GECTI'}")
    print("-" * 120)
    for kod, b, g, ok in SONUCLAR:
        print(f"{kod:<26}{b[:60]:<62}{g[:60]:<62}{'EVET' if ok else 'HAYIR'}")
    print("-" * 120)
    print(f"SONUC: {gecen}/{len(SONUCLAR)} gecti")
    print("=" * 120)
    return 0 if gecen == len(SONUCLAR) else 1


if __name__ == "__main__":
    sys.exit(main())
