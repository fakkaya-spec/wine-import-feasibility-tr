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
| FX_DOWN_10 | 42.9406 | 49.6273 | SENSITIVITY_AXIS | makro.yaml -> fx.senaryolar.FX_DOWN_10 (kur_tipi=doviz_satis, ttl_bitis=2026-08-17) |
| FX_0 | 47.7118 | 55.1414 | OBSERVED | makro.yaml -> fx.senaryolar.FX_0 (kur_tipi=doviz_satis, ttl_bitis=2026-08-17) |
| FX_UP_10 | 52.4830 | 60.6555 | SENSITIVITY_AXIS | makro.yaml -> fx.senaryolar.FX_UP_10 (kur_tipi=doviz_satis, ttl_bitis=2026-08-17) |
| FX_UP_20 | 57.2542 | 66.1697 | SENSITIVITY_AXIS | makro.yaml -> fx.senaryolar.FX_UP_20 (kur_tipi=doviz_satis, ttl_bitis=2026-08-17) |

## MAX_FOB / MAX_EXW — UST SINIR (fx geldikten sonra acildi)

| fx ekseni | para | kur | MAX_FOB ust sinir @X | @Y | MAX_EXW ust sinir @Y | nokta degeri |
|---|---|---|---|---|---|---|
| FX_DOWN_10 | EUR | 49.6273 | 4.0497 | 5.8539 | 5.8539 | BLOCKED_INPUT (FOB->CIF koprusu yok, T-866) |
| FX_DOWN_10 | USD | 42.9406 | 4.6804 | 6.7655 | 6.7655 | BLOCKED_INPUT (FOB->CIF koprusu yok, T-866) |
| FX_0 | EUR | 55.1414 | 3.6448 | 5.2685 | 5.2685 | BLOCKED_INPUT (FOB->CIF koprusu yok, T-866) |
| FX_0 | USD | 47.7118 | 4.2123 | 6.0889 | 6.0889 | BLOCKED_INPUT (FOB->CIF koprusu yok, T-866) |
| FX_UP_10 | EUR | 60.6555 | 3.3134 | 4.7896 | 4.7896 | BLOCKED_INPUT (FOB->CIF koprusu yok, T-866) |
| FX_UP_10 | USD | 52.4830 | 3.8294 | 5.5354 | 5.5354 | BLOCKED_INPUT (FOB->CIF koprusu yok, T-866) |
| FX_UP_20 | EUR | 66.1697 | 3.0373 | 4.3904 | 4.3904 | BLOCKED_INPUT (FOB->CIF koprusu yok, T-866) |
| FX_UP_20 | USD | 57.2542 | 3.5103 | 5.0741 | 5.0741 | BLOCKED_INPUT (FOB->CIF koprusu yok, T-866) |

> Bu sutunlar **UST SINIRDIR**: CIF = FOB + navlun + sigorta ve koprulerin hepsi >= 0. Nokta degeri FOB->CIF koprusu girilmeden URETILMEZ (`T-866`). MAX_CIF'in kendisi de bir ust sinirdir.

## DEGERLENDIRME SATIRLARI

*(havuzda teklif YOK — 2026-08-10 itibariyle sifir gercek teklif)*

## EKSIK GIRDILER (BLOCKED_INPUT)

*(yok)*

> `ABOVE_CEILING` bir GOZLEMDIR, bir RET DEGILDIR. Yatirimci nihai marj esigi YOK (OQ-901 / T-851, CRITICAL, OPEN). Esik olmadan bir teklif REDDEDILEMEZ. ABOVE_CEILING bir GOZLEMDIR, bir ret DEGILDIR.
