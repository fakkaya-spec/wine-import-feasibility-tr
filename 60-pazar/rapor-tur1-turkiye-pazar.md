# AJAN RAPORU — TÜRKİYE PAZAR KÂŞİFİ

```yaml
ajan:               turkiye-pazar-kasifi
tur:                TUR 1
tarih:              2026-08-09
durum:              SUBMITTED
```

---

## 1. YÖNETİCİ ÖZETİ

Birinci öncelik OQ-001'di ve **büyük ölçüde kapatıldı**: Metro Türkiye'nin kendi
resmî broşürlerinde (5–11 Ağustos 2026 ve 1–31 Ağustos 2026) **her fiyatın yanında
küçük puntoyla `KDV'li` yazmaktadır** (`EV-2026-08-09-503`, `EV-2026-08-09-504`);
Metro Türkiye bireysel müşteriye ücretsiz kartla açıktır (`EV-2026-08-09-505`);
ve Fiyat Etiketi Yönetmeliği toptan+perakende karma satış yapılan yerlerde perakende
hükümlerini uygular (`EV-2026-08-09-506`). Bu üçlü, **599,90 TL'nin KDV DAHİL bir
tüketici fiyatı olduğu** sonucunu yüksek güvenle destekler; ayrıca OQ-001'in kurucu
hipotezi olan *"Metro etiketinde KDV hariç + KDV dahil çiftli gösterim"* Metro
Türkiye materyalinde **bulunamamıştır** — etiketteki ikinci sayı KDV hariç fiyat
değil, **birim fiyattır** (`kg/L/adet fiyatı`).

Buna karşılık OQ-001 **tam kapanmadı**: fiyatın **promosyonlu mu normal mi** olduğu
`UNKNOWN` kaldı (`T-504`, CRITICAL) ve **zincir market tüketici fiyatı** hiç
gözlemlenemedi — çünkü Türkiye'de alkol tüketiciye internetten satılamaz ve reklamı
yasaktır; Metro'nun 58 sayfalık broşür setinde **tek bir alkollü içki bile yoktur**
(`EV-2026-08-09-514`).

En çarpıcı ikinci bulgu: incelenen online uzman şarap perakendecisinde **400–800 TL
bandında stokta tek bir ithal şarap yoktur** (en ucuz stokta ithal: 875 TL,
`EV-2026-08-09-509`); bu bandı **yalnızca yerli üretici** doldurmaktadır
(600–800 TL'de 25 yerli SKU, `EV-2026-08-09-510`). Yani benchmark bandında asıl
rakip ithal değil **yerli şaraptır**.

Toplam **52 raf/online fiyat gözlemi** kaydedildi, **15 kanıt kartı** açıldı
(`EV-2026-08-09-501` … `-515`), **6 ticket** (`T-501`…`T-506`) ve **3 çelişki**
(`C-501`…`C-503`) açıldı. **Türkiye şarap ithalat hacmi resmî kaynaktan
DOĞRULANAMADI** (`EV-2026-08-09-515`) — bu turun en büyük UNKNOWN'ıdır.

---

## 2. BULGULAR

### B-1: Metro Türkiye'nin ilan ettiği fiyat KDV DAHİL fiyattır

```yaml
claim:          Metro Turkiye'nin musteriye ilan ettigi raf/brosur fiyati KDV DAHIL fiyattir
value:          "KDV'li"
unit:           -
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-503, EV-2026-08-09-504
effective_date: 2026-08-05
katman:         L8
```

**Gerekçe:** Metro Türkiye'nin künyeli, süreli yayın statüsündeki iki resmî broşürünün
tamamı (8 + 2 sayfa, yüksek çözünürlükte görüntülenip okundu) her fiyat kutusunda
`<tam>,<kuruş> TL` ibaresinin altında küçük puntoyla **`KDV'li`** yazmaktadır.
Örnekler: `1.099,90 TL KDV'li`, `299,90 TL KDV'li`, `434,90 TL KDV'li`.
**58 sayfada tek bir `KDV hariç` ibaresi yoktur.**

---

### B-2: Metro etiketinde KDV hariç/dahil ÇİFTLİ gösterim yoktur — ikinci sayı BİRİM FİYATTIR

```yaml
claim:          Metro etiketindeki ikinci sayi KDV haric fiyat degil, birim fiyattir
value:          "kg fiyati: 599,80 TL / L fiyati: 90,20 TL / adet fiyati: 12,42 TL"
unit:           TRY
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-503, EV-2026-08-09-504
effective_date: 2026-08-01
katman:         L8
```

**Gerekçe:** Metro fiyat kutusu anatomisi: (1) promosyonda üstü çizili eski fiyat
(`KDV'li`), (2) büyük punto güncel fiyat (`KDV'li`), (3) küçük punto birim fiyat,
(4) promosyonda kırmızı "AVANTAJLI FİYAT" rozeti.
**Bu, OQ-001'in kurucu hipotezini kısmen çürütür.**
750 ml şişede birim fiyat satırı `L fiyatı: ~799,87 TL` olurdu — `599,90` ile
karıştırılması pratikte mümkün değildir.

---

### B-3: Metro Türkiye son tüketiciye açıktır → fiyat L8'dir (ama Metro'nun L8'i)

```yaml
claim:          Metro Turkiye'den herkes alisveris yapabilir; raf fiyati fiilen bir tuketici fiyatidir
value:          "Herkes! ... bireysel musterilerimiz magaza girislerinden gunluk kart cikarttiktan sonra ..."
unit:           -
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-505
effective_date: UNKNOWN
katman:         L8 (L8_METRO_CASH_CARRY)
```

**Gerekçe:** Metro Türkiye SSS'sinin kendi ifadesi. Belge gerekmez, kart ücretsizdir.
**Ancak:** Bu, zincir market L8'i değildir. Aynı fiyat bir bakkal/restoran için
**L7-proxy** işlevi görür. `L8_CHAIN_RETAIL` ayrı bir alan olarak `UNKNOWN` kalmalıdır.

---

### B-4: 400–800 TL bandında stokta ithal şarap YOK; bandı yerli üretici dolduruyor

```yaml
claim:          Online uzman perakendede stokta en ucuz ithal sarap 875 TL; 400-800 TL bandinda 0 ithal SKU, 600-800 TL bandinda 25 yerli SKU
value:          875 (ithal min) / 460 (yerli min) / 25 (yerli SKU 600-800 TL)
unit:           TRY, adet
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-509, EV-2026-08-09-510
effective_date: 2026-08-09
katman:         L8
```

**Gerekçe:** 474 stokta SKU'nun tamamı ürün feed'inden çekildi ve fiyata göre
bantlandı. Stokta olmayan 349 ithal listelemede gerçeklik dışı eski fiyatlar
bulunduğu için dışlandı (`C-501`).

**Bu bulgunun anlamı:** İthal edeceğimiz ürün, fiyat/performans bandında
**ÖTV/gümrük yükü taşımayan yerli üreticilerle** yarışacaktır
(Asmadan 649 · KA Winery 655 · Umurbey 659 · Nif Bağları 670 · Vinkara 710–780 ·
Turasan 758 · Çamlıbağ 760 · Diren 790 · Büyülübağ 792 TL).

---

### B-5: Metro'da mağaza fiyatı ≠ sevkiyat (HoReCa teslimat) fiyatı

```yaml
claim:          Metro brosur/magaza fiyatlari sevkiyat hizmeti alan musterilere uygulanmaz
value:          "Brosurdeki fiyatlar sevkiyat hizmeti alan musterilerimiz icin gecerli degildir"
unit:           -
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-507
effective_date: 2026-08-05
katman:         L7/L8 ayrimi
```

**Gerekçe:** Metro'nun kendi broşür künyesi. Metro içinde en az **iki fiyat rejimi**
vardır. Fark ölçülmedi — `kanal-marj-uzmani`'nın alanı (`T-506`).

---

### B-6: Alkol, Türkiye'de broşür/online fiyat keşfine kapalıdır

```yaml
claim:          Incelenen 58 sayfalik Metro brosur setinde 0 alkollu icki SKU'su vardir; alkol Metro kampanyalarinin da disindadir
value:          0
unit:           adet
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-514, EV-2026-08-09-508
effective_date: 2026-07-08
katman:         -
```

**Gerekçe:** 48 sayfalık "İçecek Trendleri ve Çözümleri" katalogu dahil, hiçbir
Metro yayınında alkollü içki yok. Ayrıca kampanya koşullarında alkol açıkça
hariç tutuluyor. Hukuki dayanak `mevzuat-ruhsat-uzmani`'nın alanıdır (`T-503`).

---

### B-7: Türkiye şarap ithalat hacmi — DOĞRULANAMADI

```yaml
claim:          Turkiye sarap ithalat hacmi, degeri, mensei kirilimi ve trendi
value:          null
unit:           litre / USD
status:         UNKNOWN
tier:           T2 (erisilemedi)
evidence_id:    EV-2026-08-09-515
effective_date: -
katman:         -
```

**Gerekçe:** TADAB'ın *Resmî İstatistikler* sayfası 2011–2026 arası **yalnızca yakıt
biyoetanolü** dönem raporları yayınlıyor. Ticaret Bakanlığı sektör PDF'i, TÜİK ve
mevzuat.gov.tr bu oturumda HTTP 503 döndü. **Uydurma yapılmadı.**

---

### B-8: Benchmark'ın menşeleri (ABD, Avustralya) uzman kanalda hiç temsil edilmiyor

```yaml
claim:          Incelenen online uzman perakendecinin ulke koleksiyonlarinda ABD ve Avustralya YOK
value:          "Fransa 33, Italya 30, Ispanya 6, Avusturya 4, Sili 2, Arjantin 2, Almanya 2; ABD 0, Avustralya 0"
unit:           adet
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-09-509
effective_date: 2026-08-09
katman:         L8
```

**Gerekçe:** Koleksiyon feed'lerinden sayıldı. Metro'nun bu iki SKU'yu kendi
ithalatıyla getiriyor olma ihtimalini gündeme getirir — **doğrulanmadı** (`OQ-503`).

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | Benchmark **promosyonlu mu, normal fiyat mı** | Tek gözlem; etiketin rozet/üstü çizili satırı bilinmiyor | **CRITICAL** | 2–4 hafta sonra ikinci gözlem (`T-504`) |
| 2 | Şarap reyonundaki **fiziksel etiketin** tam mizanpajı | Kanıt broşürden; broşür ≠ raf etiketi | **CRITICAL** | Etiketin küçük punto satırı dahil fotoğrafı (`T-504`) |
| 3 | **Zincir market tüketici raf fiyatı** (gerçek L8) | Alkol online satılamıyor; Migros/CarrefourSA'da fiyat yok | HIGH | Fiziksel mağaza turu (`OQ-502`) |
| 4 | **Türkiye şarap ithalat hacmi / menşe kırılımı / trend** | TADAB alkol istatistiği yayınlamıyor; diğer kaynaklar 503 | HIGH | TÜİK GTİP 2204 sorgusu, TADAB bilgi edinme (`T-505`) |
| 5 | **İthalatçı/distribütör haritası** (kim hangi markayı getiriyor) | Kamuya açık liste bulunamadı; yalnızca Diageo doğrulandı | HIGH | Şişe arka etiketi gözlemi + TADAB belge sahipleri (`T-505`) |
| 6 | **Gold Country / Central Creek ithalatçısı** | Hiçbir kaynakta yok | MEDIUM | Şişe arka etiketi (`OQ-503`) |
| 7 | **HoReCa fiyat yapısı ve hacim payı** | Hiç gözlem alınamadı | HIGH | Restoran şarap listesi örneklemi |
| 8 | **Tekel bayii / bağımsız perakende** fiyatları | Fiyat listesi yayınlanmıyor | HIGH | Fiziksel gözlem (`OQ-502`) |
| 9 | **BİM/A101/Şok'ta şarap var mı** | İncelenmedi | MEDIUM | Fiziksel gözlem |
| 10 | Benchmark SKU'ların **ABV, vintage (Central Creek), mağaza, şehir** | Fotoğrafta yok | MEDIUM | İkinci gözlem |
| 11 | Metro'da **üyeliğe özel fiyat** var mı | `guncelfiyatlar.metro-tr.com` giriş istiyor | MEDIUM | Metro Kart ile giriş |
| 12 | Bizim Toptan (rakip cash&carry) şarap fiyatları | İncelenmedi | MEDIUM | Fiziksel/online gözlem |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-501** | iyisarap.plus stokta SKU'lar (T4 / 2026-08-09): ithal min **875 TL** | Aynı feed, stokta olmayan SKU'lar (T4 / aynı tarih): **70–450 TL** ithal fiyatlar | Aynı sitede 10 kata varan fark; stokta olmayan kayıtlar güncellenmemiş olabilir ama `updated_at` yeni görünüyor | **OPEN** |
| **C-502** | Metro broşürleri (T4 / 2026-08): fiyatlar **`KDV'li`** | Metro kampanya koşulları (T4 / 2026): *"Alım hedeflerinize **KDV dahil değildir**"* | Aynı şirket bir yerde brüt bir yerde net konuşuyor | **OPEN (izleme)** — muhtemelen gerçek çelişki değil (etiket brüt / hedef net) |
| **C-503** | T5 medya (Ocak 2026): Metro'da Doluca 75cl **630 TL** | Online uzman perakende (T4 / Ağustos 2026): benzer segment **649–800 TL** | A kaynağı T5 ve üç site aynı tabloyu kopyalamış; bağımsız doğrulama değil | **OPEN** |

Ayrıntı: `99-ops/_parts/celiskiler-turkiye-pazar-kasifi.md`

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| `pazar.yaml` | `benchmark_1.fiyat` | 599.90 | TRY | FACT | `EV-2026-08-09-501` |
| `pazar.yaml` | `benchmark_1.kdv_durumu` | `KDV_DAHIL` | - | **ESTIMATE (HIGH)** | `EV-2026-08-09-503/504/505/506` |
| `pazar.yaml` | `benchmark_1.katman` | `L8_METRO_CASH_CARRY` | - | ESTIMATE | `EV-2026-08-09-505/507` |
| `pazar.yaml` | `benchmark_1.promosyon` | `null` | - | **UNKNOWN** | — (`T-504`) |
| `pazar.yaml` | `benchmark_2.fiyat` | 649.90 | TRY | FACT | `EV-2026-08-09-502` |
| `pazar.yaml` | `benchmark_2.kdv_durumu` | `KDV_DAHIL` | - | ESTIMATE (HIGH) | `EV-2026-08-09-503/504` |
| `pazar.yaml` | `segment.fiyat_performans_alt` | 600 | TRY | ESTIMATE | `EV-2026-08-09-509/510` |
| `pazar.yaml` | `segment.fiyat_performans_ust` | 900 | TRY | ESTIMATE | `EV-2026-08-09-509/510` |
| `pazar.yaml` | `ithal_min_stokta_uzman_kanal` | 875.00 | TRY | FACT | `EV-2026-08-09-509` |
| `pazar.yaml` | `yerli_rakip_sku_600_800` | 25 | adet | FACT | `EV-2026-08-09-510` |
| `pazar.yaml` | `ithal_sku_400_800_uzman_kanal` | 0 | adet | FACT | `EV-2026-08-09-509` |
| `pazar.yaml` | `l8_chain_retail` | `null` | TRY | **UNKNOWN** | — (`OQ-502`) |
| `pazar.yaml` | `ithalat_hacmi_litre` | `null` | litre | **UNKNOWN** | `EV-2026-08-09-515` |
| `pazar.yaml` | `ithal_pay_pct` | `null` | % | **UNKNOWN** | `EV-2026-08-09-515` |
| `pazar.yaml` | `horeca_fiyat_carpani` | `null` | x | **UNKNOWN** | — |
| `senaryolar.yaml` | `benchmark_senaryolari.BM_A` | BASE CASE | - | öneri | `EV-503/504/505/506` |
| `senaryolar.yaml` | `benchmark_senaryolari.BM_B` | SENSITIVITY | - | öneri | — |
| `senaryolar.yaml` | `benchmark_senaryolari.BM_C` (promosyon) | YENİ | - | öneri | `T-504` |
| `senaryolar.yaml` | `benchmark_senaryolari.BM_D` (zincir L8 farkı) | YENİ | - | öneri | `EV-507` |

**evidence_id'si olmayan satır modele giremez.**
`EV-2026-08-09-512` (T5 Metro şarap listesi) **modele giremez** — sadece bant işaretidir.

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `kanal-marj-uzmani` | Metro mağaza fiyatı ≠ sevkiyat (HoReCa) fiyatı (`EV-507`) | "Metro'ya tek fiyat verilir" varsayımını kırar |
| `kanal-marj-uzmani` | Alkol, Metro'nun tüm çek/sadakat kampanyalarının dışında (`EV-508`) | Ciro primi mekaniği şarapta çalışmayabilir |
| `kanal-marj-uzmani` | Metro'nun ticari dili KDV hariç, etiket dili KDV dahil (`EV-503` vs `EV-508`) | Pazarlıkta matrah karışıklığı riski |
| `kanal-marj-uzmani` | Metro 599,90 vs uzman perakende min 875 TL — %46 fark (hesaplamadım) | Kanal marjı mı, segment farkı mı? |
| `mevzuat-ruhsat-uzmani` | Metro'nun 58 sayfalık broşüründe 0 alkol SKU'su (`EV-514`) | Reklam yasağı, lansman araçlarını belirler |
| `mevzuat-ruhsat-uzmani` | Fiyat Etiketi Yönetmeliği "toptan+perakende birlikte" hükmü T1 doğrulaması bekliyor (`EV-506`) | OQ-001'in hukuki ayağı |
| `mevzuat-ruhsat-uzmani` | TADAB istatistik sayfası alkol verisi yayınlamıyor (`EV-515`) | Pazar hacmi kaynağı arayışı |
| `global-sourcing-kasifi` | ABD/Avustralya menşe, Türkiye uzman kanalında hiç yok (`EV-509`) | Fırsat mı, tüketici tanıdıklığı yokluğu mu? |
| `global-sourcing-kasifi` | 600–800 TL bandında rakip **yerli** (`EV-510`) | Hedef EXW/FOB'u sertçe aşağı çeker |
| `gumruk-vergi-uzmani` | Metro künyesi: "vergi değişiklikleri fiyatlara aynen yansıtılacaktır" (`EV-507`) | Kanal ÖTV artışını yutmuyor |
| `yatirim-komitesi-baskani` | `00-charter/benchmark.md` güncelleme önerisi (İP-515) | Benchmark alanlarının doldurulması |

Tam liste: `99-ops/_parts/capraz-ipuclari-turkiye-pazar-kasifi.md`

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| `T-501` | `mevzuat-ruhsat-uzmani` | Fiyat Etiketi Yönetmeliği'nin cash&carry'yi kapsadığı T1 doğrulaması | HIGH | OPEN |
| `T-502` | `mevzuat-ruhsat-uzmani` | Online alkol satış yasağının kapsamı; fiyat gösterimi de yasak mı | MEDIUM | OPEN |
| `T-503` | `mevzuat-ruhsat-uzmani` | Alkol reklam yasağı hangi pazarlama araçlarını bırakıyor | MEDIUM | OPEN |
| `T-504` | `yatirim-komitesi-baskani` | OQ-001 promosyon ayağı: ikinci mağaza gözlemi + etiket fotoğrafı gerekli | **CRITICAL** | OPEN |
| `T-505` | `mevzuat-ruhsat-uzmani` | TADAB/TÜİK'ten ithalat hacmi ve ithalatçı listesi | HIGH | OPEN |
| `T-506` | `kanal-marj-uzmani` | Metro mağaza/sevkiyat fiyat rejimi farkı + alkolde kampanya dışılık | HIGH | OPEN |

**Kapanan ticket yok** (TUR 1'de bu ajan tarafından açılan ilk ticket'lar).

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-09-501` | 30d | 2026-09-08 |
| `EV-2026-08-09-502` | 30d | 2026-09-08 |
| `EV-2026-08-09-503` | 30d | 2026-09-08 |
| `EV-2026-08-09-504` | 30d | 2026-09-08 |
| `EV-2026-08-09-505` | 180d | 2027-02-05 |
| `EV-2026-08-09-506` | 180d | 2027-02-05 |
| `EV-2026-08-09-507` | 30d | 2026-09-08 |
| `EV-2026-08-09-508` | 90d | 2026-11-07 |
| `EV-2026-08-09-509` | 30d | 2026-09-08 |
| `EV-2026-08-09-510` | 30d | 2026-09-08 |
| `EV-2026-08-09-511` | 30d | 2026-09-08 |
| `EV-2026-08-09-512` | 30d | 2026-09-08 |
| `EV-2026-08-09-513` | 180d | 2027-02-05 |
| `EV-2026-08-09-514` | 90d | 2026-11-07 |
| `EV-2026-08-09-515` | 90d | 2026-11-07 |

**Uyarı:** Raf fiyatı gözlemlerinin tamamı 30 gün sonra STALE olur.
Metro haftalık broşürü **7 günde bir** değişir — `EV-503`/`EV-507` fiilen
7 gün sonra eskimiş sayılmalıdır (broşür dönemi 5–11 Ağustos 2026).

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Şarap reyonundaki fiziksel raf etiketinin, Metro broşüründen FARKLI bir formatta
olduğunu gösteren tek bir fotoğraf.**

Bütün KDV sonucum, Metro'nun **broşür** fiyat gösteriminden raf etiketine yapılan
bir **çıkarıma** dayanıyor. Broşür `KDV'li` diyor — bu kesin. Ama raf etiketinin de
`KDV'li` dediğini **görmedim**. Eğer Metro alkol reyonunda (reklam yasağı nedeniyle
broşürde hiç yer almayan bir kategori) farklı bir etiket şablonu kullanıyorsa,
sonucum çöker.

İkinci bir çürütücü: **benchmark'ın promosyonlu olduğunun ortaya çıkması.**
Bu durumda 599,90 TL bir "pazar fiyatı" değil, geçici bir stok eritme fiyatıdır ve
ters model imkânsız bir hedefe kurulmuş olur.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"Broşür fiyat formatı = raf etiketi fiyat formatı" varsayımı.**

Kırılgan çünkü: (a) broşür bir pazarlama materyalidir, raf etiketi bir hukuki
belgedir; (b) alkol broşürde hiç yer almadığı için tam da ilgilendiğim kategoride
sıfır broşür kanıtım var; (c) mağazalarda hem kâğıt hem elektronik raf etiketi (ESL)
kullanılıyor olabilir ve formatları farklı olabilir.

İkinci kırılgan varsayım: **`available: true` filtresinin doğru filtre olduğu.**
`EV-509`'daki "400–800 TL'de ithal şarap yok" sonucum tamamen bu filtreye dayanıyor.
Filtre yanlışsa (`C-501`), o bandda ithal şarap **vardır** ve segment resmi değişir.

### 9.3 Hangi kaynağıma en az güveniyorum?

Üç sıralı:

1. **`EV-2026-08-09-512`** (T5 medya Metro şarap fiyat listesi) — üç site aynı tabloyu
   kopyalamış, birincil kaynak yok, tarih Ocak 2026. Zaten `UNKNOWN` işaretledim ve
   modele girmesini yasakladım. **Buna hiç güvenmiyorum.**
2. **`EV-2026-08-09-509` / `-510`** (iyisarap.plus feed'i) — tek bir ticari sitenin
   fiyatlama politikasını "Türkiye pazarı" sanma riski var. 52 gözlemin 45'i buradan
   geliyor. Ayrıca sitenin online alkol satış yasağı karşısındaki hukuki statüsü
   belirsiz (`T-502`) — yasal değilse fiyatları pazar temsilcisi sayılmamalı.
3. **`EV-2026-08-09-506`** (Fiyat Etiketi Yönetmeliği) — T1 diye işaretledim ama
   Resmî Gazete'ye erişemedim, ikincil bir hukuk veritabanından okudum, madde
   numaralarını birebir doğrulamadım. Bu, kendi tier kuralımın sınırında bir kayıttır
   ve `T-501` ile doğrulatılmalıdır.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

- **KDV dahil sonucu yanlışsa (aslında KDV hariçse):** Benchmark'ın tüketici karşılığı
  KDV oranı kadar **yukarı** kayar. Bu, ters modelde tedarikçiye ödeyebileceğimiz
  maksimum EXW/FOB'u **artırır** → proje **daha kolay** görünür. Yani hatam
  **muhafazakâr yöndedir**; yanlış çıkarsa proje lehine sürpriz olur.
- **Benchmark promosyonluysa:** Normal fiyat daha yüksektir → yine proje lehine.
  **Ama** eğer benchmark aslında bir **stok eritme** fiyatıysa ve o SKU pazardan
  çekiliyorsa, "bu bandda talep var" varsayımı çöker → **KILL yönünde** etki.
- **"400–800 TL'de ithal yok" bulgusu yanlışsa:** Bandda ithal rekabet vardır,
  fiyat baskısı sandığımdan yüksektir → hedef EXW/FOB düşer → **KILL yönünde**.
- **İthalat hacmi çok küçük çıkarsa** (halen UNKNOWN): 50.000–100.000 şişe/yıl
  ölçek hedefi anlamsızlaşır → `SCALE` kararı elenir, en fazla `TEST` kalır.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre | Maliyet |
|---|---|---|---|---|---|
| 1 | Benchmark etiketinin tam fotoğrafı + mağaza/şehir + arka etiket ithalatçı satırı | İnsan gözlemci (fotoğrafı çeken kişi) | Metro ziyareti, 15 dk | 1 gün | ~0 |
| 2 | İkinci fiyat gözlemi (promosyon testi) | Aynı kişi | 2–4 hafta sonra aynı SKU | 4 hafta | ~0 |
| 3 | Kasa fişi | Aynı kişi | 1 şişe satın alma | 1 gün | ~600 TL |
| 4 | Zincir market + tekel bayii fiyat turu (`OQ-502`) | İnsan gözlemci | İstanbul'da 1 gün, 5 nokta, 600–1.200 TL bandındaki tüm SKU'lar | 1 gün | ulaşım |
| 5 | İthalat hacmi (`T-505`) | `mevzuat-ruhsat-uzmani` | TÜİK GTİP 2204 sorgusu / TADAB bilgi edinme başvurusu | 1–15 gün | ~0 |
| 6 | Fiyat Etiketi Yönetmeliği T1 doğrulaması (`T-501`) | `mevzuat-ruhsat-uzmani` | Resmî Gazete / mevzuat.gov.tr erişimi | 1 gün | ~0 |
| 7 | HoReCa fiyat çarpanı | `turkiye-pazar-kasifi` (TUR 2) | 10 restoran şarap listesi örneklemi | 1 gün | ~0 |

**Not:** 1, 2, 3 ve 4 numaralı maddelerin tamamı **tek bir insan tarafından, iki mağaza
ziyaretiyle, yaklaşık 600 TL maliyetle** yapılabilir. OQ-001'in tamamen kapanması
için gereken şey pahalı değil — sadece **fiziksel**.
