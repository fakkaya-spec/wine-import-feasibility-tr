# TICKET İNDEKSİ — TUR 3A

> Güncellendi: **2026-08-10, TUR 3A** (`yatirim-komitesi-baskani`).
> Kaynak: `99-ops/tickets/T-*.md` — **tek doğruluk kaynağı ticket dosyalarının
> kendisidir.** Bu indeks o dosyalardan türetilmiştir.
> Karar kayıtları: `90-karar/tur-2-konsolidasyon.md` → `tur-25-preflight.md`
> → `tur-25-konsolidasyon.md` → **`90-karar/tur-3a-ticket-degerlendirmesi.md`**
> Yatırımcı girdisi: **`90-karar/investor-decisions-required.md` (SÜRÜM 2)**

```
TOPLAM : 113 ticket        (dosya sayimi ile DOGRULANDI)
impact : CRITICAL 13 · HIGH 64 · MEDIUM 34 · LOW 1 · CONSTRAINT 1
status : OPEN 98 · ANSWERED 9 · RESOLVED 6
acik   : 107  (OPEN + ANSWERED) · acik CRITICAL: 10   (DEGISMEDI)
```

> **TUR 3A'da hiçbir ticket kapatılmadı, hiçbir `impact` düşürülmedi,
> hiçbir ajan bulgusu reddedilmedi.** Yapılan: iki ticket'ın **kapsamı
> ayrıştırıldı** (`T-946`, `T-913`), dört yeni ticket açıldı, iki yeni
> **kapı** yürürlüğe girdi (`P-3b-DATED`, `P-5`).

---

## ⚠ İKİNCİ KAYIT HATASI DÜZELTMESİ — **8 TICKET İNDEKSTE HİÇ YOKTU**

TUR 2.5'te indeks *"76 → 101"* olarak düzeltilmişti. **O düzeltme de eksikti.**
Dosya sistemi sayımı ile indeks tablosu bu turda karşılaştırıldı:

```
99-ops/tickets/T-*.md dosya sayisi : 113
indeks tablosundaki id sayisi      : 105   (TUR 3A'nin 4 yenisi dahil)
FARK                               :   8
```

**İndekste hiç görünmemiş 8 ticket:**

| ticket | açan | hedef | impact | Neden önemli |
|---|---|---|---|---|
| `T-611` | `kanal-marj-uzmani` | `gumruk-vergi-uzmani` | HIGH | `f` ve `d`'nin **KDV'si indirilebilir mi**; indirilemezse ekonomik maliyet **1,20 katı** |
| `T-612` | `kanal-marj-uzmani` | `gumruk-vergi-uzmani` | HIGH | `R1`'de HoReCa satırlarına **ürün KDV'si** uygulanıyor; menü fiyatı **hizmet KDV'si** olabilir |
| `T-613` | `kanal-marj-uzmani` | `finans-fizibilite` | HIGH | `d` tek oransal katsayı; oysa altı kalemin **en az üçü SABİT TUTARLI** → hacim riski modelden **silinmiş** |
| `T-614` | `kanal-marj-uzmani` | `finans-fizibilite` | HIGH | (a) alacak matrahı `L6` değil **`L6×(1+v)`** → `peak_cash` **%20 eksik**; (b) kanal vadesinin **finansman maliyeti modelde SIFIR** (60→120 gün ≈ **−27,55 TL/şişe**, tornadoda **hiç yok**) |
| `T-881` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | HIGH | RFQ v2.2 `M5` etiket ölçüleri teyidi |
| `T-882` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | HIGH | RFQ v2.2 `M2`/`M3`/`M4` ↔ `T-302`'nin 14 maddesi eşleşiyor mu |
| `T-883` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | HIGH | Menşe ispat taahhüdünün **kabul kriteri** (`T-162` hâlâ `UNKNOWN`) |
| **`T-884`** | `global-sourcing-kasifi` | **`yatirim-komitesi-baskani`** | HIGH | **RFQ cevapsızlık kuralı ONAYI başkanındır** — bugünkü doluluk oranıyla (`bottle_weight` **26/26 `UNKNOWN`**) kural **kısa listenin tamamını** eleyebilir |

> **Bu bir başkan kayıt hatasının ikinci kez düzeltilmesidir; hiçbir ajanın
> bulgusu değişmemiştir.** Sekizi de `TÜM TICKET'LAR` tablosuna eklendi.
>
> ⚠ **Ayrıca bir süreç tespiti:** `T-611`…`T-614` ve `T-881`…`T-884`
> **TUR 3A'da açılmıştır** — yani `kanal-marj-uzmani` ve
> `global-sourcing-kasifi` TUR 3A'da **çalışmıştır.** Önceki bölümdeki
> *"TUR 3A'da ele alınmayanlar"* listesi bu ajanları kapsamaz.

### ⚠ `T-951` bu düzeltmeden DOĞRUDAN etkilendi

`T-611`'in `claim` alanı, `T-951`'in çekirdek sorusunu **zaten cevaplanmış
gibi** kullanmaktadır: *"`f` ve `d` **hizmet faturası** ile alınmaktadır
(`EV-2026-08-10-610`, `FACT`)."*

**Ama `EV-2026-08-10-610`'un kendi `claim` ve `value` alanlarında "hizmet
faturası" GEÇMEZ.** Kart bir **kalem listesidir**; mekanizmayı taşımaz.
Mekanizma ifadesi kartın değil, **`snapshot`'ın** içindedir.

> Bu bir çelişki değil, bir **kayıt boşluğudur**: kaynak metinde var olan
> bir olgu, kanıt kartına **girmemiştir** — ve `T-611` onu kart yokmuş gibi
> `FACT` diye kullanmaktadır. `T-951` bu boşluğu kapatmak üzere
> **yeniden yönlendirilmiştir** (bkz. `T-951` § TUR 3A EK).

> ⚠ **Önceki indeks (TUR 2.5 pre-flight) "76 ticket" diyordu ve BU SAYIM
> EKSİKTİ.** `T-701`, `T-702`, `T-751`, `T-801`, `T-802`, `T-851`…`T-859`,
> `T-871`…`T-873` indekse hiç girmemişti. **Bu bir başkan kayıt hatasının
> düzeltilmesidir; hiçbir ajanın bulgusu değişmemiştir.**

---

## AÇIK `CRITICAL`: **10**

*(“açık” = `status` ∈ {`OPEN`, `ANSWERED`} — yani `RESOLVED`/`REJECTED` değil)*

| # | ticket | status | hedef | **Neyi bloke ediyor** |
|---|---|---|---|---|
| 1 | **`T-104`** | ANSWERED | `finans-fizibilite` | **G1, G4** — ÖTV Yİ-ÜFE ile kendiliğinden artar; modelde sabit sayı olamaz. **Birinci ayak (`T-921`) KAPANDI**; ikinci ayak (Yİ-ÜFE `ASSUMPTION` ekseni) **AÇIK** → tüm parasal çıktı `UPPER_BOUND` kalıyor |
| 2 | **`T-301`** | OPEN | `mevzuat-ruhsat-uzmani` | **G2-L, G4** — antrepo/gümrük zorunlu bekleme süresi. `MAX_CIF`'te `0` alınan 13 kalemden biri; `D-08` (stok gün eşiği) **alt sınırını bile bilinmez kılıyor** |
| 3 | **`T-304`** | OPEN | `yatirim-komitesi-baskani` | **G2-L** — hiçbir rotada doğrulanmış FCL navlunu yok (`C-311`). ⚠ **TUR 2.5 tespiti: ters model üzerindeki etkisi SIFIRDIR** → bloke ettiği şey **ileri model + FOB pazarlığıdır**. **Bir izin sorunudur, veri eksikliği değil** |
| 4 | **`T-466`** | OPEN | `finans-fizibilite` | **G2, G4** — gerçek EXW/FOB yok; `exw`/`fob` `null` kalmalı |
| 5 | **`T-601`** | OPEN | `mevzuat-ruhsat-uzmani` | **G4-K** — şarap 6585 m.7/3 anlamında *"tarım ve gıda ürünü"* mü? **Yasal vade tavanını** belirler → `D-13`, `peak_cash`, `C-601` |
| 6 | **`T-912`** | OPEN | `finans-fizibilite` | **G4 + her parasal çıktı** — `fx` `null`. **Hedefi `T-852` ile düzeltildi**; ikisi aynı boşluğun iki ucudur |
| 7 | **`T-851`** | OPEN | `yatirim-komitesi-baskani` | **G4 + TUR 3B + TUR 6** — `TARGET`/`ACCEPTABLE`/`WALK-AWAY` üretilemiyor. **`90-karar/investor-decisions-required.md` ile belgelendi**; kapanışı **yalnızca yatırımcı** yapabilir |
| 8 | **`T-852`** | OPEN | `yatirim-komitesi-baskani` | **`MAX_FOB`/`MAX_EXW` + ülke ayrıştırması** — `fx` bir **yatırımcı girdisidir**. Hedef düzeltmesi **kabul edildi** |
| 9 | **`T-942`** ➕ | OPEN | `finans-fizibilite` | **G4-T** — **YENİ.** Kanal bacağı (`R1`–`R5`) için **hiçbir otomatik doğrulama yok**; `R8` yalnız `R6`–`R7`'yi doğruluyor. `−28,95 TL/şişe`'lik `R5` hatası **2.700/2.700 satırdan temiz geçti** |
| 10 | **`T-947`** ➕ | OPEN | `gumruk-vergi-uzmani` | **G1 + ters modelin TÜM sayıları** — **YENİ.** KDVK md.36 CB kararı **üç turdur aranmadı**. Varsa tüm tavanlar **~%22,7 düşer** |

**+ `OQ-901` (CRITICAL, sahibi: YATIRIMCI)** — hiçbir ajan kapatamaz.
**TUR 3B + TUR 6 blokeri.** → `90-karar/investor-decisions-required.md`

> **CLAUDE.md §5:** `impact: CRITICAL` açık ticket varken finans modeli
> `APPROVED` olamaz. **`reverse-price-model.md`, `sweet-spot-analizi.md` ve
> `country-buying-ceilings.csv` `DRAFT`'tır ve öyle kalır.**

---

---

## TUR 3A'DA YAPILANLAR (2026-08-10)

### Kapsam ayrıştırmaları — **statü değişmedi**

| ticket | önce | sonra | ne yapıldı |
|---|---|---|---|
| **`T-946`** | `OPEN` (HIGH) | **`OPEN` (HIGH)** — `tur_atamasi: TUR 4` | **Kapatılamadı — iki bağımsız nedenle:** (1) `seytanin-avukati` bu turda çalıştırılmadı, (2) `R5` düzeltmesini **kabul eden taraf başkandır** → kendi hükmünü denetleyemez. **Bu bir "kapatılamadı" değil, "doğru tura ait" durumudur.** Denetim sorularının **5'inden 1'i** (fatura mekanizması) alan dışı olduğu için **`T-951`**'e ayrıldı |
| **`T-913`** | `OPEN` (HIGH) | **`OPEN` (Ayak A) + `CLOSED` (Ayak B)** | Ticket **iki ayağa bölündü**: **A — PROTOKOL** *(yeniden çekim dış temas gerektiriyor mu → `navlun-lojistik-uzmani`, açık)* · **B — ZAMANLAMA** *(başkan hükmü: **`P-3b-DATED`**, verildi)*. **Cevap: bu ikisi de — ve ticket bunları karıştırıyordu.** `claim` alanındaki "11 kart" sayımı **düzeltilmedi ama not düşüldü** (bağlayıcı sayım `T-802`'deki **10 karttır**) |

### TUR 3A'da açılan ticket'lar

| ticket | hedef | impact | konu |
|---|---|---|---|
| **`T-951`** | `kanal-marj-uzmani` | **HIGH** | `d`/`f` **mekanizması**: fatura indirimi mi ayrı hizmet faturası mı? **(a) ise `R5` ÇİFT SAYIM yapıyor.** `T-946` Soru 3'ten ayrıldı |
| **`T-952`** | `finans-fizibilite` | MEDIUM | Brüt marj **üç katman tanımında yan yana** raporlansın (`L5→L6` / `L5→L7_eff` / `L5→L8`) → `D-01`(ii) yatırımcı listesinden düşer |
| **`T-953`** | `finans-fizibilite` | **HIGH** | `L5` kalemleri **`VARIABLE`/`FIXED`/`STEP`** sınıflandırılsın → `break_even_volume` **tanımlı** hâle gelir; `D-02`(ii) düşer |
| **`T-954`** | `finans-fizibilite` | **HIGH** | **`P-5`** — TUR 3B çıktısı tek "baz senaryo" olarak sunulamaz; **yüzey** olarak sunulur, post-output eşikler **`POST_OUTPUT_THRESHOLD`** damgalanır |

### TUR 3A'da yürürlüğe giren kapılar

| Kapı | İçerik |
|---|---|
| **`P-3b-DATED`** | **2026-08-17 00:00**'dan sonra 10 LCL kartı **otomatik `STALE`**; lojistik bacağı `ESTIMATE/LOW` + çıktıda **`STALE_LOGISTICS`** damgası; damgalı çıktı **`G2-L`'yi geçemez**; yenilenirse damga düşer ve **iki ölçüm farkı zorunlu kaydedilir** (`T-913`) |
| **`P-5`** | Ertelenen 21 eşiğin bedeli: çıktı **yüzeydir**, nokta seçimi `INVESTOR_DECISION` olarak **tarihlenir**, çıktıdan sonra yazılan eşik **damgalanır** ve `seytanin-avukati`'ya `IR-4` saldırı vektörü olarak verilir (`T-954`) |

### `T-851` / `T-852` / `OQ-901` — kapsam daraltması *(statü değişmedi)*

`90-karar/investor-decisions-required.md` **sürüm 2**'ye geçmiştir:

```
ONCE  : 16 esik + 8 girdi = 24 kalem
SONRA : MUST DECIDE NOW = 3   (N-1 fx · N-2 dis temas izni · N-3 L8 alt katmani)
        CAN DECIDE LATER = 21
        YATIRIMCI LISTESINDEN CIKARILAN = 3  ->  T-952, T-953, T-944
```

> **`MUST DECIDE NOW` listesinde tek bir EŞİK DEĞERİ yoktur:**
> biri bir **kayıt**, biri bir **izin**, biri bir **netleştirme**.
> `T-851`, `T-852` ve `OQ-901` **`OPEN` kalır** — kapanışlarını yalnızca
> yatırımcı yapabilir. Değişen tek şey **kapanış koşulunun küçülmesidir.**
>
> `I-8` *(TUR 3A/3B çalıştırma tarihi)* yatırımcı listesinden **çıkarıldı** —
> o bir başkan zamanlama kararıydı ve `P-3b-DATED` olarak verilmiştir.

---

## TUR 2.5 KAPANIŞINDA YAPILAN STATÜ DEĞİŞİKLİKLERİ (2026-08-10)

| ticket | önce | **sonra** | gerekçe |
|---|---|---|---|
| **`T-921`** | ANSWERED | **`RESOLVED`** | 5 kabul kriterinin 5'i karşılandı. **Başkan kodu okudu ve testi kendi koşturdu** (10/10). ⚠ **`P-1` kapısı yürürlükte kalır** (blocker → **regression guard**). Bayraksız ÖTV değeri basılırsa **otomatik yeniden açılır** |
| **`T-751`** | ANSWERED | **`RESOLVED`** | `TV-1`…`TV-10` **10/10** *(başkan koşturdu)*; `R8` round-trip **2.700/2.700**. ⚠ **Üç kapsam sınırı kaydedildi:** (a) spesifikasyon değişirse otomatik yeniden açılır (`T-941`), (b) `R8` yalnız **vergi** bacağını doğrular (`T-942`), (c) doğrulanan **matrahın SIRASIDIR, matrahın kendisi değil** (`T-947`) |

**Diğer 8 açık CRITICAL: statü DEĞİŞMEDİ, impact DÜŞÜRÜLMEDİ.**

## TUR 2.5 KAPANIŞINDA AÇILAN TICKET'LAR

| ticket | hedef | impact | konu |
|---|---|---|---|
| **`T-941`** | `gumruk-vergi-uzmani` | HIGH | `ters-model-vergi-bacagi.md` §3 `R5` başlığı **yanlış girdi katmanını** gösteriyor (`L6 → L5_max`; doğrusu `L7_eff`). Belgedeki **formülsüz tek adım** ve **tek hata çıkan adım** aynı adımdır |
| **`T-942`** | `finans-fizibilite` | **CRITICAL** | Kanal bacağı için **`R8-K` round-trip assertion'ı yok**. Zincirin 8 adımından yalnız 2'si korunuyor; tornadonun en büyük 4 ekseninin 3'ü korunmayan bacakta |
| **`T-943`** | `kanal-marj-uzmani` | HIGH | Kanal bacağı için **"en muhtemel hatalar" listesi (`H1`–`H6`'nın karşılığı) hiç yazılmamış**. 7 adaydan 3'ü bu turda **fiilen gözlendi** |
| **`T-944`** | `finans-fizibilite` | HIGH | `μ` (ithalatçı katkı payı) matrahı **`L6` alınmış, gerekçelendirilmemiş** ve **μ=0 olduğu için hiç test edilmemiş**. `T-851`'in yatırımcı cevabı bunsuz **yorumlanamaz** |
| **`T-945`** | `gumruk-vergi-uzmani` | MEDIUM | `C-851` çözümünün bağlayıcı okuma kuralı (**`L3-K`**) `matrah-sirasi.md` ve `vergi.yaml`'a yazılmalı (CLAUDE.md §1.8) |
| **`T-946`** | `seytanin-avukati` | HIGH | **`R5` düzeltmesinin bağımsız denetimi** — `EV-2026-08-10-612` yorumu (`d` kimin maliyeti). Ajan bunu **kendisi talep etti**. Ayrıca **DESEN denetimi** |
| **`T-947`** | `gumruk-vergi-uzmani` | **CRITICAL** | **KDVK md.36 CB kararı taraması** + gözetim tebliği yeniden taraması. **TUR 3A'nın birinci işi** |
| **`T-948`** | `finans-fizibilite` | MEDIUM | `P-2` tam tablosu (5 basamak × 3 tarih × 4 ÖTV noktası) **üretilmedi**; CSV'de `λ` ekseni **satır düzeyinde görünmüyor** |

## TUR 2.5 KAPANIŞINDA ÇÖZÜLEN ÇELİŞKİLER

| conflict_id | Durum | Takip |
|---|---|---|
| **`C-851`** (`L3` katman tanımı) | **`RESOLVED — TANIM`** — bağlayıcı okuma kuralı `L3-K` | `T-945` |
| **`C-852`** (*"fx olmadan `CIF_TRY`'ye kadar"*) | **`RESOLVED — TANIM (NİTELEME)`** — **başkanın kendi hükmünün düzeltilmesi** | `T-852` (veri eksikliği) |

---

## ⚠ KAYIT HİJYENİ — CEVAPLANDIĞI RAPORLANAN AMA TICKET DOSYASINA İŞLENMEYENLER

`finans-fizibilite` TUR 2.5 raporunda (`§7.1`) şu ticket'ları `ANSWERED`
olarak bildirmiştir, ancak **ticket dosyalarının `status` alanı hâlâ `OPEN`**:

| ticket | dosyada | raporda | Ne yapılmalı |
|---|---|---|---|
| `T-922` | `OPEN` | `ANSWERED` | Ajan `status` alanını **kendi ticket dosyasında** güncellemelidir |
| `T-702` | `OPEN` | `ANSWERED` | aynı |
| `T-153` | `OPEN` | `ANSWERED` *(`T-921` kapsadı)* | aynı — `T-921` `RESOLVED` olduğuna göre bu da kapanmalıdır |

> **Bu bir bulgu reddi değil, bir kayıt tutarsızlığıdır.** Başkan bu üçünü
> **kendi başına `ANSWERED` yapmaz** — statü değişikliğini hedef ajan
> kendi dosyasında yazar (`T-751`/`T-921`'de yapıldığı gibi).
> `T-153`, `T-921`'in `RESOLVED` olmasıyla fiilen kapanmıştır; ajanın
> kaydetmesi beklenmektedir.

---

## TÜM TICKET'LAR

*(impact sırasına, sonra id'ye göre. `claim` kısaltılmıştır — tam metin ticket dosyasındadır.)*

| ticket_id | açan | hedef | impact | status | claim (kısa) |
|---|---|---|---|---|---|
| `T-104` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **CRITICAL** | ANSWERED | ÖTV maktu tutarı Yİ-ÜFE ile 6 ayda bir kendiliğinden artar; modelde sabit sayı olamaz |
| `T-201` | `mevzuat-ruhsat-uzmani` | `yatirim-komitesi-baskani` | **CRITICAL** | RESOLVED | 4250 s.K. m.1/3 — 1.000.000 lt/yıl eşiği ve "yerinde teslim" şartı |
| `T-301` | `navlun-lojistik-uzmani` | `mevzuat-ruhsat-uzmani` | **CRITICAL** | OPEN | Ruhsat/analiz/bandrol nedeniyle gümrükte + antrepoda bekleme süresi |
| `T-304` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | **CRITICAL** | OPEN | Hiçbir rota için doğrulanmış (FCL) navlun yok — `C-311` |
| `T-466` | `global-sourcing-kasifi` | `finans-fizibilite` | **CRITICAL** | OPEN | Tek yayınlanmış şişe fiyatı modele giremez; `exw`/`fob` `null` kalmalı |
| `T-601` | `kanal-marj-uzmani` | `mevzuat-ruhsat-uzmani` | **CRITICAL** | OPEN | Şişelenmiş şarap 6585 m.7/3 anlamında "tarım ve gıda ürünü" mü? |
| `T-751` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **CRITICAL** | **RESOLVED** | Ters modelin vergi bacağı spesifikasyonu + 10 birim test vektörü |
| `T-851` | `finans-fizibilite` | `yatirim-komitesi-baskani` | **CRITICAL** | OPEN | `TARGET`/`ACCEPTABLE`/`WALK-AWAY` üretilemez — `OQ-901` açık |
| `T-852` | `finans-fizibilite` | `yatirim-komitesi-baskani` | **CRITICAL** | OPEN | `fx` bir **yatırımcı girdisidir**; `MAX_FOB`/`MAX_EXW`'yi tek adımda açar |
| `T-912` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **CRITICAL** | OPEN | `makro.yaml → fx` `null` — her parasal çıktı `UNKNOWN` |
| `T-921` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **CRITICAL** | **RESOLVED** | Engine `otv_maktu_zaman_serisi`'ni okumuyordu; ufuk denetimi eklendi |
| `T-942` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **CRITICAL** | OPEN | Kanal bacağı (`R1`–`R5`) için otomatik doğrulama yok — `R8-K` gerekli |
| `T-947` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **CRITICAL** | OPEN | KDVK md.36 CB kararı aranmadı — varsa tüm tavanlar ~%22,7 düşer |
| `T-101` | `gumruk-vergi-uzmani` | `navlun-lojistik-uzmani` | HIGH | OPEN | Antrepodan kısmi (parti parti) serbest dolaşıma giriş mümkün mü |
| `T-102` | `gumruk-vergi-uzmani` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | Alkollü içki ithalat denetimi tebliği — TAREKS/kontrol belgesi |
| `T-103` | `gumruk-vergi-uzmani` | `global-sourcing-kasifi` | HIGH | OPEN | 9 tedarik ülkesinin hiçbiri şarapta %0 gümrük vergili değil |
| `T-152` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | HIGH | OPEN | KDVK md.39/1 — vergilendirme dönemi üçer aylık mı birer aylık mı |
| `T-161` | `gumruk-vergi-uzmani` | `global-sourcing-kasifi` | HIGH | OPEN | AB/Şili %50 gümrük vergisi **KOŞULLUDUR** — koşul tedarikçiye bağlı |
| `T-163` | `gumruk-vergi-uzmani` | `navlun-lojistik-uzmani` | HIGH | OPEN | BİLGE menşe **ve çıkış ülkesi** kontrolü — doğrudan nakliyat kuralı |
| `T-202` | `mevzuat-ruhsat-uzmani` | `yatirim-komitesi-baskani` | HIGH | OPEN | Dağıtım yetki belgesi işlem süresi mevzuatta **TANIMSIZ** |
| `T-204` | `mevzuat-ruhsat-uzmani` | `navlun-lojistik-uzmani` | HIGH | OPEN | Bandrol **antrepoda** şişe başına uygulanır — operasyon süresi/maliyeti |
| `T-302` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | HIGH | OPEN | RFQ'ya "case & pallet spec sheet" zorunlu maddesi |
| `T-311` | `navlun-lojistik-uzmani` | `finans-fizibilite` | HIGH | OPEN | Lojistik maliyeti **üç para birimindedir** (USD + EUR + TRY) |
| `T-312` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | HIGH | OPEN | İtalya rotası **tamamen `UNKNOWN`**; menşe local charge 8/9 ülkede yok |
| `T-314` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | HIGH | OPEN | Antrepo içi operasyon + cam kırılma oranı iki turdur `UNKNOWN` |
| `T-401` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | HIGH | ANSWERED | 9 menşe için tercihli tarife rejimi eşlemesi |
| `T-402` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | HIGH | OPEN | 20DV/40HC konteynere kaç şişe + transit süreleri |
| `T-403` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | Türkçe arka etiket menşede mi Türkiye'de mi uygulanır |
| `T-404` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | HIGH | OPEN | Peşin ↔ vadeli ödeme seçiminin KKDF etkisi |
| `T-461` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | HIGH | OPEN | Paletsiz (slipsheet) 14.112 şişe iddiası ↔ paletli yükleme |
| `T-462` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | HIGH | ANSWERED | Yeni menşeler (Moldova / Yeni Zelanda) tarife durumu |
| `T-464` | `global-sourcing-kasifi` | `turkiye-pazar-kasifi` | HIGH | ANSWERED | 7 MODEL A markasının TR ithalatçısı var mı — **bulunamadı ≠ yok** |
| `T-467` | `global-sourcing-kasifi` | `yatirim-komitesi-baskani` | HIGH | OPEN | **RFQ gönderimi DIŞ İLETİŞİM izni gerektirir** — `G2`'nin tek anahtarı |
| `T-501` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | Fiyat Etiketi Yönetmeliği — etikette KDV dahil zorunluluğu |
| `T-504` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | HIGH | OPEN | **`OQ-001` promosyon ayağı** — `G3`'ün açılmasının ön koşulu |
| `T-505` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | TADAB dağıtım/ithalat uygunluk belgesi sahipleri listesi |
| `T-506` | `turkiye-pazar-kasifi` | `kanal-marj-uzmani` | HIGH | ANSWERED | Metro mağaza fiyatı ↔ Metro sevkiyat/HoReCa fiyatı farkı |
| `T-551` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | HIGH | RESOLVED | Metro etiketinde KDV çiftli gösterim — `C-551` |
| `T-563` | `turkiye-pazar-kasifi` | `kanal-marj-uzmani` | HIGH | OPEN | 4 ithalatçı grubu ismen tespit edildi — kanal yapısı |
| `T-602` | `kanal-marj-uzmani` | `finans-fizibilite` | HIGH | OPEN | `kanal.yaml` alanları **tek sayı değil SENARYO** olarak kullanılmalı |
| `T-603` | `kanal-marj-uzmani` | `turkiye-pazar-kasifi` | HIGH | OPEN | `L8_CHAIN_RETAIL` `UNKNOWN` iken `L7`/`L6` sayısal kurulamaz |
| `T-604` | `kanal-marj-uzmani` | `yatirim-komitesi-baskani` | HIGH | OPEN | Kanal ticari koşullarının **tutarları ticari sırdır** — `d`, `f`, distribütör marjı |
| `T-701` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | HIGH | OPEN | Hedef merdivenin hangi **`L8` alt katmanı** olduğu tanımsız |
| `T-702` | `turkiye-pazar-kasifi` | `finans-fizibilite` | HIGH | OPEN | `TARGET_SHELF_PRICE` ↔ `OBSERVED_BENCHMARK` **ayrı nesnelerdir** *(rapora göre `ANSWERED` — dosya güncellenmeli)* |
| `T-802` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | HIGH | OPEN | 10 LCL kotasyon kartı 2026-08-16'da `STALE` — **`P-3b`** |
| `T-854` | `finans-fizibilite` | `navlun-lojistik-uzmani` | HIGH | OPEN | TR-içi TRY bacağının **rota bağımsızlığı** doğrulanmalı (9 ülkeye uygulandı) |
| `T-856` | `finans-fizibilite` | `kanal-marj-uzmani` | HIGH | OPEN | `d` tekel/HoReCa'da `UNKNOWN → 0`; **tekel tavanı %11,4 yapay yüksek** |
| `T-857` | `finans-fizibilite` | `yatirim-komitesi-baskani` | HIGH | OPEN | En dayanıklı basamak (999) **mandanın dışında** → `D-15` |
| `T-858` | `finans-fizibilite` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | (a) ruhsat 20.000 lt kademesi ölçek eğrisini kesiyor (b) bandrol 2027'de yürürlükte olmayacak |
| `T-859` | `finans-fizibilite` | `turkiye-pazar-kasifi` | HIGH | OPEN | Hedefin hangi `L8` alt katmanı olduğu `UNKNOWN` → çıktının **anlamı** belirsiz |
| `T-871` | `global-sourcing-kasifi` | `yatirim-komitesi-baskani` | HIGH | OPEN | **RFQ pazarlık çapası hangi basamak ve hangi kanal?** → **`D-14` + `D-03`** |
| `T-901` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | HIGH | ANSWERED | `C-101` çözümünün dayandığı +%16,09 Yİ-ÜFE bağı |
| `T-902` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | HIGH | ANSWERED | `tedarikci.yaml` `L1`/FOB katman etiketi kanıtlanmamış |
| `T-903` | `yatirim-komitesi-baskani` | `turkiye-pazar-kasifi` | HIGH | RESOLVED | `pazar.yaml` model girdisi kayıt düzeltmesi |
| `T-911` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | HIGH | OPEN | İthalatta **gümrük kuru mu piyasa kuru mu** — `I-1`'in ikinci ayağı |
| `T-913` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | HIGH | OPEN | LCL kotasyonları **masabaşında yenilenebilir mi** — `P-3b` |
| `T-914` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | HIGH | OPEN | Şili × Barcelona aktarması `SIL` rejimini bozar mı — **+24 TL/şişe** |
| `T-915` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | HIGH | OPEN | Fransız adaylarının **limanı eşleşmiyor** |
| `T-916` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | HIGH | OPEN | İtalya'da **yanlış kıyı** — Tirren ↔ Veneto; DFDS Trieste değerlendirilmedi |
| `T-917` | `yatirim-komitesi-baskani` | `turkiye-pazar-kasifi` | HIGH | OPEN | **TEK FİZİKSEL GÖZLEM PAKETİ** — bir mağaza turu 5 açık kaydı birden kapatır |
| `T-922` | `yatirim-komitesi-baskani` | `finans-fizibilite` | HIGH | OPEN | TARGET merdiveni + `L1`–`L7` kuralları *(rapora göre `ANSWERED` — dosya güncellenmeli)* |
| `T-923` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | HIGH | OPEN | Kayıt düzeltmesi: "11 LCL kartı" → **10** |
| `T-941` ➕ | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | HIGH | OPEN | `R5` başlığı yanlış girdi katmanını gösteriyor (`L6` → doğrusu `L7_eff`) |
| `T-943` ➕ | `yatirim-komitesi-baskani` | `kanal-marj-uzmani` | HIGH | OPEN | Kanal bacağı için **"en muhtemel hatalar" listesi hiç yazılmamış** |
| `T-944` ➕ | `yatirim-komitesi-baskani` | `finans-fizibilite` | HIGH | OPEN | `μ`'nün matrahı (`L6`?) **tanımsız ve hiç test edilmemiş** |
| `T-946` | `yatirim-komitesi-baskani` | `seytanin-avukati` | HIGH | OPEN | `R5` düzeltmesinin **bağımsız denetimi** + **DESEN denetimi** — **TUR 4** |
| `T-951` ➕ | `yatirim-komitesi-baskani` | `kanal-marj-uzmani` | HIGH | OPEN | `d`/`f` **mekanizması**: fatura indirimi mi ayrı hizmet faturası mı — `R5` çift sayım riski |
| `T-953` ➕ | `yatirim-komitesi-baskani` | `finans-fizibilite` | HIGH | OPEN | `L5` kalemlerinin `VARIABLE`/`FIXED`/`STEP` sınıflandırması — `break_even_volume` bunsuz **tanımsız** |
| `T-954` ➕ | `yatirim-komitesi-baskani` | `finans-fizibilite` | HIGH | OPEN | **`P-5`** — TUR 3B çıktısı **yüzey** olarak sunulur; post-output eşikler damgalanır |
| `T-105` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | KKDF **matrahının** tanımı `UNKNOWN` |
| `T-151` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | İthalat KDV'sinin indirilebilirliği T1 tam metinle doğrulanmalı → **`T-947`** |
| `T-153` | `gumruk-vergi-uzmani` | `finans-fizibilite` | MEDIUM | OPEN | `matrah_sirasi.py:217` yalnız `is None` denetliyor *(`T-921` kapsadı — dosya güncellenmeli)* |
| `T-162` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Menşe ispat belgelerinin iki usul detayı |
| `T-203` | `mevzuat-ruhsat-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | ANSWERED | Bandrol ve TADAB bedelleri hangi vergi matrahına girer |
| `T-206` | `mevzuat-ruhsat-uzmani` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | Zorunlu laboratuvar analizi parametreleri |
| `T-303` | `navlun-lojistik-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Navlun/sigortanın gümrük kıymetine giriş kuralları |
| `T-305` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | MEDIUM | OPEN | Incoterm seçimi (EXW/FOB ↔ CIF) |
| `T-313` | `navlun-lojistik-uzmani` | `navlun-lojistik-uzmani` | MEDIUM | OPEN | Terminal ardiye tarifeleri ve free time |
| `T-405` | `global-sourcing-kasifi` | `turkiye-pazar-kasifi` | MEDIUM | OPEN | Benchmark markaları üretici markası mı private label mı |
| `T-406` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Dökme şarap (2204.29) ithalatı pratikte yok — neden |
| `T-463` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Tek doğrulanan ödeme şartı **tamamen sevkiyat öncesi peşin** |
| `T-465` | `global-sourcing-kasifi` | `kanal-marj-uzmani` | MEDIUM | OPEN | MODEL A adaylarının münhasırlık hacim taahhüdü |
| `T-468` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | Menşeler üç ayrı hukuki gruba dağılıyor |
| `T-502` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | Alkollü içkinin internetten satış yasağı — online fiyat gözlemi |
| `T-503` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | Reklam/kampanya yasağı — fiyat gözleminin sınırı |
| `T-561` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | MEDIUM | OPEN | `C-501` — stokta olmayan havuzun tamamı elenmeli mi |
| `T-562` | `turkiye-pazar-kasifi` | `global-sourcing-kasifi` | MEDIUM | OPEN | TUR 1 kısa listesindeki 11 tedarikçinin hiçbiri TR'de bulunamadı |
| `T-564` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | 4 ithalatçı üzerinden TADAB liste doğrulaması |
| `T-565` | `turkiye-pazar-kasifi` | `global-sourcing-kasifi` | MEDIUM | OPEN | Cantina Danese kendi markasıyla TR'de mi |
| `T-605` | `kanal-marj-uzmani` | `global-sourcing-kasifi` | MEDIUM | OPEN | RFQ 5.6 (üretici katkısı) ↔ kanal listeleme bedeli aynı şey mi |
| `T-611` ⚠ | `kanal-marj-uzmani` | `gumruk-vergi-uzmani` | HIGH | OPEN | `f`/`d`'nin KDV'si indirilebilir mi — indirilemezse ekonomik maliyet **1,20 katı** *(indekse ilk kez girdi)* |
| `T-612` ⚠ | `kanal-marj-uzmani` | `gumruk-vergi-uzmani` | HIGH | OPEN | `R1`'de HoReCa'ya **ürün KDV'si** uygulanıyor; menü fiyatı **hizmet KDV'si** olabilir *(indekse ilk kez girdi)* |
| `T-613` ⚠ | `kanal-marj-uzmani` | `finans-fizibilite` | HIGH | OPEN | `d` tek oransal katsayı; altı kalemin **en az üçü SABİT** → hacim riski silinmiş *(indekse ilk kez girdi)* |
| `T-614` ⚠ | `kanal-marj-uzmani` | `finans-fizibilite` | HIGH | OPEN | Alacak matrahı `L6×(1+v)` olmalı (`peak_cash` %20 eksik) + **vade finansman maliyeti SIFIR** (≈ −27,55 TL/şişe) *(indekse ilk kez girdi)* |
| `T-881` ⚠ | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | RFQ v2.2 `M5` etiket ölçüleri teyidi *(indekse ilk kez girdi)* |
| `T-882` ⚠ | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | HIGH | OPEN | RFQ v2.2 `M2`/`M3`/`M4` ↔ `T-302`'nin 14 maddesi *(indekse ilk kez girdi)* |
| `T-883` ⚠ | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | HIGH | OPEN | Menşe taahhüdünün **kabul kriteri** — `T-162` `UNKNOWN` *(indekse ilk kez girdi)* |
| `T-884` ⚠ | `global-sourcing-kasifi` | `yatirim-komitesi-baskani` | HIGH | OPEN | **RFQ cevapsızlık kuralı onayı başkanındır** — kısa listenin tamamını eleyebilir *(indekse ilk kez girdi)* |
| `T-853` | `finans-fizibilite` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Moldova ülke listesinde **yok** → **DÜ FALLBACK**; sonuç tesadüfen doğru |
| `T-855` | `finans-fizibilite` | `navlun-lojistik-uzmani` | MEDIUM | OPEN | `V10K` (10.000 şişe) için lojistik satırı yok → senaryo çalıştırılamadı |
| `T-872` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Menşe ispat belgesi reddedilirse tarife %50 → %70 |
| `T-873` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | MEDIUM | OPEN | Purcari (Moldova) — karayolu/liman rotası |
| `T-904` | `yatirim-komitesi-baskani` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | `ruhsat.yaml`'da hiçbir maliyet kaleminde **`katman` alanı yok** |
| `T-905` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | MEDIUM | OPEN | `EV-2026-08-09-310` tier düzeltmesi |
| `T-906` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | MEDIUM | ANSWERED | `vergi.yaml` 750 ml hijyeni — `ASSUMPTION`'a düzeltildi |
| `T-918` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | MEDIUM | OPEN | `C-401`/`C-402`/`C-403` statü kaydı düzeltmesi |
| `T-924` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | MEDIUM | OPEN | 750 ml **üç dosyada üç farklı statü** |
| `T-925` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | MEDIUM | OPEN | `urun.yaml → hacim_ml` `evidence_id` eksik |
| `T-945` ➕ | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | `L3-K` kuralı `matrah-sirasi.md`'ye yazılmalı (`C-851` çözümü) |
| `T-948` | `yatirim-komitesi-baskani` | `finans-fizibilite` | MEDIUM | OPEN | `P-2` tam tablosu + CSV'ye `λ` sütunları |
| `T-952` ➕ | `yatirim-komitesi-baskani` | `finans-fizibilite` | MEDIUM | OPEN | Brüt marj **üç katman tanımında yan yana** raporlansın → `D-01`(ii) yatırımcı listesinden düşer |
| `T-801` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | LOW | OPEN | LCL kanıt seti 11 değil **10** karttır |
| `T-205` | `mevzuat-ruhsat-uzmani` | `kanal-marj-uzmani` | CONSTRAINT | RESOLVED | 7584 s.K. m.2 görsel yasağı — `ACCEPTED BUSINESS CONSTRAINT` |

---

## HEDEF AJANA GÖRE AÇIK YÜK

*(“açık” = `status` ∈ {`OPEN`, `ANSWERED`}. Toplam açık: **107**, açık CRITICAL: **10**.)*

| Hedef ajan | Açık CRITICAL | Toplam açık | TUR 3A değişimi |
|---|---|---|---|
| **`gumruk-vergi-uzmani`** | **1** *(`T-947`)* | **23** | **+3** *(`T-611`, `T-612`, `T-883` — indekse ilk kez girdi)* |
| **`finans-fizibilite`** | **4** *(`T-104`, `T-466`, `T-912`, `T-942`)* | **16** | **+5** *(`T-952`, `T-953`, `T-954`; `T-613`, `T-614` indekse ilk kez girdi)* |
| **`navlun-lojistik-uzmani`** | 0 | 16 | **+1** *(`T-882`)* |
| **`yatirim-komitesi-baskani`** | **3** *(`T-304`, `T-851`, `T-852`)* | 15 | **+1** *(`T-884` — **RFQ eleme kuralı onayı**)* |
| **`mevzuat-ruhsat-uzmani`** | **2** *(`T-301`, `T-601`)* | 14 | **+1** *(`T-881`)* |
| `global-sourcing-kasifi` | 0 | 11 | — |
| **`kanal-marj-uzmani`** | 0 | **6** | **+1** *(`T-951`)* |
| `turkiye-pazar-kasifi` | 0 | 5 | — |
| `seytanin-avukati` | 0 | 1 | — *(`T-946` — **TUR 4**)* |

> **Başkana yönelik 3 açık `CRITICAL`'ın 3'ü de bir ARAŞTIRMA değil, bir
> KARAR veya İZİN beklemektedir** (`T-304` → dış temas izni; `T-851` →
> yatırımcı eşikleri; `T-852` → `fx` kaydı).
> Bu üçü `90-karar/investor-decisions-required.md`'ye taşınmıştır ve **sürüm
> 2'de sırasıyla `N-2`, `CAN DECIDE LATER` ve `N-1`'e karşılık gelir** —
> yani üçünden **ikisi hâlâ `MUST DECIDE NOW`**'dadır.

> ⚠ **`finans-fizibilite` TUR 3A'da en çok yük alan ajandır (+3).** Bu bir
> tesadüf değil: yatırımcı listesinden çıkarılan üç kalemin (`D-01`(ii),
> `D-02`(ii), `D-03`(i)) **üçü de bir modelleme tanımıydı** ve tanımların
> sahibi bu ajandır. **Yatırımcının listesinin kısalması, ajanın listesinin
> uzaması demektir** — iş yok olmadı, **doğru masaya taşındı.**

---

## TUR 3A'DA ELE ALINMAYANLAR *(kayıt — öncelik uyarısı)*

`tur-25-konsolidasyon.md` §6.1 TUR 3A iş listesini **öncelik sırasıyla**
vermişti. **Bu OTURUMDA** 6 ve 7 numaralı işler (`T-946`, `T-913`) ele alındı;
**1–5 arası bu oturumda ele alınmadı.**

⚠ **Not:** `kanal-marj-uzmani` ve `global-sourcing-kasifi` TUR 3A'da ayrıca
çalışmış ve **8 ticket açmıştır** (`T-611`…`T-614`, `T-881`…`T-884`) — aşağıdaki
liste yalnızca **bu oturumun** kapsamı içindir, TUR 3A'nın tamamı değil.

| Öncelik | İş | Ajan | Durum |
|---|---|---|---|
| **1** | **`T-947`** — KDVK md.36 CB kararı taraması | `gumruk-vergi-uzmani` | ⛔ **ele alınmadı** — ters modelin **TÜM sayılarını** çürütebilecek tek bulgu (~%22,7) |
| **2** | Gözetim tebliği yeniden taraması | `gumruk-vergi-uzmani` | ele alınmadı |
| **3** | **`T-942`** — `R8-K` kanal round-trip | `finans-fizibilite` | ele alınmadı |
| **4** | **`T-917`** — tek fiziksel mağaza turu | `turkiye-pazar-kasifi` | ele alınmadı — 5 kaydı **aynı anda** kapatır |
| **5** | `T-941` · `T-943` · `T-944` · `T-945` | çeşitli | ele alınmadı |

> **Sıra yanlış olmuş olabilir ve bu kayda geçirilmiştir**
> (`90-karar/tur-3a-ticket-degerlendirmesi.md` § kör nokta).
