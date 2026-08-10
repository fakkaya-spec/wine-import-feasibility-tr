# TUR 2.5 KONSOLİDASYONU — TERS FİYAT MODELİ SONRASI DURUM

```yaml
belge:                  tur-25-konsolidasyon
yazan:                  yatirim-komitesi-baskani
tarih:                  2026-08-10
tur:                    TUR 2.5 KAPANIS
karar_iceriyor_mu:      false      # YATIRIM karari icermez
arastirma_yapildi_mi:   false      # CLAUDE.md §1.16
web_aramasi_yapildi_mi: false
ajan_cagrildi_mi:       false
yeni_kanit_uretildi_mi: false      # 10-evidence/ acilmadi
yeni_sayi_uretildi_mi:  false      # tek sayi baskan tarafindan tahmin edilmedi
git_calistirildi_mi:    false
karar_gunlugune_dokunuldu_mu: false
kod_calistirildi_mi:    true       # DENETIM amaciyla: test_ters_model.py (10/10 dogrulandi)
acilan_ticket:          [T-941, T-942, T-943, T-944, T-945, T-946, T-947, T-948]
kapatilan_ticket:       [T-921, T-751]
cozulen_celiski:        [C-851, C-852]
```

> ## BU BELGE BİR YATIRIM KARARI DEĞİLDİR
>
> `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` / `SCALE` kararlarının hiçbiri
> burada verilmemiştir. Nihai karar **TUR 6**'da `90-karar/karar-gunlugu.md`'de
> verilir ve **o dosyaya bu turda DOKUNULMAMIŞTIR.**
>
> Ana çıktı bu belge değil, **`90-karar/investor-decisions-required.md`**'dir.

---

## 0. TUR 2.5 NE ÜRETTİ — ÜÇ CÜMLE

1. **Ters model çalıştı ve `MAX_CIF_TRY` pozitif çıktı.** Başkanın *"999 TL'de bile ödenebilir CIF negatif veya sıfıra yakın çıkar"* hipotezi **ÇÜRÜTÜLDÜ.** Segment **aritmetik olarak imkânsız değildir.**
2. **Çıktı iki bağımsız nedenle bir ÜST SINIRDIR** (λ=1 çapası + 13 maliyet kaleminin `0` alınması) ve **hiçbir sayısı bir fiyat değildir.**
3. **Modelin en büyük iki belirsizlik ekseni bir veri eksikliği değil, bir karar eksikliğidir** — ve o kararlar `OQ-901`'de üç turdur bekliyor.

> **Bu turun en dürüst tek cümlesi `finans-fizibilite`'nindir:**
> *"`FACT`'lerin tamamı vergi ve ruhsat bacağındadır. Ticari bacakta (fiyat,
> marj, dağıtım, kur) TEK BİR `FACT` YOKTUR."*
> Modele giren 36 girdinin **11'i `FACT` (%30,6)**, **11'i `UNKNOWN` (%30,6)**.

---

# §1 — GATE DURUM TABLOSU (TUR 2.5 SONRASI)

| Gate | Soru | Sahibi | **Durum** | TUR 2.5'te değişim | Açan tek koşul |
|---|---|---|---|---|---|
| **G0** Yasal yol | Türkiye'de yasal olarak kurulabilir mi? | `mevzuat-ruhsat-uzmani` önerir → **başkan karar verir** | **`PASS`** *(korunuyor — §1.1)* | **değişmedi ve YİNE TEST EDİLMEDİ** | — *(izleme: R1/R2/R3)* |
| **G1** Vergi yapısı | Vergi yükü kanıtlı ve satır satır hesaplanabilir mi? | `gumruk-vergi-uzmani` | **`BLOCKED`** | ⬆ **iki ayağı ilerledi:** `T-921` ve `T-751` kapandı; matrah sırası 10/10 birim testle doğrulandı. ⬇ **bir ayağı kötüleşti:** `T-947` (KDV indirim hakkı, **CRITICAL**) açıldı | `T-104` 2. ayağı (`I-3`) + **`T-947`** + gözetim eşiği |
| **G2** Tedarik | Gerçek, ulaşılabilir tedarik kaynağı var mı? | `global-sourcing-kasifi` | **`BLOCKED`** | **değişmedi** | Gerçek RFQ (≥5 tedarikçi) — **masabaşıyla açılamaz**, `I-4` izni gerekir |
| **G2-L** Lojistik / landed | `L1 → L2 → L3` kurulabiliyor mu? | `navlun-lojistik-uzmani` | **`BLOCKED`** | ⚠ **tazelik saati işliyor** — 10 LCL kartına **6 gün** kaldı. Yeni bulgu: `C-311`'in **ters model üzerindeki etkisi SIFIRDIR** (navlun CIF'in içindedir) → `T-304`'ün yeri netleşti: **ileri model + FOB pazarlığı** blokeri | `T-304` (3 forwarder yazılı FCL kotasyonu) |
| **G3** Pazar | Benchmark doğrulandı mı, segment gerçek mi? | `turkiye-pazar-kasifi` | **`BLOCKED`** | **değişmedi.** TARGET merdiveni `G3`'ü **AÇMAZ** (`K7`, `L4`); `T-859` ile **yeni bir boşluk** kayda geçti: hedefin hangi `L8` alt katmanı olduğu `UNKNOWN` | **`OQ-001` promosyon ayağı (`T-504`)** + `l8_chain_retail` (`T-603`/`T-917`) |
| **G4** Ekonomi | Model kanıtlı girdilerle pozitif contribution veriyor mu? | `finans-fizibilite` | **`NOT_EVALUATED`** | **değişmedi** — contribution margin **hesaplanmadı** (kapsam dışıydı) | G1 + G2 + G2-L + G3 + **`D-01`/`D-02`** |
| **G4-T** *(alt-durum, YENİ)* Ters model | `L8 → CIF_TRY` zinciri kurulabiliyor mu? | `finans-fizibilite` | **`DRAFT_DEMONSTRATED`** | ➕ **YENİ.** Zincir uçtan uca koştu, R8 round-trip 2.700/2.700 tuttu, 10/10 birim test geçti. **Bu bir gate PASS'i DEĞİLDİR** — çıktı `DRAFT` + `UPPER_BOUND`'dur ve `G4`'ü açmaz | `T-942` (kanal bacağı doğrulaması) + `I-1` (fx) |
| **G4-K** *(alt-durum)* Kanal | `L6 → L7 → L8` sayısal kurulabiliyor mu? | `kanal-marj-uzmani` | **`BLOCKED`** | ⬇ **kötüleşti** — `R5` düzeltmesinden sonra kanal marjı **tornadonun 3. büyük ekseni** oldu (−45,06/+32,00 TL) ve **bandın tamamı `ASSUMPTION`**'dır. Ayrıca `T-856`: `d` tekelde `0` alındığı için tekel tavanı **%11,4 yapay olarak yüksek** | `T-603` + `T-604` + `T-601` + **`T-856`** |
| **G5** Risk | Kırmızı takımın `CRITICAL`'ları kapandı mı? | `seytanin-avukati` | **`NOT_EVALUATED`** | değişmedi | TUR 4 |

> ### BU TURDA HİÇBİR GATE AÇILMAMIŞTIR.
> `G1`'in iki ayağı ilerledi ama gate açılmadı; `G4-T` yeni bir **alt-durumdur**,
> bir gate değildir ve `G4`'ü açmaz.

## 1.1 `G0 = PASS` korunuyor mu? — üç tetikleyici

`G0 PASS` **geri alınabilir** bir gate'tir. Üç geri alma tetikleyicisi
(`tur-2-preflight-housekeeping.md` §D.2) yeniden tarandı:

| # | Tetikleyici | Gerçekleşti mi | Dayanak |
|---|---|---|---|
| **R1** | `C-252` **B okuması lehine** kapanır **VE** halef merci tespit edilir *(İKİSİ BİRDEN)* | **HAYIR** | `mevzuat-ruhsat-uzmani` bu turda da **çağrılmadı**; `C-252` `OPEN`/LOW; `EV-2026-08-10-214` hâlâ `UNKNOWN` |
| **R2** | 7584 s.K. m.2'nin ürünün **rafta bulundurulmasını** kapsadığı bağlayıcı bir metinle ortaya çıkar | **HAYIR** | Yeni bağlayıcı metin yok; `C-203` `ACCEPTED BUSINESS CONSTRAINT` |
| **R3** | `C-202` sıralama döngüsünün **fiilen kilitlendiği** kanıtlanır | **HAYIR** | Yeni kanıt yok; `C-202` `OPEN` (HIGH) |

### **`G0` → `PASS` KORUNUR — ama bu turda da TEST EDİLMEDİ.**

> **Kayıt (dördüncü kez):** `mevzuat-ruhsat-uzmani` **dört turdur** (`TUR 2`,
> `TUR 2.5` pre-flight, `TUR 2.5`, bu konsolidasyon) `G0` kapsamında
> çalışmamıştır. `G0 PASS` hâlâ **iki açık çelişkinin (`C-252`, `C-203`)
> üzerinde durmaktadır** ve TUR 6'da **kararın dayandığı EN ESKİ doğrulama**
> olacaktır. Bu, orada açıkça yazılacaktır.
>
> Yaptığım şey yine yalnızca *"tetikleyiciler gerçekleşmedi"* doğrulamasıdır —
> ve bu, **"yeni olumsuz kanıt aranmadı"** ile aynı şeydir.

---

# §2 — AÇIK `CRITICAL` TICKET'LAR VE NEYİ BLOKE ETTİKLERİ

## 2.1 Bu turda kapatılanlar

| ticket | önce | **sonra** | Gerekçe — **başkan tarafından bağımsız doğrulandı** |
|---|---|---|---|
| **`T-921`** | `ANSWERED` (CRITICAL) | **`RESOLVED`** | 5 kabul kriterinin 5'i karşılandı. **Ben kodu okudum ve testi kendim koşturdum.** `otv_zaman_serisi.py` (YENİ) `effective_date <= t` seçimini, **ufuk denetimini**, `engine_yasak`'ı ve `model_hedef_tarihi_status != FACT` etiketlemesini uyguluyor. `TV-9`/`TV-10`: bayraksız çağrı **`UNKNOWN` dönüyor**, bayraklı çağrı `UPPER_BOUND` + `O-2/O-3/O-5/O-6` etiketleriyle dönüyor. **2027 ÖTV tutarı hiçbir çıktıda yazılmamıştır.** |
| **`T-751`** | `ANSWERED` (CRITICAL) | **`RESOLVED`** | `python3 80-model/engine/test_ters_model.py` → **10/10 GEÇTİ** *(başkan tarafından koşturuldu, çıktı görüldü)*. `R7-K1…K6` kurallarının hepsi test vektörleriyle kapsanıyor; `TV-6`/`TV-7` **R8'in yanlış cevabı reddettiğini** gösteriyor. Beklenen değerler koda gömülü değil, `vergi.yaml`'dan okunuyor. |

**Yeniden açılma tetikleyicileri (bağlayıcı):**
- `T-921` — herhangi bir çıktıda `otv_senaryo` bayrağı **olmadan** bir ÖTV sayısı basılırsa, veya `matrah_sirasi[sira=4].asgari_maktu_tutar` doğrudan okunursa **otomatik yeniden açılır.**
- `T-751` — `vergi.yaml → ters_model_vergi_bacagi` spesifikasyonu değişirse **otomatik yeniden açılır**; `T-941` (R5 başlık düzeltmesi) bu kapsamdadır.

> ⚠ **`P-1` kapısı KALDIRILMIYOR.** `T-921` kapandı ama kapı **yürürlükte
> kalır**: engine seriyi okumadan basılan her ÖTV değeri geçersizdir. Kapı
> artık bir *blocker* değil, bir *regression guard*'dır.

## 2.2 Açık `CRITICAL` ticket listesi — **10**

| # | ticket | status | hedef ajan | **Neyi bloke ediyor** | TUR 2.5'te değişti mi |
|---|---|---|---|---|---|
| 1 | **`T-104`** | `ANSWERED` | `finans-fizibilite` | **G1, G4** — ÖTV modelde sabit sayı olamaz. **Birinci ayağı (`T-921`) KAPANDI**; ikinci ayağı (Yİ-ÜFE `ASSUMPTION` ekseni, `I-3`) **AÇIK** → tüm parasal çıktı `UPPER_BOUND` kalıyor | ⬆ **kısmen ilerledi** |
| 2 | **`T-301`** | `OPEN` | `mevzuat-ruhsat-uzmani` | **G2-L, G4** — antrepo/gümrük zorunlu bekleme süresi. `MAX_CIF`'te **`0` alınan 13 kalemden biri**; ayrıca `D-08` (stok gün eşiği) **alt sınırını bile bilinmez kılıyor** ve `peak_cash`'in zaman eksenini kırıyor | **hayır** — ajan çağrılmadı |
| 3 | **`T-304`** | `OPEN` | `yatirim-komitesi-baskani` | **G2-L** — hiçbir rotada doğrulanmış FCL navlunu yok (`C-311`, 4–5 kat band). ⚠ **YENİ TESPİT: ters model üzerindeki etkisi SIFIRDIR** (navlun CIF'in içindedir) → bloke ettiği şey **ileri model ve FOB pazarlığıdır** | ⬇ **kapsamı daraldı, aciliyeti yer değiştirdi** |
| 4 | **`T-466`** | `OPEN` | `finans-fizibilite` | **G2, G4** — gerçek EXW/FOB yok; `exw`/`fob` `null` kalmalı. Ters model tavanı **kimseye teklif edilemez** | **hayır** |
| 5 | **`T-601`** | `OPEN` | `mevzuat-ruhsat-uzmani` | **G4-K** — şarap 6585 m.7/3 anlamında *"tarım ve gıda ürünü"* mü? **Yasal vade tavanını** belirler → `D-13`, `peak_cash`, `C-601` | **hayır** — ajan çağrılmadı |
| 6 | **`T-912`** | `OPEN` | `finans-fizibilite` | **G4 + her parasal çıktı** — `fx` `null`. **`T-852` bunun hedefini düzeltmiştir** (bkz. #7); ikisi aynı boşluğun iki ucudur | **hayır** *(üçüncü tur)* |
| 7 | **`T-851`** | `OPEN` | `yatirim-komitesi-baskani` | **G4 + TUR 6** — `TARGET`/`ACCEPTABLE`/`WALK-AWAY` üretilemiyor. **Bu turda `investor-decisions-required.md` ile GÖRÜNÜR HÂLE GETİRİLDİ**, ama kapanışı yalnızca yatırımcı yapabilir | ➕ **belgelendi, kapanmadı** |
| 8 | **`T-852`** | `OPEN` | `yatirim-komitesi-baskani` | **`MAX_FOB` / `MAX_EXW` + ülke ayrıştırması** — `fx` bir **yatırımcı girdisidir**, `finans-fizibilite`'nin araştırabileceği bir şey değil. **Hedef düzeltmesi KABUL EDİLDİ** (§3.4) | ➕ **hedefi kabul edildi** |
| 9 | **`T-942`** | `OPEN` | `finans-fizibilite` | **G4-T** — **YENİ.** Kanal bacağı (`R1`–`R5`) için **hiçbir otomatik doğrulama yoktur**; `R8` yalnız `R6`–`R7`'yi doğruluyor. `−28,95 TL/şişe`'lik `R5` hatası **2.700/2.700 satırdan temiz geçti** | ➕ **YENİ** |
| 10 | **`T-947`** | `OPEN` | `gumruk-vergi-uzmani` | **G1 + ters modelin TÜM sayıları** — **YENİ.** KDVK md.36 uyarınca alkolde KDV indirim hakkını kısıtlayan bir CB Kararı **hiç aranmamıştır** (`T-151`, `OQ-G10`). Varsa **tüm tavanlar ~%22,7 düşer** | ➕ **YENİ** |

**+ `OQ-901` (CRITICAL, sahibi: yatırımcı)** — hiçbir ajan kapatamaz;
**TUR 6'da nihai kararı bloke eder.** Bu turda `investor-decisions-required.md`
ile **6 eşikten 16 eşiğe + 8 eşik dışı girdiye** genişletilerek belgelendi.

### Sayım

```
TUR 2.5 oncesi acik CRITICAL : 10   (T-104, T-301, T-304, T-466, T-601,
                                     T-751, T-912, T-921, T-851, T-852)
kapatilan                    : -2   (T-921, T-751)
acilan                       : +2   (T-942, T-947)
-------------------------------------------------------------
TUR 2.5 sonrasi acik CRITICAL: 10
```

> **CLAUDE.md §5 yürürlüktedir:** bunlar açıkken `finans-fizibilite` çıktısı
> **`APPROVED` olamaz — en fazla `DRAFT`.**
> `reverse-price-model.md`, `sweet-spot-analizi.md` ve
> `country-buying-ceilings.csv` **`DRAFT`**'tır ve öyle kalır.

## 2.3 `T-851` ve `T-852` ne getiriyor — net cevap

| | **`T-851`** | **`T-852`** |
|---|---|---|
| **Ne** | Yatırımcı eşiği yokluğunda `TARGET`/`ACCEPTABLE`/`WALK-AWAY` fiyatlarının **üretilmediğinin** kaydı | `fx`'in bir **yatırımcı girdisi** olduğunun ve `T-912`'nin hedefinin yanlış ajanı gösterdiğinin kaydı |
| **Ajan doğru mu davrandı** | ✅ **EVET.** Keyfî yüzdelerle üç fiyat üretmek *"modelin en sinsi uydurma noktası"* olurdu. Ajan üretmedi ve **neden üretmediğini yazdı.** Bu, CLAUDE.md §1.15'in tam olarak istediği davranıştır | ✅ **EVET.** Ajan izolasyonu doğru uygulanmıştır: araştırma aracı olmayan bir ajana araştırma ticket'ı açmak hatalıydı — **hata bendedir**, `T-912`'yi ben açmıştım |
| **Bu turda ne yaptım** | `investor-decisions-required.md` yazıldı; `T-851`'in sorduğu üç alan `D-03` altında **matrah sorusuyla birlikte** genişletildi | **Hedef düzeltmesi KABUL EDİLDİ.** `T-912` kapatılmıyor *(boşluk duruyor)* ama **artık `T-852` ile birlikte okunur**: `T-912` boşluğu, `T-852` sahipliği tarif eder |
| **Kapanışı** | Yalnızca **yatırımcı** | Yalnızca **yatırımcı/başkan** — tarihli tek bir kur kaydı + bant |

> **`T-852`'nin sessiz kalan bulgusu:** `fx` bir birim dönüşümü değildir.
> Ters modelde **9 ülke için 2 sayı** vardır; ülkeler arası gerçek ayrışma
> **FOB seviyesinde** doğar. **`fx`, modelin ülke ayrıştırma gücünün ön
> koşuludur.** Yani `T-852` kapanmadan *"hangi ülkeden alalım"* sorusu
> **modelden okunamaz** — bugün okunuyor gibi görünen sıralama
> (`ES · MD · CL · PT · IT`) modelin değil, **gözlenen CIF birim
> değerlerinin** sıralamasıdır ve ajanın kendisi bunu belirtmiştir.

---

# §3 — **`R5` HATASININ DENETİMİ** *(GÖREV 3)*

> `finans-fizibilite` bu turda **kendi kodundaki bir hatayı kendisi buldu,
> düzeltti, büyüklüğünü ölçtü ve raporladı.** Bu, denetlenmesi gereken bir
> olaydır — çünkü hem düzeltmenin doğruluğu hem de **hatanın nasıl mümkün
> olduğu** karar açısından bilgi taşır.

## 3.1 Düzeltme doğru mu? — **EVET, KABUL EDİLİYOR**

```
NAIF (YANLIS):   L5_max = L6 x (1 - mu)
DOGRU:           L5_max = L7_eff - mu x L6          [ters_model.py:392]
```

| Kontrol | Sonuç |
|---|---|
| **Kanıt dayanağı** | `EV-2026-08-10-612` — Rekabet Kurulu 21-51/708-351 para.82: alkollü içkide zincirlerle imzalanan yıllık anlaşmalarda CRM, B2B, alan kullanımı, kırık ürün, lojistik ve soğutucu enerji bedelleri **"müşteriye ödenecek bedeller"**dir. **Bunları ödeyen ithalatçıdır.** ✅ |
| **İç tutarlılık** | Spesifikasyonun kendi `R2`–`R4` tanımı zaten `L7_eff = L8_net(1−m)` ve `L6 = (L7_eff + f)/(1−d)` demektedir. Buradan `L6(1−d) − f = L7_eff` özdeşliği çıkar — yani **ithalatçının fiilî net hasılatı `L7_eff`'tir**, `L6` değil. ✅ |
| **Kodda uygulandı mı** | `ters_model.py:392` → `s.l5_max = l7 - importer_katki_orani * l6`. ✅ **Başkan tarafından kodda görüldü.** |
| **Büyüklük aritmetiği** | `542,7989 − 499,3750 = 43,4239` → `/1,50 = 28,949` TL/şişe. ✅ Rapordaki **−28,95** ile tutarlı. |
| **Yön** | Hata **tavanı yükseltiyordu** → düzeltme **muhafazakâr yöndedir.** ✅ |
| **Yan doğrulama** | Düzeltmeden önce `CHAIN_RETAIL` ve `INDEPENDENT_TEKEL` tavanları **neredeyse özdeşti (<%1)**; sonra **%11,4 ayrıştılar.** Bu, düzeltmenin doğru olduğunun bağımsız bir belirtisidir. ✅ |

> **KARAR: `R5` düzeltmesi kabul edilir.** Ajanın kendi hatasını bulup
> **projenin aleyhine** raporlaması, bu turun en güvenilirlik artırıcı tek
> davranışıdır ve kayda geçirilir.
>
> ⚠ **Ama bir bağımsız denetim gereklidir ve ajan bunu kendisi istemiştir**
> (`rapor-tur25-finans.md` §9.5 #6): `d`'nin **gerçekten ithalatçının
> maliyeti** olup olmadığı `seytanin-avukati` tarafından `EV-2026-08-10-612`
> okunarak teyit edilmelidir → **`T-946`** (bu turda açıldı).
> *Düzeltme yanlışsa tavanlar %10,6 yükselir ve tekel/zincir karşılaştırması değişir.*

## 3.2 `gumruk-vergi-uzmani`'nın spesifikasyonunda boşluk var mı? — **EVET, ÜÇ TANE**

### Boşluk 1 — `R5`'in başlığı **yanlış girdi katmanını gösteriyor** → `T-941`

`30-vergi-gumruk/ters-model-vergi-bacagi.md` §3:

```
### R5 — L6 → L5_max · VERGI BACAGI DEGIL (finans-fizibilite)
Ithalatcinin hedef katki payi dusulur. Vergi etkisi yok.
```

| Gözlem | Değerlendirme |
|---|---|
| Başlıktaki ok **`L6 → L5_max`**'tir | **Yanlıştır.** Doğru girdi `L7_eff`'tir; `L6` yalnızca **katkı payının matrahı** olarak kullanılır. Başlık, okuyucuyu **tam olarak naif formüle davet eder**: *"L6'dan başla, katkı payını düş."* |
| Gövde iki cümledir ve **formül içermez** | Spesifikasyonun geri kalanı (`R1`, `R2`–`R4`, `R6`, `R7`, `R8`, `R9`) **kapalı formüllerle** yazılmıştır. `R5` **tek istisnadır** ve tek hata da orada çıkmıştır. |
| *"VERGİ BACAĞI DEĞİL"* nitelemesi | ✅ **Doğrudur** ve ajan izolasyonuna uygundur. Ama bir adımı **devretmek**, o adımın **girdi katmanını yanlış etiketlemeyi** mazur göstermez. Katman etiketleri CLAUDE.md §6 kapsamındadır ve **her ajanı bağlar.** |

> **Değerlendirme:** Bu bir **hata değil, bir boşluktur** — ve boşluğun bedeli
> ölçülmüştür: **28,95 TL/şişe.** `gumruk-vergi-uzmani`'nın **bulgusu
> reddedilmiyor**; yalnızca `R5` satırının başlığı düzeltilmeli ve
> `R5`'in girdisinin `L7_eff` olduğu, `L6`'nın **yalnızca matrah** olduğu
> yazılmalıdır → **`T-941` (HIGH)**.

### Boşluk 2 — `R8` **yalnızca vergi bacağını** doğruluyor → `T-942`

```python
# ters_model.py:478-487
geri = ileri_model(cif_try_max, ...)
s.r8_roundtrip_fark = abs(geri - s.l4_econ_max)      # L4_econ_max <-> CIF
```

| Gözlem | Değerlendirme |
|---|---|
| Spesifikasyon der ki: *"Bu tek satır, §6'daki **beş hatanın beşini de** yakalar."* | ✅ **Doğrudur** — ama §6'daki beş hata (`H1`–`H5`) **hepsi vergi bacağındadır** (`R6`/`R7`/`R9`). İfade **kendi kapsamı içinde doğrudur.** |
| **Ama proje bunu daha geniş okudu** | `R8`'in *"her şeyi yakalayan tek satır"* olduğu izlenimi doğdu. **`R5` hatası 2.700 satırın 2.700'ünde `R8`'den temiz geçti** — çünkü `R8` `L4_econ_max`'ı **veri olarak alır** ve onun nasıl hesaplandığını sorgulamaz. |
| **Yapısal sonuç** | Zincirin **8 adımından yalnızca 2'si** (`R6`→`R7`) otomatik doğrulanıyor. `R1`–`R5` (KDV bölmesi, kanal marjı, `d`, `f`, katkı payı) **hiçbir assertion tarafından korunmuyor** — ve tornadonun **en büyük dört ekseninin üçü** tam olarak orada. |

> **Değerlendirme:** Bu, spesifikasyonun değil, **modelin doğrulama
> mimarisinin** boşluğudur. Gereken: `R8`'in kanal karşılığı olan bir
> **`R8-K` round-trip assertion**'ı — verilen `L5_max`, `μ`, `d`, `f`,
> `m_retail`'den `L8` yeniden inşa edilmeli ve hedefle karşılaştırılmalıdır.
> Bu assertion **`R5` hatasını ilk çalıştırmada yakalardı.** → **`T-942`
> (CRITICAL)**

### Boşluk 3 — Kanal bacağı için **"en muhtemel hatalar" listesi hiç yazılmamış** → `T-943`

`ters-model-vergi-bacagi.md` §6 vergi bacağı için **`H1`–`H6`** listesini
verir ve her birinin **TL bedelini** hesaplar. **Kanal bacağı için böyle bir
liste yoktur.** `kanal-marj-uzmani` `marj-vs-markup.md`'de margin↔markup
karışıklığını işlemiştir — ama bu **tek bir hata türüdür**.

Yazılmamış listenin en az beş adayı, bu turda **fiilen gözlenmiştir**:

| # | Aday hata | Bu turda gözlendi mi |
|---|---|---|
| K1 | `L6`'yı ithalatçının net hasılatı sanmak (`d`, `f` düşülmeden) | ✅ **OLDU — `R5`, 28,95 TL** |
| K2 | margin ↔ markup karışıklığı | ❌ olmadı *(§5.1'de tablolandı)* |
| K3 | `d`'yi `UNKNOWN` olduğu için `0` almanın **kanallar arası karşılaştırmayı** bozması | ✅ **OLDU — tekel tavanı %11,4 yapay yüksek (`T-856`)** |
| K4 | HoReCa çarpanının **yanlış katmana** uygulanması | ❌ olmadı *(doğrulandı: `L7 → L8_HORECA`)* |
| K5 | Katkı payı matrahının (`L6`/`L7_eff`/`L5`) tanımsız bırakılması | ✅ **OLUYOR — `T-944`** |

> **Değerlendirme:** Kanal bacağı, vergi bacağının aldığı **spesifikasyon
> disiplininin hiçbirini almamıştır** — ne kapalı formül seti, ne hata
> listesi, ne birim test vektörü. Ve tornadonun **en büyük eksenleri
> oradadır.** → **`T-943` (HIGH, `kanal-marj-uzmani`)**

## 3.3 Benzer başka boşluk olabilir mi? — **DESEN TESPİT EDİLDİ**

**Üç bağımsız olayın ortak yapısı:**

| Olay | Katman geçişi | Boşluğun türü | Büyüklük |
|---|---|---|---|
| **`R5` hatası** | `L6 ↔ L7_eff ↔ L5` | Kalemin **kimin maliyeti** olduğu belirsiz (`d`, `f`) | **−28,95 TL/şişe** |
| **`C-851`** | `L2 ↔ L3 ↔ L5` | Kalemin **hangi katmanda** düşüleceği belirsiz | ±5,32 TL/şişe |
| **`C-852`** | `L2 ↔ L5` | Kalemin **hangi para biriminde** olduğu gözden kaçmış (USD kalemler `0` alındı) | `UNKNOWN`, tek yönlü **yukarı** |

> ### DESEN
> **Her katman sınırında, kalemin bir NİTELİĞİ (ödeyeni / katmanı / para
> birimi) belirsiz bırakıldığında, model o kalemi SESSİZCE ATLAR ve tavan
> YUKARI sapar.**
>
> Üç olayın **üçünde de** sapma yönü aynıdır: **projenin lehine.**
> Bu, `finans-fizibilite`'nin kendi kaydettiği *"13 maliyet kaleminin 13'ü de
> `0` alındı ve 13'ü de aynı yönde saptırır"* gözlemiyle **aynı desendir.**
> **Dört bağımsız iyimserlik kaynağı, aynı modelde, aynı yönde.**

### Bu desene göre **taranmamış** kalan katman sınırları

| Sınır | Belirsiz nitelik | Ticket |
|---|---|---|
| `L4_econ ↔ L5` — TR-içi lojistik kalemlerinin **rota bağımsızlığı** | Tablo İspanya→İstanbul için üretildi, **9 ülkeye uygulandı** | `T-854` (HIGH, açık) |
| `L5` — bandrol/TADAB/ruhsat kalemlerinin **tarih geçerliliği** | Hepsi Yİ-ÜFE endeksli, **hedef tarihlerin üçü de 2027'de** → modelde 2026 değerleri kullanıldı. ÖTV için `T-921` ile kod düzeyinde korundu; **bunlar için koruma YOK** | `T-858` (HIGH, açık) |
| `L5` — μ'nün **matrahı** | `L6` alındı, gerekçelendirilmedi, **μ=0 olduğu için hiç test edilmedi** | **`T-944` (YENİ)** |
| `L8` — hedefin **hangi alt katman** olduğu | `L8_CHAIN_RETAIL` / `L8_METRO_CASH_CARRY` / `L8_ONLINE` ayrımı yapılmadı | `T-859` (HIGH, açık) |
| `L2` — **gözetim eşiği** (alt sınır) | Tavan bir **alt sınırla hiç test edilmedi**; eşik `null`/`UNKNOWN` | `EV-2026-08-09-125` yeniden aranmalı |

> **Bu tabloda `T-941`…`T-944` dışında yeni ticket açmıyorum** — dördü de
> zaten açık ve hedef ajanları doğru. **Yaptığım tek şey, bunların
> birbirinden bağımsız hijyen sorunları değil, AYNI DESENİN örnekleri
> olduğunu kayda geçirmektir.** `seytanin-avukati` TUR 4'te bu desenden
> başlamalıdır.

## 3.4 Bir kayıt tutarsızlığı — bloke etmiyor

`reverse-price-model.md` §2.2 farkı **`−28,95 TL (−%9,6)`** olarak,
`rapor-tur25-finans.md` §1 ise **`+28,95 TL fazla tavan (%+10,6)`** olarak
yazmaktadır. **İkisi de aritmetik olarak doğrudur** *(paydalar farklıdır:
301,78 vs 272,83)* ama **aynı belgede iki farklı işaret ve iki farklı yüzde**
görünmesi, tam da bu projenin en çok korktuğu **etiket aşınmasına** açık bir
kapıdır. Bir sonraki alıntıda hangisinin taşınacağı belirsizdir.
**Bir ticket açmaya değmez; ajanın gelecek raporlarında tek gösterim
kullanması istenir** *(`T-942` içine not olarak eklendi)*.

---

# §4 — ÇELİŞKİLER

## 4.1 `C-851` — **RESOLVED — TANIM** *(başkan çözümü)*

**Çelişki:** `CLAUDE.md` §6 → `L3 PRE-TAX LANDED = CIF + vergi öncesi yurt içi
masraflar` ↔ `ters-model-vergi-bacagi.md` §4.3 + `R6` → aynı kalemler
(**ordino, antrepo, elleçleme, iç nakliye, müşavirlik**) **`L5` kalemidir** ve
`L4 → L5` geçişinde düşülür.

### Çözüm gerekçesi (Kural 5 — **KATMAN/TANIM**, sahte çelişki)

1. **`CLAUDE.md` §6 bir MALİYET KATMANI TAKSONOMİSİDİR, bir ÇIKARMA SIRASI DEĞİLDİR.** §6'nın başlığı *"MALİYET KATMANLARI (KARIŞTIRILAMAZ)"*tır ve tek talebi şudur: *"Bir katmandan diğerine geçiş açıkça gösterilir (hangi kalem eklendi/çıktı)."* **Bir kalemin hangi adımda düşüleceğini §6 belirlemez.**
2. **Ters model spesifikasyonu §6'yı ihlal etmiyor, ONU UYGULUYOR.** `L3` katmanı ortadan kalkmıyor; `L3 = CIF + o kalemler` özdeşliği **korunuyor** ve `reverse-price-model.md` `L3`'ü **bilgi amaçlı türev alan** olarak raporluyor.
3. **Fiilî davranış zaten doğrudur:** kalemler `R6`'da **tam bir kez** düşülmüştür. Çift sayım **olmamıştır**, hiç saymama da **olmamıştır**.
4. Ajanın davranışı doğrudur: sessiz seçim yapmamış, iki tanımı da göstermiş, hangisini esas aldığını yazmıştır.

### **BAĞLAYICI OKUMA KURALI (`L3-K`)**

> `L3 PRE-TAX LANDED`, ters modelde **bilgi amaçlı bir türev katmandır.**
> `L2 → L3` artışını oluşturan kalemler, `L4 → L5` geçişinde **ikinci kez
> düşülemez.** Her kalem zincirde **tam bir kez** düşülür ve hangi adımda
> düşüldüğü **`ters_model_vergi_bacagi.adimlar`'da yazılıdır.**
> `l3_pre_tax_landed_max` hiçbir çıkarma işleminde kullanılamaz.

**`CLAUDE.md` DEĞİŞTİRİLMEMİŞTİR.** Bu kural §6'ya bir **niteleme** ekler,
onunla çelişmez. Kuralın `30-vergi-gumruk/matrah-sirasi.md`'ye de yazılması
CLAUDE.md §1.8 gereğidir → **`T-945` (MEDIUM)**.

**Durum:** `C-851` → **`RESOLVED — TANIM`**
**Yeniden açılma:** `L3`'ü bir çıkarma işleminde kullanan bir model çıktısı
görülürse **otomatik olarak yeniden açılır.**

## 4.2 `C-852` — **RESOLVED — TANIM (NİTELEME)** *(başkan çözümü — kendi hükmümün düzeltilmesi)*

**Çelişki:** `90-karar/master-commercial-input-table.md` §5.3 → *"`fx` olmadan
bile ters model **`CIF_TRY`'ye kadar** çalışır"* ↔ `L2`–`L5` arasındaki
**USD cinsli varış masrafları** (THD, devanning, CFS, ardiye, drop-off, LCL
varış sabit masrafı, dokümantasyon, müşavirlik CIF kademesi) `fx` `null` iken
**düşülemez.**

### Çözüm gerekçesi

1. **`finans-fizibilite` haklıdır.** §5.3'ün türetmesi, `L5 → L4` geçişindeki kalemlerin **hepsinin TL cinsinden olduğunu** varsayar. Gerçekte varış tarafı masraflarının büyük kısmı **USD** cinsindendir (`EV-2026-08-10-315`…`-319`, `EV-2026-08-09-324`).
2. **Bu hüküm bana aittir** — `master-commercial-input-table.md` bir başkan belgesidir. **Bir ajanın bulgusunu reddetmiyorum; kendi hükmümü düzeltiyorum.**
3. Düşülemeyen kalemlerin **hepsi pozitiftir** → `0` alınmaları tavanı **yükseltir** → hesaplanan şey `CIF_TRY` değil, onun bir **üst sınırıdır.**

### **DÜZELTİLMİŞ HÜKÜM (bağlayıcı)**

> ~~*"`fx` olmadan ters model `CIF_TRY`'ye kadar çalışır."*~~
> **→ *"`fx` olmadan ters model `CIF_TRY`'nin bir ÜST SINIRINA
> (`cif_try_max_UPPER_BOUND`) kadar çalışır. `L2` ile `L5` arasındaki döviz
> cinsli kalemler düşülemediği için gerçek tavan bundan DÜŞÜKTÜR."***

**Eski metin silinmemiştir**; `master-commercial-input-table.md` §5.3'e
niteleme kutusu eklenmiştir (§6.3).

**Ajanın çıktı adlandırması doğrudur ve onaylanır:**
`cif_try_max_UPPER_BOUND` (`cif_try_max` **değil**).

**Durum:** `C-852` → **`RESOLVED — TANIM`**
**Kalan iş bir çelişki değil, bir veri eksikliğidir:** `T-852` (`fx`) kapandığı
anda üst sınır gerçek bir tavana döner.

## 4.3 TUR 2'den devreden çelişkiler — durum

| id | impact | Durum | TUR 2.5'te değişti mi |
|---|---|---|---|
| **`C-311`** FCL bandı 4–5 kat | **CRITICAL** | `OPEN` | ⚠ **KAPSAMI DARALDI:** ters model üzerindeki etkisi **SIFIRDIR** (navlun CIF'in içindedir). **İleri model ve FOB pazarlığı için blokerliği aynen sürüyor.** Band **daralmadı** |
| **`C-601`** vade 60 ↔ ~93 gün | HIGH | `OPEN` | Değişmedi. `peak_cash` hesaplanmadığı için bu turda **etkisiz**; `D-13` ve TUR 3B'de **belirleyici** |
| **`C-501`** stokta olan/olmayan 10 kat fark | HIGH | `OPEN` | Değişmedi. Sweet-spot §2 alıntısının **tabanı**; modelin sayılarını değiştirmez |
| **`C-551`** Metro KDV sunumu | HIGH | `OPEN` | Değişmedi. `OBSERVED_BENCHMARK` **hiç kullanılmadı** → bu turda **etkisiz** |
| **`C-602`** tekel/HoReCa marjı | HIGH | `RESOLVED — SAHTE ÇELİŞKİ` *(TUR 2)* | ⚠ **Ama boşluk duruyor:** `m_tekel` bandının hiçbir noktasının kanıtı yok ve `T-856`'nın tabanı bu |
| **`C-202`** sıralama döngüsü | HIGH | `OPEN` | Değişmedi. `G0` izleme listesinde `R3` |
| **`C-252`** · **`C-203`** | LOW / CONSTRAINT | `OPEN` / `ACCEPTED` | Değişmedi. **`G0 PASS` bu ikisinin üzerinde duruyor** |
| **`C-301`**, `C-313`, `C-204`, `C-251`, `C-502` | MEDIUM/LOW | `OPEN` | Değişmedi |

## 4.4 Çözülemeyen ve karara taşınacaklar

| id | Neden çözülemedi | Kim/ne kapatır |
|---|---|---|
| **`C-311`** | T4 kaynak tarihsiz ve *"from"* fiyatı; masabaşında çözülemez. **İki turdur denendi** | `T-304` — 3 forwarder yazılı FCL kotasyonu (**`I-4` izni gerekir**) |
| **`C-601`** | Çekirdeği bir **hukuki nitelemedir**; başkan kendi yorumuyla kapatamaz (CLAUDE.md §1.16) | `T-601` (CRITICAL) |
| **`C-501`** / **`C-551`** | T4↔T4, aynı feed, aynı tarih; hiçbir çözüm kuralı uygulanamıyor | **`T-917`** — tek fiziksel mağaza turu |
| **`C-202`** / **`C-252`** / **`C-203`** | T1↔T1 hukuki yorum; var olmayan ikincil düzenlemeyi okumak gerekiyor | TADAB yazılı görüşü / hukuk mütalaası |

> **Değişmeyen gözlem, üçüncü kez:** **Tek bir fiziksel eylem — bir mağaza
> turu — `C-501`, `C-551`, `T-504`, `T-603` ve `OQ-001`'in kalan iki ayağını
> AYNI ANDA kapatır** (`T-917`). Projedeki **en yüksek bilgi/maliyet oranına
> sahip eylem** olmaya devam ediyor ve **üç turdur yapılmadı.**

---

# §5 — `P-1` / `P-2` / `P-3` KAPILARININ DURUMU

| Kapı | Talep | **Durum** | Doğrulama |
|---|---|---|---|
| **`P-1`** | `T-921` kapanmadan **hiçbir ÖTV sayısı üretilemez**; engine seriyi okumadan basılan her ÖTV değeri geçersizdir | ✅ **SAĞLANDI** | `T-921` **modelin ilk işi** olarak kapatıldı (`reverse-price-model.md` §1). Bayraksız çağrı `UNKNOWN` dönüyor (`TV-9`, `TV-10`, `hesap.py` çıktısı). Üretilen ÖTV değeri (53,4519) **`UPPER_BOUND` + `O-2/O-3/O-5/O-6`** etiketli. **2027 ÖTV tutarı hiçbir yerde yazılmadı.** *(Başkan tarafından koddan ve test çıktısından doğrulandı.)* |
| **`P-2`** | Beş basamak × üç tarih × dört ÖTV noktası **AYRI AYRI**; ortalama alınmaz; tek sonuç sunulmaz | ⚠ **ÖZDE SAĞLANDI, SUNUMDA EKSİK** | Beş basamak ✅ ayrı; ortalama ✅ **alınmadı**; `EARLY`/`LATE` ✅ **iki rejim ihtimaliyle**. **AMA** 3 tarih × 4 nokta çarpımı yalnız **tek bir hücre için** (799·ES·CHAIN·BASE·5k) tablolandı (§8.2); diğer dört basamak için **kapalı formla** verildi: `Δ = −(λ−1)×53,4519/(1+g)` — mutlak etki **her basamakta aynı**. Yani eksiklik **hesapta değil, sunumdadır.** → **`T-948` (MEDIUM)** |
| **`P-3`** | **TUR 2.5, 2026-08-16'dan ÖNCE çalıştırılmalıdır** (10 LCL kartı `ttl: 6d`) | ✅ **SAĞLANDI** | Model **2026-08-10'da** koşuldu. LCL kartları **son geçerlilik 2026-08-16**. Navlun bacağı **çalıştırma anında kanıtlıydı.** |

### `P-3` için **yeni bir kapı gerekiyor** — `P-3b`

```
Bugun                       : 2026-08-10
10 LCL kotasyonu STALE      : 2026-08-17 00:00
Turev kartlar (-329, -330)  : kaynak STALE olunca fiilen ayni tarih
KALAN                       : 6 gun (5 tam calisma gunu)
```

> **`P-3b` (bağlayıcı, yeni):** TUR 3A veya TUR 3B **2026-08-16'dan sonra**
> çalıştırılırsa, ya (a) `T-913` ile kotasyonlar yenilenir, ya da (b) TR-içi
> lojistik bacağı **bilinçli olarak `ESTIMATE/LOW`'a düşürülür ve çıktıda
> açıkça yazılır.** **Sessizce bayat veriyle koşmak yasaktır.**
>
> **Etkisi sınırlıdır** (`MAX_CIF` üzerinde ±0,93 TL) — ama `seytanin-avukati`
> TUR 4'te bayat girdiyle koşulmuş bir modeli **haklı olarak** tümden
> reddedebilir. Mesele büyüklük değil, **meşruiyettir.**

### Yürürlükte kalan diğer kapılar

`master-commercial-input-table.md` §5.6 **`M-1`…`M-10`** aynen yürürlüktedir.
Bu turda eklenen:

| # | Kapı |
|---|---|
| **`L3-K`** | `L3` bilgi amaçlı türev katmandır; kalemleri ikinci kez düşülemez (§4.1) |
| **`P-1`** | *(blocker → **regression guard**)* Bayraksız ÖTV değeri basılamaz |
| **`P-4`** *(yeni)* | **`R8-K` kanal round-trip assertion'ı eklenmeden hiçbir kanal bacağı sayısı `DRAFT`'tan yukarı çıkamaz** (`T-942`) |

---

# §6 — TUR 3A'YA HAZIR MIYIZ / TUR 3B İÇİN NE EKSİK

## 6.1 TUR 3A — **EVET, HAZIRIZ**

> ### NET CEVAP: **TUR 3A BAŞLAYABİLİR.**
> Hiçbir yatırımcı girdisi, hiçbir dış temas ve hiçbir yeni izin
> gerektirmez. Bugün başlayabilir.

**TUR 3A tanımı (başkan süreç kararı):** masabaşında kapatılabilen,
maliyeti ~sıfır olan, hiçbir eşiğe bağlı olmayan işler.

| Öncelik | İş | Ajan | Neden şimdi |
|---|---|---|---|
| **1** | **`T-947` — KDVK md.36 CB kararı taraması** | `gumruk-vergi-uzmani` | ⛔ **Ters modelin TÜM sayılarını çürütebilecek tek bulgu.** Varsa tavanlar **~%22,7** düşer. Saatler, ~0 TL. **Üç turdur yapılmadı** |
| **2** | **Gözetim tebliği yeniden taraması** | `gumruk-vergi-uzmani` | Tavan bir **alt sınırla hiç test edilmedi**; eşik > tavan ise **çözüm kümesi boşalır** ve fiyat pazarlığıyla kurtarılamaz |
| **3** | **`T-942` — `R8-K` kanal round-trip** | `finans-fizibilite` | Zincirin **en büyük eksenlerini taşıyan bacağının hiçbir doğrulaması yok** |
| **4** | **`T-917` — tek fiziksel mağaza turu** | `turkiye-pazar-kasifi` | `C-501` + `C-551` + `T-504` + `T-603` + `OQ-001` **aynı anda**. Projedeki en yüksek bilgi/maliyet oranı. **Üç turdur yapılmadı** |
| **5** | `T-941` · `T-943` · `T-944` · `T-945` — spesifikasyon boşlukları | `gumruk-vergi` / `kanal-marj` / `finans` | §3'te tespit edilen **desen** |
| **6** | `T-946` — `R5` düzeltmesinin bağımsız denetimi | `seytanin-avukati` | Ajanın **kendisi istedi** |
| **7** | `T-913` — LCL kotasyonlarının masabaşı yenilenmesi | `navlun-lojistik-uzmani` | `P-3b`; **6 gün** |
| **8** | `T-853` · `T-854` · `T-855` · `T-856` · `T-858` · `T-859` · `T-923` · `T-924` · `T-925` | ilgili ajanlar | Hijyen + kayıt bütünlüğü |

**TUR 3A'nın kısıtı:** `P-3b`. 1, 2, 3, 5, 6 lojistik verisine bağlı değildir
ve **tarihten bağımsız** yürütülebilir; 7 **6 gün içinde** yapılmalıdır.

## 6.2 TUR 3B — **HAYIR, HAZIR DEĞİLİZ**

> ### NET CEVAP: **TUR 3B (İLERİ MODEL) BAŞLAYAMAZ.**
> Eksik olan şeylerin **çoğu bir araştırma boşluğu değil**, bir karar veya
> bir izin boşluğudur — ve bu, TUR 6'da açıkça yazılacaktır.

| # | Eksik | Türü | Sahibi | Ticket |
|---|---|---|---|---|
| **1** | **`fx`** (tarihli kur + LOW/BASE/HIGH bandı) | **yatırımcı girdisi** | yatırımcı/başkan | **`T-852`**, `T-912` |
| **2** | **Karar eşikleri** — asgari set `D-01`, `D-03`, `D-05`, `D-14` | **yatırımcı kararı** | yatırımcı | **`T-851`**, `OQ-901` |
| **3** | **Gerçek EXW/FOB** (≥5 tedarikçiden RFQ) | **izin** *(veri değil)* | başkan → yatırımcı | **`T-466`**, `T-467` |
| **4** | **Antrepo/gümrük zorunlu bekleme süresi** | araştırma | `mevzuat-ruhsat-uzmani` | **`T-301`** |
| **5** | **`l8_chain_retail`** (gerçek zincir raf fiyatı) | araştırma *(1 mağaza turu)* | `turkiye-pazar-kasifi` | `T-603`, **`T-917`** |
| **6** | **Yasal vade tavanı** (6585 m.7/3 nitelemesi) | araştırma | `mevzuat-ruhsat-uzmani` | **`T-601`** |
| **7** | **ÖTV `λ` varsayım ekseni** (Yİ-ÜFE) | **yatırımcı varsayımı** | yatırımcı | `T-104` 2. ayağı |
| **8** | **Distribütör marjı** (seviye) | araştırma *(ticari sır — zor)* | `kanal-marj-uzmani` | `T-604` |
| **9** | **FCL navlunu** (İspanya dışı 8 rota) | **izin** *(veri değil)* | başkan | **`T-304`** |
| **10** | **KDV indirim hakkı teyidi** | araştırma *(saatler)* | `gumruk-vergi-uzmani` | **`T-947`** |

### Türlerine göre dağılım — **kritik gözlem**

```
yatirimci karari/girdisi :  4  (fx, esikler, lambda varsayimi, ... )
IZIN sorunu              :  2  (RFQ, forwarder kotasyonu)
gercek arastirma boslugu :  4  (antrepo suresi, l8_chain, vade nitelemesi,
                                distributor marji)  + KDV teyidi
```

> **TUR 3B'yi bloke eden 10 kalemin 6'sı bir araştırma boşluğu DEĞİLDİR.**
> Dördü bir **karar**, ikisi bir **izin** bekliyor. Bu, `G2` ve `G2-L`'nin
> *"tedarik kaynağı yok"* diye değil, **"henüz sorulmadı"** diye kapalı
> olduğu anlamına gelir ve **TUR 6'da bir `KILL` gerekçesi olarak
> kullanılamaz.**

---

# §7 — BU TURDA YAPILANLAR / YAPILMAYANLAR

## 7.1 Reddedilen ajan bulgusu: **0**

| Bulgu | Karar |
|---|---|
| `R5` düzeltmesi (`finans-fizibilite`) | ✅ **KABUL** — kanıtı, aritmetiği ve kodu ayrı ayrı doğrulandı |
| `MAX_CIF` pozitifliği ve `UPPER_BOUND` etiketi | ✅ **KABUL** — iki üst-sınır nedeni de yerinde |
| `TARGET`/`WALK-AWAY` **üretmeme** kararı | ✅ **KABUL** — CLAUDE.md §1.15'in doğru uygulaması |
| Sweet-spot önerisi (`799 PRIMARY`) | ✅ **ÖNERİ OLARAK KAYDEDİLDİ** — karar değildir, `D-14` yatırımcıya bırakıldı |
| `T-852` hedef düzeltmesi | ✅ **KABUL** — hata bendeydi (`T-912`'yi araç sahibi olmayan ajana açmıştım) |
| `C-851` / `C-852` çelişki kayıtları | ✅ **KABUL VE ÇÖZÜLDÜ** — ikisi de haklıydı |
| `gumruk-vergi-uzmani` `R5` spesifikasyonu | ⚠ **REDDEDİLMEDİ** — bulgusu geçerli; yalnızca **başlığın girdi katmanı düzeltilecek** (`T-941`) |

## 7.2 Başkanın kendi düzeltmeleri: **2**

1. **`T-912`'nin hedefi yanlıştı** — araştırma aracı olmayan bir ajana araştırma ticket'ı açmıştım. `T-852` bunu düzeltti; **kabul ediyorum.**
2. **`master-commercial-input-table.md` §5.3'ün *"`CIF_TRY`'ye kadar çalışır"* hükmü fazla kesindi** — `C-852` haklıdır; hüküm **nitelendi** (§4.2).

## 7.3 Bu turda yapılmayanlar

| Yapılmadı | Neden |
|---|---|
| Araştırma, web araması, yeni kanıt kartı | CLAUDE.md §1.16 |
| Ajan çağrılması | Bu bir konsolidasyondur |
| **Herhangi bir eşiğe değer yazılması** | **Eşikler yatırımcıya aittir** — `investor-decisions-required.md` §0 |
| Yatırım kararı / gate açma | TUR 6 |
| `90-karar/karar-gunlugu.md`'ye yazma | Karar TUR 6'ya aittir |
| Bir ajanın sayısının değiştirilmesi | CLAUDE.md — başkan ajanın bulgusunu kendi tahminiyle değiştirmez |
| `CLAUDE.md` düzenlemesi | Proje anayasası; `C-851` bir **niteleme** ile çözüldü, metin değiştirilmedi |
| `git` çalıştırma | Yasak |

## 7.4 Bu turda güncellenen dosyalar

| Dosya | Ne yapıldı |
|---|---|
| **`90-karar/investor-decisions-required.md`** | **YENİ — ana çıktı.** 16 eşik + 8 eşik dışı girdi; **tek bir değer yazılmadı** |
| `90-karar/tur-25-konsolidasyon.md` | *(bu dosya)* — yeni |
| `90-karar/master-commercial-input-table.md` | §5.3'e **niteleme kutusu** eklendi (`C-852`). **Orijinal metin korundu** |
| `99-ops/acik-sorular.md` | `OQ-901` → **`OPEN — SPECIFIED`**; `OQ-002`/`OQ-912` durum notları. **Orijinal metinler korundu** |
| `99-ops/celiskiler.md` | `C-851` **`RESOLVED — TANIM`**, `C-852` **`RESOLVED — TANIM`** kayıtları eklendi. **Hiçbir metin silinmedi** |
| `99-ops/tickets/T-921.md`, `T-751.md` | `ANSWERED` → **`RESOLVED`** + başkan doğrulama notu |
| `99-ops/tickets/T-941…T-948.md` | Sekiz yeni ticket |
| `99-ops/tickets/INDEX.md` | Tam yenileme |

---

## Bu kararı ne çürütür?

*(Bu belge bir yatırım kararı içermez. Aşağıdaki soru bu turun **üç hükmüne**
ilişkindir: **(a)** `G0 PASS` korunur, **(b)** `T-921`/`T-751` kapatılabilir,
**(c)** TUR 3B'nin blokeri ağırlıklı olarak karar ve izin boşluğudur.)*

### En güçlü tek çürütücü bulgu

> ### **KDV indirim hakkının alkolde kısıtlanmış olması** (`T-947`).

Bu tek mevzuat olgusu **üç hükmü de aynı anda vurur:**

- **(c) çürür:** TUR 3B'nin blokeri bir karar boşluğu değil, bir **veri hatası** olurdu. Yatırımcıdan 16 eşik istemişiz, oysa gereken **bir saatlik mevzuat taramasıydı.**
- **(b) zayıflar:** `T-751`'i *"matrah sırası doğrulandı"* diye kapattım. Matrah **sırası** doğru olabilir ve **matrahın kendisi** yanlış olabilir — KDV ekonomik dalda `0` alınmıştır ve bu tercih `T-151`'de **doğrulanmamış** olarak işaretlidir. Round-trip assertion'ı bu hatayı **yakalamaz**, çünkü ileri model de aynı varsayımı kullanır.
- Tüm tavanlar **~%22,7** düşer; `HoReCa` sütununun tamamı negatife yaklaşır; sıralama korunur ama **seviye çöker** — yani hata **fark edilmez.** `finans-fizibilite`'nin *"en sinsi çürütücü"* nitelemesi doğrudur.

**Nasıl ararız:** `T-947` — **TUR 3A'nın birinci işidir.** Saatler sürer,
maliyeti ~sıfırdır, hiçbir izne bağlı değildir ve **üç turdur yapılmamıştır.**

### İkinci en güçlü çürütücü — **`G0 PASS`'i hedefler**

**`G0`, dört turdur test edilmemiştir.** `mevzuat-ruhsat-uzmani` TUR 2'de de,
TUR 2.5'te de `G0` kapsamında çalışmamıştır. TADAB'a yazılı bir görüş talebi
veya faal bir küçük ölçekli şarap ithalatçısıyla **tek bir görüşme**, `R1`
veya `R3` tetikleyicisini **aynı temasta** ateşleyebilir.

`G0 PASS`, `C-252` ve `C-203`'ün üzerinde durmaktadır ve bu zemin **dört
turdur hiç değişmemiştir.** Ben her turda *"tetikleyiciler gerçekleşmedi"*
yazıyorum — ama tetikleyicilerin gerçekleşip gerçekleşmediğini **arayan
kimse yok.** Bu, **"olumsuz kanıt aranmadığı için olumsuz kanıt yok"**
kısırdöngüsüdür ve bu projenin en eski açık yarasıdır.

### Bu turun en tartışmalı hükmü

**`T-921` ve `T-751`'i kapatmam.**

Karşı argüman güçlüdür: *"İkisini de kapatan şey, hedef ajanın kendi
yazdığı testin kendi kodunda geçmesidir. `finans-fizibilite` hem spesifikasyonu
uygulayan hem de uyguladığını doğrulayan taraftır. Başkanın testi koşturması
bunu değiştirmez — aynı testi koşturmuştur."*

**Bu itiraz ciddiye alınmalıdır** ve `seytanin-avukati` TUR 4'te bunu hedef
almalıdır. **Savunmam üç maddedir:** (1) Test vektörlerini **`gumruk-vergi-uzmani`
yazmıştır**, `finans-fizibilite` değil — yani spesifikasyonu yazan ile uygulayan
farklı ajanlardır. (2) Beklenen değerler **koda gömülü değil, `vergi.yaml`'dan
okunmaktadır** — kodu değiştirerek testi geçmek mümkün değildir. (3) `TV-6`/`TV-7`
**yanlış cevabın reddedildiğini** de test etmektedir, yalnızca doğrunun kabul
edildiğini değil.

**Yine de kabul ediyorum:** bu kapanış, **bir ajanın kendi işini
doğrulamasına** dayanmaktadır ve bağımsız denetimi TUR 4'e kalmıştır.
`T-946` tam olarak bu boşluk için açılmıştır.

### Bu turun en kırılgan hükmü

**`P-2`'yi *"özde sağlandı"* saymam.**

`P-2`, çapraz çarpımın **ayrı ayrı** çalıştırılmasını istiyordu. Fiilen
çalıştırılan tek hücre 799·ES·CHAIN·BASE·5k'dır; diğer basamaklar **kapalı
formla** verilmiştir. Kapalı form **doğrudur** (`Δ = −(λ−1)×53,4519/(1+g)`,
maktu ÖTV'nin cebirsel sonucu) — **ama bir kapalı formu kabul etmek, tam da
`H5`'in (ÖTV'nin oransalmış gibi taşınması) yasakladığı türden bir
kısayoldur.** Fark şu ki burada form **maktuluğu koruyor**, bozmuyor.

Bu ayrımın **ince olduğunu kabul ediyorum** ve bu yüzden `T-948`'i açtım:
tam tablo üretilmeli ve kapalı form yalnızca **kontrol** olarak kullanılmalıdır.

### Bu turun kör noktası

Bu tur da **hiçbir yeni kanıt üretmemiştir.** Ürettiğim şey bir **istek
listesi** (`investor-decisions-required.md`) ve bir **denetim raporudur.**
`10-evidence/` bu turda **hiç açılmamıştır.**

**Ve daha rahatsız edici olanı:** bu turun en değerli bulgusu — `R5` hatası —
**benim denetimimden değil, ajanın kendi dürüstlüğünden** gelmiştir. Ben o
hatayı **bulmadım**; ajan bulup raporladığı için denetleyebildim. Eğer
`finans-fizibilite` hatayı fark etmeseydi veya raporlamasaydı, `R8` onu
yakalamayacaktı, ben yakalamayacaktım ve **28,95 TL/şişe'lik iyimserlik
tavanın içinde kalacaktı.**

> **Bu, projenin denetim mimarisinin gerçek durumudur:** bugün onu ayakta
> tutan şey **mekanizma değil, ajan disiplinidir.** `T-942` (`R8-K`) tam
> olarak bu boşluğu kapatmak içindir — ve o kapanana kadar, modelin kanal
> bacağındaki her sayı **denetlenmemiş** sayılmalıdır.
