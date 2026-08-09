# BENCHMARK

Bu dosya projenin çıkış noktası olan raf gözlemlerini kaydeder.

> **UYARI:** Aşağıdaki fiyatlar *gözlem olarak* doğrudur (fotoğraftan okunmuştur).
> Ancak bu fiyatların **hangi fiyat katmanına** (L7 / L8) ve **KDV dahil/hariç**
> durumuna karşılık geldiği **DOĞRULANMAMIŞTIR**.
> Bkz. `99-ops/acik-sorular.md` → **OPEN QUESTION #001**

---

## TUR 1 GÜNCELLEMESİ (2026-08-09) — OQ-001 `PARTIALLY_RESOLVED`

`turkiye-pazar-kasifi` TUR 1'de OQ-001'i **kısmen** kapattı. Aşağıdaki
tablolardaki `UNKNOWN` alanların bir kısmı artık kanıtlıdır, bir kısmı
hâlâ açıktır. **Tablolar tarihsel kayıt olarak değiştirilmeden bırakılmıştır**;
güncel durum budur:

| Alan | TUR 1 sonrası durum | evidence_id |
|------|---------------------|-------------|
| KDV durumu | **KDV DAHİL** (Metro broşürlerinde her fiyatın yanında `KDV'li`) | `EV-2026-08-09-503`, `-504`, `-505`, `-506` |
| Tüketici fiyatı mı | **EVET** — Metro bireysel müşteriye ücretsiz günlük kartla açık | `EV-2026-08-09-505` |
| Profesyonel fiyatı mı | **EVET, aynı anda** — Metro'da tek fiyat | `EV-2026-08-09-505`, `-507`, `-508` |
| Fiyat katmanı | **`L8_METRO_CASH_CARRY`** — zincir market L8'i DEĞİL; bakkal/HoReCa için aynı anda L7-proxy | `EV-2026-08-09-507` |
| Promosyon durumu | **HÂLÂ UNKNOWN** — `T-504` (CRITICAL) | — |
| Zincir market tüketici fiyatı (gerçek L8) | **HÂLÂ UNKNOWN** — alkol online satılamadığı için alınamadı | `EV-2026-08-09-511` |

### Kurucu hipotez çürüdü

Bu dosyanın "NEDEN BU KADAR ÖNEMLİ" bölümündeki
*"Metro etiketlerinde KDV hariç profesyonel fiyat ile KDV dahil fiyat
birlikte gösterilebilir"* varsayımı, incelenen Metro Türkiye materyalinde
**karşılığını bulmamıştır.** Etiketteki ikinci sayı KDV hariç fiyat değil,
**birim fiyattır** (kg/L/adet).

### Model kullanım kuralı — güncellenmiş öneri

`finans-fizibilite` benchmark'ı hâlâ **tek sayı olarak kullanamaz**, ancak
senaryo ağırlıkları değişmiştir:

| Senaryo | Tanım | TUR 1 sonrası konum |
|---------|-------|---------------------|
| BM_A | 599,90 TL = KDV **dahil** | **BASE CASE** (kanıtlı) |
| BM_B | 599,90 TL = KDV **hariç** | SENSITIVITY (kanıtsız, ama elenmedi) |
| BM_C | 599,90 TL = **promosyonlu** fiyat | YENİ — OQ-001'in kapanmayan ayağı |
| BM_D | Zincir market L8 > Metro L8 | YENİ — katman ayrımı |

> Bu bir **öneri**dir. Senaryo setini onaylamak `yatirim-komitesi-baskani`'na aittir.

---

## BENCHMARK 1 — İLK BENCHMARK

| Alan | Değer |
|------|-------|
| Ürün | Gold Country California Colombard-Chardonnay |
| Hasat yılı (vintage) | 2023 |
| Menşe | California, ABD |
| Hacim | 750 ml |
| Kanal | Metro Türkiye |
| Gözlem tarihi | 09.08.2026 |
| Etiket fiyatı | **599,90 TL** |
| ABV | UNKNOWN |
| KDV durumu | **UNKNOWN** |
| Fiyat katmanı (L7/L8) | **UNKNOWN** |
| Promosyon durumu | UNKNOWN |
| Şehir / mağaza | UNKNOWN |
| status | `FACT_FROM_PHOTO` |
| evidence_id | TBD (TUR 1'de açılacak) |

---

## BENCHMARK 2 — KOMŞU BENCHMARK

| Alan | Değer |
|------|-------|
| Ürün | Central Creek (beyaz şarap) |
| Menşe | Avustralya |
| Hacim | 750 ml civarı / fotoğraftaki SKU |
| Kanal | Metro Türkiye (aynı gözlem) |
| Gözlem tarihi | 09.08.2026 |
| Etiket fiyatı | **649,90 TL** |
| ABV | UNKNOWN |
| Hasat yılı | UNKNOWN |
| KDV durumu | **UNKNOWN** |
| Fiyat katmanı (L7/L8) | **UNKNOWN** |
| Promosyon durumu | UNKNOWN |
| status | `FACT_FROM_PHOTO` |
| evidence_id | TBD (TUR 1'de açılacak) |

---

## `FACT_FROM_PHOTO` NE DEMEK, NE DEMEK DEĞİL

**Demek olan:** Bu rakam bir fotoğrafta gerçekten görülmüştür. Uydurulmamıştır.

**Demek OLMAYAN:**
- Bu rakamın tüketici raf fiyatı (L8) olduğu
- Bu rakamın KDV dahil olduğu
- Bu rakamın normal (promosyonsuz) fiyat olduğu
- Bu rakamın Türkiye genelini temsil ettiği
- Bu rakamın segment ortalaması olduğu

---

## NEDEN BU KADAR ÖNEMLİ

Metro bir **cash & carry** formatıdır. Bu formatta etiketlerde
**KDV hariç profesyonel fiyat** ile **KDV dahil fiyat** birlikte
gösterilebilir. Hangisinin okunduğu doğrulanmazsa:

- Ters model (`target shelf price → max EXW/FOB`) **yanlış hedefle** çalışır.
- KDV oranı kadar (yaklaşık) bir sapma, tüm fiyat merdivenini kaydırır.
- Bu sapma **doğrudan tedarikçiye ödeyebileceğimiz maksimum fiyata** yansır —
  yani projenin en kritik çıktısını bozar.

Ayrıca Metro'daki fiyat bir **cash & carry / profesyonel** fiyatıysa, zincir
market tüketici rafındaki fiyat bundan **farklı** olacaktır. Bu durumda
599,90 TL bir L8 değil, L7'ye yakın bir sayı olabilir.

---

## MODEL KULLANIM KURALI

OPEN QUESTION #001 kapanana kadar `finans-fizibilite` bu benchmark'ı
**tek bir sayı olarak kullanamaz**. Model, benchmark'ı:

- **Senaryo A:** 599,90 TL = KDV **dahil**
- **Senaryo B:** 599,90 TL = KDV **hariç**

olmak üzere **iki ayrı senaryoda** çalıştırır ve aradaki farkı raporlar.

---

## DOĞRULAMA GÖREVİ

Sorumlu: `turkiye-pazar-kasifi`
Öncelik: **1 (en yüksek)**
Bkz. `99-ops/acik-sorular.md` → OPEN QUESTION #001
