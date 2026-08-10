# PRE-RFQ INVESTMENT REPORT — ÖN FİZİBİLİTE VE GO/NO-GO

```yaml
belge:            PRE-RFQ-INVESTMENT-REPORT-v1
yazan:            yatirim-komitesi-baskani
tarih:            2026-08-10
tur:              PRE-RFQ GATE (TUR 3.25 sonrasi, TUR 3B oncesi)
okuyucu:          KURUCU / YATIRIMCI
karar_tipi:       PRELIMINARY GATE DECISION  (KILL | HOLD | PROCEED TO RFQ)
karar_tipi_degil: "IMPORT PILOT / SCALE / nihai yatirim karari VERILMEMISTIR"
yeni_arastirma:   YOK
web_aramasi:      YOK
ajan_cagrildi:    HAYIR
dis_iletisim:     NONE  (hicbir tedarikciye/forwarder'a mesaj gonderilmedi)
yeni_kanit:       0     (10-evidence/ dokunulmadi)
kanit_tabani:     "321 kanit karti - T1:91 T2:43 T3:33 T4:120 T5:32"
acik_CRITICAL:    12
toplam_ticket:    151
```

> ## BU BELGENİN SINIRI — İKİ CÜMLE
> Bu bir **ön fizibilite kararıdır.** Verilen karar yalnızca *"gerçek firmalarla
> görüşmeye ve numune/teklif toplamaya devam edilsin mi?"* sorusunu cevaplar.
> **`IMPORT PILOT` veya `SCALE` kararı bu belgede VERİLMEMİŞTİR ve verilemez** —
> onlar için gereken gerçek satın alma fiyatı, gerçek navlun ve gerçek kanal
> verisi henüz **elimizde yoktur.**

---
---

# 1. YÖNETİCİ ÖZETİ

## EXECUTIVE VERDICT

```
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   KARAR :  PROCEED TO RFQ                                        ║
║   TIP   :  PRELIMINARY  (nihai yatirim karari DEGILDIR)          ║
║   GUVEN :  MEDIUM                                                ║
║   BUTCE :  Sinirli — masabasi + iletisim; SIPARIS YOK, MAL YOK   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

**Tek cümlelik gerekçe:** Bu işi bugün öldürecek bir bulgu **yoktur**; ama bu işi
bugün onaylayacak bir bulgu da yoktur — ve eksik olan tek şey (gerçek tedarikçi
fiyatı) **yalnızca RFQ ile öğrenilebilir**, daha fazla masabaşı çalışmayla değil.

---

## 1.1 İş fırsatı nedir

Türkiye'de ithal şarap, gözlemleyebildiğimiz kanallarda **belirgin biçimde
yukarıda** duruyor. Erişebildiğimiz tek çok-SKU'lu perakende kanalında
**stokta bulunan en ucuz ithal şarap 875 TL**; aynı kanalda stokta bulunan
471 SKU'nun yerli medyanı **1.410 TL** (`EV-2026-08-10-702`). Buna karşılık
Metro rafında **599,90 TL** ve **649,90 TL** etiketli **iki ithal şarap fiilen
görülmüştür** (`EV-2026-08-09-501/-502`).

Yani 600–900 TL bandında **yerli şarap yoğun biçimde vardır** (±%10 pencerede
799 TL'de 31 stokta yerli SKU) ama **ithal şarap pratikte yoktur.** Fırsat
hipotezi budur: *"yerli fiyatına ithal şarap."*

⚠ **Bu hipotez tam olarak doğrulanmamıştır** — bkz. §4 ve §5.

## 1.2 Ne ithal edeceğiz

**750 ml, still (köpüksüz), kuru BEYAZ şarap; giriş/value kademe.**
İki ürün profili tasarlandı (§3):
- **PRODUCT 1 — VALUE HERO:** yumuşak, meyveli, düşük tanik beyaz —
  *Colombard-Chardonnay · Airén-Chardonnay · Trebbiano/Garganega* tarzı blend
- **PRODUCT 2 — STEP-UP:** tek çeşit, tanınabilir isim —
  *Chardonnay* veya *Sauvignon Blanc*

**İlk pilotta önerilen SKU sayısı: 2.** (Gerekçe §3.4.)

## 1.3 Hangi fiyat boşluğu

| Bant | Stokta yerli SKU | Stokta **ithal** SKU |
|---|---|---|
| 500–600 TL | **0** | **0** |
| 600–700 TL | 7 | **0** |
| 700–800 TL | 18 | **0** |
| 800–900 TL | 19 | **1** (875) |
| 900–1.000 TL | 21 | **1** (948) |
| 1.200+ TL | 251 | **75** |

*(`EV-2026-08-10-702`, tek kanal, 2026-08-10, stokta olanlar)*

**Boşluk 600–875 TL bandındadır ve `PARTIALLY SUPPORTED`'dır** — çünkü aynı
kanal 600 TL altında **yerli** şarap da taşımıyor. Boşluğun bir kısmı gerçek,
bir kısmı **kanal artefaktıdır** (§4.4).

## 1.4 PRIMARY satış fiyatı

**799 TL** — KDV dahil, 750 ml, tüketici rafı.
Statü: **`CURRENT DESIGN TARGET`** — kesin satış fiyatı **değildir**, bir
**pazarlık ve tasarım çapasıdır** (§6).

Merdiven: `599 FLOOR TEST` · `699 SECONDARY` · **`799 PRIMARY`** ·
`899 STRETCH` · `999 UPPER SEGMENT TEST`.

## 1.5 Hedef müşteri

Şarap içen ama **1.000 TL üstü şarap almayan** tüketici; "günlük içim" beyaz
şarap arayan, markadan çok fiyat/kalite dengesine bakan, ithal ürünü statü değil
**tercih** olarak gören segment.

⚠ **Bu bir tanımdır, bir ölçüm değildir.** Türkiye'de şarap talebi için elimizde
**tek bir veri yoktur** (`C-561`). Bu, raporun en büyük tek boşluğudur.

## 1.6 Hedef kanallar

| Rol | Kanal |
|---|---|
| **PRIMARY** | CHAIN RETAIL (Migros, Macrocenter, CarrefourSA) + Metro cash & carry |
| **SECONDARY** | INDEPENDENT / tekel bayii (48.956 nokta, `FACT` T2) |
| **OPPORTUNISTIC** | HoReCa (29.218 nokta, `FACT` T2) |

## 1.7 Hangi ülkeler

**TIER 1:** İspanya · Portekiz
**TIER 2:** İtalya · Şili · Fransa · Moldova
**LOW PRIORITY:** Güney Afrika · Avustralya · ABD/California

Belirleyici olan **iki** şeydir: (a) tercihli tarife (%50 vs %70 — şişe başına
**32,10 TL** fark), (b) Türkiye'ye çalışan bir ihracat hattının fiilen var olması.

## 1.8 Kaça almalıyız

**Yapısal tavan** (799 TL raf · zincir · BASE senaryo · 5.000 şişe):

| Grup | TRY/şişe (CIF) | EUR/şişe | USD/şişe |
|---|---|---|---|
| **P — tercihli (%50), belge OK** | **272,83** | 4,95 | 5,72 |
| **N — tercihsiz (%70) veya belge yok** | **240,73** | 4,37 | 5,05 |

> ⛔ **BUNLAR HEDEF ALIŞ FİYATI DEĞİLDİR.** Bunlar **yapısal tavanlardır** —
> "bu fiyatın üstünde alırsak model kapanmaz" sınırıdır. Tedarikçiye söylenecek
> sayı değildir ve **kâr içermez** (§10, §12).

## 1.9 Kaç şişe satmalıyız

| Senaryo | Şişe/yıl | Şişe/ay | 20 şişe/ay/nokta ile gereken nokta |
|---|---|---|---|
| PILOT | 5.000 | 417 | **21** |
| VALIDATION | 10.000 | 833 | **42** |
| COMMERCIAL | 25.000 | 2.083 | **104** |
| GROWTH | 50.000 | 4.167 | **208** |
| SCALE | 100.000 | 8.333 | **417** |

⚠ Nokta başına devir hızı **`ASSUMPTION`**'dır — Türkiye'de şarap için tek bir
store velocity gözlemimiz yoktur (§8).

## 1.10 En büyük avantaj

**Vergi tarafı sağlam ve satır satır hesaplanabiliyor.**
GTİP, gümrük vergisi, ÖTV, KDV, KKDF ve **matrah sırası** T1 (Resmî Gazete /
kanun) düzeyinde doğrulanmış, 10/10 birim testle korunmuştur. Bir ithalat
projesinde en sık öldürücü hata olan **vergi sürprizi riski burada düşüktür.**

Ayrıca ölçek ekonomisinin **%87'si 5.000 → 25.000 sıçramasında** gerçekleşiyor —
yani **büyük olmak gerekmiyor**, orta ölçek ekonominin çoğunu veriyor.

## 1.11 En büyük problem

**İki tane var ve ikisi de aynı cinsten:**

1. **Alış fiyatı bilinmiyor.** 26 tedarikçinin **26'sından da teklif
   alınmamıştır.** Havuzdaki tek yayınlanmış şişe fiyatının bile **para birimi**
   (AUD mı USD mi) ve **katmanı** (EXW mi FOB mu) `UNKNOWN`'dır. Bu, `T-466`
   (**CRITICAL, OPEN**).
2. **Satış tarafı da bilinmiyor.** Hedeflediğimiz rafta (`L8_CHAIN_RETAIL`)
   **sıfır fiyat gözlemimiz** var, ve Türkiye'de şarap için **sıfır talep
   verimiz** var.

> Yani model, **iki ucu da tahmine dayanan bir köprüdür.** Ortası (vergi,
> lojistik, mevzuat) sağlam; **iki ayağı da havada.**

## 1.12 Devam etmeye değer mi?

**EVET — ama yalnızca bir sonraki adım için, ve sadece bilgi almak için.**

RFQ göndermek şirket kurmayı, mal almayı veya para bağlamayı **gerektirmez.**
Maliyeti birkaç haftalık takip emeğidir. Karşılığında modelin **en büyük
belirsizliğini** (gerçek FOB) kapatır. Bu, elimizdeki en yüksek bilgi/maliyet
oranına sahip ikinci eylemdir.

**Birincisi ise RFQ değildir:** bir **fiziksel mağaza turudur** — tek ziyarette
beş açık soruyu birden kapatır ve maliyeti neredeyse sıfırdır (§27, madde 1).

---
---

# 2. İŞ MODELİ

## 2.1 Tek paragraf tanım

Türkiye'de bir ithalat/dağıtım şirketi kurulur; TADAB dağıtım yetki belgesi ve
toptan satış belgesi alınır. Avrupa veya Yeni Dünya'dan **750 ml şişelenmiş,
bitmiş beyaz şarap** satın alınır, deniz yoluyla getirilir, gümrük antreposunda
**bandrollenir ve Türkçe etiketlenir**, serbest dolaşıma sokulur ve zincir
market / tekel bayii / HoReCa kanallarına satılır. Tüketici rafında hedef fiyat
**799 TL** (KDV dahil); ithalatçının kazancı, tüketici fiyatından geriye doğru
düşülen kanal marjı, vergiler ve operasyon maliyeti sonrasında kalan farktır.

## 2.2 A) PRIVATE LABEL (kendi markamız)

| Boyut | Durum |
|---|---|
| **Ne** | Üreticiye kendi marka, etiket ve reçetemizle ürettiririz |
| **Doğrulanmış MOQ** | **3.000 şişe** (Interbrosa, ES) · **3.600** (The Wine Factory, FR) · **6.000** (Harland AU, Cantina Danese IT) |
| **Pilot uyumu** | ✅ 3.000–3.600 MOQ'lar **5.000 şişelik pilotla uyumlu** |
| **Marka değeri** | Bizde kalır (⚠ reçete/IP sahipliği **doğrulanmadı** — RFQ 4.9) |
| **Fiyat kontrolü** | Yüksek |
| **Tedarikçi değiştirilebilirliği** | Yüksek — ama IP üreticideyse **çöker** |
| **Zayıflığı** | Marka bilinirliği **sıfırdan** inşa edilir; alkolde **reklam yasağı** var (`7584 s.K. m.2`) → hikâye anlatacak mecra yok |

## 2.3 B) EXISTING BRAND (mevcut marka distribütörlüğü)

| Boyut | Durum |
|---|---|
| **Ne** | Üreticinin hazır markasını Türkiye'de dağıtırız |
| **Doğrulanmış MOQ** | **HİÇBİRİ** — 4 Model A adayının 4'ünde de `UNKNOWN` |
| **Pilot uyumu** | **UNKNOWN** |
| **Marka değeri** | Üreticide kalır; sözleşme biterse yatırım sıfırlanır |
| **Fiyat kontrolü** | Sınırlı; üretici yeniden satış fiyatı tavanı koyabilir |
| **Avantajı** | Etiket, analiz dosyası, sertifikalar **hazır**; hız |
| **Zayıflığı** | Türkiye bölgesi **kapalı olabilir** — 26 tedarikçiden **1'inde (Cantina Danese) fiilen kapalı çıktı** (`T-565`) |

## 2.4 Hangisi daha cazip / kolay / riskli

| Kriter | Kazanan | Neden |
|---|---|---|
| **Pilot ölçekte uygulanabilirlik** | **PRIVATE LABEL** | Tek doğrulanmış düşük MOQ'lar burada |
| **Hız** | **EXISTING BRAND** *(muhtemelen)* | Etiket/dosya hazır — ama lead time verisi yok |
| **Uzun vadeli işletme değeri** | **PRIVATE LABEL** | Marka bizde |
| **Kısa vadeli risk** | **EXISTING BRAND** daha düşük | Ürün zaten var, kalite bilinen |
| **Tedarikçiye bağımlılık** | **PRIVATE LABEL** daha düşük | Değiştirilebilir *(IP bizdeyse)* |

> ### ⚠ ÖNEMLİ UYARI — ARAMA YANLILIĞI
> Private label'ın bu raporda **daha zengin görünmesi**, modelin daha iyi
> olduğunu **göstermez.** Private label sağlayıcıları kendilerini web'de
> "private label" diye pazarlar; marka sahipleri distribütör arayışını **fuarda
> ve doğrudan temasla** yürütür. `global-sourcing-kasifi` bunu kendisi kayda
> geçirmiştir. **İki model charter'da eşit önceliklidir ve öyle kalır.**

**PRE-RFQ aşamasındaki değerlendirmem §17'dedir.**

---
---

# 3. HEDEF ÜRÜN

## 3.1 PRODUCT 1 — VALUE HERO

| Alan | Tanım | Statü |
|---|---|---|
| **Tip** | Still (köpüksüz), kuru beyaz | tasarım |
| **Hacim** | 750 ml | `ASSUMPTION` (`T-925`) |
| **Üzüm / blend** | **Colombard-Chardonnay** · **Airén-Chardonnay** · **Trebbiano/Garganega** · eşdeğer nötr-meyveli blend | tasarım |
| **İdeal ABV** | **%11,5 – 12,5** | tasarım — *ABV `UNKNOWN`, benchmark'ın ABV'si bile okunamadı* |
| **Ambalaj** | Standart Bordeaux/Burgundy cam, vidalı kapak veya mantar; **hafif şişe tercih** *(navlun hacimden ücretlenir)* | tasarım |
| **Hedef tüketici** | Günlük içim, fiyat duyarlı, marka bağımsız | tasarım |
| **Kalite algısı** | "Yerli fiyatına düzgün ithal" | tasarım |
| **Hedef raf fiyatı** | **799 TL** (SECONDARY 699) | `CURRENT DESIGN TARGET` |

**Neden bu blend ailesi:** Benchmark ürünün kendisi bir
**Colombard-Chardonnay**'dir (Gold Country, California). Côtes de Gascogne bu
stilin **yapısal kaynağıdır** ve Plaimont/Colombelle o apelasyonun amiral
markasıdır. İspanya'da Airén-Chardonnay eşdeğeri, İtalya'da
Trebbiano/Garganega eşdeğeri aynı işlevi görür: **nötr, meyveli, düşük asitli,
ucuz üretilebilir beyaz.**

## 3.2 PRODUCT 2 — STEP-UP

| Alan | Tanım |
|---|---|
| **Üzüm** | **Chardonnay** (tek çeşit) veya **Sauvignon Blanc** |
| **İdeal ABV** | %12,0 – 13,0 |
| **Ambalaj** | Aynı format, daha ağır etiket / daha koyu cam algısı |
| **Hedef tüketici** | Çeşit adını tanıyan, "Chardonnay" diye arayan tüketici |
| **Kalite algısı** | Bir adım yukarı, hâlâ f/p |
| **Hedef raf fiyatı** | **899 TL** (STRETCH) |

**Neden Sauvignon Blanc / Chardonnay:** Havuzdaki **tek** doğrulanmış Şili
üreticisinin (Corta Hojas) beyaz portföyü tam olarak **Sauvignon Blanc +
Chardonnay**'dir ve görev tanımıyla **birebir eşleşmektedir**
(`EV-2026-08-10-464` bağlamı). Bu iki çeşit **isim olarak tanınır** — reklam
yasağı altında bu bir avantajdır: rafta ürünün kendisi kendini anlatır.

## 3.3 Çeşit değerlendirmesi

| Çeşit / blend | Uygunluk | Not |
|---|---|---|
| **Colombard-Chardonnay** | ⭐⭐⭐ | Benchmark'ın kendisi; FR Gascogne yapısal kaynak |
| **Airén-Chardonnay** | ⭐⭐⭐ | İspanya'nın en ucuz beyaz tabanı; ES tedarik en güçlü rota |
| **Chardonnay (tek çeşit)** | ⭐⭐⭐ | En tanınır beyaz çeşit adı; STEP-UP için ideal |
| **Sauvignon Blanc** | ⭐⭐ | Tanınır; Şili'de doğrulanmış portföy — ama CL rotası 43 gün ve aktarma riski taşıyor |
| **Verdejo** | ⭐⭐ | İspanya'ya özgü, iyi f/p — ama Türkiye'de **tanınmıyor**; eğitim yükü var |
| **Trebbiano / Garganega** | ⭐⭐ | İtalya'nın ucuz beyaz tabanı — ama **İtalya rotası tamamen `UNKNOWN`** |
| **Pinot Grigio** | ⭐⭐ | Tanınır, ama İtalya'da fiyat baskısı var; rota `UNKNOWN` |

## 3.4 İlk pilotta kaç SKU — **ÖNERİ: 2**

| Seçenek | Artı | Eksi | Değerlendirme |
|---|---|---|---|
| **1 SKU** | En düşük sermaye, en basit operasyon, MOQ en kolay karşılanır | Rafta **tek yüz** — zincirde listeleme gücü zayıf; yanlış çeşit seçilirse tek şansı kaybederiz | Çok dar |
| **2 SKU** ✅ | İki çeşit denenir; raf blok oluşur; **öğrenme iki kat** | MOQ ×2 → 6.000–7.200 şişe; sermaye artar | **ÖNERİLEN** |
| **3 SKU** | En güçlü raf varlığı | MOQ ×3; stok riski; pilotun amacı öğrenmek, envanter değil | Erken |

> **Gerekçe:** Pilotun amacı **satmak değil, öğrenmektir.** 1 SKU tek bir
> hipotezi test eder; 2 SKU **iki fiyat noktasını** (799 ve 899) ve **iki çeşit
> algısını** aynı sevkiyatta test eder. MOQ tarafında da uyumludur: 3.000
> şişe/SKU MOQ'lu bir tedarikçide (Interbrosa) **2 SKU = 6.000 şişe** ve bu
> LCL/FCL kırılma noktasının (~5.900) hemen üstüdür — yani konteyner
> ekonomisiyle de tutarlıdır.
>
> ⚠ **Ama dikkat:** 6.000 şişe **iki farklı SKU** demektir ve tek bir SKU'nun
> MOQ'su 3.000'in altına inmiyorsa **her SKU ayrı MOQ'ya tabidir.** Bu, RFQ'da
> açıkça sorulan sorulardan biridir.

---
---

# 4. RAKİPLER

## 4.1 Ana tablo — istenen bantlar

**Kaynak A (yoğunluk sayımı):** `EV-2026-08-10-702` — tek çok-SKU'lu kanal,
2026-08-10, **stokta olanlar**, n=471 (391 yerli + 80 ithal).
**Kaynak B (isimli örnek):** `60-pazar/raf-fiyat-gozlemleri.csv`, 117 gözlem
(110 online + 7 cash & carry).

| Bant (TL) | Stokta **yerli** | Stokta **ithal** | Başlıca markalar (gözlenmiş) | Menşe | Kanal |
|---|---|---|---|---|---|
| **< 599** | **1** *(Mistia 460)* | **0** | Mistia, Doluca 480, Grand Reserve 570 | TR | online / cash&carry |
| **599 – 699** | **7** | **0** *(online)* / **2** *(Metro)* | Asmadan 649 · KA Winery 655 · Lermonos 655 · Umurbey 659 · Nif Bağları 670 · Mistia 672 — **hepsi yerli**. Metro: **Gold Country 599,90 (ABD)** · **Central Creek 649,90 (AU)** | TR + 2 ithal | online + Metro |
| **700 – 799** | **18** | **0** | Vinkara 710–754 · KA Winery 745 · Turasan 758 · Çamlıbağ 760 · Diren 790 · Barel 790 | TR | online |
| **800 – 899** | **19** | **1** | Büyülübağ 792–854 · Kastro Tireli 816–820 · Gaya 820 · Ni&Ce 860 · Antioche 861 — **+ Tesori Prosecco 875 (IT)** | TR + IT | online |
| **900 – 999** | **21** | **1** | *(yerli yoğunluk)* + **La Piuma / MGM Chianti 948 (IT)** | TR + IT | online |
| **1.000 – 1.249** | ⚠ ayrıştırılamıyor | ⚠ ayrıştırılamıyor | Marchesi Antinori 1.138 · Louis Bernard 1.145 · Concha y Toro 1.189 · Kavaklıdere 1.100 | IT/FR/CL/TR | online |
| **1.250 – 1.499** | ⚠ ayrıştırılamıyor | ⚠ ayrıştırılamıyor | Alamos 1.360 (AR) · Château de Seguin 1.405 (FR) · Sarafin 1.400 (TR) | AR/FR/TR | online |
| **1.500 +** | ⚠ ayrıştırılamıyor | ⚠ ayrıştırılamıyor | Marchesi di Barolo 1.700–1.714 · Escudo Rojo 1.782 · Uvas Felices 1.957 · Clarence Dillon 1.959 | IT/CL/ES/FR | online |

> ### ⚠ KANIT SINIRI — GİZLENMİYOR
> Yoğunluk sayımı **100 TL çözünürlükte** kaydedilmiştir ve **1.200 TL üstü tek
> bir kova** olarak durur (**251 yerli / 75 ithal**). İstenen `1.000–1.249` ·
> `1.250–1.499` · `1.500+` bantlarını **ayrıştıracak kanıt YOKTUR.**
> Bu üç satırdaki marka isimleri **isimli örnekten** gelir (n=117), bir
> **sayımdan değil**. Sayı uydurmadım.

## 4.2 Bilinen ölçüler

```
Stokta yerli   : n = 391   min   460 TL   MEDYAN 1.410 TL
Stokta ithal   : n =  80   min   875 TL
600-1.000 TL   : 65 yerli / 2 ithal (stokta)
Tum katalogda 600 TL altinda STOKTA olan SKU sayisi : 1
```

## 4.3 Ana soru: **"400–800 TL bandında ithal şarap boşluğu var mı?"**

# → `PARTIALLY SUPPORTED`

**Boşluğu DESTEKLEYEN kanıt:**
- Gözlenen kanalda 875 TL altında **stokta tek bir ithal SKU yoktur** — bu bulgu
  **iki ayrı tarihte birebir tekrarlanmıştır** (`EV-2026-08-10-501`, `-551`).
- Aynı bantta **65 yerli SKU** stokta durmaktadır — yani fiyat noktası
  **ticari olarak vardır**, sadece ithal ürün yoktur.

**Boşluğu ZAYIFLATAN kanıt (TUR 2.5 tespiti — gizlenmiyor):**
- Aynı kanal **600 TL altında hiçbir şarap taşımıyor** — yerli dahil. Tüm
  katalogda 600 TL altında stokta **1 SKU** var ve stokta yerli medyan
  **1.410 TL**. Kanalın ağırlık merkezi hedef merdivenin **1,4–2,4 katı
  üstündedir.** Yani okuduğumuz şey kanalın **alt kuyruğudur.**
- **62 ithal listeleme katalogda tanımlı ama stok dışıdır** (`C-561`).
  "Stokta ithal yok" bir **boşluk** değil, bir **dönmeme** işareti olabilir —
  yani ürün konuldu ama satmadı.

**Boşluğu ÇÜRÜTEN kanıt:**
- Metro rafında **599,90 ve 649,90 TL etiketli iki ithal şarap fiilen
  görülmüştür.** Yani boşluk **pazar geneli değildir.** İki kanal bu konuda
  **birbiriyle çelişmektedir ve çelişki çözülmemiştir.**

> ### DÜRÜST OKUMA
> Doğru cümle şudur: *"Gözlemleyebildiğimiz tek çok-SKU'lu kanal, 875 TL altında
> ithal şarap stoklamamaktadır; Metro ise 599,90 TL'de ithal şarap
> stoklamaktadır. Türkiye genelinde 400–800 TL bandında ithal şarap olup
> olmadığını BİLMİYORUZ."*
>
> Bunu bilmenin yolu masabaşı değildir — **üç turdur yapılmamış olan tek
> fiziksel mağaza turudur** (`T-917`).

## 4.4 Rekabetin gerçek yapısı — yönetim okuması

1. **Asıl rakibimiz ithal şarap değil, YERLİ şaraptır.** 600–900 TL bandında
   44 yerli SKU stokta duruyor, 2 ithal. Bu bantta ithal bir ürünle girmek
   demek, **Vinkara, Turasan, Doluca, Büyülübağ ile aynı rafta ve aynı fiyatta**
   olmak demektir — marka bilinirliği **sıfırken.**
2. **İthal şarap 875 TL'nin üstünde "dönüyor" olabilir.** Eğer öyleyse hedefimiz
   yanlış banttadır ve 899 TL doğru fiyattır. Bu ihtimal **çürütülmemiştir.**
3. **Reklam yasağı rekabeti tamamen rafa taşır.** `7584 s.K. m.2` (yürürlük
   20/6/2026) satış noktasında marka/logo görselini bile kısıtlar. Yani
   konumlandırma **etiket + fiyat + raf yeri** ile yapılacaktır, başka araç
   yoktur.

---
---

# 5. BENCHMARK ÜRÜNLER

## 5.1 GOLD COUNTRY — 599,90 TL

```
┌──────────────────────────── FACT — BİLDİKLERİMİZ ────────────────────────────┐
│ Urun    : Gold Country California Colombard-Chardonnay 2023                  │
│ Hacim   : 750 ml                                                             │
│ Mense   : California, ABD                                                    │
│ Fiyat   : 599,90 TL  — FOTOGRAFTAN OKUNDU (FACT_FROM_PHOTO)                  │
│ Kanal   : Metro Turkiye (cash & carry)                                       │
│ Tarih   : 2026-08-09                                                         │
│ KDV     : KDV DAHIL  (Metro brosurlerinde her fiyatin yaninda "KDV'li")      │
│ Katman  : L8_METRO_CASH_CARRY — zincir market L8'i DEGILDIR                  │
│ Musteri : Metro bireysel musteriye ucretsiz gunluk kartla ACIK               │
│ evidence: EV-2026-08-09-501, -503, -504, -505, -506, -507                    │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────── UNKNOWN — BİLMEDİKLERİMİZ ─────────────────────────┐
│ ⛔ PROMOSYON DURUMU        — normal fiyat mi, indirimli mi?   T-504 (OPEN)   │
│ ⛔ Zincir market karsiligi — Migros'ta kac TL?  L8_CHAIN_RETAIL = 0 gozlem   │
│ ⛔ ABV                                                                       │
│ ⛔ Sehir / magaza                                                            │
│ ⛔ Uretici kimligi         — hangi bodega uretti?  (T-405 OPEN)              │
│ ⛔ Bu fiyatin surekliligi  — tek gozlem, tek tarih, snapshot repoda YOK      │
└──────────────────────────────────────────────────────────────────────────────┘
```

## 5.2 CENTRAL CREEK — 649,90 TL

```
┌──────────────────────────── FACT — BİLDİKLERİMİZ ────────────────────────────┐
│ Urun    : Central Creek (beyaz sarap)                                        │
│ Mense   : Avustralya                                                         │
│ Fiyat   : 649,90 TL — FOTOGRAFTAN OKUNDU                                     │
│ Kanal   : Metro Turkiye (ayni gozlem)                                        │
│ Tarih   : 2026-08-09                                                         │
│ KDV     : KDV DAHIL                                                          │
│ evidence: EV-2026-08-09-502                                                  │
└──────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────── UNKNOWN — BİLMEDİKLERİMİZ ─────────────────────────┐
│ ⛔ HACIM 750 ml OLDUGU DOGRULANMADI  (charter "750 ml civari" diyor)         │
│ ⛔ Uzum / blend                                                              │
│ ⛔ Hasat yili, ABV                                                           │
│ ⛔ Promosyon durumu                                                          │
│ ⛔ Uretici kimligi (T-405 OPEN)                                              │
│ ⚠  AVUSTRALYA %70 TARIFELIDIR — yani bu urun tercihli rejim OLMADAN          │
│    649,90 TL'ye satilabiliyor. Bu, dikkate deger bir sinyaldir.              │
└──────────────────────────────────────────────────────────────────────────────┘
```

## 5.3 Neden ilham verdi

Bu iki etiket, projenin **kurucu hipotezini** doğuran gözlemdir:
*"Türkiye'de ithal şarap 599–650 TL'ye satılabiliyorsa, biz de satabiliriz."*
Ve dikkate değer bir ayrıntı taşır: **ikisi de %70 tarifeli menşeden**
(ABD ve Avustralya) gelmektedir — yani en kötü vergi köşesinde bile bu fiyat
noktası **fiilen mevcuttur.**

## 5.4 Neden doğrudan business-case sayılamaz

| # | Neden |
|---|---|
| **1** | **Promosyon durumu `UNKNOWN`** (`T-504`). Eğer bu bir kampanya fiyatıysa, sürekli bir rekabet noktası değildir ve tüm boşluk okuması kayar. |
| **2** | **Katman yanlış.** Metro bir **cash & carry**'dir; yapısı gereği zincir perakendeden ucuzdur. Bizim hedeflediğimiz raf **`L8_CHAIN_RETAIL`**'dir ve orada **sıfır gözlemimiz** var. |
| **3** | **n = 2.** İki SKU, tek tarih, tek gözlem, **snapshot repoda yok**, mağaza/şehir bilinmiyor. |
| **4** | **Maliyet yapısını bilmiyoruz.** Bu ürünler eski stok olabilir, kur avantajlı dönemde alınmış olabilir, dökme ithal edilip başka yerde şişelenmiş olabilir, ya da zarar/başabaşa satılıyor olabilir. **Bir raf fiyatı bir maliyet kanıtı değildir.** |
| **5** | **599,90 (OBSERVED) ≠ 599 (TARGET).** Bu iki sayı bu projede **hiçbir yerde birleştirilmemiştir**; 0,90 TL yakınlık bir teyit değil, bir **tesadüftür**. |

> **`OPEN QUESTION #001` hâlâ kapanmamıştır** ve `CLAUDE.md` düzeyinde bir
> kuraldır: **kapanmadan `G3` (pazar gate'i) geçilemez.**

---
---

# 6. HEDEF SATIŞ FİYATI

## 6.1 Merdiven ve roller

| Basamak | Rol | Pazar sınıfı | Confidence | Yapısal tavan (P, 5k, BASE) |
|---|---|---|---|---|
| **599** | `FLOOR / DOWNSIDE TEST` | `AGGRESSIVE` | **LOW** | 189,50 TL |
| **699** | `SECONDARY` | `ATTRACTIVE` | MEDIUM | 231,16 TL |
| **799** | **`PRIMARY`** | `ATTRACTIVE` | MEDIUM | **272,83 TL** |
| **899** | `STRETCH` | `PREMIUM_EDGE` | MEDIUM | 314,50 TL |
| **999** | `UPPER SEGMENT TEST` | `TOO_HIGH` *(manda için)* | **LOW** | 356,16 TL |

## 6.2 NEDEN 799? — beş eksende

### (a) Vergi yükü — **799'u seçmenin sebebi DEĞİL**

| Hedef | Toplam vergi | **Payı** |
|---|---|---|
| 599 | 248,03 | **%41,41** |
| 799 | 323,03 | **%40,43** |
| 999 | 398,03 | **%39,84** |

599'dan 999'a **%67 fiyat artışı**, vergi payını yalnızca **1,57 puan** düşürür.
**"Yukarı çıkarsak vergiden kaçarız" argümanı modelde ÇÜRÜTÜLMÜŞTÜR.**
Sebep: ÖTV sabittir (payı düşer) ama gümrük vergisi **oransaldır ve CIF ile
birlikte büyür** — iki etki birbirini neredeyse tam götürür.

### (b) Maktu ÖTV — **asıl mekanizma burada**

ÖTV **71,2692 TL/litre = 53,4519 TL/şişe**'dir ve **fiyattan tamamen
bağımsızdır.** Ucuz şarap ile pahalı şarap **aynı TL ÖTV'yi** öder.

| Hedef | ÖTV / raf fiyatı | ÖTV / yapısal tavan |
|---|---|---|
| 599 | **%8,92** | **%28,21** |
| **799** | **%6,69** | **%19,59** |
| 999 | %5,35 | %15,01 |

> **Maktu ÖTV, ucuz şarap ithalatını orantısız biçimde cezalandırır.**
> Bu, projenin çekirdek hipotezine (fiyat/performans) doğrudan bir tehdittir
> ve merdivende **yukarı doğru** bir baskı yaratır.

### (c) Sabit TL maliyet yığını — **en sert ayrıştırıcı**

5.000 şişelik pilotta hacme bölünen ve **hedeften bağımsız** olan kalemler
(ruhsat sabit maliyeti + ÖTV λ şoku + tek kişilik dağıtım tabanı) tavanı şu
kadar siler:

| Hedef | Yapısal tavan | Yığın sonrası | **Yığının payı** |
|---|---|---|---|
| **599** | 189,50 | **105,12** | **%44,5** |
| 699 | 231,16 | 146,78 | %36,5 |
| **799** | **272,83** | **188,45** | **%30,9** |
| 899 | 314,50 | 230,12 | %26,8 |

> **BULGU: 799, sabit maliyet yığınının payının ilk kez %31'in altına indiği
> basamaktır.** 599'da bu yığın satın alma bütçesinin **neredeyse yarısını**
> siler. Bu, pazar tarafından **tamamen bağımsız**, saf bir maliyet-yapısı
> sonucudur.

### (d) Kanal payı ve azalan getiri

Her +100 TL raf fiyatı = **+41,67 TL** satın alma bütçesi (doğrusal). Ama
**oransal getiri azalır**:

```
599 -> 699 : +%21,99
699 -> 799 : +%18,03
799 -> 899 : +%15,27     <- azalan getiri bolgesi baslar
899 -> 999 : +%13,25
```

**Getiri eğrisi tam 799'da düzleşmeye başlar.**

### (e) Rakip boşluğu

799 TL, merdivenin **whitespace içinde kalan en yoğun** basamağıdır:
±%10 pencerede **31 stokta yerli rakip** (699'un 1,8 katı) ve **stokta ithal
rakip pratikte yok** (1 SKU, o da pencerenin en üst ucunda 875 TL).
Ayrıca projenin kendi `segment` bandının (600–900) **tam ortasıdır** — yani
bant sınırı hatalarına **en az duyarlı** basamaktır.

## 6.3 799'un bilinen zayıflığı — açıkça

> **799 TL, gözlenen iki ithal benchmark'ın (599,90 / 649,90) %23–33
> ÜSTÜNDEDİR.** Bir "fiyat/performans ithal şarap" konumlandırması için bu bir
> **gerilimdir** ve **çözülmemiştir.**
>
> - `T-504` **"normal fiyat"** diye kapanırsa → 599,90 kalıcı bir ithal giriş
>   fiyatıdır, 799 onun %33 üstünde kalır → `PRIMARY` **699'a kaymalıdır.**
> - `T-504` **"promosyonlu"** diye kapanırsa → 599 basamağı `TOO_LOW`'a düşer,
>   799 ve 899 **göreli olarak güçlenir.**
> - `C-561` "bantta ürün var ama dönmüyor" yönünde çözülürse → ithal şarabın
>   fiilen döndüğü tek bölge 875 TL üstüdür → **899 lehine kayar.**

## 6.4 Sınıflandırma

```yaml
PRIMARY_TARGET_SHELF_PRICE: 799
status:   CURRENT DESIGN TARGET
degil:    "kesin satis fiyati" / "beklenen sonuc" / "pazar fiyati"
rol:      RFQ pazarlik capasi + model tasarim noktasi
katman:   L8 (tuketici rafi) — HANGI L8 ALT KATMANI oldugu UNKNOWN (T-859)
kdv:      DAHIL
confidence:
  goreli_siralama:  MEDIUM   # hangi basamak digerinden daha dayanikli
  mutlak_capalama:  LOW      # 799 TL Turkiye rafinda dogru fiyat midir
```

> ### ⚠ VE BİR ÇAPALAMA UYARISI — KAYDA GEÇİYOR
> `799 PRIMARY` seçimi, `sweet-spot-analizi.md`'nin **önerisiyle birebir
> aynıdır.** Bu bir **bağımsız doğrulama değildir** — büyük olasılıkla aynı
> belgenin okunmuş olmasıdır. **Modelin önerdiği bir sayının yatırımcı kararı
> olarak geri dönmesi, o sayıyı doğrulamaz.**

---
---

# 7. HEDEF SATIŞ NOKTALARI

## 7.1 CHAIN RETAIL (Metro · Migros · Macrocenter · CarrefourSA)

| Boyut | Durum |
|---|---|
| **Avantaj** | Tek anlaşmayla yüzlerce noktaya erişim · ölçek · marka görünürlüğü · tahsilat riski düşük |
| **Dezavantaj** | Listeleme bedeli · geri akan bedeller · uzun vade · **merkezî alım — girmek zor** · raf yerine yerli üreticilerle rekabet |
| **Marj varsayımı** | `m_retail` **%25** BASE (bant 18/25/35) — **`ASSUMPTION`** |
| **Geri akan bedeller (`d`)** | **%8** BASE (bant 3/8/18) — **`ASSUMPTION`**, kanıtlı çapası **YOK** |
| **Listeleme bedeli (`f`)** | **`UNKNOWN`** — güncel kamu kaynağı yok |
| **Vade** | **60 gün** BASE (bant 45/60/90/**120**) — **`ASSUMPTION`** |
| **Operasyon** | Merkezî depoya sevkiyat; barkod/EDI; kırık ürün bedeli; soğutucu enerji bedeli |
| **Ölçeklenebilirlik** | **En yüksek** |

⚠ **Tek kanıtlı marj çapamız Migros'un %24,31'idir ve o ŞARAP DEĞİL, TÜM
KATEGORİ karmasıdır** (`EV-2026-08-10-612` bağlamı). Alkolün resmî marj
analizinin **kapsamı dışındadır.**

## 7.2 INDEPENDENT / TEKEL BAYİİ

| Boyut | Durum |
|---|---|
| **Nokta sayısı** | **48.956** — `FACT`, T2 |
| **Avantaj** | Girmek kolay · vade kısa (30 gün BASE) · listeleme bedeli yok/az · fiyat esnekliği |
| **Dezavantaj** | **Nokta nokta satış** — dağıtım maliyeti yüksek · tahsilat riski · ölçekleme yavaş |
| **Marj varsayımı** | %18 BASE (bant 12/18/25) — **`ASSUMPTION`** |
| **Vade** | 30 gün BASE (bant 0/30/60/90) |
| **Model tavanı** | 799 TL'de **303,90 TL** — zincirden **%11,4 yüksek** |
| ⚠ **UYARI** | **Bu %11,4'ün TAMAMI bir `UNKNOWN`'dan geliyor:** `d` (geri akan bedeller) tekel için tanımlı değil ve **0 alınmış.** İki kanal arasında ekonomik tercih **modelden okunamaz** (`T-856`). |
| **Ölçeklenebilirlik** | Orta — 48.956 nokta var ama her birine ulaşmak ayrı maliyet |

## 7.3 HORECA

| Boyut | Durum |
|---|---|
| **Nokta sayısı** | **29.218** — `FACT`, T2 |
| **Avantaj** | En yüksek birim fiyat · marka inşası için en iyi ortam · deneme fırsatı |
| **Dezavantaj** | **Çarpan riski yıkıcı** · yavaş devir · tahsilat en zayıf · nokta başına düşük hacim |
| **Marj varsayımı** | **3,0× çarpan** BASE (bant 2,0 / 3,0 / **5,0×**) — **`ASSUMPTION`** |
| **Model tavanı** | 799 TL menü fiyatında: 3,0×'te **87,88 TL**, **5,0×'te 28,03 TL** |
| ⛔ **YAPISAL BULGU** | HoReCa'da 5,0× çarpan altında **yapısal taban 546,77 TL**'dir. Yani **599 TL'lik bir menü fiyatı matematiksel olarak ölüdür** — tedarikçi bedava verse bile model kapanmaz. |
| **Ölçeklenebilirlik** | Düşük — pilot için uygun değil |

## 7.4 Kanal atamaları

```
PRIMARY CHANNEL       : CHAIN RETAIL  (Metro cash&carry dahil)
SECONDARY CHANNEL     : INDEPENDENT / TEKEL BAYII
OPPORTUNISTIC CHANNEL : HORECA  (yalnizca 3,0x veya altinda carpanla)
```

**Gerekçe:** Charter kanal önceliğini bu sırayla tanımlar; model tavanları da
CHAIN ve TEKEL'i birbirine yakın (%11,4 fark, o da bir `UNKNOWN`'dan), HoReCa'yı
ise **açık ara aşağıda** göstermektedir.

> ⚠ **AÇIK KALAN KRİTİK SORU (`N-3b`, `T-966`):** **799 TL hangi rafın
> fiyatıdır?** `L8_CHAIN_RETAIL` mi, `L8_METRO_CASH_CARRY` mi,
> `L8_ONLINE_UZMAN_PERAKENDE` mi, yoksa bir **kanal karması** mı?
> Bu soru kurucuya sorulmuş ve **cevaplanmamıştır.** Kanal seçimi, tavanı
> **%11,4** oynatır.

---
---

# 8. SATIŞ HEDEFLERİ

## 8.1 Hacim merdiveni

| Senaryo | Şişe/yıl | Şişe/ay | Şişe/hafta | Sevkiyat/yıl (öneri) | Taşıma modu (öneri) |
|---|---|---|---|---|---|
| **PILOT** | 5.000 | 417 | 96 | 1 | 20DV paletli (yarı dolu) veya LCL |
| **VALIDATION** | 10.000 | 833 | 192 | 1 | 20DV paletsiz |
| **COMMERCIAL** | 25.000 | 2.083 | 481 | 2 | 2 × 20DV paletsiz |
| **GROWTH** | 50.000 | 4.167 | 962 | 3 | 20DV + 40HC karışık |
| **SCALE** | 100.000 | 8.333 | 1.923 | 5 | 40HC paletsiz |

## 8.2 Store velocity senaryoları

> # ⚠ BU BÖLÜMÜN TAMAMI `ASSUMPTION`'DIR
> **Türkiye'de şarap için tek bir store velocity, rotasyon, devir veya satış
> verisi YOKTUR.** Aşağıdaki 5/10/20/40 şişe/ay/nokta değerleri **bir ölçüm
> değil, bir duyarlılık grididir.** Hiçbiri bir tahmin veya beklenti değildir.

**Kaç aktif satış noktası gerekir?**

| Hacim (şişe/yıl) | @ **5** şişe/ay | @ **10** şişe/ay | @ **20** şişe/ay | @ **40** şişe/ay |
|---|---|---|---|---|
| **5.000** | 83 nokta | 42 nokta | **21 nokta** | 10 nokta |
| **10.000** | 167 | 83 | **42** | 21 |
| **25.000** | 417 | 208 | **104** | 52 |
| **50.000** | 833 | 417 | **208** | 104 |
| **100.000** | 1.667 | 833 | **417** | 208 |

## 8.3 Bu tablonun yönetim okuması

1. **Pilot (5.000 şişe) küçüktür ve bu iyi bir şeydir.** 20 şişe/ay/nokta
   varsayımıyla **21 aktif nokta** yeter. Bu, tek bir zincirin birkaç mağazası
   veya birkaç düzine tekel bayii demektir — **ulaşılabilir bir sayı.**
2. **25.000'de iş değişir.** 104 aktif nokta gerekir; bu artık gerçek bir
   **dağıtım organizasyonu** demektir. Model, tek kişilik bir dağıtım ekibinin
   bile 5.000 şişede satın alma tavanının **%23,6'sını** sildiğini gösteriyor
   (−64,34 TL/şişe).
3. **100.000'de 417 aktif nokta gerekir.** Bu, ulusal dağıtım demektir ve
   **bu raporun kanıt tabanı bu ölçeği desteklemez.**

> ### KRİTİK BOŞLUK
> Yukarıdaki tablonun tek gerçek girdisi (nokta başına aylık satış) **hiçbir
> kanıta dayanmıyor.** Bu, projenin talep tarafındaki **sıfır veri** durumunun
> doğrudan sonucudur. **RFQ bu boşluğu KAPATMAZ** — bunu kapatacak olan, bir
> perakendeciyle yapılacak ön görüşmedir (§23).

---
---

# 9. RAF CİROSU

## 9.1 Tüketici raf cirosu (L8) — **BU BİZİM CİROMUZ DEĞİLDİR**

> # ⛔ EN SIK YAPILAN HATA
> Aşağıdaki tablo, **tüketicinin kasada ödediği toplam paradır.** İçinde
> **%20 KDV**, **perakendecinin marjı** ve **perakendeciye geri akan bedeller**
> vardır. **Bunların hiçbiri bize gelmez.**

| Hacim (şişe/yıl) | @ 699 TL | @ **799 TL** | @ 899 TL |
|---|---|---|---|
| **5.000** | 3.495.000 TL | **3.995.000 TL** | 4.495.000 TL |
| **10.000** | 6.990.000 | **7.990.000** | 8.990.000 |
| **25.000** | 17.475.000 | **19.975.000** | 22.475.000 |
| **50.000** | 34.950.000 | **39.950.000** | 44.950.000 |
| **100.000** | 69.900.000 | **79.900.000** | 89.900.000 |

## 9.2 Üç katmanın yan yana gösterimi — 799 TL

| Hacim | **L8** tüketici raf cirosu | **L7** perakendecinin alış değeri | **L6** ithalatçı satış cirosu |
|---|---|---|---|
| **5.000** | 3.995.000 TL | 2.496.875 TL | **2.713.995 TL** |
| **10.000** | 7.990.000 | 4.993.750 | **5.427.989** |
| **25.000** | 19.975.000 | 12.484.375 | **13.569.973** |
| **50.000** | 39.950.000 | 24.968.750 | **27.139.946** |
| **100.000** | 79.900.000 | 49.937.500 | **54.279.891** |

**Diğer fiyat noktalarında ithalatçı satış cirosu (L6):**

| Hacim | @ 699 TL | @ 899 TL |
|---|---|---|
| 5.000 | 2.374.321 TL | 3.053.668 TL |
| 25.000 | 11.871.603 | 15.268.342 |
| 100.000 | 47.486.413 | 61.073.370 |

## 9.3 Bu tablonun nasıl kurulduğu (denetlenebilirlik)

```
L8 (KDV dahil)  = 799,0000
R1  / 1,20      = 665,8333   (KDV cikarildi)
R2  x (1-0,25)  = 499,3750   = L7_effective   [m_retail %25 BASE — ASSUMPTION]
R4  / (1-0,08)  = 542,7989   = L6 fatura fiyati [d %8 BASE — ASSUMPTION, f=0 UNKNOWN]
```

Kaynak: `80-model/outputs/reverse-price-model.md` §3.1 — birebir aynı sayılar.

> ### ⚠ ÜÇ UYARI
> 1. **`m_retail` ve `d`'nin ikisi de `ASSUMPTION`'dır.** Kanıtlı tek çapa
>    Migros'un tüm-kategori %24,31'idir ve **şarap değildir.**
> 2. **`f` (listeleme bedeli) `UNKNOWN`'dır ve tabloda `0` alınmıştır.**
>    Gerçekte pozitiftir → **L6 rakamları yukarı sapkındır.**
> 3. **L6 ciro, kâr değildir.** Bu rakamdan malın maliyeti, tüm vergiler,
>    lojistik, bandrol, ruhsat, depo ve dağıtım **henüz düşülmemiştir.**

---
---

# 10. ALIŞ HEDEFİ — `MAX CIF`

## 10.1 Ana rakamlar

**Referans nokta: 799 TL raf · CHAIN RETAIL · BASE senaryo · 5.000 şişe ·
ithalatçı katkı payı 0 · λ = 1**

```
╔═══════════════════════════════════════════════════════════════════╗
║  GRUP P  — tercihli (%50), mense belgesi OK                       ║
║           ES · PT · IT · FR · CL                                   ║
║                                                                    ║
║           MAX CIF  =  272,83 TRY / sise                            ║
║                    =  363,77 TRY / litre                           ║
║                                                                    ║
║  GRUP N  — tercihsiz (%70) VEYA belge alinamadi                   ║
║           AU · MD · US · ZA · AR  +  her DOC_FAIL                  ║
║                                                                    ║
║           MAX CIF  =  240,73 TRY / sise                            ║
║                    =  320,98 TRY / litre                           ║
║                                                                    ║
║  FARK    =  32,10 TRY / sise   =  TAM %11,765                      ║
╚═══════════════════════════════════════════════════════════════════╝
```

## 10.2 ⛔ BUNLAR NEDİR, NE DEĞİLDİR

> ### BUNLAR **`STRUCTURAL CEILING`**'DİR.
>
> **Anlamı:** *"799 TL raf fiyatı ve varsayılan kanal koşulları altında, CIF
> maliyeti bu sayıyı aşarsa model MATEMATİKSEL OLARAK KAPANMAZ."*
>
> ### BUNLAR **SUPPLIER TARGET DEĞİLDİR.**
>
> | Neden | Açıklama |
> |---|---|
> | **1. İçinde KÂR YOKTUR** | İthalatçı katkı payı **0** alınmıştır. Bu tavandan alırsak kârımız **tam olarak sıfırdır.** |
> | **2. 26 maliyet kalemi `0` alınmıştır** | Antrepo bekleme, kırılma/fire, bandrolleme operasyonu, listeleme bedeli, distribütör marjı, USD/EUR cinsli varış masrafları… **hepsi pozitiftir ve hiçbiri düşülmemiştir.** Gerçek tavan **bundan DÜŞÜKTÜR.** |
> | **3. λ = 1 çapası** | ÖTV'nin 2026-07-03 değeri kullanılmıştır. ÖTV Ocak/Temmuz'da **kendiliğinden artar** ve λ ≥ 1'dir → gerçek tavan **daha düşüktür.** |
> | **4. Kanal parametreleri `ASSUMPTION`'dır** | `m_retail` %35 (kanıtlı bant üst ucu) çıkarsa tavan **272,83 → ~176 TL**'ye iner (**−%35**). |
> | **5. Hedef raf katmanı ölçülmemiştir** | `L8_CHAIN_RETAIL`'de **sıfır gözlem** vardır. Tavanın dayandığı raf **hiç görülmemiştir.** |
>
> ### ⛔ BU SAYILAR TEDARİKÇİYE **SÖYLENMEZ.**
> Bir tavanı karşı tarafa söylemek, o tavanı **fiyat hâline getirir.**

## 10.3 Diğer basamaklar — tam tablo (CHAIN · BASE · 5.000 şişe)

| Hedef raf | **Grup P** (TRY/şişe) | **Grup N** (TRY/şişe) |
|---|---|---|
| 599 | 189,50 | 167,20 |
| 699 | 231,16 | 203,97 |
| **799** | **272,83** | **240,73** |
| 899 | 314,50 | 277,50 |
| 999 | 356,16 | 314,26 |

## 10.4 Pazarlık köşeleri — X ve Y

| Köşe | Tanım | MAX CIF (TRY/şişe) |
|---|---|---|
| **X — kötümser** | `HIGH` senaryo (m=%35, d=%18, lojistik HIGH) + **DOC_FAIL** + 5.000 şişe | **200,98** |
| **Y — iyimser** | `BASE` senaryo + **DOC_OK** + 25.000 şişe | **290,51** |

**Okuma kuralı:**
```
CIF <= X          -> guclu aday
X <  CIF <= Y     -> inceleme gerekir
CIF >  Y          -> mevcut modelde ZOR
```

> **X tüm ülkelerde aynıdır (200,98)** çünkü kötümser köşede tercihli menşeler de
> %70'e düşer. **Menşe farkı yalnızca Y köşesinde görünür.**

## 10.5 Yapısal taban — modelin ölüm noktası

`MAX_CIF = 0` olan raf fiyatı (5.000 şişe):

| Kanal | LOW | BASE | HIGH |
|---|---|---|---|
| CHAIN RETAIL | 129,86 | **144,21** | 168,24 |
| INDEPENDENT / TEKEL | 121,01 | 131,90 | 145,81 |
| **HoReCa (5,0× çarpan)** | 212,97 | 324,46 | **546,77** |

> **Bu fiyatların altında tedarikçi malı BEDAVA verse bile model kapanmaz.**
> Sebebi maktu ÖTV'dir — 53,45 TL/şişe fiyattan bağımsız olarak durur.
> 799 TL, zincir kanalda bu tabanın **5,54 katıdır**; 599 TL yalnızca
> **4,15 katı.** Bu, 799'un neden daha dayanıklı olduğunun en yalın ifadesidir.

---
---

# 11. FX SONRASI ALIŞ TAVANI

## 11.1 Kur — gözlenen, tahmin edilmemiş

```yaml
kaynak:      TCMB Gunluk Doviz Kurlari, Bulten No 2026/147
tarih:       2026-08-10
kur_tipi:    doviz_satis   # ithalatci dovizi SATIN ALAN taraftir
EUR/TRY:     55,1414
USD/TRY:     47,7118
status:      OBSERVED_FX / NOT_FORECAST
evidence_id: EV-2026-08-10-865, EV-2026-08-10-866
ttl:         7d   ->  2026-08-17'de BAYATLAR
```

> ⚠ **Bu bir kur tahmini DEĞİLDİR.** Bugünkü gözlemdir. Modelin hedef
> tarihlerinin **üçü de 2027'dedir** — yani bugünün kuruyla 2027 tavanını
> karşılaştırmak **yapısal olarak sorunludur** ve FX eksenleri bunu **çözmez,
> yalnızca gösterir** (`T-965`).

## 11.2 MAX CIF — döviz karşılıkları

**799 TL · CHAIN · BASE · 5.000 şişe · TCMB 2026-08-10 kuruyla:**

| Grup | MAX CIF TRY | **MAX CIF EUR** | **MAX CIF USD** |
|---|---|---|---|
| **P** (tercihli, belge OK) | 272,83 | **4,95** | **5,72** |
| **N** (tercihsiz / belge yok) | 240,73 | **4,37** | **5,05** |

**Pazarlık köşeleri:**

| Köşe | TRY | EUR | USD |
|---|---|---|---|
| **X** (kötümser, 5.000) | 200,98 | **3,64** | **4,21** |
| **Y** (iyimser, 25.000, Grup P) | 290,51 | **5,27** | **6,09** |

## 11.3 TUR 3.25 sonucu — **MAX FOB ≤ 5,2685 EUR / ≤ 6,0889 USD** ne demek?

```
MAX_CIF_TRY  (Y kosesi, Grup P, 799, CHAIN, 25.000)  =  290,5134 TRY/sise
kur (EUR/TRY, doviz satis, 2026-08-10)               =   55,1414
                                                        ─────────────
MAX_CIF_EUR                                          =    5,2685 EUR/sise

CIF = FOB + navlun + sigorta        ve    navlun >= 0,  sigorta >= 0
  =>  MAX_FOB  <=  5,2685 EUR/sise
  =>  MAX_EXW  <=  MAX_FOB          (EXW->FOB koprusu de >= 0)
```

> ## ⛔ BU SAYI **BİR ÜST SINIRIN ÜST SINIRIDIR — ÜÇ KAT**
>
> | Kat | Neden |
> |---|---|
> | **1** | `MAX_CIF`'in kendisi zaten bir üst sınırdır (λ=1 + 26 kalem `BLOCKED_INPUT`) |
> | **2** | FOB→CIF köprüsü **`0` alınmıştır.** Gerçekte navlun + sigorta pozitiftir. Yalnız okyanus navlunu bile İspanya'da **0,27–0,30 USD/şişe**, Şili'de **0,43–0,45**, Avustralya'da **0,53–1,13**'tür. |
> | **3** | `Y` köşesi **iyimser senaryodur** (BASE + belge OK + 25.000 şişe). Pilot hacminde (5.000) tavan **272,83 TRY = 4,95 EUR**'dur, 290,51 değil. |
>
> ### YANİ: 5,2685 EUR bir **NOKTA DEĞER DEĞİLDİR.**
> "Tedarikçi 5,20 EUR isterse alırız" cümlesi **kurulamaz.** Doğru cümle şudur:
> ***"Tedarikçi 5,27 EUR'nun ÜSTÜNDE bir FOB verirse, en iyimser senaryomuzda
> bile model kapanmaz — yani KESİN olarak reddedilir. Altında verirse HİÇBİR
> ŞEY SÖYLENEMEZ."***

## 11.4 Modelin bildiği tek yönlü gerçek

`gerçek_CIF ≥ teklif × kur` olduğundan (köprüler ≥ 0):

| Gözlem | Sonuç |
|---|---|
| `teklif × kur > Y` | **`ABOVE_CEILING`** — sağlam bir ret gerekçesi |
| `teklif × kur ≤ Y` | **`INCOMPLETE`** — hiçbir şey söylenemez |

> **Bugünkü pratik sonucu:** FOB→CIF köprüsü (`T-866`) kapanmadan koşulan bir
> RFQ turunda **makul fiyatlı her teklif `INCOMPLETE` döner.** Bu, RFQ'yu
> anlamsız yapmaz — çünkü RFQ'nun asıl çıktısı fiyat **değil**, fiyat + MOQ +
> ödeme şartı + lead time + menşe belgesi taahhüdü + palet konfigürasyonudur.
> Ama **köprü ticket'ları RFQ ile PARALEL kapatılmalıdır.**

## 11.5 ⛔ BU RAKAM TEDARİKÇİYE SÖYLENMEZ

```
GONDERILMEZ : "Butcemiz sise basina 5,27 EUR"
GONDERILMEZ : "Mense belgesi bize %12 kazandiriyor"
GONDERILMEZ : herhangi bir TL tavan, herhangi bir hedef raf fiyati

GONDERILIR  : "5.000 / 10.000 / 25.000 / 50.000 sise ve FULL 20FT icin
               EXW <tesis> ve FOB <liman> fiyatinizi AYRI AYRI verir misiniz?"
```

**Gerekçe:** `T-890`'da kayda geçmiştir — RFQ şablonunun eski sürümü menşe
belgesinin azami fiyatı ~%12 değiştirdiğini **üreticiye açıkça yazıyordu.**
Bu bilgi, tedarikçiye **bizim yerimize pazarlık yapma imkânı verir.**

---
---

# 12. HEDEF ALIŞ FİYATI NE OLMALI?

## 12.1 Dört kavram — karıştırılmaz

| Kavram | Tanım | Bugünkü durum |
|---|---|---|
| **`STRUCTURAL MAXIMUM`** | Modelin kapanmadığı üst sınır | ✅ **HESAPLANDI** — 272,83 (P) / 240,73 (N) TRY/şişe |
| **`TARGET BUY`** | Almayı hedeflediğimiz fiyat | ⛔ **ÜRETİLEMEZ** |
| **`ACCEPTABLE BUY`** | Kabul edilebilir üst nokta | ⛔ **ÜRETİLEMEZ** |
| **`WALK-AWAY`** | Masadan kalkma noktası | ⛔ **ÜRETİLEMEZ** |

## 12.2 Neden üçü de üretilemez

> **Çünkü yatırımcı bir marj eşiği belirtmemiştir.**
>
> `00-charter/karar-esikleri.md`'deki altı finansal eşiğin **altısı da `TBD`**'dir:
> `target_gross_margin_pct` · `minimum_contribution_try_per_bottle` ·
> `maximum_total_capital_try` · `maximum_acceptable_pilot_loss_try` ·
> `target_inventory_days` · `target_payback_months`.
>
> Bu üç fiyatı **keyfî yüzdelerle üretmek**, `finans-fizibilite`'nin kendi
> ifadesiyle *"modelin en sinsi uydurma noktası"* olurdu. Ajan üretmedi ve
> **neden üretmediğini yazdı.** Başkan bu disiplini **birebir korur.**
> (`T-851`, **CRITICAL, OPEN** · `OQ-901`)

## 12.3 Üç satın alma politikası seçeneği

> # ⚠ AŞAĞIDAKİ ÜÇ SEÇENEK `ILLUSTRATIVE`'DİR
> Bunlar **hesaplanmış eşikler değil, YATIRIMCININ SEÇMESİ GEREKEN
> POLİTİKALARDIR.** Yüzdeler bir modelden türetilmemiştir; **üç farklı risk
> iştahının somut görünümüdür.** Yatırımcı bir yüzde seçtiği anda o yüzde
> `INVESTOR_DECISION` olur ve `ILLUSTRATIVE` etiketi düşer.

### A) `CONSERVATIVE BUYING POLICY`

```yaml
politika:  "Yapisal tavanin %50'sinin ALTINDA al"
etiket:    ILLUSTRATIVE
799/P:     <= ~136 TRY/sise   (~2,47 EUR  /  ~2,86 USD)
799/N:     <= ~120 TRY/sise   (~2,18 EUR  /  ~2,52 USD)
```
**Mantık:** Tavanın yarısı, `0` alınan 26 maliyet kalemine + ÖTV artışına +
kanal marjının kötü ucuna + kur şokuna **aynı anda** yer bırakır.
**Bedeli:** Bu fiyata satacak tedarikçi bulmak zor olabilir. Gözlenen İspanya
CIF birim değeri **2,71 USD/litre = 2,03 USD/750 ml**'dir — yani bu politika
**gözlenen ortalamanın hemen üstündedir** ve teorik olarak ulaşılabilir
görünür, ama gözlenen değer bir **ülke ortalamasıdır**, bir teklif değildir.

### B) `BASE BUYING POLICY`

```yaml
politika:  "Yapisal tavanin %60-65'inin ALTINDA al"
etiket:    ILLUSTRATIVE
799/P:     <= ~164-177 TRY/sise   (~2,97-3,21 EUR  /  ~3,43-3,71 USD)
799/N:     <= ~144-156 TRY/sise   (~2,62-2,83 EUR  /  ~3,03-3,28 USD)
```
**Mantık:** Tavanın **%35–40'ı** ithalatçı katkısı + bilinmeyen maliyetler için
ayrılır. Model, tek kişilik bir dağıtım ekibinin bile tavanın **%23,6'sını**
sildiğini gösteriyor; ÖTV λ şoku **%7,3** daha siliyor. İkisi birlikte **%31**
ediyor — bu politika onun biraz üstünde tampon bırakır.

### C) `AGGRESSIVE BUYING POLICY`

```yaml
politika:  "Yapisal tavanin %75-80'ine kadar cikabil"
etiket:    ILLUSTRATIVE
799/P:     <= ~205-218 TRY/sise   (~3,71-3,96 EUR  /  ~4,29-4,58 USD)
799/N:     <= ~181-193 TRY/sise   (~3,27-3,49 EUR  /  ~3,78-4,04 USD)
```
**Mantık:** Hacim ve pazar girişi öncelikli; ilk yılda kâr hedeflenmiyor.
**Bedeli:** Tavanın **%75'i, X köşesinin (200,98) üstündedir.** Yani bu
politika, **kötümser senaryoda modelin kapanmayacağı bir fiyattan almayı**
kabul eder. Bu bilinçli bir bahistir, bir hesap değildir.

## 12.4 Karşılaştırma

| Politika | Tavanın % kaçı | 799/P TRY | 799/P EUR | Tampon | Risk |
|---|---|---|---|---|---|
| **CONSERVATIVE** | %50 | ~136 | ~2,47 | Çok geniş | Tedarikçi bulunamayabilir |
| **BASE** ✅ | %60–65 | ~164–177 | ~2,97–3,21 | Yeterli | Dengeli |
| **AGGRESSIVE** | %75–80 | ~205–218 | ~3,71–3,96 | Dar | X köşesini aşar |

## 12.5 ÖNERİM

> ## `BASE BUYING POLICY` — tavanın **%60–65**'i
>
> **Üç gerekçe:**
>
> 1. **Modelin kendi ölçtüğü silme oranı bunu gerektiriyor.** Tek kişilik
>    dağıtım (%23,6) + ÖTV λ şoku (%7,3) = **%31** — ve bu **iki kalemdir**,
>    `0` alınan **26 kalemin** yalnızca ikisi. %35–40'lık tampon **cömert
>    değil, asgaridir.**
> 2. **CONSERVATIVE muhtemelen uygulanamaz.** ~2,47 EUR/şişe CIF, gözlenen
>    İspanya CIF birim değerinin (2,03 USD/750 ml ≈ 1,78 EUR) üstünde ama
>    **navlun + sigorta düşüldükten sonraki FOB'u** çok dar bırakır. Bu politika
>    RFQ'dan **sıfır kabul edilebilir teklif** döndürebilir — ki bu bir cevap
>    değil, bir **ölçüm hatasıdır.**
> 3. **AGGRESSIVE, kanıtsız bir iyimserliğin üstüne kurulur.** X köşesini aşmak,
>    "kanal marjı kötü ucunda çıkmaz" bahsi yapmaktır — ve o bandın **tamamı
>    `ASSUMPTION`'dır.**
>
> ⚠ **Ama bu bir öneridir, bir eşik değildir.** Nihai yüzdeyi **yatırımcı**
> seçer. Seçilene kadar `TARGET BUY` / `ACCEPTABLE BUY` / `WALK-AWAY`
> **`INVESTOR_DECISION_REQUIRED` olarak kalır.**

---
---

# 13. NEREDEN ALMALIYIZ?

## 13.1 Ülke ülke değerlendirme

### 🇪🇸 SPAIN — **TIER 1**

| Boyut | Durum |
|---|---|
| **Tarife** | %50 **koşullu** (AB tarım rejimi 1/98 — **Gümrük Birliği DEĞİL**) |
| **Menşe belgesi fırsatı** | EUR.1 veya fatura beyanı; **A.TR GEÇERSİZ**. Hat rutin çalışıyor |
| **Lojistik** | **En iyi rota.** Valencia/Barcelona → İstanbul **4 gün, 0 AKTARMA, direkt**. LCL **0,274–0,297 USD/şişe** — havuzun en ucuzu |
| **Public sourcing sinyali** | L2 CIF **2,71 USD/litre** (1.916.118 lt/2025) — segment içi |
| **Tedarikçi erişimi** | Interbrosa (**MOQ 3.000 — havuzun en düşüğü**), Bodegas San Valero |
| **Private label** | **ÇOK GÜÇLÜ** — ihracatın %57'si dökme → sanayi ölçekli şişeleme altyapısı |
| **Existing brand** | VAR — San Valero (Particular) |
| **Risk** | Interbrosa sitesi 2026-08-10'da **HTTP 503**; firmanın faal olduğu teyit edilmedi (`T-889`). İspanya 2025'te üretimini %7,7 düşürdü, 3 yıl kuraklık |
| **Genel cazibe** | ⭐⭐⭐⭐⭐ **Origin charge'ları bilinen TEK menşe** (349–554 EUR/konteyner). Üç lojistik bacağın üçü de bilinen tek ülke |

### 🇵🇹 PORTUGAL — **TIER 1**

| Boyut | Durum |
|---|---|
| **Tarife** | %50 koşullu (aynı AB rejimi) |
| **Menşe belgesi** | EUR.1 / fatura beyanı |
| **Lojistik** | Lizbon → İstanbul, LCL **0,423–0,445 USD/şişe**, Barcelona aktarmalı. ⚠ Transit "~4 gün" yazıyor ama Barcelona aktarmalı — **iç tutarsız**, confidence LOW |
| **Public sinyali** | L2 CIF **3,20 USD/litre** (324.828 lt/2025) — hat çalışıyor ama küçük |
| **Tedarikçi** | Casa Santos Lima (~50 ülke, üretimin %90'ı ihracat), Vidigal (Porta 6) |
| **Private label** | ORTA — doğrulanan firmalar PL ilan etmiyor |
| **Existing brand** | **EN OLGUN ADAYLAR BURADA** |
| **Risk** | İkisinin de **MOQ'su `UNKNOWN`**; Vidigal için **doğrulanmış iletişim kanalı yok** (`T-888`) |
| **Genel cazibe** | ⭐⭐⭐⭐ Model A'yı test etmenin en iyi yeri |

### 🇮🇹 ITALY — **TIER 2**

| Boyut | Durum |
|---|---|
| **Tarife** | %50 koşullu |
| **Lojistik** | ⛔ **TAMAMEN `UNKNOWN` — LCL de FCL de.** Test edilen limanların **tamamı Tirrenya**; tedarikçi ise **Veneto**'da → Adriyatik/Ro-Ro **hiç test edilmedi** (`T-916`) |
| **Public sinyali** | L2 CIF 3,65 USD/lt · **5.749.972 lt/2025 — Türkiye'nin EN GÜÇLÜ hattı** |
| **Tedarikçi** | Cantina Danese (MOQ 6.000/SKU, gümrük antreposu işletiyor) |
| **Private label** | GÜÇLÜ — Veneto/Puglia PL yoğun |
| **Risk** | ⚠ **Danese Türkiye'de KENDİ MARKASIYLA listeli** (1.419 TL, stokta değil, ithalatçı `Midas`) → **münhasırlık çakışması riski** (`T-565`) |
| **Genel cazibe** | ⭐⭐⭐ En güçlü ticaret hattı, **en zayıf lojistik bilgisi.** Rota bilinmeden fiyat karşılaştırılamaz |

### 🇨🇱 CHILE — **TIER 2**

| Boyut | Durum |
|---|---|
| **Tarife** | %50 koşullu (TR-Şili STA, I s. Liste dipnot 2) |
| **Menşe belgesi** | EUR.1 / fatura beyanı — **çıkış ülkesi YALNIZCA ŞİLİ**, çapraz kümülasyon YOK |
| **Lojistik** | LCL **0,432–0,454 USD/şişe** (Portekiz ile aynı bant!) ama **transit 43 GÜN**, Barcelona aktarmalı |
| ⛔ **ROTA BİR VERGİ KARARIDIR** | En ucuz Şili rotası **Barcelona aktarmalıdır.** Aktarmanın çıkış ülkesi kontrolünü bozup bozmadığı **`UNKNOWN`**. Bozuyorsa **%50 → %70** ve kayıp **−32,10 TL/şişe** — yani **navlundaki tüm avantajdan büyük** (`T-914`) |
| **Public sinyali** | L2 CIF **2,89 USD/lt** (946.350 lt/2025) — segment içi |
| **Tedarikçi** | Corta Hojas — **Sauvignon Blanc + Chardonnay, görev tanımıyla birebir eşleşen tek doğrulanmış CL portföyü.** MOQ `UNKNOWN` |
| **Risk** | 43 gün transit + ekvator geçişi (**yüksek termal risk**) + kırılma oranı `UNKNOWN` |
| **Genel cazibe** | ⭐⭐⭐ Ürün eşleşmesi mükemmel, **rota riski ciddi** |

### 🇫🇷 FRANCE — **TIER 2**

| Boyut | Durum |
|---|---|
| **Tarife** | %50 koşullu |
| **Lojistik** | ⚠ **Marsilya → İstanbul, LCL 0,636–0,675 USD/şişe — ŞİLİ'DEN PAHALI.** Sebep coğrafya değil **routing**: Marsilya çıkışlı LCL **Hamburg/Antwerp'e gidip dönüyor.** Fransa lojistik olarak bir Akdeniz menşei gibi **davranmıyor** |
| ⚠ **Liman uyuşmazlığı** | Tek FR kotasyonu **Marsilya**; iki aday da **Atlantik/Güneybatı**'da (Bordeaux/Gornac, Languedoc/Valros, Saint-Mont). **Marsilya bu iki tedarikçinin çapası DEĞİLDİR** (`T-915`) |
| **Public sinyali** | L2 CIF **6,27 USD/lt — İspanya'nın 2,3 KATI.** Segment üstü |
| **Tedarikçi** | The Wine Factory (MOQ **3.600**, üretim 28–42 gün), Plaimont (Côtes de Gascogne — **havuzun en güçlü ürün eşleşmesi**) |
| **Private label** | GÜÇLÜ ama üst segment ağırlıklı; **Languedoc/Gascogne entry kanadı var** |
| **Risk** | Ülke ortalaması segment dışı; Gascogne'un bu ortalamanın altında olduğu **doğrulanmamıştır** |
| **Genel cazibe** | ⭐⭐⭐ Benchmark stilinin (Colombard-Chardonnay) **yapısal kaynağı** — ama fiyat sinyali karşı yönde |

### 🇲🇩 MOLDOVA — **TIER 2**

| Boyut | Durum |
|---|---|
| **Tarife** | **%70 — tercihsiz.** STA var ama **2204.21'i KAPSAMIYOR** |
| **Menşe belgesi** | Tercihli belge **düzenlenemez** — yapısal, kalıcı **−32,10 TL/şişe** |
| **Lojistik** | ⛔ **HİÇ TEST EDİLMEDİ.** Havuzdaki **tek karayolu erişimli menşe** — deniz kotasyon mantığı uygulanamaz |
| **Public sinyali** | L2 CIF **2,46 USD/lt — TÜM MENŞELERİN EN DÜŞÜĞÜ.** 2.038.906 lt/2025, iki yıl üst üste |
| **Tedarikçi** | Purcari Wineries Group — **Bükreş Borsası'nda halka açık**, denetlenmiş finansallar |
| ⚠ **Karşı sinyal** | Grup kendini *"the most premium wines from Moldova and Romania"* diye konumluyor |
| ⚠ **Fırsat** | Aynı grubun **RO/BG tesisleri AB üyesidir → %50 + EUR.1.** "Aynı ürünü Romanya tesisinden sevk" sorusu **doğrudan 32,10 TL/şişe değerindedir** (`T-891`) |
| **Genel cazibe** | ⭐⭐⭐ En ucuz CIF sinyali + en kısa rota + halka açık şirket; ama %70 tarife ve lojistik `UNKNOWN` |

### 🇿🇦 SOUTH AFRICA — **LOW PRIORITY**

%70 tarife (tercihsiz) · LCL **0,766–0,788 USD/şişe** (havuzun **en pahalısı**) ·
transit **49 gün** · rota **ekvatoru İKİ KEZ geçiyor** (Cape Town→Hamburg→İstanbul)
→ **termal olarak en kötü rotalardan** · Türkiye hattı **fiilen yok** (18.026 lt/2025).
Private label ekosistemi **çok güçlü** ama bu tek başına yetmez.

### 🇦🇺 AUSTRALIA — **LOW PRIORITY**

%70 tarife (STA yok) · LCL 0,529–1,133 USD/şişe · transit **36–56 gün, tropik
Singapur aktarması** → **çok yüksek termal risk** · Türkiye hattı fiilen yok
(44.674 lt/2025). **Tek avantajı:** Harland havuzun **tek şeffaf tedarikçisidir**
(MOQ, ödeme şartı, lead time, fiyat kademesi hepsi yayınlanmış). Ama o fiyatın
**para birimi bile `UNKNOWN`**'dır (`C-461`).

> ⚠ **Ve bir gözlem:** komşu benchmark (**Central Creek, 649,90 TL**) **Avustralya
> menşelidir** — yani %70 tarife altında bu fiyat noktası **fiilen mevcuttur.**
> Bu, Avustralya'yı elemek yerine **anlamayı** gerektirir.

### 🇺🇸 USA / CALIFORNIA — **LOW PRIORITY**

%70 tarife · LCL 0,505–0,574 USD/şişe, transit **20 gün** (Atlanta kara
aktarmalı — kara ayağında sıcaklık kontrolsüz) · L2 CIF **25,19 USD/lt** ama bu
**temsili değildir** (18.298 lt, `C-402`) · 2025'te ABD şarap ihracatı **değer
bazında −%35,9**.

> **Benchmark ürünün menşei burasıdır** — ve bu, projenin en büyük ironisidir:
> ilham veren ürün, **en zor yapısal koşullardaki menşeden** geliyor.

### 🇦🇷 ARGENTINA *(charter kapsamında, istenen 9'un dışında)*

%70 tarife · LCL 0,512–0,535 USD/şişe · transit 25 gün, ekvator geçişi ·
L2 CIF 13,87 USD/lt (temsili değil, 69.612 lt) → **LOW PRIORITY**.

## 13.2 Final sıralama

```
╔════════════════════════════════════════════════════════════════════╗
║  TIER 1  (ilk RFQ dalgasi — kaynak buraya)                         ║
║     1. ISPANYA    — en iyi rota, en dusuk MOQ, PL en guclu         ║
║     2. PORTEKIZ   — Model A'nin en olgun adaylari                  ║
║                                                                     ║
║  TIER 2  (ayni dalgada sorulur, ama bir UNKNOWN kapatilmadan       ║
║           karar verilmez)                                           ║
║     3. ITALYA     — en guclu ticaret hatti / rota UNKNOWN           ║
║     4. SILI       — urun eslesmesi mukemmel / rota vergi riski      ║
║     5. FRANSA     — stilin kaynagi / fiyat sinyali karsi yonde      ║
║     6. MOLDOVA    — en ucuz CIF / %70 tarife + rota UNKNOWN        ║
║                                                                     ║
║  LOW PRIORITY  (ilk turda kaynak ayrilmaz)                         ║
║     7. GUNEY AFRIKA · 8. AVUSTRALYA · 9. ABD/CALIFORNIA · AR       ║
╚════════════════════════════════════════════════════════════════════╝
```

## 13.3 Belirleyici tek gerçek

> **Ters modelde 9 ülke için 9 farklı sayı YOKTUR — 2 farklı sayı vardır.**
> Menşe, satın alma tavanını **yalnızca `(1+g)` böleni üzerinden** etkiler:
> `%50 → A`, `%70 → 0,88235 × A`. ÖTV ve KDV menşeden **bağımsızdır.**
>
> **Ülkeler arası gerçek ayrışma FOB seviyesinde doğar** — ve o bacak **hiçbir
> ülke için elimizde yoktur.** Yani bugünkü ülke sıralaması **modelden
> okunmamıştır**; tarife grubu + gözlenen CIF birim değerleri + rota kalitesi +
> tedarikçi erişilebilirliğinden **elle kurulmuştur.**

---
---

# 14. İLK 5 TEDARİKÇİ

> **Bu bir tedarikçi SEÇİMİ değildir — bir TEMAS SIRASIDIR.**
> Hiçbirinden teklif alınmamıştır (`FIRM_OFFER` sayısı: **0**).
> RFQ paketi hazırdır ve **7 hedef `READY_TO_SEND`**'dir, ancak **hiçbir mesaj
> gönderilmemiştir** (`T-885`, CRITICAL).

## 14.1 — #1 · INTERBROSA FAMILY WINES 🇪🇸

| Alan | Değer |
|---|---|
| **Ülke** | İspanya |
| **İş modeli** | PRIVATE LABEL (Model B) |
| **Neden ilk** | **Havuzun doğrulanmış EN DÜŞÜK MOQ'su: 3.000 şişe.** 5.000 şişelik pilotu mümkün kılan iki üreticiden biri. Üstelik en iyi rota üzerinde (Valencia/Barcelona → İstanbul, **4 gün, 0 aktarma**) ve origin charge'ları bilinen tek menşede |
| **Avantaj** | MOQ ↓ · rota ↑ · tarife %50 · PL ekosistemi çok güçlü · etiket/koli/kapsül **tasarımı** ücretsiz beyanı var |
| **Risk** | ⚠ Kurumsal site **2026-08-10'da iki domainde de HTTP 503**. Firmanın **faal olduğu teyit edilmedi** (`T-889`). MOQ kanıtı 2026-08-09 tarihli ve site o günden beri erişilemiyor |
| **Ne soracağız** | 750 ml kuru beyaz, value kademe — Airén-Chardonnay / Verdejo tarzı |
| **Hangi hacimler** | 3.000 · 5.000 · 10.000 · 25.000 · 50.000 · FULL 20FT |
| ⛔ **BU CEVAP ALINMADAN İLERLEMEYİZ** | **"3.000 şişelik MOQ bugün hâlâ geçerli mi, firma faal mi, ve o adette şişe başı EXW `<tesis>` / FOB `<liman>` fiyatınız nedir?"** — Firma faal değilse tüm pilot hacim mantığımızın **dayandığı tek çapa** düşer |

**Diğer iki kritik soru:** (2) *"Tasarım ücretsizse; klişe, kalıp, kesim bıçağı
ve ilk baskı hazırlığı ayrıca fatura ediliyor mu?"* — "ücretsiz" ≠ "maliyetsiz".
(3) *"Türkçe arka etiketi kendi tesisinizde uygulayabiliyor musunuz?"* — evet ise
Türkiye'deki etiketleme operasyonu (bir `L5` kalemi) **tamamen kalkar.**

## 14.2 — #2 · BODEGAS SAN VALERO (GRUPO BSV) 🇪🇸

| Alan | Değer |
|---|---|
| **Ülke** | İspanya — DOP Cariñena, Aragón |
| **İş modeli** | **İKİSİ BİRDEN** — Model A (Particular vb.) + Model B (private label) |
| **Neden ilk 5'te** | **Havuzdaki TEK doğrulanmış ikili aday.** Tek bir RFQ, iki iş modelinin fiyat farkını **AYNI maliyet tabanı üzerinde** ölçebilir. Charter'ın *"iki model eşit öncelikli"* kuralını **kanıtla** test etmenin en ucuz yolu budur |
| **Avantaj** | Ölçek (2,5 m koli/yıl, 40+ ülke, satışların %70'i ihracat) · İspanya rotası · %50 tarife |
| **Risk** | MOQ **`UNKNOWN`** · private label beyanı **firmanın kendi kanalından değil, 3. taraf sektör yayınından** · doğrudan ihracat e-postası yok, temas **fuar profili** üzerinden |
| **Ne soracağız** | Aynı 750 ml kuru beyaz — **iki modelde de** |
| **Hangi hacimler** | 5.000 · 10.000 · 25.000 · 50.000 · FULL 20FT — **her iki model için ayrı** |
| ⛔ **BU CEVAP ALINMADAN İLERLEMEYİZ** | **"Aynı 750 ml kuru beyaz için (a) kendi markanızla, (b) bizim markamızla şişe başı EXW fiyatınız nedir ve fark yüzde kaçtır?"** — Bu, **Model A ↔ Model B karşılaştırmasını yapabileceğimiz TEK ölçüm noktasıdır.** Bugün iki modelin fiyat farkı hakkında **hiçbir verimiz yok** |

## 14.3 — #3 · CASA SANTOS LIMA 🇵🇹

| Alan | Değer |
|---|---|
| **Ülke** | Portekiz — Alenquer (Lisboa) + 5 bölge |
| **İş modeli** | EXISTING BRAND (Model A) |
| **Neden ilk 5'te** | **Model A'nın en olgun adayı:** ~50 ülke, üretimin ~%90'ı ihracat, kendi markaları mevcut (Quinta da Espiga, Setencostas, Palha-Canas). Model A tarafında **MOQ verimiz sıfır** — bu boşluğu kapatacak en güçlü aday |
| **Avantaj** | Etiket/dosya/sertifika hazır → **hız** · %50 tarife · PT hattı çalışıyor · L2 CIF 3,20 USD/lt |
| **Risk** | MOQ `UNKNOWN` · fiyat `UNKNOWN` · Türkiye'de bölge **kapalı olabilir** · temas yalnızca kurumsal form üzerinden |
| **Ne soracağız** | Value segment beyaz SKU'lar + Türkiye münhasırlığı koşulları |
| **Hangi hacimler** | 5.000 · 10.000 · 25.000 · 50.000 |
| ⛔ **BU CEVAP ALINMADAN İLERLEMEYİZ** | **"Türkiye'de bir ithalatçınız/distribütörünüz var mı ve bölge kapalı mı; bu markalar Türkiye'de daha önce satıldı mı, neden durdu?"** — Bu **Model A'nın VARLIK KOŞULUDUR.** Bölge kapalıysa bu firma ve muhtemelen diğer Model A adayları **listeden düşer** |

## 14.4 — #4 · THE WINE FACTORY (SARL) 🇫🇷

| Alan | Değer |
|---|---|
| **Ülke** | Fransa — Bordeaux (Gornac) **ve** Languedoc (Valros) |
| **İş modeli** | PRIVATE LABEL (Model B) |
| **Neden ilk 5'te** | **MOQ (3.600) ve üretim süresi (28–42 gün) BİRLİKTE bilinen tek tedarikçi.** `peak_cash_requirement`'ın zaman ekseni için gereken iki girdinin ikisi de burada. Ayrıca hedef stilin (Colombard-Chardonnay) **coğrafi ailesinde** |
| **Avantaj** | MOQ pilotla uyumlu · üretim süresi taahhüt edilebilir · %50 tarife · **iki tesis = iki fiyat noktası** |
| **Risk** | ⚠ **Liman uyuşmazlığı** — tek FR kotasyonu Marsilya, tesisler Atlantik/Güneybatı'da (`T-915`) · Fransa L2 CIF **6,27 USD/lt, İspanya'nın 2,3 katı** · **yayınlanmış e-posta YOK** (Google Forms + telefon, `T-886`) |
| **Ne soracağız** | Languedoc (Valros) tesisinden IGP entry beyaz + Colombard-Chardonnay tarzı blend kabiliyeti |
| **Hangi hacimler** | 3.600 · 5.000 · 10.000 · 25.000 |
| ⛔ **BU CEVAP ALINMADAN İLERLEMEYİZ** | **"Languedoc (Valros) tesisinden IGP entry beyaz için EXW/FOB nedir — ve Bordeaux (Gornac) tesisiyle arasındaki fark şişe başına kaç EUR?"** — Tek fiyat gelirse **kullanılamaz.** Bu soru aynı zamanda *"Fransa segment içinde mi dışında mı"* sorusunun **tek doğrudan testidir** |

## 14.5 — #5 · CANTINA DANESE S.R.L. 🇮🇹

| Alan | Değer |
|---|---|
| **Ülke** | İtalya — Roncà (VR), Veneto |
| **İş modeli** | PRIVATE LABEL (Model B) |
| **Neden ilk 5'te** | **Türkiye'nin en güçlü şarap ithalat hattı** (5.749.972 lt/2025) ile **sayı olarak bilinen MOQ** (6.000/SKU) aynı tedarikçide buluşuyor. Ayrıca **gümrük antreposu işlettiğini ve ihracat evrakını hazırladığını** beyan ediyor → dokümantasyon riskini düşürür |
| **Avantaj** | %50 tarife · en güçlü hat · evrak kabiliyeti · Veneto PL yoğun |
| **Risk** | ⚠⚠ **Türkiye'de KENDİ MARKASIYLA listeli** (Danese Primitivo "Black Label", 1.419 TL, stokta değil, ithalatçı iç etiketi `Midas`) → **münhasırlık çakışması** (`T-565`). Ayrıca **İtalya rotası tamamen `UNKNOWN`** (`T-916`) ve MOQ 6.000 pilot bandının üstünde |
| **Ne soracağız** | 750 ml kuru beyaz value referans (Trebbiano / Garganega / Pinot Grigio / Chardonnay) |
| **Hangi hacimler** | 5.000 · 6.000 · 10.000 · 25.000 · FULL 20FT |
| ⛔ **BU CEVAP ALINMADAN İLERLEMEYİZ** | **"Türkiye'de kendi markanızla bir müşteriniz var; bu ilişki canlı mı, münhasırlık içeriyor mu, ve bizim private label işimiz bu ilişkiyle çakışır mı?"** — Cevap "çakışır" ise bu firma **düşer.** Ayrıca aynı üreticinin şişesi Türkiye rafında 1.419 TL'yken bizim hedefimiz 799 TL — bu **bizim aleyhimize bir referans fiyat** yaratabilir |

## 14.6 SECOND WAVE (diğer 5)

| # | Firma | Ülke | Model | Neden ikinci dalga |
|---|---|---|---|---|
| 6 | **Vidigal Wines (Porta 6)** | 🇵🇹 | A | Profil uygun (entry/orta segment, distribütör arıyor) ama **doğrulanmış hiçbir iletişim kanalı yok** (`T-888`); beyaz portföyü `UNKNOWN` |
| 7 | **Corta Hojas** | 🇨🇱 | B | **Ürün eşleşmesi mükemmel** (SB + Chardonnay) ama **MOQ, fiyat, Incoterm, lead time — dördü de yayınlanmamış**; ayrıca rota vergi riski (`T-914`) çözülmeden fiyat karşılaştırılamaz |
| 8 | **Plaimont (Colombelle)** | 🇫🇷 | A | **Havuzun en güçlü ürün eşleşmesi** (Côtes de Gascogne Colombard-Chardonnay) ama yayınlanmış e-posta yok (`T-887`) ve FR fiyat sinyali karşı yönde |
| 9 | **Purcari Wineries Group** | 🇲🇩 | A | En ucuz CIF sinyali + halka açık şirket, ama **%70 tarife**, "premium" konumlandırma ve **lojistik hiç test edilmemiş**. ⚠ **RO/BG tesisi sorusu bunu ilk dalgaya taşıyabilir** |
| 10 | **Harland Wine Company** | 🇦🇺 | B | Havuzun **en şeffaf** tedarikçisi ama **%70 tarife + 36–56 gün tropik aktarmalı transit + para birimi `UNKNOWN`** |

## 14.7 Gönderim öncesi zorunlu kontroller

| # | Kontrol | Durum |
|---|---|---|
| 1 | RFQ şablonu **price-volume grid**'e çevrilmeli (tek hacim değil) | ⛔ `T-961` OPEN |
| 2 | `<PILOT VOLUME>` doldurulmalı | ⛔ **HÂLÂ BOŞ** |
| 3 | Gönderen kimlik alanları (`<COMPANY>` `<NAME>` `<EMAIL>` `<DEADLINE>`) | ⛔ **BOŞ** (`T-892`) |
| 4 | Hacim kademelerinin **BAZI** (yıllık mı sipariş başına mı) netleşmeli | ⛔ `T-961` — **tek cümlelik kurucu doğrulaması yeterli** |
| 5 | Cevapsızlık/eleme kuralı kararı | ⛔ `T-884` OPEN — `P-6.7` gereği **ilk gönderimden ÖNCE** |
| 6 | Her hedef için `RECIPIENT` + `SUBJECT` + `PREVIEW` kurucu onayı | ⛔ `P-6.3` — **zorunlu** |
| 7 | **Tüm hedeflere AYNI metin** gitmeli | kural — metin değişirse teklifler karşılaştırılamaz |

---
---

# 15. NAVLUN

## 15.1 LCL — gerçek, tarihli kotasyonlar

`Flexport Rate Explorer (T4) · erişim 2026-08-10 · **geçerlilik 2026-08-16** ·
5 CBM / 750 kg bazlı · yalnızca base ocean freight (port-to-port)`

| Menşe | Çıkış limanı | **USD/şişe** | Transit | Aktarma | Termal risk |
|---|---|---|---|---|---|
| 🇪🇸 **İspanya** | Valencia / Barcelona | **0,274 – 0,297** | **4 gün** | **0 (direkt)** | **DÜŞÜK** |
| 🇪🇸 İspanya (2. teklif) | Barcelona | 0,360 – 0,383 | 4 gün | 0 | düşük |
| 🇵🇹 **Portekiz** | Lizbon | **0,423 – 0,445** | ~4 gün ⚠ | 1 (Barcelona) | düşük–orta |
| 🇨🇱 **Şili** | San Antonio | **0,432 – 0,454** | **43 gün** | 1 (Barcelona) | **yüksek** |
| 🇺🇸 California | Los Angeles | 0,505 – 0,527 | 20 gün | 2 (kara+deniz) | orta–yüksek |
| 🇦🇷 Arjantin | Buenos Aires | 0,512 – 0,535 | 25 gün | 1 (Hamburg) | yüksek |
| 🇦🇺 **Avustralya** | Melbourne | **0,529 – 0,551** | **36–56 gün** | 1 (**Singapur, tropik**) | **çok yüksek** |
| 🇺🇸 California | Oakland | 0,552 – 0,574 | 20 gün | 2 | orta–yüksek |
| 🇫🇷 **Fransa** | Marsilya | **0,636 – 0,675** | 12–15 gün | 1 (**Hamburg/Antwerp**) | orta |
| 🇿🇦 **G. Afrika** | Cape Town | **0,766 – 0,788** | **49 gün** | 1 (ekvator **2 kez**) | **çok yüksek** |
| 🇮🇹 **İtalya** | — | ⛔ **UNKNOWN** | UNKNOWN | UNKNOWN | UNKNOWN |
| 🇲🇩 **Moldova** | — | ⛔ **UNKNOWN** (karayolu) | UNKNOWN | — | düşük *(kısa)* |

## 15.2 İki karşı-sezgisel bulgu

> **1. Şili, Portekiz ile AYNI navlun bandındadır** (0,43–0,45 USD/şişe).
> "Uzak menşe = pahalı navlun" sezgisi bu rotada **yanlıştır.** Fark navlunda
> değil **transitte**: 43 gün vs ~4 gün.
>
> **2. Fransa (Marsilya), Şili'den PAHALIDIR.** Sebebi coğrafya değil
> **routing**: Marsilya çıkışlı LCL yükü Hamburg/Antwerp'e gidip oradan
> Türkiye'ye dönüyor. Bir Akdeniz limanı olması **hiçbir işe yaramıyor.**

## 15.3 Navlun maliyetin küçük parçasıdır

> **En önemli tek lojistik bulgusu:** İspanya çıkış **local charge'ları
> (349–554 EUR/konteyner)** tek başına, aynı lane'in **base okyanus navlununu
> (~300–700 USD)** aşabilmektedir.
>
> Yani *"navlun pazarlığı"* **yanlış yerde yapılan bir pazarlıktır.**
> **Kalem kompozisyonu, navlunun kendisinden daha belirleyicidir.**

## 15.4 Hacme göre beklenen taşıma modu

| Hacim (şişe/yıl) | Sevkiyat/yıl | Sevkiyat başı | **Beklenen mod** | Gerekçe |
|---|---|---|---|---|
| **5.000** | 1 | 5.000 | **LCL** veya **20DV paletli (yarı dolu)** | LCL/FCL kırılma noktası **~5.900 şişe** — pilot tam üstünde. Fiyat farkı **gürültü seviyesinde** |
| **10.000** | 1 | 10.000 | **20DV paletsiz** | Kırılmanın belirgin üstünde; kapasite bağlamaya başlıyor |
| **25.000** | 2 | 12.500 | **2 × 20DV paletsiz** | Her sevkiyat kapasiteye yakın |
| **50.000** | 3 | ~16.700 | **20DV + 40HC karışık** veya 4 × 20DV | Ara bölge; sabit kalemler 40HC lehine |

**Konteyner kapasiteleri (`ESTIMATE`):**
```
20DV paletli    :  6.480 – 7.200 sise
20DV paletsiz   : 11.800 – 13.700 sise
40HC paletsiz   : 19.100 – 21.500 sise
```
⚠ Paletli/paletsiz farkı **~2 kattır** ve gerçek adet **tedarikçinin koli/palet
konfigürasyonuna** bağlıdır → RFQ'da açıkça sorulur (`T-962`, `T-869`).

## 15.5 ⛔ FCL KOTASYONU HÂLÂ `UNKNOWN`

> ### TEST EDİLEN 14 TÜRKİYE VARIŞLI LANE'İN **HİÇBİRİNDE** KAMUYA AÇIK FCL
> ### KOTASYONU YOKTUR.
>
> Elimizdeki tek FCL bandı (İspanya → Türkiye 20DV: **300 – 1.200 USD**) bir
> `ESTIMATE`'tir, confidence **LOW**'dur ve **çözülmemiş bir çelişkiye
> dayanır** (`C-311`, CRITICAL):
>
> | Kaynak | Değer | Sorun |
> |---|---|---|
> | Marketplace "from" fiyatları | 295 – 650 USD | tarih **yok**, konteyner boyu belirtilmemiş, local charge'lar hariç |
> | Blog / rehber bantları | 1.200 – 2.500 EUR | **T5**, 2025 tarihli, yakıt surprimi hariç |
>
> **4–5 kat fark. Taraf seçilmedi, ortalama alınmadı, alınamaz.**
> `T-304` **CRITICAL ve OPEN**'dır. 3 forwarder'lık RFQ paketi **hazırdır ve
> gönderilmemiştir** (`T-821`).

## 15.6 ⏰ TAZELİK UYARISI

```
10 LCL kotasyon karti  :  ttl 6d  ->  2026-08-17'de STALE
Turev kartlar          :  kaynak STALE olunca fiilen ayni tarih
BUGUN                  :  2026-08-10   ->   KALAN: 6 GUN
```

> **Bu, projedeki en kısa ömürlü kanıt setidir.** 2026-08-17'den sonra
> lojistik bacağı ya yeniden doğrulanır (`T-913`) ya da **açıkça
> `ESTIMATE/LOW`'a düşürülür.** **Sessizce bayat veriyle koşmak yasaktır.**

---
---

# 16. GÜMRÜK VE VERGİ

## 16.1 Vergi tablosu — sade

| # | Kalem | Matrah | Oran / Tutar | Tip | Statü |
|---|---|---|---|---|---|
| **1** | **Gümrük Vergisi** | CIF gümrük kıymeti | **%50** (AB · BK · Şili — **koşullu**) / **%70** (Yeni Dünya) | oransal | `FACT` **T1** |
| 2 | İlave Gümrük Vergisi | — | **YOK** (2204 listede değil) | — | `FACT` T1 |
| 3 | KKDF | Vadeli ödenen ithalat bedeli | **%6** — yalnız kabul kredili / vadeli akreditif / mal mukabili. **Peşinde DOĞMAZ** | oransal koşullu | `FACT` (oran) / `UNKNOWN` (matrah) |
| **4** | **ÖTV** | CIF + GV + KKDF + diğer *(ÖTV ve KDV hariç)* | Nispi **%0**; asgari maktu **71,2692 TL/litre** → **53,45 TL / 750 ml** | **fiilen MAKTU** | `FACT` **T1** |
| **5** | **KDV** | CIF + GV + KKDF + **ÖTV** + diğer | **%20** | oransal | `FACT` **T1** |
| 6 | **Bandrol (ÜİS)** | şişe başına | **2,36073 TL/şişe** (KDV hariç) — **peşin, satıştan ÖNCE** | maktu | `FACT` **T1** |
| 7 | **TADAB hizmet bedeli** | şişe başına | **0,1587 TL/şişe** | maktu | `FACT` |
| 8 | **Ruhsat / lisans (sabit)** | yıllık | **150.839 TL** (<20.000 lt/yıl) → **253.372 TL** (≥20.000 lt/yıl) | maktu | `FACT` |
| 9 | Damga vergisi (beyanname) | beyanname başına | **UNKNOWN** (2026 tutarı doğrulanmadı) | maktu | `UNKNOWN` |
| 10 | **Gözetim / referans kıymet** | — | **Tespit edilemedi** — 2204.21 için yürürlükte gözetim tebliği bulunamadı | — | `UNKNOWN` ⚠ *negatif arama* |

## 16.2 Zincir — açık yazılışı

```
CIF                     = C
Gumruk Vergisi          = C x 0,50  veya  C x 0,70
OTV matrahi             = C + GV + KKDF          <- GV DAHIL, OTV/KDV HARIC
OTV                     = 53,4519 TL/sise        <- MAKTU, matrahtan BAGIMSIZ
KDV matrahi             = C + GV + KKDF + OTV    <- OTV DAHIL
KDV                     = KDV matrahi x 0,20
──────────────────────────────────────────────────
L4 POST-TAX LANDED      = C + GV + KKDF + OTV + KDV
```

**İllüstratif — CIF = 100 TL/şişe, peşin ödeme:**

| Kalem | %50 menşe | %70 menşe |
|---|---|---|
| CIF | 100,00 | 100,00 |
| + Gümrük Vergisi | 50,00 | 70,00 |
| = ÖTV matrahı | 150,00 | 170,00 |
| + ÖTV (maktu) | 53,45 | 53,45 |
| = KDV matrahı | 203,45 | 223,45 |
| + KDV %20 | 40,69 | 44,69 |
| **= L4 POST-TAX LANDED** | **244,14** | **268,14** |
| **L4 / CIF** | **2,44×** | **2,68×** |

## 16.3 Maktu ÖTV'nin asimetrisi — **projenin çekirdek tehdidi**

> ÖTV fiyattan **tamamen bağımsızdır.** Ucuz şarap ile pahalı şarap **aynı TL
> tutarında** ÖTV öder.
>
> ```
> CIF =  50 TL  ->  OTV, CIF'in %107'si
> CIF = 300 TL  ->  OTV, CIF'in  %18'i
> ```
>
> **Yani ucuz şarap ithal etmek vergi açısından ORANTISIZ biçimde
> cezalandırılır.** Bu, projenin fiyat/performans mandasına **doğrudan yapısal
> bir tehdittir** ve merdivende yukarı doğru sürekli bir baskı yaratır.
>
> ⚠ **Ve ÖTV kendiliğinden artar:** ÖTVK md.12/3 gereği Ocak ve Temmuz
> aylarında Yİ-ÜFE değişimi oranında **otomatik yeniden belirlenmiş sayılır.**
> Son gerçekleşen artış **+%16,09** (61,3914 → 71,2692). Model hedef tarihinin
> **üçü de 2027'dedir** — yani bugünkü tutar **2027 için bir `FACT` değildir.**

## 16.4 KDV — iki perspektif (asla toplanmaz)

### A) EKONOMİK MALİYET GÖRÜNÜMÜ

> **İthalatta ödenen KDV İNDİRİLEBİLİR** → **ekonomik maliyet DEĞİLDİR.**
> Şişe başına ekonomik KDV maliyeti = **0,00 TL**.
>
> Dayanak: KDVK md.29/1-b (ithalde ödenen KDV indirilir) + md.34/1 (gümrük
> makbuzunda gösterilme + deftere kayıt). **md.30 tam metni tarandı — alkole
> özgü indirim yasağı YOKTUR** ve md.30 **tahdidi** bir listedir.
> Ayrıca KDVK md.36 uyarınca çıkarılmış ve alkolde indirimi kısıtlayan bir CB
> Kararı arandı: **7846 s. CBK vardır ama 2204.21'e DEĞMEZ** → etki
> **0,00 TL/şişe** (`T-947` **CONFIRMED**).

### B) NAKİT AKIŞI GÖRÜNÜMÜ

> **KDV gümrükte TAM TUTARIYLA NAKDEN ödenir** (KDVK md.46/2 — "gümrük vergisi
> ile birlikte ve aynı zamanda") ve **`peak_cash_requirement`'a TAM GİRER.**
>
> | Gerçek | Sonuç |
> |---|---|
> | Devreden KDV **iade edilmez** (md.29/2) | Yalnız gelecek dönem hesaplanan KDV'sinden **mahsup** edilir |
> | Geri kazanım **satış hızına kilitlidir** | Yavaş satış = uzun süre bağlı nakit |
> | Ödeme → ilk mahsup gecikmesi | **28–59 gün** (ortalama ~44); 3 aylık dönemde 28 → ~118 gün |
> | **Kaldırılamaz KDV tabanı** | ÖTV, KDV matrahındadır → CIF sıfıra gitse bile **53,4519 × 0,20 = 10,69 TL/şişe** KDV doğar |
>
> **Devreden KDV'nin finansman maliyeti `L5`'te GERÇEK bir maliyettir.**

**Örnek (799 TL hedef, İspanya, CHAIN, BASE, 5.000 şişe):**
```
Gumrukte NAKDEN odenen  :  282,41 TL/sise
  bunun icinde KDV       :   92,54 TL/sise  <- ekonomik maliyet DEGIL,
                                               ama NAKIT olarak odenir
```

## 16.5 ⛔ MENŞE BELGESİ KAYBININ BEDELİ

> ### %50 **KOŞULLU** BİR ORANDIR.
> Dört kümülatif koşul: **(K1)** eşya anlaşma kapsamında · **(K2)** menşe
> kuralını karşılıyor · **(K3)** geçerli belge var (EUR.1 / fatura beyanı) ·
> **(K4) doğrudan nakledilmiş.** Biri bile sağlanmazsa **otomatik %70.**

```
╔════════════════════════════════════════════════════════════════════╗
║  TERCIHLI REJIMI KAYBETMENIN BEDELI                                ║
║                                                                     ║
║  MAX_CIF(%70) / MAX_CIF(%50)  =  1,50 / 1,70  =  0,88235            ║
║                                                                     ║
║  ->  TAM  %11,765  KAYIP                                            ║
║  ->  799 TL / CHAIN / BASE / 5.000 sise:  -32,10 TL / sise          ║
║                                                                     ║
║  50.000 SISEDE TOPLAM:                                              ║
║        50.000  x  32,0977  =  1.604.885 TL                          ║
╚════════════════════════════════════════════════════════════════════╝
```

> **Bu, modelin HİÇBİR `UNKNOWN`'a bağlı olmayan tek sayısıdır.**
> Hedef fiyattan, ÖTV'den, marjdan, hacimden ve navlundan **bağımsızdır.**

**Hangi durumlarda kaybederiz:**

| Senaryo | Etki |
|---|---|
| Tedarikçi EUR.1 / fatura beyanı **düzenleyemiyor** | %70 |
| Şarapta **dökme ithal bileşen** var, başka ülkede şişelendi (K2 bozulur) | %70 |
| Sevkiyat **üçüncü ülkede konsolide edildi** (K4 bozulur) | %70 |
| 🇨🇱 **Şili + Barcelona aktarması** | ⚠ `UNKNOWN` — bozuyorsa %70 |
| 🇦🇺 AU · 🇲🇩 MD · 🇺🇸 US · 🇿🇦 ZA | **zaten %70** — düşecek tercih yok |

**Pazarlık karşılığı (`OD-1…OD-5`):** Tedarikçiden **sözleşmeyle** EUR.1
taahhüdü, menşe beyanı, doğrudan sevkiyat taahhüdü ve **belge düzenlenemezse
koşullu fiyat düzeltme maddesi** istenir. Bu kalem **32,10 TL/şişe değerindedir
ve pazarlıktaki en büyük tek kalemdir.**

---
---

# 17. PRIVATE LABEL vs EXISTING BRAND

| Boyut | **A) PRIVATE LABEL** | **B) EXISTING BRAND** |
|---|---|---|
| **Marka sahipliği** | **Bizde** *(reçete/IP doğrulanmadı — RFQ 4.9)* | Üreticide |
| **Marj potansiyeli** | Teorik olarak yüksek — aracı yok | ⚠ **Dış distribütör girerse: her +1 puan = −3,62 TL/şişe.** Distribütör marjı **`UNKNOWN`** ve modelde **0 alınmış** |
| **MOQ** | ✅ **3.000 · 3.600 · 6.000 — DOĞRULANMIŞ** | ⛔ **4 adayın 4'ünde de `UNKNOWN`** |
| **Marka inşası** | Sıfırdan · uzun · pahalı | Hazır · hızlı |
| **Pazarlama kısıtı** | ⚠⚠ **Alkolde reklam/tanıtım yasak** (`7584 s.K. m.2`, yürürlük 20/6/2026) → **hikâye anlatacak mecra YOK** → PL'in en büyük dezavantajı burada | Aynı yasak — ama marka zaten tanınıyorsa **daha az zarar görür** |
| **Tedarikçi bağımlılığı** | Düşük *(IP bizdeyse)* — üretici değiştirilebilir | **Yüksek** — üretici fiyatı tek taraflı revize edebilir |
| **Münhasırlık** | Konu değil | ⚠ Bölge **kapalı olabilir.** 26 tedarikçiden **1'inde fiilen kapalı çıktı** (Cantina Danese) |
| **Pazara çıkış hızı** | Yavaş — 4–6 hafta üretim + tasarım + klişe + TADAB ürün onayı | Muhtemelen hızlı — **ama lead time verisi YOK** |
| **Türkiye hakları riski** | **Marka çakışması** (TÜRKPATENT 33. sınıf taraması zorunlu) | **Bölge kapalılığı** + sözleşme bitince yatırım sıfırlanır |
| **Uzun vadeli işletme değeri** | **YÜKSEK** — marka bizim varlığımız olur | **DÜŞÜK** — sözleşme biterse geriye hiçbir şey kalmaz |

## 17.1 PRE-RFQ aşamasındaki değerlendirmem

> ## PRIVATE LABEL, PRE-RFQ AŞAMASINDA **DAHA GÜÇLÜDÜR** — ama sadece bir
> ## nedenle: **ÖLÇÜLEBİLİRDİR.**
>
> **Üç gerekçe:**
>
> 1. **Pilot ölçekte uygulanabilirliği KANITLI.** 3.000 ve 3.600 şişelik
>    MOQ'lar 5.000 şişelik pilotla uyumludur. Model A tarafında bu bilgi
>    **hiç yoktur** — bir MOQ bile bilmiyoruz.
> 2. **Uzun vadeli işletme değeri PL'dedir.** Bu proje bir dağıtım işi değil,
>    bir **marka kurma** işi olarak tasarlanırsa, sözleşme bitiminde elde
>    kalacak tek varlık markadır.
> 3. **Tedarikçi bağımlılığı düşüktür** — ve bu projede **`tedarikci.yaml →
>    alternatif_tedarikci_sayisi` iki turdur `0`**'dır.
>
> ### ⚠ AMA ÜÇ KARŞI ARGÜMAN — GİZLENMİYOR
>
> 1. **Bu üstünlük büyük ölçüde ARAMA YANLILIĞINDAN gelir.** PL sağlayıcıları
>    web'de aranabilir; marka sahipleri fuarda bulunur. Model B'nin daha zengin
>    görünmesi, **daha iyi olduğunu göstermez.**
> 2. **Reklam yasağı PL'i orantısız vurur.** Marka bilinirliği sıfır olan bir
>    ürünü, **hiçbir tanıtım aracı olmadan** rafta satmak zorundayız. Tanınmış
>    bir markayı dağıtmak bu handikapı **kısmen ortadan kaldırır.**
> 3. **İkisinin de FİYATI YOK.** İki modelin gerçek farkı `L6`'ya giren
>    distribütör marjının içindedir ve o **`UNKNOWN`**'dır.
>
> ### SONUÇ: KARAR VERİLMEZ — ÖLÇÜLÜR.
> **`Bodegas San Valero`'ya gönderilecek TEK RFQ, iki modelin fiyat farkını AYNI
> maliyet tabanı üzerinde ölçer.** Charter iki modeli **eşit öncelikli** tutar ve
> bu kural PRE-RFQ aşamasında **kaldırılmaz.** İlk 5 tedarikçi listesi bu yüzden
> **3 Model B + 1 Model A + 1 ikili** olarak kurulmuştur.

---
---

# 18. GEREKEN SERMAYE

## 18.1 ⛔ ÖNCE NET BİR CÜMLE

> # `peak_cash_requirement` TUTARI **HESAPLANAMAZ.**
>
> Bu bir eksiklik itirafıdır, bir gecikme değil. **Sahte bir rakam
> verilmeyecektir.** Gerekçe: sermaye ihtiyacının en büyük kalemi olan **malın
> kendisinin fiyatı bilinmiyor**, ikinci en büyük kalemi olan **vergiler o
> fiyata bağlı**, üçüncü kalemi olan **navlun doğrulanmamış**, ve **paranın ne
> kadar süre bağlı kalacağı** (antrepo bekleme + kanal vadesi) `UNKNOWN`.

## 18.2 Sermaye kalemleri — ne biliyoruz, ne bilmiyoruz

| # | Kalem | Ne biliyoruz | Statü |
|---|---|---|---|
| **1** | **Supplier (mal bedeli)** | Hiçbir teklif yok. Ödeme şartı bilinen **tek** üretici var ve o **%100 sevkiyat öncesi peşin** istiyor (Harland) | ⛔ **UNKNOWN** |
| **2** | **Freight** | LCL 9 rotada biliniyor (**ttl 6 gün**); **FCL hiçbir rotada yok** | ◐ **PARTIAL** |
| **3** | **Sigorta** | Oran %0,3–0,6 (CIF+%10) — `ESTIMATE`; **Türk kotasyonu yok** | ◐ PARTIAL |
| **4** | **Customs (gümrük vergisi)** | ✅ Oran ve matrah **T1 kanıtlı** — ama **CIF'e bağlı** | ◐ formül var, tutar yok |
| **5** | **ÖTV** | ✅ **53,4519 TL/şişe** — CIF'ten **bağımsız, kesin.** 5.000 şişede **267.260 TL**; 25.000'de **1.336.298 TL** | ✅ **KNOWN** |
| **6** | **Import VAT (KDV)** | ✅ Formül kesin; ekonomik maliyet **değil** ama **gümrükte nakden ödenir** ve 28–59 gün bağlı kalır. Kaldırılamaz taban: **10,69 TL/şişe** | ◐ formül var, tutar CIF'e bağlı |
| **7** | **Bandrol** | ✅ **2,36073 TL/şişe**, **peşin, satıştan önce.** 5.000 şişede **11.804 TL** | ✅ **KNOWN** |
| **8** | **Licensing / ruhsat (sabit)** | ✅ **150.839 TL** (<20.000 lt/yıl) → **253.372 TL** (≥20.000 lt/yıl). ⚠ Bu bir **kademe sıçramasıdır** — 26.667 şişede tetiklenir | ✅ **KNOWN** |
| **9** | **Warehouse / antrepo** | Depolama 0,35 EUR/palet/gün (**T5, LOW**), **minimum 7 gün**. Elleçleme, yeniden paletleme, bandrolleme operasyonu → hepsi **UNKNOWN** | ⛔ **UNKNOWN** (`T-314`) |
| **10** | **Inventory (bağlı stok)** | Süre **UNKNOWN** — antrepo zorunlu bekleme süresi `T-301` (**CRITICAL**) ile açık | ⛔ **UNKNOWN** |
| **11** | **Retailer receivables (alacak)** | Vade **`ASSUMPTION`**: zincir 60 gün BASE (45/60/90/**120**), tekel 30 gün. ⚠ **Yasal vade tavanı belirsiz** — şarap 6585 s.K. m.7/3 anlamında "tarım ve gıda ürünü" mü? `T-601` (**CRITICAL**) | ⛔ **UNKNOWN** |
| **12** | Gümrük müşavirliği, ordino, iç nakliye, X-ray | ✅ Biliniyor: müşavirlik **6.020 TL**, ordino 2.000–5.000 TL, İstanbul içi nakliye 10.000–15.000 TL | ✅ KNOWN |
| **13** | Kendi dağıtım ekibi | Taban: **40.214,03 TL/ay/kişi** → 5.000 şişe/yılda **96,51 TL/şişe** *(yalnız 1 kişinin asgari ücreti)* | ✅ taban KNOWN |
| **14** | Marka tescili, etiket klişe/kalıp, numune | ⛔ **UNKNOWN** — numune talebi ayrı bütçe + ayrı gümrük/ÖTV sorusu doğurur (`T-893`) | ⛔ UNKNOWN |

## 18.3 Hacme göre sermaye görünürlüğü

| Hacim | Görünürlük | Neden |
|---|---|---|
| **5.000** | **PARTIAL** | ÖTV, bandrol, ruhsat, müşavirlik biliniyor (**~450 bin TL sabit taban**); mal bedeli, gümrük vergisi, KDV, navlun ve **süre** bilinmiyor |
| **10.000** | **PARTIAL** | Aynı + ⚠ **ters modelde bu hacim kademesi HİÇ ÇALIŞTIRILMAMIŞTIR** (`T-865`/`T-963`). İnterpolasyon yasaktır |
| **25.000** | **PARTIAL** | Aynı + **ruhsat kademesi sıçrar** (26.667 şişede 150.839 → 253.372 TL) |
| **50.000** | **UNKNOWN** | Sevkiyat sayısı, konteyner tipi, dağıtım organizasyonu ve stok döngüsü hakkında **hiçbir doğrulanmış veri yok** |
| **100.000** | **UNKNOWN** | ⚠ Bu hacim ilk RFQ'da **sorulmayacaktır** → fiyat çapası **yok** (`NO_RFQ_ANCHOR`). V50K'dan ekstrapolasyon **yasaktır** |

**Kesin olarak bilinen tek sermaye bileşeni — hacimle doğrusal:**

| Hacim | ÖTV | Bandrol | Ruhsat (yıllık sabit) | **Toplam kesin taban** |
|---|---|---|---|---|
| 5.000 | 267.260 TL | 11.804 TL | 150.839 TL | **429.903 TL** |
| 10.000 | 534.519 | 23.607 | 150.839 | **708.965** |
| 25.000 | 1.336.298 | 59.018 | **253.372** | **1.648.688** |
| 50.000 | 2.672.595 | 118.037 | 253.372 | **3.044.004** |

> ⚠ **Bu tablo sermaye ihtiyacı DEĞİLDİR.** Yalnızca **kesin olarak bilinen üç
> kalemin toplamıdır** ve **mal bedeli, gümrük vergisi, KDV, navlun, depo,
> dağıtım ve alacak finansmanını İÇERMEZ.** Gerçek sermaye ihtiyacı bundan
> **çok daha yüksektir.**

## 18.4 ⭐ HANGİ 3 VERİ GELİRSE SERMAYE İHTİYACINI HESAPLAYABİLİRİZ

```
╔════════════════════════════════════════════════════════════════════════╗
║                                                                         ║
║   1.  GERCEK FOB/EXW FIYATI  (para birimi + Incoterm + yer belirtilmis) ║
║       -> en az 5 tedarikciden, tarihli ve gecerlilik sureli             ║
║       Kim  : global-sourcing-kasifi (RFQ)          Ticket: T-466        ║
║       Neyi acar: CIF -> gumruk vergisi -> KDV matrahi -> mal bedeli     ║
║                  = sermayenin EN BUYUK kalemi                           ║
║                                                                         ║
║   2.  DOGRULANMIS FCL/LCL NAVLUNU  (included/excluded charges tek tek)  ║
║       -> 3 forwarder'dan YAZILI kotasyon                                ║
║       Kim  : navlun-lojistik-uzmani                Ticket: T-304        ║
║       Neyi acar: FOB -> CIF koprusu + tasima modu karari                ║
║                                                                         ║
║   3.  ZAMAN EKSENI: antrepo zorunlu bekleme suresi + yasal vade tavani  ║
║       -> (a) ruhsat/bandrol nedeniyle malin bekleyecegi gun sayisi      ║
║          (b) sarap 6585 m.7/3 anlaminda "tarim ve gida urunu" mu        ║
║       Kim  : mevzuat-ruhsat-uzmani                 Ticket: T-301, T-601 ║
║       Neyi acar: paranin KAC GUN bagli kalacagi = peak_cash'in ZAMAN    ║
║                  ekseni. Tutar bilinse bile bu olmadan PEAK bulunamaz   ║
║                                                                         ║
╚════════════════════════════════════════════════════════════════════════╝
```

> **Üçü de `CRITICAL` ticket'tır ve üçü de bugün `OPEN`'dır.**
> **1 ve 2 dış temas gerektirir** (RFQ + forwarder) — yani bu raporun önerdiği
> eylemin doğrudan çıktısıdır. **3 masabaşı araştırmadır** ve **hiçbir izne
> bağlı değildir** — bugün başlatılabilir.

---
---

# 19. KÂR POTANSİYELİ

## 19.1 ⛔ ÖNCE NET BİR CÜMLE

> # **GERÇEK KÂR HESAPLANAMAZ.**
> Çünkü **gerçek FOB yoktur.** Bir kâr rakamı üretmek, bu projenin en temel
> kuralını (`CLAUDE.md` §1.1) ihlal etmek olurdu.
>
> **`ROI` ve `IRR` bu raporda ÜRETİLMEMİŞTİR ve üretilemez.**

Ama üç soru **cevaplanabilir** — ve cevapları karar için yeterlidir.

## 19.2 SORU 1 — Model **yapısal olarak** kâra izin veriyor mu?

# ✅ EVET.

**Kanıt:** Ters model 2.700 kombinasyonda çalıştırılmıştır ve
**`MAX_CIF` hiçbirinde negatif çıkmamıştır.** Zincir ve tekel kanallarında beş
fiyat basamağının beşinde de tavan **137–429 TL/şişe** bandındadır.

> ### BAŞKANIN KENDİ HİPOTEZİ ÇÜRÜTÜLDÜ
> TUR 2.5 öncesinde şu hipotez kaydedilmişti: *"999 TL'de bile ödenebilir CIF
> negatif veya sıfıra yakın çıkar."* **Bu hipotez model tarafından
> ÇÜRÜTÜLMÜŞTÜR.** Segment **aritmetik olarak imkânsız değildir.**
>
> **Bu, bu projenin en önemli tek olumlu bulgusudur** — ve bir "iyi haber"
> değil, bir **hipotezin yanlışlanmasıdır.**

⚠ **Ama iki niteleme:**
- Tavan `UPPER_BOUND`'dur; **26 maliyet kalemi `0` alınmıştır** ve hepsi
  pozitiftir → gerçek tavan **daha düşüktür.**
- **HoReCa 5,0× çarpanda 599 TL matematiksel olarak ÖLÜDÜR** (yapısal taban
  546,77 TL). Yani model her koşulda değil, **belirli koşullarda** kâra izin
  verir.

## 19.3 SORU 2 — Hangi satın alma fiyatının altında alan açılıyor?

**Alan, satın alma fiyatı yapısal tavanın altına indiği ölçüde açılır:**

| Fiyat noktası | 799 / P grubu | Ne anlama gelir |
|---|---|---|
| **272,83 TRY/şişe** *(4,95 EUR)* | **YAPISAL TAVAN** | Kâr **tam olarak sıfır** |
| **~205–218 TRY** *(3,71–3,96 EUR)* | AGGRESSIVE politika | Dar tampon; X köşesini aşar |
| **~164–177 TRY** *(2,97–3,21 EUR)* | **BASE politika** ✅ | %35–40 tampon — **önerilen bölge** |
| **~136 TRY** *(2,47 EUR)* | CONSERVATIVE politika | Geniş tampon; tedarikçi bulmak zor olabilir |
| **144,21 TRY raf fiyatı** | **YAPISAL TABAN** | Bu raf fiyatının altında tedarikçi **bedava verse bile** model kapanmaz |

**Gözlenen referans noktaları (bunlar teklif DEĞİLDİR — ülke ortalamalarıdır):**

```
Moldova   L2 CIF  2,46 USD/litre  =  1,85 USD / 750 ml
Ispanya   L2 CIF  2,71 USD/litre  =  2,03 USD / 750 ml
Sili      L2 CIF  2,89 USD/litre  =  2,17 USD / 750 ml
Portekiz  L2 CIF  3,20 USD/litre  =  2,40 USD / 750 ml
Italya    L2 CIF  3,65 USD/litre  =  2,74 USD / 750 ml
Fransa    L2 CIF  6,27 USD/litre  =  4,70 USD / 750 ml
```

> ### DİKKATE DEĞER GÖZLEM
> Türkiye'nin İspanya'dan **fiilen ithal ettiği** ortalama CIF birim değeri
> **2,03 USD/şişe**'dir. Bizim yapısal tavanımız **5,72 USD/şişe**'dir.
> Yani **gözlenen ortalama, tavanın yaklaşık üçte biridir.**
>
> ⛔ **Bu bir "bol bol alan var" iddiası DEĞİLDİR.** Üç nedenle:
> (a) o ortalama bir **ülke karışımıdır**, bizim SKU'muz değil;
> (b) tavan **26 kalem eksik** hesaplanmıştır;
> (c) o ortalamanın içinde **kim, hangi hacimde, hangi vadeyle aldı**
> bilinmiyor. Ama **yön olarak** olumludur ve RFQ göndermeyi haklı çıkarır.

## 19.4 SORU 3 — Hangi faktör kârı **en hızlı** yok ediyor?

**Tornado — 799 TL · İspanya · CHAIN · 5.000 şişe · BASE = 272,83 TL/şişe:**

| Sıra | Eksen | Δ− (TL/şişe) | Δ+ | Tip |
|---|---|---|---|---|
| **1** | **İthalatçı katkı payı 0 → %30** | **−108,56** | 0 | **KARAR** — veri değil |
| **1** | **Distribütör marjı 0 → %30** | **−108,56** | 0 | `UNKNOWN` |
| **3** | Hedef fiyat 599 ↔ 999 | −83,33 | +83,33 | senaryo |
| **4** | **Kendi dağıtım 0 → 1 kişi** | **−64,34** | 0 | taban; gerçek daha yüksek |
| **5** | **Kanal marjı (18/25/35%) + `d`** | **−45,06** | +32,00 | **tamamı `ASSUMPTION`** |
| **6** | **Gümrük vergisi %50 → %70** | **−32,10** | 0 | **tek yönlü risk** |
| **7** | ÖTV λ (1,00 → 1,5625) | −20,04 | 0 | **tek yönlü aşağı** |
| **8** | Hacim 5.000 → 100.000 | 0 | **+20,20** | ruhsat kademesi yüzünden **sınırlı** |

### Dört yönetim okuması

> **1. Kârı en hızlı yok eden şey bir VERİ değil, bir KARARDIR.**
> En büyük iki eksen (ithalatçı katkı payı ve distribütör marjı) **model
> dışındadır** — biri bizim kâr hedefimiz, diğeri bir pazarlık meselesidir.
> Modelin belirsizliğinin en büyük kısmı **bir veri eksikliği değil, bir karar
> eksikliğidir.**
>
> **2. Vergi eksenlerinin TAMAMI TEK YÖNLÜDÜR ve hepsi AŞAĞI bakar.**
> `g` yalnızca %70'e çıkabilir (%50 zaten en iyi hâl); `λ` yalnızca ≥1 olabilir.
> **Vergi tarafında YUKARI SÜRPRİZ YOKTUR.** Bu, sağlam ama tek yönlü bir
> zemindir.
>
> **3. Kanal marjı üçüncü en büyük eksendir ve BANDININ TAMAMI `ASSUMPTION`'DIR.**
> −45,06 / +32,00 TL'lik bir bant, hiçbir kanıta dayanmıyor. Bu, raporun en
> rahatsız edici tek satırıdır.
>
> **4. HACİM, tornadonun EN KÜÇÜK eksenidir.** 20 kat büyümenin etkisi
> (+20,20 TL) **tek kişilik bir dağıtım ekibinin maliyetinden (−64,34 TL) ÜÇ
> KAT KÜÇÜKTÜR.** Yani *"büyürsek kurtarırız"* argümanı **modelde
> DOĞRULANMAMIŞTIR.**

## 19.5 Ölçek hakkında kritik bulgu

```
5.000  -> 25.000   :  MAX_CIF  +17,68 TL   (olcek kazanciNIN %87'si)
25.000 -> 50.000   :  MAX_CIF   +0,77 TL   <- neredeyse SIFIR
50.000 -> 100.000  :  MAX_CIF   +1,75 TL
```

> **Sebebi navlun DEĞİL, bir RUHSAT KADEMESİDİR:** `toplam_ruhsat_sabit_maliyeti`
> **20.000 litre/yıl** eşiğinde **150.839 → 253.372 TL**'ye sıçrar
> (= 26.667 şişe).
>
> **İş sonucu:** Bu proje **büyük olmayı gerektirmiyor.** 25.000 şişe/yıl,
> ölçek ekonomisinin **%87'sini** zaten veriyor. 100.000'e çıkmanın satın alma
> gücüne katkısı **ihmal edilebilir.** Bu, sermaye planlaması açısından
> **iyi bir haberdir.**

---
---

# 20. NECESSARY CONDITIONS

> *"Bu işin çalışması için ne DOĞRU OLMALI?"*
> Her koşul `PASS` / `UNKNOWN` / `FAIL` olarak işaretlenmiştir.
> **`UNKNOWN` bir başarısızlık değildir — henüz ölçülmemiş demektir.**

| # | Koşul | Durum | Dayanak |
|---|---|---|---|
| **NC-01** | Bu iş Türkiye'de **yasal olarak kurulabilir** olmalı | **PASS** ⚠ | TADAB dağıtım yetki belgesi + toptan satış belgesi + ürün onayı yolu **haritalanmış**. ⚠ Ama `G0` **beş turdur test edilmedi** ve iki açık çelişki üzerinde duruyor |
| **NC-02** | Vergi yükü **kanıtlı ve satır satır hesaplanabilir** olmalı | **PASS** | GTİP, GV, ÖTV, KDV, KKDF ve **matrah sırası** T1 düzeyinde doğrulanmış; 10/10 birim test |
| **NC-03** | İthalatta ödenen **KDV indirilebilir** olmalı | **PASS** | KDVK md.29/1-b + md.34/1; md.30 tam metin taraması; md.36 CB kararı arandı → **2204.21'e değmiyor** |
| **NC-04** | GTİP **2204.21** doğru olmalı (köpüklü/aromatize DEĞİL) | **PASS** | Köpüklü olsaydı ÖTV 53,45 → **361,14 TL/şişe** — projeyi tek başına öldürürdü |
| **NC-05** | Model **yapısal olarak pozitif alan** bırakmalı | **PASS** | 2.700 kombinasyonun hiçbirinde `MAX_CIF` negatif değil |
| **NC-06** | Ölçek ekonomisi **ulaşılabilir hacimde** gerçekleşmeli | **PASS** | %87'si 5.000 → 25.000 sıçramasında |
| **NC-07** | Pilot hacmiyle uyumlu **MOQ** bulunabilmeli | **PASS** | 3.000 (Interbrosa) ve 3.600 (The Wine Factory) doğrulandı |
| **NC-08** | Çalışan bir **tedarik hattı** olmalı | **PASS** | ES 1,92 m lt · IT 5,75 m lt · FR 2,85 m lt · MD 2,04 m lt · CL 0,95 m lt (2025) |
| **NC-09** | **Gerçek tedarikçi fiyatı** yapısal tavanın altında olmalı | ⛔ **UNKNOWN** | **26/26 tedarikçiden teklif YOK.** `T-466` CRITICAL |
| **NC-10** | **Menşe belgesi** her sevkiyatta alınabilmeli | ⛔ **UNKNOWN** | Hiçbir tedarikçiden taahhüt alınmadı. Kaybın bedeli **−32,10 TL/şişe** |
| **NC-11** | **Doğrulanmış navlun** (FCL) olmalı | ⛔ **UNKNOWN** | 14 lane'in hiçbirinde kamuya açık FCL kotasyonu yok. `T-304` CRITICAL |
| **NC-12** | Hedeflenen rafta **gerçek fiyat gözlemi** olmalı | ⛔ **UNKNOWN** | `L8_CHAIN_RETAIL`'de **SIFIR gözlem.** `T-603`/`T-701` |
| **NC-13** | **Kanal marjı, listeleme bedeli ve geri akan bedeller** bilinmeli | ⛔ **UNKNOWN** | Üçü de `ASSUMPTION`/`UNKNOWN`. Tek çapa Migros %24,31 ve **şarap değil** |
| **NC-14** | Ürün **rafta dönmeli** (talep olmalı) | ⛔ **UNKNOWN** | Türkiye'de şarap için **tek bir talep/rotasyon verisi YOK.** `C-561` |
| **NC-15** | **Antrepoda bekleme süresi** ve **yasal vade tavanı** bilinmeli | ⛔ **UNKNOWN** | `T-301` ve `T-601` — ikisi de **CRITICAL, OPEN** |
| **NC-16** | Bir zincir bizi **listelemeli** | ⛔ **UNKNOWN** | Hiçbir perakendeciyle temas kurulmadı |
| **NC-17** | Hedef **599,90 TL benchmark'ının statüsü** netleşmeli | ⛔ **UNKNOWN** | Promosyon durumu `UNKNOWN`. **`OQ-001` kapanmadan `G3` geçilemez** |
| **NC-18** | **Kur riski** taşınabilir olmalı | ⚠ **UNKNOWN** | Kur bugün gözlendi ama hedef tarihler **2027'de**. Model: FX ekseni açıklığı (×1,33) X→Y bandından (×1,45) **dar** — ama eksenin **dar seçilmiş olabileceği** kayıtlı (`T-874`) |
| **NC-19** | **Yatırımcı eşikleri** belirlenmeli | ⛔ **UNKNOWN** | 6 finansal eşiğin **6'sı da `TBD`**. `OQ-901` / `T-851` CRITICAL |
| **NC-20** | Ürün **marka çakışması** yaşamamalı (TÜRKPATENT 33. sınıf) | ⛔ **UNKNOWN** | Tarama yapılmadı |

## 20.1 Dağılım

```
╔═══════════════════════════════════════════════════════════╗
║   PASS      :  8  /  20     (%40)                          ║
║   UNKNOWN   : 12  /  20     (%60)                          ║
║   FAIL      :  0  /  20     (%0)      <-- BELIRLEYICI      ║
╚═══════════════════════════════════════════════════════════╝
```

> ## BU DAĞILIMIN ANLAMI — TEK CÜMLE
> **Hiçbir zorunlu koşul `FAIL` değildir.** Yani bu işi **bugün öldüren
> yapısal bir engel yoktur.** Ama 20 koşulun 12'si `UNKNOWN`'dır — yani bu işi
> **bugün onaylayacak bir temel de yoktur.**
>
> **Ve kritik ayrım şudur:** 12 `UNKNOWN`'ın **7'si masabaşıyla kapanmaz**
> (NC-09, NC-10, NC-11, NC-13, NC-14, NC-16 ve kısmen NC-12) — bunlar **dış
> temas veya fiziksel gözlem** gerektirir. Bu, `PROCEED TO RFQ` kararının
> mantığıdır: **daha fazla masabaşı çalışma bu tabloyu DEĞİŞTİRMEZ.**

---
---

# 21. STRESS TEST

> **Referans nokta:** 799 TL raf · İspanya · CHAIN RETAIL · 5.000 şişe · BASE ·
> DOC_OK · λ=1 → **`MAX CIF` = 272,83 TL/şişe**
> Aşağıdaki tüm rakamlar **satın alma tavanı** üzerindendir, kâr üzerinden değil.

## 21.1 GOOD CASE

| Değişiklik | Etki |
|---|---|
| Hacim 25.000'e çıkar | 272,83 → **290,51** (+17,68) |
| Kanal marjı LOW ucunda (%18, d=%3) | +32,00 |
| Hedef 899 TL'ye çıkar | +41,67 |
| Menşe belgesi **her sevkiyatta alınır** | %50 korunur (kayıp yok) |
| ÖTV Ocak 2027'de artmaz (CB kararı) | λ=1 korunur |

**Bileşik GOOD CASE (25.000 şişe · LOW kanal · 799 TL · DOC_OK):**
```
MAX CIF  =  321,96 TRY/sise   =  5,84 EUR   =  6,75 USD
```
*(Kaynak: `country-buying-ceilings.csv`, ES/DOC_OK/25000/LOW/799)*

## 21.2 BASE CASE

```
MAX CIF  =  272,83 TRY/sise   =  4,95 EUR   =  5,72 USD   (5.000 sise)
MAX CIF  =  290,51 TRY/sise   =  5,27 EUR   =  6,09 USD   (25.000 sise)
```

## 21.3 BAD CASE

| Değişiklik | Etki |
|---|---|
| **Menşe belgesi kaybı** (%50 → %70) | −32,10 (**−%11,765**) |
| **Kanal marjı HIGH ucunda** (m=%35, d=%18) | −45,06 |
| **Lojistik HIGH** | *(TR-içi bacak; ±0,93 TL — küçük)* |
| **ÖTV λ = 1,5625** (iki adım artış) | −20,04 |
| **Kendi dağıtım, 1 kişi** | −64,34 |
| **Raf fiyatı 799 → 699'a baskılanır** | −41,67 |

**Bileşik BAD CASE (5.000 şişe · HIGH kanal · DOC_FAIL · 799 TL):**
```
MAX CIF  =  200,98 TRY/sise   =  3,64 EUR   =  4,21 USD      <- X kosesi
```

**Daha da kötüsü (aynı köşe + 699 TL raf baskısı):**
```
MAX CIF  =  169,12 TRY/sise
```

## 21.4 Özellikle istenen beş stres

### (a) **FX +%20**

**Hesaplanabiliyor.** `makro.yaml → fx.senaryolar` dört eksende tanımlı:

| Eksen | EUR/TRY | USD/TRY | MAX CIF (272,83 TRY) → EUR | → USD |
|---|---|---|---|---|
| `FX_DOWN_10` | 49,6273 | 42,9406 | **5,50** | **6,35** |
| **`FX_0`** *(bugün)* | **55,1414** | **47,7118** | **4,95** | **5,72** |
| `FX_UP_10` | 60,6555 | 52,4830 | **4,50** | **5,20** |
| **`FX_UP_20`** | **66,1697** | **57,2542** | **4,12** | **4,77** |

> **FX +%20 → satın alma gücümüz döviz cinsinden %16,7 düşer.**
> 4,95 EUR → **4,12 EUR**.
>
> ### YAPISAL BULGU — MODELİN GİRDİSİZ İKİNCİ SAYISI
> **Kur hareketi TEK BAŞINA bir teklifi `STRONG`'dan `ABOVE_CEILING`'e
> çeviremez.** Çünkü X→Y bandı **×1,4455**, FX ekseninin uçtan uca açıklığı ise
> **×1,3333**'tür. Band, eksenden **geniştir.**
>
> ⚠ **Ama bu bir güvence değildir:** bu, kur riskinin senaryo riskinden küçük
> olduğu anlamına gelebilir — **ya da FX ekseninin çok dar seçildiği** (`T-874`,
> OPEN). 2027 ufku için ±%10/+%20 bandı **yeterince geniş mi**, doğrulanmadı.

### (b) **Menşe belgesi kaybı**

**Hesaplanabiliyor ve KESİN:** **−32,0977 TL/şişe = TAM %11,765.**
50.000 şişede **−1.604.885 TL.** Hedef fiyattan, ÖTV'den, marjdan, hacimden ve
navlundan **bağımsızdır.** Modelin hiçbir `UNKNOWN`'a bağlı olmayan tek sayısı.

### (c) **Retailer high margin** (m=%35, d=%18)

**Hesaplanabiliyor:** 272,83 → **227,78** (**−45,06 TL/şişe, −%16,5**).
⚠ Ama bandın **tamamı `ASSUMPTION`**'dır — %35'in de %18'in de kanıtı yoktur.
Tek kanıtlı çapa Migros'un **tüm kategori** %24,31'idir.

### (d) **Logistics high**

**Ters model üzerinde etkisi ≈ SIFIRDIR** — ve bu **karşı-sezgisel ama
doğrudur:** okyanus navlunu ve sigorta **CIF'in İÇİNDEDİR** (GK md.27/1-e).
Ters model CIF **tavanını** verir; navlun o tavanın **nasıl bölüşüleceğini**
belirler, tavanın kendisini değil. Modelde navlunun tek görünür etkisi TR-içi
(TRY) bacaktır: 5.000 şişede **±0,93 TL.**

> ⚠ **Bu, `C-311`'in (FCL bandının 4 katı) önemsiz olduğu anlamına GELMEZ.**
> Navlun, **`MAX_FOB`'u** doğrudan değiştirir — yani **tedarikçiye
> ödeyebileceğimiz fiyatı.** İleri model ve FOB pazarlığı için **`T-304` hâlâ
> `CRITICAL` bir blokerdir.**

### (e) **799 → 699 raf baskısı**

**Hesaplanabiliyor:** 272,83 → **231,16** (**−41,67 TL/şişe, −%15,3**).
Bileşik olarak BAD CASE köşesiyle birlikte: **200,98 → 169,12** (−%15,9).

> **Yönetim okuması:** Perakendeci *"bu ürün 699'dan yukarısını taşımaz"*
> derse, satın alma bütçemiz **şişe başına ~42 TL daralır** — bu, menşe belgesi
> kaybından (32,10) **daha büyük** bir darbedir. Raf fiyatı pazarlığı, tarife
> pazarlığından **daha değerlidir.**

## 21.5 Stres testi özeti

| Senaryo | MAX CIF TRY | EUR | USD | Bugüne göre |
|---|---|---|---|---|
| **GOOD** (25k · LOW · DOC_OK) | **321,96** | 5,84 | 6,75 | **+%18,0** |
| **BASE** (25k · BASE · DOC_OK) | 290,51 | 5,27 | 6,09 | +%6,5 |
| **BASE** (5k · BASE · DOC_OK) | **272,83** | 4,95 | 5,72 | — |
| **BASE + FX_UP_20** | 272,83 | **4,12** | **4,77** | döviz cinsinden **−%16,7** |
| **BAD** (5k · HIGH · DOC_FAIL) | **200,98** | 3,64 | 4,21 | **−%26,3** |
| **BAD + 699 raf** | **169,12** | 3,07 | 3,54 | **−%38,0** |

> **En kötü ile en iyi arasındaki fark ×1,90'dır** (169,12 ↔ 321,96).
> Bu, bir yatırım kararı vermek için **çok geniş bir banttır** — ve bandın
> genişliğinin büyük kısmı **kanıt eksikliğinden**, gerçek belirsizlikten değil.

---
---

# 22. EN BÜYÜK 10 RİSK

| # | Risk | Olasılık | Etki | Durum | Azaltma | Sıradaki kanıt |
|---|---|---|---|---|---|---|
| **1** | **Gerçek tedarikçi fiyatı yapısal tavanın üstünde çıkar** → iş modeli kapanmaz | **UNKNOWN** | **KILL-LEVEL** | 🔴 OPEN | RFQ ile ≥5 gerçek teklif; her teklifi 4 FX ekseninde ayrı ayrı ölç | `FIRM_QUOTE` × 5 · `T-466` |
| **2** | **Ürün rafta dönmez** — Türkiye'de şarap talebi hakkında sıfır verimiz var | **UNKNOWN** | **KILL-LEVEL** | 🔴 OPEN | Perakendeciyle ön görüşme: listeleme niyeti + beklenen aylık çıkış; mağaza turunda raf devri gözlemi | Perakendeciden hacim beklentisi · `C-561` |
| **3** | **Hedef raf fiyatı yanlış** — 799'un hangi rafın fiyatı olduğu bilinmiyor, `L8_CHAIN_RETAIL`'de 0 gözlem | **HIGH** | **CRITICAL** | 🔴 OPEN | **Tek fiziksel mağaza turu** — beş açık soruyu aynı anda kapatır | Zincir market raf fiyatı · `T-917` |
| **4** | **Kanal marjı, `d` ve `f` tamamen varsayım** — tornado'nun 3. büyük ekseni, bandın tamamı `ASSUMPTION` | **HIGH** | **CRITICAL** | 🔴 OPEN | Faal bir ithalatçıdan gerçekleşmiş koşul seti; perakendeci ile ön müzakere | Gerçek zincir anlaşması kalem listesi · `T-604` |
| **5** | **Menşe belgesi alınamaz / doğrudan nakliyat sağlanamaz** → %50 → %70 | **MEDIUM** | −32,10 TL/şişe · 50k'da −1,60 m TL | 🟠 OPEN | Sözleşmeye `OD-1…OD-5` + **koşullu fiyat düzeltme maddesi** (`OD-5`) | Tedarikçi EUR.1 taahhüdü · `T-161`, `T-914` |
| **6** | **Doğrulanmış FCL navlunu yok** — band 4–5 kat | **HIGH** | Pilot taşıma kararını ve peak cash'i bloke ediyor | 🔴 OPEN | 3 forwarder'dan yazılı kotasyon — **paket HAZIR, gönderilmedi** | Yazılı FCL kotasyonu · `T-304`, `T-821` |
| **7** | **Antrepo bekleme süresi + yasal vade tavanı bilinmiyor** → paranın kaç gün bağlı kalacağı `UNKNOWN` | **HIGH** | **CRITICAL** — peak cash'in zaman ekseni kırık | 🔴 OPEN | Masabaşı mevzuat araştırması **+ faal ithalatçı görüşmesi** — izin gerektirmez | Gerçekleşmiş ithalat takvimi · `T-301`, `T-601` |
| **8** | **ÖTV kendiliğinden artar** (Ocak/Temmuz, Yİ-ÜFE) — model hedef tarihi 2027 | **HIGH** *(mekanizma `FACT`)* | λ=1,5625'te **−20,04 TL/şişe** | 🟠 OPEN | Duyarlılık ekseni olarak taşı; bugünkü tutarı 2027 için `FACT` gibi **kullanma** | Ocak 2027 Resmî Gazete ilanı · `T-104`, `T-965` |
| **9** | **`G0` (yasal yol) beş turdur test edilmedi** — iki açık çelişki üzerinde duruyor | **MEDIUM** | `G0 PASS` **geri alınabilir** | 🟠 OPEN | TADAB'a yazılı görüş talebi **veya** faal küçük ölçekli ithalatçıyla tek görüşme | TADAB yazılı görüşü · `C-252`, `C-203`, `C-202` |
| **10** | **Model çıktılarının tamamı `DRAFT`/`UPPER_BOUND`** — 12 açık CRITICAL, 26 kalem `BLOCKED_INPUT` | **KESİN** | Hiçbir sayı `APPROVED` değil | 🔴 OPEN | `CLAUDE.md` §5 gereği açık CRITICAL kapanmadan model `APPROVED` olamaz; sayılar **karar aracı olarak yalnızca üst sınırdır** | CRITICAL ticket kapanışları · `INDEX.md` |

## 22.1 Risklerin ortak deseni — kayda geçiyor

> ### DÖRT BAĞIMSIZ İYİMSERLİK KAYNAĞI, AYNI MODELDE, AYNI YÖNDE
>
> | Kaynak | Yön |
> |---|---|
> | **26 maliyet kalemi `0` alındı** — hepsi pozitiftir | tavanı **yukarı** saptırır |
> | **λ = 1 çapası** — ÖTV yalnızca artabilir | tavanı **yukarı** saptırır |
> | **`d` tekelde `0` alındı** — tekel kanalı **%11,4 yapay yüksek** görünüyor | kanal karşılaştırmasını **bozar** |
> | **Kalemin niteliği belirsizse model onu SESSİZCE ATLAR** — `R5` hatası (28,95 TL), `C-851`, `C-852` — **üçünde de sapma projenin LEHİNE** | tavanı **yukarı** saptırır |
>
> **Modelin tüm bilinen sapmaları AYNI YÖNDEDİR: projenin lehine.**
> Bu, karar verirken **tavanları optimist okumamak** için yeterli gerekçedir.

---
---

# 23. "BOŞUNA EMEK HARCAMA" TESTİ

## 23.1 SORU A — *"RFQ göndermeden BUGÜN bu projeyi öldürmek için yeterli kanıt var mı?"*

# → **NO**

**Gerekçe — dört madde:**

1. **Hiçbir zorunlu koşul `FAIL` değildir.** 20 necessary condition'ın **0'ı**
   `FAIL`. 8'i `PASS`, 12'si `UNKNOWN`. **Öldüren bir bulgu yoktur.**
2. **Öldürmesi beklenen hipotez ÇÜRÜTÜLDÜ.** *"999 TL'de bile ödenebilir CIF
   negatif veya sıfıra yakın çıkar"* hipotezi 2.700 kombinasyonda test edildi ve
   **hiçbirinde `MAX_CIF` negatif çıkmadı.** Segment **aritmetik olarak
   imkânsız değildir.**
3. **Vergi tarafı — bir ithalat projesinin en sık öldüğü yer — SAĞLAM.**
   GTİP, oranlar, matrah sırası T1 düzeyinde doğrulanmış ve testle korunmuş.
   Ayrıca en tehlikeli tek olasılık (**alkolde KDV indirim kısıtı**) araştırıldı
   ve **bulunmadı** — etki **0,00 TL/şişe.**
4. **`G2` ve `G3` gate'leri *"tedarik kaynağı yok"* diye değil, "HENÜZ
   SORULMADI" diye kapalıdır.** TUR 3B'yi bloke eden 10 kalemin **6'sı bir
   araştırma boşluğu DEĞİLDİR** — dördü bir **karar**, ikisi bir **izin**
   bekliyor. **Bu, bir `KILL` gerekçesi olarak kullanılamaz.**

> ⚠ **Karşı argüman ciddiye alınmıştır ve zayıf bulunmamıştır:**
> *"Talep hakkında sıfır verimiz var; bilmediğimiz bir pazara ürün getiriyoruz."*
> Bu doğrudur. Ama bu, **`KILL` değil, `TEST` gerekçesidir** — ve zaten RFQ'nun
> yanına bir **kanal ön görüşmesi** koymamızın sebebidir (§27).

## 23.2 SORU B — *"RFQ göndermek için yeterli POZİTİF sinyal var mı?"*

# → **YES**

**Gerekçe — beş sinyal:**

| # | Sinyal | Kanıt |
|---|---|---|
| **1** | **Yapısal alan var.** 799 TL'de tavan 272,83 TL/şişe (≈4,95 EUR); Türkiye'nin İspanya'dan fiilen ithal ettiği ortalama CIF **2,03 USD/şişe** | `country-buying-ceilings.csv` + `EV-2026-08-09-405` |
| **2** | **Pilot ölçekte MOQ uyumu KANITLI.** 3.000 ve 3.600 şişe | `EV-2026-08-09-408`, `-410` |
| **3** | **Çalışan tedarik hatları var.** ES 1,92 m lt · IT 5,75 m lt · FR 2,85 m lt · MD 2,04 m lt · CL 0,95 m lt (2025) | `EV-2026-08-09-405` |
| **4** | **Fiyat noktası fiilen gözlendi.** Metro rafında 599,90 ve 649,90 TL'ye **iki ithal şarap** — ve ikisi de **%70 tarifeli menşeden** | `EV-2026-08-09-501`, `-502` |
| **5** | **Rakip yoğunluğu hedef bantta gerçek.** 799 TL ±%10'da 31 stokta yerli SKU — fiyat noktası **ticari olarak var** | `EV-2026-08-10-702` |

## 23.3 RFQ ne katar — somut liste

RFQ'nun çıktısı **yalnızca fiyat değildir.** Bir tek turda kapanabilecekler:

| Kapanan | Bugünkü durumu | Etkisi |
|---|---|---|
| **EXW / FOB fiyatı** (para birimi + Incoterm + yer) | ⛔ 26/26 `UNKNOWN` | **10 satırı `NO` → `PARTIAL`'a taşır** — tablodaki en büyük tek hareket |
| **Price-volume eğrisi** (5k/10k/25k/50k/FULL 20FT) | ⛔ yok | Hangi hacimde iş tuttuğunu **ilk kez** gösterir |
| **MOQ teyidi** (SKU bazlı **ve** konteyner bazlı) | ◐ 4 firmada var, 22'sinde yok | Pilot hacmini kesinleştirir |
| **Ödeme şartı / vade** | ⛔ n=1 | **KKDF tetiklenir mi** + `peak_cash` zaman ekseni |
| **Lead time** (üretim + hazırlık + yükleme) | ◐ n=2 | T0 takvimini kapatır |
| **Menşe belgesi taahhüdü** (`OD-1…OD-5`) | ⛔ 0 taahhüt | **32,10 TL/şişe** değerinde |
| **Palet / koli konfigürasyonu** (M3/M4) | ⛔ `UNKNOWN` | Konteyner adedi **~2 kat** belirsizliği kapatır; `FULL_20FT` teklifi **okunabilir** hale gelir |
| **Beyaz portföy + ABV + çeşit** | ⛔ çoğunda `UNKNOWN` | **Ürün uyumu hiç doğrulanmadı** |
| **Türkiye bölgesi kapalı mı** (Model A) | ◐ 1 firmada kapalı çıktı | Model A'nın **varlık koşulu** |
| **Türkçe arka etiket menşede uygulanabilir mi** | ⛔ `UNKNOWN` | Evet ise **bir `L5` kalemi tamamen kalkar** |
| **Model A ↔ Model B fiyat farkı** | ⛔ `UNKNOWN` | San Valero'ya tek RFQ ile ölçülür |

## 23.4 RFQ'nun maliyeti ve zamanı

| Kalem | Tahmin | Statü |
|---|---|---|
| **Para** | ≈ **0 TL** — e-posta, telefon, form. *(Numune talep edilirse ayrı bütçe + ayrı gümrük/ÖTV sorusu doğar — `T-893`)* | — |
| **Emek** | Paket **zaten hazır** (2 mail varyantı + response sheet + contact pack + 10 pazarlık kartı). Kalan iş: şablonu price-volume grid'e çevirmek, kimlik alanlarını doldurmak, onay turları | `T-961`, `T-892` |
| **Süre — gönderime kadar** | **3–7 gün** (şablon düzeltmesi + `P-6.3` onay turları) | `ASSUMPTION` |
| **Süre — cevap toplama** | **2–4 hafta** + takip | `ASSUMPTION` |
| ⚠ **Onay yükü** | **`P-6.3` her mesaj için ayrı onay istiyor.** 5 tedarikçi + 3 forwarder = **8 ayrı onay turu.** Bu, ilk dalgayı **5–7 hedefle sınırlı tutmayı** gerektirir | `P-6.4` ile gerilim — kayda geçti |
| **Taahhüt** | **HİÇBİRİ.** Sipariş yok, mal yok, şirket kurma zorunluluğu yok, geri dönülemez adım yok | — |

> ### RFQ, BU PROJEDEKİ **EN UCUZ GERİ DÖNÜLEBİLİR ADIMDIR.**
> Ama **en yüksek bilgi/maliyet oranına sahip adım DEĞİLDİR** — o unvan
> **mağaza turuna** aittir (`T-917`) ve **üç turdur yapılmamıştır.**

## 23.5 RFQ sonrası HEMEN `KILL` hangi durumda

```
╔══════════════════════════════════════════════════════════════════════╗
║  RFQ SONRASI ERKEN KILL TETIKLEYICILERI                              ║
║  (bunlar ESIK DEGIL, DESEN tanimlaridir — sayi uydurulmamistir)      ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  K-1  GELEN TUM TEKLIFLER "ABOVE_CEILING"                            ║
║       Yani her teklif x kur > Y kosesi (290,51 TRY / 5,27 EUR).       ║
║       Bu, modelin TEK YONLU olarak SAGLAM verebilecegi tek karardir.  ║
║       -> Fiyat/performans segmenti bu tedarikci havuzunda YOKTUR.     ║
║                                                                       ║
║  K-2  HICBIR TEDARIKCI MENSE BELGESI TAAHHUDU VERMEZ                 ║
║       Grup P'nin tamami fiilen Grup N olur -> her tavan %11,765 duser ║
║       ve tercihli menseyi secmenin ANLAMI KALMAZ.                     ║
║                                                                       ║
║  K-3  MOQ TABANI PILOT HACMININ COK USTUNE CIKAR                     ║
║       Dogrulanmis 3.000/3.600 MOQ'lar TEYIT EDILMEZSE ve gercek taban ║
║       konteyner bazina kayarsa, "kucuk pilot" mantigi COKER.          ║
║                                                                       ║
║  K-4  TUM TEDARIKCILER %100 PESIN ODEME ISTER                        ║
║       Tedarikci vadesi 0 + zincir vadesi 60-120 gun + KDV'nin 28-59   ║
║       gunluk mahsup gecikmesi = peak cash, hacimle DOGRUSAL buyur.    ║
║       -> Sermaye yapisi bu is modelini tasiyamayabilir.               ║
║                                                                       ║
║  K-5  CEVAP GELMEZ                                                    ║
║       10 hedeften anlamli cevap sayisi cok dusukse, bu bir fiyat      ║
║       bulgusu degil bir ERISILEBILIRLIK bulgusudur — ve o da bir      ║
║       KILL gerekcesidir: ulasilamayan tedarikciyle is yapilamaz.      ║
║                                                                       ║
║  K-6  URUN UYUMU YOK                                                  ║
║       Hedef profildeki (750 ml still kuru beyaz, value kademe) urunu  ║
║       hicbir tedarikci uretmiyorsa, fiyat tartismasi ANLAMSIZDIR.     ║
║                                                                       ║
╚══════════════════════════════════════════════════════════════════════╝
```

> ⚠ **Ve bir uyarı — `INCOMPLETE` ile `KILL` karıştırılmamalıdır.**
> FOB→CIF köprüsü (`T-866`) kapanmadan, **makul fiyatlı her teklif
> `INCOMPLETE` döner.** Bu, tedarikçinin pahalı olduğu anlamına **gelmez** —
> modelin cevap veremediği anlamına gelir. **`INCOMPLETE` bir `KILL` gerekçesi
> değildir.** Bu ayrım, RFQ turunun en kolay yapılacak hatasıdır.

---
---

# 24. PRE-RFQ KILL CRITERIA

## 24.1 Bugün `KILL` gerekiyor mu? — **HAYIR**

Bugün `KILL` gerektiren gerekçeler **arandı ve bulunamadı:**

| Aranan `KILL` gerekçesi | Bulundu mu | Neden |
|---|---|---|
| Yasal olarak kurulamaz mı? | ❌ | Yol haritalanmış, `G0 = PASS` *(⚠ beş turdur test edilmedi)* |
| Vergi yükü hesaplanamıyor mu? | ❌ | T1 düzeyinde kanıtlı ve testle korunuyor |
| Model **negatif** mi veriyor? | ❌ | 2.700 kombinasyonun **hiçbirinde** `MAX_CIF` negatif değil |
| GTİP yanlış mı (köpüklü/aromatize)? | ❌ | 2204.21 doğrulandı |
| Alkolde KDV indirim yasağı var mı? | ❌ | Arandı, **2204.21'e değmiyor** — etki 0,00 TL/şişe |
| Tedarik hattı yok mu? | ❌ | 5 menşede fiilen çalışan hat var |
| Pilot hacmine uyumlu MOQ yok mu? | ❌ | 3.000 ve 3.600 doğrulandı |
| Bir tedarikçi teklifi tavanı aştı mı? | ❌ | **Hiç teklif alınmadı** — bu bir bulgu değil, bir boşluk |

## 24.2 RFQ SONRASI ERKEN `KILL` KRİTERLERİ

> # ⛔ EŞİK UYDURULMAMIŞTIR
> Aşağıdaki kriterler **desen tanımlarıdır**, sayısal eşik değildir. Sayısal
> eşik (kaç teklif, hangi yüzde, hangi marj) **yatırımcı kararıdır** ve
> `OQ-901` / `T-851` altında **açıktır.** Başkan bir eşiğe sayı yazmamıştır.

### Kategori A — **Fiyat kaynaklı** *(en güçlü, çünkü tek yönlü sağlam)*

| # | Kriter | Neden sağlam |
|---|---|---|
| **KC-A1** | **Gelen tüm tekliflerin `teklif × kur > Y köşesi` olması** | Modelin **tek yönlü** olarak kesin karar verebildiği tek durum. `gerçek_CIF ≥ teklif × kur` olduğundan bu bir **ret** hükmüdür ve sağlamdır |
| **KC-A2** | Price-volume eğrisinin **düz olması** (hacim indirimi yok) | Ölçek stratejisi çöker; 25.000'e çıkmanın anlamı kalmaz |

### Kategori B — **Yapısal / erişim kaynaklı**

| # | Kriter |
|---|---|
| **KC-B1** | Hiçbir tedarikçi **menşe belgesi taahhüdü** vermezse → tüm tavanlar %11,765 düşer |
| **KC-B2** | **MOQ tabanı** doğrulanmış 3.000/3.600'ün belirgin üstüne çıkarsa → küçük pilot mantığı çöker |
| **KC-B3** | **Ürün uyumu yoksa** — hedef profili üreten tedarikçi bulunamazsa |
| **KC-B4** | **Cevapsızlık** — anlamlı cevap oranı çok düşükse (erişilebilirlik bulgusudur) |

### Kategori C — **Nakit / zaman kaynaklı**

| # | Kriter |
|---|---|
| **KC-C1** | Tüm tedarikçiler **%100 peşin** isterse **ve** kanal vadesi 90–120 gün çıkarsa → peak cash hacimle doğrusal büyür |
| **KC-C2** | **Antrepo zorunlu bekleme süresi** çok uzun çıkarsa (`T-301`) → hem depo maliyeti hem ÖTV takvim riski hem nakit döngüsü bozulur |

### Kategori D — **Pazar kaynaklı** *(RFQ'dan bağımsız, paralel yürür)*

| # | Kriter |
|---|---|
| **KC-D1** | Mağaza turunda **`L8_CHAIN_RETAIL`'de bu segmentin fiilen 799'un belirgin altında** olduğu görülürse → tüm tavanlar orantısız düşer (maktu ÖTV sabit kaldığı için) |
| **KC-D2** | **`T-504` "normal fiyat"** diye kapanırsa → 599,90 kalıcı bir ithal giriş fiyatıdır; 799 hedefi **PREMIUM_EDGE**'e kayar ve f/p konumlandırması bozulur |
| **KC-D3** | Kanal ön görüşmesinde **hiçbir perakendeci listeleme niyeti göstermezse** |
| **KC-D4** | **`C-561`** "bantta ürün var ama dönmüyor" yönünde çözülürse → whitespace argümanı **tamamen çöker** |

### Kategori E — **Mevzuat kaynaklı** *(düşük olasılık, yüksek etki)*

| # | Kriter |
|---|---|
| **KC-E1** | `G0` geri alma tetikleyicilerinden biri gerçekleşirse (`R1`/`R2`/`R3`) |
| **KC-E2** | 2204.21 için **gözetim tebliği** çıkarsa ve eşik tavanın üstünde olursa → **çözüm kümesi boşalır** ve fiyat pazarlığıyla kurtarılamaz |

## 24.3 ⛔ `KILL` OLMAYAN durumlar — kayda geçiyor

| Durum | Neden `KILL` DEĞİL |
|---|---|
| **Tekliflerin `INCOMPLETE` dönmesi** | Bu bir fiyat bulgusu değil, bir **köprü eksikliğidir** (`T-866`). Modelin cevap verememesidir |
| **Tek bir tedarikçinin pahalı çıkması** | n=1 bir dağılım değildir |
| **Bir ülkenin elenmesi** | 9 menşe var; biri düşerse diğerleri durur |
| **FCL navlununun hâlâ bilinmemesi** | Ters model üzerindeki etkisi **sıfırdır**; ileri model için blokerdir ama çözülebilir |
| **Model çıktılarının `DRAFT` olması** | Tasarımın gereğidir, bir başarısızlık değil |

---
---

# 25. PRELIMINARY PILOT DESIGN

> # ⛔ BU **FİNAL DEĞİLDİR**
> Aşağıdaki tasarım bir **konsepttir.** `IMPORT PILOT` kararı **VERİLMEMİŞTİR**
> ve bu belgede verilemez. Gerçek pilot tasarımı, RFQ cevapları geldikten sonra
> ayrı bir turda ve **yatırımcı eşikleri belirlendikten sonra** yapılır.

```yaml
────────────────────────────────────────────────────────────────
  PRELIMINARY PILOT CONCEPT          status: DRAFT / NOT APPROVED
────────────────────────────────────────────────────────────────

  SKU SAYISI      : 2
                    P1 VALUE HERO  — nötr/meyveli beyaz blend
                                     (Colombard-Chardonnay ·
                                      Airén-Chardonnay · eşdeğer)
                    P2 STEP-UP     — tek çeşit tanınır beyaz
                                     (Chardonnay veya Sauvignon Blanc)

  RENK            : YALNIZ BEYAZ
                    Gerekçe: benchmark beyaz; charter beyaz öncelikli;
                    2 SKU zaten iki hipotez test ediyor — üçüncü bir
                    değişken (renk) eklemek pilotu okunamaz kılar.

  IS MODELI       : PRIVATE LABEL (birincil)
                    + tek bir EXISTING BRAND karşılaştırma teklifi
                      (Bodegas San Valero — aynı üründe iki fiyat)
                    Gerekçe: PL ölçülebilir (MOQ kanıtlı), EB ölçülemez.
                    Ama charter iki modeli EŞİT tutar → karar değil,
                    ÖLÇÜM yapılır.

  HACIM           : 5.000 – 6.000 sise TOPLAM
                    (2 SKU x 3.000 = 6.000 — Interbrosa MOQ'suyla uyumlu)
                    ⚠ Her SKU AYRI MOQ'ya tabi olabilir — RFQ'da sorulur.
                    ⚠ 6.000 sise, LCL/FCL kirilma noktasinin (~5.900)
                      hemen ustundedir → 20DV FCL ekonomik olarak makul.

  ULKE            : ISPANYA (birincil)
                    Gerekçe: tek 0-aktarmali direkt rota (4 gün) ·
                    en ucuz LCL (0,274–0,297 USD/şişe) · %50 tarife ·
                    origin charge'lari bilinen TEK menşe ·
                    doğrulanmış en düşük MOQ (3.000).
                    ALTERNATIF: PORTEKIZ (Model A tarafi icin)

  TASIMA          : 20DV PALETLI (yari dolu)  veya  LCL
                    Fiyat farki GURULTU SEVIYESINDE (±0,05 USD/sise) →
                    karar fiyatla degil KIRILGANLIKLA verilir.
                    ⚠ FCL kotasyonu hala UNKNOWN → karar ertelenir.

  KANAL           : CHAIN RETAIL (birincil)  +  TEKEL (ikincil)
                    HoReCa PILOTTA YOK — 5,0x carpanda model olu.

  HEDEF RAF FIYATI: 799 TL (CURRENT DESIGN TARGET)
                    Test bandi: 699 – 899

  SATIS NOKTASI   : ~21 aktif nokta @ 20 sise/ay  (ASSUMPTION)

  SURE            : T0'dan ilk konteynere kadar mevzuat kaynakli
                    kritik yol ~4-6 ay (ESTIMATE/ASSUMPTION agirlikli;
                    dagitim yetki belgesi suresi MEVZUATTA TANIMSIZ)
                    + tedarikci uretimi (4-6 hafta) + navlun (4 gun ES)

  BASARI KRITERI  : ⛔ YAZILMADI — yatirimci esikleri TBD (OQ-901)
  DURDURMA KRITERI: ⛔ YAZILMADI — ayni sebep

────────────────────────────────────────────────────────────────
```

## 25.1 Bu tasarımın bilinçli boşlukları

| Boşluk | Neden boş bırakıldı |
|---|---|
| **Başarı kriteri** | Yatırımcının 6 finansal eşiğinin **6'sı da `TBD`.** Bir başarı kriteri yazmak, eşik uydurmak olurdu |
| **Durdurma kriteri** | Aynı sebep |
| **Bütçe** | `peak_cash_requirement` **hesaplanamıyor** (§18) |
| **Tedarikçi adı** | RFQ cevabı gelmeden tedarikçi seçilmez |
| **Kesin hacim** | MOQ'ların SKU bazlı mı konteyner bazlı mı olduğu tedarikçiye göre değişir |
| **Taşıma modu kesinliği** | FCL kotasyonu `UNKNOWN` |

---
---

# 26. PRE-RFQ SCORECARD

| # | Boyut | Durum | Kısa gerekçe |
|---|---|---|---|
| 1 | **Market gap** | 🟡 **YELLOW** | `PARTIALLY SUPPORTED`. Gözlenen kanalda 875 TL altında stokta ithal SKU yok — ama aynı kanal 600 TL altında **yerli de** taşımıyor. Metro'da 599,90/649,90 TL'ye iki ithal SKU **fiilen görüldü.** İki kanal **çelişiyor** |
| 2 | **Target price (799)** | 🟡 **YELLOW** | Pazar sınıfı `ATTRACTIVE`/MEDIUM; ekonomik olarak en dengeli basamak. Ama **hangi `L8` alt katmanı olduğu `UNKNOWN`** ve hedef katmanda **sıfır gözlem** var |
| 3 | **Tax economics** | 🟢 **GREEN** | Matrah sırası ve oranlar **T1** ile doğrulanmış, satır satır hesaplanabiliyor, 10/10 birim testle korunuyor. ÖTV 53,45 TL/şişe maktu · KDV %20 · **KDV indirilebilir (CONFIRMED)** |
| 4 | **Customs / origin** | 🟡 **YELLOW** | %50 **koşullu**; belge veya doğrudan nakliyat sağlanmazsa otomatik %70. Bedel **TAM %11,765 = −32,10 TL/şişe.** Şili'de **rota bir vergi kararıdır** |
| 5 | **Sourcing** | 🟡 **YELLOW** | 26 tedarikçi tarandı, 10 hedef + tam RFQ paketi hazır, 7'si `READY_TO_SEND`. Ama doğrulanmış MOQ yalnız **4 firmada** |
| 6 | **Supplier pricing** | 🔴 **RED** | **26/26 tedarikçiden teklif YOK.** Tek yayınlanmış fiyatın **para birimi ve katmanı `UNKNOWN`.** `FIRM_OFFER` sayısı: **0** |
| 7 | **Logistics** | 🟡 **YELLOW** | 9 rotanın LCL'i gerçek tarihli kotasyonla biliniyor (İtalya hariç). **FCL hiçbir rotada doğrulanmadı** (4–5 kat band). LCL kartları **2026-08-17'de STALE** |
| 8 | **Channel** | 🔴 **RED** | `L8_CHAIN_RETAIL` **null**. `m_retail`, `d`, `f` — üçü de `ASSUMPTION`/`UNKNOWN`. Tek kanıtlı çapa Migros %24,31 ve o **şarap değil, tüm kategori** |
| 9 | **Legal / regulatory** | 🟡 **YELLOW** | `G0 = PASS` ama **beş turdur test edilmedi**; iki açık çelişki üzerinde duruyor. Antrepo bekleme süresi **`UNKNOWN`** (CRITICAL) |
| 10 | **Working capital** | 🔴 **RED** | `peak_cash_requirement` **TUTARI hesaplanamıyor.** CIF yok · FCL yok · bekleme süresi yok · yasal vade tavanı nitelemesi yok — **dördü de CRITICAL** |
| 11 | **Sales velocity / demand** | 🔴 **RED** | Türkiye'de şarap için **tek bir talep, hacim, rotasyon veya satış verisi YOK.** Store velocity tamamen `ASSUMPTION` |
| 12 | **Competition** | 🟡 **YELLOW** | 600–1.000 TL'de 65 yerli / 2 ithal stokta SKU; rakip seti **isimli ve somut.** Ama **tek kanaldan** okundu ve o kanal premium'a kayık (yerli medyan 1.410 TL) |
| 13 | **Scalability** | 🟡 **YELLOW** | Ölçek ekonomisinin **%87'si 5.000 → 25.000'de.** 25.000 üstünde etki ihmal edilebilir ve sebebi navlun değil **bir ruhsat kademesidir** |

## 26.1 Skorbord özeti

```
╔═══════════════════════════════════════════════════════════════╗
║   🟢 GREEN    :  1   /  13     ( Tax economics )               ║
║   🟡 YELLOW   :  8   /  13                                     ║
║   🔴 RED      :  4   /  13                                     ║
║   ⬜ UNKNOWN  :  0   /  13                                     ║
╚═══════════════════════════════════════════════════════════════╝
```

## 26.2 Skorbordun okunması — üç gözlem

> **1. Dört `RED`'in dördü de AYNI KÖKTEN geliyor: DIŞ TEMAS EKSİKLİĞİ.**
> Supplier pricing (RFQ) · Channel (perakendeci görüşmesi) · Working capital
> (fiyat + navlun + süre) · Sales velocity (perakendeci/mağaza gözlemi).
> **Hiçbiri bir "araştırma başarısızlığı" değildir** — dördü de **kimseyle
> konuşmamış olmanın** doğrudan sonucudur.
>
> **2. Tek `GREEN`, en çok öldürme potansiyeli olan boyuttadır.**
> Bir ithalat projesinde en sık ölüm sebebi **vergi sürprizidir** ve orası
> **sağlamdır.** Bu, skorbordun en değerli satırıdır.
>
> **3. Hiçbir boyut `UNKNOWN` değildir.** Yani her boyutta **en azından bir
> okuma** yapabiliyoruz. Bu, kanıt tabanının (321 kart) gerçek bir iş yaptığını
> gösterir — eksik olan **veri değil, TEMAS**'tır.

---
---

# 27. FINAL VERDICT

```
╔══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║        KARAR    :   PROCEED TO RFQ                                    ║
║                                                                       ║
║        TIP      :   PRELIMINARY GATE DECISION                         ║
║                     (NIHAI YATIRIM KARARI DEGILDIR)                   ║
║                                                                       ║
║        CONFIDENCE:  MEDIUM                                            ║
║                                                                       ║
║        TARIH    :   2026-08-10                                        ║
║        KARAR VEREN: yatirim-komitesi-baskani                          ║
║                                                                       ║
╚══════════════════════════════════════════════════════════════════════╝
```

## 27.1 Neden `PROCEED TO RFQ` — üç cümle

1. **`KILL` değil**, çünkü 20 zorunlu koşulun **sıfırı `FAIL`**'dir ve projeyi
   öldürmesi beklenen hipotez (*"CIF tavanı negatif çıkar"*) 2.700 kombinasyonda
   **çürütülmüştür.**
2. **`HOLD` değil**, çünkü beklemek hiçbir şeyi değiştirmez: eksik olan 12
   `UNKNOWN`'ın **7'si masabaşıyla kapanmaz** ve zaman geçtikçe kanıt tabanı
   **bayatlar** (LCL kotasyonları 6 gün içinde, pazar gözlemleri 30 gün içinde).
3. **`PROCEED TO RFQ`**, çünkü modelin en büyük belirsizliği (**gerçek satın
   alma fiyatı**) **yalnızca sormakla** öğrenilebilir, ve sormanın maliyeti
   ≈ sıfırdır, geri dönülemez taahhüdü **yoktur.**

## 27.2 Neden `CONFIDENCE: MEDIUM` — `HIGH` değil

| Neden |
|---|
| Modelin **tüm bilinen sapmaları AYNI YÖNDE**: projenin lehine (26 kalem `0` alındı, λ=1 çapası, `d` tekelde `0`, üç ayrı katman sınırı hatası) |
| **`G0` beş turdur test edilmedi** — *"olumsuz kanıt aranmadığı için olumsuz kanıt yok"* kısırdöngüsü |
| **12 açık CRITICAL ticket** var; hiçbir model çıktısı `APPROVED` değil |
| **Talep tarafında sıfır veri** — bu, bir tüketici ürünü projesinde en büyük tek boşluktur |
| **`799 PRIMARY` seçimi çapalama riski taşıyor** — modelin önerdiği sayı yatırımcı kararı olarak geri döndü; bu bir doğrulama değildir |

**Neden `LOW` da değil:** vergi bacağı T1 düzeyinde sağlam, 9 rotanın LCL'i
gerçek kotasyonla biliniyor, MOQ uyumu kanıtlı, tedarik hatları fiilen çalışıyor
ve model yapısal olarak pozitif alan bırakıyor. **321 kanıt kartının 230'u
`FACT`.** Bu, bir "hiç bilmiyoruz" durumu değildir.

## 27.3 Gate durum tablosu — PRE-RFQ

| Gate | Soru | Sahibi | Durum | Açan koşul |
|---|---|---|---|---|
| **G0** Yasal yol | Türkiye'de yasal kurulabilir mi? | `mevzuat-ruhsat-uzmani` → **başkan** | **`PASS`** ⚠ *(beş turdur test edilmedi)* | — *(izleme: R1/R2/R3)* |
| **G1** Vergi yapısı | Vergi yükü kanıtlı hesaplanabilir mi? | `gumruk-vergi-uzmani` | **`BLOCKED`** | `T-104` 2. ayağı (Yİ-ÜFE ekseni) |
| **G2** Tedarik | Gerçek, ulaşılabilir kaynak var mı? | `global-sourcing-kasifi` | **`BLOCKED`** | **≥5 gerçek RFQ cevabı** — *bu kararın hedefi* |
| **G2-L** Lojistik | `L1 → L2 → L3` kurulabiliyor mu? | `navlun-lojistik-uzmani` | **`BLOCKED`** ⏰ | 3 forwarder yazılı FCL kotasyonu (`T-304`) |
| **G3** Pazar | Benchmark doğrulandı mı? | `turkiye-pazar-kasifi` | **`BLOCKED`** | **`OQ-001` promosyon ayağı** (`T-504`) + `l8_chain_retail` (`T-603`) |
| **G4** Ekonomi | Model pozitif contribution veriyor mu? | `finans-fizibilite` | **`NOT_EVALUATED`** | G1+G2+G2-L+G3 + yatırımcı eşikleri |
| **G5** Risk | Kırmızı takım CRITICAL'ları kapandı mı? | `seytanin-avukati` | **`NOT_EVALUATED`** | TUR 4 |

> **HİÇBİR GATE BU KARARLA AÇILMAMIŞTIR.** `PROCEED TO RFQ`, `G2`'yi **açmaz** —
> `G2`'yi açan şey **cevaplardır**, izin değil.

## 27.4 Bu kararı taşıyan 3 kritik varsayım

1. **`ASSUMPTION`** — *Gerçek tedarikçi FOB fiyatları, yapısal tavanın
   (799/P: 4,95 EUR/şişe CIF) **anlamlı ölçüde altında** olacaktır.*
   Dayanağı: Türkiye'nin İspanya'dan fiilen ithal ettiği ortalama CIF birim
   değeri **2,03 USD/şişe**'dir — tavanın yaklaşık üçte biri.
   **Çökerse: proje ölür.**
2. **`ASSUMPTION`** — *Zincir perakendede bu segmentin tüketici raf fiyatı
   799 TL bandındadır.*
   Dayanağı: **YOK.** `L8_CHAIN_RETAIL`'de sıfır gözlem var. Bu, modelin **tepe
   çapasıdır** ve **hiç ölçülmemiştir.**
   **Çökerse: tüm tavanlar orantısız kayar** (maktu ÖTV sabit kaldığı için).
3. **`ASSUMPTION`** — *Kanal marjı %25 (BASE) ve geri akan bedeller %8
   civarındadır.*
   Dayanağı: Migros'un **tüm kategori** %24,31'i — **şarap değildir.**
   **Çökerse: `m_retail` %35 olursa tavan 272,83 → ~176 TL'ye iner (−%35).**

## 27.5 Bu kararı tersine çevirecek bulgu

> ### "ŞUNU GÖRÜRSEM FİKRİMİ DEĞİŞTİRİRİM:"
>
> **≥5 gerçek, tarihli, para birimi ve Incoterm'i belirtilmiş tedarikçi
> teklifinin TAMAMININ `Y` köşesinin (290,51 TRY = 5,27 EUR = 6,09 USD) ÜSTÜNDE
> çıkması.**
>
> Bu, modelin **tek yönlü olarak sağlam** karar verebildiği tek durumdur:
> `gerçek_CIF ≥ teklif × kur` olduğundan, teklif Y'yi aşıyorsa **ret hükmü
> kesindir.** O gün karar **`KILL`**'e döner ve daha fazla veri aramaya gerek
> kalmaz.
>
> **İkinci en güçlü tersine çevirici:** Mağaza turunda `L8_CHAIN_RETAIL`'de bu
> segmentin fiilen **500–650 TL** bandında olduğunun görülmesi. O zaman
> tavanlar maktu ÖTV nedeniyle **orantısız** düşer ve 799 hedefi anlamını
> yitirir.

## 27.6 Açık kalan CRITICAL UNKNOWN'lar

| # | UNKNOWN | Neden kapanmadı | Kararı nasıl etkiliyor |
|---|---|---|---|
| 1 | **Gerçek EXW/FOB fiyatı** (`T-466`) | Dış temas gerekiyordu; izin yeni verildi, mesaj gönderilmedi | **Bu kararın hedefi** |
| 2 | **Doğrulanmış FCL navlunu** (`T-304`) | Aynı — paket hazır, gönderilmedi | Peak cash + taşıma kararı |
| 3 | **Antrepo zorunlu bekleme süresi** (`T-301`) | `mevzuat-ruhsat-uzmani` beş turdur bu kapsamda çalışmadı | Peak cash'in **zaman ekseni** |
| 4 | **Yasal vade tavanı** (`T-601`) | Hukuki niteleme; başkan kendi yorumuyla kapatamaz | Alacak finansmanı |
| 5 | **Yatırımcı eşikleri** (`T-851`, `OQ-901`) | Yalnızca yatırımcı kapatabilir | `TARGET`/`WALK-AWAY` üretilemiyor |
| 6 | **`l8_chain_retail`** (`T-603`, `T-701`) | Fiziksel mağaza turu üç turdur yapılmadı | Modelin **tepe çapası** |
| 7 | **Benchmark promosyon durumu** (`T-504`) | Aynı mağaza turu | **`OQ-001` → `G3` bloke** |
| 8 | **10 tedarikçilik RFQ paketi gönderilmedi** (`T-885`) | `P-6.3` onayı bekliyor | **Bu kararın konusu** |
| 9 | **Kanal marjı / `d` / `f`** (`T-604`, `T-856`) | Türkiye'de sistematik ticari sır | Tornado'nun 3. ekseni |
| 10 | **FOB→CIF ve EXW→FOB köprüleri** (`T-866`, `T-867`) | Yeni açıldı (TUR 3.25) | **RFQ cevaplarının okunabilirliği** |
| 11 | **`V10K` model satırı yok** (`T-865`/`T-963`) | Ters model bu hacimde koşulmadı | Kurucunun sorduğu bir fiyat noktası **karşılaştırılamaz** |
| 12 | **Gümrük beyan kuru** (`T-911`) | Mevzuat sorusu | Vergi matrahını etkiler |

## 27.7 Reddedilen bulgular

**Bu turda hiçbir ajan bulgusu reddedilmemiştir. Sayı: 0.**

Bu bir eksiklik değildir: bu tur bir **konsolidasyon ve karar turudur**, yeni
ajan raporu üretilmemiştir. Önceki turlarda reddedilen bulgu sayısı da **0**'dır
ve bunun gerekçesi `tur-25-konsolidasyon.md` §7.1'de kayıtlıdır.

**Başkanın kendi düzelttiği hükümler (kayıt):** `master-commercial-input-table.md`
§5.3'ün *"`fx` olmadan ters model `CIF_TRY`'ye kadar çalışır"* hükmü fazla
kesindi ve nitelendi (`C-852`); `T-912`'nin hedef ajanı yanlıştı ve `T-852` ile
düzeltildi.

## 27.8 Sonraki gözden geçirme tetikleyicisi

| Tetikleyici | Ne olur |
|---|---|
| **≥5 gerçek RFQ cevabı toplandığında** | Karar yeniden ele alınır → `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` |
| **Fiziksel mağaza turu tamamlandığında** | `G3` yeniden değerlendirilir; 799 hedefi teyit veya revize edilir |
| **2026-08-17** *(LCL kotasyonları `STALE`)* | Lojistik bacağı yeniden doğrulanır veya `ESTIMATE/LOW`'a düşürülür |
| **2026-09-08/09** *(pazar gözlemleri `STALE`)* | Tüm rakip/bant sınıflandırması yeniden doğrulanmadan kullanılamaz |
| **Yatırımcı eşikleri belirlendiğinde** | `TARGET BUY` / `ACCEPTABLE BUY` / `WALK-AWAY` üretilebilir hale gelir |
| **Herhangi bir `G0` geri alma tetikleyicisi** | `G0` yeniden değerlendirilir |

---

## 27.9 ⭐ "BEN YATIRIMCI OLSAYDIM BUGÜN NE YAPARDIM?"

```
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   1.  MAGAZAYA GIDERDIM — RFQ'DAN ÖNCE.                                   ║
║       Migros + Macrocenter + CarrefourSA + Metro + 2 tekel bayii.         ║
║       Iki sehir, en az 20 SKU, her etiketin fotografi.                    ║
║       BU TEK EYLEM SU BESINI AYNI ANDA KAPATIR:                           ║
║       T-504 (benchmark promosyonlu mu) · T-603 (zincir raf fiyati) ·      ║
║       C-551 (Metro KDV sunumu) · C-501 (stok gercekligi) · OQ-001.        ║
║       Maliyeti: bir gun + benzin.  Projedeki EN YUKSEK bilgi/maliyet      ║
║       oranina sahip eylem — ve UC TURDUR YAPILMADI.                        ║
║                                                                           ║
║   2.  "799 TL HANGI RAFIN FIYATI?" SORUSUNU BUGUN CEVAPLARDIM.            ║
║       Tek kelime yeterli: CHAIN_RETAIL / METRO_CASH_CARRY /               ║
║       ONLINE_UZMAN / KANAL KARMASI.  Model ciktisina bakmaya gerek yok.   ║
║       Bu, ay(lar)dir bekleyen TEK "MUST DECIDE NOW" kalemidir.            ║
║                                                                           ║
║   3.  HACIM KADEMELERININ BAZINI TEK CUMLEYLE NETLESTIRIRDIM.             ║
║       "5.000/10.000/25.000/50.000" — YILLIK mi, SIPARIS BASINA mi?        ║
║       50.000 sise/yil ile 50.000 sise/siparis AYNI SEY DEGIL              ║
║       (ikincisi ~7 x 20DV = bir olcek operasyonu).                        ║
║       En ucuz, en yuksek getirili tek dogrulama budur.                    ║
║                                                                           ║
║   4.  RFQ'YU 5 HEDEFE GONDERIRDIM — 10'A DEGIL.                           ║
║       Interbrosa · San Valero · Casa Santos Lima · The Wine Factory ·     ║
║       Cantina Danese.  Gerekce: her mesaj icin AYRI onay kurali (P-6.3)   ║
║       10 hedefte yorulur ve sessizce "toplu onay"a doner — yani           ║
║       kendi koydugum kurali ihlal ederim. 5 hedef yonetilebilir.          ║
║                                                                           ║
║   5.  AYNI HAFTA 3 FORWARDER'A DA YAZARDIM.                               ║
║       Paket HAZIR ve GONDERILMEMIS durumda. FCL + LCL AYNI ANDA           ║
║       fiyatlansin, included/excluded charge'lar TEK TEK listelensin.      ║
║       Sebep: LCL kanit setimiz 2026-08-17'de BAYATLIYOR — 6 gun var.      ║
║                                                                           ║
║   6.  BIR PERAKENDECIYLE KAHVE ICERDIM.                                   ║
║       RFQ satin alma tarafini acar; SATIS tarafini ACMAZ.                 ║
║       Tek soru: "Bu profilde bir ithal beyaz sarabi 799 TL'ye listeler    ║
║       misiniz, ayda kac sise beklersiniz, sartlariniz nedir?"             ║
║       Bu tek gorusme, tornadonun 3. buyuk eksenini (kanal marji) ve       ║
║       en buyuk RED'i (talep verisi) ayni anda hedefler.                   ║
║                                                                           ║
║   7.  FAAL BIR ITHALATCIYLA KONUSURDUM.                                   ║
║       Isimler ARTIK ANONIM DEGIL: Kavaklidere · Karagozoglu · Adco ·      ║
║       Baron.  Tek bir gerceklesmis ithalat dosyasi (beyanname + fatura)   ║
║       su dortünü AYNI ANDA kapatir: gercek CIF · antrepo/bandrolleme      ║
║       kalemleri · THD-terminal cift sayimi · L6 fatura fiyati.            ║
║                                                                           ║
║   8.  MARJ ESIGIMI YAZARDIM — TEK SAYI.                                   ║
║       "Sise basina en az X TL katki payi isterim" veya "brut marj en az   ║
║       %Y olmali."  Bu tek sayi olmadan TARGET BUY / WALK-AWAY             ║
║       URETILEMEZ ve gelen tekliflere "evet" ya da "hayir" DENEMEZ.        ║
║       OQ-901 ay(lar)dir bunu bekliyor.                                    ║
║                                                                           ║
║   9.  HICBIR SIPARIS VERMEZDIM. HICBIR SIRKET KURMAZDIM.                  ║
║       Numune bile ISTEMEZDIM ilk turda — numune talebi ayri butce,        ║
║       ayri gumruk ve ayri OTV sorusu dogurur (T-893).                     ║
║       Bu asamada tek yatirim EMEK'tir; para degil.                        ║
║                                                                           ║
║  10.  ILK 5 CEVAP GELDIGINDE MASAYA GERI DONERDIM — 2-4 HAFTA ICINDE.     ║
║       Kural: her teklif DORT FX EKSENINDE ayri ayri olculur; hicbir       ║
║       teklif tek kurla degerlendirilmez. Hepsi Y kosesinin ustundeyse     ║
║       O GUN KILL. Altindaysa "INCOMPLETE" — bu bir onay DEGILDIR.         ║
║                                                                           ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### Bu 10 maddenin özeti — tek cümle

> **Bu hafta harcanacak şey para değil, üç telefon görüşmesi ve bir mağaza
> turudur.** Ve bunların **dördü de** (mağaza turu, perakendeci görüşmesi,
> ithalatçı görüşmesi, marj eşiği) **RFQ'nun kapatamayacağı boşlukları** hedef
> alır. **RFQ tek başına yeterli değildir — ama RFQ olmadan da ilerlenemez.**

---
---

# Bu kararı ne çürütür?

## En güçlü tek çürütücü bulgu

> ## ZİNCİR MARKET RAFINDA BU SEGMENTİN FİİLEN 799 TL'NİN ÇOK ALTINDA OLMASI.

**Neden bu, RFQ'dan bile güçlü bir çürütücüdür:**

Ters modelin **tepe çapası** hedef raf fiyatıdır. Eğer `L8_CHAIN_RETAIL`'de bu
segment 799 TL değil de örneğin **450–650 TL** ise, azami satın alma fiyatı
**maktu ÖTV sabit kaldığı için ORANTISIZ biçimde** düşer — çünkü 53,45 TL/şişe
fiyattan bağımsızdır ve düşük fiyatta **çok daha büyük bir yüzde** kaplar.

Somut olarak: 799 → 599 kayması tavanı **272,83 → 189,50 TL**'ye indirir
(**−%30,5**). Aynı anda 799 → 599 hedefinde sabit TL maliyet yığınının payı
**%30,9'dan %44,5'e** çıkar. **İki etki birlikte** yapısal tabana (144,21 TL)
olan mesafeyi **5,54 katından 4,15 katına** düşürür.

Ve elimizde bunu dışlayan **tek bir gözlem yoktur**: `L8_CHAIN_RETAIL`'de
**sıfır ölçüm** var, ve bir T5 sinyali (`EV-2026-08-10-703`) zaten
**zincir/tekelde 450–650 TL** iddia ediyor — o sinyal `C-503` ile modele
alınmadı ama **çürütülmedi de.**

**Nasıl ararız:** Bir mağaza turu. **Bir gün. Sıfıra yakın maliyet.**
`T-917` — ve **üç turdur yapılmadı.**

## İkinci en güçlü çürütücü — farklı hükmü hedefler

> **`P-6.3`'ün (her mesaj için ayrı ayrı açık onay) uygulanamaz olduğunun
> ortaya çıkması.**

Bu, kararın **kendisini** değil, **uygulanabilirliğini** çürütür. 26 tedarikçi +
3 forwarder × ayrı önizleme = **29 ayrı onay turu.** Pratikte olacak şey şudur:
onay turları yorulur ve `P-6.3` sessizce *"toplu önizleme + tek onay"*a dönüşür —
yani kurucunun **açıkça yasakladığı şeye.**

Bu yüzden §27.9 madde 4, ilk dalgayı **5 hedefle** sınırlamayı önermektedir.
**Nasıl ararız:** İlk dalgada alıcı sayısına bakılır. 7'den fazlaysa gerilim
**gerçektir** ve kurala bir **dalga/parti tanımı** eklenmelidir.

## Bu kararın kör noktası

> **Bu rapor, "devam et" demenin BEDAVA olduğunu varsayıyor.**

RFQ'nun para maliyeti ≈ sıfırdır, bu doğrudur. Ama üç gizli maliyeti vardır ve
hiçbiri ölçülmemiştir:

1. **Dikkat maliyeti.** Kurucunun zamanı ve odağı sınırlıdır; 8 onay turu +
   takip + değerlendirme, başka fırsatlardan çalınan zamandır.
2. **Taahhüt tırmanması (escalation of commitment).** Beş firmaya yazdıktan,
   cevap aldıktan ve numune konuştuktan sonra `KILL` demek **psikolojik olarak
   çok daha zordur.** Bu rapor, o eşiği bugünden yazarak (§24.2 `KC-A1`)
   savunmaya çalışıyor — ama savunmanın işe yarayıp yaramayacağı bilinmiyor.
3. **İtibar maliyeti.** Beş üreticiye yazıp sonra kaybolmak, ileride aynı
   firmalara dönmeyi zorlaştırır.

**Ve son olarak, en rahatsız edici gerçek:** Bu proje **beş turdur veri
topluyor ve hâlâ tek bir kişiyle konuşmamış.** 321 kanıt kartının **hiçbiri**
bir insanla yapılmış görüşmeden gelmiyor. Bu raporun en güçlü önerisi de zaten
budur: **artık okumayı bırakıp konuşmaya başlamak.**

---

*Bu belge bir PRELIMINARY GATE kararıdır. `IMPORT PILOT`, `SCALE` veya nihai
yatırım kararı içermez. Karar `90-karar/karar-gunlugu.md` KAYIT #1'e
işlenmiştir.*
