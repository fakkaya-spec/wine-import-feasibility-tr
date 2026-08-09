# AJAN RAPORU — GLOBAL SOURCING KÂŞİFİ — TUR 1

```yaml
ajan:               global-sourcing-kasifi
tur:                TUR 1
tarih:              2026-08-09
durum:              SUBMITTED
evidence_araligi:   EV-2026-08-09-401 … EV-2026-08-09-428 (28 kart)
ticket_araligi:     T-401 … T-406 (6 ticket)
conflict_araligi:   C-401 … C-403 (3 çelişki)
teklif_alindi_mi:   false
uretici_ile_iletisim: NONE — bu turda hiçbir üreticiye e-posta/mesaj gönderilmedi
```

---

## 1. YÖNETİCİ ÖZETİ

Bu tur bir **haritalama turudur**; fiyat toplama turu değildir. Fiyat/performans
segmentinde şişelenmiş şarap tedariki için 12 ülke taranmış, kurumsal sitesi
erişilebilir **11 üretici/tedarikçi doğrulanmış** ve `50-sourcing/tedarikci-havuzu.csv`
dosyasına işlenmiştir. **Hiçbir üreticiden teklif alınmamıştır; `quote_type` her satırda
`NONE_YET`'tir ve `tedarikci.yaml`'daki `exw_per_sise` ile `fob_per_sise` alanları
`null`/`UNKNOWN` olarak bırakılmıştır.**

En kritik tek bulgu şudur: **doğrulanabilen en düşük private label MOQ'ları
3.000 ve 3.600 şişedir** (`EV-2026-08-09-408`, `EV-2026-08-09-410`) ve bu, charter'ın
5.000 şişelik pilot hacmiyle **uyumludur**. Yani private label modeli pilot ölçekte
teknik olarak uygulanabilir görünmektedir. Ancak aynı ülkede (İspanya) başka bir üretici
MOQ'yu **konteyner bazında** tanımlamaktadır (`EV-2026-08-09-409`) — yani MOQ, bir
sayı değil, **tedarikçi sınıfına bağlı bir yapıdır** ve bu ayrım `peak_cash_requirement`'i
doğrudan değiştirir (`C-401`).

İkinci önemli bulgu tedarik coğrafyasındadır: UN Comtrade'e göre Türkiye 2025'te
şişelenmiş şarabı ağırlıkla **İtalya, Fransa, Moldova, İspanya, Gürcistan, Bulgaristan
ve Şili'den** almıştır; en düşük CIF birim değerleri **Moldova (2,46 USD/l), Gürcistan
(2,57), İspanya (2,71) ve Şili (2,89)** menşelidir (`EV-2026-08-09-405`). Buna karşılık
**iki benchmark ürünün menşei olan ABD (18.298 litre) ve Avustralya (44.674 litre)
Türkiye'ye neredeyse hiç mal göndermemektedir** — yani benchmark'ın menşei ile fiilî
tedarik coğrafyası örtüşmemektedir.

`50-sourcing/rfq-template.md` gönderilebilir profesyonel bir taslağa (v2.0)
dönüştürülmüş, her sorusu `tedarikci-havuzu.csv` kolonlarına eşlenmiştir.

---

## 2. BULGULAR

### B-1: Private label MOQ'su pilot hacimle uyumlu olabilir

```yaml
claim:          Doğrulanabilen en düşük private label MOQ'ları 3.000–3.600 şişedir
value:          3000 (ES) / 3600 (FR)
unit:           şişe (SKU başına)
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-408, EV-2026-08-09-410
effective_date: -
katman:         -
```

**Gerekçe:** İki ayrı üretici, iki ayrı ülkede, kendi kurumsal sitelerinde bu rakamları
açıkça ilan ediyor. Interbrosa (İspanya): *"MOQ is 4 pallets per wine (3.000 bottles)"*.
The Wine Factory (Fransa): 3.600 şişe, üretim süresi ödeme sonrası 4–6 hafta.

**Ne anlama gelmez:** Bu rakamlar **fiyat içermez**. "MOQ düşük" ile "birim fiyat
kabul edilebilir" aynı şey değildir; küçük parti tipik olarak daha pahalıdır ve bu
fark bilinmiyor.

---

### B-2: MOQ bir sayı değil, bir yapıdır — iki farklı tedarikçi sınıfı var

```yaml
claim:          Tedarikçiler MOQ'yu ya SKU/şişe bazında ya konteyner bazında tanımlıyor
value:          "3.000–3.600 şişe (SKU bazlı)" vs "1 × 20ft karışık konteyner (2 SKU)"
unit:           şişe / konteyner
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-408, EV-2026-08-09-409, EV-2026-08-09-410
katman:         -
```

**Gerekçe:** Viña Maria (İspanya, yıllık 15 m şişe+) MOQ'yu *"a mixed 20ft container
with 2 different wines"* olarak tanımlıyor. Interbrosa aynı ülkede 3.000 şişe diyor.
Bu bir çelişki değil, **iki ayrı iş modelidir**: kontrat şişeleyici / butik bottler
vs konteyner satan endüstriyel üretici.

**Model için sonucu:** Pilot senaryosu (5.000 şişe) yalnızca birinci sınıfla mümkündür
ve bu **tedarikçi havuzunu daraltır**. Daralan havuz büyük ihtimalle daha yüksek birim
fiyat demektir. Bu ödünleşim `finans-fizibilite` tarafından modellenmelidir.

---

### B-3: Türkiye'ye fiilen mal gönderen menşeler ve CIF birim değerleri

```yaml
claim:          Türkiye 2025'te en ucuz şişelenmiş şarabı Moldova, Gürcistan, İspanya ve Şili'den aldı
value:          MD 2.46 / GE 2.57 / ES 2.71 / CL 2.89 / PT 3.20 / IT 3.65 / BG 3.89 / FR 6.27
unit:           USD/litre
status:         FACT
tier:           T3
evidence_id:    EV-2026-08-09-405
effective_date: 2025 takvim yılı
katman:         L2 (CIF)
```

**Gerekçe:** UN Comtrade, Türkiye'nin kendi gümrük idaresince raporlanan HS 220421
ithalat verisi. Toplam 17.848.518 litre / 66.876.002 USD CIF.

**Kritik uyarı:** Bu **L2 (CIF)** katmanıdır. FOB veya EXW yerine kullanılamaz.
CIF'ten navlun **çıkarılmamıştır** çünkü navlun tutarı `navlun-lojistik-uzmani`'nın
alanıdır (T-402). Ayrıca 100.000 litrenin altındaki menşelerde (ZA, AU, AR, US)
birim değer temsili değildir ve ülke elemesinde kullanılmamıştır.

---

### B-4: Benchmark menşei ile fiilî tedarik coğrafyası örtüşmüyor

```yaml
claim:          Türkiye 2025'te ABD'den 18.298 litre, Avustralya'dan 44.674 litre şişelenmiş şarap ithal etti
value:          US 18298 / AU 44674
unit:           litre
status:         FACT
tier:           T3
evidence_id:    EV-2026-08-09-405
katman:         -
```

**Gerekçe:** Aynı yıl İtalya'dan 5.749.972 litre gelmiştir. Yani benchmark ürünün
menşei (California) Türkiye'ye toplam ithalatın **binde birinden azını** göndermektedir.

**Ne anlama gelmez:** Benchmark ürünün var olmadığını göstermez — foto gözlemi
geçerlidir. Ancak ABD'nin ortalama CIF birim değeri 25,19 USD/litre çıkmaktadır ki
bu fiyat/performans segmentiyle bağdaşmaz. Bu bir **çelişkidir** ve `C-402` olarak
kaydedilmiştir, sessizce çözülmemiştir.

---

### B-5: EXW/FOB gösterge bandı — kanıtla sınırlandırılmış, hesaplanmamış

```yaml
claim:          f/p segmenti 750 ml FOB'u, alt sınırı 0,56 EUR (sıvı) ve üst sınırı 1,85–2,40 USD (CIF tavanı) olan bir bandın içindedir
value:          "alt: 0.56 EUR (sıvı) / üst: 1.85–2.40 USD (CIF)"
unit:           EUR ve USD / 750 ml
status:         ESTIMATE
tier:           T3
evidence_id:    EV-2026-08-09-421
katman:         L1 (üst sınır L2'den geliyor)
```

**Türetme zinciri:**
1. **Alt sınır:** OIV dünya dökme şarap ortalama ihracat fiyatı 0,75 EUR/litre
   (`EV-2026-08-09-402`) × 0,75 litre = **0,56 EUR**. Bu **yalnızca sıvıdır**; kuru
   malzeme (şişe, kapak, etiket, kapsül, koli), şişeleme işçiliği ve üretici marjı
   bunun **üzerine** eklenir ve **UNKNOWN**'dır. Yani gerçek EXW her zaman bunun
   üstündedir — bu bir taban, tahmin değil.
2. **Üst sınır:** Türkiye'ye 2025'te fiilen giren en ucuz menşelerin CIF birim
   değerleri (`EV-2026-08-09-405`): 1,85–2,40 USD/750 ml. Tanım gereği **FOB < CIF**
   olduğundan, bu menşeler için f/p FOB'u bu değerlerin **altındadır**.
3. **Ara doğrulama:** Moldova şişelenmiş sakin şarap ortalama ihracat fiyatı
   1,98 USD/şişe (`EV-2026-08-09-419`, ONVV verisi) — bant içinde ve tutarlı.

**Yapılmayanlar (bilinçli):** CIF'ten navlun düşülüp FOB hesaplanmadı (alan dışı).
EUR ve USD birleştirilmedi. Tek bir "şişe başı fiyat" üretilmedi.

**Kullanım kısıtı:** Bu bant modelde **tek başına fiyat girdisi olarak kullanılamaz**;
yalnızca duyarlılık analizinin sınırlarını belirler.

---

### B-6: Private label kapasitesi piyasa seviyesinde doğrulandı, tedarikçi seviyesinde değil

```yaml
claim:          10 üretici kendi kurumsal sitesinde private label hizmeti sunduğunu ilan ediyor
value:          10
unit:           üretici
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-408 … EV-2026-08-09-417
katman:         -
```

**Gerekçe:** Doğrulama şu ülkelerde yapıldı: İspanya (2), Fransa (1), İtalya (1),
Şili (2), Güney Afrika (2), Avustralya (1), ABD/California (1).

**Ne doğrulandı:** Web sitesinin erişilebilir olduğu ve private label iddiasının
orada yazdığı.
**Ne doğrulanMADI:** Kapasite, fiyat, Türkiye'ye ihracat kabiliyeti, menşe belgesi
düzenleme yetkisi, gerçek MOQ. Yani **"11 aday" ile "11 alternatif tedarikçi" aynı
şey değildir** ve `tedarikci.yaml`'da `alternatif_tedarikci_sayisi = 0` yazılmıştır.

---

### B-7: Model A (mevcut marka distribütörlüğü) mekaniği kısmen haritalandı, somut marka bulunamadı

```yaml
claim:          Distribütörlük sözleşmelerinin tipik yapısı belirlendi, ancak Türkiye'de temsilcisi olmayan somut bir f/p markası doğrulanamadı
value:          UNKNOWN (somut marka)
unit:           -
status:         UNKNOWN
tier:           T5 (mekanik için)
evidence_id:    -
katman:         -
```

**Gerekçe:** Sektör hukuk kaynakları münhasırlık, hacim taahhüdü, ~5 yıllık süre ve
**ithalatçının markup tavanı** gibi maddelerin yaygın olduğunu gösteriyor (T5, `ESTIMATE`).
Pazarlama katkısı için doğrulanabilir tipik bir oran/tutar **bulunamadı** (`UNKNOWN`).

**Neden somut marka bulunamadı:** "Türkiye'de temsilcisi yok" iddiası iki yönlü bir
kesişimdir ve ikinci yönü (Türkiye raf/ithalatçı verisi) `turkiye-pazar-kasifi`'nın
alanıdır. Bu ajan tek başına çözemez. → `OQ-404`

**Dürüst itiraf:** Bu, iki modelin eşit derinlikte araştırılması hedefinin
**bu turda tam olarak tutturulamadığı** anlamına gelir. Nedeni §9.2'de açıklanmıştır.

---

### B-8: Türkiye'ye dökme şarap ithalatı fiilen sıfır

```yaml
claim:          Türkiye 2025'te GTİP 2204.29 (dökme) kaleminde 628 litre ithalat yaptı
value:          628
unit:           litre
status:         FACT
tier:           T3
evidence_id:    EV-2026-08-09-407
effective_date: 2025 takvim yılı
katman:         -
```

**Gerekçe:** Aynı yıl şişelenmiş ithalat 17.848.518 litredir. Oran ~1:28.000.

**Kapsam notu:** Bulk ithalat + Türkiye'de şişeleme `00-charter/kapsam.md` uyarınca
**KAPSAM DIŞIDIR**. Bu ajan hipotezi kaydetmiş, **çözmemiştir**. Nedeni
(vergisel mi, mevzuatsal mı, ticari tercih mi) bu ajanın alanı değildir.
İpuçları `99-ops/_parts/capraz-ipuclari-global-sourcing-kasifi.md` §8'e bırakılmış,
T-406 açılmıştır.

---

### B-9: Piyasa ortamı ölçülü olarak alıcı lehine

```yaml
claim:          2025'te dünya şarap üretimi 227 mhl, tüketimi 208 mhl
value:          227 / 208
unit:           mhl
status:         FACT
tier:           T3
evidence_id:    EV-2026-08-09-425
effective_date: 2025 takvim yılı
katman:         -
```

**Gerekçe:** Dünya ihracatı 2025'te hacimde -%4,7, değerde -%6,7 daraldı. Bağ alanı
üst üste 6. yıl küçüldü. İtalya'da Ocak 2026 stokları 61 mhl (+%6).

**Aşırı yorumdan kaçınma:** OIV açıkça, ortalamanın altındaki üretimin
*"genel bir kıtlık değil, kademeli bir stok rahatlaması"* yaratmasını beklediğini
belirtiyor. Yani bu bir **"distilasyon krizi fırsatı" değildir**; ölçülü bir alıcı
kaldıracıdır. Bu ayrım önemlidir çünkü müzakere beklentisini yanlış kalibre etmek
RFQ stratejisini bozar.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| OQ-401 | Gerçek EXW ve FOB fiyatı — hiçbir ülke/üretici için | Fiyat listeleri web'de yayınlanmaz; bu turda üreticiye temas **yasaktı** | **CRITICAL** | RFQ v2.0, ≥8 üreticiye, TUR 7; 2–4 hafta |
| OQ-402 | Gerçek MOQ ve MOQ yapısı (SKU mu konteyner mı) | Çoğu üretici yayınlamıyor; yayınlayanlar farklı birimlerde ölçüyor (`C-401`) | **CRITICAL** | RFQ 3.6a/3.6b, 4.2, 4.3 |
| OQ-403 | Hangi üretici hangi menşe ispat belgesini düzenleyebiliyor | Sitelerde yok; ayrıca hangi belgenin gerektiği bilinmiyor | **CRITICAL** | T-401 kapanmalı → RFQ 6.1 |
| OQ-404 | Türkiye'de temsilcisi olmayan somut f/p markaları | İki yönlü kesişim; ikinci yön `turkiye-pazar-kasifi`'nda | HIGH | TUR 2 çapraz kontrol |
| OQ-405 | İlk siparişte ödeme vadesi | Sadece genel sektör rehberi var, taahhüt yok | HIGH | RFQ 3.8–3.10 |
| OQ-406 | Türkçe arka etiket menşede uygulanabilir mi | Hukuki taraf `mevzuat-ruhsat-uzmani`'nda | HIGH | T-403 → RFQ 4.6 |
| OQ-407 | 20'DV / 40'HC'ye kaç şişe girer | Alan dışı; ayrıca koli/palet ölçüleri de yok | HIGH | T-402 + RFQ 2.1–2.8 |
| OQ-408 | Private label'da marka/reçete IP sahipliği | Sitelerde yok | MEDIUM | RFQ 4.9, 4.10 |
| OQ-409 | Etiket klişe/kalıp tek seferlik maliyeti | Sitelerde yok | MEDIUM | RFQ 4.7 |
| OQ-410 | Aday ürünlerin ABV'si | Hiçbir üretici yayınlamıyor | MEDIUM | RFQ 1.4 + T-401 |
| OQ-411 | Bize ayrılabilecek yıllık kapasite | Sitelerde yok | MEDIUM | RFQ 3.12, 8.3 |
| OQ-412 | Moldova / Gürcistan / Bulgaristan tedarikçi tabanı | Kaynak önceliği charter'ın 9 ülkesine verildi | MEDIUM | ONVV / Georgian Wine Assoc. üye listeleri |
| OQ-413 | Les Grands Chais de France doğrulaması | Kurumsal site HTTP 503 | LOW | Sonraki tur |
| OQ-414 | Ciatti ülke bazlı dökme fiyat grid'i | Abonelik arkasında | LOW | Abonelik |
| OQ-415 | OEMV birincil İspanya ihracat verisi | Basından okundu, birincil doğrulanmadı | LOW | Sonraki tur |

Detay: `99-ops/_parts/acik-sorular-global-sourcing-kasifi.md`

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-401** | usetorg.com agregatörü (T5) — private label MOQ 300–1.200 şişe | Interbrosa (T4) 3.000 şişe / The Wine Factory (T4) 3.600 şişe / Viña Maria (T4) 1 × 20ft konteyner | 10 kata varan fark; ayrıca farklı ölçü birimleri. Hangisinin seçildiği **kararın kendisini belirler** | **OPEN** |
| **C-402** | `benchmark.md` foto gözlemi — California menşeli f/p ürün Metro rafında | UN Comtrade (T3) — Türkiye'nin ABD'den ithalatı 18.298 litre, ort. CIF 25,19 USD/l | 25,19 USD/l premium seviyedir, f/p segmentiyle bağdaşmaz | **OPEN** |
| **C-403** | Perakendeci açıklaması (T5) — "Sierra Foothills" | Başka perakendeci açıklaması (T5) — "Central Valley" | Benchmark ürünün California alt bölgesi belirsiz; ikisi de T5 | **OPEN** |

Detay ve öneriler: `99-ops/_parts/celiskiler-global-sourcing-kasifi.md`
**Hiçbiri sessizce çözülmemiştir.**

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| tedarikci.yaml | `fiyat.exw_per_sise` | **null** | — | UNKNOWN | — |
| tedarikci.yaml | `fiyat.fob_per_sise` | **null** | — | UNKNOWN | — |
| tedarikci.yaml | `fiyat.quote_type` | `NONE_YET` | — | FACT | — |
| tedarikci.yaml | `private_label.mumkun_mu` | `true` (piyasa seviyesinde) | — | FACT | EV-408…EV-417 |
| tedarikci.yaml | `arastirma_bulgulari.private_label_moq.dogrulanmis_en_dusuk` | 3000 | şişe | FACT | EV-2026-08-09-408 |
| tedarikci.yaml | `arastirma_bulgulari.private_label_moq.dogrulanmis_ikinci` | 3600 | şişe | FACT | EV-2026-08-09-410 |
| tedarikci.yaml | `arastirma_bulgulari.private_label_moq.konteyner_bazli_ornek` | 1 × 20ft mixed | konteyner | FACT | EV-2026-08-09-409 |
| tedarikci.yaml | `arastirma_bulgulari.private_label_moq.celiskili_iddia` | 300–1200 | şişe | **CONFLICT** | EV-2026-08-09-424 (C-401) |
| tedarikci.yaml | `arastirma_bulgulari.uretim_lead_time_gun.aralik` | 28–42 | gün | ESTIMATE | EV-410, EV-411 |
| tedarikci.yaml | `arastirma_bulgulari.fob_gosterge_bandi.alt_sinir_sivi_maliyeti` | 0.56 | EUR/750 ml | ESTIMATE | EV-2026-08-09-402 |
| tedarikci.yaml | `arastirma_bulgulari.fob_gosterge_bandi.ust_sinir_cif_tavani` | 1.85–2.40 | USD/750 ml (**L2**) | ESTIMATE | EV-2026-08-09-405 |
| tedarikci.yaml | `arastirma_bulgulari.fob_gosterge_bandi.ara_dogrulama` | 1.98 | USD/şişe | FACT | EV-2026-08-09-419 |
| tedarikci.yaml | `arastirma_bulgulari.ulke_gosterge_birim_degerleri.katman_L1...` | 9 ülke | EUR/litre | ESTIMATE | EV-2026-08-09-404 |
| tedarikci.yaml | `arastirma_bulgulari.ulke_gosterge_birim_degerleri.katman_L2...` | 11 menşe | USD/litre (**L2**) | FACT | EV-2026-08-09-405 |
| tedarikci.yaml | `arastirma_bulgulari.pazar_ortami` | 227 / 208 | mhl | FACT | EV-2026-08-09-425 |
| tedarikci.yaml | `arastirma_bulgulari.bulk_hipotezi.turkiye_bulk_ithalati_2025_litre` | 628 | litre | FACT | EV-2026-08-09-407 |
| tedarikci.yaml | `risk.alternatif_tedarikci_sayisi` | **0** | adet | FACT | — |

**evidence_id'si olmayan hiçbir sayı modele girmemiştir.**

> **`finans-fizibilite`'ye uyarı:** `arastirma_bulgulari` bloğu bir **fiyat girdisi
> değildir**. `kullanim_kurali: SENSITIVITY_BOUNDS_ONLY` alanı bunu YAML içinde de
> işaretler. Model, `exw_per_sise`/`fob_per_sise` null olduğu için bu turda
> **fiyat çıktısı üretmemelidir**.

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `gumruk-vergi-uzmani` | Türkiye'nin şarap ithalatı fiilen tek GTİP'te: 2204.21 (17,85 m litre); 2204.22 ve 2204.29 pratikte boş | GTİP çalışmasının ağırlığını doğru yere koyar |
| `gumruk-vergi-uzmani` | Hiçbir aday üretici ABV yayınlamıyor; private label'da ABV **ayarlanabilir** bir parametredir | Türkiye'de bir ABV eşiği varsa bu doğrudan tedarikçi/ürün seçimini değiştirir |
| `gumruk-vergi-uzmani` | Aday ülkeler üç ayrı hukuki grupta (AB / AB dışı Avrupa / okyanus ötesi) — belge tipleri farklı olabilir | RFQ 6.1 ancak bu cevaptan sonra daraltılabilir |
| `navlun-lojistik-uzmani` | Bir üretici MOQ'yu **konteyner** cinsinden tanımlıyor — konteyner doluluk bilinmeden pilot uyumu hesaplanamaz | MOQ tanımının bir parçası |
| `navlun-lojistik-uzmani` | **Sezgiye aykırı:** en ucuz CIF birim değerli menşeler aynı zamanda en yakın olanlar (Moldova, Gürcistan — karayolu) | "Ucuz ama uzak" ödünleşimi gözlenmedi; doğrulanmalı |
| `mevzuat-ruhsat-uzmani` | Türkçe arka etiket menşede uygulanabilirse Türkiye'deki etiketleme operasyonu tamamen kalkar | L5 katmanında anlamlı kalem |
| `mevzuat-ruhsat-uzmani` | Bir üretici sitesinde ithalat lisansının **ithalatçıya ait** olduğunu açıkça yazıyor | Ruhsat yükü bizde; müzakere kaldıracı değil |
| `mevzuat-ruhsat-uzmani` | Bir üretici **helal sertifikalı** şarap seçeneği sunduğunu beyan ediyor | Etikette bu tür iddiaların Türkiye'de kullanımı kısıtlıysa bilinmeli |
| `turkiye-pazar-kasifi` | "Gold Country" ve "Central Creek" üreticileri açık kaynakta bulunamadı — özel marka olabilirler (**hipotez**) | Doğruysa Model B'nin Türkiye'de zaten çalıştığının kanıtı |
| `turkiye-pazar-kasifi` | Yunanistan 2024'te 1,71 m litre → 2025'te 0,05 m litre (-%97); Bulgaristan sıfırdan 1,38 m litreye | Bir ithalatçı menşe değiştirmiş veya bir düzenleme değişmiş olabilir |
| `turkiye-pazar-kasifi` | Türkiye 2025 ithalatı 17,85 m litre / 66,88 m USD CIF (750 ml eşdeğeri ~23,8 m şişe — **sadece aritmetik**) | Pazar büyüklüğü yorumu sizin alanınız |
| `kanal-marj-uzmani` | Sektör kaynaklarına göre distribütörlük sözleşmelerinde ithalatçının **markup tavanı** yaygın bir madde | Doğruysa Model A'da kanal marjı kontrolümüz sınırlı |
| `kanal-marj-uzmani` | Model A'da üretici pazarlama/listeleme katkısı verebiliyor ama **tipik oran UNKNOWN** | Listeleme bedeli ile bu katkı aynı satırda netleşmeli, çift sayım riski |
| `finans-fizibilite` | Fiyat girdisi **yok**; `alternatif_tedarikci_sayisi = 0` | Model fiyat çıktısı üretmemeli, UNKNOWN dönmeli |
| `finans-fizibilite` | 5.000 şişe senaryosu tedarikçi havuzunu daraltır → birim fiyat muhtemelen yükselir | Bu ödünleşim modellenmeli |
| `seytanin-avukati` | Kendi işime karşı 5 maddelik cephane bıraktım | `capraz-ipuclari` §7 |

Tam liste: `99-ops/_parts/capraz-ipuclari-global-sourcing-kasifi.md`

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| T-401 | `gumruk-vergi-uzmani` | Aday ülkeler için 2204.21'de tercihli tarife var mı, hangi menşe belgesi gerekiyor? | HIGH | OPEN |
| T-402 | `navlun-lojistik-uzmani` | 20'DV/40'HC'ye kaç şişe girer; aday limanlardan rota/transit süre nedir? | HIGH | OPEN |
| T-403 | `mevzuat-ruhsat-uzmani` | Türkçe arka etiket menşede uygulanabilir mi? Bandrol/ÜİS nerede uygulanır? | HIGH | OPEN |
| T-404 | `gumruk-vergi-uzmani` | Peşin vs vadeli ödeme KKDF/matrah sonucunu değiştirir mi? | HIGH | OPEN |
| T-405 | `turkiye-pazar-kasifi` | "Gold Country" ve "Central Creek" üretici markası mı, ithalatçı özel markası mı? | MEDIUM | OPEN |
| T-406 | `gumruk-vergi-uzmani` | Türkiye'nin dökme şarap ithalatının fiilen sıfır olmasının vergisel/mevzuatsal nedeni var mı? | MEDIUM | OPEN |

**Kapanan ticket:** yok (bu ajan bu turda hiçbir ticket'a cevap vermedi).

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| EV-2026-08-09-401, -402, -403, -425 (OIV) | 1y | 2027-08-09 |
| EV-2026-08-09-404 (OIV türetme) | 1y | 2027-08-09 |
| EV-2026-08-09-405, -406, -407, -426 (Comtrade) | 180d | 2027-02-05 |
| EV-2026-08-09-419 (Moldova ihracat fiyatı) | 180d | 2027-02-05 |
| EV-2026-08-09-420 (Wine Australia rehberi) | 1y | 2027-08-09 |
| EV-2026-08-09-427, -428 (T5 basın/agregatör) | 180d | 2027-02-05 |
| EV-2026-08-09-408 … -418 (tedarikçi site beyanları) | 90d | 2026-11-07 |
| EV-2026-08-09-421 (FOB gösterge bandı) | 90d | 2026-11-07 |
| EV-2026-08-09-422, -423, -424 (UNKNOWN / CONFLICT) | 90d | 2026-11-07 |

**En kısa TTL 90 gündür** ve tedarikçi beyanlarına aittir — bu doğrudur, çünkü
üreticiler MOQ ve ürün yelpazesini sezon başında değiştirebilir.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**UN Comtrade `qtyUnitCode = 7` alanının litre olmadığının ortaya çıkması.**

Bu raporun L2 sütununun tamamı, `EV-2026-08-09-421` gösterge bandının üst sınırı,
ülke gruplandırması ve "en ucuz menşeler aynı zamanda en yakın" bulgusu — hepsi
bu tek yorum üzerine kuruludur. Ben bu alanı litre olarak yorumladım, çünkü
`qty` değeri `netWgt` ile neredeyse birebir örtüşüyor ve şarabın yoğunluğu ≈ 1 kg/l.
**Ama bu doğrulanmış bir yorum değil, benim çıkarımımdır.** Comtrade birim kodu
tablosunu birincil kaynaktan teyit etmedim.

Yanlışsa: tüm CIF birim değerleri kayar, ülke sıralaması değişebilir, gösterge
bandının üst sınırı geçersiz olur.

İkinci sırada: **MOQ'nun gerçekte konteyner bazlı olduğunun anlaşılması.** Bu
durumda B-1 bulgusu (pilot uyumu) çöker ve pilot mantığının tamamı yeniden kurulur.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"Bu turda topladığım 11 tedarikçinin dağılımı piyasayı temsil ediyor" varsayımı.
Etmiyor.**

Private label sağlayıcıları kendilerini web'de *"private label wine"* diye
pazarlar ve bu yüzden aranabilirler. Mevcut marka sahipleri distribütör arayışını
fuarlarda (ProWein, Wine Paris), ihracat destek kurumlarında ve doğrudan temasla
yürütür — web'de aranmazlar. Sonuç: havuzumda **10 private label adayı, 1 Model A
adayı** var.

Bu asimetri **Model B'nin daha iyi olduğunu göstermez; açık kaynakta daha görünür
olduğunu gösterir.** Charter iki modelin eşit öncelikli olduğunu söylüyor ve ben
bu turda eşit derinliğe **ulaşamadım**. Bunu raporda ve ülke karşılaştırma dosyasında
açıkça itiraf ettim, ama itiraf açığı kapatmıyor.

Bu, kararın Model B'ye kayması riskini taşır ve bu kayma **kanıtla değil, arama
yöntemiyle** üretilmiş olur. `yatirim-komitesi-baskani`'nın bu noktayı özellikle
denetlemesi gerekir.

### 9.3 Hangi kaynağıma en az güveniyorum?

Üç kaynak, güven sırasının en altında:

1. **Üretici web sitesi beyanları (T4).** MOQ, lead time ve kapasite iddialarının
   tamamı üreticinin kendi pazarlama metnidir. Kimse doğrulamamıştır. "MOQ 3.000 şişe"
   bir satış argümanıdır; gerçek sipariş görüşmesinde "ama o fiyattan değil"
   cümlesiyle karşılaşmak olağandır.
2. **`EV-2026-08-09-404` (ülke bazlı türetilmiş birim değerler).** OIV tablosundaki
   değerler yuvarlanmış (İspanya "3" bn EUR), dikey yapı yüzdeleri 2024 başlığıyla
   verilmiş ama hacim/değer 2025. Yani iki farklı yılın verisini çarpıyorum.
   Hata payı %5'in üzerinde olabilir.
3. **`EV-2026-08-09-427` (İspanya OEMV verisi).** Basından okundu, birincil kaynak
   doğrulanmadı. Bu yüzden modele **sokmadım**, yalnızca tutarlılık kontrolü için tuttum.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlış çıkan | Değişen karar |
|---|---|
| MOQ 3.000 şişe (gerçekte konteyner) | **`IMPORT PILOT` → `HOLD` veya `TEST`.** 5.000 şişelik pilot imkânsız hale gelir; minimum giriş bileti belki 10–15 bin şişeye çıkar ve `maximum_total_capital_try` eşiği (henüz TBD) bunu kaldıramayabilir |
| CIF birim değerleri (birim hatası) | **Ülke seçimi.** Grup 1 dağılır; İspanya/Şili yerine başka ülkeler öne çıkabilir; ters modelin hedef FOB'u kayar |
| Gösterge bandının üst sınırı | **`finans-fizibilite`'nin duyarlılık aralığı.** Model, gerçekte imkânsız bir fiyat bandını "mümkün" göstermiş olur |
| Private label'da IP'nin bizde olduğu varsayımı | **Model B'nin stratejik mantığı.** IP üreticideyse Model B, Model A'ya göre bir avantaj sağlamaz; sadece marka inşa maliyetini bize yükler |
| Model A'da somut marka bulunabileceği beklentisi | **İş modeli seçimi.** Model A hiç uygulanabilir değilse iki modelin eşit değerlendirilmesi anlamsızlaşır |

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre |
|---|---|---|---|---|
| 1 | Comtrade birim kodu teyidi | `global-sourcing-kasifi` | UN Comtrade birim kodu referans tablosunun birincil kaynaktan okunması | 1 gün |
| 2 | Gerçek EXW/FOB + MOQ | `global-sourcing-kasifi` | `rfq-template.md` v2.0'ın ≥8 üreticiye gönderilmesi; hedef ≥5 cevap | 2–4 hafta (TUR 7) |
| 3 | Model A marka listesi | `global-sourcing-kasifi` + `turkiye-pazar-kasifi` | Türkiye'deki ithalatçı/raf listesi ile üretici portföylerinin çaprazlanması; ProWein/Wine Paris katılımcı listelerinin taranması | 1–2 hafta (TUR 2) |
| 4 | Menşe belgesi kabiliyeti | `gumruk-vergi-uzmani` → sonra RFQ | T-401 kapanınca RFQ 6.1 daraltılır | T-401 + 2 hafta |
| 5 | Konteyner doluluk | `navlun-lojistik-uzmani` | T-402 + RFQ 2.1–2.8 ambalaj verisi | 1 hafta + RFQ |
| 6 | MD/GE/BG tedarikçi tabanı | `global-sourcing-kasifi` | ONVV, Georgian Wine Association, Bulgarian Assoc. üye listeleri | 3–5 gün |
| 7 | Benchmark üreticileri | `turkiye-pazar-kasifi` | Raf ziyaretinde arka etiket okuma + ABD TTB COLA kaydı araması | 1 hafta |

**Bunların 2, 3 ve 4 numaralısı tamamlanmadan bu ajan bir ülke veya tedarikçi
tavsiyesi vermemelidir — ve bu turda vermemiştir.**
