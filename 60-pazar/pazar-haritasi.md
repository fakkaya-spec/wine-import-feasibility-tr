# TÜRKİYE ŞARAP PERAKENDE PAZAR HARİTASI — TUR 1

```yaml
ajan:   turkiye-pazar-kasifi
tur:    TUR 1
tarih:  2026-08-09
durum:  DRAFT
uyari:  "Bu harita 52 gozlem satirina dayanir. Tek kanal agirlikli (online uzman perakende).
         Fiziksel magaza gozlemi yalnizca 2 satirdir (benchmark). Genellemeyin."
```

---

## 0. EN ÖNEMLİ YAPISAL BULGU — PAZAR ŞEFFAF DEĞİL

Türkiye'de şarap raf fiyatı verisi toplamak **yapısal olarak zordur**:

| Kısıt | Gözlem | evidence |
|---|---|---|
| Alkollü içki **tüketiciye internetten satılamaz** | Migros / CarrefourSA / Macrocenter online kanallarında şarap fiyatı yok | `EV-511` (T5 — hukuki dayanak mevzuat ajanının alanı) |
| Alkol **reklamı / kampanya tanıtımı yasak** | Metro'nun incelenen 58 sayfalık broşür setinde **tek bir alkollü içki bile yok** | `EV-514` |
| Metro online fiyatları **üyeliğe özel** | `guncelfiyatlar.metro-tr.com` → "Size özel fiyatları görmek için Giriş Yapın" | — |

**Sonuç:** Bu projede raf fiyatı verisi ancak (a) fiziksel mağaza gözlemi,
(b) online uzman şarap siteleri, (c) HoReCa menüleri üzerinden toplanabilir.
"Web'den fiyat çekip pazar haritası çıkarmak" bu kategoride **çalışmaz**.
Bu, kendi ürünümüzün pazarlama seçeneklerini de kısıtlar (`kanal-marj-uzmani`'na ipucu).

---

## 1. KANAL HARİTASI

| Kanal | Format | Erişildi mi | Fiyat gözlemi | Not |
|---|---|---|---|---|
| **Metro Türkiye** | Cash & carry, 32 satış noktası / 19 il (Metro'nun kendi beyanı) | Kısmen | 2 gözlem (benchmark) + 5 T5 satır | Bireysel müşteriye **açık** (`EV-505`). Mağaza fiyatı ≠ sevkiyat fiyatı (`EV-507`) |
| **Migros / Macrocenter** | Chain retail | **HAYIR** | 0 | Online'da alkol yok |
| **CarrefourSA** | Chain retail | **HAYIR** | 0 | Online'da alkol yok |
| **BİM / A101 / Şok** | Hard discount | **HAYIR** | 0 | Şarap SKU'su olup olmadığı UNKNOWN |
| **Bizim Toptan** | Cash & carry (yerli) | **HAYIR** | 0 | Metro'nun doğrudan rakibi — TUR 2'de bakılmalı |
| **Tekel bayii / bağımsız** | Independent retail | **HAYIR** | 0 | Fiyat listesi yayınlanmıyor |
| **Online uzman şarapçı** (iyisarap.plus / .pro) | Online | **EVET** | 45 gözlem | 474 stokta SKU; aynı şirketin iki sitesi (aynı fiyatlar) |
| **HoReCa** | Restoran/otel | **HAYIR** | 0 | **KRİTİK BOŞLUK** |
| **Duty free** | — | Kapsam dışı (charter) | — | — |

---

## 2. FİYAT SEGMENTLERİ (750 ml, TL, gözlemlenen)

> Bantlar **gözlemden türetilmiştir**, sektör standardı değildir. `ESTIMATE`.
> Kaynak: `EV-509` (ithal, n=80), `EV-510` (yerli, n=394), `EV-501/502` (Metro).

| Segment | Bant (TL) | Yerli SKU | İthal SKU (online uzman) | Gözlem |
|---|---|---|---|---|
| **Giriş** | < 600 | 1 (Mistia 460) | **0** | Neredeyse boş |
| **FİYAT/PERFORMANS (hedef)** | **600 – 900** | **~40** | **2** (Tesori 875, La Piuma 948*) | **Benchmark burada** (599,90 / 649,90) |
| **Orta** | 900 – 1.500 | ~165 | 6 | Yoğunlaşma başlıyor |
| **Üst-orta** | 1.500 – 2.500 | ~118 | 24 | İthalin ağırlık merkezi |
| **Üst** | > 2.500 | ~42 | 48 | İthal burada domine ediyor |

\* La Piuma 948 TL teknik olarak 900+ bandında.

### 2.1 SEGMENTİN EN ÖNEMLİ TESPİTİ

> **Online uzman perakende kanalında 400–800 TL bandında STOKTA
> TEK BİR İTHAL ŞARAP YOKTUR (`EV-509`).**
> En ucuz stokta ithal şarap **875 TL**'dir.
> Aynı bandı **yalnızca yerli üretici** dolduruyor (`EV-510`).

Bu, benchmark hakkında iki alternatif okuma üretir:

| Okuma | Anlamı | Proje için |
|---|---|---|
| **A) Metro fiyat kırıcı** | Metro doğrudan ithalat + cash&carry marj yapısıyla, uzman perakendenin giremediği bandda ithal şarap satabiliyor | Bu bandda iş var, ama **Metro'nun maliyet yapısıyla** yarışmak gerekir |
| **B) Kanal farkı** | 599,90 TL Metro'nun cash&carry fiyatıdır; aynı ürün zincir/uzman perakendede 800–900 TL'ye çıkar | Hedef raf fiyatı 599,90 değil, daha yüksek olabilir |

**İkisi arasında seçim yapılmadı.** Her ikisi de canlıdır. `finans-fizibilite`
her iki hedefi de test etmelidir.

---

## 3. BENCHMARK BANDINDAKİ (500–900 TL) RAKİPLER

### 3.1 İthal (gözlemlenen)

| SKU | Menşe | Fiyat TL | Kanal | evidence |
|---|---|---|---|---|
| Gold Country Colombard-Chardonnay 2023 | ABD / California | 599,90 | Metro (cash&carry) | `EV-501` |
| Central Creek | Avustralya | 649,90 | Metro (cash&carry) | `EV-502` |
| Tesori Prosecco Frizzante | İtalya | 875 | Online uzman | `EV-509` |

**ABD ve Avustralya menşeli şarap, incelenen online uzman kanalın ülke
koleksiyonlarında HİÇ YOK** (Fransa 33, İtalya 30, İspanya 6, Avusturya 4, Şili 2,
Arjantin 2, Almanya 2). Yani benchmark'ın iki menşei bu kanalda **temsil edilmiyor**.
Bu, Metro'nun bu SKU'ları **kendi ithalat/exclusive** hattından getiriyor olabileceğine
işaret eder — **ama doğrulanmadı (UNKNOWN).**

### 3.2 Yerli (gözlemlenen — asıl rakip)

| SKU | Üretici | Fiyat TL |
|---|---|---|
| Mistia Gafa Beyaz Blend | Mistia | 460 |
| Asmadan Kor Blend | Asmadan | 649 |
| KA Winery Pulse / Lermonos Çal Karası | KA / Lermonos | 655 |
| Umurbey Blend | Umurbey (Diren) | 659 |
| Nif Bağları Perseus Beyaz/Kırmızı | Nif Bağları | 670 |
| Mistia Cinane Ak Üzüm | Mistia | 672 |
| Vinkara Kalecik Karası / Öküzgözü-Boğazkere | Vinkara | 710 |
| Vinkara Narince | Vinkara | 752 |
| Turasan Narince / Misket | Turasan | 758 |
| Çamlıbağ Kuntra / Karalahna | Çamlıbağ | 760 |
| Umurbey Sauvignon Blanc & Chardonnay | Umurbey | 769 |
| Diren Selection Beyaz | Diren | 790 |
| Barel Cabernet Sauvignon & Merlot | Barel | 790 |
| Büyülübağ Blush | Büyülübağ | 792 |

**Beyaz şarap özelinde** (benchmark beyaz) doğrudan rakipler:
Nif Bağları Perseus Beyaz 670 · Mistia Cinane 672 · Vinkara Narince 752 ·
Turasan Narince 758 · Umurbey SB&Chardonnay 769 · Diren Selection Beyaz 790.

**Metro'daki yerli fiyatlar (T5, MODELE GİRMEZ, `EV-512`):**
Doluca 75 cl 630 TL · Grand Reserve Boğazkere 570 TL · Doluca 37,5 cl 480 TL.
→ Eğer doğruysa, Metro'da yerli giriş seviyesi 570–630 TL, ithal benchmark 599,90 TL.
**Yani ithal ürün yerli ile TAM AYNI bandda yarışıyor.** Bu, fiyat/performans
segmentinde ithalatın en zor tarafıdır: ÖTV/gümrük yükünü taşıyan ithal ürün,
yerli üreticinin fiyatına inmek zorunda kalıyor.

---

## 4. İTHALATÇI / DİSTRİBÜTÖR HARİTASI — **BÜYÜK ÖLÇÜDE UNKNOWN**

| İthalatçı | Getirdiği ithal şarap markaları | Kanal gücü | evidence |
|---|---|---|---|
| **Mey Diageo** | Cielo, Ruffino, Château Bel Air (site metninde ayrıca Echo Falls, Nobilo, Zuccardi, Antares vb.) | UNKNOWN | `EV-513` |
| Metro Türkiye (kendi ithalatı?) | Gold Country, Central Creek (varsayım — **DOĞRULANMADI**) | UNKNOWN | — |
| Diğer ~80 firma (iddia) | UNKNOWN | UNKNOWN | T5 iddia, doğrulanmadı |

**UNKNOWN — kritik:**
- Türkiye'de kaç ithalatçı var, pazar ne kadar konsolide → **UNKNOWN**
- Gold Country ve Central Creek'i kim ithal ediyor → **UNKNOWN**
- Her markanın hangi kanalda listeli olduğu → **UNKNOWN**

**Nasıl kapatılır:** TADAB "Dağıtım / İthalat Uygunluk Belgesi" sahipleri listesi
(mevzuat-ruhsat-uzmani'nın erişim alanı — `T-505`), veya şişe arka etiketindeki
"ithalatçı" bilgisinin fiziksel gözlemi.

---

## 5. İTHALAT HACMİ VE PAZAR YAPISI — **UNKNOWN (KRİTİK)**

| Veri | Durum | Neden |
|---|---|---|
| Türkiye şarap ithalatı (litre) | **UNKNOWN** | `EV-515` |
| Türkiye şarap ithalatı (değer) | **UNKNOWN** | `EV-515` |
| Menşe kırılımı | **UNKNOWN** | `EV-515` |
| İthal payı / toplam şarap tüketimi | **UNKNOWN** | `EV-515` |
| Trend | **UNKNOWN** | `EV-515` |

**Erişim denemeleri ve sonuçları:**
- TADAB *Resmî İstatistikler* sayfası (T2): 2011–2026 arası **yalnızca yakıt biyoetanolü**
  dönem raporları yayınlıyor. Alkollü içki piyasa istatistiği **bu sayfada yok**.
- Ticaret Bakanlığı "Alkollü ve Alkolsüz İçecekler" sektör PDF'i → **HTTP 503**
- mevzuat.gov.tr / resmigazete.gov.tr → **HTTP 503**
- TÜİK dış ticaret sorgusu → bu turda yapılamadı

**Bu UNKNOWN pazar büyüklüğü sorusunu bloke eder.**
"5.000 mi 100.000 şişe mi satılır" sorusu bu veri olmadan cevaplanamaz.

---

## 6. HoReCa / RETAIL AYRIMI — **UNKNOWN**

Elde edilen tek somut veri:

> `EV-2026-08-09-507` — Metro broşür künyesi:
> *"Broşürdeki fiyatlar **sevkiyat hizmeti alan müşterilerimiz için geçerli değildir**."*

Yani Metro'nun **mağazadan al-götür (cash & carry)** fiyatı ile
**Metro Gastro Servis / teslimat (HoReCa dağıtım)** fiyatı **farklıdır** —
ama fark **UNKNOWN**.

| Soru | Durum |
|---|---|
| HoReCa hacim payı | UNKNOWN |
| HoReCa fiyat çarpanı (restoran şişe fiyatı / raf fiyatı) | UNKNOWN — **hiç gözlem yok** |
| Hangi segment hangi kanalda | UNKNOWN |

**Not:** Charter'da kanal önceliği `1) Chain retail 2) Independent/tekel 3) HoReCa`.
Bu turda **1 ve 2'de sıfır gözlem** alınabildi. Bu bir eksikliktir, gizlenmemektedir.

---

## 7. GÖZLEM SAYIM ÖZETİ

| Kaynak | Gözlem | Statü |
|---|---|---|
| Metro mağaza fotoğrafı (benchmark) | 2 | FACT (fiyat) |
| Online uzman perakende — ithal | 20 | FACT |
| Online uzman perakende — yerli | 25 | FACT |
| Metro yerli şarap (T5 medya) | 5 | UNKNOWN (modele giremez) |
| **TOPLAM** | **52** | |

**Kanal çeşitliliği zayıftır: 45/52 gözlem TEK bir online kanaldan gelir.**
Bu, segment bantlarının bu kanalın fiyatlama politikasıyla yanlı (biased) olma
riskini taşır.
