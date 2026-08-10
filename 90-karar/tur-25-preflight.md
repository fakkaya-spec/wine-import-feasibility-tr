# TUR 2.5 PRE-FLIGHT — DURUM KONTROLÜ + YATIRIMCI GİRDİSİ KAYDI

```yaml
belge:                  tur-25-preflight
yazan:                  yatirim-komitesi-baskani
tarih:                  2026-08-10
tur:                    TUR 2.5 PRE-FLIGHT
kapsam:                 DURUM KONTROLU + YATIRIMCI GIRDISI KAYDI
karar_iceriyor_mu:      false      # YATIRIM karari icermez
arastirma_yapildi_mi:   false      # CLAUDE.md §1.16 — baskan arastirma yapmaz
web_aramasi_yapildi_mi: false
ajan_cagrildi_mi:       false
yeni_kanit_uretildi_mi: false      # hicbir evidence karti acilmadi/degistirilmedi
yeni_sayi_uretildi_mi:  false      # tek sayi baskan tarafindan tahmin edilmedi
karar_gunlugune_dokunuldu_mu: false
acilan_ticket:          [T-921, T-922, T-923, T-924, T-925]
```

> ## BU BELGE BİR YATIRIM KARARI DEĞİLDİR
>
> `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` / `SCALE` kararlarının **hiçbiri**
> bu belgede verilmemiştir ve verilemez. Nihai karar **TUR 6**'da,
> `90-karar/karar-gunlugu.md`'de verilir.
> **Bu turda `90-karar/karar-gunlugu.md` dosyasına DOKUNULMAMIŞTIR.**
>
> Bu belge iki iş yapar: **(§0–§1)** TUR 2.5 öncesi bir durum kontrolü,
> **(§2–§3)** iki yatırımcı girdisinin kayda geçirilmesi.

---

## 0. BU TURDA NE YAPILMADI (SINIR BEYANI)

| Yapılmadı | Neden |
|---|---|
| Yeni araştırma, web araması, yeni kanıt kartı | CLAUDE.md §1.16 |
| Ajan çağrılması | Bu bir pre-flight'tır |
| Herhangi bir **ajan bulgusunun değiştirilmesi** (599,90 dahil) | CLAUDE.md — başkan ajanın bulgusunu kendi tahminiyle değiştirmez |
| Herhangi bir gate'in açılması | Hiçbir gate koşulu gerçekleşmedi (§1.1) |
| Herhangi bir CRITICAL ticket'ın kapatılması veya impact indirimi | Hiçbiri için gerekçe yok (§1.3) |
| `90-karar/karar-gunlugu.md`'ye yazma | Karar TUR 6'ya aittir |
| **KDV hariç hedef fiyatların hesaplanması** | Türetme bir model işlemidir → `finans-fizibilite` (`T-922`) |
| Gelecek ÖTV tutarının yazılması | `BASE_DATE_kurali` + CLAUDE.md §1.1 |

**Bu turda değişen tek şeyler: (a) iki yatırımcı girdisi kaydedildi,
(b) kayıt hataları düzeltildi, (c) beş yeni ticket açıldı.**

---

# §1 — DURUM KONTROLÜ

## 1.1 `G0` = `PASS` korunuyor mu? — üç tetikleyici tek tek

`G0 PASS` **geri alınabilir** bir gate olarak işaretlidir. Üç geri alma
tetikleyicisi (`tur-2-preflight-housekeeping.md` §D.2) tek tek tarandı:

| # | Tetikleyici | TUR 2 sonundan bu yana gerçekleşti mi | Dayanak |
|---|---|---|---|
| **R1** | `C-252` **B okuması lehine** kapanır **VE** "Tekel GM eliyle" işlev için **halef merci** tespit edilir *(İKİSİ BİRDEN)* | **HAYIR** | `mevzuat-ruhsat-uzmani` bu turda **çağrılmadı**; `C-252` `OPEN`/LOW olarak değişmedi; `EV-2026-08-10-214` (halef merci) hâlâ `UNKNOWN`. **İki koşuldan sıfırı** gerçekleşti |
| **R2** | 7584 s.K. m.2'nin **ürünün rafta bulundurulmasını** kapsadığı **bağlayıcı bir metinle** ortaya çıkar | **HAYIR** | Yeni bağlayıcı metin yok. `C-203` `ACCEPTED BUSINESS CONSTRAINT` olarak duruyor; bu turda ne araştırıldı ne değiştirildi |
| **R3** | `C-202` sıralama döngüsünün **fiilen kilitlendiği** kanıtlanır | **HAYIR** | Yeni kanıt yok; `C-202` `OPEN` (HIGH), durumu değişmedi |

### **`G0` → `PASS` KORUNUR.**

**Ama bu turda da `G0` TEST EDİLMEMİŞTİR** — TUR 2'de olduğu gibi. Yaptığım
şey yine yalnızca *"tetikleyiciler gerçekleşmedi"* doğrulamasıdır ve bu,
**"yeni olumsuz kanıt aranmadı"** ile aynı şeydir. `G0 PASS` hâlâ **iki açık
çelişkinin (`C-252`, `C-203`) üzerinde durmaktadır**. `mevzuat-ruhsat-uzmani`
üç turdur (`TUR 2`, `TUR 2.5`) G0 kapsamında çalışmamıştır.

> **Kayıt:** `G0`'ın "test edilmemiş ama korunmuş" olma süresi uzuyor.
> Bu, tek başına bir blocker değildir ama **TUR 6'da kararın dayandığı en
> eski doğrulama** olacaktır ve orada belirtilmelidir.

## 1.2 Evidence bütünlüğü — programatik kontrol

`10-evidence/index.csv` üzerinde çalıştırılan kontroller (2026-08-10):

| Kontrol | Sonuç | Değerlendirme |
|---|---|---|
| Satır sayısı (header hariç) | **290** | Beklenen: 290 ✅ |
| Benzersiz `evidence_id` | **290** | ✅ |
| **Mükerrer `evidence_id`** | **0** | ✅ |
| `raw/` altındaki kanıt kartı (`.md`) | **290** | ✅ |
| **İndekste var, kartı yok** | **0** | ✅ |
| **Kartı var, indekste yok (öksüz)** | **0** | ✅ |
| **`tier: T5` + `status: FACT` ihlali** | **0** | ✅ **CLAUDE.md §2'ye tam uyum** |
| `evidence_id` referansı var ama indekste yok (9 `yaml` dosyası tarandı) | **0** | ✅ *(8 "hatalı" görünen kayıt, virgülle birleştirilmiş çoklu ID string'iydi; ayrıştırıldığında hepsi geçerli)* |

**Tier dağılımı:** T1 83 · T2 34 · T3 33 · T4 108 · T5 31 · tanımsız 1
**Statü dağılımı:** FACT 203 · ESTIMATE 47 · UNKNOWN 26 · SUPERSEDED 9 ·
CONFLICT 3 · ASSUMPTION 2

### İki küçük hijyen bulgusu (bloke etmiyor)

1. **`EV-2026-08-09-328` — `tier: -`** (tanımsız). Kart bir **negatif
   bulgudur** (*"Şili → Türkiye transit süresi ve navlunu"*, `status: UNKNOWN`).
   Negatif bulguda tier'ın boş bırakılması savunulabilir ama **şablon
   zorunlu alan** diyor. Bloke etmez; `navlun-lojistik-uzmani`'ya bildirilir.
2. **31 adet T5 kart** vardır ve **hiçbiri `FACT` değildir** — bu, projenin
   en güçlü tek disiplin göstergesidir. T5 kartlar `UNKNOWN`/`ASSUMPTION`/
   `SUPERSEDED` olarak durmaktadır.

> **Bu kontrolün göremediği şey:** kartların **içeriğinin doğruluğu**.
> Tarama yalnızca **yapısal bütünlüğü** ölçer. `EV-2026-08-09-405`'in
> Comtrade birim kodu yorumu gibi bir **içerik** hatası bu taramadan
> **temiz geçer**. Panzehir TUR 4'tür.

## 1.3 Açık CRITICAL ticket'lar — **6**, değişmedi

| ticket | status | hedef ajan | Neyi bloke ediyor | TUR 2.5'te değişti mi |
|---|---|---|---|---|
| **`T-104`** | `ANSWERED` | `finans-fizibilite` | **G1, G4** — ÖTV modelde sabit sayı olamaz | **Hayır.** Ama bugün **birinci ayağı somutlaştı** → `T-921` |
| **`T-301`** | `OPEN` | `mevzuat-ruhsat-uzmani` | **G2-L, G4** — antrepo bekleme süresi; ayrıca **konteyner modu (LCL↔FCL)** blokeri | Hayır — ajan çağrılmadı |
| **`T-304`** | `OPEN` | **`yatirim-komitesi-baskani`** | **G2-L, G4** — FCL navlunu hiçbir rotada yok (`C-311`) | Hayır — dış temas izni verilmedi |
| **`T-466`** | `OPEN` | `finans-fizibilite` | **G2, G4** — `exw`/`fob` `null` kalmalı | Hayır |
| **`T-601`** | `OPEN` | `mevzuat-ruhsat-uzmani` | **G4-K** — şarap 6585 m.7/3 anlamında "tarım ve gıda ürünü" mü (vade tavanı) | Hayır — ajan çağrılmadı |
| **`T-912`** | `OPEN` | `finans-fizibilite` | **G4 + her parasal çıktı** — `fx` `null` | Hayır |

**+ `OQ-901` (CRITICAL, sahibi: yatırımcı)** — karar eşiklerinin tamamı `TBD`.
**TUR 6'da nihai kararı bloke eder.** Bu turda ele alınmadı.

**+ YENİ: `T-921` (CRITICAL, OPEN)** — §1.4'te açıklanıyor.
**Açık CRITICAL sayısı: 6 → 7.**

> **CLAUDE.md §5 yürürlüktedir:** bunlar açıkken `finans-fizibilite` çıktısı
> **`APPROVED` olamaz — en fazla `DRAFT`.** Bu turda hiçbir CRITICAL
> kapatılmamış, hiçbirinin impact'i indirilmemiştir.

## 1.4 Model input bütünlüğü — **bir CRITICAL bulgu**

### 1.4.1 Parse ve şema

**9 `yaml` dosyasının 9'u da hatasız parse edilmektedir** (`kanal`, `lojistik`,
`makro`, `pazar`, `ruhsat`, `senaryolar`, `tedarikci`, `urun`, `vergi`) —
bu turdaki üç düzenlemeden **sonra** da doğrulanmıştır.

### 1.4.2 ⛔ CLAUDE.md §12 — GERÇEK VE CİDDİ BİR BULGU

> ### Engine `otv_maktu_zaman_serisi` bloğunu HİÇ OKUMUYOR.

Programatik tarama: `80-model/engine/*.py` (955 satır) içinde
`otv_maktu_zaman_serisi`, `BASE_DATE`, `son_gozlem_gecerlilik_ufku` veya
`asgari_maktu_tutar` ifadelerine **tek bir referans yoktur.**

Tarihle ilgili **tek** kod satırı `matrah_sirasi.py:217`'dedir:

```python
if meta.get("model_hedef_tarihi") is None:
    sonuc.eksik_girdiler.append("... model_hedef_tarihi = null ...")
```

**Bu, bugün kaydettiğim yatırımcı girdisiyle birleşince bir arıza zinciri
üretir:**

| # | Olgu |
|---|---|
| 1 | `model_hedef_tarihi` bugün `null` → **`2027-04-01`** oldu (§2) |
| 2 | Yani `matrah_sirasi.py:217`'deki **tek uyarı sustu** |
| 3 | `2027-04-01 > son_gozlem_gecerlilik_ufku (2026-12-31)` — engine bunu **fark edemez**, çünkü o alanı okumuyor |
| 4 | `VergiKalemi.hesaplanabilir_mi()` ÖTV satırını **hesaplanabilir** sayar (status `FACT`, `evidence_id` dolu, `effective_date` dolu, `matrah_tanimi` dolu, `tip: KARMA_YUKSEK_OLAN` geçerli enum) → hiçbir eksik listesine düşmez |
| 5 | Hesap implemente edildiği anda elde tek sayı vardır: `matrah_sirasi[sira=4].asgari_maktu_tutar = 71.2692` (2026-07-03 **kısayolu**) → **2027-04-01 için sessizce o kullanılır** |
| 6 | Bu, `vergi.yaml → engine_yasak` kuralının **tam olarak yasakladığı** davranıştır ve model kuralı **M-7**'nin ihlalidir |

**Hafifletici olgu:** Engine bugün **TUR 0 iskeletidir** — `hesaplandi=False`,
her adım *"HESAPLANMADI — TUR 0 iskeleti"* döner ve **hiçbir sayı
üretmemektedir.** Yani **bugün fiilî bir §12 ihlali YOKTUR.** Tehlike,
`finans-fizibilite` hesabı implemente ettiği anda **doğar** — yani TUR 2.5'te.

> **Bu, tarih girdisinin modeli DAHA GÜVENLİ değil, DAHA TEHLİKELİ yaptığı
> anlamına gelir.** Bunu gizlemiyorum; girdi kaydını yaparken aynı anda
> **`T-921`'i (CRITICAL)** açıyorum ve TUR 2.5 için bağlayıcı bir kapı
> koyuyorum (§4).

### 1.4.3 Diğer `evidence_id`'siz dolu sayılar — tarama sonucu

9 `yaml` dosyasında "dolu sayısal `value` + `evidence_id` yok" taraması
**10 aday** buldu. Tek tek değerlendirildi:

| Dosya · alan | Değer | Değerlendirme |
|---|---|---|
| `lojistik.yaml → urun_fizik.sise_hacmi_ml` | 750, **`FACT`** | ❌ **GERÇEK İHLAL.** `vergi.yaml` aynı olguyu `T-906(a)` ile **`ASSUMPTION` + `EV-2026-08-10-116`**'ya düzeltmiş; `lojistik.yaml` düzeltmeyi **almamış** ve *"Kanıt kartı gerekmez"* yazmıştır → **`T-924`** |
| `urun.yaml → urun.hacim_ml` | 750, `ASSUMPTION` | ⚠ Statü **doğru**, `evidence_id` **eksik**. Kart mevcut (`EV-2026-08-10-116`) → **`T-925`** |
| `lojistik.yaml → konteyner.spec_40hc.dara_kg` | 3900, `ASSUMPTION` | ⚠ Kabul edilebilir (`ASSUMPTION` + gerekçe) **ama** duyarlılık bandı (3.700–4.000) yalnızca serbest metindedir, engine okuyamaz → `T-924` md.3 |
| `lojistik.yaml → thd_limana_gore.*` | 165/185/192 USD | ✅ **İhlal değil.** `evidence_id: EV-2026-08-10-315` **blok seviyesinde** verilmiştir; alt alanlar miras alır |
| `pazar.yaml → gozlem_havuzu.toplam_gozlem` / `kdv_durumu_bilinen_gozlem_sayisi` | 52 / 2 | ✅ İhlal değil — ajanın **kendi tablosunun** sayımı; `notes` bunu açıkça yazıyor |
| `tedarikci.yaml → risk.alternatif_tedarikci_sayisi` | 0 | ✅ Bir **yokluk** kaydı |
| `tedarikci.yaml → rfq_ile_ogrenilebilecek_alanlar` | 21 | ✅ Ajanın kendi listesinin sayımı |

**Sonuç: bir gerçek §1.5/§1.6 ihlali (`lojistik.yaml`), bir eksik bağ
(`urun.yaml`).** İkisi de **model çıktısını değiştirmez** ama denetim
güvenini düşürür → `T-924`, `T-925` (MEDIUM).

### 1.4.4 Katman etiketleri

Tarama, katman etiketlerinde **çelişki bulmadı**. `pazar.yaml` `K1`–`K6`,
`kanal.yaml` `M1`, `master-commercial-input-table.md` `T4` (Incoterm/katman
kuralı) ve `senaryolar.yaml`'a bugün eklenen `K7`/`L1`–`L7` tutarlıdır.
`l8_chain_retail` **`null` / `UNKNOWN`** olarak durmaktadır ve bu turda da
doldurulmamıştır (§3).

## 1.5 `T-104` ve diğer `ANSWERED` ticket'lar — modeli engelliyorlar mı?

**Sorunun cevabı ticket başına farklıdır ve tek bir "hayır" yanlış olur.**

| ticket | status | **Modeli ENGELLİYOR mu?** | Gerekçe |
|---|---|---|---|
| **`T-104`** | `ANSWERED` / CRITICAL | ⚠ **KISMEN ENGELLİYOR** | *Veri yapısı* ayağı tamam; ama **engine ayağı** (`T-921`) açıldığı için **ÖTV sayısı üretilemez**. Model **çalışır**, ÖTV çıktısı **`UNKNOWN` döner**. Bu bir arıza değil, **doğru davranıştır** — ama `T-921` kapanmadan ÖTV'li hiçbir sayı basılamaz |
| `T-401` | `ANSWERED` | ❌ Engellemez | Menşe→tarife eşlemesi `vergi.yaml`'da dolu ve `FACT`. Kalan çekince kaynak erişimi (T3 belge, Şili) |
| `T-462` | `ANSWERED` | ❌ Engellemez | Moldova T1 ile kapatıldı; NZ ayağı **kapsam dışı** |
| `T-464` | `ANSWERED` | ❌ Engellemez | Negatif arama sonucu; model girdisi yok |
| `T-506` | `ANSWERED` | ❌ Engellemez | Fark büyüklüğü `UNKNOWN`; zaten `kanal.yaml` `SENSITIVITY_ONLY` |
| `T-901` · `T-902` · `T-906` | `ANSWERED` | ❌ Engellemez | Kayıt hijyeni; ilgili alanlar düzeltilmiş |

### Net cevap

> **`ANSWERED` ticket'lar modeli ÇALIŞTIRMAYI engellemez.**
> **Çıktının STATÜSÜNÜ belirlerler:** CLAUDE.md §5 gereği 7 açık CRITICAL
> ticket varken çıktı **en fazla `DRAFT`**'tır.
>
> **Tek istisna `T-104`/`T-921`'dir ve o bir statü sorunu değil, bir HESAP
> sorunudur:** engine seriyi okumadan üretilecek her ÖTV sayısı
> **geçersizdir**, `DRAFT` bile olamaz. Bu ayrım korunmalıdır.

## 1.6 LCL evidence TTL — **kayıt düzeltmesi + 6 gün kaldı**

### 1.6.1 Kayıt düzeltmesi: 11 değil, **10**

Proje kayıtlarında dört ayrı yerde tekrarlanan *"`EV-2026-08-10-301…311`
(**11 LCL kartı**), `ttl: 6d`"* ifadesi **yanlıştır**:

| evidence_id | ttl | son geçerlilik | status | nedir |
|---|---|---|---|---|
| `-301` `-302` `-303` `-305` `-306` `-307` `-308` `-309` `-310` `-311` | **6d** | **2026-08-16** | `FACT` | **10 canlı LCL kotasyonu** |
| **`-304`** | **14d** | **2026-08-24** | **`UNKNOWN`** | **LCL kotasyonu DEĞİL** — *"İtalya çıkışlı hiçbir limanda kotasyon YOK"* **negatif bulgu kartı** |

**Hata kaynağı başkandadır** (aralık notasyonu `301…311` sayılırken `-304`'ün
farklı nitelikte olduğu görülmemiştir). **Ajanın kartları doğrudur** — ajan
`-304`'ü zaten `UNKNOWN` + `14d` olarak doğru işaretlemiştir.

**Bu bir bulgu reddi değil, bir başkan kayıt hatasının düzeltilmesidir.**
Düzeltilecek yerler: `master-commercial-input-table.md` §5.6 **M-10** ·
`tur-2-konsolidasyon.md` §2.1/4 ve §4.2 **K-3** · `acik-sorular.md` `OQ-912` ·
`T-913`. → **`T-923`**

**Neden önemli:** *"11 rota için kotasyon var"* okuması **İtalya'nın
kapsandığı** izlenimi verir. Gerçek: İtalya **hiçbir modda** kotasyona sahip
değildir ve Türkiye'nin **en güçlü şarap ithalat hattıdır**
(5.749.972 L/2025, `T-916`). Hata, **projenin en büyük lojistik boşluğunu
bir "var" satırının içine gizlemektedir.**

### 1.6.2 Pencere yeterli mi?

```
Bugün                     : 2026-08-10
LCL kotasyonları STALE    : 2026-08-16
KALAN                     : 6 gün  (tam çalışma günü: 5)
```

**Diğer tazelik kapıları (programatik tarama):**

| Tarih | Ne bayatlar | Adet |
|---|---|---|
| **2026-08-16** | LCL kotasyonları | **10** |
| 2026-08-23 | Türetilmiş lojistik kartları (`-323`, `-330`…`-333`) | 5 |
| 2026-08-24 | FCL/İtalya/İspanya türev kartları (`-304`, `-312`, `-322`, `-323`, `-324`, `-329`, `-330`, `-331`) | 8 |
| **2026-09-08** | **ÖTV 71,2692 TL/lt** (`EV-2026-08-09-111`) + tüm raf gözlemleri | 1 + `pazar.yaml` |

**Bugün itibarıyla zaten STALE olan:** yalnızca `EV-2026-08-09-112`
(`ttl: 0d`) — ve o zaten **`SUPERSEDED`** statüsündeki eski ÖTV tutarıdır
(61,3914). Ayrıca dört kart daha `ttl: 0d`'dir (`-321`, `-560`, `-618`,
`-619`, `-620`) ve **hepsi bilinçli olarak `SUPERSEDED`/`UNKNOWN`/
`ASSUMPTION`**'dır — yani "tek kullanımlık, tekrar kullanılamaz" işaretidir.
**Bu doğru bir kullanımdır, bir arıza değildir.**

### **Cevap: pencere YETERLİDİR — ama sadece bu hafta.**

TUR 2.5 **2026-08-15'e kadar** çalıştırılırsa navlun bacağı kanıtlıdır.
2026-08-16'dan sonra çalıştırılırsa **projedeki tek gerçek navlun verisi
`UNKNOWN`'a döner** ve `T-304`'ün LCL ayağı yeniden açılır.

> **`OQ-912`'ye kısmi cevap (başkan kararı, bir araştırma değil):**
> **TUR 2.5 penceresi 2026-08-10 → 2026-08-15'tir.** Bu, bir tarih
> tercihidir; `T-913` (kotasyonların **masabaşında** yenilenip
> yenilenemeyeceği) hâlâ cevapsızdır ve cevaplanırsa pencere genişler.

## 1.7 TUR 3 öncesi **ucuz** kapatılabilir alanlar — güncel durum

TUR 2 konsolidasyonunda üç alan işaretlemiştim. Güncel durum:

| # | Alan | TUR 2'deki teşhis | **Bugünkü durum** |
|---|---|---|---|
| **1** | **`model_hedef_tarihi`** | *"bir yatırımcı beyanıdır"* — en ucuz | ✅ **BUGÜN KAPANDI** (girdi olarak) — **ama beklenmedik bir CRITICAL doğurdu** (`T-921`). Ucuzdu, ama **bedava değildi** |
| **2** | **`fx`** (`makro.yaml`) | *"neredeyse sıfır maliyet"* — tarihli tek kur + bant | ❌ **HÂLÂ `null`.** `T-912` (CRITICAL) ve `T-911` (HIGH) açık. **Değişmedi** |
| **3** | **`l8_chain_retail`** | *"1 kişi, 1–2 hafta, ≈0 TL"* — mağaza turu | ❌ **HÂLÂ `null`.** `T-603`, `T-917` açık. **Değişmedi.** Bugün eklenen TARGET merdiveni **bunun yerine geçmez** (§3) |

### Bu turda tespit edilen **yeni** ucuz alanlar

| # | Alan | Maliyet | Kim | Ne açar |
|---|---|---|---|---|
| **4** | **`lojistik.yaml` 750 ml hijyeni** (`FACT` → `ASSUMPTION` + kart bağı) | ~5 dakika | `navlun-lojistik-uzmani` | Denetim güveni; `T-924` |
| **5** | **`urun.yaml` `hacim_ml` kart bağı** | ~2 dakika | `global-sourcing-kasifi` | `T-925` |
| **6** | **LCL kotasyonlarının masabaşında yenilenip yenilenemeyeceği** | ~30 dakika **eğer** kotasyonlar gerçekten "yayınlanmış" ise | `navlun-lojistik-uzmani` | **10 kartlık tek gerçek navlun setinin ömrünü uzatır** — `T-913`, `T-923` |
| **7** | **`makro.yaml` Yİ-ÜFE varsayım ekseni** | düşük — bir `ASSUMPTION` + bant | `finans-fizibilite` | `T-104`'ün **ikinci ayağı**; ÖTV projeksiyonunun ön koşulu |
| **8** | **`senaryolar.yaml` meta'sının bayatlığı** | ~1 dakika | — | Dosya `"TUR 0 — kurulum"` diyordu; **bugün düzeltildi** |

> ### KALDIRAÇ GÖZLEMİ — DEĞİŞMEDİ VE KÖTÜLEŞTİ
>
> TUR 2'de *"üç ucuz alan kapatılabilir"* demiştim. **Üç turdur ikisi
> (`fx`, `l8_chain_retail`) kapanmamıştır.** Üçüncüsü bugün kapandı ve
> **yeni bir CRITICAL doğurdu.**
>
> `fx` ve `l8_chain_retail` birlikte **bir kur kaydı + bir mağaza turu**
> maliyetiyle, TUR 2.5'in üretebileceği çıktının **kapsamını iki katına
> çıkarır**. `fx` olmadan ters model yalnızca `CIF_TRY`'ye kadar gider;
> `fx` ile **azami FOB**'a kadar gider — yani *"bu segment matematiksel
> olarak mümkün mü"* sorusunun **asıl testine** ulaşır.
>
> **Bunu bir karar olarak veremem** (bu tur karar turu değildir), ama
> üçüncü kez kayda geçiriyorum.

---

# §2 — MODEL HEDEF TARİHİ KAYDI (YATIRIMCI GİRDİSİ)

## 2.1 Kaydedilen girdi

```
BASE_TARGET_DATE = 2027-04-01
status           = INVESTOR_ASSUMPTION      # FACT DEGILDIR

EARLY = 2027-01-01
BASE  = 2027-04-01
LATE  = 2027-07-01
```

**Yazıldığı yerler:**
`80-model/inputs/vergi.yaml → meta.model_hedef_tarihi` (+ `_status`,
`_kaynak`, `_notu`, `_uyarisi`) ve `meta.tarih_senaryolari` (yeni blok) ·
`80-model/inputs/senaryolar.yaml → tarih_senaryolari` (ayna kayıt).

**`evidence_id`: YOKTUR ve olmayacaktır.** Bu bir dış olgu değil, bir
yatırımcı beyanıdır; kanıt kartı açılması **yanlış olurdu** ve kanıt
sistemini kirletirdi.

## 2.2 ⚠ ÜÇ TARİH, ÜÇ FARKLI ÖTV REJİMİ

ÖTV maktu tutarları **Ocak ve Temmuz** aylarında Yİ-ÜFE ile **ayrı bir
karara gerek olmaksızın** yeniden belirlenir (ÖTVK md.12/3,
`EV-2026-08-09-114`, **T1**).

| Senaryo | Tarih | **ÖTV rejimi** | Rejim netliği | Araya giren doğrulanmamış revizyon | **Tutar** |
|---|---|---|---|---|---|
| **EARLY** | **2027-01-01** | **Ocak 2027 revizyonu** | ❌ **SINIR TARİHİ** | **0 veya 1** | `FUTURE_UNKNOWN` |
| **BASE** | **2027-04-01** | **Ocak 2027 revizyonu** | ✅ **NET** | **1** | `FUTURE_UNKNOWN` |
| **LATE** | **2027-07-01** | **Temmuz 2027 revizyonu** | ❌ **SINIR TARİHİ** | **1 veya 2** | `FUTURE_UNKNOWN` |

### 2.2.1 Sınır belirsizliği neden var — bu bir gözlem, bir tahmin değil

Doğrulanmış iki yürürlük tarihi şunlardır:

| Yürürlük | Tutar | evidence_id |
|---|---|---|
| **2025-12-31** | 61,3914 TL/lt | `EV-2026-08-09-112` (T1, `SUPERSEDED`) |
| **2026-07-03** | **71,2692 TL/lt** | `EV-2026-08-09-111` (T2, `FACT`) |

**Revizyonlar 1 Ocak / 1 Temmuz'a BİREBİR OTURMAMAKTADIR.** Kanun
*"değişimin **ilanı gününden** geçerli olmak üzere"* der — biri ayın **son
gününde** (31 Aralık), diğeri ayın **üçüncü gününde** (3 Temmuz) yürürlüğe
girmiştir.

**Sonuç:**
- **`EARLY` (2027-01-01)**, Ocak 2027 revizyonunun **öncesine de sonrasına
  da** düşebilir. İki farklı tutar ihtimali vardır.
- **`LATE` (2027-07-01)**, 2026 desenine göre (yürürlük 3 Temmuz) **hâlâ
  Ocak 2027 rejiminde** olabilir. Yine iki ihtimal.
- **`BASE` (2027-04-01)**, iki revizyonun **tam arasındadır** ve hiçbir
  sınıra değmez. **Üç senaryonun rejim açısından TEK NET olanıdır.**

> **Kayda geçirilen gözlem:** Kurucunun `BASE` seçimi, üç aday içinde
> **epistemolojik olarak en temiz olanıdır.** Bu bir tavsiye değil, bir
> tespittir — ve `EARLY`/`LATE`'in **ikisinin de iki rejim altında ayrı
> ayrı** çalıştırılması gerektiği anlamına gelir.

### 2.2.2 Bilinen tek gerçek değer vs bilinmeyen

```
CURRENT_CONFIRMED
    value           : 71,2692 TL/litre
    effective_date  : 2026-07-03
    evidence_id     : EV-2026-08-09-111   (tier T2, status FACT)
    gecerlilik sonu : 2026-12-31
    ttl             : 30d  ->  STALE: 2026-09-08

FUTURE_UNKNOWN
    kapsam          : EARLY, BASE, LATE — UCU DE
    value           : YOK. SAYI YAZILMAZ.
    temsil          : SENSITIVITY_ONLY
```

**Üç hedef tarihin ÜÇÜ DE `son_gozlem_gecerlilik_ufku` (2026-12-31)
ötesindedir.** Yani **hiçbiri için doğrulanmış ÖTV tutarı yoktur.**

**Bağlayıcı yasak:** `CURRENT_CONFIRMED`, üç tarihin **hiçbiri** için
"geçerli tutar" olarak kullanılamaz. Kullanılırsa çıktı **geçersizdir**
(CLAUDE.md §1.1 + §12). Tarihsel artış oranı (+%16,09) bir **gözlemdir**,
bir **tahmin girdisi değildir**.

### 2.2.3 Duyarlılık ekseni — sayılar bana ait DEĞİLDİR

`senaryolar.yaml → duyarlilik_eksenleri[OTV]`'de `min`/`base`/`max`
**bilinçli olarak `null` bırakılmıştır.** Yanına eklenen
`talep_edilen_senaryo_noktalari` bloğu **`%0 / %8 / %16 / %25 per 6 ay`**
setini taşır ve bu set **benim tahminim değildir** — `T-104`'te
`gumruk-vergi-uzmani` tarafından **talep edilmiştir** ve kaynağı
gösterilerek aktarılmıştır. `%16` noktasının tarihsel çapası vardır
(gerçekleşen +%16,09); diğer üçü **çapasızdır** ve saf duyarlılık
noktasıdır.

**Çapraz çarpım zorunludur:** 3 tarih × 4 artış noktası, `EARLY` ve `LATE`
için ikişer rejim ihtimaliyle. **Tek bir ÖTV sayısı üretilemez.**

## 2.3 `otv_maktu_zaman_serisi` BOZULMADI — doğrulandı

Bugünkü düzenlemeden sonra blok yeniden parse edilip alan alan
karşılaştırıldı:

| Alan | Durum |
|---|---|
| `gozlenen_degerler` (2 kayıt: 61,3914 `SUPERSEDED` / 71,2692 `FACT`) | ✅ **DEĞİŞMEDİ** |
| `son_gozlem_gecerlilik_ufku: 2026-12-31` | ✅ **DEĞİŞMEDİ** |
| `gelecek_degerler: null` / `gelecek_deger_status: UNKNOWN` | ✅ **DEĞİŞMEDİ** |
| `gelecek_deger_kurali` | ✅ **DEĞİŞMEDİ** |
| `engine_okuma_kurali` · `engine_yasak` · `antrepo_etkilesimi` | ✅ **DEĞİŞMEDİ** |
| **`epistemik_ayrim`** | ➕ **YENİ** — yalnızca **etiket** ekler; yeni otorite yaratmaz (`gozlenen_degerler` esas kalır) |

**Hiçbir vergi oranı, tutarı veya matrah tanımı değiştirilmemiştir.**

## 2.4 `OQ-002` → **`INPUT_RECORDED`**, kapatılmadı

```yaml
oq_id:        OQ-002
onceki_durum: OPEN
yeni_durum:   INPUT_RECORDED       # CLOSED DEGIL
```

**Neden kapatmıyorum — üç gerekçe:**

1. **Kaydedilen bir olgu değil, bir beyandır.** Sorunun orijinal kapanış
   yolu (*"`mevzuat-ruhsat-uzmani`'nın T0 → ilk konteyner takviminden
   türetilir"*) **kullanılmamıştır.** O takvim hâlâ `ASSUMPTION` sıralamaya
   dayanır (`C-202` açık) ve dağıtım yetki belgesinin **işlem süresi
   mevzuatta tanımsızdır** (`T-202`). Tarihin **gerçekçiliği**
   doğrulanmamıştır.
2. **Sorunun asıl blokeri tarih değil, o tarihteki ÖTV tutarıydı.** Üç
   senaryonun üçü de ufuk ötesindedir → `OQ-G08` **aynen açıktır.**
3. **Kayıt modeli güvenlileştirmedi, tehlikeyi artırdı** (§1.4.2) →
   `T-921`.

**`OQ-002`'yi kapatacak koşullar:** `T-921` `RESOLVED` **VE** tarihin T0
takviminden doğrulanması (`T-202`/`C-202`). **İkisi birden gerekir.**

---

# §3 — HEDEF RAF FİYATI MERDİVENİ KAYDI (YATIRIMCI GİRDİSİ)

## 3.1 Kaydedilen merdiven

**750 ml still wine · tüketici raf fiyatı · HEPSİ KDV DAHİL:**

| id | KDV dahil (TRY) | KDV hariç |
|---|---|---|
| `TGT_599` | **599** | `null` |
| `TGT_699` | **699** | `null` |
| `TGT_799` | **799** | `null` |
| `TGT_899` | **899** | `null` |
| `TGT_999` | **999** | `null` |

- **Etiket:** `TARGET_SHELF_PRICE`
- **Senaryo sınıfı:** `INVESTOR_TARGET_SCENARIO`
- **Katman:** `L8_CONSUMER_SHELF_PRICE` (hedef)
- **Statü:** **`INVESTOR_ASSUMPTION`** — `FACT` **değil**, `ESTIMATE` **de değil**
- **`evidence_id`: YOKTUR ve olmayacaktır**

**Yazıldığı yer:** `80-model/inputs/senaryolar.yaml →
hedef_raf_fiyati_merdiveni` (+ `L1`–`L7` bağlayıcı kurallar).

**KDV hariç karşılıklar bilinçli olarak boş bırakılmıştır.** Formül
`yaml`'da verilmiştir; **türetme bir model işlemidir** ve
`finans-fizibilite`'ye aittir (CLAUDE.md §1.16 — başkan sayı üretmez).
→ `T-922`.

## 3.2 ⛔ TARGET vs OBSERVED — tuzak nasıl kapatıldı

> ### 599 TL ile 599,90 TL SAYISAL OLARAK NEREDEYSE AYNI, EPİSTEMOLOJİK OLARAK FARKLI NESNELERDİR.

| | **(A) OBSERVED_BENCHMARK** | **(B) TARGET_SHELF_PRICE** |
|---|---|---|
| **Değer** | **599,90 TL** | **599 · 699 · 799 · 899 · 999 TL** |
| **Nerede yaşar** | `pazar.yaml → benchmark_1.raf_fiyati_try` | `senaryolar.yaml → hedef_raf_fiyati_merdiveni` |
| **Nedir** | Metro Türkiye'de 2026-08-09'da **fotoğraftan okunmuş** gerçek raf fiyatı. **Bir ÖLÇÜMDÜR** | Kurucu/yatırımcı hedefi. Piyasada **görülmemiştir**. **Bir İSTEKTİR** |
| **Katman** | `L8_METRO_CASH_CARRY` | `L8_CONSUMER_SHELF_PRICE` (hedef) |
| **Statü** | `FACT` (okuma) / temsil gücü `MEDIUM` | `INVESTOR_ASSUMPTION` |
| **evidence_id** | `EV-2026-08-09-501` | **YOK** — bir dış olgu değildir |
| **Geçerli kurallar** | `K1` `K2` `K3` `K5` `K6` | `K7` + `L1`–`L7` |

**Bir bu kadar önemli:** aradaki **0,90 TL yakınlık bir TEYİT DEĞİLDİR.**
Hedefin gözlemi doğruladığı, gözlemin hedefi mümkün kıldığı veya ikisinin
"aynı sayı" olduğu **hiçbir raporda, hiçbir tabloda, hiçbir model çıktısında
yazılamaz.** Yakınlık **tesadüftür** ve öyle raporlanır.

### Ayrımın korunma mekanizması — üç kilit

| Kilit | Nerede | Ne yapar |
|---|---|---|
| **`pazar.yaml → K7`** *(YENİ, bağlayıcı)* | `katman_kurallari` | İki nesneyi isim isim, katman katman, statü statü ayırır; beş yasak sayar |
| **`senaryolar.yaml → L1…L7`** *(YENİ, bağlayıcı)* | `hedef_raf_fiyati_merdiveni` | Merdivenin gözlem gibi alıntılanmasını, ortalanmasını ve `FACT` raporlanmasını yasaklar |
| **`pazar.yaml → l8_chain_retail.tur25_notu`** *(YENİ)* | `l8_chain_retail` | Merdivenin bu alanı **doldurmadığını** alanın kendi içinde yazar |

### `pazar.yaml`'da NE DEĞİŞMEDİ (doğrulandı)

| Alan | Değer | Durum |
|---|---|---|
| `benchmark_1.raf_fiyati_try.value` | **599.9** | ✅ **DOKUNULMADI** |
| `benchmark_2.raf_fiyati_try.value` | **649.9** | ✅ **DOKUNULMADI** |
| `benchmark_*.kdv_durumu` · `confidence` · `promosyon_durumu` | — | ✅ **DOKUNULMADI** |
| `l8_chain_retail.deger_try` | `null` / `UNKNOWN` | ✅ **DOKUNULMADI** |
| `K1`–`K6` | — | ✅ **DOKUNULMADI** |

**Eklenen tek şey `K7` ve bir `tur25_notu`'dur.**

## 3.3 Bu merdiven neyi AÇAR, neyi AÇMAZ

| **AÇAR** | **AÇMAZ** |
|---|---|
| Ters modelin **hedef çapasını** — `master-commercial-input-table.md` §5.3 md.4'ün *"açıkça `ASSUMPTION` etiketli bir hedef bandı"* şartı **karşılandı** | **`G3`'ü açmaz.** `l8_chain_retail` hâlâ `null`; `T-504`, `T-603`, `T-917` açık; `OQ-001` `PARTIALLY_RESOLVED` |
| TL zincirinin (`L8 → L7 → L6 → L5 → L4 → CIF_TRY`) **başlangıç noktasını** | **`T-921` kapanmadan ÖTV adımını geçemez** → zincir `CIF_TRY`'ye **ulaşamaz** |
| *"599 TL basamağı matematiksel olarak mümkün mü"* sorusunu — **TUR 2.5'in tek karar-değerli çıktısı** | **Gerçek zincir rafının ölçüldüğü** anlamına **gelmez** |

## 3.4 Gözlenen bantla tutarlılık — kayıt notu

*(Bu yeni araştırma değildir; iki mevcut kaydın karşılaştırılmasıdır.)*

`pazar.yaml → segment` bandı **600 – 900 TL**'dir (ikisi de `ESTIMATE`,
`MEDIUM`, tek kanala dayalı, `C-501` **AÇIK**). Merdivene göre:

| Basamak | Banda göre |
|---|---|
| 599 | bandın **hemen altında** |
| 699 · 799 · 899 | band **içinde** |
| 999 | bandın **üstünde** |

> **Bu bir doğrulama DEĞİLDİR.** Bandın kendisi **tek bir online uzman
> perakendeciye** (`iyisarap.plus`, 52 gözlemin 45'i) dayanan bir
> `ESTIMATE`'tir ve fiziksel mağaza turu yapılmadan *"pazar bandı"* diye
> okunamaz (`gozlem_havuzu.tek_kanal_yogunlasmasi_uyarisi`, `OQ-502`,
> `T-917`). İki `ASSUMPTION`/`ESTIMATE`'in birbirine yakın çıkması,
> **ikisini de doğrulamaz.**

---

# §4 — TUR 2.5 İÇİN BAĞLAYICI KAPILAR

`master-commercial-input-table.md` §5.6'daki **M-1 … M-10** kuralları
**aynen yürürlüktedir.** Bu turda **üç yeni kapı** eklenir:

| # | Kapı | Dayanak |
|---|---|---|
| **P-1** | **`T-921` kapanmadan hiçbir ÖTV sayısı üretilemez.** Engine seriyi okumadan basılan her ÖTV değeri **geçersizdir** — `DRAFT` bile olamaz | §1.4.2 |
| **P-2** | **TARGET merdiveninin beş basamağı × üç tarih × dört ÖTV noktası AYRI AYRI** çalıştırılır. Ortalama **alınmaz**; tek sonuç **sunulamaz** | `L3`, `L6`, `T-104` |
| **P-3** | ⚠ **TAZELİK KAPISI: TUR 2.5, 2026-08-16'dan ÖNCE çalıştırılmalıdır.** Aksi hâlde **10** LCL kartı `STALE`'dir ve navlun bacağı `UNKNOWN`'a döner. **6 gün kaldı** | §1.6, `T-913`, `T-923` |
| — | *(M-1 hatırlatma)* **Çıktı `DRAFT`'tır.** **7** açık CRITICAL ticket | CLAUDE.md §5 |
| — | *(M-3 hatırlatma)* **599,90 tek gerçek piyasa fiyatı olarak kullanılamaz** — ve artık **599 ile de karıştırılamaz** | `K5` + **`K7`** |

## 4.1 Güncel gate durum tablosu — 2026-08-10 (TUR 2.5 PRE-FLIGHT)

| Gate | Soru | Sahibi | **Durum** | Bu turda değişim | Açan tek koşul |
|---|---|---|---|---|---|
| **G0** Yasal yol | Yasal olarak kurulabilir mi? | `mevzuat-ruhsat-uzmani` önerir → başkan karar verir | **`PASS`** | **değişmedi** — R1/R2/R3'ün hiçbiri gerçekleşmedi; **ama test de edilmedi** | — *(izleme: R1/R2/R3)* |
| **G1** Vergi yapısı | Vergi yükü kanıtlı ve satır satır hesaplanabilir mi? | `gumruk-vergi-uzmani` | **`BLOCKED`** | ⚠ **Bir ayağı ilerledi, bir ayağı kötüleşti:** `model_hedef_tarihi` girildi (**ilerleme**) ama engine ayağı somutlaştı (**`T-921`, CRITICAL**) | `T-104` + **`T-921`** + Yİ-ÜFE varsayımı |
| **G2** Tedarik | Gerçek tedarik kaynağı ve fiyatı var mı? | `global-sourcing-kasifi` | **`BLOCKED`** | değişmedi | Gerçek RFQ (≥5 tedarikçi) — **masabaşıyla açılamaz** |
| **G2-L** Lojistik / landed | L1→L2→L3 kurulabiliyor mu? | `navlun-lojistik-uzmani` | **`BLOCKED`** | ⚠ **kötüleşti** — LCL setinin ömrüne **6 gün** kaldı; kart sayısı 11→**10** düzeltildi | `T-304` (3 forwarder yazılı FCL kotasyonu) |
| **G3** Pazar | Benchmark doğrulandı mı, segment gerçek mi? | `turkiye-pazar-kasifi` | **`BLOCKED`** | **değişmedi.** TARGET merdiveni **G3'ü AÇMAZ** (`K7`, `L4`) | `OQ-001` promosyon ayağı (`T-504`) + `l8_chain_retail` (`T-603`/`T-917`) |
| **G4** Ekonomi | Model kanıtlı girdilerle pozitif contribution veriyor mu? | `finans-fizibilite` | **`NOT_EVALUATED`** | değişmedi | G1 + G2 + G2-L + G3 |
| **G4-K** *(alt-durum)* Kanal | L6→L7→L8 sayısal kurulabiliyor mu? | `kanal-marj-uzmani` | **`BLOCKED`** | değişmedi | `T-603` + `T-604` + `T-601` |
| **G5** Risk | Kırmızı takımın CRITICAL'ları kapandı mı? | `seytanin-avukati` | **`NOT_EVALUATED`** | değişmedi | TUR 4 |

> **Bu turda hiçbir gate açılmamıştır.** İki yatırımcı girdisinin kaydı bir
> gate açmaz; yalnızca TUR 2.5'in **ne hesaplayabileceğini** genişletir.

## 4.2 Açılan ticket'lar

| ticket | hedef ajan | impact | konu |
|---|---|---|---|
| **`T-921`** | `finans-fizibilite` | **CRITICAL** | Engine `otv_maktu_zaman_serisi`'ni **hiç okumuyor**; `model_hedef_tarihi` dolduğu için `is None` uyarısı **sustu**; ufuk denetimi **yok** |
| **`T-922`** | `finans-fizibilite` | HIGH | TARGET merdiveni kaydedildi; ters model kuralları (`L1`–`L7`), KDV hariç türetmesi, çapraz çarpım |
| **`T-923`** | `navlun-lojistik-uzmani` | HIGH | **Kayıt düzeltmesi:** "11 LCL kartı" → **10**; `-304` bir negatif bulgu kartıdır; yenileme penceresi 6 gün |
| **`T-924`** | `navlun-lojistik-uzmani` | MEDIUM | `lojistik.yaml` 750 ml `FACT` + `evidence_id` yok → §1.5/§1.6 ihlali; `dara_kg` bandı yapısal değil |
| **`T-925`** | `global-sourcing-kasifi` | MEDIUM | `urun.yaml → hacim_ml` `evidence_id` eksik; kart mevcut (`EV-2026-08-10-116`) |

## 4.3 Bu turda güncellenen dosyalar

| Dosya | Ne yapıldı |
|---|---|
| `90-karar/tur-25-preflight.md` | *(bu dosya)* — yeni |
| `80-model/inputs/vergi.yaml` | `meta.model_hedef_tarihi*` (yatırımcı girdisi) · `meta.tarih_senaryolari` (yeni) · `otv_maktu_zaman_serisi.epistemik_ayrim` (yeni) · `meta.baskan_mudahalesi_tur25`. **Hiçbir vergi oranı/tutarı/matrahı değişmedi; `otv_maktu_zaman_serisi` bozulmadı** |
| `80-model/inputs/senaryolar.yaml` | `tarih_senaryolari` (yeni) · `hedef_raf_fiyati_merdiveni` (yeni, `L1`–`L7`) · `duyarlilik_eksenleri[OTV].talep_edilen_senaryo_noktalari` (T-104 kaynaklı) · `meta` bayatlığı düzeltildi |
| `80-model/inputs/pazar.yaml` | **`K7`** (TARGET vs OBSERVED, bağlayıcı) + `l8_chain_retail.tur25_notu` + `meta.baskan_mudahalesi_tur25`. **HİÇBİR DEĞER DEĞİŞMEDİ** — 599,90 / 649,90 / `l8_chain_retail: null` aynen |
| `99-ops/acik-sorular.md` | `OQ-002` → **`INPUT_RECORDED`** (kapatılmadı) + gerekçe + ÖTV rejim eşlemesi; TUR 2.5 durum tablosu eklendi. **Orijinal `OQ-002` metni korundu** |
| `99-ops/tickets/T-921…T-925.md` | Beş yeni ticket |

**`90-karar/karar-gunlugu.md` dosyasına DOKUNULMAMIŞTIR.**
**Hiçbir kanıt kartı (`10-evidence/raw/`) veya `index.csv` satırı
değiştirilmemiş, eklenmemiş veya silinmemiştir.**

## 4.4 Reddedilen bulgu listesi

**Bu turda reddedilen ajan bulgusu: 0.**

Düzeltilen kayıt hataları: **1**, ve o **başkanın kendi hatasıdır** —
*"11 LCL kartı"* ifadesi (§1.6.1). `navlun-lojistik-uzmani`'nın kartları
**doğrudur** ve ajan `-304`'ü zaten doğru işaretlemiştir.

Doğrulanan ajan davranışları:
- `gumruk-vergi-uzmani`'nın `model_hedef_tarihi`'ni **doldurmama** kararı —
  **doğrulandı**; alanı bugün **başkan** doldurmuştur, ajan değil.
- `gumruk-vergi-uzmani`'nın `gelecek_degerler: null` bırakma kararı —
  **doğrulandı** ve bugün eklenen `epistemik_ayrim` bloğuyla **pekiştirildi**.
- `turkiye-pazar-kasifi`'nin `l8_chain_retail`'i **doldurmama** kararı —
  **doğrulandı**; TARGET merdiveni o alanı doldurmak için **kullanılmadı**.
- `navlun-lojistik-uzmani`'nın `EV-2026-08-10-304`'ü `UNKNOWN` + `14d` olarak
  ayrı işaretlemesi — **doğrulandı**; hata başkanın toplamasındaydı.

---

## Bu kararı ne çürütür?

*(Bu belge bir yatırım kararı içermez. Aşağıdaki soru bu turun **iki
hükmüne** — **"tarih ve fiyat girdileri kaydedilebilir ve TUR 2.5 bu
girdilerle anlamlı bir ters model üretebilir"** ve **"G0 `PASS` korunur"** —
ilişkindir.)*

### En güçlü tek çürütücü bulgu

> **TARGET merdiveninin en üst basamağında (999 TL) bile ters modelin
> ödenebilir azami `CIF_TRY`'yi NEGATİF veya sıfıra yakın çıkarması.**

Bu tek çıktı, bu turun **her iki hükmünü de aynı anda** çürütür:

- **Fiyat girdisi anlamsızlaşır:** Eğer merdivenin **beş basamağının beşinde
  de** ödenebilir CIF sıfıra yakınsa, hedef seçmek bir **modelleme sorunu
  değil**, bir **aritmetik imkânsızlıktır**. Merdiveni kaydetmek doğru olurdu
  ama **yetersizdi**: asıl soru *"hangi hedef?"* değil, *"herhangi bir hedef
  var mı?"* olurdu.
- **Tarih girdisi ikinci dereceden kalır:** ÖTV'nin 2027'de %0 mı %25 mi
  artacağı, katkının zaten negatif olduğu bir yapıda **karar değiştirmez**.
  `T-921`'in aciliyeti düşer, `T-912` (`fx`) ve `T-466` (fiyat) **tek
  belirleyici** hâline gelir.
- Ve bu, `00-charter/benchmark.md`'nin dayandığı **segment tanımını**
  doğrudan hedef alır: fiyat/performans segmenti Türkiye'de ithal şarap için
  **maktu ÖTV nedeniyle var olmayabilir**. 53,4519 TL/şişe (BASE_DATE) ÖTV,
  599 TL'lik bir rafta KDV sonrası tutarın **çok büyük bir yüzdesidir** ve
  fiyattan **bağımsızdır**.

**Nasıl ararız:** Bu, TUR 2.5'in **birinci çıktısı** olmalıdır — ters modelin
en üst basamaktan (`TGT_999`) aşağı doğru, `T-921` kapandıktan sonra, üç
tarih ve dört ÖTV noktasıyla çalıştırılması. **Yeni veri gerektirmez.**
`fx` bile gerekmez (`master-commercial-input-table.md` §5.3: TL zinciri
`CIF_TRY`'ye kadar `fx`siz çalışır).

### İkinci en güçlü çürütücü (farklı hükmü hedefler)

**`G0 PASS`'i test eden ilk gerçek temas.**
`G0`, **üç turdur** test edilmemiştir; `mevzuat-ruhsat-uzmani` TUR 2'de de
TUR 2.5'te de çalışmamıştır. TADAB'a yazılı bir görüş talebi veya faal bir
küçük ölçekli şarap ithalatçısıyla tek bir görüşme, `R1` veya `R3`
tetikleyicisini **aynı temasta** ateşleyebilir. `G0 PASS`, iki açık
çelişkinin (`C-252`, `C-203`) üzerinde durmaktadır ve bu turda o zemin
**hiç değişmemiştir.**

### Bu turun en tartışmalı hükmü

**`model_hedef_tarihi`'ni doldurmam.**

Karşı argüman güçlüdür: *"Bir alanı, o alanın altındaki engine denetimi
`is None`'a dayandığını **bilerek** doldurmak, kendi güvenlik ağını
kesmektir. Doğru sıra önce `T-921`'i açtırıp kapatmak, sonra tarihi
girmekti."*

**Bu itiraz ciddiye alınmalıdır ve `seytanin-avukati` TUR 4'te bunu hedef
almalıdır.**

**Savunmam üç maddedir:** (1) Girdi bir **kurucu talimatıdır**, benim
tercihim değildir ve kaydını geciktirmek onu **yok saymak** olurdu.
(2) Riski **gizlemedim** — aynı anda `T-921`'i `CRITICAL` açtım, `yaml`'ın
içine **büyük harfle uyarı** yazdım ve **P-1 kapısını** koydum. (3) Ters
sıra (`T-921` önce) **daha güvenli ama daha yavaştı** ve tazelik penceresi
**6 gündür**. Yine de: **eğer TUR 2.5'te herhangi bir ÖTV sayısı `P-1`
kapısını delip çıkarsa, bu turun kaydı bir hata olarak okunmalıdır.**

### Bu turun en kırılgan hükmü

**"TARGET merdiveni `G3`'ü açmaz" ayrımının uygulamada tutacağı.**

Kırılgan çünkü bu ayrım **tamamen disipline** dayanır — üç `yaml` kuralı
(`K7`, `L1`–`L7`, `tur25_notu`) ve bir ticket (`T-922`). Hiçbir teknik
mekanizma `finans-fizibilite`'nin ters model çıktısını *"hedef fiyat
599 TL'de ödenebilir CIF şudur"* diye yazıp, bunun bir **sonraki turda**
*"599 TL'de ödenebilir CIF şudur"* diye **hedef nitelemesi düşerek**
alıntılanmasını engellemez. **Etiket aşınması bu projedeki en sık
gözlemlenen arıza türüdür** (`599,90`'ın `K5`'e ihtiyaç duyması aynı
türdendi). Bu sefer aynı sayının **iki farklı nesne** olması, aşınmayı
**daha da olası** kılar.

### Bu turun kör noktası

Bu tur da **hiçbir yeni kanıt üretmemiştir.** Yaptığım şey iki yatırımcı
beyanını kaydetmek, statüleri güncellemek ve **kendi kayıt hatamı**
düzeltmektir. Programatik evidence taraması **yapısal** bütünlüğü ölçer;
**içerik** doğruluğunu ölçmez. 290 kartın 290'ı yerli yerinde durabilir ve
içeriklerinden bir kısmı yine de yanlış olabilir. Panzehir yine **TUR 4**'tür:
`seytanin-avukati` bu belgeyi değil, **altındaki kanıt kartlarını** hedef
almalıdır — ve bu belgeye özel olarak: **`T-921`'de tarif ettiğim arıza
zincirinin gerçekten kurulup kurulmadığını kodda kendisi doğrulamalıdır.**
