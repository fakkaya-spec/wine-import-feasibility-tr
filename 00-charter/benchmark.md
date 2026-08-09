# BENCHMARK

Bu dosya projenin çıkış noktası olan raf gözlemlerini kaydeder.

> **UYARI:** Aşağıdaki fiyatlar *gözlem olarak* doğrudur (fotoğraftan okunmuştur).
> Ancak bu fiyatların **hangi fiyat katmanına** (L7 / L8) ve **KDV dahil/hariç**
> durumuna karşılık geldiği **DOĞRULANMAMIŞTIR**.
> Bkz. `99-ops/acik-sorular.md` → **OPEN QUESTION #001**

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
