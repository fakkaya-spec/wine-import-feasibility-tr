# HEDEF TÜKETİCİ RAF FİYATI ANALİZİ (TARGET SHELF PRICE)

```yaml
ajan:          turkiye-pazar-kasifi
tur:           TUR 2.5 (TARGET SEGMENT DEGERLENDIRMESI)
tarih:         2026-08-10
durum:         SUBMITTED — ONERIDIR, KARAR DEGILDIR
kapsam:        "599 / 699 / 799 / 899 / 999 TL hedef raf fiyati merdiveninin
                REKABET KONUMU ve FIYAT YOGUNLUGU acisindan degerlendirilmesi.
                YENI PAZAR HARITASI CIKARILMAMISTIR."
yasak_uygulandi: "Talep elastikiyeti TAHMIN EDILMEMISTIR. Marj HESAPLANMAMISTIR.
                Vergi/navlun/ruhsat/tedarikci fiyati konusunda SONUC URETILMEMISTIR."
```

---

## 0. ETİKET AYRIMI — BU BELGENİN OKUMA KURALI (BAĞLAYICI)

Bu belgede **iki farklı nesne** vardır ve **birbirinin yerine kullanılamaz**:

| Nesne | Etiket | Ne | Kaynak |
|---|---|---|---|
| `599 · 699 · 799 · 899 · 999 TL` | **`TARGET_SHELF_PRICE`** / `INVESTOR_TARGET_SCENARIO` | Yatırımcının **hedeflediği** tüketici raf fiyatı. Bir gözlem **değildir**. Türkiye'de bu fiyatlarla satılan bir ürünümüz **yoktur**. | Kurucu/başkan tarafından verilen senaryo seti |
| `599,90 TL` (Gold Country) · `649,90 TL` (Central Creek) | **`OBSERVED_BENCHMARK`** | Metro Türkiye rafında **gerçekten görülmüş** fiyat. | `EV-2026-08-09-501`, `EV-2026-08-09-502` |

> **599 (target) ≠ 599,90 (observed).** Sayısal yakınlık tesadüfidir ve bu belgede
> hiçbir yerde birinin diğerini "kanıtladığı" iddia edilmemektedir.
> `OBSERVED_BENCHMARK`, `TARGET_SHELF_PRICE`'ın **rakip konumunu** okumak için
> kullanılan bir gözlemdir; hedefin **ulaşılabilirliğinin kanıtı değildir**.
> `pazar.yaml` **K5** gereği her kullanımda "Metro cash & carry gözlemi" niteliği
> yazılmıştır.

**İkinci bağlayıcı ayrım (K1):** Hedef merdiven bir **tüketici raf fiyatıdır (L8)**.
Elimizdeki L8 gözlemleri **iki farklı L8 alt katmanındandır**:

| Katman | Gözlem sayısı | Not |
|---|---|---|
| `L8_METRO_CASH_CARRY` | **2** (599,90 / 649,90 — ikisi de ithal) | K3: cash & carry yapısı gereği zincir perakendeden ucuzdur |
| `L8_ONLINE_UZMAN_PERAKENDE` | **471 stokta** (391 yerli + 80 ithal) | Tek envanter, iki alan adı; **bağımsız kanal değildir** |
| `L8_CHAIN_RETAIL` (Migros / Macrocenter / CarrefourSA) | **0** | **Hedef merdivenin asıl karşılığı olan katman HİÇ GÖZLENMEMİŞTİR** |
| `L8_TEKEL_BAYII` | **0** | — |
| `HORECA` | **0** | — |

Bu tablo, aşağıdaki tüm sınıflandırmaların **tavanını** belirler. Bkz. §5.

---

## 1. SINIFLANDIRMA EKSENİNİN TANIMI

Talep verisi **yoktur**. Bu yüzden sınıflandırma **talep** üzerinden değil,
**gözlenen rekabet yoğunluğu** ve **rekabet konumu** üzerinden yapılmıştır.
Etiketlerin bu belgedeki anlamı:

| Etiket | Bu belgedeki tanımı (talep içermez) |
|---|---|
| `TOO_LOW` | Hedef, gözlenen **her** kanalın rekabet dağılımının altındadır; fiyat noktasının ticari olarak var olduğu **hiçbir** gözlemle desteklenmez |
| `AGGRESSIVE` | Hedef, gözlenen rekabet tabanının **üzerinde değil, üstünde/dibinde**; yalnızca **tek bir zayıf gözlemle** desteklenir |
| `ATTRACTIVE` | Hedefte (a) **gerçek gözlenmiş rekabet yoğunluğu** vardır (fiyat noktası ticari olarak var), **ve** (b) **stokta ithal rakip yoktur** (whitespace) |
| `PREMIUM_EDGE` | Hedef, gözlenen **stokta ithal rekabetin başladığı** noktaya değmiştir; whitespace kaybolur |
| `TOO_HIGH` | Hedef, projenin kendi **fiyat/performans segment tavanı ESTIMATE'ini (900 TL)** aşar ve tanınmış uluslararası markaların bandına girer |
| `INSUFFICIENT_EVIDENCE` | Kanıt sınıflandırmaya yetmez |

**Kritik uyarı:** `ATTRACTIVE` bu belgede **"bu fiyattan satar"** demek DEĞİLDİR.
**"Bu fiyat noktasında gözlenmiş bir pazar vardır ve orada stokta ithal rakip
yoktur"** demektir. Talebe dair hiçbir iddia yoktur.

---

## 2. SINIFLANDIRMANIN DAYANDIĞI GÖZLEM TABANI

### 2.1 Rekabet yoğunluğu eğrisi (`EV-2026-08-10-702`)

Tek gözlenebilir çok-SKU'lu kanal, 2026-08-10, **stokta** olanlar:

| Bant (TL) | Yerli SKU | İthal SKU |
|---|---|---|
| 400–500 | 1 | 0 |
| 500–600 | **0** | 0 |
| 600–700 | 7 | 0 |
| 700–800 | 18 | 0 |
| 800–900 | 19 | **1** (875) |
| 900–1.000 | 21 | **1** (948) |
| 1.000–1.100 | 28 | 0 |
| 1.100–1.200 | 46 | 3 |
| 1.200+ | 251 | 75 |

- Stokta yerli: **n=391**, min **460 TL**, **medyan 1.410 TL**
- Stokta ithal: **n=80**, min **875 TL**
- **Hedef bölge 600–1.000 TL'de: 65 yerli / 2 ithal**

### 2.2 Her hedef basamağında ±%10 penceredeki rakip sayısı (`EV-2026-08-10-702`)

| Hedef | Pencere | Yerli **stokta** | İthal **stokta** | İthal **stok dışı** (raf fiyatı DEĞİL) |
|---|---|---|---|---|
| **599** | 539–659 | **3** | **0** | 3 |
| **699** | 629–769 | **17** | **0** | 15 |
| **799** | 719–879 | **31** | **1** | 22 |
| **899** | 809–989 | **35** | **2** | 31 |
| **999** | 899–1.099 | **49** | **1** | 30 |

### 2.3 Metro tarafı (`OBSERVED_BENCHMARK`, `EV-2026-08-09-501/502`)

Kullanılabilir Metro gözlemi **yalnızca 2 adettir** ve **ikisi de ithaldir**:
599,90 TL (Gold Country, ABD) ve 649,90 TL (Central Creek, Avustralya).
Diğer 5 Metro satırı `EV-2026-08-09-512` (T5 içerik çiftliği) kaynaklıdır ve
`C-503` ile **modele giremez** kararı verilmiştir.

**Bu 2 gözlemin taşıyabileceği yük sınırlıdır:**
promosyon durumu `UNKNOWN` (`T-504`, CRITICAL), KDV sunumu `C-551` ile
nitelenmiş, mağaza/şehir `UNKNOWN`, repoda snapshot **yok**, `confidence: MEDIUM`.

### 2.4 Bu turda yeni bulunan ve sınıflandırmayı **zayıflatan** bulgu

`EV-2026-08-10-702`: Gözlenen kanalın **tüm stokta katalogunda (471 SKU)
600 TL altında yalnızca 1 SKU vardır** ve stokta yerli medyan **1.410 TL**'dir.

Yani **"bu kanalda 875 TL altında stokta ithal şarap yok"** bulgusu
**kısmen bir kanal artefaktıdır** — bu kanal 600 TL altında **yerli** şarap da
taşımamaktadır. Kanalın ağırlık merkezi hedef merdivenin **1,4–2,4 katı
üstündedir**. Aşağıdaki tüm sınıflandırmalar bu kanalın **alt kuyruğundan**
okunmuştur. Bu, TUR 1/TUR 2'nin "boşluk" bulgusunu çürütmez ama
**pazar-genelinde bir boşluk** olarak okunmasını yasaklar.

---

## 3. HEDEF FİYAT SINIFLANDIRMASI

### 3.1 — 599 TL → `AGGRESSIVE`

```yaml
target_shelf_price: 599
etiket:             TARGET_SHELF_PRICE (INVESTOR_TARGET_SCENARIO)
siniflandirma:      AGGRESSIVE
confidence:         LOW
kdv:                KDV DAHIL (hedef tanimi geregi)
evidence_id:        [EV-2026-08-10-702, EV-2026-08-09-501, EV-2026-08-09-502, EV-2026-08-10-501]
```

**Dayanak:**
1. Gözlenen kanalda 599 TL, **391 stokta yerli SKU'nun %99,7'sinin altındadır**
   (altında yalnızca 1 SKU: Mistia 460 TL). 500–600 TL bandında **hiç** yerli
   stokta SKU **yoktur** (`EV-2026-08-10-702`).
2. Aynı kanalda 599 TL'nin altında **stokta hiç ithal şarap yoktur**; stokta
   ithal taban **875 TL**'dir (`EV-2026-08-10-501`, `EV-2026-08-10-551`).
3. **`TOO_LOW` olmamasının tek nedeni `OBSERVED_BENCHMARK`'tır:** Metro
   Türkiye rafında **ithal** bir şarap 599,90 TL etiketle **fiilen görülmüştür**
   (`EV-2026-08-09-501`). Yani bu fiyat noktasının ithal şarap için Türkiye'de
   **var olduğu** en az bir kez gözlenmiştir. Bu, hedefin **ulaşılabilir**
   olduğunu göstermez; yalnızca **imkânsız olmadığını** gösterir.

**Neden `confidence: LOW`:**
Sınıflandırma tamamen **tek bir SKU'nun tek bir gözlemine** asılıdır. O gözlemin
promosyon durumu `UNKNOWN`'dır (`T-504`, CRITICAL) ve katmanı
`L8_METRO_CASH_CARRY`'dir — **K3 gereği yapısı gereği zincir perakendeden
ucuzdur**. Hedef merdiven zincir perakende L8'ini kastediyorsa, 599 TL
gözlemin ima ettiğinden **daha da agresiftir**.

**Bu sınıflandırmayı ne çürütür:**
- `T-504` "**promosyonlu**" diye kapanırsa → 599 TL'nin tek dayanağı düşer ve
  bu satır **`TOO_LOW`**'a döner.
- Bir Metro/zincir/tekel rafında 500–650 TL bandında **normal fiyatlı** ikinci
  bir ithal SKU görülürse → `AGGRESSIVE` → **`ATTRACTIVE`** yönüne kayar.
- `EV-2026-08-10-703`'teki T5 sinyali (zincir/tekelde 75 cl 450–650 TL) doğru
  çıkarsa → 599 TL zincir rafında **yerli giriş segmentinin tam içine** düşer ve
  ithal bir ürün için **rekabet konumu sertleşir** (yerliyle aynı fiyat, marka
  bilinirliği yok).

---

### 3.2 — 699 TL → `ATTRACTIVE`

```yaml
target_shelf_price: 699
etiket:             TARGET_SHELF_PRICE (INVESTOR_TARGET_SCENARIO)
siniflandirma:      ATTRACTIVE
confidence:         MEDIUM
evidence_id:        [EV-2026-08-10-702, EV-2026-08-10-501, EV-2026-08-10-502, EV-2026-08-10-551, EV-2026-08-09-502]
```

**Dayanak:**
1. **Gerçek gözlenmiş yoğunluk başlar:** ±%10 pencerede **17 stokta yerli SKU**
   (599'da 3 idi). 600–700 bandında 7, 700–800 bandında 18 yerli SKU vardır
   (`EV-2026-08-10-702`). Fiyat noktası ticari olarak **var**.
2. **Stokta ithal rakip: 0.** Gözlenen kanalda 699 TL ±%10'da stokta tek bir
   ithal SKU yoktur; stokta ithal taban 875 TL'dir → **whitespace**.
3. Rakip seti isimli ve somuttur: Asmadan 649, KA Winery 655, Lermonos 655,
   Umurbey 659, Nif Bağları 670, Mistia 672, Vinkara 710–754, KA Winery 745,
   Turasan 758, Çamlıbağ 760 — **tamamı yerli** (`EV-2026-08-10-502`).
4. `pazar.yaml` `segment.fiyat_performans_alt_try = 600` / `ust = 900`
   (ESTIMATE) bandının **alt-orta** kısmındadır.
5. `OBSERVED_BENCHMARK` ile tutarlılık (**ESTIMATE, kanıt değil**): 649,90 TL
   bir Metro **cash & carry** ithal gözlemidir; K3/`l8_chain_retail` notu gereği
   gerçek zincir L8'in bunun **üstünde** olması beklenir. 699 TL bu beklentinin
   içine düşer. **Bu bir doğrulama değil, yön tutarlılığıdır.**

**Neden `confidence: MEDIUM` (HIGH değil):**
Yoğunluk tek kanaldan okunmuştur ve o kanal premium'a kayıktır
(`EV-2026-08-10-702`). Ayrıca 4. maddedeki bant sınırlarının kendisi de
**aynı kanaldan** türetilmiştir — bağımsız doğrulama yoktur.

**Bu sınıflandırmayı ne çürütür:**
- **En güçlü çürütücü (`C-561`):** Bu bantta 15 ithal listeleme **katalogda
  tanımlı ama stok dışıdır** (Santa Helena 677, Belleruche 680, Babich 697,
  Hans Baer 702, Henkell 746 …). "Stokta ithal yok" bir **whitespace** değil,
  bir **dönmeme (rotasyon yokluğu)** işareti olabilir. O zaman `ATTRACTIVE`
  → `INSUFFICIENT_EVIDENCE` veya negatif okumaya döner. `T-561` OPEN.
- Bir zincir market rafında 650–750 TL bandında **stokta ve dönen** ithal şarap
  görülmesi → whitespace iddiası düşer.
- `available` alanının stok gerçeğini yansıtmadığı ispatlanırsa (`C-501`) →
  tüm yoğunluk eğrisi geçersizdir.

---

### 3.3 — 799 TL → `ATTRACTIVE`

```yaml
target_shelf_price: 799
etiket:             TARGET_SHELF_PRICE (INVESTOR_TARGET_SCENARIO)
siniflandirma:      ATTRACTIVE
confidence:         MEDIUM
evidence_id:        [EV-2026-08-10-702, EV-2026-08-10-501, EV-2026-08-10-502, EV-2026-08-10-551]
```

**Dayanak:**
1. **Merdivenin whitespace içindeki en yoğun basamağı:** ±%10 pencerede
   **31 stokta yerli SKU** (699'da 17 idi) — yani gözlenen rekabet yoğunluğu
   699'a göre **1,8 kat** yüksektir (`EV-2026-08-10-702`).
2. **Stokta ithal rakip pratikte yok:** pencerede 1 SKU (Tesori Prosecco 875 TL)
   ve o da pencerenin **en üst ucundadır**; 799 TL'nin **altında** stokta hiç
   ithal SKU yoktur.
3. `pazar.yaml` `segment` bandının (600–900, ESTIMATE) **tam ortasındadır**.
4. Rakip seti: KA Winery 745, Turasan 758, Çamlıbağ 760, Diren 790, Barel 790,
   Büyülübağ 792–854, Kastro Tireli 816–820, Gaya 820, Ni&Ce 860,
   Antioche 861 — **tamamı yerli**.

**Neden `confidence: MEDIUM`:**
§2.4'teki kanal artefaktı uyarısı burada da geçerlidir; ayrıca 799 TL,
`OBSERVED_BENCHMARK`'ların (599,90 / 649,90) **%23–33 üstündedir**. Bir
"fiyat/performans ithal" konumlandırması için bu bir **gerilimdir**: gözlenen
tek ithal giriş noktasının belirgin biçimde üstünde fiyatlanmak, fiyat/performans
iddiasını zayıflatır. Bu gerilim **çözülmemiştir** — çözümü `T-504`'ün
(benchmark promosyonlu muydu) ve `L8_CHAIN_RETAIL`'in kapanmasına bağlıdır.

**Bu sınıflandırmayı ne çürütür:**
- `T-504` "**normal fiyat**" diye kapanırsa → 599,90 TL kalıcı bir ithal giriş
  fiyatıdır ve 799 TL onun **%33 üstündedir**; fiyat/performans konumu bozulur,
  `ATTRACTIVE` → **`PREMIUM_EDGE`**'e kayar.
- `C-561` "bantta ürün var ama dönmüyor" yönünde çözülürse → whitespace argümanı
  çöker.
- `EV-2026-08-10-703` sinyali doğrulanırsa (zincir/tekel 450–650 TL) → 799 TL
  zincir rafında yerli giriş segmentinin **%23–78 üstüne** düşer → `PREMIUM_EDGE`.

---

### 3.4 — 899 TL → `PREMIUM_EDGE`

```yaml
target_shelf_price: 899
etiket:             TARGET_SHELF_PRICE (INVESTOR_TARGET_SCENARIO)
siniflandirma:      PREMIUM_EDGE
confidence:         MEDIUM
evidence_id:        [EV-2026-08-10-702, EV-2026-08-10-551, EV-2026-08-10-501]
```

**Dayanak:**
1. **Stokta ithal rekabetin başladığı nokta tam burasıdır:** gözlenen kanalda
   stokta en ucuz ithal şarap **875 TL** (Tesori Prosecco), ikincisi **948 TL**
   (La Piuma Chianti) — ikisi de 899 TL'nin ±%10 penceresindedir
   (`EV-2026-08-10-551`). **Whitespace burada biter.**
2. `pazar.yaml` `segment.fiyat_performans_ust_try = 900` (ESTIMATE) **tavanına
   değer**. 899 TL, projenin kendi tanımladığı fiyat/performans bandının
   **son basamağıdır**.
3. Yerli yoğunluk hâlâ yüksektir (±%10'da 35 SKU) — yani rekabet **azalmaz,
   üstüne ithal rekabet eklenir**.
4. `OBSERVED_BENCHMARK`'ların **%38–50 üstündedir**.

**Neden `TOO_HIGH` değil:** Gözlenen kanalda 899 TL hâlâ stokta yerli SKU'ların
yalnızca **%11,5**'inin üstündedir; kanalın kendi ölçeğinde "yüksek" bir fiyat
değildir. Ayrıca bant tavanı 900 TL **ESTIMATE**'tir, FACT değildir.

**Bu sınıflandırmayı ne çürütür:**
- `segment.fiyat_performans_ust_try = 900` ESTIMATE'i yanlışsa (tek kanaldan
  türetilmiştir) → 899 TL `ATTRACTIVE`'e kayabilir.
- Tesori Prosecco / La Piuma Chianti'nin bu kanalda stokta olması bir
  **tesadüf** ise (n=2), "ithal rekabet 875'te başlar" cümlesi çöker.
- Bir zincir market rafında 600–800 TL bandında düzenli dönen ithal şarap
  bulunursa → ithal taban aşağı iner, 899 daha da premium olur (**`TOO_HIGH`**
  yönünde).

---

### 3.5 — 999 TL → `TOO_HIGH` *(fiyat/performans mandası için)*

```yaml
target_shelf_price: 999
etiket:             TARGET_SHELF_PRICE (INVESTOR_TARGET_SCENARIO)
siniflandirma:      TOO_HIGH
kapsam_notu:        "PROJENIN FIYAT/PERFORMANS MANDASI ICIN. Mutlak anlamda
                     'pahali' demek DEGILDIR — talep iddiasi ICERMEZ."
confidence:         LOW
evidence_id:        [EV-2026-08-10-702, EV-2026-08-10-551, EV-2026-08-10-552]
```

**Dayanak:**
1. `pazar.yaml` `segment.fiyat_performans_ust_try = 900` (ESTIMATE) **aşılır**.
   Proje mandası `CLAUDE.md §0`'da **"fiyat/performans segmenti"** olarak
   tanımlıdır; 999 TL bu tanımın dışına çıkar.
2. `OBSERVED_BENCHMARK`'ların **%54–67 üstündedir**. Gözlenen tek ithal giriş
   fiyatının 1,5–1,7 katına fiyatlanan bir ürün, "fiyat/performans ithal şarap"
   olarak konumlanamaz.
3. Bu bantta **tanınmış uluslararası markalar** vardır — Barone Montalto 950,
   Zonin Chianti 960, La Vieille Ferme 979, Baron de Lestac 1.015, Casalforte
   1.094 (`EV-2026-08-10-552`, **stok dışı listeleme — raf fiyatı DEĞİL**).
   Marka bilinirliği sıfır olan yeni bir ithalatın bu isimlerle **fiyat üzerinden
   değil, marka üzerinden** yarışması gerekir.
4. ±%10 pencerede **49 stokta yerli SKU** — merdivenin en kalabalık basamağı.

**Neden `confidence: LOW`:**
Sınıflandırmanın belkemiği olan 900 TL tavanı bir **ESTIMATE**'tir ve **aynı
tek kanaldan** türetilmiştir. Ayrıca 3. maddedeki marka listesi **stok dışı
listelemelerden** gelir; bunlar raf fiyatı değildir ve `C-501`/`C-561` altındadır.
Karşı argüman ciddidir: gözlenen kanalda **stokta dönen** ithal şarap ancak
875 TL'den itibaren başlar — yani 999 TL, ithal şarabın fiilen **döndüğü**
tek gözlenmiş bölgedir.

**Bu sınıflandırmayı ne çürütür:**
- `segment.fiyat_performans_ust_try` başkan tarafından yukarı revize edilirse
  (örn. 1.000–1.100 TL) → 999 TL doğrudan `PREMIUM_EDGE`'e döner.
- `C-561`, "hedef bantta ithal ürün listeleniyor ama **dönmüyor**" yönünde
  çözülürse → ithal şarabın gerçekten döndüğü bölge 875 TL üstüdür ve
  999 TL **`ATTRACTIVE`**'e kayabilir. Bu, bu belgedeki **en büyük tek
  ters-çevirme riskidir**.
- `T-504` "promosyonlu" çıkarsa → `OBSERVED_BENCHMARK` yukarı kayar, 2. madde
  zayıflar.

---

### 3.6 Özet tablo

| Hedef | Sınıflandırma | Confidence | Stokta yerli rakip (±%10) | Stokta ithal rakip (±%10) | Ana dayanak |
|---|---|---|---|---|---|
| **599** | `AGGRESSIVE` | **LOW** | 3 | 0 | Yalnızca `OBSERVED_BENCHMARK` (n=1, promo UNKNOWN) |
| **699** | `ATTRACTIVE` | MEDIUM | 17 | 0 | Yoğunluk başlar + whitespace |
| **799** | `ATTRACTIVE` | MEDIUM | 31 | 1 (875, pencere ucu) | En yoğun whitespace basamağı |
| **899** | `PREMIUM_EDGE` | MEDIUM | 35 | **2** (875 / 948) | İthal taban + segment tavanı (900) |
| **999** | `TOO_HIGH` *(manda için)* | **LOW** | 49 | 1 | Segment tavanı aşılır; markalı bant |

---

## 4. ÖNERİ — PRIMARY / SECONDARY / STRETCH

> **BUNLAR ÖNERİDİR, KARAR DEĞİLDİR.** Nihai karar
> `yatirim-komitesi-baskani`'na aittir. Bu turda yatırım kararı verilmemektedir.

### PRIMARY TARGET SHELF PRICE — **799 TL** (KDV dahil, 750 ml still wine)

```yaml
oneri:        PRIMARY
deger:        799
unit:         TRY
kdv:          DAHIL
katman_niyeti: L8 (tuketici raf fiyati) — hangi L8 alt katmani oldugu UNKNOWN (bkz. §5)
confidence:   MEDIUM
evidence_id:  [EV-2026-08-10-702, EV-2026-08-10-501, EV-2026-08-10-502, EV-2026-08-10-551]
```

**Gerekçe:**
- Merdivenin **whitespace içinde kalan en yoğun** basamağıdır: ±%10 pencerede
  31 gözlenmiş stokta rakip (699'un 1,8 katı), **stokta ithal rakip yok**.
- Gözlenen stokta ithal tabanın (**875 TL**) **altındadır** — yani ithal
  rekabete girmeden, gerçek gözlenmiş bir yoğunluk bölgesine oturur.
- Projenin kendi `segment` bandının (600–900 ESTIMATE) **ortasıdır**; bant
  sınırlarına dayanmadığı için bant hatasına en az duyarlı basamaktır.

**Bilinen zayıflığı (açıkça yazılmıştır):** `OBSERVED_BENCHMARK`'ların
%23–33 üstündedir. `T-504` "normal fiyat" diye kapanırsa bu öneri
`PREMIUM_EDGE`'e kayar ve **SECONDARY ile yer değiştirmelidir**.

---

### SECONDARY TARGET SHELF PRICE — **699 TL**

```yaml
oneri:        SECONDARY
deger:        699
unit:         TRY
kdv:          DAHIL
confidence:   MEDIUM
evidence_id:  [EV-2026-08-10-702, EV-2026-08-10-502, EV-2026-08-09-502]
```

**Gerekçe:**
- **Fiyat/performans mandasına en sadık** basamaktır: `OBSERVED_BENCHMARK`
  649,90 TL'nin hemen üstünde durur ve K3'ün "gerçek zincir L8'i Metro cash &
  carry'nin üstündedir" **beklentisiyle yön olarak tutarlıdır** (ESTIMATE).
- Gerçek gözlenmiş yoğunluğun **başladığı** noktadır (17 stokta yerli rakip);
  599'un aksine tek bir gözleme asılı değildir.
- Stokta ithal rakip **0** → whitespace.

**Neden PRIMARY değil:** Gözlenen yoğunluk 799'un **%55'i** kadardır ve
600–700 bandında stokta yalnızca 7 SKU vardır — yani 699, yoğunluk eğrisinin
hâlâ **dik yükselen** kısmındadır, platosunda değil.

---

### STRETCH TARGET SHELF PRICE — **899 TL**

```yaml
oneri:        STRETCH
deger:        899
unit:         TRY
kdv:          DAHIL
confidence:   LOW-MEDIUM
evidence_id:  [EV-2026-08-10-702, EV-2026-08-10-551]
```

**Gerekçe:**
- Yukarı yönlü senaryodur: gözlenen kanalda **stokta dönen ithal şarabın
  fiilen bulunduğu** en alt bölgeye (875–948 TL) girer. Yani "ithal ürün bu
  ülkede bu fiyattan **dönüyor**" iddiasının **tek gözlenmiş** dayanağı buradadır.
- `segment` tavanının (900 ESTIMATE) tam altındadır — mandayı **teknik olarak
  ihlal etmez**.

**Bedeli açıkça yazılır:** Whitespace **kaybolur** (2 stokta ithal rakip),
`OBSERVED_BENCHMARK`'ların %38–50 üstüne çıkılır ve marka bilinirliği olmayan
bir ürün için konumlandırma yükü artar.

---

### Merdivenin diğer ucu — 599 TL neden "stretch" değil, **taban senaryosu**dur

599 TL **daha ambisiyöz değil, daha risklidir**. Eğer ters model daha düşük bir
hedef raf fiyatı **dayatırsa**, 599 TL bir **downside/floor senaryosu** olarak
çalıştırılmalı ve şu iki koşul rapora yazılmalıdır: (a) `T-504` promosyon
sorusu kapanmadan 599 TL bir "pazar fiyatı" gibi kullanılamaz, (b) K3 gereği
zincir perakende L8'inde 599 TL, Metro'da 599,90 görmekten **daha zordur**.

---

## 5. BU ÖNERİNİN KANIT SEVİYESİ — DÜRÜST DEĞERLENDİRME

| Soru | Cevap |
|---|---|
| **Kaç bağımsız kanal?** | **2** — Metro Türkiye (cash & carry) ve iyisarap.plus/.pro (online uzman perakende). İkinci kanalın iki alan adı **aynı envanterdir**, ayrı kanal değildir (`EV-2026-08-10-551`). TUR 2.5'te **17 ek alan adı** denendi, **0** kullanılabilir kanal bulundu (`EV-2026-08-10-701`) — tek kanal zaafı **üçüncü kez** kırılamadı. |
| **Kaç SKU?** | Yoğunluk eğrisi: **471 stokta SKU** (391 yerli + 80 ithal) — **hepsi tek kanaldan**. Metro: **2 kullanılabilir SKU** (5 satır daha var ama `C-503` ile modele giremez). |
| **Gözlemler ne kadar taze?** | **Çok taze** — 2026-08-09 ve 2026-08-10, yani 0–1 günlük. `ttl: 30d`; **2026-09-08/09'da STALE** olur. Bu tarihten sonra hiçbir sınıflandırma yeniden doğrulanmadan kullanılamaz (`99-ops/veri-tazeligi.md`). |
| **Tek kanala mı dayanıyor?** | **Yoğunluk eğrisinin tamamı EVET.** 599 basamağının sınıflandırması ise **tek SKU'nun tek gözlemine** dayanır. Yalnızca "599 TL'de ithal şarap var mı" sorusunda iki kanal birbirini **çelişkiye düşürecek** biçimde konuşur (Metro: var; online uzman: yok) — bu çelişki **çözülmemiştir**. |
| **Hedef katman gözlendi mi?** | **HAYIR.** Hedef merdiven bir tüketici raf fiyatıdır ve asıl karşılığı `L8_CHAIN_RETAIL`'dir (Migros / Macrocenter / CarrefourSA). Bu katmanda **SIFIR gözlem** vardır (`pazar.yaml → l8_chain_retail: null / UNKNOWN`, `EV-2026-08-09-511`). **Bu, bu belgenin en büyük zaafıdır** → `T-701`. |
| **Kanal temsil gücü** | Gözlenen çok-SKU'lu kanal **premium'a kayıktır**: 471 stokta SKU'nun **1'i** 600 TL altındadır, stokta yerli medyan **1.410 TL** (`EV-2026-08-10-702`). Hedef merdivenin tamamı bu kanalın **alt kuyruğundadır**. |
| **Açık CRITICAL ticket** | `T-504` (benchmark promosyon durumu) **OPEN / CRITICAL**. 599 ve 799 basamaklarının sınıflandırması bu ticket'a **doğrudan bağlıdır**. |
| **Açık çelişkiler** | `C-501` (available filtresi), `C-551` (Metro şarap KDV sunumu), `C-561` (bant assortmanda dolu / stokta boş) — **üçü de OPEN**. |
| **GENEL KANIT SEVİYESİ** | **Göreli sıralama (hangi basamak diğerinden daha yoğun/daha whitespace): MEDIUM.** **Mutlak çıpalama (799 TL Türkiye pazarında doğru fiyat mıdır): LOW.** |

**Tek cümleyle:** Bu belge, **hangi hedef fiyatın hangisine göre daha iyi
konumlandığını** makul bir kanıtla söyleyebilir; **hedef fiyatın Türkiye
tüketici rafında doğru olduğunu söyleyemez.**

---

## 6. SINIFLANDIRILAMAYAN / KOŞULLU BASAMAKLAR

| Hedef | Durum | Neden |
|---|---|---|
| 599 | Sınıflandırıldı ama **koşullu** | `T-504` (CRITICAL, OPEN) kapanmadan `AGGRESSIVE` etiketi geçicidir; "promosyonlu" çıkarsa `TOO_LOW` |
| 999 | Sınıflandırıldı ama **confidence LOW** | Dayanak, tek kanaldan türetilmiş bir **ESTIMATE** bant tavanıdır (900 TL); `C-561` ters çözülürse `ATTRACTIVE`'e döner |
| **Hiçbiri** | `L8_CHAIN_RETAIL` karşılığı **UNKNOWN** | Beş basamağın hiçbiri için zincir market tüketici raf fiyatı gözlemi yoktur; merdivenin **mutlak** konumu bilinmiyor |
| **Hiçbiri** | HoReCa karşılığı **UNKNOWN** | Restoran şarap listesi örneklemi hâlâ alınamadı; HoReCa fiyat çarpanı `null` |

**Talep tarafı bilinçli olarak boş bırakılmıştır.** Hiçbir basamak için
"tüketici bu fiyatı öder / ödemez" denmemiştir. Elimizde **tek bir talep,
hacim, rotasyon veya satış verisi yoktur**; `C-561` tam da bu boşluğun adıdır.

---

## 7. 500–1.000 TL BOŞLUK BULGUSUNUN GÜNCEL DURUMU (TUR 2.5)

| Tur | Bulgu | Durum |
|---|---|---|
| TUR 1 (2026-08-09) | "400–800 TL'de stokta 0 ithal SKU; en ucuz stokta ithal 875 TL (n=80)" | `EV-2026-08-10-501` |
| TUR 2 (2026-08-10) | İkinci tarihte **birebir tekrarlandı**; 500–1.000 TL'de stokta 2 ithal SKU (875 / 948), ikisi de TUR 1'de zaten görülmüştü. **62 ithal listeleme katalogda tanımlı ama stok dışı** → `C-561` | `EV-2026-08-10-551`, `-552` |
| **TUR 2.5 (bugün)** | **Boşluk KEŞFİ YENİLENMEDİ — NİTELENDİ.** Aynı snapshot 100 TL çözünürlükte yeniden binlendi: (a) 500–600 TL'de **yerli de dahil** stokta **0** SKU, (b) tüm katalogda **600 TL altında stokta yalnızca 1 SKU** var, (c) stokta yerli **medyan 1.410 TL**. | `EV-2026-08-10-702` |

**Güncel okuma (bu turun net katkısı):**

> "500–1.000 TL bandında ithal şarap yoktur" cümlesi **bu haliyle yanlış
> okunmaktadır.** Doğru cümle şudur: **gözlenen tek çok-SKU'lu kanal, 600 TL
> altında hiçbir şarap (yerli dahil) taşımamakta ve 875 TL altında hiçbir ithal
> şarabı stokta tutmamaktadır.** Bu, bir **pazar boşluğu** olabileceği gibi,
> tamamen bir **kanal seçimi** de olabilir.

**Boşluğu ÇÜRÜTEN kanıt bugün de mevcuttur ve göz ardı edilmemelidir:**
Metro rafında 599,90 ve 649,90 TL etiketli **iki ithal şarap fiilen görülmüştür**
(`EV-2026-08-09-501/502`). Yani boşluk **pazar geneli değildir** — en azından
Metro'da 500–700 TL bandında ithal şarap **vardır**. İki kanal bu konuda
**birbiriyle çelişmektedir** ve çelişki **çözülmemiştir**.

**Bu boşluğu kapatacak tek şey masabaşı çalışma değildir** (3 turda 25 alan adı
denendi, `EV-2026-08-10-559`, `-558`, `-701`): bir **fiziksel mağaza turudur**
(`OQ-502`, `OQ-552`, `T-504` — üçü aynı ziyarette kapanır).

---

## 8. MODEL GİRDİSİ ÖNERİLERİ

> `80-model/inputs/*.yaml`'a **DOKUNULMAMIŞTIR**. Aşağıdakiler **öneridir**;
> merge kararı `yatirim-komitesi-baskani`'na aittir.

| YAML | Alan | Önerilen | status | evidence_id |
|---|---|---|---|---|
| `pazar.yaml` | `target_shelf_price.primary_try` | **799** | **ONERI / ESTIMATE** | `EV-2026-08-10-702` |
| `pazar.yaml` | `target_shelf_price.secondary_try` | **699** | **ONERI / ESTIMATE** | `EV-2026-08-10-702` |
| `pazar.yaml` | `target_shelf_price.stretch_try` | **899** | **ONERI / ESTIMATE** | `EV-2026-08-10-702`, `-551` |
| `pazar.yaml` | `target_shelf_price.floor_downside_try` | **599** | **ONERI / ESTIMATE (KOSULLU — T-504)** | `EV-2026-08-09-501` |
| `pazar.yaml` | `target_shelf_price.etiket` | `TARGET_SHELF_PRICE` — `OBSERVED_BENCHMARK` ile **birleştirilemez** | KURAL | — |
| `pazar.yaml` | `target_shelf_price.katman_niyeti` | `L8` — hangi L8 alt katmanı **UNKNOWN** | UNKNOWN | `T-701` |
| `pazar.yaml` | `segment.yogunluk_egrisi_100tl` | `EV-2026-08-10-702`'deki tablo | FACT (tek kanal) | `EV-2026-08-10-702` |
| `pazar.yaml` | `gozlem_havuzu.kanal_sayisi_denenmis` | 25 alan adı denendi / 2 kullanılabilir kanal | FACT | `EV-2026-08-10-701` |
| `pazar.yaml` | `l8_chain_retail.deger_try` | **null (DEĞİŞMEMELİ)** | UNKNOWN | `EV-2026-08-09-511` |

**Ters model kuralı (öneri):** Hedef merdiven modele **tek nokta olarak değil,
en az `{699, 799, 899}` bandı olarak** girmelidir (K5 ile aynı mantık).
`599` ayrı bir **downside** senaryosu olarak koşulmalı, base case'e alınmamalıdır.

---

## 9. KAYNAK LİSTESİ (bu belgede kullanılan)

| evidence_id | tier | ne | tur |
|---|---|---|---|
| `EV-2026-08-09-501` | T4 | Gold Country 599,90 TL — Metro, foto | TUR 1 |
| `EV-2026-08-09-502` | T4 | Central Creek 649,90 TL — Metro, foto | TUR 1 |
| `EV-2026-08-09-511` | T4 | Zincir market online kanalında şarap fiyatı yok | TUR 1 |
| `EV-2026-08-10-501` | T4 | Stokta ithal n=80, min 875 TL (2026-08-09) | TUR 1.5 |
| `EV-2026-08-10-502` | T4 | Stokta yerli n=394, min 460, 600–800'de 25 SKU | TUR 1.5 |
| `EV-2026-08-10-551` | T4 | İkinci tarihli tekrar: aynı sayılar (2026-08-10) | TUR 2 |
| `EV-2026-08-10-552` | T4 | 62 ithal listeleme stok dışı — **raf fiyatı DEĞİL** | TUR 2 |
| `EV-2026-08-10-558/559` | T4 | 8 alternatif kanal denendi, kapalı | TUR 2 |
| **`EV-2026-08-10-701`** | T4 | **17 ek kanal denendi, 0 kullanılabilir** | **TUR 2.5** |
| **`EV-2026-08-10-702`** | T4 | **100 TL çözünürlükte yoğunluk eğrisi + kanal premium kayması** | **TUR 2.5** |
| **`EV-2026-08-10-703`** | T5 | **Zincir/tekel 450–650 TL iddiası — MODELE GİREMEZ** | **TUR 2.5** |

---

*Bu belge bir öneridir. Karar `yatirim-komitesi-baskani`'nındır.*
