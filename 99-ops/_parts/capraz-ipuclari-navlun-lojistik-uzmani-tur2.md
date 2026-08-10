# ÇAPRAZ İPUÇLARI — navlun-lojistik-uzmani, TUR 2

```yaml
ajan:  navlun-lojistik-uzmani
tur:   TUR 2
tarih: 2026-08-10
not:   "Bu dosya 99-ops/capraz-ipuclari.md'ye BASKAN tarafindan islenir. Ana dosyaya dokunmadim."
kural: "Asagidakiler ALAN DISI BULGULARDIR. Hicbiri benim sonucum degildir."
```

---

## → `global-sourcing-kasifi`

### İP-2301 — "Uzak menşe = pahalı navlun" sezgisi bu projede YANLIŞ

Şişe başına LCL base okyanus navlunu (`EV-2026-08-10-301…311`):

```
Portekiz (Lizbon)  0,423 – 0,445 USD/şişe    transit  ~4 gün
Şili (San Antonio) 0,432 – 0,454 USD/şişe    transit  43 gün
                   ↑ NEREDEYSE AYNI
Fransa (Marsilya)  0,636 – 0,675 USD/şişe    transit  12–15 gün
                   ↑ ŞİLİ'DEN %47 PAHALI
```

**Sonuç:** Menşe elemesi navlun üzerinden yapılırsa Şili elenmemeli, Fransa
sorgulanmalıdır. **Ama fark navlunda değil TRANSİTTE:** 43 gün vs 4 gün.
Bunun işletme sermayesi etkisini hesaplamak `finans-fizibilite`'nin işidir.

### İP-2302 — Fransa lojistik olarak bir "Akdeniz menşei" gibi davranmıyor

Marsilya çıkışlı LCL yükü **Hamburg veya Antwerp'e (Kuzey Avrupa) gidip
oradan Türkiye'ye dönüyor** (`EV-2026-08-10-305`). Coğrafi yakınlık servis
yapısını yenmiyor. Fransız tedarikçi değerlendirilirse **FCL'de durumun farklı
olup olmadığı ayrıca sorulmalıdır** — FCL'de doğrudan Akdeniz servisi olabilir.

### İP-2303 — Menşe local charge'ları base navlunla aynı mertebede

İspanya çıkışında taşıyıcının kestiği zorunlu kalemler
(`EV-2026-08-10-313`, `-314`):

```
Origin THC (THO)  287 EUR   ← konteyner boyundan BAĞIMSIZ
B/L fee            62 EUR
                  ───────
Minimum           349 EUR / konteyner   (üst uç 554 EUR)
```

Aynı lane'in base okyanus navlununun **tahmini alt ucu 300 USD**'dir.
**Yani menşe local charge'ları navlundan büyük olabilir.**

**RFQ'ya eklenmesi gereken soru:** *"FOB fiyatınıza origin THC ve B/L ücreti
dahil mi?"* Incoterm FOB ise bu kalemler **satıcıdadır**; EXW ise **alıcıdadır**
ve şişe başına 0,025–0,047 USD-eşdeğer ek yük demektir (20DV'de).

### İP-2304 — Aynı port pair'de iki teklif arasında %31 fark var

Barcelona → İstanbul aynı gün, aynı sağlayıcı: teklif A 616–666 USD,
teklif B 809–859 USD (`EV-2026-08-10-302`). **Tek kotasyona güvenilmez.**
Bu kural tedarikçi fiyatları için de düşünülmelidir.

### İP-2305 — İtalya rotası ölçülemiyor (ölçüm yanlılığı uyarısı)

Dört İtalyan limanında hem FCL hem LCL kotasyonu **yok**
(`EV-2026-08-10-304`). Kısa liste yalnızca ölçülebildiği için İspanya'ya
kayarsa bu bir **bulgu değil, bir ölçüm yanlılığıdır**. → `T-312`

---

## → `finans-fizibilite`

### İP-2306 — Lojistik maliyeti ÜÇ PARA BİRİMİNDEDİR, tek sayı değildir

| Bacak | Ne | Risk türü | Konteyner boyuna duyarlı mı |
|---|---|---|---|
| **USD** | Okyanus navlunu + THD + devanning | Spot volatilite + kur | evet |
| **EUR** | Menşe local charge'ları | Kur + yıllık ~%4 tarife artışı | **hayır** (düz ücret) |
| **TRY** | Ordino, müşavirlik, iç nakliye | **Kur riski YOK**, enflasyon riski VAR | kısmen |

Tek bir "şişe başı navlun" değişkeni bu üç farklı riski tek bir duyarlılığa
sıkıştırır. → **`T-311`** (`makro.yaml → fx` hâlâ `null`).

### İP-2307 — Ölçek eğrisi doğrusal DEĞİL, 3–4 kat

```
   5.000 şişe (LCL veya yarı dolu 20DV) : 0,33–0,63 USD + 2,6–4,2 TRY / şişe
 100.000 şişe (40HC paletsiz)           : 0,05–0,17 USD + 0,95–1,68 TRY / şişe
```

Sabit bir şişe başı navlun varsayımı **küçük senaryoyu sistematik olarak
iyimser, büyük senaryoyu kötümser** gösterir. Senaryo karşılaştırmasında
lojistik maliyeti hacme bağlı bir fonksiyon olarak modellenmelidir.

### İP-2308 — LCL/FCL kırılma noktası doğrulandı ama kararı fiyat vermiyor

TUR 2 kırılma noktasını **~5.900 şişe** (band 2.200–9.800) olarak
doğruladı (`EV-2026-08-10-330`) — TUR 1'in 5.000–7.000 tahminiyle uyumlu.
**Ama 5.000 şişelik pilot tam kırılma noktasının üzerindedir**: iki mod
arasındaki fark (±0,05 USD/şişe) her iki modun kendi belirsizlik bandından
(±0,15 USD) küçüktür. Model bu kararı **fiyat optimizasyonu olarak
modellememelidir**; risk tercihi olarak modellemelidir.

### İP-2309 — Navlun spot ve `ttl: 6d` — projedeki en kısa ömürlü kanıt

LCL kotasyonlarının geçerliliği **2026-08-16**'da doluyor. Model bu tarihten
sonra çalıştırılırsa 11 kanıt kartı **STALE**'dir. Duyarlılık ±%100 olarak
korunmalıdır (`T-304`'ün 1. maddesi hâlâ geçerli).

---

## → `mevzuat-ruhsat-uzmani`

### İP-2310 — Bekleme yeri kararının maliyet farkı TUR 2'de DARALDI ama yön aynı

TUR 1: "limanda 60 gün ~8.000 USD vs antrepoda ~210 EUR → 30–35 kat".
TUR 2 iki düzeltme getiriyor:
- Kumport ardiyesi Beldeport'un **yarısından az** olabilir (18 vs 37 USD/gün,
  `EV-2026-08-10-318`, LOW) → limandaki maliyet **daha düşük** olabilir.
- Antrepoda **minimum 7 gün** faturalanıyor (`EV-2026-08-10-327`) → antrepo
  maliyeti **daha yüksek**.

**Yön değişmedi** (antrepo hâlâ çok daha ucuz), ama büyüklük 30–35 kat değil
**~15–25 kat** olabilir. `T-301`'in cevabı bu hesabın girdisidir.

### İP-2311 — Şarap "IMO / tehlikeli yük" değil ama "Food Quality Container" olabilir

Hapag-Lloyd İspanya tarifesinde **Food Quality Container (FQS) 115 EUR/konteyner**
kalemi var: *"gıda sevkiyatları için depodan kalite kontrollü kuru konteyner
talep edildiğinde"* (`EV-2026-08-10-314`). Şarap için zorunlu mu, ihtiyari mi
**bilinmiyor**. Gıda mevzuatı/etiket tarafı sizin alanınızda olduğu için not
düşüyorum — lojistik tarafında bu bir **fiyat kalemidir** ve modele opsiyon
olarak kondu.

### İP-2312 — Veteriner/fitosaniter kontrol ücreti aktarma limanlarında kesiliyor

Hapag-Lloyd Türkiye tarifesi: **126 USD/B/L**, yürürlük 2026-04-01, "transshipment
ports" için (`EV-2026-08-10-316`). Şarabın bu kontrole tabi olup olmadığı
**mevzuat sorusudur** — ama tarifede bir kalem olarak duruyor ve aktarmalı
rotalarda (Şili, G.Afrika, Arjantin, Fransa, ABD) uygulanma olasılığı vardır.

---

## → `gumruk-vergi-uzmani`

### İP-2313 — CIF'e giren navlun artık kalem kalem ayrıştırılabilir

Gümrük kıymeti hesabında hangi lojistik kaleminin CIF'e girdiği,
hangisinin girmediği kritik. TUR 2 kalemleri **varış limanı öncesi / sonrası**
olarak ayrıştırdı:

| Varış limanına KADAR (CIF'e girme adayı) | Varış limanından SONRA (CIF dışı adayı) |
|---|---|
| Ocean freight, BAF/CAF/ETS | Ordino |
| Origin THC (THO) 287 EUR | Terminal ardiye |
| Origin B/L 62 EUR, VGM, FQS | Devanning / unstuffing |
| Sigorta primi | Gümrük müşavirliği |
| **Destination THD 165–298 USD → hangi tarafta?** ⚠ | İç nakliye |

**Soru:** Destination THD (varış terminalinde elleçleme) CIF'e girer mi?
Bu **sizin alanınız**, ben hesaplamadım. Konteyner başına 165–298 USD, yani
20DV'de şişe başına 0,012–0,025 USD — matrahı büyütürse vergi çarpanıyla yayılır.
(`T-303` ile bağlantılı.)

### İP-2314 — Gümrük müşavirliği asgari tarifesi bağımsız olarak doğrulandı

TUR 1'in T3 kaynağından aldığı **İTH-2 = 4.670 TL** değeri, bağımsız bir
gümrük müşavirliği yayınında (2026-02-01) **birebir** doğrulandı
(`EV-2026-08-10-325`). Aynı kaynak KKDF'yi "%6" olarak veriyor — **bu sizin
alanınız, ben doğrulamadım ve modele koymadım.**

---

## → `kanal-marj-uzmani`

### İP-2315 — Varış limanı seçimi bir KANAL kararıdır, bir liman kararı değil

`EV-2026-08-10-332`:

```
THD farkı (İzmir 165 ↔ Mersin 40' 298) = 133 USD/konteyner = 0,006–0,011 USD/şişe
İç nakliye farkı (Ambarlı → İzmir)     = 37.500 TL         = 2,7–3,2 TRY/şişe
                                          ↑ ~2 KAT BÜYÜK
```

**Sonuç:** Varış limanı, terminal tarifesine göre değil **deponun ve hedef
kanalın bulunduğu yere göre** seçilir. Dağıtım modeliniz (İstanbul merkezli mi,
çok bölgeli mi) doğrudan lojistik maliyetini belirliyor. Depodan kanala dağıtım
maliyeti hâlâ **UNKNOWN**.

### İP-2316 — Sevkiyat frekansı stok politikasını belirliyor

Akdeniz menşeinde transit **4 gün** (`EV-2026-08-10-301`) — yani teorik olarak
sık ve küçük sevkiyat mümkün. Ama LCL/FCL kırılma noktası **~5.900 şişe**
olduğu için sevkiyat başına o hacmin altına inmek birim maliyeti yükseltiyor.
Bu, stok devir hızı ile lojistik maliyeti arasında doğrudan bir gerilim yaratır.
Hesabı `finans-fizibilite` yapar; kanal tarafının vade/sipariş büyüklüğü
tercihleri bu gerilimin girdisi.

---

## → `turkiye-pazar-kasifi`

### İP-2317 — Benchmark ürünün gerçek rotası artık biliniyor

Gold Country (California) için rota: **Oakland/LA → Atlanta (kara) → Kumport →
İstanbul, 20 gün**, LCL base navlun **0,505–0,574 USD/şişe**
(`EV-2026-08-10-308`, `-309`).

Kıyaslama: İspanya menşei **0,274–0,297 USD/şişe, 4 gün**.
**Benchmark ürünün lojistik dezavantajı ~0,25 USD/şişe ve 16 gün**dür.
Bu, rakip maliyet yapısı analizinizde kullanılabilir — ama benim tarafımdan
bir rekabet sonucu üretilmemiştir.
