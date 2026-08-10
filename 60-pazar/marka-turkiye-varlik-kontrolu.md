# SOURCING KISA LİSTESİ × TÜRKİYE VARLIK KONTROLÜ

```yaml
ajan:            turkiye-pazar-kasifi
tur:             TUR 2 (destek kapsamı)
tarih:           2026-08-10
durum:           DRAFT
kaynak_liste:    "50-sourcing/tedarikci-havuzu.csv (TUR 1, 11 tedarikçi)
                  + 50-sourcing/supplier-shortlist-v2.csv (TUR 2, 26 tedarikçi)
                  + 50-sourcing/top-10-rfq-targets.md
                  + T-464'ün sorduğu 7 Model A markası"
kapsam:          "TOPLAM 26 tedarikçi × 30+ marka adı tarandı."
cevaplanan:      T-464 (global-sourcing-kasifi -> turkiye-pazar-kasifi)
acilan:          T-565
```

> **NOT:** `supplier-shortlist-v2.csv` ve `top-10-rfq-targets.md` bu çalışmanın
> ortasında (2026-08-10 07:29–07:35) oluştu; **kontrol tekrarlandı** ve her ikisi
> de kapsama alındı. §1 TUR 1 havuzunu, §1B TUR 2 v2 listesini kapsar.

---

## 0. BU DOSYA NE İDDİA EDER, NE İDDİA ETMEZ

**İddia eder:** Aşağıdaki markalar/üreticiler, **erişilebilen tek Türk uzman şarap
perakendecisinin 1.304 listemelik / 274 üreticilik kataloğunda** ve yapılan hedefli
web aramalarında **bulunamamıştır** (`EV-2026-08-10-553`, `EV-2026-08-10-563`).

**İddia ETMEZ:** Bu markaların Türkiye'de olmadığını. Türkiye'de şarap raf verisi
yapısal olarak kapalıdır (`EV-2026-08-10-559`); Metro, zincir market, tekel bayii ve
HoReCa rafları **görülmemiştir**. Doğru okuma **`BULUNAMADI` = presence UNKNOWN**'dır,
`YOK` değil.

---

## 1. ÖZET TABLO — 11 TEDARİKÇİ

| # | Tedarikçi (supplier_id) | Ülke | Türkiye'de ürünü bulundu mu? | Marka(lar) taranan | Mevcut TR ithalatçısı | status |
|---|---|---|---|---|---|---|
| 1 | Interbrosa Family Wines (SUP-401) | İspanya | **BULUNAMADI** | *(private label — marka adı yok)* | **BULUNAMADI** | UNKNOWN |
| 2 | Viña Maria (SUP-402) | İspanya | **BULUNAMADI** | *(private label — marka adı yok)* | **BULUNAMADI** | UNKNOWN |
| 3 | Vinicola Vedovato Mario (SUP-403) | İtalya | **BULUNAMADI** | *(private label — marka adı yok)* | **BULUNAMADI** | UNKNOWN |
| 4 | The Wine Factory (SUP-404) | Fransa | **BULUNAMADI** | *(private label — marka adı yok)* | **BULUNAMADI** | UNKNOWN |
| 5 | Antawara Vineyards (SUP-405) | Şili | **BULUNAMADI** | Antawara | **BULUNAMADI** | UNKNOWN |
| 6 | Corta Hojas (SUP-406) | Şili | **BULUNAMADI** | Corta Hojas | **BULUNAMADI** | UNKNOWN |
| 7 | Origin Wine (SUP-407) | Güney Afrika | **BULUNAMADI** | Origin Wine / Bespoke Brands | **BULUNAMADI** | UNKNOWN |
| 8 | FMS Wine Marketing (SUP-408) | Güney Afrika | **BULUNAMADI** | *(aracı — marka adı yok)* | **BULUNAMADI** | UNKNOWN |
| 9 | Kingston Estate Wines (SUP-409) | Avustralya | **BULUNAMADI** | Kingston Estate, Kingston Echelon | **BULUNAMADI** | UNKNOWN |
| 10 | Scheid Family Wines (SUP-410) | ABD / California | **BULUNAMADI** | Mundaka, Odd Lot, Blue Canyon, Paso Point, Long Valley Ranch, Windfinder | **BULUNAMADI** | UNKNOWN |
| 11 | Casa Santos Lima (SUP-411) | Portekiz | **BULUNAMADI** | Quinta da Espiga, Quinta das Setencostas, Palha-Canas | **BULUNAMADI** | UNKNOWN |

**Eşleşme sayısı: 0 / 11.**
Tarama 24 arama terimiyle yapıldı; tek eşleşme **yalancı pozitifti**:

> `Tormentoso` (Güney Afrika, Kavaklıdere portföyünde) — **MAN Vintners**'a aittir,
> Origin Wine ile ilgisi yoktur (`EV-2026-08-10-561`).

---

## 1B. ÖZET TABLO — `supplier-shortlist-v2.csv` YENİ TEDARİKÇİLERİ (SUP-451…465)

`EV-2026-08-10-564`

| # | Tedarikçi | Ülke | Model | Türkiye'de ürünü bulundu mu? | Mevcut TR ithalatçısı |
|---|---|---|---|---|---|
| SUP-451 | Harland Wine Company | Avustralya | B | BULUNAMADI | BULUNAMADI |
| **SUP-452** | **Cantina Danese s.r.l.** | **İtalya** | **B** | ✅ **BULUNDU** — *Danese Primitivo Puglia "Black Label"*, listeleme 1.419 TL, **stokta değil** | ✅ **VAR** — iç etiket `Midas`, **kimlik UNKNOWN** |
| SUP-453 | Zidela Worldwide Wines | G. Afrika | B | BULUNAMADI | BULUNAMADI |
| SUP-454 | Vidigal Wines (**Porta 6**) | Portekiz | A | BULUNAMADI | BULUNAMADI |
| SUP-455 | Parras Wines | Portekiz | A | BULUNAMADI | BULUNAMADI |
| SUP-456 | Felix Solis Avantis (**Viña Albali**, Los Molinos, **Mucho Mas**, Marques de Moral) | İspanya | A | BULUNAMADI | BULUNAMADI |
| SUP-457 | Plaimont (**Colombelle**, BIG) | Fransa | A | BULUNAMADI | BULUNAMADI |
| SUP-458 | Spanish Origin | İspanya | B | BULUNAMADI | BULUNAMADI |
| SUP-459 | Clark Estate | Yeni Zelanda | B | BULUNAMADI | BULUNAMADI |
| SUP-460 | Bodegas San Valero (**Particular**, Monte Ducay) | İspanya | A+B | BULUNAMADI | BULUNAMADI |
| SUP-461 | Purcari Wineries Group (**Purcari**, **Bostavan**, Crama Ceptura, Domeniile Cuza) | Moldova/RO/BG | A | BULUNAMADI | BULUNAMADI |
| SUP-462 | O'Neill Vintners (Line 39, Robert Hall, Harken) | ABD | B | BULUNAMADI | BULUNAMADI |
| SUP-463 | Viña Luis Felipe Edwards | Şili | B | BULUNAMADI | BULUNAMADI |
| SUP-464 | Bronco Wine Company (Charles Shaw, Forest Glen) | ABD | B | BULUNAMADI | BULUNAMADI |
| SUP-465 | Geo Vino Wines | ABD (çok menşeli) | B | BULUNAMADI | BULUNAMADI |

**Eşleşme: 1 / 15 (yeni) · 1 / 26 (toplam).**

### 1B.1 Tek eşleşme neden önemli — ve neden beklenmedik

`SUP-452` **Cantina Danese**, `top-10-rfq-targets.md`'de **2. sıradaki RFQ hedefidir**
ve **Model B (private label)** olarak listelenmiştir. Yani:

> Private label tedarikçisinin de Türkiye'de **kendi markasıyla** mevcut bir
> ithalatçı ilişkisi olabilir.

Bu, private label modelinin sessiz varsayımını ("tedarikçinin Türkiye'de markası
yok, dolayısıyla çakışma yok") **bu tedarikçi için yanlışlar**. Ticari sonucu
`global-sourcing-kasifi`'ye `T-565` ile taşındı: RFQ'ya *"Türkiye'de hâlihazırda
ithalatçınız var mı, private label işi bu ilişkiyle çakışır mı?"* sorusu eklenmelidir.

> **UYARI:** 1.419 TL bir **raf fiyatı değildir** (stok dışı listeleme). Bu satırda
> önemli olan **fiyat değil, VARLIKTIR**.

### 1B.2 T-464'ün cevabı (7 Model A markası)

| Marka | Üretici | Sonuç |
|---|---|---|
| Viña Albali · Los Molinos · Mucho Mas · Marques de Moral | Felix Solis Avantis | **BULUNAMADI** |
| Porta 6 (+ Vidigal) | Vidigal Wines | **BULUNAMADI** |
| Colombelle · BIG | Plaimont | **BULUNAMADI** |
| Quinta da Espiga · Setencostas · Palha-Canas | Casa Santos Lima | **BULUNAMADI** |
| Particular | Bodegas San Valero | **BULUNAMADI** |
| Purcari · Bostavan · Crama Ceptura · Domeniile Cuza | Purcari Wineries Group | **BULUNAMADI** |
| Parras markaları | Parras Wines | **BULUNAMADI** |

→ `T-464` cevabı: **"hiçbirinin ithalatçısı bulunamadı"** = Model A adayları
listeden **düşmez**. Ama karşılığında **pazar validasyonu da yoktur**.

Tam cevap: `99-ops/tickets/T-464.md` → CEVAP bölümü.

---

## 2. MENŞE DÜZEYİNDE DESTEKLEYİCİ BULGU

Kısa listedeki tedarikçilerin menşeleri, incelenen kanalda **yapısal olarak zayıftır**
(`EV-2026-08-10-563`, 2026-08-10):

| Menşe | Kanaldaki listeleme | Stokta | Yorum |
|---|---|---|---|
| **ABD / California** | **koleksiyon YOK** | — | Benchmark'ın menşei bu kanalda hiç temsil edilmiyor (TUR 1 B-8 doğrulandı) |
| **Avustralya** | **koleksiyon YOK** | — | Komşu benchmark'ın menşei de yok |
| **Portekiz** | 5 | **0** | 4'ü porto + Mateus Rosé. Sofra şarabı karşılığı yok → Casa Santos Lima tipi ürünün kanalda emsali yok |
| **Güney Afrika** | 2 | **0** | Hill & Dale, Tormentoso |
| Şili | 20 | 2 | Stokta olanlar 1.189 ve 1.782 TL (üst bant) |
| İspanya | 21 | 6 | |
| İtalya | 176 | 30 | Baskın menşe |
| Fransa | 150 | 33 | Baskın menşe |

**Okuma (ESTIMATE, kanıt değil):** İncelenen uzman kanal **Fransa + İtalya** eksenlidir.
Kısa listedeki 11 tedarikçinin 7'si (ES, CL, ZA, AU, US, PT) bu kanalın **zayıf veya
sıfır** menşelerindedir. Bu iki yönde okunabilir ve **seçim yapılmamıştır**:

| Okuma | Anlamı |
|---|---|
| **A) Boşluk = fırsat** | Bu menşelerde uzman kanal rekabeti yok |
| **B) Boşluk = talep yokluğu** | Tüketici tanıdıklığı yok, kanal listelemek istemiyor |

---

## 3. MEVCUT İTHALATÇI / DİSTRİBÜTÖR HARİTASI — TUR 2'DE **KISMEN AÇILDI**

TUR 1'de doğrulanmış ithalatçı sayısı **1**'di (Mey|Diageo, `EV-2026-08-09-513`).
TUR 2'de bu **4 doğrulanmış + 13 kodu bilinen ama kimliği bilinmeyen** gruba çıktı.

### 3.1 Yöntem ve neden ESTIMATE

Erişilebilen perakendecinin ürün feed'inde her ithal ürün bir **iç etiket** (merchandising
tag) taşır. Bu etiketlerin **tedarikçi/ithalatçı grubu** olduğu hipotezi **iki bağımsız
üretici/ithalatçı kaynağıyla test edildi ve doğrulandı** (`EV-2026-08-10-557`):

- `KVKLDR` etiketli 26 üreticinin **23'ü** Kavaklıdere'nin kendi *İthal Ürünler*
  sayfasında birebir yer alıyor (`EV-2026-08-10-554`).
- `KDT` etiketli Marchesi Antinori'nin Türkiye distribütörü, Antinori'nin **kendi**
  dağıtım sayfasında **Karagözoğlu Dış Ticaret A.Ş.** (`EV-2026-08-10-555`).

**Yine de ESTIMATE'tir**, çünkü: (a) kodların anlamı perakendeci tarafından ilan
edilmemiştir; (b) 13/17 kodun açılımı `UNKNOWN`'dır; (c) bir markanın bu etiketi
taşıması, o firmanın Türkiye'deki **tek** ithalatçısı olduğunu **kanıtlamaz** —
yalnızca *bu perakendecinin o markayı kimden aldığını* gösterir.

### 3.2 Harita

| Kod | İthalatçı / grup | Kimlik statüsü | Marka sayısı | Örnek markalar |
|---|---|---|---|---|
| `KVKLDR` | **Kavaklıdere Şarapları A.Ş.** | **FACT** (`EV-554`) | 26 | Torres, Montes, Santa Helena, **Gato Negro**, Baron de Lestac, Moncigale, Taittinger, Bollinger, Pommery, M. Chapoutier, Louis Bernard, Kaiken, Michele Chiarlo, Castellani, La Tordera, Serena 1881, Müller, Prinz von Hessen, Gusbourne, Bodvar, Jaffelin, Tormentoso (MAN) |
| `KDT` | **Karagözoğlu Dış Ticaret A.Ş.** | **FACT** (`EV-555`) | 20 | Marchesi Antinori, Joseph Drouhin, Pol Roger, **La Vieille Ferme**, Prunotto, Tormaresca, Niepoort, Jean Pierre Moueix, Schloss Gobelsburg, Barone Montalto, MGM Mondo del Vino (La Piuma), Paolo Scavino, Lucien Crochet, Uvas Felices |
| `ADCO` | **Adco Gıda A.Ş. / Kemer Gıda** | İthalatçı kimliği **FACT** (`EV-556`); portföy **ESTIMATE** | 22 | Concha y Toro (Casillero del Diablo), Louis Roederer, Gaja, Domaines Ott, Famille Hugel, Mionetto, Henkell, Lamberti, Bolla, Alamos, Babich, La Scolca, Chateau d'Esclans, Quinta do Noval, W&J Graham's |
| `BRN` | **Baron Şarapçılık A.Ş.** (muhtemel) | **ESTIMATE** (`EV-562`, T5 + iç tutarlılık) | 44 | **J.P. Chenet**, Calvet, Dulong, Louis Jadot, Masi, Sassicaia, Ch. Margaux, Ch. Lafite Rothschild, Ch. Pétrus, Ch. d'Yquem, Taylor's, Hans Baer, Chemin des Papes, Arthur Metz |
| `frosta` | UNKNOWN | UNKNOWN | 17 | Botter, **Gran Passione**, Castello Banfi, Campagnola, Villa Sandi, Medici Ermete, Natale Verga, Ginestet, Maison Saint Aix |
| `Midas` | UNKNOWN | UNKNOWN | 15 | Bodega Matsu, Cà dei Frati, Castellare di Castellina, La Spinetta, Hacienda López de Haro, Mar de Frades, Guerrieri Rizzardi |
| `MALTİTHAL` | UNKNOWN | UNKNOWN | 9 | Dezzani, Viña Bujanda, Bindi Sergardi, Ch. de l'Aumérade, Gabbia D'oro |
| `küregıdaithal` | UNKNOWN (Küre Gıda?) | UNKNOWN | 9 | **Fantini**, **Luccarelli**, Caparzo, Alpha Estate, Loimer, Rivetto, Maximin Grünhaus |
| `demglobal` / `Future` | UNKNOWN (LVMH portföyü) | UNKNOWN | 8 | Moët & Chandon, Dom Pérignon, Veuve Clicquot, Ruinart, Cloudy Bay, Chandon, Terrazas, Ch. Minuty |
| `ADT` | UNKNOWN | UNKNOWN | 7 | Zonin 1821, Cavicchioli, Billecart-Salmon, Escudo Rojo, **Tesori** |
| `LUCE` | UNKNOWN | UNKNOWN | 6 | Tommasi, Marchesi di Barolo, Paternoster, Masseria Surani, Poggio Al Tufo |
| `Nadiya` | UNKNOWN | UNKNOWN | 6 | Naveran, Meritxell Pallejà, Uvas Felices, 502 Vineyards |
| `piramitgıda` | UNKNOWN | UNKNOWN | 5 | **Radacini** (Moldova), Laurent-Perrier, Perlino, Uggiano |
| `PiyasaGıda` | UNKNOWN | UNKNOWN | 3 | **Imperial Vin**, **Chateau Vartely**, **Kazayak** (hepsi Moldova) |
| `INANC` | UNKNOWN | UNKNOWN | 3 | Baia's Winery, Chelti Winery, Juso's Winery (Gürcistan) |
| `Vinist` | UNKNOWN | UNKNOWN | 2 | **Alpaca** (Şili), **Mateus** (Portekiz) |

> **Kalın** yazılan markalar, fiyat/performans bandında bilinen giriş-segment ithal
> markalardır. Yani **hedef bandımızda ithalat yapan oyuncular Türkiye'de mevcuttur** —
> bu markaların o bandda **satılıp satılmadığı** ayrı bir sorudur (bkz. §4).

### 3.3 Konsolidasyon okuması (ESTIMATE)

İncelenen kanaldaki ~200 ithal markanın **%56'sı 4 grupta** toplanıyor
(`BRN` 44 + `KVKLDR` 26 + `ADCO` 22 + `KDT` 20 = 112). Bu **bir konsolidasyon
sinyalidir**, ama **kanıt değildir**: tek perakendecinin tedarikçi tercihini yansıtır,
Türkiye ithalat pazarının payını değil. `ithalatci_haritasi.konsolidasyon_derecesi`
alanı **`UNKNOWN` kalmalıdır**.

---

## 4. TİCARİ SONUÇ — DİSTRİBÜTÖRLÜK MÜZAKERESİ AÇISINDAN

| Bulgu | Ticari anlamı | Yön |
|---|---|---|
| **25 / 26** tedarikçinin Türkiye'de mevcut ithalatçısı bulunamadı (7 Model A markası dahil) | Yerinden edilecek bir **incumbent distribütör yok** → distribütörlük/private-label müzakeresi **temiz sayfadan** başlar | **LEHTE** |
| Aynı 25 tedarikçinin **hiçbir ürünü** Türkiye'de görülemedi | Türkiye'de **pazar validasyonu da yok** → talep kanıtı sıfır, listeleme ikna yükü bize ait | **ALEYHTE** |
| **1 / 26 istisna: Cantina Danese (RFQ hedefi #2)** Türkiye'de kendi markasıyla listeli ve bir ithalatçıya bağlı | Bu tedarikçide müzakere **temiz sayfa değildir**: münhasırlık / kanal çakışması / fiyat tabanı riski | **ALEYHTE (o tedarikçide)** → `T-565` |
| Kavaklıdere gibi **yerli üretici** aynı zamanda giriş-segment ithal distribütörü (Gato Negro, Santa Helena, Baron de Lestac) | Hedef bandda rakip yalnızca yerli şarap değil; **yerli üreticinin ithal portföyü** de rakip. Aynı satış gücü hem yerliyi hem ithali taşıyor | **ALEYHTE** |
| Fiyat/performans bandında ithalat yapan **küçük oyuncular var** (Moldova: PiyasaGıda, piramitgıda; Şili: Vinist/Alpaca) | Bu bantta ithalat **yapılabiliyor** — model imkânsız değil | **LEHTE** |
| Bu bandın ithal ürünlerinin **tamamı incelenen kanalda stok dışı** (`EV-2026-08-10-552`) | Bandda ithal ürün **listeleniyor ama dönmüyor** olabilir | **ALEYHTE (güçlü)** |

> **UYARI (K4 / CLAUDE.md §7):** Yukarıdaki hiçbir satır bir **marj** veya
> **kanal ekonomisi** sonucu değildir. Distribütörlük müzakeresinin *ekonomisi*
> `kanal-marj-uzmani`'nın, tedarikçi fiyatı `global-sourcing-kasifi`'nin alanıdır.

---

## 5. BU KONTROLÜN ZAYIFLIKLARI (AÇIKÇA)

1. **Tek kanal.** Marka varlık kontrolünün tamamı bir perakendecinin kataloğuna
   dayanır. TUR 1'in 45/52 tek-kanal yoğunlaşması TUR 2'de **düzelmemiştir**;
   denenen 8 alternatif kanalın hepsi kapalı çıkmıştır (`EV-2026-08-10-559`).
2. **Metro görülmedi.** Benchmark'ın kendi kanalı (Metro) taranamadı. Kısa listedeki
   bir markanın Metro rafında olması **tamamen mümkündür** ve bu kontrol onu yakalayamaz.
3. **Private label tedarikçileri zaten görünmez.** SUP-401/402/403/404/408 private
   label üreticisidir; ürünleri **müşterinin markasıyla** satılır. Bunların Türkiye'de
   "bulunamaması" **beklenen** sonuçtur ve bilgi değeri düşüktür. Gerçek soru
   "bu üreticinin şişesi Türkiye'de var mı" değil, "Türkiye'ye daha önce ihraç etti mi"
   olmalıdır — bu `global-sourcing-kasifi`'nin RFQ sorusudur (`T-562`).
   **Ama Cantina Danese bu kuralın istisnasıdır:** private label üreticisi olmasına
   rağmen **kendi markasıyla** Türkiye'de görülmüştür. Yani *"private label üreticisi
   → Türkiye'de görünmez"* kabulü **evrensel değildir**; her tedarikçi ayrı taranmalıdır.
4. **İthalatçı kodlarının 13/17'si çözülmedi** (`OQ-551`) — bunlardan biri
   (`Midas`) tam da Cantina Danese'yi getiren gruptur, yani **en kritik eşleşmenin
   karşı tarafı `UNKNOWN`'dır**.
5. **Resmî ithalatçı listesi hâlâ yok.** TADAB dağıtım/ithalat uygunluk belgesi
   sahipleri listesi alınamadı — `T-505` (TUR 1) açık kalıyor, `T-564` ile hatırlatıldı.
