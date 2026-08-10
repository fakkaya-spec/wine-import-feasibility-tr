# KANAL BACAĞI — KALEM × KATMAN × MATRAH HARİTASI

```yaml
belge:            kanal-katman-matrah-haritasi
sahibi:           kanal-marj-uzmani
tur:              TUR 3A — KANAL KATMAN DENETIMI
tarih:            2026-08-10
tip:              SPESIFIKASYON (kod degildir, sozlesmedir)
tuketici:         finans-fizibilite (engine), yatirim-komitesi-baskani
tetikleyen:       T-942 (kanal bacaginda dogrulama yok) · T-943 (kanal hata listesi yok) · T-944 (mu matrahi)
yeni_arastirma:   YOK — hicbir yeni dis kaynak taranmamistir
yeni_evidence:    YOK — tum atiflar mevcut evidence_id'leredir
yeni_marj_degeri: YOK — bu belge SAYI uretmez, MATRAH tanimlar
durum:            SUBMITTED
```

> ## ⛔ BU BELGE HİÇBİR MARJ **DEĞERİ** ÜRETMEZ
>
> TUR 2'de kanal ticari koşullarının **varlığı** kanıtlanmış, **tutarları**
> `UNKNOWN` bırakılmıştı (`T-604`, `EV-2026-08-10-610/-611/-612`: Rekabet
> Kurumu'nun kendi raporlarında bile oranlar **karartılmıştır**).
> Bu belge o kararı **değiştirmez**. Bu belgenin ürettiği tek şey, her
> kalemin **hangi katmanda** ve **hangi tutarın üzerinden** çalıştığının
> tanımıdır. **Bir kalemin matrahı yanlışsa, tutarı doğru olsa bile
> model yanlıştır.**

---

## 0. NEDEN BU BELGE VAR

TUR 2.5'te `finans-fizibilite` kendi hatasını yakaladı: `L5_max = L6×(1−μ)`
formülü, ithalatçının ödediği listeleme bedeli (`f`) ve ciro primini (`d`)
hiç düşmüyordu. Etkisi **−28,95 TL/şişe (−%9,6)** ve **2.700/2.700 satırda
`R8` round-trip'ten temiz geçti** (`T-942`).

Hatanın kök nedeni bir aritmetik hatası değildi. Kök neden şuydu:

> **`L6` ile `L7_eff`'in "ithalatçının hasılatı" olarak birbirinin yerine
> kullanılabileceği sanıldı — yani bir MATRAH hatası yapıldı.**

Vergi bacağında bu hata sınıfı `matrah-sirasi.md` ile kapatılmıştır. Kanal
bacağında **karşılığı yoktu.** Bu belge o boşluktur.

---

## 1. NOTASYON — BU BELGEDE KULLANILAN HER MATRAHIN ADI

| Sembol | Tanım | Katman | KDV durumu |
|---|---|---|---|
| `L8_gross` | tüketici raf fiyatı / HoReCa menü fiyatı | **L8** | **KDV DAHİL** |
| `L8_net` | `L8_gross / (1+v)` | **L8** | KDV hariç |
| `L7_eff` | ithalatçının **fiilî net hasılatı** = `L6·(1−d) − f` | **L7** | KDV hariç |
| `L6` | ithalatçı **fatura** fiyatı (mal faturasında yazan) | **L6** | KDV hariç |
| `L6_gross` | `L6 · (1+v)` — **fatura TOPLAMI = alacak tutarı** | **L6** | **KDV DAHİL** |
| `L5` | importer cost (bandrol, TADAB, ruhsat/hacim, TR lojistik dahil) | **L5** | KDV hariç |
| `v` | KDV oranı — **`gumruk-vergi-uzmani` alanı**, burada sembolik | — | — |

> ⛔ **`L7` çıplak tokeni bu belgede YASAKTIR.** Her kullanımda `L7_eff`
> yazılır. Sebebi `L4` yasağıyla aynıdır (`ters-model-vergi-bacagi.md` §1):
> `L6` ve `L7_eff` **iki ayrı sayıdır** ve aralarındaki fark (`d·L6 + f`)
> **tam olarak `R5` hatasının büyüklüğüdür.**
>
> ⛔ **`L6_gross` bu belgeyle repoya YENİ GİRMİŞTİR.** Bugüne kadar hiçbir
> belgede adı yoktu — ve **ödeme vadesinin uygulandığı tutar odur** (§3.6).

---

## 2. ZORUNLU ALAN SÖZLEŞMESİ

Bu belgedeki her kalem **on alanla** tanımlanır. Alanlardan biri eksikse
kalem `BLOCKED`'dır ve modele **sessizce sıfır olarak giremez.**

```yaml
payer:                 # kim ODER  (nakit fiilen kimin kasasindan cikar)
receiver:              # kim ALIR
layer:                 # L0..L8 — hangi katmanda / hangi katman koprusunde
basis:                 # HANGI TUTARIN uzerinden hesaplanir (matrah)
currency:              # TRY | USD | EUR
fixed_or_variable:     # FIXED (donem/SKU basi sabit) | VARIABLE (bir tutarin orani)
per_bottle_or_total:   # PER_BOTTLE | TOTAL (-> hacme BOLUNEREK sise basina gecer)
tax_treatment:         # KDV'ye tabi mi; hangi matraha girer; indirilebilir mi
evidence_id:           # yoksa modele giremez
status:                # FACT | ESTIMATE | ASSUMPTION | UNKNOWN | BLOCKED
```

**`BLOCKED` tanımı (bu belgeyle repoya giriyor):** kalemin **varlığı**
kanıtlıdır ama **katmanı veya matrahı** belirsizdir. `UNKNOWN`'dan farkı
şudur: `UNKNOWN` bir **seviyenin** bilinmemesidir; `BLOCKED` bir **denklemin
şeklinin** bilinmemesidir. **`UNKNOWN` duyarlılıkla yönetilebilir;
`BLOCKED` yönetilemez** — çünkü hangi eksene koyulacağı bile bilinmez.

---

## 3. KANAL A — CHAIN RETAIL (zincir market / cash & carry)

### 3.1 `m_retail` — perakendeci marjı

```yaml
kalem:                 m_retail (margin basis)
payer:                 tuketici (raf fiyatina gomulu; bir NAKIT CIKISI degil, bir FIYAT FARKIDIR)
receiver:              zincir perakendeci
layer:                 L7 -> L8   (katman KOPRUSU; tek bir katmanin uzerinde durmaz)
basis:                 L8_net     # <-- MARGIN ON SELLING PRICE: SATIS uzerinden
currency:              TRY
fixed_or_variable:     VARIABLE
per_bottle_or_total:   PER_BOTTLE (oran)
tax_treatment:         Kendisi KDV'ye tabi bir kalem DEGILDIR (fatura edilmez).
                       Hesaplandigi iki bacak da KDV HARIC olmak ZORUNDADIR.
evidence_id:           EV-2026-08-10-616 (capa; TUM KATEGORI, sarap DEGIL)
status:                ASSUMPTION (sarap icin UNKNOWN — EV-2026-08-10-611: alkol
                       resmi marj analizinin kapsami DISI ve karartilmis)
```

**MATRAH DENETİMİ — `ters_model.py:277` ✅ DOĞRU:**
```python
l7 = l8_net * (Decimal("1") - kanal.m_retail)
```
`L7_eff = L8_net·(1−m)` → `m` **satış üzerinden**. `L8_net/(1+m)` yazılsaydı
`m` markup olurdu ve `TGT_799 · BASE`'te `L7_eff` **499,375 yerine 532,667**
çıkardı (**+33,29 TL/şişe**, `MAX_CIF`'te **+22,19 TL**). **Bu hata
YAPILMAMIŞTIR** (`K2` önlendi — `marj-vs-markup.md` sayesinde).

**Ancak bir sınır vardır:** `m` **brüt** marjdır (satışların maliyeti
düşülmüş, faaliyet gideri düşülmemiş). Zincirin **kabul edeceği** marj,
brüt marjı değil **net katkısıdır** — ve zincirin net katkısına `d` ve `f`
de girer (`EV-2026-08-10-611` metodolojisi: satın alım maliyetinden ciro
primi + aktivite primi + iade tutarı + imha bedeli + iskonto faturaları
**düşülür**). Yani:

```
zincirin_gordugu_kazanc  =  m_retail  +  d  +  f/L6
bizim_gordugumuz_yuk     =  m_retail  +  d  +  f/L6      <- AYNI SAYI
```
**`m` ile `d`'yi birbirinden bağımsız iki eksen gibi çalıştırmak,
zincirin toplam talebini iki kez serbest bırakmaktır** (bkz. `K9`).

### 3.2 `k_retail` — markup karşılığı

```yaml
kalem:                 markup basis (m'nin ayni ekonomik iceriginin IKINCI ifadesi)
payer / receiver:      m_retail ile AYNI
layer:                 L7 -> L8
basis:                 L7_eff     # <-- MARKUP ON PURCHASE PRICE: ALIS uzerinden
currency:              TRY
fixed_or_variable:     VARIABLE
per_bottle_or_total:   PER_BOTTLE (oran)
tax_treatment:         m_retail ile ayni
evidence_id:           EV-2026-08-10-616 (turetme: k = m/(1-m))
status:                DERIVED — BAGIMSIZ BIR KALEM DEGILDIR
```

> ⛔ **`m` ve `k` modele AYRI AYRI GİREMEZ.** İkisi aynı gerçeğin iki
> ifadesidir; ikisini birden düşmek **çift sayımdır.** `kanal.yaml`'da
> `markup_karsiligi_pct` alanı **yalnızca müzakere tercümesi içindir**;
> engine onu **okumamalıdır**.
>
> **Müzakere uyarısı (`marj-vs-markup.md` §1.2 gereği):** perakendeci
> "marjım %X" derken `m`'yi (L8_net matrahı), tedarikçi/distribütör
> "üstüne %X koyuyorum" derken `k`'yı (L7_eff matrahı) kasteder.
> **Aynı masada iki taraf farklı matrahtan konuşur.** Görüşme notuna
> matrah yazılmadan sayı kaydedilemez.

### 3.3 KDV — zincirdeki **üç ayrı** görünüm

KDV kanal bacağında **tek bir yerde** değil, **üç ayrı yerde** vardır ve
üçü **farklı matrahlar** üzerindedir. Model bugün yalnızca birincisini
uygulamaktadır.

| # | Görünüm | payer | receiver | layer | basis | status |
|---|---|---|---|---|---|---|
| **V1** | Raf fiyatındaki KDV | tüketici | Hazine (perakendeci üzerinden) | **L8** | `L8_net` | ✅ modelde (`R1`) |
| **V2** | Mal faturasındaki KDV | perakendeci | Hazine (ithalatçı üzerinden) | **L6** | `L6` | ⚠ **modelde YOK** |
| **V3** | Hizmet faturalarındaki KDV (`f` ve `d` üzerinde) | **ithalatçı (biz)** | Hazine (perakendeci üzerinden) | **L6→L7 köprüsü** | `d·L6 + f` | ❌ **BLOCKED** |

```yaml
# V2 — MAL FATURASI KDV'si
payer:                 zincir perakendeci (bize oder)
receiver:              Hazine (biz beyan eder ve odiyoruz)
layer:                 L6 uzerine EKLENIR -> L6_gross = L6 * (1+v)
basis:                 L6 (KDV haric fatura tutari)
currency:              TRY
fixed_or_variable:     VARIABLE
per_bottle_or_total:   PER_BOTTLE
tax_treatment:         Ekonomik maliyet DEGILDIR (tahsil edilip beyan edilir).
                       AMA NAKIT AKISINDA IKI AYRI ZAMAN VARDIR:
                         - tahsilat  : fatura + kanal vadesi (zincir BASE 60 gun)
                         - beyan     : fatura tarihini izleyen donemde
                       ARADAKI FARK BIZIM FINANSMAN MALIYETIMIZDIR.
evidence_id:           v icin EV-2026-08-09-118 (gumruk-vergi-uzmani alani)
status:                STRUCTURAL_FACT (aritmetik) / zamanlama BLOCKED -> T-614
```

> ### ⚠ BULGU V2 — **VADENİN UYGULANDIĞI TUTAR `L6` DEĞİL `L6_gross`'TUR**
> Alacak, fatura **toplamıdır**; KDV alacağın içindedir. `TGT_799 · BASE`
> illüstratif tabanında `L6 = 542,80` iken **alacak `651,36` TL/şişedir**
> (`v` sembolik %20 ile). Yani `peak_cash_requirement` alacak bacağını
> `L6` üzerinden hesaplarsa **%20 eksik** çıkar. → **`T-614`**

```yaml
# V3 — HIZMET FATURASI KDV'si  (f ve d uzerindeki KDV)
payer:                 ITHALATCI (biz) — perakendeci bize hizmet faturasi keser
receiver:              Hazine (perakendeci uzerinden)
layer:                 L6 -> L7 koprusu (L7_eff'i etkiler mi ETKILEMEZ mi: BLOCKED)
basis:                 (d * L6) + f        # hizmet bedelinin KENDISI
currency:              TRY
fixed_or_variable:     VARIABLE (bedelin orani)
per_bottle_or_total:   PER_BOTTLE (turetilmis)
tax_treatment:         ⛔ BLOCKED — indirilebilir mi? ciro primi KDV'de
                       "iskonto/matrah degisikligi" olarak mi yoksa "hizmet"
                       olarak mi islem gorur? BU BIR VERGI SORUSUDUR ve
                       kanal-marj-uzmani ALANI DEGILDIR.  -> T-611
evidence_id:           EV-2026-08-10-610 (bedeller HIZMET FATURASI ile alinir — FACT)
status:                BLOCKED
```

> **Neden `BLOCKED` ve neden önemli:** `f + d·L6` bedelinin KDV'si
> indirilebiliyorsa ekonomik maliyet **net tutardır** (model bugün böyle
> varsayıyor — ama **varsaydığını yazmıyor**). İndirilemiyorsa ekonomik
> maliyet **1,20 katıdır.** `TGT_799 · BASE`'te `d·L6 = 43,42 TL/şişe`;
> KDV'si **8,68 TL/şişe** ve `MAX_CIF` etkisi **−5,79 TL/şişe** (g=0,50).
> **Her hâlükârda bir nakit çıkışıdır** ve `peak_cash`'e girer.
> → **`T-611`** (`gumruk-vergi-uzmani`).

### 3.4 `f` — listeleme / giriş bedeli

```yaml
kalem:                 f (listing fee)
payer:                 ITHALATCI (biz)
receiver:              zincir perakendeci
layer:                 L6 -> L7 koprusu.  L6'yi DEGISTIRMEZ, L7_eff'i DUSURUR.
                       L8'de GORUNMEZ (tuketici bu bedeli gormez).
basis:                 ⛔ BIR ORAN DEGILDIR — BIR TUTARDIR.
                       Matrahi = (SKU sayisi) x (zincir VEYA magaza sayisi) x (donem)
                       Hangisi oldugu BLOCKED -> yapisal senaryolar LOW/BASE/HIGH
currency:              TRY
fixed_or_variable:     ⛔ FIXED   # <-- MODELIN EN TEHLIKELI YANLIS ANLAMASI
per_bottle_or_total:   ⛔ TOTAL   # sise basina GECIS: f_per_bottle = F_total / Q_yillik
tax_treatment:         hizmet faturasi -> KDV'ye tabi (EV-2026-08-10-610);
                       indirilebilirlik BLOCKED -> T-611
evidence_id:           yasal cerceve: EV-2026-08-10-601, -605, -608
                       TUTAR: EV-2026-08-10-619 (2004, T5) -> MODELE GIREMEZ
status:                UNKNOWN (tutar) + BLOCKED (birim: SKU x zincir mi, SKU x magaza mi)
```

> ### ⚠ `f` HACME BAĞLI BİR SAYIDIR — SABİT BİR ŞİŞE BAŞI DEĞER DEĞİLDİR
> ```
> f_per_bottle = F_total / Q_yillik          <- Q DEGISINCE f_per_bottle DEGISIR
> ```
> `F_total = 300.000 TL` (illüstratif, **kanıt değil**) örneğinde:
>
> | `Q_yıllık` | `f_per_bottle` | `MAX_CIF` etkisi (g=0,50) |
> |---|---|---|
> | 5.000 | **60,00 TL** | **−40,00 TL** |
> | 25.000 | 12,00 TL | −8,00 TL |
> | 100.000 | 3,00 TL | −2,00 TL |
>
> **Engine `f_per_bottle`'ı bir GİRDİ olarak kabul etmemelidir.** `F_total`
> ve `Q` girdi, `f_per_bottle` **türev** olmalıdır. Aksi hâlde hacim
> senaryosu değiştiğinde `f` sabit kalır ve **ölçek ekonomisi olduğundan
> büyük görünür** (`K7`).
>
> **İkinci ve daha sinsi etki — KONVEKSİTE:** `f` bir **dönem maliyetidir**;
> hacim plandan sapınca `f_per_bottle` **doğrusal değil hiperbolik** artar.
> Model `f`'yi şişe başı sabit taşırsa **hacim riski tamamen görünmez olur.**

**Yapısal ek bulgu (TUR 2'den taşınır, değişmedi):** `f`'nin hukuki
karşılığı iki hizmet grubudur — (i) tanıtım, (ii) teşhirde özel
konumlandırma (`EV-2026-08-10-605`). **Alkolde (i) fiilen satın alınamaz**
(`İP-2001`, `EV-2026-08-09-222/-223`). Yani ödediğimiz `f`'nin karşılığında
**yalnızca fiziksel raf konumu** alınabilir. Bu, `f`'yi bir pazarlama
yatırımı değil, **saf bir erişim vergisi** yapar.

### 3.5 `d` — ciro primi ve geri akan bedeller

```yaml
kalem:                 d (turnover rebate + geri akan bedeller SEPETI)
payer:                 ITHALATCI (biz)
receiver:              zincir perakendeci
layer:                 L6 -> L7 koprusu.  L6'yi DEGISTIRMEZ, L7_eff'i DUSURUR.
basis:                 L6 (KDV HARIC FATURA CIROSU)     # <-- bkz. denetim asagida
currency:              TRY
fixed_or_variable:     ⛔ KARISIK — SEPETIN TAMAMI ORANSAL DEGILDIR (bkz. §3.5.2)
per_bottle_or_total:   oransal bilesenler PER_BOTTLE; sabit bilesenler TOTAL
tax_treatment:         hizmet faturasi -> KDV'ye tabi; indirilebilirlik BLOCKED -> T-611
evidence_id:           EV-2026-08-10-612 (alkolde ISMEN, FACT) · EV-2026-08-10-610 (FMCG geneli)
status:                varlik FACT · oran UNKNOWN · SEPETIN YAPISI BLOCKED -> T-613
```

#### 3.5.1 Matrah denetimi — `L6` DOĞRU MU? ✅ EVET (gerekçeli)

`ters_model.py:280`: `l6 = (l7 + f) / (1 - d)` → yani `d·L6` düşülmüştür,
`d·L7_eff` veya `d·L8` değil.

**Gerekçe (üç ayrı dayanak):**
1. Ciro primi tanımı gereği **tedarikçinin kestiği faturaların toplamı**
   üzerinden hesaplanır — perakendecinin kendi satış hasılatı üzerinden
   değil. `EV-2026-08-10-610`: bedeller **tedarikçiden** talep edilir ve
   **tedarikçinin cirosuna oranlanır**.
2. `EV-2026-08-10-612`'deki kalemler **"müşteriye ödenecek bedeller"**
   başlığı altındadır — yani ithalatçının perakendeciye ödediği tutarlardır;
   referans büyüklük ithalatçının faturasıdır.
3. `d`'nin `L8` üzerinden hesaplandığı bir dünyada perakendeci kendi
   fiyatlama kararıyla bizim primimizi yükseltebilirdi — bu, `6585 m.6/2(c)`
   "tek taraflı değişiklik yetkisi" yasağıyla çelişirdi (`EV-2026-08-10-601`).

> ⚠ **Ama denklem döngüseldir ve bu YAZILMAMIŞTIR:** ters modelde `L6`
> **`d`'den türetilir** (`L6 = (L7_eff+f)/(1−d)`) ve `d` de `L6` üzerinden
> tanımlıdır. **Cebirsel olarak tutarlıdır** (tek çözümü vardır), ama
> müzakerede `d` **anlaşma yılının fiilî cirosuna** uygulanır — yani
> gerçekleşen hacme. **Model bunu şişe başı orana çevirerek hacim
> bağımlılığını siler.** Kademeli (tiered) prim varsa bu silme **yanlıştır**
> (bkz. §3.5.3).

#### 3.5.2 ⛔ `d` HOMOJEN DEĞİLDİR — SEPETİN EN AZ YARISI ORANSAL DEĞİL

`EV-2026-08-10-612` alkollü içki yıllık anlaşmasında **ismen** sayılan altı
kalemin **matrahları birbirinden farklıdır**:

| Sepet kalemi | Muhtemel matrah | fixed / variable | Durum |
|---|---|---|---|
| Ciro primi / yılsonu iskontosu | `L6` cirosu | **VARIABLE** ✅ | matrah tutarlı |
| Lojistik bedeli (depo/dağıtım kesintisi) | `L6` cirosu **veya** palet/sevkiyat başına | **BLOCKED** | → `T-613` |
| **Alan kullanımı / teşhir bedeli** | mağaza × dönem — **TL tutarı** | **FIXED** ❌ | → `T-613` |
| **Kırık ürün bedeli** | **kırılan adet** (ciro değil) | **VARIABLE ama BAŞKA BİR HACME** ❌ | → `T-613` |
| **Soğutucu enerji bedeli** | soğutucu × dönem — TL tutarı | **FIXED** ❌ | şarapta uygulanabilirliği ayrıca UNKNOWN |
| CRM / B2B (kasa çıkışı cirosu) | kasa çıkışı cirosu (= `L8` tabanlı!) | **BLOCKED** | matrahı `L6` DEĞİL olabilir |

> ### BULGU — **ALTI KALEMİN EN AZ ÜÇÜ SABİT TUTARLIDIR VE MODEL ALTISINI DA ORANSAL SAYIYOR**
>
> Sonuç, `f`'deki ölçek asimetrisinin **`d`'nin içine gizlenmesidir**:
> sabit bileşenler düşük hacimde şişe başına çok daha ağırdır, ama tek bir
> `d` yüzdesi bunu **tanım gereği görünmez kılar.**
>
> **Doğru temsil (spesifikasyon, `T-613`):**
> ```
> L7_eff = L6·(1 − d_var)  −  f_per_bottle  −  D_fix/Q_yillik
>
>   d_var  : GERCEKTEN ciroya oranli bilesenler (ciro primi [+ lojistik?])
>   D_fix  : donem basina SABIT TL bedeller (alan kullanimi, enerji, CRM sabit kismi)
>   f      : listeleme bedeli (zaten sabit)
> ```
> **Not:** `D_fix` ve `f` **aynı davranışa** sahiptir (`TOTAL / Q`). Bunları
> `d` içine gömmek, `K7` hatasını `d` üzerinden **ikinci kez** yapmaktır.
>
> **`CRM/B2B (kasa çıkışı cirosu)` özel uyarısı:** adı bile matrahının
> **kasa çıkışı** yani `L8` hacmi olabileceğini söylüyor. Eğer öyleyse bu
> kalem `L6` üzerinden değil `L8` üzerinden hesaplanır ve `L6` matrahıyla
> yazılması **sistematik olarak eksik sayımdır** (çünkü `L8 > L6`).
> **Bu tek başına `d`'nin matrahını `BLOCKED` yapmaya yeter.**

#### 3.5.3 Kademeli (tiered) prim — taranmamış üçüncü boyut

`kanal.yaml` `d`'yi **tek bir doğrusal oran** olarak taşır. Ciro priminin
kademeli olup olmadığı (`ör. 0–X TL: %2 · X–Y TL: %4 · Y+: %6`) **hiçbir
yerde sorulmamıştır.** Kademeliyse `d` hacme bağlıdır ve şişe başı sabit bir
oran olarak taşınamaz. → **`T-613`**, `sadece_gercek_gorusmeyle_kapanir`
listesine eklenir.

### 3.6 Ödeme vadesi

```yaml
kalem:                 payment term (kanal vadesi)
payer:                 — (bir bedel DEGIL, bir SUREDIR)
receiver:              — (degeri ZAMAN DEGERI olarak perakendeciye gecer)
layer:                 L6 faturasi uzerinde islem gorur
basis:                 ⚠ L6_gross = L6 * (1+v)     # <-- KDV DAHIL FATURA TOPLAMI
                       (alacak KDV'yi ICERIR; L6 uzerinden hesaplamak %20 eksik verir)
currency:              TRY
fixed_or_variable:     VARIABLE (gun sayisi x tutar x finansman orani)
per_bottle_or_total:   TOTAL (sise basina cevrilebilir)
tax_treatment:         Vadenin KENDISI KDV'ye tabi degildir. ANCAK: KDV beyani
                       tahsilata bagli DEGILDIR -> vade uzadikca KDV'yi TAHSIL
                       ETMEDEN beyan etme riski dogar. BU BIR VERGI SORUSUDUR
                       (gumruk-vergi-uzmani) -> T-614 ile birlikte sorulmustur.
evidence_id:           EV-2026-08-10-602 (yasal tavan 60g) · -603 (yaptirim)
                       · -604 · -607 (KOBI Vasfi Belgesi) · -609 (gozlenen 70g, SUT)
                       · -617 (Migros DPO ~93g; borclarin %34,4'u 3-12 ay)
status:                BASE=ESTIMATE (yasal tavan) · C-601 ACIK (tavan 60 vs gozlenen 70-93)
```

> ### ⚠ VADE BİR MARJ KALEMİ DEĞİLDİR — AMA MODELDE **HİÇBİR YERDE** DE DEĞİL
> Vade, `L5`'te bir **finansman satırı** olarak görünmelidir. Bugün:
> - `reverse-price-model.md` §0.2 #11: *"Devreden KDV finansman maliyeti —
>   **0 alındı**, `makro.finansman` `null`"*
> - kanal alacağının finansman maliyeti için **hiçbir satır yok.**
>
> Yani **60–120 günlük kanal vadesinin ekonomik bedeli modelde SIFIRDIR.**
> Bu, `MAX_CIF`'i **yukarı** saptırır — yani projenin **lehine**.
> → **`T-614`**
>
> **Çift sayım uyarısı (`K6`):** eğer ileride hem `d` içinde bir "erken ödeme
> iskontosu" hem de ayrı bir finansman satırı taşınırsa **aynı para iki kez**
> düşülür. İkisi **birbirinin alternatifidir**, toplanamaz.

### 3.7 İade

```yaml
kalem:                 return (satilmayan / hasarli urun iadesi)
payer:                 ITHALATCI (biz) — iade riski sozlesmeyle bize aittir
receiver:              zincir perakendeci (alacak/iade faturasi ile)
layer:                 L6 faturasinin TERSINE CEVRILMESI (iade faturasi = L6 + KDV)
basis:                 ⚠ IADE EDILEN ADET x L6      # <-- L5 DEGIL, L6
currency:              TRY
fixed_or_variable:     VARIABLE (sevk edilen adedin orani)
per_bottle_or_total:   PER_BOTTLE
tax_treatment:         Iade faturasi KDV'lidir (matrah duzeltmesi). AYRICA:
                       ZAYI OLAN MALA AIT KDV INDIRILEMEZ (KDVK md.30/c —
                       Ci-15.1, gumruk-vergi-uzmani alani, EV-2026-08-10-103)
evidence_id:           EV-2026-08-10-606 (sarapta YASAL IADE SINIRI YOK — FACT)
                       EV-2026-08-10-612 (kirik urun bedeli ISMEN sozlesmede — FACT)
status:                yapisal FACT · ORAN UNKNOWN · geri kazanilabilir deger BLOCKED
```

> ### ⚠ İADENİN GERÇEK BEDELİ `L5` DEĞİL, **`L6 − geri_kazanilabilir_deger`**
> Bir şişe iade edildiğinde:
> - **kaybedilen hasılat:** `L6` (fatura geri döner)
> - **geri gelen değer:** en iyi hâlde `L5` (mal sağlam ve yeniden
>   satılabilirse) — **en kötü hâlde 0** (kırık / SKT geçmiş / bandrolü
>   zarar görmüş)
> - **ek kayıp:** zayi olan malın **indirilemeyen KDV'si**
>
> **Yani iade oranı `r`, marjı `r·L6` kadar değil, `r·(L6 − geri_kazanim)`
> kadar vurur — ve `geri_kazanim` şarapta cam şişe nedeniyle `BLOCKED`'dır.**
>
> **İkinci ve daha büyük hata (`K11`):** sabit maliyetler (ruhsat, `f`,
> `D_fix`) modelde **ithal edilen** şişe adedine bölünmektedir; oysa hasılat
> üreten adet `Q·(1−r)`'dir. `r = %5`'te bu **%5,3'lük sistematik bir
> eksik sayımdır** ve şu anda `r = 0` alındığı için **hiç görünmemektedir**.

### 3.8 Lojistik kesintisi

```yaml
kalem:                 logistics deduction (zincirin bizden aldigi lojistik bedeli)
payer:                 ITHALATCI (biz)
receiver:              zincir perakendeci
layer:                 L6 -> L7 koprusu (d sepetinin bir bileseni)
basis:                 ⛔ BLOCKED — L6 cirosu mu, palet/sevkiyat/magaza basi mi
currency:              TRY
fixed_or_variable:     BLOCKED
per_bottle_or_total:   BLOCKED
tax_treatment:         hizmet faturasi -> KDV'ye tabi; indirilebilirlik BLOCKED -> T-611
evidence_id:           EV-2026-08-10-612 (ISMEN var — FACT); tutar KARARTILMIS
status:                BLOCKED
```

> ### ⚠ ÇİFT SAYIM RİSKİ — **`d` içindeki lojistik bedeli ile bizim TR-içi lojistik maliyetimiz**
> `reverse-price-model.md` `R6`, `L5`'ten **TR-içi lojistik** düşer
> (`EV-2026-08-10-329`, 5.000 şişede 3,99 TL/şişe). Aynı anda `d` sepeti
> **zincirin lojistik bedelini** de içerir.
>
> Zincir **merkezi alım** yapar (`EV-2026-08-10-613` dipnot 14): mal zincirin
> merkez deposuna teslim edilir, oradan mağazalara **zincir** dağıtır ve
> bunun bedelini bizden alır. Yani:
> - **Bizim TR-içi lojistiğimiz** = fabrika/antrepo → **zincirin merkez deposu**
> - **Zincirin lojistik bedeli** = merkez depo → mağaza
>
> **Bunlar örtüşmez — ama örtüşmediği HİÇBİR YERDE YAZILMAMIŞTIR** ve
> `navlun-lojistik-uzmani`'nın TR-içi lojistik tanımının hangi teslim
> noktasına kadar olduğu doğrulanmamıştır. Doğrulanmazsa ya çift sayım ya
> eksik sayım vardır. → **`T-618`**

### 3.9 `μ` — ithalatçı katkı payı / distribütör marjı → **§6**

---

## 4. KANAL B — INDEPENDENT RETAIL / TEKEL BAYİ

| Kalem | payer | receiver | layer | basis | fix/var | per_bottle/total | tax_treatment | evidence_id | status |
|---|---|---|---|---|---|---|---|---|---|
| `m_tekel` | tüketici | bayi | **L7→L8** | `L8_net` | VARIABLE | oran | fatura edilmez | `EV-2026-08-10-620` (negatif kayıt) | **UNKNOWN** · `C-602` |
| **marj tipi** (margin / markup / iskonto) | — | — | L7→L8 | ⛔ **BLOCKED** | — | — | — | — | **BLOCKED** |
| `f` | — | — | — | — | — | — | — | `EV-2026-08-10-601` | **ESTIMATE = 0** (yapısal) |
| `d` | ithalatçı? | bayi? | L6→L7 | ⛔ **BLOCKED** | — | — | — | — | **UNKNOWN → 0 alındı** (`T-856`) |
| ödeme vadesi | — | — | `L6_gross` | `L6_gross` | VARIABLE | TOTAL | — | `EV-2026-08-10-609` (SÜT) | **ESTIMATE** 0/30/60 |
| iade | ithalatçı | bayi | L6 tersine | `iade_adet × L6` | VARIABLE | PER_BOTTLE | KDVK md.30/c | `EV-2026-08-10-606` | **UNKNOWN** |
| lojistik | **ithalatçı** | — | **L5** (bizim maliyetimiz) | — | — | — | — | `EV-2026-08-10-329` | ESTIMATE |
| **şüpheli alacak** | ithalatçı | — | **L5** | `L6_gross × p_temerrut` | VARIABLE | PER_BOTTLE | — | — | ⛔ **UNKNOWN → 0** |

### 4.1 ⛔ MARJ TİPİ BELİRSİZ — `BLOCKED`

`m_tekel` modelde `MARGIN_ON_SELLING_PRICE` (matrah `L8_net`) olarak
uygulanmaktadır. **Bu bir seçimdir ve gerekçelendirilmemiştir.** Bağımsız
alkollü içki noktasında ticari dil üç farklı olabilir:

| Konuşma biçimi | Matrah | `L7_eff` (illüstratif, `L8_net`=665,83, oran %18) |
|---|---|---|
| *"marjım %18"* → margin on selling price | `L8_net` | **546,00** |
| *"tavsiye fiyattan %18 iskonto"* | `L8_net` | **546,00** ← *aynı* |
| *"maliyetin üstüne %18 koyarım"* → markup | `L7_eff` | **564,27** (+18,27 TL) |

**İlk ikisi aynıdır, üçüncüsü farklıdır.** Fark `MAX_CIF`'te **+12,18 TL/şişe**
(g=0,50). Hangisinin konuşulduğu **bilinmiyor** → `BLOCKED`. Bu, `C-602`'nin
(çelişen T5 kaynaklar) **matrah boyutudur** ve `C-602`'ye eklenmelidir.

### 4.2 ⛔ `T-856`'NIN GERÇEK CEVABI — **BİR SIFIR DEĞİL, ÜÇ SIFIR**

`finans-fizibilite` haklı olarak şunu tespit etti: tekel tavanı zincirden
**%11,4 yüksek** ve farkın tamamı `d = 0` tercihinden geliyor.

**Ama düzeltme `d` için bir sayı bulmak değildir.** Tekel kanalında
`d`'nin **hukuki karşılığı gerçekten yoktur** (`6585 m.6` zincir/büyük
mağazayı hedefler — `EV-2026-08-10-601`). Kanalın yükü **başka satırlara**
düşer ve **o satırlar da modelde sıfırdır**:

| Zincirde | Tekelde karşılığı | Modeldeki değeri |
|---|---|---|
| `d` (hizmet faturası ile geri akan bedel) | **fiyat iskontosu / net fiyat pazarlığı** — `EV-2026-08-10-610`: indirim marketleri ek bedel yerine **net fiyat** üzerinden pazarlık yapar | **0** |
| zincirin lojistik bedeli | **bizim kılcal dağıtım maliyetimiz** (48.956 nokta, `EV-2026-08-10-613`) | **0** (kendi dağıtım seçilmediyse) |
| zincirin düşük karşı taraf riski | **şüpheli alacak karşılığı + tahsilat maliyeti** (binlerce küçük nokta) | **0** |

> ### SONUÇ — `T-856`'ya cevap
> **Tekel kanalının modeldeki üstünlüğü bir bulgu değil, ÜÇ AYRI SIFIRIN
> toplamıdır.** `d`'yi tekel için tahmin etmek bu artefaktı düzeltmez;
> yalnızca **yerini değiştirir.** Doğru düzeltme: **üç satırın üçünün de
> `UNKNOWN → 0` olduğunun çıktıda YAZILMASI** ve iki kanalın
> `MAX_CIF`'lerinin **karşılaştırılamaz** işaretlenmesidir (`K9`).
> **Bu ajan tekel için bir `d` bandı ÜRETMEMEKTEDİR** — üretmek, olmayan
> bir mekanizmaya sahte bir sayı vermek olurdu.

---

## 5. KANAL C — HoReCa

| Kalem | payer | receiver | layer | basis | fix/var | per_bottle/total | tax_treatment | evidence_id | status |
|---|---|---|---|---|---|---|---|---|---|
| `k_horeca` çarpan | tüketici | HoReCa noktası | **L7→L8_HORECA** | ⚠ **`L7_eff`** (çarpan **markup tipi**) | VARIABLE | oran | fatura edilmez | `EV-2026-08-10-618` (T5, 2012) | **ASSUMPTION** · `C-602` |
| **menü KDV oranı** | tüketici | Hazine | L8_HORECA | ⛔ **BLOCKED** — ürün oranı mı hizmet oranı mı | — | — | ⛔ vergi alanı | — | **BLOCKED → `T-612`** |
| yatırım desteği (`f` karşılığı) | **ithalatçı** | nokta | L6→L7 köprüsü | ⚠ **"noktanın belgelendirdiği fatura tutarları oranında"** → **VARIABLE, `d` gibi** | **KARIŞIK** | KARIŞIK | belge karşılığı ödeme | `EV-2026-08-10-615` | **UNKNOWN** (tutar) |
| menü bastırma / raf yaptırma | ithalatçı | nokta | L6→L7 | **TL tutarı** → **FIXED** | FIXED | TOTAL | — | `EV-2026-08-10-615` | **UNKNOWN** |
| ödeme vadesi | — | — | `L6_gross` | `L6_gross` | VARIABLE | TOTAL | — | — | **UNKNOWN** (kanıtsız band) |
| iade | ithalatçı? | nokta? | L6 tersine | `iade_adet × L6` | VARIABLE | PER_BOTTLE | KDVK md.30/c | — | **UNKNOWN** |
| aktivasyon / tadım | ithalatçı | nokta | L6→L7 **veya** L5 | ⛔ **BLOCKED** | — | — | — | `İP-2001` | **BLOCKED** (`T-604`) |
| lojistik | **ithalatçı** | — | **L5** | — | — | — | — | — | UNKNOWN |

### 5.1 ⛔ ÇARPANIN MATRAHI — MODELDE DOĞRU, KAYNAKTA ÇELİŞKİLİ

`ters_model.py:267`: `l7 = l8_net / kanal.k_horeca` → çarpan **`L7_eff`
matrahlıdır** (`L8_net = k × L7_eff`). `kanal.yaml`'daki tanımla
(`katmanlar: "L7 -> L8_HORECA"`) **birebir tutarlıdır** ✅ (`K4` önlendi).

**Ama kaynağın kendisi iki farklı matrah verir** (`EV-2026-08-10-618`):
*"perakende fiyatının 2 katı"* (matrah `L8`) **ya da** *"toptan fiyatının
2,5 katı"* (matrah `L7`). Bunlar **aynı sayı değildir.** Modelin seçimi
(`L7`) yazılmıştır ve doğrudur; **kaynağın belirsizliği `C-602`'de
durmaktadır ve çözülmemiştir.**

### 5.2 ⛔ **HoReCa'DA `R1` YANLIŞ ORANLA ÇALIŞIYOR OLABİLİR — `BLOCKED`**

`ters_model.py:364`: `l8_net = l8_kdv_dahil / (1 + v)` — burada `v`,
**vergi.yaml'daki ÜRÜN KDV oranıdır** (%20, `EV-2026-08-09-118`).

**HoReCa satırlarında `L8` bir MENÜ FİYATIDIR** (`reverse-price-model.md`
§5.2 bunu açıkça yazıyor). Menü fiyatındaki KDV, **yiyecek-içecek hizmeti**
KDV'sidir ve ürün KDV oranıyla **aynı olmak zorunda değildir.**
`marj-vs-markup.md` §2.3 bu riski **TUR 2'de zaten yazmıştı**:

> *"Ürün KDV oranı ile HoReCa hizmet KDV oranı aynı olmayabilir. Aynı olup
> olmadığı `gumruk-vergi-uzmani` alanıdır; bu ajan varsaymaz."*

**Model varsaymıştır.** Uyarı yazılmış, ama model onu **kullanmamıştır.**

> **Etkisi:** `reverse-price-model.md` §3.2'nin **15 HoReCa hücresinin
> 15'i** bu doğrulanmamış orandan geçmektedir. Oran %10 olsaydı
> `L8_net` **%9,1 yüksek** çıkardı ve `TGT_599 · HIGH` hücresi
> (**5,80 TL** — modelin sıfıra en yakın hücresi) tamamen farklı olurdu.
> → **`T-612`** (`gumruk-vergi-uzmani`) · HoReCa sütunu o cevaba kadar
> **`BLOCKED`** işaretlenmelidir.

### 5.3 Yatırım desteği bir `f` DEĞİL, bir `d`'dir (kısmen)

`EV-2026-08-10-615`: ödemeler noktanın **belgelendirdiği fatura tutarları
oranındadır** → **hacme oranlı = `d` davranışı.** Ama aynı kaynakta
*"menü bastırma, raf yaptırma, dükkân içi yenileme"* da vardır →
**tutar bazlı = `f` davranışı.** Yani HoReCa desteği **karma bir kalemdir**
ve tek bir katsayıyla temsil edilemez (`K8`'in HoReCa karşılığı).

---

## 6. `μ` — İTHALATÇI KATKI PAYI VE DİSTRİBÜTÖR MARJI (`T-944` CEVABI)

### 6.1 Kanal pratiğinde ithalatçı marjı hangi tutarın üzerinden konuşulur?

> ### CEVAP: **TEK BİR CEVAP YOKTUR — ÇÜNKÜ `μ` İKİ FARKLI EKONOMİK NESNEYİ AYNI SEMBOLDE TAŞIYOR.**

`reverse-price-model.md` §7.1 şunu yazıyor:
> *"bu grid, §9.2'deki ithalatçı katkı payı gridiyle **sayısal olarak
> özdeştir** — çünkü ikisi de `L6` cirosu üzerinden yapılan aynı yapıdaki
> bir kesintidir. **Aynı anda ikisi birden uygulanırsa TOPLANIRLAR.**"

**Bu ajan bu özdeşliği REDDEDİYOR.** İki nesne farklıdır:

| | **(A) DIŞ DİSTRİBÜTÖR MARJI** | **(B) İTHALATÇI KATKI PAYI** |
|---|---|---|
| Nedir | **üçüncü tarafa yapılan ÖDEME** | **bizim ARTIK (residual) kârımız** |
| Nakit çıkışı var mı | **EVET** | **HAYIR** |
| Kim belirler | pazarlık (karşı taraf) | **yatırımcı kararı** (`D-03`, `OQ-901`) |
| Pratikte hangi matrahtan konuşulur | **ciro** — distribütör "yaptığım cironun %X'i" der | **maliyet veya kendi satışı** — "maliyetin üstüne %X" ya da "marjım %X" |
| Doğru matrah | **`L6`** ✅ (mevcut model doğru) | ⛔ **TANIMSIZ** — üç aday var |
| `d`, `f` ile ilişkisi | ⚠ **BAĞIMSIZ DEĞİL** (§6.4) | bağımsız |

**Kanıt durumu:** distribütör marjı için `kanal.yaml` TUR 2'de
*"HİÇBİR KANITLI DEĞER BULUNAMAMIŞTIR"* demiştir ve bu **hâlâ geçerlidir.**
İthalatçı katkı payının matrahı için de **hiçbir dış kanıt aranmamıştır ve
aranmayacaktır** (bu bir yatırımcı kararıdır, bir pazar olgusu değil).

Bu belgenin repo-içi tek dayanağı `marj-vs-markup.md` §1.2'dir:
> *"Tedarikçi ve distribütör 'üstüne %X koyuyorum' derken **markup** kasteder."*

Bu bir **repo konvansiyonudur, bir kanıt değildir** — ve tam da bu yüzden
seçim `INVESTOR_DECISION_REQUIRED` bırakılmaktadır.

### 6.2 Üç matrah adayı ve **ölçülen** farkları

`TGT_799 · İspanya · CHAIN RETAIL · BASE (m=%25, d=%8, f=0) · 5.000 şişe ·
DOC_OK (g=0,50) · λ=1` tabanında. `L7_eff = 499,3750` · `L6 = 542,7989` ·
`L5 kalemleri = 36,6772` · `ÖTV = 53,4519`.

| Aday | Formül | `μ=%20` → `L5_max` | **`MAX_CIF`** | `μ=%30` → **`MAX_CIF`** |
|---|---|---|---|---|
| **(a) `L6`** *(model bugün)* | `L5 = L7_eff − μ·L6` | 390,8152 | **200,46** | **164,27** |
| **(b) `L7_EFF`** | `L5 = L7_eff·(1−μ)` | 399,5000 | **206,25** | 172,96 |
| **(c) `L5_MARKUP`** | `L5 = L7_eff/(1+μ)` | 416,1458 | **217,34** | 196,00 |

**Farkın kapalı formları:**
```
(b) − (a)  =  mu · (L6 − L7_eff)  =  mu · (d·L6 + f)      <- R5 hatasinin mu ile carpimi
(c) − (b)  =  L7_eff · [ 1/(1+mu) − (1−mu) ]              <- KLASIK MARGIN/MARKUP FARKI
```

| `μ` | (a)→(b) | (b)→(c) | **(a)→(c) TOPLAM** | (a)'ya göre |
|---|---|---|---|---|
| %10 | +2,90 | +3,03 | **+5,92 TL/şişe** | +2,5% |
| **%20** | +5,79 | +11,10 | **+16,89 TL/şişe** | **+8,4%** |
| %30 | +8,69 | +23,05 | **+31,73 TL/şişe** | **+19,3%** |
| %50 | +14,48 | +55,49 | **+69,96 TL/şişe** | **+76,1%** |

*(Kontrol: `μ=%10`/`%20`/`%30`/`%50`'de (a) sütunu sırasıyla **236,64 · 200,46 ·
164,27 · 91,90** — `reverse-price-model.md` §9.2 gridiyle **birebir aynıdır**.
Yani (b) ve (c) sütunları da aynı motorla tutarlı üretilmiştir.)*

> ### ÜÇ SONUÇ
>
> **1. Mevcut seçim (`L6`) ÜÇÜNÜN EN MUHAFAZAKÂRIDIR.** Yani `T-944`'ün
> bulduğu tanımsızlık, modeli **projenin lehine** değil **aleyhine**
> saptırmaktadır. Bu, `R5` hatasının **tersi yönde** bir kusurdur.
>
> **2. Ama yatırımcı için TEHLİKELİDİR.** Yatırımcı `D-03`'e *"marjım %30"*
> derse ve **maliyet üzerinden markup** kastediyorsa, model onun talebini
> **%19,3 daha ağır** uygulamış olur — yani gerçekte kapanabilecek bir
> proje modelde kapanmaz. **`T-851` bu ticket kapanmadan cevaplanamaz.**
>
> **3. Farkın büyük kısmı matrah seçiminden DEĞİL, margin↔markup
> ayrımından gelir.** `μ=%30`'da (a)→(b) 8,69 TL, (b)→(c) **23,05 TL**.
> Yani `K5` aslında `K2`'nin (`margin ↔ markup`) `μ` üzerindeki
> tekrarıdır — ve `marj-vs-markup.md` sözleşmesi `μ` için **hiç
> uygulanmamıştır.**

### 6.3 KARAR — `INVESTOR_DECISION_REQUIRED`

```yaml
importer_katki_matrahi:
  value:  null
  secenekler: [L6, L7_EFF, L5_MARKUP]
  varsayilan_bugunku_davranis: L6
  status: INVESTOR_DECISION_REQUIRED
  oq:     OQ-901 ; ticket: T-616 (bu ajan) -> T-851 / D-03
  kural: >
    Bu alan ENGINE TARAFINDAN OKUNAN bir alan olmalidir (serbest metin degil).
    Yatirimciya sorulan soru "mu kac?" DEGIL, "mu kac VE HANGI TUTARIN
    UZERINDEN?" olmalidir. Matrahsiz bir mu yuzdesi ANLAMSIZDIR.
  distributor_marji_ile_ayni_matrah_mi:
    value: false
    status: SPEC_DECISION (bu ajan)
    gerekce: "Distributor marji bir ODEMEDIR (matrah L6, ciro). Ithalatci katki
              payi bir ARTIKTIR (matrah yatirimci tanimina bagli). Ozdes
              sayilmalari T-617 ile REDDEDILMISTIR."
```

### 6.4 ⛔ `d` İLE DİSTRİBÜTÖR MARJI **BAĞIMSIZ DEĞİLDİR** — yeni bulgu

`reverse-price-model.md` §7.1 distribütör marjı gridini **`CHAIN RETAIL
BASE` (`d = %8`) üzerinde** koşturmaktadır. Yani **aynı anda**:
- distribütöre `m_dist × L6` ödüyoruz, **ve**
- zincire `d × L6 + f` ödüyoruz.

**Dış distribütör modelinde bu ikisi genellikle aynı anda BİZDE OLMAZ.**
Distribütör kullanılıyorsa zincirle yıllık anlaşmayı **distribütör** imzalar,
ciro primini ve listeleme bedelini **distribütör** öder — ve marjı zaten
bunu içerir. `kanal-marj-yapisi.md` §6 de bunu ima ediyor:
*"distribütör marjı **L6 ile L7 arasına girer**"* — yani distribütör
**zincir bedellerinin yerine geçer**, üstüne binmez.

| Senaryo | Kim öder `d` + `f` | Model bugün |
|---|---|---|
| Kendi dağıtımımız (MODEL B) | **biz** | ✅ doğru (`d` bizde, `m_dist=0`) |
| Dış distribütör (MODEL A) | **büyük olasılıkla distribütör** | ❌ **ikisi de bizde — ÇİFT SAYIM** |

> **Etkisi (`TGT_799 · m_dist=%15`):** `d·L6 = 43,42 TL/şişe` fazladan
> düşülüyor olabilir → `MAX_CIF`'te **+28,95 TL** (aynı `R5` büyüklüğü,
> ters yönde). **Bu, `R5` hatasının aynadaki görüntüsüdür ve bu kez
> projenin ALEYHİNE çalışmaktadır.**
>
> **Ancak `BLOCKED`'dır:** distribütörün zincir bedellerini üstlenip
> üstlenmediği **sözleşmeye bağlıdır ve hiçbir kanıtımız yoktur.**
> Model **iki alt senaryoyu ayrı ayrı** koşmalıdır:
> `A1: d bizde + m_dist` · `A2: d distribütörde + m_dist`. → **`C-611`**, **`T-617`**

---

## 7. ÖZET MATRİS — HANGİ KALEM HANGİ MATRAHTA

| Kalem | CHAIN RETAIL | INDEPENDENT/TEKEL | HoReCa |
|---|---|---|---|
| **margin basis** | `L8_net` ✅ | `L8_net` ⛔ *(tip BLOCKED)* | — |
| **markup basis** | `L7_eff` *(türev — modele girmez)* | `L7_eff` *(aday, BLOCKED)* | **`L7_eff`** ✅ *(çarpan)* |
| **KDV V1** (raf/menü) | `L8_net`, `v`=ürün ✅ | `L8_net`, `v`=ürün ✅ | ⛔ **BLOCKED** *(hizmet oranı?)* |
| **KDV V2** (mal faturası) | `L6` ⚠ *(vade matrahı = `L6_gross`)* | aynı | aynı |
| **KDV V3** (hizmet faturası) | `d·L6 + f` ⛔ **BLOCKED** | yok (yapısal) | destek üzerinde, BLOCKED |
| **listing fee `f`** | **FIXED / TOTAL** ⛔ birim BLOCKED | **0** (yapısal, ESTIMATE) | karma (`menü/raf` FIXED) |
| **turnover rebate `d`** | `L6` ✅ *ama sepet HETEROJEN* ⛔ | **UNKNOWN → 0** (`T-856`) | `nokta fatura tutarı` (VARIABLE) |
| **payment term** | ⚠ **`L6_gross`** (KDV dahil) | ⚠ `L6_gross` | ⚠ `L6_gross` |
| **return** | `iade_adet × L6` ⚠ *(≠ `L5`)* | `iade_adet × L6` | `iade_adet × L6` |
| **logistics deduction** | ⛔ **BLOCKED** (`d` içinde) | **yok** — `L5`'te bizim maliyetimiz | **yok** — `L5`'te bizim maliyetimiz |
| **`μ` matrahı** | ⛔ **INVESTOR_DECISION_REQUIRED** | aynı | aynı |

---

## 8. ⛔ BLOCKED LİSTESİ — MODELDEN SESSİZCE ÇIKARILAMAZ

| # | Kalem | Ne belirsiz | Yön (belirsizlik giderilirse `MAX_CIF`) | Sahibi |
|---|---|---|---|---|
| **B-1** | `f` ve `d` üzerindeki KDV'nin indirilebilirliği | matrah/vergi işlemi | **↓** (indirilemezse ×1,20) | `gumruk-vergi-uzmani` · **`T-611`** |
| **B-2** | HoReCa menü fiyatındaki KDV oranı | `R1`'in oranı | ↕ (her iki yön) | `gumruk-vergi-uzmani` · **`T-612`** |
| **B-3** | `d` sepetinin oransal/sabit ayrışması | fixed_or_variable | **↓** düşük hacimde | bu ajan → `T-613` / TUR 7 |
| **B-4** | Ciro priminin **kademeli** olup olmadığı | basis'in doğrusallığı | ↕ | TUR 7 (`T-604`) |
| **B-5** | Lojistik bedelinin matrahı (% ciro / palet / mağaza) | basis | ↓ | TUR 7 (`T-604`) |
| **B-6** | Alan kullanımı / teşhir bedelinin birimi | basis + fixed/var | **↓** düşük hacimde | TUR 7 |
| **B-7** | Kırık ürün bedelinin matrahı (kırılan adet ≠ ciro) | basis | ↓ | TUR 7 |
| **B-8** | CRM/B2B'nin matrahı — **`L8` (kasa çıkışı) olabilir** | basis katmanı | **↓** (`L8 > L6`) | TUR 7 |
| **B-9** | `f`'nin birimi: SKU×zincir mi SKU×mağaza mı | basis çarpanı | **↓↓** (mağaza bazlıysa) | TUR 7 |
| **B-10** | Tekel bayi marj tipinin margin/markup/iskonto olduğu | basis | ↕ ±12,18 TL (%18'de) | TUR 7 · `C-602` |
| **B-11** | İade oranı **ve** iade edilen malın geri kazanılabilir değeri | basis | **↓** | TUR 7 |
| **B-12** | HoReCa yatırım desteğinin fixed/variable karması | fixed_or_variable | ↓ | TUR 7 |
| **B-13** | Zincirin lojistik bedeli ile bizim TR-içi lojistiğimizin teslim noktası | çift/eksik sayım | ↕ | `navlun-lojistik-uzmani` · **`T-618`** |
| **B-14** | `μ` matrahı | basis | ↕ **+8,4% … +19,3%** | **yatırımcı** · **`T-616`** |
| **B-15** | MODEL A'da `d`+`f`'i kimin ödediği | çift sayım | **↑ +28,95 TL** | **`C-611`** · `T-617` |

> **15 `BLOCKED` kalemin 15'i de bugün modelde ya `0` ya da bir varsayılan
> davranışla geçmektedir.** Hiçbiri için "yok" kanıtı yoktur.
> **`0` bir değer değildir — `0` bir varsayımdır ve bu belgeye kadar
> yazılmamıştı.**

---

## 9. KANAL BACAĞI KAPALI FORMÜL SETİ (`T-943` kriter 3)

```
GIRDI:  L8_gross  (INVESTOR_ASSUMPTION — hedef raf/menu fiyati, KDV DAHIL)
        v         (vergi.yaml — HANGI ORAN: urun mu hizmet mi -> B-2)
        m         (kanal marji, MARGIN ON SELLING PRICE)   |  k (HoReCa carpani)
        d_var     (GERCEKTEN ciroya oranli geri akan bedeller)
        F_total   (donem basina SABIT bedeller: listeleme + alan + enerji + CRM sabit)
        Q         (yillik ITHAL EDILEN sise adedi)
        r         (iade/fire orani)
        mu        (ithalatci katki payi)  +  importer_katki_matrahi (L6|L7_EFF|L5_MARKUP)
        m_dist    (dis distributor marji; MODEL A'da)  +  d_kimde (A1|A2)

K1  L8_net       = L8_gross / (1 + v)                       [KDV: ZINCIRDEKI TEK BOLME]
K2  L7_eff       = L8_net * (1 - m)                         [CHAIN/TEKEL: margin on selling price]
    L7_eff       = L8_net / k                               [HORECA: carpan, matrah L7_eff]
K3  f_per_bottle = F_total / Q                              [<-- TUREVDIR, GIRDI DEGILDIR]
K4  L6           = (L7_eff + f_per_bottle) / (1 - d_var)    [FATURA fiyati — L5 BUTCESI DEGIL]
K5  L5_max       = L7_eff - mu_kesintisi - m_dist_kesintisi - iade_kaybi
       mu_kesintisi     : matraha gore
                          L6        -> mu * L6
                          L7_EFF    -> mu * L7_eff
                          L5_MARKUP -> L7_eff * (1 - 1/(1+mu))
       m_dist_kesintisi : m_dist * L6      [A1] ; MODEL B'de 0
       iade_kaybi       : r * (L6 - geri_kazanilabilir_deger)     [bugun 0 -> B-11]
K6  L6_gross     = L6 * (1 + v)            [ALACAK TUTARI — vade ve peak_cash BUNUN uzerinden]

CIKTI: L5_max  -> ters modelin R6'sina girer
```

### 9.1 `R8-K` — kanal round-trip assertion (⚠ `T-942`'nin önerdiği hâlde DEĞİL)

```
K1'  L7_eff_geri = L5_max + mu_kesintisi + m_dist_kesintisi + iade_kaybi
K2'  L8_net_geri = L7_eff_geri / (1 - m)        [HORECA: * k]
K3'  L8_geri     = L8_net_geri * (1 + v)
assert  | L8_geri - L8_gross | < 0,01 TL
```

> ⛔ **`T-942`'nin `adim K1 : L6_geri = (L5_max + mu*L6)` satırı HATALIDIR.**
> `L5_max + μ·L6` `L6`'ya değil **`L7_eff`'e** eşittir; `L6` etiketiyle
> devam edilince `K2`'de `×(1−d) − f` **ikinci kez** uygulanır ve
> assertion **tersine döner**: doğru formül `735,08` üretip **reddedilir**,
> naif formül `799,00` üretip **kabul edilir**.
> `T-942`'nin **teşhisi doğrudur** (kanal bacağında doğrulama yoktur);
> düzeltilmesi gereken tek şey `K1` adımının etiketidir. → **`T-619`**

**Her adımda kimin maliyeti (`T-943` kriter 3):**

| Adım | Kalem | Kimin maliyeti | Kimin geliri |
|---|---|---|---|
| K2 | `m` / `k` | — (fiyat farkı) | perakendeci / HoReCa noktası |
| K3–K4 | `f`, `d` | **ithalatçı (biz)** | perakendeci |
| K5 | `μ` | — (**bizim artığımız**, bir maliyet değil) | **biz** |
| K5 | `m_dist` | **ithalatçı (biz)** | distribütör |
| K5 | iade | **ithalatçı (biz)** | — (net kayıp) |
| K6 | KDV | ekonomik maliyet **değil**, **nakit** | Hazine |

---

## 10. BU BELGENİN MODELDE DEĞİŞTİRDİĞİ ŞEYLER — ÖZET

| # | Bugünkü davranış | Bu belgenin dediği | Yön |
|---|---|---|---|
| 1 | `d` tek homojen oran | en az 3/6 bileşen **FIXED** → `d_var` + `D_fix` | ↓ düşük hacimde |
| 2 | `f_per_bottle` girdi | **türev** olmalı: `F_total / Q` | ↓ düşük hacimde |
| 3 | vade `L6` üzerinden düşünülüyor | **`L6_gross`** (KDV dahil) | peak_cash **+%20** |
| 4 | iade `0` | `r·(L6 − geri_kazanım)`; ayrıca hacim `Q(1−r)` | ↓ |
| 5 | `μ` matrahı yazısız `L6` | **açık alan** + 3 seçenek | ↕ %8,4–19,3 |
| 6 | `μ` ≡ `m_dist` (özdeş, toplanır) | **REDDEDİLDİ** — farklı nesneler | — |
| 7 | MODEL A'da `d` + `m_dist` birlikte | **A1/A2 iki alt senaryo** | ↑ +28,95 TL (A2'de) |
| 8 | HoReCa `R1` ürün KDV oranıyla | **BLOCKED** — doğrulanana kadar | ↕ |
| 9 | tekel `d = 0` | **üç sıfır**; kanallar karşılaştırılamaz işaretlensin | — |
| 10 | `f`/`d` KDV'si sessizce indirilebilir | **yazılsın**; nakit çıkışı her hâlde var | ↓ |

**7 kalem `MAX_CIF`'i AŞAĞI, 1 kalem YUKARI, 2 kalem çift yönlü çeker.**
`reverse-price-model.md` §0.2'nin *"13 kalemin 13'ü de yukarı saptırır"*
tespiti **kanal bacağı için de geçerlidir** — bu belge o listeye **7 kalem
daha eklemektedir.**

---

## 11. BU BELGENİN ÜRETMEDİĞİ ŞEYLER (bilerek)

- **Hiçbir yeni marj değeri, bandı veya oranı.** TUR 2'nin *"bu bandın
  seviye kanıtı yoktur"* tespiti aynen geçerlidir.
- **Tekel ve HoReCa için `d` bandı.** Üretmek, olmayan bir mekanizmaya
  sahte sayı vermek olurdu (§4.2).
- **`μ` değeri.** Yatırımcı kararıdır (`D-03`, `T-851`, `OQ-901`).
- **KDV oranı / indirilebilirlik sonucu.** `gumruk-vergi-uzmani` alanıdır.
- **Listeleme bedeli tutarı.** `T-604` — TUR 7.
