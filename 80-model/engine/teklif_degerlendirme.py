"""
teklif_degerlendirme.py — QUOTE INGESTION + QUOTE EVALUATION  (TUR 3.25 §12/§13)

===========================================================================
 NE YAPAR
===========================================================================
  1) `inputs/quote-ingestion-schema.yaml` semasini okur ve icindeki
     `dogrulama_kurallari` listesini CALISTIRIR (kurallar VERI'dir, kod degil).
  2) Gelen teklifi (belge + N kademe) sinif-lar: FIRM_QUOTE / B2B_INDICATIVE /
     PUBLIC_INDICATIVE. Beyan edilen sinif etkin sinifi YUKSELTEMEZ.
  3) `outputs/country-buying-ceilings.csv`den TARGET CEILING bandini (X/Y)
     okur — hicbir tavan bu dosyaya HARD-CODE EDILMEZ.
  4) `inputs/makro.yaml`dan dort FX eksenini okur (FX_0 / FX_UP_10 /
     FX_UP_20 / FX_DOWN_10) ve teklifi DORT EKSENDE AYRI AYRI cevirir.
  5) Her (kademe x fx_ekseni) icin DORT sonuctan birini uretir:
     STRONG · NEGOTIATE · ABOVE_CEILING · INCOMPLETE

===========================================================================
 ⛔ RET YASAGI — KODA GOMULU
===========================================================================
  Yatirimci nihai marj esigi YOKTUR (`OQ-901` / `T-851`, CRITICAL, OPEN).
  Esik olmadan "kabul edilemez" DENEMEZ. Bu nedenle:
    - `SONUC_DEGERLERI` DORT elemanlidir; besinci deger yoktur.
    - `YASAKLI_SONUCLAR` icindeki her ifade `YasakliSonuc` firlatir.
    - `retmek()` fonksiyonu CAGRILDIGI AN istisna firlatir; govdesi yoktur.
  `ABOVE_CEILING` bir GOZLEMDIR: "teklif, DRAFT ust-sinir modelinin Y bandinin
  ustundedir". Tedarikcinin elenmesi DEGILDIR.

===========================================================================
 ⛔ INTERNAL_ONLY
===========================================================================
  Tavan, sonuc degeri ve kur ekseni TEDARIKCIYE GOSTERILMEZ.
    - internal cikti: `80-model/outputs/INTERNAL_ONLY-*` (ad zorunlu on ek)
    - tedarikciye giden metin: yalnizca EKSIK ALAN TALEBI
    - `disari_giden_metin_denetle()` sizinti taramasi ZORUNLU
    - `50-sourcing/`, `10-evidence/`, `99-ops/` ... bu modul tarafindan
      YAZILAMAZ (`YAZILAMAZ_DIZINLER`)

===========================================================================
 GUVENLIK KILIDI
===========================================================================
  - Bu dosyada hicbir vergi orani / OTV tutari / KDV orani / matrah tanimi
    YOKTUR. Tavanlar CSV'den, kurlar `makro.yaml`dan okunur.
  - Adinda `TEST_FIXTURE` gecen dosya uretim girdisi olarak OKUNAMAZ
    (`kalem_defteri.guvenli_girdi_yukle`).
  - Girdi yoksa UYDURULMAZ: sonuc `INCOMPLETE` + `BLOCKED_INPUT` listesi.

Calistirma:  python3 80-model/engine/teklif_degerlendirme.py
"""

from __future__ import annotations

import csv
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from kalem_defteri import (  # noqa: E402
    DAMGA_BLOCKED,
    DAMGA_OK,
    MaliyetKalemi,
    guvenli_girdi_yukle,
)

D = Decimal

MODEL_KOK = Path(__file__).resolve().parent.parent          # 80-model
INPUTS = MODEL_KOK / "inputs"
OUTPUTS = MODEL_KOK / "outputs"

SEMA_DOSYASI = INPUTS / "quote-ingestion-schema.yaml"
MAKRO_DOSYASI = INPUTS / "makro.yaml"
TAVAN_CSV = OUTPUTS / "country-buying-ceilings.csv"


# ===========================================================================
# 0. SONUC ALFABESI + RET YASAGI
# ===========================================================================

SONUC_STRONG = "STRONG"
SONUC_NEGOTIATE = "NEGOTIATE"
SONUC_ABOVE = "ABOVE_CEILING"
SONUC_INCOMPLETE = "INCOMPLETE"

#: DORT deger. Besinci deger YOKTUR ve eklenemez.
SONUC_DEGERLERI: frozenset[str] = frozenset(
    {SONUC_STRONG, SONUC_NEGOTIATE, SONUC_ABOVE, SONUC_INCOMPLETE}
)

#: Bu ifadelerden herhangi biri bir sonuc alanina yazilmaya calisilirsa
#: `YasakliSonuc` firlatilir. (`OQ-901` / `T-851` acik oldugu surece.)
YASAKLI_SONUCLAR: frozenset[str] = frozenset(
    {
        "REJECTED", "REJECT", "RED", "REDDEDILDI", "KILL",
        "NOT_VIABLE", "NOTVIABLE", "VIABLE", "ELENDI",
        "APPROVED", "ONAYLANDI", "ACCEPT", "ACCEPTED", "KABUL",
    }
)

RET_YASAGI_GEREKCESI = (
    "Yatirimci nihai marj esigi YOK (OQ-901 / T-851, CRITICAL, OPEN). "
    "Esik olmadan bir teklif REDDEDILEMEZ. ABOVE_CEILING bir GOZLEMDIR, "
    "bir ret DEGILDIR."
)


class YasakliSonuc(RuntimeError):
    """Bir teklife ret/kabul hukmu verilmeye calisildi."""


class IcerideKalmaliHatasi(RuntimeError):
    """INTERNAL_ONLY bir bilgi disari giden bir metne sizdi."""


class KademeCiftKayit(RuntimeError):
    """Ayni (supplier|product|quote_date|tier_code) iki kez yuklendi."""


class TavanBulunamadi(RuntimeError):
    """Istenen tavan satiri country-buying-ceilings.csv icinde yok."""


def _sonuc_dogrula(deger: str) -> str:
    """Sonuc alanina yazilan HER deger buradan gecer."""
    yukari = str(deger).strip().upper()
    if yukari in YASAKLI_SONUCLAR:
        raise YasakliSonuc(
            f"'{deger}' bir sonuc degeri OLAMAZ. {RET_YASAGI_GEREKCESI} "
            f"Izinli degerler: {sorted(SONUC_DEGERLERI)}"
        )
    if yukari not in SONUC_DEGERLERI:
        raise YasakliSonuc(
            f"'{deger}' tanimli bir sonuc degeri degil. "
            f"Izinli degerler: {sorted(SONUC_DEGERLERI)}"
        )
    return yukari


def retmek(*_a: Any, **_k: Any) -> None:
    """
    ⛔ BU FONKSIYONUN GOVDESI YOKTUR VE OLMAYACAKTIR.
    Cagrildigi an istisna firlatir. Ret hukmu bu turda URETILEMEZ.
    """
    raise YasakliSonuc(
        "RET YASAGI: bu modul bir teklifi reddedemez. " + RET_YASAGI_GEREKCESI
    )


# ===========================================================================
# 1. INTERNAL_ONLY
# ===========================================================================

INTERNAL_ONLY_ON_EKI = "INTERNAL_ONLY-"

INTERNAL_ONLY_DAMGASI = (
    "<!-- ================================================================\n"
    "     INTERNAL_ONLY — TEDARIKCIYE GOSTERILMEZ\n"
    "     Icerik: TARGET CEILING (X/Y), sonuc degeri, MAX_CIF/MAX_FOB/MAX_EXW,\n"
    "     FX eksenleri. Bunlarin hicbiri bir taahhut degildir ve disariya\n"
    "     verilmesi pazarligi tersine cevirir.\n"
    "     ================================================================ -->"
)

#: Bu modul bu dizinlerin ALTINA hicbir sey yazamaz.
YAZILAMAZ_DIZINLER = ("50-sourcing", "10-evidence", "99-ops", "60-pazar",
                      "70-kanal", "30-vergi-gumruk", "40-lojistik")

#: Disari giden metinde bulunmasi YASAK olan izler.
SIZINTI_DESENLERI: tuple[tuple[str, str], ...] = (
    (r"MAX_CIF", "tavan adi"),
    (r"MAX_FOB", "tavan adi"),
    (r"MAX_EXW", "tavan adi"),
    (r"CEILING", "tavan adi"),
    (r"TAVAN", "tavan adi"),
    (r"INTERNAL_ONLY", "ic damga"),
    (r"\bSTRONG\b", "sonuc degeri"),
    (r"\bNEGOTIATE\b", "sonuc degeri"),
    (r"\bABOVE_CEILING\b", "sonuc degeri"),
    (r"\bINCOMPLETE\b", "sonuc degeri"),
    (r"FX_(0|UP_10|UP_20|DOWN_10)", "fx ekseni"),
    (r"MODEL_DERIVED", "epistemik damga"),
    (r"\b\d{3}[.,]\d{2}\b", "uc haneli ondalikli sayi (tavan izi)"),
    (r"TRY\s*/\s*si", "TL/sise ifadesi"),
)


def disari_giden_metin_denetle(metin: str) -> str:
    """
    Tedarikciye/dis dunyaya gidecek HER metin buradan gecer.
    Bir tek iz bulunursa `IcerideKalmaliHatasi` firlatilir.
    """
    bulunanlar: list[str] = []
    for desen, ad in SIZINTI_DESENLERI:
        m = re.search(desen, metin, flags=re.IGNORECASE)
        if m:
            bulunanlar.append(f"{ad}: '{m.group(0)}'")
    if bulunanlar:
        raise IcerideKalmaliHatasi(
            "SIZINTI: disari giden metinde INTERNAL_ONLY iz(ler)i var -> "
            + " | ".join(bulunanlar)
        )
    return metin


def internal_rapor_yaz(yol: str | Path, metin: str) -> Path:
    """
    Internal ciktiyi yazar. Uc kilit:
      (a) dosya adi `INTERNAL_ONLY-` ile BASLAMAK ZORUNDA,
      (b) hedef `80-model/outputs/` altinda olmak ZORUNDA,
      (c) `YAZILAMAZ_DIZINLER` altina yazilamaz.
    """
    p = Path(yol)
    if not p.name.startswith(INTERNAL_ONLY_ON_EKI):
        raise IcerideKalmaliHatasi(
            f"'{p.name}' INTERNAL_ONLY ciktisi olamaz: dosya adi "
            f"'{INTERNAL_ONLY_ON_EKI}' on ekiyle BASLAMALIDIR."
        )
    parcalar = set(p.resolve().parts)
    for yasak in YAZILAMAZ_DIZINLER:
        if yasak in parcalar:
            raise IcerideKalmaliHatasi(
                f"Bu modul '{yasak}/' altina YAZAMAZ (hedef: {p})."
            )
    if p.resolve().parent != OUTPUTS.resolve():
        raise IcerideKalmaliHatasi(
            f"INTERNAL_ONLY ciktisi yalnizca {OUTPUTS} altina yazilir (hedef: {p})."
        )
    if not metin.startswith("<!--") and INTERNAL_ONLY_DAMGASI not in metin:
        metin = INTERNAL_ONLY_DAMGASI + "\n" + metin
    p.write_text(metin, encoding="utf-8")
    return p


# ===========================================================================
# 2. FX EKSENLERI
# ===========================================================================

#: Eksen adlari carpanlarini TANIMLAR (FX_UP_10 = +%10). Bu bir kur TAHMINI
#: degildir; `negotiation translation sensitivity` eksenidir.
FX_EKSEN_CARPANLARI: dict[str, Decimal] = {
    "FX_DOWN_10": D("0.90"),
    "FX_0": D("1.00"),
    "FX_UP_10": D("1.10"),
    "FX_UP_20": D("1.20"),
}
FX_EKSEN_SIRASI = ("FX_DOWN_10", "FX_0", "FX_UP_10", "FX_UP_20")


@dataclass
class FXEkseni:
    kod: str
    usd_try: Decimal | None = None
    eur_try: Decimal | None = None
    status: str = "BLOCKED_INPUT"      # OBSERVED | SENSITIVITY_AXIS
    #                                    | DERIVED_FROM_OBSERVED | BLOCKED_INPUT
    kaynak: str = ""
    kur_tarihi: str | None = None
    evidence_id: str | None = None
    kur_tipi: str | None = None        # doviz_satis / doviz_alis — KARISTIRILAMAZ
    bayat_mi: bool = False             # ttl gecti mi

    def kur(self, para_birimi: str | None) -> Decimal | None:
        if not para_birimi:
            return None
        pb = para_birimi.strip().upper()
        if pb == "USD":
            return self.usd_try
        if pb == "EUR":
            return self.eur_try
        if pb == "TRY":
            return D("1")
        return None       # AUD/CLP/MDL/GBP: kur YOK -> BLOCKED (uydurulmaz)

    def hazir_mi(self) -> bool:
        return self.status != "BLOCKED_INPUT" and (
            self.usd_try is not None or self.eur_try is not None
        )


def _d(v: Any) -> Decimal | None:
    if v is None or v == "":
        return None
    try:
        return D(str(v))
    except Exception:
        return None


def fx_eksenleri_oku(makro: dict[str, Any]) -> tuple[dict[str, FXEkseni], list[str]]:
    """
    Dort FX eksenini `makro.yaml`dan okur. UC yol denenir, sirasiyla:

      1) `fx_eksenleri:` blogu (gumruk-vergi-uzmani acikca yazdiysa) —
         eksen basina usd_try/eur_try okunur, status OBSERVED.
      2) `fx.usd_try` / `fx.eur_try` GOZLENEN taban degeri —
         dort eksen TANIMLI carpanlarla TURETILIR (status DERIVED_FROM_OBSERVED).
         Bu bir tahmin degildir: eksen adinin kendisi carpani tanimlar.
      3) Hicbiri yoksa -> dort eksen de `BLOCKED_INPUT`, kur `None`.
         KUR UYDURULMAZ.

    Doner: (eksenler, eksik_girdiler)
    """
    eksikler: list[str] = []
    eksenler: dict[str, FXEkseni] = {}

    blok = (makro or {}).get("fx_eksenleri") or {}
    if isinstance(blok, dict) and any(k in blok for k in FX_EKSEN_CARPANLARI):
        for kod in FX_EKSEN_SIRASI:
            e = blok.get(kod) or {}
            usd, eur = _d(e.get("usd_try")), _d(e.get("eur_try"))
            eksenler[kod] = FXEkseni(
                kod=kod,
                usd_try=usd,
                eur_try=eur,
                status="OBSERVED" if (usd or eur) else "BLOCKED_INPUT",
                kaynak="makro.yaml -> fx_eksenleri",
                kur_tarihi=e.get("kur_tarihi"),
                evidence_id=e.get("evidence_id"),
            )
            if not (usd or eur):
                eksikler.append(f"makro.yaml/fx_eksenleri/{kod}: kur yok")
        return eksenler, eksikler

    fx = (makro or {}).get("fx") or {}
    taban_usd = _d((fx.get("usd_try") or {}).get("value"))
    taban_eur = _d((fx.get("eur_try") or {}).get("value"))
    if taban_usd is None and taban_eur is None:
        for kod in FX_EKSEN_SIRASI:
            eksenler[kod] = FXEkseni(
                kod=kod, status="BLOCKED_INPUT",
                kaynak="makro.yaml -> fx.* (null)",
            )
        eksikler.append(
            "makro.yaml -> fx.usd_try.value ve fx.eur_try.value ikisi de null "
            "(T-912 / T-852). Dort FX ekseninin dordu de BLOCKED_INPUT."
        )
        return eksenler, eksikler

    for kod in FX_EKSEN_SIRASI:
        c = FX_EKSEN_CARPANLARI[kod]
        eksenler[kod] = FXEkseni(
            kod=kod,
            usd_try=(taban_usd * c) if taban_usd is not None else None,
            eur_try=(taban_eur * c) if taban_eur is not None else None,
            status="DERIVED_FROM_OBSERVED",
            kaynak=f"makro.yaml -> fx.* (gozlenen) x {c} (eksen tanimi)",
            kur_tarihi=(fx.get("usd_try") or {}).get("kur_tarihi")
            or (fx.get("eur_try") or {}).get("kur_tarihi"),
            evidence_id=(fx.get("usd_try") or {}).get("evidence_id")
            or (fx.get("eur_try") or {}).get("evidence_id"),
        )
    if taban_usd is None:
        eksikler.append("makro.yaml -> fx.usd_try.value null (USD teklifler cevrilemez)")
    if taban_eur is None:
        eksikler.append("makro.yaml -> fx.eur_try.value null (EUR teklifler cevrilemez)")
    return eksenler, eksikler


# ===========================================================================
# 3. TAVAN BANDI — CSV'DEN OKUNUR, HARD-CODE EDILMEZ
# ===========================================================================

#: Grup P (tercihli, KOSULLU) icin gumruk senaryosu / Grup N (tercihsiz) icin.
MENSE_GRUBU_GUMRUK = {
    "P": {"iyi": "DOC_OK", "kotu": "DOC_FAIL"},
    "N": {"iyi": "NO_PREFERENCE", "kotu": "NO_PREFERENCE"},
}

#: X ve Y koseleri — `rfq-negotiation-cards.md` §0.2 ile BIREBIR ayni tanim.
X_KOSESI = {"SCENARIO": "HIGH", "VOLUME_BOTTLES": "5000", "gumruk": "kotu"}
Y_KOSESI = {"SCENARIO": "BASE", "VOLUME_BOTTLES": "25000", "gumruk": "iyi"}


@dataclass
class TavanBandi:
    hedef_id: str
    kanal: str
    mense_grubu: str
    X_try: Decimal | None = None
    Y_try: Decimal | None = None
    sinif: str = "MODEL_DERIVED / UPPER_BOUND / DRAFT"
    kaynak: str = ""
    blocked_input_count: int = 0
    status_etiketi: str = ""
    eksikler: list[str] = field(default_factory=list)

    def hazir_mi(self) -> bool:
        return self.X_try is not None and self.Y_try is not None


def _csv_satirlari(yol: Path) -> list[dict[str, str]]:
    with yol.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def tavan_bandi_oku(
    hedef_id: str,
    kanal: str,
    mense_grubu: str,
    ulke: str | None = None,
    csv_yolu: Path = TAVAN_CSV,
) -> TavanBandi:
    """
    `country-buying-ceilings.csv`den X/Y bandini okur.
    Hicbir tavan bu dosyaya yazilmaz — hepsi CSV'den gelir.
    """
    grup = (mense_grubu or "N").upper()
    if grup not in MENSE_GRUBU_GUMRUK:
        grup = "N"      # bilinmiyorsa KOTUMSER band
    band = TavanBandi(hedef_id=hedef_id, kanal=kanal, mense_grubu=grup,
                      kaynak=f"{csv_yolu.name} (X: HIGH/5000, Y: BASE/25000)")
    if not csv_yolu.exists():
        band.eksikler.append(f"{csv_yolu} bulunamadi")
        return band

    satirlar = _csv_satirlari(csv_yolu)

    def bul(kose: dict[str, str]) -> dict[str, str] | None:
        gum = MENSE_GRUBU_GUMRUK[grup][kose["gumruk"]]
        for s in satirlar:
            if (
                s["TARGET_ID"] == hedef_id
                and s["CHANNEL"] == kanal
                and s["SCENARIO"] == kose["SCENARIO"]
                and s["CUSTOMS_SCENARIO"] == gum
                and s["VOLUME_BOTTLES"] == kose["VOLUME_BOTTLES"]
                and (ulke is None or s["COUNTRY"] == ulke)
            ):
                return s
        return None

    sx, sy = bul(X_KOSESI), bul(Y_KOSESI)
    if sx is None:
        band.eksikler.append(f"X kosesi satiri yok ({hedef_id}/{kanal}/{grup})")
    else:
        band.X_try = D(sx["MAX_CIF_TRY_UPPER_BOUND"])
        band.blocked_input_count = int(sx.get("BLOCKED_INPUT_COUNT") or 0)
        band.status_etiketi = sx.get("STATUS", "")
    if sy is None:
        band.eksikler.append(f"Y kosesi satiri yok ({hedef_id}/{kanal}/{grup})")
    else:
        band.Y_try = D(sy["MAX_CIF_TRY_UPPER_BOUND"])
    return band


def hacim_tavani_oku(
    hedef_id: str, kanal: str, mense_grubu: str, sise: int | None,
    csv_yolu: Path = TAVAN_CSV,
) -> tuple[Decimal | None, str]:
    """
    Kademenin KENDI hacmindeki tavan (BASE senaryo). Yoksa `None` + gerekce.
    ⛔ ARA DEGER URETILMEZ (interpolasyon yok). `V2 = 10.000` icin CSV'de
       satir YOKTUR -> `None` doner (`T-865`).
    """
    if sise is None:
        return None, "HACIM_BEYAN_EDILMEDI"
    grup = (mense_grubu or "N").upper()
    gum = MENSE_GRUBU_GUMRUK.get(grup, MENSE_GRUBU_GUMRUK["N"])["iyi"]
    if not csv_yolu.exists():
        return None, "TAVAN_CSV_YOK"
    for s in _csv_satirlari(csv_yolu):
        if (
            s["TARGET_ID"] == hedef_id
            and s["CHANNEL"] == kanal
            and s["SCENARIO"] == "BASE"
            and s["CUSTOMS_SCENARIO"] == gum
            and s["VOLUME_BOTTLES"] == str(int(sise))
        ):
            return D(s["MAX_CIF_TRY_UPPER_BOUND"]), "OK"
    return None, f"HACIM_KADEMESI_TAVANI_YOK({sise})"


# ===========================================================================
# 4. TEKLIF VERI YAPILARI
# ===========================================================================

SINIF_FIRM = "FIRM_QUOTE"
SINIF_B2B = "B2B_INDICATIVE"
SINIF_PUBLIC = "PUBLIC_INDICATIVE"
SINIF_SIRASI = {SINIF_PUBLIC: 1, SINIF_B2B: 2, SINIF_FIRM: 3}


@dataclass
class KopruKalemi:
    """FOB->CIF veya EXW->FOB bacagindaki TEK bir kalem."""
    ad: str
    tutar: Decimal | None
    currency: str | None
    evidence_id: str | None = None
    status: str | None = None

    def eksik_alanlar(self) -> list[str]:
        e = []
        if self.tutar is None:
            e.append(f"{self.ad}.tutar")
        if not self.currency:
            e.append(f"{self.ad}.currency")
        if not self.evidence_id:
            e.append(f"{self.ad}.evidence_id")
        if not self.status:
            e.append(f"{self.ad}.status")
        return e


@dataclass
class Kopru:
    """Teklif katmanini (L0/L1) tavan katmanina (L2/CIF) baglayan koprular."""
    exw_fob: list[KopruKalemi] = field(default_factory=list)
    fob_cif: list[KopruKalemi] = field(default_factory=list)

    def bacak(self, ad: str) -> list[KopruKalemi]:
        return self.exw_fob if ad == "EXW_FOB" else self.fob_cif

    def bacak_hazir_mi(self, ad: str) -> tuple[bool, list[str]]:
        kalemler = self.bacak(ad)
        if not kalemler:
            return False, [f"{ad}: hic kalem tanimlanmadi"]
        eksik: list[str] = []
        for k in kalemler:
            eksik += [f"{ad}.{x}" for x in k.eksik_alanlar()]
        return (not eksik), eksik

    def bacak_try(self, ad: str, eksen: FXEkseni) -> tuple[Decimal | None, list[str]]:
        toplam = D("0")
        eksik: list[str] = []
        for k in self.bacak(ad):
            kur = eksen.kur(k.currency)
            if k.tutar is None or kur is None:
                eksik.append(f"{ad}.{k.ad}: tutar/kur yok ({k.currency})")
                continue
            toplam += k.tutar * kur
        return (None if eksik else toplam), eksik


@dataclass
class Kademe:
    tier_code: str | None = None
    quantity: Decimal | None = None
    incoterm: str | None = None                 # EXW | FOB
    incoterm_named_place: str | None = None
    EXW: Decimal | None = None
    FOB: Decimal | None = None
    currency: str | None = None
    payment_terms: str | None = None
    lead_time: Decimal | None = None
    production_time: Decimal | None = None
    label_cost: Decimal | None = None
    label_cost_tek_seferlik: Decimal | None = None
    carton_cost: Decimal | None = None
    quote_class: str | None = None              # TEDARIKCI BEYANI (girdi)

    def fiyat(self) -> tuple[Decimal | None, str | None]:
        """(fiyat, katman) — Incoterm hangisiyse O fiyat kullanilir."""
        it = (self.incoterm or "").upper()
        if it == "FOB":
            return self.FOB, "L1"
        if it == "EXW":
            return self.EXW, "L0"
        return None, None


@dataclass
class Teklif:
    supplier: str | None = None
    supplier_id: str | None = None
    quote_date: str | None = None
    quote_valid_until: str | None = None
    product: str | None = None
    vintage: str | None = None
    ABV: Decimal | None = None
    business_model: str | None = None
    origin_document: str | None = None
    FOB_port: str | None = None
    EXW_place: str | None = None
    MOQ: Decimal | None = None
    MOQ_ikinci_birim: str | None = None
    bottle_weight: Decimal | None = None
    case_configuration: str | None = None
    pallet_configuration: str | None = None
    sample_cost: Decimal | None = None
    certificate_set: Any = None
    Turkey_availability: str | None = None
    confidence: str | None = None
    evidence_id: str | None = None
    ulke: str | None = None
    mense_grubu: str | None = None      # P | N | None -> N (kotumser)
    kademeler: list[Kademe] = field(default_factory=list)
    kopru: Kopru = field(default_factory=Kopru)

    def anahtar(self, k: Kademe) -> str:
        return f"{self.supplier}|{self.product}|{self.quote_date}|{k.tier_code}"

    def tekillik_denetimi(self) -> None:
        gorulen: set[str] = set()
        for k in self.kademeler:
            a = self.anahtar(k)
            if a in gorulen:
                raise KademeCiftKayit(
                    f"CIFT_KADEME: '{a}' bu teklifte ZATEN VAR "
                    f"(kademe_tekilligi ihlali)."
                )
            gorulen.add(a)


def teklif_kur(ham: dict[str, Any]) -> Teklif:
    """`quote-ingestion-schema.yaml` sekilli sozlukten `Teklif` kurar."""
    alanlar = {f for f in Teklif.__dataclass_fields__ if f not in ("kademeler", "kopru")}
    t = Teklif(**{a: ham.get(a) for a in alanlar if a in ham})
    for sayi in ("ABV", "MOQ", "bottle_weight", "sample_cost"):
        setattr(t, sayi, _d(getattr(t, sayi)))
    for hk in ham.get("kademeler") or []:
        k_alanlar = set(Kademe.__dataclass_fields__)
        k = Kademe(**{a: hk.get(a) for a in k_alanlar if a in hk})
        for sayi in ("quantity", "EXW", "FOB", "lead_time", "production_time",
                     "label_cost", "label_cost_tek_seferlik", "carton_cost"):
            setattr(k, sayi, _d(getattr(k, sayi)))
        t.kademeler.append(k)
    t.tekillik_denetimi()
    return t


# ===========================================================================
# 5. KURAL MOTORU — kurallar SEMADAN gelir, koda gomulu DEGILDIR
# ===========================================================================

@dataclass
class Ihlal:
    kural_id: str
    ad: str
    mesaj: str
    eylem: str
    hedef_sinif: str | None = None
    sonuc_zorla: str | None = None
    damga: str = DAMGA_BLOCKED


def _alan_oku(yol: str, teklif: Teklif, kademe: Kademe) -> Any:
    kok, _, ad = yol.partition(".")
    kaynak = teklif if kok == "quote" else kademe
    return getattr(kaynak, ad, None)


def _bos_mu(v: Any) -> bool:
    return v is None or (isinstance(v, str) and v.strip() == "")


def kural_uygula(
    kural: dict[str, Any], teklif: Teklif, kademe: Kademe, bugun: date
) -> list[Ihlal]:
    """Semadaki TEK bir dogrulama kuralini calistirir."""
    kid = kural.get("kural_id", "?")
    ad = kural.get("ad", "")
    tip = kural.get("tip")
    eylem = kural.get("eylem", "DAMGA")
    hedef = kural.get("hedef_sinif") or kural.get("ayrica_sinif_dusur")
    zorla = kural.get("sonuc") or kural.get("ayrica_sonuc_zorla")
    damga = kural.get("damga", DAMGA_BLOCKED)
    out: list[Ihlal] = []

    def ihlal(msg: str) -> None:
        out.append(Ihlal(kid, ad, msg, eylem, hedef, zorla, damga))

    if tip == "HEPSI_DOLU":
        eksik = [y for y in kural.get("alanlar", [])
                 if _bos_mu(_alan_oku(y, teklif, kademe))]
        if eksik:
            ihlal("eksik alan(lar): " + ", ".join(eksik))

    elif tip == "EN_AZ_BIRI_DOLU":
        alanlar = kural.get("alanlar", [])
        if all(_bos_mu(_alan_oku(y, teklif, kademe)) for y in alanlar):
            ihlal("hepsi bos: " + ", ".join(alanlar))

    elif tip == "IZINLI_DEGERLER":
        v = _alan_oku(kural["alan"], teklif, kademe)
        izinli = [str(x).upper() for x in kural.get("izinli", [])]
        if _bos_mu(v) or str(v).upper() not in izinli:
            ihlal(f"{kural['alan']}='{v}' izinli degil ({izinli})")

    elif tip == "YASAK_DEGER":
        v = _alan_oku(kural["alan"], teklif, kademe)
        yasak = [str(x).upper() for x in kural.get("yasak", [])]
        if _bos_mu(v) or str(v).strip().upper() in yasak:
            ihlal(f"{kural['alan']}='{v}' YASAK/belirsiz deger")

    elif tip == "KOSULLU_ZORUNLU":
        v = _alan_oku(kural["kosul_alan"], teklif, kademe)
        if str(v).upper() in [str(x).upper() for x in kural.get("kosul_degerler", [])]:
            eksik = [y for y in kural.get("gerekli_alanlar", [])
                     if _bos_mu(_alan_oku(y, teklif, kademe))]
            if eksik:
                ihlal(f"kosul '{v}' saglandi, eksik: " + ", ".join(eksik))

    elif tip == "TARIH_GECERLILIGI":
        v = _alan_oku(kural["alan"], teklif, kademe)
        if not _bos_mu(v):
            try:
                bit = datetime.strptime(str(v)[:10], "%Y-%m-%d").date()
                if bit < bugun:
                    ihlal(f"gecerlilik {bit} < degerlendirme {bugun}")
            except ValueError:
                ihlal(f"{kural['alan']}='{v}' tarih olarak okunamadi")

    elif tip == "SINIF_TAVANI":
        pass    # QV-2 `sinif_belirle` icinde uygulanir (min kurali)

    return out


def sinif_belirle(
    teklif: Teklif, kademe: Kademe, sema: dict[str, Any], bugun: date
) -> tuple[str, str | None, list[Ihlal]]:
    """
    Doner: (etkin_sinif, zorlanan_sonuc, ihlaller)

    QV-2 (SINIF_YUKSELTME_YASAGI): etkin = min(beyan_edilen, hesaplanan).
    """
    ihlaller: list[Ihlal] = []
    for kural in sema.get("dogrulama_kurallari", []):
        ihlaller += kural_uygula(kural, teklif, kademe, bugun)

    hesaplanan = SINIF_FIRM
    zorlanan: str | None = None
    for i in ihlaller:
        if i.hedef_sinif and SINIF_SIRASI.get(i.hedef_sinif, 3) < SINIF_SIRASI[hesaplanan]:
            hesaplanan = i.hedef_sinif
        if i.sonuc_zorla:
            zorlanan = _sonuc_dogrula(i.sonuc_zorla)

    beyan = (kademe.quote_class or "").strip().upper() or None
    if beyan in SINIF_SIRASI:
        if SINIF_SIRASI[beyan] < SINIF_SIRASI[hesaplanan]:
            hesaplanan = beyan                 # beyan DAHA DUSUKSE dusurur
        elif SINIF_SIRASI[beyan] > SINIF_SIRASI[hesaplanan]:
            ihlaller.append(Ihlal(
                "QV-2", "SINIF_YUKSELTME_YASAGI",
                f"beyan '{beyan}' > hesaplanan '{hesaplanan}'; beyan YUKSELTMEZ",
                "DAMGA",
            ))
    return hesaplanan, zorlanan, ihlaller


# ===========================================================================
# 6. DEGERLENDIRME
# ===========================================================================

KARAR_YOLU_TAM = "TAM_KOPRU"
KARAR_YOLU_TEK_YONLU = "TEK_YONLU_ALT_SINIR"
KARAR_YOLU_YOK = "KARAR_YOLU_YOK"


@dataclass
class Degerlendirme:
    """TEK bir (kademe x fx_ekseni) satiri. INTERNAL_ONLY."""
    supplier: str | None
    tier_code: str | None
    fx_ekseni: str
    sonuc: str
    karar_yolu: str = KARAR_YOLU_YOK
    etkin_sinif: str = SINIF_PUBLIC
    teklif_katmani: str | None = None
    teklif_fiyat: Decimal | None = None
    teklif_currency: str | None = None
    kur: Decimal | None = None
    cif_esdegeri_try: Decimal | None = None
    cif_alt_sinir_try: Decimal | None = None
    X_try: Decimal | None = None
    Y_try: Decimal | None = None
    hacim_tavani_try: Decimal | None = None
    hacim_tavani_notu: str = ""
    max_fob_fx: Decimal | None = None
    max_exw_fx: Decimal | None = None
    max_fob_ust_sinir_fx: Decimal | None = None
    epistemik_not: str = ""
    bayraklar: list[str] = field(default_factory=list)
    eksik_girdiler: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.sonuc = _sonuc_dogrula(self.sonuc)


def _epistemik_not(etkin_sinif: str, band: TavanBandi) -> str:
    return (
        f"ASIMETRIK KARSILASTIRMA: teklif={etkin_sinif} (gozlem) "
        f"vs tavan={band.sinif} "
        f"(BLOCKED_INPUT={band.blocked_input_count}). "
        "Iki farkli epistemik sinif karsilastiriliyor: biri OLCULMUS bir "
        "ticari beyan, digeri TURETILMIS bir ust sinir. Esitlenmeleri "
        "SAYISAL degil, YAPISAL olarak yorumlanmalidir."
    )


def kademe_degerlendir(
    teklif: Teklif,
    kademe: Kademe,
    band: TavanBandi,
    eksenler: dict[str, FXEkseni],
    sema: dict[str, Any],
    bugun: date,
    hedef_id: str = "TGT_799",
    kanal: str = "CHAIN_RETAIL",
) -> list[Degerlendirme]:
    """Bir kademeyi DORT FX ekseninde ayri ayri degerlendirir."""
    etkin_sinif, zorlanan, ihlaller = sinif_belirle(teklif, kademe, sema, bugun)
    kural_eksikleri = [f"[{i.kural_id}] {i.mesaj}" for i in ihlaller]

    sise = int(kademe.quantity) if kademe.quantity is not None else None
    hacim_tavani, hacim_not = hacim_tavani_oku(
        hedef_id, kanal, band.mense_grubu, sise
    )

    fiyat, katman = kademe.fiyat()
    gerekli_bacaklar = (["FOB_CIF"] if katman == "L1"
                        else ["EXW_FOB", "FOB_CIF"] if katman == "L0" else [])

    satirlar: list[Degerlendirme] = []
    for kod in FX_EKSEN_SIRASI:
        eksen = eksenler.get(kod) or FXEkseni(kod=kod)
        bayraklar: list[str] = []
        eksik = list(kural_eksikleri)
        if hacim_tavani is None:
            bayraklar.append(hacim_not)

        d = Degerlendirme(
            supplier=teklif.supplier, tier_code=kademe.tier_code, fx_ekseni=kod,
            sonuc=SONUC_INCOMPLETE, etkin_sinif=etkin_sinif,
            teklif_katmani=katman, teklif_fiyat=fiyat,
            teklif_currency=kademe.currency,
            X_try=band.X_try, Y_try=band.Y_try,
            hacim_tavani_try=hacim_tavani, hacim_tavani_notu=hacim_not,
            epistemik_not=_epistemik_not(etkin_sinif, band),
            bayraklar=bayraklar, eksik_girdiler=eksik,
        )

        # --- bloke edici on kosullar -----------------------------------
        if zorlanan == SONUC_INCOMPLETE:
            d.bayraklar.append("KURAL_ZORLAMASI")
            satirlar.append(d)
            continue
        if not band.hazir_mi():
            d.eksik_girdiler += band.eksikler
            d.bayraklar.append("TAVAN_YOK")
            satirlar.append(d)
            continue
        if not eksen.hazir_mi():
            d.eksik_girdiler.append(f"fx[{kod}]: {eksen.kaynak or 'kur yok'}")
            d.bayraklar.append("FX_BLOCKED_INPUT")
            satirlar.append(d)
            continue

        kur = eksen.kur(kademe.currency)
        d.kur = kur
        if kur is None:
            d.eksik_girdiler.append(
                f"fx[{kod}]: '{kademe.currency}' icin kur YOK (uydurulmaz)"
            )
            d.bayraklar.append("PARA_BIRIMI_KURU_YOK")
            satirlar.append(d)
            continue
        if fiyat is None or katman is None:
            d.bayraklar.append("FIYAT_VEYA_KATMAN_YOK")
            satirlar.append(d)
            continue

        # --- koprular ---------------------------------------------------
        kopru_try = D("0")
        kopru_eksik: list[str] = []
        for bacak in gerekli_bacaklar:
            tutar, e = teklif.kopru.bacak_try(bacak, eksen)
            hazir, e2 = teklif.kopru.bacak_hazir_mi(bacak)
            if tutar is None or not hazir:
                kopru_eksik += (e + e2)
            else:
                kopru_try += tutar

        # --- MAX_FOB / MAX_EXW (bu eksende) ------------------------------
        d.max_fob_ust_sinir_fx = (band.Y_try / kur)          # kopru >= 0 -> UST SINIR
        if not kopru_eksik:
            fob_cif_try, _ = teklif.kopru.bacak_try("FOB_CIF", eksen)
            if fob_cif_try is not None:
                d.max_fob_fx = (band.Y_try - fob_cif_try) / kur
                exw_fob_try, _ = teklif.kopru.bacak_try("EXW_FOB", eksen)
                if exw_fob_try is not None:
                    d.max_exw_fx = (band.Y_try - fob_cif_try - exw_fob_try) / kur

        # --- karsilastirma ----------------------------------------------
        if kopru_eksik:
            # Koprular >= 0 oldugu icin `fiyat*kur` gercek CIF'in ALT SINIRIDIR.
            # Bu nedenle YALNIZCA "Y'nin ustunde" yonu KARARLASTIRILABILIR.
            alt_sinir = fiyat * kur
            d.cif_alt_sinir_try = alt_sinir
            d.eksik_girdiler += kopru_eksik
            if alt_sinir > band.Y_try:
                d.sonuc = _sonuc_dogrula(SONUC_ABOVE)
                d.karar_yolu = KARAR_YOLU_TEK_YONLU
                d.bayraklar.append("TEK_YONLU_KARAR: kopru eksik olsa da alt sinir Y'yi asiyor")
            else:
                d.sonuc = _sonuc_dogrula(SONUC_INCOMPLETE)
                d.karar_yolu = KARAR_YOLU_YOK
                d.bayraklar.append(
                    "KOPRU_EKSIK: STRONG/NEGOTIATE ayrimi YAPILAMAZ "
                    "(alt sinir Y'nin altinda ama gercek CIF daha yuksek olabilir)"
                )
            satirlar.append(d)
            continue

        cif = fiyat * kur + kopru_try
        d.cif_esdegeri_try = cif
        d.karar_yolu = KARAR_YOLU_TAM
        if cif <= band.X_try:
            d.sonuc = _sonuc_dogrula(SONUC_STRONG)
        elif cif <= band.Y_try:
            d.sonuc = _sonuc_dogrula(SONUC_NEGOTIATE)
        else:
            d.sonuc = _sonuc_dogrula(SONUC_ABOVE)
            d.bayraklar.append(
                "ABOVE_CEILING BIR RET DEGILDIR: " + RET_YASAGI_GEREKCESI
            )
        satirlar.append(d)

    return satirlar


def teklif_degerlendir(
    teklif: Teklif,
    sema: dict[str, Any],
    eksenler: dict[str, FXEkseni],
    bugun: date,
    hedef_id: str = "TGT_799",
    kanal: str = "CHAIN_RETAIL",
) -> list[Degerlendirme]:
    teklif.tekillik_denetimi()
    grup = (teklif.mense_grubu or "N").upper()
    if teklif.origin_document in (None, "", "UNKNOWN"):
        grup = "N"      # menşe belgesi bilinmiyorsa KOTUMSER band
    band = tavan_bandi_oku(hedef_id, kanal, grup)
    out: list[Degerlendirme] = []
    for k in teklif.kademeler:
        out += kademe_degerlendir(teklif, k, band, eksenler, sema, bugun,
                                  hedef_id, kanal)
    return out


# ===========================================================================
# 7. KALEM DEFTERI KOPRUSU — teklif fiyati modele NASIL girer
# ===========================================================================

def teklif_kalemi(teklif: Teklif, kademe: Kademe, sema: dict[str, Any]) -> MaliyetKalemi:
    """
    Kabul edilen bir teklif fiyatini TUR 3A metadata mimarisine baglar.
    Dokuz alandan biri eksikse kalem `BLOCKED_INPUT` damgasi alir ve
    **0 SAYILMAZ** — sessiz eksik gecmez.
    """
    sabit = (sema.get("metadata_sozlesmesi") or {}).get(
        "teklif_kaleminin_sabit_alanlari", {}
    )
    fiyat, katman = kademe.fiyat()
    return MaliyetKalemi(
        kalem_kimligi=f"TEKLIF_{teklif.supplier_id}_{kademe.tier_code}",
        ad=f"{teklif.supplier} / {teklif.product} / {kademe.tier_code}",
        payer=sabit.get("payer"),
        receiver=sabit.get("receiver"),
        layer=katman,
        currency=kademe.currency,
        fixed_or_variable=sabit.get("fixed_or_variable"),
        per_bottle_or_total=sabit.get("per_bottle_or_total"),
        tax_treatment=sabit.get("tax_treatment"),
        evidence_id=teklif.evidence_id,
        status="FACT" if (kademe.quote_class or "").upper() == SINIF_FIRM else "ESTIMATE",
        tutar_try=None,             # ⛔ TL'ye CEVRILEREK saklanmaz (makro.yaml §5)
        kdv_dahil_mi="HARIC",
        hard_blocker=False,
        notes=f"teklif fiyati {fiyat} {kademe.currency} — orijinal para biriminde saklanir",
    )


# ===========================================================================
# 8. CIKTI URETIMI
# ===========================================================================

def _f(v: Decimal | None, n: int = 4) -> str:
    return "UNKNOWN" if v is None else f"{v:.{n}f}"


def internal_rapor_metni(
    degerlendirmeler: list[Degerlendirme],
    band: TavanBandi,
    eksenler: dict[str, FXEkseni],
    fx_eksikleri: list[str],
    baslik: str,
) -> str:
    s: list[str] = [INTERNAL_ONLY_DAMGASI, "", f"# {baslik}", ""]
    s.append("```yaml")
    s.append("cikti_sinifi:   INTERNAL_ONLY")
    s.append("durum:          DRAFT          # OQ-901/T-851 CRITICAL+OPEN")
    s.append(f"tavan_sinifi:   {band.sinif}")
    s.append(f"tavan_kaynagi:  {band.kaynak}")
    s.append(f"X_try:          {_f(band.X_try)}")
    s.append(f"Y_try:          {_f(band.Y_try)}")
    s.append(f"mense_grubu:    {band.mense_grubu}")
    s.append(f"blocked_input:  {band.blocked_input_count}")
    s.append("ret_hukmu:      YASAK  # REJECTED uretilemez")
    s.append("```")
    s.append("")
    s.append("## FX EKSENLERI")
    s.append("")
    s.append("| eksen | usd_try | eur_try | status | kaynak |")
    s.append("|---|---|---|---|---|")
    for kod in FX_EKSEN_SIRASI:
        e = eksenler.get(kod) or FXEkseni(kod=kod)
        s.append(f"| {kod} | {_f(e.usd_try, 4)} | {_f(e.eur_try, 4)} | "
                 f"{e.status} | {e.kaynak or '-'} |")
    if fx_eksikleri:
        s.append("")
        s.append("**FX BLOCKED_INPUT:**")
        for x in fx_eksikleri:
            s.append(f"- {x}")
    s.append("")
    s.append("## DEGERLENDIRME SATIRLARI")
    s.append("")
    if not degerlendirmeler:
        s.append("*(havuzda teklif YOK — 2026-08-10 itibariyle sifir gercek teklif)*")
    else:
        s.append("| supplier | tier | fx | sonuc | karar_yolu | sinif | "
                 "katman | fiyat | kur | CIF_TRY | X | Y | MAX_FOB(ust) |")
        s.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for d in degerlendirmeler:
            s.append(
                f"| {d.supplier} | {d.tier_code} | {d.fx_ekseni} | **{d.sonuc}** | "
                f"{d.karar_yolu} | {d.etkin_sinif} | {d.teklif_katmani} | "
                f"{_f(d.teklif_fiyat, 4)} {d.teklif_currency or ''} | {_f(d.kur, 4)} | "
                f"{_f(d.cif_esdegeri_try or d.cif_alt_sinir_try, 4)} | "
                f"{_f(d.X_try)} | {_f(d.Y_try)} | {_f(d.max_fob_ust_sinir_fx, 4)} |"
            )
    s.append("")
    s.append("## EKSIK GIRDILER (BLOCKED_INPUT)")
    s.append("")
    hepsi: list[str] = []
    for d in degerlendirmeler:
        hepsi += d.eksik_girdiler
    if not hepsi and not fx_eksikleri:
        s.append("*(yok)*")
    for x in sorted(set(hepsi + fx_eksikleri)):
        s.append(f"- {x}")
    s.append("")
    s.append("> `ABOVE_CEILING` bir GOZLEMDIR, bir RET DEGILDIR. " + RET_YASAGI_GEREKCESI)
    return "\n".join(s) + "\n"


def tedarikciye_giden_metin(teklif: Teklif, degerlendirmeler: list[Degerlendirme]) -> str:
    """
    Tedarikciye gonderilebilecek TEK metin: EKSIK ALAN TALEBI.
    Tavan, sonuc, kur, katman karsilastirmasi ICERMEZ.
    ⛔ Bu metin `disari_giden_metin_denetle()`den GECMEDEN kullanilamaz.
    """
    eksik_alanlar: set[str] = set()
    for d in degerlendirmeler:
        for e in d.eksik_girdiler:
            m = re.search(r"(quote|tier)\.([A-Za-z_]+)", e)
            if m:
                eksik_alanlar.add(m.group(2))
    satir = [
        f"Sayin {teklif.supplier or '<tedarikci>'},",
        "",
        "Teklifiniz icin tesekkur ederiz. Teklifi ic degerlendirmemize",
        "alabilmemiz icin asagidaki alanlarin acikca belirtilmesi gerekiyor:",
        "",
    ]
    for a in sorted(eksik_alanlar) or ["(eksik alan yok)"]:
        satir.append(f"  - {a}")
    satir += [
        "",
        "Ayrica her hacim kademesi icin fiyati AYRI AYRI ve teslim sekli",
        "(yer/liman adiyla birlikte) belirtilerek verilmesini rica ederiz.",
        "",
        "Saygilarimizla,",
    ]
    return disari_giden_metin_denetle("\n".join(satir) + "\n")


# ===========================================================================
# 9. ANA
# ===========================================================================

def ana(bugun: date | None = None) -> int:
    bugun = bugun or date.today()
    sema = guvenli_girdi_yukle(SEMA_DOSYASI)
    makro = guvenli_girdi_yukle(MAKRO_DOSYASI)
    eksenler, fx_eksikleri = fx_eksenleri_oku(makro)

    ham_teklifler = sema.get("teklifler") or []
    degerlendirmeler: list[Degerlendirme] = []
    for ham in ham_teklifler:
        t = teklif_kur(ham)
        degerlendirmeler += teklif_degerlendir(t, sema, eksenler, bugun)

    band = tavan_bandi_oku("TGT_799", "CHAIN_RETAIL", "P")

    print("=" * 100)
    print("TUR 3.25 §12/§13 — QUOTE INGESTION + EVALUATION   [INTERNAL_ONLY]")
    print("=" * 100)
    print(f"sema            : {SEMA_DOSYASI.name}")
    print(f"havuzdaki teklif: {len(ham_teklifler)}")
    print(f"tavan bandi (P) : X={_f(band.X_try)}  Y={_f(band.Y_try)}  "
          f"[{band.sinif}]")
    print(f"FX eksenleri    : " + ", ".join(
        f"{k}={eksenler[k].status}" for k in FX_EKSEN_SIRASI))
    if fx_eksikleri:
        print("BLOCKED_INPUT   :")
        for x in fx_eksikleri:
            print(f"  - {x}")
    print(f"degerlendirme   : {len(degerlendirmeler)} satir")
    print("RET HUKMU       : YASAK (OQ-901 / T-851)")
    print("=" * 100)

    yol = internal_rapor_yaz(
        OUTPUTS / "INTERNAL_ONLY-teklif-degerlendirme.md",
        internal_rapor_metni(
            degerlendirmeler, band, eksenler, fx_eksikleri,
            "TEKLIF DEGERLENDIRME — TUR 3.25 §13 (INTERNAL_ONLY)",
        ),
    )
    print(f"yazildi: {yol}")
    return 0


if __name__ == "__main__":
    sys.exit(ana())
