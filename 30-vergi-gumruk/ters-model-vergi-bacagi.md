# TERS MODELİN VERGİ BACAĞI — BAĞLAYICI SPESİFİKASYON

```yaml
belge:            ters-model-vergi-bacagi
sahibi:           gumruk-vergi-uzmani
tur:              TUR 2.5 — REVERSE MODEL VERGI DESTEGI
tarih:            2026-08-10
tuketici:         finans-fizibilite (engine)
tip:              SPESIFIKASYON (kod degildir)
kapsam:           GTIP 2204.21 — 750 ml siselenmis, kopuksuz (durgun) taze uzum sarabi
BASE_DATE:        2026-08-10
yeni_arastirma:   YOK — bu belgede yeni dis kaynak taranmamistir
yeni_evidence:    YOK — tum degerler mevcut evidence_id'lere referans verir
durum:            SUBMITTED
```

> **Bu belge kod değildir, sözleşmedir.** `80-model/engine/` altındaki kodu
> `finans-fizibilite` yazar. Burada yazılan hiçbir oran/tutar koda gömülmez;
> hepsi `80-model/inputs/vergi.yaml`'dan okunur (CLAUDE.md §12).
>
> **Bu belge yeni bir vergi araştırması içermez.** TUR 1 / 1.5 / 2'de kapatılmış
> bulguların **ters yönde cebirsel olarak doğru uygulanmasını** tanımlar.

---

## 0. TEK CÜMLELİK ÖZET

Ters modelde vergi bacağının tamamı **tek bir satıra** iner:

```
CIF_TRY_max = ( L4_econ_max − ÖTV_per_şişe − KKDF ) / ( 1 + gv_oranı )
```

ve bu satırdaki **çıkarma işlemi bölmeden ÖNCE** yapılmak zorundadır.
Sıra ters çevrilirse azami satın alma fiyatı, menşeye göre
**17,82 – 22,01 TL/şişe eksik** çıkar (§6, H1).

---

## 1. NOTASYON — TERİMLER KARIŞTIRILAMAZ

| Sembol | Anlam | Birim | Sahibi |
|---|---|---|---|
| `C` | **CIF_TRY** — gümrük kıymeti, TL, şişe başına | TRY/şişe | çözülen değişken |
| `g` | `gv_oranı` — fiilen uygulanacak gümrük vergisi oranı (0,50 veya 0,70) | oran | `gumruk-vergi-uzmani` |
| `O` | ÖTV, şişe başına, **maktu** = `otv_maktu(t) × hacim_litre` | TRY/şişe | `gumruk-vergi-uzmani` (parametre) |
| `v` | KDV oranı = 0,20 | oran | `gumruk-vergi-uzmani` |
| `k` | KKDF, şişe başına | TRY/şişe | peşin ödemede **0** |
| `X_pre` | tescile kadarki, **KDV'ye tabi olmayan** diğer gider/ödeme | TRY/şişe | §4.3 — baz **0** |
| `B` | bandrol birim bedeli (KDV hariç) | TRY/şişe | `mevzuat-ruhsat-uzmani` |
| `L4_econ` | `C + GV + k + O` — **KDV HARİÇ** post-tax landed | TRY/şişe | bu belge |
| `L4_cash` | `C + GV + k + O + KDV` — **KDV DAHİL** (matrah-sirasi.md §4'teki `L4`) | TRY/şişe | bu belge |

> ⛔ **`L4` çıplak token'ı bu modelde YASAKTIR.** Her kullanımda `L4_econ` veya
> `L4_cash` yazılır. `matrah-sirasi.md` §4'teki "L4 POST-TAX LANDED" ifadesi
> **`L4_cash`**'e karşılık gelir ve ters modelin ekonomik zincirinde
> **kullanılamaz** (§6, H3).

---

## 2. İLERİ YÖN — DOĞRULUK KAYNAĞI (değiştirilmedi)

`30-vergi-gumruk/matrah-sirasi.md` §4'ten birebir:

```
GV          = C × g                                  [EV-2026-08-09-103…-106]
İGV         = 0                                      [EV-2026-08-09-107]
KKDF        = k  (peşin ⇒ 0)                          [EV-2026-08-09-119]
ÖTV matrahı = C + GV + k + X_pre                      [EV-2026-08-09-115]
ÖTV         = max( 0,00 × ÖTV matrahı ; otv_maktu(t) × hacim )  = O   ← MAKTU
KDV matrahı = C + GV + k + O + X_pre                  [EV-2026-08-09-117, EV-2026-08-10-108]
KDV         = v × KDV matrahı                         [EV-2026-08-09-118]

L4_econ     = C + GV + k + O          = C(1+g) + k + O
L4_cash     = L4_econ + KDV           = (1+v)·(C(1+g) + k + O + X_pre) − v·X_pre + ...
              → X_pre = 0 iken:  L4_cash = (1+v) × L4_econ
```

> **Kritik yapısal gözlem:** `X_pre = 0` iken `L4_cash = 1,20 × L4_econ`
> **tam olarak**. Bu, ters modelde KDV'nin tek adımda geri alınabilmesini
> sağlar ve §6/H3 hatasının büyüklüğünü tam olarak `L4_econ / 6` yapar.

---

## 3. TERS YÖN — ADIM ADIM TÜRETİM

### 3.0 Girdi ve çıktı sözleşmesi

**Girdi:** `L8_target_kdv_dahil` (TRY/şişe, **BANT**), `menşe`, `ödeme_şekli`,
`tercihli_belge_ibraz_edildi`, `doğrudan_nakliyat_sağlandı`, `tarih_t`,
`hacim_litre`, ve kanal/lojistik parametreleri (diğer ajanlar).

**Çıktı:** `CIF_TRY_max` (üst sınır) + `peak_cash` bileşenleri (ayrı görünüm).

---

### R1 — L8 → L8_net · **ZİNCİRDEKİ TEK KDV İŞLEMİ**

```
L8_net = L8_target_kdv_dahil / (1 + v)          v = matrah_sirasi[sıra=5].oran_pct/100
```

`v = 0,20` — `FACT`, T2, `EV-2026-08-09-118`, `effective_date: 2023-07-10`.

> **BAĞLAYICI:** Bu, ters zincirin **tamamındaki tek KDV bölmesidir.**
> İthalatta ödenen KDV bir **maliyet değil**, bu perakende KDV'sinin
> **peşin ödenmiş kısmıdır** (`EV-2026-08-10-101`). İkinci kez düşülemez (§6, H2).

> ⚠️ `L8_target` bu ajanın alanı **değildir**. `l8_chain_retail` **`null`**'dır
> (`T-603`). Model tek fiyata kilitlenemez, **bant** kullanır (`M-3`, `K5`).

---

### R2–R4 — L8_net → L6 · **VERGİ BACAĞI DEĞİL** (kanal-marj-uzmani)

```
L7_eff = L8_net × (1 − m_retail)
L6     = (L7_eff + f_per_bottle) / (1 − d)
```

`master-commercial-input-table.md` §4.1'deki taşıyıcı denklemle aynıdır.
**Bu satırlar hakkında sonuç üretmiyorum**; yalnızca vergi bacağıyla
çakışmadıklarını teyit ediyorum: `m_retail`, `d`, `f` hiçbir vergi matrahına
girmez ve hiçbir vergiyi değiştirmez.

---

### R5 — L6 → L5_max · **VERGİ BACAĞI DEĞİL** (finans-fizibilite)

İthalatçının hedef katkı payı düşülür. Vergi etkisi yok.

---

### R6 — L5_max → L4_econ_max · **VERGİ BACAĞININ SINIRI**

```
L4_econ_max = L5_max − Σ(L5_kalemleri)
```

| Kalem | Ekonomik değeri (düşülür) | Vergi matrahına girer mi | Dayanak |
|---|---|---|---|
| **Bandrol** | `B` = **KDV hariç** bedel | **HAYIR** — §4.2 türetmesi | `EV-2026-08-10-108` + `EV-2026-08-09-213` |
| **Bandrol KDV'si** | **0,00** (indirilebilir) | — | `EV-2026-08-10-101` (genel indirim kuralı) |
| TADAB hizmet bedeli | mevzuat-ruhsat-uzmani | **HAYIR** — §4.2 | `T-203` |
| Antrepo / elleçleme / iç nakliye / müşavirlik | navlun-lojistik-uzmani | **HAYIR** — §4.3 | `EV-2026-08-09-121` |
| **İthalat KDV'si** | **0,00** — A1 baz senaryo | (matrahın kendisi) | `EV-2026-08-10-101/-102/-103` |
| Devreden KDV **finansman maliyeti** | **> 0 — gerçek maliyet** | HAYIR | `kdv-…-nakit.md` C3 |
| Fire/zayi KDV'si `f × KDV` | **> 0 — gerçek maliyet** | HAYIR | KDVK md.30/c, `EV-2026-08-10-103` |

> ⚠️ Son iki satır, "KDV maliyet değildir" cümlesinin **tam olmayan** kısmıdır.
> KDV'nin kendisi maliyet değildir; **kilitlendiği sürenin finansmanı** ve
> **kırılan şişeye isabet eden kısmı** maliyettir. Ters modelde bu ikisi
> `L5_kalemleri` içinde **ayrı satır** olarak durur, KDV satırında değil.

---

### R7 — L4_econ_max → CIF_TRY_max · **ANA VERGİ ADIMI**

Cebirsel türetme (ileri yönden birebir):

```
(1)   L4_econ  = C + GV + k + O                       [tanım]
(2)   GV       = C × g                                [EV-2026-08-09-103…-106]
(3)   L4_econ  = C + C·g + k + O
(4)   L4_econ  = C·(1 + g) + k + O
(5)   L4_econ − O − k = C·(1 + g)                     ← ÖNCE ÇIKAR
─────────────────────────────────────────────────────────────
(6)   C = ( L4_econ − O − k ) / (1 + g)               ← SONRA BÖL
```

**BAĞLAYICI SIRA (R7-KURAL):**

| Adım | İşlem | Neden bu sırada |
|---|---|---|
| **7a** | `A := L4_econ_max` | — |
| **7b** | `A := A − O` | ÖTV **maktudur**; gümrük vergisinden **etkilenmez** ve gümrük vergisine **taban oluşturmaz**. Ters yönde de gümrük vergisi bölmesine **girmez**. |
| **7c** | `A := A − k` | KKDF de ÖTV matrahındadır ama GV matrahında değildir → ÖTV ile aynı muamele |
| **7d** | `CIF_TRY_max := A / (1 + g)` | Gümrük vergisi **yalnız CIF üzerinden** oransaldır |

> **Neden `(1+g)`?** Çünkü gümrük vergisi `C × g` kadar artar ve bu artış
> ÖTV matrahına **girer** ama ÖTV tutarını **değiştirmez** (nispi %0);
> KDV matrahına **girer** ve orayı değiştirir — ancak KDV ekonomik zincirde
> zaten yoktur. Dolayısıyla ekonomik zincirde gümrük vergisinin tek etkisi
> `C(1+g)` çarpanıdır. **Bu, ters modeli bu kadar temiz kılan tek nedendir
> ve nispi ÖTV oranının %0 olmasına bağımlıdır** (`EV-2026-08-09-110`).

#### R7 — KKDF varyantı (baz senaryo dışı)

`ödeme_şekli != 'peşin'` ise KKDF doğar (%6, `EV-2026-08-09-119`) **ama
matrah tanımı `UNKNOWN`'dır** (`T-105`). İki olası cebir:

```
(i)  k, CIF'ten BAĞIMSIZ bir tutar ise:   C = (A − O − k) / (1 + g)
(ii) k = C × 0,06 (matrah CIF ise):       C = (A − O) / (1 + g + 0,06)
```

> ⛔ **Model bu ikisi arasında SEÇİM YAPMAZ.** `ödeme_şekli != 'peşin'` iken
> `CIF_TRY_max` çıktısı **`UNKNOWN`** olmalıdır (`vergi.yaml → hesap_sozlesmesi.uyari`
> ile aynı kural, ters yönde). Baz senaryoda tek kanıtlı ödeme şartı
> **peşin**tir (R1/Harland, `master-…-table` §3.4) ve `k = 0`'dır.

---

### R8 — **ZORUNLU ROUND-TRIP DOĞRULAMASI**

Ters model çıktısı, **ileri modele geri beslenip** doğrulanmadan raporlanamaz:

```
assert |  ileri_model(CIF_TRY_max, g, O, k).L4_econ  −  L4_econ_max | < 0,01 TL
```

Bu tek satır, §6'daki **beş hatanın beşini de** yakalar. Sağlanmazsa model
`UNKNOWN` döner ve hangi adımın tutmadığını raporlar.

---

### R9 — NAKİT ÖRTÜSÜ (ayrı çıktı — R7 ile **toplanmaz**)

`CIF_TRY_max` bulunduktan **sonra**, aynı sayıdan nakit görünümü üretilir:

```
GV_nakit    = CIF_TRY_max × g
ÖTV_nakit   = O
KDV_ithal   = v × ( CIF_TRY_max × (1+g) + k + O )      = v × L4_econ_max
KDV_bandrol = v × B
L4_cash     = L4_econ_max + KDV_ithal                   = 1,20 × L4_econ_max   (X_pre=0)

gümrükte_nakden_ödenen = GV_nakit + k + ÖTV_nakit + KDV_ithal
```

> **`KDV_ithal = v × L4_econ_max` özdeşliği** ters modelde bedava gelir ve
> `peak_cash_requirement` hesabını CIF bilinmeden bile yapılabilir kılar:
> hedef raf fiyatı bandı verildiği anda gümrükte ödenecek KDV **doğrudan
> hesaplanır**. Bu, TUR 3'ün `fx` olmadan üretebileceği gerçek bir çıktıdır.

---

### R10–R11 — CIF → FOB → para birimi · **SINIR**

```
FOB_TRY_max = CIF_TRY_max − navlun_TRY − sigorta_TRY      ← navlun-lojistik-uzmani
FOB_FX_max  = FOB_TRY_max / kur                            ← STOP
```

> ⛔ **Ters model burada durur.** `makro.yaml → fx` **`null`**'dır (`T-912`) ve
> gümrük beyanında hangi kurun esas alınacağı **`UNKNOWN`**'dır (`T-911`,
> target: bu ajan, **bu turda kapatılmadı**). `CIF_TRY_max` ve `FOB_TRY_max`
> **yalnız TRY cinsinden** raporlanır. Döviz cinsinden azami satın alma fiyatı
> **`UNKNOWN`**'dır.

---

## 4. MATRAH SINIRLARI — TERS MODELDE NELERİN VERGİ BACAĞINA GİRMEDİĞİ

### 4.1 Menşe/tercih yalnız `g`'yi değiştirir

ÖTV ve KDV **menşeden bağımsızdır** (`EV-2026-08-09-110`). Ters modelde de
menşenin tek etkisi `(1+g)` bölenidir. Bunun **kapalı formlu** sonucu:

```
CIF_max(g=0,70) / CIF_max(g=0,50) = 1,50 / 1,70 = 0,88235
```

> **Tercihli rejimi kaybetmek, azami satın alma fiyatını tam olarak
> %11,765 düşürür — L8'den, ÖTV'den, marjdan ve navlundan BAĞIMSIZ olarak.**
> Bu, ters modelin ürettiği en dayanıklı tek sayıdır: hiçbir `UNKNOWN`
> girdiye bağlı değildir. (İleri yöndeki karşılığı: CIF 100 TL'de +24 TL/şişe,
> `mense-tarife-eslemesi.md` §3.3.)

### 4.2 Bandrol ve TADAB — **vergi matrahına girmez** (T-203 türetmesi)

**Türetme (yeni dış kaynak yok; iki mevcut FACT'ten):**

```
(1) KDVK md.21/c: KDV matrahına giren "tescile kadarki diğer gider ve
    ödemeler" YALNIZCA "VERGİLENDİRİLMEYENLER"dir.        [EV-2026-08-10-108, T1]
(2) Bandrol bedeli Darphane fiyat listesinde "%20 KDV hariç"tir
    → bandrol bedeli KDV'ye TABİDİR = "vergilendirilen"dir. [EV-2026-08-09-213, T1]
(3) (1) ∧ (2)  ⇒  bandrol bedeli md.21/c kapsamına GİRMEZ.
(4) Bandrol satıcıya ödenen fiyatın parçası değildir; Türkiye'de idareye
    ödenir → GK md.27 ilavelerinden değildir → GÜMRÜK KIYMETİNE de girmez.
                                                          [EV-2026-08-09-120/-121]
(5) ÖTV matrahı = "hesaplanacak ÖTV hariç KDV matrahını oluşturan unsurlar"
    → (3) gereği bandrol ÖTV matrahına da girmez.          [EV-2026-08-09-115]
─────────────────────────────────────────────────────────────────────
SONUÇ: Bandrol ve TADAB hizmet bedeli L4→L5 geçişindedir.
       Hiçbir vergi matrahına girmez.   status: ESTIMATE (hukuki türetme)
```

**Karşı senaryonun büyüklüğü — neden bu `UNKNOWN` modeli bloke etmez:**

| Senaryo | Ek ÖTV | Ek KDV | Ekonomik etki |
|---|---|---|---|
| Bandrol matraha **girmez** (baz) | 0 | 0 | 0 |
| Bandrol KDV matrahına **girseydi** | **0,0000** (ÖTV maktu) | `B × 0,20` = **0,4721 TL/şişe** | **0,00 TL** (KDV indirilebilir) |

> **T-203'ün model etkisi ≤ 0,4721 TL/şişe'dir ve tamamen NAKİT tarafındadır;
> ekonomik maliyeti ve `CIF_TRY_max`'ı SIFIR etkiler.** Ticket kapanmadan da
> ters model çalıştırılabilir. *(B = 2,36073 TL/şişe, `EV-2026-08-09-213`.)*

### 4.3 `X_pre` — tescile kadarki yurt içi masraflar

Ordino, antrepo, elleçleme, gümrük müşavirliği, X-ray, devanning: hepsi
**KDV'ye tabi hizmetlerdir** → md.21/c'nin "vergilendirilmeyenler" şartını
sağlamazlar → **KDV matrahına girmezler.** Baz senaryoda `X_pre = 0`.

**Tek istisna adayı:** gümrük beyannamesi **damga vergisi** — md.21/b'ye göre
"ithalat sırasında ödenen bir vergi" olarak KDV matrahına **girer**, ancak
**tutarı `UNKNOWN`'dır** (`matrah-sirasi.md` §4 sıra 6). Ters modelde
`X_pre` **açık bir parametre** olarak durur, varsayılanı `0`, ve
`X_pre > 0` girilirse R7 şu hâle gelir:

```
C = ( L4_econ_max − O − k − X_pre ) / (1 + g)
```

> Damga vergisi **beyanname başınadır**, şişe başına değil → 5.000+ şişelik
> partide şişe başı etkisi ihmal edilebilir düzeydedir. Ancak model bunu
> **sıfır varsayarsa bunu çıktıda YAZMALIDIR.**

---

## 5. 9 ÜLKE — TERS MODEL PARAMETRE TABLOSU

Kaynak: `mense-tarife-eslemesi.md` §1 + `vergi.yaml → mense_tarife_eslemesi`.
**Yeni araştırma yapılmamıştır**; sütunlar ters model için yeniden düzenlenmiştir.

| # | `country` | `g` (baz) | **ters bölen `1+g`** | Rejim | Menşe belgesi (K3) | Çıkış ülkesi koşulu (K4) | Koşul düşerse `1+g` | `CIF_max` kaybı | evidence_id |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **ES** İspanya | 0,50 | **1,50** | 1/98 (AB tarım) | EUR.1 (0302) **veya** Fatura Beyanı (0538) · **A.TR GEÇERSİZ** | ATRM listesi (AB+EFTA+…; **BK YOK**) | **1,70** | **−%11,765** | `EV-2026-08-09-103`; `-10-155`,`-158` |
| 2 | **PT** Portekiz | 0,50 | **1,50** | 1/98 | EUR.1 veya Fatura Beyanı | ATRM listesi | **1,70** | **−%11,765** | `EV-2026-08-09-103`; `-10-155` |
| 3 | **IT** İtalya | 0,50 | **1,50** | 1/98 | EUR.1 veya Fatura Beyanı | ATRM listesi | **1,70** | **−%11,765** | `EV-2026-08-09-103`; `-10-155` |
| 4 | **FR** Fransa | 0,50 | **1,50** | 1/98 | EUR.1 veya Fatura Beyanı | ATRM listesi | **1,70** | **−%11,765** | `EV-2026-08-09-103`; `-10-155` |
| 5 | **CL** Şili | 0,50 | **1,50** | Türkiye-Şili STA, I s. Liste dipnot (2) | EUR.1 veya Fatura Beyanı | ⚠ **YALNIZCA ŞİLİ** — aktarma riski `C-…`/`T-914` | **1,70** | **−%11,765** | `EV-2026-08-09-105`; `-10-160`,`-164` |
| 6 | **ZA** G. Afrika | **0,70** | **1,70** | **YOK** | tercihsiz menşe şahadetnamesi (koşullu) | — | 1,70 | 0 (zaten en kötü) | `EV-2026-08-09-104`; `-10-152`,`-161` |
| 7 | **AU** Avustralya | **0,70** | **1,70** | **YOK** | tercihsiz (koşullu) | — | 1,70 | 0 | `EV-2026-08-09-104`; `-10-152` |
| 8 | **US** ABD/Kaliforniya | **0,70** | **1,70** | **YOK** | tercihsiz (koşullu) | — | 1,70 | 0 | `EV-2026-08-09-104`; `-10-152` |
| 9 | **MD** Moldova | **0,70** | **1,70** | **STA VAR ama 2204.21'i KAPSAMAZ** | (tercihli belge düzenlense de **oranı değiştirmez**) | — | 1,70 | 0 | `EV-2026-08-10-165` |
| +1 | **AR** Arjantin *(opsiyonel)* | **0,70** | **1,70** | **YOK** (MERCOSUR yürürlükte değil) | tercihsiz (koşullu) | — | 1,70 | 0 | `EV-2026-08-09-104`; `-10-152` |

**Tüm oranlar:** `status: FACT`, `tier: T1`, `effective_date: 2026-01-01`,
`ttl: 90d` → **2026-11-08'den sonra STALE** (İthalat Rejimi Kararı yıllıktır).

### 5.1 Ters modelde koşulluluğun anlamı — yön uyarısı

> **İleri modelde koşulun düşmesi maliyeti ARTIRIR; ters modelde azami satın
> alma fiyatını DÜŞÜRÜR.** İkisi aynı olayın iki yüzüdür ama işaretleri
> zıttır ve raporda karıştırılırsa okuyucu yanlış yöne bakar.

`ES/PT/IT/FR/CL` satırlarında `g` bir **veri değil, bir senaryo sonucudur**:

```
g = 0,50   ⟺   (K1 ∧ K2 ∧ K3 ∧ K4)  hepsi sağlanıyorsa
g = 0,70   ⟺   aksi hâlde                        [EV-2026-08-10-157]
```

`K3` (belge) `global-sourcing-kasifi`'nin (`T-161`), `K4` (çıkış ülkesi)
`navlun-lojistik-uzmani`'nın (`T-163`, `T-914`) alanındadır. **İkisi de
`ASSUMPTION: true`'dur ve `false` senaryosu ZORUNLU olarak çalıştırılır**
(`vergi.yaml → senaryo_degiskenleri`).

> **Şili'ye özgü çakışma:** en ucuz Şili LCL rotası **Barcelona aktarmalıdır**
> ama `SIL` rejiminde kabul edilen çıkış ülkesi **yalnız Şili**'dir
> (`EV-2026-08-10-160`). Bu ters modelde şu anlama gelir: **R5 (Şili) satırı
> için `1+g = 1,50` ve `1,70` senaryolarının İKİSİ DE çalıştırılmadan
> Şili'nin azami CIF'i raporlanamaz.**

---

## 6. TERS MODELDE YAPILMASI EN MUHTEMEL 5 VERGİ HATASI

Her hata için: yanlış formül · doğru formül · **sayısal büyüklük** · konulan kural.

### H1 — ⛔ **EN MUHTEMEL VE EN BÜYÜK: maktu ÖTV'nin bölmeye dahil edilmesi**

```
YANLIŞ:   C = L4_econ_max / (1 + g)  −  O
DOĞRU:    C = ( L4_econ_max − O ) / (1 + g)
```

Fark, cebirsel olarak **tam**:

```
C_yanlış − C_doğru = − O · g / (1 + g)
```

| `g` | Hata (TL/şişe, `O` = 53,4519) | Yön |
|---|---|---|
| 0,50 | **−17,8173** | azami CIF'i **eksik** gösterir |
| 0,70 | **−22,0096** | azami CIF'i **eksik** gösterir |

> **Neden bu hata bu kadar tehlikeli:** yönü **muhafazakâr** görünür
> (azami alım fiyatını düşürür) ve bu yüzden gözden kaçar; ama büyüklüğü
> gözlenen menşe CIF birim değerleriyle (2,46–2,89 USD/lt) **aynı mertebededir**.
> Yani bu tek hata, ekonomik olarak mümkün bir projeyi **imkânsız gösterebilir.**
>
> **KURAL R7-K1:** Maktu kalemler (ÖTV, ve varsa `X_pre`) **her zaman bölmeden
> önce** çıkarılır. Kod, oransal ve maktu kalemleri **ayrı listelerde** tutmalı
> ve maktu listesini bölme işleminden önce tüketmelidir.

---

### H2 — KDV'nin **iki kez** düşülmesi

```
YANLIŞ:   L8_net = L8/(1+v)  … sonra ayrıca …  L4_econ = L4_cash − KDV_ithal − …
          (ithalat KDV'si bir kez L8'de, bir kez maliyet olarak)
DOĞRU:    Zincirde TEK KDV işlemi vardır: R1'deki  L8/(1+v).
          İthalat KDV'si ekonomik zincirde SIFIR kez görünür.
```

**Büyüklük:** ithalat KDV'sinin tamamı = `v × L4_econ_max`.
`L4_econ_max = 200 TL` ise **40,00 TL/şişe** fazladan düşülür →
`CIF_max` `g=0,50`'de **26,67 TL**, `g=0,70`'te **23,53 TL** eksik çıkar.

> **KURAL R7-K2:** `kdv_ekonomik_maliyet = 0` (A1 baz senaryo,
> `EV-2026-08-10-101/-102/-103`). Ters modelin ekonomik dalında KDV yalnızca
> **R1'de bir bölme** olarak vardır. KDV'nin tutarı **hiçbir** çıkarma
> işleminde kullanılmaz.

---

### H3 — `L4_cash` ile `L4_econ`'un karıştırılması

`matrah-sirasi.md` §4'teki illüstrasyonda `L4 = 244,14` (CIF 100, %50) **KDV
DAHİLDİR**. Ters modelde `L5_max − bandrol` sonucunu bu tanımla eşleştirmek
KDV'yi maliyet saymaktır.

```
Büyüklük (X_pre = 0):   hata = L4_econ_max / 6        (çünkü L4_cash = 1,2 × L4_econ)
                        CIF_max kaybı = L4_econ_max / ( 6 × (1+g) )
```

`L4_econ_max = 200 TL` → `g=0,50`'de **−22,2222 TL/şişe**, `g=0,70`'te **−19,6078 TL/şişe**.

> **KURAL R7-K3:** Çıplak `L4` tokeni yasaktır (§1). Engine'in çıktı şeması
> `l4_econ` ve `l4_cash` alanlarını **ayrı** taşımalı ve toplamamalıdır (`C2`).

---

### H4 — Gümrük vergisi oranının **yanlış matraha** uygulanması

`g`, **yalnız CIF** üzerinden oransaldır. Ters modelde `(1+g)`'nin
`L4_econ`'a değil, `L4_econ − O − k`'ya uygulandığını unutmak H1'in
aynısıdır; ayrıca `(1+g)`'yi `L3` veya `L5` üzerine uygulamak yurt içi
masrafları gümrük vergisine tabi tutar — **GK md.28/a ihlali**
(`EV-2026-08-09-121`).

> **KURAL R7-K4:** `(1+g)` bölmesi zincirde **tam bir kez** ve **yalnız
> R7d'de** yapılır. `X_pre` ve `L5` kalemleri bölmeden **önce** çıkarılmıştır.

---

### H5 — ÖTV'nin **oransalmış gibi** taşınması

`O`'yu `L8`'in yüzdesi olarak, ya da `(1+g)` ile çarparak, ya da menşeye göre
değiştirerek taşımak. **ÖTV nispi oranı %0'dır** (`EV-2026-08-09-110`);
ÖTV ne fiyata, ne menşeye, ne kıymete duyarlıdır.

**Ters modeldeki tek doğru duyarlılık:**

```
∂ CIF_max / ∂ O  =  − 1 / (1 + g)
```

| `g` | ÖTV'de her **+1 TL/şişe** | ÖTV'de her **+%1** (`O`=53,4519 tabanında) |
|---|---|---|
| 0,50 | `CIF_max` **−0,6667 TL** | `CIF_max` **−0,3563 TL/şişe** |
| 0,70 | `CIF_max` **−0,5882 TL** | `CIF_max` **−0,3144 TL/şişe** |

> **Karşı-sezgisel sonuç:** ÖTV artışı, **yüksek tarifeli menşede TL olarak
> daha az** azami CIF kaybettirir (0,3144 < 0,3563) — çünkü kayıp `(1+g)` ile
> bölünür. Bu bir avantaj **değildir**: aynı menşenin `CIF_max` seviyesi
> zaten %11,765 daha düşüktür. **Oransal olarak** ÖTV artışı yüksek tarifeli
> menşeyi **daha ağır** vurur.

---

### H6 (ikincil) — Koşullu oranın tek senaryo olarak çalıştırılması

`g = 0,50`'yi veri sanmak. Bkz. §5.1. **KURAL:** `ES/PT/IT/FR/CL` için
`g ∈ {0,50 ; 0,70}` **iki senaryo zorunludur**.

---

## 7. ÖTV VE HEDEF TARİH — ÜÇ SENARYONUN TAŞINMASI

### 7.1 Tarih haritası

| Senaryo | `model_hedef_tarihi` | BASE_DATE'ten sonraki **planlı** ÖTVK md.12/3 güncellemesi | ÖTV durumu |
|---|---|---|---|
| **EARLY** | **2027-01-01** | 1 adım (Aralık sonu / Ocak başı) | **`FUTURE_UNKNOWN`** |
| **BASE** | **2027-04-01** | 1 adım | **`FUTURE_UNKNOWN`** |
| **LATE** | **2027-07-01** | 1 adım — **ve ikinci adımın eşiğinde** (§7.3) | **`FUTURE_UNKNOWN`** |

**Gözlenen gerçek:** 61,3914 (eff. 2025-12-31) → **71,2692 (eff. 2026-07-03)**
(`EV-2026-08-09-112`, `EV-2026-08-09-111`). Yani "Ocak" ayarlaması pratikte
**yılın son gününde** yürürlüğe girmiştir.

> ⛔ **ÜÇ SENARYONUN ÜÇÜNDE DE 71,2692 TL/lt YÜRÜRLÜKTE OLMAYACAKTIR**
> (Cumhurbaşkanı md.12/3'ün uygulanmamasına karar vermedikçe — `EV-2026-08-09-114`).
> **Hiçbiri için 2027 tutarı bu belgede yazılmaz, tahmin edilmez, türetilmez.**

### 7.2 Taşıma kuralı — `O` bir SABİT DEĞİL, PARAMETREDİR

```
O(t, λ) = CURRENT_CONFIRMED × hacim_litre × λ
        = 71,2692 × 0,75 × λ
        = 53,4519 × λ            [TRY/şişe]

CURRENT_CONFIRMED : 71,2692 TL/lt · eff 2026-07-03 · FACT · T2 · EV-2026-08-09-111
λ                 : BASE_DATE ile t arasındaki kümülatif ÖTV artış katsayısı
                    λ ≥ 1  (Yİ-ÜFE negatif olmadıkça)
                    λ = FUTURE_UNKNOWN — BU BELGEDE DEĞER ATANMAZ
```

**Üç senaryonun çalıştırılma biçimi (BAĞLAYICI):**

| # | Kural |
|---|---|
| **O-1** | Üç senaryo da **`λ = 1` (CURRENT_CONFIRMED)** ile çalıştırılır — bu **tek doğrulanmış** değerdir. |
| **O-2** | Çıktı, her üç senaryoda da şu etiketi **zorunlu** taşır: `ÖTV = CURRENT_CONFIRMED (71,2692 TL/lt, eff 2026-07-03) — HEDEF TARİHTE YÜRÜRLÜKTE OLMASI BEKLENMEZ` |
| **O-3** | `λ = 1` sonucu bir **tahmin değil, ÜST SINIRDIR**: `λ ≥ 1` olduğu için gerçek `CIF_max` bu değerden **düşük** olacaktır. Çıktı `CIF_TRY_max` değil, **`CIF_TRY_max_UPPER_BOUND`** adıyla raporlanır. |
| **O-4** | `λ > 1` bir **duyarlılık ekseni** olarak, `λ`'nın kendisi eksen değişkeni olarak çalıştırılır (`senaryolar.yaml`). `λ` için sayı seçmek **`gumruk-vergi-uzmani`'nin alanı değildir**; Yİ-ÜFE varsayımı `makro.yaml`'da `ASSUMPTION` olarak durur. |
| **O-5** | `vergi.yaml → otv_maktu_zaman_serisi.engine_okuma_kurali` gereği: `t > 2026-12-31` **ve** `senaryolar.yaml`'da açık bir ÖTV `ASSUMPTION`'ı **yoksa** engine `UNKNOWN` döner. **O-1 bu kuralı DELMEZ** — `λ=1` çalıştırması `PROJEKSİYON DEĞİL, ÇAPA (ANCHOR)` etiketiyle ve `status: UPPER_BOUND` ile üretilir. |
| **O-6** | ÖTV çıktısı **asla** `FACT` olarak raporlanmaz; en iyi hâlde `FACT (2026-07-03 tutarı) + hedef tarihte GEÇERSİZ`. |

**Sapmanın yönü ve büyüklüğü (tahmin değil, katsayı):**

```
Δ CIF_max = − ( λ − 1 ) × 53,4519 / (1 + g)

g = 0,50 →  her %1 ÖTV artışı için  −0,3563 TL/şişe azami CIF
g = 0,70 →  her %1 ÖTV artışı için  −0,3144 TL/şişe azami CIF
```

> **Tarihsel referans (TAHMİN DEĞİLDİR, tek gerçekleşmiş gözlem):**
> 2025-12-31 → 2026-07-03 arası tek adım **+%16,09**'dur
> (`EV-2026-08-09-111`, `-112`). Bu sayı burada **yalnızca mekanizmanın
> mertebesini** göstermek için, `λ` için bir değer **olarak kullanılmaksızın**
> anılmaktadır. Modelde `λ = 1,1609` yazılması **bu belgenin ihlalidir.**

### 7.3 LATE senaryosunun uçurum riski

2026'da Temmuz ayarlaması **3 Temmuz**'da yürürlüğe girmiştir. `LATE = 2027-07-01`
bu eşiğin **iki gün öncesindedir**. Yani:

- Beyanname tescili **2027-07-01**'de olursa → Ocak-2027 tutarı,
- Tescil birkaç gün kayarsa → **Temmuz-2027 tutarı** (bir adım daha yüksek).

**Vergi, serbest dolaşıma giriş beyannamesinin tescil tarihinde doğar**
(`EV-2026-08-09-122`). Antrepoda bekleme veya gümrük gecikmesi bu eşiği
**tek başına** geçirebilir.

> **KURAL O-7:** `LATE` senaryosu, `λ_1adım` ve `λ_2adım` olmak üzere
> **iki alt-koşulla** raporlanır; hangisinin gerçekleşeceği `UNKNOWN`'dır.
> Bu, `antrepo_etkilesimi` kaydının (`vergi.yaml`) sayısal karşılığıdır ve
> `T-301` (antrepo bekleme süresi, CRITICAL) ile doğrudan bağlıdır.

### 7.4 Bandrol de tarihe bağlıdır — **alan dışı uyarı**

Bandrol birim bedeli **her yıl 1 Ocak'tan geçerli olmak üzere önceki yıl
Yİ-ÜFE oranında** güncellenir (`EV-2026-08-09-213`). Üç hedef tarihin **üçü de
2027'dedir** → `B = 2,36073` de hedef tarihte yürürlükte olmayacaktır.

> Bu bir **vergi bulgusu değildir** ve `mevzuat-ruhsat-uzmani` alanındadır;
> sonuç üretmiyorum. Yalnızca ters modelin `L4_econ_max` girdisinin **aynı
> tarih hatasını taşıdığını** işaret ediyorum → `99-ops/_parts/capraz-ipuclari-…-tur25.md`.

---

## 8. KDV — ECONOMIC vs CASH AYRIMININ TERS MODELDE UYGULANMASI

**İki görünüm ters modelde FARKLI SORULARA cevap verir ve farklı çıktılara gider.**

| | **A) ECONOMIC COST VIEW** | **B) CASH REQUIREMENT VIEW** |
|---|---|---|
| Sorusu | *"Üreticiye en fazla kaç TL ödeyebilirim?"* | *"Bu işi çevirmek için kasada kaç TL olmalı?"* |
| İthalat KDV'si | **0,00 TL/şişe** — düşülmez | **Tam tutar** — `v × L4_econ` |
| Zincirde KDV işlemi | **Tek bölme** (R1: `L8/(1+v)`) | Ayrı örtü (R9), zincire girmez |
| Ürettiği çıktı | **`CIF_TRY_max`** | **`peak_cash_requirement`** bileşenleri |
| Girdiği katman | L4_econ → L2 | hiçbir katmana girmez; **zaman ekseni** |
| Dayanak | `EV-2026-08-10-101/-102/-103` (KDVK md.29/1-b, md.34/1, md.30) | `EV-2026-08-10-107` (md.46/2), `EV-2026-08-10-104` (md.29/2) |

### 8.1 Bağlayıcı kurallar (mevcut `C1–C5`'in ters yöndeki karşılığı)

| # | Kural |
|---|---|
| **RC1** | `CIF_TRY_max` **yalnızca A görünümünden** üretilir. B görünümü `CIF_TRY_max`'ı **hiçbir koşulda** değiştirmez. |
| **RC2** | B görünümü, A görünümü **bittikten sonra**, bulunan `CIF_TRY_max` üzerinde çalıştırılır (R9). Sıra ters çevrilemez. |
| **RC3** | İki görünümün sayıları **aynı tabloda toplanamaz** ve aynı satırda gösterilemez (CLAUDE.md §6). |
| **RC4** | Devreden KDV'nin **finansman maliyeti** A görünümünde `L5_kalemleri` içinde **ayrı satır**dır (`C3`). Bu, KDV'nin kendisi değildir; karıştırılırsa H2 hatasına dönüşür. |
| **RC5** | Fire/zayi oranı `f` varsa, `f × KDV_ithal` A görünümünde **gerçek maliyettir** (KDVK md.30/c). `f` `UNKNOWN` (`T-314`) → model bu satırı `0` alırsa **çıktıda yazmak zorundadır**. |
| **RC6** | B görünümü, A görünümünde `0` olan KDV'yi "kâr" gibi göstermez: devreden KDV **iade edilmez** (`EV-2026-08-10-104`), yalnız satış hızına bağlı olarak erir. |

### 8.2 Karıştırmanın sayısal bedeli

A yerine B kullanılırsa (= H2/H3), azami CIF **`L4_econ_max / (6 × (1+g))`**
kadar eksik çıkar. `L4_econ_max = 200 TL` için:

| `g` | Doğru `CIF_max` (A) | Yanlış `CIF_max` (B kullanılırsa) | Fark |
|---|---|---|---|
| 0,50 | **97,6987** | 75,4765 | **−22,2222** (%22,7) |
| 0,70 | **86,2048** | 66,5969 | **−19,6078** (%22,7) |

> **Her iki menşede de kayıp oranı aynıdır: %22,7.** Yani bu hata **menşe
> karşılaştırmasını bozmaz ama seviyeyi bozar** — sinsi olmasının nedeni budur.
> *(Bu tablo bir model çıktısı değildir; `L4_econ_max = 200 TL` keyfîdir.)*

---

## 9. BİRİM TEST VEKTÖRLERİ — `finans-fizibilite` İÇİN

Aşağıdaki vektörler **gerçek veri değildir**; `L4_econ_max = 200,0000 TL/şişe`
keyfî bir sayıdır ve **yalnız cebirin doğruluğunu test etmek** içindir.
Sabitler: `O = 53,4519`, `k = 0` (peşin), `X_pre = 0`, `v = 0,20`.

| # | Girdi | `g` | Beklenen `CIF_TRY_max` | Doğrulama (ileri yön) |
|---|---|---|---|---|
| **TV-1** | `L4_econ_max = 200,0000` | 0,50 | **97,6987** | GV=48,8494 · ÖTV mat.=146,5481 · +ÖTV=200,0000 ✓ |
| **TV-2** | `L4_econ_max = 200,0000` | 0,70 | **86,2048** | GV=60,3433 · ÖTV mat.=146,5481 · +ÖTV=200,0000 ✓ |
| **TV-3** | TV-1 / TV-2 oranı | — | **0,88235** | = 1,50/1,70 ✓ (§4.1) |
| **TV-4** | KDV nakit örtüsü, her iki menşe | — | `KDV_ithal = 40,0000` | `= 0,20 × 200,0000` — **menşeden bağımsız** ✓ |
| **TV-5** | `L4_cash` | — | **240,0000** | `= 1,20 × L4_econ_max` ✓ |
| **TV-6** | **H1 hatası** (yanlış sıra) | 0,50 | 79,8814 | doğru 97,6987 → **−17,8173** ✗ |
| **TV-7** | **H1 hatası** | 0,70 | 64,1952 | doğru 86,2048 → **−22,0096** ✗ |
| **TV-8** | **H3 hatası** (`L4_cash`↔`L4_econ`) | 0,50 | 75,4765 | doğru 97,6987 → **−22,2222** ✗ |
| **TV-9** | `ödeme_şekli = 'mal mukabili'` | 0,50 | **`UNKNOWN`** | KKDF matrahı `UNKNOWN` (`T-105`) — model sayı ÜRETMEZ ✓ |
| **TV-10** | `t = 2027-04-01`, `senaryolar.yaml`'da ÖTV ASSUMPTION yok | 0,50 | `97,6987` **+ zorunlu `UPPER_BOUND` etiketi** | O-2/O-3/O-5 etiketleri yoksa çıktı **GEÇERSİZ** ✓ |

> **TV-9 ve TV-10, "model uydurmaz" kilidinin testleridir.** Bu ikisi geçmiyorsa
> model CLAUDE.md §12'yi ihlal ediyordur ve çalıştırılmamalıdır.

---

## 10. TERS MODELDEKİ VERGİ BACAĞININ `UNKNOWN` DÖNMESİ **GEREKEN** HÂLLERİ

```
odeme_sekli != 'pesin'                        -> KKDF matrahi UNKNOWN (T-105)
mense tablosunda yoksa                        -> DU fallback %70 + "DU FALLBACK" etiketi
t > 2026-12-31 ve ASSUMPTION yok              -> OTV UNKNOWN ya da UPPER_BOUND etiketi (O-5)
L8_target verilmemis / null                   -> tum ters zincir UNKNOWN (T-603)
round-trip assertion (R8) tutmuyor            -> UNKNOWN + hangi adimin tutmadigi
doviz cinsinden CIF/FOB istenirse             -> UNKNOWN (T-911 kur kurali, T-912 fx)
gozetim esigi > CIF_TRY_max                   -> "YAPISAL OLARAK IMKANSIZ" (§11)
```

---

## 11. GÖZETİM — TERS MODELDE **ALT SINIR**, İLERİ MODELDE ÜST BASKI

İleri modelde gözetim, beyan edilen kıymeti **yukarı** iter (maliyeti artırır).
Ters modelde ise mantık farklıdır ve daha serttir:

```
ters model üretir:      CIF_TRY_max          ← ÜST SINIR (ticari olarak mümkün olan azami)
gözetim dayatır:        CIF_beyan ≥ eşik     ← ALT SINIR (hukuken beyan edilebilir asgari)

eğer  eşik > CIF_TRY_max   ⇒  ARADA ÇÖZÜM YOKTUR
```

Bu durumda proje **fiyat pazarlığıyla kurtarılamaz**: tedarikçi bedava verse
bile beyan edilecek kıymet eşiğin altına inemez ve gümrük vergisi + KDV o eşik
üzerinden doğar.

> **Durum:** 2204.21 için yürürlükte gözetim tebliği **bulunamadı**
> (`EV-2026-08-09-125`) — ancak bu **negatif bir arama sonucudur, yokluğun
> kanıtı değildir.** Ters model bu yüzden `gozetim_esigi` parametresini
> **açıkça `null`** taşımalı ve çıktıda *"gözetim eşiği doğrulanmamıştır;
> `CIF_TRY_max` bir alt sınırla test EDİLMEMİŞTİR"* uyarısını basmalıdır.
> ÖTV maktu olduğu için gözetimden **etkilenmez** (`EV-2026-08-09-113`).

---

## 12. `vergi.yaml` KARŞILIĞI

Bu belgenin makine okunur karşılığı `80-model/inputs/vergi.yaml` →
**`ters_model_vergi_bacagi`** bloğudur. Blok yalnızca **eklenmiştir**;
mevcut hiçbir blok değiştirilmemiştir.

Engine, ters modelde:
- `g`'yi `mense_tarife_eslemesi.engine_okuma_kurali`'ndan (koşullu),
- `O`'yu `otv_maktu_zaman_serisi.engine_okuma_kurali`'ndan,
- `v`'yi `matrah_sirasi[sıra=5].oran_pct`'ten,
- sırayı `ters_model_vergi_bacagi.adimlar`'dan

okur. **Hiçbiri kodda sabitlenmez.**

---

## 13. BU BULGUYU NE ÇÜRÜTÜR?

### 13.1 Hangi mevzuat değişikliği bu ters formülü geçersiz kılar?

- **ÖTV nispi oranının %0'dan farklı belirlenmesi.** Ters formülün tamamı
  `ÖTV = maktu sabit` varsayımına dayanır. Nispi oran > 0 olursa ÖTV, ÖTV
  matrahının (yani `C(1+g)`'nin) fonksiyonu olur ve R7 şu hâle gelir:
  ```
  L4_econ = C(1+g) + max( r_nispi × C(1+g) ; O )
  ```
  Bu **parçalı-doğrusal** bir denklemdir; tek bir bölmeyle çözülemez, iki dal
  ayrı çözülüp `max` koşulu doğrulanmalıdır. **Bu, bu belgeyi tek başına
  çürütecek en temiz bulgudur.** (`EV-2026-08-09-110` şu an %0 diyor.)
- **KDV indirim hakkının alkolde kısıtlanması** (KDVK md.36 uyarınca bir CB
  kararı — **aranmadı**, `T-151`, `OQ-G10`). O hâlde §8'in A sütunu çöker,
  KDV ekonomik maliyet olur ve `CIF_TRY_max` yaklaşık **%22,7 düşer** (§8.2).
  **Bu, ters modelin en kırılgan tek dayanağıdır** ve `master-commercial-input-table.md`
  §7 de aynı noktayı işaret etmektedir.
- **İthalat Rejimi Kararı'nın 2027 sürümü** (her 1 Ocak). Üç hedef tarihin
  **üçü de 2027'dedir** → §5 tablosundaki `g` değerlerinin **hiçbiri hedef
  tarihte doğrulanmış değildir.** `ttl: 90d` bu yüzden konmuştur.
  **Uyarı: ÖTV için titizlikle uygulanan "gelecek değer yazma" kuralı,
  gümrük vergisi oranı için de geçerlidir ve bu belge `g`'yi 2027'de
  değişmez varsayarak bir ASİMETRİ taşımaktadır.** Bu asimetri burada
  açıkça itiraf edilmiştir; `g` de en az `O` kadar tarihe bağlıdır.
- **1/98 sayılı OKK'nın revizyonu** → `1,50` bölenlerinin tamamı değişir.

### 13.2 Hangi GTİP itirazı tüm yapıyı değiştirir?

- **Köpüklü (2204.10) tespiti:** `O` 53,4519 → **361,1360 TL/şişe**.
  Ters formül **aynen çalışır** ama `CIF_TRY_max`'tan `(361,1360 − 53,4519)/(1+g)`
  = `g=0,50`'de **−205,1227 TL/şişe**, `g=0,70`'te **−180,9906 TL/şişe** düşer.
  Fiyat/performans segmentinde `L4_econ_max` bu mertebeye ulaşmaz →
  **`CIF_TRY_max` negatife düşer**, yani ürün matematiksel olarak imkânsızdır.
  **Ters model bunu ileri modelden daha net gösterir:** negatif azami alım
  fiyatı tartışılamaz bir sonuçtur.
- **22.05 (aromatize/vermut):** `O` = 545,0441 TL/şişe → aynı mantık, daha kötü.
- **12 haneli alt kod itirazı:** `g`'yi de `O`'yu da **değiştirmez**
  (`EV-2026-08-09-102`) → ters formül **etkilenmez.** Yapının en dayanıklı yeri.

### 13.3 Gözetim / kıymet itirazı senaryosunda ne olur?

§11'de tam olarak yazılmıştır: gözetim ters modelde bir **alt sınır** dayatır
ve `eşik > CIF_TRY_max` olduğu anda **çözüm kümesi boşalır.** İleri modelde bu
"maliyet arttı" gibi görünür ve pazarlıkla kurtarılabilirmiş izlenimi verir;
ters modelde ise **kurtarılamayacağı** hemen görülür. ÖTV maktu olduğu için
gözetimden etkilenmez, dolayısıyla itirazın etkisi `g` kanalıyla sınırlıdır ve
**DÜ menşede (%70) AB/Şili menşeye (%50) göre 1,4 kat ağırdır.**

### 13.4 Bu belgeyi çürütecek **operasyonel** bulgu

**`X_pre`'nin sıfır olmadığının tespiti.** §4.3'te tüm yurt içi masrafların
KDV'ye tabi olduğu ve bu nedenle md.21/c dışında kaldığı **türetilmiştir**,
bir gümrük müşavirine **doğrulatılmamıştır.** Gerçek bir gümrük
beyannamesinde KDV matrahı satırının CIF+GV+ÖTV toplamından **büyük** çıkması,
§4.3'ü ve dolayısıyla R7'yi çürütür. `master-commercial-input-table.md` §7'nin
işaret ettiği **tek gerçekleşmiş ithalat beyannamesi**, bu belgeyi de aynı anda
test eder — ve bu, en ucuz çürütme yoludur.

### 13.5 Bu belgenin kendi zayıflığı (dürüstlük kaydı)

- §4.2 (bandrol) ve §4.3 (`X_pre`) **hukuki türetmelerdir**, `FACT` değil
  `ESTIMATE`'tir. İkisi de aynı bende (md.21/c "vergilendirilmeyenler")
  dayanır; o bendin idari uygulaması (KDVGUT) **okunmamıştır** (`T-151`).
- `λ` (ÖTV artış katsayısı) için değer vermeyi reddettim. Bu **doğru** ama
  **bedava değil**: üç hedef tarih senaryosunun üçü de aynı `λ=1` çapasıyla
  çalışacağı için, **üç senaryo ÖTV açısından birbirinden ayrışmayacaktır.**
  Yani hedef tarih seçiminin ÖTV etkisi modelde **görünmeyecektir** —
  yalnızca §7.2'deki katsayı üzerinden okunabilir. Bu bir eksikliktir ve
  kapatılması `makro.yaml`'da bir Yİ-ÜFE `ASSUMPTION`'ı gerektirir
  (`finans-fizibilite` + başkan kararı).
