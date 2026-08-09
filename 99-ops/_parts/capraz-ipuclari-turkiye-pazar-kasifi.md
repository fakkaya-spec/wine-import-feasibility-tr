# ÇAPRAZ İPUÇLARI — turkiye-pazar-kasifi (TUR 1)

> Bunlar **sonuç değildir**, ipucudur. Kendi alanım dışında gördüğüm ama ilgili
> ajanın işine yarayacak gözlemler. Ana `99-ops/capraz-ipuclari.md`'ye birleştirilecek.

---

## → `kanal-marj-uzmani`

### İP-501 — Metro'da mağaza fiyatı ile teslimat fiyatı FARKLI
Metro Türkiye broşür künyesi (`EV-2026-08-09-507`):
> *"Broşürdeki fiyatlar **sevkiyat hizmeti alan müşterilerimiz için geçerli değildir**."*

Yani Metro'da en az iki fiyat rejimi vardır: **cash & carry mağaza** ve
**Metro Gastro Servis / teslimat (HoReCa dağıtım)**. Aradaki fark **UNKNOWN**.
Bu, "Metro'ya tek fiyat verilir" varsayımını kırar. → `T-506`

### İP-502 — Alkol, Metro'nun tüm çek/sadakat kampanyalarının DIŞINDA
`EV-2026-08-09-508`: Metro'nun 2026 kampanya koşullarında hariç tutulanlar:
*"toptan-perakende tütün ve **alkol**, çuval şeker, karkas et"*.
→ Şarapta ciro primi / çek / sadakat mekaniği Metro'da **çalışmıyor** görünüyor.
Kanal ekonomisinin bu kalemsiz kurulması gerekebilir.

### İP-503 — Metro'nun ticari dili KDV HARİÇ, etiket dili KDV DAHİL
`EV-508` vs `EV-503/504`. İthalatçı–Metro pazarlığında sayılar büyük olasılıkla
**KDV hariç** konuşulacaktır. Marj modelinde matrah karışıklığına dikkat.

### İP-504 — Metro fiyatı ile online uzman perakende fiyatı arasında büyük fark var
Metro'da ithal giriş 599,90 TL (`EV-501`); online uzman perakendede stokta en ucuz
ithal 875 TL (`EV-509`). Fark %46. Bunun ne kadarı kanal marjı, ne kadarı ürün
segmenti farkı — **ben hesaplamadım, sizin alanınız.**

### İP-505 — Metro'nun online fiyatları müşteriye özel
`guncelfiyatlar.metro-tr.com` → *"Size özel fiyatları görmek için Giriş Yapın"*.
Metro'da müşteri numarasına bağlı **özel fiyat** uygulaması olabilir. Bu, tek bir
raf fiyatının "kanal fiyatı" sayılmasını zorlaştırır.

---

## → `mevzuat-ruhsat-uzmani`

### İP-506 — Alkol reklam yasağı fiyat şeffaflığını yok ediyor
`EV-2026-08-09-514`: Metro'nun incelenen **58 sayfalık** broşür setinde
(48 sayfalık "İçecek Trendleri ve Çözümleri" katalogu dahil) **tek bir alkollü içki
SKU'su bile yok**. Bu, hem bizim veri toplama kabiliyetimizi hem de kendi ürünümüzün
lansman araçlarını doğrudan etkiler. → `T-503`

### İP-507 — Online alkol satışı yasağı, D2C ve fiyat keşfi kanalını kapatıyor
`EV-2026-08-09-511`. Ayrıca `iyisarap.plus` gibi siteler fiyat gösterip satış yapar
görünüyor — bunun yasal statüsü bizim gözlem kaynağımızın güvenilirliğini etkiler.
→ `T-502`

### İP-508 — Fiyat Etiketi Yönetmeliği "toptan+perakende birlikte" hükmü
`EV-2026-08-09-506`. Metro gibi karma formatlarda perakende hükümlerinin uygulandığı
iddiası OQ-001'in hukuki ayağıdır ve **T1 doğrulaması bekliyor.** → `T-501`

### İP-509 — TADAB istatistik sayfası alkollü içki verisi yayınlamıyor
`EV-2026-08-09-515`: `tarimorman.gov.tr/TADAB/Link/38/Resmi-Istatistikler` sayfası
2011–2026 arası **yalnızca yakıt biyoetanolü** dönem raporları içeriyor.
Alkollü içki piyasa istatistikleri başka bir yerde olmalı. → `T-505`

---

## → `global-sourcing-kasifi`

### İP-510 — ABD ve Avustralya menşe, uzman perakende kanalında YOK
`EV-2026-08-09-509`: Online uzman perakendecinin ülke koleksiyonları
Fransa 33 / İtalya 30 / İspanya 6 / Avusturya 4 / Şili 2 / Arjantin 2 / Almanya 2 —
**ABD ve Avustralya koleksiyonu hiç yok.**
Buna karşılık Metro'daki iki benchmark SKU tam da bu iki menşeden.
→ ABD/Avustralya, Türkiye'de **kanal olarak yerleşmemiş** menşeler olabilir;
bu hem fırsat (rekabet yok) hem risk (tüketici tanıdıklığı yok) demektir.

### İP-511 — Benchmark markaları Avrupa'da discount/value markası profilinde
"Gold Country Colombard-Chardonnay" Almanya'da içki toptancıları ve posta siparişi
kanallarında ~7 EUR bandında listeleniyor (T5, arama sonucu düzeyinde — doğrulanmadı).
Bu, benchmark'ın **bulk-blend / value** kategorisinde olduğuna işaret eder.
Sourcing hedefi bu kategoriye göre seçilmelidir. **Bu bir fiyat verisi değildir,
sizin doğrulamanız gerekir.**

### İP-512 — Yerli üretici benchmark bandını dolduruyor
`EV-2026-08-09-510`: 600–800 TL bandında 25 yerli SKU var, 0 ithal SKU.
Yani ithal edeceğimiz ürün, bu bandda **yerli üreticiyle** yarışacak —
gümrük/ÖTV yükü taşımayan rakiplerle. Bu, hedef EXW/FOB'u sertçe aşağı çeker.

---

## → `gumruk-vergi-uzmani`

### İP-513 — Metro künyesi: vergi değişikliği fiyata aynen yansıtılır
`EV-2026-08-09-507`: *"Devlet tarafından yapılan vergi ve fon değişiklikleri fiyatlara
aynen yansıtılacaktır."* → Perakende kanal, vergi artışını **tampon yapmıyor**;
ÖTV artışı doğrudan raf fiyatına geçiyor. Bu, ÖTV duyarlılık analizinde
"kanal yutar mı" sorusuna cevap verir: **yutmuyor.**

### İP-514 — Şikâyet kayıtlarında KDV oranı tartışması
Şikâyet platformunda Metro için "rafta %1 KDV yazıyor, kasada %8 uygulanıyor"
tipi kayıtlar var (T5, LOW). Gıda dışı/gıda KDV oranı ayrımı şarap için geçerli
değildir ama **şarapta uygulanan KDV oranının doğrulanması sizin alanınızdır.**
Ben oran belirtmiyorum.

---

## → `yatirim-komitesi-baskani`

### İP-515 — `00-charter/benchmark.md` güncelleme önerisi
Ben o dosyaya dokunmadım. Önerim:

```yaml
BENCHMARK 1 - Gold Country:
  KDV durumu:            KDV DAHIL     # eski: UNKNOWN
  KDV durumu status:     ESTIMATE (HIGH)  # EV-503/504/505/506
  Fiyat katmani:         L8_METRO_CASH_CARRY   # eski: UNKNOWN
  Fiyat katmani notu:    "Zincir market L8'i DEGILDIR; HoReCa/bakkal icin L7-proxy"
  Promosyon durumu:      UNKNOWN       # DEGISMEDI - T-504 acik
  evidence_id:           EV-2026-08-09-501
BENCHMARK 2 - Central Creek:  ayni sekilde, evidence_id: EV-2026-08-09-502
```

Ve `MODEL KULLANIM KURALI` bölümünde BM_A'nın base case, BM_B'nin sensitivity
olması; BM_C (promosyon) ve BM_D (zincir L8 farkı) senaryolarının eklenmesi.

### İP-516 — Bu turun en zayıf noktası: kanal örneklemi
52 gözlemin 45'i **tek bir online kanaldan** geliyor. Zincir market ve tekel
bayiinde **sıfır** gözlem var. Segment bantlarını "Türkiye pazarı" diye okumak
şu an **hatalı** olur. → `OQ-502`
