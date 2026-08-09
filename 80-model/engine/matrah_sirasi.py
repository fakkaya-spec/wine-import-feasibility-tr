"""
matrah_sirasi.py — VERGİ MATRAH SIRASI MOTORU (BOŞ İSKELET)

===========================================================================
 GÜVENLİK KİLİDİ
===========================================================================
Bu dosyada HİÇBİR vergi oranı, ÖTV tutarı, KDV oranı, KKDF oranı veya
matrah tanımı HARD-CODE EDİLMEZ.

Bütün değerler `80-model/inputs/vergi.yaml` dosyasından okunur ve o dosya
`30-vergi-gumruk/matrah-sirasi.md` (tek doğruluk kaynağı) ile birebir
tutarlı olmalıdır.

`vergi.yaml` içinde `a1_dogrulama_yapildi_mi: false` olduğu sürece bu modül
HESAP YAPMAZ. `UNKNOWN` döner ve eksik girdileri raporlar.

TUR 0 durumu: iskelet. Gerçek vergi formülü TUR 1'de gumruk-vergi-uzmani
A1 doğrulamasını tamamladıktan sonra yazılır.
===========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import Any


# ---------------------------------------------------------------------------
# Statü etiketleri — CLAUDE.md §3
# ---------------------------------------------------------------------------

class Status(str, Enum):
    FACT = "FACT"
    ESTIMATE = "ESTIMATE"
    ASSUMPTION = "ASSUMPTION"
    UNKNOWN = "UNKNOWN"
    CONFLICT = "CONFLICT"
    SUPERSEDED = "SUPERSEDED"


class VergiTipi(str, Enum):
    ORANSAL = "ORANSAL"
    MAKTU = "MAKTU"
    KARMA_YUKSEK_OLAN = "KARMA_YUKSEK_OLAN"
    YOK = "YOK"


# ---------------------------------------------------------------------------
# Veri yapıları
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class VergiKalemi:
    """vergi.yaml -> matrah_sirasi[] içindeki bir satırın karşılığı."""
    sira: int
    vergi: str
    matrah_tanimi: str | None = None
    oran_pct: Decimal | None = None
    tutar: Decimal | None = None
    tip: VergiTipi | None = None
    status: Status = Status.UNKNOWN
    tier: str | None = None
    evidence_id: str | None = None
    effective_date: str | None = None

    def hesaplanabilir_mi(self) -> bool:
        """
        Bir kalem yalnızca şu koşulların HEPSİ sağlanırsa hesaplanabilir:
          - status FACT
          - evidence_id dolu
          - effective_date dolu
          - matrah_tanimi dolu
          - tip belirli
        Aksi hâlde hesap yapılmaz; UNKNOWN döner.
        """
        return (
            self.status is Status.FACT
            and bool(self.evidence_id)
            and bool(self.effective_date)
            and bool(self.matrah_tanimi)
            and self.tip is not None
        )

    def eksikler(self) -> list[str]:
        eksik: list[str] = []
        if self.status is not Status.FACT:
            eksik.append(f"status={self.status.value} (FACT olmali)")
        if not self.evidence_id:
            eksik.append("evidence_id yok")
        if not self.effective_date:
            eksik.append("effective_date yok")
        if not self.matrah_tanimi:
            eksik.append("matrah_tanimi yok")
        if self.tip is None:
            eksik.append("tip (ORANSAL/MAKTU/KARMA) yok")
        return eksik


@dataclass
class MatrahAdimi:
    """Hesaplanmış tek bir vergi adımının izlenebilir kaydı."""
    sira: int
    vergi: str
    matrah_tanimi: str | None
    matrah_degeri: Decimal | None
    vergi_tutari: Decimal | None
    status: Status
    evidence_id: str | None
    aciklama: str


@dataclass
class MatrahSonucu:
    """
    Vergi zincirinin tam çıktısı.

    `hesaplandi=False` ise `vergi_toplami` ve `post_tax_landed` GÜVENİLMEZDİR
    ve None'dır. Bu durumda `eksik_girdiler` doldurulur.
    """
    hesaplandi: bool
    status: Status
    adimlar: list[MatrahAdimi] = field(default_factory=list)
    vergi_toplami: Decimal | None = None
    post_tax_landed: Decimal | None = None
    kullanilan_evidence_ids: list[str] = field(default_factory=list)
    eksik_girdiler: list[str] = field(default_factory=list)
    uyarilar: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Yükleyici
# ---------------------------------------------------------------------------

def vergi_kalemlerini_yukle(vergi_yaml: dict[str, Any]) -> list[VergiKalemi]:
    """
    vergi.yaml sözlüğünden VergiKalemi listesi üretir.

    Eksik/None alanları OLDUĞU GİBİ bırakır — varsayılan değer ATAMAZ.
    Boşluğu doldurmak bu modülün işi değildir.
    """
    kalemler: list[VergiKalemi] = []
    for satir in vergi_yaml.get("matrah_sirasi") or []:
        tip_raw = satir.get("tip")
        try:
            tip = VergiTipi(tip_raw) if tip_raw else None
        except ValueError:
            tip = None

        status_raw = satir.get("status") or "UNKNOWN"
        try:
            status = Status(status_raw)
        except ValueError:
            status = Status.UNKNOWN

        kalemler.append(
            VergiKalemi(
                sira=satir.get("sira", 0),
                vergi=satir.get("vergi", "BILINMEYEN"),
                matrah_tanimi=satir.get("matrah_tanimi"),
                oran_pct=_dec(satir.get("oran_pct")),
                tutar=_dec(satir.get("tutar")),
                tip=tip,
                status=status,
                tier=satir.get("tier"),
                evidence_id=satir.get("evidence_id"),
                effective_date=satir.get("effective_date"),
            )
        )
    kalemler.sort(key=lambda k: k.sira)
    return kalemler


def _dec(v: Any) -> Decimal | None:
    if v is None:
        return None
    return Decimal(str(v))


# ---------------------------------------------------------------------------
# Ana giriş noktası
# ---------------------------------------------------------------------------

def hesapla_vergi_zinciri(
    cif_degeri: Decimal | None,
    vergi_yaml: dict[str, Any],
) -> MatrahSonucu:
    """
    CIF (L2) girdisinden başlayarak vergi zincirini hesaplar.

    TUR 0 DAVRANIŞI:
    ----------------
    Bu fonksiyon şu an KASITLI OLARAK hesap yapmaz. Her zaman
    `hesaplandi=False`, `status=UNKNOWN` döner ve eksik girdileri listeler.

    Bunun sebebi CLAUDE.md §12'deki güvenlik kilididir:
    A1 seviyesinde resmî mevzuatla doğrulanmamış hiçbir oran/matrah
    kullanılamaz. Uydurulmuş bir vergi hesabı, hiç hesap olmamasından
    DAHA TEHLİKELİDİR.

    TUR 1'de gumruk-vergi-uzmani `vergi.yaml`'ı T1/T2 kanıtlarla doldurup
    `a1_dogrulama_yapildi_mi: true` yaptığında, gerçek zincir mantığı
    `30-vergi-gumruk/matrah-sirasi.md`'den birebir aktarılarak buraya yazılır.
    """
    sonuc = MatrahSonucu(hesaplandi=False, status=Status.UNKNOWN)

    meta = vergi_yaml.get("meta") or {}
    a1_ok = bool(meta.get("a1_dogrulama_yapildi_mi"))

    if not a1_ok:
        sonuc.eksik_girdiler.append(
            "vergi.yaml/meta.a1_dogrulama_yapildi_mi = false "
            "-> A1 resmi mevzuat dogrulamasi YAPILMAMIS. Vergi hesabi calistirilmaz."
        )

    if meta.get("model_hedef_tarihi") is None:
        sonuc.eksik_girdiler.append(
            "vergi.yaml/meta.model_hedef_tarihi = null "
            "-> Hangi tarihte gecerli oranlarin kullanilacagi belirsiz."
        )

    if cif_degeri is None:
        sonuc.eksik_girdiler.append("cif_degeri (L2) girdisi yok.")

    kalemler = vergi_kalemlerini_yukle(vergi_yaml)
    if not kalemler:
        sonuc.eksik_girdiler.append("vergi.yaml/matrah_sirasi bos.")

    for k in kalemler:
        eksik = k.eksikler()
        if eksik:
            sonuc.eksik_girdiler.append(
                f"[sira {k.sira}] {k.vergi}: " + "; ".join(eksik)
            )
        else:
            if k.evidence_id:
                sonuc.kullanilan_evidence_ids.append(k.evidence_id)

        sonuc.adimlar.append(
            MatrahAdimi(
                sira=k.sira,
                vergi=k.vergi,
                matrah_tanimi=k.matrah_tanimi,
                matrah_degeri=None,
                vergi_tutari=None,
                status=k.status,
                evidence_id=k.evidence_id,
                aciklama=(
                    "HESAPLANMADI — TUR 0 iskeleti. "
                    "A1 dogrulamasi tamamlanana kadar vergi hesabi yapilmaz."
                ),
            )
        )

    sonuc.uyarilar.append(
        "TUR 0: matrah_sirasi.py bilinçli olarak bos iskelettir. "
        "Hicbir oran hard-code edilmemistir."
    )
    return sonuc


def zincir_ozeti(sonuc: MatrahSonucu) -> str:
    """İnsan okunur özet. Hesap yapılmadıysa bunu AÇIKÇA söyler."""
    satirlar: list[str] = []
    satirlar.append("=" * 70)
    satirlar.append("VERGI MATRAH ZINCIRI")
    satirlar.append("=" * 70)
    satirlar.append(f"Durum      : {sonuc.status.value}")
    satirlar.append(f"Hesaplandi : {sonuc.hesaplandi}")

    if not sonuc.hesaplandi:
        satirlar.append("")
        satirlar.append(">>> VERGI HESABI YAPILMADI. UYDURMA DEGER URETILMEDI. <<<")

    if sonuc.adimlar:
        satirlar.append("")
        satirlar.append("Adimlar:")
        for a in sonuc.adimlar:
            satirlar.append(
                f"  {a.sira}. {a.vergi:<24} "
                f"matrah={a.matrah_tanimi or 'UNKNOWN':<20} "
                f"status={a.status.value:<10} "
                f"ev={a.evidence_id or '-'}"
            )

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

    satirlar.append("=" * 70)
    return "\n".join(satirlar)
