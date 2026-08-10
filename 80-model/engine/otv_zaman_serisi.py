"""
otv_zaman_serisi.py — ÖTV MAKTU TUTARI: ZAMAN SERİSİ OKUYUCU + UFUK DENETİMİ

===========================================================================
 T-921 (CRITICAL) KAPANIŞ MODÜLÜ
===========================================================================
Başkanın tespiti (90-karar/tur-25-preflight.md §1.4.2):

  "Engine `otv_maktu_zaman_serisi` blogunu HİÇ OKUMUYOR. Tarihle ilgili tek
   kontrol matrah_sirasi.py:217'deki `model_hedef_tarihi is None`. Hedef tarih
   2027-04-01 yapılınca bu tek uyarı sustu; 2027-04-01 >
   son_gozlem_gecerlilik_ufku (2026-12-31) olmasına rağmen engine ÖTV'yi
   hesaplanabilir sayıyor."

Bu modül o boşluğu kapatır. Uyguladığı kural METİN OLARAK ŞURADADIR ve
KODA GÖMÜLMEMİŞTİR:
    vergi.yaml -> otv_maktu_zaman_serisi.engine_okuma_kurali
    vergi.yaml -> otv_maktu_zaman_serisi.engine_yasak
    vergi.yaml -> ters_model_vergi_bacagi.otv_hedef_tarih_tasima.calistirma_kurallari (O-1..O-7)

GÜVENLİK KİLİDİ (CLAUDE.md §12):
  - Bu dosyada HİÇBİR ÖTV tutarı, oranı veya tarihi HARD-CODE EDİLMEZ.
  - `son_gozlem_gecerlilik_ufku` dosyadan okunur.
  - t > ufuk VE açık bir senaryo bayrağı YOKSA  ->  UNKNOWN döner.
  - Açık bayrak (`UPPER_BOUND_LAMBDA_1`) verildiğinde hesaplar AMA çıktıyı
    `UPPER_BOUND` olarak etiketler ve O-2/O-3/O-5/O-6 etiketlerini zorunlu
    olarak taşır.
  - 2027 ÖTV tutarı HİÇBİR YERDE yazılmaz, tahmin edilmez, türetilmez.
===========================================================================
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from typing import Any

# ---------------------------------------------------------------------------
# Senaryo bayrakları — çağıranın AÇIKÇA vermesi gerekir
# ---------------------------------------------------------------------------

#: Ufuk ötesinde hesap yapılmasına izin veren TEK açık bayrak.
#: lambda = 1 (CURRENT_CONFIRMED) ile çalışır; sonuç bir TAHMİN DEĞİL ÜST SINIRDIR.
OTV_SENARYO_UPPER_BOUND_LAMBDA_1 = "UPPER_BOUND_LAMBDA_1"

#: Açık bir Yİ-ÜFE ASSUMPTION'ı ile projeksiyon (O-4). lambda > 1 verilir.
OTV_SENARYO_PROJEKSIYON = "PROJEKSIYON_ASSUMPTION"


@dataclass
class OtvOkumasi:
    """otv_maktu(t) fonksiyonunun izlenebilir çıktısı."""
    hesaplandi: bool
    status: str                       # FACT | UPPER_BOUND | PROJEKSIYON_ASSUMPTION | UNKNOWN
    maktu_try_per_litre: Decimal | None = None
    otv_try_per_sise: Decimal | None = None
    lambda_katsayisi: Decimal | None = None
    secilen_effective_date: str | None = None
    evidence_id: str | None = None
    tier: str | None = None
    kullanilan_tarih: str | None = None
    ufuk: str | None = None
    ufuk_asildi_mi: bool = False
    upper_bound_mu: bool = False
    etiketler: list[str] = field(default_factory=list)
    eksik_girdiler: list[str] = field(default_factory=list)
    uyarilar: list[str] = field(default_factory=list)


def _d(v: Any) -> Decimal | None:
    if v is None:
        return None
    return Decimal(str(v))


def _tarih(v: Any) -> date | None:
    if v is None:
        return None
    if isinstance(v, date):
        return v
    try:
        return date.fromisoformat(str(v))
    except ValueError:
        return None


def otv_maktu(
    vergi_yaml: dict[str, Any],
    t: str | date | None = None,
    otv_senaryo: str | None = None,
    lambda_katsayisi: Decimal | float | None = None,
) -> OtvOkumasi:
    """
    `otv_maktu_zaman_serisi.engine_okuma_kurali`nı BİREBİR uygular.

    1) t = model_hedef_tarihi; t null/TBD ise t = meta.BASE_DATE.
    2) gozlenen_degerler içinde effective_date <= t olan EN SON kaydı seç.
    3) EĞER t > son_gozlem_gecerlilik_ufku İSE:
         - açık senaryo bayrağı YOKSA -> UNKNOWN + eksik girdi raporu
         - `UPPER_BOUND_LAMBDA_1`     -> lambda = 1, status = UPPER_BOUND (O-1/O-3)
         - `PROJEKSIYON_ASSUMPTION`   -> lambda çağırandan, status = PROJEKSIYON
    4) otv_per_sise = otv_maktu(t) * lambda * urun_parametreleri.sise_hacmi_litre
    5) effective_date + evidence_id ZORUNLU olarak çıktıya yazılır.
    """
    sonuc = OtvOkumasi(hesaplandi=False, status="UNKNOWN")

    meta = vergi_yaml.get("meta") or {}
    seri = vergi_yaml.get("otv_maktu_zaman_serisi") or {}

    if not seri:
        sonuc.eksik_girdiler.append(
            "vergi.yaml/otv_maktu_zaman_serisi BLOGU YOK -> OTV okunamaz."
        )
        return sonuc

    # ---- 1) tarih -------------------------------------------------------
    hedef = _tarih(t) or _tarih(meta.get("model_hedef_tarihi"))
    base_date = _tarih(meta.get("BASE_DATE"))
    if hedef is None:
        hedef = base_date
        sonuc.uyarilar.append(
            "model_hedef_tarihi null/TBD -> BASE_DATE kullanildi "
            "(engine_okuma_kurali adim 1)."
        )
    if hedef is None:
        sonuc.eksik_girdiler.append(
            "Ne model_hedef_tarihi ne BASE_DATE okunabildi -> tarih UNKNOWN."
        )
        return sonuc
    sonuc.kullanilan_tarih = hedef.isoformat()

    # ---- T-921 kabul kriteri #4: model_hedef_tarihi_status denetimi -----
    mht_status = meta.get("model_hedef_tarihi_status")
    if meta.get("model_hedef_tarihi") is not None and mht_status != "FACT":
        sonuc.etiketler.append(
            f"HEDEF TARIH {hedef.isoformat()} — model_hedef_tarihi_status="
            f"{mht_status or 'YOK'} (FACT DEGIL). Cikti "
            f"'{mht_status or 'BILINMEYEN'} uzerinden' hesaplanmistir."
        )

    # ---- 2) gözlenen değerlerden seçim ---------------------------------
    gozlemler = seri.get("gozlenen_degerler") or []
    uygun = []
    for g in gozlemler:
        ed = _tarih(g.get("effective_date"))
        if ed is not None and ed <= hedef:
            uygun.append((ed, g))
    if not uygun:
        sonuc.eksik_girdiler.append(
            "otv_maktu_zaman_serisi.gozlenen_degerler icinde effective_date <= t "
            "olan kayit YOK -> OTV UNKNOWN."
        )
        return sonuc
    uygun.sort(key=lambda x: x[0])
    secilen_tarih, secilen = uygun[-1]

    maktu = _d(secilen.get("value"))
    sonuc.secilen_effective_date = secilen_tarih.isoformat()
    sonuc.evidence_id = secilen.get("evidence_id")
    sonuc.tier = secilen.get("tier")

    if maktu is None or not sonuc.evidence_id:
        sonuc.eksik_girdiler.append(
            "Secilen otv gozlemi eksik (value veya evidence_id yok) -> UNKNOWN."
        )
        return sonuc

    # ---- engine_yasak denetimi: kisayol alani ile celiski kontrolu -----
    kisayol = None
    for satir in vergi_yaml.get("matrah_sirasi") or []:
        if satir.get("sira") == 4:
            kisayol = _d(satir.get("asgari_maktu_tutar"))
    if kisayol is not None and maktu is not None and kisayol != maktu:
        sonuc.uyarilar.append(
            f"engine_yasak: matrah_sirasi[sira=4].asgari_maktu_tutar={kisayol} ile "
            f"otv_maktu_zaman_serisi={maktu} CELISIYOR. SERI ESAS ALINDI."
        )

    # ---- 3) UFUK DENETİMİ — T-921'in ÇEKİRDEĞİ -------------------------
    ufuk = _tarih(seri.get("son_gozlem_gecerlilik_ufku"))
    sonuc.ufuk = ufuk.isoformat() if ufuk else None
    lam = Decimal("1")

    if ufuk is not None and hedef > ufuk:
        sonuc.ufuk_asildi_mi = True

        if otv_senaryo is None:
            sonuc.status = "UNKNOWN"
            sonuc.eksik_girdiler.append(
                f"otv_maktu_zaman_serisi.gelecek_degerler = null. "
                f"model_hedef_tarihi ({hedef.isoformat()}) > "
                f"son_gozlem_gecerlilik_ufku ({ufuk.isoformat()}) ve "
                f"senaryolar.yaml'da SECILMIS bir OTV artis ASSUMPTION'i YOK -> "
                f"engine UNKNOWN doner (engine_okuma_kurali adim 3, O-5, T-921)."
            )
            sonuc.uyarilar.append(
                "CURRENT_CONFIRMED tutari bu tarih icin 'gecerli tutar' olarak "
                "KULLANILMADI (vergi.yaml -> tarih_senaryolari.yasak)."
            )
            return sonuc

        if otv_senaryo == OTV_SENARYO_UPPER_BOUND_LAMBDA_1:
            lam = Decimal("1")
            sonuc.status = "UPPER_BOUND"
            sonuc.upper_bound_mu = True
            sonuc.etiketler.extend([
                # O-2 (metin vergi.yaml'dan okunur, burada sabitlenmez)
                f"O-2: OTV = CURRENT_CONFIRMED ({maktu} TRY/litre, eff "
                f"{secilen_tarih.isoformat()}) — HEDEF TARIHTE ({hedef.isoformat()}) "
                f"YURURLUKTE OLMASI BEKLENMEZ.",
                "O-3: lambda >= 1 oldugu icin lambda=1 sonucu bir TAHMIN DEGIL "
                "UST SINIRDIR. Cikti alani adi cif_try_max_UPPER_BOUND'dur.",
                "O-5: PROJEKSIYON DEGIL, CAPA (ANCHOR). engine_okuma_kurali "
                "DELINMEMISTIR; acik bayrak ile calistirilmistir.",
                "O-6: Bu OTV degeri hedef tarih icin ASLA FACT olarak raporlanamaz.",
            ])
        elif otv_senaryo == OTV_SENARYO_PROJEKSIYON:
            lam = _d(lambda_katsayisi)
            if lam is None:
                sonuc.status = "UNKNOWN"
                sonuc.eksik_girdiler.append(
                    "PROJEKSIYON_ASSUMPTION secildi ama lambda verilmedi -> UNKNOWN."
                )
                return sonuc
            if lam < 1:
                sonuc.uyarilar.append(
                    "lambda < 1 verildi. vergi.yaml alt_sinir = 1.0 "
                    "(Yi-UFE negatif olmadikca). Deger AYNEN kullanildi ama SUPHELIDIR."
                )
            sonuc.status = "PROJEKSIYON_ASSUMPTION"
            sonuc.etiketler.extend([
                f"O-4: lambda={lam} bir DUYARLILIK EKSENI noktasidir "
                f"(senaryolar.yaml -> duyarlilik_eksenleri[OTV]."
                f"talep_edilen_senaryo_noktalari, kaynak ticket T-104).",
                "PROJEKSIYON (ASSUMPTION) — ASLA FACT olarak raporlanamaz.",
                f"O-2: capa deger {maktu} TRY/litre, eff {secilen_tarih.isoformat()}.",
            ])
        else:
            sonuc.status = "UNKNOWN"
            sonuc.eksik_girdiler.append(
                f"Bilinmeyen otv_senaryo bayragi: {otv_senaryo!r} -> UNKNOWN."
            )
            return sonuc
    else:
        # Ufuk icinde: gozlenen deger dogrudan gecerlidir.
        sonuc.status = "FACT"
        sonuc.etiketler.append(
            f"t={hedef.isoformat()} <= ufuk; gozlenen tutar dogrudan gecerlidir."
        )

    # ---- 4) şişe başına ------------------------------------------------
    urun = (vergi_yaml.get("urun_parametreleri") or {}).get("sise_hacmi_litre") or {}
    hacim = _d(urun.get("value"))
    if hacim is None:
        sonuc.eksik_girdiler.append(
            "urun_parametreleri.sise_hacmi_litre YOK -> OTV/sise hesaplanamaz."
        )
        sonuc.status = "UNKNOWN"
        return sonuc

    sonuc.lambda_katsayisi = lam
    sonuc.maktu_try_per_litre = maktu * lam
    sonuc.otv_try_per_sise = maktu * lam * hacim
    sonuc.hesaplandi = True

    if urun.get("status") != "FACT":
        sonuc.uyarilar.append(
            f"sise_hacmi_litre status={urun.get('status')} "
            f"(evidence_id={urun.get('evidence_id')}) — bir DIS OLGU degil, "
            f"kapsam kararidir."
        )
    return sonuc
