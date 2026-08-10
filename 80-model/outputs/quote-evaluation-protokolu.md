# QUOTE EVALUATION PROTOKOLÜ — TUR 3.25 §13

```yaml
belge:            quote-evaluation-protokolu
sahibi:           finans-fizibilite
tur:              "TUR 3.25 §12/§13 — QUOTE INGESTION SCHEMA + EVALUATION"
tarih:            2026-08-10
durum:            DRAFT              # OQ-901 / T-851 CRITICAL + OPEN
cikti_sinifi:     INTERNAL_ONLY      # bu protokolün ÜRETTİĞİ SONUÇ tedarikçiye gösterilmez
sema:             80-model/inputs/quote-ingestion-schema.yaml
motor:            80-model/engine/teklif_degerlendirme.py
testler:          80-model/engine/test_teklif_degerlendirme.py  (34/34)
fixture:          80-model/inputs/TEST_FIXTURE-teklif-vektorleri.yaml
havuzdaki_teklif: 0                  # 2026-08-10 itibarıyla SIFIR gerçek teklif
yeni_arastirma:   YOK
yeni_evidence:    YOK
dis_iletisim:     NONE
```

---

## 0. BU BELGE NE DEĞİLDİR

- Bir tedarikçi değerlendirmesi **değildir** — havuzda **sıfır** teklif vardır.
- Bir tedarikçi tavsiyesi **değildir**.
- Bir kabul/ret hükmü **değildir** ve bu protokol **ret hükmü üretemez** (§4).
- Bu belgedeki hiçbir TL/EUR/USD rakamı bir **fiyat** değildir; hepsi
  `MODEL_DERIVED / UPPER_BOUND / DRAFT` etiketli **tavanlardır**.

---

## 1. AKIŞ — TEK BAKIŞTA

```
tedarikçi e-postası / PDF
        │
        ▼
[1] KANIT KARTI  (evidence_id) ────────── yoksa → INCOMPLETE (QV-4)
        │
        ▼
[2] ŞEMAYA YAZIM  quote-ingestion-schema.yaml
        │   belge seviyesi (supplier, ürün, MOQ, palet, sertifika…)
        │   + kademeler: V1 / V2 / V3 / V4 / FULL_20FT_CONTAINER
        ▼
[3] SINIFLANDIRMA  QV-1 … QV-6  →  FIRM_QUOTE / B2B_INDICATIVE / PUBLIC_INDICATIVE
        │
        ▼
[4] KATMAN TESPİTİ  Incoterm → EXW = L0 · FOB = L1     (L0 ≠ L1, karıştırılmaz)
        │
        ▼
[5] KÖPRÜ         L0→L1 (iç nakliye + ihracat masrafı) · L1→L2 (navlun + sigorta)
        │
        ▼
[6] FX KÖPRÜSÜ    FX_DOWN_10 · FX_0 · FX_UP_10 · FX_UP_20   ← DÖRDÜ BİRDEN
        │
        ▼
[7] KARŞILAŞTIRMA  CIF eşdeğeri (TRY)  vs  TARGET CEILING X / Y
        │
        ▼
[8] SONUÇ         STRONG · NEGOTIATE · ABOVE_CEILING · INCOMPLETE   [INTERNAL_ONLY]
```

---

## 2. ŞEMA — YAPI KARARI VE GEREKÇESİ

### 2.1 `quantity` beş kademe: **iç içe (NESTED)**, tek satır değil

| Seçenek | Neden seçilmedi / seçildi |
|---|---|
| Tek satır = tek kademe (düz/CSV) | ❌ `supplier`, `MOQ`, `pallet_configuration`, `certificate_set` gibi **kademeden bağımsız** alanlar beş kez tekrarlanır. Tekrarlanan alan er geç ayrışır; ayrıştığında hangi satırın doğru olduğu belirlenemez. Bu, `kalem_defteri.py` **K6 / LEDGER_UNIQUENESS** ile aynı hastalıktır. |
| Bir belge → `kademeler[]` (iç içe) | ✅ Tedarikçi kimliği ve ürün gerçekleri **tek kaynakta**; fiyat/ödeme/lead time **kademe başına** değişir. Ayrıca bir teklif **epistemik olarak bölünebilir**: üretici 25.000 için bağlayıcı fiyat verip 5.000 için "yaklaşık" diyebilir → `quote_class` **kademe seviyesindedir**. |

**Çıktı tarafı yine düzdür:** motor iç içe yapıyı
`(kademe × fx_ekseni)` satırlarına açar. Yani **iç içe yapı girdi tarafında,
düz yapı çıktı tarafındadır.**

**Tekillik anahtarı:** `supplier|product|quote_date|tier_code` →
aynı kademe iki kez yüklenirse `KademeCiftKayit` fırlatılır (test `E::KADEME_TEKILLIGI`).

### 2.2 Beş kademe

| kod | şişe | not |
|---|---|---|
| `V1` | 5.000 | pilot |
| **`V2`** | **10.000** | **TUR 3.25'te EKLENDİ** — önceki turlarda yoktu |
| `V3` | 25.000 | ters modelin **Y köşesi** bu hacimde tanımlı |
| `V4` | 50.000 | |
| `FULL_20FT_CONTAINER` | **`UNKNOWN`** | ⛔ şişe adedi **tedarikçi beyanıdır**, biz doldurmayız |

> `FULL_20FT_CONTAINER` için `lojistik.yaml` (`EV-2026-08-10-329`) 20DV'de
> **paletsiz 11.800–13.700**, **paletli 6.480–7.200** aralığı verir. Tek bir
> sayı **yoktur** ve palet/koli konfigürasyonu **tedarikçiye bağlıdır**.
> Bu yüzden adet beyan edilmemişse kademe `INCOMPLETE`'tir (`QV-3`) —
> **tahmin edilmez.**

### 2.3 TUR 3A metadata mimarisiyle uyum

Bir teklif fiyatı modele `kalem_defteri.MaliyetKalemi` olarak girer ve
**dokuz zorunlu alanı** taşımak zorundadır. Bugün taşımadığı alan
`tutar_try`'dır — çünkü **teklif TL'ye çevrilerek saklanmaz**
(`makro.yaml` §5: *"Kur dönüşümü yapılmış bir sayı, orijinal sayının yerine
geçmez"*). Dolayısıyla teklif kalemi defterde **`BLOCKED_INPUT`** damgasıyla,
**adıyla ve eksik alanıyla** görünür — **sessizce 0 geçmez**
(test `E::METADATA_KALEMI`).

---

## 3. `FIRM_QUOTE` DOĞRULAMA KURALI (`QV-1`) — TAM HÂLİ

> **Gerçek bir tedarikçi e-postası, gerçek olduğu için `FIRM_QUOTE` olmaz.
> `FIRM_QUOTE` olmak için AÇIK TİCARİ TEKLİF içermelidir.**

Şemadaki makine-okunur hâli (`quote-ingestion-schema.yaml → dogrulama_kurallari`):

```yaml
- kural_id: QV-1
  ad: FIRM_QUOTE_DOGRULAMA
  seviye: TIER
  tip: HEPSI_DOLU
  alanlar:
    - quote.quote_valid_until      # GEÇERLİLİK
    - tier.quantity                # MİKTAR
    - tier.incoterm                # INCOTERM
    - tier.incoterm_named_place    #   + adı belirtilen yer/liman
    - tier.currency                # FİYATIN PARA BİRİMİ
  eylem: SINIF_DUSUR
  hedef_sinif: B2B_INDICATIVE
  damga: BLOCKED_INPUT

- kural_id: QV-1B      # FİYAT: EXW veya FOB'dan en az biri sayısal
  tip: EN_AZ_BIRI_DOLU
  alanlar: [tier.EXW, tier.FOB]
  eylem: SINIF_DUSUR ; hedef_sinif: PUBLIC_INDICATIVE
  ayrica_sonuc_zorla: INCOMPLETE
```

Yani dört unsur: **FİYAT + GEÇERLİLİK + MİKTAR + INCOTERM (yer adıyla)**,
**aynı kademede, birlikte**. Biri eksikse e-posta gerçek olsa bile
`FIRM_QUOTE` **değildir** → `B2B_INDICATIVE`.

**Destekleyici kilitler:**

| kural | ne yapar | hangi gerçek arızadan doğdu |
|---|---|---|
| `QV-1C` | `currency ∈ {"$","DOLAR","AMBIGUOUS","UNKNOWN",""}` → **`INCOMPLETE`** | Kart 1: kaynakta yalnızca `$`; AUD mı USD mi **doğrulanmadı** — tek başına fiyatı ~1,5 kat değiştirir |
| `QV-1D` | `incoterm ∉ {EXW,FOB}` → **`INCOMPLETE`** | `C-461`: aynı sayı hem "ex factory" hem "FOB" olarak sunuluyor → **L0/L1 karışır** |
| `QV-2` | **sınıf yükseltme yasağı**: `etkin = min(beyan, hesaplanan)` | Tedarikçinin "bu bağlayıcı tekliftir" demesi onu bağlayıcı yapmaz |
| `QV-3` | `FULL_20FT_CONTAINER` + adet/konfigürasyon eksik → `INCOMPLETE` | konteyner kapasitesi tedarikçiye bağlı |
| `QV-4` | `evidence_id` yok → `INCOMPLETE` | `CLAUDE.md` §1.6 |
| `QV-5` | `quote_valid_until < bugün` → `B2B_INDICATIVE` | süresi dolmuş teklif **firm değildir** — ama **RET DE DEĞİLDİR** |
| `QV-6` | dokuz alan metadata denetimi → `BLOCKED_INPUT` damgası | sessiz eksik yasağı |

> **`QV-4` sınıfı düşürmez, sonucu `INCOMPLETE` yapar.** Gerekçe: `evidence_id`
> **ticari içerikle ilgili değil, bizim kayıt disiplinimizle** ilgilidir.
> Teklif ticari olarak `FIRM` olabilir ama kanıt kartı açılmadan **modele
> giremez** (test `TQV-15`: `sinif=FIRM_QUOTE`, `sonuç=INCOMPLETE`).

**Kurallar veridir, kod değildir.** Şemadan `QV-1` silinirse motor davranışı
değişir — bu **davranışsal olarak** test edilmiştir
(`F::SEMA_KURALLARI`: `QV-1 ile → B2B_INDICATIVE`, `QV-1 olmadan → FIRM_QUOTE`).

---

## 4. DÖRT SONUÇ DEĞERİ — TANIM VE EŞİK

### 4.1 Eşikler

`rfq-negotiation-cards.md` §0.2 / §0.4 ile **birebir aynı** tanım; sayılar
`country-buying-ceilings.csv`'den **okunur, koda gömülmez**
(test `F::TAVAN_CSV`):

| Köşe | Tanım | Grup **P** (tercihli, DOC_OK) | Grup **N** (tercihsiz / DOC_FAIL) |
|---|---|---|---|
| **X** | `SCENARIO=HIGH` · tercih **yok** · **5.000** şişe | **200,9780** TRY/şişe | **200,9780** |
| **Y** | `SCENARIO=BASE` · tercih **var** · **25.000** şişe | **290,5134** | **256,3354** |

Hedef: `TGT_799` · kanal: `CHAIN_RETAIL` · katman: **CIF (L2)** · TRY/şişe.

> `origin_document` **`UNKNOWN`** ise motor **kötümser bandı (N)** kullanır ve
> satırı damgalar. Menşe belgesi bir **pazarlık kalemidir**, bir varsayım değil.

### 4.2 Dört değer

| Sonuç | Tanım | Koşul |
|---|---|---|
| **`STRONG`** | Teklifin CIF eşdeğeri, **kötümser köşenin bile altında** — yani model senaryolarının **hepsinde** yapısal olarak taşıyor | `CIF_eşdeğer ≤ X` |
| **`NEGOTIATE`** | Teklif **X ile Y arasında** — BASE senaryoda taşıyor, kötümser senaryoda taşımıyor. Fark **pazarlıkla veya senaryo netleşmesiyle** kapanabilir | `X < CIF_eşdeğer ≤ Y` |
| **`ABOVE_CEILING`** | Teklif, **mevcut DRAFT üst-sınır modelinin Y bandının üstünde**. **BİR GÖZLEMDİR, BİR RET DEĞİLDİR** (§5) | `CIF_eşdeğer > Y` |
| **`INCOMPLETE`** | **Karşılaştırma yapılamadı.** Eksik alan, belirsiz para birimi, belirsiz Incoterm, eksik köprü, eksik kur veya eksik tavan | aşağıdaki tabloya bakınız |

### 4.3 `INCOMPLETE` neden **baskındır**

`INCOMPLETE` bir "kötü sonuç" değildir; **"henüz sonuç yok"**tur. Şu
durumların **herhangi biri** varsa üretilir:

| Tetikleyici | Bayrak |
|---|---|
| Kural zorlaması (`QV-1B/1C/1D/3/4`) | `KURAL_ZORLAMASI` |
| Tavan satırı yok | `TAVAN_YOK` |
| FX ekseni boş | `FX_BLOCKED_INPUT` |
| Teklifin para birimi için kur yok (AUD/CLP/MDL…) | `PARA_BIRIMI_KURU_YOK` |
| Köprü eksik **ve** alt sınır Y'nin altında | `KOPRU_EKSIK` |
| Hacim kademesinin kendi tavanı yok (ör. `V2`=10.000) | `HACIM_KADEMESI_TAVANI_YOK` |

### 4.4 **TEK YÖNLÜ KARAR** — köprü eksikken ne söylenebilir

Teklif **FOB (L1)** veya **EXW (L0)** seviyesindedir; tavan **CIF (L2)**
seviyesindedir. Aradaki köprüler (navlun, sigorta, iç nakliye, ihracat
masrafı) **hepsi `≥ 0`**'dır. Bundan **matematiksel olarak** şu çıkar:

```
gerçek_CIF  ≥  teklif_fiyatı × kur          (köprü ≥ 0 olduğu için)
```

Dolayısıyla köprü bilinmese bile:

- `teklif × kur > Y` ⇒ **`ABOVE_CEILING` SAĞLAMDIR** (`karar_yolu = TEK_YONLU_ALT_SINIR`)
- `teklif × kur ≤ Y` ⇒ **hiçbir şey söylenemez** → `INCOMPLETE`.
  **`STRONG` ASLA bu yoldan verilmez** — gerçek CIF daha yüksek olabilir.

Bu asimetri koda ve teste gömülüdür (`C::TEK_YONLU`).
**Yani model, kendi bilgisizliğinin yönünü biliyor.**

---

## 5. ⛔ `REJECTED` YASAĞI — NEDEN VE NASIL

### 5.1 Neden

**Yatırımcı nihai marj eşiği HENÜZ YOKTUR** — `OQ-901`, ticket **`T-851`**,
`impact: CRITICAL`, `status: OPEN`.

Bir teklifi reddetmek için iki şey gerekir:
1. bir **tavan** (bu var: `MAX_CIF`, ama `DRAFT` ve **üst sınırın üst sınırı**),
2. bir **eşik** — "bu tavanın altında **kaç** puan marj gerekiyor?" (bu **yok**).

İkincisi olmadan verilen bir ret, **eşiği kodun içinde gizlice icat etmek**
olurdu. Ayrıca tavanın kendisi **26 kalemi `BLOCKED_INPUT`** olan bir
modelden gelir; bu 26 kalem kapandığında tavan **yalnızca düşebilir** —
yani bugünün `ABOVE_CEILING`'i yarın **daha da yukarıda** görünebilir, ama
`STRONG`'u da **kaybolabilir**. Tek yönlü hareket eden bir tavana dayanarak
**iki yönlü bir hüküm** verilemez.

**`ABOVE_CEILING` = "bugünkü DRAFT üst-sınır modelinin Y bandının üstünde"**
— tedarikçinin elenmesi **değildir**. Sonucu değiştirebilecek en az üç şey
vardır: pazarlık, menşe belgesi taahhüdü (`+%11,765`), ve modelin
`BLOCKED_INPUT` kalemlerinin kapanması.

### 5.2 Nasıl — koda dört kilit

```python
# 1) ALFABE DÖRT ELEMANLIDIR — beşinci deger yoktur
SONUC_DEGERLERI = frozenset({"STRONG", "NEGOTIATE", "ABOVE_CEILING", "INCOMPLETE"})

# 2) YASAK KELİME LİSTESİ
YASAKLI_SONUCLAR = frozenset({
    "REJECTED", "REJECT", "RED", "REDDEDILDI", "KILL",
    "NOT_VIABLE", "NOTVIABLE", "VIABLE", "ELENDI",
    "APPROVED", "ONAYLANDI", "ACCEPT", "ACCEPTED", "KABUL",
})

# 3) TEK GEÇİT — sonuç alanına yazılan HER değer buradan geçer
def _sonuc_dogrula(deger): ...          # yasak veya tanımsız -> YasakliSonuc
#    `Degerlendirme.__post_init__` bu geçidi ÇAĞIRIR -> nesne kurulamaz.

# 4) GÖVDESİZ FONKSİYON
def retmek(*_a, **_k):
    raise YasakliSonuc("RET YASAGI: bu modul bir teklifi reddedemez. ...")
```

`Degerlendirme(sonuc="REJECTED")` **nesne olarak kurulamaz** —
`__post_init__` içinde patlar. Test: `D::RET_YASAGI` (altı yasak kelime +
`retmek()` + doğrudan nesne kurulumu).

Ayrıca her `ABOVE_CEILING` satırında **"ABOVE_CEILING BIR RET DEGILDIR"**
bayrağı zorunludur (test `D::ABOVE_RET_DEGIL`).

---

## 6. FX KÖPRÜSÜ — DÖRT EKSEN

### 6.1 Kaynak

`makro.yaml → fx.senaryolar` (**`gumruk-vergi-uzmani`**, TUR 3.25 §1,
`OBSERVED_FX / NOT_FORECAST`, TCMB bülten 2026/147, `kur_tipi: doviz_satis`,
`EV-2026-08-10-865/-866/-867/-868`, `ttl_bitis: 2026-08-17`):

| eksen | çarpan | EUR/TRY | USD/TRY | status |
|---|---|---|---|---|
| `FX_DOWN_10` | 0,90 | 49,6273 | 42,9406 | `SENSITIVITY_AXIS` |
| **`FX_0`** | 1,00 | **55,1414** | **47,7118** | **`OBSERVED`** |
| `FX_UP_10` | 1,10 | 60,6555 | 52,4830 | `SENSITIVITY_AXIS` |
| `FX_UP_20` | 1,20 | 66,1697 | 57,2542 | `SENSITIVITY_AXIS` |

Motor **eksen adının tanımladığı çarpanı** yazılan değerle karşılaştırır;
uyuşmazsa `CONFLICT` üretir (test `F::FX_CARPAN`, `F::FX_DORT_EKSEN`).
**`alis_kuru_ekseni` ayrı bir eksendir ve okunmaz** — ithalatçı dövizi
**satın alan** taraftır, `doviz_satis` kullanılır. **`ttl` dolduğunda
`FX_STALE` bayrağı basılır.**

### 6.2 Tek kur ile tek sonuç ÜRETİLMEZ

Her kademe **dört eksende ayrı ayrı** değerlendirilir ve **dört ayrı satır**
üretir. Fixture kanıtı (`TQV-7A`, sentetik kur ve sentetik band ile):

| eksen | CIF eşdeğeri | sonuç |
|---|---|---|
| `FX_DOWN_10` | 180,00 | **`STRONG`** |
| `FX_0` | 200,00 | **`STRONG`** (sınırda) |
| `FX_UP_10` | 220,00 | **`NEGOTIATE`** |
| `FX_UP_20` | 240,00 | **`NEGOTIATE`** |

`TQV-7B` aynı bandda `NEGOTIATE → NEGOTIATE → ABOVE_CEILING → ABOVE_CEILING`
verir. Yani **aynı teklif, aynı gün, kur eksenine göre farklı sonuç alır**
(test `FX::EKSEN_AYRISMASI`).

### 6.3 YAPISAL BULGU — FX tek başına `STRONG`'u `ABOVE_CEILING`'e çeviremez

```
X → Y bandının genişliği   =  290,5134 / 200,9780  =  ×1,4455
FX ekseninin açıklığı      =  1,20 / 0,90          =  ×1,3333
```

**Band, eksenden geniştir.** Dolayısıyla tek bir teklif, **salt kur
hareketiyle** `STRONG`'dan `ABOVE_CEILING`'e **geçemez**; en fazla bir
komşu kademeye kayar. Bu, bir veri bulgusu değil **bir geometri
sonucudur** ve test edilmiştir (`FX::BAND_GENISLIGI`).

> **İki okuma:** (a) kur riski, senaryo riskinden (m, d, DOC_FAIL) **daha
> küçüktür** — tavanı asıl oynatan şey kur değil, kanal ve menşe
> varsayımlarıdır; (b) ±%20'lik eksen, **2027 ufuklu** bir model için
> yeterince geniş **olmayabilir** → `T-874`.

### 6.4 `MAX_FOB` / `MAX_EXW` — üç turdur `UNKNOWN` olan alan **kısmen açıldı**

`fx` geldiği için artık **hesaplanabilir** — ama **nokta değeri olarak
değil, ÜST SINIR olarak**:

```
CIF = FOB + navlun + sigorta         ve tüm köprüler ≥ 0
  ⇒  MAX_FOB ≤ MAX_CIF_TRY / kur     ⇒  MAX_EXW ≤ MAX_FOB
```

**Grup P · `TGT_799` · CHAIN · Y köşesi (25.000):**

| eksen | `MAX_FOB` üst sınır @X (EUR) | @Y (EUR) | @X (USD) | @Y (USD) |
|---|---|---|---|---|
| `FX_DOWN_10` | 4,0497 | **5,8539** | 4,6804 | **6,7655** |
| **`FX_0`** | **3,6448** | **5,2685** | **4,2123** | **6,0889** |
| `FX_UP_10` | 3,3134 | 4,7896 | 3,8294 | 5,5354 |
| `FX_UP_20` | 3,0373 | 4,3904 | 3,5103 | 5,0741 |

> ⛔ **Bu sayılar bir üst sınırın üst sınırının üst sınırıdır.** Üç kat:
> (1) `MAX_CIF` zaten üst sınırdır (λ=1 + 26 kalem `BLOCKED_INPUT`),
> (2) köprü `0` alınmıştır (gerçekte `>0`),
> (3) Y köşesi iyimser senaryodur (BASE + DOC_OK + 25.000).
> **Nokta değeri için FOB→CIF köprüsü gerekir → `T-866` (navlun+sigorta,
> CIF kapsamlı, şişe başına).** `lojistik.yaml → sise_basi_lojistik_maliyeti`
> **kullanılmadı**: kapsamı `L1→L3`'tür (CIF değil) ve **sigortayı içermez**.

---

## 7. `INTERNAL_ONLY` AYRIMI — MEKANİZMA

| Katman | Mekanizma | Test |
|---|---|---|
| **Dosya adı** | `internal_rapor_yaz()` yalnızca `INTERNAL_ONLY-` ön ekli dosyayı kabul eder | `E::DOSYA_ADI` |
| **Dizin** | Hedef `80-model/outputs/` **olmak zorunda**; `50-sourcing/`, `10-evidence/`, `99-ops/`, `60-pazar/`, `70-kanal/`, `30-vergi-gumruk/`, `40-lojistik/` altına **yazılamaz** | `E::DOSYA_ADI` |
| **Damga** | Her internal çıktının ilk satırı `INTERNAL_ONLY — TEDARIKCIYE GOSTERILMEZ` HTML yorumudur (otomatik eklenir) | — |
| **Yüzey ayrımı** | Tedarikçiye giden **tek** metin `tedarikciye_giden_metin()`tir ve **yalnızca eksik alan talebi** üretir | `E::TEDARIKCI_METNI` |
| **Sızıntı taraması** | `disari_giden_metin_denetle()` — dışarı giden her metin buradan geçer; `MAX_CIF`, `CEILING`, `TAVAN`, sonuç değerleri, `FX_*`, `MODEL_DERIVED` ve **üç haneli ondalıklı sayı** (`290,51` gibi) desenleri **istisna fırlatır** | `E::SIZINTI` |

> Sızıntı tarayıcı **kasıtlı olarak aşırı hassastır**: `290,51` gibi herhangi
> bir üç haneli ondalıklı sayıyı reddeder. Yanlış pozitif maliyeti (bir
> cümleyi yeniden yazmak) yanlış negatif maliyetinden (pazarlık çapamızı
> karşı tarafa vermek) **çok daha ucuzdur.**

---

## 8. EPİSTEMİK ASİMETRİ — ÇIKTIDA GÖRÜNÜR

Her değerlendirme satırı şu notu taşır (test `F::EPISTEMIK_ASIMETRI`):

```
ASIMETRIK KARSILASTIRMA: teklif=<FIRM_QUOTE|B2B_INDICATIVE|PUBLIC_INDICATIVE> (gozlem)
vs tavan=MODEL_DERIVED / UPPER_BOUND / DRAFT (BLOCKED_INPUT=26)
```

| | Teklif | Tavan |
|---|---|---|
| Ne | Bir tedarikçinin **ticari beyanı** | Bir hedef raf fiyatından **türetilmiş üst sınır** |
| Kaynak | T4 (ticari teklif) | Model — `reverse-price-model.md` (`DRAFT`) |
| Statü | `FACT` (firm ise) | `MODEL_DERIVED / UPPER_BOUND` |
| Hata yönü | İki yönlü (pazarlıkla iner) | **Tek yönlü**: 26 kalem kapanınca **yalnızca düşer** |
| Doğrulanma | Tedarikçi imzası | **Doğrulanmamış** — `L8_CHAIN_RETAIL` katmanında Türkiye'de **sıfır gözlem** (`T-701`, `T-603`) |

**`STRONG` bir eşitlik iddiası değildir.** İki farklı epistemik sınıfın
karşılaştırılmasıdır ve **yapısal** okunmalıdır: *"bu teklif, bugünkü
üst-sınır modelinin en kötümser köşesinde bile sığıyor."*

---

## 9. BUGÜNKÜ DURUM (2026-08-10)

```
havuzdaki teklif      : 0            ← hiçbir üreticiye temas edilmedi
FX eksenleri          : 4/4 HAZIR    ← FX_0 = OBSERVED (TCMB, ttl 2026-08-17)
TARGET CEILING (P)    : X=200,9780  Y=290,5134   [MODEL_DERIVED/UPPER_BOUND/DRAFT]
TARGET CEILING (N)    : X=200,9780  Y=256,3354
MAX_FOB nokta degeri  : BLOCKED_INPUT (T-866)
MAX_FOB ust siniri    : HESAPLANDI (4 eksen x 2 para birimi)
V2 = 10.000 tavani    : YOK          ← T-865, interpolasyon YAPILMADI
uretilen ret hukmu    : 0            ← YASAK
```

Motorun bugünkü canlı çıktısı: `80-model/outputs/INTERNAL_ONLY-teklif-degerlendirme.md`

---

## 10. AÇILAN TICKET'LAR

| ticket | hedef ajan | impact | konu |
|---|---|---|---|
| `T-865` | finans-fizibilite | HIGH | `V2 = 10.000` şişe kademesi `country-buying-ceilings.csv`'de **yok** |
| `T-866` | navlun-lojistik-uzmani | HIGH | **FOB→CIF köprüsü** (navlun + sigorta, CIF kapsamlı, şişe başına) |
| `T-867` | navlun-lojistik-uzmani | HIGH | **EXW→FOB köprüsü** (menşe içi nakliye + ihracat masrafı, şişe başına) |
| `T-868` | global-sourcing-kasifi | MEDIUM | Gelen teklife **kanıt kartı açma** ve şemaya yazma sorumluluğu |
| `T-869` | global-sourcing-kasifi | MEDIUM | `FULL_20FT_CONTAINER` kademesi için **palet/koli/şişe ağırlığı** beyanı |
| `T-874` | yatirim-komitesi-baskani | MEDIUM | FX ekseninin açıklığı (±%20) 2027 ufku için yeterli mi |
