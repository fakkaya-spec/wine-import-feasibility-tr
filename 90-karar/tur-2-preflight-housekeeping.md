# TUR 2 PRE-FLIGHT — KAYIT BAKIMI VE GATE GÜNCELLEMESİ

```yaml
belge:              tur-2-preflight-housekeeping
yazan:              yatirim-komitesi-baskani
tarih:              2026-08-10
kapsam:             KAYIT BAKIMI (housekeeping) + GATE GUNCELLEMESI
tur:                TUR 2 PRE-FLIGHT
karar_iceriyor_mu:  false
arastirma_yapildi_mi: false      # CLAUDE.md §1.16 — baskan arastirma yapmaz
yeni_kanit_uretildi_mi: false    # hicbir yeni evidence karti acilmadi
```

> ## BU BELGE BİR YATIRIM KARARI DEĞİLDİR
>
> `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` / `SCALE` kararlarının **hiçbiri**
> bu belgede verilmemiştir ve verilemez. Nihai karar **TUR 6**'da,
> `90-karar/karar-gunlugu.md` dosyasında verilir.
> **Bu turda `90-karar/karar-gunlugu.md` dosyasına DOKUNULMAMIŞTIR.**
>
> Bu belge yalnızca dört işi kayda geçirir: **(A)** T-201 kapanışı,
> **(B)** T-205/C-203'ün BUSINESS CONSTRAINT olarak sınıflandırılması,
> **(C)** T-504/T-551/C-551'in TUR 2 için de-blocking'i, **(D)** gate
> durumlarının güncellenmesi.

---

## 0. BU TURDA NE YAPILMADI (SINIR BEYANI)

| Yapılmadı | Neden |
|---|---|
| Yeni araştırma, web araması, yeni kanıt kartı | CLAUDE.md §1.16 — başkan araştırma yapmaz |
| 7584 s.K. / reklam / raf teşhiri konusunun incelenmesi | Kurucu kararı: bu konu **kabul edilmiş kısıttır**, yeniden araştırılmayacaktır |
| Ajan çağırma, TUR 2 araştırmasının başlatılması | Bu tur bir pre-flight'tır |
| Herhangi bir **değerin** değiştirilmesi (599,90 dahil) | CLAUDE.md — başkan başka ajanın bulgusunu kendi tahminiyle değiştirmez |
| Herhangi bir çelişki **metninin** silinmesi | CLAUDE.md §1.13 / §4 — kayıtlar immutable, üzerine yazılmaz |
| `90-karar/karar-gunlugu.md`'ye yazma | Karar TUR 6'ya aittir |

**Bu turda değişen tek şey kayıtların STATÜSÜDÜR, İÇERİĞİ DEĞİL.**

---

## A) `T-201` → **`RESOLVED`**

```yaml
ticket_id:        T-201
onceki_status:    ANSWERED  (mevzuat-ruhsat-uzmani, TUR 1.5)
yeni_status:      RESOLVED
resolution_type:  NON_MATERIAL_FOR_SCOPE
kapatan:          yatirim-komitesi-baskani
kapanis_tarihi:   2026-08-10
bagli_celiski:    C-201 -> RESOLVED — NON_MATERIAL
kalan_kayitlar:   C-251 (LOW, OPEN), C-252 (LOW, OPEN)
```

### A.1 Kapanışın çekirdeği: eşik, bizim ölçeğimizde bir ithalat engeli değildir

TUR 1.5 bulguları (`20-mevzuat/1m-litre-esigi.md`) **yeterlidir** ve kapanış
için gereken şeyi kanıtla göstermektedir. Kapanışı taşıyan zincir:

**1 — Ölçünün büyüklüğü düzeldi: 1.000.000 değil, en çok 600.000 litre/yıl.**
`EV-2026-08-10-204` (T1, 4619 s.K. Geçici m.1) ve `EV-2026-08-10-205`
(T1, Ticaret Yönetmeliği **Geçici m.6**): kademeli indirim takvimi **2006 yılı
sonunda 600.000 litre** ile sona erer. Ticket'ın sorduğu haliyle "1.000.000
litre/yıl eşiği" bugün uygulanan rakam değildir.

**2 — Eşik ithalat / dağıtım yetkisi / bedel eşiği DEĞİLDİR.**
`EV-2026-08-10-207` (T1): ithalat yapmak ve dağıtım yetki belgesi almak için
**asgari hacim şartı yoktur**; beyan edilen hacim bir yeterlilik ölçütü değil,
**bedel matrahıdır**. `EV-2026-08-10-206` (T1): Yönetmeliğin **esas
maddelerinde hiçbir hacim eşiği yoktur**.

**3 — Litre hesabı (`20-mevzuat/1m-litre-esigi.md` §7, `EV-2026-08-10-215`).**
litre/yıl = şişe/yıl × **0,75 L** (750 ml; `00-charter/kapsam.md` kapsam tanımı —
harici kaynak değildir, bu yüzden türetmeye T1 verilmemiştir).

| Senaryo | Şişe/yıl | **Litre/yıl** | 600.000 L'nin %'si | 1.000.000 L'nin %'si | Eşik aşıldı mı |
|---|---|---|---|---|---|
| S1 | 5.000 | **3.750** | %0,625 | %0,375 | **HAYIR** |
| S2 | 10.000 | **7.500** | %1,25 | %0,75 | **HAYIR** |
| S3 | 25.000 | **18.750** | %3,125 | %1,875 | **HAYIR** |
| S4 | 50.000 | **37.500** | %6,25 | %3,75 | **HAYIR** |
| S5 | 100.000 | **75.000** | **%12,5** | %7,5 | **HAYIR** |

Eşiğe **ulaşmak** için **800.001 şişe/yıl** (600.000 L ölçüsü) veya
**1.333.334 şişe/yıl** (1.000.000 L ölçüsü) gerekir — en büyük senaryonun
(S5) **8,0 / 13,3 katı**.

**4 — Yürürlükteki resmî tarife, eşiğin çok altındaki ithalatçıyı olağan bir
muhatap olarak fiyatlandırıyor.**
`EV-2026-08-09-206` / `EV-2026-08-09-207` + Tebliğ 2025/39 (yürürlük
2026-01-01): şarapta **≤20.000 litre/yıl** için ayrı ve **fiyatlanmış** bir
dağıtım yetki belgesi bedeli sınıfı (68.375 TL) vardır. İdare, 600.000 litrenin
**30 katı altında** faaliyet gösteren bir şarap ithalatçısı için bir sınıf
tanımlamaktadır.

### A.2 `resolution_evidence` (ticket dosyasına yazıldı)

**Kapanışı taşıyan çekirdek kanıtlar:**

| evidence_id | tier | ne kanıtlıyor | effective_date |
|---|---|---|---|
| `EV-2026-08-10-204` | T1 | 4619 Geç. m.1 — ölçü 600.000'de sona erer | 2001-01-20 |
| `EV-2026-08-10-205` | T1 | Yön. Geç. m.6 — takvim 2006 sonunda biter | 2003-06-06 |
| `EV-2026-08-10-207` | T1 | İthalat/dağıtım yetkisinde **asgari hacim YOK**; hacim = bedel matrahı | 2015-12-31 |
| `EV-2026-08-10-215` | T2 | Beş senaryonun litre aritmetiği (ESTIMATE) | — |
| `EV-2026-08-09-206` | T1 | ≤20.000 L/yıl ayrı ve fiyatlanmış bedel sınıfı | 2026-01-01 |

**Tam set** (16 kart, `EV-2026-08-10-201` … `-216`) ticket dosyasının
`resolution_evidence` alanında korunmuştur.

### A.3 Bu kapanışın AÇIKÇA iddia ETMEDİĞİ üç şey

1. **"Eşik hükmü ölüdür"** — iddia edilmemiştir. Aksine `EV-2026-08-10-208`
   (T1) 4250'nin uygulanmasının Bakanlığa devredildiğini, `EV-2026-08-10-210`
   (T1) 4733 m.8'in **belge iptali** yolunu açık tuttuğunu gösterir. Bunlar
   proje **aleyhine** bulgulardır. `mevzuat-ruhsat-uzmani` bunları kendi G0
   önerisinin aleyhine olmasına rağmen **kendisi işaretlemiştir**; bu davranış
   kayda geçirilmiştir.
2. **Muafiyet fıkrasının kapsamı hakkında bir seçim** — yapılmamıştır (C-252).
3. **"Ülke genelinde yerinde teslim" şartının ortadan kalktığı** — kalkmamıştır.
   Bu şart m.1/3'te **hacimden bağımsız** durur. Kapanan şey **eşiktir**.
   Bu şart bir G0 sorusu değil, bir **dağıtım maliyeti** sorusudur →
   `kanal-marj-uzmani` (`EV-2026-08-10-212` ile daraltılmış haliyle:
   Yönetmelik m.9/2 "ülke genelinde/yerinde teslim" **demez**).

### A.4 `C-201` → **`RESOLVED — NON_MATERIAL`**

`mevzuat-ruhsat-uzmani`'nın önerisi **aynen kabul edilmiştir**; ekleme veya
çıkarma yapılmamıştır. Üç ayaktan ikisi kanıtla düşmüş, üçüncüsü `C-252`
olarak ayrı kayda alınmıştır.

### A.5 `C-251` ve `C-252` → **AÇIK KALIR (LOW)** — gerekçe

**Karar: ikisi de `OPEN` kalır. Kapatmıyorum.**

| Neden kapatmıyorum | Neden bloke etmiyor |
|---|---|
| İkisi de **T1 ↔ T1 hukuki yorum** sorunudur. Çözüm hiyerarşisinin 1–5. kurallarının hiçbiri uygulanamaz. Kendi yorumumla kapatmam **CLAUDE.md §1.16 ihlali** olur. | Sonuç **girdi değerine duyarsızdır**: C-251'de 600.000 da 1.000.000 da olsa cevap aynıdır; C-252'de A da B de doğru olsa beş senaryo eşiğin altındadır. `model_girdisi_etkisi: YOK`. |

Bu, bir çelişkinin **çözülmeden zararsızlaştırıldığı** meşru bir durumdur ve
CLAUDE.md §3'ün `CONFLICT` etiketiyle uyumludur: çelişki **kayıtta durur**,
karara taşınır, ama modeli kilitlemez.

**C-251 ne zaman maddi olur:** Hedef hacim **800.001 şişe/yıl**'a yaklaşırsa
(S5'in 8 katı). `SCALE` tartışması bu hacmi aşarsa C-251 **otomatik olarak**
yeniden gündeme gelir.

**C-252 G0'ı ne zaman yeniden bloke eder — İKİSİ BİRDEN gerekir:**
(1) C-252'nin **B okuması lehine** kapanması, **VE** (2) "Tekel GM eliyle"
işlevi için yürürlükte bir **halef merci** tespiti (`EV-2026-08-10-214` bugün
`UNKNOWN`). Tek başına hiçbiri yetmez.

---

## B) `T-205` / `C-203` → **`ACCEPTED BUSINESS CONSTRAINT`**

```yaml
ticket_id:        T-205
onceki:           impact CRITICAL / status OPEN
yeni:             impact CONSTRAINT / status RESOLVED
resolution_type:  ACCEPTED_BUSINESS_CONSTRAINT
conflict_id:      C-203 -> ACCEPTED BUSINESS CONSTRAINT
karar_kaynagi:    KURUCU KARARI (baglayici, tartisilmaz)
g0_etkisi:        BLOKE ETMEZ
yeniden_arastirilacak_mi: HAYIR
```

### B.1 Kurucu kararı (bağlayıcı)

> *"Alkol ürünlerine ilişkin reklam / görsel / tanıtım kısıtları bu projede
> **bilinçli olarak kabul edilen bir BUSINESS CONSTRAINT**'tir."*

Bu bir **araştırma bulgusu değildir**; bir **kurucu tercihidir** ve o şekilde
etiketlenmiştir. Kanıt üretmez, kanıtı yorumlamaz — bir **planlama çerçevesi**
belirler.

### B.2 Bu sınıflandırma NE DEMEK

| Şudur | Şu DEĞİLDİR |
|---|---|
| Kısıt **doğrulanmıştır** (T1: 7584 s.K. m.2 ile 4250 m.6/1'e eklenen cümle, RG 20/6/2026-33286 — `EV-2026-08-09-223`) ve **kabul edilmiştir** | Kısıt "yok sayılmıştır" |
| Kısıt bir **belirsizlik** olmaktan çıkıp bir **VERİ** olmuştur | Kısıt "önemsizdir" / "hafiftir" |
| `kanal-marj-uzmani` bunu bir **girdi** olarak alır ve üzerine inşa eder | `kanal-marj-uzmani` bunu görmezden gelebilir |
| Planlama, kısıtın **var olduğu** dünyaya göre yapılır | `C-203`'ün dar/geniş yorum belirsizliği **çözülmüştür** |

**Kısıt kayıttan silinmemiştir.** `C-203`'ün metni, `mevzuat-ruhsat-uzmani`'nın
tespiti ve tüm kanıt kartları `99-ops/celiskiler.md`'de **aynen durmaktadır**.

### B.3 Neden bu sınıflandırma G0'ı bloke etmez

G0'ın sorusu: *"Bu iş Türkiye'de yasal olarak kurulabilir mi?"*
7584 s.K. m.2, alkollü içki **ithalatını, dağıtımını veya satışını yasaklamaz**;
**marka/ambalaj görsellerinin satış noktasında bulundurulmasını** kısıtlar.
Bu bir **kuruluş engeli** değil, bir **pazarlama kısıtıdır**. Kısıtın kabul
edilmesiyle G0 kapsamında cevaplanmamış bir soru kalmaz.

### B.4 Yön uyarısı — bu kabul MUHAFAZAKÂRDIR

Reklam/tanıtım/görsel kaldıraçlarının **yok** sayılması, kapsamın ileride
**dar yorum** lehine netleşmesi hâlinde proje **lehine** bir sürpriz bırakır.
Yani bu sınıflandırma bir **iyimserlik riski taşımaz**; taşıdığı risk
gereğinden fazla kötümser planlamadır ve o risk kurucu tarafından bilinçle
üstlenilmiştir.

### B.5 Operasyonel sonuç — `capraz-ipuclari.md`'ye bırakılan not

`99-ops/capraz-ipuclari.md` → **İP-2001** (`kanal-marj-uzmani` hedefli):

> **Marka bilinirliği reklamla kurulamaz → raf / kanal / fiyat üzerinden
> kurulur.** Bu, kanal ekonomisinin bir varsayımı değil, **başlangıç
> koşuludur.**

Üç doğrudan sonucu (hepsi `kanal-marj-uzmani`'nın alanındadır):
1. ATL/reklam bütçesi diye bir kalem yoktur; marka inşa harcaması varsa
   **kanal maliyeti** olarak görünür.
2. Kalan kaldıraçların (listeleme, raf konumu, dağıtım genişliği, fiyat)
   pazarlık ağırlığı orantısız biçimde yüksektir. *(Bu, bedellerin
   **büyüklüğü** hakkında bir iddia değildir — büyüklük ajanın kanıtıyla gelir.)*
3. Private label ile mevcut marka distribütörlüğü arasındaki risk asimetrisi
   **yapısaldır** ve iki modelin karşılaştırmasında **açıkça gösterilmelidir**.
   Private label **elenmemiştir** (`00-charter/karar-esikleri.md` ikisini eşit
   öncelikli tutar).

### B.6 Bu sınıflandırmayı ne geri açar

TADAB'ın (veya bir yargı kararının) yasağı **ürünün satış ünitesinde fiziksel
olarak bulundurulmasını** kapsayacak şekilde yorumlayan bağlayıcı bir metni.
Böyle bir metin çıkarsa `T-205` ve `C-203` `OPEN`'a döner ve konu **G0
kapsamına girer** — çünkü o zaman soru pazarlama değil, **kanalın var olup
olmadığıdır**.

---

## C) `T-504` / `T-551` / `C-551` → **TUR 2'yi BLOKE ETMEZ**

### C.1 Kurucu kararı — benchmark kullanım rejimi

Gold Country **599,90 TL** (ve Central Creek **649,90 TL**) için:

| # | Kural | Uygulandı |
|---|---|---|
| **B1** | Gözlenen **gerçek fiyat** olarak tutulur; değer **değiştirilmez** | `pazar.yaml` — 599.90 / 649.90 **aynen** |
| **B2** | **Metro cash & carry benchmark'ı** olduğu açıkça belirtilir; genel piyasa fiyatı değildir | `pazar.yaml` → `katman_kurallari.K5` + alan bazında `kullanim_kurali` |
| **B3** | Promosyon / normal ayrımı **`UNKNOWN` kalabilir** | `promosyon_durumu: null / UNKNOWN` **korundu** |
| **B4** | `C-551` nedeniyle **confidence düşürülür** | `HIGH → MEDIUM` (4 alan) |
| **B5** | **TUR 2'yi bloke etmez** | `blocking_status: NON_BLOCKING_TUR2` |
| **B6** | Modelde **tek gerçek piyasa fiyatı gibi kullanılamaz** | `katman_kurallari.K5` (bağlayıcı) |

### C.2 `T-504` — statü seçimi ve gerekçesi

```yaml
status:            OPEN            # KAPATILMADI
impact:            HIGH            # onceki: CRITICAL
blocking_status:   NON_BLOCKING_TUR2
hala_bloke_ettigi: [G3, OQ-001]
```

**Neden `OPEN` bıraktım (kapatmadım):** İstenen şey fiziksel bir gözlemdir ve
yapılmamıştır. `turkiye-pazar-kasifi` TUR 1.5'te **8 ayrı masabaşı yolu**
denemiş, hepsi kapalı çıkmıştır (`EV-2026-08-10-504`) ve `UNKNOWN`'ı
**zorlamamıştır** — bu doğru davranıştır. Ticket'ı "de-blocking" gerekçesiyle
kapatmak, yapılmamış bir gözlemi yapılmış saymak olurdu.

**Neden `impact: CRITICAL → HIGH`:** CRITICAL etiketinin **tek gerekçesi**
ticket'ın kendi ifadesiydi — *"promosyonlu bir fiyat benchmark alınırsa tüm
fiyat merdiveni kalıcı olarak ulaşılamayacak bir hedefe kurulur."*
**B6 bu arıza modunu kuralla ortadan kaldırır.** Benchmark artık modelde tek
hedef fiyat olamayacağı için "yanlış tek sayıya kilitlenme" riski kapanmıştır.
Geriye kalan risk (bandın tepe noktasının belirsizliği) **HIGH**'dır.

> **Bu bir kolaylık indirimi değildir.** Azalan şey belirsizlik değil, o
> belirsizliğin **modele sızma yoludur**. Belirsizliğin kendisi `UNKNOWN`
> olarak aynen durmaktadır ve **G3'ü bloke etmeye devam eder**.

### C.3 `T-551` — `RESOLVED (DIRECTIVE_ISSUED)`, dört sorunun dördü

Ticket bir araştırma değil, **başkandan dört soruya karar** talep ediyordu.
Dördüne de karar verildi → ticket kapanır. Bağlı çelişki `C-551` **açık kalır**.

| # | Soru | Karar |
|---|---|---|
| S1 | `C-551` `TARIH` mi `KAPSAM` mı? | **ÇÖZEMİYORUM** — kural 2 (tarih, A lehine) ile kural 4 (kapsam, B lehine) **zıt yönü** işaret ediyor; kural 1 (tier) uygulanamıyor (ikisi de T4, ikisi de Metro'nun kendi künyeli yayını). **Sessiz seçim yapılmadı.** C-551 `OPEN` + `NON_BLOCKING_TUR2`. |
| S2 | `kdv_durumu` `confidence` `HIGH` kalsın mı? | **HAYIR → `MEDIUM`.** Değer (`KDV_DAHIL`) **değiştirilmedi**. Gerekçe: sonuç, **sıfır alkol SKU'su** içeren broşürlerden şarap rafına yapılmış bir çıkarımdır ve tek Metro **şarap kategorisi** iletişiminde karşı örnek vardır. |
| S3 | **BM_B** senaryosu elensin mi? | **HAYIR — ELENMEZ.** Ajanın görüşü onaylandı. Elemek, C-551'i sessizce A lehine çözmek olurdu. *(Yalnızca eleme yasağıdır; yeni senaryo/ağırlık TUR 3'e aittir.)* |
| S4 | Denetim §5.5 satırı nitelensin mi? | **EVET, önerilen niteleme aynen kabul edildi** (aşağıda). |

**S4 — bağlayıcı niteleme.** `90-karar/tur-1-kanit-kalitesi-denetimi.md` §5.5
tablosundaki *"Etikette çiftli KDV gösterimi var mı? → ✅ KAPANDI — YOK"*
satırı bundan böyle şöyle okunur:

> **"2026 GENEL broşürlerinde YOK; 2010 ŞARAP kataloğunda VARDI;
> 2026 ŞARAP rafı GÖRÜLMEDİ."**

Denetim belgesi **geriye dönük düzeltilmemiştir** — o belge 2026-08-09 tarihli
bir kayıttır ve öyle kalır. Niteleme burada, bu belgede yaşar.

### C.4 `C-551` — `OPEN`, `NON_BLOCKING_TUR2`

Neden bloke etmiyor: B6 kuralı C-551'in modele sızma yolunu kapatır **ve**
etki yönü muhafazakârdır — sonuç "KDV hariç" çıkarsa benchmark'ın tüketici
karşılığı **yukarı** kayar, ters modelde ödenebilecek maksimum EXW/FOB **artar**,
yani proje **daha kolay** görünür. Mevcut `KDV_DAHIL` etiketi projeyi
kayırmıyor, **sıkıyor**.

Kapanış yolu değişmedi: **şarap reyonundaki fiziksel etiketin fotoğrafı**.
`C-551` ve `T-504` **aynı tek eylemle** kapanır.

### C.5 `pazar.yaml`'da yapılan tam değişiklik listesi

| Alan | Önce | Sonra | Değer değişti mi |
|---|---|---|---|
| `katman_kurallari.K5` | yok | **eklendi** (benchmark kullanım kuralı, bağlayıcı) | — |
| `katman_kurallari.K6` | yok | **eklendi** (confidence'ın anlamı) | — |
| `benchmark_1.raf_fiyati_try.confidence` | HIGH | **MEDIUM** | **HAYIR** — 599.90 aynen |
| `benchmark_1.kdv_durumu.confidence` | HIGH | **MEDIUM** | **HAYIR** — `KDV_DAHIL` aynen |
| `benchmark_2.raf_fiyati_try.confidence` | HIGH | **MEDIUM** | **HAYIR** — 649.90 aynen |
| `benchmark_2.kdv_durumu.confidence` | HIGH | **MEDIUM** | **HAYIR** |
| `benchmark_*.promosyon_durumu` | null / UNKNOWN | **değişmedi** | — |

**Confidence düşüşünün anlamı (K6'da kayıtlı):** düşen şey **piyasayı temsil
gücüdür**, sayının **okunuşu değil**. Bu ayrım `okuma_confidence: HIGH` alanı
ile korunmuştur.

---

## D) GATE GÜNCELLEMESİ

### D.1 G0 — önce blocker taraması

**Soru: `T-201` kapandıktan ve `T-205` constraint'e çevrildikten sonra G0
kapsamında BAŞKA gerçek ve açık bir hukuki blocker var mı?**

Aday kayıtlar tek tek incelendi ve **blocker** ile **zamanlama/uygulama riski**
ayrımı yapıldı:

| Kayıt | impact | Nedir | **Blocker mı?** |
|---|---|---|---|
| `C-252` (muafiyet fıkrasının kapsamı) | LOW | Lafzî yorum belirsizliği; her iki okumada da beş senaryo eşiğin altında | **HAYIR** — model girdisi etkisi YOK. Yeniden bloke etmesi için **iki koşul birden** gerekir (§A.5). |
| `C-251` (600.000 mi 1.000.000 mi) | LOW | Aynı; sonuç girdiye duyarsız | **HAYIR** |
| `T-202` / `C-202` (dağıtım yetki belgesi **işlem süresi** mevzuatta tanımsız) | HIGH | Belgenin **alınabildiği** tartışmalı değil; **ne kadar sürdüğü** bilinmiyor | **HAYIR — ZAMANLAMA RİSKİ.** Bir yasal engel, "belge verilmez" demektir; burada "ne zaman verilir bilinmiyor" denmektedir. Bu **T0 takvimini ve nakit ihtiyacını** etkiler, **yasallığı** değil. → **G4 / nakit modeli riski**, G0 değil. |
| `C-202` (bildirim ↔ belge ↔ ithalat **sıralama** döngüsü) | HIGH | Adımların hangi sırayla yapılacağı doğrulanmadı; `t0-takvimi.md` sırayı **`ASSUMPTION` olarak** işaretlemiştir | **HAYIR — SIRALAMA/ZAMANLAMA RİSKİ.** Hiçbir kanıt döngünün **kırılamaz** olduğunu iddia etmiyor. *(Uyarı: bir kanıt döngünün fiilen kilitlendiğini gösterirse bu **G0'a döner** — aşağıdaki izleme listesine alındı.)* |
| `T-102` (alkol ithalat denetimi tebliği / uygunluk prosedürü) | HIGH | Prosedürel doğrulama eksiği | **HAYIR** — bir yasak değil, doğrulanmamış bir **süreç adımı**. G1/G4 kapsamında izlenir. |
| `C-204` (TGK Şarap Tebliği'nin mülga kanuna dayanması) | LOW | Etiket kuralının **hangi metinden** okunacağı belirsiz | **HAYIR** — uyum detayı; "etiket kuralı yoktur" veya "ithalat yasaktır" denmiyor. |
| `T-206` (zorunlu laboratuvar analizi) | MEDIUM | Var mı, parti başı mı bilinmiyor | **HAYIR** — maliyet/takvim kalemi |
| `T-403` (Türkçe arka etiket nerede uygulanır) | HIGH | Operasyonel | **HAYIR** |
| `T-502` (alkolün internetten tüketiciye satış yasağı) | MEDIUM | **Bizim kanalımız değil** | **HAYIR** — kanal kısıtı |

**Sonuç: G0 kapsamında kaldırılamaz veya çözülmemiş bir hukuki blocker
YOKTUR.**

### D.2 `G0` → **`PASS`**

```yaml
gate:            G0 — YASAL YOL
onceki_durum:    BLOCKED (kosullu) — 2026-08-09
yeni_durum:      PASS
karar_veren:     yatirim-komitesi-baskani
karar_tarihi:    2026-08-10
oneri_sahibi:    mevzuat-ruhsat-uzmani (G0 PASS onerisi, TUR 1.5) — KABUL EDILDI
```

**Gerekçe — dört adım:**

1. **G0'ı BLOCKED bırakma gerekçem tekti ve o gerekçe kalkmıştır.** 2026-08-09
   denetiminde yazdığım şey: *"`T-201` ve `C-201` doğrudan G0'ın sorusunu
   hedefler."* Her ikisi de bugün `RESOLVED`'dır (§A). Ayrıca aynı denetimde
   *"G0, `T-201` olumsuz olmayan bir cevapla kapandığı anda **`PASS`'e döner**
   — ek araştırma turu gerekmez"* diye taahhüt etmiştim. O koşul gerçekleşti.
2. **İkinci gerekçe (`C-203` / `T-205`) kurucu kararıyla constraint'e
   çevrilmiştir** ve §B.3'te gösterildiği gibi bir **kuruluş engeli değildir**.
3. **Kalan hiçbir kayıt blocker değildir** (§D.1). `T-202` ve `C-202`
   **zamanlama/sıralama riskidir** ve gate'leri G4 tarafında etkiler.
4. **`G0 FAIL` için hiçbir dayanak yoktur** ve `mevzuat-ruhsat-uzmani`'nın
   dört tespiti (yasaklayıcı hüküm yok; belge seti tanımlı ve 2026 bedelleri
   RG ile bilinir; depo zorunluluğu akde bağlanmış dağıtım ağıyla
   karşılanabilir; yürürlükteki tarife ≤20.000 L/yıl sınıfını tanır)
   değiştirilmeden kabul edilmiştir.

**`G0 PASS` NE DEMEK — sınırları:**

| Demek | Demek DEĞİL |
|---|---|
| Türkiye'de şarap ithalatçısı olarak **yasal kurulum yolu vardır** ve gerekli belge seti **tanımlıdır** | "Hukuki risk sıfırdır" |
| Bilinen hiçbir hüküm bu ölçekte ithalatı **yasaklamamaktadır** | "Bütün mevzuat soruları cevaplanmıştır" |
| Diğer gate'ler **kendi gerekçeleriyle** değerlendirilir | "Proje yapılabilir" *(bu bir yatırım kararıdır ve verilmemiştir)* |

**G0 izleme listesi (PASS'i geri alacak üç tetikleyici):**

| # | Tetikleyici | Nereden gelir |
|---|---|---|
| **R1** | `C-252` **B okuması lehine** kapanır **VE** "Tekel GM eliyle" işlev için **halef merci** tespit edilir *(ikisi birden)* | TADAB yazılı görüşü / hukuk mütalaası |
| **R2** | 7584 s.K. m.2'nin **ürünün rafta bulundurulmasını** kapsadığı bağlayıcı bir metinle ortaya çıkar | TADAB ikincil düzenlemesi / yargı kararı |
| **R3** | `C-202` sıralama döngüsünün **fiilen kilitlendiği** (belge alınamadan bildirim, bildirim olmadan belge) kanıtlanır | TADAB uygulaması / faal ithalatçı görüşmesi |

### D.3 Güncel gate durum tablosu — 2026-08-10

| Gate | Soru | Sahibi | **Durum** | Değişim | Açan tek koşul |
|---|---|---|---|---|---|
| **G0** Yasal yol | Bu iş Türkiye'de yasal olarak kurulabilir mi? | `mevzuat-ruhsat-uzmani` önerir → **başkan karar verir** | **PASS** | ⬆️ `BLOCKED` → **`PASS`** | — *(izleme: R1/R2/R3)* |
| **G1** Vergi yapısı | Vergi yükü kanıtlı ve satır satır hesaplanabilir mi? | `gumruk-vergi-uzmani` | **BLOCKED** | ⬆️ daraldı (3 boşluktan 1'i kapandı) | `T-104` (ÖTV zaman endeksli) + gözetim/referans kıymet |
| **G2** Tedarik | Gerçek, ulaşılabilir tedarik kaynağı ve fiyatı var mı? | `global-sourcing-kasifi` | **BLOCKED** | değişmedi | Gerçek RFQ cevabı (≥5 tedarikçi); `exw/fob` hâlâ `null` |
| **G2-L** Lojistik / landed | L1→L2→L3 geçişi kanıtla kurulabiliyor mu? | `navlun-lojistik-uzmani` | **BLOCKED** | değişmedi | `T-304` — 3 forwarder'dan yazılı kotasyon |
| **G3** Pazar | Benchmark doğrulandı mı, segment gerçek mi? | `turkiye-pazar-kasifi` | **BLOCKED** | değişmedi *(de-blocking ≠ gate açılışı)* | **OQ-001'in promosyon ayağı** (`T-504`) + fiziksel raf etiketi |
| **G4** Ekonomi | Model kanıtlı girdilerle pozitif contribution veriyor mu? | `finans-fizibilite` | **NOT_EVALUATED** | değişmedi | G1 + G2 + G2-L + G3 |
| **G5** Risk | Kırmızı takımın CRITICAL ticket'ları kapandı mı? | `seytanin-avukati` | **NOT_EVALUATED** | değişmedi | TUR 4 |

> **Gate kuralı (değişmedi):** Kapsamında `impact: CRITICAL` açık ticket veya
> çözülmemiş CRITICAL çelişki bulunan gate `PASS` alamaz.
> **`blocking_status: NON_BLOCKING_TUR2` bir gate açmaz** — yalnızca TUR 2'nin
> başlamasını durdurmaz.

### D.4 G1 — TUR 1.5 sonrası durum (üç boşluğun biri kapandı)

| # | Boşluk (2026-08-09 denetimi) | **Durum 2026-08-10** |
|---|---|---|
| 1 | **İthalatta ödenen KDV indirilebilir mi?** | ✅ **KAPANDI** — `OQ-G01`. KDVK md.29/1-b + md.34/1 + md.30 **tahdidi liste** taraması (T1): `EV-2026-08-10-101`, `-102`, `-103`. Cevap: **EVET, indirilebilir** → KDV **ekonomik maliyet değildir**; ama `peak_cash_requirement`'a **tam tutarıyla** girer (md.29/2: devreden KDV **iade edilmez**). |
| 2 | **Model hedef tarihinde geçerli ÖTV tutarı** | ❌ **AÇIK** — daraldı. `BASE_DATE = 2026-08-10` konvansiyonu tanımlanmış olsa da `model_hedef_tarihi` hâlâ `null` (`OQ-002`, **yatırımcı girdisi**) ve **`T-104` (CRITICAL) OPEN**: ÖTV modelde sabit sayı olamaz. |
| 3 | **Gözetim / referans kıymet var mı?** | ❌ **AÇIK** — TUR 1.5'te **kapsam dışı** ilan edilmiştir. Negatif arama; "yokluğun kanıtı değildir" doğru şekilde korunmuştur. |

Ayrıca TUR 1.5'te **üç yeni soru** açılmıştır ve G1'in altında izlenir:
`OQ-G09` (fiili KDV vergilendirme dönemi 1 ay mı 3 ay mı — `peak_cash`'i
büyütür, `T-152`), `OQ-G10` (KDVK md.36 CB kararları taranmadı — bulunursa
`OQ-G01`'in cevabı **tersine döner**, `T-151`), `OQ-G11` (LOW).

> **`OQ-G10` özellikle kayda geçirilir:** OQ-G01'in kapanışı, md.36 uyarınca
> çıkarılmış bir Cumhurbaşkanı Kararı **aranmamış** olması kaydıyla geçerlidir.
> Ajan bunu kendisi işaretlemiştir. Bu, G1'in en kırılgan yeridir.

### D.5 G3 — `C-551` sonrası durum

**`BLOCKED` — değişmedi. Başkan kuralı yürürlüktedir: OPEN QUESTION #001
kapanmadan G3 geçilemez.** `OQ-001` `PARTIALLY_RESOLVED`'dır.

| OQ-001 ayağı | Durum 2026-08-10 |
|---|---|
| KDV dahil mi? | ⚠️ **KAPANDI ama NİTELENDİ** — `KDV_DAHIL` korunur, `confidence` **MEDIUM**'a çekildi, `C-551` **OPEN / NON_BLOCKING_TUR2**, `BM_B` **elenmez** |
| Tüketiciye açık mı / cash & carry mi? | ✅ KAPANDI — ikisi de |
| Etikette çiftli KDV gösterimi var mı? | ⚠️ **NİTELENDİ** (§C.3 S4): *"2026 genel broşürlerinde YOK; 2010 şarap kataloğunda VARDI; 2026 şarap rafı GÖRÜLMEDİ"* |
| **Promosyonlu mu, normal fiyat mı?** | ❌ **UNKNOWN** — `T-504` (HIGH, **OPEN**, `NON_BLOCKING_TUR2`) |
| **Zincir market gerçek L8'i** | ❌ **UNKNOWN** — `OQ-502`; `l8_chain_retail` hâlâ `null` |
| **Şarap reyonundaki fiziksel etiket** | ❌ **GÖRÜLMEDİ** |

Ek olarak `C-501` (HIGH) açıktır ve `pazar_hacmi.ithalat_hacmi_litre` hâlâ
`UNKNOWN`'dır — ikincisi `SCALE` hedefinin doğrulanamaması demektir.

**Not:** C-551'in ortaya çıkması G3'ü **daha da açmamış**, aksine KDV ayağının
güvenini **düşürmüştür**. G3'ün durumu bu turda iyileşmemiştir.

---

## E) AÇIK CRITICAL TICKET DURUMU

**Önce: 6 · Şimdi: 3**

| ticket | hedef ajan | konu | neyi bloke ediyor |
|---|---|---|---|
| `T-104` | `finans-fizibilite` | ÖTV maktu tutarı Yİ-ÜFE ile 6 ayda bir kendiliğinden artar; modelde **sabit sayı olamaz** | **G1, G4** |
| `T-301` | `mevzuat-ruhsat-uzmani` | Ruhsat/analiz/bandrol nedeniyle malın gümrükte + antrepoda bekleme süresi; bandrolün fiziksel yeri | **G2-L, G4** *(limanda mı antrepoda mı beklendiği ~30 kat maliyet farkı)* |
| `T-304` | `yatirim-komitesi-baskani` | Hiçbir rota için doğrulanmış navlun yok | **G2-L, G4** |

**CLAUDE.md §5 yürürlüktedir:** bu üçü açıkken `finans-fizibilite` çıktısı
`APPROVED` olamaz — en fazla `DRAFT`.

**Kapanan üç CRITICAL kaydın nasıl kapandığı (şeffaflık):**
- `T-201` → **kanıtla** kapandı (16 T1/T2 kartı, litre aritmetiği).
- `T-205` → **kurucu kararıyla** kısıt olarak kabul edildi *(kanıtla
  çözülmedi — bu açıkça yazılmıştır)*.
- `T-504` → **kapanmadı**; impact'i gerekçeli olarak HIGH'a indirildi ve
  TUR 2 için de-block edildi. **G3'ü hâlâ bloke ediyor.**

Ayrıca **`OQ-901` (CRITICAL, sahibi: yatırımcı)** açıktır:
`00-charter/karar-esikleri.md`'deki **karar eşiklerinin tamamı `TBD`'dir.**
Bu araştırmayla kapanmaz ve **TUR 6'da nihai kararı bloke eder.**

---

## F) TUR 2 HAZIRLIK DURUMU (bilgi — bu turda TUR 2 BAŞLATILMAMIŞTIR)

2026-08-09 denetiminde `kanal-marj-uzmani` önündeki beş engel (E1–E5)
sayılmıştı. Güncel durum:

| # | Engel | Durum 2026-08-10 |
|---|---|---|
| **E1** | `T-205` / `C-203` — 7584 s.K. raf kapsamı (*"en büyük tek belirsizlik"*) | ✅ **KALKTI** — `ACCEPTED BUSINESS CONSTRAINT`; artık bir **girdi** (İP-2001) |
| **E2** | L5/L6 yokluğu — ithalatçı maliyeti hesaplanamıyor | ❌ **DURUYOR** — fiyat, navlun `null`. Kanal marjı **yüzde** olarak araştırılabilir, **TL** olarak kapatılamaz |
| **E3** | `T-504` — benchmark promosyonlu mu | ⚠️ **DURUYOR ama BLOKE ETMİYOR** (`NON_BLOCKING_TUR2`) |
| **E4** | `OQ-502` — zincir market gerçek L8'i hiç gözlenmedi | ❌ **DURUYOR** |
| **E5** | `pazar.yaml` yok | ✅ **KALKTI** — `T-903` `RESOLVED`, dosya mevcut ve K1–K6 kurallarıyla bağlanmış |

**2026-08-09 kapsam kısıtlamasında değişen tek madde:** *"`T-205` kapanmadan
7584 s.K.'nın kanal etkisi hakkında sonuç yazamaz — yalnızca iki yorumu ayrı
senaryo olarak modelleyebilir"* **maddesi düşmüştür.** Yerine İP-2001 geçer:
kısıt tek bir kabul edilmiş çerçeve olarak alınır, iki senaryoya bölünmez.
Diğer üç kısıtlama (**hedef EXW/FOB hesaplayamaz**, **kapalı fiyat merdiveni
kuramaz**, **`L8_METRO_CASH_CARRY`'yi L7/L8_CHAIN_RETAIL yerine kullanamaz**)
**aynen yürürlüktedir**, artı yeni **K5/K6**.

---

## G) BU TURDA GÜNCELLENEN DOSYALAR

| Dosya | Ne yapıldı |
|---|---|
| `90-karar/tur-2-preflight-housekeeping.md` | *(bu dosya)* — yeni |
| `99-ops/tickets/T-201.md` | `ANSWERED` → **`RESOLVED`**; KAPANIŞ bölümü dolduruldu; ajan cevabı **korundu** |
| `99-ops/tickets/T-205.md` | `OPEN/CRITICAL` → **`RESOLVED`/`CONSTRAINT`** (`ACCEPTED_BUSINESS_CONSTRAINT`); geçmiş içerik **korundu** |
| `99-ops/tickets/T-504.md` | `OPEN` **kaldı**; `CRITICAL` → `HIGH`; `blocking_status: NON_BLOCKING_TUR2`; TUR 1.5 doğrulama kaydı **korundu** |
| `99-ops/tickets/T-551.md` | `OPEN` → **`RESOLVED`** (`DIRECTIVE_ISSUED`); dört soruya karar; `C-551` **açık bırakıldı** |
| `99-ops/celiskiler.md` | C-201, C-203 satırları güncellendi + **§TUR 2 PRE-FLIGHT — BAŞKAN KAYITLARI** eklendi (C-201, C-251, C-252, C-203, C-551). **Hiçbir metin silinmedi** |
| `99-ops/tickets/INDEX.md` | Güncel statülerle yeniden üretildi (38 ticket, açık CRITICAL 6 → 3) |
| `80-model/inputs/pazar.yaml` | K5/K6 eklendi; 4 alanda `confidence` HIGH → MEDIUM; `kullanim_kurali` eklendi. **Hiçbir DEĞER değişmedi** |
| `99-ops/capraz-ipuclari.md` | İP-2001 (`kanal-marj-uzmani` — kısıt bir veridir) ve İP-2002 (benchmark kullanımı) eklendi |

**`90-karar/karar-gunlugu.md` dosyasına DOKUNULMAMIŞTIR.**
**Hiçbir kanıt kartı (`10-evidence/raw/`) değiştirilmemiş veya eklenmemiştir.**

---

## H) REDDEDİLEN BULGU LİSTESİ

**Bu turda reddedilen ajan bulgusu: 0.**

- `mevzuat-ruhsat-uzmani`'nın `G0 PASS` önerisi **kabul edilmiştir** (2026-08-09'da
  aynı ajanın `PASS (koşullu)` **etiketini** reddetmiştim; bu turda etiket
  reddi **kalkmıştır** çünkü reddin dayandığı `T-201`/`C-201` kapanmıştır).
- `turkiye-pazar-kasifi`'nın `T-551` önerileri (confidence düşürme, BM_B'yi
  elememe, denetim satırını niteleme) **kabul edilmiştir**.
- `turkiye-pazar-kasifi`'nın `T-504`'ü kapatmama kararı **kabul edilmiştir** —
  ticket açık bırakılmıştır.

**Düzeltilen tek kayıt hatası:** `99-ops/celiskiler.md` TUR 1.5 tablosunda
`C-551` `CRITICAL` yazıyordu; aynı çelişkinin kendi `yaml` bloğunda ve
`T-551`'de `HIGH` yazmaktadır. **Ajanın kendi bloğundaki değer (HIGH) esas
alınmıştır.** Bu bir değerlendirme değişikliği değil, bir tutarsızlık
düzeltmesidir ve dipnotla işaretlenmiştir.

---

## Bu kararı ne çürütür?

*(Bu belge bir yatırım kararı içermez. Aşağıdaki soru bu turda verilen
**dört hükme** — T-201 kapanışı, T-205 sınıflandırması, T-504 de-blocking'i
ve **G0 PASS** — ilişkindir.)*

### En güçlü tek çürütücü bulgu

**TADAB'ın, 4250 s.K. m.1/3'ün fiyat belirleme serbestisi koşulunu bugün de
uyguladığını gösteren yazılı bir işlemi veya duyurusu** — yani eşiğin altındaki
bir ithalatçının fiyatlandırma/dağıtım yetkisinin sınırlandığına dair
**tek bir somut idari uygulama örneği.**

Bu tek belge şu zinciri aynı anda kırar:
- `T-201`'in `NON_MATERIAL` kapanışı çöker — çünkü kapanış, mekanizmanın
  ikincil mevzuata **aktarılmamış olmasına** dayanıyordu (`EV-2026-08-10-206`,
  `-209`);
- `C-252`'nin "her iki okumada da sonuç aynı" gerekçesi geçersizleşir;
- **`G0` derhal `PASS` → `BLOCKED`** olur (tetikleyici R1);
- ters modelin (`target shelf price → max EXW/FOB`) **varlık sebebi** ortadan
  kalkar — fiyatı biz belirlemiyorsak modelin sorduğu soru anlamsızdır.

**Nasıl ararız:** `T-201`'in kendi doğrulama yolu değişmemiştir — (1) TADAB'a
KEP ile yazılı görüş talebi, (2) TADAB "Yetkili Dağıtım Firmaları
Listesi"nden **eşiğin çok altında faaliyet gösteren** küçük ölçekli şarap
ithalatçılarının tespiti, (3) alkol mevzuatında uzman hukuk bürosu mütalaası.
**Maliyeti düşük, bilgi getirisi yüksektir** ve aynı temas U-1, U-4, U-5 ve
`C-202` sıralama sorusunu da aydınlatır.

### İkinci en güçlü çürütücü (farklı hükmü hedefler)

**Şarap reyonundaki fiziksel raf etiketinin fotoğrafı** — üzerinde "üstü çizili
eski fiyat" veya "AVANTAJLI FİYAT" rozeti bulunması. Bu, `T-504`'ün
de-blocking'ini değil (o kural olarak duruyor), **benchmark'ın kendisini**
çürütür: 599,90 promosyonluysa fiyat merdiveninin tepesi yanlış yerdedir.
Aynı fotoğraf `C-551`'i de kapatır. **Tek kişi, ~15 dakika, ~0 TL** — projedeki
en yüksek bilgi/maliyet oranına sahip eylem olmaya devam etmektedir.

### Bu turun en tartışmalı hükmü

**`T-504`'ün `CRITICAL` → `HIGH` indirilmesi.**

Karşı argüman güçlüdür: *"Bir ticket'ın impact'ini, o ticket'ın konusu
değişmeden, yalnızca bir kullanım kuralı koyarak düşürmek, gate kuralını
etrafından dolaşmaktır."* Bu itiraz ciddiye alınmalıdır ve `seytanin-avukati`
TUR 4'te bunu hedef almalıdır.

**Savunmam:** İmpact, belirsizliğin **büyüklüğünün** değil, **modele verdiği
zararın** ölçüsüdür. B6 kuralı (benchmark tek gerçek piyasa fiyatı olarak
kullanılamaz) o zararı kesmiştir. Ayrıca indirim **maskelenmemiştir**:
ticket `OPEN` kalmış, `hala_bloke_ettigi: [G3, OQ-001]` alanı eklenmiş ve
**G3 `BLOCKED` bırakılmıştır**. Eğer TUR 3'te model, K5/K6'yı ihlal ederek
599,90'ı tek hedef olarak kullanırsa **bu indirim geçersizdir** ve `T-504`
derhal `CRITICAL`'a döner.

### Bu turun en kırılgan hükmü

**`G0 PASS`.** Kırılgan çünkü iki ayağının **ikisi de kanıtla çözülmüş
değildir**: biri *"maddi değil"* (C-252 açık), diğeri *"kurucu tarafından
kabul edildi"* (C-203 açık). Yani `G0 PASS`, **iki açık çelişkinin üzerinde
duran bir gate'tir**. Bunu gizlemiyorum: üç tetikleyici (R1/R2/R3) tam da bu
yüzden yazılmıştır ve G0 bu projede **geri alınabilir** bir gate olarak
işaretlenmiştir.

### Bu turun kör noktası

Bu tur **hiçbir yeni kanıt üretmemiştir.** Yaptığım şey, mevcut kanıtların
**statüsünü** güncellemektir. Eğer TUR 1.5'in kanıt tabanı sistematik olarak
hatalıysa (örneğin `mevzuat-ruhsat-uzmani`'nın erişemediği
`mevzuat.gov.tr`/`resmigazete.gov.tr` yerine kullandığı TADAB konsolide
metinleri güncel değilse), bu tur o hatayı **yakalayamaz** — sadece üzerine
statü yazar. Panzehir yine TUR 4'tür: `seytanin-avukati` bu belgeyi değil,
**altındaki kanıtları** hedef almalıdır.
