# KARAR GÜNLÜĞÜ

Bu dosya `yatirim-komitesi-baskani`'nın verdiği tüm kararları ve
gerekçelerini kaydeder. Kararlar **silinmez**, üzerine yazılmaz — yeni karar
yeni kayıt olarak eklenir.

---

## KARAR TÜRLERİ

| Karar | Anlamı |
|-------|--------|
| `KILL` | Yapılmamalı |
| `HOLD` | Şu an değil |
| `TEST` | Karar için gerçek veri gerekiyor |
| `IMPORT PILOT` | Sınırlı hacimde gerçek ithalat |
| `SCALE` | Büyütme |

---

## KAYIT #0 — TUR 0 KURULUM

```yaml
tarih:            2026-08-09
tur:              TUR 0
karar:            KARAR VERILMEDI
karar_veren:      -
```

### Neden karar verilmedi

Bu tur **sadece kurulum turudur.** Kullanıcı talimatı açıktır:
web araştırması yapılmadı, vergi/navlun/fiyat verisi toplanmadı, model
çalıştırılmadı. **Karar verilecek hiçbir kanıt yoktur.**

Kanıtsız karar vermek `CLAUDE.md` §1'in doğrudan ihlalidir.

### Gate durumu

| Gate | Soru | Durum |
|------|------|-------|
| G0 | Yasal yol açık mı? | ⬜ **NOT STARTED** |
| G1 | Vergi yükü kanıtlı hesaplanabilir mi? | ⬜ **NOT STARTED** |
| G2 | Gerçek tedarik kaynağı var mı? | ⬜ **NOT STARTED** |
| G3 | Benchmark doğrulandı mı? | ⬜ **BLOCKED** — OQ-001 açık |
| G4 | Model pozitif contribution veriyor mu? | ⬜ **NOT STARTED** |
| G5 | CRITICAL ticket'lar kapandı mı? | ⬜ **NOT STARTED** |

### Kurulan sistem

- 9 ajan (`.claude/agents/`)
- 7 komut (`.claude/commands/`)
- Kanıt sistemi (immutable kanıt kartları, `EV-YYYY-MM-DD-###`)
- Ticket sistemi (`T-###`, CRITICAL gate kuralı)
- Maliyet katmanları L0–L8, KDV iki perspektif, `peak_cash_requirement`
- Model iskeleti — **hiçbir vergi oranı hard-code edilmemiş**

### Açık kalanlar

| # | Konu | Etki |
|---|------|------|
| OQ-001 | Metro 599,90 TL — KDV dahil/hariç, L7/L8 | **G3'ü bloke ediyor** |
| OQ-002 | Model hedef tarihi | Vergi verilerinin geçerlilik tarihi belirsiz |
| — | Karar eşikleri `TBD` | Nihai karar için eşik gerekli |
| — | 9 ajanın registry doğrulaması | TUR 1 başlayamaz |

### Sonraki adım

`SESSION RESTART` → 9 ajanın registry'de varlığını doğrula → `/tur-1-kesif`

---

## KARAR KAYIT FORMATI (SONRAKİ TURLAR)

```yaml
tarih:
tur:
karar:              # KILL | HOLD | TEST | IMPORT PILOT | SCALE
karar_veren:        yatirim-komitesi-baskani
```

### Karar gerekçesi

### Dayandığı kanıtlar

| evidence_id | claim | tier | status |
|-------------|-------|------|--------|

### Kararı taşıyan 3 kritik varsayım

1.
2.
3.

### Kararı tersine çevirecek bulgu

> "Şunu görürsem fikrimi değiştiririm: ..."

### Açık kalan CRITICAL UNKNOWN'lar

| # | UNKNOWN | Neden kapanmadı | Kararı nasıl etkiliyor |
|---|---------|-----------------|------------------------|

### Reddedilen bulgular

| Ajan | Bulgu | Red gerekçesi |
|------|-------|---------------|

### Çözülen çelişkiler

| conflict_id | Çözüm | Gerekçe |
|-------------|-------|---------|

### Bir sonraki gözden geçirme tetikleyicisi

Hangi olay gerçekleşirse bu karar yeniden ele alınır?

### Bu kararı ne çürütür?

---

## BAŞKANIN DEĞİŞMEZ KURALLARI

1. Araştırma yapmaz — eksik veri için ticket açar.
2. Kanıtsız sayıyı reddeder.
3. Başka ajanın bulgusunu kendi tahminiyle değiştirmez.
4. Çelişkiyi sessizce çözmez.
5. **"Yeterli veri yok" geçerli bir çıktıdır** — bundan kaçınmak için
   karar uydurmaz.
6. `impact: CRITICAL` açık ticket varken model `APPROVED` olamaz.

---

## KAYIT #1 — PRE-RFQ GATE (PRELIMINARY)

```yaml
tarih:            2026-08-10
tur:              PRE-RFQ GATE  (TUR 3.25 sonrasi, TUR 3B oncesi)
karar:            PROCEED TO RFQ
karar_tipi:       PRELIMINARY GATE DECISION
confidence:       MEDIUM
karar_veren:      yatirim-komitesi-baskani
ana_belge:        90-karar/PRE-RFQ-INVESTMENT-REPORT-v1.md
```

> ## ⛔ BU KAYIT BİR NİHAİ YATIRIM KARARI DEĞİLDİR
>
> Verilen karar **yalnızca bir ön kapı kararıdır** ve tek bir soruyu cevaplar:
> *"Gerçek firmalarla görüşmeye ve teklif toplamaya devam edilsin mi?"*
>
> **`IMPORT PILOT` ve `SCALE` kararları VERİLMEMİŞTİR ve bu turda verilemez.**
> `KILL` ve `HOLD` de verilmemiştir — ikisi de RFQ sonrasında yeniden masaya
> gelir. Nihai yatırım kararı, gerçek satın alma fiyatı, doğrulanmış navlun ve
> yatırımcı eşikleri geldikten sonra **ayrı bir kayıt** olarak yazılır.
>
> Bu karar **hiçbir gate'i AÇMAZ.** `G2`'yi açan şey **cevaplardır**, izin değil.

---

### Karar gerekçesi

**Üç cümle:**

1. **`KILL` değil** — 20 necessary condition'ın **sıfırı `FAIL`**'dir. Projeyi
   öldürmesi beklenen hipotez (*"999 TL'de bile ödenebilir CIF negatif veya
   sıfıra yakın çıkar"*) 2.700 kombinasyonda test edilmiş ve **çürütülmüştür**;
   `MAX_CIF` hiçbir kombinasyonda negatif değildir.
2. **`HOLD` değil** — beklemek hiçbir şeyi değiştirmez. 12 açık `UNKNOWN`'ın
   **7'si masabaşıyla kapanmaz** (dış temas veya fiziksel gözlem gerektirir) ve
   zaman geçtikçe kanıt tabanı bayatlar: LCL kotasyonları **2026-08-17'de**,
   pazar gözlemleri **2026-09-08/09'da** `STALE` olur.
3. **`PROCEED TO RFQ`** — modelin en büyük belirsizliği (**gerçek satın alma
   fiyatı**, `T-466`) yalnızca **sormakla** öğrenilebilir; sormanın para
   maliyeti ≈ sıfırdır ve **geri dönülemez taahhüdü yoktur.**

**Kapsam sınırı (bağlayıcı):** Bu karar **yalnızca bilgi toplamaya** izin verir.
Sipariş verilmez, numune ilk turda istenmez (`T-893`), şirket kurulmaz, hiçbir
mali taahhüde girilmez. Her mesaj `P-6.3` uyarınca **RECIPIENT + SUBJECT +
PREVIEW** onayından geçer. **İlk dalga 5 hedefle sınırlıdır** (gerekçe: 10
hedefte onay yükü `P-6.4`'ü fiilen ihlal eder).

---

### Dayandığı kanıtlar

| evidence_id | claim | tier | status |
|---|---|---|---|
| `EV-2026-08-09-103` | Şarapta gümrük vergisi AB/BK/Şili %50, Yeni Dünya %70; şarap I s. Liste (tarım) — **Gümrük Birliği kapsamında değil** | **T1** | FACT |
| `EV-2026-08-09-110` / `-111` / `-113` | ÖTV (III)/A cetveli: nispi **%0**, asgari maktu **71,2692 TL/litre** → **53,4519 TL/şişe**; birim **litre** | **T1** | FACT |
| `EV-2026-08-09-115` / `-117` / `-118` | ÖTV matrahı = CIF+GV+KKDF *(ÖTV/KDV hariç)*; KDV matrahı = **ÖTV dahil**; KDV **%20** | **T1** | FACT |
| `EV-2026-08-10-101` / `-102` / `-103` | İthalatta ödenen KDV **indirilebilir**; md.30'da alkole özgü yasak **YOK** | **T1** | FACT |
| `EV-2026-08-10-852` / `-860` / `-861` / `-862` | KDVK md.36 CB kararı (7846 s.) **vardır ama 2204.21'e değmez** → etki **0,00 TL/şişe** | **T1** | FACT |
| `EV-2026-08-10-157` | Menşe belgesi ibraz edilemezse tercihli oran düşer, **%70 uygulanır** | **T1/T2** | FACT |
| `EV-2026-08-09-213` | Bandrol **2,36073 TL/şişe** (KDV hariç), peşin, satıştan önce | **T1** | FACT |
| `EV-2026-08-09-234` | Toplam ruhsat sabit maliyeti **150.839 TL** → **253.372 TL** (20.000 lt/yıl eşiğinde kademe) | T2/T3 | FACT |
| `EV-2026-08-10-301` … `-311` | 9 rotanın **LCL navlunu** — gerçek, tarihli kotasyon (⏰ `ttl 6d`, **2026-08-17 STALE**) | T4 | FACT |
| `EV-2026-08-10-330` | LCL/FCL kırılma noktası **~5.900 şişe** (band 2.200–9.800) | T4 türev | ESTIMATE |
| `EV-2026-08-09-405` | Türkiye'ye 2025 CIF birim değerleri: MD 2,46 · ES 2,71 · CL 2,89 · PT 3,20 · IT 3,65 · FR 6,27 USD/lt | T3 | FACT |
| `EV-2026-08-09-408` / `-410` | Doğrulanmış private label MOQ: **3.000** (Interbrosa, ES) · **3.600** (The Wine Factory, FR) | T4 | FACT |
| `EV-2026-08-09-501` / `-502` | Metro Türkiye: **Gold Country 599,90 TL** · **Central Creek 649,90 TL** — fotoğraftan | T4 | FACT |
| `EV-2026-08-10-702` | Yoğunluk eğrisi (100 TL bin): stokta n=471 (391 yerli + 80 ithal); stokta ithal min **875 TL**; stokta yerli medyan **1.410 TL** | T4 | FACT |
| `EV-2026-08-10-612` | Rekabet Kurulu 21-51/708-351 para.82 — alkollü içkide zincire **geri akan bedeller ismen kanıtlı** | T1 | FACT |
| `EV-2026-08-10-865` / `-866` | TCMB 2026-08-10 (Bülten 2026/147), döviz satış: **EUR/TRY 55,1414** · **USD/TRY 47,7118** | **T2** | FACT |
| `country-buying-ceilings.csv` | `MAX_CIF` 799/CHAIN/BASE/5.000: **272,8306** (P) / **240,7329** (N); X=200,978 · Y=290,5134 | MODEL_DERIVED | **DRAFT / UPPER_BOUND** |

---

### Kararı taşıyan 3 kritik varsayım

1. **`ASSUMPTION` — Gerçek tedarikçi FOB fiyatları, yapısal tavanın anlamlı
   ölçüde altında olacaktır.**
   Dayanağı: Türkiye'nin İspanya'dan fiilen ithal ettiği ortalama CIF birim
   değeri **2,03 USD/şişe**; yapısal tavan **5,72 USD/şişe** (799/P/5k/BASE).
   **Çökerse: proje ölür.**

2. **`ASSUMPTION` — Zincir perakendede bu segmentin tüketici raf fiyatı 799 TL
   bandındadır.**
   Dayanağı: **YOK.** `L8_CHAIN_RETAIL`'de **sıfır gözlem** vardır (`T-603`,
   `T-701`). Bu, modelin **tepe çapasıdır** ve hiç ölçülmemiştir.
   **Çökerse: maktu ÖTV sabit kaldığı için tüm tavanlar ORANTISIZ düşer.**

3. **`ASSUMPTION` — Kanal marjı %25 (BASE) ve geri akan bedeller (`d`) %8
   civarındadır.**
   Dayanağı: Migros 2025 konsolide **%24,31** — ve o **şarap değil, TÜM
   KATEGORİ** karmasıdır; alkolün resmî marj analizinin kapsamı dışındadır.
   **Çökerse: `m_retail` %35 olursa tavan 272,83 → ~176 TL (−%35).**

---

### Kararı tersine çevirecek bulgu

> **"Şunu görürsem fikrimi değiştiririm:"**
>
> **≥5 gerçek, tarihli, para birimi ve Incoterm'i belirtilmiş tedarikçi
> teklifinin TAMAMININ `Y` köşesinin ÜSTÜNDE çıkması**
> (Y = **290,5134 TRY/şişe** = **5,2685 EUR** = **6,0889 USD**, TCMB 2026-08-10).
>
> Bu, modelin **tek yönlü olarak sağlam** karar verebildiği tek durumdur:
> `gerçek_CIF ≥ teklif × kur` olduğundan, teklif Y'yi aşıyorsa **ret hükmü
> kesindir.** O gün karar **`KILL`**'e döner.
>
> **İkinci tersine çevirici:** Fiziksel mağaza turunda `L8_CHAIN_RETAIL`'de bu
> segmentin fiilen **500–650 TL** bandında olduğunun görülmesi.
>
> ⚠ **Ve bir uyarı:** `INCOMPLETE` bir `KILL` gerekçesi **değildir.**
> FOB→CIF köprüsü (`T-866`) kapanmadan makul fiyatlı her teklif `INCOMPLETE`
> döner; bu, tedarikçinin pahalı olduğunu değil, **modelin cevap veremediğini**
> gösterir.

---

### Açık kalan CRITICAL UNKNOWN'lar

| # | UNKNOWN | Ticket | Neden kapanmadı | Kararı nasıl etkiliyor |
|---|---|---|---|---|
| 1 | Gerçek EXW/FOB fiyatı | `T-466` | Dış temas gerekiyordu; mesaj gönderilmedi | **Bu kararın hedefi** |
| 2 | Doğrulanmış FCL navlunu | `T-304` | Aynı — paket hazır, gönderilmedi | Peak cash + taşıma modu |
| 3 | Antrepo zorunlu bekleme süresi | `T-301` | `mevzuat-ruhsat-uzmani` bu kapsamda çalışmadı | **Peak cash'in zaman ekseni** |
| 4 | Yasal vade tavanı (6585 m.7/3 nitelemesi) | `T-601` | Hukuki niteleme — başkan kendi yorumuyla kapatamaz | Alacak finansmanı |
| 5 | Yatırımcı marj eşikleri | `T-851` / `OQ-901` | **Yalnızca yatırımcı kapatabilir** | `TARGET`/`WALK-AWAY` üretilemiyor |
| 6 | RFQ paketi gönderilmedi | `T-885` | `P-6.3` onayı bekliyor | **Bu kararın konusu** |
| 7 | ÖTV Yİ-ÜFE ekseni (2. ayak) | `T-104` | Yatırımcı varsayımı | Tüm parasal çıktı `UPPER_BOUND` |
| 8 | `fx` sahipliği / hedef tarih kuru | `T-852`, `T-912` | Gözlem alındı; **2027 projeksiyonu yatırımcıda** | Ülke ayrıştırma gücü |
| 9 | `R8-K` kanal round-trip doğrulaması | `T-942` | `ANSWERED`, bağımsız denetimi TUR 4'te | Kanal bacağı **denetlenmemiş** |
| 10 | KDVK md.36 taraması *(kapandı, kayıt)* | `T-947` | ✅ **CONFIRMED — etki 0,00 TL/şişe** | Risk **elendi** |
| 11 | KDV indirim hakkı teyidi *(kapandı, kayıt)* | `T-171` | ✅ **ANSWERED** | `MAX_CIF` değişmedi |
| 12 | ÖTV zaman serisi kilidi *(kapandı, kayıt)* | `T-921` | ✅ **RESOLVED** — regression guard olarak yürürlükte | 2027 ÖTV hiçbir çıktıda yazılmadı |

**Açık `CRITICAL` sayısı: 12** *(2026-08-10, TUR 3.25 §0 derlemesi)*
**Toplam ticket: 151** · **Kanıt kartı: 321** (T1: 91 · T2: 43 · T3: 33 · T4: 120 · T5: 32)

> **`CLAUDE.md` §5 yürürlüktedir:** açık `CRITICAL` ticket varken finans modeli
> **`APPROVED` olamaz.** `reverse-price-model.md`, `sweet-spot-analizi.md` ve
> `country-buying-ceilings.csv` **`DRAFT`**'tır ve öyle kalır. Bu karar o
> kuralı **ihlal etmez**, çünkü model çıktılarını bir **üst sınır** olarak
> kullanmaktadır, bir onay olarak değil.

---

### Reddedilen bulgular

| Ajan | Bulgu | Red gerekçesi |
|---|---|---|
| — | — | **Bu turda hiçbir ajan bulgusu reddedilmemiştir. Sayı: 0.** |

Bu tur bir **konsolidasyon ve karar turudur**; yeni ajan raporu üretilmemiştir.

**Başkanın kendi düzelttiği hükümler (kayıt, önceki turlardan):**
`master-commercial-input-table.md` §5.3'ün *"`fx` olmadan ters model
`CIF_TRY`'ye kadar çalışır"* hükmü **fazla kesindi** ve nitelendi (`C-852`);
`T-912`'nin hedef ajanı **yanlıştı** ve `T-852` ile düzeltildi.

---

### Çözülen çelişkiler

| conflict_id | Çözüm | Gerekçe |
|---|---|---|
| — | — | **Bu turda yeni çelişki çözülmemiştir.** `99-ops/celiskiler.md` dosyasına **DOKUNULMAMIŞTIR.** |

**Karara taşınan, ÇÖZÜLMEMİŞ çelişkiler (kayıt):**

| id | impact | Konu | Karara etkisi |
|---|---|---|---|
| `C-311` | **CRITICAL** | FCL base okyanus navlunu: yüzlerce USD mi, binlerce EUR mu (**4–5 kat**) | Ters model üzerinde **etkisi SIFIR**; ileri model ve **FOB pazarlığı** için bloker |
| `C-501` | HIGH | Stokta olmayan listelemelerin fiyatları gerçeklik dışı mı | Yoğunluk eğrisinin **tabanı** |
| `C-551` | HIGH | Metro şarap kategorisinde KDV sunumu | Benchmark okunuşu |
| `C-561` | MEDIUM | Bant assortmanda dolu / stokta boş — **whitespace mi, dönmeme mi** | **Boşluk argümanının tamamı buna bağlı** |
| `C-601` | HIGH | Zincir vade: 60 gün ↔ ~93 gün | `peak_cash` |
| `C-602` | *(RESOLVED — sahte çelişki)* | Tekel/HoReCa marjı | Ama `m_tekel` bandının **hiçbir noktasının kanıtı yok** |
| `C-202` · `C-252` · `C-203` | HIGH / LOW / CONSTRAINT | Sıralama döngüsü · halef merci · rafta marka bulundurma yasağı | **`G0 = PASS` bu üçünün üzerinde duruyor** |
| `C-461` | — | "FOB" terimi iki farklı katmana işaret ediyor (Harland) | Tek yayınlanmış fiyat **modele giremiyor** |

---

### Gate durumu (PRE-RFQ)

| Gate | Durum | Bu kararla değişti mi |
|---|---|---|
| **G0** Yasal yol | **`PASS`** ⚠ *(beş turdur test edilmedi)* | HAYIR |
| **G1** Vergi yapısı | **`BLOCKED`** | HAYIR |
| **G2** Tedarik | **`BLOCKED`** | **HAYIR** — izin bir veri değildir; `G2`'yi cevaplar açar |
| **G2-L** Lojistik | **`BLOCKED`** ⏰ *(2026-08-17 tazelik)* | HAYIR |
| **G3** Pazar | **`BLOCKED`** — `OQ-001` açık | HAYIR |
| **G4** Ekonomi | **`NOT_EVALUATED`** | HAYIR |
| **G5** Risk | **`NOT_EVALUATED`** | HAYIR |

> **HİÇBİR GATE AÇILMAMIŞTIR.**

---

### Bir sonraki gözden geçirme tetikleyicisi

| Tetikleyici | Sonuç |
|---|---|
| **≥5 gerçek RFQ cevabı** | Karar yeniden ele alınır → `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` |
| **Fiziksel mağaza turu tamamlanması** (`T-917`) | `G3` yeniden değerlendirilir; **799 hedefi teyit veya revize** edilir |
| **2026-08-17** | LCL kotasyonları `STALE` → lojistik bacağı yeniden doğrulanır veya `ESTIMATE/LOW`'a düşürülür |
| **2026-09-08/09** | Pazar gözlemleri `STALE` → rakip/bant sınıflandırması yeniden doğrulanmadan kullanılamaz |
| **Yatırımcı marj eşiğinin yazılması** | `TARGET BUY` / `ACCEPTABLE BUY` / `WALK-AWAY` **üretilebilir hale gelir** |
| **Herhangi bir `G0` geri alma tetikleyicisi** (`R1`/`R2`/`R3`) | `G0` yeniden değerlendirilir |
| **İlk dalgada alıcı sayısının 7'yi aşması** | `P-6.3` ↔ `P-6.4` gerilimi gerçek demektir → kurala **dalga/parti tanımı** eklenmesi istenir |

---

### Bu kararı ne çürütür?

> ## Zincir market rafında bu segmentin fiilen 799 TL'nin ÇOK ALTINDA olması.

Ters modelin **tepe çapası** hedef raf fiyatıdır. Segment `L8_CHAIN_RETAIL`'de
799 değil de **450–650 TL** ise, azami satın alma fiyatı **maktu ÖTV sabit
kaldığı için ORANTISIZ** düşer: 799 → 599 kayması tavanı **272,83 → 189,50 TL**
yapar (**−%30,5**) ve sabit TL maliyet yığınının payı **%30,9 → %44,5**'e çıkar.

Elimizde bunu **dışlayan tek bir gözlem yoktur** — o katmanda **sıfır ölçüm**
var ve bir T5 sinyali (`EV-2026-08-10-703`) zaten zincir/tekelde **450–650 TL**
iddia ediyor; o sinyal `C-503` ile modele alınmadı ama **çürütülmedi de.**

**Nasıl ararız:** Bir mağaza turu — **bir gün, sıfıra yakın maliyet** (`T-917`).
**Üç turdur yapılmadı.**

**İkinci çürütücü:** `P-6.3`'ün (her mesaj için ayrı onay) pratikte
uygulanamaz olduğunun ortaya çıkması. 29 ayrı onay turu yorulur ve kural
sessizce *"toplu önizleme + tek onay"*a döner — yani kurucunun **açıkça
yasakladığı şeye.** Bu yüzden ilk dalga **5 hedefle** sınırlanmıştır.

**Bu kararın kör noktası:** Rapor, *"devam et"* demenin **bedava** olduğunu
varsayıyor. Para maliyeti ≈ sıfırdır, ama üç ölçülmemiş maliyeti vardır:
**dikkat**, **taahhüt tırmanması** (beş firmayla konuştuktan sonra `KILL` demek
psikolojik olarak çok daha zordur) ve **itibar**. Ve en rahatsız edici gerçek:
**bu proje beş turdur veri topluyor ve 321 kanıt kartının hiçbiri bir insanla
yapılmış görüşmeden gelmiyor.**
