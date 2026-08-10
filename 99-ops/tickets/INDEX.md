# TICKET İNDEKSİ — TUR 2.5 KAPANIŞ SONRASI

> Güncellendi: **2026-08-10, TUR 2.5 KAPANIŞ** (`yatirim-komitesi-baskani`).
> Kaynak: `99-ops/tickets/T-*.md` — **tek doğruluk kaynağı ticket dosyalarının
> kendisidir.** Bu indeks o dosyalardan programatik olarak türetilmiştir.
> Karar kayıtları: `90-karar/tur-2-konsolidasyon.md` → `90-karar/tur-25-preflight.md`
> → **`90-karar/tur-25-konsolidasyon.md`**

```
TOPLAM : 101 ticket
impact : CRITICAL 13 · HIGH 53 · MEDIUM 33 · LOW 1 · CONSTRAINT 1
status : OPEN 86 · ANSWERED 9 · RESOLVED 6
```

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
| `T-946` ➕ | `yatirim-komitesi-baskani` | `seytanin-avukati` | HIGH | OPEN | `R5` düzeltmesinin **bağımsız denetimi** + **DESEN denetimi** |
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
| `T-948` ➕ | `yatirim-komitesi-baskani` | `finans-fizibilite` | MEDIUM | OPEN | `P-2` tam tablosu + CSV'ye `λ` sütunları |
| `T-801` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | LOW | OPEN | LCL kanıt seti 11 değil **10** karttır |
| `T-205` | `mevzuat-ruhsat-uzmani` | `kanal-marj-uzmani` | CONSTRAINT | RESOLVED | 7584 s.K. m.2 görsel yasağı — `ACCEPTED BUSINESS CONSTRAINT` |

---

## HEDEF AJANA GÖRE AÇIK YÜK

*(“açık” = `status` ∈ {`OPEN`, `ANSWERED`}. Toplam açık: **95**, açık CRITICAL: **10**.)*

| Hedef ajan | Açık CRITICAL | Toplam açık |
|---|---|---|
| `gumruk-vergi-uzmani` | **1** *(`T-947`)* | **20** |
| `navlun-lojistik-uzmani` | 0 | 15 |
| **`yatirim-komitesi-baskani`** | **3** *(`T-304`, `T-851`, `T-852`)* | 14 |
| `mevzuat-ruhsat-uzmani` | **2** *(`T-301`, `T-601`)* | 13 |
| `finans-fizibilite` | **4** *(`T-104`, `T-466`, `T-912`, `T-942`)* | 11 |
| `global-sourcing-kasifi` | 0 | 11 |
| `turkiye-pazar-kasifi` | 0 | 5 |
| `kanal-marj-uzmani` | 0 | 5 |
| `seytanin-avukati` | 0 | 1 |

> **Başkana yönelik 3 açık `CRITICAL`'ın 3'ü de bir ARAŞTIRMA değil, bir
> KARAR veya İZİN beklemektedir** (`T-304` → dış temas izni; `T-851` →
> yatırımcı eşikleri; `T-852` → `fx` kaydı).
> Bu üçü `90-karar/investor-decisions-required.md`'ye taşınmıştır.
