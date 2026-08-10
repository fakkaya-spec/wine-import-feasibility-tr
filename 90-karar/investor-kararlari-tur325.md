# TUR 3.25 §0 — KURUCU KARARLARININ KAYDI

```yaml
belge:                  investor-kararlari-tur325
yazan:                  yatirim-komitesi-baskani
tarih:                  2026-08-10
tur:                    TUR 3.25 §0
kapsam:                 "Kurucu tarafindan VERILMIS uc kararin kayda gecirilmesi,
                         yapilandirilmasi ve SONUCLARININ yazilmasi"
karar_iceriyor_mu:      false      # YATIRIM karari (KILL/HOLD/TEST/PILOT/SCALE) YOK
esik_degeri_yazildi_mi: false      # HICBIR ESIGE BASKAN SAYI YAZMADI
arastirma_yapildi_mi:   false      # CLAUDE.md §1.16
web_aramasi_yapildi_mi: false
ajan_cagrildi_mi:       false
yeni_kanit_uretildi_mi: false      # kurucu beyani KANIT DEGILDIR -> kanit karti YOK
karar_gunlugune_dokunuldu_mu: false
git_calistirildi_mi:    false
acilan_ticket:          [T-961, T-962, T-963, T-964, T-965, T-966, T-967, T-968]
guncellenen_ticket:     [T-467, T-304, T-871, T-884, T-857]
yeni_kapi:              P-6        # DIS TEMAS ONAY KAPISI
```

> ## SINIR BEYANI
> Bu belge bir **yatırım kararı içermez.** `KILL` / `HOLD` / `TEST` /
> `IMPORT PILOT` / `SCALE` kararlarının hiçbiri verilmemiştir.
> `90-karar/karar-gunlugu.md` dosyasına **DOKUNULMAMIŞTIR.**
> Hiçbir araştırma yapılmamış, hiçbir ajan çağrılmamış, hiçbir eşiğe sayı
> yazılmamıştır.
>
> ## VE BİR EPİSTEMOLOJİK UYARI — BU BELGENİN EN ÖNEMLİ CÜMLESİ
> Aşağıdaki kararlar **kurucunun verdiği kararlardır**, başkanın türettiği
> sonuçlar **değildir.** Hiçbiri bir **bulgu**, bir **gözlem** veya bir
> **kanıt** değildir. Hiçbiri `FACT` olarak etiketlenmemiştir ve
> `evidence_id` taşımaz — çünkü bir **dış olgu değil, bir niyet
> beyanıdırlar.** Bir kurucu kararının doğru olması, onun **gerçekleşeceği**
> anlamına gelmez.

---

# §1 — KARAR 1: HEDEF RAF FİYATLARI

## 1.1 Kayda geçen

| Sabit | Değer | `status` | Rol |
|---|---|---|---|
| `PRIMARY_TARGET_SHELF_PRICE` | **799 TRY** | `INVESTOR_TARGET` | RFQ strateji çapası |
| `SECONDARY_TARGET_SHELF_PRICE` | **699 TRY** | `INVESTOR_TARGET` | — |
| `STRETCH_TARGET_SHELF_PRICE` | **899 TRY** | `INVESTOR_TARGET` | — |
| `599 TRY` | **DOWNSIDE / FLOOR TEST** | `INVESTOR_TARGET` | **ana RFQ stratejisini BELİRLEMEZ** |
| `999 TRY` | **UPPER SEGMENT TEST** | `INVESTOR_TARGET` | **ana RFQ stratejisini BELİRLEMEZ** |

Kayıt yeri: `80-model/inputs/senaryolar.yaml` →
`hedef_raf_fiyati_merdiveni.investor_rol_atamasi_tur325`

## 1.2 Karara bağlanan şey **basamaklar değil, basamakların ROLÜDÜR**

Merdivenin beş basamağı TUR 2.5'te **zaten** kaydedilmişti
(`INVESTOR_ASSUMPTION`, KDV dahil, 750 ml still). Bu turda değişen tek şey
**hangi basamağın hangi işi gördüğüdür.** Beş basamağın beşi de yerinde
durmaktadır; hiçbiri silinmemiş, hiçbiri "seçilmiş fiyat" hâline gelmemiştir.

## 1.3 Bu atamanın **YÜRÜRLÜKTEN KALDIRMADIĞI** kurallar

| Kural | Durum |
|---|---|
| `L3` — beş basamak **ayrı ayrı** çalışır, ortalaması alınmaz | **YÜRÜRLÜKTE** |
| `P-2` / `T-948` — 5 basamak × 3 tarih × 4 ÖTV noktası ayrı ayrı | **YÜRÜRLÜKTE** |
| `P-5.1` — çıktı tek bir "baz senaryo" olarak sunulamaz | **YÜRÜRLÜKTE** |
| `L1` — merdiven **piyasa fiyatı değildir**, bir hedeftir | **YÜRÜRLÜKTE** |
| `L2` — `599 (TARGET)` ≠ `599,90 (OBSERVED)` | **YÜRÜRLÜKTE** |
| `L4` — merdiven `l8_chain_retail`'in yerine geçmez; o `null` kalır | **YÜRÜRLÜKTE** |

> **`PRIMARY` bir "beklenen sonuç" değildir.** Bir pazarlık çapasıdır.
> `PRIMARY` seçimi, modelin çıktısını beş basamaklı bir yüzeyden tek bir
> noktaya indirmez ve indiremez. Bunu yapan bir rapor **geçersizdir.**

## 1.4 `N-3` — hangi kısmı kapandı, hangi kısmı **açık kaldı**

`N-3`, TUR 3A'da `D-14`'ün ikiye bölünmüş hâliydi:

| Alt kalem | İçerik | TUR 3A'daki yeri | TUR 3.25 sonrası |
|---|---|---|---|
| **`D-14a`** | **hangi basamak `PRIMARY`** | `CAN DECIDE LATER` | ✅ **KAPANDI — 799** |
| **`N-3b`** *(eski `D-14b`)* | **hangi `L8` ALT KATMANI** | **`MUST DECIDE NOW`** | ⛔ **AÇIK — `INVESTOR_DECISION_REQUIRED`** |

> ### KURUCU **FİYAT BASAMAĞINI** SEÇTİ, **KOORDİNAT SİSTEMİNİ** SEÇMEDİ
>
> `MUST DECIDE NOW`'daki kalem `D-14a` **değildi** — `N-3b` idi. Yani
> **kapanan kısım, zaten ertelenebilir olan kısımdır; ertelenemez olan kısım
> hâlâ açıktır.** Bu, sevindirici olmayan ama kayda geçirilmesi zorunlu bir
> sonuçtur.

**Açık kalan tam soru** *(değiştirilmeden, `N-3`'ün orijinal formatında)*:

```
799 TRY (KDV dahil, 750 ml still) HANGI RAFIN fiyatidir?
  [ ] L8_CHAIN_RETAIL            (zincir market rafi)
  [ ] L8_METRO_CASH_CARRY        (toptanci / cash & carry)
  [ ] L8_ONLINE_UZMAN_PERAKENDE  (online uzman perakende)
  [ ] KANAL KARMASI              -> karmanin agirliklari da yazilir
status: INVESTOR_DECISION_REQUIRED
```

Bağlam *(değişmedi)*: elimizdeki **473 fiyat gözleminin
`L8_CHAIN_RETAIL`'deki sayısı SIFIRDIR** (`T-859`, `T-603`, `T-701`,
`T-917`). `L8_CHAIN_RETAIL` seçilirse, **seçilen katmanda hiç gözlem
olmadığı bilinerek** seçilmiş olur.

⚠ **Kurucu beyanı "kanal karması" seçeneğini de kapatmamıştır.** Bu seçenek
`N-3`'ün sürüm 2 metninde **yoktu**; bu turda eklendi, çünkü kurucu üç
katmandan birini söylemeyerek dördüncü ihtimali açık bırakmıştır. Başkan bunu
**kendi doldurmamıştır.**

## 1.5 Bu atamanın **KAPATMADIĞI** ticket'lar

| Ticket | Neden kapanmadı |
|---|---|
| `T-859` (HIGH) | `L8` alt katmanı hâlâ `UNKNOWN` |
| `T-851` (**CRITICAL**) | Hedef **RAF** fiyatı ≠ hedef **ALIŞ** fiyatı. `TARGET_DISCOUNT_FROM_MAX` ve `REQUIRED_IMPORTER_MARGIN` hâlâ `INVESTOR_DECISION_REQUIRED` |
| `T-504` (HIGH) | 599'un dayandığı tek gözlemin promosyon durumu — 599 artık `FLOOR TEST` olsa da soru aynen duruyor |
| `T-857` (HIGH) | 999 `UPPER SEGMENT TEST` oldu, ama **manda tavanı (900, `ESTIMATE`) değiştirilmedi** — "test" ile "manda dışı" birlikte durabilir |
| `T-603` / `T-701` / `T-917` | `l8_chain_retail` hâlâ `null` → **`G3` AÇILMADI** |

> **`G3` bu kararla AÇILMAZ.** `OPEN QUESTION #001` (Metro 599,90'ın KDV/kanal
> statüsü) kapanmadan `G3` geçilemez — bu kural `CLAUDE.md` düzeyindedir ve
> bir hedef fiyat seçimiyle aşılamaz.

---

# §2 — KARAR 2: RFQ HACİM KADEMELERİ

## 2.1 Kayda geçen

```
V1 = 5.000   V2 = 10.000   V3 = 25.000   V4 = 50.000 sise
+ FULL_20FT_CONTAINER  -> AYRI fiyat
100.000 sise ILK RFQ'DA SORULMAYACAK
Amac: PRICE-VOLUME CURVE. Tek hacim fiyati ISTENMEYECEK.
```

Kayıt yeri: `80-model/inputs/senaryolar.yaml` → `rfq_hacim_kademeleri`
*(yeni blok — `hacim_senaryolari` bloğuna **dokunulmadı**)*

## 2.2 Model açısından **beş** sonuç

### (1) `V2 = 10.000` artık bir **boşluk değil, bir EKSİK**

`V10K` `senaryolar.yaml`'da tanımlıydı ama `lojistik-senaryolari-tur25.md` §4
tablolarında **satırı yoktu** ve ters model bu hacmi **hiç
çalıştırmamıştı** — `T-855` (MEDIUM, `navlun-lojistik-uzmani`) bunu doğru
biçimde bir `UNKNOWN` olarak bırakmış ve **interpolasyon yapmamıştı.**

Kurucu kararından sonra durum değişir: 10.000 artık **tedarikçiye
sorulacak bir fiyat noktasıdır.** Gelen fiyatın karşılaştırılacağı bir model
satırı yoksa, o fiyat **hiçbir şeye çevrilemez.**
→ **`T-963`** *(finans-fizibilite)* ve `T-855` bu nedenle bağlandı.

### (2) `FULL_20FT` bir **şişe adedi değildir** — ve bu kademeyi kırılgan yapar

| Yükleme biçimi | 20DV şişe kapasitesi | Kaynak |
|---|---|---|
| **Paletli** | **6.480 – 7.200** | `EV-2026-08-09-320` (`ESTIMATE`) |
| **Paletsiz (floor-loaded)** | **11.800 – 13.700** | `EV-2026-08-09-320` (`ESTIMATE`) |

Aradaki fark **~2 kattır.** Dahası, gerçek adet **tedarikçinin kendi koli ve
palet konfigürasyonuna** bağlıdır — yani RFQ zorunlu alanları **M3 / M4**'e.

> ### BU, `T-884`'Ü DOĞRUDAN VE BEKLENMEDİK BİÇİMDE ETKİLER
> `T-884` bugüne kadar bir **navlun belirsizliği** meselesiydi (M2/M3/M4
> cevapsız kalırsa şişe başı navlun %38 belirsizlikle taşınır).
> Kurucunun `FULL_20FT` kararından sonra M3/M4 **kurucunun kendi fiyat
> kademesinin okunabilmesi için** gereklidir: M3/M4 cevapsızsa
> *"full 20ft = X EUR"* teklifi **şişe başına çevrilemez** ve iki tedarikçi
> arasında **karşılaştırılamaz.**
>
> Yani `T-884`'ün "eleme kuralı" tartışması artık yalnızca lojistik
> hassasiyeti değil, **kademenin okunabilirliği** meselesidir.

### (3) Kademeler **LCL/FCL kırılma noktasını çaprazlıyor**

```
LCL/FCL kirilma merkezi : ~5.900 sise/sevkiyat  (EV-2026-08-10-330, ESTIMATE, LOW)
band                    :  2.200 – 9.800
V1 = 5.000  -> kirilmanin ALTINDA
V2 = 10.000 -> kirilmanin USTUNDE
```

Kademeler arasında yalnızca fiyat değil **taşıma MODU** da değişebilir.
Şişe başı lojistik maliyeti kademeler arasında **doğrusal değildir.**
→ **Kademeler arası interpolasyon yasaktır** (`TR325-V3`).
→ **`T-962`** *(navlun-lojistik-uzmani)*.

⚠ Ve bu kırılma noktası **`2026-08-17` itibarıyla `STALE` olacak veri
setine dayanmaktadır** (`P-3b-DATED` / `T-913`). Kurucunun hacim kademeleri,
tazeliği **7 gün sonra dolan** bir kırılma noktasının iki yanına düşmektedir.

### (4) `V100K` artık **çapasız** bir model satırıdır

100.000 şişe charter'ın belirlediği bir hacim senaryosudur ve **silinmez.**
Ama ilk RFQ'dan **fiyat çapası almayacaktır.**
→ `V50K` fiyatından `V100K`'ya **ekstrapolasyon yasaktır**; `V100K` alış
fiyatı `UNKNOWN` kalır ve o satırdan türeyen her çıktı **`NO_RFQ_ANCHOR`**
damgası taşır (`T-963`).

Bu, `T-858`'in ölçek bulgusuyla birlikte okunmalıdır: ölçek ekonomisinin
**%87'si 5.000 → 25.000 sıçramasında** gerçekleşmektedir. Yani 100.000'i ilk
turda sormamanın **ekonomik bedeli, o bulguya göre küçüktür** — ama bu bir
başkan hesabı değil, mevcut bir ajan bulgusunun aktarımıdır ve `T-858` hâlâ
`OPEN`'dır.

### (5) ⚠ **BAZ BELİRSİZLİĞİ — kurucu beyanı bunu söylemedi**

`rfq-template.md` **iki ayrı baz** taşır:

| Alan | Baz |
|---|---|
| `Indicative annual volume: <VOLUME> bottles/year` | **YILLIK** |
| `First (pilot) order: <PILOT VOLUME> bottles` | **SİPARİŞ BAŞINA** |

`FULL_20FT` ise **yalnızca sevkiyat başına** tanımlıdır.
Kurucu "5.000 · 10.000 · 25.000 · 50.000 şişe" derken **hangi bazı**
kastettiğini söylememiştir. 50.000 şişe/yıl ile 50.000 şişe/sipariş
**aynı şey değildir** (ikincisi ~7 × 20DV'dir).

> **Başkan bunu kendi doldurmamıştır.** `senaryolar.yaml`'daki
> `V1↔V5K … V4↔V50K` eşlemesi bu nedenle **`PROVISIONAL`** olarak
> işaretlenmiştir ve `T-961` kapanmadan kesinleşmez.

## 2.3 `<VOLUME>` / `<PILOT VOLUME>` — RFQ geçerliliği

`rfq-template.md` §0.9, `<VOLUME>` ve `<PILOT VOLUME>` boşken şablonu
**geçersiz** sayıyordu.

| Alan | Durum |
|---|---|
| `<VOLUME>` | ⚠ **Artık boş değil — ama tek bir sayı da değil.** Kurucu bir **eğri** istedi; şablon **tek bir yıllık hacim** soruyor. Şablonun **yapısı** değişmelidir → `T-961` |
| `<PILOT VOLUME>` | ⛔ **HÂLÂ BOŞ.** Kurucu **hangi kademenin pilot** olduğunu söylemedi. Pilot hacmi `D-09`/`D-10` alanıdır ve `CAN DECIDE LATER`'dadır |

> **Sonuç: `T-871` KAPANAMAZ** *(ayrıntı §4.3)*.

---

# §3 — KARAR 3: DIŞ TEMAS POLİTİKASI → **`P-6` KAPISI**

## 3.1 Kayda geçen

Kurucu **prensip olarak ONAY** vermiştir. Bu, `N-2`'nin (dış temas izni)
**verildiği** anlamına gelir — **koşullu olarak.**

> ### `P-6` — DIŞ TEMAS ONAY KAPISI *(bağlayıcı)*
>
> | # | Kural |
> |---|---|
> | **P-6.1** | Dış temas **prensip izni VERİLMİŞTİR** (kurucu, 2026-08-10). İzin **iki bacağı da** kapsar: **(a)** tedarikçilere RFQ (`T-467`), **(b)** forwarder'lardan FCL kotasyonu (`T-304`). |
> | **P-6.2** | **Bu turda hiçbir mesaj GÖNDERİLMEZ.** Bu turda yapılacak tek şey: gönderilecek **mesaj metinlerinin** ve **alıcı listesinin** FİNAL hâline getirilmesidir. |
> | **P-6.3** | Gerçek gönderim öncesi her temas için **`RECIPIENT` + `SUBJECT` + `MESSAGE PREVIEW`** kurucuya gösterilir ve **açık onay** beklenir. Onay **tarihiyle kaydedilir**. |
> | **P-6.4** | **OTOMATİK TOPLU MAİL YOKTUR.** Mail-merge, toplu BCC, otomatik dalga gönderimi **yasaktır.** |
> | **P-6.5** | **YAPTIRIM:** `P-6.3` onayı alınmadan yapılmış bir temastan gelen hiçbir veri **kanıt kartı açamaz** ve modele giremez. |
> | **P-6.6** | Prensip izni bir **gönderim onayı değildir.** `P-6.1` `G2`'yi **açmaz**; `G2`'yi açan şey **cevaplardır**, izin değil. |
> | **P-6.7** | `T-884` (RFQ eleme kuralı) kararı, ilk `P-6.3` onayından **ÖNCE** kayda geçer. Gerekçe `T-884`'ün kendi uyarısıdır: kural gönderimden sonra onaylanırsa tedarikçiye §0'da yazdığımız sonuçlarla iç kuralımız çelişebilir. |

## 3.2 Bu iznin **DEĞİŞTİRMEDİĞİ** şeyler

| İddia | Doğru mu |
|---|---|
| "`G2` açıldı" | ❌ **Hayır.** `G2`'yi açan şey ≥5 gerçek RFQ cevabıdır. İzin yalnızca **eylemi mümkün kıldı.** |
| "`T-466` kapandı" | ❌ **Hayır.** Gerçek `EXW`/`FOB` hâlâ yok; `T-466` **CRITICAL, OPEN.** |
| "`T-304` kapandı" | ❌ **Hayır.** Doğrulanmış navlun hâlâ yok; `T-304` **CRITICAL, OPEN.** İzin `T-304`'ün **izin ayağını** açar, **veri ayağını** değil. |
| "Artık ithalat kararı verilebilir" | ❌ **Hayır.** Bu bir izin, bir yatırım kararı değil. |

## 3.3 Takvim sonucu — **bu iznin gerçek getirisi**

`N-2` bir **model blokeri değil, TAKVİM blokeriydi.** İzin verildiğine göre:
`TUR 7`'nin başlama tarihi artık *"izin bekleniyor"* değil, **`P-6.2`
paketinin hazır olmasına** bağlıdır → `T-967` *(sourcing)* ve `T-968`
*(forwarder)*.

⚠ **Ve bir zamanlama gerilimi kayda geçirilir:** LCL kotasyon seti
**2026-08-17'de `STALE`** olur (`P-3b-DATED`). `P-6.2` paketi hazırlanırken
forwarder temasının (`T-968`) `T-913` **Ayak A**'yı da (kotasyon yenileme
protokolü) kapsayıp kapsamayacağı **`navlun-lojistik-uzmani`'nın kararıdır** —
başkan bunu emretmez, çünkü içeriği araştırmadır.

---

# §4 — TICKET KARŞILIKLARI

## 4.1 `T-467` — RFQ izni · `OPEN` → **`ANSWERED`**

Ticket'ın dört sorusunun tamamı cevaplanmıştır:

| # | Soru | Cevap |
|---|---|---|
| 1 | Onay: RFQ gönderilsin mi | ✅ **EVET — prensip izni verildi** (`P-6.1`), **koşullu** (`P-6.2`…`P-6.5`) |
| 2 | Zamanlama: şimdi mi, `TEST`/`PILOT` kararına kadar mı | **HAZIRLIK ŞİMDİ, GÖNDERİM `P-6.3` ONAYIYLA.** `TUR 7`'ye kadar bekletilmez |
| 3 | Ön koşullar (`T-462`, `T-464` önce kapansın mı) | ⚠ **BU BAŞKANIN KARARI DEĞİLDİR.** İkisi de `ANSWERED`'dır; cevapların **yeterli olup olmadığı** `global-sourcing-kasifi`'nın kendi teknik değerlendirmesidir → `T-967` |
| 4 | Hacim | ✅ **VERİLDİ** — `V1…V4` + `FULL_20FT`; ⚠ **bazı belirsiz** (`T-961`), `<PILOT VOLUME>` **hâlâ boş** |

**`RESOLVED` değil, `ANSWERED`:** ticket'ın kendi ifadesiyle bu bir *"kayıt
talebidir"* ve kapanışı, ilk `P-6.3` onayının kaydedilmesine bağlıdır.

## 4.2 `T-304` — forwarder izni · `OPEN` (**CRITICAL, DEĞİŞMEDİ**)

İzin verildi (`P-6.1(b)`), **ama ticket'ın iddiası izinle ilgili değildir:**
*"Hiçbir rotamız için doğrulanmış navlun YOKTUR."* Bu iddia **hâlâ
doğrudur.**

| Alan | Değişti mi |
|---|---|
| `status` | **HAYIR** — `OPEN` |
| `impact` | **HAYIR** — `CRITICAL` |
| Eklenen | `tur325_izin_ayagi: VERILDI` (P-6) + `T-968` |

> **İzni bir veri gibi saymak, bu projede yapılabilecek en kolay hatadır.**
> Yapılmadı.

## 4.3 `T-871` — RFQ çapası · `OPEN` (**kısmen cevaplandı — kapanamaz**)

| # | Soru | Durum |
|---|---|---|
| 1 | Hangi basamak (599…999) | ✅ **KAPANDI — 799 `PRIMARY`** |
| 2 | Hangi kanal (CHAIN / TEKEL / HoReCa) | ⛔ **AÇIK.** Kurucu kanal söylemedi. `rfq-negotiation-cards.md`'nin `CHAIN_RETAIL` çapası bir **ajan varsayımıdır** → `T-966` |
| 3 | `<VOLUME>` / `<PILOT VOLUME>` | ◐ **KISMEN.** `<VOLUME>` için kademeler geldi ama **şablon yapısı** eğriyi taşımıyor (`T-961`); `<PILOT VOLUME>` **boş** |

> ### CEVAP: **HAYIR, `T-871` KAPANAMAZ.**
> Üç sorudan **biri tam**, biri **kısmi**, biri **açıktır.** 10 pazarlık
> kartının rakamları **basamak** tarafından sabitlenmiş, **kanal** tarafından
> sabitlenmemiştir — ve `T-871`'in kendi tablosuna göre kanal değişimi
> zincir↔tekel arasında **%11,4**'lük bir tavan farkı üretir. Kartlar bugün
> **yarı sabitlenmiş** durumdadır.
>
> ⚠ Ve `T-871`'in kendi uyarısı geçerliliğini korur: o %11,4 farkın
> **tamamı** `d`'nin tekelde `0` alınmasından gelmektedir (`T-856`) — yani
> tekel çapası seçilirse eşikler **bir `UNKNOWN` üzerine** kurulmuş olur.

## 4.4 `T-884` — eleme kuralı · `OPEN` (**ONAYLANMADI — ama artık kritik yolda**)

**Bu turda A/B/C/D seçeneklerinden hiçbiri seçilmemiştir.** Gerekçe:

1. `global-sourcing-kasifi` dördünü de savunulabilir bulmuş ve **seçimin
   risk iştahına bağlı** olduğunu yazmıştır. Başkanın gerekçesiz bir seçenek
   işaretlemesi, ajanın açıkça reddettiği şeyi yapmak olurdu.
2. Kurucu bu konuda **hiçbir şey söylememiştir.** `T-884`'ü kurucu kararı
   gibi kapatmak, **verilmemiş bir kararı verilmiş göstermek** olurdu.

**Ama üç şey değişti:**

| Değişiklik | Sonuç |
|---|---|
| `N-2` verildi | `T-884` artık *"RFQ gönderilmeden hüküm doğurmaz"* diye ertelenemez — gönderim **yakındır** |
| `P-6.7` konuldu | `T-884` kararı ilk `P-6.3` onayından **ÖNCE** kayda geçer → **kritik yola girdi** |
| `FULL_20FT` kademesi geldi | M3/M4 artık yalnızca navlun için değil, **kurucunun kendi fiyat kademesinin okunabilmesi** için gerekli → seçenek **B**'nin (kuralı yumuşat) bedeli **arttı**, ama bu bir **argümandır, karar değildir** |

`impact` **yükseltilmedi** (HIGH kalır): kural finans modelini bloke etmez,
RFQ **karşılaştırılabilirliğini** bloke eder.

## 4.5 `T-857` — 999 mandası · `OPEN` (kısmi not eklendi)

999 artık `UPPER_SEGMENT_TEST`'tir → **`PRIMARY` değildir.** Ama
`T-857`'nin sorduğu şey bu değildi: **manda tavanı (900) değişiyor mu?**
Kurucu bunu söylemedi. `OUT OF MANDATE` etiketi **düşmez**, ticket **açık**
kalır.

## 4.6 Açılan yeni ticket'lar

| ticket | hedef | impact | konu |
|---|---|---|---|
| **`T-961`** | `global-sourcing-kasifi` | **HIGH** | RFQ şablonu tek hacimden **price-volume grid**'e; kademelerin **bazı** (yıllık ↔ sipariş); `<PILOT VOLUME>` tek sayı gerektiriyor mu |
| **`T-962`** | `navlun-lojistik-uzmani` | **HIGH** | `FULL_20FT`'in şişe adedi tanımı; V1/V2'nin LCL-FCL kırılmasını çaprazlaması |
| **`T-963`** | `finans-fizibilite` | **HIGH** | `V10K` satırı modele girsin; `V100K` **`NO_RFQ_ANCHOR`**; interpolasyon/ekstrapolasyon yasağı |
| **`T-964`** | `finans-fizibilite` | **HIGH** | Gözlenen tek spot kur ile **9 ülke ayrıştırması** yapılabilir mi — `N-1b`'nin ertelenebilirliği buna bağlı |
| **`T-965`** | `gumruk-vergi-uzmani` | **HIGH** | 2026-08 spot kuru **2027 hedef tarihlerinde** kullanılabilir mi (`T-858(b)` deseni); gümrük beyan kuru ayrımı (`T-911`) |
| **`T-966`** | `kanal-marj-uzmani` | **HIGH** | `L8` alt katmanı seçimi `TARGET_CHANNEL`'ı **tek anlamlı belirler mi**, yoksa iki ayrı seçim mi |
| **`T-967`** | `global-sourcing-kasifi` | **HIGH** | `P-6.2` gönderim paketi: alıcı listesi + her alıcı için `RECIPIENT`/`SUBJECT`/`PREVIEW`; `T-462`/`T-464` yeterlilik değerlendirmesi |
| **`T-968`** | `navlun-lojistik-uzmani` | **HIGH** | `P-6.2` forwarder paketi; `T-913` Ayak A ile birleştirilip birleştirilmeyeceği ajanın kararı |

**Hiçbiri `CRITICAL` değildir** → açık `CRITICAL` sayısı **11'de sabittir.**

---

# §5 — GÜNCEL `MUST DECIDE NOW` *(sürüm 3)*

| # | Kalem | TUR 3A | **TUR 3.25** |
|---|---|---|---|
| **`N-1a`** | **gözlenen** spot kur | `MUST` | ✅ **LİSTEDEN ÇIKTI** — bir yatırımcı kararı değil, **ajan gözlemi** (`T-852`/`T-912`); bu turda `gumruk-vergi-uzmani` alıyor |
| **`N-1b`** | **hedef tarih** kuru / `LOW-BASE-HIGH` | *(ayrılmamıştı)* | ◐ **KOŞULLU** — `T-964` cevabına bağlı: ülke ayrıştırması tek gözlenen kurla yapılabiliyorsa **`CAN DECIDE LATER`** (FX ekseni, `P-5` damgalı); yapılamıyorsa **`MUST`** olur |
| **`N-2`** | dış temas izni | `MUST` | ✅ **VERİLDİ (koşullu)** → `P-6` |
| **`N-3a`** *(`D-14a`)* | hangi basamak `PRIMARY` | `LATER` | ✅ **VERİLDİ — 799** |
| **`N-3b`** | hangi **`L8` alt katmanı** | **`MUST`** | ⛔ **AÇIK — tek kalan `MUST DECIDE NOW` kalemi** |
| `N-3c` | `TARGET_CHANNEL` | *(yoktu)* | ⚠ **AÇIK, ama önce AJANA** — `N-3b`'den türeyip türemediği `T-966`'da; türemiyorsa yatırımcıya gelir |

> ## SONUÇ: **`MUST DECIDE NOW` = 1 KALEM** *(+1 koşullu)*
>
> ```
> N-3b — 799 TL HANGI RAFIN FIYATIDIR?
>        L8_CHAIN_RETAIL | L8_METRO_CASH_CARRY | L8_ONLINE_UZMAN_PERAKENDE | KANAL KARMASI
>        Tek kelimelik cevap yeterlidir. Bir sayi istenmemektedir.
>        Model ciktisina bakmaya gerek YOKTUR — bakilacak sey KENDI BEYANINIZDIR.
> ```
>
> Liste **3 → 1**'e indi. Ama bu bir **ilerleme raporu değildir**: inen iki
> kalemin biri **verildi** (`N-2`), diğeri **yanlış masadaydı** (`N-1a`).
> Kalan tek kalem, TUR 3A'da da `MUST` olan ve **hâlâ cevaplanmamış**
> olandır.

## 5.1 `fx` — istenen netleştirme

**Soru:** *`fx` bir yatırımcı kaydı olarak hâlâ senaryo seçimi gerektiriyor
mu, yoksa gözlem yeterli mi?*

**Cevap: GÖZLEM YETERLİ DEĞİLDİR — ama eksik kalan kısım büyük ölçüde
yatırımcıda DEĞİLDİR.**

| Ayak | Nedir | Kimde |
|---|---|---|
| **`N-1a`** — gözlenen spot kur (3 sayı + tarih + kaynak) | Bir **olgudur**, `evidence_id` alır, `FACT` olabilir | **AJAN** (`gumruk-vergi-uzmani`, bu tur) |
| **`N-1b`** — model hedef tarihindeki kur | Hedef tarihlerin **üçü de 2027'dedir** → **gözlenemez**; bir projeksiyon noktasıdır | **YATIRIMCI** *(ertelenebilirliği `T-964`'e bağlı)* |
| **beyan kuru** — gümrükte hangi kur | Bir **mevzuat** sorusudur | **AJAN** (`T-911`) |

⚠ **Kayda geçirilen risk:** `senaryolar.yaml` → `tarih_senaryolari`
bağlayıcı kuralı ÖTV için *"bugünkü doğrulanmış tutar bu üç tarihin hiçbiri
için geçerli kullanılamaz"* der. **Aynı kural fx için yazılmamıştır.**
`T-858(b)` tam olarak bu hatanın bandrolde yapıldığını göstermiştir.
→ `T-965`. **Başkan bu kuralın fx'e uygulanıp uygulanmayacağını kendi
kararlaştırmamıştır** — çünkü bu, kur ve matrah alanının uzmanına aittir.

---

# §5B — EŞZAMANLILIK BULGUSU *(bu belge yazılırken ortaya çıktı)*

Ticket indeksi dosya sistemiyle karşılaştırıldığında **üçüncü bir kayıt
sapması** çıktı — ama bu sefer nedeni farklı:

```
TUR 3A indeksi           : 125 ticket
Dosya sistemi (derleme 1): 145   -> 8'i bu belgenin actigi, 12'si INDEKSTE YOK
Dosya sistemi (derleme 2): 148   -> +3 (T-865, T-866, T-867) BU BELGE YAZILIRKEN acildi
```

**Bu bir "unutuldu" hatası değildir.** `T-821`…`T-823` ve `T-885`…`T-893`,
TUR 3.25'te **paralel çalışan** `navlun-lojistik-uzmani` ve
`global-sourcing-kasifi` tarafından açılmıştır. TUR 3.25'te birden fazla
ajan **eşzamanlı** çalışmaktadır; indeks derlendiği anda doğru olup bir saat
sonra yanlış olabilir. Onbeşi de indekse eklendi.

## 5B.1 — ⚠ AÇIK `CRITICAL` SAYISI DEĞİŞTİ: **11 → 12**

**`T-885`** (`global-sourcing-kasifi` → başkan, **CRITICAL, OPEN**):

> *"10 tedarikçilik RFQ paketi hazırlandı (2 mail varyantı + response sheet +
> contact pack). 7 hedef `READY_TO_SEND`. **HİÇBİR MESAJ GÖNDERİLMEDİ.**
> Fiilî gönderim, her hedef için `RECIPIENT` + `SUBJECT` + `PREVIEW`
> onayına bağlıdır."*

> ### Bu ticket, `P-6.3`'ün ticket karşılığıdır — ve ajan onu **başkan
> kuralı koymadan önce** açmıştır.
> Yani `P-6` kapısı bir başkan icadı değil, sahada **zaten uygulanan**
> davranışın kurala bağlanmasıdır. Bu, kuralın **uygulanabilirliğine** dair
> ilk kanıttır.

## 5B.2 — Bu turda açtığım iki ticket **kısmen zaten yapılmış**

| Benim ticket'ım | Paralel ajan karşılığı | Sonuç |
|---|---|---|
| **`T-967`** *(sourcing `P-6.2` paketi)* | **`T-885`** — paket hazır, 7 hedef `READY_TO_SEND`; ayrıca `T-886`…`T-893` (kanal/kimlik/numune boşlukları) | Kapsamım **daraldı**: geriye `T-467` soru 3 değerlendirmesi + hacim kademelerinin pakete işlenmesi kalır |
| **`T-968`** *(forwarder `P-6.2` paketi)* | **`T-821`** — 3 forwarder paketi hazır, gönderilmemiş; **`T-823`** — `T-913` Ayak A'yı ikiye ayırıp cevaplamış | Kapsamım **daraldı**: `T-823` zaten *"aynı kaynaktan yeniden çekme bir okuma işlemidir, dış temas değildir"* diyor |
| **`T-963`** *(V10K satırı)* | **`T-865`** — `finans-fizibilite` **bağımsız olarak aynı bulguyu** yazmış: *"V2 = 10.000 `country-buying-ceilings.csv` içinde YOK"* | **Çapraz doğrulama.** İki ajan aynı boşluğu birbirinden bağımsız buldu |

**Hiçbir ticket silinmedi.** Örtüşen kapsamlar ticket'ların içinde
**bağlanarak** işaretlendi; mükerrer iş yapılmasını önleyen şey ticket'ın
kapatılması değil, **atıflandırılmasıdır.**

⚠ Ve bir gözlem kayda geçirilir: **`T-892`** (gönderici kimlik alanları
`<COMPANY>`/`<NAME>`/`<EMAIL>`/`<DEADLINE>` **boş**) ile **`T-885`**
birlikte okunduğunda, paket *"`READY_TO_SEND`"* etiketli olmasına rağmen
**kimin adına gönderileceği tanımsızdır.** Bu, `P-6.3` önizlemesinin
**ilk kontrol kalemidir.**

---

# §6 — DEĞİŞMEYENLER *(kayıt)*

| Kalem | Durum |
|---|---|
| Reddedilen ajan bulgusu | **0** |
| `impact` değiştirilen ticket | **0** |
| `RESOLVED`/`REJECTED` edilen ticket | **0** |
| Açık `CRITICAL` ticket | **12** ⚠ *(11 değil — `T-885` paralel ajan tarafından açıldı; bkz. §5B)* |
| Eşiğe yazılan sayı | **0** |
| `karar-gunlugu.md` | **dokunulmadı** |
| Yeni kanıt kartı | **0** *(kurucu beyanı bir dış olgu değildir)* |
| `G0`…`G5` gate durumu | **değişmedi** — `G2`, `G3` hâlâ `BLOCKED` |
| `OQ-901` | **`OPEN`** — eşikler hâlâ `TBD`; `D-14a` kapandı ama `OQ-901` bir eşik sorusudur ve `T-851` açıktır |

---

# §7 — KURUCUYA GERİ DÖNEN TEK SORU

```
799 TL HANGI RAFIN FIYATIDIR?
  L8_CHAIN_RETAIL / L8_METRO_CASH_CARRY / L8_ONLINE_UZMAN_PERAKENDE / KANAL KARMASI
```

Ve bir **bilgi notu, bir soru değil:** `L8_CHAIN_RETAIL` seçilirse, o
katmanda elimizde **sıfır fiyat gözlemi** olduğu bilinerek seçilmiş olur.

---

## Bu kararı ne çürütür?

*(Bu belge bir yatırım kararı içermez. Aşağıdaki soru, bu belgenin **kayıt ve
yapılandırma hükümlerine** ilişkindir.)*

### En güçlü tek çürütücü: **kademelerin BAZI "sipariş başına" çıkarsa**

Bu belgedeki yapılandırmanın tamamı — `V1↔V5K … V4↔V50K` eşlemesi, LCL/FCL
kırılma noktası yorumu, `V100K`'nın "çapasız" sayılması, hatta
`T-963`'ün içeriği — kademelerin **yıllık hacim** okumasına daha yakın
olduğu varsayımıyla düzenlenmiştir *(bu yüzden `PROVISIONAL` etiketlendi)*.

**Eğer kurucu "sipariş başına" demek istediyse:**
- `V4 = 50.000 şişe/sipariş` ≈ **7 × 20DV** demektir — bu bir pilot değil,
  bir **ölçek operasyonudur** ve `V1…V4`'ün tamamı `hacim_senaryolari` ile
  **eşleşmez**;
- `FULL_20FT` kademesi `V1` ile `V2` arasına düşer ve **ayrı bir kademe
  olmaktan çıkar**;
- `T-962` ve `T-963`'ün soruları **yanlış sorulmuş** olur.

**Nasıl ararız:** `T-961`'in birinci sorusu tam olarak budur ve **kurucuya
tek cümlelik bir doğrulama** ile kapanır. Bu, bu belgedeki en ucuz ve en
yüksek getirili tek doğrulamadır.

### İkinci çürütücü — `P-6`'yı hedefler

**`P-6.3`'ün (her mesaj için tek tek açık onay) uygulanamaz olduğunun
ortaya çıkması.** 26 tedarikçi + 3 forwarder × ayrı önizleme = **29 ayrı
onay turu.** Kurucu, "otomatik toplu mail yok" derken **onay yükünün bu
büyüklükte** olduğunu görmemiş olabilir. Pratikte olacak şey şudur: onay
turları yorulur ve `P-6.3` sessizce *"toplu önizleme + tek onay"*a dönüşür —
yani kurucunun **açıkça yasakladığı şeye.**

**Nasıl ararız:** `T-967`/`T-968` paketleri geldiğinde **alıcı sayısına
bakılır.** İlk dalgada 7'den fazla alıcı varsa `P-6.3` ile `P-6.4`
arasındaki gerilim **gerçek** demektir ve kurala bir **dalga/parti tanımı**
eklenmesi kurucudan istenmelidir.

### Bu belgenin kör noktası

**Kurucu üç karar verdi ve üçü de "ileri git" yönünde.** Bu belge, bu
kararların **sonuçlarını** yazdı ama hiçbirinin **gerekçesini
sorgulamadı** — çünkü sorgulamak başkanın işi değildir. Ancak şu kayda
geçirilmelidir: `799 PRIMARY` seçimi, `sweet-spot-analizi.md` §3.1'in
**önerisiyle birebir aynıdır** (799 `PRIMARY` / 699 `SECONDARY` / 899
`STRETCH` / 599 `FLOOR`). Bu bir **bağımsız doğrulama değildir** —
büyük olasılıkla aynı belgenin **okunmuş** olmasıdır. `seytanin-avukati`
TUR 4'te bunu **`IR-4` (hedef kaydırma) değil, ÇAPALAMA (anchoring)**
saldırı vektörü olarak kullanmalıdır: modelin önerdiği sayının yatırımcı
kararı olarak geri dönmesi, o sayıyı **doğrulamaz**.
