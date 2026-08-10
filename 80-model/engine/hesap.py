"""
hesap.py — MALİYET KATMANI MOTORU (BOŞ İSKELET)

===========================================================================
 TUR 0 — GÜVENLİ BOŞ İSKELET
===========================================================================
Bu modül L0 EXW'den L8 CONSUMER SHELF PRICE'a giden maliyet merdivenini
kurar. Şu an KASITLI OLARAK hesap yapmaz.

Kurallar (CLAUDE.md §6, §12):
  - Hicbir vergi orani burada HARD-CODE EDILMEZ. Vergi hesabi
    matrah_sirasi.py'ye devredilir, o da vergi.yaml'dan okur.
  - evidence_id'si olmayan sayi modele GIREMEZ.
  - Eksik girdi UYDURULMAZ; UNKNOWN doner ve eksik listesi raporlanir.
  - Katmanlar KARISTIRILMAZ. Her katman ayri saklanir.
  - KDV iki ayri perspektifte tutulur: ekonomik maliyet / cash timing.
===========================================================================
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from pathlib import Path
from typing import Any

from matrah_sirasi import (  # noqa: E402
    MatrahSonucu,
    Status,
    hesapla_vergi_zinciri,
    zincir_ozeti,
)

INPUTS_DIR = Path(__file__).resolve().parent.parent / "inputs"


# ---------------------------------------------------------------------------
# Maliyet katmanları — CLAUDE.md §6
# ---------------------------------------------------------------------------

class Katman(str, Enum):
    L0_EXW = "L0_EXW"
    L1_FOB = "L1_FOB"
    L2_CIF = "L2_CIF"
    L3_PRE_TAX_LANDED = "L3_PRE_TAX_LANDED"
    L4_POST_TAX_LANDED = "L4_POST_TAX_LANDED"
    L5_IMPORTER_COST = "L5_IMPORTER_COST"
    L6_IMPORTER_SELLING_PRICE = "L6_IMPORTER_SELLING_PRICE"
    L7_RETAILER_PURCHASE_PRICE = "L7_RETAILER_PURCHASE_PRICE"
    L8_CONSUMER_SHELF_PRICE = "L8_CONSUMER_SHELF_PRICE"


KATMAN_SIRASI: list[Katman] = list(Katman)


@dataclass
class KatmanDegeri:
    """Tek bir maliyet katmanının değeri ve izlenebilirliği."""
    katman: Katman
    value: Decimal | None = None
    currency: str | None = None
    status: Status = Status.UNKNOWN
    evidence_ids: list[str] = field(default_factory=list)
    # Bu katmana bir onceki katmandan gecerken eklenen kalemler
    eklenen_kalemler: list[tuple[str, Decimal | None, str | None]] = field(default_factory=list)
    notlar: list[str] = field(default_factory=list)


@dataclass
class KdvPerspektifi:
    """
    KDV asla tek satirda gosterilmez — CLAUDE.md §6.

    A) ekonomik maliyet / indirilebilirlik
    B) nakit akisindaki fiili odeme zamani (cash_tax_timing)
    """
    # A
    indirilebilir_mi: bool | None = None
    ekonomik_maliyete_giren_tutar: Decimal | None = None
    # B
    odeme_ani: str | None = None
    mahsup_gecikmesi_gun: int | None = None
    nakit_cikisi_tutari: Decimal | None = None
    status: Status = Status.UNKNOWN
    evidence_ids: list[str] = field(default_factory=list)


@dataclass
class NakitProfili:
    """peak_cash_requirement ve bilesenleri."""
    peak_cash_requirement: Decimal | None = None
    isletme_sermayesi: Decimal | None = None
    inventory_days: int | None = None
    cash_conversion_cycle_gun: int | None = None
    status: Status = Status.UNKNOWN
    eksikler: list[str] = field(default_factory=list)


@dataclass
class ModelSonucu:
    hesaplandi: bool
    status: Status
    yon: str                                   # FORWARD | REVERSE
    senaryo_id: str | None = None
    katmanlar: dict[Katman, KatmanDegeri] = field(default_factory=dict)
    vergi: MatrahSonucu | None = None
    kdv: KdvPerspektifi = field(default_factory=KdvPerspektifi)
    nakit: NakitProfili = field(default_factory=NakitProfili)
    eksik_girdiler: list[str] = field(default_factory=list)
    uyarilar: list[str] = field(default_factory=list)
    kullanilan_evidence_ids: list[str] = field(default_factory=list)
    status_dagilimi: dict[str, int] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Girdi yükleme
# ---------------------------------------------------------------------------

GEREKLI_INPUT_DOSYALARI = [
    "urun.yaml",
    "tedarikci.yaml",
    "lojistik.yaml",
    "vergi.yaml",
    "ruhsat.yaml",
    "kanal.yaml",
    "makro.yaml",
    "senaryolar.yaml",
]


def girdileri_yukle(inputs_dir: Path = INPUTS_DIR) -> tuple[dict[str, Any], list[str]]:
    """
    inputs/ altındaki YAML'ları yükler.

    PyYAML yoksa hata FIRLATMAZ ve DEĞER UYDURMAZ — boş sözlük ve
    açık bir eksik-girdi mesajı döner.
    """
    hatalar: list[str] = []
    veri: dict[str, Any] = {}

    try:
        import yaml  # type: ignore
    except ImportError:
        hatalar.append(
            "PyYAML kurulu degil (pip install pyyaml). "
            "Girdiler okunamadi — model UYDURMA yapmaz, UNKNOWN doner."
        )
        return veri, hatalar

    for dosya in GEREKLI_INPUT_DOSYALARI:
        yol = inputs_dir / dosya
        if not yol.exists():
            hatalar.append(f"Girdi dosyasi yok: {yol}")
            veri[dosya] = {}
            continue
        try:
            with yol.open("r", encoding="utf-8") as f:
                veri[dosya] = yaml.safe_load(f) or {}
        except Exception as exc:  # noqa: BLE001
            hatalar.append(f"{dosya} okunamadi: {exc}")
            veri[dosya] = {}

    return veri, hatalar


def evidence_denetimi(veri: dict[str, Any]) -> tuple[dict[str, int], list[str]]:
    """
    Girdilerdeki status dağılımını çıkarır ve evidence_id'siz FACT/ESTIMATE
    değerlerini yakalar.

    KURAL: evidence_id'si olmayan sayı modele GİREMEZ.
    """
    dagilim: dict[str, int] = {}
    ihlaller: list[str] = []

    def gez(dugum: Any, yol: str) -> None:
        if isinstance(dugum, dict):
            if "status" in dugum:
                st = str(dugum.get("status") or "UNKNOWN")
                dagilim[st] = dagilim.get(st, 0) + 1
                deger_var = dugum.get("value") is not None
                ev = dugum.get("evidence_id")
                if st in ("FACT", "ESTIMATE") and deger_var and not ev:
                    ihlaller.append(
                        f"{yol}: status={st} ve value dolu ama evidence_id YOK "
                        "-> modele GIREMEZ"
                    )
            for k, v in dugum.items():
                gez(v, f"{yol}.{k}" if yol else str(k))
        elif isinstance(dugum, list):
            for i, v in enumerate(dugum):
                gez(v, f"{yol}[{i}]")

    for dosya, icerik in veri.items():
        gez(icerik, dosya)

    return dagilim, ihlaller


# ---------------------------------------------------------------------------
# İleri model — L0 -> L8
# ---------------------------------------------------------------------------

def ileri_model(veri: dict[str, Any], senaryo_id: str | None = None) -> ModelSonucu:
    """
    EXW/FOB'dan tüketici raf fiyatına giden merdiven.

    TUR 0 DAVRANIŞI: hesap yapmaz. Katman iskeletini kurar, eksik girdileri
    listeler, `hesaplandi=False` döner.
    """
    sonuc = ModelSonucu(
        hesaplandi=False,
        status=Status.UNKNOWN,
        yon="FORWARD",
        senaryo_id=senaryo_id,
    )

    for katman in KATMAN_SIRASI:
        sonuc.katmanlar[katman] = KatmanDegeri(
            katman=katman,
            status=Status.UNKNOWN,
            notlar=["TUR 0 iskeleti — hesaplanmadi."],
        )

    vergi_yaml = veri.get("vergi.yaml") or {}
    sonuc.vergi = hesapla_vergi_zinciri(cif_degeri=None, vergi_yaml=vergi_yaml)
    sonuc.eksik_girdiler.extend(sonuc.vergi.eksik_girdiler)

    dagilim, ihlaller = evidence_denetimi(veri)
    sonuc.status_dagilimi = dagilim
    sonuc.eksik_girdiler.extend(ihlaller)

    sonuc.uyarilar.append(
        "TUR 0: hesap.py bilinçli olarak bos iskelettir. "
        "Katman gecisleri ve formuller TUR 3'te kanitli girdilerle yazilacaktir."
    )
    return sonuc


# ---------------------------------------------------------------------------
# Ters model — L8 -> L0/L1
# ---------------------------------------------------------------------------

def ters_model(
    veri: dict[str, Any],
    hedef_raf_fiyati: Decimal | None = None,
    benchmark_senaryo: str | None = None,
    kanal: "Any | None" = None,
    country: str | None = None,
    l5_kalemleri: "list[Any] | None" = None,
    **kw: Any,
) -> ModelSonucu:
    """
    PROJENİN ASIL SORUSU:
    Hedef raf fiyatını (L8) yakalayabilmek için üreticiye en fazla kaç
    dolar/euro ödeyebiliriz? (max L0 EXW / L1 FOB)

    UYARI — OPEN QUESTION #001:
    Benchmark'ın (599,90 TL) KDV dahil mi hariç mi, L7 mi L8 mi olduğu
    DOĞRULANMAMIŞTIR. Bu soru kapanana kadar ters model TEK BİR SAYIYLA
    çalıştırılamaz; BM_A (KDV dahil) ve BM_B (KDV hariç) senaryoları
    AYRI AYRI çalıştırılır ve fark raporlanır.

    TUR 2.5 DAVRANIŞI:
    `hedef_raf_fiyati` + `kanal` + `country` + `l5_kalemleri` verilirse GERÇEK
    ters zincir `ters_model.ters_zincir()` üzerinden çalıştırılır (R1..R11).
    Aksi hâlde eski iskelet davranışı korunur ve UNKNOWN döner.
    """
    if hedef_raf_fiyati is not None and kanal is not None and country is not None:
        from ters_model import ters_zincir  # yerel import — döngüsel bağımlılık yok

        ts = ters_zincir(
            veri.get("vergi.yaml") or {},
            l8_kdv_dahil=hedef_raf_fiyati,
            kanal=kanal,
            country=country,
            l5_kalemleri=l5_kalemleri or [],
            **kw,
        )
        sonuc = ModelSonucu(
            hesaplandi=ts.hesaplandi,
            status=Status.UNKNOWN if not ts.hesaplandi else Status.ESTIMATE,
            yon="REVERSE",
            senaryo_id=benchmark_senaryo,
        )
        for katman in KATMAN_SIRASI:
            sonuc.katmanlar[katman] = KatmanDegeri(katman=katman, status=Status.UNKNOWN)
        eslesme = {
            Katman.L2_CIF: ts.cif_try_max_upper_bound,
            Katman.L3_PRE_TAX_LANDED: ts.l3_pre_tax_landed_max,
            Katman.L4_POST_TAX_LANDED: ts.l4_econ_max,   # l4_econ — l4_cash AYRI
            Katman.L5_IMPORTER_COST: ts.l5_max,
            Katman.L6_IMPORTER_SELLING_PRICE: ts.l6,
            Katman.L7_RETAILER_PURCHASE_PRICE: ts.l7_eff,
            Katman.L8_CONSUMER_SHELF_PRICE: ts.l8_kdv_dahil,
        }
        for k, val in eslesme.items():
            sonuc.katmanlar[k] = KatmanDegeri(
                katman=k, value=val, currency="TRY",
                status=Status.ESTIMATE if val is not None else Status.UNKNOWN,
            )
        sonuc.katmanlar[Katman.L4_POST_TAX_LANDED].notlar.append(
            f"l4_econ (KDV HARIC). l4_cash = {ts.l4_cash_max} AYRI ALANDIR, "
            f"TOPLANMAZ (R7-K3 / RC3)."
        )
        sonuc.kdv = KdvPerspektifi(
            indirilebilir_mi=True,
            ekonomik_maliyete_giren_tutar=Decimal("0"),
            odeme_ani="gumrukte, beyanname tescilinde",
            nakit_cikisi_tutari=ts.kdv_ithal_nakit,
            status=Status.FACT,
            evidence_ids=["EV-2026-08-10-101", "EV-2026-08-10-102", "EV-2026-08-10-103"],
        )
        sonuc.eksik_girdiler.extend(ts.eksik_girdiler)
        sonuc.uyarilar.extend(ts.uyarilar + ts.etiketler)
        sonuc.kullanilan_evidence_ids.extend(ts.kullanilan_evidence_ids)
        return sonuc

    sonuc = ModelSonucu(
        hesaplandi=False,
        status=Status.UNKNOWN,
        yon="REVERSE",
        senaryo_id=benchmark_senaryo,
    )

    for katman in KATMAN_SIRASI:
        sonuc.katmanlar[katman] = KatmanDegeri(
            katman=katman,
            status=Status.UNKNOWN,
            notlar=["TUR 0 iskeleti — hesaplanmadi."],
        )

    if benchmark_senaryo is None:
        sonuc.eksik_girdiler.append(
            "benchmark_senaryo verilmedi. OPEN QUESTION #001 acikken ters model "
            "BM_A (KDV dahil) ve BM_B (KDV haric) icin AYRI calistirilmalidir."
        )

    if hedef_raf_fiyati is None:
        sonuc.eksik_girdiler.append(
            "hedef_raf_fiyati (L8) verilmedi. Benchmark tek basina kullanilamaz "
            "— bkz. 00-charter/benchmark.md"
        )

    vergi_yaml = veri.get("vergi.yaml") or {}
    sonuc.vergi = hesapla_vergi_zinciri(cif_degeri=None, vergi_yaml=vergi_yaml)
    sonuc.eksik_girdiler.extend(sonuc.vergi.eksik_girdiler)

    dagilim, ihlaller = evidence_denetimi(veri)
    sonuc.status_dagilimi = dagilim
    sonuc.eksik_girdiler.extend(ihlaller)

    sonuc.uyarilar.append("TUR 0: ters model iskeleti — hesaplanmadi.")
    return sonuc


# ---------------------------------------------------------------------------
# Raporlama
# ---------------------------------------------------------------------------

def rapor(sonuc: ModelSonucu) -> str:
    satirlar: list[str] = []
    satirlar.append("=" * 74)
    satirlar.append(f"MODEL CIKTISI — yon={sonuc.yon} senaryo={sonuc.senaryo_id or '-'}")
    satirlar.append("=" * 74)
    satirlar.append(f"Durum      : {sonuc.status.value}")
    satirlar.append(f"Hesaplandi : {sonuc.hesaplandi}")
    satirlar.append("Cikti tipi : DRAFT  (APPROVED degil)")

    if not sonuc.hesaplandi:
        satirlar.append("")
        satirlar.append(">>> MODEL HESAP YAPMADI. UYDURMA SAYI URETILMEDI. <<<")

    satirlar.append("")
    satirlar.append("MALIYET KATMANLARI:")
    for katman in KATMAN_SIRASI:
        kd = sonuc.katmanlar.get(katman)
        if kd is None:
            continue
        deger = "UNKNOWN" if kd.value is None else f"{kd.value} {kd.currency or ''}"
        satirlar.append(f"  {katman.value:<28} {deger:<20} [{kd.status.value}]")

    satirlar.append("")
    satirlar.append("KDV — IKI PERSPEKTIF:")
    satirlar.append(f"  A) ekonomik maliyet   : indirilebilir_mi={sonuc.kdv.indirilebilir_mi} "
                    f"[{sonuc.kdv.status.value}]")
    satirlar.append(f"  B) cash_tax_timing    : odeme_ani={sonuc.kdv.odeme_ani} "
                    f"mahsup_gecikmesi_gun={sonuc.kdv.mahsup_gecikmesi_gun}")

    satirlar.append("")
    satirlar.append("NAKIT PROFILI:")
    satirlar.append(f"  peak_cash_requirement : {sonuc.nakit.peak_cash_requirement or 'UNKNOWN'}")
    satirlar.append(f"  isletme_sermayesi     : {sonuc.nakit.isletme_sermayesi or 'UNKNOWN'}")
    satirlar.append(f"  inventory_days        : {sonuc.nakit.inventory_days or 'UNKNOWN'}")
    satirlar.append(f"  cash_conversion_cycle : {sonuc.nakit.cash_conversion_cycle_gun or 'UNKNOWN'}")

    if sonuc.status_dagilimi:
        satirlar.append("")
        satirlar.append("GIRDI STATUS DAGILIMI:")
        for st, adet in sorted(sonuc.status_dagilimi.items()):
            satirlar.append(f"  {st:<12} {adet}")

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


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    veri, hatalar = girdileri_yukle()

    print("=" * 74)
    print("WINE IMPORT FEASIBILITY TURKEY — MODEL (TUR 0 ISKELET)")
    print("=" * 74)
    if hatalar:
        print("\nGIRDI YUKLEME NOTLARI:")
        for h in hatalar:
            print(f"  - {h}")

    ileri = ileri_model(veri)
    print()
    print(rapor(ileri))

    ters = ters_model(veri)
    print()
    print(rapor(ters))

    if ileri.vergi is not None:
        print()
        print(zincir_ozeti(ileri.vergi))

    print()
    print("TUR 0 tamamlandi. Gercek hesap TUR 3'te, kanitli girdilerle yapilacaktir.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
