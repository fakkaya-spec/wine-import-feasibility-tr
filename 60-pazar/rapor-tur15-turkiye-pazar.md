# AJAN RAPORU — TÜRKİYE PAZAR KÂŞİFİ

```yaml
ajan:               turkiye-pazar-kasifi
tur:                TUR 1.5 (BLOCKER REMEDIATION)
tarih:              2026-08-10
durum:              SUBMITTED
kapsam:             DAR — yalnizca T-903 ve T-504. Yeni pazar arastirmasi ACILMADI.
```

---

## 1. YÖNETİCİ ÖZETİ

İki görev vardı. **Biri kapandı, biri kapanmadı.**

**T-903 → `RESOLVED`.** `80-model/inputs/pazar.yaml` oluşturuldu. TUR 1'in tek
gerçek pazar verisi artık bir model girdi dosyasında yaşıyor: benchmark 599,90 TL
(`EV-2026-08-09-501`), `KDV_DAHIL` (ESTIMATE), `L8_METRO_CASH_CARRY` (ESTIMATE),
segment bandı 600–900 TL (ESTIMATE, türetme zinciri dosyada). Başkanın K1–K3
katman kuralları dosyanın **içine** yazıldı; ben K4'ü ekledim (*bu dosyadan marj
türetilemez*). `EV-509`/`-510` tarih hatası CLAUDE.md §4'e uygun giderildi:
kartlar düzeltilmedi, yerlerine `EV-2026-08-10-501`/`-502` açıldı, eskilerin
**yalnızca `status`** alanı `SUPERSEDED` yapıldı. Doğru `publication_date`
**uydurulmadı** — canlı feed'i bugün yeniden çekmek düzeltme değil *yeni gözlem*
olurdu; alan `UNKNOWN`'a çekildi. **Referans bütünlüğü programatik olarak
doğrulandı: 19/19 evidence_id hem index kaydında hem raw kartında mevcut,
başarısız referans = 0.**

**T-504 → `OPEN` kalır.** Promosyon sorusu için **8 ayrı masabaşı yol** denendi;
hepsi kapalı çıktı (`EV-2026-08-10-504`). Benchmark SKU'larının 09.08.2026
dışında **ikinci bir tarihli fiyat izi hiçbir erişilebilir kaynakta yoktur.**
Cevap **`UNKNOWN`**'dır ve tahminle kapatılmamıştır. **OQ-001
`PARTIALLY_RESOLVED` olarak kalır; G3 açılmaz.**

**Bu turun beklenmedik bulgusu:** Web Archive'da Metro Türkiye'nin
**2008/2009/2010 şarap katalogları** bulundu. Üçünün de künyesi *"fiyatlar
**KDV Hariç ve KDV'li** olarak verilmiştir"* diyor ve fiyat kutuları fiilen
**çift** (`131,36 / 155,00 KDV'li`, oran 1,18). Yani OQ-001'in "çürüdü" ilan
edilen kurucu hipotezi, Metro'nun **şarap kategorisinde fiilen uygulanmış bir
formattır**. Sonucu **kendiliğimden değiştirmedim** (CLAUDE.md §1.13):
`C-551` açıldı, `T-551` ile başkana taşındı, `pazar.yaml`'daki değer
`KDV_DAHIL` olarak **korundu**.

---

## 2. BULGULAR

### B-1: `pazar.yaml` oluşturuldu ve referans bütünlüğü tam

```yaml
claim:          80-model/inputs/pazar.yaml mevcuttur ve icindeki her evidence_id kanit sisteminde karsiligi olan gercek bir karta isaret eder
value:          19 / 19 referans dogrulandi; basarisiz = 0
unit:           adet
status:         FACT
tier:           -
evidence_id:    -   (dogrulama ciktisi T-903 ticket'inda tam metin olarak kayitli)
effective_date: 2026-08-10
katman:         -
```

**Gerekçe:** Programatik kontrol (a) `10-evidence/index.csv` + `_index-parts/*.csv`
içinde varlık, (b) `10-evidence/raw/EV-….md` dosyasının varlık kontrolünü ayrı
ayrı yaptı. 15 referans ana `index.csv`'den, 4 referans bu turda açılan
`_index-parts/turkiye-pazar-kasifi-tur15.csv`'den karşılandı.
Ek olarak dört yeni kartın `publication_date ≤ access_date` mantığı da
doğrulandı — bu turda düzeltilen hatanın tekrarlanmadığı kanıtlandı.

---

### B-2: Benchmark promosyon durumu — `UNKNOWN`, 8 yol kapalı

```yaml
claim:          Benchmark SKU'larinin 09.08.2026 disinda ikinci bir tarihli fiyat izi hicbir erisilebilir kaynakta YOKTUR
value:          null
unit:           -
status:         UNKNOWN
tier:           T4
evidence_id:    EV-2026-08-10-504
effective_date: -
katman:         L8_METRO_CASH_CARRY (sorgulanan sayinin katmani)
```

**Gerekçe:** Metro canlı siteleri (403), Metro `/shop` (login-gated SPA), Metro'nun
arşivden tespit edilen açık fiyat API'si (404, emekli), `/UrunListeleri` kategori
sayfaları (404), 2026-07-02 tarihli Web Archive shop snapshot'ı (SPA kabuğu, fiyat
yok), `metro-tr.com` alan adında taranan 20.000 arşiv URL'si (tek şarap fiyat
kaynağı 2008–2010 katalogları; benchmark SKU'ları **yok**), cimri/akakçe (403),
web araması (yalnızca `C-503` ile kapatılmış T5 içerik çiftlikleri; SKU'lar orada
da yok).

**Bu bir başarısızlık değil, bir yapı tespitidir:** Türkiye'de alkolün broşür ve
online fiyat iletişimi kapalıdır (`EV-2026-08-09-514`, `-508`). Promosyon/normal
ayrımı **tanım gereği** iki tarihli gözlem ya da etiketin promosyon işaretlerini
gerektirir. Bu veri masabaşından **hiçbir zaman** gelmeyecektir.

---

### B-3: Metro'nun ŞARAP kataloglarında çiftli KDV gösterimi VARDI (2008–2010)

```yaml
claim:          Metro Turkiye'nin arsivlenmis sarap kataloglarinda fiyatlar 'KDV Haric ve KDV'li' olarak CIFTLI gosterilmistir
value:          "131,36 / 155,00 KDV'li ; 262,71 / 310,00 KDV'li ; 11,86 / 13,99 KDV'li ; 32,20 / 37,99 KDV'li (oran 1,18)"
unit:           TRY
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-503
effective_date: 2010-12-09
katman:         L8_METRO_CASH_CARRY (tarihsel)
```

**Gerekçe:** Üç katalog PDF'i (04–31 Aralık 2008 · 03–31 Aralık 2009 ·
09 Aralık 2010 – 06 Ocak 2011) Web Archive'dan indirilip metne çevrildi.
Üçünde de aynı künye cümlesi: *"Bu Metropost'taki fiyatlar KDV Hariç ve KDV'li
olarak verilmiştir."*

**Ne yaptım, ne yapmadım:**
- **Yapmadım:** KDV sonucunu değiştirmedim. Bu tur bana onu *korunacak
  doğrulama* olarak verdi.
- **Yaptım:** Kanıt kartını açtım, `C-551` çelişkisini kaydettim, `T-551` ile
  başkana taşıdım, `pazar.yaml`'da yalnızca `conflict_id: C-551` işareti koydum.

**Sonucu neden hâlâ ayakta görüyorum (ESTIMATE, kanıt değil):** Gözlenen **her**
Metro çiftinde "pazarlama-yuvarlak" sayı **KDV'li** olandır (155,00 / 310,00 /
13,99 / 37,99); KDV hariç olan türetilmiş ondalıklıdır (131,36 / 262,71 / 11,86 /
32,20). `599,90` ve `649,90` pazarlama-yuvarlak sayılardır. 599,90 KDV hariç
olsaydı brütü `719,88` olurdu — Metro'nun hiçbir dönemde kullanmadığı bir bitiş
deseni.

**Neden yine de rahatsız edici:** TUR 1'in KDV sonucu, içinde **sıfır alkol**
bulunan broşürlerden şarap rafına yapılmış bir **çıkarımdır**. Bu kart, projenin
bulabildiği **tek Metro şarap kategorisi fiyat iletişimidir** — ve orada çiftli
gösterim **vardır**.

---

### B-4: Metro'nun tarihsel şarap fiyatları DÖNEMSELDİ

```yaml
claim:          Metro sarap kataloglarinin kunyesi fiyatlarin belirli bir tarih araliginda gecerli ve stoklarla sinirli oldugunu soyler
value:          "Bu Metropost'taki fiyatlar 03 Aralik - 31 Aralik 2009 tarihleri arasinda ... gecerlidir ve stoklarla sinirlidir"
unit:           -
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-503
effective_date: 2009-12-03
katman:         -
```

**Gerekçe:** *"Metro şarap rafında kendiliğinden bir **normal fiyat** vardır"*
varsayımı bu kanalda otomatik değildir. Promosyon ihtimalini **elemez, artırır**.
Ancak 16–18 yıllık bir kayıttır ve 2026 için kanıt değildir; `T-504`'ü çözmez.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | **Benchmark promosyonlu mu, normal fiyat mı** | 8 masabaşı yolun tamamı kapalı; SKU'nun ikinci tarihli fiyat izi yok | **CRITICAL** | Fiziksel: etiket fotoğrafı + 2–4 hafta sonra ikinci gözlem + kasa fişi (`T-504`) |
| 2 | **2026 şarap reyonu fiziksel etiketinin mizanpajı** | Broşürlerde 0 alkol var; raf etiketi görülmedi | **CRITICAL** | Aynı ziyaret (`T-504`) |
| 3 | `EV-509`/`-510`'un gerçek feed `publication_date`'i | Canlı feed; bugün çekmek *yeni gözlem* olur, düzeltme olmaz | LOW | Yeni bir gözlem turunda feed `updated_at` alanı **ayrıca** kaydedilmeli |
| 4 | `C-551` çözümü: 2010 şarap kataloğu formatı 2026'da geçerli mi | 2013 sonrası Metro şarap katalogu yayınlamıyor | HIGH | Fiziksel etiket fotoğrafı (aynı ziyaret) — `T-551` |
| 5 | Metro'nun şarap assortman büyüklüğü ("502 çeşit / 160 ithal") | Birincil kaynağa ulaşılamadı; kanıt kartı **açılmadı** | MEDIUM | Fiziksel mağaza turunda sayım (`OQ-551`) |
| 6–13 | TUR 1'den devreden UNKNOWN'lar (zincir L8, ithalat hacmi, ithalatçı haritası, HoReCa, tekel bayii, ABV, mağaza/şehir, Central Creek hacmi) | **Bu turda araştırılmadı — kapsam dışı** | HIGH/MEDIUM | TUR 2 |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-551** | `EV-2026-08-09-503/504` (T4 / 2026-08): Metro broşürlerinde **tek** fiyat + `KDV'li`; ikinci sayı **birim fiyat**. İncelenen broşürlerde **0 alkol SKU'su** | `EV-2026-08-10-503` (T4 / 2008–**2010**): Metro **şarap** kataloglarında *"fiyatlar KDV Hariç ve KDV'li olarak verilmiştir"* + fiilen **çift** fiyat kutusu | Çözüm hiyerarşisinin **kural 2 (tarih)** A'yı, **kural 4 (kapsam)** B'yi işaret ediyor — **zıt yön**. İkisi de T4, ikisi de Metro'nun kendi künyeli yayını | **OPEN** → `T-551` |

Ayrıntı: `99-ops/_parts/celiskiler-turkiye-pazar-kasifi-tur15.md`
*(TUR 1'den devreden `C-501`, `C-502`, `C-503` bu turda ele alınmadı.)*

---

## 5. MODEL GİRDİLERİ

**Bu turda `pazar.yaml` YENİ sayı üretmemiştir.** TUR 1 değerleri dosyaya
taşınmış, iki `evidence_id` düzeltilmiş referansla değiştirilmiştir.

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| `pazar.yaml` | `benchmark_1.raf_fiyati_try` | 599.90 | TRY | FACT | `EV-2026-08-09-501` |
| `pazar.yaml` | `benchmark_1.kdv_durumu` | `KDV_DAHIL` | - | ESTIMATE (HIGH) ⚠`C-551` | `EV-...-503/504/505/506` |
| `pazar.yaml` | `benchmark_1.katman` | `L8_METRO_CASH_CARRY` | - | ESTIMATE | `EV-...-505/507` |
| `pazar.yaml` | `benchmark_1.promosyon_durumu` | `null` | - | **UNKNOWN** | `EV-2026-08-10-504` (`T-504`) |
| `pazar.yaml` | `benchmark_1.hacim_ml` | 750 | ml | FACT | `EV-2026-08-09-501` |
| `pazar.yaml` | `benchmark_2.raf_fiyati_try` | 649.90 | TRY | FACT | `EV-2026-08-09-502` |
| `pazar.yaml` | `benchmark_2.hacim_ml` | `null` | ml | **UNKNOWN** | `EV-2026-08-09-502` |
| `pazar.yaml` | `segment.fiyat_performans_alt_try` | 600 | TRY | ESTIMATE | `EV-2026-08-10-501/502` |
| `pazar.yaml` | `segment.fiyat_performans_ust_try` | 900 | TRY | ESTIMATE | `EV-2026-08-10-501/502` |
| `pazar.yaml` | `segment.ithal_min_stokta_uzman_kanal_try` | 875.00 | TRY | FACT | `EV-2026-08-10-501` |
| `pazar.yaml` | `segment.ithal_sku_400_800_uzman_kanal` | 0 | adet | FACT ⚠`C-501` | `EV-2026-08-10-501` |
| `pazar.yaml` | `segment.yerli_rakip_sku_600_800` | 25 | adet | FACT | `EV-2026-08-10-502` |
| `pazar.yaml` | `segment.yerli_min_stokta_uzman_kanal_try` | 460.00 | TRY | FACT | `EV-2026-08-10-502` |
| `pazar.yaml` | `l8_chain_retail.deger_try` | `null` | TRY | **UNKNOWN** | `EV-2026-08-09-511` |
| `pazar.yaml` | `l7_retailer_purchase_price.deger_try` | `null` | TRY | **UNKNOWN** | — (K2: bu ajan dolduramaz) |
| `pazar.yaml` | `horeca.fiyat_carpani` | `null` | x | **UNKNOWN** | — |
| `pazar.yaml` | `horeca.metro_magaza_vs_sevkiyat_fiyat_rejimi` | FARKLI | - | FACT | `EV-2026-08-09-507` |
| `pazar.yaml` | `pazar_hacmi.ithalat_hacmi_litre` | `null` | litre | **UNKNOWN** | `EV-2026-08-09-515` |
| `pazar.yaml` | `ithalatci_haritasi.dogrulanmis_ithalatci_sayisi` | 1 | adet | FACT | `EV-2026-08-09-513` |
| `pazar.yaml` | `kanal_yapisi.metro_brosurunde_alkol_sku_sayisi` | 0 | adet | FACT | `EV-2026-08-09-514` |
| `pazar.yaml` | `gozlem_havuzu.tek_kanal_yogunlasmasi_uyarisi` | 45/52 tek kanal | - | FACT | `EV-...-501/502/512` |

**evidence_id'si olmayan satır modele giremez.**
`modele_giremez` kara listesi dosyaya yazıldı: `EV-2026-08-09-512` (T5 içerik
çiftliği) + iki `SUPERSEDED` kart.

`senaryolar.yaml` ve `urun.yaml`'a **DOKUNULMADI** (sahiplik/onay başkanda).

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `kanal-marj-uzmani` | Metro'nun 2010 şarap kataloğunda KDV hariç sayı **ondalıklı** (131,36), KDV'li sayı **yuvarlak** (155,00) | Metro şarapta **brütten geriye** çalışıyor. Pazarlıkta matrah yönü önemli. |
| `kanal-marj-uzmani` | Metro'nun tarihsel şarap fiyatları **dönemsel** ("stoklarla sınırlıdır") | Fiyat taahhüdünün **süresi** sorulmalı |
| `mevzuat-ruhsat-uzmani` | Metro 2013'e kadar basılı şarap katalogu yayınlıyordu; 2026'da hiç alkol yok | Somut "önce/sonra" karşılaştırması *(yasağın kapsamı bu turda yeniden araştırılmadı)* |
| `global-sourcing-kasifi` | Metro'nun 2008–2010 assortmanında **ABD ve Avustralya menşe zaten vardı** (Terra California, Sunset Creek, Yellow Tail, Huntington, Gallo) | `EV-509`'un "uzman kanalda ABD/AU yok" bulgusuyla birleşince: bu menşeler **cash&carry/market kanalının** menşeleridir, uzman kanalın değil |
| `finans-fizibilite` | K4: `pazar.yaml`'dan **marj türetilemez**; 599,90 ↔ 875 TL farkı kasten hesaplanmadı | İki sayı farklı kanal **ve** farklı katman etiketli |
| `yatirim-komitesi-baskani` | `index.csv`'de `EV-509`/`-510` hâlâ `FACT`; raw kartlar `SUPERSEDED` | Merge'de düzeltilmezse desenkron kalır |

Tam liste: `99-ops/_parts/capraz-ipuclari-turkiye-pazar-kasifi-tur15.md`

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| `T-903` | `turkiye-pazar-kasifi` | `pazar.yaml` yok + `EV-509/510` tarih hatası | HIGH | **RESOLVED** ✅ |
| `T-504` | `yatirim-komitesi-baskani` | OQ-001 promosyon ayağı | **CRITICAL** | **OPEN** (girişim kaydedildi, kapanmadı) |
| `T-551` | `yatirim-komitesi-baskani` | Metro **şarap** kataloglarında çiftli KDV gösterimi vardı → `C-551` | HIGH | **OPEN** (yeni) |

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-10-501` | 30d | 2026-09-08 *(gözlem tarihi 2026-08-09'dur, kart tarihi değil)* |
| `EV-2026-08-10-502` | 30d | 2026-09-08 |
| `EV-2026-08-10-503` | 365d | 2027-08-10 *(tarihsel arşiv kaydı — eskimez, ama 2026'yı da temsil etmez)* |
| `EV-2026-08-10-504` | 30d | 2026-09-09 *(negatif arama; Metro kanalları açılırsa erken tazelenmeli)* |

**Uyarı değişmedi:** tüm raf gözlemleri **2026-09-08**'de STALE olur. TUR 3 o
tarihten sonra çalıştırılırsa `pazar.yaml`'daki hiçbir fiyat yeniden
doğrulanmadan model çıktısını `DRAFT`'tan yukarı taşıyamaz.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Şarap reyonundaki 2026 tarihli fiziksel raf etiketinin, üzerinde iki fiyat
(KDV hariç + KDV'li) bulunduğunu gösteren tek bir fotoğraf.**

O fotoğraf, `pazar.yaml`'daki `benchmark_1.kdv_durumu = KDV_DAHIL` satırını
ve dolayısıyla dosyanın **en çok kullanılacak sayısını** çürütür. Bu turdan
önce bu ihtimali "hipotez çürüdü" diye kapatmıştım; `EV-2026-08-10-503` bana
kapatmakta acele ettiğimi gösterdi.

İkinci çürütücü: **benchmark'ın promosyonlu olduğunun ortaya çıkması.**
Hâlâ elenmedi ve bu turda elenemedi.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"Metro'nun 2026 genel broşür fiyat formatı = 2026 şarap raf etiketi formatı."**

Kırılgan çünkü bu turda tam da bu çıkarımın **karşı örneğini** buldum:
Metro'nun şarap kategorisi, genel broşürden **farklı** bir fiyat gösterim
formatı kullanmıştı (2010). Kategori bazlı format farkı bu şirkette
**gerçekleşmiş bir olaydır**, teorik bir endişe değil.

İkinci kırılgan varsayım (TUR 1'den devrediyor, düzelmedi):
**`available: true` filtresinin doğru filtre olduğu.** Segment bandının
alt **ve** üst sınırı buna dayanıyor ve `C-501` hâlâ `OPEN`.

Üçüncüsü: **45/52 gözlemin tek kanaldan gelmesi.** `pazar.yaml`'a uyarı olarak
yazdım, ama uyarı yazmak veriyi düzeltmez.

### 9.3 Hangi kaynağıma en az güveniyorum?

1. **`EV-2026-08-10-501` / `-502`** (iyisarap.plus feed'i). Düzeltme kartları
   **veriyi güçlendirmedi**, yalnızca tarih hijyenini düzeltti.
   `publication_date` artık `UNKNOWN`'dır — yani kaydın *daha az* bilgi içerdiği
   bir hâle geldi. Tek ticari sitenin fiyat politikası + hukuki statüsü belirsiz
   (`T-502`) + `C-501` açık.
2. **`EV-2026-08-10-503`'ten yaptığım "pazarlama-yuvarlak sayı KDV'li olandır"
   çıkarımı.** Bu bir desen okumasıdır, 4 fiyat çiftine dayanır ve **kanıt
   değildir**. `ESTIMATE` diye etiketledim; öyle okunmalı.
3. **`gozlem_havuzu.toplam_gozlem = 52`** gibi kendi tablomu sayan alanlar —
   `evidence_id: null`'dur. Kanıt kartı gerektirmezler ama denetlenebilir de
   değillerdir.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

- **`kdv_durumu` yanlışsa (aslında KDV hariçse):** benchmark'ın tüketici
  karşılığı KDV oranı kadar **yukarı** kayar → ters modelde ödenebilecek
  maksimum EXW/FOB **artar** → proje **daha kolay** görünür. Yani mevcut etiket
  **muhafazakâr yöndedir**; hata proje lehine sürpriz üretir.
- **Benchmark promosyonluysa:** normal fiyat daha yüksektir → yine lehte.
  **Ama** bu bir **stok eritme** fiyatıysa ve SKU pazardan çekiliyorsa,
  "bu bantta talep var" varsayımı çöker → **KILL yönünde**.
  `EV-2026-08-10-503`'teki *"stoklarla sınırlıdır"* künyesi bu ikinci ihtimali
  **artıran** bir izdir.
- **Segment bandı yanlışsa (`C-501`):** 600–900 TL bandında ithal rekabet
  **vardır** → fiyat baskısı sandığımdan yüksek → hedef EXW/FOB düşer →
  **KILL yönünde**.
- **`pazar.yaml`'ın kendisi yanlış okunursa:** K2 ihlal edilip
  `L8_METRO_CASH_CARRY` bir L7 proxy'si olarak kullanılırsa, model **kanal
  marjını iki kez** yer ve pozitif contribution **sahte** olur. Bu yüzden kural
  dosyanın içine yazıldı.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre | Maliyet |
|---|---|---|---|---|---|
| 1 | Şarap reyonu etiketinin tam fotoğrafı (küçük punto satırlar dahil) + mağaza/şehir | İnsan gözlemci | Metro ziyareti, 15 dk | 1 gün | ~0 |
| 2 | İkinci fiyat gözlemi (promosyon testi) — `T-504` | Aynı kişi | 2–4 hafta sonra aynı SKU | 4 hafta | ~0 |
| 3 | Kasa fişi (KDV satırı) — `T-504` + `T-551`'i **birlikte** kapatır | Aynı kişi | 1 şişe satın alma | 1 gün | ~600 TL |
| 4 | Şişe arka etiketi (ithalatçı satırı) | Aynı kişi | Aynı ziyaret | — | ~0 |
| 5 | `C-551` kararı | `yatirim-komitesi-baskani` | `T-551` | — | ~0 |
| 6 | `index.csv`'de `EV-509/510` → `SUPERSEDED` | `yatirim-komitesi-baskani` | `_index-parts` merge | — | ~0 |

**Kritik not:** 1–4'ün tamamı **tek ziyaret, ~600 TL**. Bu tur, masabaşı
yolların tamamının kapalı olduğunu **kanıtlayarak** bu listeyi kısalttı;
uzatmadı. **OQ-001 ve G3'ün önündeki engel pahalı değil — fiziksel.**
