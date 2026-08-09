# AJAN RAPORU — NAVLUN & LOJİSTİK (TUR 1)

```yaml
ajan:    navlun-lojistik-uzmani
tur:     TUR 1
tarih:   2026-08-09
durum:   SUBMITTED
```

Ekler:
- `40-lojistik/konteyner-kapasitesi.md` — şişe/koli/palet/konteyner hesabı (her adım gösterilmiş)
- `40-lojistik/navlun-aralıkları.md` — rota bazlı navlun aralıkları, masraf kalemleri, sıcaklık, sigorta
- `80-model/inputs/lojistik.yaml` — model girdileri
- `10-evidence/raw/EV-2026-08-09-301 … -380` — 38 kanıt kartı

---

## 1. YÖNETİCİ ÖZETİ

750 ml şarabın Türkiye'ye deniz yoluyla ithalatında konteyner kapasitesi, ağırlık
kısıtları, navlun seviyeleri, liman/antrepo masraf kalemleri, demurrage riski,
sıcaklık riski ve transit süreleri araştırıldı. **38 kanıt kartı** açıldı;
konteyner kapasitesi ilk ilkelerden, hesabın her adımı gösterilerek türetildi.

**En kritik tek bulgu — kapasite:** Şarapta bağlayıcı kısıt formata göre değişir
ve yaygın sezginin tersidir. **20DV'de bağlayıcı kısıt AĞIRLIK DEĞİL HACİM'dir**
— paletli 20DV'de payload'ın yalnızca %30–33'ü kullanılır (`EV-2026-08-09-320`).
Buna karşılık **40HC paletsizde bağlayıcı kısıt AĞIRLIK'tır ve bağlayıcı olan
konteynerin 28.690 kg'lık payload'ı değil, Türkiye karayolu 44 ton GVW limitidir**
(`EV-2026-08-09-310`, `EV-2026-08-09-321`). Bunun doğrudan sonucu:
**2 × 20DV, 1 × 40HC'den %24–27 daha fazla şişe taşır** (`EV-2026-08-09-322`).

**En kritik tek bulgu — navlun:** **Bizim rotalarımızın hiçbiri için doğrulanmış
navlun yoktur.** Drewry WCI ve Freightos FBX yalnızca Asya çıkışlı rotaları
ölçer; şarap Çin'den gelmez. Benchmark ürünün rotası olan **California →
İstanbul navlunu ve transit süresi tamamen UNKNOWN'dır.** Bu, `L1 → L2`
(FOB → CIF) geçişinin bu turda varsayımsal olduğu anlamına gelir (`T-304`,
`impact: CRITICAL`).

**En kritik tek bulgu — operasyon:** Ruhsat/bandrol beklemesi **limanda**
yaşanırsa 20DV başına 60 günde ~8.000 USD demurrage+ardiye doğar; **antrepoda**
yaşanırsa ~210 EUR. **Fark ~30–35 kat** (`EV-2026-08-09-344`). Bu, modelde
hangi senaryonun varsayıldığının açıkça yazılmasını zorunlu kılar.

---

## 2. BULGULAR

### B-1: 20DV'de şarap hacim kısıtlıdır, ağırlık kısıtlı değil

```yaml
claim:          20DV konteynerde 750 ml şarapta bağlayıcı kısıt HACİM'dir; payload'ın %30–60'ı boş kalır
value:          paletli 6.480–7.200 şişe | paletsiz 11.800–13.700 şişe | ağırlık kısıtı 20.400–22.400 şişe
unit:           adet
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-09-320
katman:         -
```

**Gerekçe:** Yaygın sezgi "şarap ağırdır, konteyner ağırlıktan dolar" der. Hesap
bunu 20DV'de yalanlıyor. Paletli yüklemede yüklü palet 1.480 mm, konteyner iç
yüksekliği 2.390 mm — ikinci palet konamaz (2×1.480=2.960 > 2.390), yüksekliğin
%38'i boşa gider ve yük ağırlığı yalnızca 9.270 kg'da kalır (payload'ın %33'ü).

**Türetme zinciri:**
```
Paketli şişe ağırlığı: Cellwind std palet spec (EV-...-307)
  927 kg brüt − 20 kg palet = 907 kg / 60 koli = 15,12 kg/koli / 12 = 1,26 kg/şişe
  6'lı format çapraz kontrolü: 870−20=850/112=7,59 kg/koli /6 = 1,265 kg  ✓ tutarlı

Paketli şişe hacmi:
  koli taban alanı = 1,20 m² / 15 koli = 0,0800 m²
  koli yüksekliği  = (1.480 − 145) / 4 = 334 mm
  koli hacmi = 0,02672 m³ → şişe başı 0,002227 m³

HACİM KISITI (paletli): 9–10 std palet × 720 şişe = 6.480–7.200
HACİM KISITI (paletsiz): 33,14 m³ × %85–92 / 0,00223–0,00239 = 11.800–13.700
AĞIRLIK KISITI: kargo tavanı 25.700–28.300 kg / 1,26 kg = 20.400–22.400
BAĞLAYICI = min(hacim, ağırlık) = HACİM
```

Çapraz kontrol: yayınlanmış "20ft paletsiz 13.200 şişe" iddiası
(`EV-2026-08-09-311`, T5) hesapladığım 11.800–13.700 bandının **üst ucundadır** —
tutarlı.

---

### B-2: 40HC'de bağlayıcı kısıt konteyner payload'ı değil, Türkiye karayolu limitidir

```yaml
claim:          40HC paletsiz yüklemede bağlayıcı kısıt Türkiye karayolu 44 ton GVW limitidir
value:          hacim kapasitesi 27.100–31.400 şişe; ağırlık kapasitesi 19.100–21.500 şişe
unit:           adet
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-09-321
```

**Gerekçe:** Karayolları Trafik Yönetmeliği Md.128 (`EV-2026-08-09-310`, **T2**),
ISO konteyner taşıyan yarı römorklu araçlarda azami yüklü ağırlığı **44 ton**
olarak belirler.

**Türetme zinciri:**
```
KARGO TAVANI = 44.000 − çekici/şasi darası − konteyner darası
40HC: 44.000 − (13.000…16.000) − 3.900 = 24.100 … 27.100 kg
                                          ↑ konteyner payload'ı 28.690 kg'dan DÜŞÜK

Ağırlık kısıtlı kapasite = 24.100/1,26 … 27.100/1,26 = 19.127 … 21.508 şişe
Hacim kısıtlı kapasite   = 76,4 m³ × %85–92 / 0,00223–0,00239 = 27.100 … 31.400 şişe
BAĞLAYICI = AĞIRLIK → 19.100–21.500 şişe
→ 40HC'nin iç hacminin %30–39'u kullanılamaz.
```

**Varsayım gerekçesi:** Çekici + şasi darası **13.000–16.000 kg** olarak
varsayıldı — **kanıtı yoktur** (`ASSUMPTION`). Bu, hesabın ikinci en kırılgan
girdisidir; gerçek dara 17 t ise 5 katmanlı paletli 40HC yüklemesi Türkiye'de
karayoluna çıkamaz. → `T-304`.

---

### B-3: 2 × 20DV, 1 × 40HC'den daha fazla şişe taşır

```yaml
claim:          Ağırlık limiti araç başına uygulandığı için 2×20DV > 1×40HC
value:          2×20DV 23.600–27.400 şişe | 1×40HC 19.100–21.500 şişe
unit:           adet
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-09-322
```

**Gerekçe:** 20DV hacimden, 40HC ağırlıktan dolar. Ağırlık limiti ise konteyner
başına değil **araç başına** uygulanır. Ekonomik sonuç navlun oranına bağlıdır:

```
40HC ancak şu koşulda daha ucuzdur:  Navlun_40HC / Navlun_20DV < 20.300/13.200 = 1,54
+ konteyner başı sabit masraflar 40HC lehine çalışır
  (THC 113 USD, müşavirlik ek konteyner 1.350 TL, iç nakliye, ardiye)

Bu oran UNKNOWN → karar RFQ olmadan verilemez (T-304).
```

Piyasada bu oranın 1,3–1,8 aralığında olduğu söylenir; **bu aralığın her iki ucu
farklı sonuç verir.** Bu yüzden bir sayı yazmıyorum.

---

### B-4: Paletsiz (floor loaded) yükleme 20DV kapasitesini %64–90 artırır

```yaml
claim:          Paletsiz yükleme kapasiteyi belirgin artırır ama net finansal fayda UNKNOWN
value:          20DV: 7.200 → 11.800–13.700 şişe (+%64…+%90); 40HC: 15.120 → 19.100–21.500 (+%27…+%42)
unit:           adet
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-09-320, EV-2026-08-09-321
```

**Gerekçe:** Palet, konteyner yüksekliğinin %38–45'ini israf eder.
**Ama bedeli vardır ve bedeli nicelendiremedim:**

| Maliyet kalemi | Değer | status |
|---|---|---|
| Terminal iç boşaltım (devanning) | 20ft **275 USD**, 40ft **350 USD** + KDV | FACT `EV-...-341` |
| Antrepoda yeniden paletleme | **UNKNOWN** | UNKNOWN |
| Ekstra elleçlemeden kırılma oranı | **UNKNOWN** | UNKNOWN |

**Sonuç:** Paletsizin navlun avantajı büyüktür, net faydası **UNKNOWN**'dır.
Türkiye'ye özgü bir hipotez: alkollü içki bandrol nedeniyle zaten antrepoda
koli koli elleçlenecekse, paletsizin dezavantajı azalır — **bu doğrulanmadı.**

---

### B-5: LCL/FCL kırılma noktası ~5.000–7.000 şişe/sevkiyat

```yaml
claim:          Sevkiyat başına ~5.000–7.000 şişeden sonra FCL ucuzlar
value:          5.000–7.000 şişe (tam belirsizlik bandı 1.600–9.900)
unit:           adet
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-09-323
```

**Türetme zinciri:**
```
Şarap yoğunluğu = 1,26 kg × 449 şişe/m³ = 566 kg/m³ = 0,57 t/m³ < 1 t/m³
→ LCL w/m hesabında CBM baglayıcıdır (ağırlık değil). Şarap hacimden ücretlenir.

FCL_20DV = LCL_sabit + LCL_per_cbm × V
  FCL 1.800 ; LCL 150/cbm + 400 → 9,3 m³ ≈ 4.190 şişe
  FCL 2.500 ; LCL 100/cbm + 300 → 22,0 m³ ≈ 9.880 şişe
  FCL 1.200 ; LCL 200/cbm + 500 → 3,5 m³ ≈ 1.570 şişe
Çapraz kontrol (T4): ">15 m³ veya >10.000 kg FCL'i haklı kılar" ≈ 6.735 şişe
```

**Band bu kadar geniştir çünkü FCL navlunu UNKNOWN'dır.**

**Charter senaryolarına uygulama:**

| Yıllık hacim | Mod | Not |
|---|---|---|
| 5.000 şişe | **LCL** | Lojistik olarak verimsiz — birim maliyet yüksek, kırılma riski fazla, varış sabit masrafları (200–500 USD) hacimden bağımsız |
| 10.000 şişe | sınırda / FCL 20DV | ~0,8 × 20DV (paletsiz) |
| 25.000 şişe | **FCL 20DV** | ~2 konteyner/yıl |
| 50.000 şişe | FCL | ~4 × 20DV veya ~2,5 × 40HC |
| 100.000 şişe | FCL 40HC değerlendirilmeli | ~8 × 20DV veya ~5 × 40HC |

---

### B-6: Türkiye'de gecikmede iki sayaç birden çalışır

```yaml
claim:          Türkiye ithalatında armatör D&D'si ve terminal ardiyesi AYRI AYRI faturalanır
value:          Maersk import free time 7 gün; sonrası 20ft 60→80→100 USD/gün, 40ft 75→115→150 USD/gün. Terminal ardiyesi ayrıca 33–90 USD/gün
unit:           USD/gün
status:         FACT
tier:           T3
evidence_id:    EV-2026-08-09-343, EV-2026-08-09-340, EV-2026-08-09-341
effective_date: 2025-09-15
```

**Gerekçe:** Maersk'in Türkiye ithalat sayfası açıkça "In Turkey Import Storage
charged by terminal operator directly" diyor. Yani modelde tek bir "demurrage"
kalemi yazmak **eksik**tir.

**Türetilmiş gecikme maliyeti (`EV-2026-08-09-344`):**

| 20DV bekleme | D&D | Ardiye | Toplam | Şişe başı (13.200) |
|---|---|---|---|---|
| 21 gün | ~1.100 USD | ~972 USD | **~2.072 USD** | ~0,16 USD |
| 60 gün | ~5.000 USD | ~3.000 USD | **~8.000 USD** | ~0,61 USD |

---

### B-7: Bekleme limanda değil antrepoda yapılmalıdır — ~30 kat fark

```yaml
claim:          Konteyneri free time içinde antrepoya çekmek bekleme maliyetini ~30–35 kat düşürür
value:          Limanda 60 gün ~8.000 USD | Antrepoda 60 gün ~210 EUR + beyanname + elleçleme
unit:           USD / EUR
status:         ESTIMATE
tier:           T4/T5
evidence_id:    EV-2026-08-09-344, EV-2026-08-09-350
```

**Gerekçe:** Konteyner boşaltılıp iade edilince detention ve terminal ardiyesi
**durur**; yerine antrepo depolama (~0,35 EUR/palet/gün) başlar.
10 palet × 60 gün × 0,35 EUR = 210 EUR.

**Uyarı:** Antrepo depolama birim fiyatı **T5** (LOW confidence) ve giriş/çıkış
elleçleme ile minimum süre ücretleri **UNKNOWN**'dır. Bunlar farkı daraltabilir
— ama büyüklük mertebesini değiştirmez.

**Bu, bu raporun en pratik operasyonel bulgusudur.**

---

### B-8: Hiçbir rotamız için doğrulanmış navlun yoktur

```yaml
claim:          Akdeniz/ABD/Şili/G.Afrika → Türkiye rotalarının hiçbiri için doğrulanmış navlun yok
value:          UNKNOWN
unit:           -
status:         UNKNOWN
tier:           -
evidence_id:    EV-2026-08-09-333 (yalnızca T5 gösterge), EV-2026-08-09-328, EV-2026-08-09-329
katman:         L1 → L2 geçişi
```

**Gerekçe:** Kamuya açık navlun endeksleri (Drewry WCI, Freightos FBX) yalnızca
Asya çıkışlı rotaları ölçer. FBX13'ün **varış** limanları arasında Ambarlı ve
İzmit vardır (`EV-2026-08-09-331`) — ama **menşe Çin'dir**. Bir Asya→Akdeniz
rakamını İspanya→Türkiye yerine koymak uydurmadır; yapmadım.

**Piyasa seviyesi çapaları (bizim rotamız DEĞİL, `FACT`, 2026-08-06):**

| Endeks | Değer | evidence_id |
|---|---|---|
| Drewry WCI kompozit | 4.297 USD/FEU | `EV-2026-08-09-330` |
| Drewry Shanghai→Genoa | 5.506 USD/FEU | `EV-2026-08-09-330` |
| Freightos FBX13 Çin→Akdeniz | 6.066,80 USD/FEU | `EV-2026-08-09-331` |
| Freightos Asya→Akdeniz | ~6.000 USD/FEU (Temmuz zirvesinin %16 altı) | `EV-2026-08-09-332` |

**Bizim rotalarımız:**

| Rota | 20DV | 40HC | conf. | status |
|---|---|---|---|---|
| İspanya → Türkiye | 1.200–2.500 EUR | 2.000–4.600 EUR | **LOW** (T5, all-in mi base mi bilinmiyor) | ESTIMATE |
| İtalya / Fransa → Türkiye | — | — | — | **UNKNOWN** |
| ABD Doğu → İstanbul | 2.550 USD | 4.600 USD | **LOW** (T5) | ESTIMATE |
| **California → İstanbul** | — | — | — | **UNKNOWN** ⚠ |
| Şili → Türkiye | — | — | — | **UNKNOWN** |
| G. Afrika → Türkiye | — | — | — | **UNKNOWN** |

---

### B-9: Transit süreleri — Akdeniz açık ara üstün

```yaml
claim:          Akdeniz menşei 5–10 gün, uzak menşeler 26–45 gün transit gerektirir
value:          Valencia→Ambarlı 7–10 gün; Valencia→Mersin 5–8; Valencia→İzmir 6–9; TR↔Cape Town ~26 gün
unit:           gün
status:         FACT (Akdeniz) / ESTIMATE (diğer)
tier:           T4 / T3
evidence_id:    EV-2026-08-09-325, EV-2026-08-09-326, EV-2026-08-09-327
```

**Gerekçe:** İki bağımsız kaynak Akdeniz sürelerini doğruluyor: bir sektör
rehberi (T4, 2026-05-19) ve **Maersk'in kendi SLR Marmara Sea A servis tarifesi**
(T3): Valencia→Barcelona 3g + →Piraeus 5g + →Ambarlı 2g = ~10 gün.

**ABD rotaları çelişkilidir** (`C-302`) ve California rotası **UNKNOWN**'dır.
Benchmark ürünün rotası tam budur.

**Sefer sıklığı:** Akdeniz haftalık/2 haftalık; G.Afrika 1–2 haftada bir. Düşük
frekans, bir sefer kaçırıldığında lead time'a **+7–14 gün** ekler.

---

### B-10: Toplam lead time UNKNOWN'dır ve bu kritiktir

```yaml
claim:          PO → satışa hazır toplam lead time hesaplanamıyor
value:          UNKNOWN
unit:           gün
status:         UNKNOWN
evidence_id:    -
```

**Gerekçe:** Zincirin yalnızca **bir halkasını** (transit) doğrulayabildim:

| Bileşen | Durum | Sahibi |
|---|---|---|
| Üretim/hazırlık | UNKNOWN | `global-sourcing-kasifi` |
| **Transit (Akdeniz)** | **7–10 gün** ✓ | bu ajan |
| Transit (California) | UNKNOWN | bu ajan → `T-304` |
| Gümrükleme | UNKNOWN | bu ajan / `gumruk-vergi-uzmani` |
| Antrepo + analiz + bandrol | UNKNOWN | `mevzuat-ruhsat-uzmani` → `T-301` |
| Bandrolleme operasyonu | UNKNOWN | bu ajan → `T-304` |
| İç nakliye | UNKNOWN | bu ajan → `T-304` |

**Yalnız transit süresini lead time sanmak modeli sistematik olarak iyimser
yapar.** `finans-fizibilite` bunu `UNKNOWN` olarak ele almalıdır.

---

### B-11: Sıcaklık riski rotaya bağlıdır; reefer göründüğünden pahalıdır

```yaml
claim:          Reefer'ın maliyeti navlun primiyle bitmez; gecikme riskiyle çarpılır
value:          Reefer okyanus primi %20–50 (T5) + terminal ardiyesi kuru konteynerin ~4 katı (135 vs 33 USD/gün)
unit:           % / USD/gün
status:         ESTIMATE / FACT
tier:           T5 / T4
evidence_id:    EV-2026-08-09-372, EV-2026-08-09-341
```

**Gerekçe:** Alkollü içkide gümrük/bandrol beklemesi olasılığı yüksektir. Reefer
seçilip beklenirse ardiye 4 kat işler. Şarabın 20 °C üstünde oksidasyonu hızlanır
ve ısı genleşmesi mantarı iterek **leakage** yaratır (`EV-2026-08-09-370`, T5).

| Rota | Transit | Yaz riski | Öneri (ESTIMATE) |
|---|---|---|---|
| Akdeniz (ES/IT/FR) | 5–10 gün | düşük–orta | Kuru konteyner yeterli olabilir; Tem–Ağu yüklemesinde liner |
| ABD Doğu | ~20–38 gün | orta–yüksek | Liner; yazdan kaçın |
| California | UNKNOWN (uzun) | **yüksek** | Liner/reefer; sevkiyat mevsimi planı |
| Şili / G.Afrika | 26–45 gün | **yüksek** | Liner/reefer değerlendirilmeli |

**Karar verilemiyor çünkü:** thermal liner birim maliyeti **UNKNOWN**,
beklenen fire oranı **UNKNOWN**. → `T-304`.

---

### B-12: Alkolde iki beyanname → gümrük müşavirliği iki kez

```yaml
claim:          Alkollü içkide antrepo + serbest dolaşıma giriş olmak üzere iki beyanname beklenmelidir
value:          ANT-1 1.350 TL (+CIF kademesi) + İTH-2 4.670 TL (+CIF kademesi) + ek konteyner 1.350 TL
unit:           TRY
status:         FACT (tarife) / ASSUMPTION (iki beyanname varsayımı)
tier:           T3
evidence_id:    EV-2026-08-09-342
effective_date: 2026-01-01
```

**Gerekçe:** 2026 Gümrük Müşavirliği **Asgari** Ücret Tarifesi'nden okundu.
Ayrıca `ÖZ-4` (laboratuvar tahlili / ekspertiz) **940 TL/işlem** ve terminal
tarafında **tam muayene** 20ft 2.322 TL / 40ft 3.249 TL kalemleri vardır
(`EV-2026-08-09-341`) — alkollü içkide muayene olasılığı yüksektir.

**Varsayım gerekçesi:** "İki beyanname" varsayımı bandrolün antrepoda
uygulandığı varsayımına dayanır ve **mevzuat teyidi yoktur** → `T-301`.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | **Rota bazlı FCL navlunu** (tüm rotalar, all-in) | Türkiye'ye giriş rotaları kamuya açık endekslerde yok; forwarder'lar kotasyonu yayınlamıyor | **CRITICAL** | 3 forwarder'dan yazılı RFQ (`T-304`) |
| 2 | **California → İstanbul transit + navlun** | Kaynaklar çelişkili ve iç tutarsız (`C-302`) | **CRITICAL** | Armatör servis tarifesi + RFQ |
| 3 | **Ruhsat/bandrol bekleme süresi (gün)** | Mevzuat alanı — benim alanım değil | **CRITICAL** | `mevzuat-ruhsat-uzmani` (`T-301`) |
| 4 | **Toplam lead time** | Yukarıdaki 3 kalemden türetilir | **CRITICAL** | `T-301` + `T-304` |
| 5 | Tedarikçinin gerçek koli/palet/şişe spec'i | Tedarikçi henüz seçilmedi | HIGH | RFQ'ya spec sheet maddesi (`T-302`) |
| 6 | Çekici + şasi darası (kg) | Türk nakliyeci verisi kamuya açık değil | HIGH | Nakliyeciden ruhsat bilgisi (`T-304`) |
| 7 | Terminal ardiye **free time** gün sayısı | Terminal tarifelerinden çıkarılamadı | HIGH | Terminal/acente (`T-304`) |
| 8 | Ambarlı terminallerinin (Marport/Kumport/Mardaş) tarifesi | Sayfalar 503/erişilemez | HIGH | Terminal tarife sayfaları |
| 9 | Bandrolleme birim maliyeti ve kapasitesi (şişe/gün) | Antrepo hizmet teklifi gerekiyor | HIGH | Antrepo işletmecisi (`T-304`) |
| 10 | Beklenen fire/leakage/kırılma oranı (%) | Sektör hasar istatistiği kamuya açık değil | HIGH | Sigortacı / uzman forwarder (`T-304`) |
| 11 | Thermal liner birim maliyeti | Hiçbir kaynakta fiyat yok | HIGH | Forwarder (`T-304`) |
| 12 | Origin THC, BAF/CAF, ISPS, doc fee, ordino | Kotasyona bağlı | MEDIUM | RFQ (`T-304`) |
| 13 | Limandan depoya çekme ücreti | Bulunan band (3.000–30.000 TL) çok geniş | MEDIUM | Nakliyeci teklifi (`T-304`) |
| 14 | Antrepo giriş/çıkış elleçleme + minimum süre | Sayfa 403 | MEDIUM | Antrepo işletmecisi |
| 15 | Türk sigortacıdan gerçek kotasyon + muafiyet | Kotasyon gerekli | MEDIUM | Sigorta brokerı (`T-304`) |
| 16 | Paletsiz yüklemede kırılma oranı + yeniden paletleme maliyeti | Veri yok | MEDIUM | Uzman forwarder (`T-304`) |
| 17 | İtalya / Fransa → Türkiye transit süreleri | Rehber kaynak yok | MEDIUM | Armatör servis tarifeleri |
| 18 | Şili → Türkiye rota yapısı | Kamuya açık veri yok | MEDIUM | Forwarder (`T-304`) |
| 19 | Diğer armatörlerin (MSC/CMA CGM/Arkas) D&D free time'ı | Sayfalar 403 | MEDIUM | Armatör local info sayfaları |
| 20 | 40HC gerçek dara ağırlığı | Maersk sayfası payload veriyor, dara vermiyor | LOW | Konteyner CSC plakası |
| 21 | LCL konsolidasyon beklemesinin süreye etkisi | Veri yok | LOW | Forwarder |
| 22 | Şarap konteyneri IMO sınıfına girer mi (%20 surprim) | Mevzuat alanı | LOW | `mevzuat-ruhsat-uzmani` |
| 23 | Şişe fiziksel boyutları (çap/yükseklik) | Tedarikçi verisi | MEDIUM | `T-302` |
| 24 | Alkole özel antrepo yetkisi gerekli mi | Mevzuat alanı | MEDIUM | `T-301` |
| 25 | Depodan kanala dağıtım (şişe başı) | Kanal modeli belirsiz | MEDIUM | `kanal-marj-uzmani` ile birlikte |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-301** | Hillebrand Gori *pallet types* (T4 / 2025-04-08): 20ft 10 std + 11 Euro; 40ft 21 std + 24 Euro | Hillebrand Gori *freight containers* (T4 / 2022-10-28): 20ft 9 std + 10 Euro; 40ft 20 std + 23 Euro | Aynı firmanın iki yayını uyuşmuyor; palet standardı (std/VMF/GMA) ayrımı net değil | **OPEN** |
| **C-302** | JSV Logistic (T4 / 2026-05-19) + Maersk servis tarifesi (T3): Valencia→İstanbul **7–10 gün** | BR Logistics (T5 / 2026): Valencia→İstanbul **32–35 gün**, LA→İstanbul **15 gün** | Kaynak B kendi içinde tutarsız (LA→İstanbul 15 gün fiziksel olarak imkânsız); door-to-door / port-to-port karışmış olabilir | **OPEN** |
| **C-303** | Maersk resmî FAQ (T3): 20DV payload 28.300 kg | iContainers (T4): ~28.200 kg; bir T5 kaynak: 26.000 kg | Konteyner serisi farkı veya CSC plakası vs ülke kısıtı karışması | **OPEN** (düşük etkili — şarapta 20DV zaten hacim kısıtlı) |

Detay: `99-ops/_parts/celiskiler-navlun-lojistik-uzmani.md`

**Hiçbir çelişkide sessizce taraf seçilmedi.** C-301'de band (9–11 / 20–24)
kullanıldı; C-302'de Akdeniz süreleri iki bağımsız kaynak doğruladığı için
kullanıldı, ABD süreleri `UNKNOWN` bırakıldı.

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| `lojistik.yaml` | `urun_fizik.paketli_sise_agirlik_kg` | 1,26 (band 1,21–1,38) | kg | ESTIMATE | `EV-2026-08-09-307` |
| `lojistik.yaml` | `urun_fizik.paketli_sise_hacim_m3` | 0,00223–0,00239 | m³ | ESTIMATE | `EV-2026-08-09-307` |
| `lojistik.yaml` | `urun_fizik.dolu_sise_brut_agirlik_kg` | 1,16–1,32 | kg | ESTIMATE | `EV-2026-08-09-305` |
| `lojistik.yaml` | `urun_fizik.palet_basina_sise.std_palet_12li_4katman` | 720 | adet | FACT | `EV-2026-08-09-307` |
| `lojistik.yaml` | `konteyner.spec_20dv.azami_payload_kg` | 28.300 | kg | FACT | `EV-2026-08-09-302` |
| `lojistik.yaml` | `konteyner.spec_40hc.azami_payload_kg` | 28.690 | kg | FACT | `EV-2026-08-09-302` |
| `lojistik.yaml` | `konteyner.spec_40hc.ic_hacim_m3` | 76,4 | m³ | FACT | `EV-2026-08-09-302` |
| `lojistik.yaml` | `karayolu_agirlik.iso_konteyner_azami_yuklu_agirlik_ton` | **44** | ton | **FACT (T2)** | `EV-2026-08-09-310` |
| `lojistik.yaml` | `konteyner.dv20.sise_kapasitesi_hacim_kisitli_paletsiz` | 11.800–13.700 | adet | ESTIMATE | `EV-2026-08-09-320` |
| `lojistik.yaml` | `konteyner.dv20.sise_kapasitesi_agirlik_kisitli` | 20.400–22.400 | adet | ESTIMATE | `EV-2026-08-09-320` |
| `lojistik.yaml` | `konteyner.dv20.baglayici_kisit` | **HACİM** | — | ESTIMATE | `EV-2026-08-09-320` |
| `lojistik.yaml` | `konteyner.hc40.sise_kapasitesi_hacim_kisitli_paletsiz` | 27.100–31.400 | adet | ESTIMATE | `EV-2026-08-09-321` |
| `lojistik.yaml` | `konteyner.hc40.sise_kapasitesi_agirlik_kisitli` | 19.100–21.500 | adet | ESTIMATE | `EV-2026-08-09-321` |
| `lojistik.yaml` | `konteyner.hc40.baglayici_kisit` | **AĞIRLIK** | — | ESTIMATE | `EV-2026-08-09-321` |
| `lojistik.yaml` | `navlun.lcl_fcl_kirilma_noktasi_sise` | 5.000–7.000 | adet | ESTIMATE | `EV-2026-08-09-323` |
| `lojistik.yaml` | `navlun.ek_masraflar.thc_destination` | 113 | USD | FACT | `EV-2026-08-09-340` |
| `lojistik.yaml` | `liman_ve_gumrukleme.ardiye_gunluk_20ft` | 33–52 | USD/gün | FACT | `EV-2026-08-09-340` |
| `lojistik.yaml` | `liman_ve_gumrukleme.ardiye_gunluk_40ft` | 58–90 | USD/gün | FACT | `EV-2026-08-09-340` |
| `lojistik.yaml` | `liman_ve_gumrukleme.ic_bosaltim_devanning` | 275 / 350 | USD | FACT | `EV-2026-08-09-341` |
| `lojistik.yaml` | `liman_ve_gumrukleme.gumruk_musavirligi_ithalat_deniz` | 4.670 | TRY | FACT (T3) | `EV-2026-08-09-342` |
| `lojistik.yaml` | `liman_ve_gumrukleme.antrepo_beyannamesi` | 1.350 | TRY | FACT (T3) | `EV-2026-08-09-342` |
| `lojistik.yaml` | `demurrage_detention.free_time_gun` | 7 | gün | FACT (T3) | `EV-2026-08-09-343` |
| `lojistik.yaml` | `demurrage_detention.dd_gunluk_20ft` | 60/80/100 | USD/gün | FACT (T3) | `EV-2026-08-09-343` |
| `lojistik.yaml` | `sigorta.prim_orani_pct` | 0,3–0,6 | % | ESTIMATE | `EV-2026-08-09-360` |
| `lojistik.yaml` | `sigorta.tasiyici_sinirli_sorumluluk_usd_kg` | 3 | USD/kg | FACT | `EV-2026-08-09-361` |
| `lojistik.yaml` | `sure.transit_gun_port_to_port.ispanya_ambarli` | 7–10 | gün | FACT | `EV-2026-08-09-325` |
| `lojistik.yaml` | `antrepo.depolama_ucreti_palet_gun` | 0,35 | EUR | ESTIMATE (LOW) | `EV-2026-08-09-350` |
| `lojistik.yaml` | `navlun.ocean_freight_per_konteyner` | **null** | — | **UNKNOWN** | — |
| `lojistik.yaml` | `sure.toplam_lead_time_gun` | **null** | — | **UNKNOWN** | — |

**evidence_id'si olmayan satır modele giremez** — bu kurala uyuldu; kanıtsız
her alan `null` + `UNKNOWN` bırakıldı.

---

## 6. ÇAPRAZ İPUÇLARI

Tam liste: `99-ops/_parts/capraz-ipuclari-navlun-lojistik-uzmani.md`

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `mevzuat-ruhsat-uzmani` | Bandrolün menşede mi antrepoda mı uygulandığı (T5 bilgi var, doğrulanmadı) | Lead time ve demurrage riskinin en büyük belirsizliği |
| `mevzuat-ruhsat-uzmani` | Alkolde iki beyanname (antrepo + ithalat) varsayımım teyide muhtaç | Müşavirlik maliyetini ikiye katlıyor |
| `mevzuat-ruhsat-uzmani` | Şarap terminal tarifesinde IMO sayılır mı (%20 surprim) | Terminal maliyeti |
| `gumruk-vergi-uzmani` | Navlun+sigorta gümrük kıymetine girer; ben hesaplamadım (`T-303`) | Matrah tabanı |
| `gumruk-vergi-uzmani` | Antrepo rejiminin nakit akışı avantajı (vergi serbest dolaşımda doğar) | `peak_cash_requirement` |
| `gumruk-vergi-uzmani` | ÖZ-4 laboratuvar/ekspertiz 940 TL ve terminal tam muayene 2.322/3.249 TL kalemleri | Unutulan kalemler |
| `global-sourcing-kasifi` | Şişe formu/koli geometrisi kapasiteyi %38 değiştiriyor → RFQ'ya spec sheet (`T-302`) | Şişe başı navlunun en büyük belirleyicisi |
| `global-sourcing-kasifi` | Hafif cam bir sourcing kriteri olmalı (40HC'de ağırlık bağlayıcı) | Kapasite |
| `global-sourcing-kasifi` | Akdeniz menşei lojistik olarak açık ara üstün; benchmark ürünü (California) en kötü rota | Menşe seçimi |
| `global-sourcing-kasifi` | Incoterm: CIF alımda ICC (C) kırılmayı kapsamaz (`T-305`) | Risk transferi |
| `finans-fizibilite` | 5.000 şişe/yıl lojistik olarak verimsiz — ölçek eğrisi doğrusal değil | Senaryo karşılaştırması |
| `finans-fizibilite` | Gecikme limanda mı antrepoda mı — 30 kat fark; model varsayımını yazmalı | Pilot maliyeti |
| `finans-fizibilite` | Navlun spot ve `ttl: 14d`; duyarlılık değişkeni olmalı (±%100) | Model geçerliliği |
| `kanal-marj-uzmani` | Yılda 1–2 konteyner gelişi stoku tek seferde yaratır → nakit döngüsü uzar | Vade/stok politikası |
| `turkiye-pazar-kasifi` | Rafta rakip şişelerin cam ağırlığı ve koli formatı gözlemlenebilir | Rakip maliyet yapısı |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| `T-301` | `mevzuat-ruhsat-uzmani` | Ruhsat/analiz/bandrol bekleme süresi kaç gün + bandrol nerede uygulanıyor | **CRITICAL** | OPEN |
| `T-302` | `global-sourcing-kasifi` | RFQ'ya "case & pallet spec sheet" zorunlu maddesi (kapasiteyi %38 değiştirir) | HIGH | OPEN |
| `T-303` | `gumruk-vergi-uzmani` | Navlun+sigortanın gümrük kıymetine girişi + Incoterm çift sayım riski | MEDIUM | OPEN |
| `T-304` | `yatirim-komitesi-baskani` | Hiçbir rota için doğrulanmış navlun yok; TUR 7'de gerçek RFQ zorunlu | **CRITICAL** | OPEN |
| `T-305` | `global-sourcing-kasifi` | Incoterm seçimi lojistik kontrolünü ve sigorta teminatını belirler | MEDIUM | OPEN |

> **İki CRITICAL ticket açıktır.** `CLAUDE.md` §5 gereği bunlar kapanmadan
> finans modeli `APPROVED` olamaz.

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-09-330` (Drewry WCI) | 14d | **2026-08-23** |
| `EV-2026-08-09-331` (FBX13) | 14d | **2026-08-23** |
| `EV-2026-08-09-332` (Freightos haftalık) | 14d | **2026-08-23** |
| `EV-2026-08-09-333` (rota navlun bandı) | 14d | **2026-08-23** |
| `EV-2026-08-09-323` (LCL/FCL kırılma) | 14d | **2026-08-23** |
| `EV-2026-08-09-324` (LCL maliyet yapısı) | 30d | 2026-09-08 |
| `EV-2026-08-09-340`, `-341`, `-343`, `-344`, `-350`, `-351`, `-372` | 90d | 2026-11-07 |
| `EV-2026-08-09-304`, `-305`, `-306`, `-307`, `-311`, `-320`, `-321`, `-322`, `-325`, `-326`, `-327`, `-328`, `-329`, `-360`, `-370`, `-380` | 180d | 2027-02-05 |
| `EV-2026-08-09-301`, `-302`, `-303`, `-308`, `-309`, `-310`, `-342`, `-361`, `-371` | 1y | 2027-08-09 |

**Navlun kanıtları 2026-08-23'te STALE olur.** Model bu tarihten sonra
çalıştırılacaksa navlun yeniden doğrulanmalıdır (`99-ops/veri-tazeligi.md`).

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Tedarikçinin gerçek koli/şişe geometrisinin varsaydığımdan belirgin farklı
çıkması.**

Tüm kapasite hesabım tek bir türetilmiş sayıya dayanıyor:
`0,00223–0,00239 m³/şişe`. Bu sayıyı bir logistics spec sheet'ten (Cellwind,
T4) geri hesapladım — **tedarikçiden almadım.**

Yayınlanmış Burgundy formu 12'li koli (410×305×345 mm) `0,0036 m³/şişe` verir.
Bu tek değişiklik:
- 20DV paletsiz kapasitesini 13.700 → 8.500 şişeye düşürür (**−%38**)
- şişe başı navlunu **+%61** artırır
- LCL/FCL kırılma noktasını yaklaşık 1/1,6 oranında kaydırır
- "20DV hacim kısıtlıdır" sonucunu **daha da güçlendirir** (bu yönü değişmez)

Yani: yön (hacim vs ağırlık) sağlam, **büyüklük kırılgan.**

İkinci bir çürütücü: **çekici + şasi darasının 13–16 t olmadığı** ortaya çıkarsa
40HC'nin "ağırlık kısıtlı" sonucunun büyüklüğü kayar. Dara 11 t ise 40HC tavanı
29,1 t'a çıkar ve konteyner payload'ı (28,69 t) tekrar bağlayıcı olur — sonuç
"ağırlık kısıtlı" kalır ama sebebi değişir. Dara 17 t ise durum daha da kötüleşir.

### 9.2 En kırılgan varsayımım hangisi ve neden?

Sıralı olarak:

1. **Şişe başı paketli hacim (0,00223–0,00239 m³).** Türetilmiş, tedarikçiden
   alınmamış, şişe formuna aşırı duyarlı. → `T-302`
2. **Çekici + şasi darası 13–16 t.** `ASSUMPTION`, **hiçbir kanıtı yok.**
   40HC kargo tavanını doğrudan belirliyor. → `T-304`
3. **Floor loading kup verimi %85–92.** `ASSUMPTION`. %80'e düşerse 20DV
   paletsiz 11.100 şişeye iner.
4. **Palet adedi 9–11 / 20–24.** Kaynaklar çelişiyor (`C-301`), band kullandım.
5. **"Alkolde iki beyanname" varsayımı.** Mevzuat teyidi yok, müşavirlik
   maliyetini ikiye katlıyor.
6. **Ardiye free time = 0 gün.** Muhafazakâr; gerçekte 3–7 gün olabilir →
   gecikme maliyeti tahminim yüksek olabilir.

### 9.3 Hangi kaynağıma en az güveniyorum?

**BR Logistics'in navlun ve transit tablosu (`EV-2026-08-09-333`,
`EV-2026-08-09-329`).** Sebepleri:

- **T5** pazarlama sayfası, geçerlilik tarihi yok
- **all-in mi base mi yazmıyor** — bu tek başına diskalifiye edici
- "20ft–40ft" aralığı veriyor ama hangi ucun hangisi olduğu belirsiz
- **kendi içinde tutarsız**: LA→İstanbul 15 gün (fiziksel olarak imkânsız),
  Valencia→İstanbul 32–35 gün (Akdeniz içi bir rota için absürt)

Bu yüzden bu kaynağı `CONFLICT`/`LOW` olarak işaretledim, ABD sayılarını modele
almadım ve İspanya bandını **yalnızca duyarlılık için** bıraktım.

İkinci en az güvendiğim: **antrepo depolama 0,35 EUR/palet/gün** (T5 ticari blog).
Bu sayı "limanda değil antrepoda bekle" sonucunun büyüklüğünü belirliyor. 10 kat
yanlış olsa bile sonucun yönü değişmez (2.100 EUR hâlâ 8.000 USD'den ucuz) —
ama bu bir şans, bir doğrulama değil.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlış çıkan bulgu | Değişen karar |
|---|---|
| **Şişe başı hacim %60 kötü** | Şişe başı navlun +%61 → düşük hacim senaryolarında (5.000–10.000 şişe) marj negatif olabilir → `KILL` veya yalnızca yüksek hacimde `TEST` |
| **Navlun 2× çıkarsa** | Şişe başı +0,10–0,20 USD; ayrıca gümrük kıymetine girdiği için vergi de artar → `IMPORT PILOT` yerine `HOLD` |
| **California navlunu aşırı pahalı çıkarsa** | Benchmark ürünle doğrudan rekabet stratejisi çöker → Akdeniz menşeine kayma zorunlu → sourcing yönü değişir |
| **Ruhsat/bandrol beklemesi 60+ gün çıkarsa** | Lead time ve `peak_cash_requirement` patlar → pilot büyüklüğü küçülür veya `HOLD` |
| **40HC dara varsayımı yanlışsa** | 20DV/40HC seçimi değişir → şişe başı lojistik maliyeti ±%10 |
| **20DV'de ağırlık bağlayıcı çıkarsa** (yani hesabım tersse) | Paletsiz yüklemenin faydası kaybolur → kapasite tahminleri düşer |

**Değişmeyecek olan:** "Bekleme limanda değil antrepoda yapılmalı" bulgusu.
Bu, büyüklük mertebesi farkı olduğu için girdi hataları karşısında dayanıklıdır.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre |
|---|---|---|---|---|
| 1 | **3 forwarder'dan yazılı FCL kotasyonu** (port pair, 20DV+40HC, all-in kalem listesi, spot/kontrat, geçerlilik tarihi, free time, transit) | `navlun-lojistik-uzmani` / TUR 7 | RFQ e-postası | **1–2 hafta** |
| 2 | **Tedarikçi case & pallet spec sheet** (14 kalem, bkz. `T-302`) | `global-sourcing-kasifi` | RFQ'ya zorunlu ek | 1–3 hafta |
| 3 | **Ruhsat/bandrol takvimi** (gün) | `mevzuat-ruhsat-uzmani` | TADAB mevzuatı + sektör görüşmesi (`T-301`) | 1 hafta |
| 4 | **Ambarlı terminal tarifeleri** (Marport/Kumport/Mardaş) + ardiye free time | `navlun-lojistik-uzmani` | Terminal/acente talebi | 3–5 gün |
| 5 | **Çekici/şasi darası + iç nakliye teklifi** | `navlun-lojistik-uzmani` | Türk nakliyeciden ruhsat + fiyat | 3–5 gün |
| 6 | **Sigorta kotasyonu** (ICC A + kırılma + termal şok, muafiyet dahil) | `navlun-lojistik-uzmani` | Sigorta brokerı | 1 hafta |
| 7 | **Antrepo + bandrolleme hizmet teklifi** (depolama, elleçleme, şişe/gün kapasite, birim maliyet) | `navlun-lojistik-uzmani` | İstanbul/İzmir/Mersin antrepo işletmecileri | 1–2 hafta |
| 8 | **C-301 çözümü** (stowage planı) | `navlun-lojistik-uzmani` | Forwarder'dan yazılı stowage | RFQ ile birlikte |

**Toplam:** yaklaşık **2–4 hafta** ve gerçek ticari temas gerektirir. Bu turda
masa başında yapılabilecek her şey yapılmıştır; kalan boşluklar **ancak piyasaya
çıkarak** kapanır.
