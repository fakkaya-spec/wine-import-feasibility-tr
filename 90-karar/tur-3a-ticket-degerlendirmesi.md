# TUR 3A — `T-946` / `T-913` DEĞERLENDİRMESİ

```yaml
belge:                  tur-3a-ticket-degerlendirmesi
yazan:                  yatirim-komitesi-baskani
tarih:                  2026-08-10
tur:                    TUR 3A
kapsam:                 "T-946 ve T-913'un ticket sisteminden degerlendirilmesi:
                         karar-kritik mi, ucuz kapanabilir mi, hangi tura ait"
karar_iceriyor_mu:      false      # YATIRIM karari icermez
esik_degeri_yazildi_mi: false
arastirma_yapildi_mi:   false      # CLAUDE.md §1.16
web_aramasi_yapildi_mi: false
ajan_cagrildi_mi:       false
yeni_kanit_uretildi_mi: false
karar_gunlugune_dokunuldu_mu: false
acilan_ticket:          [T-951, T-952, T-953, T-954]
yeni_kapi:              [P-3b-DATED, P-5]
```

> ## SINIR BEYANI
> Bu belgede `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` / `SCALE` kararlarının
> hiçbiri verilmemiştir ve verilemez. `90-karar/karar-gunlugu.md` dosyasına
> **DOKUNULMAMIŞTIR.** Hiçbir araştırma yapılmamış, hiçbir ajan
> çağrılmamış, hiçbir eşiğe değer yazılmamıştır.

---

# §1 — DEĞERLENDİRME ÇERÇEVESİ

Her iki ticket için aynı iki soru soruldu:

| Soru | Neden |
|---|---|
| **Karar-kritik mi?** | Kritik olmayan bir ticket'ı bu turda kapatmak, kritik olanın önüne geçmektir. |
| **Ucuz kapanabilir mi?** | *"Ucuz"* = masabaşı, dış temas gerektirmeyen, saatler mertebesinde. |

⚠ Ve **üçüncü, sık atlanan bir soru:**

> **Ucuz olmak, KAPATILABİLİR olmak demek değildir.**
> Bir iş ucuz olabilir ve yine de **başkan tarafından yapılamaz** —
> çünkü ya araştırmadır (`CLAUDE.md §1.16`), ya da başkan o konuda **taraf**
> hâline gelmiştir.

---

# §2 — `T-946` — `R5` DÜZELTMESİNİN BAĞIMSIZ DENETİMİ

```
target_agent : seytanin-avukati
impact       : HIGH
status       : OPEN  ->  OPEN   (DEGISMEDI)
tur atamasi  : TUR 4
```

## 2.1 Karar-kritik mi? — **EVET**

| Denetim sonucu | Etki |
|---|---|
| Düzeltme **doğru** | Tavanlar bugünkü seviyede kalır; `T-943`'ün `K1` maddesi kanal hata listesinin 1 numarası olur |
| Düzeltme **yanlış** | Tavanlar **%10,6 yükselir**; tekel/zincir karşılaştırması **tersine dönebilir**; `reverse-price-model.md`'nin tüm tabloları yeniden hesaplanır |
| **Kısmen** doğru | `d` bandının **bileşen bazında** ayrıştırılması gerekir |

Bu doğrudan **`G4`**'ü ilgilendirir.

## 2.2 Ama TUR 3B'yi bloke ediyor mu? — **HAYIR**

TUR 3B zaten **parametrik bir yüzey** üretecektir. `R5` tanımı o yüzeyin bir
**ekseni değil, taban tanımıdır**: denetim sonucu geldiğinde yüzey yeniden
ölçeklenir, yeniden kurulmaz. Yani `T-946` **TUR 3B'nin önkoşulu değildir.**

## 2.3 Ucuz kapanabilir mi? — **DENETİM UCUZ, KAPANIŞ DEĞİL**

Denetimin kendisi ~saatler, ~0 TL, tek kanıt kartı okunur. **Ama bu turda
kapatılamaz — iki bağımsız nedenle:**

| # | Neden | Dayanak |
|---|---|---|
| **1** | **Hedef ajan bu turda çalıştırılmıyor.** `seytanin-avukati` TUR 4 ajanıdır. | `CLAUDE.md §8` |
| **2** | **Başkan bu denetimi kendisi yapamaz.** (a) Başkan araştırma yapmaz, kanıt kartı yorumlamaz. (b) **Bağımsızlık:** `R5` düzeltmesini kabul eden taraf başkandır (`tur-25-konsolidasyon.md` §3.1). Başkanın kendi kabul hükmünü denetlemesi, `T-946`'nın var olma nedenini — *"denetlenen taraf denetleyen olamaz"* — **aynen ihlal ederdi.** | `CLAUDE.md §1.16`; `T-946` § "Neden `seytanin-avukati`" |

> ### HÜKÜM: `T-946` **`OPEN` kalır ve TUR 4'e aittir.**
> Bu bir *"kapatılamadı"* değil, **"doğru tura ait"** durumudur.
> `impact` düşürülmemiş, kapsam daraltılmamıştır.

## 2.4 TUR 3A'da yapılan tek şey — **KAPSAM AYRIŞTIRMASI**

`T-946`'nın **5 denetim sorusunun hepsi aynı ajanın işi değildir.**

| Soru | Kimin işi | Nerede |
|---|---|---|
| 1 — para.82 ithalatçıyı mı üreticiyi mi tarif ediyor | `seytanin-avukati` *(kartın yorumu)* | `T-946` |
| 2 — ürün grubu / ithal ürünü kapsıyor mu | `seytanin-avukati` | `T-946` |
| 4 — kararın tarihi / `ttl` | `seytanin-avukati` | `T-946` |
| 5a — `d`'nin **varlığı** kanıtlı mı | `seytanin-avukati` | `T-946` |
| **3 — fatura indirimi mi ayrı hizmet faturası mı** | ⚠ **`kanal-marj-uzmani`** | **`T-951` (YENİ)** |
| 5b — `d`'nin **bant seviyesi** | `kanal-marj-uzmani` | `T-604`, `T-856` *(açık)* |

**Neden Soru 3 ayrıldı:** `EV-2026-08-10-612` altı kalemi *"müşteriye ödenecek
bedeller"* olarak **sayar**; hangi **mekanizmayla** aktığını **söylemez.**
`seytanin-avukati` bu soruyu o kartı okuyarak cevaplarsa, **kartın söylemediği
bir şeyi kanıt diye sunmuş olur** — yani `T-946`'nın denetlemeye çalıştığı
hatanın aynısını yapar.

Ve Soru 3, `R5`'in **çift sayım** yapıp yapmadığını belirleyen sorudur:

```
(b) ayri hizmet faturasi  ->  L6 brut  ->  R5 DOGRU        [model bunu varsayiyor]
(a) fatura indirimi       ->  L6 zaten NET  ->  R5 CIFT SAYIYOR
```

> **`T-951` (HIGH, `kanal-marj-uzmani`)** — `T-946`'nın *"düzeltme yanlış
> olabilir"* ihtimalinin **tek somut mekanizmasıdır.**

---

# §3 — `T-913` — LCL KOTASYONLARININ TAZELİĞİ

```
target_agent : navlun-lojistik-uzmani
impact       : HIGH
status       : OPEN  ->  OPEN (ayak A)  +  CLOSED (ayak B)
```

## 3.1 Sorulan soru: **yenileme mi, zamanlama kararı mı?**

> ## CEVAP: **İKİSİ DE — ve ticket bunları birbirine karıştırıyordu.**

Bu ticket bugüne kadar **tek bir iş** gibi yazılmıştı. Değildir:

| Ayak | Soru | Sahibi | Durum |
|---|---|---|---|
| **A — PROTOKOL** *(yenileme)* | Kotasyon **dış iletişim gerektirmeden** yeniden çekilebilir mi? | **`navlun-lojistik-uzmani`** | **`OPEN`** |
| **B — ZAMANLAMA** *(karar)* | 2026-08-16 penceresi kaçarsa ne olur? | **`yatirim-komitesi-baskani`** | **`CLOSED` — bu turda** |

**Ayak A başkan tarafından kapatılamaz:** hem araştırmadır, hem de cevabı
*"evet, dış temas gerekiyor"* çıkarsa iş **`I-4` / `N-2` iznine** tabi hâle
gelir — yani başkanın tek başına veremeyeceği bir karara dönüşür. Emir
vermek, izin rejimini atlamak olurdu.

## 3.2 Ayak B — HÜKÜM: `P-3b-DATED` *(bağlayıcı)*

### Zemin: pencerenin kaçması bir ihtimal değil, **bugünkü planın sonucudur**

```
Bugun                                : 2026-08-10
10 LCL kotasyonu son gecerli gun     : 2026-08-16   (5 tam calisma gunu)
TUR 3B on kosulu (OQ-901 §A)         : YATIRIMCIDA — cevap tarihi UNKNOWN
```

TUR 3B, yatırımcı girdisi gelmeden başlayamaz (`tur-25-konsolidasyon.md` §6.2)
ve o girdinin geliş tarihi **bilinmemektedir.** Dolayısıyla *"modeli
2026-08-16'dan önce koştur"* **uygulanabilir bir çözüm değildir.** Bunu
yazmamak, kaçınılmaz olanı kaçınılabilirmiş gibi göstermek olurdu.

### Hüküm — beş kural

| # | Kural |
|---|---|
| **B-1** | **2026-08-17 00:00** itibarıyla `EV-2026-08-10-301, -302, -303, -305, -306, -307, -308, -309, -310, -311` ve türevleri (`-329`, `-330`) **otomatik `STALE`** sayılır. Ayrı bir karar/onay beklenmez. |
| **B-2** | O tarihten sonraki **her** koşuda lojistik bacağı **`ESTIMATE / LOW`** etiketlenir ve çıktıya **`STALE_LOGISTICS`** damgası basılır. **Sessizce bayat veriyle koşmak yasaktır.** |
| **B-3** | `STALE_LOGISTICS` damgalı çıktı **`G2-L`'yi geçemez** ve `DRAFT`'tan yukarı çıkamaz. |
| **B-4** | Damga **geri alınabilir**: Ayak A çözülüp kotasyonlar yenilenirse (yeni kartlar + `supersedes` + eskiler `SUPERSEDED`, `CLAUDE.md §4`) damga düşer. |
| **B-5** | Yenileme yapılırsa **iki ölçüm arasındaki fark ölçülür ve kaydedilir.** Bugün `senaryolar.yaml`'daki navlun duyarlılık bandı bir `ASSUMPTION`'dır; ikinci ölçüm ona **ilk kanıtlı dayanağı** verir. **Yenilemenin asıl getirisi budur — tazelik değil.** |

### Neden acil bir yenileme emri VERİLMİYOR

| Gerekçe | Kayıt |
|---|---|
| **Etki mertebesi en küçük uçta** | `MAX_CIF` üzerinde **±0,93 TL/şişe** (`tur-25-konsolidasyon.md` §5). Karşılaştırma: `R5` farkı **28,95 TL**, μ ekseni **108,56 TL**. |
| **Mesele büyüklük değil, meşruiyet** | Ve meşruiyet **damgayla** korunur (`B-2`), yenilemeyle değil. `seytanin-avukati` TUR 4'te bayat girdiyle koşulmuş bir modeli **haklı olarak** tümden reddedebilir — damga tam olarak bunu önler. |
| **Yenileme dış temas gerektirebilir** | O hâlde `N-2` iznine tabidir. |
| **Hedef ajan bu turda çalışmıyor** | `navlun-lojistik-uzmani` TUR 3A'da çağrılmadı. |

## 3.3 Bir kayıt düzeltmesi

`T-913`'ün kendi `claim` alanı **"11 LCL kotasyon karti"** ve
`EV-2026-08-10-301...-311` demektedir. `navlun-lojistik-uzmani` `T-802`'de
seti **10 kart** olarak saymış ve `-304`'ün bulunmadığını belirtmiştir
(`T-801`, `T-923`).

> `claim` alanı **DEĞİŞTİRİLMEMİŞTİR** (ticket geçmişi silinmez). Bağlayıcı
> sayım **10 karttır.** Bu bir başkan hükmü değil, **ajanın kendi
> düzeltmesinin kayda geçirilmesidir**; `T-801`/`T-923` açık kalır.

## 3.4 `I-8` / `OQ-912` üzerindeki etkisi

`investor-decisions-required.md` sürüm 1'de `I-8` *(TUR 3A/3B çalıştırma
tarihi)* bir **yatırımcı girdisi** olarak listelenmişti. **Yanlış masaydı** —
o bir **başkan zamanlama kararıdır** ve bu turda verilmiştir.

> **`I-8` yatırımcı listesinden ÇIKARILDI.** Karşılığı `P-3b-DATED`'dir.

---

# §4 — TUR 3A'DA AÇILAN TICKET'LAR

| ticket | hedef | impact | konu | nereden doğdu |
|---|---|---|---|---|
| **`T-951`** | `kanal-marj-uzmani` | **HIGH** | `d`/`f` **mekanizması**: fatura indirimi mi ayrı hizmet faturası mı — `R5` çift sayım riski | `T-946` Soru 3'ün ayrıştırılması |
| **`T-952`** | `finans-fizibilite` | MEDIUM | Brüt marj **üç katman tanımında yan yana** raporlansın → `D-01`(ii) yatırımcı listesinden düşer | Investor inputs sadeleştirmesi |
| **`T-953`** | `finans-fizibilite` | **HIGH** | `L5` kalemlerinin **`VARIABLE`/`FIXED`/`STEP`** sınıflandırması → `break_even_volume` tanımlı hâle gelir; `D-02`(ii) düşer | Investor inputs sadeleştirmesi |
| **`T-954`** | `finans-fizibilite` | **HIGH** | **`P-5`** — ertelenen 21 eşiğin bedeli: TUR 3B çıktısı **yüzey** olarak sunulur, post-output eşikler **damgalanır** | Ertelemenin meşruiyet şartı |

**Yeni kapılar:** `P-3b-DATED` *(`T-913`)* · `P-5` *(`T-954`)*

---

# §4B — İNDEKS DENETİMİNDE ÇIKAN İKİNCİ KAYIT HATASI

Ticket indeksi bu turda **dosya sistemiyle karşılaştırıldı**:

```
99-ops/tickets/T-*.md dosya sayisi : 113
indeks tablosundaki id sayisi      : 105
FARK                               :   8   ->  T-611...T-614, T-881...T-884
```

TUR 2.5'te indeks *"76 → 101"* olarak düzeltilmişti; **o düzeltme de
eksikmiş.** Sekiz ticket **hiç indekse girmemiş.** Sekizi de eklendi.

> **Bu bir ajan bulgusu reddi değil, ikinci bir başkan kayıt hatasının
> düzeltilmesidir.** Ve bir süreç tespiti içerir: `T-611`…`T-614` ile
> `T-881`…`T-884` **TUR 3A'da açılmıştır** — yani `kanal-marj-uzmani` ve
> `global-sourcing-kasifi` TUR 3A'da **çalışmıştır.** Bu oturum TUR 3A'nın
> tamamı değildir.

## 4B.1 — `T-951` bu düzeltmeden **doğrudan** etkilendi

`T-611`'in `claim` alanı, `T-951`'in çekirdek sorusunu **zaten cevaplanmış
gibi** kullanıyor:

> *"`f` ve `d` **HİZMET FATURASI** ile alınmaktadır
> (`EV-2026-08-10-610`, **`FACT`**)"* — yani **(b) senaryosu.**

**Ama `EV-2026-08-10-610`'un `claim` ve `value` alanlarında "hizmet faturası"
GEÇMİYOR.** Kartın kendi `notes`'u şöyle diyor:
*"BU KART BİR KALEM LİSTESİDİR, BİR TUTAR DEĞİLDİR."*

İfade **kartta değil, `snapshot`'ın içinde** duruyor. Ve aynı snapshot
**iki zıt cümle** taşıyor:

| İçerik | İşaret ettiği mekanizma |
|---|---|
| *"...bu bedellere ilişkin olarak belirlenen zamanlar için **hizmet faturası** düzenlendiğini belirtmiştir"* | **(b)** — ayrı hizmet faturası |
| *"...**indirim marketlerinin** ek bedel talep etmek yerine ürünün **net fiyatı üzerinden pazarlık** yapmayı tercih ettikleri..."* | **(a)** — net fiyat |

> ### Bu, `T-946`'nın **"KISMEN DOĞRU"** dalına işaret ediyor
> Mekanizma **kanala göre değişiyor olabilir.** Öyleyse `R5` zincir
> satırlarında doğru, indirim marketi satırlarında **çift sayıyor** olabilir
> — ve modeldeki **tek bir `d` katsayısı** bu ayrımı gizliyor.

**Başkan bu soruyu CEVAPLAMAMIŞTIR.** Yapılan tek şey `T-951`'in ajanı
**doğru satıra yönlendirmesi** ve dört somut iş kalemi eklenmesidir
(yeni kanıt kartı · kanal bazında ayrım · `f` ayrıca · `T-611`'in atıf
düzeltmesi). **Kart açılmadan `T-951` kapanmaz.**

## 4B.2 — `T-614` ertelenen `D-05`'i **güçlendiriyor**

`T-614` (`kanal-marj-uzmani` → `finans-fizibilite`) iki şey söylüyor:
(a) kanal alacağının matrahı `L6` değil **`L6×(1+v)`**'dir → `peak_cash`
**%20 eksik**; (b) kanal vadesinin **finansman maliyeti modelde SIFIRDIR**
(60→120 gün ≈ **−27,55 TL/şişe**, ve **tornadoda hiç yok**).

> Bu, `D-05` (sermaye tavanı) ve `D-13` (vade) eşiklerinin ertelenmesini
> **zayıflatmıyor, güçlendiriyor**: bugün bir sermaye tavanı yazmak, **hatalı
> hesaplanmış bir `peak_cash`** ile karşılaştırılacak bir sayı yazmak olurdu.
> **Önce sayı düzelir, sonra tavan konur.**

## 4B.3 — `T-884` **başkana açık** ve `N-2`'ye bağlı

`T-884` (`global-sourcing-kasifi` → **başkan**, HIGH): RFQ v2.2'nin
*cevapsızlık kuralı* bir **ticari eleme kuralıdır** ve onayı başkanındır.
Bugünkü doluluk oranıyla (`bottle_weight` **26/26 `UNKNOWN`**) kural
**kısa listenin tamamını** değerlendirme dışı bırakabilir.

> **Bu turda ONAYLANMADI.** İki nedenle: (1) bu oturumun kapsamı `T-946` /
> `T-913` ve yatırımcı listesidir; (2) kural, **RFQ gönderilmeden** hüküm
> doğurmaz ve RFQ **`N-2` (dış temas izni)** olmadan gönderilemez.
> **`T-884`, `N-2` verildiği gün başkanın ilk işidir.**

---

# §5 — DESEN GÜNCELLEMESİ *(TUR 4'e devir)*

`tur-25-konsolidasyon.md` §3.3'teki **DESEN** bu turda **iki yeni aday**
kazanmıştır:

> **DESEN:** Her katman sınırında, kalemin bir NİTELİĞİ (ödeyeni / katmanı /
> para birimi) belirsiz bırakıldığında, model o kalemi **sessizce atlar** ve
> tavan **yukarı** sapar — yani **projenin lehine.**

| Olay | Belirsiz nitelik | Yön | Ticket |
|---|---|---|---|
| `R5` hatası | kalemin **ödeyeni** | ↑ | `T-946` |
| `C-851` | kalemin **katmanı** | belirsiz | `T-945` |
| `C-852` | kalemin **para birimi** | ↑ | `T-852` |
| 13 maliyet kaleminin `0` alınması | tutarın `UNKNOWN` olması | ↑ *(13/13)* | çeşitli |
| ➕ **`d`/`f`'nin akış mekanizması** | kalemin **faturalanma biçimi** | **belirsiz — her iki yöne de açık** | **`T-951`** |
| ➕ **maliyet kaleminin sabit/değişken sınıfı** | kalemin **davranışı** | ↑ *(değişken sayılan sabit kalem break-even'ı düşürür)* | **`T-953`** |

> `seytanin-avukati` TUR 4'te bu **altı satırdan** başlamalıdır.

---

# §6 — DEĞİŞMEYENLER *(kayıt)*

| Kalem | Durum |
|---|---|
| Reddedilen ajan bulgusu | **0** |
| `impact` düşürülen ticket | **0** |
| Kapatılan ticket | **0** *(`T-913` Ayak B bir hüküm kaydıdır, ticket kapanışı değildir)* |
| Açık `CRITICAL` sayısı | **10** — değişmedi |
| `karar-gunlugu.md` | **dokunulmadı** |
| Yeni kanıt kartı | **0** |

---

## Bu kararı ne çürütür?

*(Bu belge bir yatırım kararı içermez. Aşağıdaki soru bu belgenin iki
hükmüne ilişkindir.)*

### Hüküm 1: *"`T-946` bu turda kapatılamaz ve TUR 4'e aittir."*

> ### En güçlü çürütücü: **`seytanin-avukati`'nın TUR 4'te de bu denetimi yapamayacağının ortaya çıkması.**

Eğer `EV-2026-08-10-612`'nin kaynağı (Rekabet Kurulu kararının tam metni)
elde değilse — yalnızca bir alıntı/özet varsa — `seytanin-avukati` **hiçbir
turda** Soru 1, 2 ve 4'ü cevaplayamaz. O durumda `T-946` bir *"denetim
bekliyor"* ticket'ı değil, **bir `UNKNOWN` ticket'ıdır** ve `R5` düzeltmesi
kalıcı olarak **tek bir doğrulanamamış yoruma** dayanır kalır.

**Nasıl ararız:** `T-946`'nın Soru 4'ü (`ttl` + tarih) bunu **ilk adımda**
gösterir. Kartın `snapshot_path` alanı boşsa, kırmızı bayrak oradadır.

### Hüküm 2: *"`T-913` bir yenileme değil, bir zamanlama meselesidir ve damga yeterlidir."*

> ### En güçlü çürütücü: **spot navlunun 6 günde anlamlı ölçüde oynaması.**

`±0,93 TL/şişe` mertebesi **bugünkü** kotasyonlardan türetilmiştir — yani
navlunun **oynaklığını** değil, **seviyesinin modele katkısını** ölçer.
Oynaklık hiç ölçülmemiştir. İki ölçüm arasında %30–50'lik bir fark çıkarsa,
`STALE_LOGISTICS` damgası *"küçük bir kalem eskidi"* demek olmaz;
**lojistik girdisinin bandının bilinmediği** anlamına gelir — ve o band
`senaryolar.yaml`'da bugün bir `ASSUMPTION`'dır.

**Nasıl ararız:** `T-913` Ayak A çözülüp ikinci ölçüm alındığında,
**`B-5` gereği fark zorunlu olarak kaydedilir.** Bu, bu belgedeki hükmü
sınayan tek gözlemdir ve **yenilemenin asıl gerekçesi de budur** — tazelik
değil, **oynaklığın ilk ölçümü.**

### Bu belgenin kör noktası

**Her iki ticket da "ucuz" olduğu için değerlendirildi — ama ucuzluk bir
öncelik ölçütü değildir.** Bu turda `T-947` (KDVK md.36, **CRITICAL**,
`gumruk-vergi-uzmani`) ve `T-917` (tek fiziksel mağaza turu,
`turkiye-pazar-kasifi`) **hiç ele alınmadı** — oysa `tur-25-konsolidasyon.md`
§6.1 ikisini de `T-946`/`T-913`'ün **önüne** koymuştu. `T-947` doğruysa bu
belgedeki her şey önemsizdir: tüm tavanlar **~%22,7 düşer.**
**Sıra yanlış olabilir ve bu kayda geçirilmiştir.**
