# MASTER COMMERCIAL INPUT TABLE — TUR 2 KONSOLİDASYONU

```yaml
belge:                  master-commercial-input-table
yazan:                  yatirim-komitesi-baskani
tarih:                  2026-08-10
tur:                    TUR 2 SONU — KONSOLIDASYON
amac:                   HESAPLANABILIRLIK ENVANTERI
karar_iceriyor_mu:      false
arastirma_yapildi_mi:   false      # CLAUDE.md §1.16 — baskan arastirma yapmaz
yeni_kanit_uretildi_mi: false      # hicbir yeni evidence karti acilmadi
yeni_sayi_uretildi_mi:  false      # hicbir hucre baskan tarafindan tahmin edilmedi
satir_sayisi:           11
model_ready_dagilimi:   "YES 0 · PARTIAL 1 · NO 10"
```

> ## BU TABLONUN AMACI
>
> Bu bir **hazırlık tablosu değildir**, bir **hesaplanabilirlik envanteridir.**
>
> Tek sorusu şudur: **TUR 3'te `finans-fizibilite` neyi gerçekten hesaplayabilir?**
> Tablo, o soruya satır satır cevap verir. Boş hücre bir eksiklik itirafıdır,
> doldurulacak bir yer değildir.
>
> **Bu belge bir tedarikçi seçimi, bir öneri veya bir yatırım kararı DEĞİLDİR.**
> `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` / `SCALE` kararlarının hiçbiri burada
> verilmemiştir ve verilemez. Nihai karar **TUR 6**'da,
> `90-karar/karar-gunlugu.md`'de verilir. **O dosyaya bu turda DOKUNULMAMIŞTIR.**

---

## 0. TABLOYU OKUMADAN ÖNCE — SEKİZ BAĞLAYICI KURAL

| # | Kural |
|---|---|
| **T1** | **Her hücre ya kanıtlı bir değerdir ya `UNKNOWN`'dır.** Ara statü yoktur. "Muhtemelen", "yaklaşık", "genelde" hiçbir hücrede geçmez. |
| **T2** | **Başkan hiçbir hücreyi doldurmamıştır.** Her değer bir ajanın kendi raporundan/`yaml`'ından **birebir** aktarılmıştır. Değiştirilmiş, yuvarlanmış veya birleştirilmiş tek sayı yoktur. |
| **T3** | **Para birimleri TOPLANMAMIŞTIR ve toplanamaz.** `makro.yaml → fx` **`null`**'dır. USD / EUR / TRY sütunları ayrı durur (`T-311`, `T-912`). |
| **T4** | **Katman disiplini:** `EXW` = **L0**, `FOB` = **L1**. Kaynağında Incoterm + yer/liman açıkça yazılmayan hiçbir fiyat L0 veya L1 diye etiketlenmemiştir (`C-461` — bu turda **çözüldü**, aşağıda §5). |
| **T5** | **Navlun iki modda ayrı gösterilir.** LCL = **gerçek, tarihli, geçerlilik süreli kotasyon** (`ttl: 6d`, **2026-08-16'da STALE**). FCL = **hiçbir rotada yoktur** (`C-311`, CRITICAL). Aynı hücrede karıştırılamaz. |
| **T6** | **Kanal marjı hücrelerinin tamamı `ASSUMPTION` / `SENSITIVITY_ONLY`'dir.** Tek kanıtlı çapa (Migros %24,31) **şarap değildir** ve **tüm kategori** karmasıdır. |
| **T7** | **`599,90 TL` bu tabloda hedef fiyat olarak KULLANILMAMIŞTIR** (`pazar.yaml → K5/K6`, `M3`). O bir **Metro cash & carry gözlemidir**, `l8_chain_retail` değildir ve `l8_chain_retail` **`null`**'dır. |
| **T8** | **Tedarikçi seviyesinde değişmeyen alanlar tekrarlanmaz.** Gümrük oranı **menşe** seviyesindedir (`mense-tarife-eslemesi.md` §0); kanal koşulları **proje** seviyesindedir. Bunlar §3 ve §4'te bir kez verilir. Tedarikçi satırında tekrarlamak **yanlış hassasiyet** üretir. |

**17 kolon tek bir tabloya sığmaz ve sığdırılırsa okunmaz.** Tablo üç bloğa
bölünmüştür (**A** kimlik/tedarik · **B** maliyet zinciri · **C** kanal/hazırlık);
satır kimlikleri (`R1`…`R10`) üç blokta **aynıdır**.

---

## 1. `MODEL_READY` — KRİTER ÖNCE TANIMLANDI, SONRA UYGULANDI

### 1.1 Zincirin halkaları

Bir satırın hesaplanabilir olması için `L0/L1 → L8` zincirinin **sekiz halkasının
sekizi de** kanıtlı olmalıdır:

| # | Halka | Katman | Sahibi |
|---|---|---|---|
| **H1** | **Fiyat çapası** — EXW veya FOB; **para birimi belirli**, **Incoterm + yer/liman belirli** | L0 / L1 | `global-sourcing-kasifi` |
| **H2** | MOQ (SKU **ve** konteyner biriminde) | — | `global-sourcing-kasifi` |
| **H3** | Gümrük vergisi oranı + menşe ispat belgesi | L2→L4 | `gumruk-vergi-uzmani` |
| **H4** | Navlun — **rotası eşleşmiş**, moduna göre (LCL/FCL) gerçek kotasyon | L1→L2 | `navlun-lojistik-uzmani` |
| **H5** | Diğer lojistik — menşe + varış local charge'ları, antrepo, bandrolleme operasyonu | L2→L3→L5 | `navlun-lojistik-uzmani` |
| **H6** | Lead time — üretim **ve** transit | — | `global-sourcing-kasifi` + `navlun-lojistik-uzmani` |
| **H7** | Ödeme şartı — vade günü (KKDF tetikleyicisi) | L0 nakit | `global-sourcing-kasifi` |
| **H8** | Kanal — `l8_chain_retail`, `m_retail`, `d`, `f`, vade | L6→L8 | `turkiye-pazar-kasifi` + `kanal-marj-uzmani` |

**Ayrıca zincirin tamamı için bir çapraz koşul:** `fx` (`makro.yaml`) — üç para
birimini birbirine bağlayan tek alan. **`null`**'dır.

### 1.2 Kriter

| Değer | Koşul |
|---|---|
| **`YES`** | H1–H8'in **hiçbirinde** `UNKNOWN` yok **ve** `fx` dolu. Zincir uçtan uca hesaplanır. |
| **`PARTIAL`** | `evidence_id`'si olan bir **fiyat çapası vardır** (nitelenmiş olsa bile, en azından `SENSITIVITY_ONLY` biçiminde kullanılabilir) **ancak** H2–H8'den **en az biri** `UNKNOWN`. |
| **`NO`** | **L0'da da L1'de de hiçbir sayı yoktur.** Zincir **başlatılamaz**. |

> **`PARTIAL` bir iyi haber değildir.** Yalnızca "zincirin ilk halkasında bir sayı
> var" demektir. `PARTIAL` bir satır da modele giremez.

---

## 2. BLOK A — KİMLİK, İŞ MODELİ, MOQ, FİYAT ÇAPASI

| # | supplier | country | product | business_model | MOQ | **EXW (L0)** | **FOB (L1)** | evidence_id |
|---|---|---|---|---|---|---|---|---|
| **R1** | Harland Wine Company Pty Ltd | **AU** | Still, 750 ml, şişelenmiş; entry/mid/premium kademe. **Beyaz çeşit `UNKNOWN`** | PRIVATE_LABEL (B) | **6.000 şişe/şarap** (500×12 veya 1000×6) `FACT` | **`2.85+` / 5.00+ / 8.50+** — ⚠ **PARA BİRİMİ `UNKNOWN`** (kaynakta yalnız "$"), MOQ siparişinde *ex factory* → **L0 olabilir**. `ESTIMATE`, `SENSITIVITY_ONLY`. **Etiket baskısı HARİÇ.** | **Aynı sayı**, tam 20ft konteynerde *FOB* beyanı → **L1 olabilir**. Liman **adı yok**. `C-461` | `EV-2026-08-10-451`, `-452` |
| **R2** | Cantina Danese s.r.l. | **IT** | Still, şişelenmiş; İtalyan apelasyonları. **Beyaz portföy `UNKNOWN`** | PRIVATE_LABEL (B) | **6.000 şişe/SKU** `FACT` | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-10-453` |
| **R3** | Interbrosa Family Wines | **ES** | Şişelenmiş + BIB; vegan/organik/helal opsiyon | PRIVATE_LABEL (B) | **3.000 şişe** (4 palet) `FACT` ⚠ site 2026-08-10'da **HTTP 503**, teyit edilemedi | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-09-408`; `EV-2026-08-10-467` |
| **R4** | The Wine Factory (SARL) | **FR** | Still; AOP Bordeaux / Corbières / Côtes de Provence; Sauvignon, Viognier | PRIVATE_LABEL (B) | **3.600 şişe** `FACT` | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-09-410` |
| **R5** | Corta Hojas Export Wine | **CL** | Still + BIB + dökme; **Sauvignon Blanc + Chardonnay** — ürün tanımıyla **birebir eşleşme** `FACT` | PRIVATE_LABEL (B) | **`UNKNOWN`** — 2026-08-10'da yeniden okundu, hâlâ yayınlanmamış (**negatif bulgu**) | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-10-464` |
| **R6a** | Bodegas San Valero | **ES** | Still + cava; DOP Cariñena; marka: Particular | EXISTING_BRAND (A) | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-10-461` |
| **R6b** | Bodegas San Valero | **ES** | aynı üretim tabanı | PRIVATE_LABEL (B) ⚠ beyan **3. taraf yayından** | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-10-461` |
| **R7** | Casa Santos Lima | **PT** | Still; Quinta da Espiga, Setencostas, Palha-Canas | EXISTING_BRAND (A) | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-09-418` |
| **R8** | Vidigal Wines S.A. | **PT** | Still + dessert; amiral marka **Porta 6**. **Beyaz portföy `UNKNOWN`** | EXISTING_BRAND (A) | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-10-456` |
| **R9** | Plaimont (Vignerons en Gascogne) | **FR** | IGP Côtes de Gascogne **Colombard-Chardonnay** — havuzun **en güçlü ürün eşleşmesi** `FACT` | EXISTING_BRAND (A); PL kabiliyeti `UNKNOWN` | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-10-459` |
| **R10** | Purcari Wineries Group | **MD** (+RO/BG) | Still; Purcari, Bostavan, Crama Ceptura, Domeniile Cuza | EXISTING_BRAND (A) | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | `EV-2026-08-10-462` |

### 2.1 Fiyat sütunlarının tek cümlelik özeti

**26 tedarikçinin 26'sından da teklif alınmamıştır.** Havuzda **tek** yayınlanmış
şişe başı fiyat vardır (R1) ve o da **para birimi bilinmediği ve katmanı belirsiz
olduğu için modele giremez** — `tedarikci.yaml → fiyat.exw_per_sise` ve
`fiyat.fob_per_sise` **`null`** kalmıştır (**`T-466`, CRITICAL, OPEN**).

`tedarikci.yaml → risk.alternatif_tedarikci_sayisi` **iki turdur `0`**'dır.

---

## 3. BLOK B — MALİYET ZİNCİRİ (L1 → L5)

### 3.1 `customs_rate` — **menşe seviyesindedir, tedarikçi seviyesinde değil**

| Menşe | Satırlar | `applicable_customs_rate` | Rejim | Belge | tier | evidence_id |
|---|---|---|---|---|---|---|
| **ES / IT / PT / FR** | R2, R3, R4, R6a, R6b, R7, R8, R9 | **%50** ⚠ **KOŞULLU** | Türkiye-AB OKK **1/98** (tarım). **Gümrük Birliği 1/95 DEĞİL** | **EUR.1 (0302)** veya **Fatura Beyanı (0538)**. **A.TR GEÇERSİZ** | **T1** (oran) / T2 (belge) | `EV-2026-08-09-103`; `EV-2026-08-10-155`, `-158`, `-159` |
| **CL** | R5 | **%50** ⚠ **KOŞULLU** | Türkiye-Şili STA, I s. Liste dipnot (2) | EUR.1 / Fatura Beyanı · **çıkış ülkesi YALNIZCA ŞİLİ** | T1 (oran) / **T3** (belge) | `EV-2026-08-09-105`; `EV-2026-08-10-160`, `-164` |
| **AU** | R1 | **%70** | STA **YOK** | Tercihli belge **düzenlenemez** | **T1** | `EV-2026-08-09-104`; `EV-2026-08-10-152` |
| **MD** | R10 | **%70** | STA **VAR ama 2204.21'i KAPSAMAZ** | — | **T1** | `EV-2026-08-10-165` |
| *(aynı grubun RO/BG tesisleri)* | R10 alt | **%50** | AB üyesi → 1/98 | EUR.1 / Fatura Beyanı | T1 | `EV-2026-08-10-165` |

> **"%50" KOŞULLU BİR ORANDIR.** Belge ibraz edilemez veya doğrudan nakliyat
> sağlanamazsa **otomatik olarak %70** uygulanır (`EV-2026-08-10-157`).
> Sayısal kaldıraç: **CIF = 100 TL/şişe'de +24,00 TL/şişe** — nominal 20 puanlık
> farktan büyüktür, çünkü gümrük vergisi KDV matrahına da girer.
> `belge_ibraz_edildi` bir **senaryo değişkenidir**, bir vergi verisi değildir.

### 3.2 `freight_per_bottle` — **LCL gerçek, FCL YOK**

`⚠ TÜM LCL KOTASYONLARININ GEÇERLİLİĞİ 2026-08-16'DA DOLAR (`ttl: 6d`).`

| # | Menşe limanı | **LCL base ocean (USD/şişe)** | Transit / aktarma | **FCL base ocean** | Rota eşleşmesi | evidence_id |
|---|---|---|---|---|---|---|
| **R1** | Melbourne (AU) | **0,529 – 0,551** (A) / 1,111 – 1,133 (B) | 36–56 gün · **1 aktarma (Singapur, tropik)** | **`UNKNOWN`** | ✅ eşleşiyor | `EV-2026-08-10-311` |
| **R2** | İtalya (Genova/La Spezia/Livorno/Napoli) | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | ⚠ **test edilen limanların tamamı Tirrenya**; tedarikçi **Veneto (Roncà, VR)** → Adriyatik/Ro-Ro test edilmedi (**`T-916`**) | `EV-2026-08-10-304` |
| **R3 · R6a · R6b** | Valencia / Barcelona (ES) | **0,274 – 0,297** (A) / 0,360 – 0,383 (B) | **4 gün · 0 AKTARMA (direkt)** | **300 – 1.200 USD/20DV** `ESTIMATE` `LOW` — **`C-311`, 4 kat band** | ✅ eşleşiyor | `EV-2026-08-10-301`, `-302`, `-322`, `-324` |
| **R4 · R9** | Marsilya (FR) | 0,636 – 0,675 | 12–15 gün · **1 aktarma (Hamburg/Antwerp)** | **`UNKNOWN`** | ❌ **EŞLEŞMİYOR** — R4 Bordeaux(Gornac)+Languedoc(Valros), R9 Saint-Mont/Gaskonya → **Atlantik/Güneybatı**. Marsilya bu iki tedarikçinin çapası **değildir** (**`T-915`**) | `EV-2026-08-10-305` |
| **R5** | San Antonio (CL) | **0,432 – 0,454** (via **Barcelona**, 43 g) / 0,595 – 0,618 (via Hamburg, 49 g) | 43–49 gün · 1 aktarma | **`UNKNOWN`** | ⚠⚠ **VERGİ ÇAKIŞMASI** — bkz. §3.2.1 | `EV-2026-08-10-306` |
| **R7 · R8** | Lizbon (PT) | 0,423 – 0,445 | ~4 gün ⚠ **iç tutarsız** (Barcelona aktarmalı ama 4 gün yazıyor; transit `LOW` confidence) | **`UNKNOWN`** | ✅ eşleşiyor | `EV-2026-08-10-303` |
| **R10** | Moldova | **`UNKNOWN`** — hiç test edilmedi | **`UNKNOWN`** | **`UNKNOWN`** | ⚠ havuzdaki **tek karayolu erişimli menşe**; deniz kotasyon mantığı uygulanamaz | — |

> **USD/şişe türetmesi:** `USD/CBM ÷ 449 şişe/m³` (`EV-2026-08-09-323`).
> Bu satırlar **yalnızca base ocean freight'tir** — origin ve destination local
> charge'lar **dahil değildir**.

#### 3.2.1 ⚠ R5 (Şili) — bu satırda "bilinen navlun" ile "bilinen tarife" AYNI ANDA DOĞRU OLMAYABİLİR

En ucuz Şili LCL rotası **Barcelona aktarmalıdır** (`EV-2026-08-10-306`).
`SIL` (Türkiye-Şili STA) rejiminde BİLGE'nin kabul ettiği **çıkış ülkesi
yalnızca Şili'dir** (`EV-2026-08-10-160`).

Aktarmanın (tek konşimento altında transshipment) çıkış ülkesi kontrolünü bozup
bozmadığı **`UNKNOWN`**'dır. Bozuyorsa R5'in tarife hücresi **%50 değil %70**
olur ve fark **CIF 100 TL'de +24 TL/şişe**'dir — yani navlundaki tüm avantajdan
büyüktür.

**Bu, iki ajanın bulgularının kesiştiği ama hiçbirinin görmediği noktadır.**
`T-163` bu soruyu LCL rotaları bilinmeden önce açmıştı. Yeni ticket: **`T-914`**.
**Bu risk yalnızca Şili'ye özgüdür:** ES direkt (0 aktarma); PT/FR aktarmaları
AB içi (ATRM çıkış ülkesi listesinde var); AU/MD zaten %70.

### 3.3 `other_logistics_per_bottle` — üç para birimi, TOPLANMAMIŞ

| Kalem | Değer | Birim | Kim için biliniyor | status / tier | evidence_id |
|---|---|---|---|---|---|
| **Origin THC (THO)** | **287 EUR** (Algeciras 277; reefer 355) | /konteyner | **YALNIZCA İSPANYA** (R3, R6a, R6b) | `FACT` / **T3** | `EV-2026-08-10-313` |
| **Origin B/L (EDI)** | **62 EUR** (manuel SI 104) | /konteyner | **YALNIZCA İSPANYA** | `FACT` / T3 | `EV-2026-08-10-314` |
| **Origin opsiyonlar** (VGM/RHO/**FQS 115**) | 0 – 205 EUR | /konteyner | **YALNIZCA İSPANYA** | `FACT` / T3 | `EV-2026-08-10-314` |
| **ORIGIN TOPLAM** | **349 – 554 EUR** | /konteyner | **YALNIZCA İSPANYA** — diğer 6 menşe **`UNKNOWN`** (`T-312`) | `FACT` / T3 | — |
| **Destination THD** | 192 (Ambarlı) · 165 (İzmir) · 261–298 (Mersin) · 185 (Gemlik) | USD/konteyner | **TÜM SATIRLAR** | `FACT` / T3 | `EV-2026-08-10-315` |
| **Drop-off** | 50 | USD/konteyner | tüm satırlar | `FACT` / T3 | `EV-2026-08-10-316` |
| **Terminal ardiye (5 gün)** | 90 – 195 (20') · 145 – 300 (40HC) | USD | tüm satırlar | `FACT` / T4 | `EV-2026-08-10-317`, `-318` |
| **Free time** | **0 gün** (muhafazakâr) | gün | terminale bağlı — **`C-312` bu turda ÇÖZÜLDÜ (KAPSAM)**, §5 | `FACT` (SafiPort için) | `EV-2026-08-10-317` |
| **Devanning** | 257 – 275 (20') · 332 – 365 (40HC) | USD | tüm satırlar | `FACT` / T4 | `EV-2026-08-10-317`, `-319` |
| **Ordino** | **2.000 – 5.000** | TRY | tüm satırlar | `ESTIMATE` / T4 | `EV-2026-08-10-325` |
| **Gümrük müşavirliği** (ANT-1 + İTH-2) | **6.020** | TRY | tüm satırlar | `FACT` / T3 | `EV-2026-08-09-342` |
| **İç nakliye (İstanbul içi)** | **10.000 – 15.000** (20') · 12.500 – 18.000 (40HC) | TRY | tüm satırlar | `FACT` / T4 | `EV-2026-08-10-326` |
| **X-ray** | 0 – 3.000 | TRY | tüm satırlar | `ESTIMATE` / T4 | `EV-2026-08-10-325` |
| **Sigorta** | **%0,3 – 0,6** (CIF+%10) | oran | tüm satırlar — **Türk kotasyonu `UNKNOWN`** | `ESTIMATE` | `EV-2026-08-09-360` |
| **Bandrol** | **2,36073** (KDV hariç) — **peşin, satıştan önce** | TRY/şişe | tüm satırlar | `FACT` / T1 | `EV-2026-08-09-213` |
| **TADAB hizmet bedeli** | **0,1587** | TRY/şişe | tüm satırlar | `FACT` | *(`T-203` — hangi matraha gireceği `UNKNOWN`)* |
| **Antrepo depolama** | 0,35 EUR/palet/gün · **min 7 gün** | — | tüm satırlar | `ESTIMATE` / **T5, LOW** | `EV-2026-08-10-327` |
| **Antrepo elleçleme / yeniden paletleme** | **`UNKNOWN`** | — | — | — | `T-314` |
| **Bandrolleme operasyon birim maliyeti** | **`UNKNOWN`** | — | — | — | `T-314` |
| **Bandrolleme kapasitesi (şişe/gün)** | **`UNKNOWN`** | — | — | — | `T-314` |
| **Cam kırılma / fire oranı** | **`UNKNOWN`** | — | — | — | `T-314` |
| **Antrepoda bekleme süresi** | **`UNKNOWN`** | gün | — | — | **`T-301` (CRITICAL)** |
| **Thermal liner birim maliyeti** | **`UNKNOWN`** | — | R1/R5 için kritik (tropik/ekvator geçişi) | — | `T-304` |

**İspanya rotası için şişe başı toplam** (L1→L3, 5.000 şişelik pilot,
`EV-2026-08-10-329`):

| Mod | USD/şişe | EUR/şişe | TRY/şişe |
|---|---|---|---|
| **LCL** | 0,326 – 0,632 | **0** | 2,60 – 4,20 |
| **20DV FCL** | 0,181 – 0,456 | 0,070 – 0,111 | 3,60 – 5,80 |

> ⛔ **BU ÜÇ SÜTUN TOPLANMAMIŞTIR VE TOPLANAMAZ** (`makro.yaml → fx = null`).
> **İspanya, üç bacağın üçü de bilinen TEK menşedir.** Diğer altı menşede
> EUR bacağı (origin charges) **`UNKNOWN`**'dır.

### 3.4 `lead_time` ve `payment_terms`

| # | **lead_time — üretim** | **lead_time — transit** | **payment_terms** | KKDF sonucu |
|---|---|---|---|---|
| **R1** | **4–5 hafta şişeleme + 1 hafta paketleme ≈ 6 hafta** `FACT` | 36–56 gün | **%50 sipariş peşin + %50 şişeleme sonrası = TAMAMI SEVKİYAT ÖNCESİ** `FACT` | **KKDF = 0** (peşin) `FACT` T1 |
| **R2** | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | `UNKNOWN` |
| **R3** | **`UNKNOWN`** | 4 gün | **`UNKNOWN`** | `UNKNOWN` |
| **R4** | **28–42 gün (ödeme sonrası)** `FACT` | 12–15 gün ⚠ rota eşleşmiyor | **`UNKNOWN`** — *"ödeme sonrası üretim"* peşin **ipucudur**, şart olarak doğrulanmadı | `UNKNOWN` |
| **R5** | **`UNKNOWN`** | 43–49 gün | **`UNKNOWN`** | `UNKNOWN` |
| **R6a · R6b** | **`UNKNOWN`** | 4 gün | **`UNKNOWN`** | `UNKNOWN` |
| **R7 · R8** | **`UNKNOWN`** | ~4 gün ⚠ | **`UNKNOWN`** | `UNKNOWN` |
| **R9** | **`UNKNOWN`** | ⚠ rota eşleşmiyor | **`UNKNOWN`** | `UNKNOWN` |
| **R10** | **`UNKNOWN`** | **`UNKNOWN`** | **`UNKNOWN`** | `UNKNOWN` |

> **n = 1.** Havuzda ödeme şartını yayınlayan **tek** üretici vardır ve
> **tedarikçi vadesi 0**'dır. Bu `kanal.yaml`/`tedarikci.yaml`'da
> `odeme.vade_gun` alanını **doldurmaz** — tek gözlem bir dağılım değildir.
> Yön uyarısı: peşin ödeme KKDF doğurmaz (**lehte**) ama
> `peak_cash_requirement`'ı büyütür (**aleyhte**). İki etki **zıt yönlüdür.**

---

## 4. BLOK C — KANAL, MARJ SENARYOSU, KANIT KAPSAMI, HAZIRLIK

### 4.1 `channel` ve `channel_margin_scenario` — **TÜM SATIRLAR İÇİN AYNI**

Kanal koşulları tedarikçiye göre değişmez; **proje seviyesindedir** (kural T8).

| Kanal | Nokta sayısı (2020) | `m` BASE | Bant | Vade BASE | Vade bandı | status |
|---|---|---|---|---|---|---|
| **A — Chain retail** (öncelik 1) | MK: **tabloda YOK** (merkezî alım) | **%25** | 18 / 25 / 35 | **60 gün** | 45 / 60 / 90 / **120** | **`ASSUMPTION` · `SENSITIVITY_ONLY`** |
| **B — Tekel / bağımsız** (öncelik 2) | **48.956** `FACT` T2 | **%18** | 12 / 18 / 25 | **30 gün** | 0 / 30 / 60 / 90 | **`ASSUMPTION` · `SENSITIVITY_ONLY`** |
| **C — HoReCa** (öncelik 3) | **29.218** `FACT` T2 | **3,0×** *(çarpan)* | 2,0 / 3,0 / 5,0× | **45 gün** | 15 / 45 / 90 / 120 | **`ASSUMPTION` · `SENSITIVITY_ONLY`** |

**Marj disiplini (`M1` — dört nitelik olmadan alıntılanamaz):**
`m_retail` = **MARGIN on selling price** · **BRÜT** · **KDV HARİÇ** · **L7 → L8**.

| Alan | Değer | status | Not |
|---|---|---|---|
| `l8_chain_retail` | **`null`** | **`UNKNOWN`** | **`T-603`** — merdivenin tepesi yok |
| `L8_METRO_CASH_CARRY` | 599,90 / 649,90 TL | `FACT` (okuma) · `MEDIUM` (temsil) | **K5: hedef fiyat olarak kullanılamaz.** Promosyon durumu **`UNKNOWN`** (`T-504`) |
| Tek kanıtlı marj çapası | **%24,31** (Migros 2025 konsolide, markup %32,12) | `FACT` (Migros) → **`ESTIMATE` (şarap)** | **Tüm kategori** karması; **alkol resmî marj analizinin kapsamı DIŞI**; **tedarikçiden alınan bedelleri İÇERİR** |
| `d` — geri akan bedeller | 3 / **8** / 18 % | **`ASSUMPTION`** | **Kanıtlı çapası YOKTUR** — tek dayanak **kalem sayısıdır** (en az 6, alkolde ismen kanıtlı) |
| `f` — listeleme bedeli | **`UNKNOWN`** | — | Güncel kamu kaynağı **yok**; tek iz **2004 tarihli T5** → **modele giremez** |
| Dış distribütör marjı | **`UNKNOWN`** | — | **Ne T4 ne T5 — hiçbir kanıt yok.** A/B dağıtım kararı bunsuz verilemez |
| `t_kdv` | **%20** | `FACT` T2 | `EV-2026-08-09-118` |

**Taşıyıcı denklem** (`finans-fizibilite` bunu aynen kullanır):

```
L7_effective = L6 × (1 − d) − f_per_bottle
TERS:  L8_kdv_haric = L8_kdv_dahil / (1 + t_kdv)
       L7_effective = L8_kdv_haric × (1 − m_retail)
       L6           = (L7_effective + f_per_bottle) / (1 − d)
```

**Yapısal kısıt (kabul edilmiş, yeniden araştırılmayacak):** Perakendecinin bedel
karşılığı verebileceği **iki** hizmet grubundan biri (**tanıtım**) alkolde fiilen
satın alınamaz (`İP-2001` / `T-205` / `C-203` — `ACCEPTED BUSINESS CONSTRAINT`).
Geriye **yalnızca fiziksel raf/teşhir konumlandırması** kalır ve aynı anda
tüketiciye ulaşmanın **başka yolu yoktur**.

### 4.2 `evidence_coverage` · `confidence` · **`MODEL_READY`**

`H1`…`H8` = §1.1'deki zincir halkaları. ✅ kanıtlı · ⚠ kısmen/nitelenmiş · ❌ `UNKNOWN`.

| # | supplier | H1 fiyat | H2 MOQ | H3 vergi | H4 navlun | H5 diğer loj. | H6 lead | H7 ödeme | H8 kanal | **coverage** | confidence | **MODEL_READY** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **R1** | Harland (AU) | ⚠ | ✅ | ✅ | ⚠ | ⚠ | ✅ | ✅ | ❌ | **4 / 8** | MEDIUM *(kaynak)* / **fiyat KULLANILAMAZ** | **`PARTIAL`** |
| **R2** | Cantina Danese (IT) | ❌ | ✅ | ✅ | ❌ | ⚠ | ❌ | ❌ | ❌ | **2 / 8** | MEDIUM | **`NO`** |
| **R3** | Interbrosa (ES) | ❌ | ⚠ | ✅ | ⚠ | ✅ | ❌ | ❌ | ❌ | **2 / 8** | MEDIUM | **`NO`** |
| **R4** | The Wine Factory (FR) | ❌ | ✅ | ✅ | ❌ | ⚠ | ⚠ | ❌ | ❌ | **2 / 8** | MEDIUM | **`NO`** |
| **R5** | Corta Hojas (CL) | ❌ | ❌ | ⚠ | ⚠ | ⚠ | ❌ | ❌ | ❌ | **0 / 8** | MEDIUM | **`NO`** |
| **R6a** | San Valero — Model A (ES) | ❌ | ❌ | ✅ | ⚠ | ✅ | ❌ | ❌ | ❌ | **2 / 8** | LOW | **`NO`** |
| **R6b** | San Valero — Model B (ES) | ❌ | ❌ | ✅ | ⚠ | ✅ | ❌ | ❌ | ❌ | **2 / 8** | **LOW** *(PL beyanı 3. taraftan)* | **`NO`** |
| **R7** | Casa Santos Lima (PT) | ❌ | ❌ | ✅ | ⚠ | ⚠ | ❌ | ❌ | ❌ | **1 / 8** | MEDIUM | **`NO`** |
| **R8** | Vidigal (PT) | ❌ | ❌ | ✅ | ⚠ | ⚠ | ❌ | ❌ | ❌ | **1 / 8** | LOW | **`NO`** |
| **R9** | Plaimont (FR) | ❌ | ❌ | ✅ | ❌ | ⚠ | ❌ | ❌ | ❌ | **1 / 8** | MEDIUM | **`NO`** |
| **R10** | Purcari (MD) | ❌ | ❌ | ✅ | ❌ | ⚠ | ❌ | ❌ | ❌ | **1 / 8** | MEDIUM | **`NO`** |

```
MODEL_READY DAĞILIMI:   YES 0   ·   PARTIAL 1   ·   NO 10
H8 (kanal) SÜTUNU:      11 satırın 11'inde  ❌   — tek istisna yok
H1 (fiyat) SÜTUNU:      10 satırda ❌, 1 satırda ⚠ — hiçbir satırda ✅ yok
```

---

## 5. HESAPLANABİLİRLİK DEĞERLENDİRMESİ

### 5.1 Dağılım TUR 3 için ne anlama geliyor

**`YES` sayısı sıfırdır ve bu bir sürpriz değil, tasarımın doğruladığı sonuçtur.**

TUR 2 bir **ticari doğrulama** turuydu ve dış iletişim yasaktı. Fiyat, MOQ teyidi,
ödeme şartı ve lead time yalnızca **gerçek RFQ** ile öğrenilebilir
(`global-sourcing-kasifi` bunu **21 alanlık** bir listeyle kanıtladı: 26
tedarikçinin **26'sında** FOB fiyatı, para birimi, teklif geçerliliği ve palet
konfigürasyonu açık kaynakta **bulunamamıştır**). Bu alanlarda daha fazla
masabaşı araştırma **kaynak israfıdır** — ajanın kendi ifadesiyle.

Üç sonuç:

1. **`finans-fizibilite` TUR 3'te tek bir tedarikçi için ileri model
   çalıştıramaz.** İleri model (L0 → L8) **11 satırın 11'inde** ilk halkada
   kırılır.
2. **`H8` (kanal) sütunu 11/11 `❌`'dir.** Bu, tedarikçi sayısı 26'dan 260'a
   çıksa da değişmez. Kanal, **tedarikçiden bağımsız** bir blokerdir ve
   `MODEL_READY`'yi tedarikçi tarafından **kurtarmak matematiksel olarak
   imkânsızdır.**
3. **Kanıt kapsamı ile ticari uygunluk TERS orantılıdır.** Havuzun en yüksek
   kapsamlı satırı (**R1, 4/8**) aynı zamanda **%70 tarifeli**, **Türkiye hattı
   fiilen olmayan** (44.674 L/2025), **en uzun ve termal olarak en kötü rotaya**
   sahip satırdır. `global-sourcing-kasifi` bunu kendisi itiraf etmiştir:
   *"sıralamam tedarikçinin kalitesini değil, şeffaflığını ödüllendiriyor."*
   **Bu tablo o çarpıklığı gizlemez, görünür kılar.** `R1`'in `PARTIAL` olması
   bir tavsiye değildir.

### 5.2 Kaldıraç analizi — hangi tek eksik alan en çok satırı taşır?

**Sorunun literal cevabı: HİÇBİRİ.**
Tek bir alanın doldurulması **hiçbir satırı `YES`'e taşımaz** — çünkü `H8`
(kanal) sütunu 11/11 `❌`'dir ve `fx` çapraz koşulu `null`'dır. `YES`'e ulaşmak
için **en az üç bağımsız alanın birlikte** kapanması gerekir.

Bunu gizlemeden, kaldıraç sıralaması:

| Sıra | Eksik alan | Kaç hücreyi değiştirir | Maliyeti | Nasıl kapanır | Tek başına `YES` üretir mi |
|---|---|---|---|---|---|
| **1** | **EXW/FOB + para birimi + Incoterm/liman** | **10 satırı `NO` → `PARTIAL`**; 1 satırı ⚠ → ✅. Tablodaki **en büyük tek hareket** | **Yüksek** — dış iletişim izni + 2–3 hafta + takip | RFQ v2.1 Dalga 1 (`T-467`) | **HAYIR** |
| **2** | **`l8_chain_retail`** | 11/11 `H8`'in **tepe çapasını** açar; **ters modeli çalıştırılabilir kılar** | **En düşük** — 1 kişi, 1–2 hafta, ≈0 TL | Fiziksel mağaza turu ≥2 şehir / ≥20 SKU / etiket fotoğrafı (`T-603`) | **HAYIR** — ama TUR 3'ün **tek gerçek çıktısını** açar |
| **3** | **`fx` (usd_try, eur_try, eur_usd + kur tarihi)** | Üç para birimini birbirine bağlar; **her parasal çıktının ön koşulu** | **Neredeyse sıfır** — tarihli, kanıtlı tek kur + duyarlılık bandı | `T-912` (yeni) + `T-911` (gümrük kuru, `gumruk-vergi-uzmani`) | **HAYIR** |
| **4** | **FCL navlunu** (`C-311`) | LCL/FCL kırılma bandının **genişliğinin TAMAMI** buradan geliyor (2.200–9.800 şişe) | Orta — 3 forwarder yazılı kotasyon | `T-304` (CRITICAL) | HAYIR |
| **5** | `d` + `f` (kanal bedelleri) | `L6`'yı kapatır; küçük hacim senaryolarını tek başına öldürebilir | Yüksek — gerçek zincir müzakeresi, 4–8 hafta | `T-604` | HAYIR |

> ### KALDIRAÇ BULGUSU
> **En pahalı alan (#1, RFQ) ile en ucuz alan (#2, mağaza turu) aynı sırada
> DEĞİLDİR.** `l8_chain_retail` ve `fx`, birlikte **bir mağaza turu + bir kur
> kaydı** maliyetiyle, TUR 3'ün üretebileceği **tek karar-değerli çıktıyı**
> (ters model) açar. RFQ ise çok daha pahalıdır ve **tek başına hiçbir satırı
> `YES` yapmaz.**
>
> Bu, kaynak tahsisi açısından belirleyici bir asimetridir ve TUR 6'ya
> taşınmalıdır.

### 5.3 `finans-fizibilite` TUR 3'te NE HESAPLAYABİLİR

> **Kritik yapısal gözlem:** Ters modelin **büyük kısmı TL cinsindendir ve `fx`
> GEREKTİRMEZ.** `L8` (TL) → KDV (%20) → `L7` → `L6` → `L5` → `L4` → ÖTV
> (**maktu, TL, 53,4519 TL/şişe**) ve bandrol (**TL, 2,36073**) düşülür →
> geriye `CIF + GV` kalır ve `GV = CIF × oran` olduğundan **`CIF_TRY` doğrudan
> çözülür.** `fx` yalnızca **son iki adımda** (navlunun USD/EUR bacaklarını
> düşmek ve `FOB_TRY`'yi tedarikçi para birimine çevirmek) gerekir.
>
> Yani: **`fx` olmadan bile ters model `CIF_TRY`'ye kadar çalışır.**

| # | Hesaplanabilir | Neden | Ön koşul |
|---|---|---|---|
| **1** | **Vergi merdiveninin tamamı, bir `CIF` fonksiyonu olarak** — `GV(%50/%70) → ÖTV(maktu) → KDV(%20)`, matrah sırası ve sırası T1 ile doğrulanmış | `matrah_sirasi` bloğunun tamamı `FACT` | yok |
| **2** | **Birimsiz vergi kaldıraç oranları** — ör. belge riski = `CIF × 0,24`; %50↔%70 farkının KDV üzerinden çarpan etkisi | Oranlar `fx` gerektirmez | yok |
| **3** | **ÖTV'nin raf fiyatındaki yapısal ağırlığı** — 53,4519 TL/şişe, hedef fiyat **bandı** üzerinden yüzde olarak | ÖTV **TL** ve L8 **TL** — aynı para birimi | **K5**: tek fiyata kilitlenmek yasak, **bant** kullanılır |
| **4** | **TERS MODEL — hedef raf fiyatı bandından azami `CIF_TRY`** | §5.3 üstündeki TL-zinciri | `l8_chain_retail` (**`T-603`**) veya açıkça `ASSUMPTION` etiketli bir hedef bant |
| **5** | **Azami `CIF_TRY` → azami `FOB`** ve bunun gözlenen menşe CIF birim değerleriyle (MD 2,46 · ES 2,71 · CL 2,89 USD/l) karşılaştırılması — **"segment matematiksel olarak mümkün mü"** sorusunun ilk gerçek testi | Navlun bacağı düşülür | **`fx`** (`T-912`) + navlun bandı |
| **6** | **`peak_cash_requirement`'ın YAPISI ve zaman ekseni** — bandrol peşin · ÖTV+KDV gümrükte peşin · KDV mahsup gecikmesi · kanal vadesi 45/60/90/120 · tedarikçi vadesi 0 | Zamanlama kuralları `FACT` (`cash_tax_timing`) | tutar için `CIF` gerekir |
| **7** | **LCL/FCL kırılma noktası** ve bandın **hangi çelişkiden geldiği** ayrıştırması | ~5.900 şişe (2.200–9.800); bandın genişliğinin **tamamı `C-311`'den** | — |
| **8** | **Ölçek eğrisi** — şişe başı lojistik 5.000'de vs 100.000'de **3–4 kat** fark; **doğrusal değildir** | Oran hesabı | — |
| **9** | **Listeleme bedelinin hacme bölünme etkisi** — sabit bedel, değişken hacim → 5.000 vs 100.000'de **20 kat** | Yapısal | `f` tutarı `UNKNOWN` → yalnızca duyarlılık |
| **10** | **Kendi dağıtım kırılma noktası** — taban 40.214,03 TL/ay/kişi; 5.000 şişe/yıl'da **96,5 TL/şişe** (yalnızca 1 kişinin asgari ücreti) | TL-only | — |
| **11** | **Belge riski senaryosu** — `belge_ibraz_edildi = true/false` ekseni | `mense_tarife_eslemesi` + `senaryo_degiskenleri` | — |

### 5.4 `finans-fizibilite` TUR 3'te NE HESAPLAYAMAZ

| # | Hesaplanamaz | Kilitleyen |
|---|---|---|
| 1 | **Herhangi bir contribution margin / kâr / marj sayısı** | `exw`/`fob` **`null`** — **`T-466` (CRITICAL)** |
| 2 | **`L4` / `L5` landed cost'un MUTLAK değeri** | `CIF` yok |
| 3 | **Break-even hacim (TL)** | Birim katkı yok |
| 4 | **`peak_cash_requirement` TUTARI** | `CIF` + navlun + `fx` yok |
| 5 | **Tedarikçi veya menşe tavsiyesi** | Fiyat yok; sıralama **şeffaflığı** ödüllendiriyor (§5.1/3) |
| 6 | **LCL vs FCL fiyat kararı** | Fark **gürültü seviyesinde** (±0,05 vs ±0,15 USD bandı) **ve** FCL bandı 4 kat (`C-311`) |
| 7 | **`L6` / `L7` sayısal değeri** | `d`, `f`, `m_retail` — hepsi `ASSUMPTION`/`UNKNOWN` |
| 8 | **Model A ↔ Model B karşılaştırması** | İkisinin de fiyatı yok. **Tek ölçüm aracı R6a/R6b'ye tek RFQ göndermektir** |
| 9 | **2027+ ÖTV** | `model_hedef_tarihi` **`null`** (`OQ-002`, yatırımcı girdisi) + Yİ-ÜFE varsayımı yok |
| 10 | **Herhangi bir çok-para-birimli TOPLAM** | `fx` **`null`** — `T-311`, **`T-912`** |
| 11 | **Antrepo maliyeti ve ÖTV takvim riski** | Bekleme süresi **`UNKNOWN`** — **`T-301` (CRITICAL)** |
| 12 | **İtalya rotasının hiçbir maliyeti** | LCL **ve** FCL ikisi de `UNKNOWN` (`T-312`, **`T-916`**) |

### 5.5 Modelin **`UNKNOWN` DÖNMEK ZORUNDA OLDUĞU** çıktılar (CLAUDE.md §12, §15)

Aşağıdakiler bir **hata değil, tasarımın gereğidir**. Model bu çıktılarda sayı
üretirse **o çıktı geçersizdir**:

```
exw_per_sise · fob_per_sise · ve bunlara bağlı HER TÜREV
cif · landed_cost_L4 · importer_cost_L5 · L6 · L7 · l8_chain_retail
contribution_margin · break_even_hacim · peak_cash_requirement (tutar)
fx-bagimli HER TOPLAM
otv(t) — t > 2026-12-31 ve senaryolar.yaml'da acik ASSUMPTION yoksa
listeleme_bedeli (f) · distributor_marj_orani
kirilma_fire_orani · antrepo_bekleme_suresi
fcl_navlun (TEK DEGER olarak — yalnizca band)
italya_rotasi (tum kalemler)
```

### 5.6 TUR 3 için **BAĞLAYICI ÇALIŞTIRMA KURALLARI**

| # | Kural | Dayanak |
|---|---|---|
| **M-1** | **Çıktı en fazla `DRAFT` olabilir, `APPROVED` OLAMAZ.** | CLAUDE.md §5 — **5 açık CRITICAL ticket** |
| **M-2** | `exw`/`fob` **`null` kalır.** Harland fiyatı yalnızca `SENSITIVITY_ONLY` çitinin içinde, **her kullanımda üç uyarı birlikte** yazılarak (*para birimi UNKNOWN · katman belirsiz · etiket hariç*) ve **iki para birimi okuması (AUD/USD) AYRI AYRI**, **ortalama alınmadan** | `T-466` |
| **M-3** | **599,90 TL tek gerçek piyasa fiyatı olarak kullanılamaz.** İhlal edilirse `T-504`'ün `CRITICAL → HIGH` indirimi **geçersizdir** ve ticket derhal `CRITICAL`'a döner | `pazar.yaml` K5/K6 |
| **M-4** | **MOQ tek değere kilitlenemez.** SKU bazlı (3.000 / 3.600), SKU bazlı (6.000) ve konteyner bazlı **ayrı senaryo** | `C-401` + `C-462` |
| **M-5** | **Para birimleri toplanamaz.** USD/EUR/TRY ayrı taşınır; `fx` dolana kadar toplam **`UNKNOWN`** | `T-311`, `T-912` |
| **M-6** | **FCL bandının ortalaması alınamaz.** 300 ve 1.200 USD **ayrı ayrı** çalıştırılır | `C-311` |
| **M-7** | **ÖTV `otv_maktu_zaman_serisi`'nden okunur**, `matrah_sirasi[4].asgari_maktu_tutar` kısayolundan değil. Çelişirse **seri esastır** | `T-104`, `vergi.yaml → engine_yasak` |
| **M-8** | **Palet bandı korunur** (9–11 / 20–24). Tek değer seçmek **yasak** | Başkan direktifi, `C-301` |
| **M-9** | **Kanal marjı üç senaryo AYRI AYRI** çalıştırılır; BASE tek sonuç olarak sunulamaz | `T-602`, `kanal.yaml → SENSITIVITY_ONLY` |
| **M-10** | ⚠ **TAZELİK KAPISI:** Model **2026-08-16'dan sonra** çalıştırılırsa `EV-2026-08-10-301…311` (11 LCL kartı) **STALE**'dir ve navlun bacağı **`UNKNOWN`'a döner**. Bu, projedeki **en kısa ömürlü kanıt setidir** | `ttl: 6d`, `T-913` |

---

## 6. BU TABLONUN KENDİ ZAYIFLIKLARI (dürüstlük kaydı)

1. **`MODEL_READY` kriterini ben yazdım ve ben uyguladım.** Kriter §1'de
   **önce** tanımlanmış, sonra uygulanmıştır ve sonuca göre geriye dönük
   ayarlanmamıştır — ama bunu doğrulayacak bağımsız bir göz yoktur.
   `seytanin-avukati` TUR 4'te **önce bu kriteri** denetlemelidir.
2. **`R1`'in `PARTIAL` olması tartışmaya açıktır.** Para birimi bilinmeyen bir
   sayı, katı okumada bir sayı değildir; o okumada `R1` de `NO` olurdu ve tablo
   **11/11 `NO`** olurdu. `PARTIAL` verdim çünkü `NO` etiketi *"hiç veri yok"*
   ile *"bir kalifiye çapa var"* arasındaki farkı siler. **Karşı argüman
   geçerlidir ve burada yazılıdır.**
3. **`evidence_coverage` skoru sekiz halkayı eşit ağırlıklandırır.** Bu yanlıştır:
   `H1` (fiyat) tek başına diğer yedisinden daha belirleyicidir. Ağırlık
   vermedim çünkü ağırlık verecek verim yok — bu, `global-sourcing-kasifi`'nin
   kendi A/B/C kriterlerinde itiraf ettiği **aynı zayıflıktır** ve tabloda
   tekrarlanmaktadır.
4. **Tablo 26 tedarikçinin 11'ini içerir.** Kalan 15'i (B/C öncelikli) hiçbir
   `MODEL_READY` boyutunda daha iyi değildir — hepsinde `H1` `❌`'dir — ama
   **bakılmadı ile bakıldı-yok** ayrımı için bu belirtilmelidir.
5. **`H8` (kanal) sütununu tek bir sütuna sıkıştırdım.** Gerçekte beş ayrı alan
   (`l8`, `m_retail`, `d`, `f`, vade) vardır ve **hepsi ayrı ajanlarda**.
   Tek sütun, kanal blokerinin **büyüklüğünü küçük gösterir**.

---

## 7. BU BULGUYU NE ÇÜRÜTÜR?

*(Bu belge bir yatırım kararı içermez. Aşağıdaki soru bu tablonun tek hükmüne —
**"TUR 3'te ileri model çalıştırılamaz, ters model kısmen çalıştırılabilir"** —
ilişkindir.)*

### En güçlü tek çürütücü bulgu

**Türkiye'de bu segmentte fiilen ithalat yapan küçük bir oyuncunun gerçek maliyet
yapısı** — tek bir gerçekleşmiş ithalat beyannamesi + fatura seti.

Bu tek belge tabloyu **aynı anda dört yerden** çürütür:
- `H1`'i kapatır (gerçek CIF, gerçek Incoterm, gerçek para birimi),
- `H5`'i kapatır (antrepo, bandrolleme, elleçleme **gerçek** kalemleri —
  `T-314`'ün tamamı),
- `C-313`'ü kapatır (THD ↔ terminal kapı-çıkış çift sayımı bir faturada görünür),
- `H8`'in bir bacağını kapatır (`L6` fatura fiyatı).

Ve tablonun tezini tersine çevirir: **"masabaşı ile kapanmaz" dediğim alanların
çoğu, bir ithalatçı görüşmesiyle tek seferde kapanabilir.**
`turkiye-pazar-kasifi` TUR 2'de **4 ithalatçı grubunu isimlendirmiştir**
(Kavaklıdere, Karagözoğlu, Adco, Baron) — yani muhatap artık **anonim değildir.**
Bu, tablonun görmediği en ucuz kapanış yoludur ve **kayda geçirilmiştir.**

### İkinci en güçlü çürütücü (farklı hükmü hedefler)

**`l8_chain_retail`'in gerçekte 599,90'ın çok altında veya çok üstünde çıkması.**
Ters modelin **tepe çapası** budur. Eğer zincir market gerçek rafında bu segment
600–900 TL değil de örneğin 450–650 TL ise, azami `CIF_TRY` **maktu ÖTV sabit
kaldığı için orantısız biçimde** düşer — çünkü 53,4519 TL/şişe fiyattan
bağımsızdır ve düşük fiyatta **çok daha büyük bir yüzde** kaplar. Bu tek gözlem
§5.3'teki **11 hesaplanabilir çıktının 4'ünü** (madde 3, 4, 5 ve dolaylı olarak
6) yeniden kurar.

### Bu tablonun en kırılgan hükmü

**"`fx` olmadan ters model `CIF_TRY`'ye kadar çalışır" (§5.3).**
Kırılgan çünkü bu, KDV'nin **indirilebilir** olduğu ve dolayısıyla ekonomik
maliyet olmadığı sonucuna dayanır (`OQ-G01`, `EV-2026-08-10-101/-102/-103`).
O sonuç ise, **KDVK md.36 uyarınca çıkarılmış bir Cumhurbaşkanı Kararı
ARANMAMIŞ olması kaydıyla** geçerlidir (`OQ-G10`, `T-151`) — bunu
`gumruk-vergi-uzmani` kendisi işaretlemiştir. Böyle bir karar varsa KDV ekonomik
maliyet olur, TL zinciri değişir ve §5.3'ün 4. ve 5. maddeleri **yeniden
kurulmalıdır.** **G1'in en kırılgan yeri budur ve bu tablo ona dayanmaktadır.**

### Bu tablonun kör noktası

Tablo **var olan kanıtların envanteridir**; kanıtların **doğruluğunu test
etmez.** Eğer TUR 1/1.5/2'nin kanıt tabanı sistematik olarak hatalıysa
(örneğin `EV-2026-08-09-405`'in Comtrade birim kodu yorumu yanlışsa — ki
`global-sourcing-kasifi` bunu **iki turdur** kapatmadığını itiraf etmektedir),
bu tablo o hatayı **yakalayamaz**; yalnızca üzerine bir hazırlık etiketi yazar.
Panzehir **TUR 4**'tür: `seytanin-avukati` bu tabloyu değil, **altındaki kanıt
kartlarını** hedef almalıdır.
</content>
</invoke>
