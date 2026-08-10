"""
calistir_tur25.py — TUR 2.5 REVERSE TARGET MODEL koşucusu

Üretir:
  80-model/outputs/country-buying-ceilings.csv
ve markdown çıktılarına giren özet tabloları stdout'a basar.

BAĞLAYICI:
  - Hiçbir oran/tutar burada hard-code EDİLMEZ; hepsi inputs/*.yaml'dan gelir.
  - ÖTV yalnızca AÇIK bayrakla (`UPPER_BOUND_LAMBDA_1`) hesaplanır ve çıktı
    `cif_try_max_UPPER_BOUND` adıyla raporlanır (O-3).
  - Kanal senaryoları LOW/BASE/HIGH KORELASYONLU koşulur (marj + geri akan
    bedeller + lojistik AYNI YÖNDE) — `marj-vs-markup.md` §3.2 uyarısı gereği.
"""

from __future__ import annotations

import csv
import sys
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml  # noqa: E402

from otv_zaman_serisi import (  # noqa: E402
    OTV_SENARYO_PROJEKSIYON,
    OTV_SENARYO_UPPER_BOUND_LAMBDA_1,
)
from ters_model import KanalGirdisi, L5Kalemi, ters_zincir  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INPUTS = ROOT / "inputs"
OUTPUTS = ROOT / "outputs"

D = Decimal


def yukle(ad: str) -> dict:
    with (INPUTS / ad).open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


VERGI = yukle("vergi.yaml")
SENARYOLAR = yukle("senaryolar.yaml")
KANAL = yukle("kanal.yaml")
RUHSAT = yukle("ruhsat.yaml")
TEDARIKCI = yukle("tedarikci.yaml")

# ---------------------------------------------------------------------------
# GİRDİLER — hepsi dosyadan
# ---------------------------------------------------------------------------

HEDEFLER = [
    (b["id"], D(str(b["kdv_dahil_try"])))
    for b in SENARYOLAR["hedef_raf_fiyati_merdiveni"]["basamaklar"]
]

DUY = KANAL["duyarlilik_senaryolari"]
M_ZINCIR = {s: D(str(DUY["m_retail_zincir_pct"][s.lower()])) / 100 for s in ("LOW", "BASE", "HIGH")}
M_TEKEL = {s: D(str(DUY["m_tekel_pct"][s.lower()])) / 100 for s in ("LOW", "BASE", "HIGH")}
K_HORECA = {s: D(str(DUY["k_horeca_carpan"][s.lower()])) for s in ("LOW", "BASE", "HIGH")}
D_GERI = {s: D(str(DUY["d_geri_akan_bedeller_pct"][s.lower()])) / 100 for s in ("LOW", "BASE", "HIGH")}

BANDROL = D(str(RUHSAT["bandrol_uis"]["bandrol_birim_bedeli"]["value"]))
BANDROL_EV = RUHSAT["bandrol_uis"]["bandrol_birim_bedeli"]["evidence_id"]
_TADAB_BLOK = RUHSAT["surekli_yukumlulukler"]["hizmet_bedeli_per_sise_750ml"]
TADAB = D(str(_TADAB_BLOK["value"]))
TADAB_EV = _TADAB_BLOK["evidence_id"]

# Ruhsat SABIT maliyeti — hacme bolunur (L5 kalemi).
_RUH = RUHSAT["toplam_ruhsat_sabit_maliyeti"]
RUHSAT_KUCUK = D(str(_RUH["kucuk_hacim_ilk_yil"]["value"]))
RUHSAT_BUYUK = D(str(_RUH["buyuk_hacim_ilk_yil"]["value"]))
RUHSAT_TEKRAR = D(str(_RUH["ikinci_yil_tekrarlayan"]["value"]))
RUHSAT_EV = _RUH["kucuk_hacim_ilk_yil"]["evidence_id"]
# esik: 20.000 litre/yil  ->  sise cinsinden
RUHSAT_ESIK_SISE = D("20000") / D(str(VERGI["urun_parametreleri"]["sise_hacmi_litre"]["value"]))


def ruhsat_per_sise(volume: int, ilk_yil: bool = True) -> Decimal:
    if not ilk_yil:
        return RUHSAT_TEKRAR / D(str(volume))
    taban = RUHSAT_KUCUK if D(str(volume)) <= RUHSAT_ESIK_SISE else RUHSAT_BUYUK
    return taban / D(str(volume))

# lojistik.yaml TRY bacağı serbest metinde olduğu için kaynak belge
# 40-lojistik/lojistik-senaryolari-tur25.md §4'tür (LCL, İspanya→İstanbul,
# TR-içi kalemler rota-bağımsızdır: ordino, müşavirlik, lab, X-ray, iç nakliye).
TR_LOJISTIK_LCL_TRY = {
    5000:   {"LOW": D("2.60"), "BASE": D("3.99"), "HIGH": D("4.99")},
    25000:  {"LOW": D("1.04"), "BASE": D("1.60"), "HIGH": D("2.57")},
    50000:  {"LOW": D("0.91"), "BASE": D("1.42"), "HIGH": D("2.07")},
    100000: {"LOW": D("0.84"), "BASE": D("1.32"), "HIGH": D("1.82")},
}
TR_LOJISTIK_EV = "EV-2026-08-10-329"   # türev kart; kaynak 10 LCL kartı

ULKELER = [
    ("ES", True), ("PT", True), ("IT", True), ("FR", True), ("CL", True),
    ("ZA", False), ("AU", False), ("US", False), ("MD", False), ("AR", False),
]

VOLUMES = [5000, 25000, 50000, 100000]
SENARYO_ADLARI = ["LOW", "BASE", "HIGH"]

CIF_GOZLEM_USD_PER_LT = TEDARIKCI["arastirma_bulgulari"]["ulke_gosterge_birim_degerleri"][
    "katman_L2_turkiye_cif_USD_per_litre_2025"]["degerler"]
CIF_GOZLEM_EV = TEDARIKCI["arastirma_bulgulari"]["ulke_gosterge_birim_degerleri"][
    "katman_L2_turkiye_cif_USD_per_litre_2025"]["evidence_id"]
ULKE_ADI_ESLEME = {
    "ES": "ispanya", "PT": "portekiz", "IT": "italya", "FR": "fransa",
    "CL": "sili", "ZA": "guney_afrika_TEMSILI_DEGIL", "AU": "avustralya_TEMSILI_DEGIL",
    "US": None, "MD": "moldova", "AR": "arjantin_TEMSILI_DEGIL",
}
SISE_LT = D(str(VERGI["urun_parametreleri"]["sise_hacmi_litre"]["value"]))


def l5_kalemleri(volume: int, senaryo: str) -> list[L5Kalemi]:
    """
    ⛔ TUR 3A — ZORUNLU METADATA (`kanal-katman-matrah-haritasi.md` §2).

    Dokuz alanın dokuzu DOLU olan kalem `OK` damgası alır ve DÜŞÜLÜR.
    Bir alanı bile eksik olan kalem `BLOCKED_INPUT` damgası alır ve
    **DÜŞÜLMEZ, 0 DA SAYILMAZ** — çıktıda ADIYLA görünür.

    Aşağıdaki metadata **UYDURULMAMIŞTIR**: `payer`/`receiver`/`layer`/
    `tax_treatment` alanları `ruhsat.yaml`, `vergi.yaml` ve
    `40-lojistik/lojistik-senaryolari-tur25.md`'de zaten yazılı olan
    yapısal bilgilerin AKTARIMIDIR. Tutarı `UNKNOWN` olan sekiz kalemin
    metadata'sı BİLEREK doldurulmamıştır — çünkü eksik olan şey tutardır
    ve kalem zaten `BLOCKED_INPUT`'tur.
    """
    tr = TR_LOJISTIK_LCL_TRY[volume][senaryo]
    return [
        L5Kalemi("bandrol", BANDROL, "TRY", "FACT", BANDROL_EV,
                 not_="KDV haric; vergi matrahina GIRMEZ (ters-model §4.2)",
                 payer="ithalatci", receiver="Hazine (bandrol bedeli)", layer="L5",
                 fixed_or_variable="VARIABLE", per_bottle_or_total="PER_BOTTLE",
                 tax_treatment="KDV HARIC liste fiyati; ITHALAT VERGI MATRAHINA GIRMEZ "
                               "(ruhsat.yaml bandrol_birim_bedeli.kdv_durumu)",
                 kdv_dahil_mi="HARIC"),
        L5Kalemi("tadab_hizmet_bedeli", TADAB, "TRY", "ESTIMATE", TADAB_EV,
                 not_="211,60 TL/1000 lt x 0,75 lt; aylik satis raporu hacmi uzerinden",
                 payer="ithalatci", receiver="TADAB", layer="L5",
                 fixed_or_variable="VARIABLE", per_bottle_or_total="PER_BOTTLE",
                 tax_treatment="surekli yukumluluk hizmet bedeli; ITHALAT VERGI "
                               "MATRAHINA GIRMEZ (satis sonrasi dogar)",
                 kdv_dahil_mi="HARIC"),
        L5Kalemi(f"ruhsat_sabit_ilk_yil_per_sise@{volume}", ruhsat_per_sise(volume),
                 "TRY", "ESTIMATE", RUHSAT_EV,
                 not_="dagitim yetki belgesi + toptan satis belgesi; ILK YIL; "
                      "haric_tutulan_kalemler UNKNOWN -> yon: YUKARI",
                 payer="ithalatci", receiver="TADAB (belge harclari)", layer="L5",
                 fixed_or_variable="FIXED", per_bottle_or_total="TOTAL",
                 tax_treatment="belge harci; ITHALAT VERGI MATRAHINA GIRMEZ",
                 kdv_dahil_mi="HARIC",
                 yon="ASAGI (haric tutulan kalemler UNKNOWN)"),
        L5Kalemi(f"TR_yurt_ici_lojistik_LCL_{senaryo}", tr, "TRY", "ESTIMATE", TR_LOJISTIK_EV,
                 not_="ordino+musavirlik+lab+X-ray+ic nakliye; rota bagimsiz. "
                      "⚠ TESLIM NOKTASI TANIMI YAZILI DEGIL -> B-13 / T-618 "
                      "(zincirin lojistik bedeliyle ORTUSME riski)",
                 payer="ithalatci", receiver="lojistik saglayicilar / musavir", layer="L5",
                 fixed_or_variable="VARIABLE", per_bottle_or_total="PER_BOTTLE",
                 tax_treatment="KDV'ye tabi hizmet; ithalat KDV'si indirilebilir "
                               "(kdv_perspektifleri A CONFIRMED)",
                 kdv_dahil_mi="HARIC",
                 ticket="T-618", yon="CIFT (teslim noktasi BLOCKED)"),

        # ---- TUTARI BİLİNMEYEN SEKİZ KALEM -> BLOCKED_INPUT ----
        # Bunlar TUR 2.5'te SESSİZCE 0 geçiyordu. Artık ADIYLA görünürler.
        L5Kalemi("varis_local_charges_USD", None, "USD", "UNKNOWN", None,
                 not_="THD/devanning/CFS/ardiye — fx null (T-912)",
                 ticket="T-912", yon="ASAGI"),
        L5Kalemi("mense_local_charges_EUR", None, "EUR", "UNKNOWN", None,
                 not_="yalniz Ispanya icin bilinir; fx null (T-912)",
                 ticket="T-912", yon="ASAGI"),
        L5Kalemi("musavirlik_cif_kademesi", None, "USD", "UNKNOWN", None,
                 not_="CIF 15.001-225.000 USD ustu %0,3 — CIF USD gerekir",
                 ticket="T-911", yon="ASAGI"),
        L5Kalemi("bandrolleme_operasyonu", None, "TRY", "UNKNOWN", None, not_="T-314",
                 ticket="T-314", yon="ASAGI"),
        L5Kalemi("antrepo_bekleme", None, "TRY", "UNKNOWN", None, not_="T-301 CRITICAL",
                 ticket="T-301", yon="ASAGI"),
        L5Kalemi("devreden_kdv_finansman_maliyeti", None, "TRY", "UNKNOWN", None,
                 not_="RC4 — KDV'nin KENDISI degil, kilitlendigi surenin finansmani",
                 ticket="T-912", yon="ASAGI"),
        L5Kalemi("fire_zayi_kdv_maliyeti", None, "TRY", "UNKNOWN", None,
                 not_="RC5 — KDVK md.30/c; fire orani UNKNOWN (T-314, K11)",
                 ticket="T-615", yon="ASAGI"),
        L5Kalemi("kanal_alacagi_vade_finansmani", None, "TRY", "UNKNOWN", None,
                 not_="K12 — MATRAH L6_gross (L6 DEGIL); makro.finansman_orani null. "
                      "60 gunde -27,55 TL/sise mertebesinde (kanal-bacagi-hata-listesi K12)",
                 ticket="T-614", yon="ASAGI"),
    ]


def kanal_girdisi(kanal_kodu: str, senaryo: str,
                  mu_matrahi: str | None = None) -> KanalGirdisi:
    if kanal_kodu == "CHAIN_RETAIL":
        return KanalGirdisi(kanal_kodu, senaryo, m_retail=M_ZINCIR[senaryo],
                            d=D_GERI[senaryo], f_per_bottle=D("0"),
                            mu_matrahi=mu_matrahi)
    if kanal_kodu == "INDEPENDENT_TEKEL":
        return KanalGirdisi(kanal_kodu, senaryo, m_retail=M_TEKEL[senaryo],
                            d=D("0"), f_per_bottle=D("0"), d_unknown_sifir_alindi=True,
                            mu_matrahi=mu_matrahi)
    return KanalGirdisi(kanal_kodu, senaryo, k_horeca=K_HORECA[senaryo],
                        d=D("0"), f_per_bottle=D("0"), mu_matrahi=mu_matrahi)


def kos(hedef: Decimal, country: str, kanal_kodu: str, senaryo: str,
        volume: int, belge_ok: bool, importer_katki: Decimal = D("0"),
        otv_senaryo: str = OTV_SENARYO_UPPER_BOUND_LAMBDA_1,
        lam: Decimal | None = None,
        mu_matrahi: str | None = None):
    """
    ⛔ TUR 3A / K5 / T-616: `mu_matrahi` VARSAYILANA DUSMEZ.
    `importer_katki != 0` iken `mu_matrahi` verilmezse engine `UNKNOWN` doner.
    Duyarlilik gridleri matrahi ACIKCA gecmek ZORUNDADIR.
    """
    return ters_zincir(
        VERGI,
        l8_kdv_dahil=hedef,
        kanal=kanal_girdisi(kanal_kodu, senaryo, mu_matrahi=mu_matrahi),
        country=country,
        l5_kalemleri=l5_kalemleri(volume, senaryo),
        tercihli_belge_ibraz_edildi=belge_ok,
        dogrudan_nakliyat_saglandi=belge_ok,
        odeme_sekli="pesin",
        importer_katki_orani=importer_katki,
        otv_senaryo=otv_senaryo,
        lambda_katsayisi=lam,
        # TUR 3A: `kanal-marj-uzmani`nin 15 kalemlik BLOCKED envanteri
        # (kanal.yaml -> blocked_envanteri) kalem defterine BAGLANIR.
        # 15'inin 15'i bugune kadar SESSIZCE 0 geciyordu; artik ADIYLA gorunur.
        kanal_yaml=KANAL,
    )


def q(x, n="0.01"):
    return "UNKNOWN" if x is None else str(Decimal(x).quantize(Decimal(n)))


# ---------------------------------------------------------------------------
# 1) ANA CSV
# ---------------------------------------------------------------------------

def csv_uret() -> tuple[int, int, int]:
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    yol = OUTPUTS / "country-buying-ceilings.csv"
    satirlar = 0
    r8_fail = 0
    r8k_fail = 0
    with yol.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "TARGET_SHELF_TRY_KDV_DAHIL", "TARGET_ID", "COUNTRY", "CHANNEL",
            "SCENARIO", "CUSTOMS_SCENARIO", "CUSTOMS_RATE_PCT", "CUSTOMS_RATE_SOURCE",
            "LOGISTICS_SCENARIO", "LOGISTICS_MODE", "VOLUME_BOTTLES",
            "MAX_CIF_TRY_UPPER_BOUND", "MAX_FOB_TRY", "MAX_EXW_TRY",
            "MAX_FOB_EUR_USD", "MAX_EXW_EUR_USD",
            "L4_ECON_MAX_TRY", "L4_CASH_MAX_TRY", "OTV_TRY_PER_BOTTLE",
            "KDV_ITHAL_CASH_TRY", "MAX_CIF_TRY_PER_LITRE",
            "IMPLIED_BREAKEVEN_USDTRY_VS_OBSERVED_CIF",
            "R8_ROUNDTRIP_OK", "R8K_ROUNDTRIP_OK", "BLOCKED_INPUT_COUNT",
            "STATUS", "LABEL", "CONFIDENCE", "MISSING_INPUTS",
        ])
        for tid, hedef in HEDEFLER:
            for country, kosullu in ULKELER:
                belge_senaryolari = [(True, "DOC_OK"), (False, "DOC_FAIL")] if kosullu \
                    else [(True, "NO_PREFERENCE")]
                for belge_ok, cs_ad in belge_senaryolari:
                    for kanal_kodu in ("CHAIN_RETAIL", "INDEPENDENT_TEKEL", "HORECA"):
                        for senaryo in SENARYO_ADLARI:
                            for volume in VOLUMES:
                                s = kos(hedef, country, kanal_kodu, senaryo,
                                        volume, belge_ok)
                                if s.r8_gecti_mi is False:
                                    r8_fail += 1
                                if s.r8k_gecti_mi is False:
                                    r8k_fail += 1
                                cif = s.cif_try_max_upper_bound
                                cif_lt = (cif / SISE_LT) if cif is not None else None
                                anahtar = ULKE_ADI_ESLEME.get(country)
                                gozlem = CIF_GOZLEM_USD_PER_LT.get(anahtar) if anahtar else None
                                implied = (cif_lt / D(str(gozlem))) if (cif_lt and gozlem) else None
                                w.writerow([
                                    str(hedef), tid, country, kanal_kodu, senaryo, cs_ad,
                                    q(s.gv_orani * 100 if s.gv_orani is not None else None),
                                    s.gv_orani_kaynagi or "UNKNOWN",
                                    senaryo, "LCL", volume,
                                    q(cif, "0.0001"),
                                    "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN",
                                    q(s.l4_econ_max, "0.0001"), q(s.l4_cash_max, "0.0001"),
                                    q(s.otv_try, "0.0001"), q(s.kdv_ithal_nakit, "0.0001"),
                                    q(cif_lt, "0.0001"),
                                    q(implied, "0.01") if implied else "UNKNOWN",
                                    "EVET" if s.r8_gecti_mi else "HAYIR",
                                    "EVET" if s.r8k_gecti_mi else "HAYIR",
                                    str(len(s.blocked_input)),
                                    s.status,
                                    "TARGET / MODEL_DERIVED / UPPER_BOUND — FACT DEGIL",
                                    "LOW",
                                    "fx(T-912); FOB/EXW; USD-EUR L5 kalemleri; f listeleme; "
                                    "d(tekel/horeca); fire; antrepo bekleme; distributor marji; "
                                    "OTV(2027) FUTURE_UNKNOWN",
                                ])
                                satirlar += 1
    return satirlar, r8_fail, r8k_fail


# ---------------------------------------------------------------------------
# 2) ÖZET TABLOLAR
# ---------------------------------------------------------------------------

def bolum(baslik: str) -> None:
    print()
    print("#" * 100)
    print("# " + baslik)
    print("#" * 100)


def tablo_katman_izi() -> None:
    bolum("A) KATMAN KATMAN İZ — TGT_799 · ES · CHAIN_RETAIL · BASE · 5.000 şişe · DOC_OK")
    s = kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, True)
    print(f"L8 (KDV dahil, hedef)        = {q(s.l8_kdv_dahil)}")
    print(f"L8_net (R1: /1+v)            = {q(s.l8_net,'0.0001')}   v={s.kdv_orani}")
    print(f"L7_eff (R2: x(1-m))          = {q(s.l7_eff,'0.0001')}   m={M_ZINCIR['BASE']}")
    print(f"L6 (R4: (L7+f)/(1-d))        = {q(s.l6,'0.0001')}   d={D_GERI['BASE']} f=0")
    print(f"L5_max (R5)                  = {q(s.l5_max,'0.0001')}   importer_katki=0")
    for k in s.l5_kalemleri:
        print(f"    - {k.ad:<34} {q(k.tutar_try,'0.0001'):>12} {k.para_birimi:<4} [{k.status}]")
    print(f"L4_econ_max (R6)             = {q(s.l4_econ_max,'0.0001')}")
    print(f"  - OTV (R7b, MAKTU)         = {q(s.otv_try,'0.0001')}")
    print(f"  - KKDF (R7c)               = {q(s.kkdf_try,'0.0001')}")
    print(f"  - X_pre (R7c)              = {q(s.x_pre_try,'0.0001')}")
    print(f"  / (1+g) (R7d)              g={s.gv_orani} kaynak={s.gv_orani_kaynagi}")
    print(f"CIF_TRY_max_UPPER_BOUND      = {q(s.cif_try_max_upper_bound,'0.0001')}")
    print(f"  turev GV                   = {q(s.gv_try,'0.0001')}")
    print(f"L3_pre_tax_landed (bilgi)    = {q(s.l3_pre_tax_landed_max,'0.0001')}")
    print(f"R8 round-trip fark           = {s.r8_roundtrip_fark}  -> {'GECTI' if s.r8_gecti_mi else 'KALDI'}")
    print(f"--- CASH VIEW (AYRI, TOPLANMAZ) ---")
    print(f"KDV_ithal (nakit)            = {q(s.kdv_ithal_nakit,'0.0001')}")
    print(f"l4_cash_max                  = {q(s.l4_cash_max,'0.0001')}")
    print(f"gumrukte nakden odenen       = {q(s.gumrukte_nakden_odenen,'0.0001')}")
    print(f"uygulanan adim sirasi        = {s.uygulanan_adim_sirasi}")
    print(f"evidence_ids                 = {sorted(set(s.kullanilan_evidence_ids))}")


def tablo_hedef_x_kanal() -> None:
    bolum("B) MAX_CIF_TRY (UPPER BOUND) — 5 HEDEF x 3 KANAL x 3 SENARYO · g=0,50 · 5.000 şişe")
    print(f"{'HEDEF':<8}{'KANAL':<20}{'LOW':>12}{'BASE':>12}{'HIGH':>12}")
    for tid, hedef in HEDEFLER:
        for kanal_kodu in ("CHAIN_RETAIL", "INDEPENDENT_TEKEL", "HORECA"):
            vals = []
            for sc in SENARYO_ADLARI:
                s = kos(hedef, "ES", kanal_kodu, sc, 5000, True)
                vals.append(q(s.cif_try_max_upper_bound))
            print(f"{str(hedef):<8}{kanal_kodu:<20}{vals[0]:>12}{vals[1]:>12}{vals[2]:>12}")

    bolum("B2) AYNI TABLO g=0,70 (DOC_FAIL / tercihsiz menşe)")
    print(f"{'HEDEF':<8}{'KANAL':<20}{'LOW':>12}{'BASE':>12}{'HIGH':>12}")
    for tid, hedef in HEDEFLER:
        for kanal_kodu in ("CHAIN_RETAIL", "INDEPENDENT_TEKEL", "HORECA"):
            vals = []
            for sc in SENARYO_ADLARI:
                s = kos(hedef, "ES", kanal_kodu, sc, 5000, False)
                vals.append(q(s.cif_try_max_upper_bound))
            print(f"{str(hedef):<8}{kanal_kodu:<20}{vals[0]:>12}{vals[1]:>12}{vals[2]:>12}")


def tablo_ulke() -> None:
    bolum("C) ÜLKE x HEDEF — MAX_CIF_TRY (CHAIN_RETAIL, BASE, 5.000 şişe)")
    print(f"{'ULKE':<6}{'g':<8}{'KAYNAK':<20}" + "".join(f"{str(h):>10}" for _, h in HEDEFLER))
    for country, kosullu in ULKELER:
        for belge_ok, ad in ([(True, "DOC_OK"), (False, "DOC_FAIL")] if kosullu
                             else [(True, "NO_PREF")]):
            hucreler = []
            g = None
            kaynak = ""
            for _, hedef in HEDEFLER:
                s = kos(hedef, country, "CHAIN_RETAIL", "BASE", 5000, belge_ok)
                g = s.gv_orani
                kaynak = s.gv_orani_kaynagi
                hucreler.append(q(s.cif_try_max_upper_bound))
            print(f"{country:<6}{str(g):<8}{(ad+'/'+str(kaynak)):<20}"
                  + "".join(f"{h:>10}" for h in hucreler))


def tablo_hacim() -> None:
    bolum("D) HACİM ETKİSİ — MAX_CIF_TRY (ES, CHAIN_RETAIL, BASE, DOC_OK)")
    print(f"{'HEDEF':<8}" + "".join(f"{str(v):>12}" for v in VOLUMES))
    for _, hedef in HEDEFLER:
        hucre = []
        for v in VOLUMES:
            s = kos(hedef, "ES", "CHAIN_RETAIL", "BASE", v, True)
            hucre.append(q(s.cif_try_max_upper_bound))
        print(f"{str(hedef):<8}" + "".join(f"{h:>12}" for h in hucre))
    print("\nTR-ici lojistik TRY/sise (LCL, BASE):",
          {v: str(TR_LOJISTIK_LCL_TRY[v]['BASE']) for v in VOLUMES})


def tablo_lambda() -> None:
    bolum("E) ÖTV DUYARLILIĞI (λ ekseni) — PROJEKSİYON (ASSUMPTION), FACT DEĞİL")
    noktalar = SENARYOLAR["duyarlilik_eksenleri"]
    otv_eksen = [e for e in noktalar if e["eksen"] == "OTV"][0]
    pts = otv_eksen["talep_edilen_senaryo_noktalari"]["noktalar"]
    print(f"kaynak: senaryolar.yaml -> duyarlilik_eksenleri[OTV]."
          f"talep_edilen_senaryo_noktalari (T-104, {otv_eksen['talep_edilen_senaryo_noktalari']['status']})")
    print(f"noktalar (% / 6 ay): {pts}")
    print(f"\n{'TARIH':<12}{'ADIM':<6}" + "".join(f"{'+'+str(p)+'%':>12}" for p in pts))
    for tarih, adimlar in (("2027-01-01", [0, 1]), ("2027-04-01", [1]), ("2027-07-01", [1, 2])):
        for adim in adimlar:
            hucre = []
            for p in pts:
                lam = (D("1") + D(str(p)) / 100) ** adim
                sen = (OTV_SENARYO_UPPER_BOUND_LAMBDA_1 if lam == 1
                       else OTV_SENARYO_PROJEKSIYON)
                s = kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, True,
                        otv_senaryo=sen, lam=lam)
                hucre.append(q(s.cif_try_max_upper_bound))
            print(f"{tarih:<12}{str(adim):<6}" + "".join(f"{h:>12}" for h in hucre))
    print("\n(hedef 799 TL, ES, CHAIN_RETAIL BASE, 5.000 sise, g=0,50)")
    print("ADIM = BASE_DATE ile hedef tarih arasindaki DOGRULANMAMIS revizyon sayisi")


def tablo_importer_marj() -> None:
    bolum("F) İTHALATÇI KATKI PAYI EKSENİ — INVESTOR_DECISION_REQUIRED")
    print("MAXIMUM STRUCTURAL BUY PRICE = katki 0 satiri. Digerleri PARAMETRIKTIR.")
    print("⛔ TUR 3A / K5 / T-616: mu'nun MATRAHI bir YATIRIMCI KARARIDIR ve")
    print("   kanal.yaml -> dagitim_modeli.importer_katki_matrahi = null'dir.")
    print("   Engine VARSAYILANA DUSMEZ: matrah verilmezse UNKNOWN doner.")
    print("   Asagidaki grid, UC MATRAHTAN BIRI (L6) ACIKCA SECILEREK kosulmustur.")
    yuzdeler = [D("0"), D("0.10"), D("0.20"), D("0.30"), D("0.40"), D("0.50")]
    for matrah in ("L6", "L7_EFF", "L5_MARKUP"):
        etiket = " <- bugunku engine varsayilani" if matrah == "L6" else ""
        print(f"\nMATRAH = {matrah}{etiket}")
        print(f"{'HEDEF':<8}" + "".join(f"{str(int(y*100))+'%':>12}" for y in yuzdeler))
        for _, hedef in HEDEFLER:
            hucre = []
            for y in yuzdeler:
                s = kos(hedef, "ES", "CHAIN_RETAIL", "BASE", 5000, True,
                        importer_katki=y, mu_matrahi=matrah)
                hucre.append(q(s.cif_try_max_upper_bound))
            print(f"{str(hedef):<8}" + "".join(f"{h:>12}" for h in hucre))
    print("\nUC MATRAHIN AYRILIGI mu=0'da SIFIRDIR ve mu ile BUYUR (T-944/T-616).")


def tablo_distributor() -> None:
    bolum("G) MODEL A — 3. TARAF DİSTRİBÜTÖR · DISTRIBUTOR_MARGIN_ASSUMPTION_REQUIRED")
    print("Distributor marji L6 ile L7 arasina girer: L6_importer = L6_modelB x (1 - m_dist).")
    print("kanal.yaml -> dagitim_modeli.dis_distributor.marj_pct = min/base/max NULL (UNKNOWN).")
    print("Asagidaki GRID BIR TAHMIN DEGILDIR; saf duyarlilik gridi.")
    print("⛔ TUR 3A / T-617 / C-611: bu grid A1 (d ve f BIZDE) senaryosudur.")
    print("   A2 (d ve f DISTRIBUTORDE) senaryosu KOSULMAMISTIR — d_kimde BLOCKED.")
    print("   Fark d*L6 = 43,42 TL/sise -> MAX_CIF'te 28,95 TL (g=0,50).")
    print("   mu ile m_dist OZDES DEGILDIR ve TOPLANMAZ (T-617 SPEC_DECISION).")
    grid = [D("0"), D("0.05"), D("0.10"), D("0.15"), D("0.20"), D("0.25"), D("0.30")]
    print(f"\n{'HEDEF':<8}" + "".join(f"{str(int(y*100))+'%':>11}" for y in grid))
    for _, hedef in HEDEFLER:
        hucre = []
        for y in grid:
            # matrah L6 ACIKCA gecilir: distributor marjinin matrahi
            # kanal.yaml -> dis_distributor.marj_matrahi = L6 (SPEC_DECISION).
            s = kos(hedef, "ES", "CHAIN_RETAIL", "BASE", 5000, True,
                    importer_katki=y, mu_matrahi="L6")
            hucre.append(q(s.cif_try_max_upper_bound))
        print(f"{str(hedef):<8}" + "".join(f"{h:>11}" for h in hucre))
    s0 = kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, True)
    print(f"\nKATSAYI: her +1 puan distributor marji -> MAX_CIF_TRY degisimi = "
          f"-L6/(100*(1+g)) = {q(-(s0.l6/(D('100')*(D('1')+s0.gv_orani))),'0.0001')} TL/sise "
          f"(hedef 799, g=0,50)")


def tablo_kendi_dagitim() -> None:
    bolum("H) MODEL B — KENDİ DAĞITIM · KANITLI TABAN + UNKNOWN'LAR")
    taban = D(str(KANAL["dagitim_modeli"]["kendi_dagitimimiz"]
                  ["personel_taban_maliyeti_aylik"]["value"]))
    ev = KANAL["dagitim_modeli"]["kendi_dagitimimiz"]["personel_taban_maliyeti_aylik"]["evidence_id"]
    alan = KANAL["dagitim_modeli"]["kendi_dagitimimiz"]["alan_sayisi"]
    print(f"personel taban maliyeti = {taban} TRY/ay/kisi  [{ev}]  (BEKLENEN UCRET DEGIL, TABAN)")
    print(f"alan sayimi: toplam={alan['toplam']} kanitli_dolu={alan['kanitli_dolu']} "
          f"unknown={alan['unknown']}")
    print(f"\nSADECE PERSONEL TABANI — TRY/sise:")
    print(f"{'KISI':<6}" + "".join(f"{str(v):>12}" for v in VOLUMES))
    for kisi in (1, 2, 3):
        hucre = [q(taban * 12 * kisi / D(str(v))) for v in VOLUMES]
        print(f"{str(kisi):<6}" + "".join(f"{h:>12}" for h in hucre))
    print("\nMAX_CIF_TRY etkisi (ES, 799, CHAIN_RETAIL BASE, g=0,50): -X/(1+g) = -X/1,50")
    print(f"{'KISI':<6}" + "".join(f"{str(v):>12}" for v in VOLUMES))
    for kisi in (1, 2, 3):
        hucre = [q(-(taban * 12 * kisi / D(str(v))) / D("1.5")) for v in VOLUMES]
        print(f"{str(kisi):<6}" + "".join(f"{h:>12}" for h in hucre))
    print("\nEKSIK (UNKNOWN, uydurulmadi): arac, yakit, depo kirasi, satis primi, "
          "yol/yemek, ceptelefonu, sigorta, tahsilat maliyeti, her depo icin ayri "
          "toptan satis belgesi (82.464 TL/yil), IT/siparis sistemi, iade lojistigi.")


def tablo_tornado() -> None:
    bolum("I) TORNADO — MAX_CIF_TRY (TGT_799, ES, CHAIN_RETAIL, 5.000 şişe)")
    base = kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, True)
    b = base.cif_try_max_upper_bound
    satir = []

    def ekle(ad, lo, hi, notu=""):
        satir.append((ad, lo, hi, (lo - b) if lo else None, (hi - b) if hi else None, notu))

    ekle("KANAL MARJI m (18/25/35%)",
         kos(D("799"), "ES", "CHAIN_RETAIL", "LOW", 5000, True).cif_try_max_upper_bound,
         kos(D("799"), "ES", "CHAIN_RETAIL", "HIGH", 5000, True).cif_try_max_upper_bound,
         "d ile KORELASYONLU (LOW=iyi, HIGH=kotu)")
    ekle("GUMRUK VERGISI (50% / 70%)",
         kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, False).cif_try_max_upper_bound,
         b, "DOC_FAIL / DOC_OK — tek yonlu risk")
    lam125 = kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, True,
                 otv_senaryo=OTV_SENARYO_PROJEKSIYON, lam=D("1.25")).cif_try_max_upper_bound
    lam1562 = kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, True,
                  otv_senaryo=OTV_SENARYO_PROJEKSIYON, lam=D("1.5625")).cif_try_max_upper_bound
    ekle("OTV lambda (1,00 / 1,25 / 1,5625)", lam1562, b, "lambda>=1 -> TEK YONLU asagi")
    ekle("HACIM 5.000 -> 100.000",
         b, kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 100000, True).cif_try_max_upper_bound,
         "TR-ici lojistik seyrelmesi")
    ekle("ITHALATCI KATKI 0 -> 30%",
         kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, True,
             importer_katki=D("0.30")).cif_try_max_upper_bound, b,
         "INVESTOR_DECISION_REQUIRED")
    ekle("HEDEF FIYAT 599 -> 999",
         kos(D("599"), "ES", "CHAIN_RETAIL", "BASE", 5000, True).cif_try_max_upper_bound,
         kos(D("999"), "ES", "CHAIN_RETAIL", "BASE", 5000, True).cif_try_max_upper_bound,
         "INVESTOR_TARGET_SCENARIO")
    print(f"BASE = {q(b)} TL/sise\n")
    print(f"{'EKSEN':<38}{'DUSUK':>12}{'YUKSEK':>12}{'DELTA-':>12}{'DELTA+':>12}  NOT")
    for ad, lo, hi, dl, dh, notu in sorted(
            satir, key=lambda r: -(abs(r[3] or 0) + abs(r[4] or 0))):
        print(f"{ad:<38}{q(lo):>12}{q(hi):>12}{q(dl):>12}{q(dh):>12}  {notu}")
    print(f"\nlambda=1,25 (1 adim +%25) -> {q(lam125)} | lambda=1,5625 (2 adim) -> {q(lam1562)}")


def tablo_vergi_yuku() -> None:
    bolum("J) VERGİ YÜKÜNÜN HEDEF FİYAT İÇİNDEKİ PAYI (ES, CHAIN_RETAIL BASE, 5.000, g=0,50)")
    print(f"{'HEDEF':<8}{'KDV':>10}{'OTV':>10}{'GV':>10}{'TOPLAM':>10}{'PAY%':>9}"
          f"{'OTV_PAY%':>10}{'MAX_CIF':>10}{'CIF_PAY%':>10}")
    for _, hedef in HEDEFLER:
        s = kos(hedef, "ES", "CHAIN_RETAIL", "BASE", 5000, True)
        kdv_perakende = hedef - hedef / (D("1") + s.kdv_orani)
        toplam = kdv_perakende + s.otv_try + s.gv_try
        print(f"{str(hedef):<8}{q(kdv_perakende):>10}{q(s.otv_try):>10}{q(s.gv_try):>10}"
              f"{q(toplam):>10}{q(toplam/hedef*100):>9}{q(s.otv_try/hedef*100):>10}"
              f"{q(s.cif_try_max_upper_bound):>10}{q(s.cif_try_max_upper_bound/hedef*100):>10}")
    print("\nNOT: KDV satiri PERAKENDE KDV'sidir (L8'in 1/6'si). Ithalat KDV'si EKONOMIK")
    print("     maliyet DEGILDIR (indirilebilir) ve bu tabloda YOKTUR — RC1/RC3.")


def tablo_rfq_tavan() -> None:
    bolum("K) RFQ TARGET CEILING — CIF TL/şişe (X = kötümser köşe, Y = BASE köşe)")
    print("X = SCENARIO HIGH + DOC_FAIL(kosullu menselerde) + 5.000 sise")
    print("Y = SCENARIO BASE + DOC_OK + 25.000 sise")
    print(f"\n{'ULKE':<6}{'HEDEF':<8}{'X (guclu aday <=)':>20}{'Y (inceleme <=)':>20}"
          f"{'X_USD/lt_@fx':>16}{'gozlem_CIF_USD/lt':>20}{'IMPLIED_USDTRY@Y':>18}")
    for country, kosullu in ULKELER:
        for _, hedef in [h for h in HEDEFLER if h[1] in (D("699"), D("799"), D("899"))]:
            sx = kos(hedef, country, "CHAIN_RETAIL", "HIGH", 5000, not kosullu and True or False)
            sy = kos(hedef, country, "CHAIN_RETAIL", "BASE", 25000, True)
            anahtar = ULKE_ADI_ESLEME.get(country)
            gozlem = CIF_GOZLEM_USD_PER_LT.get(anahtar) if anahtar else None
            y_lt = sy.cif_try_max_upper_bound / SISE_LT
            implied = (y_lt / D(str(gozlem))) if gozlem else None
            print(f"{country:<6}{str(hedef):<8}"
                  f"{q(sx.cif_try_max_upper_bound):>20}{q(sy.cif_try_max_upper_bound):>20}"
                  f"{'fx gerekli':>16}{str(gozlem) if gozlem else 'UNKNOWN':>20}"
                  f"{q(implied) if implied else 'UNKNOWN':>18}")


def tablo_yapisal_taban() -> None:
    bolum("L) YAPISAL TABAN — MAX_CIF = 0 OLAN HEDEF RAF FİYATI (5.000 şişe, ithalatçı katkı 0)")
    print("Bu fiyatin ALTINDA tedarikci BEDAVA verse bile model kapanmaz.")
    print("Formul ters cevrilmistir: CIF=0 -> L4_econ = OTV -> L5 -> L6 -> L7 -> L8.")
    v = D("0.2")
    print(f"\n{'KANAL':<20}{'SENARYO':<8}{'g=0,50':>12}{'g=0,70':>12}")
    for kanal_kodu in ("CHAIN_RETAIL", "INDEPENDENT_TEKEL", "HORECA"):
        for sc in SENARYO_ADLARI:
            hucre = []
            for belge_ok in (True, False):
                s = kos(D("799"), "ES", kanal_kodu, sc, 5000, belge_ok)
                # L5 toplam (TRY, düşülen) = L5_max - L4_econ_max
                l5_toplam = s.l5_max - s.l4_econ_max
                l5_min = s.otv_try + l5_toplam
                kg = kanal_girdisi(kanal_kodu, sc)
                # R5 duzeltmesi geregi: CIF=0 iken L5_max = L7_eff
                l7 = l5_min
                if kanal_kodu == "HORECA":
                    l8_net = l7 * kg.k_horeca
                else:
                    l8_net = l7 / (D("1") - kg.m_retail)
                hucre.append(q(l8_net * (D("1") + v)))
            print(f"{kanal_kodu:<20}{sc:<8}{hucre[0]:>12}{hucre[1]:>12}")
    print("\nNOT: g bu tabloda SONUCU DEGISTIRMEZ (CIF=0 iken GV=0). Iki sutunun")
    print("     ayni cikmasi bir hata degil, maktu OTV'nin yapisal imzasidir.")


def tablo_nakit_ortusu() -> None:
    bolum("M) CASH VIEW (R9) — TAVANDAKİ NAKİT ÖRTÜSÜ · ECONOMIC VIEW İLE TOPLANMAZ")
    print("RC1/RC2/RC3: bu tablo cif_try_max'i DEGISTIRMEZ; ondan SONRA turetilmistir.")
    print("Rakamlar CIF = TAVAN varsayimiyla hesaplanmistir -> NAKIT CIKISININ UST SINIRI.")
    print(f"\n{'HEDEF':<8}{'GV':>10}{'OTV':>10}{'KDV_ith':>10}{'KKDF':>8}"
          f"{'GUMRUK_TOPLAM':>15}{'l4_econ':>10}{'l4_cash':>10}")
    for _, hedef in HEDEFLER:
        s = kos(hedef, "ES", "CHAIN_RETAIL", "BASE", 5000, True)
        print(f"{str(hedef):<8}{q(s.gv_try):>10}{q(s.otv_try):>10}{q(s.kdv_ithal_nakit):>10}"
              f"{q(s.kkdf_try):>8}{q(s.gumrukte_nakden_odenen):>15}"
              f"{q(s.l4_econ_max):>10}{q(s.l4_cash_max):>10}")
    s = kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", 5000, True)
    print(f"\nSEVKIYAT BASINA (799 TL hedef, tavanda) — TRY:")
    print(f"{'HACIM':<10}{'GUMRUKTE_PESIN':>18}{'BANDROL_PESIN':>18}{'TOPLAM_PESIN':>16}")
    for vol in VOLUMES:
        sv = kos(D("799"), "ES", "CHAIN_RETAIL", "BASE", vol, True)
        gum = sv.gumrukte_nakden_odenen * D(str(vol))
        ban = BANDROL * D(str(vol))
        print(f"{str(vol):<10}{q(gum):>18}{q(ban):>18}{q(gum+ban):>16}")
    print("\npeak_cash_requirement HESAPLANMAMISTIR: gercek CIF (T-466), antrepo")
    print("bekleme suresi (T-301, CRITICAL), fiili tahsilat vadesi (C-601) ve fx")
    print("(T-912) olmadan tutar UNKNOWN'dir. Yukaridaki tablo YALNIZCA vergi ve")
    print("bandrol bacaginin TAVAN nakit cikisini gosterir.")


def main() -> int:
    satir, r8fail, r8kfail = csv_uret()
    print("=" * 100)
    print("TUR 2.5 REVERSE TARGET MODEL — CIKTI URETIMI")
    print("=" * 100)
    print(f"country-buying-ceilings.csv : {satir} satir yazildi")
    print(f"R8   (vergi bacagi) round-trip BASARISIZ satir sayisi : {r8fail}")
    print(f"R8-K (kanal bacagi) round-trip BASARISIZ satir sayisi : {r8kfail}   <-- T-619 / T-942")
    tablo_katman_izi()
    tablo_hedef_x_kanal()
    tablo_ulke()
    tablo_hacim()
    tablo_lambda()
    tablo_importer_marj()
    tablo_distributor()
    tablo_kendi_dagitim()
    tablo_tornado()
    tablo_vergi_yuku()
    tablo_yapisal_taban()
    tablo_nakit_ortusu()
    tablo_rfq_tavan()
    return 0


if __name__ == "__main__":
    sys.exit(main())
