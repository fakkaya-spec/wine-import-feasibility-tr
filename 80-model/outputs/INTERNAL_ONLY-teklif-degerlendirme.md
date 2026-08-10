<!-- ================================================================
     INTERNAL_ONLY — TEDARIKCIYE GOSTERILMEZ
     Icerik: TARGET CEILING (X/Y), sonuc degeri, MAX_CIF/MAX_FOB/MAX_EXW,
     FX eksenleri. Bunlarin hicbiri bir taahhut degildir ve disariya
     verilmesi pazarligi tersine cevirir.
     ================================================================ -->

# TEKLIF DEGERLENDIRME — TUR 3.25 §13 (INTERNAL_ONLY)

```yaml
cikti_sinifi:   INTERNAL_ONLY
durum:          DRAFT          # OQ-901/T-851 CRITICAL+OPEN
tavan_sinifi:   MODEL_DERIVED / UPPER_BOUND / DRAFT
tavan_kaynagi:  country-buying-ceilings.csv (X: HIGH/5000, Y: BASE/25000)
X_try:          200.9780
Y_try:          290.5134
mense_grubu:    P
blocked_input:  26
ret_hukmu:      YASAK  # REJECTED uretilemez
```

## FX EKSENLERI

| eksen | usd_try | eur_try | status | kaynak |
|---|---|---|---|---|
| FX_DOWN_10 | 42.9406 | 49.6273 | DERIVED_FROM_OBSERVED | makro.yaml -> fx.* (gozlenen) x 0.90 (eksen tanimi) |
| FX_0 | 47.7118 | 55.1414 | DERIVED_FROM_OBSERVED | makro.yaml -> fx.* (gozlenen) x 1.00 (eksen tanimi) |
| FX_UP_10 | 52.4830 | 60.6555 | DERIVED_FROM_OBSERVED | makro.yaml -> fx.* (gozlenen) x 1.10 (eksen tanimi) |
| FX_UP_20 | 57.2542 | 66.1697 | DERIVED_FROM_OBSERVED | makro.yaml -> fx.* (gozlenen) x 1.20 (eksen tanimi) |

## DEGERLENDIRME SATIRLARI

*(havuzda teklif YOK — 2026-08-10 itibariyle sifir gercek teklif)*

## EKSIK GIRDILER (BLOCKED_INPUT)

*(yok)*

> `ABOVE_CEILING` bir GOZLEMDIR, bir RET DEGILDIR. Yatirimci nihai marj esigi YOK (OQ-901 / T-851, CRITICAL, OPEN). Esik olmadan bir teklif REDDEDILEMEZ. ABOVE_CEILING bir GOZLEMDIR, bir ret DEGILDIR.
