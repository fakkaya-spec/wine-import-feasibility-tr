# AJAN RAPORU — NAVLUN & LOJİSTİK (TUR 2)

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2 — COMMERCIAL VALIDATION
tarih:  2026-08-10
durum:  SUBMITTED
```

Ekler:
- `40-lojistik/rota-maliyet-matrisi.md` — **ana çıktı**: rota × kalem × konteyner tipi
- `40-lojistik/lcl-vs-fcl-pilot.md` — 5.000 şişelik pilot için LCL/20DV analizi
- `80-model/inputs/lojistik.yaml` → `tur2:` bloğu (TUR 1 blokları değiştirilmedi)
- `10-evidence/raw/EV-2026-08-10-301 … -332` — **32 kanıt kartı**
- `10-evidence/_index-parts/navlun-lojistik-uzmani-tur2.csv`
- `99-ops/_parts/{capraz-ipuclari,celiskiler,acik-sorular}-navlun-lojistik-uzmani-tur2.md`
- `99-ops/tickets/T-311.md`, `T-312.md`, `T-313.md`, `T-314.md`
- `99-ops/tickets/T-304.md` — **TUR 2 güncellemesi eklendi, status korundu**

---

## 1. YÖNETİCİ ÖZETİ

TUR 1'in en büyük boşluğu şuydu: **"hiçbir rotamız için doğrulanmış navlun
yok."** Bu turda teorik konteyner çalışmasını bıraktım ve rota bazlı gerçek
maliyet aradım. **32 kanıt kartı** açtım.

**Bulunan:** 9 rota için **gerçek, tarihli, geçerlilik süreli LCL kotasyonu**
(`EV-2026-08-10-301…311`, geçerlilik **2026-08-16**, `ttl: 6d`) ve — daha
önemlisi — **menşe ve varış local charge'larının T3 taşıyıcı tarifelerinden
kalem kalem çıkarılması** (`EV-...-313…316`).

**Bulunamayan:** **FCL navlunu.** Test edilen 14 Türkiye varışlı lane'in
**hiçbirinde** kamuya açık FCL kotasyonu yoktur (`EV-2026-08-10-312`).
`T-304` **kapanmamıştır**, `G2-L` **BLOCKED kalır**.

**En kritik tek bulgu:** Akdeniz→Türkiye rotasında **base okyanus navlunu
maliyetin küçük parçasıdır.** İspanya çıkış local charge'ları
(**349–554 EUR/konteyner**, `EV-...-313`, `-314`) tek başına aynı lane'in
tahmini base okyanus navlununun alt ucunu (**~300 USD**) aşmaktadır.
Yani **"navlun kaç para?" sorusu tek başına yanıltıcıdır** — belirleyici olan
kalem kompozisyonudur.

**İkinci en kritik bulgu:** TUR 1'de `CRITICAL UNKNOWN` olan **benchmark
ürünün rotası (California → İstanbul) kapandı**: **20 gün**, Oakland/LA →
Atlanta (kara) → Kumport → İstanbul, LCL base **0,505–0,574 USD/şişe**
(`EV-...-308`, `-309`).

---

## 2. BULGULAR

### B-1: Menşe local charge'ları base okyanus navlunuyla aynı mertebede

```yaml
claim:          Ispanya cikis local charge'lari (349-554 EUR/konteyner) base okyanus navlununun alt ucunu asiyor
value:          THO 287 EUR + B/L 62 EUR = min 349 EUR; ust uc 554 EUR
unit:           EUR / konteyner
status:         FACT
tier:           T3
evidence_id:    EV-2026-08-10-313, EV-2026-08-10-314
effective_date: 2026-04-01 (THO) / 2026-01-01 (B/L)
katman:         L1 → L2 gecisinin bir parcasi
```

**Gerekçe:** Hapag-Lloyd'un resmî İspanya local charge tarifesi (T3) taşıyıcının
kendi yayınıdır, yürürlük tarihleri kalem kalem yazılıdır ve pazarlığa açık
değildir. Bulunan kalemler:

| Kalem | Değer | Yürürlük | Konteyner boyuna bağlı mı |
|---|---|---|---|
| Origin THC (THO), dry | **287 EUR** | 2026-04-01 | **HAYIR** |
| B/L fee (EDI) | 62 EUR | 2026-01-01 | hayır (B/L başına) |
| VGM (manuel) | 50 EUR | — | hayır |
| Food Quality Container ⚠ | 115 EUR | 2022-04-01 | hayır |
| Equipment assignment | 40 EUR | 2023-04-01 | hayır |

**Karşılaştırma:** aynı lane'in base okyanus navlunu ESTIMATE bandı
**300–1.200 USD**. Yani alt uçta local charge'lar **navlundan büyüktür**.

**Bu bulgunun üç sonucu:**
1. Tedarikçiyle Incoterm pazarlığı (FOB mu EXW mi) navlun pazarlığından
   **daha değerli** olabilir → `T-312`, `T-305`.
2. Origin charge'lar **konteyner boyundan bağımsızdır** → 40HC lehine yapısal
   avantaj (bkz. B-4).
3. Sadece "navlun" soran bir RFQ **yanlış soru sorar**.

---

### B-2: 9 rotanın LCL navlunu artık biliniyor; sıralama karşı-sezgisel

```yaml
claim:          Sise basi LCL base okyanus navlununda Sili, Portekiz ile ayni bandda; Fransa Sili'den pahali
value:          Ispanya 0,274-0,297 | Portekiz 0,423-0,445 | Sili 0,432-0,454 | Fransa 0,636-0,675 | G.Afrika 0,766-0,788 USD/sise
unit:           USD / sise
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-301 … EV-2026-08-10-311
effective_date: 2026-08-10 (validity 2026-08-16)
katman:         L1 → L2 gecisinin bir parcasi (yalnizca okyanus bacagi)
```

**Türetme zinciri:**
```
Flexport kotasyonu (5 CBM / 750 kg bazli, USD)
  → USD/CBM = kotasyon / 5
  → USD/sise = (USD/CBM) / 449 sise/m3     [449: EV-2026-08-09-323]

Ornek (Valencia): 616 USD / 5 CBM = 123,2 USD/CBM / 449 = 0,274 USD/sise
                  666 USD / 5 CBM = 133,2 USD/CBM / 449 = 0,297 USD/sise
```

**Varsayım gerekçesi:** Kotasyonlar 5 CBM içindir; 11–12 CBM'lik pilot hacme
**doğrusal ölçeklendi** (`ASSUMPTION`). LCL'de per-CBM fiyat genellikle hacimle
**düşer**, yani bu varsayım **muhafazakârdır** (LCL'i olduğundan pahalı
gösterir) → `U-14`.

**İki karşı-sezgisel sonuç:**

1. **Şili ≈ Portekiz** (0,43–0,45 USD/şişe). "Uzak menşe = pahalı navlun"
   sezgisi bu rotada yanlıştır. Fark navlunda değil **transitte**: 43 gün vs
   ~4 gün.
2. **Fransa (Marsilya) > Şili** (0,64–0,68 vs 0,43–0,45). Sebebi coğrafya
   değil **routing**: Marsilya çıkışlı LCL yükü Hamburg/Antwerp'e gidip
   Türkiye'ye dönüyor (`EV-...-305`). **Fransa lojistik olarak bir Akdeniz
   menşei gibi davranmıyor.**

---

### B-3: FCL navlunu hâlâ UNKNOWN — ve bu bir arama başarısızlığı değil, piyasa yapısı

```yaml
claim:          Test edilen 14 Turkiye varisli lane'in hicbirinde kamuya acik FCL kotasyonu yoktur
value:          0 offerings (FCL), 14/14 lane
unit:           -
status:         FACT (yoklugun kaydi) / navlun degeri UNKNOWN
tier:           T4
evidence_id:    EV-2026-08-10-312
katman:         L1 → L2
```

**Gerekçe:** Test edilen lane'ler: ESVLC, ESBCN, PTLIS, ITGOA, ITSPE, ITLIV,
ITNAP, FRMRS, CLSAI, ZACPT, USOAK, USLAX, ARBUE, AUMEL → hepsi TRIST varışlı.
LCL kimi lane'de var kimi lane'de yok; **FCL hiçbirinde yok.**

Buna karşılık Türkiye **çıkışlı** (ihracat) FCL fiyatları kolayca bulunuyor:
DFDS yayınlanmış tarifesi, Nakliyerehberim rota listeleri, CANXANSA gösterge
oranları. **Kalıp açıktır:** Türk piyasası ihracat fiyatı yayınlıyor, ithalat
fiyatı yayınlamıyor.

**Kullanılabilen tek şey bir banddır:**

| | Değer | status | confidence |
|---|---|---|---|
| 20DV base ocean (İspanya→TR) | **300 – 1.200 USD** | ESTIMATE | **LOW** |
| 40HC base ocean | 411 – 1.776 USD | ESTIMATE | LOW |
| BAF/CAF/ETS | +%15 – 25 | ESTIMATE | LOW |

**4 kat genişliğinde bir band merkezî varsayım olamaz.** Bandın genişliğinin
tamamı `C-311`'den gelir.

---

### B-4: 40HC şişe başına ucuzdur — TUR 1'in eşiği ölçüldü

```yaml
claim:          Ampirik 40HC/20DV navlun orani (1,37-1,48) kapasite esiginin (1,39-1,82) ALTINDA -> 40HC sise basina avantajli
value:          ampirik oran 1,37-1,48 | esik 1,39-1,82 (merkez 1,59)
unit:           oran
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-328
katman:         -
```

**Türetme zinciri:**
```
ESIK (kapasiteden, EV-2026-08-09-320/321):
  kotu uc : 19.100 / 13.700 = 1,394
  merkez  : 20.300 / 12.750 = 1,592
  iyi uc  : 21.500 / 11.800 = 1,822

AMPIRIK ORAN — iki bagimsiz kaynak:
  DFDS 2025 yayinlanmis tarife : 1.115/785=1,420 | 1.520/1.030=1,476
                                 1.230/900=1,367 | 1.620/1.095=1,479
  Cin->Turkiye 2026            : 3.350/2.350=1,426 | 3.550/2.450=1,449
  → BAND 1,37 - 1,48

1,37-1,48  <  1,39-1,82  → 40HC sise basina daha ucuz
                            (yalnizca en kotu kosede marjinal kaybeder)

SABIT KALEMLER DE 40HC LEHINE:
  Origin THO 287 EUR         → konteyner boyundan BAGIMSIZ
  THD Istanbul/Izmir 165-192 → konteyner boyundan BAGIMSIZ
  Drop-off 50 USD, ordino, musavirlik ek konteyner 1.350 TL → konteyner basina
```

**Bu, TUR 1'i çürütmüyor, tamamlıyor.** TUR 1'in B-3 bulgusu ("2×20DV,
1×40HC'den daha fazla şişe taşır") **doğrudur ve değişmemiştir**. Değişen şey,
o bulgunun **ekonomik yorumudur**: daha fazla şişe taşımak, şişe başına daha
ucuz olmak demek değildir.

**Ama uygulama sınırı vardır:** 40HC ancak **~19.000+ şişe/sevkiyat**ta dolar.
Pilot ölçeğinde (5.000–13.700 şişe) 40HC **anlamsızdır.**

**Uyarı:** 40HC kapasitesi Türkiye karayolu 44 t GVW limitine, o da **çekici/şasi
darası varsayımına** (13–16 t, `ASSUMPTION`, kanıt yok) dayanır. Bu varsayım
TUR 2'de de doğrulanamadı (`U-7`).

---

### B-5: Varış limanı kararı terminal tarifesiyle değil iç nakliyeyle verilir

```yaml
claim:          THD farki (max 133 USD/konteyner) ic nakliye farkindan (37.500 TL) yaklasik 2 KAT kucuktur
value:          THD farki 0,006-0,011 USD/sise | ic nakliye farki 2,7-3,2 TRY/sise
unit:           USD ve TRY / sise
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-332, EV-2026-08-10-315, EV-2026-08-10-326
katman:         L2 → L3
```

**Gerekçe:** TUR 2'de varış THC'sinin **limana göre değiştiği** ilk kez
ölçüldü (`EV-...-315`, **T3**):

| Liman | THD 20DV | THD 40HC | 20/40 ayrımı |
|---|---|---|---|
| **İzmir / Aliağa** | **165** | **165** | **YOK** |
| Gemlik | 185 | 185 | YOK |
| **İstanbul / İzmit** | **192** | **192** | **YOK** |
| İskenderun | 207 | 238 | var |
| **Mersin** | **261** | **298** | var |

İzmir ile Mersin (40') arasında **%81 fark** var — bu ilk bakışta önemli
görünüyor. Ama şişe başına çevirince:

```
THD farki max     : 298 - 165 = 133 USD / konteyner
                    / 11.800-13.700 sise = 0,006 - 0,011 USD/sise

Ic nakliye farki  : Ambarli -> Izmir = 37.500 TL (2025-01-15, KDV haric)
                    / 11.800-13.700 sise = 2,7 - 3,2 TRY/sise
```

**Kur ne olursa olsun iç nakliye farkı THD farkının ~2 katı mertebesindedir.**

**Operasyonel kural (ESTIMATE):** **Varış limanı, terminal tarifesine göre
değil, antrepo/bandrolleme tesisinin ve hedef pazarın bulunduğu yere göre
seçilir.** Terminal tarife karşılaştırması yapmak, yanlış değişkeni optimize
etmektir.

---

### B-6: 5.000 şişelik pilotta LCL ile 20DV arasındaki fark gürültü seviyesindedir

```yaml
claim:          5.000 sisede LCL ve 20DV FCL arasindaki fiyat farki, her iki modun kendi belirsizlik bandindan KUCUKTUR
value:          kirilma noktasi ~5.900 sise (band 2.200-9.800)
unit:           adet / sevkiyat
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-330
katman:         L1 → L3
```

**Türetme zinciri:**
```
LCL(V)   = 123,2-133,2 USD/CBM x V  +  250-600 USD sabit    [EV-2026-08-10-301, EV-2026-08-09-324]
FCL_20DV = 1.256 - 2.946 USD-esdeger                        [USD 907-2.281 + EUR 349-554 @1,00-1,20]

V* = (FCL - sabit) / birim
  alt uc : (1.256 - 600) / 133,2 =  4,93 CBM = 2.210 sise
  merkez : (2.100 - 425) / 128,0 = 13,09 CBM = 5.875 sise
  ust uc : (2.946 - 250) / 123,2 = 21,88 CBM = 9.825 sise
```

**TUR 1 ne demişti:** 5.000–7.000 şişe (geniş band 1.600–9.900), genel LCL/FCL
kurallarından.
**TUR 2 ne diyor:** ~5.900 şişe (band 2.200–9.800), **rotaya özgü gerçek
kotasyondan**. **TUR 1'in merkezî tahmini bağımsız olarak doğrulandı.**

**Band neden hâlâ 4,5 kat geniş?** Çünkü LCL tarafı artık gerçek kotasyona
dayanıyor ama **FCL tarafı hâlâ UNKNOWN**. Bandın genişliğinin tamamı
`C-311`'den gelir.

**Kritik sonuç:** 5.000 şişelik pilot **kırılma noktasının tam üzerindedir.**
Bu tesadüf değil, matematiksel bir sonuçtur (5.000 şişe ≈ 11,6 CBM ≈ bir
20DV'nin %40'ı).

**Öneri (`40-lojistik/lcl-vs-fcl-pilot.md`):** **20DV FCL, paletli, yarı dolu.**
Gerekçe **fiyat değil**, üç non-finansal kriter: (a) cam kırılma riski —
LCL'de yük iki ayrı CFS'te elle elleçlenir ve kırılma oranı **UNKNOWN**;
(b) pilotun amacı ölçeklenecek operasyonun provasıdır; (c) sıcaklık ve
kontaminasyon kontrolü.

**Bu öneri iki koşulda tersine döner:** `T-301` cevabı "30+ gün bekleme"
çıkarsa, veya FCL base ocean bandın üst ucunda (1.200 USD) çıkarsa.

---

### B-7: Güney Afrika transit süresi TUR 1'de ~2 kat iyimser tahmin edilmişti

```yaml
claim:          Cape Town -> Istanbul gercek transit 49 gundur; TUR 1'in ~26 gun tahmini TERS YON olcumune dayaniyordu
value:          49 gun (Hamburg aktarmali)
unit:           gun
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-307
katman:         -
```

**Gerekçe:** TUR 1, Türkiye → Cape Town yönündeki bir ölçümden (~26 gün)
ithalat yönünü tahmin etmişti (`EV-2026-08-09-327`). Gerçek ithalat rotası
**Cape Town → Hamburg → İstanbul, 49 gün**dür.

**Bu, kendi TUR 1 tahminimin yanlışlanmasıdır ve kayda geçirilmiştir.**
Ders: **ters yön ölçümü aktarma yapısını yansıtmaz.** `EV-2026-08-09-327`'nin
`SUPERSEDED` sayılmasını öneriyorum.

Aynı düzeltme sıcaklık riskini de büyütür: Cape Town→Hamburg→İstanbul
güzergâhı ekvatoru geçip Kuzey Denizi'ne çıkıyor, oradan Akdeniz'e dönüyor.
**49 günün büyük kısmı yüksek sıcaklık gradyanında geçiyor.**

---

### B-8: Şişe başı toplam lojistik maliyeti tek para biriminde ifade edilemiyor

```yaml
claim:          Lojistik maliyeti UC PARA BIRIMINDEDIR ve makro.yaml -> fx null oldugu icin toplanamaz
value:          20DV paletsiz: 0,066-0,193 USD + 0,025-0,047 EUR + 1,32-2,46 TRY per sise
unit:           USD + EUR + TRY / sise
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-329
katman:         L1 → L3 arasi lojistik kalemleri
```

| Senaryo | USD/şişe | EUR/şişe | TRY/şişe |
|---|---|---|---|
| 20DV paletsiz (11.800–13.700) | 0,066 – 0,193 | 0,025 – 0,047 | 1,32 – 2,46 |
| 20DV paletli (6.480–7.200) | 0,090 – 0,310 | 0,048 – 0,086 | 2,50 – 4,48 |
| 40HC paletsiz (19.100–21.500) | 0,054 – 0,169 | 0,016 – 0,029 | 0,95 – 1,68 |
| LCL 5.000 şişe | 0,326 – 0,632 | 0 | 2,60 – 4,20 |
| 20DV'de yalnızca 5.000 şişe | 0,181 – 0,456 | 0,070 – 0,111 | 3,60 – 5,80 |

**Neden toplamadım:** `80-model/inputs/makro.yaml` kendi kuralında *"Kur tarihi
belirtilmeden kullanılan kur geçersizdir"* diyor ve `fx.usd_try`, `fx.eur_try`,
`kur_tarihi` alanlarının **hepsi `null`**. Kendi tahminimle kur uydurmak
`CLAUDE.md` §1.1 ihlali olurdu. → **`T-311`**

**Üç bacak üç farklı riske maruzdur:**
- **USD** = okyanus navlunu → spot volatilite (`ttl: 6–14d`) + kur riski
- **EUR** = menşe local charge'ları → sabit, yıllık ~%4 artıyor, **konteyner
  boyundan bağımsız** (40HC ile 3 kat seyreliyor)
- **TRY** = Türkiye operasyonu → **kur riski YOK**, enflasyon riski VAR

**Ölçek eğrisi doğrusal değildir:** 5.000 şişeden 100.000 şişeye giderken şişe
başı lojistik maliyeti **3–4 kat düşer.** Sabit bir "şişe başı navlun"
varsayımı küçük senaryoyu **iyimser**, büyük senaryoyu **kötümser** gösterir.

---

### B-9: TUR 1'in üç UNKNOWN'ı kapandı, ikisi daraldı

```yaml
claim:          Ordino, antrepo minimum suresi ve origin/destination masraf kalemleri artik biliniyor
value:          Ordino 2.000-5.000 TL | Antrepo minimum 7 gun | Ardiye free time 0 gun (celiskili)
unit:           TRY / gun
status:         ESTIMATE / FACT
tier:           T4
evidence_id:    EV-2026-08-10-325, EV-2026-08-10-327, EV-2026-08-10-317
katman:         L2 → L3
```

| Kalem | TUR 1 | TUR 2 |
|---|---|---|
| Ordino | UNKNOWN | **2.000–5.000 TL** |
| Antrepo minimum süre | UNKNOWN | **7 gün** |
| Antrepo depolama | 0,35 EUR/palet/gün (T5, tek kaynak) | **bağımsız olarak doğrulandı** |
| Ardiye free time | UNKNOWN (0 varsayıldı) | **0 gün (SafiPort)** — ama `C-312` |
| Limandan depoya çekme | 3.000–30.000 TL | **10.000–15.000 TL** (İstanbul içi, 20') |
| Gümrük müşavirliği İTH-2 4.670 TL | T3 tek kaynak | **bağımsız olarak doğrulandı** |
| Ambarlı terminal tarifesi | UNKNOWN | Kumport ardiye 18/29 USD/gün — **LOW, teyit gerekli** |

**Kumport bulgusu önemlidir ve TUR 1'i düzeltebilir:** Kumport ardiyesi
(18 USD/gün, 20ft) Beldeport/SafiPort'un (37–39 USD/gün) **yarısından azdır**.
Doğruysa TUR 1'in gecikme maliyeti hesabı (`EV-2026-08-09-344`) ~%40 yüksek
tahmin etmiştir. **Ama `confidence: LOW`** — tarife PDF'ine erişilemedi,
değerler arama özetinden alındı (`T-313`).

---

### B-10: Taşıyıcı THD'si ile terminal kapı-çıkış ücreti çakışıyor olabilir

```yaml
claim:          Tasiyicinin THD'si (165-298 USD) ile terminalin kapi-cikis ucreti (113-116 USD) ayni fiziksel olayi fiyatliyor olabilir
value:          fark ~115 USD/konteyner = 0,008-0,010 USD/sise
unit:           USD
status:         CONFLICT
tier:           T3 vs T4
evidence_id:    EV-2026-08-10-315, EV-2026-08-10-319
conflict_id:    C-313
katman:         L2 → L3
```

**Gerekçe:** TUR 1, terminalin tarifesini (113 USD) tek kalem olarak modele
koymuştu. TUR 2'de taşıyıcının kendi tarifesi (T3) bulundu ve **165–298 USD**
gösteriyor. Fiziksel olay tektir; iki taraf iki tarife yayınlıyor.

**Bu turda ne yaptım:** Muhafazakâr olarak yalnızca taşıyıcı THD'sini hesaba
kattım, çift saymadım. **Sessiz seçim değildir** — gerekçesi: taşıyıcı tarifesi
T3, terminal tarifesi T4 ve ithalatçının faturasını genellikle taşıyıcı keser.
**Ama çözülmedi** → `C-313`, `T-313`.

**Yön uyarısı:** TUR 1'in 113 USD'lik varsayımı, Senaryo 1 doğruysa **%32–62
düşüktür**. Yani bu düzeltme modeli proje **aleyhine** kaydırır.

---

## 3. UNKNOWN LİSTESİ

Tam liste: `99-ops/_parts/acik-sorular-navlun-lojistik-uzmani-tur2.md` (25 madde
+ başarısız olan 13 arama yolu).

**En kritik 8'i:**

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| U-1 | **Rota bazlı FCL navlunu (all-in kalem listesiyle)** | 14 lane'de "0 offerings"; dolaylı çapalar 4–5 kat çelişiyor | **CRITICAL** | 3 forwarder RFQ (`T-304`) |
| U-21 | **Ruhsat/bandrol bekleme süresi** | Mevzuat alanı — benim alanım değil | **CRITICAL** | `mevzuat-ruhsat-uzmani` (`T-301`) |
| U-22 | **Toplam lead time** | U-1 + U-13 + U-21'den türetilir | **CRITICAL** | `T-301` + `T-304` |
| U-2 | **İtalya → Türkiye navlunu (LCL ve FCL)** | 4 İtalyan limanında "0 offerings" | **HIGH** | Forwarder / armatör tarifesi (`T-312`) |
| U-3 | **İspanya dışı menşelerin origin charge'ları** | Yalnızca İspanya tarifesi tarandı | **HIGH** | Menşe başına taşıyıcı tarifesi (`T-312`) |
| U-4 | **Beklenen cam kırılma / fire oranı** | Sektör hasar istatistiği kamuya açık değil | **HIGH** | Sigortacı + forwarder (`T-314`) |
| U-5 | **Bandrolleme birim maliyeti + kapasite** | Antrepo hizmet teklifi gerekiyor | **HIGH** | Antrepo işletmecisi (`T-314`) |
| U-7 | **Çekici + şasi darası** | Kamuya açık değil (TUR 1'de de yoktu) | **HIGH** | Nakliyeciden ruhsat (`T-304`) |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

Detay: `99-ops/_parts/celiskiler-navlun-lojistik-uzmani-tur2.md`

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-311** | Freightify marketplace "from": Rotterdam→İzmir **295 USD**, İstanbul→Barcelona **500 USD** (T4, tarih yok) | FreightAmigo + BR Logistics: İspanya→Türkiye 20ft **1.200–2.500 EUR** (T5, 2025) | **4–5 kat fark.** Üç hipotez var (base vs all-in / eski veri / pazarlama taban fiyatı), hiçbiri doğrulanmadı | **OPEN — CRITICAL** |
| **C-312** | SafiPort 2026 tarifesi: ardiye "gemi yanaşmasından itibaren" → **free time 0 gün** (T4) | Gümrük müşavirliği rehberi 2026: "ardiye 6. günden itibaren" → **5 gün** (T4) | İkisi de T4, ikisi de 2026; ikisi de doğru olabilir (terminale göre değişebilir) | **OPEN — MEDIUM** |
| **C-313** | Hapag-Lloyd THD: **165–298 USD** (T3, 2026) | Beldeport/SafiPort kapı çıkış: **113–116 USD** (T4) | Aynı fiziksel olayı iki taraf ayrı fiyatlıyor; çift sayım riski | **OPEN — MEDIUM** |

**TUR 1 çelişkilerinin durumu:**

| conflict_id | TUR 2 durumu |
|---|---|
| **C-302** (Akdeniz transit) | **A LEHİNE KAPATILMASI ÖNERİLİR.** Flexport (T4, tarihli) **üçüncü bağımsız kaynak** olarak İspanya→İstanbul **4 gün** veriyor. B'nin ikinci ayağı ("LA→İstanbul 15 gün") de yanlışlandı: gerçek 20 gün (kara aktarmalı) veya 44 gün. **Kapatma yetkisi bende değildir.** |
| C-301 (palet sayısı) | Değişmedi, `OPEN` |
| C-303 (20DV payload) | Değişmedi, `OPEN`, düşük etkili |

**Hiçbir çelişkide sessizce taraf seçilmedi.** C-312 ve C-313'te muhafazakâr
olan kullanıldı ve bunun bir **seçim değil ihtiyat** olduğu her yerde yazıldı.

---

## 5. MODEL GİRDİLERİ

`80-model/inputs/lojistik.yaml → tur2:` bloğu. **TUR 1 blokları değiştirilmedi.**

| Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|
| `tur2.lcl_navlun_rota_bazli.ispanya_valencia_istanbul` | 616–666 | USD/5CBM | FACT | `EV-2026-08-10-301` |
| `…portekiz_lizbon_istanbul` | 949–999 | USD/5CBM | FACT | `EV-2026-08-10-303` |
| `…italya_istanbul` | **null** | — | **UNKNOWN** | `EV-2026-08-10-304` |
| `…fransa_marsilya_istanbul` | 1.428–1.515 | USD/5CBM | FACT | `EV-2026-08-10-305` |
| `…sili_sanantonio_istanbul` | 970–1.387 | USD/5CBM | FACT | `EV-2026-08-10-306` |
| `…guney_afrika_capetown_istanbul` | 1.720–1.770 | USD/5CBM | FACT | `EV-2026-08-10-307` |
| `…california_oakland_istanbul` | 1.239–1.289 | USD/5CBM | FACT | `EV-2026-08-10-308` |
| `…arjantin_buenosaires_istanbul` | 1.150–1.200 | USD/5CBM | FACT | `EV-2026-08-10-310` |
| `…avustralya_melbourne_istanbul` | 1.187–2.545 | USD/5CBM | FACT | `EV-2026-08-10-311` |
| `tur2.fcl_navlun.kamuya_acik_kotasyon_var_mi` | **false** | — | FACT | `EV-2026-08-10-312` |
| `tur2.fcl_navlun.ispanya_turkiye_20dv_base_ocean` | 300–1.200 | USD | **ESTIMATE (LOW)** | `EV-...-322/320/324` |
| `tur2.fcl_navlun.hc40_dv20_navlun_orani` | **1,37–1,48** | oran | ESTIMATE | `EV-2026-08-10-328` |
| `tur2.fcl_navlun.hc40_karlilik_esigi` | 1,39–1,82 | oran | ESTIMATE | `EV-2026-08-10-328` |
| `tur2.origin_charges_ispanya.thc_origin_tho` | **287** | EUR/ktr | **FACT (T3)** | `EV-2026-08-10-313` |
| `tur2.origin_charges_ispanya.dokuman_bl_edi` | 62 | EUR | **FACT (T3)** | `EV-2026-08-10-314` |
| `tur2.origin_charges_ispanya.toplam_minimum` | 349 | EUR/ktr | ESTIMATE | `EV-...-313/314` |
| `tur2.destination_charges_turkiye.thd_limana_gore` | 165 / 185 / 192 / 261 / 298 | USD/ktr | **FACT (T3)** | `EV-2026-08-10-315` |
| `tur2.destination_charges_turkiye.ordino` | 2.000–5.000 | TRY | ESTIMATE | `EV-2026-08-10-325` |
| `tur2.destination_charges_turkiye.fuel_surcharge_destination_truck_pct` | 39 | % | **FACT (T3)** | `EV-2026-08-10-316` |
| `tur2.terminal_tarifeleri.safiport_ardiye_20ft` | 39/44/53 | USD/gün | FACT | `EV-2026-08-10-317` |
| `tur2.terminal_tarifeleri.kumport_ambarli_ardiye` | 18/29/46 | USD/gün | **ESTIMATE (LOW)** | `EV-2026-08-10-318` |
| `tur2.terminal_tarifeleri.ardiye_free_time_gun` | 0 | gün | ESTIMATE (LOW) | `EV-2026-08-10-317` ⚠`C-312` |
| `tur2.ic_lojistik_tur2.limandan_depoya_istanbul_ici_20ft` | 10.000–15.000 | TRY | ESTIMATE (LOW) | `EV-2026-08-10-326` |
| `tur2.antrepo_tur2.minimum_sure_gun` | **7** | gün | ESTIMATE | `EV-2026-08-10-327` |
| `tur2.sise_basi_lojistik_maliyeti.*` | üç para birimi ayrı | USD+EUR+TRY | ESTIMATE | `EV-2026-08-10-329` |
| `tur2.lcl_fcl_kirilma_tur2.merkez_sise` | **5.900** | adet | ESTIMATE | `EV-2026-08-10-330` |
| `tur2.transit_tur2.california_istanbul_gun` | **20** | gün | FACT | `EV-...-308/309` |
| `tur2.transit_tur2.guney_afrika_istanbul_gun` | **49** | gün | FACT | `EV-2026-08-10-307` |
| `tur2.transit_tur2.italya_turkiye_gun` | **null** | — | **UNKNOWN** | `EV-2026-08-10-304` |
| `tur2.transit_tur2.toplam_lead_time_gun` | **null** | — | **UNKNOWN** | — |
| `tur2.sicaklik_riski_tur2.beklenen_fire_orani_pct` | **null** | — | **UNKNOWN** | — |

**evidence_id'si olmayan satır modele giremez** — bu kurala uyuldu.

---

## 6. ÇAPRAZ İPUÇLARI

Tam liste (17 ipucu): `99-ops/_parts/capraz-ipuclari-navlun-lojistik-uzmani-tur2.md`

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `global-sourcing-kasifi` | "Uzak menşe = pahalı navlun" **yanlış**: Şili ≈ Portekiz (0,43–0,45 USD/şişe) | Menşe elemesi navlunla yapılırsa Şili haksız yere elenir |
| `global-sourcing-kasifi` | Fransa lojistik olarak Akdeniz menşei gibi davranmıyor (Hamburg üzerinden, Şili'den pahalı) | Coğrafi sezgi servis yapısını yenmiyor |
| `global-sourcing-kasifi` | Menşe local charge'ları (349–554 EUR) base navlunla aynı mertebede → **RFQ'ya Incoterm sorusu** | FOB mu EXW mu pazarlığı navlun pazarlığından değerli olabilir |
| `global-sourcing-kasifi` | İtalya rotası ölçülemiyor → kısa listenin İspanya'ya kayması **ölçüm yanlılığı** olur | Sourcing kararının bütünlüğü |
| `finans-fizibilite` | Lojistik maliyeti **üç para birimindedir**; `makro.yaml → fx` null (`T-311`) | Tek değişkene sıkıştırmak modeli yanlış yerden hassas yapar |
| `finans-fizibilite` | Ölçek eğrisi **3–4 kat**; sabit şişe başı navlun varsayımı yasak | Senaryo karşılaştırmasının geçerliliği |
| `finans-fizibilite` | LCL/FCL kararını **fiyat vermiyor** — risk tercihi olarak modellenmeli | Modal seçim optimizasyon problemi değil |
| `mevzuat-ruhsat-uzmani` | "Limanda değil antrepoda bekle" farkı 30–35 kat değil **~15–25 kat** olabilir (Kumport + antrepo min 7 gün) | Yön aynı, büyüklük düzeltildi |
| `mevzuat-ruhsat-uzmani` | Taşıyıcı tarifesinde **veteriner/fitosaniter 126 USD/BL** (aktarma limanları) kalemi var — şarapta geçerli mi? | Aktarmalı rotalarda ek kalem |
| `mevzuat-ruhsat-uzmani` | "Food Quality Container" 115 EUR — şarapta zorunlu mu ihtiyari mi? | Fiyat kalemi, mevzuat sorusu |
| `gumruk-vergi-uzmani` | **Destination THD (165–298 USD) CIF'e girer mi?** Kalemler varış öncesi/sonrası ayrıştırıldı | Matrah tabanı; vergi çarpanıyla yayılır |
| `gumruk-vergi-uzmani` | İTH-2 = 4.670 TL bağımsız kaynakta doğrulandı; aynı kaynak KKDF'yi %6 diyor (**doğrulamadım**) | Çapraz doğrulama |
| `kanal-marj-uzmani` | Varış limanı seçimi bir **kanal kararıdır**: iç nakliye farkı THD farkının 2 katı | Dağıtım modeli lojistik maliyetini belirliyor |
| `turkiye-pazar-kasifi` | Benchmark ürünün rotası: 20 gün, 0,505–0,574 USD/şişe vs İspanya 4 gün, 0,274–0,297 | Rakip maliyet yapısı |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| **`T-304`** | `yatirim-komitesi-baskani` | Hiçbir rota için doğrulanmış navlun yok | **CRITICAL** | **OPEN — korundu** ⚠ |
| `T-311` | `finans-fizibilite` | Lojistik maliyeti üç para biriminde; `fx` null olduğu için toplanamaz | HIGH | OPEN *(yeni)* |
| `T-312` | `global-sourcing-kasifi` | İtalya rotası tamamen UNKNOWN; İspanya dışı origin charge'lar UNKNOWN → ölçüm yanlılığı | HIGH | OPEN *(yeni)* |
| `T-313` | `navlun-lojistik-uzmani` | Terminal ardiye/free time/THD çift sayımı üçlüsü çözülmedi | MEDIUM | OPEN *(yeni)* |
| `T-314` | `yatirim-komitesi-baskani` | Antrepo içi operasyon + kırılma oranı iki turdur UNKNOWN; masabaşında kapanmaz | HIGH | OPEN *(yeni)* |
| `T-301` | `mevzuat-ruhsat-uzmani` | *(benim ticket'ım değil — dokunmadım)* | CRITICAL | OPEN |

### `T-304` — neden kapatmadım

**Ticket'ın çekirdek iddiası hâlâ doğrudur.** Kapanan ve kapanmayan ayaklar
ticket dosyasına ayrıntılı işlendi (`99-ops/tickets/T-304.md` → "TUR 2
GÜNCELLEMESİ"). Özet:

| Ayak | Durum |
|---|---|
| LCL navlunu (9 rota) | ✅ **KAPANDI** |
| Origin THC / doc fee / ordino / destination THC / iç nakliye / antrepo min | ✅ **KAPANDI** |
| 40HC/20DV oranı | ✅ **KAPANDI** |
| California rotası | ✅ **KAPANDI** |
| **FCL navlunu (tüm rotalar)** | ❌ **KAPANMADI** — 14/14 lane'de kotasyon yok |
| İtalya rotası | ❌ KAPANMADI → `T-312` |
| Çekici/şasi darası | ❌ KAPANMADI |
| Kırılma oranı, bandrolleme, liner, sigorta kotasyonu | ❌ KAPANMADI → `T-314` |

**`status: OPEN`, `impact: CRITICAL` korundu. `G2-L` BLOCKED kalır.**
Açan tek koşul değişmedi: **3 forwarder'dan yazılı FCL kotasyonu.**

**Ticket'a iki yeni istenen aksiyon eklendi:**
(4) RFQ'da FCL ve LCL **aynı anda** fiyatlansın;
(5) RFQ'da `included/excluded charges` **tek tek** listelensin.

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-10-301 … -311` (**11 LCL kotasyonu**) | **6d** | **2026-08-16** ⚠⚠ |
| `EV-2026-08-10-312` (FCL kotasyonu yokluğu) | 14d | 2026-08-24 |
| `EV-2026-08-10-322`, `-323`, `-324`, `-331` (FCL göstergeler) | 14d | 2026-08-24 |
| `EV-2026-08-10-329`, `-330` (türetilmiş maliyet + kırılma noktası) | 14d | 2026-08-24 |
| `EV-2026-08-10-313 … -319`, `-325`, `-326`, `-327`, `-328`, `-332` | 90d | 2026-11-08 |
| `EV-2026-08-10-320` (DFDS 2025) | **zaten eski** | yalnızca oran için kullanılır |
| `EV-2026-08-10-321` (DFDS 2018) | 0d | **SUPERSEDED** |

> ⚠⚠ **Bu, projedeki en kısa ömürlü kanıt setidir.** LCL kotasyonlarının
> geçerliliği **2026-08-16**'da doluyor — bu rapordan **6 gün sonra**. Model
> bu tarihten sonra çalıştırılacaksa 11 kart yeniden doğrulanmalıdır.
> Ayrıca TUR 1'in navlun kartları (`EV-2026-08-09-330…333`) **2026-08-23**'te
> STALE olur.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Bir forwarder'dan gelecek gerçek FCL kotasyonunun 300–1.200 USD bandının
dışında çıkması.**

Bu raporun **finansal** sonuçlarının tamamı — şişe başı maliyet tablosu (B-8),
LCL/FCL kırılma noktası (B-6), pilot mod önerisi, 40HC eşik karşılaştırması
(B-4) — o bandın içine düşen bir FCL navlunu varsayıyor. Band **4 kat
geniştir** ve `C-311` çözülmediği için bandın hangi ucuna yakın olduğumuzu
bilmiyorum.

**Somut kırılma:** FCL 20DV base ocean **2.000 USD** çıkarsa (yani bandın
üstünde):
- 20DV şişe başı USD bacağı 0,193 → **0,25** USD'ye çıkar
- LCL/FCL kırılma noktası ~5.900 → **~9.500 şişe**'ye kayar
- 5.000 şişelik pilotta **LCL açık ara ucuz olur** → mod önerim (20DV FCL)
  yalnızca kırılganlık argümanıyla ayakta kalır, fiyat argümanı çöker
- 40HC eşik karşılaştırması **etkilenmez** (oran bazlı)

**İkinci çürütücü:** LCL per-CBM fiyatının 5 CBM'den 12 CBM'e **doğrusal
ölçeklenmemesi.** LCL'de hacim iskontosu tipiktir. Gerçek 12 CBM fiyatı
%20 daha ucuzsa LCL bacağı 1.380–1.598 → 1.100–1.280 USD'ye iner ve kırılma
noktası **~7.400 şişe**'ye kayar — yani 5.000'lik pilotta **LCL kazanır.**
Bu, benim `ASSUMPTION`'ımdır ve muhafazakâr yöndedir, ama yanlış olabilir.

### 9.2 En kırılgan varsayımım hangisi ve neden?

Sıralı olarak:

1. **FCL base ocean freight = 300–1.200 USD.** Bu bir varsayım bile değil,
   **iki çelişen kaynağın birleşimi**dir (`C-311`). Raporun finansal
   sonuçlarının çoğu buna dayanıyor. **En kırılgan yer burasıdır.**
2. **LCL per-CBM'in doğrusal ölçeklendiği.** 5 CBM kotasyonundan 12 CBM
   hacmine ekstrapolasyon. Muhafazakâr ama doğrulanmamış (`U-14`).
3. **THD ile terminal kapı-çıkış ücretinin çakıştığı** (`C-313`). Yalnızca
   THD'yi saydım. Yanılıyorsam konteyner başına 115 USD eksik hesapladım.
4. **Ardiye free time = 0 gün** (`C-312`). Muhafazakâr; yanılıyorsam gecikme
   maliyeti tahminim yüksek.
5. **Kumport ardiye değerleri** (18/29 USD). Arama özetinden alındı, PDF
   doğrulanmadı. Doğruysa TUR 1'in gecikme hesabını %40 düşürür.
6. **Çekici/şasi darası 13–16 t** — TUR 1'den devraldığım, **kanıtı olmayan**
   varsayım. TUR 2'de de kapanmadı. 40HC kararının altındaki zemin.
7. **449 şişe/m³** (TUR 1'den). Tüm USD/şişe çevrimleri buna dayanıyor;
   şişe formu değişirse tüm sütun kayar (`T-302`).

### 9.3 Hangi kaynağıma en az güveniyorum?

**Freightify'ın "from" fiyatları (`EV-2026-08-10-322`).**

Sebepleri:
- **Tarih yok** — 2026 mı 2024 mü bilmiyorum
- **Konteyner boyu belirtilmemiş** — 295 USD 20ft mi 40ft mi?
- **"from" fiyatıdır** — gerçekleşen değil, en düşük teorik
- **Neyin dahil olduğu yazmıyor** — bu tek başına diskalifiye edici
- Yine de **bandın alt ucunu tek başına bu kaynak belirliyor**

Ama bu kaynağı **atmadım**, çünkü atarsam band otomatik olarak T5 blogların
lehine kapanır ve o da bir sessiz taraf seçimi olur. `LOW` olarak işaretledim
ve `C-311`'e taşıdım.

**İkinci en az güvendiğim:** **Kumport ardiye değerleri** (`EV-...-318`).
Tarife PDF'ine erişemedim; değerler arama motoru özetinden geldi. Bu, kanıt
zincirinin en zayıf halkasıdır ve `T-313` ile işaretlendi.

**Üçüncü:** iç nakliye fiyatları (`EV-...-326`) — mesafeli seferler
**2025-01-15** tarihli, şehir içi "from" fiyatları 2026. **Aynı satırda
kullanılmamalıdır** ve `LOW` işaretlendi.

**Not:** En çok güvendiğim kaynaklar Hapag-Lloyd'un İspanya ve Türkiye local
charge tarifeleridir (**T3**, kalem kalem yürürlük tarihli, taşıyıcının kendi
resmî yayını). Bu turun en sağlam bulguları oradan geldi.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlış çıkan bulgu | Değişen karar |
|---|---|
| **FCL navlunu bandın üst ucunda (2.000+ USD)** | Kırılma noktası ~9.500 şişeye kayar → 5.000'lik pilot **LCL** ile yapılır; 25.000 şişe altı senaryolarda lojistik maliyeti +%30 |
| **LCL per-CBM hacimle düşüyorsa** | Kırılma noktası ~7.400'e kayar → yine **LCL** kazanır; pilot mod önerim değişir |
| **Menşe local charge'ları FOB'a dahilse** (tedarikçi ödüyorsa) | EUR bacağı sıfırlanır → 20DV şişe başı 0,025–0,047 EUR düşer; **sourcing Incoterm pazarlığının değeri artar** |
| **THD ile terminal ücreti ayrı faturalanıyorsa** | Konteyner başına +115 USD → şişe başı +0,008–0,010 USD; küçük ama **sistematik** |
| **Kumport ardiyesi doğruysa** | TUR 1'in gecikme maliyeti (60 gün → 8.000 USD) **%40 düşer** → `T-301`'in bekleme riski daha az yıkıcı olur |
| **İtalya navlunu İspanya'dan ucuz çıkarsa** | Menşe kısa listesi değişir; İtalya lojistik olarak dışlanmış görünüyor ama bu **ölçüm eksikliğidir**, bulgu değil |
| **Çekici/şasi darası 17 t çıkarsa** | 40HC paletli yükleme Türkiye karayoluna çıkamaz → 40HC ölçek senaryosu çöker, her şey 20DV'ye döner |
| **449 şişe/m³ yanlışsa (Burgundy formu → 278/m³)** | **Tüm USD/şişe sütunu %61 artar** → İspanya LCL 0,274 → 0,44 USD/şişe; rota sıralaması değişmez ama seviyeler kayar |

**Değişmeyecek olanlar:**
1. **Rota sıralaması** (İspanya < Portekiz ≈ Şili < ABD < Fransa < G.Afrika) —
   bu bir **oranlar** bulgusudur, seviye hatalarına dayanıklıdır.
2. **"Varış limanı iç nakliyeyle seçilir"** — büyüklük mertebesi farkı.
3. **"Menşe local charge'ları önemlidir"** — T3 tarifeden okundu, pazarlığa
   kapalı.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre | Kapattığı |
|---|---|---|---|---|---|
| 1 | **3 forwarder'dan yazılı FCL + LCL kotasyonu** — aynı port pair, 20DV + 40HC + 12 CBM LCL, `included/excluded` tek tek listeli, spot/kontrat, geçerlilik tarihi, free time, transit | `navlun-lojistik-uzmani` / TUR 7 | RFQ e-postası | **1–2 hafta** | `T-304`, `C-311`, `U-1`, `U-14` |
| 2 | **İtalya → Türkiye servis tarifesi** (armatör) | `navlun-lojistik-uzmani` | Armatör servis sayfaları + forwarder | 3–5 gün | `T-312`, `U-2` |
| 3 | **Menşe başına taşıyıcı local charge tarifesi** (PT/IT/FR/CL/ZA/US) | `navlun-lojistik-uzmani` | Taşıyıcıların yayınlanmış local charge PDF'leri — **İspanya için bu turda işe yaradı** | 2–3 gün | `T-312`, `U-3` |
| 4 | **Kumport/Marport/Mardaş 2026 tarife PDF'leri + free time** | `navlun-lojistik-uzmani` | Terminal/acente talebi | 3–5 gün | `T-313`, `C-312`, `U-10` |
| 5 | **Bir gerçek ithalat faturası** (THD ↔ terminal kalem ilişkisi) | `navlun-lojistik-uzmani` | Forwarder / müşavir | RFQ ile birlikte | `C-313`, `U-9` |
| 6 | **Antrepo + bandrolleme hizmet teklifi** (depolama, elleçleme, şişe/gün, birim maliyet) | `navlun-lojistik-uzmani` | İstanbul/İzmir/Mersin antrepo işletmecileri | **1–2 hafta** | `T-314`, `U-5`, `U-6`, `U-18` |
| 7 | **Sigorta kotasyonu + hasar oranı istatistiği** (ICC A + kırılma + termal şok) | `navlun-lojistik-uzmani` | Sigorta brokerı | 1 hafta | `T-314`, `U-4`, `U-12` |
| 8 | **Çekici/şasi darası + iç nakliye teklifi** | `navlun-lojistik-uzmani` | Türk nakliyeciden ruhsat + fiyat | 3–5 gün | `U-7` |
| 9 | **Ruhsat/bandrol takvimi** | `mevzuat-ruhsat-uzmani` | `T-301` | 1 hafta | `U-21`, `U-22` |
| 10 | **FX kuru ve kur tarihi** | `finans-fizibilite` | `makro.yaml` | — | `T-311`, `U-20` |

**Toplam:** yaklaşık **2–4 hafta** ve gerçek ticari temas gerektirir.

**Bu turda ne yapılamadı ve neden:** Görev tanımı bu turda dışarıya e-posta/form
gönderilmesini (forwarder'lara teklif istemek dahil) **yasaklamıştır.** Bu
yüzden yalnızca açık kaynak taranmıştır. **Açık kaynakta bulunabilecek her şey
bulunmuştur** — 13 farklı arama yolu denenmiş ve başarısız olanları
`99-ops/_parts/acik-sorular-navlun-lojistik-uzmani-tur2.md` §3'e kaydedilmiştir
ki tekrar denenmesin. **Kalan boşluk masabaşı boşluğu değil, ticari temas
boşluğudur.**
