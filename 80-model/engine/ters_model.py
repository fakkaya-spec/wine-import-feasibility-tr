"""
ters_model.py — TERS (REVERSE) FİYAT MODELİ · L8 -> L0/L1

===========================================================================
 KAYNAK SPESİFİKASYON (kod değil, sözleşme)
===========================================================================
  30-vergi-gumruk/ters-model-vergi-bacagi.md        (R1..R11, RC1..RC6, O-1..O-7,
                                                     H1..H6, TV-1..TV-10)
  80-model/inputs/vergi.yaml -> ters_model_vergi_bacagi   (makine okunur karşılık)
  70-kanal/kanal-marj-yapisi.md §1.3                (R2..R4 taşıyıcı denklem)
  70-kanal/marj-vs-markup.md                        (margin != markup)

GÜVENLİK KİLİDİ (CLAUDE.md §12):
  - Bu dosyada HİÇBİR vergi oranı / ÖTV tutarı / KDV oranı / KKDF oranı /
    matrah tanımı HARD-CODE EDİLMEZ. Hepsi vergi.yaml'dan okunur.
  - İşlem SIRASI da (R7a->R7b->R7c->R7d) vergi.yaml'daki `adimlar`
    listesinden okunur; koda gömülmez.
  - Girdi yoksa UNKNOWN döner; "makul değer" ile doldurulmaz.

KATMAN DİSİPLİNİ (CLAUDE.md §6):
  - `L4` çıplak tokeni YASAKTIR. `l4_econ` ve `l4_cash` AYRI alanlardır ve
    TOPLANMAZ (R7-K3, RC3).
  - ECONOMIC view `cif_try_max` üretir; CASH view `peak_cash` bileşenlerini
    üretir ve `cif_try_max`'ı DEĞİŞTİRMEZ (RC1/RC2).
===========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, getcontext
from typing import Any

from otv_zaman_serisi import (  # noqa: E402
    OTV_SENARYO_UPPER_BOUND_LAMBDA_1,
    OtvOkumasi,
    otv_maktu,
)

getcontext().prec = 28

SIFIR = Decimal("0")


def _d(v: Any) -> Decimal | None:
    if v is None:
        return None
    return Decimal(str(v))


# ---------------------------------------------------------------------------
# Girdi sözleşmesi
# ---------------------------------------------------------------------------

@dataclass
class KanalGirdisi:
    """
    R2-R4 — kanal-marj-uzmani alanı. Hepsi ASSUMPTION / SENSITIVITY_ONLY.
    `M1` gereği dört nitelik burada sabittir:
      margin ON SELLING PRICE · BRÜT · KDV HARİÇ · L7 -> L8
    """
    kanal_kodu: str                    # CHAIN_RETAIL | INDEPENDENT_TEKEL | HORECA
    senaryo: str                       # LOW | BASE | HIGH
    m_retail: Decimal | None = None    # margin on selling price (CHAIN/TEKEL)
    k_horeca: Decimal | None = None    # çarpan (HORECA), L7 (KDV hariç) üzerine
    d: Decimal = SIFIR                 # geri akan bedeller, L6 cirosu oranı
    f_per_bottle: Decimal = SIFIR      # sabit bedellerin şişe başı payı
    f_unknown_sifir_alindi: bool = True
    d_unknown_sifir_alindi: bool = False


@dataclass
class L5Kalemi:
    ad: str
    tutar_try: Decimal | None
    para_birimi: str
    status: str
    evidence_id: str | None = None
    dusuldu_mu: bool = True
    not_: str = ""


@dataclass
class TersSonuc:
    hesaplandi: bool
    status: str                                   # MODEL_DERIVED_UPPER_BOUND | UNKNOWN
    etiketler: list[str] = field(default_factory=list)
    eksik_girdiler: list[str] = field(default_factory=list)
    uyarilar: list[str] = field(default_factory=list)
    kullanilan_evidence_ids: list[str] = field(default_factory=list)

    # --- katmanlar (TRY/şişe) ---
    l8_kdv_dahil: Decimal | None = None
    l8_net: Decimal | None = None
    l7_eff: Decimal | None = None
    l6: Decimal | None = None
    l5_max: Decimal | None = None
    l4_econ_max: Decimal | None = None
    l4_cash_max: Decimal | None = None            # AYRI ALAN — l4_econ ile TOPLANMAZ
    l3_pre_tax_landed_max: Decimal | None = None  # bilgi amaçlı, çift sayılmaz
    cif_try_max_upper_bound: Decimal | None = None
    fob_try_max: Decimal | None = None            # fx olmadan UNKNOWN
    exw_try_max: Decimal | None = None            # fx olmadan UNKNOWN

    # --- vergi bacağı ---
    gv_orani: Decimal | None = None
    gv_orani_kaynagi: str | None = None
    gv_try: Decimal | None = None
    otv_try: Decimal | None = None
    otv_okumasi: OtvOkumasi | None = None
    kkdf_try: Decimal | None = None
    x_pre_try: Decimal | None = None
    kdv_orani: Decimal | None = None

    # --- CASH view (RC1/RC2/RC3 — ayrı tutulur) ---
    kdv_ithal_nakit: Decimal | None = None
    gumrukte_nakden_odenen: Decimal | None = None

    # --- izlenebilirlik ---
    l5_kalemleri: list[L5Kalemi] = field(default_factory=list)
    r8_roundtrip_fark: Decimal | None = None
    r8_gecti_mi: bool | None = None
    uygulanan_adim_sirasi: list[str] = field(default_factory=list)
    importer_katki_orani: Decimal = SIFIR


# ---------------------------------------------------------------------------
# vergi.yaml okuyucuları — hiçbiri kodda sabit değildir
# ---------------------------------------------------------------------------

def kdv_orani_oku(vergi_yaml: dict[str, Any]) -> tuple[Decimal | None, str | None, list[str]]:
    """matrah_sirasi[sira=5].oran_pct -> oran (0-1) + evidence_id."""
    eksik: list[str] = []
    for satir in vergi_yaml.get("matrah_sirasi") or []:
        if satir.get("vergi") == "KDV":
            oran = _d(satir.get("oran_pct"))
            ev = satir.get("evidence_id")
            if oran is None:
                eksik.append("matrah_sirasi[KDV].oran_pct = null -> KDV orani UNKNOWN")
                return None, ev, eksik
            if satir.get("status") != "FACT":
                eksik.append(
                    f"matrah_sirasi[KDV].status={satir.get('status')} (FACT degil)"
                )
            return oran / Decimal("100"), ev, eksik
    eksik.append("matrah_sirasi icinde KDV satiri YOK -> KDV orani UNKNOWN")
    return None, None, eksik


def gv_orani_oku(
    vergi_yaml: dict[str, Any],
    country: str,
    tercihli_belge_ibraz_edildi: bool,
    dogrudan_nakliyat_saglandi: bool,
) -> tuple[Decimal | None, str, list[str], str | None]:
    """
    mense_tarife_eslemesi.engine_okuma_kurali'ni BİREBİR uygular.
    Dönüş: (oran 0-1, kaynak açıklaması, uyarılar, evidence_id)
    """
    uyarilar: list[str] = []
    blok = vergi_yaml.get("mense_tarife_eslemesi") or {}
    kayit = None
    for u in blok.get("ulkeler") or []:
        if str(u.get("country")).upper() == country.upper():
            kayit = u
            break

    if kayit is None:
        # adim 1: DU fallback
        du = (vergi_yaml.get("gumruk_vergisi_oranlari_by_mense") or {}).get(
            "diger_ulkeler_DU"
        ) or {}
        oran = _d(du.get("oran_pct"))
        if oran is None:
            uyarilar.append(
                f"{country}: mense tablosunda YOK ve DU fallback orani da null -> UNKNOWN"
            )
            return None, "UNKNOWN", uyarilar, None
        uyarilar.append(
            f"{country}: mense_tarife_eslemesi.ulkeler listesinde YOK -> "
            f"DU FALLBACK (%{oran}) uygulandi (engine_okuma_kurali adim 1)."
        )
        return oran / Decimal("100"), "DU_FALLBACK", uyarilar, du.get("evidence_id")

    tercihli = kayit.get("preferential_regime")
    oran_pct = _d(kayit.get("applicable_customs_rate"))
    ev = kayit.get("evidence_id")

    if tercihli is None:
        if oran_pct is None:
            uyarilar.append(f"{country}: applicable_customs_rate null -> UNKNOWN")
            return None, "UNKNOWN", uyarilar, ev
        return oran_pct / Decimal("100"), "KOSULSUZ", uyarilar, ev

    # adım 3: KOŞULLU
    if tercihli_belge_ibraz_edildi and dogrudan_nakliyat_saglandi:
        if oran_pct is None:
            uyarilar.append(f"{country}: applicable_customs_rate null -> UNKNOWN")
            return None, "UNKNOWN", uyarilar, ev
        return oran_pct / Decimal("100"), "KOSULLU_SAGLANDI", uyarilar, ev

    ceza = ((vergi_yaml.get("tercihli_tarife") or {})
            .get("mense_ispat_belgesi_yoksa_uygulanan_oran") or {})
    ceza_oran = _d(ceza.get("value") if isinstance(ceza, dict) else ceza)
    if ceza_oran is None:
        du = (vergi_yaml.get("gumruk_vergisi_oranlari_by_mense") or {}).get(
            "diger_ulkeler_DU"
        ) or {}
        ceza_oran = _d(du.get("oran_pct"))
        if ceza_oran is not None:
            uyarilar.append(
                f"{country}: tercihli_tarife.mense_ispat_belgesi_yoksa_uygulanan_oran "
                f"okunamadi -> diger_ulkeler_DU (%{ceza_oran}) kullanildi."
            )
    if ceza_oran is None:
        uyarilar.append(f"{country}: kosul saglanmadi ve ceza orani UNKNOWN")
        return None, "UNKNOWN", uyarilar, ev
    return ceza_oran / Decimal("100"), "KOSULLU_DUSTU", uyarilar, ev


def r7_adim_sirasini_oku(vergi_yaml: dict[str, Any]) -> tuple[list[str], list[str]]:
    """
    R7 alt adımlarının SIRASINI vergi.yaml'dan okur (koda gömülmez).
    Beklenen: R7a -> R7b -> R7c -> R7d, ama otorite DOSYADIR.
    """
    uyarilar: list[str] = []
    blok = vergi_yaml.get("ters_model_vergi_bacagi") or {}
    kodlar = [str(a.get("kod")) for a in (blok.get("adimlar") or []) if a.get("kod")]
    r7 = [k for k in kodlar if k.startswith("R7")]
    if not r7:
        uyarilar.append(
            "vergi.yaml/ters_model_vergi_bacagi.adimlar icinde R7* adimi YOK -> "
            "ters vergi bacagi sirasi okunamadi."
        )
        return [], uyarilar
    if "R7d" in r7:
        bolme = r7.index("R7d")
        maktu_sonrasi = [k for k in r7[bolme + 1:] if k in ("R7b", "R7c")]
        if maktu_sonrasi:
            uyarilar.append(
                f"H1 RISKI: {maktu_sonrasi} adimlari bolme adimindan (R7d) SONRA "
                f"tanimlanmis. Spesifikasyon MAKTU kalemlerin bolmeden ONCE "
                f"cikarilmasini emreder (R7-K1)."
            )
    return r7, uyarilar


# ---------------------------------------------------------------------------
# R2-R4 : kanal bacağı (vergi bacağı DEĞİL)
# ---------------------------------------------------------------------------

def kanal_bacagi(l8_net: Decimal, kanal: KanalGirdisi) -> tuple[Decimal | None, Decimal | None, list[str]]:
    """
    Dönüş: (l7_eff, l6, uyarılar)

    CHAIN_RETAIL / INDEPENDENT_TEKEL:
        L7_eff = L8_net * (1 - m)                      [MARGIN ON SELLING PRICE]
        L6     = (L7_eff + f) / (1 - d)
    HORECA:
        çarpan KDV HARİÇ L7 üzerine uygulanır (kanal.yaml k_horeca_carpan.kdv_dahil_mi)
        L7_horeca = L8_net / k    ;    L6 = L7_horeca
    """
    uyarilar: list[str] = []
    if kanal.kanal_kodu == "HORECA":
        if kanal.k_horeca is None or kanal.k_horeca == 0:
            return None, None, ["HoReCa carpani (k) yok -> UNKNOWN"]
        l7 = l8_net / kanal.k_horeca
        uyarilar.append(
            "HoReCa: carpan KDV HARIC L7 uzerine uygulanmistir "
            "(kanal.yaml -> duyarlilik_senaryolari.k_horeca_carpan.kdv_dahil_mi). "
            "Hedef merdiven burada MENU FIYATI olarak yorumlanmistir."
        )
        return l7, l7, uyarilar

    if kanal.m_retail is None:
        return None, None, ["m_retail yok -> UNKNOWN"]
    l7 = l8_net * (Decimal("1") - kanal.m_retail)
    if kanal.d >= 1:
        return l7, None, ["d >= 1 -> L6 tanimsiz"]
    l6 = (l7 + kanal.f_per_bottle) / (Decimal("1") - kanal.d)
    return l7, l6, uyarilar


# ---------------------------------------------------------------------------
# İLERİ YÖN (R8 round-trip için) — matrah-sirasi.md §4'ten birebir
# ---------------------------------------------------------------------------

def ileri_l4_econ(
    cif: Decimal, gv_orani: Decimal, kkdf: Decimal, otv: Decimal, x_pre: Decimal
) -> Decimal:
    """L4_econ = C + C*g + k + O + X_pre   (KDV HARİÇ — l4_cash DEĞİL)."""
    gv = cif * gv_orani
    return cif + gv + kkdf + otv + x_pre


def r7_coz(
    l4_econ_max: Decimal,
    otv: Decimal,
    kkdf: Decimal,
    x_pre: Decimal,
    gv_orani: Decimal,
    r7_sira: list[str],
) -> tuple[Decimal | None, bool]:
    """
    R7 çekirdeği. Adım SIRASI dışarıdan (vergi.yaml'dan) gelir.
    Dönüş: (cif_try_max, bolme_yapildi_mi)
    """
    A = l4_econ_max
    bolundu = False
    for kod in r7_sira:
        if kod == "R7a":
            A = l4_econ_max
        elif kod == "R7b":
            A = A - otv
        elif kod == "R7c":
            A = A - kkdf - x_pre
        elif kod == "R7d":
            A = A / (Decimal("1") + gv_orani)
            bolundu = True
    return (A if bolundu else None), bolundu


# ---------------------------------------------------------------------------
# ANA FONKSİYON
# ---------------------------------------------------------------------------

def ters_zincir(
    vergi_yaml: dict[str, Any],
    l8_kdv_dahil: Decimal,
    kanal: KanalGirdisi,
    country: str,
    l5_kalemleri: list[L5Kalemi],
    *,
    tercihli_belge_ibraz_edildi: bool = True,
    dogrudan_nakliyat_saglandi: bool = True,
    odeme_sekli: str = "pesin",
    x_pre: Decimal = SIFIR,
    importer_katki_orani: Decimal = SIFIR,
    t: str | None = None,
    otv_senaryo: str | None = OTV_SENARYO_UPPER_BOUND_LAMBDA_1,
    lambda_katsayisi: Decimal | None = None,
) -> TersSonuc:
    """
    L8 (KDV dahil hedef) -> ... -> CIF_TRY_max_UPPER_BOUND

    `importer_katki_orani` = ithalatçının L6 üzerinden hedef katkı payı.
    VARSAYILAN 0 -> çıktı **MAXIMUM STRUCTURAL BUY PRICE**'tır
    (yatırımcı eşiği OQ-901 belirlenmediği için TARGET/ACCEPTABLE/WALK-AWAY
    üretilmez — GÖREV 7).
    """
    s = TersSonuc(hesaplandi=False, status="UNKNOWN")
    s.l8_kdv_dahil = l8_kdv_dahil
    s.importer_katki_orani = importer_katki_orani
    s.x_pre_try = x_pre

    # ---- R1 : zincirdeki TEK KDV işlemi -------------------------------
    v, kdv_ev, eksik = kdv_orani_oku(vergi_yaml)
    s.eksik_girdiler.extend(eksik)
    if v is None:
        return s
    s.kdv_orani = v
    if kdv_ev:
        s.kullanilan_evidence_ids.append(kdv_ev)
    s.l8_net = l8_kdv_dahil / (Decimal("1") + v)
    s.uygulanan_adim_sirasi.append("R1")

    # ---- R2-R4 : kanal bacağı -----------------------------------------
    l7, l6, ky = kanal_bacagi(s.l8_net, kanal)
    s.uyarilar.extend(ky)
    if l7 is None or l6 is None:
        s.eksik_girdiler.append("Kanal bacagi cozulemedi -> UNKNOWN")
        return s
    s.l7_eff, s.l6 = l7, l6
    s.uygulanan_adim_sirasi.append("R2_R4")

    # ---- R5 : ithalatçı katkı payı ------------------------------------
    #
    # ⚠ ÇİFT SAYIM / EKSİK SAYIM DÜZELTMESİ (finans-fizibilite, TUR 2.5)
    # ------------------------------------------------------------------
    # R5'in sahibi bu ajandır (`ters_model_vergi_bacagi.adimlar[R5].sahibi`).
    # NAIF UYGULAMA:   L5_max = L6 * (1 - mu)          <-- YANLIS
    # Cunku `d` (geri akan bedeller) ve `f` (listeleme bedeli) ITHALATCININ
    # ODEDIGI bedellerdir (perakendeci -> ithalatci HIZMET FATURASI,
    # EV-2026-08-10-612). Ithalatcinin FIILI net hasilati L6 degil,
    #     L7_eff = L6*(1-d) - f
    # dir. L5_max = L6 alinirsa `d*L6 + f` HICBIR YERDE dusulmez ->
    # azami CIF YUKARI sapar (799/CHAIN/BASE'te +28,95 TL/sise).
    #
    # DOGRU UYGULAMA:
    #     L5_max = L7_eff - mu * L6        (mu = katki payi, L6 cirosu uzerinden)
    #     mu = 0  =>  L5_max = L7_eff
    s.l5_max = l7 - importer_katki_orani * l6
    s.uygulanan_adim_sirasi.append("R5")
    if kanal.d > 0 or kanal.f_per_bottle > 0:
        s.uyarilar.append(
            f"R5: kanal geri akan bedelleri (d={kanal.d}, f={kanal.f_per_bottle}) "
            f"ITHALATCI MALIYETIDIR ve L5_max = L7_eff olarak TEK KEZ dusulmustur. "
            f"L6 ({l6}) yalnizca FATURA fiyatidir; L5 butcesi DEGILDIR."
        )

    # ---- R6 : L5 kalemleri --------------------------------------------
    s.l5_kalemleri = list(l5_kalemleri)
    toplam_l5 = SIFIR
    for k in l5_kalemleri:
        if not k.dusuldu_mu:
            continue
        if k.tutar_try is None:
            s.uyarilar.append(
                f"L5 kalemi '{k.ad}' UNKNOWN -> 0 alindi ve BU CIKTIDA YAZILDI "
                f"(RC5 tipi acik). Yon: sonucu YUKARI SAPTIRIR."
            )
            continue
        if k.para_birimi != "TRY":
            s.uyarilar.append(
                f"L5 kalemi '{k.ad}' {k.para_birimi} cinsindendir; makro.yaml/fx "
                f"null oldugu icin TRY'ye CEVRILMEDI ve 0 alindi (T-912). "
                f"Yon: sonucu YUKARI SAPTIRIR."
            )
            continue
        toplam_l5 += k.tutar_try
        if k.evidence_id:
            s.kullanilan_evidence_ids.append(k.evidence_id)
    s.l4_econ_max = s.l5_max - toplam_l5
    s.uygulanan_adim_sirasi.append("R6")

    # ---- R7 : vergi bacağı --------------------------------------------
    g, g_kaynak, g_uyari, g_ev = gv_orani_oku(
        vergi_yaml, country, tercihli_belge_ibraz_edildi, dogrudan_nakliyat_saglandi
    )
    s.uyarilar.extend(g_uyari)
    if g is None:
        s.eksik_girdiler.append(f"{country}: gumruk vergisi orani UNKNOWN")
        return s
    s.gv_orani, s.gv_orani_kaynagi = g, g_kaynak
    if g_ev:
        s.kullanilan_evidence_ids.append(g_ev)

    # KKDF — TV-9 kilidi
    if odeme_sekli != "pesin":
        s.eksik_girdiler.append(
            f"odeme_sekli='{odeme_sekli}' -> KKDF MATRAHI UNKNOWN (T-105). "
            f"Iki olasi cebir arasinda MODEL SECIM YAPMAZ -> cif_try_max UNKNOWN."
        )
        s.status = "UNKNOWN"
        return s
    s.kkdf_try = SIFIR

    # ÖTV — T-921 ufuk denetimi buradan geçer
    okuma = otv_maktu(vergi_yaml, t=t, otv_senaryo=otv_senaryo,
                      lambda_katsayisi=lambda_katsayisi)
    s.otv_okumasi = okuma
    s.etiketler.extend(okuma.etiketler)
    s.uyarilar.extend(okuma.uyarilar)
    s.eksik_girdiler.extend(okuma.eksik_girdiler)
    if not okuma.hesaplandi or okuma.otv_try_per_sise is None:
        s.status = "UNKNOWN"
        return s
    s.otv_try = okuma.otv_try_per_sise
    if okuma.evidence_id:
        s.kullanilan_evidence_ids.append(okuma.evidence_id)

    # --- R7 alt adımlarının SIRASI DOSYADAN okunur (R7-K1) -------------
    r7_sira, r7_uyari = r7_adim_sirasini_oku(vergi_yaml)
    s.uyarilar.extend(r7_uyari)
    if not r7_sira:
        s.eksik_girdiler.append("R7 adim sirasi okunamadi -> UNKNOWN")
        return s

    A, bolundu = r7_coz(s.l4_econ_max, s.otv_try, s.kkdf_try, x_pre, g, r7_sira)
    s.uygulanan_adim_sirasi.extend(r7_sira)
    if not bolundu or A is None:
        s.eksik_girdiler.append("R7d (bolme adimi) uygulanmadi -> UNKNOWN")
        return s

    s.cif_try_max_upper_bound = A
    s.gv_try = A * g

    # ---- R8 : ZORUNLU round-trip --------------------------------------
    geri = ileri_l4_econ(A, g, s.kkdf_try, s.otv_try, x_pre)
    s.r8_roundtrip_fark = abs(geri - s.l4_econ_max)
    s.r8_gecti_mi = s.r8_roundtrip_fark < Decimal("0.01")
    s.uygulanan_adim_sirasi.append("R8")
    if not s.r8_gecti_mi:
        s.status = "UNKNOWN"
        s.eksik_girdiler.append(
            f"R8 ROUND-TRIP TUTMADI: |ileri(cif).L4_econ - L4_econ_max| = "
            f"{s.r8_roundtrip_fark} >= 0.01 TL. Tutmayan adim: R7 zinciri."
        )
        return s

    # ---- R9 : CASH view (AYRI — RC1/RC2/RC3) --------------------------
    s.kdv_ithal_nakit = v * s.l4_econ_max
    s.l4_cash_max = s.l4_econ_max + s.kdv_ithal_nakit
    s.gumrukte_nakden_odenen = s.gv_try + s.kkdf_try + s.otv_try + s.kdv_ithal_nakit
    s.uygulanan_adim_sirasi.append("R9")

    # ---- L3 (bilgi amaçlı; ÇİFT SAYILMAZ) -----------------------------
    # L3 = CIF + vergi ÖNCESİ yurt içi masraflar. Bu masraflar YUKARIDA
    # L5 kalemleri olarak ZATEN düşülmüştür; burada yalnızca GÖSTERİLİR.
    yurt_ici = sum(
        (k.tutar_try or SIFIR)
        for k in l5_kalemleri
        if k.dusuldu_mu and k.para_birimi == "TRY" and k.ad.startswith("TR_")
    )
    s.l3_pre_tax_landed_max = s.cif_try_max_upper_bound + Decimal(str(yurt_ici))

    # ---- R10/R11 : FOB / EXW -> fx olmadan UNKNOWN --------------------
    s.fob_try_max = None
    s.exw_try_max = None
    s.eksik_girdiler.append(
        "R10/R11: fob_try_max ve exw_try_max UNKNOWN — navlun ve mense local "
        "charge'lari USD/EUR cinsindendir, makro.yaml/fx null (T-912) ve "
        "gumruk beyan kuru kurali UNKNOWN (T-911)."
    )

    s.hesaplandi = True
    s.status = (
        "MODEL_DERIVED_UPPER_BOUND" if okuma.upper_bound_mu else "MODEL_DERIVED"
    )
    s.etiketler.append(
        "TARGET_SHELF_PRICE (INVESTOR_ASSUMPTION) uzerinden hesaplanmistir — "
        "sonuc TARGET / MODEL_DERIVED'dir, FACT veya QUOTE DEGILDIR (L5)."
    )
    s.etiketler.append(
        "USD/EUR cinsli L5 kalemleri (varis local charge, devanning, CFS, "
        "musavirlik CIF kademesi) 0 alinmistir -> cif_try_max IKINCI BIR "
        "NEDENLE de UST SINIRDIR."
    )
    # gözetim uyarısı — vergi.yaml'dan okunur
    goz = ((vergi_yaml.get("ters_model_vergi_bacagi") or {})
           .get("gozetim_ters_model_mantigi") or {})
    esik = ((goz.get("gozetim_esigi") or {}).get("value"))
    if esik is None:
        s.uyarilar.append(
            "GOZETIM: esik dogrulanmamistir (null/UNKNOWN, EV-2026-08-09-125). "
            "cif_try_max BIR ALT SINIRLA TEST EDILMEMISTIR."
        )
    s.uyarilar.append(f"X_pre = {x_pre} TL/sise alinmistir (vergi.yaml X_pre.cikti_kurali).")
    return s
