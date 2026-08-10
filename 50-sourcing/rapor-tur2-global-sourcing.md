# AJAN RAPORU — GLOBAL SOURCING KÂŞİFİ — TUR 2

```yaml
ajan:                 global-sourcing-kasifi
tur:                  TUR 2 — COMMERCIAL VALIDATION
tarih:                2026-08-10
durum:                SUBMITTED
evidence_araligi:     EV-2026-08-10-451 … EV-2026-08-10-471 (21 kart)
ticket_araligi:       T-461 … T-468 (8 ticket)
conflict_araligi:     C-461, C-462 (2 çelişki)
tedarikci_sayisi:     26 (11 devir + 15 yeni)
teklif_alindi_mi:     false
uretici_ile_iletisim: NONE — bu turda hiçbir üreticiye e-posta / form / mesaj gönderilmedi
```

---

## 1. YÖNETİCİ ÖZETİ

Bu tur, TUR 1'in **ülke haritasını satın alınabilir ürüne çevirme** turudur.
26 üretici/ihracatçı shortlist'e alındı (11 devir + 15 yeni doğrulama), önceden
tanımlanmış beş kriterle **A/B/C** önceliklendirildi (A: 7, B: 10, C: 9) ve
gönderime hazır bir **TOP 10 RFQ hedef listesi** ile **iletişim paketi** kuruldu.

**En kritik tek bulgu:** İki tur boyunca aranan şey — bir üreticinin yayınladığı
şişe başı fiyat — **ilk kez bulundu** (`EV-2026-08-10-451`, Harland Wine Company,
AU: entry `$2.85+`/şişe). **Ve bu sayı modele giremez.** Para birimi kaynakta
yazılı değil ("$", AUD mı USD mi doğrulanamadı, ~1,5 kat fark), katmanı belirsiz
(tam konteynerde FOB/L1, MOQ siparişinde ex factory/L0 — `C-461`) ve etiket
baskısı hariç. `fiyat.exw_per_sise` ve `fiyat.fob_per_sise` **`null`/`UNKNOWN`
bırakıldı** (T-466, CRITICAL).

**İkinci kritik bulgu:** TUR 1'in *"private label pilot ölçekte uygulanabilir"*
sonucu **nitelendi** (`EV-2026-08-10-471`, `C-462`). Doğrulanmış MOQ aralığı
3.000–3.600'den **3.000–6.000 şişeye** genişledi; charter'ın 5.000 şişelik pilotu
bu aralığın **tam ortasına** düşüyor. Doğru ifade: **5.000'lik pilot, MOQ'su
bilinen beş üreticinin üçüyle mümkün, ikisiyle değildir.** MOQ bir ülke veya
sektör özelliği değil, **firma özelliğidir.**

**Üçüncü bulgu — TUR 1'in en büyük açığında ilerleme:** Model A tarafında
**7 somut marka adayı** bulundu (Viña Albali, Porta 6, Colombelle, Quinta da
Espiga, Particular, Purcari/Bostavan, Parras). Ancak yedisinin de Türkiye'de
ithalatçısı olup olmadığı `UNKNOWN`'dır (**T-464**) — açığın yarısı kapandı.

---

## 2. BULGULAR

### B-1: İki tur sonra ilk yayınlanmış şişe fiyatı bulundu — ve modele giremez

```yaml
claim:          Bir üretici private label şişe başı fiyat kademesini kamuya açık yayınlıyor; ancak para birimi ve katmanı belirsiz olduğu için fiyat girdisi olamaz
value:          "2.85+ (entry) / 5.00+ (mid) / 8.50+ (premium)"
unit:           "PARA BİRİMİ BİLİNMİYOR ($) / 750 ml şişe"
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-451
effective_date: -
katman:         null — UNKNOWN (L0 veya L1, sipariş büyüklüğüne bağlı)
```

**Gerekçe:** Harland Wine Company (AU) OEM/private label sayfası fiyatı üç
kademede yayınlıyor **ve neyi kapsadığını yazıyor**: *"All prices include: Bulk
Wine, Bottling, Dry Goods, Container Packing, FOB Transport to Port, Export
Documentation"* — buna karşılık *"Our price does not include the cost of printing
your labels"*.

**Neden `ESTIMATE`, neden `FACT` değil — üç bağımsız gerekçe:**
1. **Para birimi kaynakta yazılı değil.** Firma `.com.au`'dur, AUD muhtemeldir —
   ama bu **benim çıkarımım olurdu**, kaynağın beyanı değil. AUD/USD farkı
   ~1,5 kattır ve tek başına tüm ekonomiyi değiştirir.
2. **Katman belirsiz.** Aynı sayfa tam konteynerde fiyatın **FOB**, MOQ
   siparişinde **ex factory** olduğunu söylüyor. Yani **tek yayınlanmış sayı,
   sipariş büyüklüğüne göre L0 veya L1 oluyor** (`C-461`).
3. **Kapsam eksik.** Etiket baskısı hariç, karton dahil — L0'ın kapsamı tamamlanmamış.

**Ne anlama gelmez:** Bu bir teklif değildir (`quote_class: PUBLIC_INDICATIVE`).
`90-karar/tur-2-preflight-housekeeping.md` §D.3'e göre **G2 gate'i "gerçek RFQ
cevabı (≥5 tedarikçi)" ile açılır** — bir katalog fiyatı bunu karşılamaz ve
**G2'yi açmaz.**

---

### B-2: MOQ aralığı genişledi, pilot uyumu nitelendi

```yaml
claim:          Doğrulanmış private label MOQ aralığı 3.000-6.000 şişe/SKU'dur; 5.000'lik pilot beş üreticinin üçüyle mümkündür
value:          "3000 - 6000"
unit:           şişe (SKU başına)
status:         ESTIMATE
tier:           T4
evidence_id:    EV-2026-08-10-471
katman:         -
```

**Türetme zinciri (n=5, medyan 3.600):**

| Üretici | Ülke | MOQ | evidence_id | Tur |
|---|---|---|---|---|
| Interbrosa | ES | 3.000 | EV-2026-08-09-408 | 1 |
| Clark Estate | NZ | 3.000 | EV-2026-08-10-455 | 2 |
| The Wine Factory | FR | 3.600 | EV-2026-08-09-410 | 1 |
| Cantina Danese | IT | 6.000 | EV-2026-08-10-453 | 2 |
| Harland Wine Co. | AU | 6.000 | EV-2026-08-10-452 | 2 |

**TUR 1'in ifadesinin düzeltilmesi:** TUR 1 B-1 *"3.000–3.600 şişe … 5.000 şişelik
pilot hacmiyle UYUMLUDUR"* diyordu. Bu **hâlâ doğru ama artık eksiktir.**
TUR 2'de eklenen iki üretici 6.000 istiyor. **Pilot hacmi tedarikçi havuzunu
~%40 daraltıyor** — ve daralan havuz tipik olarak daha yüksek birim fiyat demektir.

**Bu bir CONFLICT'tir, ortalama alınamaz** (`C-462`). 3.000 ile 6.000'in ortalaması
(4.500) hiçbir üreticinin gerçek MOQ'su değildir. Ayrıca `C-401` (T5 agregatör
iddiası: 300–1.200) **hâlâ açıktır** — belirsizlik **iki yönlüdür.**

---

### B-3: Model A'da 7 somut marka adayı — ama temsilci durumu bilinmiyor

```yaml
claim:          Türkiye'de temsilcisi olup olmadığı bilinmeyen 7 somut f/p marka grubu tespit edildi
value:          7
unit:           marka grubu
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-456, -457, -458, -459, -461, -462; EV-2026-08-09-418
katman:         -
```

**Gerekçe:** Viña Albali/Los Molinos (Félix Solís, ES) · Porta 6 (Vidigal, PT) ·
Colombelle (Plaimont, FR) · Quinta da Espiga/Palha-Canas (Casa Santos Lima, PT) ·
Particular (San Valero, ES) · Purcari/Bostavan (Purcari Group, MD) · Parras (PT).

**TUR 1 açığına göre ilerleme:** `OQ-404` *"Türkiye'de temsilcisi olmayan somut
f/p markası bulunamadı"* diyordu. TUR 2 bu açığın **yarısını** kapattı: marka
listesi artık var. **İkinci yarısı** (Türkiye rafı/ithalatçı verisi)
`turkiye-pazar-kasifi`'nın alanıdır → **T-464**.

**Kendi aleyhime not:** Félix Solís 115 ülkede bulunuyor, Casa Santos Lima ~50
ülkede. **Bu ölçekteki markaların Türkiye'de boş olma ihtimali düşüktür.**
Bu, kendi bulgumu zayıflatan bir gözlemdir ve `supplier-priority-ranking.md`'de
de açıkça yazılmıştır.

---

### B-4: Doğrulanan tek ödeme şartı tamamen sevkiyat öncesi peşin

```yaml
claim:          Havuzda ödeme şartını yayınlayan tek üretici, bedelin tamamını sevkiyattan önce istiyor
value:          "%50 sipariş peşin + %50 şişeleme sonrası"
unit:           -
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-452
katman:         -
```

**Gerekçe:** *"We require 50% of the order paid upfront, with the remaining 50%
balance paid once the product has been bottled"*. The Wine Factory'nin (FR)
"ödeme sonrası üretim" ifadesi aynı yönde bir ipucudur ama şart olarak
doğrulanmamıştır.

**İki yönlü ve ters etki:**
- **Lehte:** Peşin ödeme KKDF doğurmuyorsa havuzun doğal yapısı vergi açısından
  avantajlı olabilir. **Sonucu bu ajan üretmez** → T-463.
- **Aleyhte:** Tedarikçi vadesi **0** olur; mal Türkiye'ye varmadan tam bedel
  ödenir; CCC kısalmaz, `peak_cash_requirement` **büyür**.

**n = 1.** Bu tek gözlem `odeme.vade_gun` alanını **doldurmaz.**

---

### B-5: İlk somut konteyner doluluk rakamı — ama paletsiz

```yaml
claim:          Bir üretici 20ft konteynere paletsiz (slipsheet) 14.112 şişe girdiğini ilan ediyor
value:          14112
unit:           şişe / 20ft DV (PALETSİZ)
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-452
katman:         -
```

**Gerekçe:** *"In a full 20' container, there are 14,112 bottles on slipsheets"*.
Bu, TUR 1'de açılan `T-402`'nin **ilk somut veri noktasıdır.**

**Kritik türetme (yalnızca aritmetik, yorum değil):** MOQ 6.000 / konteyner 14.112
= **%42**. Yani MOQ konteyneri doldurmuyor; charter'ın pilot hacimleri
(5.000 ve 10.000 şişe) de konteyner altındadır.

**Yapılmayan (bilinçli):** Paletli yüklemede kaç şişe gireceği hesaplanmadı,
LCL/groupage maliyeti tahmin edilmedi, birim navlun türetilmedi.
**Bunların tamamı `navlun-lojistik-uzmani` alanıdır** → T-461.

---

### B-6: Ürün tanımıyla doğrulanmış iki eşleşme

```yaml
claim:          İki tedarikçi/bölge, görev tanımındaki ürün profiliyle doğrulanmış biçimde eşleşiyor
value:          2
unit:           eşleşme
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-464, EV-2026-08-10-459
katman:         -
```

**Gerekçe:**
1. **Corta Hojas (CL)** private label beyaz portföyü = **Sauvignon Blanc +
   Chardonnay** — ürün listesiyle birebir.
2. **Plaimont (FR) / IGP Côtes de Gascogne** = **Colombard-Chardonnay** tarzının
   yapısal kaynağı; Colombelle bu apelasyonun amiral markası.

**Ne anlama GELMEZ — fiyat uyumu iddia edilmemiştir.** Fransa'nın Türkiye'ye L2
CIF birim değeri **6,27 USD/l**'dir (`EV-2026-08-09-405`) — segmentin çok üstünde.
Gascogne'un bu ortalamanın **altında** olduğu **doğrulanmamıştır**; TUR 1'de
Fransa'yı "f/p için yapısal olarak zorlayıcı" (Grup 4) diye işaretlemiştim ve
Gascogne bu genellemenin **sınanması gereken istisnasıdır**, kanıtlanmış istisnası değil.

---

### B-7: Dört negatif bulgu kaydedildi

```yaml
claim:          "Bakılmadı" ile "bakıldı, yok" ayrı kaydedildi
value:          4
unit:           negatif bulgu
status:         UNKNOWN (üçü) / FACT (biri)
tier:           T4
evidence_id:    EV-2026-08-10-466, -469, -467, -464
katman:         -
```

| # | Negatif bulgu | evidence_id |
|---|---|---|
| 1 | **Bronco Wine (US)** private label kabiliyeti kurumsal sitede **kanıtlanamadı** → `private_label_capable: UNKNOWN`, YES değil | EV-466 |
| 2 | **Arjantin'de üretici seviyesinde** private label **doğrulanamadı**; tüm yollar aracı/negociant veya dökme brokerinden geçiyor | EV-469 |
| 3 | **Interbrosa sitesi 2026-08-10'da HTTP 503** — `tedarikci.yaml`'daki "doğrulanmış en düşük MOQ" alanının **tek kaynağı** bugün teyit edilemedi | EV-467 |
| 4 | **Corta Hojas'ta MOQ/fiyat/Incoterm 2026-08-10'da hâlâ yayınlanmamış** (aynı sayfa yeniden okundu) | EV-464 |

**Neden önemli:** #2 Arjantin'i **elemez**, doğrulayamamıştır — ayrım kritiktir.
#1 charter'ın "private label yapar demeden önce kanıt göster" kuralının doğrudan
uygulanmasıdır: Bronco kavramsal olarak mükemmel bir adaydır (Charles Shaw),
**ama uygunluk kanıt değildir.**

---

### B-8: "FOB" terimi iki farklı katmana işaret ediyor

```yaml
claim:          Şarap ticaretinde FOB terimi hem Incoterms FOB (L1) hem ABD iç ticaretinde ex-cellar fiyat (fiilen L0) anlamında kullanılıyor
value:          "iki farklı tanım"
unit:           -
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-468
conflict_id:    C-461
katman:         L0 ↔ L1 (çelişki)
```

**Gerekçe ve somut tetikleyici:** Sektör kaynağı iki tanımı da doğruluyor.
Somut örnek TUR 2'nin kendi bulgusudur: Harland aynı fiyatı FCL'de FOB, MOQ
siparişinde ex factory diye tanımlıyor.

**Uygulanan kural:** Incoterm metinde açıkça tanımlanmadan hiçbir fiyat L0 veya
L1 diye etiketlenmedi. `supplier-shortlist-v2.csv`'de `price_layer` kolonu ayrı
tutuluyor ve belirsizse belirsizliği yazıyor.

**RFQ değişikliği GEREKMEDİ:** `rfq-template.md` v2.1 zaten 3.1'de EXW için
**yer**, 3.2'de FOB için **adı belirtilen liman** zorunlu tutuyor. Bu bulgu o
zorunluluğun **neden** konulduğunun kanıtıdır — şablon değiştirilmedi.

---

## 3. UNKNOWN LİSTESİ

### 3.A — Yalnızca gerçek RFQ ile öğrenilebilecek 21 alan

Bu turun **en önemli metodolojik çıktısı**: aşağıdaki alanlar için **daha fazla
açık kaynak araştırması yapmak kaynak israfıdır.**

| # | Alan | Açık kaynakta kaç tedarikçide bulundu (26 üzerinden) | RFQ sorusu |
|---|---|---|---|
| 1 | EXW şişe fiyatı | **1** (kademe hâlinde, para birimsiz) | 3.1 / S11 |
| 2 | FOB şişe fiyatı + adı belirtilen liman | **0** | 3.2 / S12 |
| 3 | Para birimi | **0** | 3.13 |
| 4 | Hacim bazlı fiyat kırılımı | **0** | 3.7 |
| 5 | Teklifin INDICATIVE/FIRM olması | **0** (tanım gereği) | 3.4 / S25 |
| 6 | Teklif geçerlilik tarihi | **0** | 3.5 / S25 |
| 7 | Gerçek MOQ (SKU **ve** konteyner) | **5** (ikisi farklı birimde) | 3.6a/3.6b |
| 8 | Ödeme şartı — ilk sipariş | **1** | 3.8 |
| 9 | Ödeme şartı — sonraki + vade günü | **0** | 3.9, 3.10 |
| 10 | Toplam lead time (PO → yüklemeye hazır) | **0** | 3.11 / S15 |
| 11 | Lead time kırılımı | **0** | 3.17 |
| 12 | Koli konfigürasyonu + ağırlık + ölçü | **1** (kısmen) | 2.1–2.3 |
| 13 | Palet konfigürasyonu | **0** | 2.4–2.7 |
| 14 | Boş / dolu şişe ağırlığı | **0** | 1.14, 1.15 |
| 15 | Etiket maliyeti (klişe + şişe başı) | **0** | 4.13 |
| 16 | Karton maliyeti + EXW'ye dahil mi | **1** (yalnızca "dahil" beyanı) | 3.18e |
| 17 | Numune politikası | **0** | 7.1–7.5 |
| 18 | **Bize ayrılabilir** yıllık kapasite | **0** | 3.12, 8.3 |
| 19 | Menşe ispat belgesi tipi | **0** | 6.1 |
| 20 | Türkiye'ye ihracat geçmişi | **0** — hiçbiri Türkiye'yi listelemiyor | 6.6 |
| 21 | Marka / reçete / artwork IP sahipliği | **0** | 4.9 |

**Yalnızca Model A'da, yalnızca RFQ ile:** münhasırlık koşulları (5.4), münhasırlık
için hacim taahhüdü (5.5), pazarlama/listeleme desteği (5.6), **ithalatçıya
markup tavanı (5.7)**, fesih ve stok (5.8), marka tescili (5.9), fiyat revizyon
mekanizması (5.10).

### 3.B — Diğer açık sorular

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| OQ-451 | Harland fiyatının **para birimi** | Kaynakta yalnızca "$" | **CRITICAL** | RFQ 3.1/3.13 |
| OQ-452 | 7 Model A markasının Türkiye'de temsilcisi | İki yönlü kesişim | **CRITICAL** | T-464 |
| OQ-453 | Hiçbir tedarikçi için gerçek EXW/FOB | Dış iletişim bu turda yasaktı | **CRITICAL** | RFQ Dalga 1, 2–3 hafta |
| OQ-454 | Interbrosa MOQ'su bugün hâlâ 3.000 mü | Site HTTP 503 | HIGH | E-posta/telefon |
| OQ-455 | Havuzda vade veren tedarikçi var mı | Tek doğrulanan şart peşin | HIGH | RFQ 3.8–3.10 |
| OQ-456 | Côtes de Gascogne'un fiyat seviyesi | Bölgesel birim değer verisi yok | HIGH | RFQ 3.1 / FranceAgriMer |
| OQ-464 | **Paletli** konteyner doluluğu | Yalnızca paletsiz rakam bulundu | HIGH | T-461 |
| OQ-457 | Zidela'nın kendi kurumsal beyanları | Site yaş duvarı arkasında | MEDIUM | Telefon / fuar profili |
| OQ-458 | Parras private label yapıyor mu | Çıkarım var, kanıt yok | MEDIUM | RFQ 4.1 / Goanvi |
| OQ-459 | Bronco private label programı | Kurumsal sitede yok | MEDIUM | broncowine-trade.com |
| OQ-460 | Arjantin üretici seviyesi PL | Kaynak önceliği TIER A'ya verildi | MEDIUM | Wines of Argentina dizini |
| OQ-461 | LFE güncel kurumsal sitesi | HTTP 404 | LOW | Wines of Chile |
| OQ-462 | Cantine Sgarzi (IT) PL şartları | Sayfa iki denemede boş döndü | LOW | Yeniden deneme |
| OQ-463 | Purcari'nin şişe bazında hacmi | Gelir RON, hacim kırılımı yok | LOW | BVB faaliyet raporu |

Detay: `99-ops/_parts/acik-sorular-global-sourcing-kasifi-tur2.md`
**TUR 1'in `OQ-401`…`OQ-415`'inin tamamı açıktır**; dördü kısmen ilerledi.

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-461** | Incoterms® 2020 FOB = adı belirtilen yükleme limanı → **L1** (T4 / 2026-08-10) | Şarap sektörü kullanımı: FOB = ex-cellar üretici fiyatı → fiilen **L0** (T4, `EV-2026-08-10-468`) | Aynı üç harf, maliyet merdiveninin **iki farklı basamağını** adlandırıyor. Somut tetikleyici: tek yayınlanmış sayı sipariş büyüklüğüne göre L0 veya L1 oluyor | **OPEN** |
| **C-462** | MOQ 3.000–3.600 (3 üretici, T4) | MOQ 6.000 (2 üretici, T4) — ayrıca T5 agregatör 300–1.200 (`C-401`) | 20 kat makas; **charter'ın 5.000'lik pilotu tam ortaya düşüyor** → MOQ pilotu ne kesin mümkün ne kesin imkânsız kılıyor | **OPEN** |

**TUR 1'den devreden ve hâlâ açık olanlar:**

| conflict_id | TUR 2'de ne oldu |
|---|---|
| **C-401** | **AÇIK.** Doğrulanmış üst sınır 3.600 → 6.000 çıktı; makas **genişledi** |
| **C-402** | **AÇIK.** İki ABD private label sağlayıcısı daha bulundu, **hiçbiri Türkiye'ye ihracat kabiliyeti beyan etmedi** — çelişki derinleşti |
| **C-403** | **AÇIK.** `EV-2026-08-10-463` "Central Valley" ayağını **dolaylı** destekliyor, **çözmüyor** |

Detay: `99-ops/_parts/celiskiler-global-sourcing-kasifi-tur2.md`
**Hiçbiri sessizce çözülmemiştir.**

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| tedarikci.yaml | `fiyat.exw_per_sise` | **null** | — | **UNKNOWN** | — |
| tedarikci.yaml | `fiyat.fob_per_sise` | **null** | — | **UNKNOWN** | — |
| tedarikci.yaml | `fiyat.quote_type` | `NONE_YET` | — | FACT | — |
| tedarikci.yaml | `risk.alternatif_tedarikci_sayisi` | **0** | adet | FACT | — |
| tedarikci.yaml | `…tur2_bulgulari.havuz_buyuklugu.aday_tedarikci_sayisi` | 26 | adet | FACT | EV-451…EV-471 |
| tedarikci.yaml | `…havuz_buyuklugu.oncelik_dagilimi` | A=7, B=10, C=9 | — | FACT | — |
| tedarikci.yaml | `…havuz_buyuklugu.is_modeli_dagilimi` | PL=17, EB=7, İkisi=1, UNK=1 | — | FACT | — |
| tedarikci.yaml | `…private_label_moq_TUR2_GENISLEME` | 3000–6000 | şişe/SKU | **ESTIMATE** | EV-2026-08-10-471 |
| tedarikci.yaml | `…yayinlanmis_katalog_fiyati_TEK_GOZLEM` | 2.85+/5.00+/8.50+ | **para birimi UNKNOWN**/şişe | **ESTIMATE** | EV-2026-08-10-451 |
| tedarikci.yaml | `…odeme_sarti_TEK_GOZLEM` | %50+%50 peşin | — | FACT | EV-2026-08-10-452 |
| tedarikci.yaml | `…konteyner_doluluk_TEK_GOZLEM` | 14112 (paletsiz) | şişe/20ft | FACT | EV-2026-08-10-452 |
| tedarikci.yaml | `…model_A_somut_marka_adaylari` | 7 | marka grubu | FACT | EV-456,-457,-458,-459,-461,-462 |
| tedarikci.yaml | `…urun_eslesmesi_dogrulanmis` | 2 | eşleşme | FACT | EV-2026-08-10-464, -459 |
| tedarikci.yaml | `…negatif_bulgular` | 4 | bulgu | FACT/UNKNOWN | EV-466,-469,-467,-464 |
| tedarikci.yaml | `…rfq_ile_ogrenilebilecek_alanlar` | 21 | alan | FACT | — |

**evidence_id'si olmayan hiçbir sayı modele girmemiştir.**

> ### `finans-fizibilite`'ye üç bağlayıcı uyarı
> 1. **TUR 1.5'te T-902 ile düzeltilen katman etiketlerine DOKUNULMADI.**
>    `duyarlilik_sinirlari_KARISIK_KATMAN`, `ihracat_ort_birim_degeri_EUR_per_litre`
>    ve `SENSITIVITY_BOUNDS_ONLY` çiti aynen duruyor.
> 2. **`tur2_bulgulari` bloğu bir fiyat girdisi DEĞİLDİR.** Yayınlanmış katalog
>    fiyatı `SENSITIVITY_BOUNDS_ONLY` çitinin içindedir. Duyarlılıkta kullanılırsa
>    **her çıktıda** üç uyarı birlikte yazılmak zorundadır: *para birimi UNKNOWN ·
>    katman belirsiz (L0 veya L1) · etiket hariç.* **İki para birimi okuması
>    (AUD / USD) ayrı ayrı gösterilir, ortalama alınmaz.**
> 3. **Model bu turda da fiyat çıktısı üretmemelidir.** `exw`/`fob` `null`'dır.

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `gumruk-vergi-uzmani` | Havuza **Moldova + Romanya + Bulgaristan** aynı grup içinde girdi (Purcari); ayrıca Yeni Zelanda. "STA var/yok" kontrolü genişledi | Aynı tedarikçiden hangi tesisten yüklendiği **belge tipini değiştirebilir** (T-462) |
| `gumruk-vergi-uzmani` | Doğrulanan tek ödeme şartı **tamamen sevkiyat öncesi peşin**; havuzda vade veren tedarikçi yok | "Peşin" senaryosu havuzun **varsayılanı** olabilir → T-404'ün pratik önemi arttı (T-463) |
| `gumruk-vergi-uzmani` | **"FOB" iki farklı katmana işaret ediyor** (`EV-2026-08-10-468`) | Gümrük kıymeti matrahı yanlış katmanla kurulursa baştan hatalı |
| `navlun-lojistik-uzmani` | **İlk konteyner doluluk rakamı:** 14.112 şişe/20ft, **paletsiz** | T-402'nin ilk veri noktası; paletli rakam UNKNOWN (T-461) |
| `navlun-lojistik-uzmani` | **MOQ konteyneri doldurmuyor** (6.000/14.112 = %42); pilot hacimler konteyner altında | Pilotta LCL/groupage kaçınılmaz görünüyor → birim navlun yapısal olarak farklı |
| `navlun-lojistik-uzmani` | Havuzda **karayolu erişimli tek menşe Moldova** (+ grubun RO/BG tesisleri) | TUR 1'in "ucuz olan aynı zamanda yakın" sezgiye aykırı bulgusu somutlaştı |
| `mevzuat-ruhsat-uzmani` | Bir üretici **kendi gümrük antreposunu** işletiyor (Cantina Danese) | Türkçe arka etiket menşede uygulanabiliyorsa bu kabiliyet **tedarikçi seçim kriteri** olur (T-468) |
| `mevzuat-ruhsat-uzmani` | Menşe ülke lisans belgeleri farklı formatlarda (NZ Off Licence, ZA DAFF) | RFQ 6.5'in menşeye göre daraltılması gerekebilir |
| `turkiye-pazar-kasifi` | **7 somut Model A markası** — hepsinin TR temsilci durumu UNKNOWN | **Model A'nın uygulanabilirliğini tek başına belirler** (T-464) |
| `turkiye-pazar-kasifi` | O'Neill'in ana tesisi **Parlier/Central Valley** | `C-403`'ün "Central Valley" ayağını **dolaylı** destekler, çözmez |
| `turkiye-pazar-kasifi` | **26 tedarikçinin hiçbiri Türkiye'yi ihracat pazarı olarak listelemiyor** | 17,85 m litrelik bir pazara üretici düzeyinde tek görünür bağ yok → yoğunlaşmış ithalatçı yapısı **hipotezi** |
| `kanal-marj-uzmani` | San Valero **aynı üretim tabanında** hem kendi markasını hem private label üretiyor | İki modelin kanal ekonomisi **aynı maliyet tabanında** karşılaştırılabilir (T-465) |
| `kanal-marj-uzmani` | Viña Albali "gıda perakende kanalının en çok satan İspanyol markası" | Model A'da hangi markanın hangi kanala kurgulandığı listeleme müzakeresini değiştirir |
| `finans-fizibilite` | `exw`/`fob` **hâlâ null**; tek yayınlanmış fiyat para birimi bilinmediği için çiti aşamıyor | Model bu turda da fiyat çıktısı üretmemeli (T-466) |
| `finans-fizibilite` | Ödeme peşin → tedarikçi vadesi **0**, `peak_cash_requirement` büyür | Nakit modelinin en kötü senaryo ucu |
| `finans-fizibilite` | **Pilot havuzu ~%40 daraltıyor** (5 üreticinin 3'ü) | 5.000 vs 10.000 şişe fiyat farkının kaynağı |
| `seytanin-avukati` | Kendi işime karşı **6 maddelik cephane** bıraktım | `capraz-ipuclari` §7 (İP-469…İP-474) |

Tam liste: `99-ops/_parts/capraz-ipuclari-global-sourcing-kasifi-tur2.md`

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| **T-461** | `navlun-lojistik-uzmani` | 14.112 şişe/20ft **paletsiz**; paletli kaç? Pilot hacimde LCL/groupage mi gerekir? | HIGH | OPEN |
| **T-462** | `gumruk-vergi-uzmani` | Yeni menşeler (MD + RO + BG aynı grupta; NZ) — STA var mı, hangi belge grubunda? | HIGH | OPEN |
| **T-463** | `gumruk-vergi-uzmani` | Tam peşin ödeme KKDF'yi doğurur mu? (T-404'ün somutlaşmış hâli) | MEDIUM | OPEN |
| **T-464** | `turkiye-pazar-kasifi` | **7 Model A markasının Türkiye'de ithalatçısı var mı?** | HIGH | OPEN |
| **T-465** | `kanal-marj-uzmani` | Üreticinin markup/yeniden satış fiyatı tavanı chain retail ile uyumlu mu? | MEDIUM | OPEN |
| **T-466** | `finans-fizibilite` | Tek yayınlanmış fiyat **modele giremez**; exw/fob null kalmalı | **CRITICAL** | OPEN |
| **T-467** | `yatirim-komitesi-baskani` | G2'yi açacak eylem (RFQ gönderimi) **izin/zamanlama** kararı gerektiriyor | HIGH | OPEN |
| **T-468** | `mevzuat-ruhsat-uzmani` | Menşede yapılabilecek etiketleme/belgeleme tedarikçi seçim kriteri olur mu? | MEDIUM | OPEN |

**Kapanan ticket:** yok (bu ajan bu turda hiçbir ticket'a cevap vermedi).

**T-466 CRITICAL'dır** ve CLAUDE.md §5 uyarınca açıkken `finans-fizibilite`
çıktısı `APPROVED` olamaz. Bu bilinçlidir: iki tur sonra bulunan ilk fiyat
benzeri sayı, modele sızma baskısı en yüksek olan sayıdır.

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| EV-2026-08-10-467 (Interbrosa erişilebilirlik) | **30d** | 2026-09-09 |
| EV-2026-08-10-451, -452, -453, -454, -455, -460, -463, -464, -466, -469, -470, -471 | 90d | 2026-11-08 |
| EV-2026-08-10-456, -457, -458, -459, -461, -462, -465 | 180d | 2027-02-06 |
| EV-2026-08-10-468 (FOB terminolojisi) | 1y | 2027-08-10 |

**En kısa TTL 30 gündür** ve bir **erişilebilirlik** kaydına aittir — bu doğrudur,
çünkü bir sitenin 503 vermesi geçici olabilir ve yeniden denenmelidir.

Üretici beyanlarına 90 gün verilmiştir: üreticiler MOQ, fiyat kademesi ve ürün
yelpazesini **sezon başında** değiştirebilir. `EV-2026-08-10-451` (fiyat) için
90 gün **cömert** olabilir; teklif geldiğinde teklifin geçerlilik tarihi kartın
`ttl`'i olur ve bu kartı `SUPERSEDE` eder.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Harland'ın yayınladığı fiyatın USD olduğunun ortaya çıkması — ve daha kötüsü,
bu fiyatın entry seviyesi için sektörde temsili olduğunun anlaşılması.**

Neden bu tek bulgu: Bu raporun en çok atıfta bulunulacak sayısı `$2.85`'tir.
Ben onu "para birimi bilinmiyor" diye çitledim, ama insan okuru çiti değil,
sayıyı hatırlar. Eğer USD ise, 750 ml şişe için FOB **2,85 USD**, Türkiye'ye
2025'te giren en ucuz menşelerin **CIF** birim değerlerinin (1,85–2,40 USD/750 ml,
`EV-2026-08-09-405`) **üstündedir** — yani navlun **eklenmeden önce** bile
tavanı aşıyor demektir.

Bu doğruysa şu sonuç çıkar: **Avustralya'dan bu segmentte tedarik matematiksel
olarak imkânsızdır** ve Harland'ı A önceliğe koymam bir hatadır. Ben onu A'ya
"en çok bilinmeyeni kapatıyor" diye koydum — **bilgi değeri yüksek diye**, ticari
uygunluk kanıtı olduğu için değil. Bu ayrım rapor boyunca korunmuştur ama
sıralamanın kendisi bu ayrımı **görsel olarak silmektedir**.

İkinci sırada: **`EV-2026-08-09-405`'in birim yorumunun yanlış çıkması.**
TUR 1 §9.1'de işaretlediğim bu kırılganlık **hâlâ kapanmamıştır** — Comtrade
`qtyUnitCode=7` alanını birincil kaynaktan teyit etmedim ve bu turda da etmedim.
Bu rapordaki her "L2 CIF" atfı o yoruma dayanıyor.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"Havuzu 11'den 26'ya çıkarmak ilerlemedir" varsayımı. Muhtemelen değil.**

`risk.alternatif_tedarikci_sayisi` iki turdur **0**'dır ve bu turda da 0 kaldı.
26 tedarikçinin **26'sından da fiyat alınmadı.** Yaptığım şey aday sayısını
2,4 kat artırmaktır — ve aday sayısı, karar veren bir büyüklük değildir.

Daha rahatsız edici olan şu: havuzu büyütmek **belirsizliği artırdı.**
TUR 1'de doğrulanmış MOQ aralığı 3.000–3.600 idi ve pilot uyumlu görünüyordu.
TUR 2'de aralık 3.000–6.000 oldu ve pilot uyumu **koşullu** hale geldi. Yani
daha fazla veri, **daha net değil, daha bulanık** bir tablo üretti. Bu normaldir
(küçük n'de dar aralık yanıltıcıdır), ama "ilerleme" diye sunulması yanıltıcı olur.

**İkinci kırılgan varsayım:** A/B/C kriterlerimi (K1–K5) ben yazdım, ben uyguladım
ve hiçbirine ağırlık vermedim. "Ağırlık vermemek tarafsızlıktır" diye
gerekçelendirdim — ama gerçek neden **ağırlık verecek verimin olmamasıdır.**
Ağırlıksız beş kriter, sonucu fiilen "kaç boyutta veri buldum"a indirger.
Yani **sıralamam tedarikçinin kalitesini değil, şeffaflığını ödüllendiriyor.**
Şeffaf ama pahalı bir tedarikçi A'ya çıkıyor; sessiz ama ucuz olan C'de kalıyor.

### 9.3 Hangi kaynağıma en az güveniyorum?

Üçü, güven sırasının en altında:

1. **`EV-2026-08-10-454` (Zidela).** Üreticinin **kendi sitesi okunamadı** (yaş
   doğrulama duvarı); tüm bilgi bir üçüncü taraf sektör dizininden geldi.
   "Ayda 2 milyon şişe" iddiası hiçbir bağımsız kaynakla doğrulanmadı ve dizin
   kaydının güncelleme tarihi bilinmiyor. Bunu yine de B önceliğe koydum çünkü
   "value for money private label" konumlandırması segment tanımıyla en doğrudan
   örtüşen ifadeydi — **yani zayıf kaynağı çekici olduğu için tuttum.** Bu bir
   seçim yanlılığıdır ve burada itiraf ediyorum.
2. **`EV-2026-08-10-461` (San Valero private label beyanı).** Bir sektör
   yayınındaki röportajdan geliyor, **firmanın kendi kanalından değil**, ve
   yayının tarihi bile bilinmiyor. Buna rağmen bu firmayı **A önceliğe** koydum
   ve gerekçem "ikili aday olması" idi — ama ikili adaylığın **yarısı** (private
   label) tam da en zayıf kaynağa dayanıyor. Yani A önceliğin gerekçesi ile
   kanıtın gücü **ters orantılı.**
3. **`EV-2026-08-10-457` (Parras) ve `EV-2026-08-10-456` (Vidigal).** İkisi de
   fuar/basın profillerinden; Parras'ın ciro rakamı **2020 tarihli** bir haberden.
   Altı yıllık bir ciro rakamını 2026 raporuna koymak, güncel gibi okunma riski
   taşıyor — kartta işaretledim, tabloda görünmüyor.

Ayrıca genel olarak: **26 kaydın 26'sı da T4'tür.** Bu doğaldır (tedarikçi verisi
tanım gereği T4'tür ve charter bunu meşru sayar), ama tek bir T1/T2/T3 çapraz
doğrulaması yoktur. Sektör dernek verileri (Wines of Chile, Wines of Argentina,
Winesofportugal) kullanılabilirdi ve kullanılmadı.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlış çıkan | Değişen karar |
|---|---|
| **Harland fiyatı USD** | **Avustralya elenir** ve daha önemlisi: 750 ml FOB'un 2,85 USD civarında olduğu bir dünyada, Türkiye'ye giren en ucuz CIF'ler (1,85–2,40 USD/750 ml) ile **çelişki** doğar → ya benchmark segmenti yanlış anlaşılmıştır ya fiyat sınıfı temsili değildir. `finans-fizibilite`'nin duyarlılık **üst sınırı** kayar |
| **MOQ'lar gerçekte 3×** (`C-462`) | Düşük MOQ alternatifi **5'ten 0'a** iner. 5.000 ve 10.000 şişelik senaryolar private label'da **imkânsız** hale gelir → `IMPORT PILOT` → `HOLD`/`TEST`. Model A'ya (mevcut markadan küçük parti) doğru zorunlu kayma |
| **7 Model A markasının hepsinin TR ithalatçısı var** (T-464) | **Model A fiilen kapanır.** İki modeli eşit değerlendirme hedefi kanıtla imkânsızlaşır ve karar **zorunlu olarak** Model B'ye kayar — bu kez arama yanlılığından değil, kanıttan. Başkanın bunu kararda açıkça ayırması gerekir |
| **Konteyner doluluğu paletli yüklemede çok daha düşük** (T-461) | Pilot hacimlerde birim navlun beklenenden yüksek çıkar; `peak_cash_requirement` ve break-even hacmi yukarı kayar |
| **Peşin ödeme KKDF'yi doğuruyor** (T-463) | Havuzun **varsayılan** ödeme yapısı vergi yükü ekler; ters modelin ödeyebileceği max EXW **düşer** |
| **Côtes de Gascogne fiyatı Fransa ortalamasında** | Ürün eşleşmesi en güçlü aday (Plaimont) elenir; "Colombard-Chardonnay" hedefi ya Güney Afrika'ya ya Kaliforniya'ya kayar — ikisinin de Türkiye hattı zayıf |

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| # | Ne | Kim | Nasıl | Süre |
|---|---|---|---|---|
| 1 | **Harland fiyatının para birimi** | `global-sourcing-kasifi` | Tek satırlık e-posta veya firmanın başka sayfasında para birimi beyanı — **dış iletişim izni gerekir** (T-467) | 1–3 gün (izin sonrası) |
| 2 | **Gerçek EXW/FOB + MOQ + ödeme (≥5 tedarikçi)** | `global-sourcing-kasifi` | RFQ v2.1, Dalga 1 (7 A öncelikli hedef), hedef ≥5 cevap → **G2'yi açan tek eylem** | 2–3 hafta + 1 hafta takip |
| 3 | **7 Model A markasının TR temsilci durumu** | `turkiye-pazar-kasifi` | Raf gözlemi + TADAB yetkili dağıtım firmaları listesi + marka×ithalatçı çaprazlaması (T-464) | 1–2 hafta |
| 4 | **Menşe belgesi grubu** (MD/RO/BG/NZ dahil) | `gumruk-vergi-uzmani` | T-401 + T-462 → sonra RFQ 6.1 daraltılır | ? |
| 5 | **Paletli konteyner doluluğu** | `navlun-lojistik-uzmani` | T-461 + RFQ 2.4–2.9 ambalaj verisi | 1 hafta + RFQ |
| 6 | **Comtrade birim kodu teyidi** *(TUR 1'den devir, hâlâ yapılmadı)* | `global-sourcing-kasifi` | UN Comtrade birim kodu referans tablosunun birincil kaynaktan okunması | 1 gün |
| 7 | **Arjantin üretici tabanı** | `global-sourcing-kasifi` | Wines of Argentina / Bodegas de Argentina üye dizinleri | 2–3 gün |
| 8 | **Bağımsız kriter denetimi** | `seytanin-avukati` | K1–K5 kriterlerinin ve A/B/C atamalarının, sonuca göre geriye dönük ayarlanıp ayarlanmadığının denetlenmesi | 1 gün |

**1, 2 ve 3 numaralı doğrulamalar tamamlanmadan bu ajan bir tedarikçi veya ülke
tavsiyesi vermemelidir — ve bu turda da vermemiştir.**
`A` önceliği bir tavsiye değil, bir **RFQ gönderim sırasıdır.**
