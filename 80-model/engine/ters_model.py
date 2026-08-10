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

import kanal_bacagi as KB  # noqa: E402
from kalem_defteri import (  # noqa: E402
    DAMGA_BLOCKED,
    DAMGA_EXCLUDED,
    DAMGA_OK,
    KalemDefteri,
    MaliyetKalemi,
    blocked_envanterinden_kalemler,
)
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
    d: Decimal = SIFIR                 # geri akan bedeller, L6 cirosu oranı (= d_var)
    f_per_bottle: Decimal = SIFIR      # ⛔ TÜREV — doğrudan girdi olarak VERİLMEMELİ (K7)
    f_unknown_sifir_alindi: bool = True
    d_unknown_sifir_alindi: bool = False

    # ---- TUR 3A eklentileri (kanal-katman-matrah-haritasi.md §9) ----
    mu_matrahi: str | None = None          # L6 | L7_EFF | L5_MARKUP  (K5 / T-616)
    F_total: Decimal | None = None         # listeleme bedeli DÖNEM TOPLAMI (K7)
    F_total_kdv_dahil_mi: str | None = None
    D_fix_total: Decimal | None = None     # d sepetinin SABİT bileşenleri (K8)
    D_fix_kdv_dahil_mi: str | None = None
    q_ithal: Decimal | None = None         # sabit maliyetlerin BÖLENİ (K11)
    r_iade: Decimal | None = None
    geri_kazanilabilir_deger: Decimal | None = None
    m_dist: Decimal = SIFIR                # dış distribütör marjı (matrah L6)
    dagitim_modeli: str = "MODEL_B"        # MODEL_A | MODEL_B
    d_kimde: str | None = None             # BIZDE | DISTRIBUTORDE (MODEL_A'da ZORUNLU)
    odeme_vadesi_gun: Decimal | None = None
    finansman_orani_yillik: Decimal | None = None

    def kanal_parametreleri(self, v: Decimal) -> "KB.KanalParametreleri":
        """`KanalGirdisi` -> `kanal_bacagi.KanalParametreleri` köprüsü."""
        return KB.KanalParametreleri(
            kanal_kodu=self.kanal_kodu,
            v=v,
            m=self.m_retail,
            k=self.k_horeca,
            d_var=self.d,
            F_total=self.F_total,
            F_total_kdv_dahil_mi=self.F_total_kdv_dahil_mi,
            D_fix_total=self.D_fix_total,
            D_fix_kdv_dahil_mi=self.D_fix_kdv_dahil_mi,
            Q_ithal=self.q_ithal,
            r_iade=self.r_iade,
            geri_kazanilabilir_deger=self.geri_kazanilabilir_deger,
            mu=SIFIR,                       # ters_zincir kendi mu'sunu enjekte eder
            mu_matrahi=self.mu_matrahi,
            m_dist=self.m_dist,
            dagitim_modeli=self.dagitim_modeli,
            d_kimde=self.d_kimde,
            odeme_vadesi_gun=self.odeme_vadesi_gun,
            finansman_orani_yillik=self.finansman_orani_yillik,
        )


@dataclass
class L5Kalemi:
    """
    ⚠ TUR 3A: ZORUNLU METADATA (`kanal-katman-matrah-haritasi.md` §2).
    Dokuz alandan biri eksikse kalem `BLOCKED_INPUT` damgası alır ve
    **SESSİZCE 0 SAYILMAZ.** Eski çağrılar bozulmasın diye alanlar
    varsayılan `None`'dır — ama `None` artık GÖRÜNÜR bir eksikliktir.
    """
    ad: str
    tutar_try: Decimal | None
    para_birimi: str
    status: str
    evidence_id: str | None = None
    dusuldu_mu: bool = True
    not_: str = ""

    # ---- dokuz zorunlu alandan geri kalanlar ----
    payer: str | None = None
    receiver: str | None = None
    layer: str | None = None
    fixed_or_variable: str | None = None
    per_bottle_or_total: str | None = None
    tax_treatment: str | None = None
    kdv_dahil_mi: str | None = None
    haric_gerekce: str | None = None       # doluysa EXCLUDED_WITH_REASON
    hard_blocker: bool = False
    sahibi: str | None = None
    ticket: str | None = None
    yon: str | None = None

    def to_maliyet_kalemi(self) -> MaliyetKalemi:
        return MaliyetKalemi(
            kalem_kimligi=f"L5::{self.ad}",
            ad=self.ad,
            payer=self.payer,
            receiver=self.receiver,
            layer=self.layer,
            currency=self.para_birimi,
            fixed_or_variable=self.fixed_or_variable,
            per_bottle_or_total=self.per_bottle_or_total,
            tax_treatment=self.tax_treatment,
            evidence_id=self.evidence_id,
            status=self.status,
            tutar_try=self.tutar_try if self.para_birimi == "TRY" else None,
            kdv_dahil_mi=self.kdv_dahil_mi,
            dusuldu_mu=self.dusuldu_mu,
            haric_gerekce=self.haric_gerekce,
            hard_blocker=self.hard_blocker,
            sahibi=self.sahibi,
            ticket=self.ticket,
            yon=self.yon,
            notes=self.not_,
        )


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

    # --- TUR 3A : R8-K (kanal round-trip, T-619) ---
    r8k_gecti_mi: bool | None = None
    r8k_fark: Decimal | None = None
    r8k_adimlari: list[str] = field(default_factory=list)
    r8k_tutmayan_adim: str | None = None

    # --- TUR 3A : metadata damgaları (GÖREV 1) ---
    defter: KalemDefteri | None = None
    damga_ozeti: dict[str, int] = field(default_factory=dict)
    blocked_input: list[str] = field(default_factory=list)
    excluded_with_reason: list[str] = field(default_factory=list)
    kanal_bayraklari: list[str] = field(default_factory=list)

    # --- TUR 3A : md.36 koşullu KDV kilidi (T-171) ---
    md36_tetiklendi_mi: bool | None = None
    md36_indirilemeyen_kdv: Decimal | None = None

    # --- TUR 3A : L6_gross (K12a) ---
    l6_gross: Decimal | None = None


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


def _bilincli_haric_kalemler() -> list[MaliyetKalemi]:
    """
    `EXCLUDED_WITH_REASON` — modelden **bilinçli olarak** çıkarılan kalemler.

    Bunlar `BLOCKED_INPUT` DEĞİLDİR: eksik veri yoktur, bir MİMARİ KARAR
    vardır. Karar yazılmadığı sürece "unutulmuş" ile "çıkarılmış" ayırt
    edilemez — bu blok o ayrımı kurar.
    """
    return [
        MaliyetKalemi(
            "KANAL::markup_karsiligi_k", ad="markup karsiligi (k)", status="DERIVED",
            dusuldu_mu=False,
            haric_gerekce=(
                "m ve k AYNI gercegin iki ifadesidir (k = m/(1-m)). Ikisi birden "
                "dusulurse CIFT SAYIMDIR. kanal.yaml/markup_basis."
                "modele_girme_kurali = ENGINE_OKUMAZ (K2)."),
        ),
        MaliyetKalemi(
            "KANAL::kdv_v2_mal_faturasi", ad="mal faturasi KDV'si (V2)", status="STRUCTURAL_FACT",
            dusuldu_mu=False,
            haric_gerekce=(
                "EKONOMIK MALIYET DEGILDIR (tahsil edilip beyan edilir) -> P&L'e "
                "GIRMEZ. YALNIZCA nakit akisinda vardir ve matrahi L6_gross'tur "
                "(K12a). Ekonomik daldan CIKARILMISTIR, nakit dalinda DURUR."),
        ),
        MaliyetKalemi(
            "VERGI::kdv_ithal_ekonomik", ad="ithalat KDV'si — ekonomik dal", status="FACT",
            dusuldu_mu=False,
            haric_gerekce=(
                "(A) KDV INDIRIMI CONFIRMED (T-947/T-171, KDVK md.29/1-b + md.34/1; "
                "7846 s. CBK VARDIR ama 2204.21'e DEGMEZ). Indirilebilir KDV "
                "EKONOMIK MALIYET DEGILDIR -> l4_econ'a GIRMEZ. Nakit dalinda "
                "l4_cash / gumrukte_nakden_odenen icinde AYRICA durur (RC1/RC3)."),
        ),
        MaliyetKalemi(
            "KATMAN::L3_pre_tax_landed", ad="L3 pre-tax landed", status="DERIVED",
            dusuldu_mu=False,
            haric_gerekce=(
                "L3 BILGI AMACLIDIR. Bilesenleri (TR-ici yurt ici masraflar) L5 "
                "kalemleri olarak ZATEN dusulmustur; L3 ayrica dusulurse CIFT "
                "SAYIM olur (LEDGER_UNIQUENESS / K6)."),
        ),
        MaliyetKalemi(
            "KATMAN::L6_fatura_fiyati", ad="L6 fatura fiyati", status="STRUCTURAL_FACT",
            dusuldu_mu=False,
            haric_gerekce=(
                "L6 bir FATURA fiyatidir, bir HASILAT degildir ve bir L5 BUTCESI "
                "hic degildir. R8-K geri insa zincirinde HIC KULLANILMAZ (T-619). "
                "Yalnizca (i) d_var'in matrahi ve (ii) L6_gross uzerinden alacak "
                "hesabi icin tutulur."),
        ),
    ]


def md36_indirilemeyen_kdv_oku(
    vergi_yaml: dict[str, Any],
) -> tuple[bool | None, Decimal | None, list[str], list[str]]:
    """
    ⛔ KOŞULLU KİLİT — `T-171` / `T-947`
    `vergi.yaml -> kdv_perspektifleri.a_ekonomik_maliyet.md36_indirim_kisiti`

    SONUÇ `(A) KDV İNDİRİMİ CONFIRMED`'dir; ama GEREKÇE değişmiştir:
    md.36'ya dayanan **yürürlükte bir CB kararı VARDIR (7846)** — yalnızca
    2204.21'e DEĞMEZ. Tetikleyici (gözetim OR korunma önlemi OR damping)
    `true` olursa indirilemeyen KDV **ekonomik maliyettir** ve ters modelde
    **MAKTU KALEM** gibi, `(1+gv)` bölmesinden **ÖNCE** çıkarılır.

    Dönüş: (tetiklendi_mi, indirilemeyen_kdv, uyarilar, bloke_girdiler)

    BUGÜN: tetiklendi_mi = False -> indirilemeyen_kdv = 0 -> MAX_CIF DEĞİŞMEZ.
    """
    uyarilar: list[str] = []
    bloke: list[str] = []
    blok = (
        ((vergi_yaml.get("kdv_perspektifleri") or {}).get("a_ekonomik_maliyet") or {})
        .get("md36_indirim_kisiti")
    ) or {}
    if not blok:
        bloke.append(
            "md36_indirim_kisiti: BLOCKED_INPUT (blok vergi.yaml'da YOK) | HARD | T-171"
        )
        return None, None, uyarilar, bloke

    # tetikleyici = G1 OR G2 OR G3 — HER BİRİ vergi.yaml'daki KENDİ alanından
    tetik = False
    okunamayan: list[str] = []
    for t in blok.get("tetikleyiciler") or []:
        yol = str(t.get("alan_referansi") or "")
        dugum: Any = vergi_yaml
        for parca in yol.split("."):
            dugum = (dugum or {}).get(parca) if isinstance(dugum, dict) else None
        deger = dugum.get("value") if isinstance(dugum, dict) else dugum
        if deger is None:
            okunamayan.append(f"{t.get('kod')}({yol})")
        elif bool(deger):
            tetik = True
    if okunamayan:
        bloke.append(
            f"md36 tetikleyicileri okunamadi: {', '.join(okunamayan)} -> "
            f"BLOCKED_INPUT (eksik alan: value) | HARD | T-171"
        )
        return None, None, uyarilar, bloke

    if not tetik:
        uyarilar.append(
            "md.36 KOSULLU KILIDI: tetikleyici (gozetim OR korunma onlemi OR "
            "dampinge karsi vergi) = FALSE -> 7846 s. CBK UYGULANMAZ -> ithalat "
            "KDV'si TAM INDIRILEBILIR -> kdv_ekonomik_maliyet = 0 (EV-2026-08-10-852/"
            "-860/-861/-862). DIKKAT: gerekce 'md.36 karari YOK' DEGIL, 'md.36 "
            "karari VAR ama bu urune DEGMIYOR'dur."
        )
        return False, SIFIR, uyarilar, bloke

    # --- tetiklendi: KISMİ kısıt. D (tevsik edilemeyen tutar) GEREKİR ---
    bloke.append(
        "md36_indirim_kisiti.D (tevsik edilemeyen tutar): BLOCKED_INPUT "
        "(eksik alan: tutar_try) | HARD | T-171 | kisit KISMIDIR, TAM DEGIL "
        "(KDVGUT III/C-2.6, EV-2026-08-10-854)"
    )
    return True, None, uyarilar, bloke


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
    md36_indirilemeyen_kdv: Decimal = SIFIR,
) -> tuple[Decimal | None, bool]:
    """
    R7 çekirdeği. Adım SIRASI dışarıdan (vergi.yaml'dan) gelir.
    Dönüş: (cif_try_max, bolme_yapildi_mi)

    `md36_indirilemeyen_kdv` KOŞULLU bir MAKTU kalemdir (T-171): tetikleyici
    `false` iken 0'dır ve hiçbir sayıyı değiştirmez; `true` olursa `(1+gv)`
    bölmesinden **ÖNCE** (R7c'de, ÖTV/KKDF ile aynı sırada) çıkarılır.
    """
    A = l4_econ_max
    bolundu = False
    for kod in r7_sira:
        if kod == "R7a":
            A = l4_econ_max
        elif kod == "R7b":
            A = A - otv
        elif kod == "R7c":
            A = A - kkdf - x_pre - md36_indirilemeyen_kdv
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
    kanal_yaml: dict[str, Any] | None = None,
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

    # ---- R2-R5 : KANAL BACAĞI — artık `kanal_bacagi.py` çözüyor -------
    #
    # TUR 3A / T-619: kanal bacağı K1..K6 kapalı formül setiyle hesaplanır ve
    # ARDINDAN `R8-K` ile BAĞIMSIZ olarak geri inşa edilir.
    kp = kanal.kanal_parametreleri(v)
    kp.mu = importer_katki_orani
    ks = KB.kanal_ileri(l8_kdv_dahil, kp)
    s.uyarilar.extend(ks.uyarilar)
    s.kanal_bayraklari.extend(ks.bayraklar)
    s.blocked_input.extend(ks.bloke_girdiler)
    s.blocked_input.extend(KB.kanala_ozgu_bloke_kalemler(kanal.kanal_kodu))
    if ks.l7_eff is None or ks.l6 is None or ks.l5_max is None:
        s.eksik_girdiler.append(
            "Kanal bacagi cozulemedi -> UNKNOWN. BLOCKED_INPUT: "
            + " ; ".join(ks.bloke_girdiler)
        )
        s.status = "UNKNOWN"
        return s
    l7, l6 = ks.l7_eff, ks.l6
    s.l7_eff, s.l6, s.l6_gross = l7, l6, ks.l6_gross
    s.uygulanan_adim_sirasi.append("K1_K6")

    # -- eski `kanal_bacagi()` ile PARİTE DENETİMİ (regresyon kilidi) ----
    l7_eski, l6_eski, ky = kanal_bacagi(s.l8_net, kanal)
    s.uyarilar.extend(ky)
    if l7_eski is not None and abs(l7_eski - l7) >= Decimal("0.0001"):
        s.eksik_girdiler.append(
            f"KANAL PARITE HATASI: eski kanal_bacagi L7_eff={l7_eski}, yeni "
            f"kanal_ileri L7_eff={l7}. Iki uygulama AYRISMIS -> UNKNOWN."
        )
        s.status = "UNKNOWN"
        return s

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
    #     L5_max = L7_eff - mu_kesintisi   (mu_kesintisi MATRAHA bagli — K5/T-616)
    #     mu = 0  =>  L5_max = L7_eff  (uc matrah da AYNI sonucu verir)
    s.l5_max = ks.l5_max
    s.uygulanan_adim_sirasi.append("R5")
    if kanal.d > 0 or (ks.f_per_bottle or SIFIR) > 0:
        s.uyarilar.append(
            f"R5: kanal geri akan bedelleri (d_var={kanal.d}, f={ks.f_per_bottle}) "
            f"ITHALATCI MALIYETIDIR ve L5_max = L7_eff olarak TEK KEZ dusulmustur. "
            f"L6 ({l6}) yalnizca FATURA fiyatidir; L5 butcesi DEGILDIR. "
            f"L6_gross ({s.l6_gross}) ise ALACAK tutaridir (K12a)."
        )

    # ---- R8-K : KANAL ROUND-TRIP (T-942 teshisi + T-619 duzeltmesi) ---
    #
    # ⛔ T-942'nin onerdigi `L6_geri = L5_max + mu*L6` ETIKETI YANLISTIR ve
    #    assertion'i TERSINE CEVIRIR. Burada `kanal-katman-matrah-haritasi.md`
    #    §9.1'deki DOGRU zincir kullanilir: L5_max -> L7_eff -> L8_net -> L8.
    #    `L6` bu zincirde HIC KULLANILMAZ.
    ok_k, fark_k, adim_k, tutmayan_k = KB.r8k_roundtrip(l8_kdv_dahil, s.l5_max, kp)
    s.r8k_gecti_mi, s.r8k_fark = ok_k, fark_k
    s.r8k_adimlari, s.r8k_tutmayan_adim = adim_k, tutmayan_k
    s.uygulanan_adim_sirasi.append("R8-K")
    if not ok_k:
        s.status = "UNKNOWN"
        s.eksik_girdiler.append(
            f"R8-K KANAL ROUND-TRIP TUTMADI: |L8_geri - L8_target| = {fark_k}. "
            f"Tutmayan adim: {tutmayan_k}. Adimlar: {' | '.join(adim_k)}"
        )
        return s

    # ---- R6 : L5 kalemleri — ZORUNLU METADATA + KALEM DEFTERİ ---------
    #
    # ⛔ TUR 3A GÖREV 1: hiçbir kalem SESSİZCE 0 GEÇMEZ.
    #    Her kalem üç damgadan birini alır: OK / BLOCKED_INPUT /
    #    EXCLUDED_WITH_REASON. LEDGER_UNIQUENESS (K6) defterde zorunludur.
    s.l5_kalemleri = list(l5_kalemleri)
    defter = KalemDefteri(kanal_kodu=kanal.kanal_kodu)
    try:
        for k in l5_kalemleri:
            defter.ekle(k.to_maliyet_kalemi())
        if kanal_yaml:
            defter.ekle_hepsi(blocked_envanterinden_kalemler(kanal_yaml))
        defter.ekle_hepsi(_bilincli_haric_kalemler())
    except Exception as exc:                       # DefterCiftKayit / FixtureSizintisi
        s.status = "UNKNOWN"
        s.eksik_girdiler.append(f"KALEM DEFTERI REDDETTI: {exc}")
        return s

    s.defter = defter
    s.damga_ozeti = defter.damga_ozeti()
    for k, eksik in defter.bloke_kalemler():
        s.blocked_input.append(
            f"{k.kalem_kimligi}: BLOCKED_INPUT (eksik alan: {', '.join(eksik)})"
            + (f" | sahibi={k.sahibi}" if k.sahibi else "")
            + (f" | ticket={k.ticket}" if k.ticket else "")
        )
    for k in defter.haric_kalemler():
        s.excluded_with_reason.append(
            f"{k.kalem_kimligi}: EXCLUDED_WITH_REASON — {k.haric_gerekce}"
        )
    sert = defter.hard_blocker_var_mi()
    if sert:
        s.status = "UNKNOWN"
        s.eksik_girdiler.extend(f"HARD BLOCKED_INPUT: {x}" for x in sert)
        return s

    toplam_l5 = defter.toplam_dusulen()
    for k in l5_kalemleri:
        if k.evidence_id and k.tutar_try is not None and k.para_birimi == "TRY":
            s.kullanilan_evidence_ids.append(k.evidence_id)
        if k.para_birimi not in (None, "TRY") and k.dusuldu_mu:
            s.uyarilar.append(
                f"L5 kalemi '{k.ad}' {k.para_birimi} cinsindendir; makro.yaml/fx "
                f"null oldugu icin TRY'ye CEVRILEMEDI -> BLOCKED_INPUT (T-912). "
                f"0 SAYILMAMISTIR; hesaba HIC GIRMEMISTIR. Yon: YUKARI SAPTIRIR."
            )
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

    # --- md.36 KOŞULLU KDV KİLİDİ (T-171) — MAKTU, BÖLMEDEN ÖNCE ------
    tetik, md36_kdv, md36_uyari, md36_bloke = md36_indirilemeyen_kdv_oku(vergi_yaml)
    s.md36_tetiklendi_mi = tetik
    s.uyarilar.extend(md36_uyari)
    s.blocked_input.extend(md36_bloke)
    if md36_bloke or md36_kdv is None:
        s.status = "UNKNOWN"
        s.eksik_girdiler.extend(md36_bloke)
        return s
    s.md36_indirilemeyen_kdv = md36_kdv

    A, bolundu = r7_coz(s.l4_econ_max, s.otv_try, s.kkdf_try, x_pre, g, r7_sira,
                        md36_indirilemeyen_kdv=md36_kdv)
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
    # ---- GÖZETİM — TUR 3A: ESKİ UYARI METNİ YÜRÜRLÜKTEN KALKTI (T-171)
    #
    # ESKI (YANLIS, KALDIRILDI):
    #   "gozetim esigi dogrulanmamistir; cif_try_max BIR ALT SINIRLA TEST
    #    EDILMEMISTIR"
    # YENI: metin `vergi.yaml -> ...gozetim_ters_model_mantigi.cikti_kurali`
    # alanindan OKUNUR; koda GOMULMEZ.
    goz = ((vergi_yaml.get("ters_model_vergi_bacagi") or {})
           .get("gozetim_ters_model_mantigi") or {})
    esik_blok = goz.get("gozetim_esigi") or {}
    esik_status = str(esik_blok.get("status") or "")
    kural = str(goz.get("cikti_kurali") or "").strip()
    if esik_status == "N/A":
        s.uyarilar.append(
            "GOZETIM (TUR 3A, POZITIF TARAMA): " + (kural or
            "2204.21 icin gozetim/korunma onlemi/dampinge karsi vergi TARANMIS VE "
            "BULUNMAMISTIR. cif_try_max uzerinde HUKUKI BIR ALT SINIR YOKTUR.")
        )
        s.etiketler.append("GOZETIM_ALT_SINIRI_YOK (N/A, EV-2026-08-10-860)")
    elif esik_blok.get("value") is None:
        s.uyarilar.append(
            "GOZETIM: esik dogrulanmamistir (null/UNKNOWN). cif_try_max BIR ALT "
            "SINIRLA TEST EDILMEMISTIR."
        )
    s.uyarilar.append(f"X_pre = {x_pre} TL/sise alinmistir (vergi.yaml X_pre.cikti_kurali).")

    # ---- ÇIKTI DAMGASI (GÖREV 1) --------------------------------------
    if s.blocked_input:
        s.status = "DRAFT_" + s.status + "_BLOCKED_INPUT"
        s.etiketler.append(
            f"BLOCKED_INPUT: {len(s.blocked_input)} kalem. Bu kalemler 0 "
            f"SAYILMAMISTIR; hesaba HIC GIRMEMISTIR. Cikti DRAFT'tir ve "
            f"APPROVED OLAMAZ (CLAUDE.md §5 gate kurali)."
        )
    return s
