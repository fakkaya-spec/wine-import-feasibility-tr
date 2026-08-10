"""
test_ters_model.py — `vergi.yaml -> ters_model_vergi_bacagi.birim_test_vektorleri`

10 vektörün 10'u da BURADAN OKUNUR; beklenen değerler koda GÖMÜLMEZ.
`T-751` kabul kriteri #2'nin karşılığıdır.

Çalıştırma:  python3 80-model/engine/test_ters_model.py
"""

from __future__ import annotations

import sys
from decimal import Decimal
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml  # noqa: E402

from otv_zaman_serisi import (  # noqa: E402
    OTV_SENARYO_UPPER_BOUND_LAMBDA_1,
    otv_maktu,
)
from ters_model import (  # noqa: E402
    KanalGirdisi,
    L5Kalemi,
    ileri_l4_econ,
    r7_adim_sirasini_oku,
    r7_coz,
    ters_zincir,
)

INPUTS = Path(__file__).resolve().parent.parent / "inputs"
TOL = Decimal("0.0001")


def _yukle() -> dict:
    with (INPUTS / "vergi.yaml").open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def _q(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.0001"))


def calistir() -> tuple[int, int, list[tuple[str, str, str, bool]]]:
    vergi = _yukle()
    blok = vergi["ters_model_vergi_bacagi"]["birim_test_vektorleri"]
    sabitler = blok["sabitler"]
    O = Decimal(str(sabitler["otv_per_sise"]))
    K = Decimal(str(sabitler["kkdf"]))
    XP = Decimal(str(sabitler["X_pre"]))
    V = Decimal(str(sabitler["kdv_orani"]))

    r7_sira, _ = r7_adim_sirasini_oku(vergi)
    sonuclar: list[tuple[str, str, str, bool]] = []
    tv = {v["kod"]: v for v in blok["vektorler"]}

    # ---- TV-1 / TV-2 : doğru cebir --------------------------------------
    cif = {}
    for kod in ("TV-1", "TV-2"):
        g = Decimal(str(tv[kod]["girdi"]["gv_orani"]))
        l4 = Decimal(str(tv[kod]["girdi"]["L4_econ_max"]))
        beklenen = Decimal(str(tv[kod]["beklenen_cif_try_max"]))
        c, _ = r7_coz(l4, O, K, XP, g, r7_sira)
        cif[kod] = c
        ok = abs(c - beklenen) < TOL
        # ileri yön doğrulaması (R8)
        geri = ileri_l4_econ(c, g, K, O, XP)
        ok = ok and abs(geri - l4) < Decimal("0.01")
        sonuclar.append((kod, str(beklenen), str(_q(c)), ok))

    # ---- TV-3 : oran ----------------------------------------------------
    oran = cif["TV-2"] / cif["TV-1"]
    ok3 = abs(oran - Decimal("0.88235")) < Decimal("0.00001")
    sonuclar.append(("TV-3", "0.88235", str(oran.quantize(Decimal("0.00001"))), ok3))

    # ---- TV-4 : KDV nakit örtüsü, menşeden bağımsız ---------------------
    l4 = Decimal(str(tv["TV-1"]["girdi"]["L4_econ_max"]))
    kdv_ithal = V * l4
    ok4 = abs(kdv_ithal - Decimal("40.0000")) < TOL
    sonuclar.append(("TV-4", "40.0000", str(_q(kdv_ithal)), ok4))

    # ---- TV-5 : l4_cash --------------------------------------------------
    l4_cash = l4 + kdv_ithal
    ok5 = abs(l4_cash - Decimal("240.0000")) < TOL
    sonuclar.append(("TV-5", "240.0000", str(_q(l4_cash)), ok5))

    # ---- TV-6 / TV-7 : H1 hatası (yanlış sıra) YAKALANIYOR mu -----------
    for kod, g in (("TV-6", Decimal("0.50")), ("TV-7", Decimal("0.70"))):
        yanlis_beklenen = Decimal(str(tv[kod]["yanlis_sonuc"]))
        dogru_beklenen = Decimal(str(tv[kod]["dogru_sonuc"]))
        # H1: önce böl, sonra çıkar
        yanlis, _ = r7_coz(l4, O, K, XP, g, ["R7a", "R7d", "R7b", "R7c"])
        dogru, _ = r7_coz(l4, O, K, XP, g, r7_sira)
        ok = (abs(yanlis - yanlis_beklenen) < TOL
              and abs(dogru - dogru_beklenen) < TOL
              and dogru != yanlis)
        # R8 yanlış sonucu REDDETMELİ
        r8_yanlis = abs(ileri_l4_econ(yanlis, g, K, O, XP) - l4) < Decimal("0.01")
        ok = ok and (r8_yanlis is False)
        sonuclar.append(
            (kod, f"yanlis={yanlis_beklenen} dogru={dogru_beklenen}",
             f"yanlis={_q(yanlis)} dogru={_q(dogru)} R8_yanlisi_reddetti={not r8_yanlis}",
             ok)
        )

    # ---- TV-8 : H3 hatası (l4_cash <-> l4_econ) -------------------------
    g = Decimal("0.50")
    yanlis_beklenen = Decimal(str(tv["TV-8"]["yanlis_sonuc"]))
    dogru_beklenen = Decimal(str(tv["TV-8"]["dogru_sonuc"]))
    # H3: L4_econ_max yerine L4_cash tanımı kullanılırsa (yani L4_econ/1.2)
    l4_yanlis = l4 / (Decimal("1") + V)
    yanlis, _ = r7_coz(l4_yanlis, O, K, XP, g, r7_sira)
    dogru, _ = r7_coz(l4, O, K, XP, g, r7_sira)
    # spec'teki -22,2222 farkı: 200/6/1.5
    fark = dogru - yanlis
    ok8 = (abs(yanlis - yanlis_beklenen) < Decimal("0.01")
           and abs(dogru - dogru_beklenen) < TOL
           and abs(fark - Decimal("22.2222")) < Decimal("0.01"))
    sonuclar.append(
        ("TV-8", f"yanlis={yanlis_beklenen} dogru={dogru_beklenen}",
         f"yanlis={_q(yanlis)} dogru={_q(dogru)} fark={_q(fark)}", ok8)
    )

    # ---- TV-9 : ödeme şekli 'mal mukabili' -> UNKNOWN --------------------
    s9 = ters_zincir(
        vergi,
        l8_kdv_dahil=Decimal("799"),
        kanal=KanalGirdisi("CHAIN_RETAIL", "BASE", m_retail=Decimal("0.25"),
                           d=Decimal("0.08")),
        country="ES",
        l5_kalemleri=[L5Kalemi("bandrol", Decimal("2.36073"), "TRY", "FACT")],
        odeme_sekli="mal mukabili",
        otv_senaryo=OTV_SENARYO_UPPER_BOUND_LAMBDA_1,
    )
    ok9 = (s9.status == "UNKNOWN"
           and s9.cif_try_max_upper_bound is None
           and any("KKDF" in e for e in s9.eksik_girdiler))
    sonuclar.append(("TV-9", "UNKNOWN", f"{s9.status} cif={s9.cif_try_max_upper_bound}", ok9))

    # ---- TV-10 : t=2027-04-01, ASSUMPTION yok -> UPPER_BOUND etiketi ----
    # (a) bayrak YOKSA -> UNKNOWN  (T-921 ufuk denetimi)
    okuma_bayraksiz = otv_maktu(vergi, t="2027-04-01", otv_senaryo=None)
    # (b) bayrak VARSA -> hesaplar ama UPPER_BOUND etiketli
    okuma_bayrakli = otv_maktu(vergi, t="2027-04-01",
                               otv_senaryo=OTV_SENARYO_UPPER_BOUND_LAMBDA_1)
    l4_tv10 = Decimal("200.0000")
    c10, _ = r7_coz(l4_tv10, okuma_bayrakli.otv_try_per_sise or Decimal("0"),
                    K, XP, Decimal("0.50"), r7_sira)
    etiket_kodlari = " ".join(okuma_bayrakli.etiketler)
    ok10 = (
        okuma_bayraksiz.status == "UNKNOWN"
        and okuma_bayraksiz.hesaplandi is False
        and okuma_bayrakli.status == "UPPER_BOUND"
        and okuma_bayrakli.upper_bound_mu is True
        and all(x in etiket_kodlari for x in ("O-2", "O-3", "O-5", "O-6"))
        and abs(c10 - Decimal("97.6987")) < TOL
    )
    sonuclar.append((
        "TV-10",
        "bayraksiz=UNKNOWN ; bayrakli=97.6987 + UPPER_BOUND(O-2/O-3/O-5/O-6)",
        f"bayraksiz={okuma_bayraksiz.status} ; bayrakli={okuma_bayrakli.status} "
        f"cif={_q(c10)} etiket={'O-2/O-3/O-5/O-6' if ok10 else 'EKSIK'}",
        ok10,
    ))

    gecen = sum(1 for *_r, ok in sonuclar if ok)
    return gecen, len(sonuclar), sonuclar


def main() -> int:
    gecen, toplam, sonuclar = calistir()
    print("=" * 96)
    print("BIRIM TEST VEKTORLERI — vergi.yaml/ters_model_vergi_bacagi.birim_test_vektorleri")
    print("=" * 96)
    print(f"{'TV':<7}{'BEKLENEN':<62}{'GERCEKLESEN':<52}{'GECTI'}")
    for kod, bek, ger, ok in sonuclar:
        print(f"{kod:<7}{bek:<62}{ger:<52}{'EVET' if ok else 'HAYIR'}")
    print("-" * 96)
    print(f"SONUC: {gecen}/{toplam} gecti")
    print("=" * 96)
    return 0 if gecen == toplam else 1


if __name__ == "__main__":
    sys.exit(main())
