# RAPOR — TUR 2.5 · NAVLUN & LOJİSTİK

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2.5 — TAZELİK KONTROLÜ + TERS MODEL SENARYO HAZIRLIĞI
tarih:  2026-08-10
durum:  SUBMITTED
```

---

## 1. YÖNETİCİ ÖZETİ

Bu turda **yeni navlun araştırması yapılmadı** ve **yeni kanıt kartı
açılmadı** — görev tanımı gereği. İki iş yapıldı: (1) TUR 2'nin LCL kanıt
setinin tazelik durumu tespit edildi, (2) mevcut kanıtlar ters model için
**kaynağı yazılı LOW/BASE/HIGH senaryolarına** dönüştürüldü.

**En kritik tek bulgu:** projedeki **tek gerçek navlun verisi olan 10 LCL
kotasyon kartı 2026-08-16'da ölüyor** — hem `ttl` hem de kotasyonun kendi
geçerlilik tarihi aynı günü gösteriyor. Bugün (2026-08-10) hepsi geçerli,
**6 gün ömrü kaldı**. FCL zaten `UNKNOWN` olduğu için, 2026-08-17'den sonra
çalıştırılan bir model lojistik girdisini **bütünüyle kanıtsız** kullanmış
olur (`T-802`, impact HIGH).

İkinci bulgu: TUR 2'nin *"şişe başı lojistik 5.000 → 100.000 arasında 3–4 kat
düşer"* iddiası **yalnızca FCL için doğrudur**; LCL'de USD bacağı sadece
**%12–14** düşer (`EV-2026-08-10-329` üzerinden yeniden hesaplandı).

Üçüncü bulgu: FCL `UNKNOWN` olmasına rağmen lojistik girdisi **sınırsız
değildir** — kırılma noktasının üstünde LCL fiyatı FCL için **koşullu bir üst
sınırdır**. Ters model bu tavanı kullanabilir.

---

## 2. BULGULAR

### B-1: LCL kanıt seti 2026-08-16'da ölüyor; bugün geçerli

```yaml
claim:          "10 LCL kotasyon kartinin son gecerli gunu 2026-08-16, STALE tarihi 2026-08-17. Bugun (2026-08-10) hepsi GECERLI."
value:          "son gecerli gun 2026-08-16 / STALE 2026-08-17 / kalan omur 6 gun"
unit:           tarih
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-301, -302, -303, -305, -306, -307, -308, -309, -310, -311
katman:         L2 (CIF bileseni)
```

**Gerekçe:** `veri-tazeligi.md` §KURALLAR-2 (`access_date + ttl < bugün` →
STALE) uygulandığında `2026-08-10 + 6d = 2026-08-16`; bu tarihte koşul eşitlik
verir, sağlanmaz → son geçerli gün 2026-08-16, STALE 2026-08-17.
**Ayrı ikinci kontrol** (§ÖZEL KONTROL — kaynağın kendi geçerliliği) aynı
tarihi veriyor: Flexport quote validity = 2026-08-16. İki kontrol birbirini
gevşetmiyor, **doğruluyor**.

### B-2: Set "11 kart" değil, **10 kart**

```yaml
claim:          "EV-2026-08-10-304 (Italya) 6d setine ait DEGILDIR: ttl 14d, status UNKNOWN, icinde navlun rakami yok."
value:          10
unit:           adet kanit karti
status:         FACT
tier:           T4
evidence_id:    10-evidence/index.csv (dogrudan kontrol)
```

**Gerekçe:** `rota-maliyet-matrisi.md` §8 ve `T-304` §4 aralık gösterimi
(`-301 … -311`) kullandığı için `-304`'ü sete dahil etmiş görünüyor.
`index.csv`'de `-304` `ttl: 14d`, `status: UNKNOWN`'dır. Kanıt kartları
immutable, `index.csv` bu turda kapalı → **hiçbir kayıt değiştirilmedi**,
düzeltme `T-801` ile kayda geçirildi. **Modele sayısal etkisi yok.**

### B-3: LCL'de ölçek ekonomisi yoktur — TUR 2'nin iddiası moda bağlıdır

```yaml
claim:          "5.000 -> 100.000 sise arasinda sise basi lojistik 3-4 kat duser iddiasi YALNIZCA FCL icin dogrudur."
value:          "LCL USD/sise -%13 · LCL TRY/sise -%67 · FCL USD/sise -%68 · FCL EUR/sise -%74"
unit:           "%"
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-301, EV-2026-08-10-329
katman:         L2/L3
```

**Türetme zinciri:** LCL maliyeti = `USD/CBM × CBM` (tamamen değişken) +
sevkiyat başı sabitler. Hacim büyüdükçe yalnızca sabit bacak seyrelir; USD
bacağı m³ ile doğrusal büyür. Hesap: `40-lojistik/lojistik-senaryolari-tur25.md`
§4.5. **Sonuç:** "büyürsek navlun ucuzlar" beklentisi **LCL varsayımıyla
yanlıştır**; ölçek ekonomisi FCL'e geçmeyi gerektirir — ve FCL fiyatı
`UNKNOWN`'dır. Bu, `T-304`'ün çekirdeğini ticari olarak daha da kritik yapar.

### B-4: LCL, FCL için koşullu bir ÜST SINIR çapasıdır

```yaml
claim:          "Kirilma noktasinin (~5.900 sise/sevkiyat) ustundeki hacimlerde LCL'in sise basi maliyeti FCL'in UST SINIRIDIR."
value:          "25.000 sise: LCL LOW 0,295 > FCL kose-LOW ~0,10 ; LCL HIGH 0,558 > FCL kose-HIGH ~0,36 USD/sise"
unit:           USD/sise
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-330, EV-2026-08-10-301
katman:         L2
```

**Türetme zinciri:** Kırılma noktası tanımı gereği, o hacmin üstünde FCL
ucuzdur. LCL fiyatı **gerçek kotasyondur**, FCL fiyatı `UNKNOWN`'dır →
gerçek bir sayı bilinmeyeni **yukarıdan sınırlar.** Sayısal doğrulama iki
köşede de tutuyor (EUR→USD 1,00–1,20 `ASSUMPTION`).

**Koşullar (biri düşerse iddia düşer):** (a) `EV-2026-08-10-330` doğru olmalı;
(b) EUR/USD 1,00–1,20 (fx `UNKNOWN`, `T-311`); (c) **LCL kotasyonu taze
olmalı** → 2026-08-16'dan sonra bu iddia da ölür; (d) 5 CBM kotasyonunun
55–239 CBM'e doğrusal uzatımı — gerçekte LCL birim fiyatı hacimle **düşer**,
yani uzatım **muhafazakârdır** ve üst sınırı güvenli tarafa iter.

### B-5: LCL'in en büyük belirsizliği artık okyanus navlunu değil, CFS'tir

```yaml
claim:          "LCL'de CFS (30-80 USD/CBM) okyanus navlununun (123-133 USD/CBM) %25-65'i kadardir ve kotasyona DAHIL OLUP OLMADIGI bilinmiyor."
value:          "30 - 80"
unit:           USD/CBM
status:         ASSUMPTION
tier:           T4
evidence_id:    EV-2026-08-09-324, EV-2026-08-10-301
katman:         L2
```

**Varsayım gerekçesi:** `EV-2026-08-10-301`'in kendi metni *"excluded: origin
local charges, CFS destination"* diyor. TUR 2'nin pilot tablosu ise LOW ucunda
CFS'i **sıfır** kabul etmişti. Bu turda LOW köşesi karşılaştırılabilirlik için
korundu, **BASE (30) ve HIGH (80) CFS'i açıkça ekliyor.** Bu, LCL BASE'ini
TUR 2'ye göre yukarı taşır (5.000 şişede 0,450 vs TUR 2'nin ~0,33–0,63 bandının
ortası). **Bilinçli ve kaynaklı bir sapmadır**, gizlenmemiştir.

### B-6: Gecikme maliyeti antrepoda değil limanda doğar

```yaml
claim:          "Antrepo depolama sise basina ihmal edilebilir (60 gunde 0,03 EUR); limanda 60 gun bekleme ~0,61 USD/sise."
value:          "antrepo 60 gun 0,0294 EUR/sise · limanda 60 gun 0,61 USD/sise"
unit:           EUR/sise · USD/sise
status:         ESTIMATE
tier:           T4/T5
evidence_id:    EV-2026-08-10-327, EV-2026-08-09-344
katman:         L5
```

**Gerekçe:** 0,35 EUR/palet/gün × 7–139 palet, şişeye bölündüğünde 60 günde
bile 0,03 EUR kalıyor. Buna karşılık limanda bekleme **iki sayaç** çalıştırıyor
(detention + terminal ardiyesi) ve 60 günde **en pahalı FCL okyanus
navlununu aşıyor.** Ruhsat/bandrol gecikmesi riski `T-301`'e bağlıdır ve
maliyeti **konteyneri free time içinde antrepoya çekmekle** ~30–35 kat düşer.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | **FCL okyanus navlunu — 9 rotanın 8'inde** | Kamuya açık marketplace 14 lane'in 14'ünde kotasyon vermiyor (`EV-2026-08-10-312`); bu turda **yeni tarama yasaktı** | **CRITICAL** | Forwarder RFQ — `T-304`, TUR 7 |
| 2 | FCL okyanus navlunu — İspanya'da **BASE** | `C-311` açık: 4–5 kat çelişki, taraf seçilemez (`M-6`) | **CRITICAL** | Aynı RFQ |
| 3 | **İtalya — LCL ve FCL** | 4 liman denendi, 0 offerings (`EV-2026-08-10-304`) | HIGH | `T-312` |
| 4 | İspanya dışı 8 menşenin **origin charge'ları** | Taşıyıcı local tarifeleri taranmadı; bu turda yasak | HIGH | `T-312` |
| 5 | **LCL CFS kotasyona dahil mi** | Kotasyon metni "hariç" diyor ama tutar vermiyor | HIGH | Aynı RFQ (`included/excluded` listesi) |
| 6 | Beklenen **kırılma / fire oranı** | Hiçbir turda bulunamadı | HIGH | `T-314` |
| 7 | Bandrolleme birim maliyeti + kapasitesi | — | HIGH | `T-314` |
| 8 | Antrepo giriş/çıkış elleçleme | — | MEDIUM | `T-314` |
| 9 | Thermal liner birim maliyeti | — | MEDIUM | `T-304` |
| 10 | Türk sigortacıdan gerçek kotasyon | — | MEDIUM | `T-304` |
| 11 | Çekici + şasi darası (40HC tavanını belirler) | `ASSUMPTION`, kanıt yok | MEDIUM | `T-304` |
| 12 | Ardiye free time (0 gün mü 5 gün mü) | `C-312` çözülmedi | MEDIUM | `T-313` |
| 13 | Ruhsat/bandrol bekleme süresi | Başka ajanın alanı | **CRITICAL** | `T-301` |
| 14 | `fx` (USD/TRY, EUR/TRY) | `makro.yaml` null | **CRITICAL** | `T-311` |

---

## 4. ÇELİŞKİLER

Bu turda **yeni çelişki açılmadı** (`C-801 … C-819` bloğu kullanılmadı).
Mevcut çelişkiler senaryoların içine **kapatılmadan** taşındı:

| conflict_id | Kaynak A | Kaynak B | Neden çelişiyor | Durum |
|---|---|---|---|---|
| `C-311` | Marketplace "from" 295–650 USD | T5 blog 1.200–2.500 EUR | 4–5 kat fark; base mi all-in mi bilinmiyor | **OPEN** — `M-6` ile iki köşe ayrı taşınıyor; şişe başına **0,10–0,35 USD** belirsizlik üretiyor |
| `C-312` | SafiPort: ardiye 1. günden | Müşavirlik kaynağı: 6. günden | Free time 0 mı 5 mi | **OPEN** — senaryolarda 5 gün ardiye ücretlendirildi (muhafazakâr) |
| `C-313` | Taşıyıcı THD 165–298 USD | Terminal kapı-çıkış 113–116 USD | Aynı olayı mı fiyatlıyor | **OPEN** — senaryolarda **yalnızca THD** kullanıldı (çift sayım yok) |

**Sessizce taraf seçilmedi. `99-ops/celiskiler.md` bu turda değiştirilmedi**
(dokunma listesinde).

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| `lojistik.yaml` | `tur25_senaryolar.lcl_okyanus_usd_per_sise.ispanya_valencia` | 0,275 / 0,296 / 0,318 | USD/şişe | ESTIMATE | `EV-2026-08-10-301` |
| `lojistik.yaml` | `…lcl_okyanus_usd_per_sise` (8 rota daha) | §3 tablosu | USD/şişe | ESTIMATE | `EV-2026-08-10-302…-311` |
| `lojistik.yaml` | `…lcl_okyanus_usd_per_sise.italya` | `null` | — | **UNKNOWN** | `EV-2026-08-10-304` |
| `lojistik.yaml` | `…hacim_senaryolari_ispanya.v5000.lcl` | 0,325/0,450/0,630 USD · 0 EUR · 2,60/3,99/4,99 TRY | şişe başı | ESTIMATE | `EV-2026-08-10-301` + `-313…-327` |
| `lojistik.yaml` | `…v25000.lcl` | 0,295/0,399/0,558 USD · 1,04/1,60/2,57 TRY | şişe başı | ESTIMATE | aynı |
| `lojistik.yaml` | `…v50000.lcl` | 0,290/0,391/0,546 USD · 0,91/1,42/2,07 TRY | şişe başı | ESTIMATE | aynı |
| `lojistik.yaml` | `…v100000.lcl` | 0,287/0,387/0,540 USD · 0,84/1,32/1,82 TRY | şişe başı | ESTIMATE | aynı |
| `lojistik.yaml` | `…*.fcl_*_kose_low` / `_kose_high` | §4 tabloları | şişe başı | ESTIMATE / **LOW** | `EV-2026-08-10-322`, `-320`, `-324`, `-328` (`C-311`) |
| `lojistik.yaml` | `…*.fcl_*_base` | **`null`** | — | **UNKNOWN** | `M-6` gereği |
| `lojistik.yaml` | `…c311_belirsizlik_usd_per_sise` | 0,105 – 0,350 | USD/şişe | ESTIMATE | `C-311` |
| `lojistik.yaml` | `…lcl_ust_sinir_capasi` | koşullu üst sınır | — | ESTIMATE / LOW | `EV-2026-08-10-330` |
| `lojistik.yaml` | `…tazelik.bu_blogun_gecerliligi` | 2026-08-16 | tarih | FACT | 10 LCL kartı |
| `lojistik.yaml` | `…ters_model_onerilen_girdi` | §6 tablosu | şişe başı | ESTIMATE | — |

**Bu turda yeni `evidence_id` açılmadı.** Bütün satırlar mevcut kartlardan
türevdir ve `status: ESTIMATE`'tir.

---

## 6. ÇAPRAZ İPUÇLARI

`99-ops/capraz-ipuclari.md` bu turda **dokunma listesindedir**; ipuçları
`99-ops/_parts/capraz-ipuclari-navlun-lojistik-uzmani-tur25.md` dosyasına
bırakıldı.

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `finans-fizibilite` | Müşavirlik ücreti CIF'e bağlı bir kademe içeriyor: CIF 15.001–225.000 USD → aşan kısmın **%0,3**'ü (`EV-2026-08-09-342`) | 25.000 şişe ve üstünde CIF bu eşiği aşar; sabit 6.020 TL varsayımı **eksik kalır** |
| `finans-fizibilite` | LCL'de ölçek ekonomisi **yok** (USD bacağı −%13) | "Hacim büyürse birim lojistik düşer" varsayımı mod değişmeden **çalışmaz** |
| `global-sourcing-kasifi` | Koli formatı (6'lı / 12'li) konteyner başına şişe sayısını ve **25.000 şişede konteyner sayısını 2'den 3'e** çıkarabiliyor | `T-302` sanılandan daha maliyetli bir `UNKNOWN` |
| `mevzuat-ruhsat-uzmani` | Gecikmenin maliyeti antrepoda değil **limanda** doğuyor (60 gün ≈ 0,61 USD/şişe vs 0,03 EUR/şişe) | `T-301` cevabı "kaç gün" değil, **"yük nerede bekliyor"** olarak da sorulmalı |
| `gumruk-vergi-uzmani` | LCL'de navlun CBM fiyatına gömülü, FCL'de kalem kalem | Gümrük kıymetine hangi kalemin gireceği **moda göre değişir** |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|---|---|---|---|---|
| `T-801` | `yatirim-komitesi-baskani` | 6d LCL seti 11 değil **10** karttır; `-304` sete ait değil | **LOW** | OPEN |
| `T-802` | `yatirim-komitesi-baskani` | Tek gerçek navlun verisi **2026-08-16'da ölüyor**; sonrasında lojistik girdisi kanıtsızdır | **HIGH** | OPEN |

**Kapatılan ticket yok.** `T-304` (CRITICAL) ve `C-311` **aynen açıktır** —
bu tur onları çözecek hiçbir araştırma yapmadı ve yapmaması gerekiyordu.

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-10-301, -302, -303, -305, -306, -307, -308, -309, -310, -311` | **6d** | **2026-08-17** ⚠ |
| `EV-2026-08-10-304`, `-312`, `-322`, `-323`, `-324`, `-331` | 14d | 2026-08-25 |
| `EV-2026-08-10-329`, `-330` (türev) | 14d ama **kaynağa bağlı** | **fiilen 2026-08-17** |
| `EV-2026-08-09-330`, `-331`, `-333` | 14d | 2026-08-24 |
| `EV-2026-08-09-324` | 30d | 2026-09-09 |
| `EV-2026-08-10-313 … -319`, `-325`, `-326`, `-327`, `-328`, `-332` | 90d | 2026-11-09 |
| `EV-2026-08-09-342` (müşavirlik tarifesi) | 1y | 2027-08-10 |

**Bu raporun kendi raf ömrü: 2026-08-16.** §3 ve §4'ün LCL satırları o
tarihten sonra `FACT` olarak okunamaz.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR?

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Gerçek bir FCL kotasyonu.** Tek bir forwarder'dan alınacak tarihli,
`included/excluded` listeli bir 20DV/40HC İspanya→Türkiye kotasyonu şunları
aynı anda çürütür veya doğrular: `C-311`'in hangi ucunun doğru olduğunu,
§4'teki bütün FCL köşelerini, §5.1'deki üst sınır iddiasını ve LCL/FCL
kırılma noktasını (~5.900 şişe).

Eğer gerçek FCL navlunu **1.200 USD'ye yakın** çıkarsa: 5.000 şişelik pilotta
FCL'in USD avantajı **kaybolur**, LCL öne geçer ve TUR 2'nin "20DV FCL paletli"
önerisi yalnızca kırılganlık argümanıyla ayakta kalır.
Eğer **300 USD'ye yakın** çıkarsa: 25.000 şişede FCL, LCL'den **4 kat** ucuzdur
ve ters modelin lojistik tavanı ciddi biçimde aşağı iner.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**LCL kotasyonunun 5 CBM'den 55–239 CBM'e doğrusal uzatılması.**
Gerçek LCL tarifeleri kademelidir; büyük hacimde birim fiyat düşer. Bu, benim
LCL sayılarımı **yüksek** (muhafazakâr) yapar — ama ne kadar yüksek olduğunu
bilmiyorum. §5.1'deki "üst sınır" iddiası tam da bu muhafazakârlığa yaslanıyor;
yani **iddia kendi hatasıyla korunuyor**, bu zayıf bir savunmadır.

İkinci en kırılgan: **CFS'in dahil olup olmadığı** (B-5). BASE senaryom
30 USD/CBM CFS içeriyor. CFS aslında dahilse LCL BASE'im 5.000 şişede
**0,450 → 0,382 USD/şişe** düşer (%15 hata). Hariçse ve üst uçtaysa
0,450 → 0,570'e çıkar.

### 9.3 Hangi kaynağıma en az güveniyorum?

**Kumport ardiye tarifesi** (`EV-2026-08-10-318`) — PDF'e erişilemedi, arama
özetinden alındı ve LOW senaryomun ardiye ayağını **tek başına** taşıyor.
Yanlışsa LOW senaryosunun USD bacağı konteyner başına 105 USD artar.

İkincisi: **FCL BAF/CAF/ETS %15–25** (`EV-2026-08-10-324`, **T5**). `M-6`
gereği zaten `UNKNOWN` olan bir base'in üzerine çarpılıyor — yani **belirsizin
belirsizi**.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlış çıkarsa | Değişen karar |
|---|---|
| LCL ölçek ekonomisi bulgusu (B-3) yanlışsa | "Ölçeğe geçmek için FCL zorunlu" sonucu düşer; `T-304`'ün aciliyeti azalır |
| Üst sınır iddiası (B-4) yanlışsa | Ters model lojistik girdisi için **tavansız** kalır → `UNKNOWN` döndürmek zorunda kalır |
| Tazelik tespiti (B-1) yanlışsa (kotasyon aslında daha uzun geçerliyse) | `T-802` ve TUR 3'ün zaman baskısı ortadan kalkar — **karar takvimi değişir** |
| Gecikme maliyeti bulgusu (B-6) yanlışsa | Antrepo/liman stratejisi değişir; `T-301`'in finansal ağırlığı yeniden hesaplanır |

**Ama hiçbiri tek başına projeyi öldürmez.** Şişe başı lojistik en kötü
senaryoda bile ~0,63 USD + ~5 TRY mertebesindedir; f/p segmentinde öldürücü
olan kalem vergidir, navlun değildir. **Navlunun rolü marjini aşındırmak, tek
başına kararı vermek değildir.**

### 9.5 Bunu doğrulamak için ne gerekir?

| Ne | Kim | Nasıl | Süre |
|---|---|---|---|
| FCL kotasyonu (3 forwarder, İspanya→TR, 20DV+40HC, included/excluded listeli) | `navlun-lojistik-uzmani` | **Dış temas** — başkan izni gerekli (`T-304` §5: TUR 7 ve `TEST`/`IMPORT PILOT` kararına bağlı) | 3–10 iş günü |
| LCL kotasyonunun yenilenmesi | `navlun-lojistik-uzmani` | Masabaşı — aynı kaynaktan yeni kart + `supersedes` | **1 saat**, ama 2026-08-16'dan sonra gerekli |
| CFS'in dahil olup olmadığı | aynı RFQ | RFQ'da zorunlu alan | RFQ ile birlikte |
| Ardiye free time (`C-312`) | `navlun-lojistik-uzmani` | Terminal tarifelerinin PDF'lerine doğrudan erişim | 1–2 saat |
| Bandrol/ruhsat bekleme süresi | `mevzuat-ruhsat-uzmani` | `T-301` | — |

> **Bu turda hiçbir dış temas yapılmadı, yapılamazdı ve önerilmiyor** —
> yalnızca kaydediliyor: **`G2-L` masabaşı araştırmayla açılamaz.**
