"""
duyarlilik.py — DUYARLILIK ANALİZİ MOTORU (BOŞ İSKELET)

===========================================================================
 TUR 0 — GÜVENLİ BOŞ İSKELET
===========================================================================
Duyarlılık eksenleri (senaryolar.yaml/duyarlilik_eksenleri):
  FX · FREIGHT · OTV · PRICE

Kural (CLAUDE.md §1): Model kanitsiz sayi uretmez.
Duyarlilik analizi de bir istisna DEGILDIR — min/base/max degerleri
kanitli girdilerden gelir, UYDURULMAZ.

Kural: Tek bir sayi sunulmaz. Her sonuc bir ARALIK olarak gosterilir.
===========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Any, Callable

from matrah_sirasi import Status


class Eksen(str, Enum):
    FX = "FX"
    FREIGHT = "FREIGHT"
    OTV = "OTV"
    PRICE = "PRICE"


@dataclass
class EksenAraligi:
    """Bir duyarlılık ekseninin min/base/max tanımı."""
    eksen: Eksen
    min: Decimal | None = None
    base: Decimal | None = None
    max: Decimal | None = None
    unit: str | None = None
    status: Status = Status.UNKNOWN
    evidence_ids: list[str] = field(default_factory=list)
    kaynak_dosya: str | None = None

    def kullanilabilir_mi(self) -> bool:
        return (
            self.min is not None
            and self.base is not None
            and self.max is not None
            and self.status in (Status.FACT, Status.ESTIMATE, Status.ASSUMPTION)
        )

    def eksikler(self) -> list[str]:
        eksik: list[str] = []
        if self.min is None:
            eksik.append("min yok")
        if self.base is None:
            eksik.append("base yok")
        if self.max is None:
            eksik.append("max yok")
        if self.status is Status.UNKNOWN:
            eksik.append("status UNKNOWN")
        if not self.evidence_ids:
            eksik.append("evidence_id yok")
        return eksik


@dataclass
class TornadoSatiri:
    """Tek eksenin çıktı üzerindeki etkisi."""
    eksen: Eksen
    dusuk_senaryo_sonuc: Decimal | None = None
    baz_sonuc: Decimal | None = None
    yuksek_senaryo_sonuc: Decimal | None = None
    salinim: Decimal | None = None          # |yuksek - dusuk|
    status: Status = Status.UNKNOWN
    not_: str = ""


@dataclass
class DuyarlilikSonucu:
    hesaplandi: bool
    status: Status
    eksenler: list[EksenAraligi] = field(default_factory=list)
    tornado: list[TornadoSatiri] = field(default_factory=list)
    kirilma_noktalari: dict[str, Any] = field(default_factory=dict)
    eksik_girdiler: list[str] = field(default_factory=list)
    uyarilar: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Yükleyici
# ---------------------------------------------------------------------------

def eksenleri_yukle(senaryolar_yaml: dict[str, Any]) -> list[EksenAraligi]:
    """
    senaryolar.yaml/duyarlilik_eksenleri -> EksenAraligi listesi.
    Eksik değerleri OLDUĞU GİBİ bırakır; varsayılan ATAMAZ.
    """
    araliklar: list[EksenAraligi] = []
    for satir in senaryolar_yaml.get("duyarlilik_eksenleri") or []:
        try:
            eksen = Eksen(satir.get("eksen"))
        except ValueError:
            continue

        status_raw = satir.get("status") or "UNKNOWN"
        try:
            status = Status(status_raw)
        except ValueError:
            status = Status.UNKNOWN

        araliklar.append(
            EksenAraligi(
                eksen=eksen,
                min=_dec(satir.get("min")),
                base=_dec(satir.get("base")),
                max=_dec(satir.get("max")),
                unit=satir.get("unit"),
                status=status,
                evidence_ids=[e for e in [satir.get("evidence_id")] if e],
                kaynak_dosya=satir.get("kaynak_dosya"),
            )
        )
    return araliklar


def _dec(v: Any) -> Decimal | None:
    if v is None:
        return None
    return Decimal(str(v))


# ---------------------------------------------------------------------------
# Ana giriş noktası
# ---------------------------------------------------------------------------

def calistir(
    veri: dict[str, Any],
    model_fn: Callable[..., Any] | None = None,
) -> DuyarlilikSonucu:
    """
    Duyarlılık analizini çalıştırır.

    TUR 0 DAVRANIŞI:
    ----------------
    Hesap yapmaz. Eksen tanımlarını yükler, hangi eksenin kullanılabilir
    olduğunu denetler, eksikleri raporlar ve `hesaplandi=False` döner.

    Duyarlılık analizi ancak `hesap.py` gerçek hesap yapabildiğinde
    anlamlıdır — TUR 0'da model hesap yapmadığı için burada da hesap
    yapılmaz. Sahte bir tornado grafiği, hiç grafik olmamasından daha
    yanıltıcıdır.
    """
    sonuc = DuyarlilikSonucu(hesaplandi=False, status=Status.UNKNOWN)

    senaryolar = veri.get("senaryolar.yaml") or {}
    sonuc.eksenler = eksenleri_yukle(senaryolar)

    if not sonuc.eksenler:
        sonuc.eksik_girdiler.append("senaryolar.yaml/duyarlilik_eksenleri bos.")

    for eksen in sonuc.eksenler:
        eksik = eksen.eksikler()
        if eksik:
            sonuc.eksik_girdiler.append(
                f"[{eksen.eksen.value}] " + "; ".join(eksik)
                + (f" (kaynak: {eksen.kaynak_dosya})" if eksen.kaynak_dosya else "")
            )
        sonuc.tornado.append(
            TornadoSatiri(
                eksen=eksen.eksen,
                status=Status.UNKNOWN,
                not_="HESAPLANMADI — TUR 0 iskeleti.",
            )
        )

    # Kırılma noktaları: TUR 3'te doldurulacak
    sonuc.kirilma_noktalari = {
        "contribution_sifirlanan_fx": None,
        "contribution_sifirlanan_freight": None,
        "contribution_sifirlanan_otv": None,
        "break_even_hacim_sise": None,
        "lcl_fcl_kirilma_sise": None,
        "kendi_dagitim_vs_distributor_kirilma_sise": None,
    }

    sonuc.uyarilar.append(
        "TUR 0: duyarlilik.py bilinçli olarak bos iskelettir. "
        "Model hesap yapmadigi surece duyarlilik de hesaplanmaz."
    )
    sonuc.uyarilar.append(
        "OTV ekseni f/p segmentte en oldurucu tek degiskendir — maktu OTV "
        "artisi tek basina senaryolari oldurebilir. TUR 3'te oncelikli incelenecek."
    )
    return sonuc


def rapor(sonuc: DuyarlilikSonucu) -> str:
    satirlar: list[str] = []
    satirlar.append("=" * 74)
    satirlar.append("DUYARLILIK ANALIZI")
    satirlar.append("=" * 74)
    satirlar.append(f"Durum      : {sonuc.status.value}")
    satirlar.append(f"Hesaplandi : {sonuc.hesaplandi}")

    if not sonuc.hesaplandi:
        satirlar.append("")
        satirlar.append(">>> DUYARLILIK HESAPLANMADI. SAHTE TORNADO URETILMEDI. <<<")

    if sonuc.eksenler:
        satirlar.append("")
        satirlar.append("EKSENLER:")
        for e in sonuc.eksenler:
            satirlar.append(
                f"  {e.eksen.value:<10} min={e.min or 'UNKNOWN':<10} "
                f"base={e.base or 'UNKNOWN':<10} max={e.max or 'UNKNOWN':<10} "
                f"[{e.status.value}]"
            )

    if sonuc.kirilma_noktalari:
        satirlar.append("")
        satirlar.append("KIRILMA NOKTALARI:")
        for k, v in sonuc.kirilma_noktalari.items():
            satirlar.append(f"  {k:<44} {v if v is not None else 'UNKNOWN'}")

    if sonuc.eksik_girdiler:
        satirlar.append("")
        satirlar.append(f"EKSIK GIRDILER ({len(sonuc.eksik_girdiler)}):")
        for e in sonuc.eksik_girdiler:
            satirlar.append(f"  - {e}")

    if sonuc.uyarilar:
        satirlar.append("")
        satirlar.append("UYARILAR:")
        for u in sonuc.uyarilar:
            satirlar.append(f"  ! {u}")

    satirlar.append("=" * 74)
    return "\n".join(satirlar)


if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from hesap import girdileri_yukle  # noqa: E402

    veri, hatalar = girdileri_yukle()
    if hatalar:
        print("GIRDI YUKLEME NOTLARI:")
        for h in hatalar:
            print(f"  - {h}")
        print()
    print(rapor(calistir(veri)))
