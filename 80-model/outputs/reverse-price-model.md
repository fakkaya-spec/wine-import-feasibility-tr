# TERS FİYAT MODELİ — TARGET SHELF PRICE → AZAMİ SATIN ALMA FİYATI

```yaml
belge:              reverse-price-model
ajan:               finans-fizibilite
tur:                TUR 2.5 — REVERSE TARGET MODEL
tarih:              2026-08-10
durum:              DRAFT                      # APPROVED DEGIL — CLAUDE.md §5
cikti_etiketi:      TARGET / MODEL_DERIVED / UPPER_BOUND
yeni_arastirma:     YOK                        # bu ajan veri URETMEZ
yeni_evidence:      YOK                        # 10-evidence/ dokunulmadi
girdi_yaml_yazildi: HAYIR                      # 80-model/inputs/* salt okundu
motor:              80-model/engine/{otv_zaman_serisi,ters_model,calistir_tur25}.py
birim_test:         10/10 GECTI (TV-1..TV-10)
r8_roundtrip:       2.700/2.700 satirda GECTI (max fark < 1e-24 TL)
```

> ## ⛔ BU ÇIKTI `DRAFT`'TIR — `APPROVED` DEĞİLDİR
>
> `impact: CRITICAL` açık ticket sayısı **7** (`T-104`, `T-301`, `T-304`,
> `T-466`, `T-601`, `T-912` + bu turda açılan `T-851`, `T-852`).
> CLAUDE.md §5 gereği bu koşulda finans modeli çıktısı **en fazla `DRAFT`**
> olabilir. `T-921` ve `T-751` bu belgeyle **cevaplanmıştır** (§1) — ama
> tek başlarına gate açmazlar.

> ## ⛔ BU BELGEDEKİ HİÇBİR SAYI BİR FİYAT DEĞİLDİR
>
> Ters modelden çıkan her değer **`TARGET` / `MODEL_DERIVED`**'dır.
> **`FACT` değildir. `QUOTE` değildir. Bir tedarikçi teklifi değildir.**
> Hepsi bir **yatırımcı hedefinden (`INVESTOR_ASSUMPTION`)** geriye doğru
> türetilmiştir ve **iki bağımsız nedenle ÜST SINIRDIR** (§3.4).

---

## 0. GİRDİ ENVANTERİ — evidence_id ve STATUS DAĞILIMI

### 0.1 Modele fiilen giren girdiler

| # | Girdi | Değer | status | tier | evidence_id | Sahibi |
|---|---|---|---|---|---|---|
| 1 | KDV oranı `v` | %20 | **FACT** | T2 | `EV-2026-08-09-118` | gümrük-vergi |
| 2 | GV oranı — AB (ES/PT/IT/FR) | %50 **KOŞULLU** | **FACT** | T1 | `EV-2026-08-09-103` | gümrük-vergi |
| 3 | GV oranı — Şili | %50 **KOŞULLU** | **FACT** | T1 | `EV-2026-08-09-105` | gümrük-vergi |
| 4 | GV oranı — DÜ (ZA/AU/US/AR) | %70 | **FACT** | T1 | `EV-2026-08-09-104` | gümrük-vergi |
| 5 | GV oranı — Moldova | %70 (**DÜ fallback**) | **FACT** | T1 | `EV-2026-08-10-165` | gümrük-vergi |
| 6 | ÖTV maktu çapa | 71,2692 TRY/lt · eff **2026-07-03** | **FACT (çapa) / hedef tarihte GEÇERSİZ** | T2 | `EV-2026-08-09-111` | gümrük-vergi |
| 7 | KKDF oranı / peşinde 0 | 0 | **FACT** | T1 | `EV-2026-08-09-119` | gümrük-vergi |
| 8 | İthalat KDV'si indirilebilir | ekonomik maliyet **0** | **FACT** | T1 | `EV-2026-08-10-101/-102/-103` | gümrük-vergi |
| 9 | Bandrol birim bedeli | 2,36073 TRY/şişe (KDV hariç) | **FACT** | T1 | `EV-2026-08-09-213` | mevzuat-ruhsat |
| 10 | Gözlenen TR ithalat CIF birim değeri | USD/litre, ülke bazlı | **FACT** | T3 | `EV-2026-08-09-405` | global-sourcing |
| 11 | Kendi dağıtım personel tabanı | 40.214,03 TRY/ay/kişi | **FACT** | T2 | `EV-2026-08-10-621` | kanal-marj |
| 12 | TADAB hizmet bedeli | 0,1587 TRY/şişe | ESTIMATE | — | `EV-2026-08-09-235` | mevzuat-ruhsat |
| 13 | Ruhsat sabit maliyeti (ilk yıl) | 150.839 / 253.372 TRY | ESTIMATE | — | `EV-2026-08-09-234` | mevzuat-ruhsat |
| 14 | TR-içi lojistik TRY/şişe (LCL) | 2,60–4,99 (5k) … 0,84–1,82 (100k) | ESTIMATE | — | `EV-2026-08-10-329` (+ `-301…-311`) | navlun-lojistik |
| 15 | Şişe hacmi | 0,75 lt | **ASSUMPTION** | — | `EV-2026-08-10-116` | kapsam kararı |
| 16 | `X_pre` | 0 TRY/şişe | **ASSUMPTION** | — | vergi.yaml türetme | gümrük-vergi |
| 17 | Ödeme şekli = peşin (KKDF = 0) | — | **ASSUMPTION** (n=1 gözlem) | — | `EV-2026-08-10-451` | global-sourcing |
| 18 | `m_retail` zincir | 18 / 25 / 35 % | **ASSUMPTION** | — | çapa `EV-2026-08-10-616` | kanal-marj |
| 19 | `m_tekel` | 12 / 18 / 25 % | **ASSUMPTION** (çapasız) | — | `EV-2026-08-10-620` (negatif) | kanal-marj |
| 20 | `k_horeca` | 2,0 / 3,0 / 5,0× | **ASSUMPTION** | T5 | `EV-2026-08-10-618` | kanal-marj |
| 21 | `d` geri akan bedeller (zincir) | 3 / 8 / 18 % | **ASSUMPTION** | — | çapa `EV-2026-08-10-612` | kanal-marj |
| 22 | Hedef raf fiyatı merdiveni | 599/699/799/899/999 KDV dahil | **INVESTOR_ASSUMPTION** | — | **YOK — bir dış olgu değildir** | yatırımcı |
| 23 | `model_hedef_tarihi` | 2027-04-01 (EARLY/BASE/LATE) | **INVESTOR_ASSUMPTION** | — | **YOK** | yatırımcı |

### 0.2 Modele GİREMEYEN, `0` alınan veya `UNKNOWN` bırakılan girdiler

| # | Girdi | Model davranışı | Yön etkisi | Bloke eden |
|---|---|---|---|---|
| 1 | `fx` (USD/TRY, EUR/TRY) | **`null`** — çevrim YAPILMADI | FOB/EXW **UNKNOWN** | `T-912`, `T-852` |
| 2 | Gümrük beyan kuru kuralı | **UNKNOWN** | aynı | `T-911` |
| 3 | Varış local charge (THD/devanning/CFS/ardiye) — **USD** | **0 alındı** | `MAX_CIF` **YUKARI** | `T-912` |
| 4 | Menşe local charge — **EUR** | **0 alındı** | `MAX_CIF` **YUKARI** | `T-312`, `T-912` |
| 5 | Müşavirlik CIF kademesi (%0,3) | **0 alındı** | `MAX_CIF` **YUKARI** | CIF USD gerekir |
| 6 | Listeleme bedeli `f` | **0 alındı** | `MAX_CIF` **YUKARI** | `T-604` |
| 7 | `d` (tekel + HoReCa) | **0 alındı** | `MAX_CIF` **YUKARI** | `T-856` |
| 8 | Fire/zayi oranı ve `f × KDV_ithal` | **0 alındı** (RC5 açığı) | `MAX_CIF` **YUKARI** | `T-314` |
| 9 | Antrepo bekleme maliyeti | **0 alındı** | `MAX_CIF` **YUKARI** | `T-301` (CRITICAL) |
| 10 | Bandrolleme operasyon maliyeti | **0 alındı** | `MAX_CIF` **YUKARI** | `T-314` |
| 11 | Devreden KDV **finansman maliyeti** (RC4) | **0 alındı** | `MAX_CIF` **YUKARI** | `makro.finansman` `null` |
| 12 | Gözetim eşiği | **`null`** — alt sınır testi YAPILMADI | tavan test EDİLMEDİ | `EV-2026-08-09-125` |
| 13 | 2027 ÖTV tutarı (`λ`) | **FUTURE_UNKNOWN** — λ=1 çapası | `MAX_CIF` **YUKARI** | `T-104` |
| 14 | Dış distribütör marjı | **UNKNOWN** — parametrik grid | `MAX_CIF` **YUKARI** | `T-604` |
| 15 | İthalatçı katkı payı eşiği | **INVESTOR_DECISION_REQUIRED** | `MAX_CIF` **YUKARI** | `OQ-901`, `T-851` |
| 16 | Gerçek EXW/FOB tedarikçi fiyatı | **`null`** | — | `T-466` (CRITICAL) |
| 17 | `l8_chain_retail` (gerçek zincir rafı) | **`null`** — merdiven **yerine geçmez** | — | `T-603`, `T-917` |
| 18 | İtalya navlunu (LCL **ve** FCL) | **UNKNOWN** | — | `T-916` |
| 19 | FCL navlunu (İspanya dışı 8 rota) | **UNKNOWN** | — | `T-304` (CRITICAL) |
| 20 | 10.000 şişe hacim senaryosu | **çalıştırılmadı** | — | `T-855` |

> **13 maliyet kaleminin 13'ü de aynı yönde saptırır: YUKARI.** Bu bir tesadüf
> değildir — hepsi bir **maliyettir** ve maliyetin sıfır alınması tavanı
> yükseltir. **Bu, `MAX_CIF_TRY`'nin neden bir tahmin değil ÜST SINIR olduğunun
> ikinci nedenidir** (birincisi λ=1, §3.4).

### 0.3 Status dağılımı (modele giren 36 girdi)

| status | adet | pay |
|---|---|---|
| `FACT` | **11** | %30,6 |
| `ESTIMATE` | 3 | %8,3 |
| `ASSUMPTION` | 7 | %19,4 |
| `INVESTOR_ASSUMPTION` | 2 | %5,6 |
| `UNKNOWN` | **11** | %30,6 |
| `FUTURE_UNKNOWN` | 1 | %2,8 |
| `INVESTOR_DECISION_REQUIRED` | 1 | %2,8 |

> **`FACT`'lerin tamamı vergi ve ruhsat bacağındadır. Ticari bacakta
> (fiyat, marj, dağıtım, kur) TEK BİR `FACT` YOKTUR.**

---

## 1. GÖREV 0 — `T-921` KAPANDI (P-1 KAPISI AÇILDI)

### 1.1 Teşhis doğrulandı

Başkanın tespiti **kodda birebir doğrulanmıştır**. TUR 2.5 öncesi tarama:

```
$ grep -rn "otv_maktu_zaman_serisi|son_gozlem_gecerlilik_ufku|BASE_DATE|asgari_maktu_tutar" \
       80-model/engine/*.py
  -> 0 eslesme
```

Tarihle ilgili tek satır `matrah_sirasi.py:217`'deki `is None` kontrolüydü ve
`model_hedef_tarihi = 2027-04-01` yazıldığı anda **fiilen susmuştu**.

### 1.2 Engine'e eklenenler

| # | Ekleme | Dosya | `T-921` kabul kriteri |
|---|---|---|---|
| 1 | `otv_maktu(t)` — `gozlenen_degerler` içinden `effective_date <= t` olan **en son** kaydı seçer | **`80-model/engine/otv_zaman_serisi.py`** (YENİ) | **#1 ✅** |
| 2 | **UFUK DENETİMİ** — `t > son_gozlem_gecerlilik_ufku` **ve** açık senaryo bayrağı yoksa → `UNKNOWN` + eksik girdi `otv_maktu_zaman_serisi.gelecek_degerler` | aynı dosya | **#2 ✅** |
| 3 | `engine_yasak` — `matrah_sirasi[sira=4].asgari_maktu_tutar` **doğrudan okunmaz**; çelişirse **seri esas** + uyarı | aynı dosya | **#3 ✅** |
| 4 | `model_hedef_tarihi_status != FACT` → çıktı `"INVESTOR_ASSUMPTION üzerinden"` etiketlenir (`T-153` kapsandı) | aynı dosya + `matrah_sirasi.py` | **#4 ✅** |
| 5 | Üç tarih senaryosu **ayrı ayrı**; `EARLY`/`LATE` **iki rejim ihtimaliyle**; ortalama **alınmaz** | `calistir_tur25.py` | **#5 ✅** |

### 1.3 Açık bayrak sözleşmesi

```python
otv_maktu(vergi_yaml, t="2027-04-01", otv_senaryo=None)
    -> status = UNKNOWN,  hesaplandi = False
       eksik  = "otv_maktu_zaman_serisi.gelecek_degerler = null ... (O-5, T-921)"

otv_maktu(vergi_yaml, t="2027-04-01", otv_senaryo="UPPER_BOUND_LAMBDA_1")
    -> status = UPPER_BOUND,  lambda = 1,  otv/sise = 53,4519
       ZORUNLU etiketler: O-2, O-3, O-5, O-6
       cikti alani adi:  cif_try_max_UPPER_BOUND      (cif_try_max DEGIL)

otv_maktu(..., otv_senaryo="PROJEKSIYON_ASSUMPTION", lambda=...)
    -> status = PROJEKSIYON_ASSUMPTION  (ASLA FACT)
```

**Fiilî doğrulama** (`python3 80-model/engine/hesap.py`):

```
EKSIK GIRDILER (21):
  - otv_maktu_zaman_serisi.gelecek_degerler = null. model_hedef_tarihi (2027-04-01)
    > son_gozlem_gecerlilik_ufku (2026-12-31) ve senaryolar.yaml'da SECILMIS bir
    OTV artis ASSUMPTION'i YOK -> engine UNKNOWN doner (O-5, T-921).
```

> **`T-921` → `ANSWERED`.** Kapanış kararı başkanındır.
> **2027 ÖTV tutarı bu belgede hiçbir yerde yazılmamış, tahmin edilmemiş veya
> türetilmemiştir.**

### 1.4 Birim test vektörleri — `T-751` kabul kriteri #2

`python3 80-model/engine/test_ters_model.py` → **10/10 GEÇTİ**
(beklenen değerlerin tamamı `vergi.yaml`'dan okunur, koda gömülmemiştir):

| TV | Beklenen | Gerçekleşen | ✔ |
|---|---|---|---|
| TV-1 | 97,6987 | 97,6987 | ✅ |
| TV-2 | 86,2048 | 86,2048 | ✅ |
| TV-3 | 0,88235 | 0,88235 | ✅ |
| TV-4 | KDV_ithal = 40,0000 (menşeden bağımsız) | 40,0000 | ✅ |
| TV-5 | l4_cash = 240,0000 = 1,20 × l4_econ | 240,0000 | ✅ |
| TV-6 | H1 yanlış=79,8814 / doğru=97,6987 | aynı **+ R8 yanlışı REDDETTİ** | ✅ |
| TV-7 | H1 yanlış=64,1952 / doğru=86,2048 | aynı **+ R8 yanlışı REDDETTİ** | ✅ |
| TV-8 | H3 yanlış=75,4765 / doğru=97,6987 (fark 22,2222) | aynı | ✅ |
| TV-9 | `mal mukabili` → **UNKNOWN** | `UNKNOWN`, cif=None | ✅ |
| TV-10 | bayraksız **UNKNOWN**; bayraklı 97,6987 + `UPPER_BOUND` | aynı, O-2/O-3/O-5/O-6 etiketli | ✅ |

**R8 round-trip:** 2.700 CSV satırının **2.700'ünde**
`|ileri(cif).L4_econ − L4_econ_max| < 0,01 TL`; en büyük fark **1e-24 TL**.

---

## 2. MODEL SÖZLEŞMESİ — KATMAN DİSİPLİNİ

### 2.1 Uygulanan zincir

```
L8  CONSUMER SHELF PRICE (KDV DAHIL, TARGET)
 |  R1  : / (1 + v)                       <- ZINCIRDEKI TEK KDV ISLEMI
L8_net
 |  R2  : x (1 - m_retail)                <- MARGIN ON SELLING PRICE (markup DEGIL)
L7  RETAILER PURCHASE PRICE (effective)   <- ithalatcinin FIILI NET HASILATI
 |  R4  : L6 = (L7 + f) / (1 - d)         <- FATURA fiyati (bilgi; L5 butcesi DEGIL)
 |  R5  : L5_max = L7_eff - mu x L6       <- DUZELTME, bkz. §2.2
L5  IMPORTER COST
 |  R6  : - bandrol - TADAB - ruhsat/hacim - TR_lojistik
 |        [ USD/EUR kalemleri 0 ALINDI -> UST SINIR ]
L4_econ  POST-TAX LANDED, KDV HARIC        <- l4_cash AYRI ALAN, TOPLANMAZ
 |  R7b : - OTV        (MAKTU  -> BOLMEDEN ONCE)
 |  R7c : - KKDF - X_pre (MAKTU -> BOLMEDEN ONCE)
 |  R7d : / (1 + g)   (ORANSAL -> EN SON)
L2  CIF TURKEY  =  cif_try_max_UPPER_BOUND
 |  R10 : - navlun(USD) - sigorta          <- fx null  => UNKNOWN
L1  FOB   = UNKNOWN
 |  R11 : - mense local charges (EUR)      <- fx null  => UNKNOWN
L0  EXW   = UNKNOWN
```

### 2.2 ⚠ R5'TE BULUNAN VE DÜZELTİLEN EKSİK SAYIM — MODELİN EN ÖNEMLİ TEK DÜZELTMESİ

**R5'in sahibi bu ajandır** (`vergi.yaml → ters_model_vergi_bacagi.adimlar[R5]`).
İlk uygulamada naif tanım kullanıldı ve **hatalıydı**:

```
NAIF (YANLIS):   L5_max = L6 x (1 - mu)
DOGRU:           L5_max = L7_eff - mu x L6
```

**Neden:** `d` (geri akan bedeller) ve `f` (listeleme bedeli)
**ithalatçının ödediği** bedellerdir — perakendeci ithalatçıya **hizmet
faturası** keser (`EV-2026-08-10-612`, Rekabet Kurulu 21-51/708-351 para.82).
İthalatçının **fiilî net hasılatı** `L6` değil, `L7_eff = L6(1−d) − f`'dir.

`L5_max = L6` alınırsa **`d × L6 + f` hiçbir yerde düşülmez** ve azami CIF
yukarı sapar.

**Büyüklüğü (799 TL · İspanya · CHAIN RETAIL · BASE · 5.000 şişe):**

| | `L5_max` | `MAX_CIF_TRY` |
|---|---|---|
| Naif (yanlış) | 542,7989 | **301,78** |
| **Düzeltilmiş** | **499,3750** | **272,83** |
| **Fark** | −43,42 | **−28,95 TL/şişe (−%9,6)** |

> **Bu hata `H1` (maktu ÖTV'nin bölmeye dahil edilmesi, −17,82 TL) ve
> `H3` (l4_cash ↔ l4_econ, −22,22 TL) hatalarından DAHA BÜYÜKTÜR ve
> `ters-model-vergi-bacagi.md` §6'nın beş hata listesinde YOKTUR** —
> çünkü o belge vergi bacağını kapsar, kanal bacağını değil.
> **Bu, ters modelin altıncı hatasıdır ve buraya kayda geçirilmiştir.**
>
> **Yönü de tehlikelidir:** hata **projenin lehine** çalışır (tavanı
> yükseltir), yani gözden kaçması **daha olasıdır** — tıpkı `H1`'in ters
> yönde muhafazakâr görünmesi gibi.

**Doğrulama:** düzeltmeden sonra `INDEPENDENT_TEKEL` (`d = 0`) ile
`CHAIN_RETAIL` (`d = %8`) tavanları **ayrışmıştır** (799 TL: 303,90 vs 272,83).
Düzeltmeden önce **neredeyse özdeştiler (< %1)** — bu, hatanın en görünür
belirtisiydi.

### 2.3 Hesaplanamayan katmanlar — açıkça

| Katman | Durum | Neden |
|---|---|---|
| **L3 PRE-TAX LANDED** | ⚠ **KISMİ / BİLGİ AMAÇLI** | CLAUDE.md §6'da L3 = CIF + vergi öncesi yurt içi masraflar. Ancak `ters-model-vergi-bacagi.md` §4.3 gereği bu masraflar **hiçbir vergi matrahına girmez** ve zincirde **L5 kalemi** olarak düşülür. L3 burada **yalnızca gösterilir**, ikinci kez düşülmez → **`C-851`** |
| **L1 FOB** | **UNKNOWN** | Navlun USD; `fx` `null` (`T-912`) |
| **L0 EXW** | **UNKNOWN** | Menşe local charge EUR; ayrıca 9 menşenin 8'inde **tutar da** `UNKNOWN` (`T-312`) |
| **L2 CIF (döviz)** | **UNKNOWN** | `MAX_CIF_TRY` hesaplanır; **döviz karşılığı hesaplanamaz** |

### 2.4 KDV — İKİ AYRI PERSPEKTİF (zorunlu)

| | **A) EKONOMİK MALİYET** | **B) NAKİT (cash_tax_timing)** |
|---|---|---|
| Sorusu | *Üreticiye en fazla kaç TL ödeyebilirim?* | *Kasada kaç TL olmalı?* |
| İthalat KDV'si | **0,00 TL/şişe** — indirilebilir (`EV-2026-08-10-101/-102/-103`) → **P&L'e girmez** | **Tam tutar** = `v × L4_econ_max` |
| Zincirdeki KDV işlemi | **Tek bölme** (R1: `L8/1,20`) | Ayrı örtü (R9) — zincire **girmez** |
| Ürettiği çıktı | `cif_try_max_UPPER_BOUND` | gümrükte peşin ödenen tutar |
| Ödeme anı | — | **beyanname tescilinde peşin** (`EV-2026-08-09-122`) |
| Mahsup anı | — | satış hızına bağlı; **iade EDİLMEZ** (`EV-2026-08-10-104`, RC6) |
| Gecikmenin bedeli | **finansman maliyeti — ayrı L5 satırı** (RC4), tutar `UNKNOWN` | `peak_cash`'i büyütür |

> **RC3 UYGULANDI:** iki perspektifin sayıları hiçbir tabloda toplanmamış,
> hiçbir satırda birlikte gösterilmemiştir. `l4_econ` ve `l4_cash` CSV'de
> **ayrı sütunlardır.**

**ÖTV için aynı zamanlama sorusu:** ÖTV de gümrükte **tescilde peşin** doğar
(`EV-2026-08-09-122`) ama **tahsilatı satışta, kanal vadesinden sonra** gelir
(zincir BASE 60 gün, STRESS 120 gün). Bandrol ise **hem gümrükten hem
satıştan önce** peşin ödenir (`EV-2026-08-09-214`) — zincirin **en erken
nakit çıkışıdır**.

---

## 3. ANA SONUÇ — `MAX CIF TRY` (ÜST SINIR)

### 3.1 Katman katman iz — tek örnek (denetlenebilirlik için)

**TGT_799 · İspanya · CHAIN RETAIL · BASE · 5.000 şişe · DOC_OK · g=0,50**

| Adım | İşlem | Sonuç (TRY/şişe) |
|---|---|---|
| — | `L8` hedef (KDV dahil, **INVESTOR_ASSUMPTION**) | **799,0000** |
| R1 | `/ (1+0,20)` | 665,8333 |
| R2 | `× (1 − 0,25)` — margin on selling price (markup karşılığı %33,33) | **L7_eff = 499,3750** |
| R4 | `L6 = (L7_eff + 0) / (1 − 0,08)` — **fatura fiyatı, bilgi** | *(542,7989)* |
| R5 | `L5_max = L7_eff − 0 × L6` — ithalatçı katkı **0** | **L5_max = 499,3750** |
| R6 | − bandrol 2,3607 − TADAB 0,1587 − ruhsat 30,1678 − TR loj. 3,9900 | **L4_econ_max = 462,6978** |
| R7b | − ÖTV **53,4519** (MAKTU, bölmeden ÖNCE) | 409,2459 |
| R7c | − KKDF 0 − `X_pre` 0 | 409,2459 |
| R7d | `/ (1 + 0,50)` (ORANSAL, EN SON) | **`cif_try_max_UPPER_BOUND` = 272,8306** |
| türev | GV = 272,8306 × 0,50 | 136,4153 |
| **R8** | `|ileri(272,8306).L4_econ − 462,6978|` | **0 < 0,01 ✅** |

**CASH VIEW (R9 — ayrı, toplanmaz):** `KDV_ithal = 92,5396` ·
`l4_cash_max = 555,2373` · `gümrükte nakden ödenen = 282,4067`

**Kullanılan evidence_id'ler:** `EV-2026-08-09-103`, `EV-2026-08-09-111`,
`EV-2026-08-09-118`, `EV-2026-08-09-213`, `EV-2026-08-09-234`,
`EV-2026-08-09-235`, `EV-2026-08-10-329`

### 3.2 5 HEDEF × 3 KANAL × 3 SENARYO — `g = 0,50` · 5.000 şişe · TRY/şişe

| Hedef (KDV dahil) | Kanal | LOW | BASE | HIGH |
|---|---|---|---|---|
| **599** | CHAIN RETAIL | 213,72 | **189,50** | 155,55 |
| 599 | INDEPENDENT/TEKEL | 233,69 | **212,79** | 188,83 |
| 599 | HoReCa *(menü fiyatı)* | 107,23 | **50,84** | **5,80** |
| **699** | CHAIN RETAIL | 259,27 | **231,16** | 191,66 |
| 699 | INDEPENDENT/TEKEL | 282,57 | **258,35** | 230,50 |
| 699 | HoReCa | 135,01 | **69,36** | 16,91 |
| **799** | CHAIN RETAIL | 304,83 | **272,83** | 227,78 |
| 799 | INDEPENDENT/TEKEL | 331,46 | **303,90** | 272,16 |
| 799 | HoReCa | 162,79 | **87,88** | 28,03 |
| **899** | CHAIN RETAIL | 350,39 | **314,50** | 263,89 |
| 899 | INDEPENDENT/TEKEL | 380,35 | **349,46** | 313,83 |
| 899 | HoReCa | 190,56 | **106,40** | 39,14 |
| **999** | CHAIN RETAIL | 395,94 | **356,16** | 300,00 |
| 999 | INDEPENDENT/TEKEL | 429,24 | **395,01** | 355,50 |
| 999 | HoReCa | 218,34 | **124,91** | 50,25 |

**Aynı tablo `g = 0,70` (DOC_FAIL veya tercihsiz menşe):** her hücre
**tam %11,765 düşer** (`1,50/1,70 = 0,88235` — §4.3).
Örn. 799/CHAIN/BASE: 272,83 → **240,73**.

### 3.3 `MAX_CIF` her zaman POZİTİF mi?

**Evet — tarandığı 2.700 kombinasyonun hiçbirinde `MAX_CIF` negatif değildir.**
Sıfıra en yakın hücre **HoReCa 5,0× / 599 TL / HIGH = 5,80 TL/şişe**'dir ve
**ithalatçı katkısı sıfırken bile** bu seviyededir (§6.4).

> **Başkanın "en güçlü çürütücü bulgu" hipotezi (`tur-25-preflight.md`)
> — *"999 TL'de bile ödenebilir CIF negatif veya sıfıra yakın çıkar"* —
> ÇÜRÜTÜLMÜŞTÜR.** Zincir ve tekel kanallarında beş basamağın beşinde de
> `MAX_CIF` **137–429 TL/şişe** bandındadır. Segment **aritmetik olarak
> imkânsız değildir.** Bu, bu turun en önemli tek sonucudur — ve bir
> **hipotezin çürütülmesidir**, bir "iyi haber" değil.

### 3.4 Neden `UPPER_BOUND` — iki bağımsız neden

| # | Neden | Yön | Büyüklük |
|---|---|---|---|
| **1** | **λ = 1** (ÖTV 2026-07-03 çapası). λ ≥ 1 olduğu için gerçek ÖTV **daha yüksek**, gerçek `MAX_CIF` **daha düşük** | ↓ | `Δ = −(λ−1) × 53,4519 / (1+g)`. λ=1,25 → **−8,91 TL**; λ=1,5625 → **−20,04 TL** (g=0,50) |
| **2** | **13 maliyet kalemi 0 alındı** (§0.2) | ↓ | Her **+1 TL/şişe** kalem → `MAX_CIF` **−0,667 TL** (g=0,50) / **−0,588 TL** (g=0,70) |

**Birleşik örnek** (5.000 şişe · 799 TL · CHAIN BASE, tavan **272,83**):

| Eklenen | Yeni tavan | Kayıp |
|---|---|---|
| Kendi dağıtım, **1 kişinin asgari ücret tabanı** | 208,49 | −64,34 |
| + ÖTV λ = 1,5625 | 188,45 | −84,38 |
| + distribütör marjı %15 (grid) | ~134 | −139 |
| + listeleme bedeli 10 TL/şişe | ~127 | −146 |

**Dört kalem tavanın %53'ünü siliyor.** Hiçbiri modele konmadı çünkü hiçbirinin
kanıtı yok — **ama koymamak da bir seçimdir ve bu seçim projenin lehinedir.**

---

## 4. ÜLKE BAZLI AZAMİ SATIN ALMA (GÖREV 6 — ANA ÇIKTI)

### 4.1 Özet — CHAIN RETAIL · BASE · 5.000 şişe · TRY/şişe

| Ülke | `g` | Senaryo | Kaynak | 599 | 699 | **799** | 899 | 999 |
|---|---|---|---|---|---|---|---|---|
| **ES** İspanya | 0,50 | DOC_OK | KOŞULLU_SAĞLANDI | 189,50 | 231,16 | **272,83** | 314,50 | 356,16 |
| ES | **0,70** | **DOC_FAIL** | KOŞULLU_DÜŞTÜ | 167,20 | 203,97 | **240,73** | 277,50 | 314,26 |
| **PT** Portekiz | 0,50 / **0,70** | DOC_OK / **DOC_FAIL** | aynı | 189,50 / 167,20 | 231,16 / 203,97 | **272,83 / 240,73** | 314,50 / 277,50 | 356,16 / 314,26 |
| **IT** İtalya | 0,50 / **0,70** | DOC_OK / **DOC_FAIL** | aynı | 189,50 / 167,20 | 231,16 / 203,97 | **272,83 / 240,73** | 314,50 / 277,50 | 356,16 / 314,26 |
| **FR** Fransa | 0,50 / **0,70** | DOC_OK / **DOC_FAIL** | aynı | 189,50 / 167,20 | 231,16 / 203,97 | **272,83 / 240,73** | 314,50 / 277,50 | 356,16 / 314,26 |
| **CL** Şili | 0,50 / **0,70** | DOC_OK / **DOC_FAIL** ⚠ | aynı — **aktarma riski `T-914`** | 189,50 / 167,20 | 231,16 / 203,97 | **272,83 / 240,73** | 314,50 / 277,50 | 356,16 / 314,26 |
| **ZA** G. Afrika | 0,70 | tercihsiz | KOŞULSUZ | 167,20 | 203,97 | **240,73** | 277,50 | 314,26 |
| **AU** Avustralya | 0,70 | tercihsiz | KOŞULSUZ | 167,20 | 203,97 | **240,73** | 277,50 | 314,26 |
| **US** ABD/California | 0,70 | tercihsiz | KOŞULSUZ | 167,20 | 203,97 | **240,73** | 277,50 | 314,26 |
| **MD** Moldova | 0,70 | tercihsiz | **DÜ FALLBACK** ⚠ | 167,20 | 203,97 | **240,73** | 277,50 | 314,26 |
| **AR** Arjantin *(ops.)* | 0,70 | tercihsiz | KOŞULSUZ | 167,20 | 203,97 | **240,73** | 277,50 | 314,26 |

> ⚠ **MD satırı `DU FALLBACK` etiketiyle üretilmiştir**: Moldova
> `mense_tarife_eslemesi.ulkeler` listesinde **satır olarak yoktur**.
> Engine `engine_okuma_kurali` adım 1'i uygulayıp %70'e düşmüştür.
> **Sonuç `EV-2026-08-10-165` ile uyumludur — yani fallback TESADÜFEN doğru
> cevabı vermiştir.** Bu bir doğrulama değildir → **`T-853`**.

**Tüm kombinasyonlar:** `80-model/outputs/country-buying-ceilings.csv`
(**2.700 satır** — 5 hedef × 15 ülke/gümrük senaryosu × 3 kanal × 3 senaryo
× 4 hacim; `MAX_FOB_*` ve `MAX_EXW_*` sütunları **`UNKNOWN`**).

### 4.2 En sert bulgu: **ülkeler arası tek fark `g`'dir**

Ters modelde menşe, `MAX_CIF_TRY`'yi **yalnızca `(1+g)` böleni üzerinden**
etkiler. ÖTV ve KDV **menşeden bağımsızdır** (`EV-2026-08-09-110`):

```
MAX_CIF_TRY, YALNIZCA IKI DEGER ALIR:
   g = 0,50  ->  A
   g = 0,70  ->  0,88235 x A
```

> **9 ülke için 9 farklı sayı YOKTUR — 2 farklı sayı vardır.**
> Ülkeler arası gerçek ayrışma **FOB seviyesinde** (navlun + menşe local
> charge) doğar ve o bacak **fx olmadan hesaplanamaz.** Yani `fx` yalnızca
> bir birim dönüşümü değil, **modelin ülke ayrıştırma gücünün ön koşuludur**
> (`T-852`).

### 4.3 Tercih kaybının kapalı formu

```
MAX_CIF(g=0,70) / MAX_CIF(g=0,50) = 1,50 / 1,70 = 0,88235
```

**Tercihli rejimi kaybetmek azami satın alma fiyatını TAM %11,765 düşürür —
hedef fiyattan, ÖTV'den, marjdan, hacimden ve navlundan BAĞIMSIZ olarak.**
Bu, modelin **hiçbir `UNKNOWN`'a bağlı olmayan tek sayısıdır.**

TL karşılığı (799 TL hedef, CHAIN BASE, 5.000 şişe): **−32,10 TL/şişe**.
Koşullar: `K3` (belge — `T-161`, `global-sourcing-kasifi`) ve `K4` (doğrudan
nakliyat — `T-163`/`T-914`, `navlun-lojistik-uzmani`); **ikisi de
`ASSUMPTION: true`'dur.**

### 4.4 FX olmadan hesaplanamayanlar (GÖREV 5)

| Alan | Durum |
|---|---|
| `MAX_CIF_TRY` | ✅ **HESAPLANDI** (üst sınır) |
| `MAX_CIF_TRY_PER_LITRE` | ✅ hesaplandı (`/0,75`) |
| `MAX_FOB_TRY` | ❌ **UNKNOWN** — navlun USD cinsinden, `fx` `null` |
| `MAX_EXW_TRY` | ❌ **UNKNOWN** — menşe local charge EUR cinsinden |
| `MAX_FOB_EUR` / `MAX_FOB_USD` | ❌ **UNKNOWN** |
| `MAX_EXW_EUR` / `MAX_EXW_USD` | ❌ **UNKNOWN** |
| FX LOW/BASE/HIGH alanları | **oluşturuldu, `UNKNOWN` bırakıldı** — `senaryolar.yaml → duyarlilik_eksenleri[FX]` min/base/max hepsi `null` |

**Tek adımlık açılış:** `fx` dolduğu anda
`MAX_FOB_FX = MAX_CIF_TRY/fx − navlun_USD/şişe` **anında** hesaplanır.
Navlun USD/şişe **9 rotanın 9'unda zaten elimizdedir**
(`EV-2026-08-10-301…-311`). **Eksik olan tek şey tarihli tek bir kur
kaydıdır** → `T-852`.

---

## 5. KANAL SENARYOLARI (GÖREV 2)

### 5.1 Margin ↔ markup — hiçbir yerde karıştırılmadı

| Kanal | Senaryo | `m` (**margin on selling price**) | **markup** `m/(1−m)` | çarpan |
|---|---|---|---|---|
| **A) CHAIN RETAIL** | LOW | %18 | **%21,95** | 1,220× |
| A | BASE | %25 | **%33,33** | 1,333× |
| A | HIGH | %35 | **%53,85** | 1,538× |
| **B) INDEPENDENT / TEKEL** | LOW | %12 | **%13,64** | 1,136× |
| B | BASE | %18 | **%21,95** | 1,220× |
| B | HIGH | %25 | **%33,33** | 1,333× |
| **C) HoReCa** | LOW | %50,0 *(eşdeğer)* | **%100,0** | **2,0×** |
| C | BASE | %66,7 *(eşdeğer)* | **%200,0** | **3,0×** |
| C | HIGH | %80,0 *(eşdeğer)* | **%400,0** | **5,0×** |

**Hepsi `ASSUMPTION` · `SENSITIVITY_ONLY`.** Tek kanıtlı çapa
`EV-2026-08-10-616` (Migros 2025 tüm-kategori %24,31) ve **şarap değildir**;
Rekabet Kurumu'nun alkol brüt marj analizi **kapsam dışı ve karartılmıştır**
(`EV-2026-08-10-611`).

### 5.2 HoReCa çarpanının uygulandığı katman — **DOĞRULANDI**

`kanal.yaml → duyarlilik_senaryolari.k_horeca_carpan`:
```
katmanlar:     "L7 -> L8_HORECA"
kdv_dahil_mi:  "menu fiyati KDV DAHIL; carpan KDV HARIC L7 uzerine uygulanir"
```
**Doğrulandı ve modelde birebir uygulandı:** `L7_horeca = L8_net / k`.

> ⚠ **YORUM UYARISI (bağlayıcı okuma kuralı):** HoReCa satırlarında hedef
> merdiven bir **MENÜ FİYATI** olarak yorumlanmıştır. Aynı şişe zincir
> rafında 799 TL ise HoReCa menüsünde 3,0× ile **~2.400 TL** olur.
> **HoReCa sütunu zincir sütunuyla aynı ürün konumlandırmasını temsil
> ETMEZ ve doğrudan karşılaştırılamaz.**

### 5.3 Korelasyon uyarısı uygulandı

`marj-vs-markup.md` §3.2 uyarısı — *"gerçek risk, üç parametrenin **aynı
yönde** kötüleşmesidir; **korelasyonlu** senaryo çalıştırılmalıdır"* —
**birebir uygulanmıştır:** `LOW` = m düşük **+** d düşük **+** lojistik düşük;
`HIGH` = üçü de kötü.

**Etkisi ölçüldü:** R5 düzeltmesinden sonra kanal marjı bandı artık
**modelin ikinci büyük eksenidir** (799 TL'de −45,06 / +32,00 TL) —
düzeltmeden önce yalnızca −10,67 / +14,31 görünüyordu. **Yani R5 hatası,
kanal riskinin büyüklüğünü de gizliyordu.**

### 5.4 `d` ve `f`'nin kanal bazında farklı ele alınması

| Kanal | `d` | `f` | Gerekçe |
|---|---|---|---|
| CHAIN RETAIL | **3/8/18 %** (ASSUMPTION, çapa `EV-2026-08-10-612`) | **0 — UNKNOWN** | `f` için güncel kamu kaynağı yok (`EV-2026-08-10-619` T5/2004 → modele giremez) |
| INDEPENDENT/TEKEL | **0 — UNKNOWN, 0 ALINDI** | **0** | 6585 m.6 zincir/büyük mağazayı hedefler; tek şubeli bayi kapsam dışı (`EV-2026-08-10-601`). **Yapısal olarak beklenmez ama `UNKNOWN`'dır** |
| HoReCa | **0 — UNKNOWN, 0 ALINDI** | **0** | Yerine yatırım/menü desteği geçer (`EV-2026-08-10-615`), tutar `UNKNOWN` |

> ⚠ **BU, TEKEL KANALINI YAPAY OLARAK İYİ GÖSTERİR.** R5 düzeltmesinden sonra
> tekel tavanı zincirden **%11,4 yüksektir** (799 TL: 303,90 vs 272,83) — ve
> bu farkın **tamamı** `d`'nin tekelde `0` alınmasından gelir.
> **İki kanal arasında ekonomik tercih modelden okunamaz** → **`T-856`**.

---

## 6. HACİM SENARYOLARI (GÖREV 8)

### 6.1 `MAX_CIF_TRY` — ES · CHAIN RETAIL · BASE · DOC_OK

| Hedef | **5.000** | **25.000** | **50.000** | **100.000** |
|---|---|---|---|---|
| 599 | 189,50 | 207,18 | 207,94 | 209,70 |
| 699 | 231,16 | 248,85 | 249,61 | 251,37 |
| **799** | **272,83** | **290,51** | **291,28** | **293,03** |
| 899 | 314,50 | 332,18 | 332,94 | 334,70 |
| 999 | 356,16 | 373,85 | 374,61 | 376,37 |

### 6.2 ⚠ ÖLÇEK EĞRİSİ 25.000'DEN SONRA **DÜZLEŞİYOR** — sebebi navlun DEĞİL

| Kalem (TRY/şişe) | 5.000 | 25.000 | 50.000 | 100.000 |
|---|---|---|---|---|
| TR-içi lojistik (LCL BASE) | 3,99 | 1,60 | 1,42 | 1,32 |
| **Ruhsat sabit maliyeti (ilk yıl)** | **30,17** | **6,03** | **5,07** | **2,53** |
| Bandrol + TADAB | 2,52 | 2,52 | 2,52 | 2,52 |
| **Toplam düşülen L5 (TRY)** | **36,68** | **10,15** | **9,01** | **6,37** |

> ### BULGU — RUHSAT KADEME SIÇRAMASI ÖLÇEK KAZANCINI YİYOR
> `ruhsat.yaml → toplam_ruhsat_sabit_maliyeti` **20.000 litre/yıl** eşiğinde
> kademe atlar: **150.839 TL → 253.372 TL** (`EV-2026-08-09-234`).
> 20.000 lt = **26.667 şişe** (0,75 lt `ASSUMPTION` üzerinden).
>
> - 5.000 → 25.000: `MAX_CIF` **+17,68 TL**
> - **25.000 → 50.000: yalnızca +0,77 TL** — ruhsat tabanı sıçradığı için
> - 50.000 → 100.000: **+1,75 TL**
>
> **Ölçek ekonomisinin %87'si ilk sıçramada (5k → 25k) gerçekleşir.**
> 25.000'in üstünde büyümenin `MAX_CIF` üzerindeki etkisi **ihmal
> edilebilirdir** ve bunun sebebi navlun değil, **bir ruhsat kademesidir**
> → **`T-858`**.

### 6.3 Navlun modu ve MOQ

| Hacim | Mod | Konteyner | MOQ uyumu | FCL fiyatı |
|---|---|---|---|---|
| **5.000** | **LCL** (11,2–12,0 CBM) | — | ⚠ **6.000 şişe/SKU MOQ'lu tedarikçiler (R1 Harland, R2 Danese) UYUMSUZ.** 3.000 (R3) ve 3.600 (R4) uyumlu | **UNKNOWN** (İspanya hariç, o da 4 kat bant) |
| **25.000** | LCL veya **2× 20DV** (HIGH'da 3) | 2–3 | tüm MOQ'lar uyumlu | **İspanya: 300 / 1.200 USD iki köşe. Diğer 8 rota: UNKNOWN** |
| **50.000** | LCL veya **3× 20DV / 3× 40HC** | 3–5 | uyumlu | aynı |
| **100.000** | LCL veya **5–6× 40HC** | 5–9 | uyumlu | aynı |

> ⛔ **FCL'DE BASE YOKTUR (`M-6`).** `C-311` açıktır: marketplace "from"
> 295–650 USD vs T5 blog 1.200–2.500 EUR → **4–5 kat fark, taraf seçilmedi.**
> Bandın **ortalaması alınmamıştır** ve alınamaz.
>
> ⚠ **`navlun-lojistik-uzmani` düzeltmesi modele işlendi:**
> *"5.000 → 100.000 arasında şişe başı lojistik 3–4 kat düşer"* iddiası
> **YALNIZ FCL için doğrudur.** LCL'de **USD bacağı yalnızca %12–14 düşer**;
> ölçek yalnızca **TRY (sabit) bacağını** seyreltir. Model LCL varsayımıyla
> koştuğu için **§6.2'deki düzleşme bu düzeltmenin doğrudan sonucudur.**

### 6.4 Yapısal taban — `MAX_CIF = 0` olan hedef raf fiyatı (5.000 şişe)

| Kanal | LOW | BASE | HIGH |
|---|---|---|---|
| CHAIN RETAIL | 129,86 | 144,21 | 168,24 |
| INDEPENDENT/TEKEL | 121,01 | 131,90 | 145,81 |
| **HoReCa** | 212,97 | 324,46 | **546,77** |

> **Bu fiyatların ALTINDA tedarikçi bedava verse bile model kapanmaz.**
> `g` bu tabloyu **değiştirmez** (CIF = 0 iken GV = 0) — bir hata değil,
> **maktu ÖTV'nin yapısal imzasıdır.**
>
> **En keskin sonuç:** HoReCa 5,0× senaryosunda yapısal taban **546,77 TL**.
> `TGT_599` bu tabanın **yalnızca 52 TL üstündedir** → 5,80 TL'lik `MAX_CIF`.
> **HoReCa'da 599 TL'lik bir menü fiyatı, 5× çarpan altında matematiksel
> olarak ölüdür.**

### 6.5 10.000 şişe senaryosu

`senaryolar.yaml → V10K` tanımlıdır ama **çalıştırılmamıştır**:
`lojistik-senaryolari-tur25.md` §4 tabloları 5.000/25.000/50.000/100.000
kapsar; 10.000 için **türetilmiş şişe başı lojistik verisi yoktur.**
**İnterpolasyon YAPILMAMIŞTIR** (uydurma olurdu) → **`T-855`**.

---

## 7. DAĞITIM MODELİ A / B (GÖREV 3)

### 7.1 MODEL A — IMPORTER → 3. TARAF DİSTRİBÜTÖR → RETAILER

> ## `DISTRIBUTOR_MARGIN_ASSUMPTION_REQUIRED`
>
> `kanal.yaml → dagitim_modeli.dis_distributor.marj_pct` → `min/base/max` =
> **`null`**, `status: UNKNOWN`, `evidence_id: null`.
> `kanal-marj-uzmani`: *"TUR 2'DE HİÇBİR KANITLI DEĞER BULUNAMAMIŞTIR ve
> UYDURULMAMIŞTIR."* **Ben de uydurmuyorum.** Aşağıdaki tablo bir **tahmin
> değil, saf duyarlılık gridi**dir; hiçbir noktası "beklenen" değildir.

**Yapı:** distribütör marjı `L6` cirosu üzerinden alınır ve ithalatçının
`L5` bütçesinden çıkar: `L5_max = L7_eff − m_dist × L6`.

`MAX_CIF_TRY` — ES · CHAIN RETAIL · BASE · 5.000 şişe · g=0,50 (TRY/şişe):

| Hedef | m_dist=0% *(=MODEL B)* | 5% | 10% | 15% | 20% | 25% | 30% |
|---|---|---|---|---|---|---|---|
| 599 | 189,50 | 175,93 | 162,37 | 148,80 | 135,24 | 121,68 | 108,11 |
| 699 | 231,16 | 215,34 | 199,51 | 183,68 | 167,85 | 152,02 | 136,19 |
| **799** | **272,83** | 254,74 | 236,64 | 218,55 | 200,46 | 182,36 | 164,27 |
| 899 | 314,50 | 294,14 | 273,78 | 253,42 | 233,07 | 212,71 | 192,35 |
| 999 | 356,16 | 333,54 | 310,92 | 288,30 | 265,67 | 243,05 | 220,43 |

**KATSAYI (kanıtlı, gridden bağımsız):** `Δ MAX_CIF / Δ m_dist = −L6/(1+g)`
→ 799 TL hedefte **her +1 puan distribütör marjı = −3,62 TL/şişe** (g=0,50) /
**−3,19 TL** (g=0,70).

> **`MODEL A ↔ MODEL B` KARŞILAŞTIRMASI YAPILAMAZ.** İki modelin farkı
> tamamen bu tek `UNKNOWN` sayının içindedir.
> **Not:** bu grid, §9.2'deki ithalatçı katkı payı gridiyle **sayısal olarak
> özdeştir** — çünkü ikisi de `L6` cirosu üzerinden yapılan aynı yapıdaki bir
> kesintidir. **Aynı anda ikisi birden uygulanırsa TOPLANIRLAR.**

### 7.2 MODEL B — IMPORTER → RETAILER (kendi dağıtım)

> **5.000 şişe senaryosunda SAHTE KESİNLİK ÜRETİLMEMİŞTİR.**
> `70-kanal/kendi-dagitim-senaryosu.md`: **58 alanın 48'i `UNKNOWN`**
> (kanıtlı dolu: 10).

**Kanıtlı taban:** 2026 asgari ücretin işverene toplam maliyeti, imalat dışı:
**40.214,03 TRY/ay/kişi** — `FACT`, T2, `EV-2026-08-10-621`.
**Bu bir TABANDIR, beklenen ücret DEĞİLDİR.**

**YALNIZCA personel tabanı — TRY/şişe:**

| Kişi | 5.000 | 25.000 | 50.000 | 100.000 |
|---|---|---|---|---|
| 1 | **96,51** | 19,30 | 9,65 | 4,83 |
| 2 | 193,03 | 38,61 | 19,30 | 9,65 |
| 3 | 289,54 | 57,91 | 28,95 | 14,48 |

**`MAX_CIF_TRY` üzerindeki etki** (`−X/(1+g)`, g=0,50):

| Kişi | 5.000 | 25.000 | 50.000 | 100.000 |
|---|---|---|---|---|
| 1 | **−64,34** | −12,87 | −6,43 | −3,22 |
| 2 | −128,68 | −25,74 | −12,87 | −6,43 |
| 3 | −193,03 | −38,61 | −19,30 | −9,65 |

> **5.000 şişe / 799 TL / CHAIN BASE'te tek kişilik ekip bile tavanı
> 272,83 → 208,49 TL'ye indirir (−%23,6).** Ve bu **yalnızca bir kişinin
> asgari ücret tabanıdır.**

**MODELDE `UNKNOWN` BIRAKILAN (uydurulmayan) MODEL B kalemleri:**
araç · yakıt · depo kirası · satış primi · yol/yemek · telefon · sigorta ·
tahsilat maliyeti · **her depo için ayrı toptan satış belgesi (82.464 TL/yıl,
`EV-2026-08-09-211`)** · IT/sipariş sistemi · iade lojistiği · satış
temsilcisi ücret çarpanı.

> **MODEL B için 5.000 şişede bir SAYI üretilmemiştir.** Üretilen şey bir
> **tabandır** ve gerçek maliyet **kesinlikle bunun üstündedir.**

---

## 8. DUYARLILIKLAR — TORNADO

### 8.1 `TGT_799` · ES · CHAIN RETAIL · 5.000 şişe · BASE = **272,83 TL/şişe**

| Eksen | Düşük | Yüksek | Δ− | Δ+ | Tip |
|---|---|---|---|---|---|
| **İTHALATÇI KATKI 0 → %30** | 164,27 | 272,83 | **−108,56** | 0 | **INVESTOR_DECISION_REQUIRED** |
| **DİSTRİBÜTÖR MARJI 0 → %30** | 164,27 | 272,83 | **−108,56** | 0 | `UNKNOWN` — grid |
| **HEDEF FİYAT 599 ↔ 999** | 189,50 | 356,16 | **−83,33** | **+83,33** | INVESTOR_TARGET_SCENARIO |
| **KANAL MARJI (18/25/35%) + `d`** | 227,78 | 304,83 | **−45,06** | **+32,00** | korelasyonlu, ASSUMPTION |
| **KENDİ DAĞITIM 0 → 1 kişi** | 208,49 | 272,83 | **−64,34** | 0 | taban; gerçek maliyet daha yüksek |
| **GÜMRÜK VERGİSİ 50% → 70%** | 240,73 | 272,83 | **−32,10** | 0 | tek yönlü risk (`T-161`/`T-163`) |
| **ÖTV λ (1,00 → 1,5625)** | 252,79 | 272,83 | **−20,04** | 0 | **tek yönlü aşağı** (λ ≥ 1) |
| **HACİM 5.000 → 100.000** | 272,83 | 293,03 | 0 | **+20,20** | ruhsat kademesi yüzünden sınırlı |

> ### TORNADO'NUN OKUNMASI — DÖRT GÖZLEM
>
> **1. En büyük iki eksen MODEL DIŞINDADIR.** `İthalatçı katkı payı` ve
> `distribütör marjı` — ikisi de **karar/pazarlık** meselesidir, veri değil.
> Modelin belirsizliğinin en büyük kısmı **bir veri eksikliği değil, bir
> karar eksikliğidir** (`OQ-901` → `T-851`; `T-604`).
>
> **2. Vergi eksenlerinin tamamı TEK YÖNLÜDÜR ve hepsi AŞAĞI bakar.**
> `g` yalnızca %70'e çıkabilir (%50 zaten en iyi hâl); `λ` yalnızca ≥1
> olabilir. **Vergi tarafında yukarı sürpriz YOKTUR.**
>
> **3. Kanal marjı, R5 düzeltmesinden sonra ÜÇÜNCÜ EN BÜYÜK eksene çıktı.**
> Düzeltme öncesi görünen bant (−10,67/+14,31) **yanıltıcıydı**: `d` hiçbir
> yerde düşülmediği için kanal riski yapay olarak küçük görünüyordu.
> Gerçek bant **−45,06 / +32,00**'dir ve **tamamı `ASSUMPTION`'dır.**
>
> **4. Hacim, tornadonun EN KÜÇÜK ekseni.** 20 kat büyümenin `MAX_CIF`
> etkisi (+20,20 TL) tek kişilik bir dağıtım ekibinin maliyetinden
> (−64,34 TL) **üç kat küçüktür.**

### 8.2 ÖTV (λ) — çapraz çarpım, 3 tarih × 4 nokta × rejim ihtimali

`MAX_CIF_TRY` (799 · ES · CHAIN BASE · 5.000 · g=0,50) — **PROJEKSİYON
(ASSUMPTION), FACT DEĞİL:**

| Hedef tarih | Doğrulanmamış revizyon | +%0 | +%8 | +%16 | +%25 |
|---|---|---|---|---|---|
| **EARLY 2027-01-01** | **0 adım** (sınır öncesi) | 272,83 | 272,83 | 272,83 | 272,83 |
| **EARLY 2027-01-01** | **1 adım** (sınır sonrası) | 272,83 | 269,98 | 267,13 | 263,92 |
| **BASE 2027-04-01** | 1 adım | 272,83 | 269,98 | 267,13 | **263,92** |
| **LATE 2027-07-01** | **1 adım** (`λ_1adım`) | 272,83 | 269,98 | 267,13 | 263,92 |
| **LATE 2027-07-01** | **2 adım** (`λ_2adım`) | 272,83 | 266,90 | 260,52 | **252,79** |

- **O-1:** üç senaryo da `λ=1` çapasıyla ayrıca koşuldu (+%0 sütunu).
- **O-7:** `LATE` **iki alt koşulla** raporlandı.
- **`EARLY` de iki rejim ihtimaliyle** (0/1 adım) — gözlenen yürürlük deseni
  düzensizdir (2025-12-31 · 2026-07-03).
- **Ortalama ALINMADI**; hiçbir nokta "beklenen" diye sunulmadı.
- `%16` noktasının tarihsel çapası vardır (gerçekleşen +%16,09); **diğer üçü
  çapasızdır.** Hiçbiri bir tahmin değildir.

**Kapalı form:** `Δ MAX_CIF = −(λ−1) × 53,4519 / (1+g)`
→ her **+%1** ÖTV artışı: **−0,3563 TL** (g=0,50) / **−0,3144 TL** (g=0,70).

> **Karşı-sezgisel not (`H5`):** ÖTV artışı yüksek tarifeli menşede **TL olarak
> daha az** kaybettirir (0,3144 < 0,3563) çünkü kayıp `(1+g)` ile bölünür.
> **Bu bir avantaj DEĞİLDİR** — o menşenin seviyesi zaten %11,765 düşüktür;
> **oransal olarak** ÖTV artışı yüksek tarifeli menşeyi **daha ağır** vurur.

### 8.3 Navlun (FREIGHT) duyarlılığı — **yapısal bir tespit**

> ### NAVLUN SENARYOSU `MAX_CIF_TRY`'Yİ DEĞİŞTİRMEZ
>
> Okyanus navlunu ve sigorta **CIF'in İÇİNDEDİR** (GK md.27/1-e,
> `EV-2026-08-09-120`). Ters model CIF **tavanını** verir; navlun o tavanın
> **nasıl bölüşüleceğini** belirler, tavanın **kendisini** değil.
>
> - **LCL/FCL LOW–BASE–HIGH farkı `MAX_CIF_TRY`'ye SIFIR etki eder.**
> - Navlun yalnızca **`MAX_FOB`**'u değiştirir ve `MAX_FOB` **zaten `fx`
>   olmadan `UNKNOWN`**'dır.
> - Modelde navlunun tek görünür etkisi **TR-içi (TRY) bacaktır** ve o da
>   `MAX_CIF`'i 5.000 şişede yalnızca **±0,93 TL** oynatır.
>
> **Sonuç: `C-311`'in (FCL bandının 4 katı) ters model üzerindeki etkisi
> SIFIRDIR.** `T-304` (CRITICAL) **ileri model** ve **FOB pazarlığı** için
> blokerdir; **ters model için değildir.**

### 8.4 LCL kanıt setinin ölüm tarihi (GÖREV 4)

```
LCL kotasyonlari (10 kart: EV-2026-08-10-301,-302,-303,-305,-306,-307,-308,-309,-310,-311)
access_date  : 2026-08-10
ttl          : 6d
SON GECERLI  : 2026-08-16
STALE        : 2026-08-17 00:00
```

**Bu model 2026-08-10'da koşulmuştur → LCL bacağı BUGÜN GEÇERLİDİR** (`P-3`
kapısı sağlandı). 2026-08-17'den sonra §6'daki TR-içi lojistik satırları
`ESTIMATE / LOW`'a düşer; **etkisi sınırlıdır** (`MAX_CIF` üzerinde ±0,93 TL).
**`EV-2026-08-10-304` bir LCL kotasyonu DEĞİLDİR** — İtalya için "kotasyon yok"
negatif bulgu kartıdır (`ttl: 14d`). Sayım **11 değil 10**'dur
(`T-801`/`T-923`).

---

## 9. BUYING TARGET / WALK-AWAY (GÖREV 7)

> ## ⛔ `TARGET` / `ACCEPTABLE` / `WALK-AWAY` FİYATLARI **ÜRETİLMEMİŞTİR**
>
> Bu üç seviye bir **yatırımcı eşiği** gerektirir. `OQ-901` **CRITICAL ve
> açıktır**: karar eşiklerinin tamamı `TBD`'dir. Keyfî yüzdelerle üretilmiş
> üç fiyat, **modelin en sinsi uydurma noktası** olurdu → **`T-851`**.

### 9.1 Üretilen tek nesne: `MAXIMUM STRUCTURAL BUY PRICE`

**Tanım:** ithalatçı katkı payı = **0** iken ödenebilecek azami CIF
(TRY/şişe): *"kâr sıfır, tüm bilinmeyen maliyetler sıfır, ÖTV 2026 çapasında"*.

| Hedef | ES/PT/IT/FR/CL **DOC_OK** | DOC_FAIL · ZA/AU/US/MD/AR |
|---|---|---|
| 599 | **189,50** | **167,20** |
| 699 | **231,16** | **203,97** |
| **799** | **272,83** | **240,73** |
| 899 | **314,50** | **277,50** |
| 999 | **356,16** | **314,26** |

*(CHAIN RETAIL · BASE · 5.000 şişe. Diğer kombinasyonlar
`country-buying-ceilings.csv`'de.)*

### 9.2 Yatırımcı kararına bırakılan alanlar

```yaml
TARGET_DISCOUNT_FROM_MAX:
  value:  null
  status: INVESTOR_DECISION_REQUIRED
  oq:     OQ-901 ; ticket: T-851

REQUIRED_IMPORTER_MARGIN:
  value:  null
  status: INVESTOR_DECISION_REQUIRED
  oq:     OQ-901 ; ticket: T-851

WALK_AWAY_PRICE:
  value:  null
  status: INVESTOR_DECISION_REQUIRED
  not:    "Esik belirlenmeden uretilmesi UYDURMA olurdu."
```

**Parametrik köprü** (`MAX_CIF_TRY`, ES · CHAIN BASE · 5.000 şişe):

| Hedef \ katkı payı | 0% | 10% | 20% | 30% | 40% | 50% |
|---|---|---|---|---|---|---|
| 599 | 189,50 | 162,37 | 135,24 | 108,11 | 80,98 | 53,85 |
| 699 | 231,16 | 199,51 | 167,85 | 136,19 | 104,53 | 72,88 |
| **799** | **272,83** | 236,64 | 200,46 | 164,27 | 128,08 | 91,90 |
| 899 | 314,50 | 273,78 | 233,07 | 192,35 | 151,63 | 110,92 |
| 999 | 356,16 | 310,92 | 265,67 | 220,43 | 175,19 | 129,94 |

Yatırımcı bir eşik verdiği **anda** bu satır `TARGET BUY PRICE`'a dönüşür.
**Model o adımı kendi başına atmaz.**

---

## 10. RFQ TARGET CEILING (GÖREV 10)

> ## ⛔ `VIABLE` / `NOT VIABLE` KARARI VERİLMEMİŞTİR
>
> Havuzdaki **26 tedarikçinin 26'sından da teklif alınmamıştır**. Gerçek quote
> olmadan ülke elemesi yapmak, **şeffaflığı ödüllendirip kaliteyi
> cezalandırmak** olurdu.

### 10.1 Tanım — X ve Y **modelden** gelir

```
X = kotumser kose : SCENARIO HIGH (m=%35, d=%18, lojistik HIGH)
                    + DOC_FAIL (kosullu menselerde g=0,70) + 5.000 sise
Y = BASE kose     : SCENARIO BASE (m=%25, d=%8, lojistik BASE)
                    + DOC_OK + 25.000 sise
```

**Okuma kuralı:**
`CIF ≤ X` → **güçlü aday** (kötümser köşede bile kapanır)
`X < CIF ≤ Y` → **inceleme** (BASE'te kapanır, kötümserde kapanmaz)
`CIF > Y` → **mevcut modelde zor**

### 10.2 CIF tavanları — **TRY/şişe** (fx gerektirmez)

| Ülke grubu | Hedef 699 · X / Y | Hedef **799** · **X / Y** | Hedef 899 · X / Y |
|---|---|---|---|
| **ES · PT · IT · FR · CL** | 169,12 / 248,85 | **200,98 / 290,51** | 232,84 / 332,18 |
| **ZA · AU · US · MD · AR** | 169,12 / 219,57 | **200,98 / 256,34** | 232,84 / 293,10 |

*(X tüm ülkelerde aynıdır çünkü kötümser köşede tercihli menşeler de %70'e düşer.)*

### 10.3 Döviz köprüsü — `IMPLIED_BREAKEVEN_USDTRY`

`fx` `null` olduğu için CIF tavanı dövize **çevrilemez.** Bunun yerine
**fx-siz bir tanı** üretildi:

```
IMPLIED_BREAKEVEN_USDTRY = (MAX_CIF_TRY / 0,75 lt) / gozlenen_CIF_USD_per_litre
```

Yani: *"Türkiye'nin o menşeden fiilen ithal ettiği ortalama CIF birim değeri
(`EV-2026-08-09-405`, **FACT**, T3) modelin tavanına TAM OTURSA, USD/TRY kaç
olurdu?"*

| Ülke | Gözlenen CIF (USD/lt, 2025) | `IMPLIED_BREAKEVEN_USDTRY` @ **Y**, hedef 799 |
|---|---|---|
| **ES** İspanya | 2,71 | **142,93** |
| **MD** Moldova | 2,46 | **138,94** |
| **CL** Şili | 2,89 | **134,03** |
| **PT** Portekiz | 3,20 | **121,05** |
| **IT** İtalya | 3,65 | **106,12** |
| **FR** Fransa | 6,27 | **61,78** |
| **ZA** G. Afrika ⚠ | 7,03 *(temsili DEĞİL)* | 48,62 |
| **AU** Avustralya ⚠ | 7,33 *(temsili DEĞİL)* | 46,63 |
| **AR** Arjantin ⚠ | 13,87 *(temsili DEĞİL)* | 24,64 |
| **US** ABD | **UNKNOWN** — seride yok | **UNKNOWN** |

> **NASIL OKUNUR — ve nasıl OKUNMAZ:**
> Bu sütun bir **kur tahmini DEĞİLDİR.** Gerçek USD/TRY'nin bu sayıların
> altında mı üstünde mi olduğu bu modelde **`UNKNOWN`**'dır (`T-912`,
> `T-852`). Sütunun tek işlevi: **yatırımcı tek bir tarihli kur kaydı girdiği
> anda, her ülke için "ne kadar pay var" tek bölmeyle görülür.**
>
> ⚠ **ZA/AU/AR satırları `TEMSİLİ DEĞİL` işaretlidir** (hacim <100 bin litre,
> `EV-2026-08-09-405` uyarısı) — sıralamada kullanılamazlar.
> ⚠ Bu seri **ülke ortalamasıdır ve premium SKU'ları içerir**; fiyat/performans
> segmentinin gerçek CIF'i **bunun altındadır** → gerçek pay **daha büyüktür.**

### 10.4 Sıralama — **bir tavsiye değil, bir gözlem**

Mevcut modelde **en geniş nefes payı** sırasıyla **ES · MD · CL · PT · IT**'dedir;
**FR** belirgin biçimde dardır; **ZA/AU/AR** ölçülemez; **US** `UNKNOWN`.

> **Bu bir tedarikçi/ülke tavsiyesi DEĞİLDİR.** `MAX_CIF_TRY` 9 ülkenin
> 9'unda yalnızca **iki değer** alır (§4.2); sıralamayı üreten şey **modelin
> çıktısı değil, gözlenen CIF birim değeridir** — ve o da `global-sourcing-kasifi`'nin
> **iki turdur kapatmadığını itiraf ettiği** bir Comtrade yorumuna dayanır.

---

## 11. GÖZETİM — TAVAN BİR ALT SINIRLA TEST EDİLMEDİ

```
ters model uretir :  MAX_CIF_TRY        <- UST SINIR (ticari)
gozetim dayatir   :  CIF_beyan >= esik  <- ALT SINIR (hukuki)
esik > MAX_CIF_TRY  =>  ARADA COZUM YOKTUR
```

`vergi.yaml → gozetim.birim_kiymet_esigi` = **`null` / `UNKNOWN`**
(`EV-2026-08-09-125` — **negatif arama sonucu, yokluğun kanıtı değil**).

> **Model bu uyarıyı her çalıştırmada basmaktadır:**
> *"GÖZETİM: eşik doğrulanmamıştır. `cif_try_max` BİR ALT SINIRLA
> TEST EDİLMEMİŞTİR."*
>
> ÖTV maktu olduğu için gözetimden **etkilenmez** (`EV-2026-08-09-113`);
> itirazın etkisi **yalnız `g` ve KDV matrahı kanalıyladır** ve **DÜ menşede
> (%70) tercihli menşeye (%50) göre 1,4 kat ağırdır.**

---

## 12. ÇIKTI DOSYALARI

| Dosya | İçerik |
|---|---|
| **`80-model/outputs/country-buying-ceilings.csv`** | **2.700 satır** · R8 başarısız satır: **0** |
| `80-model/outputs/sweet-spot-analizi.md` | GÖREV 9 |
| `80-model/outputs/rapor-tur25-finans.md` | Ajan raporu + *"Bu bulguyu ne çürütür?"* |
| `80-model/engine/otv_zaman_serisi.py` | **YENİ** — ufuk denetimi (`T-921`) |
| `80-model/engine/ters_model.py` | **YENİ** — R1–R11, RC1–RC6, **R5 düzeltmesi** |
| `80-model/engine/test_ters_model.py` | **YENİ** — TV-1…TV-10 (10/10) |
| `80-model/engine/calistir_tur25.py` | **YENİ** — koşucu |
| `80-model/engine/matrah_sirasi.py` | **DEĞİŞTİ** — ufuk denetimi eklendi, eski davranış korundu |
| `80-model/engine/hesap.py` | **DEĞİŞTİ** — `ters_model()` gerçek zincire delege eder |

`80-model/inputs/*.yaml` **salt okunmuştur; hiçbiri değiştirilmemiştir.**
`10-evidence/` **hiç açılmamıştır** — bu ajan kanıt üretmez.
