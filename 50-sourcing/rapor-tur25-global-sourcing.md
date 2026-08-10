# AJAN RAPORU — GLOBAL SOURCING KÂŞİFİ · TUR 2.5

```yaml
ajan:               global-sourcing-kasifi
tur:                TUR 2.5 — RFQ NEGOTIATION CARDS
tarih:              2026-08-10
durum:              SUBMITTED
yeni_arastirma:     YOK — yeni tedarikci/ulke/fiyat arastirmasi YAPILMADI
web_arama:          YOK — WebSearch/WebFetch kullanilmadi
dis_iletisim:       NONE — hicbir ureticiye e-posta/form/mesaj GONDERILMEDI
yeni_evidence:      YOK — 10-evidence/ acilmadi, index.csv'ye dokunulmadi
yazilan_dosyalar:   50-sourcing/rfq-negotiation-cards.md
                    50-sourcing/rapor-tur25-global-sourcing.md
                    99-ops/tickets/T-871.md, T-872.md, T-873.md
```

---

## 1. YÖNETİCİ ÖZETİ

TUR 2 shortlist'indeki **10 RFQ hedefinin her biri için** bir pazarlık kartı
üretildi (`50-sourcing/rfq-negotiation-cards.md`). Kartlar, `finans-fizibilite`'nin
ters modelinden gelen **`MAXIMUM STRUCTURAL BUY PRICE`**'ı — 799 TL hedef raf
fiyatı, CHAIN RETAIL kanalı, 5.000 şişe, λ=1, ithalatçı katkı payı 0 varsayımıyla
**272,83 TRY/şişe (tercihli menşe)** ve **240,73 TRY/şişe (tercihsiz menşe /
belge düşerse)** — her tedarikçinin menşe grubuna bağlar.
`TARGET` / `ACCEPTABLE` / `WALK-AWAY` fiyatları **üretilmemiştir**; `OQ-901`
açık olduğu için `TARGET_DISCOUNT_FROM_MAX` ve `REQUIRED_IMPORTER_MARGIN`
alanları `INVESTOR_DECISION_REQUIRED` bırakılmıştır (`T-851` disiplini korundu).

**En kritik tek bulgu:** 10 kartın 10'unda **`MAX_FOB` ve `MAX_EXW` `UNKNOWN`**
— yani üreticiyle **fiilen konuşulacak iki katmanda hiçbir tavanımız yok**.
Elimizdeki tavan **CIF ve TL cinsindendir**; tedarikçi ise **EXW/FOB, EUR/USD**
verecektir. Köprü tek bir tarihli kur kaydıdır (`T-852`, `T-912`).

**İkinci bulgu:** ters model **9 ülke için 9 sayı üretmiyor, 2 sayı üretiyor**.
Bu nedenle kartlarda ülkeye özgü sahte hassasiyet yaratılmadı; menşe farkı
**pazarlık kalemine** dönüştürüldü (`ORIGIN DOCUMENT COMMITMENT`, OD-1…OD-5),
değeri **32,10 TRY/şişe**.

---

## 2. BULGULAR

### B-1: 10 kart tek bir ortak çapa setine bağlandı

```yaml
claim:          "10 RFQ hedefinin tamami ayni hedef raf fiyati, ayni kanal ve
                 ayni iki hacim kosesinden turetilmis pazarlik kartina sahiptir."
value:          10 kart / 1 capa seti
unit:           adet
status:         ASSUMPTION            # capa bir INVESTOR_ASSUMPTION'a dayanir
tier:           -
evidence_id:    -                     # tureti belge: 80-model/outputs/reverse-price-model.md
katman:         L2 (CIF Turkiye)
```

**Gerekçe:** `rfq-template.md` §0.8 bağlayıcıdır — aynı metin herkese gider,
yoksa teklifler karşılaştırılamaz. Aynı disiplin pazarlık çapası için de
uygulandı. Çapa (**799 TL / CHAIN RETAIL / 5.000 ve 25.000 şişe**)
`sweet-spot-analizi.md` §3.1'in **`PRIMARY` önerisidir, bir karar değildir** →
`T-871` ile başkana taşındı.

**Varsayım gerekçesi:** Alternatif, her kart için farklı bir basamak seçmekti;
bu, teklifleri karşılaştırılamaz kılar ve **seçimin gerekçesi de olmazdı**.
Duyarlılık: her ±100 TL hedef = ∓41,67 TRY/şişe tavan; 599↔999 arası bant
**±83,33 TRY/şişe**.

---

### B-2: `MAXIMUM STRUCTURAL BUY PRICE` yalnızca iki değer alır

```yaml
claim:          "10 tedarikcinin 10'unda azami yapisal alim fiyati sadece iki
                 degerden birini alir: tercihli menside 272,83, tercihsizde 240,73."
value:          272,83 / 240,73
unit:           TRY/sise
status:         TARGET / MODEL_DERIVED / UPPER_BOUND    # FACT DEGIL, QUOTE DEGIL
tier:           -
evidence_id:    tureti: reverse-price-model.md §9.1 + country-buying-ceilings.csv
katman:         L2 (CIF Turkiye)
```

**Türetme zinciri:** `finans-fizibilite` → `L8 799 TL (KDV dahil)` → R1…R7d →
`cif_try_max_UPPER_BOUND`. Menşe zincire **yalnızca `(1+g)` böleni** üzerinden
girer; ÖTV ve KDV menşeden bağımsızdır (`EV-2026-08-09-110`).
`MAX_CIF(g=0,70)/MAX_CIF(g=0,50) = 1,50/1,70 = 0,88235` → **tam −%11,765**.

**Bu benim türetmem değildir; alıntıdır.** Benim katkım bu iki değeri
`mense-tarife-eslemesi.md` §1 üzerinden **tedarikçi kartlarına eşlemektir.**

| Grup | Kartlar | `g` |
|---|---|---|
| **P** — tercihli **KOŞULLU** | 2 Danese (IT) · 3 Interbrosa (ES) · 4 TWF (FR) · 5 Corta Hojas (CL) · 6 San Valero (ES) · 7 Casa Santos Lima (PT) · 8 Vidigal (PT) · 9 Plaimont (FR) | %50 |
| **N** — tercihsiz | 1 Harland (AU) · 10 Purcari (**MD**) | %70 |
| **N→P kaldıracı** | 10 Purcari — **RO/BG tesisleri AB üyesi, %50** | değişken |

---

### B-3: Menşe belgesi bir pazarlık kalemine dönüştürüldü (OD-1…OD-5)

```yaml
claim:          "Tarife orani pazarlik konusu degildir; belgenin duzenlenebilirligi
                 pazarlik konusudur ve degeri 32,10 TRY/sise'dir."
value:          32,10
unit:           TRY/sise (799/CHAIN/BASE/5.000)
status:         TARGET / MODEL_DERIVED
tier:           -
evidence_id:    tureti: reverse-price-model.md §4.3 + mense-tarife-eslemesi.md §3.1, §5
katman:         L2
```

**Gerekçe:** `mense-tarife-eslemesi.md` §5 açıkça devretmiştir:
*"Tarife menşe seviyesindedir. Ancak K3 (geçerli belge) ve K2 (menşe kuralı)
tedarikçiye bağlıdır."* Kartlarda beş maddelik standart set üretildi:

| Kod | Talep |
|---|---|
| **OD-1** | Her sevkiyatta EUR.1 **veya** fatura beyanı — **sözleşme taahhüdü** |
| **OD-2** | "Onaylanmış ihracatçı" statüsü / fatura beyanı değer eşiği |
| **OD-3** | Şarap tamamen menşe ülkede üretildi/şişelendi mi — **dökme ithal bileşen var mı** |
| **OD-4** | Sevkiyat hangi limandan **çıkacak** — çıkış ülkesi kontrolü |
| **OD-5** | Belge düşerse **koşullu fiyat düzeltme maddesi** |

**OD-3 private label'da yüksek risklidir** ve bu, `mense-tarife-eslemesi.md`
§3.1 K2'nin doğrudan sonucudur: dökme ithal şarabın başka ülkede şişelenmesi
menşei bozar. **Kartların 8'i private label veya private label ihtimali
taşıyan tedarikçilerdir.**
**OD-5 bir hukuki görüş değildir** → `T-872` ile `gumruk-vergi-uzmani`'na.

---

### B-4: Purcari — tarife dezavantajı gözlenen fiyat avantajını silmez, daraltır

```yaml
claim:          "Moldova STA'si 2204.21'i kapsamadigi icin Purcari %70 oder ve
                 azami alim fiyati 240,73'e iner; buna ragmen IMPLIED_BREAKEVEN
                 138,94 ile havuzun ikinci en genis nefes payidir."
value:          240,73 (MD) / 272,83 (RO-BG) ; IMPLIED_BREAKEVEN 138,94
unit:           TRY/sise ; USD/TRY
status:         TARGET / MODEL_DERIVED
tier:           -
evidence_id:    EV-2026-08-10-165 (oran, T1, gumruk-vergi) ; EV-2026-08-09-405 (gozlenen CIF, T3)
katman:         L2
```

**Gerekçe:** TUR 2'de Purcari *"Moldova Türkiye'ye en düşük L2 CIF menşeidir
(2,46 USD/lt)"* gerekçesiyle listeye alınmıştı. `gumruk-vergi-uzmani` bu
gerekçenin bir kısmını **geri almıştır** ve kart bunu **gizlememektedir**:
azami alım fiyatı 32,10 TRY/şişe daha düşüktür ve bu kayıp **koşulsuzdur**,
belge getirilerek geri alınamaz.

**Ama kart karşı tarafı da yazar:** `IMPLIED_BREAKEVEN_USDTRY` = **138,94**
(ES 142,93'ün hemen ardında) — çünkü gözlenen CIF de o kadar düşüktür.
**İki etkinin net sonucu ancak gerçek teklifle ölçülür.**

**Ve bir kaldıraç doğar:** aynı grubun **Romanya ve Bulgaristan tesisleri AB
üyesidir ve %50 öder.** *"Aynı ürünü RO/BG tesisinizden verebilir misiniz"*
sorusu **havuzdaki en yüksek getirili tek pazarlık sorusudur** (+32,10 TRY/şişe)
→ navlun tarafı `T-873`.

---

### B-5: Cantina Danese — private label modelinin sessiz varsayımı bu tedarikçide yanlış

```yaml
claim:          "RFQ hedef listesinin 2. sirasindaki private label tedarikcisi,
                 Turkiye'de KENDI markasiyla listelidir; munhasirlik/kanal
                 cakismasi riski kartta acikca yer almaktadir."
value:          "Danese Primitivo Puglia Black Label — 1.419,00 TL, stokta DEGIL,
                 ithalatci ic etiketi 'Midas' (kimlik UNKNOWN)"
unit:           TRY (L8, tek kanal listeleme fiyati)
status:         FACT (tek kanal gozlemi) / iliskinin canliligi UNKNOWN
tier:           T4
evidence_id:    EV-2026-08-10-564 (turkiye-pazar-kasifi) ; OBS-665 ; T-565
katman:         L8 (baska bir urun ve baska bir segment — bizim hedefimizle KIYASLANAMAZ)
```

**Gerekçe:** Bu bulgu `turkiye-pazar-kasifi`'ye aittir; ben yalnızca **sourcing
sonucunu** yazıyorum: private label modelinin *"tedarikçinin Türkiye'de markası
yok → çakışma yok"* varsayımı **bu tedarikçide geçersizdir.** Kart, üç somut
riski (münhasırlık talebi, aleyhimize referans fiyat, segment uyumsuzluğu)
listeler ve **hiçbirini doğrulanmış saymaz.**

⚠ **Kartta ayrıca yazılmıştır:** 1.419 TL bir **Primitivo Puglia "Black Label"**
fiyatıdır; bizim 799 TL beyaz hedefimizle **aynı ürün değildir** ve
karşılaştırma **kurulmamıştır**.

---

### B-6: Havuzdaki tek yayınlanmış fiyat, tavanla karşılaştırılamaz

```yaml
claim:          "Harland'in '$2.85+ per bottle' gosterge fiyati, ters model
                 tavaniyla UC bagimsiz nedenle karsilastirilamaz."
value:          "2,85+ / 5,00+ / 8,50+"
unit:           UNKNOWN para birimi (kaynakta yalnizca '$')
status:         PUBLIC_INDICATIVE — teklif DEGIL
tier:           T4
evidence_id:    EV-2026-08-10-451
katman:         L0 VEYA L1 — BELIRSIZ (C-461)
```

**Üç engel:** (1) para birimi `UNKNOWN` (AUD/USD farkı ~1,5 kat),
(2) katman `UNKNOWN` — MOQ siparişinde *ex factory (L0)*, tam konteynerde
*FOB (L1)*; **aynı sayı iki katmana işaret ediyor**, (3) tavanımız **TL**,
kur **yok**.

> **"2,85 < 240,73" cümlesi kurulamaz ve `rfq-negotiation-cards.md`'de
> hiçbir yerde kurulmamıştır.** CLAUDE.md §9 (EXW/FOB/CIF karıştırılamaz)
> burada birebir uygulanmıştır.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | **`MAX_FOB` — 10 kartın 10'unda** | Navlun **USD**, `fx` `null` | **CRITICAL** | Tek tarihli kur kaydı (`T-852`, `T-912`) — sonra tek adımda açılır |
| 2 | **`MAX_EXW` — 10 kartın 10'unda** | Menşe local charge **EUR**, `fx` `null`; ayrıca 9 menşenin 8'inde **tutar da** `UNKNOWN` (`T-312`) | **CRITICAL** | fx + menşe local charge |
| 3 | **Gerçek EXW/FOB tedarikçi fiyatı — 10/10** | Hiçbir tedarikçiden teklif alınmadı; **dış iletişim bu turda yasak** | **CRITICAL** | Gerçek RFQ (TUR 7), başkan onayıyla (`T-466`) |
| 4 | `TARGET` / `ACCEPTABLE` / `WALK-AWAY` fiyatı | Yatırımcı eşiği yok | **CRITICAL** | `OQ-901` → `T-851` |
| 5 | **MOQ — 5 kartta** (Corta Hojas, San Valero, Casa Santos Lima, Vidigal, Plaimont, Purcari) | Hiçbiri yayınlamıyor | HIGH | RFQ 3.6a/3.6b |
| 6 | Harland fiyatının **para birimi** ve **katmanı** | Kaynakta yazılı değil (`C-461`) | HIGH | RFQ tek soruyla |
| 7 | **Ödeme şartı — 9 kartta** | Yalnızca Harland yayınlamış (%50+%50 sevkiyat öncesi) | HIGH | RFQ 3.8–3.10; **KKDF sonucu `gumruk-vergi-uzmani`'nın** |
| 8 | **Lead time — 8 kartta** | Yalnızca Harland (~6 hafta) ve TWF (28–42 gün) | MEDIUM | RFQ 3.11 |
| 9 | Beyaz value portföyü (Danese, Vidigal, Purcari, Harland çeşit düzeyi) | Sitelerde yok | HIGH | RFQ 1.2/1.4/5.1 |
| 10 | Model A'da **münhasırlık şartı, hacim taahhüdü, fiyat tavanı** | Hiçbiri yayınlamıyor | HIGH | RFQ 5.4–5.7 |
| 11 | Private label kabiliyeti — San Valero (3. taraf yayın), Plaimont, Vidigal, Purcari | Firma kendi kanalında beyan etmiyor | MEDIUM | RFQ 4.1 |
| 12 | Türkiye'ye ihracat geçmişi — **26 kaydın hiçbirinde doğrulanmadı** | Firmalar yayınlamıyor | MEDIUM | RFQ 6.6 |
| 13 | RO/BG için gözlenen CIF birim değeri | Bu projede seri kullanılmadı | LOW | Comtrade yeniden okuması (**bu turda yapılmadı**) |
| 14 | Çapa basamağı ve kanal seçimi | Başkan kararı | HIGH | `T-871` |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

**Bu turda YENİ çelişki açılmamıştır.** Mevcut çelişkiler kartlara **taşınmıştır**:

| conflict_id | İçerik | Hangi kartta görünür | Durum |
|---|---|---|---|
| `C-461` | Harland fiyatı L0 mu L1 mi — aynı sayı iki katmana işaret ediyor | **Kart 1** — `quote_class` satırında açıkça | OPEN |
| `C-462` | MOQ'lar gerçekte 3× çıkarsa düşük-MOQ alternatifi 5→0 | Kart 1, 2 (pilotla uyumsuz), 3, 4 | OPEN |
| `C-401` | MOQ birimi (şişe mi konteyner mi) tedarikçiden tedarikçiye değişiyor | **Kart 5** — soru #1 doğrudan bunu kapatıyor | OPEN |
| `C-311` | FCL navlun bandı 4–5 kat | Kart 5, 10 (rota kararı) — **ama ters model tavanına etkisi SIFIR** | OPEN |
| `C-851` | L3 katmanının ikinci kez düşülmemesi | Kartlarda L3 **hiç kullanılmadı** | OPEN |

`99-ops/celiskiler.md` dosyasına **dokunulmamıştır** (bu turda yasak).

---

## 5. MODEL GİRDİLERİ

**Bu turda `80-model/inputs/*.yaml`'a HİÇBİR DEĞER YAZILMADI.**
`80-model/` yalnızca **okundu**.

`tedarikci.yaml` için hazır ama **henüz doldurulamayan** alanlar (hepsi gerçek
RFQ cevabıyla dolacak):

| YAML dosyası | Alan | Değer | status | evidence_id |
|---|---|---|---|---|
| `tedarikci.yaml` | `secili_tedarikci.exw_fiyat` | `null` | **UNKNOWN** | — (`T-466`) |
| `tedarikci.yaml` | `secili_tedarikci.fob_fiyat` | `null` | **UNKNOWN** | — |
| `tedarikci.yaml` | `secili_tedarikci.incoterm` | `null` | **UNKNOWN** | — |
| `tedarikci.yaml` | `secili_tedarikci.moq` | 3.000 / 3.600 / 6.000 (üç firmada bilinen) | **FACT** | `EV-2026-08-09-408`, `EV-2026-08-09-410`, `EV-2026-08-10-452`, `EV-2026-08-10-453` |
| `tedarikci.yaml` | `secili_tedarikci.odeme_sekli` | "peşin" — **n=1 gözlem** | **ASSUMPTION** | `EV-2026-08-10-452` |
| `tedarikci.yaml` | `secili_tedarikci.mense_belgesi_taahhudu` | `null` | **UNKNOWN** | — (OD-1, `T-872`) |
| `tedarikci.yaml` | `secili_tedarikci.uretim_suresi_gun` | 28–42 (TWF) | **FACT** | `EV-2026-08-09-410` |

**evidence_id'si olmayan satır modele giremez.** Yukarıdaki `null` satırlar
**bilinçli olarak `null`** bırakılmıştır.

---

## 6. ÇAPRAZ İPUÇLARI

`99-ops/capraz-ipuclari.md` bu turda **DOKUNULMAMIŞTIR** (yasak listesinde).
İpuçları ticket olarak açıldı ve kartlara işlendi:

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `gumruk-vergi-uzmani` | **OD-5** — belge düşerse koşullu fiyat düzeltme maddesi; sonradan ibraz / sonradan kontrol / geri ödeme yolları açık mı? | Açıksa OD-5 bir nakit maddesine iner; kapalıysa **pazarlıktaki en değerli tek madde** (`T-872`) |
| `gumruk-vergi-uzmani` | **Karışık menşeli tek konteyner** (Purcari MD+RO+BG) — tek sevkiyatta iki tarife oranı doğar mı? | Kart 10 soru #3'ün cevabı ham hâliyle iletilecek |
| `navlun-lojistik-uzmani` | Purcari MD/RO/BG **ayrı navlun**; Moldova denize kıyısı olmayan menşe; RO/BG rotası MD'den 32,10 TRY/şişe'den pahalıysa **menşe değiştirme kazancı negatife döner** | `T-873` |
| `navlun-lojistik-uzmani` | Şili — üçüncü ülkede konsolidasyon tercihi düşürür; **LCL avantajı 20 puanlık tarifeyi yakabilir** | Kart 5 OD ŞİLİ EKİ (`T-163`, `T-914`) |
| `kanal-marj-uzmani` | Model A'da marka sahibi **yeniden satış fiyatı tavanı / markup sınırı** dayatabilir — kanal marjı **dışarıdan kısıtlanır** | Kart 6, 7, 8, 9 soru #2 bunu ölçüyor |
| `turkiye-pazar-kasifi` | Danese'nin TR'deki `Midas` ilişkisi **canlı mı** — ürün stokta değil | `T-565`; Kart 2'nin münhasırlık riski buna bağlı |
| `mevzuat-ruhsat-uzmani` | Interbrosa'ya *"Türkçe arka etiketi menşede uygulayabiliyor musunuz"* soruluyor — **evet ise TR'deki etiketleme operasyonu (L5) tamamen kalkar** | Kart 3 soru #3 |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|---|---|---|---|---|
| **T-871** | `yatirim-komitesi-baskani` | RFQ pazarlık çapası hangi basamak + hangi kanal + `<VOLUME>` | **HIGH** | **OPEN** |
| **T-872** | `gumruk-vergi-uzmani` | OD-5 koşullu fiyat düzeltme maddesinin gümrük tarafındaki sonucu; sonradan ibraz/kontrol; fatura beyanı eşiği | MEDIUM | **OPEN** |
| **T-873** | `navlun-lojistik-uzmani` | Purcari MD/RO/BG yükleme noktası — üç menşe için ayrı navlun/rota | MEDIUM | **OPEN** |

**Kapanmaya aday (kapanış kararı başkanındır):**

| ticket_id | Neden aday |
|---|---|
| **T-161** | *"Menşe belgesi soruları RFQ'da sorulacak"* — `rfq-negotiation-cards.md` §0.6'da OD-1…OD-5 olarak **karşılandı**; `rfq-template.md` §6 zaten içeriyor |

`99-ops/tickets/INDEX.md`'ye **dokunulmamıştır** (yasak listesinde).

---

## 8. TAZELİK

**Bu turda yeni kanıt kartı açılmamıştır.** Kartlarda kullanılan mevcut
kanıtların tazeliği:

| evidence_id | ttl | STALE olacağı tarih | Kartlara etkisi |
|---|---|---|---|
| `EV-2026-08-10-451` / `-452` (Harland fiyat + MOQ) | 30d | 2026-09-09 | Kart 1'in tek fiyat çapası |
| `EV-2026-08-10-453` (Danese MOQ) | 30d | 2026-09-09 | Kart 2 |
| `EV-2026-08-09-408` (Interbrosa MOQ) | 30d | 2026-09-08 | ⚠ **Site 2026-08-10'da 503** — teyit edilemedi |
| `EV-2026-08-09-410` (TWF MOQ + üretim süresi) | 30d | 2026-09-08 | Kart 4 |
| `EV-2026-08-09-405` (gözlenen CIF birim değerleri) | — | — | `IMPLIED_BREAKEVEN`'in tek tabanı |
| `EV-2026-08-10-301…-311` (LCL kotasyonları) | **6d** | **2026-08-17** | Dolaylı — `MAX_CIF` üzerinde ±0,93 TL |
| `EV-2026-08-10-564` (Danese TR listelemesi) | — | — | Kart 2 münhasırlık riski |

> ⚠ **En kısa ömürlü bacak LCL kotasyonlarıdır (2026-08-17).** Kartlar üzerindeki
> etkisi küçüktür (±0,93 TRY/şişe) ama **`MAX_FOB` hesabı açıldığında bu
> değişir** — o zaman navlun doğrudan pazarlık kalemine girer.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR?

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Tek bir gerçek teklif (`FIRM_OFFER`).**
10 kartın 10'unda `quote_class` ya `NONE` ya da `PUBLIC_INDICATIVE`'dir.
Kartlar tamamen **model tarafında** durmaktadır: tavan var, teklif yok.
İlk gerçek teklif geldiği anda —

- eğer teklif **X'in (200,98 TRY/şişe CIF) çok altındaysa**, kartların tüm
  pazarlık kurgusu (MOQ indirimi, vade, etiket maliyeti) **ikincil** hale gelir;
- eğer **Y'nin (290,51 / 256,34) üstündeyse**, o tedarikçi düşer ve tavanın
  hangi kaleminin fazla iyimser olduğu (λ=1, 13 sıfır kalem) **asıl soru** olur.

**İkinci geçersizleştirici:** başkan çapa olarak 799/CHAIN dışında bir şey
seçerse (`T-871`) **10 kartın tüm rakamları birden değişir** — 599'da −83,33,
999'da +83,33 TRY/şişe.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**Hedef raf fiyatının 799 TL ve kanalın CHAIN RETAIL olması.**

İkisi de bir **karar değil, bir öneriye** dayanıyor — ve o önerinin dayandığı
katman (`L8_CHAIN_RETAIL`) Türkiye'de **hiç gözlenmemiştir** (`T-701`, `T-603`).
Yani pazarlık çapamın altında **sıfır gözlem** var.
`sweet-spot-analizi.md` bunu kendisi de yazıyor: *"Model, hangi basamağın
hangisine göre daha dayanıklı olduğunu söyleyebilir; hedef fiyatın Türkiye
tüketici rafında doğru olduğunu söyleyemez."*

**İkinci kırılgan varsayım:** 5.000 şişelik pilot hacmi.
Kart 1 (Harland, MOQ 6.000) ve Kart 2 (Danese, MOQ 6.000) bu hacimle
**uyumsuzdur** ve kartlarda öyle yazılıdır. Eğer MOQ'lar gerçekte 3× çıkarsa
(`C-462`), **düşük-MOQ alternatifi 5'ten 0'a iner** ve private label tarafındaki
pilot mantığı **tamamen çöker**.

### 9.3 Hangi kaynağıma en az güveniyorum?

**`IMPLIED_BREAKEVEN_USDTRY` sütununa.**

Bu sütun, ülkeler arası tek sıralama aracımdır ve **modelin çıktısına değil,
gözlenen CIF birim değerine** dayanır (`EV-2026-08-09-405`). O seri:
- **ülke ortalamasıdır ve premium SKU'ları içerir** → segmentimizin gerçek CIF'i
  bunun altındadır;
- **ZA/AU/AR satırları `TEMSİLİ DEĞİL`** (hacim <100 bin lt) — **Kart 1'in
  (Harland/AU) sıralama değeri fiilen yoktur**;
- ve bu Comtrade yorumu **benim iki turdur kapatamadığım** bir yorumdur —
  `finans-fizibilite` bunu raporunda açıkça yazmıştır (§10.4).

**İkinci en az güvendiğim:** `EV-2026-08-09-408` (Interbrosa'nın 3.000 MOQ'su).
Havuzun **en düşük doğrulanmış MOQ'su** ve **pilot mantığının taşıyıcısı** —
ama kaynak sitesi **2026-08-10'da HTTP 503** döndü; yani **tek çapa, teyit
edilemeyen bir siteden geliyor.**

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlışlık | Değişen karar |
|---|---|
| Gerçek teklifler Y'nin üstünde gelirse | **Fiyat/performans segmentinde ithalat tezi çöker** → `KILL` veya hedef basamağın yukarı revizyonu (mandayı ihlal ederek) |
| MOQ'lar 3× çıkarsa | **Pilot ölçek kararı** değişir: 5.000 → 15.000+ ; `peak_cash_requirement` katlanır → `TEST` yerine daha büyük bir taahhüt gerekir |
| Menşe belgesi taahhüdü alınamazsa (8 kartta) | Tavan **272,83 → 240,73**; tercihli menşenin avantajı **sıfırlanır** → ülke seçimi tamamen **navlun ve EXW fiyatına** kayar |
| Purcari RO/BG'den tedarik mümkünse | **Menşe, tedarikçi seçilirken bağımsız bir pazarlık değişkenine dönüşür** — havuzda tek örnektir |
| Danese'nin TR ilişkisi münhasırsa | RFQ hedef listesinin **2. sırası düşer**; İtalya (en güçlü hat) tarafında A-öncelikli tek aday kalmaz |
| fx girildiğinde tavan çok düşük çıkarsa | Tüm kartlar **tek adımda** yeniden hesaplanır; **ülke sıralaması ilk kez anlamlı hale gelir** |

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre |
|---|---|---|---|---|
| 1 | **Tek tarihli USD/TRY ve EUR/TRY kaydı** | `yatirim-komitesi-baskani` / `finans-fizibilite` | T1/T2 kur kaynağı + kanıt kartı | **saatler** — en ucuz, en yüksek getirili adım |
| 2 | Çapa kararı (basamak + kanal + `<VOLUME>`) | `yatirim-komitesi-baskani` | `T-871` | günler |
| 3 | Yatırımcı eşikleri (`OQ-901`) | `yatirim-komitesi-baskani` | `T-851` | günler |
| 4 | **Dalga 1 RFQ — 7 A-öncelikli hedef** | `global-sourcing-kasifi` | `rfq-template.md` v2.1, **aynı metin**, başkan onayı sonrası | **2–3 hafta** (+1 hafta takip) |
| 5 | Gelen her teklif için ayrı kanıt kartı, `quote_type: FIRM_OFFER`, teklif geçerliliği = `ttl` | `global-sourcing-kasifi` | `rfq-contact-pack.md` §5.3 | teklifle eşzamanlı |
| 6 | OD-5'in hukuki sonucu | `gumruk-vergi-uzmani` | `T-872` | 1 tur |
| 7 | Purcari MD/RO/BG navlunu | `navlun-lojistik-uzmani` | `T-873` | 1 tur |

> **Sıra önemlidir:** 1 ve 2 olmadan 4 yapılırsa, gelen teklifler
> **değerlendirilemez** — elimizde karşılaştırılacak bir eşik olmaz.
> **Gerçek RFQ'nun değeri, ondan önce alınacak iki karara bağlıdır.**
