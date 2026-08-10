# AJAN RAPORU — TÜRKİYE PAZAR KÂŞİFİ

```yaml
ajan:               turkiye-pazar-kasifi
tur:                TUR 2 (COMMERCIAL VALIDATION — DESTEK, DAR KAPSAM)
tarih:              2026-08-10
durum:              SUBMITTED
kapsam:             "SADECE 3 gorev: (1) 500-1.000 TL ithal SKU testi,
                     (2) sourcing kisa listesi marka varlik kontrolu,
                     (3) mevcut Turk ithalatci eslesmesi.
                     Benchmark KDV/promosyon arastirmasi YAPILMADI (kapsam disi).
                     7584 / reklam / raf-teshir arastirilmadi (ACCEPTED CONSTRAINT)."
```

---

## 1. YÖNETİCİ ÖZETİ

**Üç görevin üçü de yapıldı. Bir tanesi beklenmedik bir kapı açtı.**

**(1) 500–1.000 TL bandı.** TUR 1'in bulgusu **çürümedi, doğrulandı — ve nitelendi.**
Aynı kanal ikinci bir tarihte (2026-08-10) yeniden ölçüldü: stokta 80 ithal SKU,
en ucuzu **hâlâ 875 TL**, 0–800 TL bandında **hâlâ sıfır** (`EV-2026-08-10-551`).
TUR 2'nin sorduğu **500–1.000 TL** bandında stokta **2** ithal SKU vardır
(Tesori Prosecco 875 TL, La Piuma Chianti 948 TL) — ikisi de **TUR 1'de zaten
gözlenmişti, yeni değildir**. **YENİ doğrulanabilir ithal SKU sayısı: 0.**

Ama önemli bir nitelik bulundu: bu bantta **62 ithal ürün katalogda TANIMLIDIR**,
hepsi **stok dışıdır** (`EV-2026-08-10-552`). Yani bant *assortmanda dolu, stokta
boş*. Bu, "bu bantta ithal şarap yok" cümlesinden **farklı ve daha kötü** bir
cümledir: ürün var, dönmüyor olabilir. `C-561` açıldı, `T-561` ile başkana taşındı.
**`pazar.yaml`'a dokunulmadı.**

**(2) Kısa liste marka kontrolü.** Kontrol **iki kez** yapıldı: önce TUR 1 havuzu
(11 tedarikçi), sonra çalışma sırasında oluşan `supplier-shortlist-v2.csv`
(26 tedarikçi) + `top-10-rfq-targets.md` + `T-464`'ün 7 Model A markası.
**26 tedarikçinin 25'i ve 30+ marka adının tamamı bulunamadı**
(`EV-2026-08-10-553`, `EV-2026-08-10-564`). "Tormentoso" eşleşmesi **yalancı
pozitiftir** — MAN Vintners'ındır, Origin Wine'ın değil (`EV-2026-08-10-561`).

**TEK GERÇEK EŞLEŞME ve beklenmedik yerden geldi:** `SUP-452` **Cantina Danese
s.r.l.** — `top-10-rfq-targets.md`'nin **2. sıradaki RFQ hedefi** ve **Model B
(private label)** olarak sınıflanmış tedarikçi — **kendi markasıyla Türkiye'de
listelenmiştir** (*Danese Primitivo Puglia "Black Label"*, listeleme 1.419 TL,
**stokta değil**, ithalatçı iç etiketi `Midas`, kimlik `UNKNOWN`).
Yani private label modelinin sessiz varsayımı ("tedarikçinin Türkiye'de markası
yok → çakışma yok") **bu tedarikçide yanlıştır** → `T-565`.

`T-464` (global-sourcing → bu ajan) **ANSWERED**: 7 Model A markasının hiçbirinin
Türkiye'de ithalatçısı bulunamadı → Model A hedefleri listeden **düşmez**, ama
pazar validasyonu da **yoktur**.

**(3) Mevcut ithalatçı — TURUN EN BÜYÜK KAZANIMI.** Kısa liste için mevcut Türk
ithalatçısı **25/26 tedarikçide bulunamadı**; tek istisna yukarıdaki Cantina Danese.
Ama bunu ararken **Türkiye ithal şarap ithalatçı
haritası kısmen açıldı**: perakendeci ürün feed'indeki iç etiketlerin ithalatçı
grubu olduğu keşfedildi ve hipotez **iki bağımsız üretici/ithalatçı kaynağıyla
doğrulandı**. TUR 1'de **1** doğrulanmış ithalatçı vardı; artık **4 isimli grup +
13 kodu bilinen grup** var: **Kavaklıdere Şarapları**, **Karagözoğlu Dış Ticaret**,
**Adco Gıda**, **Baron Şarapçılık**.

**En rahatsız edici bulgu:** Kavaklıdere hem Türkiye'nin büyük **yerli üreticisi**,
hem **giriş-segment ithal şarabın distribütörü** (Gato Negro, Santa Helena,
Baron de Lestac, Moncigale). Hedef bandımızda rakip ile dağıtıcı **aynı şirket**
olabilir.

**14 kanıt kartı** (`EV-2026-08-10-551` … `-564`), **5 ticket açıldı**
(`T-561`…`T-565`), **1 ticket cevaplandı** (`T-464` → `ANSWERED`),
**1 çelişki** (`C-561`), **3 açık soru** (`OQ-551`…`OQ-553`).
`raf-fiyat-gozlemleri.csv`'ye **65 satır** eklendi (**OBS-601…665**; OBS-551/552 TUR 1'de kullanıldığı için ID bloğu 601'den başlatıldı) — ama bunların
**63'ü raf fiyatı DEĞİLDİR** ve modele giremez.

---

## 2. BULGULAR

### B-1: 500–1.000 TL bandında YENİ in-stock ithal SKU YOKTUR; TUR 1 bulgusu ikinci tarihte tekrarlandı

```yaml
claim:          10.08.2026'da ayni kanalda stokta ithal n=80, min 875 TL; 0-800 TL'de 0 SKU; 500-1.000 TL'de 2 SKU (ikisi de TUR 1'de gozlenmisti)
value:          "0 YENI SKU; 2 tekrar dogrulanmis SKU (875,00 / 948,00 TL)"
unit:           adet / TRY
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-551
effective_date: 2026-08-10
katman:         L8_ONLINE_UZMAN_PERAKENDE
```

**Gerekçe:** 429 ithal listelemenin 349'u `available=false`. Ölçüm `iyisarap.pro`'da
tekrarlandı: **birebir aynı sayılar** — yani iki alan adı aynı envanterdir,
**bağımsız kanal değildir**.

**Bant tanımı uyarısı:** TUR 1'in cümlesi *"400–800 TL'de 0 ithal SKU"* idi ve
**aynen tekrarlanmıştır**. TUR 2'nin sorduğu bant 500–1.000 TL'dir ve o bantta
2 SKU vardır. Aradaki fark **bant tanımıdır, bulgu değişikliği değildir.**

---

### B-2: Bant assortmanda DOLU, stokta BOŞ — 62 ithal listeleme

```yaml
claim:          500-1.000 TL bandinda 62 ithal listeleme katalogda TANIMLI ama hicbiri stokta degil
value:          "stokta olmayan ithal n=349; <300 TL: 18, 300-500: 26, 500-1000: 62, 1000-2000: 108, 2000+: 135"
unit:           adet
status:         UNKNOWN
tier:           T4
evidence_id:    EV-2026-08-10-552
effective_date: 2026-08-10
katman:         — (RAF FIYATI DEGILDIR)
conflict_id:    C-561
```

**Gerekçe:** Bandda görünen markalar tam da fiyat/performans ithal setidir:
Imperial Vin 512 · Itynera 528 · Moncigale 548 · Tallero 600 · Marques de Casa
Concha 664 · Santa Helena 677 · M. Chapoutier Belleruche 680 · Babich 697 ·
Hans Baer 702 · Henkell 746 · Terra Mater Reserve 770 · Botter Caleo 838 ·
Luccarelli Primitivo 864 · Barone Montalto 950 · Zonin Chianti 960 ·
La Vieille Ferme 979.

**Ne yaptım, ne yapmadım:**
- **Yapmadım:** Bu fiyatları raf fiyatı saymadım, `pazar.yaml`'ı değiştirmedim,
  `C-501`'i kapatmadım/daraltmadım.
- **Yaptım:** `C-561` açtım, `T-561` ile başkana taşıdım, 62 satırı CSV'ye
  `ONLINE_LISTING_STOKTA_YOK` / `status=UNKNOWN` etiketiyle ekledim.

---

### B-3: Sourcing kısa listesinin 25/26'sı Türkiye'de BULUNAMADI — tek istisna Cantina Danese

```yaml
claim:          TUR 1 havuzu (11) + shortlist-v2 (15 yeni) = 26 tedarikci ve 30+ marka tarandi; TEK eslesme Cantina Danese s.r.l. (SUP-452)
value:          "1 / 26 eslesme; T-464'un 7 Model A markasi: 0 / 7"
unit:           adet eslesme
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-553, EV-2026-08-10-564, EV-2026-08-10-561
effective_date: 2026-08-10
katman:         —
```

**Gerekçe:** 24 + 30 arama terimi tarandı. Ayrıntı:
`60-pazar/marka-turkiye-varlik-kontrolu.md` §1 ve §1B.

**Tek eşleşme neden önemli:** `SUP-452` Cantina Danese, `top-10-rfq-targets.md`'nin
**2. hedefi** ve **Model B** olarak sınıflanmış. Türkiye'de **kendi markasıyla**
listeli (*Danese Primitivo Puglia "Black Label"*, 1.419 TL listeleme, **stokta değil**,
ithalatçı kodu `Midas`). Bu, private label modelinin "tedarikçinin Türkiye'de markası
yok → çakışma yok" varsayımını **bu tedarikçide yanlışlar**. Fiyat önemli değildir
(stok dışı listeleme); **varlık** önemlidir → `T-565`.

**Kritik okuma kuralı:** "Bu katalogda yok" ≠ "Türkiye'de yok". Metro, zincir market,
tekel bayii ve HoReCa görülmedi. Sonuç **`BULUNAMADI` (presence UNKNOWN)**'dır.

Ayrıca private label üreticileri için bu sonuç genelde **beklenendir** ve bilgi
değeri düşüktür — doğru soru "Türkiye'ye daha önce ihracat yaptı mı?"dır (`T-562`).
**Ama Cantina Danese bunun karşı örneğidir:** private label üreticisi olmasına rağmen
kendi markasıyla görüldü. Yani "private label üreticisi → görünmez" kabulü
**evrensel değildir**.

---

### B-4: İthalatçı haritası açıldı — 4 isimli grup doğrulandı

```yaml
claim:          Turkiye ithal sarap dagitiminda 4 ithalatci grubu ismen dogrulandi; TUR 1'de bu sayi 1'di
value:          "Kavaklidere Saraplari A.S. (26 marka) | Karagozoglu Dis Ticaret A.S. (20) | Adco Gida/Kemer Gida (22) | Baron Sarapcilik (44, ESTIMATE)"
unit:           adet
status:         FACT (Kavaklidere, Karagozoglu) / FACT-kimlik + ESTIMATE-portfoy (Adco) / ESTIMATE (Baron)
tier:           T4
evidence_id:    EV-2026-08-10-554, EV-2026-08-10-555, EV-2026-08-10-556, EV-2026-08-10-557, EV-2026-08-10-562
effective_date: 2026-08-10
katman:         —
```

**Gerekçe (yöntem ve doğrulaması):** Perakendeci feed'inde her ithal ürün bir iç
etiket taşır. Bu etiketlerin ithalatçı grubu olduğu hipotezi **iki bağımsız
kaynakla test edildi**:

1. `KVKLDR` etiketli 26 üreticinin **23'ü** Kavaklıdere'nin kendi *İthal Ürünler*
   sayfasında birebir yer alıyor (`EV-2026-08-10-554`).
2. `KDT` etiketli Marchesi Antinori'nin Türkiye distribütörü, **Antinori'nin kendi
   dağıtım sayfasında** "KARAGOZOGLU DIS TICARET AS, Kemerburgaz — İstanbul"
   (`EV-2026-08-10-555`).

İkisi de hipotezi doğruladı. **Yine de ESTIMATE'tir:** 13/17 kodun açılımı `UNKNOWN`
(`OQ-551`) ve bir etiket, o firmanın Türkiye'deki **tek** ithalatçı olduğunu
kanıtlamaz.

---

### B-5: Hedef bandımızda rakip ile dağıtıcı AYNI ŞİRKET olabilir

```yaml
claim:          Kavaklidere hem buyuk yerli uretici hem giris-segment ithal distributorudur
value:          "Gato Negro, Santa Helena, Baron de Lestac, Moncigale, Torres, Montes, Kaiken, Castellani, Serena 1881 ..."
unit:           —
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-554
effective_date: 2026-08-10
katman:         —
```

**Gerekçe:** Kavaklıdere'nin kendi resmî *İthal Ürünler* sayfası, 9 ülkeden ~30
markayı ülke ülke ilan ediyor. TUR 1'in "benchmark bandında asıl rakip **yerli**
şaraptır" bulgusu bununla birleşince şu hâle geliyor: **aynı satış ve dağıtım gücü
hem yerli hem ithal ürünü taşıyor.** Bu bir **marj sonucu değildir** — mekanik bir
gözlemdir; ekonomisi `kanal-marj-uzmani`'nın alanı (`T-563`).

---

### B-6: Kısa listenin menşe profili Türkiye kanalının menşe profiliyle örtüşmüyor

```yaml
claim:          Kanalda ABD ve Avustralya koleksiyonu HIC YOK; Portekiz 5/0, Guney Afrika 2/0; Fransa 150/33, Italya 176/30
value:          "listeleme/stokta: Fransa 150/33, Italya 176/30, Ispanya 21/6, Almanya 13/2, Avusturya 8/4, Arjantin 12/2, Sili 20/2, Ingiltere 2/1, GAfrika 2/0, Gurcistan 6/0, Portekiz 5/0, YZelanda 3/0, Moldova 10/0, Yunanistan 2/0"
unit:           adet
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-563
effective_date: 2026-08-10
katman:         —
```

**Gerekçe:** TUR 1'in B-8 bulgusu ikinci tarihte doğrulandı. **Yeni bilgi:**
Portekiz koleksiyonundaki 5 kaydın 4'ü portodur; Casa Santos Lima tipi sofra
şarabının bu kanalda **emsali yoktur**. Moldova ise 380–512 TL bandında 10 listeleme
ile fiyat/performans bandında ithalat yapılabildiğini gösteriyor (hepsi stok dışı).

---

### B-7: 8 alternatif kanal denendi, hepsi kapalı — tek kanal zaafı DÜZELMEDİ

```yaml
claim:          iyisarap disinda denenen 8 kanaldan 2026 tarihli dogrulanabilir ithal sarap fiyati ALINAMADI
value:          "A101 403 | CarrefourSA 403 | Macrocenter 403 | SOK 0 sonuc | WineGarage tanitim sitesi | Mahzen26 fiyat yok | WineAnatolia kapali | marketkarsilastir alkolde guncel takip yok"
unit:           adet kanal
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-559, EV-2026-08-10-558
effective_date: 2026-08-10
katman:         —
```

**Gerekçe:** Ayrıca 12 alan adı DNS/e-ticaret düzeyinde elendi. TUR 1'in
"raf fiyatı verisi masabaşından toplanamaz" yapısal tespiti **TUR 2'de de geçerli**.
Bu bir arama başarısızlığı değil, **pazarın yapısıdır** — ama sonucu şudur:
**tek kanal yoğunlaşması TUR 2'de de kırılamadı.**

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | 500–1.000 TL bandı **boş mu, stoksuz mu** | Tek kanalda 62 listeleme var, 0'ı stokta | **HIGH** | Fiziksel mağaza turu; aranacak SKU listesi hazır (`OQ-552`) |
| 2 | 13/17 **ithalatçı kodunun** kimliği | Kodlar perakendeci tarafından ilan edilmiyor | MEDIUM | Üretici "distributors" sayfaları / şişe arka etiketi (`OQ-551`) |
| 3 | Kısa listedeki üreticilerin **Türkiye'ye ihracat geçmişi** | Ticari veri sağlayıcıları 403 (volza, exportgenius) | MEDIUM | RFQ sorusu (`T-562`, `OQ-553`) |
| 4 | Kısa liste markalarının **Metro / zincir / tekel rafında** olup olmadığı | Bu kanallar erişilemedi | **HIGH** | Fiziksel gözlem (`OQ-502` ile aynı ziyaret) |
| 5 | **Resmî ithalatçı listesi** ve toplam ithalatçı sayısı | TADAB listesi alınamadı | MEDIUM | `T-564` / `T-505` |
| 6 | **İthalat hacmi / menşe kırılımı** | TUR 2'de yeniden denenmedi (kapsam dışı) | HIGH | `T-505` |
| 7 | `Gold Country` markasının **üretici/sahibi** | Hiçbir kaynakta yok | LOW | Şişe arka etiketi (`OQ-503`) |
| 8 | J.P. Chenet'yi Baron mu, Interay Trading mi getiriyor | İki zayıf kaynak, ikisi de T5 | LOW | `OQ-551` |
| 9 | **HoReCa fiyat çarpanı** | TUR 2 kapsamı dışında bırakıldı | HIGH | Restoran şarap listesi örneklemi |
| 10 | Benchmark **promosyon durumu** | **Kasten ele alınmadı** (TUR 2 kesin sınırı) | **CRITICAL** | `T-504` — fiziksel gözlem |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-561** | `EV-2026-08-10-501` (T4 / 2026-08-09): stokta olmayan listelemeler "70–450 TL gibi gerçeklik dışı" → havuz **bütünüyle** dışlanır (`C-501`) | `EV-2026-08-10-552` (T4 / 2026-08-10): havuz **iki modlu** — 44 kayıt <500 TL (gerçeklik dışı), **62 kayıt 500–1.000 TL** (makul), 243 kayıt >1.000 TL | `C-501`'in gerekçesi düşük uçtan, sonucu tüm havuza uygulanıyor; düşük uç havuzun yalnızca %12,6'sı | **OPEN** → `T-561` |

Ayrıntı: `99-ops/_parts/celiskiler-turkiye-pazar-kasifi-tur2.md`
*(`C-501`, `C-502`, `C-551` bu turda ele alınmadı; `C-551` kapsam sınırı gereği
kasten ele alınmadı.)*

---

## 5. MODEL GİRDİLERİ

**Bu tur `pazar.yaml`'a DOKUNMAMIŞTIR** (talimat gereği). Aşağıdaki tablo
**önerilerdir**; merge kararı `yatirim-komitesi-baskani`'na aittir.

| YAML dosyası | Alan | Mevcut | Önerilen | status | evidence_id |
|---|---|---|---|---|---|
| `pazar.yaml` | `segment.ithal_min_stokta_uzman_kanal_try` | 875.00 | **875.00 (değişmedi — ikinci tarihte doğrulandı)** | FACT | `EV-2026-08-10-551` |
| `pazar.yaml` | `segment.ithal_sku_400_800_uzman_kanal` | 0 | **0 (değişmedi — ikinci tarihte doğrulandı)** | FACT ⚠`C-561` | `EV-2026-08-10-551` |
| `pazar.yaml` | `segment.ithal_sku_500_1000_stokta` | *(yok)* | **2** (875 / 948; ikisi de eski gözlem) | FACT | `EV-2026-08-10-551` |
| `pazar.yaml` | `segment.ithal_listeleme_500_1000_stok_disi` | *(yok)* | **62** — **RAF FİYATI DEĞİL, MODELE GİREMEZ** | UNKNOWN | `EV-2026-08-10-552` |
| `pazar.yaml` | `ithalatci_haritasi.dogrulanmis_ithalatci_sayisi` | 1 | **4** (Kavaklıdere, Karagözoğlu, Adco, +Baron ESTIMATE) | FACT | `EV-...-554/555/556` |
| `pazar.yaml` | `ithalatci_haritasi.konsolidasyon_derecesi` | null | **null (DEĞİŞMEMELİ)** — tek kanaldan pay çıkarılamaz | UNKNOWN | — |
| `pazar.yaml` | `ithalatci_haritasi.sourcing_shortlist_mevcut_ithalatci` | *(yok)* | **1 / 26** (yalnızca Cantina Danese) | FACT | `EV-2026-08-10-553`, `EV-2026-08-10-564` |
| `pazar.yaml` | `kanal_yapisi.bim_a101_sok_sarap_var_mi` | null | **null (DEĞİŞMEMELİ)** — ŞOK online 0 sonucu mağaza rafını kanıtlamaz | UNKNOWN | `EV-2026-08-10-558` |
| `pazar.yaml` | `gozlem_havuzu.toplam_gozlem` | 52 | **117** — ama **63'ü raf fiyatı değildir**; model girdisi sayısı **artmamıştır** | FACT | `EV-2026-08-10-552`, `EV-2026-08-10-564` |
| `pazar.yaml` | `gozlem_havuzu.tek_kanal_yogunlasmasi_uyarisi` | 45/52 | **UYARI GÜÇLENDİ** — 8 alternatif kanal denendi, hepsi kapalı | FACT | `EV-2026-08-10-559` |

**evidence_id'si olmayan satır modele giremez.**
Kara listeye eklenmesi önerilenler: `EV-2026-08-10-552` (stok dışı listeleme fiyatları),
`EV-2026-08-10-560` (2022–2023 arşiv fiyatı, `ttl: 0d`).

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `kanal-marj-uzmani` | Kavaklıdere hem yerli üretici hem giriş-segment ithal distribütörü (`EV-554`) | Rakip ile dağıtıcı aynı şirket olabilir |
| `kanal-marj-uzmani` | ~200 ithal markanın %56'sı 4 grupta (`EV-557`) | Dağıtım konsolidasyon sinyali — payı ölçmedim |
| `kanal-marj-uzmani` | Bandımızda ithalat yapan küçük oyuncular var (Moldova 380–512 TL) ama ürünleri stok dışı | "Listeleniyor ama dönmüyor" hipotezi |
| `global-sourcing-kasifi` | 11/11 tedarikçinin TR ithalatçısı yok → temiz sayfa **ama** pazar validasyonu da yok (`EV-553`) | Distribütörlük müzakeresi açısından çift yönlü |
| `global-sourcing-kasifi` | Kısa listenin menşe profili kanalın menşe profiliyle örtüşmüyor (`EV-563`) | ABD/AU/PT/ZA kanalda sıfıra yakın |
| `global-sourcing-kasifi` | `exported_to_turkey_before` UNKNOWN → RFQ'da zorunlu sorulmalı | `T-562` |
| `global-sourcing-kasifi` | **RFQ hedefi #2 Cantina Danese Türkiye'de kendi markasıyla listeli ve bir ithalatçıya bağlı** | `T-565` — private label müzakeresinde münhasırlık/kanal çakışması riski |
| `mevzuat-ruhsat-uzmani` | Artık 4 ithalatçının **adı** var → TADAB listesinde aranabilir | `T-564` |
| `gumruk-vergi-uzmani` | Fiyat/performans bandında **Moldova** menşeli ithal listeleniyor (`EV-563`) | Tercihli tarife ihtimali — sadece ipucu |
| `yatirim-komitesi-baskani` | CSV'ye eklenen 62 satır **raf fiyatı değildir**; merge'de ayrım korunmalı | Yanlış okuma riski |

Tam liste: `99-ops/_parts/capraz-ipuclari-turkiye-pazar-kasifi-tur2.md`

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| `T-561` | `yatirim-komitesi-baskani` | `C-501` daraltılmalı mı? Stok dışı havuz iki modlu | MEDIUM | **OPEN** (yeni) |
| `T-562` | `global-sourcing-kasifi` | 11/11 tedarikçi TR'de bulunamadı; RFQ'da "TR'ye ihracat geçmişi" zorunlu sorulmalı | MEDIUM | **OPEN** (yeni) |
| `T-563` | `kanal-marj-uzmani` | 4 ithalatçı ismen tespit edildi; biri aynı zamanda yerli üretici | **HIGH** | **OPEN** (yeni) |
| `T-564` | `mevzuat-ruhsat-uzmani` | İsimler artık biliniyor → TADAB belge sahipleri listesi | MEDIUM | **OPEN** (yeni) |
| `T-565` | `global-sourcing-kasifi` | RFQ hedefi #2 Cantina Danese'nin TR'de zaten ithalatçısı var → RFQ'ya 4. soru | MEDIUM | **OPEN** (yeni) |
| `T-464` | `turkiye-pazar-kasifi` *(bana açıldı)* | 7 Model A markasının TR ithalatçısı var mı | HIGH | **ANSWERED** ✅ |
| `T-504` | `yatirim-komitesi-baskani` | OQ-001 promosyon ayağı | **CRITICAL** | **OPEN** — bu turda **kasten dokunulmadı** |
| `T-551` | `yatirim-komitesi-baskani` | `C-551` Metro şarap katalogu çiftli KDV | HIGH | **OPEN** — bu turda dokunulmadı |
| `T-501`…`T-506` | çeşitli | TUR 1'den devrediyor | — | **OPEN** |

**Bu turda kapanan ticket yoktur; `T-464` cevaplandı (`ANSWERED`) ve başkan onayı bekliyor.**

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-10-551` | 30d | 2026-09-09 |
| `EV-2026-08-10-552` | 30d | 2026-09-09 |
| `EV-2026-08-10-553` | 30d | 2026-09-09 |
| `EV-2026-08-10-554` | 180d | 2027-02-06 |
| `EV-2026-08-10-555` | 180d | 2027-02-06 |
| `EV-2026-08-10-556` | 180d | 2027-02-06 |
| `EV-2026-08-10-557` | 90d | 2026-11-08 |
| `EV-2026-08-10-558` | 90d | 2026-11-08 |
| `EV-2026-08-10-559` | 30d | 2026-09-09 |
| `EV-2026-08-10-560` | **0d** | **ZATEN STALE** — 2022–2023 verisi, modele giremez |
| `EV-2026-08-10-561` | 180d | 2027-02-06 |
| `EV-2026-08-10-562` | 180d | 2027-02-06 |
| `EV-2026-08-10-563` | 30d | 2026-09-09 |
| `EV-2026-08-10-564` | 30d | 2026-09-09 |

**Uyarı:** Fiyat/stok gözlemlerinin tamamı **2026-09-09**'da STALE olur. İthalatçı
haritası kartları (554–557, 561–562) daha uzun ömürlüdür — dağıtım anlaşmaları
raf fiyatından yavaş değişir.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Bir Metro / Migros / tekel bayii rafında, 500–1.000 TL arasında fiyat etiketiyle
duran ve bu raporda "stok dışı" diye kaydettiğim ithal şaraplardan birinin fotoğrafı.**

Örneğin Santa Helena (677), Botter Caleo (838) veya La Vieille Ferme (979) fiziksel
bir rafta bulunursa, bu raporun merkez cümlesi — *"hedef bantta ithal ürün var ama
dönmüyor"* — çöker ve yerine çok daha iyi bir cümle gelir: *"hedef bantta ithal ürün
normal olarak satılıyor, sadece incelediğim online kanal onu taşımıyor."* Bu, projenin
lehine bir düzeltmedir ve **tek bir mağaza ziyaretiyle** test edilebilir (`OQ-552`).

İkinci çürütücü: **`supplier-shortlist-v2.csv`'de, Türkiye'de hâlihazırda satılan bir
markanın çıkması.** Kontrolü TUR 1 havuzuyla yaptım çünkü v2 dosyası yoktu; v2 yeni
isimler getirirse §1'deki "0/11" sonucu **kısmen geçersizdir** ve kontrol
tekrarlanmalıdır.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"Perakendeci feed'indeki iç etiketler ithalatçı gruplarıdır."**

Bu, turun en değerli bulgusunun (ithalatçı haritası) tek dayanağıdır. İki bağımsız
testten geçti (Kavaklıdere 23/26 örtüşme, Antinori→Karagözoğlu birebir isim) —
ama testler **2 kod üzerindedir, 17 kodun 15'i test edilmemiştir**. Etiketler
pekâlâ "tedarikçi" değil "satın alma grubu", "raf planogram grubu" veya
"komisyon oranı grubu" olabilir. Yanılıyorsam B-4 ve B-5 tamamen çöker.

İkinci kırılgan varsayım (TUR 1'den devrediyor, **düzelmedi**): **tek kanalın
Türkiye pazarını temsil ettiği.** TUR 2'de bunu kırmak için 8 kanal denedim ve
**başarısız oldum**. Yani bu turda kanıt tabanı **genişlemedi, yalnızca derinleşti** —
aynı kaynağın daha çok alanını okudum. Bu, istatistiksel olarak **daha az** bir
iyileşmedir; öyle okunmalıdır.

Üçüncüsü: **`available` alanının stok gerçeğini yansıttığı.** 62 kaydın "stok dışı"
olması bu alana dayanıyor. Alan bakımsızsa (ki `C-501` tam da bunu iddia ediyor)
hem TUR 1'in hem TUR 2'nin segment resmi yanlıştır.

### 9.3 Hangi kaynağıma en az güveniyorum?

1. **`EV-2026-08-10-562`** (Baron Şarapçılık = J.P. Chenet ithalatçısı). T5 blog +
   tumblr. Üstelik `interaytrading.com` da aynı markayı sitesinde gösteriyor.
   `ESTIMATE` diye etiketledim; öyle okunmalı ve modele girmemeli.
2. **`EV-2026-08-10-552`'deki fiyatlar.** Kartın kendisi (62 listelemenin varlığı)
   sağlam, ama **fiyatları** doğrulanmamıştır ve `C-501` altındadır. CSV'ye eklerken
   `status=UNKNOWN` verdim; bu satırların ortalaması alınırsa **veri suistimali** olur.
3. **`EV-2026-08-10-557`'deki 13 çözülmemiş kod.** Bunlar "harita" gibi görünüyor
   ama aslında **kodlanmış cehalettir**. Bandımıza en yakın markaları taşıyan kodlar
   (`PiyasaGıda`, `piramitgıda`, `Vinist`, `frosta`) tam da çözülemeyenler.
4. **`EV-2026-08-10-560`** (Metro J.P. Chenet 2022–2023). `ttl: 0d` verdim ve modele
   girmesini yasakladım. 2023'ten 2026'ya ekstrapolasyon yapılmadı; yapılmamalı.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

- **"Bantta ithal ürün var ama dönmüyor" yanlışsa** (aslında normal satılıyorsa):
  hedef bant sağlamdır, sadece gözlem aracım yanlıştı → **TEST / IMPORT PILOT lehine.**
- **Doğruysa:** hedef bantta ithal ürün listeleniyor ama satılmıyor demektir →
  talep sorunu → **KILL yönünde güçlü sinyal.** Bu, bu turun en ağır bulgusudur.
- **İthalatçı haritası yanlışsa:** `kanal-marj-uzmani`'nın müzakere varsayımları
  yanlış kurulur; ama model **sayısal olarak** etkilenmez (bu turda hiç sayı
  üretmedim). Hasar sınırlıdır.
- **"11/11 tedarikçinin TR ithalatçısı yok" yanlışsa** (biri varsa): o tedarikçi
  için distribütörlük **imkânsız veya çok farklı bir müzakere** olur → sourcing
  kısa listesi daralır → **hedef daralır, KILL yönünde.**
- **Kavaklıdere bulgusu doğruysa (ki en sağlam bulgum):** hedef bantta hem yerli
  hem ithal rakip **aynı dağıtım gücünü** kullanıyor. Bu, yeni bir markanın
  listelenme maliyetini yükseltir → **KILL yönünde**, ama büyüklüğü
  `kanal-marj-uzmani`'nın işidir.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre | Maliyet |
|---|---|---|---|---|---|
| 1 | **Hazır SKU listesiyle** mağaza turu: Santa Helena · Belleruche · Hans Baer PN · Henkell · Terra Mater Reserve · Botter Caleo · Luccarelli Primitivo · Barone Montalto · La Vieille Ferme · Alpaca · Imperial Vin — rafta var mı, fiyatı ne? | İnsan gözlemci | Metro + 1 zincir market + 1 tekel bayii, İstanbul, 1 gün | 1 gün | ulaşım |
| 2 | Aynı ziyarette **şişe arka etiketi** fotoğrafı (ithalatçı satırı) — 13 kodun bir kısmını çözer | Aynı kişi | 10 şişe, 10 dk | — | ~0 |
| 3 | `OQ-001` / `T-504` (benchmark etiketi + ikinci gözlem) — **aynı ziyarette** | Aynı kişi | Metro şarap reyonu | — | ~600 TL |
| 4 | Kısa liste üreticilerine "Türkiye'ye ihracat geçmişi" sorusu | `global-sourcing-kasifi` | RFQ maddesi | RFQ süresi | ~0 |
| 5 | TADAB ithalatçı listesi + TÜİK GTİP 2204 | `mevzuat-ruhsat-uzmani` | `T-564` / `T-505` | 1–15 gün | ~0 |
| 6 | `C-561` kararı (C-501 daraltılsın mı) | `yatirim-komitesi-baskani` | `T-561` | — | ~0 |

**Not:** 1, 2 ve 3 **tek ziyarette** yapılır. TUR 1.5'te "OQ-001'in önündeki engel
pahalı değil, fiziksel" demiştim. TUR 2 bu ziyaretin **kapsamını genişletti**:
aynı gezi artık `T-504`, `OQ-502`, `OQ-552` ve `OQ-551`'in bir kısmını **birlikte**
kapatabilir. Maliyet aynı kaldı, getirisi arttı.
