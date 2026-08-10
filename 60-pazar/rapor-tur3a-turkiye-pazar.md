# TUR 3A RAPORU — SAHA MAĞAZA GÖZLEM PAKETİ (T-917)

```yaml
ajan:            turkiye-pazar-kasifi
tur:             TUR 3A
tarih:           2026-08-10
durum:           SUBMITTED
nitelik:         ARAC URETIMI — PAZAR ARASTIRMASI DEGILDIR
yeni_gozlem:     0
yeni_kanit_karti: 0
yeni_fiyat:      0
```

---

## 1. YÖNETİCİ ÖZETİ

`T-917` (fiziksel mağaza turu) **dış dünyada bir insan aksiyonu gerektiriyor** ve
üç turdur masabaşından kapatılamadı: alkol tüketiciye online satılamıyor
(`EV-2026-08-09-511`), Metro broşürlerinde **sıfır alkol SKU'su** var
(`EV-2026-08-09-514`), Metro'nun açık fiyat API'si emekli, agregatörler 403
(`EV-2026-08-10-504` — 8 yol), 25 alan adı denendi, 2 kullanılabilir kanal çıktı
(`EV-2026-08-10-701`). Bu turda **dördüncü bir masabaşı denemesi yapılmamıştır.**

Bunun yerine kurucunun sahada kullanacağı **minimal veri seti ve tek sayfalık
kontrol listesi** üretilmiştir: **23 alan** (8'i sahada elle yazılır, 10'u
masabaşında fotoğraftan doldurulur, 5'i mağaza başlığı), **1 sayım formu**,
**1 arama listesi (14 SKU)**, **5 kodlu fotoğraf tipi**, **mağaza başına 30
dakika**, asgari **4 mağaza / 2 şehir / 2 kanal**.

**En kritik tek tasarım kararı:** *sahada az yaz, çok fotoğrafla.* Etiketin ince
yazısı (KDV satırı, birim fiyat, üstü çizili eski fiyat, "AVANTAJLI FİYAT"
rozeti) sahada okunmaya **çalışılmaz** — fotoğraflanır ve masabaşında okunur.
30 dakikalık bütçe ancak böyle tutar ve `C-551` ancak böyle kapanır.

**Bu turda hiçbir fiyat, SKU, sayım veya kanıt kartı üretilmemiştir.**

---

## 2. BULGULAR

### B-1: `T-917` bir araştırma ticket'ı değil, bir lojistik ticket'ıdır

```yaml
claim:        "T-917'nin kapanmasi icin gereken veri masabasi kanallarda YOKTUR; ticket ajan turuyla ilerletilemez."
value:        "3 tur x 0 sonuc"
status:       FACT
tier:         T4
evidence_id:  [EV-2026-08-10-504, EV-2026-08-10-701, EV-2026-08-09-511, EV-2026-08-09-514]
katman:       n/a
```

**Gerekçe:** Üç bağımsız turda toplam 8 + 8 + 17 = **33 erişim yolu** denenmiş,
kullanılabilir tek yeni kanal çıkmamıştır. Bu bir yöntem hatası değil, pazarın
**yapısal opaklığıdır**: Türkiye'de alkolün fiyat iletişimi kapalıdır.
Dolayısıyla doğru aksiyon, dördüncü bir arama turu değil, **aksiyonu insana
devredilebilir hâle getirmektir.**

### B-2: Tek ziyaret `T-504`'ü ancak asimetrik olarak kapatır

```yaml
claim:        "Raf etiketinde promosyon isareti BULUNURSA T-504 tek ziyarette kapanir; BULUNMAZSA kapanmaz."
status:       FACT   # mantiksal, gozlemsel degil
evidence_id:  [EV-2026-08-09-504, EV-2026-08-10-503]
```

**Gerekçe:** Üstü çizili eski fiyat veya "AVANTAJLI FİYAT" rozeti **pozitif**
kanıttır (`EV-2026-08-09-504` — Metro'nun promosyon etiket anatomisi). Ancak
yokluğu **negatif kanıt değildir**: Metro'nun tarihsel şarap fiyat iletişimi
**dönemseldi** (*"…tarihleri arasında geçerlidir ve stoklarla sınırlıdır"*,
`EV-2026-08-10-503`), yani rozetsiz bir fiyat da geçici olabilir. Bu yüzden
kontrol listesine **2–4 hafta sonra 10 dakikalık ikinci ziyaret** ayrı bir adım
olarak yazılmıştır.

### B-3: Odak bandı 400–800 değil, **400–1.200 TL** olmalıdır

```yaml
claim:        "Hedef merdiven 599-999 TL oldugu icin saha bandi her iki uctan bir basamak tasirilmalidir."
status:       ESTIMATE
evidence_id:  [EV-2026-08-10-702]
katman:       L8
```

**Türetme zinciri:** `EV-2026-08-10-702` gözlenen kanalın **premium'a kayık**
olduğunu gösterdi (471 stokta SKU'nun yalnızca 1'i 600 TL altında; stokta yerli
medyan 1.410 TL). Bandı 800 TL'de kesmek, aynı kayma riskini fiziksel gözlemde
tekrarlar. 1.200 TL üst sınırı, `PREMIUM_EDGE` ve `TOO_HIGH` basamaklarının
(899 / 999) **üstünü** de görmeyi sağlar.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | Benchmark promosyonlu mu | Alkolde masabaşı fiyat izi yok (33 yol) | HIGH | §D + ikinci ziyaret |
| 2 | `L8_CHAIN_RETAIL` | Zincirlerin online kanalında alkol yok | HIGH | §A P0 zincir mağaza |
| 3 | Metro **şarap rafında** KDV gösterimi | Broşürlerde 0 alkol SKU'su | HIGH | §D(b) F2 fotoğrafı |
| 4 | 400–1.200 TL bandında fiziksel ithal SKU sayısı | Tek online kanal, premium kayık | HIGH | §G sayım formu |
| 5 | Gold Country / Central Creek ithalatçısı | Hiçbir kaynakta yok | MEDIUM | §E arka etiket |
| 6 | Tekel bayii fiyat yapısı | Fiyat listesi yayınlanmıyor | MEDIUM | §A P1 |
| 7 | HoReCa fiyat çarpanı | — | MEDIUM | **Bu turun kapsamında değil** — ayrı restoran örneklemi |
| 8 | Benchmark'ın mağazası/şehri | Fotoğraf metaverisi paylaşılmadı | MEDIUM | §B mağaza başlığı |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Durum |
|---|---|
| — | **Bu turda yeni çelişki açılmamıştır.** Gözlem yapılmadığı için çelişecek iki kaynak yoktur. `C-501`, `C-551`, `C-561` **olduğu gibi durmaktadır**; hiçbirine dokunulmamıştır. |

`C-711`…`C-729` bloğu **kullanılmamıştır.**

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| — | — | **YOK** | — | — | — |

**Bu turda `80-model/` altına hiçbir değer önerilmemiştir.** Saha turu
yapılmadan önerilecek sayı yoktur. Turdan sonra dolabilecek alanların listesi:
`saha-kontrol-listesi.md §K`.

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `gumruk-vergi-uzmani` | Saha formunda **ABV** ve **hacim** zorunlu alan yapıldı; benchmark'ın ABV'si bugün `UNKNOWN` | GTİP alt kırılımı için girdi olabilir — **sonucu bu ajan üretmez** |
| `kanal-marj-uzmani` | Tur, `l8_chain_retail`'i **dağılım olarak** doldurmayı hedefliyor; `kanal.yaml → m_retail`'in tepe çapası buradan gelir | Raf fiyatı gözlenir, **marj burada hesaplanmaz (K4)** |
| `mevzuat-ruhsat-uzmani` | Arka etiketten **ithalatçı ünvanı** okunacak (İP-008); etiket zorunlulukları alanı onundur | Etiket mevzuatı doğrulaması |
| `global-sourcing-kasifi` | Arka etiketten **üretici/şişeleyici** de okunacak | Rakip tedarik yapısı ipucu |

> `99-ops/capraz-ipuclari.md`'ye **yazılmamıştır** (bu turda o dosyaya dokunma
> talimatı vardır). Başkan uygun görürse taşınır.

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|---|---|---|---|---|
| `T-917` | turkiye-pazar-kasifi | Fiziksel gözlem paketi | HIGH | **OPEN** → `alt_durum: SAHA_PAKETI_HAZIR__INSAN_AKSIYONU_BEKLIYOR` |

**Yeni ticket açılmamıştır.** `T-711`…`T-729` bloğu kullanılmamıştır — gerekçe:
açılacak her ticket `T-917`'nin kopyası olurdu ve `99-ops/tickets/INDEX.md`
bu turda dokunulmaz listededir.

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| *(yeni kanıt yok)* | — | — |

**Devralınan tazelik riski:** Mevcut **tüm** raf gözlemleri **2026-09-08**'de
STALE olur (`pazar.yaml → tazelik`). Saha turu bu tarihten **sonra** yapılırsa,
turun kendisi bir tazeleme işlevi de görür; **önce** yapılırsa iki gözlem seti
karşılaştırılabilir kalır. **Turu 2026-09-08'den önce yapmak belirgin biçimde
daha değerlidir.**

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

Alkollü içki raf fiyatının masabaşından **erişilebilir** olduğunun gösterilmesi.
Örneğin bir zincirin B2B/kurumsal portalında şarap fiyat listesi, bir Metro
müşteri hesabıyla giriş, ya da bir tekel bayii zincirinin yayınlanmış fiyat
listesi bulunursa, bu belgenin **"bu veri sahada üretilmek zorundadır"**
önermesi çürür ve tur **gereksizleşir** (ya da ucuzlar). 33 yol denendi, ama
denenmemiş yol olmadığı **iddia edilemez**.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"30 dakikada 20 SKU kaydedilebilir."** Bu bir ölçüm değil, bir
`ASSUMPTION`'dır (SKU başına ~45 sn). Elektronik raf etiketi (ESL) parlaması,
kalabalık reyon, mağaza görevlisinin fotoğraf çekimine itirazı veya alkol
reyonunda fotoğraf yasağı bu bütçeyi **2 katına** çıkarabilir. **Mitigasyon:**
öncelik sırası — F0 → sayım → ithal SKU'lar → yerli çapa SKU'lar. Süre yetmezse
**yerli çapalar feda edilir**, sayım ve ithal SKU'lar edilmez.

### 9.3 Hangi kaynağıma en az güveniyorum?

**Metro'nun promosyon etiket anatomisi (`EV-2026-08-09-504`).** Bu, gıda dışı
kategorilerin **broşüründen** çıkarılmıştır; şarap rafındaki **fiziksel** etiket
mizanpajının aynı olduğu **doğrulanmamıştır**. §D'deki şema bu yüzden bir
"beklenti"dir; sahada başka bir mizanpaj görülürse **şema değil, gözlem
geçerlidir** ve form serbest metinle doldurulur.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

Doğrudan bir yatırım kararı değişmez — bu bir **araçtır**. Ancak yanlışsa
(yani veri masabaşından alınabiliyorsa) `G3` gate'inin önündeki engel
**fiziksel değil metodolojik** demektir ve karar **daha erken** verilebilirdi.
Tersine, tur **yapılmaz** ise `OQ-001` `PARTIALLY_RESOLVED`, `T-504`/`T-701`
`OPEN` kalır ve `G3` **kapalı** kalmaya devam eder.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

**Kim:** kurucu veya bir kişi (uzmanlık gerekmez).
**Nasıl:** Şehir 1'de 4 mağaza (Metro + Migros/Macrocenter + CarrefourSA +
tekel bayii) × 30 dk ≈ **yarım gün**; Şehir 2'de 2 mağaza ≈ **3 saat**;
2–4 hafta sonra **10 dakikalık** ikinci Metro ziyareti.
**Maliyet:** ~600 TL (1–2 şişe + kasa fişi) + yol.
**Ne zaman:** **2026-09-08'den önce** (§8).

---

## 10. ZORUNLU EK — BENCHMARK ŞÜPHESİNE DAİR ÜÇ SORU

### 10.1 Benchmark KDV **hariç** çıkarsa fiyat merdiveni nasıl değişir?

599,90 TL'nin tüketici karşılığı **yukarı** kayar (KDV oranı kadar — oran
`gumruk-vergi-uzmani` alanıdır, burada **hesaplanmamıştır**). Etkisi:
gözlenen ithal giriş noktası yükselir → 799 TL hedefinin benchmark'a göre
"%23–33 üstünde" olma gerilimi **azalır** ve `799 → ATTRACTIVE`
sınıflandırması **güçlenir**; buna karşılık 599 TL basamağının tek dayanağı
olan gözlem **kaybolur** ve 599 `TOO_LOW`'a yaklaşır. Yön **proje lehinedir**
— yani mevcut `KDV_DAHIL` etiketi projeyi kayırmıyor, **sıkıyor**. `C-551`.

### 10.2 Gözlenen SKU'lar promosyonluysa segment resmi nasıl kayar?

Tüm gözlenen bant **yapay olarak aşağı** kaymış demektir. `599,90` ve `649,90`
normal fiyatın altındaysa: (a) "Metro'da 500–700 TL bandında ithal şarap var"
cümlesi **kalıcı bir pazar gerçeği değil, bir kampanya fotoğrafı** olur,
(b) `segment.fiyat_performans_alt_try = 600` ESTIMATE'i yukarı kayar,
(c) 599 basamağı `AGGRESSIVE` → **`TOO_LOW`**'a döner. Saha turunda **sayım
formu** (§G) tam da bunu bağımsız olarak test eder: promosyonlu tek bir SKU
bandı temsil edemez, **bandın tamamının sayımı** edebilir.

### 10.3 Metro cash & carry ile zincir market tüketici fiyatı farkı modeli hangi yönde yanıltır?

**Modeli daha agresif yönde yanıltır.** K3 gereği cash & carry formatı yapısı
gereği zincir perakendeden ucuzdur. Ters model hedefini `L8_METRO_CASH_CARRY`
seviyesine kurarsa, gerçekte olması gerekenden **daha düşük** bir hedef raf
fiyatı → **daha düşük** maksimum EXW/FOB → tedarikçi havuzu gereksiz yere
daralır ve proje **haksız yere ölür**. Ters yön de mümkündür: zincir fiyatı
Metro'nunkinin **çok** üstündeyse ve model bunu hedef alırsa, ürün rafta
**pahalı** kalır. Bu iki hatanın **yönü zıttır ve büyüklüğü bilinmiyor** —
bu yüzden §A'da Metro **ve** zincir aynı turda, **aynı SKU'lar aranarak**
gözlenir. Turun tek en değerli çıktısı budur: **aynı SKU'nun iki kanaldaki
fiyat farkı.**

---

*Bu belge bir öneridir. Karar `yatirim-komitesi-baskani`'nındır.*
