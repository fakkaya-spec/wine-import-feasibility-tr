# SWEET-SPOT ANALİZİ — HANGİ HEDEF RAF FİYATI EKONOMİK OLARAK EN MANTIKLI BAŞLANGIÇ?

```yaml
belge:             sweet-spot-analizi
ajan:              finans-fizibilite
tur:               TUR 2.5 — REVERSE TARGET MODEL §13
tarih:             2026-08-10
durum:             DRAFT                     # APPROVED DEGIL
cikti_etiketi:     MODEL_DERIVED / ONERI     # KARAR DEGIL
karar_iceriyor_mu: false
talep_iddiasi:     YOK                       # elastikiyet kaniti YOKTUR, tahmin EDILMEDI
kaynak_model:      80-model/outputs/reverse-price-model.md
```

> ## ⛔ İKİ SINIR
>
> **1.** Bu belge bir **öneridir, karar değildir.** Nihai karar TUR 6'da
> `yatirim-komitesi-baskani`'na aittir.
> **2.** **TALEP TARAFI HAKKINDA HİÇBİR İDDİA YOKTUR.** *"Tüketici bu fiyatı
> öder / ödemez"* cümlesi bu belgede hiçbir yerde geçmez. Talep elastikiyeti
> için projede **tek bir veri yoktur** (`C-561` tam da bu boşluğun adıdır) ve
> **tahmin edilmemiştir.**

---

## 0. SORUNUN DOĞRU KURULUŞU

> **"En yüksek fiyat en iyisidir" cevabı yanlıştır** ve bu belgenin ilk işi
> onu **modelle çürütmektir** (§1.1).

| # | Eksen | Sahibi | Bölüm |
|---|---|---|---|
| 1 | Vergi yükünün fiyat içindeki payı | finans (türev) | §1.1 |
| 2 | **Sabit maktu ÖTV'nin etkisi** | finans (türev) | §1.2 |
| 3 | Sabit TL maliyet yığınının direnci | finans (türev) | §1.3 |
| 4 | Kanal marjı ve kanal seçimi | kanal-marj | §1.4 |
| 5 | Lojistik | navlun-lojistik | §1.5 |
| 6 | Gümrük vergisi | gümrük-vergi | §1.6 |
| 7 | Satın alma bütçesi / RFQ payı | finans (türev) | §1.7 |
| 8 | Yerli rekabet · ithal fiyat boşluğu · f/p konumu | **türkiye-pazar** (alıntı) | §2 |

---

## 1. EKONOMİK EKSENLER

*(Hepsi: İspanya · CHAIN RETAIL · BASE · 5.000 şişe · `g=0,50` · λ=1 ·
ithalatçı katkı payı 0. TL/şişe. Kaynak: `reverse-price-model.md`.)*

### 1.1 Vergi yükünün fiyat içindeki payı — **neredeyse SABİT**

| Hedef | KDV (perakende) | ÖTV | GV | **Toplam vergi** | **Payı** | `MAX_CIF` | CIF payı |
|---|---|---|---|---|---|---|---|
| 599 | 99,83 | 53,45 | 94,75 | 248,03 | **%41,41** | 189,50 | %31,64 |
| 699 | 116,50 | 53,45 | 115,58 | 285,53 | **%40,85** | 231,16 | %33,07 |
| **799** | 133,17 | 53,45 | 136,42 | 323,03 | **%40,43** | **272,83** | %34,15 |
| 899 | 149,83 | 53,45 | 157,25 | 360,53 | **%40,10** | 314,50 | %34,98 |
| 999 | 166,50 | 53,45 | 178,08 | 398,03 | **%39,84** | 356,16 | %35,65 |

> ### BULGU 1 — MERDİVENİ TIRMANMAK VERGİ YÜKÜNDEN KAÇMAZ
> 599'dan 999'a **%67 fiyat artışı**, toplam vergi payını yalnızca
> **1,57 puan** düşürür (%41,41 → %39,84).
>
> **Neden:** ÖTV sabittir (payı düşer: %8,92 → %5,35) ama **gümrük vergisi
> oransaldır ve CIF ile birlikte büyür** (%15,8 → %17,8). İki etki birbirini
> **neredeyse tam olarak götürür.**
>
> **Sonuç: "yukarı çıkarsak vergi baskısı azalır" argümanı MODELDE
> DOĞRULANMAMIŞTIR.** Sweet-spot vergi ekseninde **çözülemez.**

### 1.2 Sabit maktu ÖTV'nin etkisi — asıl mekanizma

| Hedef | ÖTV / raf fiyatı | ÖTV / `MAX_CIF` | ÖTV=0 olsaydı `MAX_CIF` artışı |
|---|---|---|---|
| 599 | **%8,92** | **%28,21** | +35,63 TL → **+%18,80** |
| 699 | %7,65 | %23,12 | +35,63 TL → **+%15,41** |
| **799** | **%6,69** | **%19,59** | +35,63 TL → **+%13,06** |
| 899 | %5,95 | %17,00 | +35,63 TL → **+%11,33** |
| 999 | %5,35 | %15,01 | +35,63 TL → **+%10,00** |

**ÖTV'nin `MAX_CIF` üzerindeki MUTLAK etkisi her basamakta AYNIDIR
(35,63 TL), oransal etkisi 599'da 999'un neredeyse İKİ KATIDIR.**

**λ şok direnci** (λ = 1,5625 = iki adım × +%25 — `senaryolar.yaml` duyarlılık
noktası, **tahmin değil**; şok = −20,04 TL, her basamakta aynı):

| Hedef | λ şokunun `MAX_CIF`'e oranı |
|---|---|
| 599 | **%10,58** |
| 699 | %8,67 |
| **799** | **%7,34** |
| 899 | %6,37 |
| 999 | %5,63 |

> ### BULGU 2 — MERDİVEN VERGİ VERİMLİLİĞİ DEĞİL, **DAYANIKLILIK** SATIN ALIR
> Yukarı çıkmanın gerçek kazancı vergi payı **değil**, sabit TL şoklarına
> karşı **tampon**dur.

### 1.3 Sabit TL maliyet yığını — **en sert ayrıştırıcı**

5.000 şişe/yıl'da `MAX_CIF`'ten çıkan **sabit TL** kalemleri (hepsi hacme
bölünür ve **hedeften bağımsızdır**):

| Kalem | TRY/şişe | `MAX_CIF` etkisi (`/1,5`) | Kaynak |
|---|---|---|---|
| Ruhsat sabit maliyeti (ilk yıl) — *zaten düşülü* | 30,17 | −20,11 | `EV-2026-08-09-234` |
| **ÖTV λ şoku (1 → 1,5625)** | 30,06 | **−20,04** | senaryo noktası |
| **Kendi dağıtım — 1 kişi tabanı** | 96,51 | **−64,34** | `EV-2026-08-10-621` |
| Listeleme bedeli `f` | **UNKNOWN** | −0,725 × `f` | `T-604` |
| **YIĞIN TOPLAMI** (λ şoku + 1 kişi) | — | **−84,38** | — |

**Yığın uygulandıktan sonra kalan `MAX_CIF`:**

| Hedef | baz | yığın sonrası | **yığının payı** | kalan / litre |
|---|---|---|---|---|
| **599** | 189,50 | **105,12** | **%44,5** | 140,16 |
| 699 | 231,16 | 146,78 | %36,5 | 195,71 |
| **799** | **272,83** | **188,45** | **%30,9** | **251,27** |
| 899 | 314,50 | 230,12 | %26,8 | 306,83 |
| 999 | 356,16 | 271,78 | %23,7 | 362,37 |

> ### BULGU 3 — 599 TL, PİLOT ÖLÇEKTE YAPISAL OLARAK EN KIRILGAN BASAMAKTIR
> 5.000 şişede tek kişilik bir dağıtım ekibi **+** iki adımlık ÖTV artışı,
> 599 TL hedefinin satın alma tavanının **%44,5'ini** siler.
> Aynı yığın 799'da **%30,9**, 999'da **%23,7** yer kaplar.
>
> **Bu, pazar tarafından bağımsız, saf bir maliyet-yapısı sonucudur.**

**Marjinal satın alma gücü** (her +100 TL raf fiyatı = **+41,67 TL** `MAX_CIF`,
doğrusal — ama oransal getiri azalır):

| Basamak geçişi | `MAX_CIF` artışı | **oransal** |
|---|---|---|
| 599 → 699 | +41,67 | **+%21,99** |
| 699 → 799 | +41,67 | **+%18,03** |
| **799 → 899** | +41,67 | **+%15,27** |
| 899 → 999 | +41,67 | **+%13,25** |

> **Azalan getiri eğrisi 799'da düzleşmeye başlar.**

### 1.4 Kanal marjı — merdiven içinde ayrıştırıcı DEĞİL, ama **kanal SEÇİMİ ayrıştırıcı**

Kanal marjı `MAX_CIF`'i büyük ölçüde **oransal** etkiler (599'da −%17,9/+%12,8;
799'da −%16,5/+%11,7) → **basamakları birbirinden ayırmaz.**

**Kanal karşılaştırması (BASE):**

| Hedef | CHAIN | TEKEL | HoReCa (3,0×) | HoReCa (5,0×) |
|---|---|---|---|---|
| 599 | 189,50 | **212,79** | 50,84 | **5,80** |
| 799 | 272,83 | **303,90** | 87,88 | 28,03 |
| 999 | 356,16 | **395,01** | 124,91 | 50,25 |

> ⚠ **TEKEL'in %11–12 üstün görünmesi bir `UNKNOWN`'ın sonucudur:** `d`
> (geri akan bedeller) yalnız zincir için tanımlıdır; tekelde **`UNKNOWN` ve
> 0 alınmıştır.** Farkın **tamamı** buradan gelir.
> **İki kanal arasında ekonomik tercih modelden okunamaz** → `T-856`.

### 1.5 Lojistik — sweet-spot'a **etkisi yok**

Navlun **CIF'in içindedir** → ters modelde tavanı **değiştirmez**
(`reverse-price-model.md` §8.3). TR-içi TRY bacağı 5.000 şişede `MAX_CIF`'i
yalnızca **±0,93 TL** oynatır. **Lojistik bu kararın belirleyicisi değildir.**

### 1.6 Gümrük vergisi — **oransal, ayrıştırıcı DEĞİL**

`g` 0,50 → 0,70 her basamakta **tam %11,765** düşürür. Merdiven içi bir tercih
üretmez; **menşe/belge tercihini** üretir.

### 1.7 Satın alma bütçesi payı — `IMPLIED_BREAKEVEN_USDTRY`

*(fx `null`; bu sütun bir kur tahmini DEĞİLDİR.)*
Gözlenen İspanya CIF birim değeri **2,71 USD/lt** (`EV-2026-08-09-405`, FACT, T3):

| Hedef | `MAX_CIF`/lt (baz) | implied USD/TRY | **yığın sonrası** implied USD/TRY |
|---|---|---|---|
| 599 | 252,67 | 93,2 | **51,7** |
| 699 | 308,21 | 113,7 | 72,2 |
| **799** | **363,77** | **134,2** | **92,7** |
| 899 | 419,33 | 154,7 | 113,2 |
| 999 | 474,88 | 175,2 | 133,7 |

> Bu tablo bir **"pay var" iddiası DEĞİLDİR** — gerçek USD/TRY bu modelde
> `UNKNOWN`'dır (`T-912`, `T-852`). Söylediği tek şey: **merdivenin üst
> basamakları, aynı gözlenen CIF için kur şokuna karşı ~2,6 kat daha geniş
> bir bant taşır** (599 → 51,7 vs 999 → 133,7).

---

## 2. PAZAR TARAFI — **ALINTIDIR, BENİM BULGUM DEĞİLDİR**

`60-pazar/target-shelf-price-analysis.md` (`turkiye-pazar-kasifi`, TUR 2.5):

| Hedef | Sınıflandırma | Confidence | Stokta yerli (±%10) | Stokta ithal (±%10) |
|---|---|---|---|---|
| 599 | `AGGRESSIVE` | **LOW** | 3 | 0 |
| 699 | `ATTRACTIVE` | MEDIUM | 17 | 0 |
| **799** | `ATTRACTIVE` | MEDIUM | **31** | 1 *(875, pencere ucu)* |
| 899 | `PREMIUM_EDGE` | MEDIUM | 35 | **2** (875/948) |
| 999 | `TOO_HIGH` *(f/p mandası için)* | **LOW** | 49 | 1 |

**Bağlayıcı nitelemeler (aynen taşınır):**
- `L8_CHAIN_RETAIL` katmanında **SIFIR gözlem** vardır (`T-701`, `T-603`).
- Yoğunluk eğrisinin tamamı **tek kanaldan** okunmuştur ve o kanal
  **premium'a kayıktır** (471 stokta SKU'nun **1'i** 600 TL altında).
- `599` sınıflandırması **tek SKU'nun tek gözlemine** asılıdır ve o gözlemin
  promosyon durumu **`UNKNOWN`**'dır (`T-504`, **CRITICAL**).
- `999`'un `TOO_HIGH` gerekçesi olan 900 TL tavanı bir **`ESTIMATE`**'tir.

> ⛔ **`OBSERVED_BENCHMARK` (599,90 / 649,90) ile `TARGET_SHELF_PRICE` (599)
> bu belgede hiçbir yerde birleştirilmemiştir** (`K7`, `L2`). Aradaki
> 0,90 TL yakınlık **bir teyit değil, bir tesadüftür.**

---

## 3. ÖNERİ

> **BUNLAR ÖNERİDİR, KARAR DEĞİLDİR.**

### 3.1 `PRIMARY` — **799 TL** (KDV dahil, 750 ml still wine)

```yaml
oneri:        PRIMARY
deger:        799
kdv:          DAHIL
katman:       L8_CONSUMER_SHELF_PRICE (HEDEF — hangi L8 alt katmani UNKNOWN, T-859)
etiket:       TARGET_SHELF_PRICE / INVESTOR_TARGET_SCENARIO
confidence:   LOW-MEDIUM
max_cif_try_upper_bound:
  ES/PT/IT/FR/CL DOC_OK  : 272,83   (CHAIN, BASE, 5.000 sise, katki 0)
  DOC_FAIL / ZA-AU-US-MD : 240,73
```

**Ekonomik gerekçe (bu ajanın kendi türetmesi):**
1. **Sabit TL yığınının payı burada ilk kez %31'in altına iner** (%30,9) —
   599'da %44,5, 699'da %36,5. Pilot ölçekte (5.000 şişe) **yapısal
   dayanıklılığın eşiğidir** (§1.3).
2. **ÖTV λ şokuna direnç %7,34**'tür; 599'da %10,58. İki adımlık bir ÖTV
   artışı 799'u **sarsar ama devirmez.**
3. Vergi payı ekseni **ayrıştırıcı değildir** (§1.1) → yukarı çıkmanın tek
   ekonomik gerekçesi **dayanıklılıktır** ve dayanıklılık kazancının
   **marjinal getirisi 799'dan sonra %15'in altına iner** (§1.3).
4. Pazar tarafı (**alıntı**) 799'u `ATTRACTIVE` ve **whitespace içindeki en
   yoğun basamak** olarak işaretlemiştir (31 yerli rakip, 0 stokta ithal).

**Bilinen zayıflığı — açıkça:**
- Ekonomik gerekçem ile pazar gerekçesi **aynı sonuca varıyor ama bu bir
  doğrulama DEĞİLDİR**: ikisi de kısmen aynı zayıf tabana (`segment` bandı
  600–900, tek kanal `ESTIMATE`, `C-501` açık) dayanmaktadır.
- `T-504` *"normal fiyat"* diye kapanırsa 799, gözlenen tek ithal giriş
  fiyatının **%33 üstünde** kalır ve `PREMIUM_EDGE`'e kayar → o durumda
  **SECONDARY ile yer değiştirmelidir.**

### 3.2 `SECONDARY` — **699 TL**

```yaml
oneri:        SECONDARY
deger:        699
confidence:   LOW-MEDIUM
max_cif_try_upper_bound: 231,16 (DOC_OK) / 203,97 (DOC_FAIL)
```

- **Fiyat/performans mandasına en sadık** basamak (CLAUDE.md §0).
- **Marjinal satın alma gücü artışının en yüksek olduğu geçiştir**
  (599 → 699: **+%21,99**) — *"bir basamak yukarı çıkmanın en kârlı olduğu yer."*
- **Neden PRIMARY değil:** 5.000 şişelik pilotta sabit TL yığını tavanın
  **%36,5'ini** siler ve kalan tavan **146,78 TL/şişe**'ye iner — 799'un
  taşıdığı bandın **%78'i**.

### 3.3 `STRETCH` — **899 TL**

```yaml
oneri:        STRETCH
deger:        899
confidence:   LOW
max_cif_try_upper_bound: 314,50 (DOC_OK) / 277,50 (DOC_FAIL)
```

- Ekonomik olarak **en dayanıklı savunulabilir** basamaktır (yığın payı %26,8).
- **Bedeli (alıntı):** whitespace **kaybolur** (2 stokta ithal rakip: 875/948)
  ve projenin kendi `segment` tavanına (900 `ESTIMATE`) **değer**.
- Marjinal kazanç 799'a göre yalnızca **+%15,27** — **azalan getiri bölgesi.**

### 3.4 **599 TL — `FLOOR / DOWNSIDE`, `PRIMARY` ADAYI DEĞİLDİR**

**Bir "daha ambisiyöz hedef" değil, bir DAYANIKLILIK TESTİDİR.**

| Neden | Kanıt |
|---|---|
| Sabit TL yığını tavanın **%44,5'ini** siler (5.000 şişe) | §1.3 |
| ÖTV λ şokuna direnç en zayıf (**%10,58**) | §1.2 |
| Yapısal tabana (144,21 TL) uzaklık **4,15×** — 799'da **5,54×** | `reverse-price-model.md` §6.4 |
| Pazar sınıflandırması `AGGRESSIVE` · confidence **LOW** · tek gözleme asılı | §2 |
| Tek dayanağı olan gözlemin **promosyon durumu `UNKNOWN`** | `T-504` **CRITICAL** |

> **Koşullu kullanım kuralı:** 599 TL yalnızca bir **downside senaryosu**
> olarak çalıştırılır; base case'e alınmaz. Alınacaksa iki koşul rapora
> yazılmak zorundadır: (a) `T-504` kapanmadan 599 bir "pazar fiyatı" gibi
> kullanılamaz, (b) `K3` gereği zincir perakende L8'inde 599 TL, Metro'da
> 599,90 görmekten **daha zordur**.

### 3.5 **999 TL — `OUT OF MANDATE`**

Ekonomik olarak **en dayanıklı** basamaktır (yığın payı %23,7) — ve bu tam da
neden dikkatli olunması gerektiğini gösterir: **model, mandayı ihlal etme
yönünde bir teşvik üretir.**
`CLAUDE.md §0` projeyi **fiyat/performans segmenti** olarak tanımlar;
`pazar.yaml → segment.fiyat_performans_ust_try = 900` (`ESTIMATE`) aşılır.

> **`999`'u ekonomik gerekçeyle önermek, mandayı model çıktısıyla
> değiştirmek olurdu. Bu bir başkan kararıdır, model kararı değildir.**
> Model yalnızca şunu kayda geçirir: *"merdivenin ekonomik olarak en
> dayanıklı basamağı, projenin kendi tanımladığı segmentin dışındadır."*
> → **`T-857`**

---

## 4. ÖZET

| Hedef | Öneri | Yığın payı | λ direnci | `MAX_CIF` (ES, DOC_OK) | Pazar (alıntı) | Confidence |
|---|---|---|---|---|---|---|
| **599** | `FLOOR / DOWNSIDE` | %44,5 | %10,58 | 189,50 | `AGGRESSIVE` LOW | **LOW** |
| **699** | **`SECONDARY`** | %36,5 | %8,67 | 231,16 | `ATTRACTIVE` MED | LOW-MEDIUM |
| **799** | **`PRIMARY`** | **%30,9** | **%7,34** | **272,83** | `ATTRACTIVE` MED | **LOW-MEDIUM** |
| **899** | **`STRETCH`** | %26,8 | %6,37 | 314,50 | `PREMIUM_EDGE` MED | LOW |
| **999** | `OUT OF MANDATE` | %23,7 | %5,63 | 356,16 | `TOO_HIGH` LOW | LOW |

**Genel confidence: `LOW-MEDIUM`.**
- **Göreli sıralama** (hangi basamak diğerinden daha dayanıklı): **MEDIUM** —
  saf aritmetiktir, yalnızca sabit/değişken maliyet ayrımına dayanır.
- **Mutlak çıpalama** (799 TL Türkiye rafında doğru fiyat mıdır): **LOW** —
  `L8_CHAIN_RETAIL` **hiç gözlenmemiştir** ve talep verisi **yoktur**.

> **Tek cümleyle:** Model, **hangi basamağın hangisine göre daha dayanıklı
> olduğunu** makul bir aritmetikle söyleyebilir; **hedef fiyatın Türkiye
> tüketici rafında doğru olduğunu söyleyemez.**

---

## 5. BU ÖNERİYİ NE ÇÜRÜTÜR?

| # | Bulgu | Sonuç |
|---|---|---|
| 1 | **`T-504` "promosyonlu" çıkarsa** | 599 `TOO_LOW`'a düşer; `FLOOR` senaryosu **anlamsızlaşır**; 799 ve 899 göreli olarak güçlenir |
| 2 | **`T-504` "normal fiyat" çıkarsa** | 599,90 kalıcı bir ithal giriş fiyatıdır; 799 onun **%33 üstündedir** → `PRIMARY` **699'a kayar** |
| 3 | **`C-561` "bantta ürün var ama dönmüyor" yönünde çözülürse** | Whitespace argümanı çöker; ithal şarabın **fiilen döndüğü** tek bölge 875 TL üstüdür → **899/999 lehine kayar** |
| 4 | **`segment.fiyat_performans_ust_try` revize edilirse** | 999 `OUT OF MANDATE` olmaktan çıkar; ekonomik olarak **en dayanıklı basamak base case adayı olur** (`T-857`) |
| 5 | **`OQ-901` yüksek bir minimum katkı payı belirlerse** | Alt basamaklar (599, 699) **matematiksel olarak elenebilir**: %30 katkıda 599'un tavanı **108,11 TL/şişe**'ye iner |
| 6 | **Kendi dağıtım kararı verilirse (`MODEL B`)** | 5.000 şişede tek kişi bile 599'un tavanının **%34'ünü** siler → pilot ölçekte 599 **fiilen kapanır** |
| 7 | **KDV indirim hakkı alkolde kısıtlanmışsa** (`T-151`, `OQ-G10`) | Tüm tavanlar **~%22,7 düşer**; sıralama korunur ama **seviye çöker** — bu belgenin **tüm sayıları yeniden hesaplanmalıdır** |

> **En sinsi olan #7'dir:** menşe ve basamak **karşılaştırmasını bozmaz**,
> yalnızca **seviyeyi** bozar — yani bu belgedeki sıralama doğru kalır ve
> hata **fark edilmez.**
