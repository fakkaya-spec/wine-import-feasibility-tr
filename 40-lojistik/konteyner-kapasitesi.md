# KONTEYNER KAPASİTESİ — 750 ml ŞARAP

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 1
tarih:  2026-08-09
durum:  DRAFT
```

> **KURAL:** Bu dosyadaki her sayı ya kanıt kartına ya da bu dosyada **adım adım
> gösterilen** bir hesaba dayanır. Hatırlanan sayı yoktur.
>
> **En kritik uyarı:** Hacim kısıtı ile ağırlık kısıtı **ayrı ayrı** hesaplanmış,
> bağlayıcı kısıt her senaryo için açıkça belirtilmiştir.

---

## 0. ÖZET TABLO (ÖNCE SONUÇ)

| Senaryo | Hacim kısıtlı kapasite (şişe) | Ağırlık kısıtlı kapasite (şişe) | **Bağlayıcı kısıt** | **Pratik kapasite (şişe)** |
|---|---|---|---|---|
| **20DV — paletli**, std palet, 12'li koli, 4 katman | 6.480 – 7.200 | 20.400 – 22.400 | **HACİM** (zemin alanı + palet yüksekliği) | **6.480 – 7.200** |
| **20DV — paletli**, Euro palet, 12'li koli, 4 katman | ~6.336 | 20.400 – 22.400 | **HACİM** | **~6.336** |
| **20DV — paletsiz (floor loaded)** | 11.800 – 13.700 | 20.400 – 22.400 | **HACİM** | **11.800 – 13.700** |
| **40HC — paletli**, std palet, 12'li koli, 4 katman | 14.400 – 15.120 | 19.100 – 21.500 | **HACİM** | **14.400 – 15.120** |
| **40HC — paletli**, std palet, 12'li koli, **5 katman** | 18.000 – 18.900 | 19.100 – 21.500 | **SINIRDA** (ikisi de) | **18.000 – 18.900** ⚠ |
| **40HC — paletsiz (floor loaded)** | 27.100 – 31.400 | **19.100 – 21.500** | **AĞIRLIK** | **19.100 – 21.500** |

**Ana bulgu 1 — 20DV'de şarap AĞIRLIK değil HACİM kısıtlıdır.**
Paletli 20DV'de payload'ın yalnızca **%30–33'ü** kullanılır. "Şarap ağırdır,
20'lik konteyner ağırlıktan dolar" sezgisi **bu formatta yanlıştır**.

**Ana bulgu 2 — 40HC paletsizde bağlayıcı kısıt konteynerin payload'ı değil,
Türkiye karayolu 44 ton GVW limitidir.** Konteyner 28.690 kg taşıyabilir, ama
Türkiye'de karayoluna çıkabilmesi için yük ~24,1–27,1 tonla sınırlıdır
(`EV-2026-08-09-310`).

**Ana bulgu 3 — Sarapta 2 × 20DV, 1 × 40HC'den DAHA FAZLA şişe taşır**
(23.600–27.400 vs 19.100–21.500). Çünkü ağırlık limiti **konteyner başına değil
araç başına** uygulanır. 40HC'nin iç hacminin ~%30'u kullanılamaz kalır
(`EV-2026-08-09-322`).

---

## 1. GİRDİ PARAMETRELERİ

### 1.1 Şişe (750 ml durgun şarap)

| Parametre | Değer | status | evidence_id |
|---|---|---|---|
| Şarap kütlesi | 750 ml × ~0,99 g/ml ≈ **0,743 kg** | ESTIMATE | `EV-2026-08-09-305` |
| Boş cam — hafifletilmiş | 300 – 420 g | ESTIMATE | `EV-2026-08-09-304` |
| Boş cam — durgun şarap tipik | 420 – 550 g | ESTIMATE | `EV-2026-08-09-304` |
| Boş cam — köpüklü (kapsam dışı) | 800 – 900 g | ESTIMATE | `EV-2026-08-09-304` |
| Mantar + kapsül + etiket | ~10 – 15 g | ASSUMPTION | — |
| **Dolu şişe brüt** | **1,16 – 1,32 kg** | ESTIMATE | `EV-2026-08-09-305` |
| Şişe boyutları (çap/yükseklik) | **UNKNOWN** | UNKNOWN | — |

> **Şişe boyutu UNKNOWN'dır.** Kaset içi geometri, koli spec'inden *dolaylı*
> türetilmiştir (§1.3). Gerçek şişe çap/yükseklik ölçüsü tedarikçiden alınmalıdır
> (ticket `T-302`). Burgundy formu şişe, Bordeaux formuna göre koli hacmini
> belirgin biçimde büyütür ve konteyner kapasitesini düşürür.

### 1.2 Koli

| Parametre | 6'lı koli | 12'li koli | evidence_id |
|---|---|---|---|
| Boş karton + bölme | ~0,28 kg (türetilmiş) | **0,55 kg** | `EV-2026-08-09-306` |
| Koli brüt (yayınlanmış) | — | **13,6 – 18 kg** | `EV-2026-08-09-306` |
| Koli brüt (spec sheet'ten geri hesap) | **7,59 kg** | **15,1 kg** | `EV-2026-08-09-307` |
| Yayınlanmış dış ölçü örnekleri | — | Burgundy 410×305×345 mm; Sauvignon 375×275×380 mm | `EV-2026-08-09-306` |

**Geri hesap (türetme zinciri):**
```
Cellwind spec: std palet (1000×1200), 12'li koli, 4 katman = 60 koli, 927 kg brüt
  927 kg − ahşap palet darası ~20 kg = 907 kg net yük
  907 kg / 60 koli = 15,12 kg / koli
  15,12 kg / 12 şişe = 1,26 kg / şişe (ambalaj payı dahil)

Çapraz kontrol — 6'lı format:
Cellwind spec: std palet, 6'lı koli, 4 katman = 112 koli, 870 kg brüt
  870 − 20 = 850 kg / 112 koli = 7,59 kg / koli
  7,59 / 6 = 1,265 kg / şişe   ✓ 12'li ile TUTARLI (%0,4 fark)
```

**→ `PACKED_WEIGHT_PER_BOTTLE` = 1,26 kg** (merkezî değer)
**→ Band: 1,21 – 1,38 kg** (hafif cam → ağır cam)
```
hafif  : (0,743 + 0,400 + 0,012) + 0,055 (karton payı) ≈ 1,21 kg
ağır   : (0,743 + 0,550 + 0,015) + 0,070              ≈ 1,38 kg
```

### 1.3 Şişe başına paketli HACİM (türetme — kritik ara değer)

Cellwind palet spec'i hem alan hem katman verdiği için koli hacmi geri hesaplanabilir:

```
12'li koli:
  Palet alanı 1,000 m × 1,200 m = 1,20 m², katmanda 15 koli
  → koli taban alanı = 1,20 / 15 = 0,0800 m²  (koliler arası boşluk dahil)
  Yüklü palet yüksekliği 1.480 mm − palet deck ~145 mm = 1.335 mm / 4 katman
  → koli yüksekliği = 334 mm
  → koli hacmi = 0,0800 × 0,334 = 0,02672 m³
  → şişe başına = 0,02672 / 12 = 0,002227 m³/şişe

6'lı koli:
  1,20 / 28 koli = 0,04286 m² × 0,334 m = 0,01431 m³
  → şişe başına = 0,01431 / 6 = 0,002386 m³/şişe
```

**→ `PACKED_VOLUME_PER_BOTTLE` = 0,00223 – 0,00239 m³/şişe**
(6'lı koli hacimsel olarak ~%7 daha verimsizdir — daha çok karton, daha çok boşluk.)

> ⚠ Burgundy formu şişe için yayınlanan 410×305×345 mm'lik 12'li koli
> 0,00360 m³/şişe verir — yani **%60 daha kötü**. Bu senaryoda tüm kapasiteler
> ~%38 düşer. Bu, tek başına en büyük belirsizlik kaynağıdır (bkz. §7).

### 1.4 Palet konfigürasyonları (`EV-2026-08-09-307`)

| Palet | Koli tipi | Katman | Koli/palet | **Şişe/palet** | Brüt kg | Yükseklik mm |
|---|---|---|---|---|---|---|
| Std 1000×1200 | 6'lı | 4 | 112 | **672** | 870 | 1.480 |
| Std 1000×1200 | 6'lı | 5 | 140 | **840** | 1.083 | 1.818 |
| Std 1000×1200 | 12'li | 4 | 60 | **720** | 927 | 1.480 |
| Std 1000×1200 | 12'li | 5 | 75 | **900** | 1.154 | 1.818 |
| Euro 800×1200 | 6'lı | 4 | 100 | **600** | 780 | 1.490 |
| Euro 800×1200 | 12'li | 4 | 48 | **576** | 751 | 1.490 |

Hillebrand Gori tavsiyesi: **yüklü palet yüksekliği 1,7 m'yi aşmamalı**
(`EV-2026-08-09-308`). → 5 katman (1.818 mm) bu tavsiyenin **dışındadır**;
yalnızca 40HC'de ve yükleme onayıyla düşünülmelidir.

### 1.5 Konteynerler

| | 20DV | 40HC | evidence_id |
|---|---|---|---|
| İç ölçü | 5,90 × 2,35 × 2,39 m | ~12,03 × 2,35 × 2,69 m | `EV-...-301` / `EV-...-303` |
| Hesaplanan iç hacim | 5,90×2,35×2,39 = **33,14 m³** | — | hesap |
| **Yayınlanmış iç hacim (Maersk)** | **33,2 m³** | **76,4 m³** | `EV-2026-08-09-302` |
| Dara | ~2.300 kg | ~3.900 kg (ASSUMPTION) | `EV-...-301` / — |
| **Azami payload (Maersk)** | **28.300 kg** | **28.690 kg** | `EV-2026-08-09-302` |
| Palet adedi — Std (1000×1200) | **9 – 10** | **20 – 21** | `EV-...-308`,`EV-...-309` ⚠C-301 |
| Palet adedi — Euro (800×1200) | **10 – 11** | **23 – 24** | `EV-...-308`,`EV-...-309` ⚠C-301 |

Hesaplarda `33,14 m³` (20DV) ve `76,4 m³` (40HC) kullanılmıştır.

### 1.6 Türkiye karayolu ağırlık tavanı (kritik ve sık atlanan kısıt)

`EV-2026-08-09-310` (KGM, Karayolları Trafik Yönetmeliği Md.128 — **T2**):

- **Konteyner taşıyan yarı römorklu araçlarda (ISO Konteynerli 3-S2/3): 44 ton**
- 5+ dingilli yarı römorklu/römorklu katarlarda: 40 ton
- Tartı toleransı: azami yüklü ağırlığın en çok **%5'i**

```
KARGO TAVANI = 44.000 kg − (çekici + şasi darası) − (konteyner darası)

Çekici + şasi darası: 13.000 – 16.000 kg   ← ASSUMPTION, kanıt YOK (T-304)

20DV : 44.000 − 13.000 − 2.300 = 28.700 kg → konteyner payload'ı (28.300) bağlar
       44.000 − 16.000 − 2.300 = 25.700 kg
       → 20DV kargo tavanı: 25.700 – 28.300 kg

40HC : 44.000 − 13.000 − 3.900 = 27.100 kg
       44.000 − 16.000 − 3.900 = 24.100 kg
       → 40HC kargo tavanı: 24.100 – 27.100 kg   ← KONTEYNER PAYLOAD'INDAN DÜŞÜK
```

> **Bu, modelin en kolay gözden kaçan kısıtıdır.** 40HC'de yükleme limanında
> 28,6 ton yüklenebilir, ama Türkiye'de o konteyneri karayoluna çıkaramazsınız.

---

## 2. 20DV HESABI

### 2.1 Paletli (standart 1000×1200 palet, 12'li koli, 4 katman)

```
HACİM/ZEMİN KISITI
  Palet adedi 20DV'de: 9 – 11 (kaynak çelişkisi C-301 → band kullanıldı)
  Std palet (1000×1200) için: 9 – 10 palet
  Şişe = palet_adedi × 720
     9 palet  →  6.480 şişe
    10 palet  →  7.200 şişe
  → HACİM KISITLI KAPASİTE = 6.480 – 7.200 şişe

  Kullanılan yükseklik: 1.480 mm / 2.390 mm = %62
  → Konteyner yüksekliğinin %38'i BOŞ (palet üstüne ikinci palet konamaz:
    2 × 1.480 = 2.960 mm > 2.390 mm)

AĞIRLIK KISITI
  Yük ağırlığı = palet_adedi × 927 kg
     9 palet → 8.343 kg    10 palet → 9.270 kg
  Kargo tavanı (§1.6) = 25.700 – 28.300 kg
  Payload kullanımı = 9.270 / 28.300 = %33
  Ağırlık kısıtlı kapasite = 25.700 / 1,26 = 20.400 şişe
                             28.300 / 1,26 = 22.400 şişe
  → AĞIRLIK KISITLI KAPASİTE = 20.400 – 22.400 şişe

BAĞLAYICI KISIT = min(7.200 ; 22.400) = HACİM
PRATİK KAPASİTE = 6.480 – 7.200 şişe
```
`EV-2026-08-09-320`

### 2.2 Paletli — Euro palet (800×1200, 12'li koli, 4 katman)

```
11 palet × 576 şişe = 6.336 şişe ; ağırlık 11 × 751 = 8.261 kg (payload %29)
→ HACİM KISITLI. Std palete göre biraz DAHA KÖTÜ (6.336 < 7.200).
```

### 2.3 Paletli — 6'lı koli (std palet, 4 katman)

```
9–10 palet × 672 şişe = 6.048 – 6.720 şişe ; 7.830 – 8.700 kg
→ 12'li koliden ~%7 daha az şişe. 6'lı koli hacimsel olarak verimsizdir.
```

### 2.4 Paletsiz — floor loaded (kolilerin doğrudan istiflenmesi)

```
HACİM KISITI
  Kullanılabilir hacim = 33,14 m³ × kup_verimi
  Kup verimi (floor loading, istif boşlukları + kapı payı): %85 – %92  [ASSUMPTION]

  Alt uç (6'lı koli, %85 verim):
     33,14 × 0,85 / 0,002386 = 11.806 şişe
  Üst uç (12'li koli, %92 verim):
     33,14 × 0,92 / 0,002227 = 13.691 şişe
  → HACİM KISITLI KAPASİTE = 11.800 – 13.700 şişe

  ÇAPRAZ KONTROL: yayınlanmış iddia 13.200 şişe (2.200 × 6'lı karton)
  → EV-2026-08-09-311, T5. Bandımızın ÜST ucunda. Tutarlı. ✓

AĞIRLIK KISITI
  13.700 × 1,26 = 17.262 kg → kargo tavanının (25.700–28.300) %61–67'si
  Ağırlık kısıtlı kapasite = 20.400 – 22.400 şişe

BAĞLAYICI KISIT = min(13.700 ; 20.400) = HACİM
PRATİK KAPASİTE = 11.800 – 13.700 şişe
```
`EV-2026-08-09-320`

**Paletsiz kazancı: +%64 ile +%90 daha fazla şişe** (7.200 → 11.800–13.700).
Bu, 20DV'de paletlemenin çok pahalı bir tercih olduğunu gösterir.

---

## 3. 40HC HESABI

### 3.1 Paletli (std palet, 12'li koli, 4 katman)

```
HACİM/ZEMİN KISITI
  20 – 21 std palet × 720 şişe = 14.400 – 15.120 şişe
  Kullanılan yükseklik 1.480 / 2.690 mm = %55 → %45 boş

AĞIRLIK KISITI
  20–21 × 927 kg = 18.540 – 19.467 kg
  Kargo tavanı (§1.6) = 24.100 – 27.100 kg → SIĞAR (%72–81 kullanım)
  Ağırlık kısıtlı kapasite = 24.100/1,26 = 19.127 ; 27.100/1,26 = 21.508

BAĞLAYICI KISIT = min(15.120 ; 19.127) = HACİM
PRATİK KAPASİTE = 14.400 – 15.120 şişe
```

### 3.2 Paletli — 5 katman (1.818 mm) ⚠

```
20 – 21 palet × 900 şişe = 18.000 – 18.900 şişe
Ağırlık = 20–21 × 1.154 kg = 23.080 – 24.234 kg
Kargo tavanı = 24.100 – 27.100 kg

→ 24.234 kg, tavanın ALT UCUNU (24.100 kg) AŞIYOR.
→ Çekici/şasi darası 16 t ise bu yükleme Türkiye'de KARAYOLUNA ÇIKAMAZ.
→ 5 katman ayrıca Hillebrand'ın 1,7 m tavsiyesini aşar (EV-...-308) ve
  alt kolilerde ezilme (crush) riski yaratır.
STATUS: SINIRDA — kullanılacaksa gerçek dara ile VGM hesabı zorunlu.
```

### 3.3 Paletsiz — floor loaded

```
HACİM KISITI
  76,4 m³ × 0,85 / 0,002386 = 27.216 şişe
  76,4 m³ × 0,92 / 0,002227 = 31.564 şişe
  → HACİM KISITLI KAPASİTE = 27.100 – 31.400 şişe

AĞIRLIK KISITI
  (a) Konteyner payload'ı 28.690 kg / 1,26 = 22.770 şişe
  (b) Türkiye karayolu tavanı 24.100 – 27.100 kg / 1,26 = 19.127 – 21.508 şişe
  → Bağlayıcı olan (b): 19.100 – 21.500 şişe

BAĞLAYICI KISIT = min(27.100 ; 19.100) = AĞIRLIK  ← ve ağırlık kısıtı içinde de
                  bağlayıcı olan KARAYOLU limiti, konteyner payload'ı değil.
PRATİK KAPASİTE = 19.100 – 21.500 şişe
```
`EV-2026-08-09-321`

**40HC paletsizde iç hacmin %30–39'u kullanılamaz** (ağırlık dolduğunda ~47–55 m³
dolmuş olur, 76,4 m³'ün altında).

---

## 4. 20DV vs 40HC — ŞİŞE BAŞINA NAVLUN MANTIĞI

```
2 × 20DV paletsiz : 23.600 – 27.400 şişe   (ağırlık: 2 × ~17,3 t, her biri ayrı araç)
1 × 40HC paletsiz : 19.100 – 21.500 şişe

→ İKİ ADET 20DV, BİR ADET 40HC'DEN %24–27 DAHA FAZLA ŞİŞE TAŞIR.
```
`EV-2026-08-09-322`

Bu, ağırlık limitinin **konteyner başına değil araç başına** uygulanmasından
kaynaklanır. Sonuç ekonomik olarak şu koşula bağlıdır:

```
40HC daha ucuzsa:  Navlun_40HC / Navlun_20DV  <  20.300 / 13.200 = 1,54
                   (+ konteyner başına sabit masraflar 40HC lehine çalışır:
                     THC, ardiye, gümrük müşavirliği ek konteyner ücreti
                     1.350 TL/konteyner (EV-...-342), iç nakliye)

Navlun_40HC / Navlun_20DV oranı = UNKNOWN  → RFQ zorunlu (T-304)
```

> **Bu oranı uydurmuyorum.** Piyasada tipik olarak 1,3–1,8 aralığında olduğu
> söylenir; bu aralığın **her iki ucu da farklı sonuç** verir. Karar ancak gerçek
> kotasyonla alınabilir.

---

## 5. PALETLİ vs PALETSİZ (FLOOR LOADED)

| Kriter | Paletli | Paletsiz (floor loaded / slip sheet) |
|---|---|---|
| 20DV kapasite | 6.480 – 7.200 şişe | **11.800 – 13.700 şişe (+%64…+%90)** |
| 40HC kapasite | 14.400 – 15.120 şişe | **19.100 – 21.500 şişe (+%27…+%42)** |
| Şişe başına navlun | yüksek | **düşük** |
| Yükleme/boşaltma işçiliği | forklift, hızlı (~1–2 saat) | **manuel, yavaş (elden istif/deistif)** |
| Boşaltma maliyeti | düşük | yüksek — terminal "iç boşaltım" 20ft **275 USD**, 40ft **350 USD** (`EV-...-341`) |
| Hasar/kırılma riski | düşük (streç + palet bütünlüğü) | **yüksek** — her şişe ekstra elleçlenir |
| İç istifin kayması | düşük | yüksek — dunnage/hava yastığı gerekir |
| Antrepoda depolama | doğrudan rafa | **antrepoda yeniden paletleme gerekir (ek maliyet)** |
| Bandrolleme operasyonu | palet açılıp koli koli işlenir | zaten koli koli — nötr |

**Ara sonuç (ESTIMATE):** Şişe/konteyner navlun tasarrufu paletsizde belirgindir,
ama boşaltma + yeniden paletleme + kırılma maliyeti bunun bir kısmını yer.
**Net fark nicelendirilemedi (UNKNOWN)** — çünkü kırılma oranı ve yeniden
paletleme birim maliyeti bilinmiyor. Bu, `T-304`'ün konusudur.

**Türkiye'ye özgü not:** Alkollü içki bandrol nedeniyle zaten antrepoda
elleçlenecekse (`EV-2026-08-09-380`), paletsiz gelen yükün antrepoda paletlenmesi
bandrolleme ile aynı operasyonda birleştirilebilir → paletsizin dezavantajı azalır.
Bu bir **hipotezdir**, doğrulanmadı.

---

## 6. LCL / FCL KIRILMA NOKTASI

### 6.1 Şarap w/m'de hangi taraftan ölçülür?

```
1 CBM paketli şarap = 1 / 0,002227 = 449 şişe
449 şişe × 1,26 kg   = 566 kg
→ yoğunluk ≈ 0,57 ton/m³  <  1 ton/m³
→ LCL "w/m" (weight or measurement) hesabında **CBM (hacim) BAĞLAYICIDIR.**
   Şarap LCL'de hacimden ücretlenir, ağırlıktan değil.
```

### 6.2 Kırılma noktası hesabı

```
FCL_20DV_all_in  =  LCL_sabit + LCL_per_cbm × V

LCL maliyet yapısı (EV-2026-08-09-324, T5, LOW confidence):
  okyanus 40–180 USD/CBM ; CFS mense+varis 30–80 USD/CBM ;
  varış sabit masrafları 200–500 USD ; doküman 50–100 USD
  → LCL_per_cbm ≈ 80 – 260 USD/CBM ; LCL_sabit ≈ 250 – 600 USD

FCL 20DV all-in (Akdeniz → Türkiye) = UNKNOWN, ESTIMATE bandı 1.200 – 2.500 USD

Senaryolar:
  FCL 1.800 ; LCL 150/cbm + 400  → V = (1800−400)/150 = 9,3 cbm ≈  4.190 şişe
  FCL 2.500 ; LCL 100/cbm + 300  → V = 22,0 cbm            ≈  9.880 şişe
  FCL 1.200 ; LCL 200/cbm + 500  → V = 3,5 cbm             ≈  1.570 şişe

ÇAPRAZ KONTROL: JSV Logistic (T4) "15 m³ veya 10.000 kg üstü FCL'i haklı kılar"
  15 m³ ≈ 6.735 şişe  (EV-2026-08-09-325)
```

**SONUÇ (`EV-2026-08-09-323`, status: ESTIMATE, confidence: LOW):**

| | |
|---|---|
| Kırılma noktası — merkezî tahmin | **~5.000 – 7.000 şişe / sevkiyat** |
| Kırılma noktası — tam belirsizlik bandı | 1.600 – 9.900 şişe |
| Bandın genişliğinin sebebi | FCL navlunu **UNKNOWN** |

### 6.3 Charter hacim senaryolarına uygulama

| Yıllık hacim | Sevkiyat başına adet (varsayım: 2 sevkiyat/yıl) | Mod | Konteyner ihtiyacı |
|---|---|---|---|
| 5.000 şişe | 2.500 | **LCL** (~5,6 m³) — veya yılda tek 20DV kısmi | 0,4 × 20DV |
| 10.000 şişe | 5.000 | **SINIRDA** — tek sevkiyatta 10.000 ise FCL 20DV | ~0,8 × 20DV |
| 25.000 şişe | 12.500 | **FCL 20DV** | ~2 × 20DV/yıl |
| 50.000 şişe | 25.000 | **FCL** — 20DV mi 40HC mi §4'e bağlı | ~4 × 20DV veya ~2,5 × 40HC |
| 100.000 şişe | 50.000 | **FCL 40HC** değerlendirilmeli | ~8 × 20DV veya ~5 × 40HC |

> **5.000 şişe/yıl senaryosu lojistik açıdan verimsizdir**: LCL birim maliyeti
> yüksek, cam için elleçleme riski fazla, ama FCL'de konteyner yarım kalır.
> Bu bulgu `finans-fizibilite`'nin ölçek eğrisini doğrudan etkiler.

### 6.4 LCL'in gizli maliyetleri (kalem listesi)

| Kalem | Kim keser | Not |
|---|---|---|
| Minimum 1 CBM ücreti | forwarder | 0,5 m³ göndersen de 1 m³ ödersin |
| CFS mense konsolidasyon | mense CFS | 35–75 USD veya 15–40 USD/cbm |
| CFS varış dekonsolidasyon | varış CFS | 45–95 USD veya 15–40 USD/cbm |
| Varış liman/terminal sabit masrafları | terminal/acente | 200–500 USD/sevkiyat — **hacimden bağımsız** |
| Doküman/BL | forwarder | 50–100 USD |
| **Ekstra elleçleme kaynaklı kırılma** | kimse — sen yersin | cam için LCL'in en büyük gizli maliyeti; oran **UNKNOWN** |
| Konsolidasyon beklemesi | — | transit süresine +3–10 gün ekler (**UNKNOWN**, tahmin) |

---

## 7. HESABIN EN KIRILGAN NOKTALARI

| # | Varsayım | Etki | Nasıl kırılır |
|---|---|---|---|
| 1 | `PACKED_VOLUME_PER_BOTTLE` = 0,00223–0,00239 m³ | **TÜM kapasiteler** | Burgundy formu şişe → 0,0036 m³ → kapasiteler **%38 düşer** |
| 2 | Çekici+şasi darası 13–16 t | 40HC ağırlık tavanı | Gerçek dara 17 t ise 40HC tavanı 23,1 t → 5 katman imkânsız |
| 3 | Kup verimi %85–92 (floor load) | paletsiz kapasite | %80'e düşerse 20DV 11.100 şişe |
| 4 | Palet adedi 9–11 / 20–24 (C-301) | paletli kapasite | Çelişki çözülmeden ±%11 belirsizlik |
| 5 | 4 katman istif (crush limiti) | paletli kapasite | Tedarikçi 5 katman garanti ederse 40HC'de +%25 |
| 6 | Cam ağırlığı 400–550 g | ağırlık kısıtı | Ağır cam (700 g) → 40HC paletsiz 17.500 şişeye düşer |

---

## 8. MODELE GİRECEK DEĞERLER

| Alan | Değer | status | evidence_id |
|---|---|---|---|
| `packed_weight_per_bottle_kg` | 1,26 (band 1,21–1,38) | ESTIMATE | `EV-2026-08-09-305`, `EV-2026-08-09-307` |
| `packed_volume_per_bottle_m3` | 0,00223 – 0,00239 | ESTIMATE | `EV-2026-08-09-307` |
| `20dv_bottles_volume_limited` | 11.800 – 13.700 (floor) / 6.480 – 7.200 (paletli) | ESTIMATE | `EV-2026-08-09-320` |
| `20dv_bottles_weight_limited` | 20.400 – 22.400 | ESTIMATE | `EV-2026-08-09-320` |
| `20dv_binding_constraint` | **HACİM** | ESTIMATE | `EV-2026-08-09-320` |
| `40hc_bottles_volume_limited` | 27.100 – 31.400 (floor) / 14.400 – 15.120 (paletli) | ESTIMATE | `EV-2026-08-09-321` |
| `40hc_bottles_weight_limited` | 19.100 – 21.500 | ESTIMATE | `EV-2026-08-09-321` |
| `40hc_binding_constraint` | **AĞIRLIK (Türkiye karayolu 44 t)** | ESTIMATE | `EV-2026-08-09-321` |
| `lcl_fcl_breakeven_bottles` | 5.000 – 7.000 (band 1.600 – 9.900) | ESTIMATE | `EV-2026-08-09-323` |
