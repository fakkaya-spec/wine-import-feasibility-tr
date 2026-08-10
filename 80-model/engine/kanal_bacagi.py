"""
kanal_bacagi.py — KANAL BACAĞI (K1..K6) + `R8-K` ROUND-TRIP

===========================================================================
 KAYNAK SPESİFİKASYON (kod değil, sözleşme)
===========================================================================
  70-kanal/kanal-katman-matrah-haritasi.md §9    (kapalı formül seti K1..K6)
  70-kanal/kanal-katman-matrah-haritasi.md §9.1  (DOĞRU `R8-K`)
  70-kanal/kanal-bacagi-hata-listesi.md   K1..K12
  80-model/inputs/kanal.yaml -> merdiven_denklemi.tur3a_duzeltilmis_ileri
  99-ops/tickets/T-619.md                        (⛔ `T-942`'nin `R8-K`'sı TERSTEN ÇALIŞIR)

===========================================================================
 ⛔ T-619 — BU DOSYANIN VAR OLMA SEBEBİ
===========================================================================
`T-942` (CRITICAL, teşhisi DOĞRU) kanal bacağında hiçbir otomatik doğrulama
olmadığını gösterdi. Ama önerdiği assertion'ın `K1` adımı **etiket
hatalıdır**:

    T-942:  L6_geri = L5_max + mu*L6          <-- YANLIS ETIKET

`L5_max + mu·L6` ifadesi `L6`'ya değil **`L7_eff`**'e eşittir. `L6`
etiketiyle devam edilince bir sonraki adımda `×(1−d) − f` **ikinci kez**
uygulanır ve assertion **tersine döner**:

    DOGRU formul (L5_max = L7_eff)  -> 735,08 TL uretir -> REDDEDILIR
    NAIF  formul (L5_max = L6)      -> 799,00 TL uretir -> KABUL EDILIR

Yani birebir kodlansaydı `R5` düzeltmesini geri alır ve −28,95 TL'lik hatayı
"test edilmiş" damgasıyla MÜHÜRLERDİ.

**DOĞRU GERİ İNŞA (bu dosyada uygulanan):**

    K1'  L7_eff_geri = L5_max + mu_kesintisi + m_dist_kesintisi + iade_kaybi
    K2'  L8_net_geri = L7_eff_geri / (1 - m)        [HORECA: * k]
    K3'  L8_geri     = L8_net_geri * (1 + v)
    assert | L8_geri - L8_gross | < 0,01

**`L6` bu zincirde HİÇ KULLANILMAZ.** `L6` yalnızca (i) `d`'nin matrahı ve
(ii) `L6_gross` üzerinden alacak/vade hesabı için gereklidir.

===========================================================================
 GERİ İNŞA GERÇEKTEN BAĞIMSIZDIR
===========================================================================
`R8-K`, ileri yönde hesaplanmış HİÇBİR ara değeri (ne `L6`, ne `L7_eff`)
yeniden kullanmaz. `L5_max` ve kanal parametrelerinden `L7_eff`'i CEBİRSEL
OLARAK ÇÖZER. Aksi hâlde test kendi kendini doğrular ve hiçbir şey kanıtlamaz.
===========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any

SIFIR = Decimal("0")
BIR = Decimal("1")

# μ'nun matrah seçenekleri — kanal.yaml/dagitim_modeli.importer_katki_matrahi
MU_MATRAH_L6 = "L6"
MU_MATRAH_L7 = "L7_EFF"
MU_MATRAH_L5_MARKUP = "L5_MARKUP"
MU_MATRAHLARI = (MU_MATRAH_L6, MU_MATRAH_L7, MU_MATRAH_L5_MARKUP)


# ---------------------------------------------------------------------------
# PARAMETRE SÖZLEŞMESİ
# ---------------------------------------------------------------------------

@dataclass
class KanalParametreleri:
    """
    Kanal bacağının TAM parametre seti (`kanal-katman-matrah-haritasi.md` §9).

    ⛔ `f_per_bottle` BİR GİRDİ DEĞİLDİR (K7). Girdi `F_total` + `Q_ithal`'dir.
    ⛔ `d` tek homojen skaler DEĞİLDİR (K8). `d_var` + `D_fix_total` ayrıdır.
    ⛔ `Q_ithal != Q_satilan` (K11).
    """

    kanal_kodu: str                          # CHAIN_RETAIL | INDEPENDENT_TEKEL | HORECA
    v: Decimal                               # KDV oranı (vergi.yaml — R1)
    m: Decimal | None = None                 # margin ON SELLING PRICE
    k: Decimal | None = None                 # HoReCa çarpanı (matrah L7_eff)

    d_var: Decimal = SIFIR                   # GERÇEKTEN ciroya oranlı bileşenler
    d_var_unknown_sifir_alindi: bool = False

    F_total: Decimal | None = None           # listeleme bedeli — DÖNEM TOPLAMI
    F_total_kdv_dahil_mi: str | None = None  # K10 / TVK-N3 — mutlak tutar => ZORUNLU
    D_fix_total: Decimal | None = None       # d sepetinin SABIT bileşenleri (dönem)
    D_fix_kdv_dahil_mi: str | None = None
    Q_ithal: Decimal | None = None           # ithal edilen şişe (SABİTLER BUNA BÖLÜNÜR)

    r_iade: Decimal | None = None            # iade/fire oranı
    geri_kazanilabilir_deger: Decimal | None = None   # iade edilen şişenin değeri

    mu: Decimal = SIFIR                      # ithalatçı katkı payı
    mu_matrahi: str | None = None            # L6 | L7_EFF | L5_MARKUP

    m_dist: Decimal = SIFIR                  # dış distribütör marjı (matrah L6)
    dagitim_modeli: str = "MODEL_B"          # MODEL_A (dış dist.) | MODEL_B (kendi)
    d_kimde: str | None = None               # BIZDE | DISTRIBUTORDE (MODEL_A'da ZORUNLU)

    odeme_vadesi_gun: Decimal | None = None
    finansman_orani_yillik: Decimal | None = None     # makro.yaml — bugün null


@dataclass
class KanalSonuc:
    hesaplandi: bool = False
    status: str = "UNKNOWN"
    l8_gross: Decimal | None = None
    l8_net: Decimal | None = None
    l7_eff: Decimal | None = None
    l6: Decimal | None = None
    l6_gross: Decimal | None = None          # ALACAK TUTARI (K12a)
    l5_max: Decimal | None = None
    f_per_bottle: Decimal | None = None
    d_fix_per_bottle: Decimal | None = None
    q_satilan: Decimal | None = None
    mu_kesintisi: Decimal = SIFIR
    m_dist_kesintisi: Decimal = SIFIR
    iade_kaybi: Decimal = SIFIR
    bayraklar: list[str] = field(default_factory=list)
    bloke_girdiler: list[str] = field(default_factory=list)   # BLOCKED_INPUT
    uyarilar: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# K3 — f_per_bottle TÜREVDİR (K7 / SCALE_MONOTONICITY / TVK-P4)
# ---------------------------------------------------------------------------

def toplam_bolu_hacim(
    toplam: Decimal | None, q: Decimal | None, ad: str
) -> tuple[Decimal | None, list[str]]:
    """`TOTAL -> PER_BOTTLE` geçişi. TEK YOL BUDUR; sabit girdi kabul edilmez."""
    if toplam is None:
        return None, [f"{ad}: DONEM TOPLAMI (TOTAL) UNKNOWN -> per_bottle TURETILEMEZ"]
    if q is None or q <= 0:
        return None, [f"{ad}: Q_ithal yok/0 -> per_bottle TURETILEMEZ"]
    return toplam / q, []


# ---------------------------------------------------------------------------
# μ KESİNTİSİ — matraha göre (K5 / TVK-P1/P2/P3)
# ---------------------------------------------------------------------------

def mu_kesintisi_hesapla(
    mu: Decimal, matrah: str | None, l7_eff: Decimal, l6: Decimal
) -> tuple[Decimal | None, str | None]:
    if mu == 0:
        # μ=0'da üç matrah da AYNI sonucu verir; matrah seçimi ANLAMSIZDIR.
        return SIFIR, None
    if matrah is None:
        return None, (
            "importer_katki_matrahi = null VE mu != 0 -> UNKNOWN. Engine "
            "VARSAYILANA DUSMEZ (kanal.yaml/dagitim_modeli.importer_katki_matrahi"
            ".engine_kurali, K5, T-616)."
        )
    if matrah == MU_MATRAH_L6:
        return mu * l6, None
    if matrah == MU_MATRAH_L7:
        return mu * l7_eff, None
    if matrah == MU_MATRAH_L5_MARKUP:
        return l7_eff * (BIR - BIR / (BIR + mu)), None
    return None, f"importer_katki_matrahi='{matrah}' TANINMIYOR -> UNKNOWN"


# ---------------------------------------------------------------------------
# İLERİ YÖN — K1..K6
# ---------------------------------------------------------------------------

def kanal_ileri(l8_gross: Decimal, p: KanalParametreleri) -> KanalSonuc:
    """
    `L8_gross` -> `L5_max`  (kanal-katman-matrah-haritasi.md §9)

    K1  L8_net       = L8_gross / (1+v)
    K2  L7_eff       = L8_net*(1-m)      [CHAIN/TEKEL]  |  L8_net/k  [HORECA]
    K3  f_per_bottle = F_total / Q_ithal                 <-- TUREV
    K4  L6           = (L7_eff + f + D_fix/Q) / (1-d_var)
    K5  L5_max       = L7_eff - mu_kes - m_dist_kes - iade_kaybi
    K6  L6_gross     = L6*(1+v)
    """
    s = KanalSonuc()
    s.l8_gross = l8_gross

    # ---- K1 : zincirdeki TEK KDV bölmesi ------------------------------
    s.l8_net = l8_gross / (BIR + p.v)

    # ---- K2 : marj / çarpan -------------------------------------------
    if p.kanal_kodu == "HORECA":
        if p.k is None or p.k == 0:
            s.bloke_girdiler.append("k_horeca: BLOCKED_INPUT (eksik alan: value)")
            return s
        s.l7_eff = s.l8_net / p.k
        s.uyarilar.append(
            "HoReCa: carpan KDV HARIC L7_eff uzerine uygulanmistir (matrah L7_eff). "
            "MENU KDV ORANI vergi.yaml URUN oranidir ve DOGRULANMAMISTIR -> "
            "B-2 / T-612 BLOCKED."
        )
        s.bloke_girdiler.append(
            "horeca_menu_kdv_orani: BLOCKED_INPUT (eksik alan: basis/tax_treatment) "
            "| sahibi=gumruk-vergi-uzmani | ticket=T-612"
        )
    else:
        if p.m is None:
            s.bloke_girdiler.append("m_retail: BLOCKED_INPUT (eksik alan: value)")
            return s
        s.l7_eff = s.l8_net * (BIR - p.m)

    # ---- K3 : f ve D_fix TÜREVDİR (K7, K8) ----------------------------
    f_pb, f_uy = toplam_bolu_hacim(p.F_total, p.Q_ithal, "F_total (listeleme bedeli)")
    if p.F_total is not None and p.F_total_kdv_dahil_mi in (None, ""):
        # K10 / TVK-N3 — mutlak tutarli kalemde KDV tabani ZORUNLU
        s.bloke_girdiler.append(
            "F_total.kdv_dahil_mi: BLOCKED_INPUT (eksik alan: kdv_dahil_mi) | "
            "HARD | ticket=T-611 | K10"
        )
        s.status = "UNKNOWN"
        return s
    if f_pb is None:
        s.bloke_girdiler.append(
            "f_listeleme_bedeli: BLOCKED_INPUT (eksik alan: tutar_try/F_total) | "
            "sahibi=kanal-marj-uzmani | ticket=T-604 | yon=ASAGI (K7: 5k->100k'da 38,00 TL)"
        )
        s.uyarilar.extend(f_uy)
        f_pb = SIFIR   # hesap devam eder ama CIKTI DAMGALIDIR

    d_pb, d_uy = toplam_bolu_hacim(p.D_fix_total, p.Q_ithal, "D_fix (d sepetinin SABIT kismi)")
    if p.D_fix_total is not None and p.D_fix_kdv_dahil_mi in (None, ""):
        s.bloke_girdiler.append(
            "D_fix.kdv_dahil_mi: BLOCKED_INPUT (eksik alan: kdv_dahil_mi) | HARD | K10"
        )
        s.status = "UNKNOWN"
        return s
    if d_pb is None:
        s.bloke_girdiler.append(
            "D_fix_sabit_bilesenler: BLOCKED_INPUT (eksik alan: tutar_try/D_fix_total) | "
            "sahibi=kanal-marj-uzmani | ticket=T-613 | yon=ASAGI (K8)"
        )
        s.uyarilar.extend(d_uy)
        d_pb = SIFIR

    s.f_per_bottle, s.d_fix_per_bottle = f_pb, d_pb

    # ---- K4 : L6 (FATURA fiyati — L5 BUTCESI DEGILDIR) ----------------
    if p.d_var >= 1:
        s.bloke_girdiler.append("d_var >= 1 -> L6 TANIMSIZ")
        return s
    F = f_pb + d_pb
    s.l6 = (s.l7_eff + F) / (BIR - p.d_var)
    s.l6_gross = s.l6 * (BIR + p.v)          # K6 / K12a — ALACAK TUTARI

    # ---- MODEL A kilidi (K6d / TVK-N6) --------------------------------
    if p.dagitim_modeli == "MODEL_A":
        if p.d_kimde in (None, ""):
            s.bloke_girdiler.append(
                "d_kimde: BLOCKED_INPUT (eksik alan: value) | HARD | "
                "ticket=T-617 | C-611 | A1/A2 secimi olmadan MODEL A KOSULAMAZ"
            )
            s.status = "UNKNOWN"
            return s
        if p.d_kimde == "DISTRIBUTORDE" and p.d_var > 0:
            s.bloke_girdiler.append(
                "CIFT_SAYIM: d_kimde=DISTRIBUTORDE iken d_var>0 -> ayni bedel iki "
                "kez dusuluyor (K6d / LEDGER_UNIQUENESS)"
            )
            s.status = "UNKNOWN"
            return s

    # ---- K5 : L5_max ---------------------------------------------------
    mu_kes, mu_hata = mu_kesintisi_hesapla(p.mu, p.mu_matrahi, s.l7_eff, s.l6)
    if mu_kes is None:
        s.bloke_girdiler.append(f"importer_katki_matrahi: BLOCKED_INPUT | HARD | {mu_hata}")
        s.status = "UNKNOWN"
        return s
    s.mu_kesintisi = mu_kes
    if p.mu == 0:
        s.uyarilar.append(
            "mu = 0 -> importer_katki_matrahi (L6/L7_EFF/L5_MARKUP) SONUCU "
            "DEGISTIRMEZ; ucu de ayni sayiyi verir. Cikti MAXIMUM STRUCTURAL "
            "BUY PRICE'tir, bir HEDEF ALIS FIYATI DEGILDIR."
        )

    # Distribütör marjı: matrah L6 (ciro) — `kanal.yaml/dis_distributor.marj_matrahi`
    # SPEC_DECISION. μ ile ÖZDEŞ DEĞİLDİR (T-617 / C-611) ve TOPLANMAZ.
    s.m_dist_kesintisi = p.m_dist * s.l6

    # ---- iade kaybı (K11 / B-11) ---------------------------------------
    if p.r_iade is None:
        s.iade_kaybi = SIFIR
        s.q_satilan = p.Q_ithal
        s.bayraklar.append("FIRE_SIFIR_VARSAYILDI")
        s.bloke_girdiler.append(
            "iade_orani_r: BLOCKED_INPUT (eksik alan: tutar_try) | ticket=T-615 | "
            "yon=ASAGI (K11: r=%5'te -19,38 TL)"
        )
    else:
        if p.geri_kazanilabilir_deger is None:
            s.bloke_girdiler.append(
                "geri_kazanilabilir_deger: BLOCKED_INPUT (eksik alan: tutar_try) | "
                "ticket=T-615 | B-11 -> 0 ALINMADI, UST SINIR olarak isaretlendi"
            )
            geri = SIFIR
            s.bayraklar.append("IADE_GERI_KAZANIM_UST_SINIR")
        else:
            geri = p.geri_kazanilabilir_deger
        s.iade_kaybi = p.r_iade * (s.l6 - geri)
        s.q_satilan = (p.Q_ithal * (BIR - p.r_iade)) if p.Q_ithal is not None else None

    s.l5_max = s.l7_eff - s.mu_kesintisi - s.m_dist_kesintisi - s.iade_kaybi

    # ---- K12b : vade finansmani ----------------------------------------
    if p.odeme_vadesi_gun and p.odeme_vadesi_gun > 0 and p.finansman_orani_yillik is None:
        s.bayraklar.append("VADE_MALIYETI_MODELLENMEDI")
        s.bloke_girdiler.append(
            "vade_finansman_maliyeti: BLOCKED_INPUT (eksik alan: tutar_try) | "
            "makro.yaml/finansman_orani null | ticket=T-614 | "
            "yon=ASAGI (K12: 60g -27,55 TL) | MATRAH = L6_gross (L6 DEGIL)"
        )

    s.hesaplandi = True
    s.status = "OK" if not s.bloke_girdiler else "DRAFT_BLOCKED_INPUT"
    return s


# ---------------------------------------------------------------------------
# ⛔ `R8-K` — DOĞRU GERİ İNŞA  (T-619)
# ---------------------------------------------------------------------------

def kanal_geri_insa(l5_max: Decimal, p: KanalParametreleri) -> tuple[Decimal | None, list[str], str | None]:
    """
    `L5_max` -> `L8_gross`   (SADECE `L5_max` + parametrelerden; ileri yönde
    hesaplanan HİÇBİR ara değer yeniden kullanılmaz).

    Cebir:
        L6      = (L7 + F)/(1-d)                     ; F = f + D_fix/Q
        mu_kes  = mu*L6 | mu*L7 | L7*mu/(1+mu)
        md_kes  = m_dist*L6
        iade    = r*(L6 - G)
        L5_max  = L7 - mu_kes - md_kes - iade
                = L7*(1 - A) - B
      =>  L7    = (L5_max + B)/(1 - A)

    K2'  L8_net = L7/(1-m)   [CHAIN/TEKEL]   |   L7*k   [HORECA]
    K3'  L8     = L8_net*(1+v)
    """
    adimlar: list[str] = []

    if p.d_var >= 1:
        return None, adimlar, "K1': d_var >= 1 -> geri insa TANIMSIZ"

    f_pb, _ = toplam_bolu_hacim(p.F_total, p.Q_ithal, "F_total")
    d_pb, _ = toplam_bolu_hacim(p.D_fix_total, p.Q_ithal, "D_fix")
    F = (f_pb or SIFIR) + (d_pb or SIFIR)

    c1 = BIR / (BIR - p.d_var)          # L6 = c1*L7 + c0
    c0 = F / (BIR - p.d_var)

    # A : L7 katsayısı ; B : sabit terim
    A = SIFIR
    B = SIFIR

    if p.mu != 0:
        if p.mu_matrahi is None:
            return None, adimlar, "K1': mu != 0 ve mu_matrahi null -> UNKNOWN"
        if p.mu_matrahi == "L6":
            A += p.mu * c1
            B += p.mu * c0
        elif p.mu_matrahi == "L7_EFF":
            A += p.mu
        elif p.mu_matrahi == "L5_MARKUP":
            A += p.mu / (BIR + p.mu)
        else:
            return None, adimlar, f"K1': mu_matrahi='{p.mu_matrahi}' TANINMIYOR"

    if p.m_dist != 0:
        A += p.m_dist * c1
        B += p.m_dist * c0

    if p.r_iade:
        G = p.geri_kazanilabilir_deger or SIFIR
        A += p.r_iade * c1
        B += p.r_iade * (c0 - G)

    if A == 1:
        return None, adimlar, "K1': (1 - A) = 0 -> geri insa TANIMSIZ"

    l7 = (l5_max + B) / (BIR - A)
    adimlar.append(f"K1' L7_eff_geri = ({l5_max} + {B}) / (1 - {A}) = {l7}")

    if p.kanal_kodu == "HORECA":
        if p.k is None or p.k == 0:
            return None, adimlar, "K2': k_horeca yok"
        l8_net = l7 * p.k          # ⚠ T-619 kriter #3: `/k` DEGIL `*k`
        adimlar.append(f"K2' L8_net_geri = L7_eff_geri * k = {l7} * {p.k} = {l8_net}")
    else:
        if p.m is None:
            return None, adimlar, "K2': m_retail yok"
        if p.m >= 1:
            return None, adimlar, "K2': m >= 1 -> TANIMSIZ"
        l8_net = l7 / (BIR - p.m)
        adimlar.append(f"K2' L8_net_geri = L7_eff_geri / (1 - m) = {l7} / {BIR - p.m} = {l8_net}")

    l8 = l8_net * (BIR + p.v)
    adimlar.append(f"K3' L8_geri = L8_net_geri * (1 + v) = {l8}")
    return l8, adimlar, None


def r8k_roundtrip(
    l8_gross: Decimal,
    l5_max: Decimal,
    p: KanalParametreleri,
    tolerans: Decimal = Decimal("0.01"),
) -> tuple[bool, Decimal | None, list[str], str | None]:
    """
    `R8-K` — kanal round-trip assertion. `R8`'in (vergi bacağı) kanal karşılığı.
    Dönüş: (gecti_mi, fark, adim_izleri, tutmayan_adim)
    """
    l8_geri, adimlar, hata = kanal_geri_insa(l5_max, p)
    if l8_geri is None:
        return False, None, adimlar, hata or "K1'"
    fark = abs(l8_geri - l8_gross)
    if fark < tolerans:
        return True, fark, adimlar, None
    return False, fark, adimlar, "K1'..K3' zinciri (L5_max <-> L8_gross tutmuyor)"


# ---------------------------------------------------------------------------
# ⛔⛔ NEGATİF VEKTÖR — `T-942`'nin BİREBİR SPESİFİKASYONU
# ---------------------------------------------------------------------------

def R8K_T942_BIREBIR_HATALI_ASLA_URETIMDE_KULLANMA(
    l8_gross: Decimal, l5_max: Decimal, p: KanalParametreleri
) -> tuple[bool, Decimal]:
    """
    ⛔⛔⛔ BU FONKSİYON BİR **NEGATİF TEST VEKTÖRÜDÜR** (`TVK-N1b`, `T-619`).
    ÜRETİMDE ÇAĞRILMAZ. Yalnızca `T-942`'nin önerdiği assertion'ın
    **tersten çalıştığını** kalıcı olarak kanıtlamak için durur; böylece
    gelecekte biri aynı spesifikasyonu yeniden yazarsa test KIRILIR.

        T-942 K1 : L6_geri     = L5_max + mu*L6        <-- ETIKET YANLIS
        T-942 K2 : L7_eff_geri = L6_geri*(1-d) - f     <-- (1-d), f IKINCI KEZ
        T-942 K3 : L8_net_geri = L7_eff_geri/(1-m)
        T-942 K4 : L8_geri     = L8_net_geri*(1+v)
    """
    f_pb, _ = toplam_bolu_hacim(p.F_total, p.Q_ithal, "F_total")
    d_pb, _ = toplam_bolu_hacim(p.D_fix_total, p.Q_ithal, "D_fix")
    F = (f_pb or SIFIR) + (d_pb or SIFIR)

    l6_geri = l5_max                      # mu=0 halinde T-942'nin K1'i budur
    if p.mu != 0 and p.mu_matrahi == "L6":
        # T-942 "mu'nun matrahina gore cozulur" der; L6 matrahinda kapali form:
        l6_geri = l5_max / (BIR - p.mu)
    l7_geri = l6_geri * (BIR - p.d_var) - F
    if p.kanal_kodu == "HORECA":
        l8_net_geri = l7_geri * (p.k or BIR)
    else:
        l8_net_geri = l7_geri / (BIR - (p.m or SIFIR))
    l8_geri = l8_net_geri * (BIR + p.v)
    return abs(l8_geri - l8_gross) < Decimal("0.01"), l8_geri


# ---------------------------------------------------------------------------
# KARMA — birleşik çıktı kilidi (K9c / TVK-N7)
# ---------------------------------------------------------------------------

def kanala_ozgu_bloke_kalemler(kanal_kodu: str) -> list[str]:
    """
    `kanal-katman-matrah-haritasi.md` §4.2 — "T-856'nın gerçek cevabı: BİR
    SIFIR DEĞİL, ÜÇ SIFIR".

    Tekel kanalında `d`'nin hukuki karşılığı YOKTUR; yükü ÜÇ AYRI SATIRA
    düşer ve üçü de modelde `0`'dır. HoReCa'da dördüncü bir satır (aktivasyon)
    daha vardır. Bu satırlar `d = 0` yazıldığı için bugüne kadar GÖRÜNMEZDİ.

    Bu fonksiyon SAYI ÜRETMEZ — yalnızca eksik satırların ADINI verir.
    """
    if kanal_kodu == "INDEPENDENT_TEKEL":
        return [
            "tekel_net_fiyat_iskontosu: BLOCKED_INPUT (eksik alan: tutar_try) | "
            "EV-2026-08-10-610 | d'nin tekeldeki KARSILIGI | yon=ASAGI",
            "tekel_kilcal_dagitim_maliyeti: BLOCKED_INPUT (eksik alan: tutar_try) | "
            "EV-2026-08-10-613 (48.956 nokta) | yon=ASAGI",
            "tekel_supheli_alacak_karsiligi: BLOCKED_INPUT (eksik alan: tutar_try) | "
            "matrah = L6_gross * p_temerrut | yon=ASAGI",
        ]
    if kanal_kodu == "HORECA":
        return [
            "horeca_yatirim_destegi: BLOCKED_INPUT (eksik alan: tutar_try) | "
            "EV-2026-08-10-615 | KARMA (d gibi + f gibi) | B-12",
            "horeca_kilcal_dagitim_maliyeti: BLOCKED_INPUT (eksik alan: tutar_try) | yon=ASAGI",
            "horeca_supheli_alacak_karsiligi: BLOCKED_INPUT (eksik alan: tutar_try) | yon=ASAGI",
            "horeca_aktivasyon_tadim: BLOCKED_INPUT (eksik alan: layer/basis) | "
            "IP-2001 | T-604 | B-12",
        ]
    return []


def karma_gecerli_mi(kanal_yaml: dict[str, Any]) -> tuple[bool, str]:
    km = kanal_yaml.get("kanal_karmasi") or {}
    alanlar = ("zincir_market_pay_pct", "tekel_bayi_pay_pct", "horeca_pay_pct")
    paylar = []
    for a in alanlar:
        blok = km.get(a) or {}
        v = blok.get("value") if isinstance(blok, dict) else None
        if v is None:
            return False, (
                f"KARMA_UNKNOWN: kanal_karmasi.{a} = null -> BIRLESIK (blended) "
                f"CIKTI URETILMEZ. Yalniz kanal bazinda cikti verilir (K9c)."
            )
        paylar.append(Decimal(str(v)))
    if sum(paylar) != Decimal("100"):
        return False, f"KARMA_UNKNOWN: sum(paylar) = {sum(paylar)} != 100 (K9c assertion)"
    return True, "KARMA OK"
