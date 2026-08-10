# LCL vs 20DV FCL — 5.000 ŞİŞELİK PİLOT

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2
tarih:  2026-08-10
durum:  DRAFT
kanit:  EV-2026-08-10-301, -302, -322, -324, -329, -330 + TUR 1: EV-2026-08-09-323, -324, -320
rota:   Ispanya (Valencia/Barcelona) -> Istanbul  [en iyi kanitlanmis rota]
```

> **Neden yalnızca İspanya rotası?** 5.000 şişelik pilotun LCL/FCL kararı için
> **her iki modun da fiyatlanabildiği tek rota** budur. Diğer rotalarda LCL
> kotasyonu var ama FCL `UNKNOWN`; İtalya'da ikisi de `UNKNOWN`.

---

## 1. PİLOTUN FİZİKSEL BÜYÜKLÜĞÜ

```
5.000 şişe × 0,00223 – 0,00239 m³/şişe   =  11,15 – 11,95 m³   → 11,2 – 12,0 CBM
5.000 şişe × 1,26 kg/şişe                =  6.300 kg           → 6,3 ton

YOĞUNLUK = 6,3 t / 11,6 m³ = 0,54 t/m³  <  1 t/m³
→ LCL w/m (weight-or-measure) hesabında BAĞLAYICI OLAN CBM'DİR, ağırlık değil.
→ Şarap LCL'de HACİMDEN ücretlenir.  (EV-2026-08-09-323 ile aynı sonuç)

20DV paletsiz kapasitesi : 11.800 – 13.700 şişe
→ 5.000 şişe bir 20DV'nin YALNIZCA %36 – 42'sidir.
```

**İlk gözlem:** 5.000 şişelik bir pilot, 20DV seçilirse konteynerin **yaklaşık
%60'ını boş taşır.** Bu, kararın tamamını belirleyen tek gerçektir.

---

## 2. İKİ MODUN KALEM KALEM MALİYETİ

### 2.1 LCL (gerçek, tarihli kotasyon)

`source: Flexport (T4) · date: 2026-08-10 · validity: 2026-08-16 ·
route: ESVLC/ESBCN → TRIST · currency: USD · confidence: MEDIUM`

| Kalem | Alt uç | Üst uç | Kaynak / not |
|---|---|---|---|
| Base ocean freight | 11,2 × 123,2 = **1.380** | 12,0 × 133,2 = **1.598** | `EV-...-301` — 5 CBM kotasyonundan **doğrusal ölçeklendi** (ASSUMPTION) |
| Origin CFS | *(base'e dahil varsayıldı)* | 0 – 960 | `EV-2026-08-09-324` — 30–80 USD/CBM, dahil mi belirsiz |
| Destination CFS + sabit masraflar | 200 | 500 | `EV-2026-08-09-324` |
| Dokümantasyon | 50 | 100 | `EV-2026-08-09-324` |
| **USD TOPLAM** | **1.630** | **3.158** | |
| **EUR toplam** | **0** | **0** | Konteyner bazlı origin THC yok — CBM fiyatına gömülü |
| Ordino (TRY) | 2.000 | 5.000 | `EV-...-325` |
| Gümrük müşavirliği ANT-1 + İTH-2 (TRY) | 6.020 | 6.020 | `EV-2026-08-09-342` |
| CFS'ten depoya iç nakliye (TRY) | 5.000 | 10.000 | küçük araç, `EV-...-326`'dan türetildi (LOW) |
| X-ray (TRY) | 0 | 3.000 | `EV-...-325` |
| **TRY TOPLAM** | **13.020** | **24.020** | |

**Şişe başına:** `0,326 – 0,632 USD` + `0 EUR` + `2,60 – 4,20 TRY`

**LCL'in FİYATLANAMAYAN maliyetleri (hepsi UNKNOWN):**

| Gizli maliyet | Neden önemli | status |
|---|---|---|
| **Cam kırılma oranı** | LCL'de yük **iki ayrı CFS'te** elle elleçlenir; şarap kırılgan yük | **UNKNOWN** |
| Konsolidasyon beklemesi | Konteyner dolana kadar yük menşede bekler → lead time'a **+? gün** | **UNKNOWN** |
| CFS'te sıcaklık | CFS deposu iklimlendirilmiş değildir; yaz aylarında bekleme riski | **UNKNOWN** |
| Diğer yüklerle temas | Kokulu/kimyasal yük yanında konsolidasyon → şarapta koku transferi riski | **UNKNOWN** |
| Minimum ücretlendirme | 1 m³ / 1 ton minimum (`EV-2026-08-09-324`) — 11,6 m³'te bağlayıcı değil | bilinen |

### 2.2 20DV FCL (ESTIMATE, LOW confidence)

`route: Valencia/Barcelona → İstanbul veya İzmir · confidence: LOW (ocean
freight UNKNOWN) · ttl: 14d`

| Kalem | Alt uç | Üst uç | Kaynak / not |
|---|---|---|---|
| Base ocean freight (20DV) | **300** | **1.200** | `EV-...-322` (alt) / `EV-...-320`, `-324` (üst) — **CONFLICT `C-311`** |
| BAF / CAF / ETS (%15–25) | 45 | 300 | `EV-...-324` |
| Destination THD | 165 (İzmir) | 261 (Mersin) | `EV-...-315` (T3) |
| Drop-off fee | 50 | 50 | `EV-...-316` (T3) |
| Terminal ardiye (5 gün) | 90 | 195 | `EV-...-318` / `-317`, `-319` |
| Devanning (paletsizse) | 257 | 275 | `EV-...-317`, `-319` |
| **USD TOPLAM** | **907** | **2.281** | |
| Origin THC (THO) | **287** | 287 | `EV-...-313` (T3) |
| Origin B/L | 62 | 62 | `EV-...-314` (T3) |
| Origin opsiyonlar (VGM, RHO, FQS) | 0 | 205 | `EV-...-314` |
| **EUR TOPLAM** | **349** | **554** | |
| Ordino (TRY) | 2.000 | 5.000 | `EV-...-325` |
| Gümrük müşavirliği (TRY) | 6.020 | 6.020 | `EV-2026-08-09-342` |
| Limandan depoya çekme (TRY) | 10.000 | 15.000 | `EV-...-326` (LOW) |
| X-ray (TRY) | 0 | 3.000 | `EV-...-325` |
| **TRY TOPLAM** | **18.020** | **29.020** | |

**5.000 şişeye bölünürse:** `0,181 – 0,456 USD` + `0,070 – 0,111 EUR` +
`3,60 – 5,80 TRY` per şişe

---

## 3. DOĞRUDAN KARŞILAŞTIRMA — 5.000 ŞİŞE

| Para birimi | LCL | 20DV FCL | Kim kazanır |
|---|---|---|---|
| **USD/şişe** | 0,326 – 0,632 | **0,181 – 0,456** | **FCL** (fark 0,15 – 0,18) |
| **EUR/şişe** | **0** | 0,070 – 0,111 | **LCL** (fark 0,07 – 0,11) |
| **TRY/şişe** | **2,60 – 4,20** | 3,60 – 5,80 | **LCL** (fark 1,00 – 1,60) |

> ⛔ **Bu üç satır toplanamaz** (`makro.yaml → fx` = `null`, `T-311`).
> Ama yönü okunabilir: **FCL'in USD avantajı, EUR ve TRY dezavantajlarıyla
> büyük ölçüde nötralize olur.**
>
> Kaba bir mertebe kontrolü (EUR/USD 1,00–1,20 ve USD/TRY 30–50 aralığında,
> **ASSUMPTION — MODEL GİRDİSİ DEĞİLDİR**): iki mod arasındaki net fark
> **şişe başına ±0,05 USD mertebesindedir**, yani her iki modun kendi
> belirsizlik bandından (±0,15 USD) **küçüktür.**

### **SONUÇ: 5.000 şişelik pilotta LCL ile 20DV FCL arasında FİYAT FARKI GÜRÜLTÜ SEVİYESİNDEDİR.**

**Bu, kararın fiyatla verilemeyeceği anlamına gelir.**

---

## 4. KIRILMA NOKTASI HESABI (`EV-2026-08-10-330`)

```
MODEL:
  LCL(V)  = birim_cbm × V + varış_sabit
  FCL_20DV = sabit (hacimden bağımsız)

GİRDİLER (kanıtlı):
  birim_cbm   = 123,2 – 133,2 USD/CBM        [EV-2026-08-10-301, gerçek kotasyon]
  varış_sabit = 250 – 600 USD                [EV-2026-08-09-324]
  FCL_20DV    = 1.256 – 2.946 USD-eşdeğer    [USD 907–2.281 + EUR 349–554 @ 1,00–1,20]
                (EUR→USD çevrimi ASSUMPTION; EUR bacağı küçük olduğu için
                 sonuca etkisi < %5)

KIRILMA HACMİ  V* = (FCL_20DV − varış_sabit) / birim_cbm

  alt uç  : (1.256 − 600) / 133,2 =  4,93 CBM  →  2.210 şişe
  merkez  : (2.100 − 425) / 128,0 = 13,09 CBM  →  5.875 şişe
  üst uç  : (2.946 − 250) / 123,2 = 21,88 CBM  →  9.825 şişe
```

| | TUR 1 | **TUR 2** | Değişim |
|---|---|---|---|
| Merkezî tahmin | 5.000 – 7.000 şişe | **~5.900 şişe** | ✅ **doğrulandı** |
| Belirsizlik bandı | 1.600 – 9.900 | **2.200 – 9.800** | marjinal daraldı |
| Dayanak | genel LCL/FCL kuralları | **rotaya özgü, tarihli gerçek LCL kotasyonu** | ⬆ kalite |

> **Band neden hâlâ 4,5 kat geniş?** Çünkü LCL tarafı artık gerçek kotasyona
> dayanıyor ama **FCL tarafı hâlâ `UNKNOWN`.** Bandın genişliğinin tamamı
> `C-311`'den (base ocean 295–1.200 USD) geliyor. **`T-304` kapanmadan bu band
> daralmaz.**

**Yorum:** 5.000 şişelik pilot **kırılma noktasının tam üzerindedir.**
Bu bir tesadüf değil, matematiksel bir sonuçtur: 5.000 şişe ≈ 11,6 CBM ≈ bir
20DV'nin %40'ı — ve 20DV'nin sabit maliyeti tam da bu civarda LCL'in değişken
maliyetine eşitlenir.

---

## 5. KARAR FİYATLA VERİLEMEDİĞİNE GÖRE — NON-FİNANSAL KRİTERLER

| Kriter | LCL | 20DV FCL | Kazanan |
|---|---|---|---|
| **Cam kırılma riski** | 2 ayrı CFS'te elle elleçleme + diğer yüklerle istifleme | Menşede mühürlenir, Türkiye'de açılır | **FCL** ✔✔ |
| **Detention riski** | Konteyner iade yok → detention sayacı **yok** | 7 gün free time, sonrası 60–100 USD/gün | **LCL** ✔ |
| **Terminal ardiyesi** | CFS'te ayrı tarifeye tabi (UNKNOWN) | 0 gün free time, 18–39 USD/gün | belirsiz |
| **Ruhsat/bandrol beklemesi** (`T-301`) | Yük zaten CFS'te boşaltılmış — konteyner tutmuyor | Free time içinde antrepoya çekilmeli, aksi hâlde 30–35 kat maliyet | **LCL** ✔ |
| **Bandrolleme operasyonu** | Yük CFS'te koli koli; antrepoya transfer gerekir | Doğrudan antrepoya boşaltılır | **FCL** ✔ |
| **Sıcaklık kontrolü** | CFS bekleme süresi UNKNOWN + konsolidasyon beklemesi | Sevkiyat tarihi kontrol edilebilir | **FCL** ✔ |
| **Koku/kontaminasyon** | Diğer yüklerle aynı konteynerde | Yalnız kendi yükü | **FCL** ✔ |
| **Yükleme esnekliği** | Palet/paletsiz fark etmez | Yarı boş konteynerde **yük kayması riski** → dunnage/airbag gerekir | **LCL** ✔ |
| **Lead time öngörülebilirliği** | Konsolidasyon beklemesi UNKNOWN | Sefer tarihi belli | **FCL** ✔ |
| **Nakit akışı** | Küçük parti, düşük tek seferlik ödeme | Aynı hacimde benzer | eşit |
| **Öğrenme değeri (pilot amacı)** | Gerçek FCL operasyonunu **öğretmez** | Ölçeklenecek operasyonun **provasıdır** | **FCL** ✔ |

**Skor: FCL 6 – LCL 3 – eşit/belirsiz 2.**

---

## 6. ÖNERİ

```yaml
oneri:        20DV FCL (paletli, yarim dolu)
guven:        ORTA
status:       ESTIMATE
gerekce_tipi: NON-FINANSAL (fiyat farki gurultu seviyesinde)
karar_sahibi: yatirim-komitesi-baskani / finans-fizibilite
```

**Gerekçe — üç madde:**

1. **Fiyat kararı vermiyor.** İki mod arasındaki fark (±0,05 USD/şişe) her iki
   modun kendi belirsizlik bandından (±0,15 USD) küçüktür. Fiyata bakarak
   seçim yapmak **gürültüye bakarak seçim yapmaktır.**
2. **Kırılganlık kararı veriyor.** Şarap kırılgan yüktür ve LCL'in tek büyük
   gizli maliyeti olan **kırılma oranı `UNKNOWN`'dır.** Bilinmeyen bir riski,
   bilinen bir maliyetle (yarı boş konteyner) satın almak muhafazakâr seçimdir.
3. **Pilotun amacı öğrenmektir.** 5.000 şişelik bir sevkiyatın işi, gelecek
   25.000–100.000 şişelik sevkiyatların operasyonunu prova etmektir. LCL bunu
   yapmaz: gümrükleme, antrepo, devanning ve **bandrolleme akışı** LCL'de farklı
   çalışır.

**İki koşullu istisna — bu öneri şu iki durumda tersine döner:**

| Koşul | Sonuç |
|---|---|
| `T-301` cevabı "**ruhsat/bandrol beklemesi 30+ gün**" çıkarsa | FCL'de konteyner tutma/iade baskısı ve demurrage riski doğar → **LCL** avantaja geçer |
| FCL base ocean freight bandın **üst ucunda** (1.200 USD) çıkarsa | 5.000 şişede FCL şişe başına 0,456 USD'ye çıkar → LCL ile eşitlenir, kırılganlık argümanı tek başına kalır |

**Paletli mi paletsiz mi?**
Pilotta **paletli** öneriyorum. Paletsiz yükleme 20DV kapasitesini %64–90
artırır — ama **5.000 şişede kapasite zaten bağlayıcı değil** (konteyner
%40 dolu). Paletsizin bedeli (devanning 257–275 USD + kırılma riski + yeniden
paletleme, `EV-2026-08-09-341`) karşılığında hiçbir fayda alınmaz.
**Paletsiz yükleme yalnızca konteyner hacim-kısıtlı olduğunda anlamlıdır.**

---

## 7. HACİM SENARYOLARINA GÖRE MOD TABLOSU

| Yıllık hacim | Sevkiyat/yıl | Sevkiyat başı şişe | **Önerilen mod** | Gerekçe |
|---|---|---|---|---|
| 5.000 | 1 | 5.000 | **20DV paletli** (yarı dolu) | Kırılma riski + operasyon provası; fiyat nötr |
| 10.000 | 1 | 10.000 | **20DV paletsiz** | Kırılma noktasının (5.900) belirgin üstünde; kapasite bağlamaya başlıyor |
| 25.000 | 2 | 12.500 | **2 × 20DV paletsiz** | Her sevkiyat kapasiteye yakın |
| 50.000 | 3 | ~16.700 | **20DV + 40HC karışık** veya 4 × 20DV | Ara bölge — sabit kalemler 40HC lehine |
| 100.000 | 5 | 20.000 | **40HC paletsiz** | 40HC ancak burada dolar (19.100–21.500) |

> **Ölçek eğrisi doğrusal değildir.** 5.000 şişede şişe başı lojistik maliyeti
> (`0,181–0,456 USD + 0,070–0,111 EUR + 3,60–5,80 TRY`), 100.000 şişede
> (`0,054–0,169 USD + 0,016–0,029 EUR + 0,95–1,68 TRY`) **3–4 kat düşer.**
> Bu, `finans-fizibilite`'nin senaryo karşılaştırmasında **açıkça
> gösterilmelidir** — sabit bir "şişe başı navlun" varsayımı küçük senaryoyu
> sistematik olarak **iyimser**, büyük senaryoyu **kötümser** gösterir.
