# ROTA × KALEM × KONTEYNER TİPİ MALİYET MATRİSİ

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2 — COMMERCIAL VALIDATION
tarih:  2026-08-10
durum:  DRAFT
kanit:  EV-2026-08-10-301 … EV-2026-08-10-332 (32 kart)
```

> ## ⛔ BU DOSYAYI OKUMADAN ÖNCE — 7 KURAL
>
> 1. **Tek bir "navlun" rakamı yoktur.** Her kalem ayrı fiyatlanmıştır. Bir
>    kalemi diğerinin yerine koymak yasaktır.
> 2. **Her fiyatın `excluded_charges` alanı doludur.** Boş bırakılmamıştır —
>    çünkü gizli maliyet hatası en çok orada doğar.
> 3. **LCL rakamları gerçek, tarihli, geçerlilik süreli kotasyonlardır**
>    (Flexport, erişim 2026-08-10, geçerlilik **2026-08-16**). `ttl: 6d`.
> 4. **FCL rakamları hâlâ `ESTIMATE`'tir ve confidence `LOW`'dur.** Test edilen
>    14 Türkiye varışlı lane'in **hiçbirinde** kamuya açık FCL kotasyonu yoktur
>    (`EV-2026-08-10-312`). `T-304`'ün FCL ayağı **kapanmamıştır**.
> 5. **2024/2025 verisi 2026 FACT'i değildir.** DFDS tarifesi (2025-01-01) ve
>    FreightAmigo bandı (2025) tarihleriyle işaretlenmiş ve statüsü
>    düşürülmüştür.
> 6. **Toplam maliyet üç para birimindedir (USD + EUR + TRY) ve tek sayıya
>    indirgenmemiştir**, çünkü `80-model/inputs/makro.yaml → fx` hâlâ `null`.
>    Toplama işlemi `finans-fizibilite`'nindir (`T-311`).
> 7. **Yön uyarısı:** Bazı kanıtlar Türkiye→Avrupa (ihracat) yönündedir.
>    Headhaul/backhaul asimetrisi nedeniyle ters çevrilerek kullanılamazlar;
>    yalnızca **mertebe** ve **oran** çapası olarak kullanılmışlardır.

---

## 1. YÖNETİCİ ÖZETİ — TUR 2'DE NE DEĞİŞTİ

| # | TUR 1 durumu | TUR 2 durumu | Kanıt |
|---|---|---|---|
| 1 | **Hiçbir rota için navlun yok** | **9 rotanın LCL navlunu gerçek, tarihli kotasyonla biliniyor**; İtalya hâlâ UNKNOWN | `EV-...-301…311` |
| 2 | California → İstanbul **CRITICAL UNKNOWN** | **Kapandı (LCL düzeyinde):** Oakland 1.239–1.289 USD/5 CBM, **20 gün**, Atlanta→Kumport rotası | `EV-...-308`, `-309` |
| 3 | Origin charges **tamamen UNKNOWN** | **T3 taşıyıcı tarifesiyle biliniyor:** İspanya THO **287 EUR**, B/L **62 EUR** | `EV-...-313`, `-314` |
| 4 | Destination THC = tek sayı (113 USD) | **Limana göre 165–298 USD** ve **İzmir/İstanbul'da 20ft/40ft ayrımı YOK** | `EV-...-315` |
| 5 | Ardiye free time **UNKNOWN** | **SafiPort: 0 gün** (gemi yanaşmasından itibaren) — ama başka kaynak "6. günden" diyor → `C-312` | `EV-...-317`, `-325` |
| 6 | Ordino **UNKNOWN** | **2.000–5.000 TL** | `EV-...-325` |
| 7 | Antrepo minimum süre **UNKNOWN** | **minimum 7 gün** | `EV-...-327` |
| 8 | 40HC/20DV navlun oranı **UNKNOWN**, eşik 1,54 | **Ampirik oran 1,37–1,48**; eşik bandı 1,39–1,82 → **40HC şişe başına avantajlı** | `EV-...-328` |
| 9 | LCL/FCL kırılma 5.000–7.000 (geniş 1.600–9.900) | **~5.900 şişe (band 2.200–9.800)** — rotaya özgü gerçek kotasyonla | `EV-...-330` |
| 10 | İç nakliye bandı 3.000–30.000 TL | **Şehir içi 10.000–15.000 TL**'ye daraldı | `EV-...-326` |

**Tek cümlelik en önemli bulgu:**
Akdeniz→Türkiye rotasında **base okyanus navlunu maliyetin küçük parçasıdır.**
İspanya çıkış local charge'ları (**349–554 EUR/konteyner**) tek başına, aynı
lane'in marketplace base okyanus navlununu (**~300–700 USD**) aşabilmektedir.
Yani "navlun pazarlığı" yanlış yerde yapılan bir pazarlıktır; **kalem
kompozisyonu navlunun kendisinden daha belirleyicidir.**

---

## 2. ROTA BAZLI NAVLUN TABLOSU (ANA TABLO)

### 2.1 LCL — gerçek kotasyon, 5 CBM / 750 kg bazlı

Tüm satırlar: `date: 2026-08-10 · validity: 2026-08-16 · container_type: LCL
(5 CBM / 750 kg) · currency: USD · source: Flexport Rate Explorer (T4) ·
included_charges: base ocean freight (port-to-port) ·
excluded_charges: origin local charges, destination local charges, CFS
destination, ordino, gümrükleme, iç nakliye, sigorta, antrepo, tüm vergiler ·
confidence: MEDIUM`

| # | Rota (origin → İstanbul) | Fiyat (USD) | USD/CBM | **USD/şişe** | Transit (gün) | Routing | evidence_id |
|---|---|---|---|---|---|---|---|
| **R1** | **Valencia (ES)** | **616 – 666** | 123,2 – 133,2 | **0,274 – 0,297** | 4 | direkt | `EV-...-301` |
| **R1b** | **Barcelona (ES)** — teklif A | 616 – 666 | 123,2 – 133,2 | 0,274 – 0,297 | 4 | direkt | `EV-...-302` |
| **R1c** | Barcelona (ES) — teklif B | 809 – 859 | 161,8 – 171,8 | 0,360 – 0,383 | 4 | direkt | `EV-...-302` |
| **R2** | **Lizbon (PT)** | 949 – 999 | 189,8 – 199,8 | **0,423 – 0,445** | ~4 ⚠ | via Barcelona | `EV-...-303` |
| **R3** | **İtalya** (Genova/La Spezia/Livorno/Napoli) | **UNKNOWN** | — | **UNKNOWN** | UNKNOWN | — | `EV-...-304` |
| **R4** | **San Antonio (CL)** — A | 970 – 1.020 | 194,0 – 204,0 | **0,432 – 0,454** | **43** | via Barcelona | `EV-...-306` |
| R4b | San Antonio (CL) — B | 1.337 – 1.387 | 267,4 – 277,4 | 0,595 – 0,618 | 49 | via Hamburg | `EV-...-306` |
| **R5** | **Cape Town (ZA)** | 1.720 – 1.770 | 344,0 – 354,0 | **0,766 – 0,788** | **49** | via Hamburg | `EV-...-307` |
| **R6** | **Marsilya (FR)** — A | 1.428 – 1.478 | 285,6 – 295,6 | **0,636 – 0,658** | 15 | via **Hamburg** | `EV-...-305` |
| R6b | Marsilya (FR) — B | 1.465 – 1.515 | 293,0 – 303,0 | 0,653 – 0,675 | 12 | via **Antwerp** | `EV-...-305` |
| **R7** | **Buenos Aires (AR)** | 1.150 – 1.200 | 230,0 – 240,0 | **0,512 – 0,535** | 25 | via Hamburg | `EV-...-310` |
| **R8** | **Oakland (US-CA)** | 1.239 – 1.289 | 247,8 – 257,8 | **0,552 – 0,574** | **20** | via Atlanta→Kumport | `EV-...-308` |
| R8b | **Los Angeles (US-CA)** — A | 1.133 – 1.183 | 226,6 – 236,6 | 0,505 – 0,527 | 20 | via Atlanta→Kumport | `EV-...-309` |
| R8c | Los Angeles (US-CA) — B | 1.270 – 1.320 | 254,0 – 264,0 | 0,566 – 0,588 | 44 | via Savannah | `EV-...-309` |
| **R9** | **Melbourne (AU)** — A | 1.187 – 1.237 | 237,4 – 247,4 | **0,529 – 0,551** | 36 | via Singapur | `EV-...-311` |
| R9b | Melbourne (AU) — B | 2.495 – 2.545 | 499,0 – 509,0 | 1,111 – 1,133 | 56 | via Singapur | `EV-...-311` |

> **USD/şişe türetmesi:** `USD/CBM ÷ 449 şişe/m³` (`EV-2026-08-09-323`).
> **⚠ R2 uyarısı:** Flexport, Barcelona aktarmalı Lizbon rotası için de "4 gün"
> yazıyor. Bu **iç tutarsızdır**; fiyat MEDIUM, transit süresi LOW confidence.

#### 2.1.1 LCL navlununa göre rota sıralaması (yalnızca base ocean freight)

```
1. İspanya (Valencia/Barcelona)   0,274 – 0,297 USD/şişe   transit  4 gün
2. Barcelona (2. teklif)          0,360 – 0,383            transit  4 gün
3. Portekiz (Lizbon)              0,423 – 0,445            transit ~4 gün ⚠
4. Şili (San Antonio)             0,432 – 0,454            transit 43 gün ⚠⚠
5. Los Angeles                    0,505 – 0,527            transit 20 gün
6. Arjantin                       0,512 – 0,535            transit 25 gün
7. Avustralya                     0,529 – 0,551            transit 36 gün
8. Oakland (California)           0,552 – 0,574            transit 20 gün
9. Fransa (Marsilya)              0,636 – 0,658            transit 15 gün ⚠
10. Güney Afrika                  0,766 – 0,788            transit 49 gün
--  İtalya                        UNKNOWN
```

**İki karşı-sezgisel bulgu:**

- **Şili, Portekiz ile aynı navlun bandındadır** (0,43–0,45 USD/şişe). Şarapta
  "uzak menşe = pahalı navlun" sezgisi bu rotada **yanlıştır**. Fark navlunda
  değil, **transitte**: 43 gün vs ~4 gün.
- **Fransa (Marsilya), Şili'den PAHALIDIR.** Sebebi coğrafya değil **routing**:
  Marsilya çıkışlı LCL yükü Hamburg/Antwerp'e (Kuzey Avrupa) gidip oradan
  Türkiye'ye dönüyor. Bir Akdeniz limanı olması hiçbir işe yaramıyor.
  **Fransa lojistik olarak bir Akdeniz menşei gibi davranmıyor.**

### 2.2 FCL — hâlâ `ESTIMATE`, confidence `LOW`

**Kamuya açık, bizim rotalarımıza ait, tarihli FCL kotasyonu BULUNAMADI.**
Aşağıdakiler dolaylı çapalardır; **hiçbiri `FACT` değildir.**

| Kaynak | Değer | Yön | date / validity | included | **excluded** | tier | conf. | evidence_id |
|---|---|---|---|---|---|---|---|---|
| Freightify marketplace "from" | Rotterdam→İzmir **295 USD**; London Gateway→Mersin **350**; Aarhus→İstanbul **650**; İstanbul→Barcelona **500** | karışık | tarih **YOK** | base ocean (varsayım) | **tüm origin + destination local charge'lar; konteyner boyu belirtilmemiş** | T4 | **LOW** | `EV-...-322` |
| DFDS yayınlanmış tarife | Mersin–Trieste 20' **1.030 EUR** / 40HC **1.520 EUR**; Pendik–Trieste 785 / 1.115 | TR→IT (**ihracat**) | eff. **2025-01-01** | base navlun | **BAF, ETS ("aylık güncellenir"), liman elleçleme** | T4 | MEDIUM (2025 için) | `EV-...-320` |
| CANXANSA gösterge | Mersin→Barcelona 40' **1.400–2.000 USD** (8–10 gün) | TR→ES (**ihracat**) | tarih **YOK** | port-to-port | **belirtilmemiş → tek başına modele giremez** | T4 | LOW | `EV-...-323` |
| FreightAmigo rehberi | İspanya→Türkiye 20ft **1.200–2.500 EUR** (ort. 1.800) | ES→TR ✔ | **2025** | base rate | **yakıt surprimi %15–25 hariç; local charge'lar belirsiz** | **T5** | **LOW** | `EV-...-324` |
| BR Logistics (TUR 1) | İspanya→Türkiye 20ft 1.200–2.500 EUR | ES→TR ✔ | tarih yok | **belirsiz** | **belirsiz** | T5 | LOW | `EV-2026-08-09-333` |

> **`C-311` — ÇÖZÜLMEMİŞ ÇELİŞKİ.** Marketplace "from" fiyatları (295–650 USD)
> ile blog bantları (1.200–2.500 EUR) arasında **4–5 kat** fark vardır. İki
> açıklama da mümkündür ve **hiçbiri doğrulanmamıştır**:
> (a) düşük rakamlar yalnızca base ocean, yüksek rakamlar quasi-all-in;
> (b) blog rakamları eski/geri dönüştürülmüş veri.
> **Sessizce taraf seçmedim.** Modelde band olarak taşınır.

**Modelde kullanılacak FCL ESTIMATE bandı (İspanya → Türkiye):**

| Konteyner | Base ocean freight | status | confidence | ttl |
|---|---|---|---|---|
| 20DV | **300 – 1.200 USD** | ESTIMATE | **LOW** | 14d |
| 40HC | **411 – 1.776 USD** (= 20DV × 1,37–1,48) | ESTIMATE | **LOW** | 14d |
| BAF / CAF / ETS / PSS | **+%15 – 25** (base üzerine) | ESTIMATE | LOW | 14d |

**Diğer rotalar için FCL: `UNKNOWN`.** Şili, G.Afrika, California, Arjantin,
Avustralya, İtalya, Portekiz, Fransa → FCL navlunu **hiçbir kaynakta yok**.

---

## 3. KALEM KALEM FİYATLAMA (ROTA × KALEM)

### 3.1 ORIGIN CHARGES — İspanya (en iyi kanıtlanmış menşe)

`source: Hapag-Lloyd SPAIN Local Charges (T3, resmî taşıyıcı tarifesi) ·
currency: EUR · confidence: HIGH`

| Kalem | Kod | 20DV | 40HC | effective_date | Zorunlu mu | evidence_id |
|---|---|---|---|---|---|---|
| **Origin THC** | THO | **287** | **287** | 2026-04-01 | **evet** | `EV-...-313` |
| — Algeciras çıkışlı | THO | 277 | 277 | 2026-04-01 | — | `EV-...-313` |
| — reefer | THO | 355 | 355 | 2026-04-01 | reefer ise | `EV-...-313` |
| **Documentation / B/L (EDI)** | MTD | **62** | **62** | 2026-01-01 | **evet** | `EV-...-314` |
| Documentation / B/L (manuel SI) | MSI | 104 | 104 | 2025-10-01 | manuel ise | `EV-...-314` |
| VGM (manuel bildirim) | VGM | 50 | 50 | — | manuel ise | `EV-...-314` |
| İhracat gümrükleme (taşıyıcı yaparsa) | CDO | 60 | 60 | 2023-04-01 | opsiyon | `EV-...-314` |
| Equipment assignment | RHO | 40 | 40 | 2023-04-01 | opsiyon | `EV-...-314` |
| **Food Quality Container** ⚠ | FQS | 115 | 115 | 2022-04-01 | **şarapta muhtemel** | `EV-...-314` |
| Lift-on charge | LFO | 70 | 70 | — | opsiyon | `EV-...-314` |
| Terminal Security Fee | TSO | *(THO'ya dahil)* | *(dahil)* | 2025-07-01 | — | `EV-...-313` |
| Logistic Fee & Seal | SEC | *(THO'ya dahil)* | *(dahil)* | 2018-01-01 | — | `EV-...-313` |
| **ORIGIN TOPLAM — minimum** | | **349 EUR** | **349 EUR** | | | |
| **ORIGIN TOPLAM — üst uç** | | **554 EUR** | **554 EUR** | | | |

> **YAPISAL BULGU:** Origin charge'ların **hiçbiri konteyner boyuna bağlı
> değildir.** 40HC, 20DV ile aynı 349–554 EUR'yu öder ama %40–60 daha fazla
> şişe taşır. Bu tek başına 40HC lehine güçlü bir argümandır.

**Diğer menşelerin origin charge'ları: `UNKNOWN`.**
Portekiz, İtalya, Fransa, Şili, G.Afrika, ABD, Arjantin, Avustralya için
taşıyıcı local tarifesi bu turda taranmamıştır → `T-312`.

### 3.2 DESTINATION CHARGES — Türkiye

#### A) Taşıyıcının kestiği (Hapag-Lloyd, T3, `EV-...-315`, `-316`)

| Kalem | Ambarlı/İstanbul | İzmir/Aliağa | Mersin | Gemlik | effective |
|---|---|---|---|---|---|
| **THD — kuru, 20DV** | **192** | **165** | **261** | 185 | 2026-01-01 / 2024-10-01 / 2026-02-12 |
| **THD — kuru, 40HC** | **192** | **165** | **298** | 185 | aynı |
| THD — reefer, 40' | — | — | 333 | — | 2026-02-12 |
| Drop-off fee | 50 | 50 | 50 | 50 | 2021-04-01 |
| Unstuffing (müşteri tesisinde) | — | — | 172 (+%20 KDV) | — | 2024-10-01 |
| Veteriner / fitosaniter kontrol | 126 / B/L | 126 / B/L | 126 / B/L | 126 / B/L | 2026-04-01 |
| Manifest amendment | 200 / B/L | 200 | 200 | 200 | — |
| **Fuel surcharge destination (kamyon)** ⚠ | **+%39** transfer ücreti üzerine | +%39 | +%39 | +%39 | 2023-10-26 |

> **İKİ KRİTİK NOKTA:**
> 1. **İstanbul, İzmir ve Gemlik'te THD 20ft/40ft ayrımı yoktur** — düz ücret.
>    Mersin ve İskenderun'da vardır. → 40HC bu üç limanda ekstra avantajlı.
> 2. **Taşıyıcının iç nakliyesi kullanılırsa navlunun üzerine %39 yakıt
>    surprimi biner.** Bağımsız nakliyeci ile karşılaştırılmadan seçilmemelidir.

#### B) Terminalin kendi kestiği (`EV-...-317`, `-318`, `-319`)

| Kalem | SafiPort (2026) | Beldeport | Kumport (Ambarlı) ⚠LOW |
|---|---|---|---|
| THC / kapı çıkış | 116 (+10 enerji) | 113 | UNKNOWN |
| **Ardiye 20' dolu** | 39 / 44 / 53 (1-5 / 6-10 / 11+ g) | 37 / 43 / 52 | **18** (1-5 g) |
| **Ardiye 40' dolu** | 60 / 65 / 77 | 58 / 66 / 75 | **29** (1-5 g), 46 (16+ g) |
| Ardiye reefer 20' | **109 / 120** | 135–165 | UNKNOWN |
| **Ardiye free time** | **0 gün** ("gemi yanaşmasından itibaren") | UNKNOWN | UNKNOWN |
| İç boşaltım (devanning) 20' | 275 (manuel 405) | 257 | UNKNOWN |
| İç boşaltım (devanning) 40' | 365 (manuel 475) | 332 | UNKNOWN |
| Tam muayene | 2.321–3.248 TL | 2.322 TL | UNKNOWN |
| X-ray | 1.972 TL | — | UNKNOWN |
| Numune alma | 1.972 TL | — | UNKNOWN |

> **`C-313`:** Taşıyıcının THD'si (165–298 USD) ile terminalin kapı-çıkış
> ücreti (113–116 USD) **aynı fiziksel olayı** fiyatlıyor gibi görünüyor.
> İkisi de faturaya giriyorsa toplam 278–414 USD; biri diğerini kapsıyorsa
> yalnızca THD. **Çözülmedi. Model her iki senaryoyu da taşımalıdır.**
> Muhafazakâr varsayım: yalnızca taşıyıcı THD'si (çift sayım riski yok).
>
> **`C-312`:** Ardiye free time. SafiPort tarifesi 1. günden ücretlendiriyor;
> bir gümrük müşavirliği kaynağı "6. günden itibaren 40–60 USD" diyor. **0 gün
> mü 5 gün mü?** Çözülmedi → gecikme senaryosunda muhafazakâr olarak **0 gün**
> kullanıldı (TUR 1 ile aynı).

#### C) Türk yerel kalemleri (`EV-...-325`, `EV-2026-08-09-342`)

| Kalem | Değer | Birim | status | tier |
|---|---|---|---|---|
| **Ordino (yük teslim talimatı)** | **2.000 – 5.000** | TRY | ESTIMATE | T4 |
| Gümrük müşavirliği — İTH-2 (deniz ithalat) | 4.670 | TRY | FACT | T3 |
| Gümrük müşavirliği — ANT-1 (antrepo beyannamesi) | 1.350 | TRY | FACT | T3 |
| Gümrük müşavirliği — ek konteyner (İTH-14) | 1.350 | TRY | FACT | T3 |
| Laboratuvar / ekspertiz (ÖZ-4) | 940 / işlem | TRY | FACT | T3 |
| X-ray geçiş | 2.000 – 3.000 | TRY | ESTIMATE | T4 |
| Mesai dışı | 510 | TRY | ESTIMATE | T4 |

### 3.3 CONTAINER HAULAGE / İÇ NAKLİYE (`EV-...-326`)

| Güzergâh | 20' | 40' | date | KDV |
|---|---|---|---|---|
| İstanbul içi (liman → depo) | **10.000+** | **12.500+** | 2026 | hariç |
| Ambarlı → Bursa | 23.000 | 23.000 | 2025-01-15 | hariç |
| Ambarlı → Ankara | 30.000 | 30.000 | 2025-01-15 | hariç |
| Ambarlı → İzmir | 37.500 | 37.500 | 2025-01-15 | hariç |
| Bekleme | 6 saat ücretsiz, sonrası 1.500 TL+KDV/saat | | 2025 | — |

> **`EV-...-332` — VARIŞ LİMANI KURALI:**
> THD farkı (İzmir 165 ↔ Mersin 40' 298) = **max 133 USD/konteyner** =
> 0,006–0,011 USD/şişe.
> İç nakliye farkı (Ambarlı→İzmir 37.500 TL) = **2,7–3,2 TRY/şişe**.
> **Büyüklük mertebesi farkı ~2 kat.** Sonuç: **varış limanı, terminal
> tarifesine göre değil, antrepo/bandrolleme tesisinin ve hedef pazarın
> bulunduğu yere göre seçilir.**

### 3.4 ANTREPO, UNLOADING, PALLET HANDLING, STORAGE

| Kalem | Değer | status | evidence_id |
|---|---|---|---|
| Antrepo paletli depolama | **0,35 EUR/palet/gün** | ESTIMATE (T5, LOW) | `EV-...-327` |
| **Antrepo minimum süre** | **7 gün** | ESTIMATE (T5, LOW) | `EV-...-327` |
| Antrepo giriş/çıkış elleçleme (hammaliye) | **UNKNOWN** | UNKNOWN | — |
| Unloading — terminalde (devanning) | 257–275 USD (20'), 332–365 (40') | FACT | `EV-...-317`, `-319` |
| Unloading — müşteri tesisinde (taşıyıcı) | 172 USD + %20 KDV | FACT | `EV-...-316` |
| **Pallet handling / yeniden paletleme** | **UNKNOWN** | UNKNOWN | — |
| Depolama (serbest dolaşım sonrası, m²/palet) | **UNKNOWN** | UNKNOWN | — |
| **Bandrolleme operasyon birim maliyeti** | **UNKNOWN** | UNKNOWN | → `T-314` |
| **Bandrolleme kapasitesi (şişe/gün)** | **UNKNOWN** | UNKNOWN | → `T-314` |

### 3.5 SİGORTA

TUR 1'den **değişmedi**; bu turda yeni kotasyon alınamadı.

| Parametre | Değer | status | evidence_id |
|---|---|---|---|
| Prim oranı (tipik) | %0,3 – 0,6 | ESTIMATE | `EV-2026-08-09-360` |
| Teminat esası | CIF + %10 | ESTIMATE | `EV-2026-08-09-360` |
| Gerekli teminat | ICC (A) + kırılma + termal şok | ESTIMATE | `EV-2026-08-09-361` |
| Taşıyıcı sınırlı sorumluluğu | 3 USD/kg (~3,8 USD/şişe) | FACT | `EV-2026-08-09-361` |
| **Gerçek Türk kotasyonu** | **UNKNOWN** | UNKNOWN | → `T-304` |

> **TUR 2 ekleme — sigortanın rota bağımlılığı:** Prim oranı değil, **beklenen
> hasar** rotaya bağlıdır. Aktarma sayısı = elleçleme sayısı = cam kırılma
> riski. Bu turda ölçülen aktarma yapıları:
> `İspanya→İstanbul: 0 aktarma (direkt, 4 gün)` ·
> `Şili→İstanbul: 1 aktarma (Barcelona, 43 gün)` ·
> `Cape Town / Arjantin / Fransa→İstanbul: 1 aktarma (Hamburg/Antwerp)` ·
> `California→İstanbul: kara + deniz aktarması (Atlanta), 20 gün`.
> **Kırılma oranı hâlâ UNKNOWN** → prim/rota etkileşimi fiyatlanamıyor.

---

## 4. ŞİŞE BAŞINA TOPLAM LOJİSTİK MALİYETİ (İSPANYA → TÜRKİYE)

> **Kapsam:** L1 (FOB) → L3 (pre-tax landed) arası lojistik kalemleri.
> **Dahil değildir:** sigorta (CIF değerine bağlı), bandrolleme operasyonu,
> antrepo bekleme (süre UNKNOWN → `T-301`), kanala dağıtım, tüm vergiler.

### 4.1 Konteyner başına kalem dökümü

| Kalem | 20DV paletsiz | 20DV paletli | 40HC paletsiz | LCL (5.000 şişe) |
|---|---|---|---|---|
| Şişe kapasitesi | 11.800 – 13.700 | 6.480 – 7.200 | 19.100 – 21.500 | 5.000 (11,2–12,0 m³) |
| **USD kalemleri** | | | | |
| Ocean freight (base) | 300 – 1.200 | 300 – 1.200 | 411 – 1.776 | 1.380 – 1.598 |
| BAF / CAF / ETS (%15–25) | 45 – 300 | 45 – 300 | 62 – 444 | *(base'e dahil varsayıldı)* |
| Destination THD | 165 – 261 | 165 – 261 | 165 – 298 | — *(CBM fiyatında)* |
| Drop-off | 50 | 50 | 50 | — |
| Terminal ardiye (5 gün) | 90 – 195 | 90 – 195 | 145 – 300 | — |
| Devanning / unloading | 257 – 275 | — | 332 – 365 | — |
| CFS destination + sabit + doc | — | — | — | 250 – 1.560 |
| **USD ARA TOPLAM** | **907 – 2.281** | **650 – 2.006** | **1.165 – 3.233** | **1.630 – 3.158** |
| **EUR kalemleri** | | | | |
| Origin THC + doc + opsiyonlar | 349 – 554 | 349 – 554 | 349 – 554 | 0 *(CBM'e dahil)* |
| **EUR ARA TOPLAM** | **349 – 554** | **349 – 554** | **349 – 554** | **0** |
| **TRY kalemleri** | | | | |
| Ordino | 2.000 – 5.000 | 2.000 – 5.000 | 2.000 – 5.000 | 2.000 – 5.000 |
| Gümrük müşavirliği (ANT-1 + İTH-2) | 6.020 | 6.020 | 6.020 | 6.020 |
| İç nakliye (İstanbul içi) | 10.000 – 15.000 | 10.000 – 15.000 | 12.500 – 18.000 | 5.000 – 10.000 |
| X-ray (uygulanırsa) | 0 – 3.000 | 0 – 3.000 | 0 – 3.000 | 0 – 3.000 |
| **TRY ARA TOPLAM** | **18.020 – 29.020** | **18.020 – 29.020** | **20.520 – 32.020** | **13.020 – 24.020** |

### 4.2 Şişe başına (üç para birimi ayrı — `EV-...-329`)

| Senaryo | USD/şişe | EUR/şişe | TRY/şişe |
|---|---|---|---|
| **20DV paletsiz** (11.800–13.700) | **0,066 – 0,193** | **0,025 – 0,047** | **1,32 – 2,46** |
| **20DV paletli** (6.480–7.200) | **0,090 – 0,310** | **0,048 – 0,086** | **2,50 – 4,48** |
| **40HC paletsiz** (19.100–21.500) | **0,054 – 0,169** | **0,016 – 0,029** | **0,95 – 1,68** |
| **LCL, 5.000 şişe** | **0,326 – 0,632** | **0** | **2,60 – 4,20** |
| 20DV'de yalnızca 5.000 şişe taşınırsa | 0,181 – 0,456 | 0,070 – 0,111 | 3,60 – 5,80 |

> ⛔ **BU ÜÇ SÜTUN TOPLANMAMIŞTIR VE TOPLANAMAZ.**
> `80-model/inputs/makro.yaml → fx.usd_try` ve `fx.eur_try` **`null`**'dır.
> Kur tarihi belirtilmeden yapılan dönüşüm `makro.yaml`'ın kendi kuralına göre
> geçersizdir. Toplama işlemi `finans-fizibilite`'nindir → **`T-311`**.

**Üç sütunun anlattığı üç ayrı hikâye:**

1. **USD bacağı okyanus navlunudur** → belirsizliğin kaynağı burasıdır (`T-304`).
2. **EUR bacağı menşe local charge'larıdır** → sabit, iyi bilinen, konteyner
   boyundan bağımsız. **40HC ile 3 kat seyrelir.**
3. **TRY bacağı Türkiye içi operasyondur** → en büyük tek kalem **iç nakliye**;
   kur riski taşımaz ama enflasyon riski taşır.

### 4.3 Diğer rotalar için şişe başı toplam

**Yalnızca LCL bacağı hesaplanabilmektedir** (FCL navlunu UNKNOWN). Aşağıdaki
tabloda **yalnızca base ocean freight** vardır; origin/destination charge'lar
İspanya dışındaki menşeler için `UNKNOWN`'dır.

| Rota | LCL base ocean USD/şişe | + origin charges | + destination charges | Toplam |
|---|---|---|---|---|
| İspanya | 0,274 – 0,297 | **biliniyor** (349–554 EUR/ktr) | biliniyor | **hesaplanabilir** |
| Portekiz | 0,423 – 0,445 | UNKNOWN | biliniyor | **UNKNOWN** |
| İtalya | **UNKNOWN** | UNKNOWN | biliniyor | **UNKNOWN** |
| Şili | 0,432 – 0,454 | UNKNOWN | biliniyor | **UNKNOWN** |
| G. Afrika | 0,766 – 0,788 | UNKNOWN | biliniyor | **UNKNOWN** |
| Fransa | 0,636 – 0,675 | UNKNOWN | biliniyor | **UNKNOWN** |
| California | 0,505 – 0,574 | UNKNOWN | biliniyor | **UNKNOWN** |
| Arjantin | 0,512 – 0,535 | UNKNOWN | biliniyor | **UNKNOWN** |
| Avustralya | 0,529 – 1,133 | UNKNOWN | biliniyor | **UNKNOWN** |

---

## 5. KONTEYNER TİPİ KARARI — TUR 1'İN RAFİNE EDİLMESİ

TUR 1 bulgusu (`EV-2026-08-09-322`): **2 × 20DV, 1 × 40HC'den daha fazla şişe
taşır** (23.600–27.400 vs 19.100–21.500). **Bu bulgu DEĞİŞMEDİ ve doğrudur.**

TUR 1'de eksik olan şuydu: *hangisi şişe başına daha ucuz?* Eşik `1,54` olarak
verilmiş, oran `UNKNOWN` bırakılmıştı. **TUR 2'de oran ölçüldü.**

```
EŞİK (kapasite oranı):
  kötü uç : 19.100 / 13.700 = 1,394
  merkez  : 20.300 / 12.750 = 1,592
  iyi uç  : 21.500 / 11.800 = 1,822

AMPİRİK 40HC/20DV NAVLUN ORANI (iki bağımsız kaynak):
  DFDS 2025 tarifesi : 1.115/785 = 1,420 | 1.520/1.030 = 1,476
                       1.230/900 = 1,367 | 1.620/1.095 = 1,479
  Çin→Türkiye 2026   : 3.350/2.350 = 1,426 | 3.550/2.450 = 1,449
  → BAND: 1,37 – 1,48

KARŞILAŞTIRMA: 1,37–1,48  <  1,39–1,82 (eşik)
  → Bandın büyük kısmında 40HC ŞİŞE BAŞINA DAHA UCUZ.
  → Yalnızca en kötü köşede (eşik 1,39 & oran 1,48) 40HC marjinal kaybeder.

EK OLARAK — sabit kalemler tamamen 40HC lehine:
  Origin THO 287 EUR      : konteyner boyundan BAĞIMSIZ
  Origin B/L 62 EUR       : B/L başına
  THD İstanbul/İzmir      : konteyner boyundan BAĞIMSIZ (192 / 165 USD)
  Drop-off 50 USD         : konteyner başına
  Ordino 2.000–5.000 TL   : konteyner/BL başına
  Müşavirlik ek konteyner : 1.350 TL (2×20DV seçilirse TEKRARLAR)
```

**Sonuç (`EV-...-328`):**

| Karar | Gerekçe |
|---|---|
| **Pilot (≤13.700 şişe/sevkiyat): 20DV veya LCL** | 40HC ancak ~19.000+ şişede dolar; yarı boş 40HC'nin sabit maliyeti seyrelmez |
| **Ölçek (≥19.000 şişe/sevkiyat): 40HC** | Hem ocean oranı hem sabit kalemler 40HC lehine |
| **Ara bölge (13.700–19.000): 2 × 20DV vs 1 × 40HC** | 2×20DV daha çok şişe taşır ama **tüm sabit kalemleri ikiye katlar** → 40HC muhtemelen üstün, ama kanıt yeterli değil |

> **Uyarı:** 40HC'nin kapasitesi **Türkiye karayolu 44 t GVW limitiyle**
> sınırlıdır ve bu limit **çekici/şasi darası varsayımına** dayanır
> (13–16 t, `ASSUMPTION`, kanıt yok). Bu varsayım TUR 2'de de doğrulanamadı.
> 40HC kararı bu varsayımdan bağımsız değildir.

---

## 6. TRANSİT SÜRE MATRİSİ (GÜNCELLENMİŞ)

| Rota | TUR 1 | **TUR 2 (yeni kanıt)** | Kaynak sayısı | Değişim |
|---|---|---|---|---|
| İspanya → İstanbul | 7–10 gün (FACT) | **4 gün** (LCL, Flexport) | **3** (JSV T4 + Maersk T3 + Flexport T4) | ⬇ daha da kısa |
| İspanya → Mersin | 5–8 gün | değişmedi | 1 | — |
| İspanya → İzmir | 6–9 gün | değişmedi | 1 | — |
| Portekiz → İstanbul | — | **~4 gün** ⚠ (iç tutarsız) | 1 | **YENİ** |
| **İtalya → Türkiye** | UNKNOWN | **UNKNOWN** | 0 | — |
| Fransa → İstanbul | UNKNOWN | **12–15 gün** (Kuzey Avrupa aktarmalı) | 1 | **YENİ** |
| **California → İstanbul** | **UNKNOWN** ⚠ | **20 gün** (Atlanta→Kumport) | 2 (Oakland + LA) | **KAPANDI** |
| ABD Doğu → İstanbul | 18–38 (CONFLICT) | LA→Savannah→İstanbul **44 gün** | 1 | ⬆ uzadı |
| Şili → İstanbul | UNKNOWN | **43 gün** (via Barcelona) / 49 (via Hamburg) | 1 | **YENİ** |
| Arjantin → İstanbul | — | **25 gün** (via Hamburg) | 1 | **YENİ** |
| G. Afrika → İstanbul | ~26 gün (ters yön) | **49 gün** (via Hamburg) | 1 | ⬆ **~2 kat uzadı** |
| Avustralya → İstanbul | — | **36–56 gün** (via Singapur) | 1 | **YENİ** |

> **`C-302` için öneri (kapatma yetkisi bende değil):** Flexport (T4, tarihli,
> 2026-08-10) İspanya→İstanbul için **4 gün** veriyor. Bu, **üçüncü bağımsız
> kaynak** olarak A tarafını (kısa transit) destekliyor. B tarafı (BR Logistics,
> "Valencia→İstanbul 32–35 gün") artık 3 bağımsız kaynağa karşı tek başınadır ve
> kendi içinde de tutarsızdır. **C-302'nin A lehine kapatılmasını öneriyorum.**
> Ancak `LA→İstanbul 15 gün` iddiası **hiçbir kaynakla doğrulanmadı** (gerçek:
> 20 gün kara-aktarmalı veya 44 gün deniz-aktarmalı) — o ayak **reddedilmelidir.**

> **G. Afrika düzeltmesi kayda geçirilmelidir:** TUR 1, Türkiye→Cape Town ters
> yön ölçümünden ~26 gün tahmin etmişti. İthalat yönünde gerçek **49 gündür**
> (Hamburg aktarmalı). **TUR 1 tahmini yaklaşık 2 kat iyimserdi.** Bu, ters yön
> ölçümünün neden kullanılmaması gerektiğinin somut örneğidir.

---

## 7. SICAKLIK RİSKİ — ROTA YAPISIYLA YENİDEN DEĞERLENDİRME

TUR 2'nin routing bilgisi, sıcaklık riskini transit süresinden **daha keskin**
tanımlıyor: risk yalnızca gün sayısı değil, **hangi enlemlerden geçildiği** ve
**kaç kez elleçlendiğidir.**

| Rota | Transit | Aktarma | Rota yapısı | Yaz riski (ESTIMATE) |
|---|---|---|---|---|
| İspanya → İstanbul | **4 gün** | **0** | Akdeniz içi direkt | **DÜŞÜK** — kuru konteyner yeterli |
| Portekiz → İstanbul | ~4 gün ⚠ | 1 (Barcelona) | Atlantik + Akdeniz | düşük–orta |
| Fransa → İstanbul | 12–15 gün | 1 (Hamburg/Antwerp) | **Kuzey Avrupa dolaşması** | orta |
| California → İstanbul | 20 gün | 2 (kara Atlanta + deniz) | ABD karası + Atlantik | **orta–yüksek** (kara ayağında sıcaklık kontrolsüz) |
| Arjantin → İstanbul | 25 gün | 1 (Hamburg) | ekvator geçişi + Kuzey Avrupa | **yüksek** |
| Şili → İstanbul | 43 gün | 1 (Barcelona) | ekvator geçişi | **yüksek** |
| Avustralya → İstanbul | 36–56 gün | 1 (Singapur) | **tropik Singapur aktarması** | **çok yüksek** |
| G. Afrika → İstanbul | 49 gün | 1 (Hamburg) | ekvator **iki kez** (güney→kuzey→güney) | **çok yüksek** |

> **Yeni bulgu:** G. Afrika ve Avustralya rotaları yalnızca uzun değil,
> **termal olarak en kötü** rotalardır: Cape Town→Hamburg→İstanbul güzergâhı
> ekvatoru geçip Kuzey Denizi'ne çıkıyor, oradan tekrar güneye Akdeniz'e
> dönüyor. 49 günün büyük kısmı yüksek sıcaklık gradyanında geçiyor.
>
> **Thermal liner birim maliyeti ve beklenen fire oranı hâlâ UNKNOWN** →
> bu rotalar için liner/reefer kararı **finansal olarak verilemiyor**.

---

## 8. TAZELİK (`ttl`)

| evidence_id | ttl | STALE tarihi |
|---|---|---|
| `EV-2026-08-10-301 … -311` (Flexport LCL kotasyonları) | **6d** | **2026-08-16** ⚠ |
| `EV-2026-08-10-312` (FCL kotasyonu yokluğu) | 14d | 2026-08-24 |
| `EV-2026-08-10-322`, `-323`, `-324`, `-331` (FCL göstergeler) | 14d | 2026-08-24 |
| `EV-2026-08-10-329`, `-330` (türetilmiş maliyet/kırılma) | 14d | 2026-08-24 |
| `EV-2026-08-10-313 … -319`, `-325`, `-326`, `-327`, `-328`, `-332` | 90d | 2026-11-08 |
| `EV-2026-08-10-320` (DFDS 2025) | STALE-1y | **zaten eski — yalnızca oran için** |
| `EV-2026-08-10-321` (DFDS 2018) | 0d | **SUPERSEDED** |

> ⚠ **LCL kotasyonlarının geçerliliği 2026-08-16'da doluyor.** Bu, projedeki
> **en kısa ömürlü kanıt setidir.** Model 2026-08-16'dan sonra çalıştırılacaksa
> bu 11 kart yeniden doğrulanmalıdır (`99-ops/veri-tazeligi.md`).
