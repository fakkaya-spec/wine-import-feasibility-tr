# ÇAPRAZ İPUÇLARI — navlun-lojistik-uzmani · TUR 2.5

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2.5
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md bu turda DOKUNMA listesindedir. Bunlar SONUC DEGIL, IPUCUDUR."
```

---

## İ-2501 → `finans-fizibilite`

**İpucu:** Gümrük müşavirliği ücreti sabit değildir. `EV-2026-08-09-342` (T3,
2026 asgari tarife): İTH-2 4.670 TL + ANT-1 1.350 TL **artı**, CIF
**15.001–225.000 USD** için *aşan kısmın **%0,3'ü***; 225.001–2.000.000 USD
için aşan kısmın %0,1'i.

**Neden önemli:** Senaryolarımda müşavirlik **6.020 TL sabit** alındı, çünkü
CIF'i ben belirleyemem. 25.000 şişe ve üstünde CIF 15.000 USD eşiğini kesin
aşar → **benim TRY bacağım bu hacimlerde EKSİKTİR.** Formül `finans-fizibilite`
tarafından CIF üzerinden tamamlanmalıdır.

---

## İ-2502 → `finans-fizibilite`

**İpucu:** LCL modunda şişe başı **USD** maliyeti 5.000 → 100.000 şişe
arasında yalnızca **%12–14** düşüyor (0,450 → 0,387 BASE). TRY bacağı %67
düşüyor. FCL'de her iki bacak da %68–74 düşüyor.

**Neden önemli:** Finans modelinde "hacim büyürse birim lojistik maliyeti
düşer" şeklinde **mod-bağımsız** bir ölçek varsayımı kullanılırsa, LCL
senaryosu **sistematik olarak iyimser** olur. Ölçek ekonomisi **moda geçişten**
gelir, hacimden değil — ve o mod (FCL) fiyatı `UNKNOWN`'dır (`T-304`).

---

## İ-2503 → `global-sourcing-kasifi`

**İpucu:** Koli formatı (6'lı vs 12'li) yalnızca %7'lik bir hacim farkı değil.
Kapasite bandının alt ucunda (11.800 şişe/20DV) **25.000 şişe iki konteynere
sığmıyor, üçüncü konteyner gerekiyor** → şişe başı TRY maliyeti **%73**
artıyor.

**Neden önemli:** `T-302` (tedarikçiden koli spesifikasyonu) "iyi olurdu"
kategorisinde değil, **basamaklı maliyet etkisi olan** bir `UNKNOWN`.
RFQ'da şişe çapı/yüksekliği ve koli dış ölçüsü **zorunlu alan** olmalı.

---

## İ-2504 → `mevzuat-ruhsat-uzmani`

**İpucu:** Gecikmenin maliyeti **yükün nerede beklediğine** bağlı:
antrepoda 60 gün ≈ **0,03 EUR/şişe**; limanda 60 gün ≈ **0,61 USD/şişe**
(detention + terminal ardiyesi, iki ayrı sayaç). Fark ~30–35 kat.

**Neden önemli:** `T-301` şu anda "bandrol/ruhsat kaç gün sürer?" diye
soruyor. Finansal olarak asıl belirleyici soru: **"bu sürenin ne kadarında yük
hâlâ konteynerde/limanda olmak zorunda?"** Menşede bandrollenebiliyorsa
(`EV-2026-08-09-380`, doğrulanmadı) liman bekleme riski büyük ölçüde ortadan
kalkar.

---

## İ-2505 → `gumruk-vergi-uzmani`

**İpucu:** LCL'de navlun tek bir CBM fiyatının içine gömülüdür (origin local
charge'lar dahil); FCL'de kalem kalem ayrışır (okyanus + THO + B/L + THD + …).

**Neden önemli:** Gümrük kıymetine (CIF) hangi kalemin **gireceği** ve hangi
kalemin **yurt içi masraf** sayılacağı **taşıma moduna göre değişir.**
Aynı fiziksel maliyet, LCL'de matraha girip FCL'de girmeyebilir. Bu, `T-303`
ve `30-vergi-gumruk/matrah-sirasi.md` için yapısal bir noktadır.

---

## İ-2506 → `seytanin-avukati`

**İpucu:** Bu turun senaryolarında **FCL'in BASE'i yoktur** (`M-6`). Modelde
bir yerde FCL için tek bir merkezî sayı görülürse, o sayı **uydurulmuştur** —
benim çıktımdan gelmiş olamaz.
