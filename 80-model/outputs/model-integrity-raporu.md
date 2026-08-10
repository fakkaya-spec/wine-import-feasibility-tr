# MODEL BÜTÜNLÜK (INTEGRITY) RAPORU — TUR 3A

```yaml
belge:            model-integrity-raporu
sahibi:           finans-fizibilite
tur:              TUR 3A — MODEL AUDIT + ROUND-TRIP ASSERTIONS
tarih:            2026-08-10
tip:              DENETIM CIKTISI (yeni karlilik modeli DEGILDIR)
durum:            DRAFT                     # APPROVED OLAMAZ — bkz. §0
yeni_arastirma:   YOK — hicbir dis kaynak taranmamistir
yeni_evidence:    YOK — tum atiflar mevcut evidence_id'leredir
yeni_girdi:       YOK — hicbir kanitsiz sayi modele sokulmamistir
```

> ## ⛔ BU RAPOR HİÇBİR **YENİ SAYI** ÜRETMEZ
> Bu tur bir **model bütünlüğü** turudur. İleri kârlılık modeli
> çalıştırılmadı; contribution margin, break-even, ROI, IRR ve tedarikçi
> tavsiyesi **üretilmedi**. Üretilen tek şey, mevcut modelin **kendi
> kendini yanlışlayabilme kapasitesidir.**

---

## 0. GATE DURUMU — ÇIKTI `DRAFT`'TIR, `APPROVED` DEĞİLDİR

`CLAUDE.md` §5 gereği `impact: CRITICAL` açık ticket varken model çıktısı
`APPROVED` olamaz. Bu tura girerken açık CRITICAL ticket'lar: `T-619`,
`T-942`, `T-301`. Ayrıca **her koşu satırı** artık kendi damgasını taşır:

```
STATUS = DRAFT_MODEL_DERIVED_UPPER_BOUND_BLOCKED_INPUT     (2.700/2.700 satır)
```

Bu damga bir hata değildir. TUR 2.5'te aynı satırlar
`MODEL_DERIVED_UPPER_BOUND` yazıyordu ve **26 ayrı kalem sessizce `0`
geçiyordu.** Damganın kendisi bu turun ürünüdür.

---

## 1. GÖREV 1 — SILENT OMISSION → ZORUNLU METADATA

### 1.1 Mimari

Yeni modül: **`80-model/engine/kalem_defteri.py`**

Her maliyet kalemi **dokuz zorunlu alanla** tanımlanır
(`kanal-katman-matrah-haritasi.md` §2):

```
payer · receiver · layer · currency · fixed_or_variable ·
per_bottle_or_total · tax_treatment · evidence_id · status
```

`basis` (matrah) onuncu alandır ve kanal kalemlerinde ayrıca zorunludur.
Bir alan veya **tutar** eksikse kalem üç damgadan birini alır:

| Damga | Anlamı | Davranış |
|---|---|---|
| **`OK`** | dokuz alan dolu **ve** tutar biliniyor | düşülür |
| **`BLOCKED_INPUT`** | bir alan veya tutar eksik | **düşülmez ve `0` DA SAYILMAZ**; adıyla ve **eksik alan adıyla** çıktıya basılır |
| **`EXCLUDED_WITH_REASON`** | bilinçli mimari dışlama | düşülmez, **gerekçe zorunludur** |

`BLOCKED_INPUT`'un iki sertliği vardır:
`hard_blocker=True` → sonuç **`UNKNOWN`** (sayı üretilmez);
`hard_blocker=False` → sayı üretilir ama çıktı **`DRAFT`** ve damgalıdır.

> **Neden `0` yerine "hesaba hiç girmemek":** `0` bir değerdir ve bir
> **karar** gibi görünür. "Hesaba girmedi" bir **boşluktur** ve boşluk
> sayılabilir. `BLOCKED_INPUT_COUNT` sütunu tam olarak bunu sayar.

### 1.2 Sayım — `TGT_799 · ES · BASE · 5.000 şişe`

| Damga | CHAIN RETAIL | INDEPENDENT/TEKEL | HoReCa |
|---|---|---|---|
| `OK` (defterde, düşülüyor) | **4** | 4 | 4 |
| `BLOCKED_INPUT` (toplam, defter + kanal bacağı) | **26** | **29** | **31** |
| `EXCLUDED_WITH_REASON` | **5** | 5 | 5 |
| **Kapsamdaki toplam kalem** | **35** | **38** | **40** |

`BLOCKED_INPUT`'un dağılımı (CHAIN, 26 kalem):

| Kaynak | Adet | Örnek |
|---|---|---|
| `kanal.yaml → blocked_envanteri` (`B-1`…`B-15`) | **15** | `f`/`d` KDV indirilebilirliği, `μ` matrahı, `d` sepetinin ayrışması… |
| `L5` kalemleri, tutarı `UNKNOWN` | **8** | varış local charges, antrepo bekleme, fire/zayi KDV, **kanal alacağı vade finansmanı** |
| Kanal bacağı, TUR 3A'da yeni görünür oldu | **3** | `f_listeleme_bedeli`, `D_fix_sabit_bilesenler`, `iade_orani_r` |

Kanala özgü ek `BLOCKED`'lar (`kanal-katman-matrah-haritasi.md` §4.2 —
*"bir sıfır değil, ÜÇ sıfır"*):

| Kanal | Ek satır |
|---|---|
| TEKEL (+3) | net fiyat iskontosu · kılcal dağıtım maliyeti · şüpheli alacak karşılığı |
| HoReCa (+5) | yatırım desteği · kılcal dağıtım · şüpheli alacak · aktivasyon/tadım · **menü KDV oranı** (`T-612`) |

> ### BULGU 1.A — `T-856`'NIN CEVABI ARTIK MODELDE GÖRÜNÜYOR
> Tekel tavanının zincirden **%11,4 yüksek** olması bir bulgu değildi;
> **eşit olmayan sıfır sayısının** artefaktıydı. Artık bu **sayılabilir**:
> `26` vs `29` vs `31`. `ZERO_PARITY` kontrolü bu farkı gördüğünde
> **`KANALLAR_KARSILASTIRILAMAZ`** bayrağı basar.

### 1.3 `EXCLUDED_WITH_REASON` — beş bilinçli dışlama

| Kalem | Gerekçe |
|---|---|
| `KANAL::markup_karsiligi_k` | `m` ve `k` aynı gerçeğin iki ifadesidir (`k = m/(1−m)`); ikisi birden düşülürse **çift sayım** (`K2`) |
| `KANAL::kdv_v2_mal_faturasi` | Ekonomik maliyet **değildir** (tahsil edilip beyan edilir); **yalnızca nakit dalında**, matrahı `L6_gross` (`K12a`) |
| `VERGI::kdv_ithal_ekonomik` | `(A) İNDİRİM CONFIRMED` → `l4_econ`'a **girmez**; `l4_cash`'te **ayrıca** durur (`RC1`/`RC3`) |
| `KATMAN::L3_pre_tax_landed` | Bileşenleri `L5`'te **zaten** düşüldü; ayrıca düşülürse **çift sayım** (`K6`) |
| `KATMAN::L6_fatura_fiyati` | `L6` bir **fatura fiyatıdır**, hasılat değil, `L5` bütçesi hiç değil → `R8-K` zincirinde **hiç kullanılmaz** (`T-619`) |

---

## 2. GÖREV 2 — `T-619`'UN ÇÖZÜMÜ (BU TURUN EN KRİTİK BULGUSU)

### 2.1 Sorun neydi

`T-942` (CRITICAL) doğru bir teşhis koydu: **kanal bacağında hiçbir
otomatik doğrulama yoktu** ve −28,95 TL/şişelik `R5` hatası
**2.700/2.700 satırdan temiz geçmişti.** Ama önerdiği assertion'ın `K1`
adımı **etiket hatalıydı**:

```
T-942:  adim K1 : L6_geri = (L5_max + mu * L6)        <-- ETIKET YANLIS
```

`L5_max + μ·L6` ifadesi `L6`'ya değil **`L7_eff`**'e eşittir. `L6`
etiketiyle devam edilince bir sonraki adımda `×(1−d) − f` **ikinci kez**
uygulanır.

### 2.2 Doğrulama — spesifikasyon gerçekten tersten çalışıyor

`TVK-N1b` vektörü bunu **çalıştırarak** kanıtladı
(`f = 6,00` tabanı, `m=%25`, `d=%8`, `v=%20`, `μ=0`):

| Girilen `L5_max` | `T-942` birebir → `L8_geri` | Sonuç | **DOĞRU `R8-K`** → `L8_geri` | Sonuç |
|---|---|---|---|---|
| **DOĞRU** `= L7_eff = 499,3750` | **725,48** *(f=0 tabanında 735,08)* | ⛔ **REDDEDİLİR** | **799,0000** | ✅ **KABUL** |
| **NAİF** `= L6 = 549,3207` | **799,0000** | ✅ **KABUL EDİLİR** | **878,9130** (Δ +79,9130) | ⛔ **RED** |

**Yani `T-942`'nin assertion'ı birebir kodlansaydı `R5` düzeltmesini geri
alır ve −28,95 TL'lik hatayı "test edilmiş" damgasıyla mühürlerdi.**

### 2.3 Uygulanan doğru çözüm

`80-model/engine/kanal_bacagi.py`:

```
K1'  L7_eff_geri = L5_max + mu_kesintisi + m_dist_kesintisi + iade_kaybi
K2'  L8_net_geri = L7_eff_geri / (1 - m)        [HORECA: * k]
K3'  L8_geri     = L8_net_geri * (1 + v)
assert  | L8_geri - L8_gross | < 0,01 TL
```

**Üç ek disiplin:**

1. **`L6` bu zincirde hiç kullanılmaz.** Bu bir yorum değil, **test edilen
   bir özelliktir**: `INV::L6_ZINCIRDE_YOK` vektörü `L5_max`'i sabit tutup
   `d_var`'ı `0 → 0,08 → 0,18` ve `f`'yi `0 → 6` değiştiriyor — yani `L6`'yı
   değiştiriyor — ve `L8_geri`'nin **üçünde de tam olarak 799,0000**
   kaldığını doğruluyor.
2. **Geri inşa bağımsızdır.** İleri yönde hesaplanmış hiçbir ara değer
   (`L6`, `L7_eff`) yeniden kullanılmaz; `L7_eff` yalnızca `L5_max`'ten
   **cebirsel olarak** çözülür (`L7 = (L5_max + B)/(1 − A)`). Aksi hâlde
   test kendi kendini doğrular ve **hiçbir şey kanıtlamaz.**
3. **HoReCa `*k` ile geri kurulur** (`T-619` kriter #3), `/k` ile değil.

### 2.4 `TVK-N1b` KALICIDIR

`T-942`'nin birebir spesifikasyonu koda
`R8K_T942_BIREBIR_HATALI_ASLA_URETIMDE_KULLANMA()` adıyla **negatif
vektör olarak** girdi. Üretimde çağrılmaz. Amacı tek: **gelecekte biri
aynı spesifikasyonu yeniden yazarsa test kırılır** (`T-619` kriter #2).

---

## 3. EKLENEN TESTLER VE SONUÇLARI

### 3.1 `test_model_butunlugu.py` — **30/30 GEÇTİ**

| # | Test | Ne kanıtlar | Sonuç |
|---|---|---|---|
| 1 | `TVK-1` | temel zincir `K1..K5` | ✅ |
| 2 | `TVK-2` | `R8-K` kapanıyor (fark `0`) | ✅ |
| 3 | `TVK-3` | HoReCa çarpanının matrahı `L7_eff` + `*k` geri inşa | ✅ |
| 4 | `TVK-4` | `f=0, d=0` → `L6 == L7_eff` **tam eşit** | ✅ |
| 5 | `TVK-P1` | `μ` matrahı `L6` → `L5_max=390,8152` · `MAX_CIF=200,4574` | ✅ |
| 6 | `TVK-P2` | `μ` matrahı `L7_EFF` → `399,5000` · `206,2473` | ✅ |
| 7 | `TVK-P3` | `μ` matrahı `L5_MARKUP` → `416,1458` · `217,3445` | ✅ |
| 8 | `TVK-P1/2/3-AYRIM` | üç matrah **üç FARKLI** sonuç verir (`K5`) | ✅ |
| 9 | `TVK-P4` | `SCALE_MONOTONICITY`: `f=F/Q`, `f·Q` sabit, `f@5k=60,00`, `f@100k=3,00` (`K7`) | ✅ |
| 10 | `TVK-P5` | `Q_satilan = 0,95·Q_ithal`; sabitler `Q_ithal`'e bölünür; `r=None` → `FIRE_SIFIR_VARSAYILDI` (`K11`) | ✅ |
| 11 | `TVK-P6` | alacak matrahı `L6_gross = 651,3587` (≠ `L6 = 542,7989`) + `VADE_MALIYETI_MODELLENMEDI` (`K12`) | ✅ |
| 12 | `TVK-N1` | naif `R5` → `R8-K` **REDDEDER**; `L8_geri = 878,9130` (Δ `+79,9130`) | ✅ |
| 13 | **`TVK-N1b`** | **`T-942` spesifikasyonu TERSTEN çalışıyor** — kalıcı regresyon kilidi (`T-619`) | ✅ |
| 14 | `TVK-N2` | margin↔markup karışıklığı → **REDDEDİLİR**; Δ `+53,2667` (`K2`) | ✅ |
| 15 | `TVK-N3` | `kdv_dahil_mi` boş → `UNKNOWN` + `BLOCKED_INPUT` (`K10`) | ✅ |
| 16 | `TVK-N4` | `μ≠0` & matrah `null` → `UNKNOWN`; `μ=0` → çalışır (`K5`) | ✅ |
| 17 | `TVK-N5` | `ZERO_PARITY` → `KANALLAR_KARSILASTIRILAMAZ` (`K3`) | ✅ |
| 18 | `TVK-N6` | `d_kimde` boş → `UNKNOWN`; `A2`+`d>0` → `CIFT_SAYIM`; `A1` → çalışır (`K6d`) | ✅ |
| 19 | `TVK-N7` | `kanal_karmasi` `null` → `KARMA_UNKNOWN`, birleşik çıktı **yok** (`K9c`) | ✅ |
| 20–24 | `ROUNDTRIP::*` | **ANA ROUND-TRIP** — 5 farklı yapılandırmada `fark = 0,00000000` | ✅ |
| 25 | `INV::LEDGER_UNIQUENESS` | aynı `kalem_kimligi` iki kez → istisna (`K6`) | ✅ |
| 26 | `INV::METADATA` | `OK` / `BLOCKED_INPUT`(8 eksik alan) / `EXCLUDED_WITH_REASON` | ✅ |
| 27 | `INV::TEST_FIXTURE` | fixture dosyası **ve** `status: TEST_FIXTURE` **reddedilir** | ✅ |
| 28 | `INV::BLOCKED_ENVANTERI` | 15 kalem → 15 `BLOCKED_INPUT`, `toplam_dusulen = 0` | ✅ |
| 29 | `INV::SCALE_MONOTONICITY` | `F_total` yoksa `f` **`BLOCKED_INPUT`**, sessiz `0` değil | ✅ |
| 30 | **`INV::L6_ZINCIRDE_YOK`** | `L5_max` sabitken `d`/`f` değişse de `L8_geri` **799,0000** kalır | ✅ |

### 3.2 Ana round-trip — beş yapılandırma

```
L8 -> (kanal K1..K5) -> L5_max -> (-L5 kalemleri) -> L4_econ
   -> (R7: -OTV, -KKDF, -X_pre, /(1+g)) -> MAX_CIF
MAX_CIF -> (ileri: +GV +KKDF +OTV +X_pre) -> L4_econ -> (+L5) -> L5_max
        -> (R8-K: K1' K2' K3') -> L8_geri
```

| Yapılandırma | `MAX_CIF` | `L8_geri` | **fark** |
|---|---|---|---|
| `TVK-1` (CHAIN, μ=0, f=6) | 272,8306 | 799,000000 | **0,00000000** |
| `TVK-P1` (μ=%20, matrah `L6`) | 200,4574 | 799,000000 | **0,00000000** |
| `TVK-P2` (μ=%20, matrah `L7_EFF`) | 206,2473 | 799,000000 | **0,00000000** |
| `TVK-P3` (μ=%20, matrah `L5_MARKUP`) | 217,3445 | 799,000000 | **0,00000000** |
| `TVK-3` (HoReCa, `k=3,0`) | 87,8769 | 799,000000 | **0,00000000** |

> `μ ≠ 0` kolu **ilk kez** test edildi (`T-942` kriter #5, `T-944`,
> `T-616` kriter #3). TUR 2.5'e kadar tüm baz koşularda `μ = 0` idi ve
> `R5`'in katkı payı terimi **hiç çalıştırılmamıştı.**

### 3.3 Tüm koşu üzerinde `R8-K`

```
country-buying-ceilings.csv : 2700 satir
R8   (vergi bacagi) round-trip BASARISIZ satir sayisi : 0
R8-K (kanal bacagi) round-trip BASARISIZ satir sayisi : 0      <-- YENI
```

CSV'ye üç yeni sütun eklendi (`T-942` kriter #3):
**`R8K_ROUNDTRIP_OK`**, **`BLOCKED_INPUT_COUNT`**, ve `STATUS` damgalandı.

### 3.4 Regresyon — eski testler

`test_ters_model.py` (`TV-1`…`TV-10`, vergi bacağı): **10/10 GEÇTİ**.

---

## 4. BU TURDA MODELDE BULUNAN / DÜZELTİLEN HATALAR

| # | Bulgu | Nerede | Yön | Durum |
|---|---|---|---|---|
| **M-1** | `T-942`'nin `R8-K` spesifikasyonu **tersten çalışıyor** — kodlansaydı `R5` düzeltmesini geri alacaktı | `T-619` | **projenin lehine** (hatayı mühürlerdi) | ✅ **DÜZELTİLDİ**, negatif vektör olarak kilitlendi |
| **M-2** | `f_per_bottle` **girdi** olarak taşınıyordu; `Q` değişince sabit kalıyordu | `K7` | lehe | ✅ **TÜREVE çevrildi** (`F_total/Q`); `F_total` yoksa `BLOCKED_INPUT` |
| **M-3** | `d` tek homojen skalerdi; sepetin en az yarısı **sabit tutarlı** | `K8` | lehe | ⚠ `d_var`+`D_fix` **ayrımı kuruldu**, `D_fix` girdisi **yok** → `BLOCKED_INPUT` |
| **M-4** | `μ`'nun matrahı hiçbir yerde gerekçelendirilmemişti ve `μ=0` olduğu için **hiç test edilmemişti** | `K5` | aleyhe | ✅ Üç matrah **kodlandı ve test edildi**; `μ≠0` & matrah `null` → **`UNKNOWN`** |
| **M-5** | `listeleme_bedeli_f` **hem `L5` kaleminde hem kanal bacağında** duruyordu | `K6` | — | ✅ `L5`'ten **kaldırıldı** (çift kayıt riski); tek yeri kanal bacağı |
| **M-6** | Vade finansmanı modelde **hiç yoktu** ve düşünüldüğü matrah `L6` idi | `K12` | lehe | ⚠ `L6_gross` **hesaplanıyor ve test ediliyor**; maliyet satırı `BLOCKED_INPUT` (`makro.finansman_orani = null`) |
| **M-7** | `Q_ithal` ile `Q_satilan` aynıydı | `K11` | lehe | ⚠ **Ayrıldı**; `r=None` → `FIRE_SIFIR_VARSAYILDI` bayrağı |
| **M-8** | Gözetim uyarı metni **artık yanlıştı** (`alt sınırla test edilmedi`) | `T-171` | — | ✅ Metin `vergi.yaml`'dan **okunuyor**; `N/A` dalı eklendi |
| **M-9** | `%22,7` rakamı **tam kısıt** varsayımıydı | `T-171` | — | ✅ Üç çıktıda **düzeltildi**; 7846 **kısmi** kısıt getirir |
| **M-10** | 26 kalem **sessizce `0`** geçiyordu | GÖREV 1 | lehe | ✅ **`BLOCKED_INPUT`** mimarisi |

> ### BULGU 4.A — HATALARIN YÖNÜ
> Yukarıdaki on kalemin **altısı projenin lehine** çalışıyordu.
> `kanal-marj-uzmani`'nın tespiti (`12 hatanın 6'sı lehe`) bu turda
> **doğrulanmıştır.** *Lehe çalışan hata, aleyhe çalışandan daha uzun yaşar.*

---

## 5. TAVANLAR YENİDEN HESAPLANDI MI? — **HAYIR**

**Net cevap: `MAX_CIF_TRY` değerlerinin hiçbiri değişmedi.**

Bit-düzeyinde doğrulandı: TUR 2.5 CSV'si ile TUR 3A CSV'si
**ilk 22 sütunda 2.700 satırın 2.700'ünde birebir aynıdır**
(`cols 0-21 diff: 0`). Değişen tek şey damga sütunlarıdır:

| Sütun | TUR 2.5 | TUR 3A |
|---|---|---|
| `MAX_CIF_TRY_UPPER_BOUND` … `IMPLIED_BREAKEVEN_*` (22 sütun) | — | **DEĞİŞMEDİ** |
| `R8K_ROUNDTRIP_OK` | *(yoktu)* | **`EVET` × 2.700** |
| `BLOCKED_INPUT_COUNT` | *(yoktu)* | `26` / `29` / `31` |
| `STATUS` | `MODEL_DERIVED_UPPER_BOUND` | **`DRAFT_..._BLOCKED_INPUT`** |

**Neden değişmedi:**
1. KDV `(A) CONFIRMED` → `MAX_CIF` etkisi **0,00 TL/şişe** (`T-171`).
2. Gözetim `NO APPLICABLE MEASURE` → alt sınır yok, **üst sınır değişmez**.
3. Yapısal düzeltmelerin (`T-613`/`T-614`/`T-615`) **girdisi yok** →
   `BLOCKED_INPUT`; **tahminle doldurulmadı.**

---

## 6. PRIMARY `799` HEDEFİ DEĞİŞTİ Mİ? — **HAYIR**

`799,90 TL` **PRIMARY** hedefi bu turda **değişmedi** ve
`TGT_799 · ES · CHAIN · BASE · 5.000 şişe · DOC_OK` tavanı
**272,83 TL/şişe** olarak **aynen durmaktadır.**

> **Ama tavanın ANLAMI değişti.** Aynı sayı artık şu damgayı taşıyor:
> *"26 kalem `BLOCKED_INPUT`'tur; hiçbiri `0` sayılmamıştır ama hiçbiri de
> hesaba girmemiştir."* `kanal-marj-uzmani`'nın ölçtüğü büyüklükler
> (`K7` 38,00 + `K11` 19,38 + `K12` 27,55 ≈ **85 TL/şişe**, tavanın **%31'i**)
> bu 26 kalemin **içindedir** ve **hepsi tek yönlüdür: aşağı.**
>
> Yani `272,83` bir tahmin değil, bir **üst sınırın üst sınırıdır.**

---

## 7. `TEST_FIXTURE` DİSİPLİNİ

| Katman | Uygulama |
|---|---|
| **Dosya adı** | `80-model/inputs/TEST_FIXTURE-kanal-test-vektorleri.yaml` |
| **Yükleyici kilidi** | `kalem_defteri.guvenli_girdi_yukle()` adında `TEST_FIXTURE` geçen dosyayı **`FixtureSizintisi` istisnasıyla reddeder** |
| **Değişken adı** | `TEST_FIXTURE_yukle()`, `TEST_FIXTURE_VEKTORLER`, `TEST_FIXTURE_f_per_bottle`, `TEST_FIXTURE_F_total`, `TEST_FIXTURE_r`, `TEST_FIXTURE_m_dist` |
| **Status kilidi** | `status: TEST_FIXTURE` taşıyan kalem üretim defterine giremez (`MaliyetKalemi._fixture_denetimi`) |
| **Çıktı** | Test başlığında ve bu raporda açıkça yazılı |
| **Test** | `INV::TEST_FIXTURE` — her iki kilidi de doğrular ✅ |

**Sentetik olan değerler (beşi):** `f = 6,00` · `F_total = 300.000` ·
`r = 0,05` · `μ = 0,20` · `m_dist = 0,15`.
**Sentetik OLMAYANLAR:** `v = 0,20` (`vergi.yaml`, FACT), `m = 0,25` /
`d = 0,08` (`kanal.yaml` BASE, ASSUMPTION), `L8 = 799` (`senaryolar.yaml`,
INVESTOR_ASSUMPTION). Bunlar fixture dosyasında **ayna (`*_MIRROR`)**
olarak işaretlidir ve **oradan okunmazlar.**

Beklenen değerlerin **hiçbiri uydurulmamıştır**:
`70-kanal/kanal-bacagi-hata-listesi.md` ve
`kanal-katman-matrah-haritasi.md` §6.2'den **birebir aktarılmıştır**.
Kaynak bir **spesifikasyondur**, bir kanıt değildir — ve tam da bu yüzden
`TEST_FIXTURE`'dır.

---

## 8. HÂLÂ `BLOCKED` KALAN KALEMLER

| Grup | Adet | Kim kapatacak |
|---|---|---|
| `kanal.yaml → blocked_envanteri` `B-1`…`B-15` | **15** | `gumruk-vergi-uzmani` (2) · `kanal-marj-uzmani` (2) · `navlun-lojistik` (1) · yatırımcı (1) · **TUR 7 gerçek görüşme (9)** |
| `L5` tutarı `UNKNOWN` | **8** | `navlun-lojistik-uzmani` (5) · `gumruk-vergi-uzmani` (1) · `kanal-marj-uzmani` (1) · yatırımcı/`makro.yaml` (1) |
| Kanal bacağı yapısal | **3** | `kanal-marj-uzmani` + TUR 7 |
| Tekel/HoReCa'ya özgü "sıfırlar" | **3 / 5** | TUR 7 |

**Hiçbiri bu turda tahminle doldurulmadı.** Doldurulabilecek olanlar
girdi bekliyor; ticket'ları açık.

---

## 9. YAPILMAYANLAR (bilerek)

- İleri kârlılık modeli, contribution margin, break-even, EBITDA, ROI, IRR
- `peak_cash_requirement` **sayısal** hesabı — `L6_gross` matrahı **kuruldu
  ve test edildi** ama `makro.finansman_orani` ve `odeme_vadesi_gun` girdisi
  bağlanmadı → sayı üretilmedi
- Tedarikçi tavsiyesi, ülke sıralaması değişikliği
- Herhangi bir yeni marj, oran, tutar veya kanıt
- Dışarıya iletişim, nihai yatırım kararı

---

## 10. DEĞİŞEN / EKLENEN DOSYALAR

| Dosya | Durum |
|---|---|
| `80-model/engine/kalem_defteri.py` | **YENİ** — metadata sözleşmesi, damgalar, `LEDGER_UNIQUENESS`, `ZERO_PARITY` |
| `80-model/engine/kanal_bacagi.py` | **YENİ** — `K1..K6`, **doğru `R8-K`**, `T-942` negatif vektörü, `KARMA_UNKNOWN` |
| `80-model/engine/test_model_butunlugu.py` | **YENİ** — 30 test |
| `80-model/inputs/TEST_FIXTURE-kanal-test-vektorleri.yaml` | **YENİ** — sentetik, üç katmanlı kilitli |
| `80-model/engine/ters_model.py` | **DEĞİŞTİ** — `R8-K`, μ matrah kilidi, md.36 koşullu dalı, gözetim metni, kalem defteri |
| `80-model/engine/calistir_tur25.py` | **DEĞİŞTİ** — L5 metadata, `R8K_ROUNDTRIP_OK` + `BLOCKED_INPUT_COUNT` sütunları |
| `80-model/outputs/country-buying-ceilings.csv` | **YENİDEN ÜRETİLDİ** — 22 sayısal sütun **birebir aynı**, 3 damga sütunu eklendi |
| `80-model/outputs/reverse-price-model.md` §11 | **DÜZELTİLDİ** — gözetim (`T-171`) |
| `80-model/outputs/rapor-tur25-finans.md` | **DÜZELTİLDİ** — `%22,7` (`T-171`) |
| `80-model/outputs/sweet-spot-analizi.md` | **DÜZELTİLDİ** — risk #7 kapandı (`T-171`) |

---

## Bu bulguyu ne çürütür?

### 1. Hangi TEK girdinin yanlış olması sonucu tersine çevirir?

**`kanal-katman-matrah-haritasi.md` §9'un kapalı formül setinin kendisi.**
Bu turda kurulan bütün doğrulama mimarisi o spesifikasyonun **doğru
olduğunu varsayar** ve onu **test etmez** — onunla test eder.
`R8-K`'nın kanıtladığı tek şey **iç tutarlılıktır**: model kendi
cebriyle çelişmiyor. **Cebrin gerçeğe karşılık gelip gelmediğini
kanıtlamaz.** `L7_eff = L6·(1−d) − f` denklemi ticari gerçekte böyle
işlemiyorsa, 30/30 geçen test **yanlış bir dünyayı tutarlı biçimde**
tarif eder. Bu, `T-942`'nin uyardığı tuzağın **bir üst katıdır**: o
"doğrulama yok" diyordu; buradaki risk **"doğrulama var ama yanlış şeyi
doğruluyor"**.

**İkinci aday: `d`'nin matrahının `L6` olduğu tespiti.** `kanal-marj-uzmani`
kendisi işaretledi: `CRM/B2B` kaleminin matrahı **"kasa çıkışı cirosu"**,
yani `L8` olabilir (`B-8`). Öyleyse `d·L6` **sistematik olarak eksik
sayımdır** (çünkü `L8 > L6`) ve `R8-K` bunu **göremez** — çünkü `R8-K`
`d`'yi zaten `L6` matrahında varsayıyor. **Bir round-trip, kendi
varsayımını test edemez.**

### 2. Modelde çift sayım riski nerede?

| Yer | Risk | Bugünkü durum |
|---|---|---|
| **`K6a`** `d` içindeki lojistik bedeli ↔ `L5`'teki TR-içi lojistik | Teslim noktası tanımı **hiçbir yerde yazılı değil** | `B-13` / `T-618` **AÇIK** — `LEDGER_UNIQUENESS` bunu **yakalayamaz**, çünkü iki kalemin `kalem_kimligi` farklı; **aynı ekonomik olay, iki ad** |
| **`K6d`** `m_dist` ↔ `d + f` | MODEL A'da ikisi birden bizde varsayılıyor | Engine artık `d_kimde` boşsa **`UNKNOWN` dönüyor** ✅ ama `A1`/`A2` seçimi için **kanıt yok** |
| **`K6b`** `d` içindeki erken ödeme iskontosu ↔ vade finansman satırı | İkisi **birbirinin alternatifi**, toplanamaz | İkisi de bugün `BLOCKED_INPUT` → risk **uykuda** |
| **`K6c`** üreticiden alınan pazarlama katkısı ↔ `f` | Aynı para hem gelir hem gider | `T-605` **AÇIK** |
| **`L3` ↔ `L5`** | `L3` bileşenleri `L5`'te zaten düşülü | ✅ `EXCLUDED_WITH_REASON` ile kapatıldı |

> **En sinsi olanı `K6a`'dır ve bu turda kapatılamadı.**
> `LEDGER_UNIQUENESS` yalnızca **aynı isimli** kalemi yakalar. **Aynı
> ekonomik olayın iki farklı isimle iki satırda durması** bir isim
> denetiminin göremeyeceği bir hatadır. Bunu ancak `payer` + `receiver` +
> `layer` üçlüsünün **çakışma denetimi** yakalayabilir — ve o denetim
> **yazılmadı**, çünkü `BLOCKED` kalemlerin `payer`/`receiver` alanları
> zaten boş.

### 3. Hangi ASSUMPTION'lar sonucu taşıyor?

| Assumption | Nerede | Çökerse |
|---|---|---|
| `m_retail = %25` (BASE) | `kanal.yaml`, çapa **Migros tüm-kategori %24,31 — şarap DEĞİL** | `m = %35`'te `MAX_CIF` **272,83 → ~176** (`−%35`). Kararın tamamı bu tek ASSUMPTION üzerinde duruyor. |
| `d = %8` (BASE) | `kanal.yaml`, **seviye kanıtı YOK** — tek dayanak "en az 6 kalem var" | `d = %18`'de tek başına `−85 TL/şişe` mertebesinde |
| `L8 = 799` PRIMARY | yatırımcı girdisi | Hedef `699`'a inerse tavan **~%20 düşer** |
| ÖTV `λ = 1` (2027) | `otv_zaman_serisi`, **açık bayrakla** | Yİ-ÜFE ile `λ = 1,3` olursa `MAX_CIF` **−10,7 TL** (`53,4519 · 0,3 / 1,5`) |
| KDV `(A) CONFIRMED` | `T-947`, `ttl 30d` — **2026-09-09'da bayatlıyor** | Tetikleyici doğarsa **kısmi** kısıt; `D` girdisi yok → model `UNKNOWN` döner |
| **`BLOCKED` kalemlerin `0` olmadığı ama modele de girmediği** | bu turun kendi mimarisi | ⚠ **Bu bir ASSUMPTION değil, bir SUNUM KARARIDIR.** Sayı hâlâ 26 kalem eksik hesaplanıyor. Damga bunu **görünür** kılar, **düzeltmez.** |

### 4. Bu turun kendi en zayıf noktası

**30/30 geçen bir test paketi, bir güven kaynağı olduğu kadar bir risk
kaynağıdır.** `T-942`'nin asıl dersi *"test yoktu"* değil, *"yanlış test
hatayı mühürler"*di. Bu turda yazılan 30 testin **tamamı aynı ajanın
(bu ajanın) kendi cebir anlayışına** dayanıyor ve beklenen değerlerin
tamamı **tek bir kaynaktan** (`kanal-marj-uzmani`'nın spesifikasyonu)
geliyor. **Bağımsız bir ikinci uygulama yoktur.**

Tek gerçek bağımsızlık kaynağı `INV::L6_ZINCIRDE_YOK` testidir — çünkü o
bir sayıyı değil bir **yapısal özelliği** (`L6`'nın zincirde bulunmaması)
sınar ve beklenen değeri spesifikasyondan almaz.
**`seytanin-avukati` saldırısına ilk bu paket açılmalıdır.**
