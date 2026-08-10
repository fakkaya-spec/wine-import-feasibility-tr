# TUR 3.25 §11 RAPORU — TÜRKİYE PAZAR KÂŞİFİ

```yaml
ajan:            turkiye-pazar-kasifi
tur:             TUR 3.25 §11 (FIZIKSEL MAGAZA OPERASYON GOREVI)
tarih:           2026-08-10
durum:           SUBMITTED
nitelik:         ARAC / OPERASYON BELGESI — VERI URETMEZ
```

---

## 0. ÖNCE ŞU YAZILMALIDIR (BAĞLAYICI DÜRÜSTLÜK BEYANI)

> **SAHA TURU YAPILMAMIŞTIR.**
> Bu ajan fiziksel bir mağazaya gidememektedir. Bu turda **hiçbir fiyat, hiçbir
> SKU, hiçbir sayım, hiçbir fotoğraf, hiçbir kanıt kartı üretilmemiştir.**
> `raf-fiyat-gozlemleri.csv` **değiştirilmemiştir**; `10-evidence/index.csv`,
> `99-ops/*` kayıtları ve `80-model/` **elle sürülmemiştir.**
>
> Üretilen tek şey **görev emridir**: kurucunun eline alıp mağazaya
> gidebileceği tek sayfalık bir operasyon belgesi.

---

## 1. YÖNETİCİ ÖZETİ

TUR 3A'da hazırlanan saha **kontrol listesi** (protokol), bu turda bir saha
**görev paketine** (operasyon emri) dönüştürüldü: sıralı adımlar, mağaza rotası,
dakika bütçesi, açık **durma kuralları** ve satır-geçerlilik kapısı.
İkinci ve asıl değişiklik, sabitlenen yatırımcı kararının
(`PRIMARY 799 · SECONDARY 699 · STRETCH 899 TRY`) belgeye **taşınmasıdır**:
odak bandı `500–1.200 TL` beş alt banda (**B1–B5**) bölündü ve her alt bant
**hangi hedefi test ettiğine** bağlandı; bu bağ artık her CSV satırının üstünde
(`saha_hedef_bant`) taşınıyor. Üçüncü değişiklik alan disiplinidir: TUR 3A'nın
23 alanı, parent'ın dayattığı **12 zorunlu alanla** hizalandı — 3 alan
(marka, üzüm/blend, ABV) zorunluya **yükseltildi**, ithalatçı alanı yalnızca
ithal SKU'dan **tüm SKU'lara** genişletildi, 3 alan (vintage, ürün tipi,
gözlemci) **opsiyonele indirildi**. Satır başına yazılan alan sayısı **artmadı**.

**En kritik tek bulgu:** `T-917` bir ajan turuyla daha ilerletilemez.
`EV-2026-08-10-504` (8 masabaşı yolu kapalı) + `EV-2026-08-10-701`
(17 ek kanal denendi, 0 kullanılabilir) zincirinden sonra **beşinci bir masabaşı
denemesi bilgi üretmez**. Gereken girdi bir araştırma değil, **bir insan
aksiyonudur**.

---

## 2. BULGULAR

### B-1: TUR 3A'nın 23 alanı, 12 zorunlu alanla tam olarak hizalanabilir — alan sayısı ARTMADAN

```yaml
claim:          "12 zorunlu alanin tamami TUR 3A listesinde zaten vardi; eksik olan sey ZORUNLULUK SEVIYESIYDI, ALAN DEGILDI."
value:          "23 alan -> 12 zorunlu + 5 proje zorunlusu + 3 opsiyonel + 2 yeni = 22 aktif alan"
unit:           adet
status:         FACT
tier:           —   # kendi belgemin ic tutarliligi; dis dunya iddiasi degildir
evidence_id:    —   # bir dis olgu degildir, bir belge tasarim kararidir
katman:         —
```

**Gerekçe:** Parent'ın 12 zorunlusu (`photo · shelf label · price · promotion
marker · brand · origin · grape/blend · 750 ml? · ABV · importer · store · date`)
TUR 3A'nın 8+10+5 alanlık listesiyle karşılaştırıldığında **hiçbir yeni veri
türü** talep etmediği görüldü. Fark üç noktadaydı ve üçü de düzeltildi:

1. **`brand` · `grape/blend` · `ABV`** TUR 3A'da "masabaşında fotoğraftan
   doldurulacak" grubundaydı — yani fiilen *"olursa iyi olur"* seviyesindeydi.
   Artık **satır geçerlilik kapısındadır**. Operasyonel sonucu: **F3 (arka
   etiket) fotoğrafı artık YERLİ SKU için de çekilir** — TUR 3A'da yalnızca
   ithal SKU için zorunluydu.
2. **`importer`** TUR 3A'da yalnızca ithal SKU için zorunluydu. Artık tüm
   SKU'larda zorunludur (yerlide `YERLI_URETICI` + üretici ünvanı). Bu, ithalatçı
   haritasını genişletmez ama **yerli/ithal ayrımını arka etiketten kanıtlar** —
   bugün `mensei` alanı sahada `?` yazılabilen tek zorunlu alandır.
3. **`shelf label`** tek bir alan değildir. TUR 3A §D'deki beş işaretin
   (üstü çizili fiyat / KDV ibaresi / rozet / birim fiyat satırı / kampanya
   tarihi) **dördü** bu alanın içeriğidir. Bu, belgede açıkça yeniden
   tanımlandı — aksi hâlde "shelf label ✓" işaretlemek `C-551`'i kapatmaz.

**Opsiyonele indirilenler ve gerekçesi:** `vintage` (fotoğrafta zaten var,
modelde yeri yok), `urun_tipi` (tur **beyaz odaklı** olduğu için varsayılan
"sakin beyaz"; yalnızca köpüklü/tatlı ise işaretlenir), `gozlemci` (mağaza
başlığında 1 kez yeter). Bu üçünün çıkarılması, yukarıdaki üç yükseltmenin
sahada yarattığı ek süreyi **dengeler**.

---

### B-2: Odak bandı 400–1.200'den 500–1.200'e çekildi ve hedeflere bağlandı

```yaml
claim:          "Sabitlenen INVESTOR_TARGET (699/799/899) geldigi icin odak bandi bu uc hedefin ETRAFINA yeniden kuruldu."
value:          "B1 500-629 | B2 629-769 | B3 719-879 | B4 809-989 | B5 990-1200"
unit:           TRY
status:         ASSUMPTION      # bant sinirlarinin kendisi bir gozlem degildir
tier:           —
evidence_id:    [EV-2026-08-10-702, EV-2026-08-09-501, EV-2026-08-09-502]
katman:         L8
```

**Varsayım gerekçesi:** B2/B3/B4 sınırları, `target-shelf-price-analysis.md`
§2.2'de kullanılan **±%10 pencere** tanımının aynısıdır — yeni bir sınır
uydurulmamış, mevcut analizin penceresi sahaya taşınmıştır. B1'in alt ucu
500 TL'dir çünkü `OBSERVED_BENCHMARK` 599,90 TL'nin **altında** en az bir
basamak görülmeden 599 downside senaryosu sınıflandırılamaz. B5'in üst ucu
1.200 TL'dir çünkü projenin segment tavanı **900 TL bir ESTIMATE'tir** ve tek
kanaldan türetilmiştir; tavanın doğru yerde olup olmadığı ancak **dışarıdan**
görülür.

TUR 3A'nın alt ucu 400 TL idi; 500'e çekilmesinin tek nedeni **süre**dir:
gözlenen tek çok-SKU'lu kanalda **600 TL altında stokta yalnızca 1 SKU** vardır
(`EV-2026-08-10-702`) ve 400–500 aralığında geçirilecek dakika, B3'ten
(PRIMARY 799) çalınmış dakikadır. **Sınır tamamen kaybolmasın diye** sayım
formunda `"500 TL altında hiç şarap var mı?"` sorusu ayrı bir satır olarak
korunmuştur — yani alt sınır **taranmaz ama sorulur**.

---

### B-3: Turun kendi kendini durdurma kuralları tanımlandı

```yaml
claim:          "Operasyon belgesinin TUR 3A'ya gore en somut eklentisi, turun NE ZAMAN DURACAGIDIR."
value:          "7 durma kurali"
status:         FACT
tier:           —
```

**Gerekçe:** TUR 3A bir *protokoldü* — neyin toplanacağını söylüyordu, ne zaman
durulacağını söylemiyordu. Sahada en pahalı hata "mağaza sayısını şişirmek"
veya "süre bitince kalanı hatırlayarak doldurmak"tır. İki kural bu yüzden
öne çıkarıldı:

- **Yeterlilik durması:** 4 mağaza bitip ithal satır ≥20 ve zincir-ithal ≥8 ise
  **tur biter** — 5. ve 6. mağaza opsiyoneldir.
- **Yetersizlik durması:** eşik tutmuyorsa tekel bayii eklenir, sonra
  **yine de durulur ve eksik dürüstçe raporlanır.** Mağaza sayısını şişirerek
  eşik doldurmak, örneklemi bozar.
- **Boş mağaza durması:** 500–1.200 TL'de hiç ithal şarap olmayan bir mağazada
  15 dakikada çıkılır — bu bir **bulgudur**, kayıp değil.

---

### B-4: `T-504` asimetri kuralı ve ikinci ziyaret, belgenin ön sayfasına alındı

```yaml
claim:          "Tek ziyaret T-504'u ancak PROMOSYON ISARETI BULUNURSA kapatir; bulunmazsa kapanmaz."
status:         FACT            # bir mantik kurali, bir gozlem degil
evidence_id:    —
ticket:         T-504
```

**Gerekçe:** Bu, turun **en kolay ihlal edilecek** kuralıdır çünkü sezgiye
aykırıdır: gözlemci "baktım, indirim etiketi yoktu" dediğinde bunun
*"fiyat normaldi"* demek olduğunu düşünür. Değildir. TUR 3A'da bu kural
§D'nin altındaki bir not kutusundaydı; şimdi kilitli bir blok olarak §4'te ve
ayrı bir §12 (10 dakikalık ikinci ziyaret) olarak takvimdedir.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | `l8_chain_retail` — zincir market tüketici raf fiyatı | Türkiye'de alkolün online/broşür fiyat iletişimi **yapısal olarak kapalı** (`EV-2026-08-09-514`, `EV-2026-08-09-511`) | **HIGH** | `saha-gorev-paketi.md` §1 durak 2–4 |
| 2 | Benchmark'ın promosyon durumu | 8 masabaşı yolu kapalı (`EV-2026-08-10-504`) | **HIGH** | §4 (a)(c)(e) + §12 ikinci ziyaret |
| 3 | Metro **şarap rafında** KDV sunumu (`C-551`) | Broşürlerde 0 alkol SKU'su var | **HIGH** | §4(b) — F2 fotoğrafı + F4 kasa fişi |
| 4 | 500–1.200 TL'de fiziksel olarak **satın alınabilir** ithal şarap var mı | Tek online kanal, `available` filtresine bağlı (`C-501`) | **HIGH** | §5 sayım formu + §7 stok alanı |
| 5 | Benchmark SKU'ların ithalatçısı | Arka etiket hiçbir kaynakta yok (`OQ-503`) | MEDIUM | §8 — şişeyi çevir, F3 |
| 6 | **Kırmızı/rosé** segment haritası | Bu turun odağı **beyaz**tır | MEDIUM | Ayrı bir tur gerekir — bkz. §EK-D/1 |
| 7 | Şehir farkı büyüklüğü | Tek şehir gözlemi bile yok | MEDIUM | §1 durak 3–6 (2. bölge/şehir) |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**
Bu turda 7 UNKNOWN'ın **hiçbiri kapatılmamıştır** ve kapatıldığı
iddia edilmemektedir.

---

## 4. ÇELİŞKİLER

Bu turda **yeni çelişki açılmamıştır** ve mevcut çelişkilerin hiçbiri
çözülmemiştir. `C-501`, `C-551`, `C-561` **OPEN** kalır.
`99-ops/celiskiler.md` **değiştirilmemiştir**.

Belgeye taşınan tek çelişki **notu** şudur: iki gözlenen kanal, "500–700 TL'de
ithal şarap var mı" sorusunda birbiriyle çelişmektedir (Metro: **var**;
online uzman perakende: **yok**). Saha turu bu çelişkiyi **hakem gözlemle**
çözmek üzere kurgulanmıştır — B1 bandı tam bu yüzden vardır.

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| — | — | **HİÇBİRİ** | — | — | — |

**Bu turda `80-model/` altındaki hiçbir dosyaya girdi üretilmemiştir ve
hiçbir dosyaya dokunulmamıştır.** Gözlem yoksa girdi de yoktur.
`pazar.yaml` içindeki `l8_chain_retail.deger_try` **`null` / `UNKNOWN`**
olarak durmaya devam eder (K1 + K7 + `T-603`).

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `kanal-marj-uzmani` | Saha turu `m_retail` merdiveninin **tepe çapasını** besler ama **hesaplamaz**; L8 gözlemi geldiğinde marj türetimi o ajanın işidir (K4) | `kanal.yaml → m_retail` bu çapa olmadan kurulamaz |
| `mevzuat-ruhsat-uzmani` | Arka etiketten okunacak **ithalatçı ünvanı + üretici + net hacim + ABV** aynı zamanda Türkçe etiket zorunluluğunun **fiili uygulama örneğidir** | Etiket mevzuatının rafta nasıl uygulandığı gözlenebilir |
| `gumruk-vergi-uzmani` | Arka etiketten okunacak **ABV %**, GTİP alt kırılımı için ipucudur — **sonuç o ajanındır**, burada üretilmez | `benchmark_1.abv_pct` bugün `UNKNOWN` |

> Bunlar **sonuç değildir, ipucudur.** Bu turda `99-ops/capraz-ipuclari.md`
> dosyasına **yazılmamıştır** (görev tanımı gereği o dosyaya dokunulmamıştır);
> yeni bir alan-dışı bulgu da üretilmemiştir — yukarıdakiler mevcut kayıtların
> tekrarıdır.

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|---|---|---|---|---|
| `T-917` | `turkiye-pazar-kasifi` | Tek fiziksel gözlem paketi 5 kaydı aynı anda kapatır | HIGH | **OPEN** — `alt_durum: SAHA_GOREV_PAKETI_TESLIM__INSAN_AKSIYONU_BEKLIYOR` |

**Bu turda yeni ticket AÇILMAMIŞTIR ve hiçbir ticket KAPATILMAMIŞTIR.**
`T-504`, `T-603`, `T-701`, `T-405`, `T-561` **OPEN** kalır.
`99-ops/tickets/INDEX.md` **değiştirilmemiştir.**

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-09-501` / `-502` (benchmark) | 30d | **2026-09-08** |
| `EV-2026-08-10-501` / `-502` / `-551` / `-702` (yoğunluk eğrisi) | 30d | **2026-09-08/09** |

> **OPERASYONEL SONUÇ:** Saha turu **2026-09-08'den önce** yapılırsa, gelen
> gözlemler mevcut eğriyle **aynı tazelik penceresinde** karşılaştırılabilir.
> Bu tarihten sonra yapılırsa, karşılaştırma tabanının kendisi STALE olacağı
> için tur **iki kat** iş çıkarır (hem yeni gözlem, hem eski gözlemin yeniden
> doğrulanması). **Turun tarihi bir maliyet kalemidir.**

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Zincir marketlerin (Migros / Macrocenter / CarrefourSA) şarap raflarında
500–1.200 TL bandında hiç ithal SKU olmadığının ortaya çıkması.**
O durumda bu görev paketi *"799 TL'nin zincir rafında karşılığı var mı"*
sorusunu değil, çok daha temel bir soruyu ölçmüş olur: *"zincir market bu
segmentte ithal şarap satıyor mu, hiç?"* Belgenin B1–B5 bant mimarisi,
**bandın içinde ürün olduğu** varsayımı üzerine kuruludur; bu varsayım
yanlışsa 5 alt bandın 4'ü boş döner ve tur, bir fiyat haritası değil, tek bir
**kanal yokluğu** bulgusu üretir. (Bu bile değerlidir — ama bu rapordaki
bant tasarımını gereksiz kılar.)

İkinci geçersiz kılıcı: **12 zorunlu alanın sahada 45 saniyede
doldurulamadığının** görülmesi. Dakika bütçesi (SKU başına ~45 sn ×
~18 SKU = 13,5 dk) TUR 3A'nın 8 elle-yazılan alanına göre kurulmuştu;
şimdi F3 (arka etiket) yerli SKU'lar için de zorunlu. Şişeyi eline alıp
çevirme süresi hesaba **katılmıştır ama ölçülmemiştir**. Gerçek süre 90 sn
çıkarsa mağaza başına ~12 SKU'ya düşülür ve **≥20 ithal satır eşiği 4 mağazayla
tutmaz.**

### 9.2 En kırılgan varsayımım hangisi ve neden?

**Beyaz şarap odağının bandı temsil ettiği varsayımı.**
Mevcut yoğunluk eğrisi (`EV-2026-08-10-702`) **renk ayrımı yapmadan**
üretilmiştir: 799 TL ±%10'daki "31 stokta yerli SKU" sayısı **tüm renkleri**
içerir. Saha turu yalnızca beyaz satır toplayacağı için gelen sayı, mevcut
eğriyle **doğrudan karşılaştırılamaz** — beyazın pay oranı bilinmiyor.
Bunu telafi etmek için sayım formuna "beyaz" ve "tüm renk" olmak üzere
**iki sütun** konuldu; ama bu bir telafi, bir çözüm değil. Türkiye'de şarap
raflarının renk kompozisyonu hakkında elimizde **sıfır veri** vardır.

İkinci kırılgan varsayım: **Metro'nun tek fiyat uyguladığı.** Rotanın 1.
durağı "mümkünse benchmark fotoğrafının çekildiği şube" diyor — ama o şubenin
hangisi olduğu **`UNKNOWN`**'dır (`benchmark_1.magaza / sehir = null`).
Farklı bir Metro şubesinde farklı fiyat çıkarsa, `T-504` kapanmaz; yerine
**yeni bir çelişki** açılır.

### 9.3 Hangi kaynağıma en az güveniyorum?

`EV-2026-08-10-702`'den türetilen **±%10 pencere sınırlarına**.
Bu pencereler tek bir online kanaldan okunmuştur ve o kanal kendi kabulüyle
**premium'a kayıktır** (471 stokta SKU'nun 1'i 600 TL altında; stokta yerli
medyan 1.410 TL). B1–B5 bant sınırlarını bu pencerelerden türetmek,
**saha turunun ölçeceği şeyi kısmen önceden varsaymak** demektir. Eğer
fiziksel rafın fiyat dağılımı bu kanaldan yapısal olarak farklıysa
(ki `EV-2026-08-10-703` T5 sinyali tam bunu ima ediyor: zincir/tekelde
450–650 TL), bantlar **yanlış yere** kurulmuş olur ve B3 (PRIMARY 799) tarama
zamanının çoğunu **rafın üst kuyruğunda** harcar.

Bu riski azaltan tek şey, sayım formunun **rafın kendi dağılımını** bant
sınırlarımızdan bağımsız olarak kaydetmesidir (en ucuz ithal, en ucuz şarap,
500 TL altı var mı). Yani tur, kendi bant tasarımını **çürütebilecek** veriyi
de topluyor. Kasıtlıdır.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

Bu belge bir **araçtır**; yanlış olması doğrudan bir yatırım kararını
değiştirmez. Ancak **iki dolaylı yol** vardır:

1. **Görev paketi yanlış tasarlanmışsa** (yanlış bant, yetersiz süre, eksik
   alan), tur yapılır ama `T-917` / `T-504` / `C-551` **kapanmaz**. O zaman
   `G3` gate'i bloke kalır, `l8_chain_retail` `null` kalır, `kanal.yaml →
   m_retail` kurulamaz ve `finans-fizibilite` **`APPROVED` olamaz**. Yani bu
   belgenin hatası, projeyi **yanlış karara değil, KARARSIZLIĞA** sürükler.
2. **Bant tasarımı, turu PRIMARY 799'un lehine yanlı hâle getirirse** — örneğin
   B3 en geniş dikkat payını aldığı için gözlemci o bandı daha titiz tararsa —
   799'un etrafında **yapay bir yoğunluk** ölçülür. Bu, `target-shelf-price-analysis.md`
   §3.3'ün `ATTRACTIVE` sınıflandırmasını **kendi kendini doğrulayan** hâle
   getirir. Bunu engellemek için §6'ya *"bandı aşağıdan yukarı tara"* kuralı ve
   §5'e **bant-bağımsız sayım formu** konmuştur.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| Kim | Ne | Süre | Maliyet |
|---|---|---|---|
| **Kurucu / insan gözlemci** | 4 mağaza (Metro + 3 zincir), ≥2 bölge/şehir, `saha-gorev-paketi.md` ön sayfası | **~yarım gün** (2 sa 10 dk raf + yol) | ~600 TL (1–2 şişe + kasa fişi) + yol |
| Aynı kişi | Tekel bayii (5. durak) — yalnızca ithal satır eşiği tutmazsa | +20 dk | — |
| Aynı kişi | **İkinci ziyaret** — yalnızca promosyon işareti bulunamazsa | +10 dk, **2–4 hafta sonra** | — |
| `turkiye-pazar-kasifi` | Satırların `raf-fiyat-gozlemleri.csv`'ye taşınması, mağaza başına kanıt kartı, `pazar.yaml` **önerisi** | 1 ajan turu | — |
| `yatirim-komitesi-baskani` | `pazar.yaml` merge kararı, `T-917` kapanışı | — | — |

**En hızlı kısmi doğrulama (30 dakika):** yalnızca **1. durak Metro**.
Tek başına `C-551`'i (KDV ibaresi), `OQ-001`'in mağaza/şehir ayağını ve
— işaret bulunursa — `T-504`'ü kapatabilir. `l8_chain_retail` için yetmez.

---

## 10. TESLİM EDİLENLER

| Dosya | Ne |
|---|---|
| `60-pazar/saha-gorev-paketi.md` | **Ana çıktı** — tek sayfalık operasyon görevi (§0–§14) + gerekçe eki (EK-A…EK-D) |
| `60-pazar/saha-veri-sablonu.csv` | 44 kolon; `TEST_FIXTURE` satırı **korundu**, 12 zorunlu alanı kolonlara bağlayan **şema satırı** eklendi |
| `60-pazar/rapor-tur325-turkiye-pazar.md` | Bu rapor |
| `99-ops/tickets/T-917.md` | Statü güncellemesi — **OPEN kalır**, insan aksiyonu bekliyor |

**Dokunulmayanlar (doğrulanmıştır):** `10-evidence/index.csv`,
`99-ops/capraz-ipuclari.md`, `99-ops/celiskiler.md`, `99-ops/acik-sorular.md`,
`99-ops/tickets/INDEX.md`, `80-model/`, `60-pazar/raf-fiyat-gozlemleri.csv`,
`50-sourcing/`, `70-kanal/`. `git` çalıştırılmamıştır.
