# SAHA MAĞAZA KONTROL LİSTESİ — ŞARAP RAFI GÖZLEMİ

```yaml
belge:          60-pazar/saha-kontrol-listesi.md
ajan:           turkiye-pazar-kasifi
tur:            TUR 3A
tarih:          2026-08-10
nitelik:        ARAC / PROTOKOL — VERI ICERMEZ, GOZLEM URETMEZ
kapatmayi_hedefledigi: [T-917, T-504, T-603, T-701, C-501, C-551, OQ-001, OQ-502, OQ-552, OQ-503]
kullanici:      kurucu / insan gozlemci (sahada)
bagli_sablon:   60-pazar/saha-veri-sablonu.csv
```

> **BU BELGE BİR BULGU DEĞİLDİR.** Hiçbir fiyat, hiçbir SKU, hiçbir sayım
> içermez. Sahada doldurulmak üzere hazırlanmış boş bir protokoldür.
> Doldurulmadan hiçbir modele girdi üretmez.

> **NEDEN BU BELGE VAR:** `T-504` / `C-551` / `OQ-001`'in kalan ayakları ve
> `T-701`'in `L8_CHAIN_RETAIL` boşluğu **üç turdur masabaşından kapatılamadı**
> (`EV-2026-08-10-504` — 8 yol denendi, hepsi kapalı). Türkiye'de alkolün
> online/broşür fiyat iletişimi **yapısal olarak kapalıdır**
> (`EV-2026-08-09-514`). Bu veri masabaşında **yoktur**. Tek yolu rafa gitmektir.

---
---

# SAYFA 1 — SAHADA KULLANILACAK KISIM

## A. TURUN ASGARİ KAPSAMI (ne kadarı "yeterli")

> İstatistiksel temsil **iddia edilmemektedir**. Amaç, projenin
> **tek-kanal zaafını kırmak** ve `L8_CHAIN_RETAIL`'de **sıfır gözlemi**
> sıfır olmaktan çıkarmaktır.

| Öncelik | Mağaza | Şehir | Neden bu mağaza | Hedef SKU (400–1.200 TL) |
|---|---|---|---|---|
| **P0** | **Metro** — mümkünse benchmark fotoğrafının çekildiği şube | Şehir 1 | `T-504` + `C-551` + `OQ-001` yalnızca **aynı SKU / aynı raf** ile kapanır | **15–25** (bandaki **tüm ithal** + ≥5 yerli çapa) |
| **P0** | **Migros 5M / Macrocenter** (büyük format) | Şehir 1 | `L8_CHAIN_RETAIL` → **projenin en büyük kanıt boşluğu** (`T-701`, `T-603`) | **10–20** |
| **P1** | **CarrefourSA** (hiper) | Şehir 1 | Tek zincire dayanmamak; zincir-içi fiyat farkı | **10–20** |
| **P1** | **Tekel bayii** (şarap ağırlıklı bağımsız) | Şehir 1 | `L8_TEKEL_BAYII` = 0 gözlem; alt bandı asıl bu kanal taşıyor olabilir | **10–15** |
| **P2** | **Metro** — ikinci şehir | Şehir 2 | Metro'nun **tek fiyat** varsayımı ve şehir farkı riski test edilir | 10–15 |
| **P2** | **Zincir market** — ikinci şehir | Şehir 2 | Zincir fiyatının şehir farkı | 10–15 |

**ASGARİ GEÇER NOT (bunun altı turu geçersiz kılmaz ama hedefleri kapatmaz):**

| Kriter | Asgari | Neden |
|---|---|---|
| Şehir sayısı | **≥ 2** | `T-917` P1 — tek şehir, şehir farkı riskini taşır |
| Kanal sayısı | **≥ 2** (Metro + ≥1 zincir market) | `T-917` P2 — K1: `L8_METRO_CASH_CARRY` ≠ `L8_CHAIN_RETAIL` |
| Toplam **ithal** SKU satırı | **≥ 20** | `T-917` P3 — `l8_chain_retail` bir **dağılımdır**, tek sayı değil |
| Bunların zincir marketten geleni | **≥ 8** | `T-701` tek sayıyla kapanmaz |
| Mağaza sayısı | **≥ 4** (ideal 6) | — |
| **Odak bandı** | **400–1.200 TL** | Hedef merdiven 599–999; bant her iki uçtan **1 basamak** taşırılır ki sınır görülebilsin |

**Süre:** mağaza başına **30 dakika** (aşağıdaki dakika bütçesi) → Şehir 1'de
4 mağaza ≈ yarım gün + yol. **İKİNCİ ZİYARET: 2–4 hafta sonra, yalnızca P0 Metro,
yalnızca 2 SKU, ~10 dakika** (bkz. §F — `T-504` fiilen bunu bekliyor).

---

## B. MAĞAZA BAŞLIĞI — her mağaza için 1 kez doldurulur

```
[ ] Mağaza adı/şube : ______________________________
[ ] Şehir / ilçe    : ______________________________
[ ] Kanal tipi      : ( ) CASH_CARRY  ( ) CHAIN_RETAIL  ( ) TEKEL  ( ) DIGER
[ ] Tarih           : ____ / ____ / 2026      Saat: ______
[ ] Gözlemci        : ______________________________
[ ] F0 fotoğrafı çekildi mi (mağaza tabelası / reyon künyesi)?   ( ) E  ( ) H
[ ] Reyonda "kampanya / indirim" genel afişi var mı?             ( ) E  ( ) H  → varsa F1'de görünsün
```

---

## C. SKU SATIRI — SAHADA YAZILACAK 8 ALAN

> **30 dakikanın sırrı budur: sahada AZ YAZ, ÇOK FOTOĞRAFLA.**
> Aşağıdaki 8 alan elle yazılır; kalan 10 alan **masabaşında fotoğraftan**
> doldurulur. Etiketin ince yazısını sahada okumaya **çalışma** — fotoğrafla.

| # | Alan | Nasıl yazılır |
|---|---|---|
| 1 | **Sıra no** | 01, 02, … (fotoğraf dosya adıyla eşleşir) |
| 2 | **SKU adı** (kısaltma yeterli) | "Gold Country Colombard" |
| 3 | **Raf fiyatı TL** | Etiketteki **büyük punto** sayı, kuruşuyla |
| 4 | **İTH / YRL** | Ön etiketten menşe; emin değilsen `?` yaz, arka etiket fotoğrafı karar verir |
| 5 | **Hacim** | 750 / 375 / 1000 ml — **750 dışıysa mutlaka yaz** |
| 6 | **PROMO?** | `E` / `H` — E ise §D'deki 4 işaretten hangisi (a/b/c/d) |
| 7 | **STOK** | `DOLU` / `AZ` (1–2 şişe) / `BOŞ` (etiket var şişe yok) |
| 8 | **Foto no** | Etiket + arka etiket foto numaraları |

### Masabaşında fotoğraftan doldurulacak 10 alan
`marka` · `menşe (tam)` · `ABV %` · `vintage` · `üzüm/blend` · `ürün tipi` ·
`KDV ibaresinin tam metni` · `birim fiyat satırının tam metni` ·
`üstü çizili eski fiyat` · `ithalatçı firma adı (arka etiket)`

---

## D. ⚠ EN KRİTİK ALAN — RAF ETİKETİNİN ANATOMİSİ (`T-504` · `C-551`)

**Fotoğrafta ŞU DÖRT ŞEYİN görünüp görünmediği tek tek işaretlenecek.**
"Bakmadım" ile "baktım, yoktu" **aynı şey değildir** — ikisi ayrı kaydedilir.

```
┌──────────────────────────────────────────────┐
│  6̶9̶9̶,̶9̶0̶ ̶T̶L̶      ← (a) ÜSTÜ ÇİZİLİ ESKİ FİYAT   │  → varsa PROMOSYON = FACT
│                                              │
│   599 , 90 TL     ← ana fiyat (büyük punto)  │
│           KDV'li  ← (b) KDV İBARESİ          │  → C-551'in doğrudan cevabı
│                                              │
│  [AVANTAJLI FİYAT] ← (c) KIRMIZI ROZET       │  → varsa PROMOSYON = FACT
│  L fiyatı: 799,87 TL ← (d) BİRİM FİYAT SATIRI│  → "ikinci sayı" bu mu?
│  Geçerlilik: __.__ - __.__  ← (e) KAMPANYA TARİHİ │
└──────────────────────────────────────────────┘
```

| İşaret | Sahada | Ne kanıtlar |
|---|---|---|
| **(a) Üstü çizili eski fiyat** | `VAR` / `YOK` / `OKUNMADI` | VAR → fiyat **promosyonludur** (`T-504` tek ziyarette kapanır). Eski fiyatı da yaz → `normal_fiyat` |
| **(b) KDV ibaresi — TAM METİN** | `KDV'li` / `KDV Hariç` / **çift satır** / **ibare yok** | `C-551`. **Çift satır varsa iki sayıyı da yaz** (2010 şarap kataloğu çiftliydi — `EV-2026-08-10-503`) |
| **(c) "AVANTAJLI FİYAT" rozeti** | `VAR` / `YOK` / `OKUNMADI` | `T-504`. Metro'nun promosyon etiket anatomisi (`EV-2026-08-09-504`) |
| **(d) Birim fiyat satırı** | tam metin (`L fiyatı: …`) | `OQ-001 §7`: "iki fiyat gördük, hangisini okuduk?" endişesini **rafta** kapatır — ikinci sayının **birim fiyat** olduğu broşürden değil raftan doğrulanmalı |
| **(e) Kampanya geçerlilik tarihi / "stoklarla sınırlıdır"** | `VAR` / `YOK` | Metro'nun tarihsel şarap fiyatı **dönemseldi** (`EV-2026-08-10-503`); tarih varsa fiyat **süresiz raf fiyatı değildir** |

> **DÜRÜSTLÜK KURALI:** (a) ve (c) **YOK** çıkarsa bu, "fiyat normaldir"in
> **kanıtı değildir** — yalnızca zayıf bir negatiftir. `T-504` bu durumda
> **ikinci ziyaretle** kapanır (§F). Tek ziyaretle `T-504` ancak **promosyon
> işareti BULUNURSA** kapanır. Bu asimetri bilerek kabul edilmiştir.

---

## E. ARKA ETİKET — İTHALATÇI ADI (`İP-008` · `OQ-503` · `T-405`)

Türkçe arka etiketten okunacak ve **her ithal SKU için zorunlu**:

```
[ ] İthalatçı / dağıtıcı firma ünvanı  : ______________________  ← ASIL HEDEF
[ ] Üretici / şişeleyici               : ______________________
[ ] Alkol derecesi (% vol)             : ______
[ ] Net hacim                          : ______ ml
[ ] Menşe ülke (arka etiket yazımı)    : ______________________
```

**Neden:** "Hangi ithalatçı hangi markayı getiriyor" sorusu bugün
**1 doğrulanmış ithalatçıya** dayanıyor (`pazar.yaml →
ithalatci_haritasi.dogrulanmis_ithalatci_sayisi: 1`). Arka etiket bunu
**tek ziyarette kanıtlı** hâle getirir. **Gold Country ve Central Creek'in
arka etiketi öncelikli** (`OQ-503` — hiçbir kaynakta bulunamadı).

> Şişeyi eline alıp çevirmek gerekir; raf fotoğrafı arka etiketi göstermez.

---

## F. HEDEF SKU ARAMA LİSTESİ — "yok" mu, "var ama dönmüyor" mu (`C-561` · `OQ-552` · `C-501`)

Her mağazada **tek tek arayıp** işaretle. **Bulunmayan da bir veridir.**

| Aranan SKU | Bulundu? | Raf fiyatı | Stok |
|---|---|---|---|
| **Gold Country** (California) — *benchmark* | V / Y | | |
| **Central Creek** (Avustralya) — *benchmark* | V / Y | | |
| Santa Helena | V / Y | | |
| M. Chapoutier Belleruche | V / Y | | |
| Babich | V / Y | | |
| Hans Baer Pinot Noir | V / Y | | |
| Henkell | V / Y | | |
| Terra Mater Reserve | V / Y | | |
| Botter Caleo | V / Y | | |
| Luccarelli Primitivo | V / Y | | |
| Barone Montalto | V / Y | | |
| La Vieille Ferme | V / Y | | |
| Alpaca | V / Y | | |
| Tesori Prosecco | V / Y | | |

*(Liste kaynağı: `OQ-552` + `EV-2026-08-10-552` — bu isimler tek online kanalda
**katalogda tanımlı ama stok dışıydı**. Fiziksel rafta **varsa** "boşluk" bir
kanal artefaktıdır; **yoksa** bulgu güçlenir.)*

---

## G. SAYIM FORMU — mağaza başına 1 kez (`C-561`'in asıl testi)

> **SKU kaydından ayrıdır.** Burada tek tek fiyat yazılmaz, sadece **sayılır**.
> Etiketler sayılır (facing değil). 5 dakika.

| Bant (TL) | İTHAL SKU adedi | YERLİ SKU adedi |
|---|---|---|
| 400 – 600 | | |
| 600 – 800 | | |
| 800 – 1.000 | | |
| 1.000 – 1.200 | | |
| **400–1.200 TOPLAM** | | |

```
[ ] Rafta EN UCUZ İTHAL şarap        : ____________________  ______ TL
[ ] Rafta EN UCUZ şarap (yerli dahil): ____________________  ______ TL
[ ] Reyonda toplam şarap SKU (kaba)  : ______
[ ] 400 TL altında hiç şarap var mı? : ( ) E  ( ) H
[ ] Köpüklü/şampanya bandın içinde sayıldı mı? ( ) E  ( ) H   ← ayrı işaretle
```

---

## H. FOTOĞRAF PROTOKOLÜ

| Kod | Ne | Kaç adet | Zorunlu? | İçermeli |
|---|---|---|---|---|
| **F0** | **Mağaza kimliği** — tabela / reyon künyesi / kasa fişi başlığı | 1 / mağaza | **EVET** | Mağaza adı + mümkünse şube. `benchmark_1.magaza / sehir = UNKNOWN` bunu bekliyor |
| **F1** | **Raf geneli** — şarap reyonu | 3–5 / mağaza | **EVET** | Reyonun tamamı, **%30 örtüşmeli** ardışık kareler. Bant yoğunluğunu ve boş facing'leri gösterir |
| **F2** | **Etiket yakın çekim** | **HER kaydedilen SKU için 1** | **EVET** | Etiketin **tamamı** çerçevede: büyük punto fiyat + **KDV ibaresi** + **birim fiyat satırı** + varsa **üstü çizili fiyat** + varsa **rozet** + varsa kampanya tarihi. **Bu foto olmadan satır geçersizdir.** |
| **F3** | **Arka etiket** | Her **ithal** SKU için 1 | **EVET (ithal)** | İthalatçı firma ünvanı satırı + ABV + hacim |
| **F4** | **Kasa fişi** | 1–2 şişe alınırsa | Şiddetle önerilir | Ürün adı + ödenen tutar + **KDV satırı**. `OQ-001`'i en güçlü kapatan tek kanıt (~600 TL) |
| **F5** | Ön etiket (marka/vintage okunmuyorsa) | gerektiğinde | Hayır | — |

**Okunabilirlik kriteri (bağlayıcı):**
- Fotoğraf, ekranda **%100 zoom'da etiketin EN KÜÇÜK yazısı okunuyorsa** geçerlidir.
  Okunmuyorsa satır `kdv_gosterimi = OKUNMADI` olur — **tahmin edilmez.**
- 20–30 cm mesafe, etiket kadraja **paralel**, flaş **kapalı**.
- **ESL (elektronik etiket)** ise ekran parlamasını kırmak için ~30° açı; LED
  titremesi için 1 yerine **2 kare** çek.
- Şişe **rafta dururken** çek; ürünü başka rafa taşıma (fiyat–ürün eşleşmesi bozulur).
- **EXIF tarih/saat açık kalsın** — gözlem tarihinin ikinci kanıtıdır.

**Dosya adlandırma (zorunlu):**
`YYYYMMDD_KANAL_SEHIR_SUBE_SIRANO_TIP.jpg`
→ `20260812_METRO_IST_BAYRAMPASA_007_ETIKET.jpg` · `..._007_ARKA.jpg` ·
`..._000_F0.jpg` · `..._RAF01.jpg`

**Tahmini foto sayısı:** mağaza başına ≈ 1 + 4 + 20 + 8 = **33**;
6 mağazalık tur ≈ **200 fotoğraf**.

---

## I. 30 DAKİKALIK MAĞAZA BÜTÇESİ

| Dakika | İş |
|---|---|
| 0–2 | F0 + mağaza başlığını doldur (§B) |
| 2–5 | F1 raf geneli — reyonu baştan sona ardışık kareler |
| 5–10 | **Sayım formu** (§G) — sadece say, fiyat yazma |
| 10–25 | SKU satırları: 8 alan + **F2** (SKU başına ~45 sn, ~20 SKU) |
| 25–29 | İthal şişelerin **arka etiketi** (F3) + arama listesi (§F) |
| 29–30 | Eksik kontrolü: her satırın F2'si var mı? |

---
---

# SAYFA 2 — GEREKÇE (sahada okunması gerekmez)

## J. HER ALAN NEDEN VAR VE HANGİ AÇIK KAYDI KAPATIR

| Alan | Neden gerekli | Kapattığı / beslediği kayıt |
|---|---|---|
| `magaza` + `sehir` | Bugün **benchmark'ın mağazası ve şehri `UNKNOWN`**. Lokalize olmayan T4 gözlemi kayda değmez (charter kuralı) | `OQ-001` (mağaza/şehir ayağı) · `pazar.yaml → benchmark_1.magaza/sehir` · `T-917 P1` |
| `kanal_tipi` | **K1**: `L8_METRO_CASH_CARRY` ≠ `L8_CHAIN_RETAIL`, birbirinin yerine geçemez | `T-701` · `T-603` · `T-917 P2` |
| `gozlem_tarihi` | `ttl: 30d`; ayrıca promosyonun dönemselliği ancak tarihle ölçülür | `99-ops/veri-tazeligi.md` · `T-504` |
| `sku_adi` · `marka` | Aynı SKU'nun kanallar arası izlenmesi (Metro ↔ zincir farkı) | `T-701` · `C-501` |
| `mensei` (İTH/YRL) | Sayımın tamamı bu ayrıma dayanıyor: "bantta ithal var mı?" | `C-501` · `C-561` · `OQ-552` |
| `hacim_ml` | 750 dışı SKU fiyat karşılaştırmasını bozar; **Central Creek'in hacmi bugün `UNKNOWN`** | `pazar.yaml → benchmark_2.hacim_ml` |
| `abv_pct` | Benchmark ABV `UNKNOWN`; GTİP alt kırılımı için **ipucu** *(sonuç `gumruk-vergi-uzmani`nındır — burada üretilmez)* | `pazar.yaml → benchmark_1.abv_pct` |
| `urun_tipi` | Köpüklü ≠ sakin şarap; segment bantları karışmasın | `segment.*` |
| **`raf_fiyati`** | Ana gözlem — L8 | `l8_chain_retail` · `raf-fiyat-gozlemleri.csv` |
| **`kdv_gosterimi` (tam metin)** | Mevcut `KDV_DAHIL` sonucu **içinde sıfır alkol SKU'su olan broşürlerden** çıkarımdır (`EV-2026-08-09-514`); projenin bulduğu **tek** Metro şarap fiyat iletişimi **çiftliydi** (`EV-2026-08-10-503`). Broşürden değil **raftan** doğrulama gerekiyor | **`C-551`** · `OQ-001` KDV ayağı · `benchmark_*.kdv_durumu.confidence` |
| `birim_fiyat_satiri` | `OQ-001 §7`'nin "ikinci sayı birim fiyattır" tespiti **broşüre** dayanıyor; rafta doğrulanmadı | `OQ-001` · `C-551` |
| **`kampanya_etiketi` (a/c/e)** | Promosyon/normal ayrımı **tanım gereği** ya etiket işaretiyle ya iki tarihli gözlemle yapılır | **`T-504`** · `BM_C` senaryosu · `benchmark_*.promosyon_durumu` |
| `normal_fiyat` | Üstü çizili fiyat varsa gerçek referans odur | `T-504` |
| `stok_durumu` (DOLU/AZ/BOŞ) | `C-561`'in asıl sorusu: **"yok" mu, "var ama dönmüyor" mu** | `C-561` · `OQ-552` |
| **`ithalatci_distributor`** (arka etiket) | Bugün doğrulanmış ithalatçı sayısı **1**; benchmark'ın ithalatçısı `UNKNOWN` | `İP-008` · `OQ-503` · `T-405` · `ithalatci_haritasi` |
| `foto_id` | Foto olmadan T4 gözlemi kanıtlanamaz; repoda benchmark'ın **snapshot'ı bile yok** | CLAUDE.md §4 · `T-917 P4` |
| Sayım formu (§G) | 400–1.200 TL bandının **fiziksel** yoğunluğu; bugünkü eğri **tek online kanaldan** ve o kanal premium'a kayık (`EV-2026-08-10-702`) | **`C-501`** · `C-561` · `segment.ithal_sku_400_800_*` |
| Arama listesi (§F) | *"bakıldı, yok"* ile *"bakılmadı"* ayrımı | `T-917 P7` · `OQ-552` |

---

## K. BU TUR YAPILIRSA KAPANACAK KAYITLAR

| Kayıt | Bugün | Saha turundan sonra | Koşul |
|---|---|---|---|
| **`T-917`** | OPEN | **RESOLVED** | Asgari kapsam (§A) tutturulursa |
| **`T-504`** | OPEN (HIGH) | **RESOLVED** *(promosyon işareti bulunursa)* / **ANSWERED→ikinci ziyaret** *(bulunmazsa)* | §D(a)(c)(e) + §F ikinci ziyaret |
| **`C-551`** | OPEN (HIGH) | **RESOLVED** | Şarap rafında etiketin KDV satırı okunabilir F2'de görülürse |
| **`OQ-001`** | PARTIALLY_RESOLVED | **RESOLVED** *(KDV + mağaza/şehir + promosyon üçü birlikte kapanırsa)* | Aksi hâlde promosyon ayağı açık kalır |
| **`T-701` / `T-603`** | OPEN (HIGH) | **ANSWERED** — `l8_chain_retail` **dağılım olarak** dolar | ≥8 ithal zincir SKU |
| **`OQ-502`** | OPEN (HIGH) | **RESOLVED** | Zincir + tekel bayii gözlemi |
| **`C-501`** | OPEN (HIGH) | **RESOLVED veya ÇÜRÜTÜLÜR** | Fiziksel raf, `available` filtresinden **bağımsız** ikinci ölçümdür |
| **`C-561` / `OQ-552`** | RESOLVED(tanım) / OPEN | **OQ-552 RESOLVED** | §F arama listesi + `stok_durumu` |
| **`OQ-503` / `T-405`** | OPEN | **RESOLVED** | Benchmark SKU'ların arka etiketi okunursa |
| `pazar.yaml` alanları | `null`/`UNKNOWN` | Dolabilir: `l8_chain_retail`, `benchmark_*.promosyon_durumu`, `kdv_durumu.confidence`, `benchmark_*.magaza/sehir`, `benchmark_1.abv_pct`, `benchmark_2.hacim_ml`, `segment.ithal_sku_400_800_*`, `ithalatci_haritasi.*`, `kanal_yapisi.tekel_bayii_fiyatlari` | Doldurmayı **bu ajan** yapar, gözlemci değil |

> **`kanal.yaml → m_retail`** bu turdan **beslenir ama burada hesaplanmaz.**
> Raf fiyatı gözlenir; **marj `kanal-marj-uzmani`nın işidir** (K4).

---

## L. TURU GEÇERSİZ KILAN 6 HATA

1. **F2'siz satır** — etiket fotoğrafı olmayan fiyat kayda geçmez.
2. **Etiketin ince yazısını "hatırlayarak" doldurmak** — okunmuyorsa `OKUNMADI`.
3. **Promosyon işareti yokluğunu "normal fiyat" diye yazmak** — o `UNKNOWN`'dır.
4. **Metro fiyatını zincir market fiyatıyla aynı sütunda toplamak** — K1 ihlali.
5. **Sadece ilgi çekici SKU'ları kaydetmek** — bandın **tamamı** taranır, yoksa sayım yanlıdır.
6. **Şişeyi rafından çıkarıp başka yere koymak** — fiyat/ürün eşleşmesi bozulur.

---

## M. VERİ NEREYE GİRER

1. Sahada: kağıt form / telefon notu + fotoğraflar.
2. Masabaşı: `60-pazar/saha-veri-sablonu.csv` doldurulur (kolonlar
   `raf-fiyat-gozlemleri.csv` ile **birebir uyumlu**, sonuna `SAHA_*` alanları eklidir).
3. `turkiye-pazar-kasifi` satırları `raf-fiyat-gozlemleri.csv`'ye taşır,
   **her mağaza için ayrı kanıt kartı** açar (`gozlem_yontemi = MAGAZA_FOTO`,
   `tier: T4`, `ttl: 30d`), `10-evidence/index.csv`'ye işler.
4. Fotoğraflar `10-evidence/snapshots/` altına konur → `snapshot_path`
   (bugün benchmark'ın snapshot'ı **yok**; bu bir kanıt zayıflığıdır).
5. `pazar.yaml` güncellemesi **öneri** olarak sunulur; merge kararı başkanındır.
