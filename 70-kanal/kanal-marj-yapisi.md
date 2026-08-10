# KANAL MARJ VE TİCARİ KOŞULLAR YAPISI — TUR 2

```yaml
ajan:   kanal-marj-uzmani
tur:    TUR 2
tarih:  2026-08-10
durum:  DRAFT
kapsam: "Uc kanal (chain retail / independent-tekel / HoReCa) x ticari kosul kalemleri.
         L6 -> L7 -> L8 merdiveninin YAPISI. Sayilarin cogu UNKNOWN'dir ve oyle birakilmistir."
```

---

## 0. BU DOSYAYI OKUMADAN BURADAN SAYI ALINAMAZ — BAĞLAYICI KURALLAR

| # | Kural |
|---|---|
| **M1** | Bu dosyadaki **hiçbir marj rakamı** dört niteliği (katman çifti · brüt/net · KDV dahil/hariç · margin/markup) belirtilmeden alıntılanamaz. |
| **M2** | `pazar.yaml → katman_kurallari.K2` gereği **599,90 TL'den L7 türetilmemiştir** ve türetilemez. Bu dosyada L7 bağımsız olarak, formülle kurulmuştur. |
| **M3** | `pazar.yaml → K5` gereği 599,90 / 649,90 TL bir **Metro cash & carry gözlemidir**, genel piyasa fiyatı değildir. Bu dosyada hedef fiyat olarak **kullanılmamıştır**. |
| **M4** | `İP-2001` / `T-205` gereği **alkolde reklam-tanıtım-görsel kaldıraçları YOKTUR** — bu bir belirsizlik değil, bu analizin **başlangıç koşuludur**. |
| **M5** | Bu dosyadaki FMCG geneli / süt kategorisi / tüm-kategori perakende verilerinden şaraba yapılan her geçiş `ESTIMATE`'tir ve türetme zinciri gösterilmiştir. **Şarap verisi gibi sunulmamıştır.** |
| **M6** | Vergi oranı (KDV/ÖTV), navlun, ruhsat ve tedarikçi fiyatı bu dosyanın **kapsamı dışındadır**; formüllerde sembolik olarak (`t_kdv`) bırakılmıştır. |

---

## 1. FİYAT MERDİVENİ — L5 → L8 (YAPI, SAYI DEĞİL)

### 1.1 Katmanların bu projedeki kanal karşılıkları

| Katman | Tanım (CLAUDE.md §6) | Kanal karşılığı |
|---|---|---|
| **L5** | IMPORTER COST | Bizim tam maliyetimiz (bandrol, depo, iç nakliye, finansman dahil) |
| **L6** | IMPORTER SELLING PRICE | **Faturada yazan** ithalatçı satış fiyatı, KDV hariç |
| **L7** | RETAILER PURCHASE PRICE | Perakendecinin **fiili** alış maliyeti = L6 − geri akan bedeller |
| **L8** | CONSUMER SHELF PRICE | Tüketici raf fiyatı (KDV dahil) |

### 1.2 L6 ile L7 AYNI SAYI DEĞİLDİR — kanal ekonomisinin merkezi

Türkiye zincir perakendesinde ithalatçı ile perakendeci arasında **iki ayrı para akışı** vardır:

```
(A) MAL FATURASI      : ithalatçı -> perakendeci       (tutar = L6)
(B) HİZMET FATURALARI : perakendeci -> ithalatçı       (ciro primi, alan kullanımı,
                        lojistik bedeli, kırık ürün bedeli, enerji bedeli, CRM, B2B ...)
```

(B) akışının varlığı **alkollü içki için ismen kanıtlıdır** — `EV-2026-08-10-612`
(Rekabet Kurulu 21-51/708-351, para.82): Migros, Carrefour, Özdilek, **Metro** ve
Tespo ile imzalanan **yıllık satış anlaşmalarının** içeriğinde
*"CRM, B2B (kasa çıkışı cirosu), alan kullanımı, kırık ürün bedeli, lojistik bedeli,
soğutucuların harcadığı enerji karşılığı bedeli gibi müşteriye ödenecek bedeller ile
satın alınan malın geri ödeme vadesi"* yazılıdır.

Bu nedenle **modelin taşıyıcı denklemi**:

```
L7_effective = L6 × (1 − d)  −  f_per_bottle

  L6            = fatura fiyatı (KDV hariç)
  d             = ciroya oranlı geri akan bedeller toplamı (%)   [ciro primi, lojistik
                  bedeli, alan kullanımı, kırık ürün bedeli, enerji, CRM/B2B ...]
  f_per_bottle  = sabit tutarlı bedellerin şişe başına düşen payı (listeleme/giriş bedeli
                  ÷ yıllık şişe adedi)
```

### 1.3 İleri ve ters formül (finans-fizibilite bunu aynen kullanmalıdır)

```
İLERİ:
  L8_kdv_haric = L7_effective / (1 − m_retail)
  L8_kdv_dahil = L8_kdv_haric × (1 + t_kdv)

TERS (hedef raf fiyatından geriye):
  L8_kdv_haric = L8_kdv_dahil / (1 + t_kdv)
  L7_effective = L8_kdv_haric × (1 − m_retail)
  L6           = (L7_effective + f_per_bottle) / (1 − d)
```

`m_retail` = **gross margin on selling price**, KDV hariç, L7→L8 arası.
`t_kdv` bu ajanın alanı **değildir** (`gumruk-vergi-uzmani`).

### 1.4 Merdiven neden SAYISAL OLARAK KAPANMIYOR

| Girdi | Durum | Sahibi |
|---|---|---|
| `L8_CHAIN_RETAIL` | **UNKNOWN** (`pazar.yaml → l8_chain_retail`) | `turkiye-pazar-kasifi` → **T-603** |
| `m_retail` (şarap) | **UNKNOWN**; yalnızca tüm-kategori proxy var (`EV-616`) | bu ajan |
| `d` | **UNKNOWN** (kalem listesi FACT, oranlar karartılmış — `EV-610`, `EV-612`) | bu ajan → TUR 7 |
| `f_per_bottle` | **UNKNOWN** (güncel kamu kaynağı yok — `EV-619`) | bu ajan → TUR 7 |
| `t_kdv` | `vergi.yaml` | `gumruk-vergi-uzmani` |

> **Sonuç: `L7` ve `L6` bu turda sayısal olarak üretilemez ve üretilmemiştir.**
> Üretilen şey, dört bilinmeyeni açıkça isimlendiren **denklem** ve her bilinmeyen için
> gerekçelendirilmiş bir **duyarlılık bandıdır**.

---

## 2. KANAL A — CHAIN RETAIL (zincir market / cash & carry) · öncelik 1

### 2.1 Kanalın hukuki ve yapısal çerçevesi

| Bulgu | Statü | evidence |
|---|---|---|
| Zincir perakendeci, **ürün talebini doğrudan etkileyen bir hizmet verdiği** ve hizmetin türü + bedelin tutar/oranı **sözleşmede yazılı olduğu** sürece prim/bedel alabilir. Mağaza açılışı, tadilat, ciro açığı, kart katılım bedeli **her durumda yasaktır**. | FACT | `EV-2026-08-10-601` |
| Bedel karşılığı verilebilecek hizmetler metinde **iki gruptur**: (i) aktivite/reklam/dergi/anons yoluyla **tanıtım hizmeti**, (ii) **teşhir ünitelerinde özel konumlandırma hizmeti**. | FACT | `EV-2026-08-10-605` |
| **Alkolde (i) fiilen satın alınamaz** (kabul edilmiş iş kısıtı — `İP-2001`, `T-205`, `EV-2026-08-09-222/-223`). Geriye yalnızca **fiziksel konumlandırma** kalır. | ESTIMATE | `EV-605` + `İP-2001` |
| Alkollü içkide zincirlerle **1 yıllık yıllık satış anlaşması** imzalanır; içeriğinde CRM, B2B (kasa çıkışı cirosu), alan kullanımı, kırık ürün bedeli, lojistik bedeli, soğutucu enerji bedeli ve **geri ödeme vadesi** yer alır. | FACT | `EV-2026-08-10-612` |
| Perakendecilerin tedarikçiden aldığı bedel adları: raf bedeli, ürün listeleme bedeli, insert bedeli, enerji bedeli, teşhir bedeli, yılsonu iskontosu, kampanya bedeli, yeni ürün tanıtım bedeli, veri paylaşım bedeli, ciro primi. Ankete katılan **20 tedarikçinin tamamı** ödediğini beyan etmiştir. **Oranlar ticari sır olarak karartılmıştır.** | FACT | `EV-2026-08-10-610` |
| İndirim marketleri (BİM/A101/ŞOK tipi) ek bedel yerine **ürünün net fiyatı** üzerinden pazarlık yapmayı tercih eder. | FACT | `EV-2026-08-10-610` |

> **YAPISAL SONUÇ (bu ajanın en önemli tespiti):**
> Şarapta, listeleme bedelinin hukuki dayanağı olan **iki hizmet kategorisinden biri
> (tanıtım) kullanılamaz durumdadır.** Yani ödediğimiz bedelin karşılığında
> alabileceğimiz şey **yalnızca fiziksel raf/teşhir konumlandırmasıdır**.
> Aynı anda, `İP-2001` gereği tüketiciye ulaşmanın **başka yolu da yoktur**.
> Bu iki gerçek birlikte, kanalın pazarlık gücünü artıran ama **karşılığında
> alınabilecek hizmeti daraltan** asimetrik bir yapı üretir.

### 2.2 Marj — L7 → L8

| Alan | Değer |
|---|---|
| **claim** | Türkiye zincir perakendesinin **tüm kategori** brüt marjı için doğrulanmış tek güncel birincil sayı Migros 2025 konsolide finansallarıdır. |
| **value** | **%24,31** |
| **katmanlar** | **L7 → L8** |
| **brüt mü net mi** | **BRÜT** (satışların maliyeti düşülmüş, faaliyet gideri düşülmemiş) |
| **KDV** | **KDV HARİÇ** (net satış geliri KDV'siz raporlanır) |
| **margin mi markup mı** | **MARGIN on selling price**. Markup karşılığı **%32,12**'dir. |
| **status** | `FACT` (Migros için) → **şarap için `ESTIMATE`** |
| **tier** | T4 |
| **evidence_id** | `EV-2026-08-10-616` |

**Türetme zinciri:** 412.756.429 − 312.409.547 = 100.346.882 bin TL; 100.346.882 / 412.756.429 = 0,2431.

**Bu sayının şarap için NEDEN doğrudan kullanılamayacağı (üç ayrı hata kaynağı):**

1. **Kategori karması.** Tüm kategorilerin (taze, temizlik, kişisel bakım, private label)
   ağırlıklı ortalamasıdır. Şarap kategorisi ayrıştırılmamıştır.
2. **Alkol resmi analizin kapsamı dışında.** Rekabet Kurumu'nun beş büyük zincir için
   yaptığı brüt marj analizi *"alkol ve tütün hariç"* tanımlıdır ve **yayımlanan tüm marj
   oranları ticari sır olarak karartılmıştır** (`EV-2026-08-10-611`). Yani Türkiye'de
   zincir perakendenin **alkol brüt marjı hiçbir kamu kaynağında yoktur.**
3. **Raporlanan brüt marj, tedarikçiden alınan bedelleri içerir.** Rekabet Kurumu'nun
   metodolojisi satın alım maliyetinden *ciro primi + aktivite primi + iade tutarı +
   ürün imha bedeli + iskonto faturaları*'nı düşer (`EV-2026-08-10-611`). Yani
   **"perakendeci marjı" ile "tedarikçinin toplam yükü" aynı şey değildir**:
   `tedarikçi_toplam_yükü = m_retail + d` — bunlar birbirinin üstüne biner.

**Duyarlılık bandı (ASSUMPTION — modele band olarak girer, tek sayı olarak girmez):**

| Senaryo | `m_retail` (margin, KDV hariç, L7→L8) | markup karşılığı | Gerekçe |
|---|---|---|---|
| LOW | **%18** | %21,95 | Alkolde ÖTV nedeniyle birim fiyat yüksektir; yüksek birim fiyatlı kategorilerde yüzde marj tipik olarak baskılanır. Cash & carry formatı da aşağı çeker. |
| **BASE** | **%25** | %33,33 | Migros tüm-kategori %24,31'in hemen üstü; şarabın devir hızı gıdadan düşük ve raf işgali yüksektir. |
| HIGH | **%35** | %53,85 | Düşük devirli, yüksek raf maliyetli, "kategori uzmanlığı" gerektiren ürünlerde zincirlerin talep edebileceği üst uç. |

> Bandın **tamamı `ASSUMPTION`'dır.** Tek kanıtlı çapa `EV-616`'dır ve o da şarap değildir.
> `finans-fizibilite` bu üç senaryoyu **ayrı ayrı** çalıştırmalıdır.

### 2.3 Listeleme / giriş bedeli

| Alan | Değer |
|---|---|
| **status** | **`UNKNOWN`** |
| **Neden** | Türkiye'de zincir market listeleme bedeli için **güncel, doğrulanabilir, kamuya açık hiçbir tutar yoktur.** Rekabet Kurumu'nun 33 perakendeci + 20 tedarikçi ile yaptığı ankette bedellerin ciroya oranı **ticari sır olarak karartılmıştır** (`EV-2026-08-10-610`). |
| **Bulunabilen tek sayısal iz** | Capital dergisi, **2004**: "markete girme bedeli 10 bin dolardan başlıyor, 60 bin dolara kadar çıkıyor"; kategori kırılımı var, alkol/şarap **yok** (`EV-2026-08-10-619`). |
| **Bu izin modele girip giremeyeceği** | **GİREMEZ.** 22 yıllık, T5, birim tanımı yok (SKU mu ürün mü mağaza mı), hukuki çerçeve 2015 ve 2024'te tamamen değişti. |

**Yapısal olarak bilinen (FACT):**
- Bedel **sözleşmede türü + tutarı/oranı yazılmak zorundadır** (`EV-601`) → gizli kalem olamaz,
  pazarlıkta **görünür** olacaktır.
- 2015 orijinal metninde *"prim/bedel talebine konu ürünün sözleşme süresince **rafta
  satışa sunulması zorunludur**"* koruması vardı (`EV-2026-08-10-608`); **2024 metninde bu
  cümle aynen görünmemektedir.** Bu, "listeleme bedelini ödedik ama raftan çıkarıldık"
  riskinin hukuki zeminini değiştirmiş olabilir → **T-601**.

**Duyarlılık bandı (ASSUMPTION — `SENSITIVITY_ONLY`, base case değil):**

| Senaryo | Yapı | Şişe başına etki tabanı |
|---|---|---|
| LOW | Listeleme bedeli **yok**, karşılığı **net fiyat iskontosuna** gömülü (indirim marketi mantığı, `EV-610`) | `f = 0`, ama `d` yukarı kayar |
| BASE | SKU × zincir başına **tek seferlik giriş bedeli** + yıllık anlaşma | `f = giriş_bedeli / yıllık_şişe` |
| HIGH | SKU × **mağaza** başına bedel (mağaza sayısına bağlı yapı) + yıllık yenileme | `f = (bedel × mağaza_sayısı) / yıllık_şişe` |

> **Kritik uyarı — ölçek asimetrisi:** listeleme bedeli **sabit**, hacim **değişkendir**.
> 5.000 şişe/yıl senaryosunda aynı mutlak bedel, 100.000 şişe senaryosunun **20 katı**
> şişe başına maliyet üretir. Bu, pilot ekonomisini tek başına öldürebilecek bir kalemdir
> ve `finans-fizibilite` bunu **hacme bölünen sabit maliyet** olarak modellemek zorundadır.

### 2.4 Ciro primi ve diğer geri akan bedeller (`d` bileşenleri)

| Kalem | Varlığı | Tutarı/oranı | evidence |
|---|---|---|---|
| Ciro primi / yılsonu iskontosu | **FACT** | **UNKNOWN** (karartılmış) | `EV-610` |
| Alan kullanımı (teşhir/raf) | **FACT** (alkolde ismen) | **UNKNOWN** | `EV-612` |
| **Kırık ürün bedeli** | **FACT** (alkolde ismen) | **UNKNOWN** | `EV-612` |
| Lojistik bedeli (depo/dağıtım kesintisi) | **FACT** (alkolde ismen) | **UNKNOWN** | `EV-612` |
| Soğutucu enerji bedeli | **FACT** (alkolde ismen) | **UNKNOWN** | `EV-612` |
| CRM / B2B (kasa çıkışı cirosu) | **FACT** (alkolde ismen) | **UNKNOWN** | `EV-612` |
| İnsert / katalog bedeli | FACT (FMCG geneli) | UNKNOWN | `EV-610` |

**Metro'ya özel çelişki uyarısı:** `İP-502` (`EV-2026-08-09-508`) Metro'nun çek/sadakat
kampanyalarında **alkolün hariç tutulduğunu** gösterir. Buna karşılık `EV-2026-08-10-612`
Metro'nun alkollü içki tedarikçisiyle **yıllık satış anlaşması** imzaladığını ve bu
anlaşmada bedel kalemleri bulunduğunu gösterir. **Bunlar çelişmez**: tüketiciye yönelik
kampanya mekaniği ile tedarikçiden alınan ticari bedeller ayrı şeylerdir. Ancak
`İP-502`'nin "şarapta ciro primi çalışmıyor olabilir" okuması **doğrulanmamıştır** ve
`T-506`'nın cevabı budur: **ciro primi mekaniği alkolde de vardır, ama tüketici kampanya
mekaniği yoktur.**

**Duyarlılık bandı (ASSUMPTION):** `d` toplamı — LOW **%3** · BASE **%8** · HIGH **%18**
(fatura cirosu üzerinden, KDV hariç). Gerekçe: kalem sayısı en az 6'dır (`EV-612`), her
biri tek başına küçük olsa bile toplamları anlamlıdır; üst uç, listeleme bedelinin
tamamının orana çevrildiği senaryodur. **Bu bandın hiçbir kanıtlı çapası yoktur** — tek
dayanağı kalem sayısıdır. `seytanin-avukati` bu bandı hedef almalıdır.

### 2.5 Ödeme vadesi ve kredi riski — **modelin en iyi kanıtlanmış kalemi**

| Kaynak | Bulgu | Statü | evidence |
|---|---|---|---|
| **Yasal tavan** | 30 gün içinde bozulmayan **tarım ve gıda ürünlerinde** ödeme süresi, alacaklı küçük/orta + borçlu orta/büyük ise **60 günü geçemez** (yürürlük 01.01.2024) | FACT (kuralın metni) | `EV-2026-08-10-602` |
| **Şarabın kapsama girip girmediği** | Şarap 30-gün bozulabilir listesinde **yoktur**; "içecek" olarak hızlı tüketim malıdır | FACT | `EV-2026-08-10-604` |
| **"Şarap tarım ve gıda ürünüdür" tespiti** | **ASSUMPTION** — hukuki niteleme bu ajanın alanı değil | → **T-601** | — |
| **Yaptırım** | İlk 30 gün gecikmede günlük **binde 5**, sonrasında günlük **%1** idari para cezası | FACT | `EV-2026-08-10-603` |
| **Tavanın otomatik olmadığı** | Ölçek tespiti için **karşılıklı KOBİ Vasfı Belgesi** değişimi zorunludur | FACT | `EV-2026-08-10-607` |
| **Gözlenen fiili vade (süt, 2020)** | Organize kanal ortalaması **70 gün**; distribütör ~49 gün; geleneksel ~47 gün. 2011→2020: 64→70 gün. Raporun dipnotu: *"fiili süreler sözleşmedekinden çok daha uzun olabilmektedir."* | FACT (süt için) → ESTIMATE (şarap) | `EV-2026-08-10-609` |
| **Gözlenen zincir davranışı (2025)** | Migros ticari borçlarının **%34,4'ü 3–12 ay vadeli**; hesaplanan DPO **~93 gün**; borçlar **yıllık %38,6** ile iskonto ediliyor | ESTIMATE | `EV-2026-08-10-617` |

> **`C-601` (AÇIK ÇELİŞKİ):** Yasal tavan 60 gün diyor; gözlenen pratik 70–93 gün ve
> borçların üçte biri 3–12 ay vadeli. Bu, "kanun var ama fiiliyat farklı" olabileceği
> anlamına gelir; ya da Migros verisinin şarap/gıda dışı kalemleri de içermesinden
> kaynaklanıyor olabilir. **Bu ajan sessizce seçim yapmamıştır.**

**Model bandı (ESTIMATE + ASSUMPTION karışımı, ayrı ayrı etiketli):**

| Senaryo | Vade (gün) | Statü | Dayanak |
|---|---|---|---|
| LOW (bize iyimser) | **45** | ASSUMPTION | Yasal tavanın altında müzakere edilmiş vade |
| **BASE** | **60** | ESTIMATE | Yasal tavan (`EV-602`) + yaptırımın varlığı (`EV-603`) |
| HIGH | **90** | ESTIMATE | `EV-609` (70 gün, süt, 2020) ve `EV-617` (Migros DPO ~93 gün) arası |
| **STRESS** | **120** | ASSUMPTION | `EV-617`: borçların %34,4'ü 3–12 ay vadeli; `EV-609` dipnot 69 |

**Kredi riski:** Zincir marketlerde karşı taraf riski düşüktür (halka açık, denetlenen
şirketler) ama **konsantrasyon riski yüksektir**. Rekabet Kurumu, AB Komisyonu
kararlarına atıfla, bir sağlayıcının satışlarının **%22'sinin tek bir perakendeciye**
bağlı olması durumunda **ekonomik bağımlılık** eşiğinin aşıldığını kaydeder
(`EV-2026-08-10-609` ile aynı rapor, para.246). Tek zincirle çalışan bir pilot bu eşiğin
**çok üstünde** olacaktır.

### 2.6 İade ve fire/kırık sorumluluğu

| Bulgu | Statü | evidence |
|---|---|---|
| Satılamama gerekçesiyle iadeyi yasaklayan hüküm **yalnızca 30 gün içinde bozulabilen** tarım-gıda ürünleri içindir; %5'lik iade sınırı ise **yalnızca azami fiyatı tarifeyle belirlenen** mallar içindir. **Şarap her ikisinin de dışındadır.** | FACT | `EV-2026-08-10-606` |
| Sonuç: **şarapta satılmayan ürün iadesi için yasal sınır yoktur; iade tamamen sözleşmeseldir.** | FACT | `EV-606` |
| **Kırık ürün bedeli**, alkollü içki zincir yıllık anlaşmasında **"müşteriye ödenecek bedeller"** arasında ismen sayılmıştır → kırılma maliyeti sözleşmeyle **tedarikçiye yansıtılmaktadır**. | FACT | `EV-2026-08-10-612` |
| İade oranı (%) | **UNKNOWN** | — |

> **Cam şişe + iade riski + KDV birleşimi:** `Cİ-15.1` (gümrük-vergi ajanı) KDVK md.30/c
> uyarınca **zayi olan mala ait KDV'nin indirilemediğini** kaydetmiştir. Yani her %1 fire
> yalnızca malın maliyeti değil, **indirilemeyen KDV** olarak da geri gelir. Kırık ürün
> bedelinin sözleşmede olması, bu riskin **kanal tarafından bize itildiğinin** kanıtıdır.

### 2.7 Kampanya / fiyat indirimi katkısı

| Bulgu | Statü | evidence |
|---|---|---|
| **Kampanya maliyetini, kampanyalı satış yapmak istemeyen tarafa yansıtmak** her durumda haksız ticari uygulamadır. | FACT | `EV-2026-08-10-601` (6585 m.6/2(b)) |
| Buna karşılık, alkolde **promosyon/kampanya/hediye/bedelsiz ürün zaten yasaktır** (`K3`, `EV-2026-08-09-222`) → kampanya kaldıracı **nakit fiyat indirimi dışında yoktur**. | ACCEPTED CONSTRAINT | `İP-2001` |
| **ÖTV maktu ve fiyattan bağımsızdır** (`Cİ-11`, `EV-2026-08-09-111`) → indirim yapıldığında ödenen ÖTV **düşmez**; indirimin tamamı marjdan çıkar. | FACT (vergi ajanı alanı) | `EV-2026-08-09-111` |

> **Bu üçlü birleşim şarapta fiyat indiriminin FMCG'dekinden çok daha pahalı olduğunu
> gösterir:** indirim marjdan doğrudan düşer, vergiden hiçbir şey geri gelmez ve
> indirimi tüketiciye **duyurmak da yasaktır**.

---

## 3. KANAL B — INDEPENDENT RETAIL / TEKEL BAYİ · öncelik 2

### 3.1 Kanalın büyüklüğü ve yapısı

| Bulgu | Değer | Statü | evidence |
|---|---|---|---|
| Resmî taksonomi: **KSN** (kapalı satış noktası: bakkal, market, büfe, kuruyemişçi) → **GK** (geleneksel) + **MK** (modern/organize) | — | FACT | `EV-2026-08-10-613` |
| **GK'de alkollü içecek satan nokta sayısı (2020, TADB)** | **48.956** | FACT | `EV-2026-08-10-613` |
| Ürünler yalnızca **alkollü içki satış belgesi olan** kişilere satılabilir | — | FACT (mevzuat ajanı) | `EV-2026-08-09-224` |
| İthalatçının doğrudan perakendeciye satabilmesi için **toptan satış belgesi** gerekir (82.464 TL/yıl) | — | FACT (mevzuat ajanı) | `EV-2026-08-09-210/-211` |

### 3.2 Marj

| Alan | Değer |
|---|---|
| **status** | **`UNKNOWN`** |
| **Neden** | Yapılan aramada yalnızca T5 içerik-çiftliği sayfaları bulunmuştur ve bunlar **birbiriyle çelişmektedir**: "alkolde ~%17", "rakı %8", "brüt %10–15", "ciro üzerinden %18–30". **Hiçbiri** margin/markup ayrımını, KDV/ÖTV tabanını veya katman çiftini belirtmemektedir → **`M1` gereği hepsi geçersizdir.** |
| **evidence** | `EV-2026-08-10-620` (negatif kayıt) · `C-602` |

**Duyarlılık bandı (ASSUMPTION):**

| Senaryo | `m_tekel` (margin on selling price, KDV hariç, L7→L8) | markup |
|---|---|---|
| LOW | **%12** | %13,64 |
| **BASE** | **%18** | %21,95 |
| HIGH | **%25** | %33,33 |

**Gerekçe (ve bandın zayıflığı):** Alt uç, ÖTV nedeniyle çok yüksek birim fiyatlı bir
üründe bağımsız perakendecinin yüzde marjının sıkıştığı varsayımıdır. Üst uç, zincir
marjı ile aynı düzeye çıkabileceği varsayımıdır. **Bandın hiçbir noktasının kanıtı
yoktur.** Tek gerçek bilgi, `EV-2026-08-10-613`'ün ASN ile KSN fiyatları arasında
*"ciddi farklılıklar"* olduğunu söylemesidir — ki bu KSN'nin ASN'den **ucuz** olduğunu
söyler, marjını değil.

### 3.3 Diğer ticari koşullar

| Kalem | Durum | Not |
|---|---|---|
| Listeleme bedeli | **YOK (yapısal)** | 6585 m.6 **büyük mağaza, zincir mağaza, bayi işletme ve özel yetkili işletmeleri** hedefler; tek şubeli bağımsız bir tekel bayii "zincir mağaza" tanımına (en az 5 şube / en az 10 şube) girmez (`EV-2026-08-10-601` + Yönetmelik m.3/1(ü)). Pratikte bedel talebi **beklenmez**, ama `UNKNOWN`. |
| Ödeme vadesi | **ESTIMATE: 0–45 gün** | `EV-2026-08-10-609`: geleneksel kanal vadesi organize kanaldan **23 gün kısa** (2020, süt) → ~47 gün. Alkolde nakit/kısa vade beklentisi vardır ama **doğrulanmadı**. LOW 0 (peşin) · BASE 30 · HIGH 60. |
| Kredi riski | **YÜKSEK ve dağıtık** | Binlerce küçük nokta; tahsilat riski ve tahsilat maliyeti zincirden yapısal olarak yüksektir. Karşılık oranı **UNKNOWN**. |
| İade | **UNKNOWN** | Yasal koruma yok (`EV-606`); tamamen ticari teamül. |
| Minimum sipariş | **UNKNOWN** | Nokta başına düşen düşük hacim, dağıtım maliyetini şişe başına yukarı çeker (bkz. `kendi-dagitim-senaryosu.md`). |
| Yasal dağıtım yükümlülüğü | **NİTELENDİ** | `X-251` (mevzuat ajanı, `EV-2026-08-10-212`): Yönetmelik yükümlülüğü *"perakende satıcıların taleplerini zamanında karşılayacak dağıtımı sağlamak"*tır; "ülke genelinde yerinde teslim" ifadesi **yalnızca kanunda** geçer. Yani ulusal kılcal ağ zorunluluğu varsayımı TUR 1'de sanıldığından **daha zayıf** zemindedir. |

---

## 4. KANAL C — HoReCa (açık satış noktası / yerinde tüketim) · öncelik 3

### 4.1 Kanalın büyüklüğü ve yapısı

| Bulgu | Değer | Statü | evidence |
|---|---|---|---|
| **ASN** = bar, otel, restoran, kafe; "yerinde tüketim (YT)" olarak da anılır; HoReCa noktaları | — | FACT | `EV-2026-08-10-613` |
| **ASN nokta sayısı (2020, TADB)** | **29.218** | FACT | `EV-2026-08-10-613` |
| ASN'de satılan ürünün fiyatı ile KSN'de satılanın fiyatı arasında **"ciddi farklılıklar"** vardır | — | FACT | `EV-2026-08-10-613` |
| Alkolde satış noktasına **yatırım destek sözleşmesi** ile nakit destek (raf yaptırma, menü bastırma, etkinlik katkısı, personel maliyeti desteği) verilmesi **yerleşik bir uygulamadır**; ödemeler noktanın **belgelendirdiği fatura tutarları** oranındadır | — | FACT | `EV-2026-08-10-615` |
| Şarap kategorisinde satış noktalarıyla **beş yıllık** mal alım sözleşmesi imzalanmaktadır | 5 yıl | FACT | `EV-2026-08-10-614` |

> **Giriş engeli sinyali:** Türkiye'nin en büyük alkollü içki oyuncusu, **şarap
> kategorisinde** satış noktalarıyla **5 yıllık** sözleşme yapmaktadır (`EV-614`).
> Aynı karar, şarapta **münhasırlık olmadığının** beyan edildiğini de kaydeder
> (para.90) — yani bu bir münhasırlık iddiası değildir. Ancak yeni bir ithalatçı için
> **noktaların bir kısmının çok yıllık bağlı olması** gerçek bir erişim riskidir.
> Kaç noktanın bağlı olduğu **UNKNOWN** (tablolar karartılmış).

### 4.2 Fiyat çarpanı (HoReCa'da marj "çarpan" olarak konuşulur)

| Alan | Değer |
|---|---|
| **status** | **`ASSUMPTION`** (tek kaynak T5, 2012) |
| **Bulunan tek kaynak** | Şef Murat Bozok, Milliyet, 28.09.2012: teamül *"restorandaki şarabın fiyatı, perakende fiyatının **iki katı** ya da toptan fiyatının **2,5 katı** olmalıdır"*; gözlenen üst uç *"market fiyatının **4-5 kat** üzerinde"* (`EV-2026-08-10-618`) |
| **Sorun** | Çarpanın hangi katmandan (perakende mi toptan mı) hesaplandığı kaynağın kendisinde **iki farklı şekilde** geçer; KDV tabanı belirtilmemiştir; 14 yıllıktır. |

**Duyarlılık bandı (ASSUMPTION):** `L8_horeca = L7_horeca × k`

| Senaryo | `k` (çarpan, L7→menü fiyatı) | Eşdeğer margin on selling price |
|---|---|---|
| LOW | **2,0×** | %50,0 |
| **BASE** | **3,0×** | %66,7 |
| HIGH | **5,0×** | %80,0 |

> **KDV UYARISI:** HoReCa menü fiyatı KDV **dahildir** ve hizmet KDV oranı ile ürün KDV
> oranı **aynı olmayabilir**. Bu bir vergi sorusudur ve `gumruk-vergi-uzmani` alanıdır —
> bu ajan oran belirtmemektedir. Çarpan hesabı yapılırken hangi tabandan hesaplandığı
> **yazılmak zorundadır**.

### 4.3 Diğer ticari koşullar

| Kalem | Durum |
|---|---|
| Listeleme bedeli | Yerine **yatırım desteği / menü desteği / şarap listesi yerleşimi** geçer (`EV-615`). Tutar **UNKNOWN**. |
| Ödeme vadesi | **UNKNOWN**. HoReCa'da tahsilat riski üç kanalın en yükseğidir (mevsimsellik, işletme devir hızı). LOW 15 · BASE 45 · HIGH 90 (ASSUMPTION). |
| İade | **UNKNOWN**; şarapta HoReCa iadesi teamülen düşüktür ama doğrulanmadı. |
| Aktivasyon / tadım maliyeti | **YAPISAL RİSK:** tadım/eğitim etkinliği **tanıtım** sayılabilir; alkolde tanıtım kabul edilmiş kısıt kapsamındadır (`İP-2001`). Bu ajan bu kalemi modele **sıfır** koymaz, **UNKNOWN** bırakır ve `T-604` ile başkana taşır. |
| Kanal erişimi | 29.218 nokta (`EV-613`); kılcal ve emek yoğun; ithalatçının doğrudan satışı için **toptan satış belgesi** gerekir. |

---

## 5. ÜÇ KANALIN KARŞILAŞTIRMASI (özet tablo)

| Kalem | A) CHAIN RETAIL | B) TEKEL / BAĞIMSIZ | C) HoReCa |
|---|---|---|---|
| Nokta sayısı (2020) | UNKNOWN (MK tabloya alınmamış) | **48.956** (`EV-613`) | **29.218** (`EV-613`) |
| Marj tipi | margin on selling price | margin on selling price | **çarpan (multiplier)** |
| Marj/çarpan BASE | **%25** (ASSUMPTION) | **%18** (ASSUMPTION) | **3,0×** (ASSUMPTION) |
| KDV tabanı | hariç | hariç | menü fiyatı **dahil** |
| Listeleme bedeli | **VAR** (tutar UNKNOWN) | yapısal olarak yok | yatırım/menü desteği |
| Ciro primi | **VAR** (oran UNKNOWN) | UNKNOWN | UNKNOWN |
| Kırık/fire sorumluluğu | **sözleşmeyle bize** (`EV-612`) | UNKNOWN | UNKNOWN |
| Lojistik kesintisi | **VAR** (`EV-612`) | yok (biz taşırız) | yok (biz taşırız) |
| Ödeme vadesi BASE | **60 gün** (yasal tavan) | **30 gün** | **45 gün** |
| Vade stres | **120 gün** | 60 gün | 90 gün |
| Kredi riski | düşük / **konsantre** | yüksek / dağıtık | **en yüksek** |
| Tahsilat maliyeti | düşük | yüksek | yüksek |
| Bilinirlik inşa gücü | **yüksek** (raf) | orta | **yüksek** (deneme) |
| Reklamsız dünyada kaldıraç | raf konumu + fiyat | dağıtım genişliği | şarap listesi + garson tavsiyesi |

---

## 6. DAĞITIM MODELİ A/B — YAPI KARŞILAŞTIRMASI

> Kırılma noktası **hesabı** `finans-fizibilite`'ye aittir. Burada yalnızca **girdi yapısı**
> ve **ekonomik mantık** verilmiştir. Doldurulacak alanlar: `kendi-dagitim-senaryosu.md`.

| Boyut | A) KENDİ DAĞITIMIMIZ | B) DIŞ DİSTRİBÜTÖR |
|---|---|---|
| Marj devri | Yok — L6→L7 marjı bizde kalır | **Var** — distribütör marjı L6 ile L7 arasına girer (`UNKNOWN`) |
| Maliyet tipi | **SABİT** (personel, araç, depo) | **DEĞİŞKEN** (% ciro) |
| Ölçek davranışı | Düşük hacimde **yıkıcı**, yüksek hacimde üstün | Her hacimde doğrusal |
| Kanal erişimi | Sıfırdan kurulur; GK 48.956 + ASN 29.218 nokta (`EV-613`) | Hazır |
| Belge maliyeti | Her depo için **ayrı toptan satış belgesi** (`L4`, mevzuat ajanı) | Distribütörün belgesi kullanılır |
| Vade riski | **Bizde** (CCC uzar) | Distribütörde (ama o da bize vade dayatır) |
| Kontrol | Fiyat, raf, tahsilat bizde | **Bağımlılık riski**; üretici markup tavanı dayatabilir (`İP 5.2`) |
| Reklamsız dünyada | Kılcal dağıtım = tek bilinirlik kanalı → **stratejik değeri yüksek** | Distribütörün önceliği bizim SKU'muz olmayabilir |

**Kırılma noktası mantığı (formül — sayı değil):**

```
Kendi dağıtım ekonomik hale gelir  <=>  yıllık_sabit_dagitim_maliyeti
                                        <  hacim × L6 × distribütör_marj_oranı
```

`distribütör_marj_oranı` **UNKNOWN**'dır ve bu turda hiçbir kanıtlı değer bulunamamıştır.
`yıllık_sabit_dagitim_maliyeti` için tek kanıtlı taban `EV-2026-08-10-621`'dir
(2026 asgari ücret işveren maliyeti, imalat dışı: **40.214,03 TL/ay/kişi**).

---

## 7. YALNIZCA GERÇEK KANAL GÖRÜŞMESİYLE ÖĞRENİLEBİLECEK ALANLAR

> Bunlar masabaşı araştırmayla **kapatılamaz**. TUR 7 işidir ve başkan onayı gerektirir (`T-604`).

| # | Alan | Neden masabaşı kapanmaz |
|---|---|---|
| 1 | Listeleme / giriş bedeli **tutarı** | Resmî sektör raporunda bile ticari sır olarak karartılmış (`EV-610`) |
| 2 | Ciro primi **oranı** ve kademeleri | Aynı (`EV-610`) |
| 3 | Alan kullanımı / kırık ürün / lojistik / enerji bedeli **tutarları** | Kararda ismen var, tutar karartılmış (`EV-612`) |
| 4 | Zincirin şarap kategorisi **hedef marjı** | Alkol resmî marj analizinin kapsamı dışı (`EV-611`) |
| 5 | Fiili **ödeme vadesi** (sözleşme vs pratik) | Sözleşme süresi ≠ fiili süre (`EV-609` dipnot 69) |
| 6 | **İade oranı** ve iade koşulları | Yasal düzenleme yok, tamamen sözleşmesel (`EV-606`) |
| 7 | Tekel bayii **marjı** ve iskonto yapısı | Yalnızca çelişen T5 kaynak (`EV-620`, `C-602`) |
| 8 | HoReCa **çarpanı** ve şarap listesi yerleşim bedeli | Tek kaynak T5 ve 14 yıllık (`EV-618`) |
| 9 | Dış distribütör **marj oranı** | Hiçbir kanıt bulunamadı |
| 10 | Metro **mağaza fiyatı vs sevkiyat fiyatı** farkı | `İP-501` / `T-506`; Metro fiyatları müşteriye özel (`İP-505`) |
| 11 | Zincirin şaraba ayırdığı **raf/SKU kotası** | Hiçbir kamu kaynağı yok |
| 12 | Minimum sipariş, teslimat sıklığı, sipariş kanalı | Sözleşme eki |

---

## 8. BU DOSYADAN ÇIKAN MODEL GİRDİLERİ

`80-model/inputs/kanal.yaml` dosyasına yazılmıştır. **evidence_id'si olmayan hiçbir değer
`value` alanına yazılmamış**, duyarlılık bantları ayrı bir `duyarlilik_senaryolari`
bloğunda `modele_girme_kurali: SENSITIVITY_ONLY` etiketiyle tutulmuştur.
