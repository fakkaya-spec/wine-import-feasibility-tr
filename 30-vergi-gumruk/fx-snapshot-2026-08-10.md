# FX SNAPSHOT — 2026-08-10

> **ETİKET: `OBSERVED_FX` · `NOT_FORECAST`**
>
> Bu dosya bir **gözlem kaydıdır**. İçindeki hiçbir sayı gelecekteki bir kur
> hakkında iddia taşımaz. Aşağıdaki "senaryo" başlıkları **kur tahmini
> değildir**; bunlar `negotiation translation sensitivity` eksenleridir.
> Bu ayrım `CLAUDE.md §1.1` ve `§3` gereğidir ve bu dosyanın **varlık sebebidir**.

| | |
|---|---|
| Tur | TUR 3.25 §1 |
| Gözlemi alan ajan | `gumruk-vergi-uzmani` |
| Gözlem tarihi | **2026-08-10** |
| Gözlem zamanı | **19:50 UTC** (= 22:50 TRT) |
| Kaynak | **TCMB — Günlük Döviz Kurları bülteni, Bülten No 2026/147** |
| Tier | **T2** (kamu kurumunun resmî güncel sayfası) |
| TTL | **7d** → `2026-08-17` sonrası **STALE** |
| Evidence | `EV-2026-08-10-865` · `-866` · `-867` · `-868` |

---

## 1. GÖZLENEN DEĞERLER

TCMB günlük bülteninde **dört ayrı kur** ilan edilir ve bunlar
**birbirinin yerine kullanılamaz**. Hepsi kaydedilmiştir:

| Kur tipi (XML alanı) | EUR/TRY | USD/TRY |
|---|---|---|
| Döviz Alış (`ForexBuying`) | 55,0422 | 47,6260 |
| **Döviz Satış (`ForexSelling`) — BİRİNCİL** | **55,1414** | **47,7118** |
| Efektif Alış (`BanknoteBuying`) | 55,0037 | 47,5927 |
| Efektif Satış (`BanknoteSelling`) | 55,2241 | 47,7834 |
| Alış-satış spread | 0,0992 (%0,18) | 0,0858 (%0,18) |

**Çapraz kur:** 1 EUR = **1,1557 USD** (`CrossRateOther`, `EV-2026-08-10-867`)

### Neden "Döviz Satış" birincil alındı
İthalatçı, tedarikçiye ödemek için dövizi **satın alan** taraftır. Maliyet
tarafında muhafazakâr olan kur **satış** kurudur. Alış kuru silinmemiştir;
`makro.yaml → fx.observed.*.doviz_alis` ve
`fx.senaryolar.alis_kuru_ekseni` altında **paralel olarak** taşınır.

### İç tutarlılık kontrolü (yapıldı, geçti)
| Türetme | Hesap | Sonuç | TCMB ilanı |
|---|---|---|---|
| Satış üzerinden | 55,1414 / 47,7118 | 1,1557 | 1,1557 |
| Alış üzerinden | 55,0422 / 47,6260 | 1,1557 | 1,1557 |

Sapma yok → EUR ve USD kurları **aynı bültenden ve aynı ana** aittir.
Farklı saatlerden karışık kur alınmamıştır.

### Kayıt altına alınan belirsizlikler (uydurulmadı)
- **Bültenin gün içi hangi saatte sabitlendiği `UNKNOWN`'dır.** Bu turda
  doğrulanmadı. Kaydedilen şey **gözlem anıdır** (19:50 UTC), bültenin fixing
  saati değildir.
- **Bu kurların gümrük beyanında kullanılıp kullanılmayacağı bu dosyanın
  KAPSAMI DIŞINDADIR.** `T-911` (gümrük beyan kuru) **AÇIK** kalır ve bu turda
  bilerek açılmamıştır (görev: yalnızca gözlem, yeni vergi araştırması yasak).
  `makro.yaml → fx.gumruk_kuru_kullanilir_mi` **`UNKNOWN` bırakılmıştır.**

---

## 2. SENSITIVITY EKSENLERİ — **TAHMİN DEĞİLDİR**

### 2.1 Bu eksen neyin cevabıdır

> **"Tedarikçi EUR isterken bizim TL tavanımız ne kadar dayanır?"**

Ters modelde tavan (`MAX_CIF_TRY`) **TL** cinsindendir ve TL kanal
fiyatlarından türer. Tedarikçinin fiyatı ise **EUR/USD** cinsindendir.
Bu eksen, iki dünya arasındaki **çeviri katsayısının** oynama aralığını
gösterir — yani bugün kabul edilebilir görünen bir EXW/FOB fiyatının **hangi
kur seviyesinde tavanı aşacağını**.

**Bu bir yatırım beklentisi, kur görüşü veya olasılık dağılımı DEĞİLDİR.**
Çarpanlar (%10/%20) **keyfî ve simetrik** seçilmiş eksen noktalarıdır; hiçbir
dış kaynak bunları öne sürmemiştir (`EV-2026-08-10-868`, `status: ASSUMPTION`,
`tier: -`).

### 2.2 YÖN KURALI (karıştırılması en kolay yer)

Kur `TRY / 1 EUR` biçiminde kotedir.

> **"TRY %10 zayıf" = 1 EUR **daha çok** TL eder = EUR/TRY **ARTAR** = maliyet **ARTAR**.**

```
FX_0        = gözlenen
FX_UP_10    = FX_0 × 1,10      TRY zayıf   -> kotasyon ARTAR -> maliyet ARTAR
FX_UP_20    = FX_0 × 1,20      TRY daha zayıf
FX_DOWN_10  = FX_0 × 0,90      TRY güçlü   -> kotasyon DÜŞER -> maliyet AZALIR
```

**Sayısal örnek (EUR/TRY döviz satış):**

```
FX_0     = 55,1414 TRY/EUR
FX_UP_10 = 55,1414 × 1,10 = 60,6555 TRY/EUR

1 EUR'luk bir EXW şişe fiyatı:   55,14 TL  ->  60,66 TL
Kotasyon ARTTI, ithalatçının TL maliyeti ARTTI.  Yön doğrudur.
```

Tersini test: `FX_DOWN_10` = 55,1414 × 0,90 = 49,6273 → aynı şişe **49,63 TL**.
TL güçlendi, maliyet **azaldı**. Yön doğrudur.

### 2.3 EKSEN DEĞERLERİ — döviz satış (birincil)

| Eksen | Çarpan | **EUR/TRY** | **USD/TRY** | İthalatçıya etkisi |
|---|---|---|---|---|
| `FX_DOWN_10` | 0,90 | **49,6273** | **42,9406** | maliyet ↓ |
| **`FX_0`** (gözlem) | 1,00 | **55,1414** | **47,7118** | — |
| `FX_UP_10` | 1,10 | **60,6555** | **52,4830** | maliyet ↑ |
| `FX_UP_20` | 1,20 | **66,1697** | **57,2542** | maliyet ↑↑ |

### 2.4 EKSEN DEĞERLERİ — döviz alış (paralel, karıştırılmaz)

| Eksen | EUR/TRY | USD/TRY |
|---|---|---|
| `FX_DOWN_10` | 49,5380 | 42,8634 |
| `FX_0` | 55,0422 | 47,6260 |
| `FX_UP_10` | 60,5464 | 52,3886 |
| `FX_UP_20` | 66,0506 | 57,1512 |

### 2.5 EUR/USD tüm eksenlerde **SABİTTİR** = 1,1557

TL şoku EUR/USD paritesini **değiştirmez**; çarpan hem paya hem paydaya
uygulandığı için sadeleşir:

```
(EUR/TRY × k) / (USD/TRY × k) = EUR/USD
```

EUR/USD için bu dosyada **ayrı bir duyarlılık ekseni tanımlanmamıştır.**
O ayrı bir risktir (menşe ülke seçimi EUR bölgesi ↔ USD bölgesi arasında
kayarsa önem kazanır) ve ayrıca açılmalıdır.

### 2.6 İKİ KONVANSİYON — hangisi kullanıldı

"TRY %10 zayıf" iki farklı şekilde matematikleştirilebilir. Karışıklığı
önlemek için ikisi de yazılıyor; **modelde KONVANSİYON A kullanılmıştır.**

| | Tanım | EUR/TRY | USD/TRY |
|---|---|---|---|
| **A — KOTASYON ÇARPANI (KULLANILAN)** | kotasyon ×1,10 | **60,6555** | **52,4830** |
| B — TL SATIN ALMA GÜCÜ | TL değerinin %10'unu kaybeder (÷0,90) | 61,2682 | 53,0131 |

Konvansiyon A'da kotasyonun %10 artması, TL'nin EUR cinsinden satın alma
gücünün **%9,0909** azalmasına denktir (1 − 1/1,10). `FX_UP_*` adları
**kotasyon yönünü** işaret ettiği için A seçilmiştir. Fark ~%0,9'dur ve bir
**veri farkı değil, adlandırma farkıdır**.

---

## 3. KULLANIM KURALI (BAĞLAYICI)

1. **Kur tarihi belirtilmeden bu sayılar kullanılamaz.** (`makro.yaml` kendi
   kuralı.) Kur tarihi: **2026-08-10**.
2. **Kur tipi belirtilmeden kullanılamaz.** "EUR/TRY = 55" yazmak yetersizdir;
   "EUR/TRY döviz satış = 55,1414 (TCMB, 2026-08-10)" yazılır.
3. **Dönüştürülmüş sayı orijinalin yerine geçmez.** (`makro.yaml` başlığı.)
   Her kalem **kendi orijinal para biriminde** saklanır; TL karşılığı
   **türetilmiş bir görünümdür**, kaynak değildir.
4. **TTL 7 gündür.** `2026-08-17` sonrası bu snapshot `STALE`'dir ve
   `99-ops/veri-tazeligi.md` üzerinden yenilenir. **Yenileme = yeni evidence
   kartı**; bu kartlar overwrite edilmez (`CLAUDE.md §4`).
5. **Gümrük beyan kuru ≠ bu kurlar (doğrulanmadı).** Vergi hesabında
   kullanılmadan önce `T-911` cevaplanmalıdır.
6. **Eksen değerleri rapora "beklenen kur" diye taşınamaz.** Taşınırsa
   `CLAUDE.md §1.1` ihlal edilmiş olur.

---

## 4. BU SNAPSHOT NEYİ AÇAR (hesabı bu ajan YAPMAZ)

`T-852` ve `T-912`, `fx`'in üç turdur `null` olması nedeniyle ters modelin
**L2 (CIF TRY) üst sınırında durduğunu** kaydetmişti. Girdi artık hazırdır.

| Model çıktısı | Önceki | Şimdi |
|---|---|---|
| `MAX_CIF_TRY` | hesaplandı (üst sınır) | değişmedi |
| **`MAX_FOB_TRY`** | `UNKNOWN` | **girdi HAZIR** |
| **`MAX_EXW_TRY`** | `UNKNOWN` | **girdi HAZIR** |
| **`MAX_FOB_EUR` / `MAX_FOB_USD`** | `UNKNOWN` | **girdi HAZIR** |
| **`MAX_EXW_EUR` / `MAX_EXW_USD`** | `UNKNOWN` | **girdi HAZIR** |
| USD/EUR cinsli L5 kalemlerinin düşülmesi | 0 alınıyordu | **girdi HAZIR** |
| Ülkeler arası **gerçek ayrışma** (FOB seviyesi) | çalışmıyordu | **girdi HAZIR** |

> **HESABI BU AJAN YAPMAZ.** `MAX_FOB` / `MAX_EXW` hesabı ve
> `80-model/engine/ters_model.py` R10/R11 adımının açılması
> **`finans-fizibilite`'nin işidir** (`CLAUDE.md §7`, ajan izolasyonu).
> Bu dosya yalnızca **girdinin hazır olduğunu** bildirir.
> `80-model/engine/` bu turda **ellenmemiştir**.

**Hâlâ açık kalan kısıtlar (fx bunları ÇÖZMEZ):**
- `T-911` — gümrük beyan kuru kuralı `UNKNOWN`.
- `fiyat_guncelleme_gecikmesi_gun` — `kanal-marj-uzmani` girdisi, hâlâ `null`.
  **Modelde sıfır varsayılamaz.** Asimetri gerçektir: alış dövizle, satış TL
  ile yapılır; TL değer kaybettiğinde maliyet **anında** artar, kanal fiyatı
  **anında artmaz**.
- `finansman`, `enflasyon`, `model_donemi` blokları hâlâ `null`.

---

## 5. KAYNAK

- **URL (kalıcı atıf):** `https://www.tcmb.gov.tr/kurlar/202608/10082026.xml`
- **URL (günlük):** `https://www.tcmb.gov.tr/kurlar/today.xml`
  — aynı gün içinde **birebir aynı içeriği** döndürdü (doğrulandı).
- **Snapshot:**
  `10-evidence/raw/snapshots/EV-2026-08-10-865_tcmb-today-kurlar-10082026.xml`
- Bülten başlığı: `Tarih="10.08.2026" Date="08/10/2026" Bulten_No="2026/147"`
- `Unit` = **1** her iki para birimi için (kur 1 birim içindir, 100 değil).

---

## Bu bulguyu ne çürütür?

**1. Tek gün gözlemi bir kur değildir — TTL 7 gün bile cömert olabilir.**
Bu bir **spot gözlemdir**. TL'nin oynaklığı düşünüldüğünde, karar anı ile
gözlem anı arasındaki her gün bu snapshot'ı geçersizleştirmeye yaklaşır.
Model bu tek noktaya **kilitlenirse** çürür. Çürütmeyi engelleyen şey eksenin
kendisidir: `FX_UP_20`'de bile ayakta kalan bir yapı, kur gözlemine
dayanıklıdır; yalnızca `FX_0`'da ayakta kalan bir yapı **kırılgandır ve
raporlanan sonuç değil, uyarı üretmelidir**.

**2. `T-911` bu snapshot'ı vergi hesabında kullanılamaz kılabilir.**
Gümrük beyanında TCMB'nin **döviz satış** kuru mu, başka bir kur mu, hangi
**tarihli** kur mu (beyanname tescil tarihi mi, gözlem tarihi mi) esas alınır —
**doğrulanmadı**. Eğer beyan kuru farklı bir tarih/tip ise, vergi bacağındaki
TL karşılıkları **kayar**. Bu dosyanın kurları o durumda **ticari çeviri**
için geçerli kalır ama **vergi matrahı** için geçersiz olur.

**3. Kur tipi seçimi itiraz görürse sayılar değişir.**
Birincil olarak **döviz satış** alındı. "Efektif satış" veya "döviz alış"
esas alınırsa EUR/TRY sırasıyla 55,2241 / 55,0422 olur. Fark %0,18–0,33
bandındadır — tek başına küçüktür, **ama** ÖTV maktu olduğu ve TL cinsinden
sabit durduğu için marj bandı zaten dar olan bir modelde bu fark
**işaret değiştirebilir**. Bandın darlığı ölçüsünde bu itiraz büyür.

**4. Çarpan konvansiyonu itirazı.**
Konvansiyon A yerine B kullanılırsa `FX_UP_10`'da EUR/TRY 60,6555 değil
61,2682 olur. Sonuç yalnızca **eşiğe çok yakın** senaryolarda değişir; ama
biri bu eksenleri "beklenen kur" diye okursa **bulgu değil, yanlış bilgi**
üretilir — bu dosyanın en gerçek çürütülme riski **yanlış okunmasıdır**,
sayının kendisi değil.

**5. Bankanın uyguladığı gerçek kur TCMB kuru değildir.**
İthalatçı dövizi TCMB kurundan almaz; **bankasının kurundan + komisyondan**
alır. Gerçek transfer kuru TCMB satış kurunun **üzerinde** olabilir. Bu fark
`makro.yaml → finansman.banka_masraflari` (hâlâ `null`) ile birlikte
değerlendirilmelidir. Bu snapshot **resmî göstergedir**, ödenen fiyat değil —
ve bu yönüyle **iyimser taraftadır**.
