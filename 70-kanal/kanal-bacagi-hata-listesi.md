# KANAL BACAĞINDA YAPILMASI EN MUHTEMEL HATALAR — `K1`…`K12`

```yaml
belge:            kanal-bacagi-hata-listesi
sahibi:           kanal-marj-uzmani
tur:              TUR 3A
tarih:            2026-08-10
tip:              SPESIFIKASYON — ters-model-vergi-bacagi.md §6'nin KANAL KARSILIGI
tuketici:         finans-fizibilite (test mimarisi), seytanin-avukati (saldiri vektorleri)
tetikleyen:       T-943
karsilik:         30-vergi-gumruk/ters-model-vergi-bacagi.md §6 (H1..H6)
yeni_arastirma:   YOK
yeni_evidence:    YOK
durum:            SUBMITTED
```

> **Bu belge kanıt değil, SPESİFİKASYON üretir.** Hiçbir yeni marj değeri,
> bandı veya oranı içermez. İçerdiği bütün TL rakamları, **tek bir
> illüstratif taban** üzerinde hesaplanmış **hata büyüklükleridir** —
> fiyat değildir.

---

## 0. İLLÜSTRATİF TABAN (bütün TL bedelleri bu tabanda ölçülmüştür)

```
TGT_799 · Ispanya · CHAIN RETAIL · BASE · 5.000 sise · DOC_OK (g=0,50) · lambda=1

  L8_gross     = 799,0000  (INVESTOR_ASSUMPTION — bir fiyat DEGIL, bir HEDEF)
  v            = 0,20      (SEMBOLIK — vergi.yaml alani)
  m_retail     = 0,25      (ASSUMPTION, margin on selling price)
  d            = 0,08      (ASSUMPTION)
  f            = 0,00      (UNKNOWN -> 0 alindi)   |  bazi hatalarda f = 6,00 kullanilir
  mu           = 0,00      (INVESTOR_DECISION_REQUIRED)
  -----------------------------------------------------------------------
  L8_net       = 665,8333    L7_eff = 499,3750    L6 = 542,7989
  L5 kalemleri =  36,6772    OTV    =  53,4519    MAX_CIF = 272,8306
```

**Dönüşüm sabiti:** `L5`'te her **±1 TL/şişe** → `MAX_CIF`'te
**∓0,6667 TL** (g=0,50) / **∓0,5882 TL** (g=0,70).

---

## `K1` — ⛔ **GÖZLENDİ.** `L6`'yı ithalatçının net hasılatı sanmak

```
YANLIS:   L5_max = L6 * (1 - mu)
DOGRU:    L5_max = L7_eff - mu_kesintisi        ;  L7_eff = L6*(1-d) - f
```

**Mekanizma:** `d` ve `f` **ithalatçının ödediği** bedellerdir (perakendeci
→ ithalatçı **hizmet faturası**, `EV-2026-08-10-612`). `L6` bir **fatura
fiyatıdır**, bir hasılat değildir.

**Kapalı form:** `hata = d·L6 + f` → `MAX_CIF` sapması `= (d·L6 + f)/(1+g)`

| `d` | `f` | `L5` hatası | `MAX_CIF` hatası (g=0,50) |
|---|---|---|---|
| %3 | 0 | 15,44 | **+10,30** |
| **%8** | **0** | **43,42** | **+28,95** ← *fiilen gözlendi* |
| %8 | 6,00 | 49,95 | **+33,30** |
| %18 | 15,00 | 127,91 | **+85,27** |

**Yön:** **projenin LEHİNE** (tavanı yükseltir) → gözden kaçması **daha
olasıdır.** `H1`'in tersi (o muhafazakâr görünüyordu).

**YAKALAYACAK TEST:** **`R8-K` round-trip** — **ama `T-942`'de yazılan
hâliyle DEĞİL** (bkz. aşağıdaki kutu). Doğru geri inşa:

```
K1  L7_eff_geri = L5_max + mu_kesintisi        <-- L5_max'in karsiligi L7_eff'TIR
K2  L6_geri     = (L7_eff_geri + f)/(1-d)      [bilgi; assertion'da KULLANILMAZ]
K3  L8_net_geri = L7_eff_geri / (1 - m)
K4  L8_geri     = L8_net_geri * (1 + v)
assert |L8_geri - L8_target| < 0,01
```
Sapmanın kapalı formu: `(d·L6 + f) · (1+v)/(1−m)`
→ `d=%8, f=0`'da **+69,48 TL** · `d=%8, f=6,00`'da **+79,91 TL**.
→ **`TVK-N1`**

> ### ⛔ `T-942`'DEKİ `R8-K` SPESİFİKASYONU **TERSTEN ÇALIŞIR** — DÜZELTME
>
> `T-942` şunu yazıyor:
> `adim K1 : L6_geri = (L5_max + mu * L6)`
>
> **`L5_max + μ·L6` `L6`'ya değil `L7_eff`'e eşittir.** Etiket yanlıştır ve
> `K2`'de bir kez daha `×(1−d) − f` uygulandığı için **`d` ve `f` iki kez
> düşülür.** Sonuç, testin **tam tersine dönmesidir**:
>
> | Formül | `L8_geri` | Sonuç |
> |---|---|---|
> | **DOĞRU** `L5_max = L7_eff` | **735,08** | ⛔ **REDDEDİLİR** *(yanlış!)* |
> | **NAİF** `L5_max = L6` | **799,00** | ✅ **KABUL EDİLİR** *(yanlış!)* |
>
> Yani `T-942`'nin assertion'ı **birebir kodlanırsa `R5` düzeltmesini
> geri alır ve `−28,95 TL`'lik hatayı MÜHÜRLER.** → **`T-619`**
> *(`T-942` bir teşhis ticket'ıdır ve teşhisi doğrudur; hatalı olan tek
> şey önerilen assertion'ın `K1` adımının etiketidir.)*

---

## `K2` — margin ↔ markup karışıklığı *(önlendi, ama `μ` için önlenmedi)*

```
YANLIS:   L7_eff = L8_net / (1 + m)
DOGRU:    L7_eff = L8_net * (1 - m)
```

**Büyüklük:** `L8_net·[1/(1+m) − (1−m)] = L8_net·m²/(1+m)`

| `m` | `L7_eff` hatası | `MAX_CIF` hatası |
|---|---|---|
| %18 | +18,28 | **+12,19** |
| **%25** | **+33,29** | **+22,19** |
| %35 | +60,42 | **+40,28** |

**Durum:** `m_retail` ve `k_horeca` için **YAPILMAMIŞTIR** ✅
(`marj-vs-markup.md` sayesinde). **AMA `μ` için hiç sorulmamıştır** —
`kanal-katman-matrah-haritasi.md` §6.2: `μ=%30`'da margin↔markup farkı
**23,05 TL/şişe**, matrah farkından (8,69 TL) **büyüktür.**

**YAKALAYACAK TEST:** `R8-K` (`TVK-N2`) + **`μ` için ayrı vektör**
`TVK-P1/P2/P3`.

---

## `K3` — ⛔ **GÖZLENİYOR.** `UNKNOWN` olanı `0` almanın **kanallar arası karşılaştırmayı** bozması

**Mekanizma:** `d` yalnızca zincir için tanımlıdır. Tekel ve HoReCa'da
`0` alınmıştır. Sonuç: **tekel tavanı zincirden %11,4 yüksek** ve farkın
**tamamı** bu tercihten geliyor (`T-856`).

**Ama gerçek hata daha derindir** (`kanal-katman-matrah-haritasi.md` §4.2):
tekelde `d`'nin **hukuki karşılığı gerçekten yoktur**; yükü **üç ayrı
satıra** düşer ve **üçü de modelde `0`'dır**:
`net fiyat iskontosu` · `kılcal dağıtım maliyeti` · `şüpheli alacak`.

| Kanal | Modeldeki `0` sayısı | Tavanın yapay yüksekliği |
|---|---|---|
| CHAIN RETAIL | 1 (`f`) | düşük |
| **INDEPENDENT/TEKEL** | **3** (`d`, dağıtım, alacak) | **+%11,4** *(ölçülen alt sınır)* |
| **HoReCa** | **4** (`d`, dağıtım, alacak, aktivasyon) | **ölçülmedi** |

**Yön:** projenin **LEHİNE**; ve **en çok en zayıf kanıtlı kanalı** kayırır.

**YAKALAYACAK TEST:** **`ZERO_PARITY` kontrolü** — iki kanalın `MAX_CIF`'i
karşılaştırılmadan önce engine, **her iki kanalda `UNKNOWN→0` alınan kalem
sayısını** saymalı ve **eşit değilse çıktıya
`KANALLAR_KARSILASTIRILAMAZ` bayrağı** basmalıdır. → **`TVK-N5`**

---

## `K4` — Kanal çarpanının **yanlış katmana** uygulanması *(önlendi)*

```
YANLIS:   L7_horeca = L8_net / k   uygulanirken k'nin L8 CARPANI oldugu varsayilirsa
DOGRU:    kanal.yaml -> k_horeca_carpan.katmanlar = "L7 -> L8_HORECA"  (matrah L7_eff)
```

**Büyüklük:** `k`'yı `L8` üzerinden uygulamak (`L7 = L8_net·k` yerine
`L8_net/k`) — `k=3`'te `L7_eff` **9 kat** sapar. Kaynağın kendisi iki
farklı matrah verir (`EV-2026-08-10-618`: *"perakende fiyatının 2 katı"*
**vs** *"toptan fiyatının 2,5 katı"*).

**Durum:** modelde **DOĞRU** uygulanmıştır ✅ (`ters_model.py:267`).
**Kaynaktaki belirsizlik `C-602`'de açıktır ve çözülmemiştir.**

**YAKALAYACAK TEST:** her çarpan girdisinde `katmanlar` alanının **zorunlu
ve boş olamaz** olması; engine `katmanlar` yoksa **`UNKNOWN` dönmelidir.**

---

## `K5` — ⛔ **GÖZLENİYOR.** `μ` / distribütör marjının **matrahının** tanımsız bırakılması

**Mekanizma:** `ters_model.py:392` `l5_max = l7 - mu * l6` — matrah `L6`
seçilmiş, **hiçbir belgede gerekçelendirilmemiş**, ve tüm baz koşularda
`μ=0` olduğu için **hiç test edilmemiştir** (`T-944`).

**Ölçülen büyüklük** (`kanal-katman-matrah-haritasi.md` §6.2):

| `μ` | `L6` matrahı | `L7_EFF` matrahı | `L5_MARKUP` matrahı | **yayılım** |
|---|---|---|---|---|
| %10 | 236,64 | 239,54 | 242,63 | **5,92 TL** |
| %20 | 200,46 | 206,25 | 217,34 | **16,89 TL** |
| %30 | 164,27 | 172,96 | 196,00 | **31,73 TL** |
| %50 | 91,90 | 106,37 | 161,86 | **69,96 TL** |

**Yön:** mevcut seçim (`L6`) **üçünün en muhafazakârıdır** → hata
projenin **ALEYHİNE**. Ama yatırımcı *"maliyetin üstüne %30"* kastediyorsa
model onun talebini **%19,3 daha ağır** uygular. **`T-851` bu düzeltmeden
önce cevaplanamaz.**

**YAKALAYACAK TEST:** `importer_katki_matrahi` **engine tarafından okunan
zorunlu bir alan** olmalı; `null` ise engine **`UNKNOWN` dönmeli**,
varsayılana düşmemelidir. + `TVK-P1/P2/P3` (üç matrah, aynı `μ`).

---

## `K6` — ⛔ **AYNI KALEMİN İKİ KEZ TEMSİL EDİLMESİ** *(hiç sorulmamıştı)*

Kanal bacağında **dört ayrı çift sayım kanalı** vardır. Hiçbiri
taranmamıştır.

| # | Çift sayan iki satır | Büyüklük | Durum |
|---|---|---|---|
| **K6a** | **`d` içindeki lojistik bedeli** ↔ **`L5`'teki TR-içi lojistik** (`EV-2026-08-10-329`) | 5.000 şişede `L5` bacağı 3,99 TL/şişe; `d` bacağı **UNKNOWN** | **`T-618`** · `B-13` |
| **K6b** | **`d` (ciro primi)** ↔ **vade finansman maliyeti** (erken ödeme iskontosu her ikisinde de görünebilir) | ikisi de bugün ya `d`'de ya `0` | `T-614` |
| **K6c** | **üreticiden alınan "marka/pazarlama katkısı"** (RFQ 5.6, `İP 5.1`) ↔ **`f` listeleme bedeli** | aynı para hem gelir hem gider | **`T-605` açık** |
| **K6d** | ⛔ **MODEL A'da `m_dist` ↔ `d` + `f`** — distribütör kullanılıyorsa zincir bedellerini **distribütör** öder | **28,95 TL/şişe** (`d`=%8) | **`C-611`** · `T-617` |

**`K6d` en büyüğü ve en yenisidir.** `reverse-price-model.md` §7.1
distribütör gridini `d=%8` üzerinde koşturmakta ve *"aynı anda ikisi
birden uygulanırsa TOPLANIRLAR"* demektedir. **Toplanmaları gerektiği
kanıtlanmamıştır**; sözleşmeye bağlıdır.

**Yön:** `K6a`–`K6c` **aleyhte** (fazla düşülür), **`K6d` aleyhte**
(tavan 28,95 TL düşük çıkar). Yani çift sayım **modeli aşırı kötümser**
yapar — bu, `R5`'in aynadaki görüntüsüdür.

**YAKALAYACAK TEST:** **`LEDGER_UNIQUENESS` kontrolü** — her ekonomik
kalem, çıktının kalem defterinde (`l5_kalemleri` + `d` sepeti + `f`)
**tam bir kez** görünmelidir. Engine bir `kalem_kimligi` etiketi taşımalı
ve **aynı kimlik iki farklı satırda düşülüyorsa `CIFT_SAYIM` hatası**
vermelidir. MODEL A için ayrıca **`A1` (d bizde) / `A2` (d distribütörde)
iki senaryo zorunlu**. → **`TVK-N6`**

---

## `K7` — ⛔ **`f` SABİT OLDUĞU HÂLDE ŞİŞE BAŞINA DEĞİŞKEN GİBİ TAŞINMASI** *(hiç sorulmamıştı)*

```
YANLIS:   f_per_bottle bir GIRDIDIR ve hacim senaryolari arasinda SABIT KALIR
DOGRU:    f_per_bottle = F_total / Q      <- TUREVDIR; Q degisince DEGISIR
```

**Mekanizma:** listeleme bedeli **dönem başına sabit bir TL tutarıdır**
(SKU × zincir/mağaza × süre). Şişe başına değeri **hacme bölünerek**
doğar ve **hiperboliktir**, doğrusal değil.

**Büyüklük** (`F_total = 300.000 TL` — **illüstratif, kanıt DEĞİL**):

| `Q` | `f_per_bottle` | `MAX_CIF` etkisi | 5.000'e göre |
|---|---|---|---|
| **5.000** | **60,00** | **−40,00** | — |
| 10.000 | 30,00 | −20,00 | +20,00 |
| 25.000 | 12,00 | −8,00 | +32,00 |
| 100.000 | 3,00 | −2,00 | **+38,00** |

**Karşılaştırma:** hacim ekseninin bugünkü modeldeki toplam etkisi
(5.000→100.000) **+20,20 TL**'dir (`reverse-price-model.md` §8.1).
**`f` tek başına o eksenin iki katı büyüklüğünde bir ölçek etkisi
yaratır ve bugün `0` alındığı için TAMAMEN GÖRÜNMEZDİR.**

> **Aynı hata `d` içinde de saklıdır** (`K8`): sepetin sabit bileşenleri
> (alan kullanımı, enerji, CRM) da `TOTAL/Q` davranışındadır.

**Yön:** projenin **LEHİNE** — ve **özellikle pilot (5.000 şişe)
senaryosunda**, yani karar için en kritik hücrede.

**YAKALAYACAK TEST:** **`SCALE_MONOTONICITY` kontrolü** — engine
`f_per_bottle`'ı **girdi olarak reddetmeli**, yalnızca `F_total` + `Q`
kabul etmelidir. Ek assertion: `f_per_bottle(Q1)·Q1 == f_per_bottle(Q2)·Q2`
(sabit toplam). → **`TVK-P4`**

---

## `K8` — ⛔ **`d`'nin HOMOJEN SANILMASI** *(yeni)*

**Mekanizma:** `EV-2026-08-10-612`'nin altı kaleminin **en az üçü sabit
tutarlıdır** (alan kullanımı, soğutucu enerji, CRM sabit kısmı), biri
**başka bir hacme** oranlıdır (kırık ürün bedeli → kırılan adet), biri
**`L8` matrahlı olabilir** (CRM/B2B "kasa çıkışı cirosu"). Model altısını
da tek bir `d` yüzdesiyle, `L6` matrahında taşımaktadır.

```
YANLIS:   L7_eff = L6*(1-d) - f
DOGRU:    L7_eff = L6*(1-d_var) - f - D_fix/Q
```

**Büyüklük:** `d = %8`'in yarısı sabit bileşense (`d_var=%4`,
`D_fix = 0,04×L6×Q_plan`):

| `Q_gerçek / Q_plan` | tek-`d` temsili | ayrışmış temsil | **hata** |
|---|---|---|---|
| 1,0 (plan tutuyor) | 43,42 | 43,42 | 0 |
| **0,5 (hacim yarısı)** | 43,42 | **65,13** | **−21,71 TL/şişe** → `MAX_CIF` **+14,47** |
| 2,0 | 43,42 | 32,57 | +10,85 → `MAX_CIF` −7,23 |

**Yön:** projenin **LEHİNE** — çünkü **hacim hedefin altında kaldığında**
gerçek yük artar ve tek-`d` temsili bunu **tanım gereği göremez.**
Bu, **plan riskini modelden tamamen silen** bir temsil hatasıdır.

**YAKALAYACAK TEST:** `kanal.yaml`'da `d` **tek skaler olarak kabul
edilmemeli**; `d_var` + `D_fix` iki ayrı alan olmalı ve engine `d`
skalerini okursa **`BLOCKED` uyarısı** basmalıdır. → **`TVK-P4`** ile
aynı ailede.

---

## `K9` — ⛔ **KANALLARIN KARŞILAŞTIRILABİLİR SANILMASI / KARMA OLMADAN AĞIRLIKLANDIRMA** *(yeni)*

**Üç ayrı alt hata:**

| # | Hata | Kanıt / durum |
|---|---|---|
| **K9a** | HoReCa sütununu zincir sütunuyla **aynı ürün konumlandırması** sanmak | `reverse-price-model.md` §5.2 uyarıyı **yazmış** ✅ — ama tabloda üç kanal **yan yana** duruyor |
| **K9b** | Kanal `MAX_CIF`'lerini **alternatif** sanmak (`K3`: eşit olmayan sıfır sayısı) | **`T-856`** |
| **K9c** | Tek kanalın tavanını **tüm hacme** uygulamak — `kanal_karmasi` üç alanın **üçü de `null`** | `kanal.yaml → kanal_karmasi` **UNKNOWN** |

**Büyüklük (`K9c`):** ağırlıklı ortalama tavan, karma bilinmeden
**hesaplanamaz**. `TGT_799 · BASE`'te üç kanalın tavanı
**272,83 / 303,90 / 87,88** — yani karma varsayımı **tek başına tavanı
3,5 kat oynatabilir.** Bu, tornado'nun **hiçbir ekseninde yoktur.**

**Yön:** ↕ — ama **en büyük tek belirsizlik** olabilir ve **ölçülmemiştir.**

**YAKALAYACAK TEST:** engine, `kanal_karmasi` toplamı 100 değilse veya
herhangi biri `null` ise **birleşik (blended) çıktı ÜRETMEMELİ**, yalnızca
kanal bazında çıktı vermeli ve **`KARMA_UNKNOWN`** bayrağı basmalıdır.
Ayrıca: **`Σ pay = 100`** assertion'ı. → **`TVK-N7`**

---

## `K10` — ⛔ **KDV TABANI KARIŞMASI (kanal kalemlerinde)** *(yeni)*

`marj-vs-markup.md` §2.3 oransal marjın KDV'den etkilenmediğini doğru
saptamıştır. **Ama mutlak tutarlı kalemler için bu koruma YOKTUR:**

```
f, D_fix, kirik urun bedeli, yatirim destegi = TL TUTARLARIDIR
-> KDV'li mi KDV'siz mi faturalandigi, marji ORANSAL DEGIL MUTLAK kaydirir
```

**Büyüklük:** `f + d·L6 = 43,42 TL/şişe` (`f=0`, `d=%8`) → yanlış tabanda
alınırsa **±8,68 TL/şişe**, `MAX_CIF`'te **±5,79 TL**.
`f = 60 TL` (5.000 şişe senaryosu) eklenirse **±20,68 TL/şişe**,
`MAX_CIF`'te **±13,79 TL**.

**Ek katman:** bu tutarların KDV'sinin **indirilebilir olup olmadığı**
`BLOCKED`'dır (`B-1`, `T-611`). İndirilemezse ekonomik maliyet **1,20
katıdır** — bu bir tabana çevirme hatası değil, **gerçek bir maliyet
artışıdır**.

**Yön:** ↕ ama **indirilemezlik hâlinde tek yönlü aleyhte.**

**YAKALAYACAK TEST:** her mutlak tutarlı kalem için `kdv_dahil_mi` alanı
**zorunlu**; boşsa engine **`UNKNOWN` dönmeli**, "muhtemelen hariçtir"
varsayımına düşmemelidir. → **`TVK-N3`**

---

## `K11` — ⛔ **SATILAN ŞİŞE ≠ İTHAL EDİLEN ŞİŞE** *(yeni)*

**Mekanizma:** model bütün sabit maliyetleri (ruhsat 30,17 TL/şişe @5.000,
`f`, `D_fix`) **ithal edilen** adede böler ve **hasılatı da aynı adet
üzerinden** kurar. Gerçekte:

```
maliyet tasiyan adet  = Q            (ithal edilen)
hasilat ureten adet   = Q * (1 - r)  (iade + fire + kirik dusuldukten sonra)
```

**Büyüklük:** iade/fire oranı `r`:

| `r` | Sabit maliyet şişirmesi | `L5` etkisi (@5.000, sabitler 36,68 TL) | + iade hasılat kaybı `r·L6` | **`MAX_CIF` toplam etki** |
|---|---|---|---|---|
| %2 | ×1,0204 | −0,75 | −10,86 | **−7,74** |
| **%5** | ×1,0526 | **−1,93** | **−27,14** | **−19,38** |
| %10 | ×1,1111 | −4,07 | −54,28 | **−38,90** |

*(iade kaybı burada `geri_kazanılabilir_değer = 0` ile, yani üst sınırla
hesaplanmıştır — gerçek değer `B-11` gereği `BLOCKED`'dır.)*

**Ek olarak:** zayi olan malın **KDV'si indirilemez** (KDVK md.30/c,
`Ci-15.1`, `EV-2026-08-10-103`) → kaybın üstüne **ayrıca** KDV biner.
Ve **kırık ürün bedeli** sözleşmeyle **bize** yansıtılmaktadır
(`EV-2026-08-10-612`).

**Yön:** projenin **LEHİNE** ve büyüklüğü `%5`'te **`R5` hatasının
(28,95 TL) mertebesinde (19,38 TL)** — yani modelin bilinen en büyük
kanal hatasıyla aynı sınıfta bir kalem **bugün tamamen `0`'dır**
(`reverse-price-model.md` §0.2 #8: *"Fire/zayi oranı — 0 alındı, RC5
açığı, `T-314`"*).

**YAKALAYACAK TEST:** engine iki ayrı adet alanı taşımalı
(`Q_ithal`, `Q_satilan`) ve **sabit maliyet bölmesinde `Q_ithal`,
hasılat hesabında `Q_satilan`** kullanmalıdır. `r = 0` girildiğinde
çıktıya **`FIRE_SIFIR_VARSAYILDI`** uyarısı basmalıdır.
→ **`TVK-P5`**

---

## `K12` — ⛔ **VADENİN NE MARJDA NE MALİYETTE GÖRÜNMEMESİ + YANLIŞ MATRAH** *(yeni)*

**İki ayrı hata:**

**K12a — matrah:** alacak tutarı `L6` değil **`L6_gross = L6·(1+v)`**'dir.
`TGT_799 · BASE`: `542,80` yerine **`651,36` TL/şişe**.
`peak_cash` alacak bacağı `L6` üzerinden kurulursa **%20 eksik** çıkar.

**K12b — hiç yok:** kanal alacağının finansman maliyeti modelde **`0`**'dır.

**Büyüklük** (`L6_gross = 651,36`, yıllık finansman oranı `i` — **`makro.yaml`
`null`, bu ajanın alanı değil**, sembolik olarak Migros'un kendi borçlarını
iskonto ettiği **%38,6**, `EV-2026-08-10-617`):

| Vade | `L6` matrahı (yanlış) | **`L6_gross` matrahı (doğru)** | `MAX_CIF` etkisi |
|---|---|---|---|
| 45 gün | −25,82 | **−30,99** | −20,66 |
| **60 gün (BASE)** | −34,43 | **−41,32** | **−27,55** |
| 90 gün | −51,65 | **−61,98** | −41,32 |
| **120 gün (STRESS)** | −68,86 | **−82,64** | **−55,09** |

> **60 → 120 gün geçişi tek başına `MAX_CIF`'i 27,55 TL daha düşürür.**
> Bu, `R5` hatasıyla **aynı mertebededir** ve **tornado'da hiç yoktur.**
> Matrah hatası (`L6` vs `L6_gross`) tek başına **6,89 TL/şişe**'dir.

**Çift sayım uyarısı:** finansman maliyeti **ya** ayrı bir `L5` satırı
olur **ya da** `d` içinde erken ödeme iskontosu olarak görünür.
**İkisi birden olursa `K6b`.**

**Yön:** projenin **LEHİNE** (bugün `0`).

**YAKALAYACAK TEST:** engine, `odeme_vadesi_gun > 0` **ve**
`makro.finansman_orani == null` ise **`VADE_MALIYETI_MODELLENMEDI`
uyarısı** basmalı; ayrıca alacak matrahının `L6_gross` olduğunu
assertion ile doğrulamalıdır (`alacak == L6*(1+v)`). → **`TVK-P6`**

---

## ÖZET — HATA MATRİSİ

| # | Hata | Gözlendi mi | Yön | Büyüklük (TL/şişe, `MAX_CIF`) | Yakalayan test |
|---|---|---|---|---|---|
| **K1** | `L6` ≠ net hasılat | ✅ **OLDU** | **lehe** | **+28,95** | `R8-K` / `TVK-N1` |
| **K2** | margin ↔ markup | ⚠ `μ` için **açık** | lehe | +22,19 (`m`) · +23,05 (`μ`) | `R8-K` / `TVK-N2`, `TVK-P1-3` |
| **K3** | `UNKNOWN→0` kanal asimetrisi | ✅ **OLUYOR** | **lehe** | tekelde **+%11,4** | `ZERO_PARITY` / `TVK-N5` |
| **K4** | çarpanın yanlış katmanı | ❌ önlendi | — | ×9'a kadar | `katmanlar` zorunlu alan |
| **K5** | `μ` matrahı tanımsız | ✅ **OLUYOR** | **aleyhe** | 5,92 … **69,96** | `TVK-P1/P2/P3` |
| **K6** | çift sayım (4 kanal) | ⚠ **taranmadı** | aleyhe | **K6d: 28,95** | `LEDGER_UNIQUENESS` / `TVK-N6` |
| **K7** | `f` sabit ↔ değişken | ⚠ **taranmadı** *(`f=0`)* | **lehe** | **38,00** (5k↔100k) | `SCALE_MONOTONICITY` / `TVK-P4` |
| **K8** | `d` homojen sanılıyor | ⚠ **yeni** | **lehe** | +14,47 (hacim ½) | `d_var` + `D_fix` ayrımı |
| **K9** | kanallar karşılaştırılamaz / karma yok | ⚠ **yeni** | ↕ | tavan **3,5×** oynayabilir | `KARMA_UNKNOWN` / `TVK-N7` |
| **K10** | KDV tabanı (mutlak kalemler) | ⚠ **yeni** | ↕ | ±5,79 … ±13,79 | `kdv_dahil_mi` zorunlu / `TVK-N3` |
| **K11** | satılan ≠ ithal şişe | ⚠ **yeni** | **lehe** | **−19,38** (`r`=%5) | `Q_ithal` ≠ `Q_satilan` / `TVK-P5` |
| **K12** | vade: matrah + hiç yok | ⚠ **yeni** | **lehe** | **−27,55** (60g) | `L6_gross` assertion / `TVK-P6` |

> ### İKİ OKUMA
>
> **1. Yönlerin dağılımı `H1`–`H6`'nın TERSİDİR.** Vergi bacağında
> hataların çoğu **muhafazakâr** görünüyordu; kanal bacağında **12
> hatanın 6'sı projenin LEHİNE** çalışıyor (`K1`, `K3`, `K7`, `K8`,
> `K11`, `K12`). **Lehe çalışan hata, aleyhe çalışandan daha uzun yaşar.**
>
> **2. Bugün `0` alınan kanal kalemlerinin toplam mertebesi.**
> `K7` (38,00) + `K11` (19,38) + `K12` (27,55) ≈ **85 TL/şişe** —
> `TGT_799 · CHAIN · BASE` tavanının (**272,83**) **%31'i.**
> Hiçbiri kanıtlı değildir ve hiçbiri modele konmamıştır.
> **Konmaması bir seçimdir ve bu seçim projenin lehinedir.**

---

## BİRİM TEST VEKTÖRLERİ — `finans-fizibilite` İÇİN (`T-943` kriter 5)

> Bunlar `TV-1`…`TV-10`'un (vergi bacağı) **kanal karşılığıdır**.
> Beklenen değerler **`kanal.yaml`'dan okunmalı**, koda gömülmemelidir.
> Taban: §0. **`N` = negatif vektör (hatalı formül REDDEDİLMELİDİR).**

| # | Girdi | Beklenen | Ne kanıtlar |
|---|---|---|---|
| **TVK-1** | `L8=799, v=0,20, m=0,25, d=0,08, f=6,00, μ=0` | `L8_net=665,8333` · `L7_eff=499,3750` · `L6=549,3207` · `L5_max=499,3750` | temel zincir |
| **TVK-2** | `R8-K` geri inşa (TVK-1 çıktısından) | `L8_geri = 799,0000` · `\|Δ\|<0,01` | round-trip kapanıyor |
| **TVK-3** | HoReCa: `L8=799, k=3,0` | `L7_eff = L6 = 221,9444` | çarpan matrahı `L7_eff` |
| **TVK-4** | `f=0` ve `d=0` (tekel) | `L6 == L7_eff` **tam eşit** | `d`/`f` yokken köprü kapanır |
| **TVK-N1** | **naif `R5`:** `L5_max = L6·(1−μ)` | ⛔ **`R8-K` REDDETMELİ**; `L8_geri = 878,91` (`Δ = +79,91`) | `K1` |
| **TVK-N1b** | `T-942`'nin **birebir** `R8-K` spesifikasyonu (`L6_geri = L5_max + μ·L6`) | ⛔ **DOĞRU formülü reddeder, NAİF formülü kabul eder** → spesifikasyon **düzeltilmeli** | `T-619` |
| **TVK-N2** | **markup karışıklığı:** `L7_eff = L8_net/(1+m)` | ⛔ **`R8-K` REDDETMELİ**; `L8_geri − 799 = +53,27` | `K2` |
| **TVK-N3** | `f` girildi ama `kdv_dahil_mi` **boş** | ⛔ engine **`UNKNOWN`** dönmeli (varsayıma düşmemeli) | `K10` |
| **TVK-N5** | `CHAIN` (1 sıfır) vs `TEKEL` (3 sıfır) karşılaştırması | ⛔ **`KANALLAR_KARSILASTIRILAMAZ`** bayrağı | `K3` |
| **TVK-N6** | MODEL A: `m_dist=0,15` **ve** `d=0,08` aynı anda, `d_kimde` **boş** | ⛔ engine **`A1`/`A2` seçimi olmadan çalışmamalı** | `K6d` |
| **TVK-N7** | `kanal_karmasi` üçü de `null`, birleşik çıktı istendi | ⛔ **`KARMA_UNKNOWN`**, birleşik çıktı **üretilmemeli** | `K9c` |
| **TVK-P1** | `μ=0,20`, matrah **`L6`** | `L5_max=390,8152` · `MAX_CIF=200,4574` | `K5` — mevcut davranış |
| **TVK-P2** | `μ=0,20`, matrah **`L7_EFF`** | `L5_max=399,5000` · `MAX_CIF=206,2473` | `K5` |
| **TVK-P3** | `μ=0,20`, matrah **`L5_MARKUP`** | `L5_max=416,1458` · `MAX_CIF=217,3445` | `K5` — **üçü FARKLI olmalı** |
| **TVK-P4** | `F_total=300.000`; `Q=5.000` ve `Q=100.000` | `f=60,00` ve `f=3,00`; **`f·Q` sabit** | `K7`, `K8` |
| **TVK-P5** | `r=0,05` | `Q_satilan = 0,95·Q_ithal`; sabitler **`Q_ithal`**'e bölünür | `K11` |
| **TVK-P6** | `vade=60`, `makro.finansman_orani=null` | alacak `= L6·(1+v) = 651,3587`; **`VADE_MALIYETI_MODELLENMEDI`** uyarısı | `K12` |

*(`TVK-P1/P2/P3` beklenen değerleri `f=0` tabanında verilmiştir — §0 —
`reverse-price-model.md` §9.2 gridiyle çapraz doğrulanabilsin diye.
`TVK-1`/`TVK-2`/`TVK-N1`/`TVK-N2` ise `f=6,00` tabanındadır.)*

---

## `seytanin-avukati` İÇİN SALDIRI SIRASI

Bu listeyi **büyüklük × kanıtsızlık** çarpımına göre okuyun:

| Sıra | Hedef | Neden en kırılgan |
|---|---|---|
| 1 | **`K9c`** — kanal karması | Tavanı **3,5 kat** oynatabilir, tornado'da **yok**, üç alan da `null` |
| 2 | **`K7`** — `f` ölçek asimetrisi | Pilot (5.000 şişe) hücresini tek başına öldürebilir; bugün `0` |
| 3 | **`K12`** — vade finansmanı | 60→120 günde −27,55 TL; `C-601` **açık** |
| 4 | **`K11`** — fire/iade | Cam şişe + indirilemeyen KDV + kırık ürün bedeli **üçü birden** bize |
| 5 | **`K5`/`K6d`** — `μ` ve distribütör | Tornado'nun en büyük iki ekseni ve **ikisi de veri değil, karar** |
