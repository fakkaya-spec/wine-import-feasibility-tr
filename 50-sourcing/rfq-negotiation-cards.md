# RFQ NEGOTIATION CARDS — TOP 10 TEDARİKÇİ

```yaml
belge:                 rfq-negotiation-cards
sahibi:                global-sourcing-kasifi
tur:                   TUR 2.5 — RFQ NEGOTIATION CARDS
tarih:                 2026-08-10
girdi_listesi:         50-sourcing/top-10-rfq-targets.md (10 hedef)
fiyat_capasi:          80-model/outputs/reverse-price-model.md (DRAFT) +
                       80-model/outputs/country-buying-ceilings.csv (2.700 satir)
hedef_secimi:          80-model/outputs/sweet-spot-analizi.md (ONERI — KARAR DEGIL)
mense_capasi:          30-vergi-gumruk/mense-tarife-eslemesi.md
yeni_tedarikci_arama:  YOK — bu turda yeni supplier/ulke/fiyat arastirmasi YAPILMADI
web_arama:             YOK
dis_iletisim:          NONE — hicbir ureticiye e-posta/form/mesaj GONDERILMEDI
yeni_evidence:         YOK — 10-evidence/ dokunulmadi
kart_sayisi:           10
```

---

> ## ⛔ 1. UYARI — BU BELGEDEKİ HİÇBİR TL RAKAMI BİR FİYAT DEĞİLDİR
>
> Kartlardaki **`MAXIMUM STRUCTURAL BUY PRICE`**, **`RFQ TARGET CEILING (X/Y)`**
> ve **`IMPLIED_BREAKEVEN_USDTRY`** değerlerinin **tamamı**
> `finans-fizibilite`'nin ters modelinden gelir ve etiketleri:
>
> ### `TARGET` / `MODEL_DERIVED` / `UPPER_BOUND`
>
> **`FACT` DEĞİLDİR. `QUOTE` DEĞİLDİR. Bir tedarikçi teklifi DEĞİLDİR.**
> Hepsi bir **yatırımcı hedef raf fiyatından (`INVESTOR_ASSUMPTION`)** geriye
> doğru türetilmiştir ve **iki bağımsız nedenle üst sınırdır**
> (λ=1 çapası + 13 maliyet kaleminin `0` alınması — `reverse-price-model.md` §3.4).
> Kaynak model **`DRAFT`**'tır, `APPROVED` değildir.

> ## ⛔ 2. UYARI — `TARGET` / `ACCEPTABLE` / `WALK-AWAY` FİYATI ÜRETİLMEMİŞTİR
>
> Bu üç seviye bir **yatırımcı eşiği** gerektirir. `OQ-901` **CRITICAL ve
> açıktır** (`T-851`). Kartlarda bu üç alan **keyfî yüzdelerle doldurulmamıştır**;
> `INVESTOR_DECISION_REQUIRED` olarak bırakılmıştır.
> **Üretilen tek nesne `MAXIMUM STRUCTURAL BUY PRICE`'tır.**
> `finans-fizibilite` bu disiplini uyguladı; bu belge onu **birebir korur**.

> ## ⛔ 3. UYARI — BU TURDA HİÇBİR ÜRETİCİYE TEMAS EDİLMEDİ
>
> Kartlar bir **hazırlıktır**. Gönderim koşulu `rfq-contact-pack.md` §4'te
> tanımlıdır: karar `TEST`/`IMPORT PILOT` **ve** başkan onayı **ve**
> `T-401`/`T-462` kapalı **ve** `<VOLUME>` doldurulmuş.

---

## 0. ORTAK ÇAPA SETİ — 10 KARTIN TAMAMI İÇİN AYNI

`rfq-template.md` §0.8 bağlayıcıdır: **aynı metin herkese gider**, yoksa
teklifler karşılaştırılamaz. Aynı kural pazarlık çapası için de geçerlidir —
**10 kartın hepsi aynı hedef fiyattan, aynı kanaldan ve aynı hacim köşelerinden
türetilmiştir.** Kartlar arasında farklılaşan **tek yapısal değişken menşe
tarifesidir** (§0.3).

### 0.1 Hedef ve kanal — `ÖNERİ`, karar değil

| Alan | Değer | Statü | Kaynak |
|---|---|---|---|
| `TARGET SHELF PRICE` (PRIMARY) | **799 TRY** · KDV **dahil** · 750 ml still | `INVESTOR_ASSUMPTION` / `TARGET_SHELF_PRICE` | `sweet-spot-analizi.md` §3.1 (**ÖNERİ**) |
| `TARGET SHELF PRICE` (SECONDARY) | 699 TRY | aynı | `sweet-spot-analizi.md` §3.2 |
| `TARGET SHELF PRICE` (STRETCH) | 899 TRY | aynı | `sweet-spot-analizi.md` §3.3 |
| `TARGET CHANNEL` | **CHAIN RETAIL** (`L8_CHAIN_RETAIL`) | `ASSUMPTION` | `reverse-price-model.md` §5 |
| `TARGET CHANNEL` (alternatif) | INDEPENDENT / TEKEL | `ASSUMPTION` — ⚠ **model bu kanalı yapay olarak iyi gösterir** (`T-856`) | aynı |

> ⚠ **`L8_CHAIN_RETAIL` katmanında Türkiye'de SIFIR gözlem vardır**
> (`target-shelf-price-analysis.md`, `T-701`, `T-603`). Yani pazarlık
> çapamızın dayandığı raf katmanı **hiç ölçülmemiştir.** Bu, kartların
> **en zayıf tek noktasıdır** ve her karta ayrıca yazılmamıştır çünkü
> **10 kartın 10'unda da aynıdır.**
>
> ⚠ Hangi hedef basamağın ve hangi kanalın RFQ çapası olacağı **başkan
> kararıdır** → **`T-871`**. Kartlar 799/CHAIN üzerinden yazılmıştır çünkü
> `sweet-spot-analizi.md` `PRIMARY` olarak onu **önermiştir**; bu bir seçim
> değil, mevcut tek türetilmiş öneriye bağlanmadır.

### 0.2 Hacim köşeleri

| Köşe | Tanım | Hacim |
|---|---|---|
| **X** — kötümser | SCENARIO `HIGH` (m=%35, d=%18, lojistik HIGH) + **DOC_FAIL** | **5.000 şişe** |
| **Y** — BASE | SCENARIO `BASE` (m=%25, d=%8, lojistik BASE) + **DOC_OK** | **25.000 şişe** |

**Okuma kuralı (`reverse-price-model.md` §10.1):**
`CIF ≤ X` → güçlü aday · `X < CIF ≤ Y` → inceleme · `CIF > Y` → mevcut modelde zor.

> **X tüm ülkelerde aynıdır (200,98 TRY/şişe)** çünkü kötümser köşede tercihli
> menşeler de %70'e düşer. Menşe farkı **yalnızca Y köşesinde** görünür.

### 0.3 MENŞE ETKİSİ — **9 ÜLKE İÇİN 9 SAYI YOKTUR, 2 SAYI VARDIR**

`reverse-price-model.md` §4.2: menşe `MAX_CIF_TRY`'yi **yalnızca `(1+g)` böleni
üzerinden** etkiler; ÖTV ve KDV menşeden bağımsızdır.

```
MAX_CIF(g=0,70) / MAX_CIF(g=0,50) = 1,50 / 1,70 = 0,88235
```

> **Tercihli rejimi kaybetmek azami alım fiyatını TAM %11,765 düşürür** —
> hedef fiyattan, ÖTV'den, marjdan, hacimden ve navlundan **bağımsız olarak.**
> Bu, modelin **hiçbir `UNKNOWN`'a bağlı olmayan tek sayısıdır.**

**Bu nedenle kartlarda ülkeye özgü sahte hassasiyet üretilmemiştir.** Ülke
satırları yalnızca **iki gruba** ayrılır:

| Grup | Ülkeler (kartlarda geçen) | `g` | Koşul |
|---|---|---|---|
| **P — tercihli, KOŞULLU** | ES · PT · IT · FR (1/98 AB tarım rejimi) · **CL** (TR-Şili STA) | **%50** | **belge + doğrudan nakliyat** sağlanırsa; sağlanmazsa **otomatik %70** |
| **N — tercihsiz** | **AU** · **MD** | **%70** | koşulsuz — düşecek bir tercih yok |

Kaynak: `mense-tarife-eslemesi.md` §1, §3.1 (`EV-2026-08-09-103/-104/-105`,
`EV-2026-08-10-165`) — **`gumruk-vergi-uzmani`'nın alanıdır; burada yalnızca
alıntılanmıştır.**

### 0.4 ÇAPA TABLOSU — 799 TL · CHAIN RETAIL · TRY/şişe

| Alan | **Grup P** (DOC_OK) | **Grup N** + her DOC_FAIL |
|---|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** *(BASE · 5.000 şişe · λ=1 · katkı payı 0)* | **272,83** | **240,73** |
| aynı, litre başına | 363,77 | 320,98 |
| **`RFQ TARGET CEILING X`** *(HIGH · DOC_FAIL · 5.000)* | **200,98** | **200,98** |
| **`RFQ TARGET CEILING Y`** *(BASE · DOC_OK · 25.000)* | **290,51** | **256,34** |
| Tercih kaybının bedeli | **−32,10 TRY/şişe** (−%11,765) | — (zaten kayıp) |

Diğer basamaklar (CHAIN · BASE · 5.000 · P/N):
**699 → 231,16 / 203,97** · **899 → 314,50 / 277,50**
X/Y: **699 → 169,12 / 248,85 · 219,57** — **899 → 232,84 / 332,18 · 293,10**

Alternatif kanal (INDEPENDENT/TEKEL · 799 · BASE · 5.000): **303,90 / 268,15**
— ⚠ farkın **tamamı** `d`'nin tekelde `0` alınmasından gelir (`T-856`).

### 0.5 FX BOŞLUĞU — KARTLARDA GİZLENMEMİŞTİR

> ### ÜRETİCİYLE EUR/USD KONUŞULACAK; BİZİM TAVANIMIZ TL CİNSİNDEN
>
> `MAX_CIF_TRY` **hesaplanmıştır.**
> **`MAX_FOB` ve `MAX_EXW` — hangi para biriminde olursa olsun — `UNKNOWN`'dır.**
>
> Neden: navlun **USD**, menşe local charge **EUR** cinsindendir ve
> `senaryolar.yaml → duyarlilik_eksenleri[FX]` **min/base/max hepsi `null`**'dır
> (`T-912`, `T-852`). `country-buying-ceilings.csv`'nin
> `MAX_FOB_TRY`, `MAX_EXW_TRY`, `MAX_FOB_EUR_USD`, `MAX_EXW_EUR_USD`
> sütunlarının **2.700 satırının 2.700'ü `UNKNOWN`**'dır.
>
> **Sonuç — pazarlık masasında ne olur:**
> Tedarikçi bize **EXW EUR/şişe** veya **FOB USD/şişe** verecektir.
> Biz o sayıyı bugün **kabul edilebilir mi değil mi diye ölçemeyiz**, çünkü
> (a) tavanımız TL'dir, (b) FOB→CIF köprüsü için navlun USD'dir ve kur yoktur.
> **Bu bir eksik araştırma değil, tek bir tarihli kur kaydının yokluğudur.**
> Kur girildiği **an** `MAX_FOB_FX = MAX_CIF_TRY/fx − navlun_USD/şişe` **tek
> adımda** açılır; navlun USD/şişe **9 rotanın 9'unda zaten elimizdedir**
> (`EV-2026-08-10-301…-311`).
>
> **Bu boşluk kapanana kadar hiçbir tedarikçi teklifi için `VIABLE` /
> `NOT VIABLE` denemez.**

**FX'siz pazarlık çapası:** `IMPLIED_BREAKEVEN_USDTRY` — *"Türkiye'nin o
menşeden fiilen ithal ettiği ortalama CIF birim değeri (`EV-2026-08-09-405`,
FACT, T3) modelin Y tavanına tam otursa USD/TRY kaç olurdu?"*
**Bu bir kur tahmini DEĞİLDİR.** Yalnızca ülkeler arası **nefes payını**
fx olmadan sıralar.

### 0.6 MENŞE BELGESİ — HER KARTTA BİR **PAZARLIK KALEMİ**

`mense-tarife-eslemesi.md` §5: *"Tarife menşe seviyesindedir. Ancak K3 (geçerli
belge) ve K2 (menşe kuralı) **tedarikçiye bağlıdır.**"*
Yani **tarife oranı pazarlık konusu değildir — belgenin düzenlenebilirliği
pazarlık konusudur.** Kartlarda bu, dört maddelik **standart bir sözleşme
kalemi** olarak yer alır (Grup P) veya **açıkça yoktur** (Grup N):

**`ORIGIN DOCUMENT COMMITMENT` — Grup P standart metni (talep edilecek):**

| # | Talep | Neden | Karşılığı |
|---|---|---|---|
| **OD-1** | İhracatçı, her sevkiyat için **EUR.1** düzenlemeyi **veya** geçerli **fatura beyanı** yapmayı sözleşmeyle taahhüt eder | Belge yoksa %50 → %70 | **−32,10 TRY/şişe** (799/CHAIN/BASE/5k) |
| **OD-2** | "Onaylanmış ihracatçı" statüsü var mı; fatura beyanının **değer eşiği** aşılıyorsa EUR.1'e geçilir | Fatura beyanı eşiği **`UNKNOWN`** (`T-162`) | belge reddi riski |
| **OD-3** | Şarap **tamamen menşe ülkede** üretildi ve şişelendi mi; **dökme ithal bileşen** var mı | Dökme ithal şarabın başka ülkede şişelenmesi **K2'yi bozar** — **private label'da yüksek risk** | tercih tamamen düşer |
| **OD-4** | Sevkiyat **hangi limandan çıkacak** — çıkış ülkesi kontrolü (BİLGE) | AB rejimi için AB/EFTA vb. liste; **Şili için yalnızca Şili** | tercih düşer |
| **OD-5** | Belge düzenlenemez/reddedilirse **fiyat düzeltme (price adjustment) maddesi** | Riski tedarikçiyle paylaşır | pazarlık kaldıracı |

> **OD-5 bu belgenin tek gerçek "yeni" pazarlık fikridir ve bir mevzuat iddiası
> değildir:** tercih kaybının bedeli (%11,765) **hesaplanabilir ve tek yönlü**
> olduğu için, sözleşmeye **koşullu fiyat maddesi** olarak yazılabilir.
> Maddenin hukuki geçerliliği ve gümrük tarafındaki sonucu
> **`gumruk-vergi-uzmani`'nın alanıdır** → **`T-872`**.

**Grup N (AU · MD) için:** tercihli belge **düzenlenemez** — bu bir tedarikçi
kusuru değil, **yapısal durumdur.** Kartlarda tek talep şudur: *tedarikçi
"belgeleri biz hallederiz" gerekçesiyle **prim isteyemez**, çünkü düzenlenecek
tercihli belge yoktur.* Tercihsiz menşe şahadetnamesinin **zorunlu olup
olmadığı `UNKNOWN`**'dır (`T-162`) ve **oranı değiştirmez.**

### 0.7 KARTLARDA KULLANILAN ETİKETLER

| Etiket | Anlamı |
|---|---|
| `PUBLIC_INDICATIVE` | Üreticinin kendi kamuya açık kanalında yayınladığı gösterge fiyat — **teklif değildir** |
| `NONE` | Hiçbir fiyat yayınlanmamış |
| `FIRM_OFFER` | Alınmış, tarihli, geçerlilik süresi olan gerçek teklif — **havuzda 0 adet** |
| `TARGET / MODEL_DERIVED` | Ters modelden gelen tavan |
| `INVESTOR_DECISION_REQUIRED` | Yatırımcı eşiği olmadan üretilemez |

---
---

# KART 1 — HARLAND WINE COMPANY PTY LTD

| Alan | Değer |
|---|---|
| **Supplier** | Harland Wine Company Pty Ltd (`SUP-451`) |
| **Country** | **Avustralya** — South Eastern Australia / Langhorne Creek / Barossa / McLaren Vale |
| **Business model** | **Model B — Private label** |
| **Target product** | 750 ml still **beyaz**, entry kademe (üretici "Entry Level" kademesini adıyla yayınlıyor) |
| **MOQ (bilinen)** | **6.000 şişe / şarap** (500×12×750 ml veya 1000×6×750 ml) — `EV-2026-08-10-452`, `FACT` |
| **Target shelf price** | 799 TRY (KDV dahil) · alt/üst: 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **N — tercihsiz (%70)** · `mense-tarife-eslemesi.md` §1.1 |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **240,73** *(799·CHAIN·BASE·5.000·λ=1·katkı 0)* |
| `RFQ TARGET CEILING X` | **200,98** |
| `RFQ TARGET CEILING Y` | **256,34** |
| 699 / 899 karşılıkları | 203,97 / 277,50 |
| `MAX_FOB` (TRY veya USD/EUR) | **`UNKNOWN`** — fx `null` (`T-912`, `T-852`) |
| `MAX_EXW` (TRY veya USD/EUR) | **`UNKNOWN`** — aynı |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **46,63** ⚠ `TEMSİLİ DEĞİL` (AU→TR hacmi <100 bin lt) |
| `TARGET_DISCOUNT_FROM_MAX` | **`INVESTOR_DECISION_REQUIRED`** (`OQ-901`, `T-851`) |
| `REQUIRED_IMPORTER_MARGIN` | **`INVESTOR_DECISION_REQUIRED`** |
| `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | "Entry Level **$2.85+** per bottle" · Mid $5.00+ · Premium $8.50+ — `EV-2026-08-10-451` |
| **Quote class** | **`PUBLIC_INDICATIVE`** — kamuya açık gösterge; **teklif değildir** |
| **Para birimi** | **`UNKNOWN`** — kaynakta yalnızca `$`; AUD mı USD mi **doğrulanmadı** |
| **Katman (Incoterm)** | **BELİRSİZ** — tam konteynerde **FOB (L1)**, MOQ siparişinde **ex factory (L0)**; **aynı sayı iki katmana işaret ediyor** → `C-461` |
| Kapsam | **Etiket baskısı fiyata DAHİL DEĞİL**; koli ("Dry Goods") dahil |

> ⛔ **Bu sayı ters model tavanıyla KARŞILAŞTIRILAMAZ.** Üç bağımsız engel:
> para birimi `UNKNOWN`, katman (L0/L1) `UNKNOWN`, ve tavanımız TL — kur yok.
> **"2,85 < 240,73" cümlesi kurulamaz ve bu belgede hiçbir yerde kurulmamıştır.**

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **FOB, adı belirtilen liman** (birincil) + **EXW, adı belirtilen tesis** (ikincil) — **ikisi ayrı ayrı** |
| **Target MOQ** | **≤5.000 şişe/SKU** — mevcut 6.000, pilot bandının **üstünde** (`C-462`). İkinci kademe **25.000** (Y köşesi) |
| **Required payment term** | Mevcut beyan: **%50 peşin + %50 şişeleme sonrası, tamamı sevkiyat öncesi** (`EV-2026-08-10-452`). **Hem peşin hem vadeli için AYRI fiyat** istenir |
| **Required lead time** | Beyan: 4–5 hafta şişeleme + 1 hafta paketleme (~6 hafta) + navlun. **Sözleşmede taahhüt edilmesi** istenir |
| **Origin document** | **Grup N** — tercihli belge **düzenlenemez**; belge gerekçesiyle **prim kabul edilmez** |

### Critical unknowns

1. **Para birimi (AUD/USD)** — tek başına fiyatı ~1,5 kat değiştirir.
2. **L0 mu L1 mi** — `C-461` açık; katman karışırsa tüm zincir bozulur.
3. **Etiket baskısı tek seferlik (klişe) + tekrarlayan maliyeti** — L0'ın gerçek kapsamı.
4. **Beyaz portföy** — kademe adları biliniyor, **çeşit/ABV bilinmiyor**.
5. **AU→TR hattı fiilen yok** (44.674 lt/2025) — navlun/transit **`UNKNOWN`** (`T-304`).
6. **`IMPLIED_BREAKEVEN` temsili değil** — AU sıralamada kullanılamaz.

### 3 NEGOTIATION QUESTION

1. **"Yayınladığınız 2,85 gösterge fiyatını, para birimini ve Incoterm'ini
   açıkça yazarak 5.000 / 6.000 / 25.000 şişe için teyit eder misiniz — ve aynı
   ürün için EXW `<tesis>` ile FOB `<liman>` fiyatını AYRI AYRI verir misiniz?"**
   *(Tek soruda `C-461` + para birimi + hacim kademesi kapanır.)*
2. **"6.000 şişelik MOQ'yu 5.000'e indirmenin bedeli nedir — şişe başına kaç
   birim fiyat farkı, yoksa kesin bir hayır mı?"**
   *(MOQ bir firma özelliğidir, sektör özelliği değildir; fiyatlanabilirliği
   ölçülmemiştir.)*
3. **"Ödemenin tamamı sevkiyat öncesi isteniyor; sevkiyat sonrası 60/90 gün
   vadeli bir yapı mümkün mü ve mümkünse şişe başına fiyat farkı nedir?"**
   *(Vadenin Türkiye tarafındaki vergi sonucu `gumruk-vergi-uzmani` alanıdır —
   biz yalnızca **fiyat farkını** soruyoruz.)*

---

# KART 2 — CANTINA DANESE S.R.L. UNIPERSONALE

| Alan | Değer |
|---|---|
| **Supplier** | Cantina Danese s.r.l. Unipersonale (`SUP-452`) |
| **Country** | **İtalya** — Roncà (VR), Veneto |
| **Business model** | **Model B — Private label** |
| **Target product** | 750 ml still **kuru beyaz**, value kademe (Trebbiano / Garganega / Pinot Grigio / Chardonnay adayları — **doğrulanmadı**) |
| **MOQ (bilinen)** | **6.000 şişe / tek referans (SKU)** — `EV-2026-08-10-453`, `FACT` |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **P — tercihli KOŞULLU (%50)** · 1/98 AB tarım rejimi · **A.TR GEÇERSİZ** |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **272,83** (DOC_OK) · **240,73** (DOC_FAIL) |
| `RFQ TARGET CEILING X` | **200,98** |
| `RFQ TARGET CEILING Y` | **290,51** (DOC_OK) · 256,34 (DOC_FAIL) |
| 699 / 899 karşılıkları | 231,16 / 314,50 (DOC_OK) |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **106,12** (DOC_OK) · **93,64** (DOC_FAIL) |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** — sitede hiçbir fiyat yayınlanmamış |

### ⚠ MÜNHASIRLIK / KANAL ÇAKIŞMASI RİSKİ — BU KARTIN AYIRT EDİCİ MADDESİ

> **Cantina Danese Türkiye'de KENDİ MARKASIYLA listelidir:**
> *"Danese Primitivo Puglia Black Label"*, listeleme fiyatı **1.419,00 TL**,
> **stokta değil**, ithalatçı iç etiketi **`Midas`** (kimlik `UNKNOWN`) —
> `EV-2026-08-10-564`, `OBS-665`, `T-565` (`turkiye-pazar-kasifi`, T-464 cevabı).
>
> **Private label modelinin sessiz varsayımı — "tedarikçinin Türkiye'de markası
> yok, dolayısıyla çakışma yok" — bu tedarikçide YANLIŞTIR.**
>
> Somut riskler (hiçbiri doğrulanmadı, hepsi RFQ'da sorulacak):
> - Mevcut Türk müşteri **münhasırlık** iddia edebilir ve üretici bizim private
>   label işimizi **reddedebilir** veya **fiyat/bölge kısıtı** koyabilir.
> - Aynı üreticinin şişesi Türkiye rafında **1.419 TL**'ye listelenmişken bizim
>   hedefimiz **799 TL**'dir — aynı tesis, iki fiyat noktası. Bu **bizim
>   aleyhimize bir referans fiyat** yaratabilir.
> - Ürün premium (Primitivo Puglia, "Black Label") olduğu için üreticinin
>   **value beyaz** kabiliyeti hâlâ **`UNKNOWN`**'dır — listelenmiş olması
>   segment uyumunun kanıtı **değildir**.
>
> ⚠ Kaynak **tek bir online uzman perakendecinin** kataloğudur ve ürün
> **stokta değildir**; ilişkinin **hâlâ canlı olup olmadığı `UNKNOWN`**'dır.

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<Roncà>`** ve **FOB `<liman>`** — ayrı ayrı |
| **Target MOQ** | **≤5.000 şişe/SKU** (mevcut 6.000, pilotun üstünde); ikinci kademe 25.000 |
| **Required payment term** | **`UNKNOWN`** — hem peşin hem 60/90 gün vadeli için ayrı fiyat |
| **Required lead time** | **`UNKNOWN`** — üretim + hazırlık + yükleme ayrı ayrı, **gün** olarak |
| **Origin document** | **OD-1…OD-5 tam set.** ⚠ **OD-3 burada kritiktir:** üretici **gümrük antreposu işlettiğini** beyan ediyor (`EV-2026-08-10-453`) — antrepoda **başka menşeli dökme/şişelenmiş ürün** bulunması menşe kuralı (K2) açısından **açıkça sorulmalıdır** |

### Critical unknowns

1. **Beyaz value portföyü var mı** (çeşit + ABV) — ürün uyumu **hiç doğrulanmadı**.
2. **Fiyat** — hiçbir katmanda hiçbir sayı yok.
3. **Türkiye'deki mevcut ilişki canlı mı, münhasırlık talebi var mı** (`T-565`).
4. **İtalya navlunu — LCL ve FCL ikisi de `UNKNOWN`** (`T-916`); Veneto→liman iç nakliyesi de.
5. Ödeme şartı, lead time, palet/koli konfigürasyonu, sertifikalar — hepsi `UNKNOWN`.

### 3 NEGOTIATION QUESTION

1. **"Türkiye'de hâlihazırda kendi markanızla bir müşteriniz var; bu ilişki
   canlı mı, münhasırlık içeriyor mu, ve bizim markamızla (private label)
   yapılacak iş bu ilişkiyle çakışır mı — çakışıyorsa hangi koşulda çakışmaz?"**
2. **"750 ml kuru beyaz value referansınız için EXW `<Roncà>` ve FOB `<liman>`
   fiyatınızı 5.000 / 10.000 / 25.000 şişe kademelerinde ayrı ayrı verir
   misiniz; kademeler arası fiyat farkı yüzde kaçtır?"**
3. **"Her sevkiyat için EUR.1 veya fatura beyanı düzenlemeyi sözleşmeyle taahhüt
   eder misiniz; şarabın tamamı İtalya'da üretilip şişeleniyor mu ve
   işlettiğiniz gümrük antreposunda başka menşeli ürünle karışma ihtimali var mı?"**

---

# KART 3 — INTERBROSA FAMILY WINES

| Alan | Değer |
|---|---|
| **Supplier** | Interbrosa Family Wines (`SUP-401`) |
| **Country** | **İspanya** |
| **Business model** | **Model B — Private label** |
| **Target product** | 750 ml still kuru beyaz, value kademe (bottled; BIB de var — **kapsam dışı**) |
| **MOQ (bilinen)** | **3.000 şişe** (şarap başına 4 palet) — `EV-2026-08-09-408`, `FACT` · **havuzun doğrulanmış en düşük MOQ'su** |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **P — tercihli KOŞULLU (%50)** · 1/98 |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **272,83** (DOC_OK) · **240,73** (DOC_FAIL) |
| `RFQ TARGET CEILING X / Y` | **200,98 / 290,51** (DOC_FAIL Y: 256,34) |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **142,93** (DOC_OK) · 126,12 (DOC_FAIL) — **havuzun en geniş nefes payı** |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** |
| Yanıltıcı olabilecek beyan | Etiket/koli/kapsül/mantar **tasarımı** ek ücretsiz — bu bir **tasarım** beyanıdır, **baskı/klişe fiyatı değildir** ve fiyat teyidi **sayılmaz** |

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<tesis>`** + **FOB `<liman>`** ayrı ayrı |
| **Target MOQ** | **3.000 mevcut ve pilotla uyumlu** → burada pazarlık MOQ'yu düşürmek değil, **3.000'de fiyatın 25.000'e göre ne kadar cezalandırıldığını** ölçmektir |
| **Required payment term** | **`UNKNOWN`** — peşin ve vadeli ayrı fiyat |
| **Required lead time** | **`UNKNOWN`** — gün olarak |
| **Origin document** | **OD-1…OD-5 tam set.** İspanya→TR hattı çalışıyor (1.916.118 lt/2025) |

### Critical unknowns

1. **Fiyat — hiçbir katmanda yok.**
2. **Klişe/kalıp/kesim bıçağı gibi tek seferlik baskı maliyetleri** ayrıca fatura ediliyor mu ("ücretsiz" ≠ "maliyetsiz").
3. **Türkçe arka etiketi menşede uygulayabiliyor mu** — evet ise Türkiye'deki etiketleme operasyonu (L5 kalemi) **tamamen kalkar**.
4. **Kurumsal site 2026-08-10'da HTTP 503** (`EV-2026-08-10-467`) — firmanın **faal olduğu** teyit edilmedi; temas **yalnızca e-posta/telefonla**.
5. **3.000 MOQ hâlâ geçerli mi** — kanıt kartı 2026-08-09 tarihli, site o günden beri erişilemiyor.
6. Beyaz çeşit ve ABV `UNKNOWN`.

### 3 NEGOTIATION QUESTION

1. **"3.000 şişelik MOQ bugün hâlâ geçerli mi ve bu adette şişe başı EXW/FOB
   fiyatınız nedir; aynı ürün 25.000 şişede kaç para — yani küçük partinin
   fiyat cezası yüzde kaçtır?"**
   *(Havuzun tek düşük-MOQ çapasını teyit eder ve ölçek cezasını sayısallaştırır.)*
2. **"Tasarımın ücretsiz olduğunu belirtiyorsunuz; klişe, kalıp, kesim bıçağı ve
   ilk baskı hazırlığı ayrıca fatura ediliyor mu — tek seferlik tutar ve şişe
   başı tekrarlayan tutar nedir?"**
3. **"Türkçe arka etiketi ve gerekirse ikinci bir uyarı etiketini kendi
   tesisinizde uygulayabiliyor musunuz; bunun şişe başı bedeli nedir ve lead
   time'a kaç gün ekler?"**

---

# KART 4 — THE WINE FACTORY (SARL)

| Alan | Değer |
|---|---|
| **Supplier** | The Wine Factory (SARL) (`SUP-404`) |
| **Country** | **Fransa** — Bordeaux (Gornac) **ve** Languedoc (Valros) — **iki tesis, iki fiyat noktası** |
| **Business model** | **Model B — Private label** |
| **Target product** | 750 ml still beyaz, entry/value — **Languedoc / IGP tarafı hedeflenir** (Bordeaux AOP değil) |
| **MOQ (bilinen)** | **3.600 şişe** — `EV-2026-08-09-410`, `FACT` |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **P — tercihli KOŞULLU (%50)** · 1/98 |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **272,83** (DOC_OK) · **240,73** (DOC_FAIL) |
| `RFQ TARGET CEILING X / Y` | **200,98 / 290,51** (DOC_FAIL Y: 256,34) |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **61,78** (DOC_OK) · 54,51 (DOC_FAIL) — **P grubunun en dar payı** |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

> ⚠ **Fransa'nın karşı sinyali sayısaldır:** gözlenen FR→TR CIF birim değeri
> **6,27 USD/lt** — İspanya'nın (2,71) **2,3 katı.** `IMPLIED_BREAKEVEN` 61,78
> ile Fransa, P grubunun **en dar** ülkesidir. **Bu bir eleme değildir** —
> gözlenen değer **ülke ortalamasıdır ve premium SKU'ları içerir**; entry
> Languedoc'un altında olup olmadığı **bu RFQ'nun cevaplayacağı sorudur.**

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** |
| Bilinen tek ticari şart | Üretim **28–42 gün (4–6 hafta), "ödeme sonrası"** — **peşin ödeme İPUCUDUR, şart olarak doğrulanmamıştır** |

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<Valros>` ve EXW `<Gornac>` AYRI** + FOB `<liman>` — tesis adı yazılmadan fiyat kabul edilmez |
| **Target MOQ** | **3.600 mevcut, pilotla uyumlu**; 25.000 kademesi için fiyat farkı istenir |
| **Required payment term** | **Kritik:** "ödeme sonrası üretim" %100 peşin mi? İkinci siparişten itibaren vade mümkün mü? **Peşin/vadeli ayrı fiyat** |
| **Required lead time** | **28–42 gün üretim `FACT`** + navlun. Sözleşmede **üst sınır (42 gün) taahhüdü** istenir |
| **Origin document** | **OD-1…OD-5 tam set** |

### Critical unknowns

1. **Hangi tesis** — Bordeaux AOP ile Languedoc IGP **aynı fiyat noktası değildir**; tek fiyat gelirse **kullanılamaz**.
2. **Fiyat** — hiçbir katmanda yok.
3. **Colombard-Chardonnay tarzı blend** üretebiliyor mu, minimum parti nedir (görev tanımındaki örnek stil).
4. **%100 peşin mi** — `peak_cash_requirement` ve KKDF ipucu buraya bağlı.
5. **E-posta adresi yok** (`K-C`) — önce telefonla kurumsal e-posta alınmalı.

### 3 NEGOTIATION QUESTION

1. **"Languedoc (Valros) tesisinizden IGP entry beyaz için EXW ve FOB fiyatınızı
   verir misiniz — ve aynı ürünün Bordeaux (Gornac) tesisindeki karşılığıyla
   arasındaki fark şişe başına kaç EUR'dur?"**
   *(İki tesisin fiyat farkı, Fransa'nın segment içi/dışı olduğunu belirleyen
   asıl bilgidir.)*
2. **"'Ödeme sonrası üretim' ifadesi %100 peşin anlamına mı geliyor; ilk sipariş
   peşin, ikinci siparişten itibaren 60/90 gün vade mümkün mü ve vadeli yapıda
   şişe başı fiyat farkı nedir?"**
3. **"Côtes de Gascogne veya benzer bir IGP'de Colombard-Chardonnay tarzı bir
   blend üretebilir misiniz; minimum parti kaç şişe ve reçete değişikliği
   lead time'a kaç gün ekler?"**

---

# KART 5 — CORTA HOJAS EXPORT WINE

| Alan | Değer |
|---|---|
| **Supplier** | Corta Hojas Export Wine (`SUP-406`) |
| **Country** | **Şili** — Curicó, Maule |
| **Business model** | **Model B — Private label** |
| **Target product** | 750 ml still **Sauvignon Blanc / Chardonnay** — **görev tanımıyla birebir eşleşen tek doğrulanmış Şili portföyü** |
| **MOQ (bilinen)** | **`UNKNOWN`** — 2026-08-10'da yeniden okundu, hâlâ yayınlanmamış (`EV-2026-08-10-464`). **Negatif bulgudur, eksik araştırma değildir** |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **P — tercihli KOŞULLU (%50)** · TR-Şili STA, I sayılı Liste dipnot (2) |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **272,83** (DOC_OK) · **240,73** (DOC_FAIL) |
| `RFQ TARGET CEILING X / Y` | **200,98 / 290,51** (DOC_FAIL Y: 256,34) |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **134,03** (DOC_OK) · **118,26** (DOC_FAIL) |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

### ⚠ ŞİLİ'YE ÖZGÜ TERCİH RİSKİ — **ROTA BİR VERGİ KARARIDIR**

> TR-Şili STA'sında **çıkış ülkesi yalnızca Şili** olabilir; **çapraz
> kümülasyon yoktur** (`EV-2026-08-10-160`, `mense-tarife-eslemesi.md` §3.2).
>
> **Somut arıza:** Şili menşeli şarap **Rotterdam/Antwerp'te konsolide edilip
> oradan yüklenirse çıkış ülkesi Şili değildir → %50 düşer, %70 uygulanır** →
> `MAX_CIF` 272,83 → **240,73 (−32,10 TRY/şişe)**.
>
> **Bu tam da LCL/konsolidasyon avantajının doğal rotasıdır.** Yani 5.000
> şişelik pilotta ucuz görünen LCL rotası, **20 puanlık tarife farkını
> yakabilir.** Rota kararı `navlun-lojistik-uzmani` alanıdır (`T-163`, `T-914`)
> — **ama pazarlık masasında bu bir tedarikçi taahhüdü olarak istenir.**

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** — fiyat, MOQ, Incoterm ve lead time'ın **hiçbiri** yayınlanmamış |

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<Curicó>`** + **FOB `<Valparaíso veya San Antonio>`** ayrı ayrı |
| **Target MOQ** | **≤5.000 şişe/SKU** hedeflenir; **iki birimde birden** istenir: (a) SKU başına şişe, (b) sevkiyat başına konteyner — `C-401`'in doğrudan cevabı |
| **Required payment term** | **`UNKNOWN`** — peşin ve vadeli ayrı fiyat |
| **Required lead time** | **`UNKNOWN`** — üretim + yükleme; Şili transit süresi ayrı |
| **Origin document** | **OD-1…OD-5 + ŞİLİ EKİ: "sevkiyat Şili limanından doğrudan çıkacak; üçüncü ülkede konsolide edilmeyecek" taahhüdü sözleşmeye yazılır** |

### Critical unknowns

1. **MOQ — hiçbir birimde yok.** Pilot uyumu **ölçülemiyor**.
2. **Fiyat, Incoterm, lead time** — üçü de yayınlanmamış.
3. **Türkiye'ye ihracat geçmişi** — ihracat bölgeleri listesinde Türkiye **anılmıyor**.
4. **Rota/konsolidasyon** — tercihin düşüp düşmeyeceği buna bağlı.
5. Şili FCL/LCL navlunu `UNKNOWN` (`T-304`).

### 3 NEGOTIATION QUESTION

1. **"MOQ'nuzu iki birimde birden verir misiniz — (a) SKU başına minimum şişe,
   (b) sevkiyat başına minimum konteyner — ve Sauvignon Blanc / Chardonnay için
   o adetlerde EXW `<Curicó>` ve FOB `<Valparaíso/San Antonio>` fiyatınız nedir?"**
2. **"Sevkiyatın Şili limanından **doğrudan** Türkiye'ye çıkacağını ve üçüncü bir
   ülkede konsolide edilmeyeceğini sözleşmeyle taahhüt eder misiniz; EUR.1'i her
   sevkiyatta düzenler misiniz?"**
   *(Bu iki taahhüt birlikte 32,10 TRY/şişe değerindedir — pazarlıktaki en
   büyük tek kalem.)*
3. **"Türkiye'ye daha önce ihracat yaptınız mı — hangi ithalatçıya, hangi
   yıllarda, hangi hacimde; yapmadıysanız Türkiye'ye ilk sevkiyat için ek bir
   şartınız var mı?"**

---

# KART 6 — BODEGAS SAN VALERO (GRUPO BSV)

| Alan | Değer |
|---|---|
| **Supplier** | Bodegas San Valero — Grupo BSV (`SUP-460`) |
| **Country** | **İspanya** — DOP Cariñena, Aragón |
| **Business model** | **İKİSİ BİRDEN — Model A (kendi markaları, ör. Particular) + Model B (private label)** — havuzdaki **tek doğrulanmış ikili aday** |
| **Target product** | 750 ml still kuru beyaz, value kademe — **aynı ürün iki modelde de fiyatlandırılacak** |
| **MOQ (bilinen)** | **`UNKNOWN`** — `EV-2026-08-10-461` |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **P — tercihli KOŞULLU (%50)** · 1/98 |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **272,83** (DOC_OK) · **240,73** (DOC_FAIL) |
| `RFQ TARGET CEILING X / Y` | **200,98 / 290,51** (DOC_FAIL Y: 256,34) |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **142,93** (DOC_OK) · 126,12 (DOC_FAIL) |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

> ⚠ **MODEL A İÇİN EK BİR KESİNTİ VARDIR VE MODELDE `0` ALINMIŞTIR.**
> Model A'da araya bir **dış distribütör** girerse `L6` cirosu üzerinden marj
> alır: **her +1 puan distribütör marjı = −3,62 TRY/şişe** (g=0,50).
> `kanal.yaml → dis_distributor.marj_pct` = **`null` / `UNKNOWN`** (`T-604`).
> **Yani yukarıdaki 272,83 sayısı Model A ve Model B için AYNI görünmektedir —
> ama bu bir eşitlik değil, bir `UNKNOWN`'dır.** İki modelin gerçek farkı
> tamamen bu sayının içindedir ve **bu tedarikçi onu ölçmenin en ucuz yoludur.**

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** — ölçek bilgisi var (2,5 m koli/yıl, 40+ ülke, satışların %70'i ihracat) ama **bunlar fiyat değildir** |
| Private label beyanının kaynağı | ⚠ **Firmanın kendi kanalı değil, üçüncü taraf sektör yayını** — RFQ 4.1 ile teyit **şart** |

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<Cariñena>`** + **FOB `<liman>`** — **ve aynı ürün için iki modelde ayrı ayrı** |
| **Target MOQ** | **≤5.000 şişe/SKU** hedeflenir; **Model A ve Model B MOQ'su ayrı sorulur** (farklı olabilir) |
| **Required payment term** | **`UNKNOWN`** — peşin/vadeli ayrı; **Model A'da vade genelde farklıdır, ayrı sorulur** |
| **Required lead time** | **`UNKNOWN`** — Model A'da stoktan sevk mümkünse **belirtilmesi istenir** (private label'ın 4–6 haftalık üretim süresini elimine eder) |
| **Origin document** | **OD-1…OD-5 tam set** |

### Critical unknowns

1. **Private label kabiliyeti firmanın kendi kanalında doğrulanmadı.**
2. **MOQ — hiçbir modelde bilinmiyor.**
3. **Türkiye'de ithalatçısı var mı / bölge kapalı mı** — Model A'nın **varlık koşulu**. `T-464` cevabı: Particular markası Türkiye'de **BULUNAMADI** — ama *"BULUNAMADI ≠ YOK"* (tek kanal taraması).
4. **Model A'da münhasırlık, hacim taahhüdü, yeniden satış fiyatı tavanı** — hepsi `UNKNOWN`; üçü de kanal marjını **doğrudan kısıtlar**.
5. Doğrudan ihracat e-postası yok (`K-E`) — temas **fuar profili** üzerinden.

### 3 NEGOTIATION QUESTION

1. **"Aynı 750 ml kuru beyaz için (a) kendi markanızla, (b) bizim markamızla
   şişe başı EXW fiyatınız nedir — ve iki fiyat arasındaki fark yüzde kaçtır?"**
   *(Havuzda **iki iş modelinin fiyat farkını aynı maliyet tabanında ölçen tek
   soru** budur; charter'ın "iki model eşit öncelikli" kuralının kanıtla
   sınanması buna bağlıdır.)*
2. **"Model A'da Türkiye için münhasırlık verir misiniz; hangi yıllık hacim
   taahhüdü karşılığında, ve ithalatçıya bir yeniden satış fiyatı tavanı veya
   markup sınırı uygular mısınız?"**
   *(Cevap "evet, tavan var" ise kanal marjı hesabı **dışarıdan kısıtlanır**.)*
3. **"Model A ve Model B için MOQ'nuz farklı mı; private label'da ilave lead
   time kaç gün ve ilk siparişte tek seferlik hazırlık bedeli var mı?"**

---

# KART 7 — CASA SANTOS LIMA

| Alan | Değer |
|---|---|
| **Supplier** | Casa Santos Lima (`SUP-411`) |
| **Country** | **Portekiz** — Alenquer (Lisboa) + 5 bölge |
| **Business model** | **Model A — Mevcut marka distribütörlüğü** (Quinta da Espiga, Quinta das Setencostas, Palha-Canas) |
| **Target product** | 750 ml still kuru **beyaz**, value SKU — **hangi SKU olduğu `UNKNOWN`** |
| **MOQ (bilinen)** | **`UNKNOWN`** — `EV-2026-08-09-418` |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **P — tercihli KOŞULLU (%50)** · 1/98 |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **272,83** (DOC_OK) · **240,73** (DOC_FAIL) |
| `RFQ TARGET CEILING X / Y` | **200,98 / 290,51** (DOC_FAIL Y: 256,34) |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **121,05** (DOC_OK) · 106,81 (DOC_FAIL) |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

> ⚠ **Model A uyarısı (Kart 6 ile aynı):** dış distribütör marjı `UNKNOWN` ve
> **modelde `0` alınmıştır** (`T-604`). Her +1 puan = **−3,62 TRY/şişe**.
> Ayrıca Model A'da **marka sahibi ithalatçıya fiyat tavanı dayatabilir** —
> bu, tavanı **tedarikçi tarafından** daraltan tek mekanizmadır.

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** |

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<Alenquer>`** + **FOB `<Lisboa/Leixões>`** ayrı ayrı |
| **Target MOQ** | **≤5.000 şişe/SKU** hedeflenir; **karışık palet/karışık konteyner kabul edilir mi** ayrıca sorulur (Model A'da çok SKU'lu ilk sipariş tipiktir) |
| **Required payment term** | **`UNKNOWN`** — peşin/vadeli ayrı |
| **Required lead time** | **`UNKNOWN`** — **stoktan sevk mümkün mü** (Model A'nın asıl avantajı) |
| **Origin document** | **OD-1…OD-5 tam set** |

### Critical unknowns

1. **Türkiye'de ithalatçısı/distribütörü var mı, bölge kapalı mı** — Model A'nın **varlık koşulu**. `T-464`: 4 markanın hiçbiri Türkiye'de **BULUNAMADI**; **ama Metro, zincir market, tekel ve HoReCa rafları görülmedi** — doğru statü **`presence UNKNOWN`**.
2. **Marka daha önce Türkiye'de satıldı mı, satıldıysa neden durdu.**
3. **Münhasırlık şartları, yıllık hacim taahhüdü, pazarlama katkısı** — `UNKNOWN`.
4. **Hangi beyaz SKU value segmenttedir ve fiyatı nedir** — `UNKNOWN`.
5. **MOQ ve private label kabiliyeti** — private label sitede **anılmıyor** = `UNKNOWN`, "yok" değil.
6. Temas kanalı yalnızca **web formu** (`K-D`) — iki aşamalı temas gerekir.

### 3 NEGOTIATION QUESTION

1. **"Türkiye'de hâlihazırda bir ithalatçınız/distribütörünüz var mı, bölge açık
   mı; bu markalar Türkiye'de daha önce satıldı mı ve satış neden durdu?"**
   *(Cevap "bölge kapalı" ise bu kart **düşer** — pazarlığa girmeden.)*
2. **"Türkiye için münhasırlık karşılığında hangi yıllık hacim taahhüdünü
   istiyorsunuz; ithalatçıya yeniden satış fiyatı tavanı veya markup sınırı
   uyguluyor musunuz ve pazarlama katkısı (listeleme/tanıtım) bütçeniz var mı?"**
   *(Üç cevap birlikte kanal marjı hesabının dış kısıtını verir.)*
3. **"Value segmentteki beyaz SKU'larınız için EXW/FOB şişe fiyatınız nedir ve
   bu fiyat stoktan sevk edilebiliyor mu — yoksa üretim planına mı bağlı?"**

---

# KART 8 — VIDIGAL WINES S.A.

| Alan | Değer |
|---|---|
| **Supplier** | Vidigal Wines S.A. (`SUP-454`) |
| **Country** | **Portekiz** — Leiria bölgesi |
| **Business model** | **Model A — Mevcut marka distribütörlüğü** (amiral marka **Porta 6**) · **Model B kabiliyeti `UNKNOWN`, ayrıca sorulacak** |
| **Target product** | 750 ml still kuru **beyaz** value SKU — **beyaz portföy tamamen `UNKNOWN`** |
| **MOQ (bilinen)** | **`UNKNOWN`** — `EV-2026-08-10-456` |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **P — tercihli KOŞULLU (%50)** · 1/98 |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **272,83** (DOC_OK) · **240,73** (DOC_FAIL) |
| `RFQ TARGET CEILING X / Y` | **200,98 / 290,51** (DOC_FAIL Y: 256,34) |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **121,05** (DOC_OK) · 106,81 (DOC_FAIL) |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** |
| ⚠ Kanal uyarısı | Kurumsal site (vidigalwines.com) 2026-08-10'da **porta6.com'a yönlendiriyor** ve yaş doğrulama duvarının arkasında → temas **fuar profili** üzerinden (`K-E`) |

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<Leiria>`** + **FOB `<liman>`** ayrı ayrı |
| **Target MOQ** | **≤5.000 şişe/SKU**; Model A ve Model B için ayrı |
| **Required payment term** | **`UNKNOWN`** — peşin/vadeli ayrı |
| **Required lead time** | **`UNKNOWN`** — stoktan sevk mümkün mü |
| **Origin document** | **OD-1…OD-5 tam set** |

### Critical unknowns

1. **Beyaz value portföyü var mı** — **ürün uyumunun ön koşulu ve tamamen `UNKNOWN`**. Porta 6 bilinen bir **kırmızı** amiral markadır.
2. **Porta 6 veya diğer markalar Türkiye'de satılıyor mu, bölge açık mı** — `T-464`: **BULUNAMADI**, ama *"Porta 6 küresel hacimli bir value markadır ve Türkiye'de zincir market veya Metro rafında bulunması tamamen mümkündür"* (`turkiye-pazar-kasifi`'nin kendi uyarısı).
3. **Private label yapıyor mu, MOQ farkı nedir.**
4. **Fiyat, MOQ, ödeme, lead time** — hiçbiri yok.
5. **Temas kanalı zayıf** (`K-E`) — kurumsal e-posta doğrulanamadı.

### 3 NEGOTIATION QUESTION

1. **"Portföyünüzde 750 ml kuru BEYAZ value SKU var mı — hangi çeşitlerle,
   hangi ABV'de ve EXW/FOB şişe fiyatı nedir?"**
   *(Cevap "yok" ise bu kart **ürün uyumu nedeniyle düşer**, fiyat pazarlığına
   hiç gelinmez.)*
2. **"Porta 6 ve diğer markalarınız Türkiye'de hâlihazırda satılıyor mu; bölge
   açıksa münhasırlık için hangi yıllık hacmi ve hangi listeleme/tanıtım
   katkısını öngörüyorsunuz?"**
3. **"Model A'nın yanında bizim markamızla (private label) üretim yapar
   mısınız; MOQ ve şişe başı fiyat farkı nedir?"**
   *(Aynı firmada iki modeli aynı maliyet tabanında test etme fırsatı — Kart 6
   ile birlikte **iki bağımsız ölçüm** verir.)*

---

# KART 9 — PLAIMONT (VIGNERONS EN GASCOGNE)

| Alan | Değer |
|---|---|
| **Supplier** | Plaimont — Vignerons en Gascogne & Piémont Pyrénéen (`SUP-457`) |
| **Country** | **Fransa** — Saint-Mont, Gaskonya (IGP Côtes de Gascogne) |
| **Business model** | **Model A — Mevcut marka distribütörlüğü** (Colombelle, BIG) · **private label kabiliyeti `UNKNOWN`** |
| **Target product** | **IGP Côtes de Gascogne Colombard / Colombard-Chardonnay** — **görev tanımındaki örnek blendin yapısal kaynağı; havuzun en güçlü ürün eşleşmesi** |
| **MOQ (bilinen)** | **`UNKNOWN`** — `EV-2026-08-10-459` |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **P — tercihli KOŞULLU (%50)** · 1/98 |

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | Değer (TRY/şişe, CIF Türkiye) |
|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **272,83** (DOC_OK) · **240,73** (DOC_FAIL) |
| `RFQ TARGET CEILING X / Y` | **200,98 / 290,51** (DOC_FAIL Y: 256,34) |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **61,78** (DOC_OK) · 54,51 (DOC_FAIL) — **P grubunun en dar payı** |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** |

> ⚠ **Bu kartın merkezindeki gerilim:** ürün eşleşmesi **havuzun en güçlüsü**,
> ülke sinyali **havuzun en zayıflarından biri** (FR→TR gözlenen CIF
> **6,27 USD/lt**). Gascogne'un bu ortalamanın **altında** olduğu
> **doğrulanmamıştır** — ve gözlenen seri **ülke ortalamasıdır, premium SKU
> içerir**, yani entry Gascogne'un altında olması **beklenir ama kanıtlanmamıştır.**
> **Bu RFQ'nun tek işi bu gerilimi çözmektir.**

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** |

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<Saint-Mont>`** + **FOB `<liman>`** ayrı ayrı |
| **Target MOQ** | **≤5.000 şişe/SKU** (Model A) — kooperatif yapısı nedeniyle **parti bazlı bir alt sınır olabilir**, ayrıca sorulur |
| **Required payment term** | **`UNKNOWN`** — peşin/vadeli ayrı |
| **Required lead time** | **`UNKNOWN`** — hasat yılı bazlı stok mevcudiyeti sorulur |
| **Origin document** | **OD-1…OD-5 tam set.** ⚠ Kooperatifte üzüm **çok sayıda üreticiden** gelir — bu K2'yi bozmaz (hepsi Fransa) ama **OD-3 yine de yazılı istenir** |

### Critical unknowns

1. **Entry IGP Colombard fiyatı** — Fransa'nın segment içi olup olmadığını belirleyen **tek sayı**.
2. **Türkiye'de ithalatçısı var mı, Colombelle için bölge açık mı** — `T-464`: **BULUNAMADI** (tek kanal).
3. **Kooperatif private label (müşteri markası) üretiyor mu**, MOQ ve ek lead time.
4. **MOQ, ödeme, lead time, palet konfigürasyonu** — hepsi `UNKNOWN`.
5. Temas kanalı **form + telefon** (`K-D/K-C`) — kurumsal ihracat e-postası yok.

### 3 NEGOTIATION QUESTION

1. **"IGP Côtes de Gascogne Colombard veya Colombard-Chardonnay için 5.000 /
   25.000 şişe/yıl hacminde EXW `<Saint-Mont>` ve FOB `<adı belirtilen liman>`
   şişe fiyatınız nedir?"**
   *(Fransa'nın 6,27 USD/lt ülke ortalamasının **altında** olup olmadığını
   belirleyen tek soru — bu cevap gelmeden Fransa hakkında hiçbir sonuç
   üretilemez.)*
2. **"Colombelle markası için Türkiye bölgesi açık mı; açıksa münhasırlık
   karşılığında hangi yıllık hacmi istiyorsunuz ve bir yeniden satış fiyatı
   politikanız var mı?"**
3. **"Kooperatif olarak müşteri markası (private label) üretiyor musunuz; MOQ,
   ek lead time ve şişe başı fiyat farkı nedir?"**
   *(Evet ise bu kart Model A'dan **ikili adaya** yükselir ve Kart 6 ile
   karşılaştırılabilir hale gelir.)*

---

# KART 10 — PURCARI WINERIES GROUP

| Alan | Değer |
|---|---|
| **Supplier** | Purcari Wineries Group (`SUP-461`) — Château Purcari · **Bostavan** · Crama Ceptura · Domeniile Cuza · Angels Estate |
| **Country** | **Moldova** (+ **Romanya**, **Bulgaristan**) — **üç ayrı hukuki menşe grubu** |
| **Business model** | **Model A — Mevcut marka distribütörlüğü** · private label **`UNKNOWN`** |
| **Target product** | 750 ml still kuru beyaz, **value/entry** (Bostavan adayı) — **doğrulanmadı** |
| **MOQ (bilinen)** | **`UNKNOWN`** — `EV-2026-08-10-462` |
| **Target shelf price** | 799 TRY · alt/üst 699 / 899 |
| **Target channel** | CHAIN RETAIL |
| **Menşe grubu** | **N — tercihsiz (%70) — MOLDOVA İÇİN** · **P (%50) — Romanya/Bulgaristan tesisleri için** |

### ⚠ MENŞE — BU KARTIN EN ÖNEMLİ MADDESİ

> **Türkiye-Moldova STA'sı VARDIR ama 2204.21'i KAPSAMAZ** → **%70**
> (`EV-2026-08-10-165`, T1; `mense-tarife-eslemesi.md` §1.1.1).
> *Bir STA'nın varlığı, o üründe indirim olduğu anlamına gelmez.*
>
> **TUR 2'de Purcari, "Moldova Türkiye'ye en düşük L2 CIF menşeidir
> (2,46 USD/lt)" gerekçesiyle listeye alınmıştı. Bu avantajın bir kısmı
> tarifeyle geri alınır:** azami alım fiyatı **272,83 değil 240,73** TRY/şişe —
> **−%11,765 (−32,10 TRY/şişe)** — ve bu kayıp **koşulsuzdur**, belge
> getirilerek geri alınamaz.
>
> **Buna rağmen `IMPLIED_BREAKEVEN_USDTRY` = 138,94 ile Purcari hâlâ havuzun
> ikinci en geniş nefes payına sahiptir** (ES 142,93'ün hemen ardında) —
> çünkü gözlenen CIF birim değeri de o kadar düşüktür. **Yani tarife dezavantajı
> gözlenen fiyat avantajını SİLMEZ, DARALTIR.** Bu iki etkinin net sonucu
> **ancak gerçek teklifle** ölçülür.
>
> **Ve bir kaldıraç doğar:** aynı grubun **Romanya (Crama Ceptura, Domeniile
> Cuza) ve Bulgaristan (Angels Estate) tesisleri AB üyesidir ve %50 öder.**
> **Aynı gruptan hangi tesisten yüklendiği vergi sonucunu değiştirir** →
> tavan 240,73 → **272,83**. Bu, havuzda **tek bir tedarikçiyle menşe
> değiştirilebilen tek durumdur** ve doğrudan bir pazarlık kalemidir.

### Fiyat seviyeleri — `TARGET / MODEL_DERIVED / UPPER_BOUND`

| Alan | **Moldova menşeli** | **Romanya/Bulgaristan menşeli** |
|---|---|---|
| **`MAXIMUM STRUCTURAL BUY PRICE`** | **240,73** | **272,83** (DOC_OK) / 240,73 (DOC_FAIL) |
| `RFQ TARGET CEILING X` | **200,98** | **200,98** |
| `RFQ TARGET CEILING Y` | **256,34** | **290,51** (DOC_OK) |
| `IMPLIED_BREAKEVEN_USDTRY` @Y | **138,94** (MD gözlenen CIF 2,46) | **`UNKNOWN`** — RO/BG için gözlenen CIF serisi bu projede kullanılmadı |
| `MAX_FOB` / `MAX_EXW` | **`UNKNOWN`** — fx `null` | **`UNKNOWN`** |
| `TARGET_DISCOUNT_FROM_MAX` · `REQUIRED_IMPORTER_MARGIN` · `WALK_AWAY_PRICE` | **`INVESTOR_DECISION_REQUIRED`** | aynı |

> ⚠ **`DÜ FALLBACK` uyarısı:** Moldova `mense_tarife_eslemesi.ulkeler`
> listesinde **satır olarak yoktur**; engine fallback ile %70'e düşmüş ve sonuç
> `EV-2026-08-10-165` ile **tesadüfen uyuşmuştur**. Bu bir doğrulama değildir
> (`T-853`).

### Bilinen tedarikçi fiyatı

| Alan | Değer |
|---|---|
| **Known supplier price** | **YOK** |
| **Quote class** | **`NONE`** — grup geliri 437,2 m RON (2025) yayınlı ama **hacim kırılımı olmadığı için şişe başı fiyat türetilemez**; türetmek uydurma olurdu |
| ⚠ Karşı sinyal | Grup kendini *"the most premium wines from Moldova and Romania"* diye konumlandırıyor — **segmentimizle ters** |
| ✅ Lehte sinyal | **Bükreş Borsası'nda işlem gören halka açık şirket (BVB: WINE)** — denetlenmiş finansallar; **havuzun tedarikçi sağlamlığı en şeffaf doğrulanabilir adayı** |

### Pazarlık pozisyonu

| Alan | Talep |
|---|---|
| **Target Incoterm** | **EXW `<tesis adı + ülke>`** + **FOB `<liman>`** — **her menşe için ayrı** |
| **Target MOQ** | **≤5.000 şişe/SKU**; grup içi **karışık menşeli konteyner mümkün mü** ayrıca sorulur (mümkünse **tek konteynerde iki tarife oranı** doğar — `gumruk-vergi-uzmani`'na sorulacak yeni bir soru) |
| **Required payment term** | **`UNKNOWN`** — peşin/vadeli ayrı |
| **Required lead time** | **`UNKNOWN`** |
| **Origin document** | **Moldova için: tercihli belge YOK — belge gerekçesiyle prim kabul edilmez.** **Romanya/Bulgaristan için: OD-1…OD-5 tam set** |

### Critical unknowns

1. **Value/entry beyaz SKU var mı** — "premium" konumlandırması segmentimizi **dışlıyor olabilir**.
2. **Fiyat — hiçbir katmanda yok.**
3. **Türkiye'ye ihracat geçmişi** — Moldova hattı **ülke düzeyinde** çalışıyor (2.038.906 lt/2025) ama **bu firmanın payı `UNKNOWN`**.
4. **Aynı ürün RO/BG tesisinden yüklenebilir mi** — %50/%70 farkının pazarlık değeri buna bağlı.
5. **MD/RO/BG rotalarının navlunu** `UNKNOWN` (`T-304`); Moldova **denize kıyısı olmayan** bir menşedir — transit rota sorusu ayrıca doğar.
6. Türkiye'de mevcut ithalatçı `presence UNKNOWN` (`T-464`).

### 3 NEGOTIATION QUESTION

1. **"Value/entry segmentinizde (ör. Bostavan) 750 ml kuru beyaz SKU'larınız var
   mı ve EXW/FOB şişe fiyatı nedir — 'premium' konumlandırmanız bu segmenti
   dışlıyor mu?"**
   *(Cevap "dışlıyor" ise kart pazarlığa girmeden düşer.)*
2. **"Aynı ürünü veya muadilini Romanya (Crama Ceptura / Domeniile Cuza) ya da
   Bulgaristan (Angels Estate) tesisinizden tedarik edebilir misiniz — ve o
   durumda EXW fiyat farkı nedir?"**
   *(Bu tek soru, tarife oranını %70'ten %50'ye çekebilir: azami alım fiyatımız
   **+32,10 TRY/şişe** genişler. **Havuzdaki en yüksek getirili tek pazarlık
   sorusudur.**)*
3. **"Her menşe için hangi menşe ispat belgesini düzenleyebiliyorsunuz — Romanya
   ve Bulgaristan için EUR.1 veya fatura beyanı, Moldova için ne — ve tek
   sevkiyatta birden fazla menşeyi birleştirebiliyor musunuz?"**
   *(Cevap ham hâliyle `gumruk-vergi-uzmani`'na iletilir; **biz vergi sonucu
   üretmiyoruz.**)*

---
---

## 11. ÖZET TABLO — 10 KART

| # | Supplier | Ülke | Model | Menşe grubu | **MAX STRUCTURAL BUY PRICE** (TRY/şişe, CIF) | Y tavanı | X tavanı | Quote class | MOQ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Harland Wine Company | AU | B | **N (%70)** | **240,73** | 256,34 | 200,98 | `PUBLIC_INDICATIVE` ⚠ para birimi/katman belirsiz | 6.000 `FACT` |
| 2 | Cantina Danese | IT | B | P (%50 koşullu) | **272,83** / 240,73 | 290,51 | 200,98 | `NONE` | 6.000 `FACT` |
| 3 | Interbrosa Family Wines | ES | B | P (%50 koşullu) | **272,83** / 240,73 | 290,51 | 200,98 | `NONE` | **3.000** `FACT` |
| 4 | The Wine Factory | FR | B | P (%50 koşullu) | **272,83** / 240,73 | 290,51 | 200,98 | `NONE` | 3.600 `FACT` |
| 5 | Corta Hojas Export Wine | CL | B | P (%50 koşullu) ⚠ rota | **272,83** / 240,73 | 290,51 | 200,98 | `NONE` | `UNKNOWN` |
| 6 | Bodegas San Valero | ES | **A+B** | P (%50 koşullu) | **272,83** / 240,73 | 290,51 | 200,98 | `NONE` | `UNKNOWN` |
| 7 | Casa Santos Lima | PT | A | P (%50 koşullu) | **272,83** / 240,73 | 290,51 | 200,98 | `NONE` | `UNKNOWN` |
| 8 | Vidigal Wines | PT | A (+B?) | P (%50 koşullu) | **272,83** / 240,73 | 290,51 | 200,98 | `NONE` | `UNKNOWN` |
| 9 | Plaimont | FR | A (+B?) | P (%50 koşullu) | **272,83** / 240,73 | 290,51 | 200,98 | `NONE` | `UNKNOWN` |
| 10 | Purcari Wineries Group | **MD** (+RO/BG) | A | **N (%70)** · RO/BG **P** | **240,73** (MD) · **272,83** (RO/BG) | 256,34 · 290,51 | 200,98 | `NONE` | `UNKNOWN` |

**Model dağılımı: 5 × B · 3 × A · 2 × A+B(?)** — charter'ın "iki model eşit
öncelikli" kuralı korunmuştur.

> ### BU TABLONUN OKUNMASI
> **10 kartın 10'unda `MAXIMUM STRUCTURAL BUY PRICE` yalnızca İKİ değer alıyor.**
> Bu bir hata veya tembellik değil, `reverse-price-model.md` §4.2'nin doğrudan
> sonucudur: **ters modelde menşe, tavanı yalnızca `(1+g)` böleni üzerinden
> etkiler.** Ülkeler arası gerçek ayrışma **FOB seviyesinde** (navlun + menşe
> local charge) doğar ve **o bacak fx olmadan hesaplanamaz.**
>
> **Yani bu tabloda tedarikçiler arasında görünen tek yapısal fark tarifedir.
> Gerçek fark, gelmemiş olan tekliflerin içindedir.**

### 11.1 Fiyat isteme eşiği — **hangi tedarikçiden hangi rakamın altında teklif isteneceği**

| Menşe grubu | Tedarikçiler | **Öncelikli hedef: `CIF ≤ X`** | Kabul edilebilir bant: `X < CIF ≤ Y` | Bandın üstü |
|---|---|---|---|---|
| **P** — ES/PT/IT/FR/CL | Danese, Interbrosa, TWF, Corta Hojas, San Valero, Casa Santos Lima, Vidigal, Plaimont | **≤ 200,98 TRY/şişe CIF** | 200,98 – **290,51** | > 290,51 → mevcut modelde zor |
| **N** — AU/MD | Harland, Purcari (MD menşeli) | **≤ 200,98 TRY/şişe CIF** | 200,98 – **256,34** | > 256,34 → mevcut modelde zor |
| **N→P dönüşümü** | Purcari (RO/BG menşeli) | ≤ 200,98 | 200,98 – **290,51** | > 290,51 |

**Litre karşılığı:** X = **267,97 TRY/lt** · Y = **387,35 TRY/lt** (P) /
**341,78 TRY/lt** (N).

> ⛔ **BU EŞİKLER TEDARİKÇİYE SÖYLENMEZ.** Bunlar **iç pazarlık sınırlarıdır**;
> RFQ'da hedef fiyat açıklanmaz, aksi hâlde her teklif tavana yapışır.
> `rfq-template.md` §0 zaten hedef fiyat açıklamayan bir yapıdadır.
>
> ⛔ **VE BU EŞİKLER FX OLMADAN UYGULANAMAZ.** Tedarikçi EUR/USD verecek;
> karşılaştırma TL'dir. **Kur girilene kadar hiçbir teklif için
> "eşiğin altında/üstünde" denemez** (`T-852`, `T-912`).

### 11.2 Menşe belgesi pazarlık kaleminin kartlara girişi — özet

| Kart | Menşe grubu | Kartta yer alan pazarlık kalemi | Değeri |
|---|---|---|---|
| 2, 3, 4, 6, 7, 8, 9 | **P** | **OD-1…OD-5 tam set** (EUR.1/fatura beyanı taahhüdü, onaylanmış ihracatçı, dökme bileşen yok, çıkış limanı, fiyat düzeltme maddesi) | **+32,10 TRY/şişe** (799/CHAIN/BASE/5k) |
| 5 (Corta Hojas) | **P** | OD tam set **+ ŞİLİ EKİ:** "üçüncü ülkede konsolide edilmeyecek" taahhüdü | aynı 32,10 — **ama burada riski taşıyan rota kararıdır** |
| 1 (Harland) | **N** | **Tercihli belge yok** → "belgeleri hallederiz" primi **reddedilir** | 0 (kazanılacak tercih yok) |
| 10 (Purcari) | **N** (MD) | **Tercihli belge yok** — **ama menşe tesisi değiştirilebilir** (RO/BG) | **+32,10 TRY/şişe** — havuzun **tek menşe değiştirme kaldıracı** |

---

## 12. GÖNDERİM ÖNCESİ ZORUNLU KONTROLLER — GÜNCELLENMİŞ

| # | Kontrol | Sorumlu | Durum |
|---|---|---|---|
| 1 | `T-401` / `T-462` — hangi ülke hangi menşe belgesi grubunda | `gumruk-vergi-uzmani` | **Fiilen kapandı** — `mense-tarife-eslemesi.md` §1 + §5; kartlarda OD-1…OD-5 olarak uygulandı |
| 2 | `T-161` — RFQ'da sorulacak menşe belgesi soruları | `global-sourcing-kasifi` | **Bu belgede karşılandı** (§0.6) — kapanış kararı başkanındır |
| 3 | `T-464` — Model A adaylarının TR'de ithalatçısı | `turkiye-pazar-kasifi` | **ANSWERED** — hiçbiri bulunamadı; **`presence UNKNOWN`** statüsüyle kartlara işlendi |
| 4 | `T-565` — Cantina Danese'nin TR'deki mevcut ilişkisi | `turkiye-pazar-kasifi` | **AÇIK** — Kart 2'de münhasırlık riski olarak yazıldı |
| 5 | `<VOLUME>` / hedef basamak / kanal seçimi | `yatirim-komitesi-baskani` | **AÇIK** → **`T-871`** |
| 6 | `OQ-901` — TARGET/ACCEPTABLE/WALK-AWAY eşikleri | `yatirim-komitesi-baskani` | **AÇIK** (`T-851`, CRITICAL) — kartlarda `INVESTOR_DECISION_REQUIRED` |
| 7 | `fx` — tek tarihli kur kaydı | `yatirim-komitesi-baskani` / `finans-fizibilite` | **AÇIK** (`T-852`, `T-912`) — **eşikler bu olmadan uygulanamaz** |
| 8 | OD-5 (koşullu fiyat düzeltme maddesi) hukuken uygulanabilir mi | `gumruk-vergi-uzmani` | **AÇIK** → **`T-872`** |
| 9 | Purcari MD/RO/BG yükleme noktası — navlun ve çıkış ülkesi | `navlun-lojistik-uzmani` | **AÇIK** → **`T-873`** |
| 10 | Tüm 10 hedefe **aynı metin** | `global-sourcing-kasifi` | Uygulanacak (`rfq-template.md` §0.8) |
| 11 | Gönderim onayı | `yatirim-komitesi-baskani` | **AÇIK** — karar `TEST`/`IMPORT PILOT` değilse gönderim yok |

---

## 13. KARTLARIN KENDİ ZAYIFLIKLARI — DÜRÜST ENVANTER

| # | Zayıflık | Etki |
|---|---|---|
| 1 | **10 kartın 10'unda `MAX_FOB` ve `MAX_EXW` `UNKNOWN`** | Tedarikçiyle konuşulacak **tam da o iki katmandır**. Kartlar CIF tavanı verir, pazarlık EXW/FOB'da geçer |
| 2 | **9 kartta `quote_class: NONE`** | Havuzda **tek bir gerçek teklif yoktur**; kartlar tamamen model tarafındadır |
| 3 | **Tek `PUBLIC_INDICATIVE` fiyatın para birimi ve katmanı belirsiz** | "Gösterge fiyat ↔ gerçek teklif" sapması **hâlâ ölçülemiyor** (TUR 1 §7.1'den beri açık) |
| 4 | **Çapa (799/CHAIN) bir öneriye dayanıyor, karara değil** | Başkan farklı bir basamak/kanal seçerse **10 kartın tüm rakamları değişir** (699'da −41,67 TRY/şişe) |
| 5 | **`L8_CHAIN_RETAIL` hiç gözlenmemiş** | Çapanın dayandığı raf katmanı Türkiye'de **ölçülmemiştir** (`T-701`) |
| 6 | **5 kartta MOQ `UNKNOWN`** | Pilot uyumu **ölçülemiyor**; hacim köşeleri (5.000/25.000) tedarikçi tarafında **doğrulanmamış** |
| 7 | **`MAXIMUM STRUCTURAL BUY PRICE` iki bağımsız nedenle şişkin** | λ=1 çapası + 13 maliyet kaleminin `0` alınması. **Gerçek tavan bunun altındadır** — kartlar projenin **lehine** sapar |
