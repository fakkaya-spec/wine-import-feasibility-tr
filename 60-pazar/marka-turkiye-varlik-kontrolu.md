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
| Kısa listedeki 11 tedarikçinin **hiçbirinin** Türkiye'de mevcut ithalatçısı bulunamadı | Yerinden edilecek bir **incumbent distribütör yok** → distribütörlük/private-label müzakeresi **temiz sayfadan** başlar | **LEHTE** |
| Aynı 11 tedarikçinin **hiçbir ürünü** Türkiye'de görülemedi | Türkiye'de **pazar validasyonu da yok** → talep kanıtı sıfır, listeleme ikna yükü bize ait | **ALEYHTE** |
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
4. **İthalatçı kodlarının 13/17'si çözülmedi** (`OQ-551`).
5. **Resmî ithalatçı listesi hâlâ yok.** TADAB dağıtım/ithalat uygunluk belgesi
   sahipleri listesi alınamadı — `T-505` (TUR 1) açık kalıyor, `T-564` ile hatırlatıldı.
