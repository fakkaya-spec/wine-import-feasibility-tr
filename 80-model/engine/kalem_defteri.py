"""
kalem_defteri.py — ZORUNLU METADATA SÖZLEŞMESİ + KALEM DEFTERİ

===========================================================================
 KAYNAK SPESİFİKASYON (kod değil, sözleşme)
===========================================================================
  70-kanal/kanal-katman-matrah-haritasi.md §2   (on alanlı zorunlu sözleşme)
  70-kanal/kanal-katman-matrah-haritasi.md §8   (15 kalemlik BLOCKED envanteri)
  70-kanal/kanal-bacagi-hata-listesi.md  K6     (LEDGER_UNIQUENESS)
  70-kanal/kanal-bacagi-hata-listesi.md  K3     (ZERO_PARITY)
  80-model/inputs/kanal.yaml -> blocked_envanteri (makine okunur karşılık)

===========================================================================
 NEDEN VAR — SILENT OMISSION YASAĞI (TUR 3A GÖREV 1)
===========================================================================
TUR 2.5'e kadar bir maliyet kaleminin tutarı `None` ise model onu **sessizce
0** alıyordu. `kanal-marj-uzmani`'nın 15 kalemlik `BLOCKED` envanterinin
**15'i de** bu yoldan geçiyordu. `0` bir değer değildir, `0` bir varsayımdır.

Bu modülden sonra bir kalem modele **yalnızca üç damgadan biriyle** girer:

  OK                    -> dokuz alanın dokuzu dolu VE tutar biliniyor
  BLOCKED_INPUT         -> bir alan veya tutar eksik; kalem 0 SAYILMAZ,
                           çıktı damgalanır ve EKSİK ALAN ADI yazılır
  EXCLUDED_WITH_REASON  -> kalem BİLİNÇLİ olarak dışarıda; gerekçe zorunlu

`BLOCKED_INPUT`'un iki sertliği vardır:
  hard_blocker=True  -> sonuç UNKNOWN döner (sayı ÜRETİLMEZ)
  hard_blocker=False -> sayı üretilir ama çıktı `DRAFT` ve damgalıdır

===========================================================================
 GÜVENLİK KİLİDİ
===========================================================================
  - Bu dosyada hiçbir vergi oranı / tutar / matrah tanımı YOKTUR.
  - `status: TEST_FIXTURE` taşıyan bir kalem üretim defterine GİREMEZ
    (`FixtureSizintisi` istisnası fırlatılır).
  - Adında `TEST_FIXTURE` geçen bir dosya gerçek girdi olarak OKUNAMAZ
    (`guvenli_girdi_yukle`).
===========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# SÖZLEŞME
# ---------------------------------------------------------------------------

#: `kanal-katman-matrah-haritasi.md` §2 — dokuz zorunlu alan.
#: (`basis` onuncu alandır ve kanal kalemleri için ayrıca zorunludur; L5
#:  kalemlerinde matrah tanım gereği "tutar" olduğu için opsiyoneldir.)
ZORUNLU_ALANLAR: tuple[str, ...] = (
    "payer",
    "receiver",
    "layer",
    "currency",
    "fixed_or_variable",
    "per_bottle_or_total",
    "tax_treatment",
    "evidence_id",
    "status",
)

DAMGA_OK = "OK"
DAMGA_BLOCKED = "BLOCKED_INPUT"
DAMGA_EXCLUDED = "EXCLUDED_WITH_REASON"

#: Mutlak TL tutarlı kalemlerde `kdv_dahil_mi` ZORUNLUDUR (K10 / TVK-N3).
MUTLAK_TUTAR_BIRIMLERI = ("PER_BOTTLE", "TOTAL")

GECERLI_STATUSLER = (
    "FACT", "ESTIMATE", "ASSUMPTION", "UNKNOWN", "BLOCKED",
    "CONFLICT", "SUPERSEDED", "DERIVED", "SPEC_DECISION",
    "STRUCTURAL_FACT", "INVESTOR_DECISION_REQUIRED", "N/A",
)


class FixtureSizintisi(RuntimeError):
    """Bir TEST_FIXTURE değeri gerçek girdi olarak okunmaya çalışıldı."""


class DefterCiftKayit(RuntimeError):
    """LEDGER_UNIQUENESS ihlali — aynı kalem_kimligi iki kez düşülüyor (K6)."""


def guvenli_girdi_yukle(yol: str | Path) -> Any:
    """
    Gerçek girdi yükleyicisi. Adında `TEST_FIXTURE` geçen dosyayı REDDEDER.
    (`TEST_FIXTURE` dosyaları YALNIZCA test modülünden okunabilir.)
    """
    import yaml

    p = Path(yol)
    if "TEST_FIXTURE" in p.name:
        raise FixtureSizintisi(
            f"'{p.name}' bir TEST_FIXTURE dosyasidir ve GERCEK GIRDI olarak "
            f"OKUNAMAZ. Uretim kodu bu dosyayi ithal edemez."
        )
    with p.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


# ---------------------------------------------------------------------------
# KALEM
# ---------------------------------------------------------------------------

@dataclass
class MaliyetKalemi:
    """
    Modele giren HER maliyet kalemi. Dokuz zorunlu alandan biri eksikse
    kalem `BLOCKED_INPUT` damgası alır ve **0 SAYILMAZ**.
    """

    kalem_kimligi: str                     # LEDGER_UNIQUENESS anahtarı (K6)
    ad: str = ""

    # --- dokuz zorunlu alan ---
    payer: str | None = None
    receiver: str | None = None
    layer: str | None = None               # L0..L8 veya "L6->L7"
    currency: str | None = None
    fixed_or_variable: str | None = None   # FIXED | VARIABLE | KARISIK
    per_bottle_or_total: str | None = None # PER_BOTTLE | TOTAL | ORAN
    tax_treatment: str | None = None
    evidence_id: str | None = None
    status: str | None = None

    # --- onuncu alan: matrah (kanal kalemlerinde zorunlu) ---
    basis: str | None = None
    basis_zorunlu_mu: bool = False

    # --- değer ---
    tutar_try: Decimal | None = None
    kdv_dahil_mi: str | None = None        # mutlak tutarlı kalemlerde ZORUNLU (K10)

    # --- damga kontrolü ---
    dusuldu_mu: bool = True                # False -> hesaba katılmaz
    haric_gerekce: str | None = None       # doluysa EXCLUDED_WITH_REASON
    hard_blocker: bool = False             # True -> sonuc UNKNOWN
    sahibi: str | None = None              # hangi ajan kapatacak
    ticket: str | None = None
    yon: str | None = None                 # belirsizlik giderilirse MAX_CIF yönü
    notes: str = ""

    # ---------------------------------------------------------------
    def _fixture_denetimi(self) -> None:
        if self.status == "TEST_FIXTURE":
            raise FixtureSizintisi(
                f"kalem '{self.kalem_kimligi}': status=TEST_FIXTURE bir URETIM "
                f"defterine GIREMEZ. Fixture degerleri yalniz test modulunde kullanilir."
            )

    def eksik_alanlar(self) -> list[str]:
        eksik = [a for a in ZORUNLU_ALANLAR if getattr(self, a) in (None, "")]
        if self.basis_zorunlu_mu and self.basis in (None, ""):
            eksik.append("basis")
        if self.tutar_try is None:
            eksik.append("tutar_try")
        if (
            self.tutar_try is not None
            and self.per_bottle_or_total in MUTLAK_TUTAR_BIRIMLERI
            and self.kdv_dahil_mi in (None, "")
        ):
            # K10 / TVK-N3: mutlak tutarli kalemde KDV tabani ZORUNLU
            eksik.append("kdv_dahil_mi")
        return eksik

    def damga(self) -> tuple[str, list[str]]:
        self._fixture_denetimi()
        if self.haric_gerekce:
            return DAMGA_EXCLUDED, []
        eksik = self.eksik_alanlar()
        if eksik:
            return DAMGA_BLOCKED, eksik
        return DAMGA_OK, []

    def dusulecek_tutar(self) -> Decimal:
        """
        SADECE `OK` damgalı ve `dusuldu_mu` olan kalem tutar üretir.
        `BLOCKED_INPUT` kalem **0 döndürmez — hesaba HİÇ girmez** ve bu
        farkın kaydı `KalemDefteri.damgalar` üzerinden tutulur.
        """
        d, _ = self.damga()
        if d != DAMGA_OK or not self.dusuldu_mu:
            return Decimal("0")
        return self.tutar_try or Decimal("0")


# ---------------------------------------------------------------------------
# DEFTER
# ---------------------------------------------------------------------------

@dataclass
class KalemDefteri:
    """
    Tek bir koşunun kalem defteri.

    LEDGER_UNIQUENESS (K6): aynı `kalem_kimligi` iki kez eklenirse
    `DefterCiftKayit` fırlatılır — çift sayım kodun içinde ölür.
    """

    kanal_kodu: str = ""
    kalemler: list[MaliyetKalemi] = field(default_factory=list)
    _kimlikler: set[str] = field(default_factory=set, repr=False)

    def ekle(self, k: MaliyetKalemi) -> MaliyetKalemi:
        if k.kalem_kimligi in self._kimlikler:
            raise DefterCiftKayit(
                f"CIFT_SAYIM: '{k.kalem_kimligi}' defterde ZATEN VAR "
                f"(LEDGER_UNIQUENESS / K6 ihlali)."
            )
        self._kimlikler.add(k.kalem_kimligi)
        self.kalemler.append(k)
        return k

    def ekle_hepsi(self, ks: list[MaliyetKalemi]) -> None:
        for k in ks:
            self.ekle(k)

    # --- damgalar -------------------------------------------------------
    def damgalar(self) -> list[tuple[MaliyetKalemi, str, list[str]]]:
        out = []
        for k in self.kalemler:
            d, eksik = k.damga()
            out.append((k, d, eksik))
        return out

    def damga_ozeti(self) -> dict[str, int]:
        ozet = {DAMGA_OK: 0, DAMGA_BLOCKED: 0, DAMGA_EXCLUDED: 0}
        for _k, d, _e in self.damgalar():
            ozet[d] += 1
        return ozet

    def bloke_kalemler(self) -> list[tuple[MaliyetKalemi, list[str]]]:
        return [(k, e) for k, d, e in self.damgalar() if d == DAMGA_BLOCKED]

    def haric_kalemler(self) -> list[MaliyetKalemi]:
        return [k for k, d, _e in self.damgalar() if d == DAMGA_EXCLUDED]

    def hard_blocker_var_mi(self) -> list[str]:
        return [
            f"{k.kalem_kimligi}: eksik={','.join(e)}"
            for k, e in self.bloke_kalemler()
            if k.hard_blocker
        ]

    def toplam_dusulen(self) -> Decimal:
        return sum((k.dusulecek_tutar() for k in self.kalemler), Decimal("0"))

    # --- ZERO_PARITY (K3) ----------------------------------------------
    def sifir_sayisi(self) -> int:
        """Bu kanalda kaç kalem `UNKNOWN -> hesaba girmedi` durumunda."""
        return len(self.bloke_kalemler())

    def rapor_satirlari(self) -> list[str]:
        satir: list[str] = []
        for k, d, eksik in self.damgalar():
            if d == DAMGA_OK:
                continue
            if d == DAMGA_EXCLUDED:
                satir.append(
                    f"  [{DAMGA_EXCLUDED}] {k.kalem_kimligi} — {k.haric_gerekce}"
                )
            else:
                sert = " (HARD)" if k.hard_blocker else ""
                satir.append(
                    f"  [{DAMGA_BLOCKED}{sert}] {k.kalem_kimligi} — eksik alan(lar): "
                    f"{', '.join(eksik)}"
                    + (f" | sahibi={k.sahibi}" if k.sahibi else "")
                    + (f" | ticket={k.ticket}" if k.ticket else "")
                    + (f" | yon={k.yon}" if k.yon else "")
                )
        return satir


# ---------------------------------------------------------------------------
# ZERO_PARITY — iki kanal karşılaştırılabilir mi (K3 / TVK-N5)
# ---------------------------------------------------------------------------

def zero_parity(a: KalemDefteri, b: KalemDefteri) -> tuple[bool, str]:
    """
    İki kanalın `MAX_CIF`'i karşılaştırılmadan ÖNCE koşulur.
    Sıfır (BLOCKED) sayıları eşit değilse kanallar KARŞILAŞTIRILAMAZ.
    """
    na, nb = a.sifir_sayisi(), b.sifir_sayisi()
    if na == nb:
        return True, f"ZERO_PARITY OK ({a.kanal_kodu}={na}, {b.kanal_kodu}={nb})"
    return False, (
        f"KANALLAR_KARSILASTIRILAMAZ: {a.kanal_kodu} icinde {na}, "
        f"{b.kanal_kodu} icinde {nb} kalem BLOCKED_INPUT. Tavan farkinin "
        f"ne kadari GERCEK, ne kadari EKSIK SAYIM AYRIMI YAPILAMAZ (K3)."
    )


# ---------------------------------------------------------------------------
# kanal.yaml -> blocked_envanteri  (15 kalem) okuyucusu
# ---------------------------------------------------------------------------

def blocked_envanterinden_kalemler(kanal_yaml: dict[str, Any]) -> list[MaliyetKalemi]:
    """
    `kanal-marj-uzmani`'nın 15 kalemlik `BLOCKED` envanterini
    (`kanal.yaml -> blocked_envanteri`) metadata mimarisine bağlar.

    Bu kalemlerin HİÇBİRİ için tutar YOKTUR — dolayısıyla hepsi
    `BLOCKED_INPUT` damgası alır. Bugüne kadar **sessizce 0** geçiyorlardı.
    Buradan sonra çıktıda İSİMLERİYLE görünürler.
    """
    env = kanal_yaml.get("blocked_envanteri") or {}
    kalemler: list[MaliyetKalemi] = []
    for kod, blok in env.items():
        if not isinstance(blok, dict) or "kalem" not in blok:
            continue  # 'uyari' gibi serbest metin satırları
        kalemler.append(
            MaliyetKalemi(
                kalem_kimligi=f"BLOCKED_{kod}",
                ad=str(blok.get("kalem")),
                # metadata BİLEREK boş bırakılır: bu kalemlerin belirsiz olan
                # şeyi zaten `basis` / `fixed_or_variable` / tutar'dır.
                basis_zorunlu_mu=True,
                tutar_try=None,
                status="BLOCKED",
                sahibi=str(blok.get("sahibi")) if blok.get("sahibi") else None,
                ticket=str(blok.get("ticket") or blok.get("conflict_id") or ""),
                yon=str(blok.get("yon")) if blok.get("yon") else None,
                dusuldu_mu=False,   # tutarı yok; hesaba GİRMEZ ama GÖRÜNÜR
                notes="kanal.yaml/blocked_envanteri — 70-kanal/kanal-katman-matrah-haritasi.md §8",
            )
        )
    return kalemler
