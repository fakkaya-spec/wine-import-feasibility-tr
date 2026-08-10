# AJAN RAPORU — TÜRKİYE PAZAR KÂŞİFİ

```yaml
ajan:               turkiye-pazar-kasifi
tur:                TUR 2.5 (TARGET SEGMENT DEGERLENDIRMESI — SINIRLI GOREV)
tarih:              2026-08-10
durum:              SUBMITTED
kapsam:             "TEK gorev: 599/699/799/899/999 TL hedef tuketici raf fiyati
                     merdiveninin siniflandirilmasi + PRIMARY/SECONDARY/STRETCH
                     onerisi. YENI PAZAR HARITASI CIKARILMAMISTIR.
                     Gold Country promosyon arastirmasina DONULMEDI (T-504
                     bilincli acik). 7584 / reklam ARASTIRILMADI.
                     Vergi / navlun / ruhsat / tedarikci fiyati / kanal marji
                     konusunda SONUC URETILMEMISTIR."
ana_cikti:          60-pazar/target-shelf-price-analysis.md
```

---

## 1. YÖNETİCİ ÖZETİ

Beş hedef fiyatın beşi de sınıflandırıldı; hiçbiri `INSUFFICIENT_EVIDENCE`
olmadı, ama **ikisi düşük güvenle** sınıflandırıldı:
**599 `AGGRESSIVE` (LOW)** · **699 `ATTRACTIVE` (MEDIUM)** ·
**799 `ATTRACTIVE` (MEDIUM)** · **899 `PREMIUM_EDGE` (MEDIUM)** ·
**999 `TOO_HIGH` (LOW)**. Öneri: **PRIMARY 799 · SECONDARY 699 · STRETCH 899**,
`599` ise stretch değil **downside/floor senaryosu**dur.

Sınıflandırma **talep üzerinden değil**, mevcut kanıtlardan yeniden hesaplanan
**rekabet yoğunluğu eğrisi** üzerinden yapıldı (`EV-2026-08-10-702`). TUR 2
snapshot'ı **100 TL çözünürlükte yeniden binlendi** — yeni veri toplanmadı.
Sonuç: hedef bölgede (600–1.000 TL) **65 yerli / 2 ithal** stokta SKU vardır;
stokta ithal taban **875 TL**'dir; whitespace **650–875 TL** aralığındadır.

**Bu turun en rahatsız edici bulgusu kendi aleyhimedir:** gözlenen kanalın
**tüm stokta katalogunda (471 SKU) 600 TL altında yalnızca 1 SKU vardır** ve
stokta yerli **medyan 1.410 TL**'dir. Yani "500–1.000 TL'de ithal şarap yok"
bulgusu **kısmen bir kanal artefaktıdır** — bu kanal o bantta **yerli** şarap
da taşımamaktadır. Tüm sınıflandırma bu kanalın **alt kuyruğundan** okunmuştur.

**Önerinin kanıt seviyesi düşüktür ve bu açıkça yazılmıştır:** 2 bağımsız
kanal (biri **n=2** SKU), 471 SKU'nun tamamı **tek kanaldan**, hedefin asıl
karşılığı olan `L8_CHAIN_RETAIL` katmanında **SIFIR gözlem**. Tek kanal zaafını
kırmak için 17 ek alan adı denendi, **0** kullanılabilir kanal bulundu
(`EV-2026-08-10-701`) — üçüncü başarısız deneme.

**3 kanıt kartı** (`EV-2026-08-10-701`…`-703`), **2 ticket** (`T-701`, `T-702`),
**3 açık soru** (`OQ-701`…`OQ-703`). **Yeni çelişki açılmadı.**
`80-model/inputs/*.yaml`'a ve `raf-fiyat-gozlemleri.csv`'ye **dokunulmadı**
(yeni raf gözlemi toplanmadığı için CSV'ye eklenecek satır yoktur).

---

## 2. BULGULAR

### B-1: Hedef merdivenin rekabet yoğunluğu eğrisi çıkarıldı — whitespace 650–875 TL

```yaml
claim:          Gozlenen kanalda hedef bolgede (600-1.000 TL) 65 stokta yerli / 2 stokta ithal SKU vardir; stokta ithal taban 875 TL'dir
value:          "+-%10 pencerede stokta yerli/ithal -> 599: 3/0 | 699: 17/0 | 799: 31/1 | 899: 35/2 | 999: 49/1"
unit:           adet
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-702
effective_date: 2026-08-10
katman:         L8_ONLINE_UZMAN_PERAKENDE
```

**Gerekçe:** TUR 2'de alınan snapshot (1.304 kayıt) 100 TL çözünürlükte yeniden
binlendi. **Yeni veri toplanmadı**; `EV-2026-08-10-551`/`-552` **supersede
edilmedi**, yalnızca ayrıştırıldı. Stokta yerli n=391 (min 460, medyan 1.410,
max 7.600), stokta ithal n=80 (min 875).

**Anlamı:** Yoğunluk eğrisi 600 TL'den itibaren yükselir ve 800–1.000 TL'de
platoya yaklaşır; stokta ithal rekabet ise ancak **875 TL**'den başlar.
Aradaki **650–875 TL** aralığı, gözlenen kanalda **stokta ithal rakibin
bulunmadığı ama gerçek yerli yoğunluğun olduğu** tek bölgedir.

---

### B-2: Gözlenen kanal giriş segmentini taşımıyor — "boşluk" bulgusu kısmen artefakt

```yaml
claim:          Kanalin tum stokta katalogunda (471 SKU) 600 TL altinda YALNIZCA 1 SKU vardir; stokta yerli medyan 1.410 TL'dir
value:          "1 / 471 SKU (Mistia Gafa Beyaz Blend 460 TL); 500-600 TL bandinda 0 SKU (yerli dahil)"
unit:           adet / TRY
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-702
effective_date: 2026-08-10
katman:         L8_ONLINE_UZMAN_PERAKENDE
```

**Gerekçe:** Aynı yeniden binleme. Kanalın ağırlık merkezi hedef merdivenin
**1,4–2,4 katı üstündedir**.

**Neden bu bulgu bu turun en önemlisi:** TUR 1 ve TUR 2 boyunca taşınan
*"500–1.000 TL bandında stokta ithal şarap yok"* cümlesi, kanalın **hiçbir
şarabı** o bandın altında taşımadığı gerçeği eklenmeden **fazla iddialıdır**.
`C-501` ve `C-561`'i **çözmez** ama **yeniden çerçeveler** → `OQ-702`.

**Ne yapmadım:** `pazar.yaml`'daki `segment.*` alanlarını **değiştirmedim**,
`C-501`/`C-561`'i **kapatmadım/daraltmadım**, `ithal_sku_400_800_uzman_kanal = 0`
değerine **dokunmadım**.

---

### B-3: Beş hedef fiyatın sınıflandırması

```yaml
claim:          599 AGGRESSIVE (LOW) | 699 ATTRACTIVE (MEDIUM) | 799 ATTRACTIVE (MEDIUM) | 899 PREMIUM_EDGE (MEDIUM) | 999 TOO_HIGH (LOW)
value:          "siniflandirma ekseni = REKABET YOGUNLUGU + REKABET KONUMU; TALEP DEGIL"
unit:           -
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-702, EV-2026-08-10-501, EV-2026-08-10-502, EV-2026-08-10-551, EV-2026-08-09-501, EV-2026-08-09-502
effective_date: 2026-08-10
katman:         TARGET_SHELF_PRICE (L8 niyeti — hangi L8 alt katmani UNKNOWN)
```

**Türetme zinciri:** Ayrıntı `60-pazar/target-shelf-price-analysis.md` §3.
Özet:
- **599** — gözlenen her kanalın rekabet dağılımının **altında**; `TOO_LOW`
  olmamasının tek nedeni Metro'da 599,90 TL etiketli **ithal** bir şarabın
  fiilen görülmüş olmasıdır (`EV-2026-08-09-501`, n=1, promo `UNKNOWN`).
- **699 / 799** — gerçek gözlenmiş yoğunluk **var**, stokta ithal rakip **yok**
  → whitespace. 799'da yoğunluk 699'un **1,8 katı**.
- **899** — stokta ithal taban (875) ve `segment.fiyat_performans_ust_try = 900`
  (ESTIMATE) tavanına **değer**; whitespace biter.
- **999** — projenin kendi fiyat/performans mandasının **dışına** çıkar;
  `OBSERVED_BENCHMARK`'ların %54–67 üstündedir.

**Kritik uyarı:** `ATTRACTIVE` bu belgede **"bu fiyattan satar" demek
değildir**. Talep verisi **yoktur** ve tahmin **edilmemiştir**.

---

### B-4: Tek kanal zaafı üçüncü kez kırılamadı

```yaml
claim:          TUR 2.5'te 17 ek Turk sarap perakendecisi alan adi denendi; 0 kullanilabilir ikinci fiyat kanali bulundu
value:          "17 alan adi; 15 DNS/baglanti hatasi, 1 x 404, 1 x 200 (park edilmis lander sayfasi)"
unit:           adet kanal
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-701
effective_date: 2026-08-10
katman:         -
```

**Gerekçe:** TUR 1 ve TUR 2'de zaten 8 kanal denenmişti (`EV-2026-08-10-558`,
`-559`). Toplam **25 alan adı**, **2 kullanılabilir kanal**.

**Anlamı:** Bu turun kanıt tabanı TUR 2'ye göre **genişlememiştir**; yalnızca
mevcut veri **daha ince analiz edilmiştir**. Bu, istatistiksel olarak
**daha zayıf** bir iyileşmedir ve öyle okunmalıdır.

---

### B-5: Hedef merdivenin asıl katmanı (`L8_CHAIN_RETAIL`) hiç gözlenmemiştir

```yaml
claim:          Hedef merdiven bir TUKETICI raf fiyatidir; ancak L8_CHAIN_RETAIL katmaninda projenin SIFIR gozlemi vardir
value:          0
unit:           adet gozlem
status:         UNKNOWN
tier:           -
evidence_id:    EV-2026-08-09-511
effective_date: 2026-08-10
katman:         L8_CHAIN_RETAIL
```

**Gerekçe:** `pazar.yaml → l8_chain_retail.deger_try: null / UNKNOWN`.
Türkiye'de alkol tüketiciye internetten satılamadığı için zincir marketlerin
online kanalında şarap fiyatı **yoktur**.

**Anlamı:** Merdivenin **göreli** sıralaması yapılabilmiştir; **mutlak** konumu
doğrulanamamıştır. Bu, `OQ-001`'in **hedef tarafındaki aynasıdır** ve bugüne
kadar adlandırılmamıştır → `T-701`.

---

### B-6: Zincir perakendeye dair tek sinyal T5'tir ve gözlenen kanalın TERSİNİ söyler

```yaml
claim:          T5 icerik ciftlikleri zincir market/tekelde 75 cl sarabin 450-650 TL oldugunu iddia ediyor
value:          "450-650 TL (DOGRULANMAMIS)"
unit:           TRY
status:         UNKNOWN
tier:           T5
evidence_id:    EV-2026-08-10-703
effective_date: UNKNOWN
katman:         L8_CHAIN_RETAIL (iddia)
conflict_id:    C-503
```

**Gerekçe:** `EV-2026-08-09-512` ile **aynı kaynak sınıfıdır** ve `C-503` ile
başkan tarafından zaten "modele giremez" kararı verilmiştir. Kart yalnızca
sınıfın **yeniden karşımıza çıktığını ve yeniden reddedildiğini** belgeler.

**Neden yine de kayda değer:** Yönü, gözlenen online uzman kanalın (stokta
yerli medyan **1.410 TL**) **tersidir**. Doğru çıkarsa hedef merdivenin
üst basamakları (899 / 999 TL) çok daha zor bir rekabet konumuna düşer.
**Bir kanıt olarak değil, bir çürütücü hipotez olarak** raporlanmıştır
(`OQ-701`).

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | **`L8_CHAIN_RETAIL`** — zincir market tüketici raf fiyatı, 600–1.000 TL bandı | Alkol online satılamıyor; 25 alan adı denendi | **HIGH** | Fiziksel mağaza turu (`OQ-701`, `T-701`, `OQ-502`) |
| 2 | Hedef merdivenin **hangi L8 alt katmanını** kastettiği | Charter'da tanımlı değil | **HIGH** | Başkan kararı (`T-701`) |
| 3 | 599 TL basamağının **promosyonsuz** dayanağı | `T-504` bilinçli olarak açık bırakıldı (kapsam) | **CRITICAL** | `T-504` — fiziksel gözlem (`OQ-703`) |
| 4 | Gözlenen kanalın giriş segmentini **kalıcı olarak mı** taşımadığı | Tek tarihli assortman gözlemi | MEDIUM | Aynı kanalın +30/+60 gün ölçümü (`OQ-702`) |
| 5 | 650–875 TL "whitespace"in **boşluk mu, ölü bölge mi** olduğu | Talep/rotasyon verisi yok | **HIGH** | `C-561` / `T-561` çözümü + fiziksel gözlem |
| 6 | **Tekel bayii** ve **HoReCa** karşılığı | Hiç gözlem alınamadı | HIGH | Fiziksel gözlem / restoran listesi örneklemi |
| 7 | **Talep elastikiyeti** — her basamakta hacim ne olur | Türkiye'de kamuya açık SKU-bazlı satış verisi yok | **HIGH** | Bu ajan **çözemez**; pilot satış verisi gerekir |

**Talep tarafı bilinçli olarak boş bırakılmıştır. UNKNOWN yazmak başarısızlık
değildir; uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

**Bu turda YENİ çelişki açılmamıştır.** Mevcut çelişkilerin hedef merdivene
etkisi:

| conflict_id | Durum | Hedef merdivene etkisi |
|---|---|---|
| `C-501` (available filtresi) | **OPEN** (TUR 1'den) | Yanlışsa **tüm yoğunluk eğrisi** geçersizdir → beş sınıflandırma da düşer |
| `C-551` (Metro şarap KDV sunumu) | **OPEN** (TUR 1.5'ten) | `OBSERVED_BENCHMARK`'ın KDV niteliğini etkiler → 599 basamağının dayanağını kaydırır |
| `C-561` (bant assortmanda dolu / stokta boş) | **OPEN** (TUR 2'den, `T-561`) | "Whitespace" mi "ölü bölge" mi sorusunun ta kendisi → 699/799 `ATTRACTIVE` ↔ 999 `TOO_HIGH` **ters çevrilebilir** |
| `C-503` (T5 Metro fiyat listesi) | **RESOLVED** (modele giremez) | `EV-2026-08-10-703` aynı sınıftadır; **aynı karar uygulanmıştır** |

**Yeni bir gerilim tespit edildi ama çelişki açılmadı** (gerekçe: aynı olguyu
iki kanal iki farklı segmentte gözlemliyor olabilir, bu tanım gereği çelişki
değildir): Metro'da 500–700 TL bandında **ithal şarap vardır** (n=2), online
uzman kanalda **yoktur** (n=0/80). Bu, `C-561`'in kapsamındadır ve
`T-561` üzerinden başkana zaten taşınmıştır.

---

## 5. MODEL GİRDİLERİ

**Bu tur `80-model/inputs/*.yaml`'a DOKUNMAMIŞTIR** (talimat gereği).
Aşağıdakiler **önerilerdir**; merge kararı `yatirim-komitesi-baskani`'na aittir.

| YAML | Alan | Önerilen | status | evidence_id |
|---|---|---|---|---|
| `pazar.yaml` | `target_shelf_price.primary_try` | **799** | **ONERI / ESTIMATE** | `EV-2026-08-10-702` |
| `pazar.yaml` | `target_shelf_price.secondary_try` | **699** | **ONERI / ESTIMATE** | `EV-2026-08-10-702` |
| `pazar.yaml` | `target_shelf_price.stretch_try` | **899** | **ONERI / ESTIMATE** | `EV-2026-08-10-702`, `EV-2026-08-10-551` |
| `pazar.yaml` | `target_shelf_price.floor_downside_try` | **599** *(KOŞULLU — `T-504`)* | **ONERI / ESTIMATE** | `EV-2026-08-09-501` |
| `pazar.yaml` | `target_shelf_price.etiket_kurali` | `TARGET_SHELF_PRICE` ≠ `OBSERVED_BENCHMARK`; **birleştirilemez** | **KURAL** | — |
| `pazar.yaml` | `target_shelf_price.katman_niyeti` | `L8`, alt katman **UNKNOWN** | UNKNOWN | `T-701` |
| `pazar.yaml` | `segment.yogunluk_egrisi_100tl` | `EV-2026-08-10-702` tablosu | FACT (tek kanal) | `EV-2026-08-10-702` |
| `pazar.yaml` | `segment.whitespace_araligi_try` | **650–875** *(tek kanal, ESTIMATE)* | ESTIMATE | `EV-2026-08-10-702`, `-551` |
| `pazar.yaml` | `gozlem_havuzu.denenen_kanal_sayisi` | 25 alan adı / **2** kullanılabilir | FACT | `EV-2026-08-10-701` |
| `pazar.yaml` | `l8_chain_retail.deger_try` | **null (DEĞİŞMEMELİ)** | UNKNOWN | `EV-2026-08-09-511` |
| `pazar.yaml` | `segment.*` (mevcut alanlar) | **DEĞİŞMEMELİ** — bu turda yeni raf gözlemi alınmadı | — | — |

**Kara listeye eklenmesi önerilen:** `EV-2026-08-10-703` (T5, `ttl: 0d`,
`C-503` ile aynı sınıf) — **modele giremez**.

**evidence_id'si olmayan satır modele giremez.**

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `kanal-marj-uzmani` | Her hedef basamağında gözlenen rakip SKU sayısı (3 / 17 / 31 / 35 / 49) | Raf pazarlığı rakip yoğunluğuna duyarlıdır — **marj hesaplanmamıştır** (K4) |
| `kanal-marj-uzmani` | Gözlenen kanal giriş segmentini taşımıyor (471 SKU'da 1 adet <600 TL) | Fiyat/performans için **doğru kanal bu olmayabilir** |
| `finans-fizibilite` | Stokta ithal taban 875 TL; 799 ve altı hedefler bu tabanın **altındadır** | Ters model çıktısında açıkça yazılmalı (`T-702`) |
| `global-sourcing-kasifi` | 600–1.000 TL'de gözlenen rakip **65 yerli / 2 ithal**; ABD ve Avustralya bu kanalda **hiç yok** | İki `OBSERVED_BENCHMARK` tam da kanalın taşımadığı menşelerden |
| `yatirim-komitesi-baskani` | `L8_CHAIN_RETAIL`'de **sıfır gözlem** — `OQ-001`'in hedef tarafındaki aynası | `T-701` |
| `seytanin-avukati` | **Kendi aleyhime:** yoğunluk eğrisinin tamamı tek kanalın **alt kuyruğundan** | Saldırı için en zayıf nokta, hazır cephane §9 |

Tam liste: `99-ops/_parts/capraz-ipuclari-turkiye-pazar-kasifi-tur25.md`

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| `T-701` | `yatirim-komitesi-baskani` | Hedef merdiven hangi L8 alt katmanını kastediyor? `L8_CHAIN_RETAIL`'de sıfır gözlem | **HIGH** | **OPEN** (yeni) |
| `T-702` | `finans-fizibilite` | `TARGET_SHELF_PRICE` ≠ `OBSERVED_BENCHMARK`; hedef modele **band** olarak girmeli | **HIGH** | **OPEN** (yeni) |
| `T-504` | `yatirim-komitesi-baskani` | OQ-001 promosyon ayağı | **CRITICAL** | **OPEN** — bu turda **kasten dokunulmadı** |
| `T-561` | `yatirim-komitesi-baskani` | `C-501` daraltılmalı mı (stok dışı havuz iki modlu) | MEDIUM | **OPEN** — bu turun sonucu bu ticket'a **doğrudan bağlıdır** |
| `T-551` · `T-501`…`T-506` · `T-562`…`T-565` | çeşitli | Önceki turlardan devrediyor | — | **OPEN** |

**Bu turda kapanan ticket yoktur.**

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-10-701` | 30d | 2026-09-09 |
| `EV-2026-08-10-702` | 30d | **2026-09-09** |
| `EV-2026-08-10-703` | **0d** | **ZATEN STALE** — modele giremez |

**Uyarı:** `EV-2026-08-10-702` bu turun **tek gerçek analitik dayanağıdır** ve
**2026-09-09'da STALE olur**. O tarihten sonra bu belgedeki beş sınıflandırmanın
hiçbiri `99-ops/veri-tazeligi.md` üzerinden yeniden doğrulanmadan
kullanılamaz. Türev belge `60-pazar/target-shelf-price-analysis.md` de aynı
tarihte **STALE** sayılmalıdır.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Bir zincir market (Migros / Macrocenter / CarrefourSA) rafının 600–1.000 TL
bandının fotoğrafı.**

Bu tek fotoğraf iki şeyi aynı anda yapar: (a) hedef merdivenin **mutlak**
konumunu ilk kez çıpalar, (b) whitespace iddiasını doğrular veya yok eder.
Şu anda beş sınıflandırmanın tamamı, **hedeflenen katmanın kendisinde sıfır
gözlemle** yapılmıştır. Fotoğrafta 650–875 TL arasında düzenli satılan ithal
şaraplar görülürse, "bu bantta stokta ithal rakip yok" cümlesi çöker ve
699/799 basamaklarının `ATTRACTIVE` etiketi düşer.

**İkinci çürütücü:** `T-504`'ün "**promosyonlu**" diye kapanması. O zaman
599 TL basamağının **tek** dayanağı yok olur ve `AGGRESSIVE` → `TOO_LOW`'a döner.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"Tek bir online uzman perakendecinin fiyat dağılımı, Türkiye'nin 600–1.000 TL
bandındaki rekabet yoğunluğunu temsil eder."**

Bu varsayım bu turda **kendi verimle zayıfladı**: aynı kanalın tüm stokta
katalogunda 600 TL altında **yalnızca 1 SKU** var ve stokta yerli medyan
**1.410 TL**. Yani kanal, hedef merdivenin **tamamını alt kuyruğunda tutuyor**.
Bir dağılımın kuyruğundan o dağılımın dışındaki bir bandın rekabet yapısını
okumak **yapısal olarak kırılgandır**. Bunu düzeltemedim: 17 ek kanal denedim,
hepsi kapalı (`EV-2026-08-10-701`).

**İkinci kırılgan varsayım:** `segment.fiyat_performans_ust_try = 900`.
999 TL'nin `TOO_HIGH` sınıflandırması büyük ölçüde buna dayanıyor — ve bu değer
bir **ESTIMATE**'tir, **aynı tek kanaldan** türetilmiştir. Başkan bu tavanı
1.000–1.100'e çekerse 999 TL doğrudan `PREMIUM_EDGE`'e döner.

**Üçüncüsü:** `available` alanının stok gerçeğini yansıttığı (`C-501`, OPEN).
Yansıtmıyorsa yoğunluk eğrisinin **tamamı** yanlıştır.

### 9.3 Hangi kaynağıma en az güveniyorum?

1. **`EV-2026-08-10-703`** (T5 zincir/tekel 450–650 TL iddiası). `C-503` ile
   aynı sınıf, `ttl: 0d`, **modele giremez** işaretledim. **Hiç güvenmiyorum** —
   ama tek zincir perakende sinyalim olduğu için kaydettim, kanıt olarak değil
   **çürütücü hipotez** olarak.
2. **`OBSERVED_BENCHMARK`'ların temsil gücü** (`EV-2026-08-09-501/502`).
   Okuma güveni HIGH (fotoğraftan), ama **temsil gücü MEDIUM** (`pazar.yaml` K6).
   n=2, tek mağaza, tek tarih, mağaza/şehir `UNKNOWN`, repoda snapshot yok,
   promosyon `UNKNOWN`. 599 basamağının **tamamı** buna asılıdır.
3. **`EV-2026-08-10-552`'deki stok dışı listeleme fiyatları.** 999 TL'nin
   "markalı bant" argümanında (Barone Montalto 950, Zonin 960, La Vieille Ferme
   979) bu isimleri kullandım — ama bunlar **raf fiyatı değildir** ve
   `C-501`/`C-561` altındadır. Argümanı **marka varlığı** üzerinden kurdum,
   **fiyat** üzerinden değil; yine de zayıf bir dayanaktır.
4. **Kendi ±%10 pencere seçimim.** Pencere genişliği bir **metodolojik
   tercihtir**, kanıt değildir. ±%5 seçseydim 699 ile 799 arasındaki fark
   daralırdı; ±%20 seçseydim tüm basamaklar birbirine benzerdi. Bu seçim
   PRIMARY önerisini **etkilemektedir** ve savunulabilir ama tek doğru değildir.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

- **Whitespace (650–875 TL) aslında bir "ölü bölge" ise** (`C-561` bu yönde
  çözülürse): 699 ve 799 basamakları `ATTRACTIVE` olmaktan çıkar, ithal şarabın
  fiilen döndüğü tek bölge 875 TL üstü olur → **PRIMARY 899'a kayar**, hedef
  fiyat yükselir, ters modelde tedarikçiye ödenebilecek maksimum fiyat **artar**
  → paradoksal olarak proje **kolaylaşır** ama fiyat/performans mandası **çöker**.
- **Whitespace gerçek boşluksa:** 799 TL hedefi ayakta kalır → **TEST / IMPORT
  PILOT lehine**.
- **`L8_CHAIN_RETAIL` gözlendiğinde merdivenin altında çıkarsa** (örn.
  `EV-2026-08-10-703`'ün ima ettiği gibi zincirde giriş 450–650 TL ise):
  799 TL zincir rafında yerli giriş segmentinin **%23–78 üstüne** düşer →
  konumlandırma zorlaşır → **KILL yönünde**.
- **`T-504` "promosyonlu" çıkarsa:** 599 downside senaryosu elenir; base case
  değişmez ama benchmark'a dayalı her cümle zayıflar → **HOLD yönünde**.
- **Tek kanal varsayımı çökerse:** bu belgenin **tamamı** yeniden yazılmalıdır.
  Model **sayısal olarak** doğrudan etkilenmez (bu turda `*.yaml`'a hiçbir sayı
  yazılmadı), ama ters modelin **hedefi** yeniden kurulur.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre | Maliyet |
|---|---|---|---|---|---|
| 1 | **Zincir market 600–1.000 TL bandının tam fiyat listesi** (Migros / Macrocenter / CarrefourSA) — `L8_CHAIN_RETAIL` ilk kez çıpalanır | İnsan gözlemci | 1 zincir market + 1 tekel bayii, İstanbul; banttaki **tüm** SKU'ların fiyatı + yerli/ithal ayrımı | 1 gün | ulaşım |
| 2 | **Hazır SKU listesiyle** whitespace testi: Santa Helena · Belleruche · Babich · Hans Baer · Henkell · Terra Mater · Botter Caleo · Luccarelli · Barone Montalto · La Vieille Ferme — rafta var mı, fiyatı ne? | Aynı kişi | Aynı ziyaret | — | ~0 |
| 3 | `T-504` / `OQ-001` — benchmark etiketi + ikinci gözlem | Aynı kişi | Metro şarap reyonu, **aynı gün** | — | ~600 TL |
| 4 | `OQ-702` — gözlenen kanalın giriş segmentini kalıcı olarak taşımadığının testi | `turkiye-pazar-kasifi` | Aynı feed'in +30 / +60 gün ölçümü | 60 gün | ~0 |
| 5 | `T-701` — hedef merdivenin hangi L8 alt katmanı olduğu | `yatirim-komitesi-baskani` | Karar | — | ~0 |
| 6 | `T-561` / `C-561` — whitespace mi ölü bölge mi | `yatirim-komitesi-baskani` | Karar + 1. ve 2. maddenin sonucu | — | ~0 |

**Not:** 1, 2 ve 3 **tek ziyarette** yapılır ve bu, TUR 1'den beri üçüncü kez
aynı sonuca varılan tespittir: **OQ-001'in ve şimdi hedef merdivenin önündeki
engel pahalı değil, fiziksel.** TUR 2.5 bu ziyaretin kapsamını bir kez daha
genişletmiştir — aynı gezi artık `T-504`, `T-701`, `OQ-502`, `OQ-552`,
`OQ-701` ve `C-561`'in bir kısmını **birlikte** kapatabilir. Maliyet aynı,
getirisi yine arttı.
