---
description: TUR 3 — Finans modelini kanıtlı girdilerle çalıştırır
---

# MODEL ÇALIŞTIR

Yürüten ajan: `finans-fizibilite`

## ÖN KOŞUL

1. TUR 1 ve TUR 2 tamamlanmış olmalı.
2. `/capraz-kontrol` çalıştırılmış olmalı.
3. `80-model/inputs/` altındaki YAML'larda **kritik** alanlar doldurulmuş olmalı.

Kritik girdi eksikse: **model çalışır ama `UNKNOWN` döner.** Uydurma yapılmaz.
Eksik girdi listesi ve sorumlu ajan raporlanır.

## ADIMLAR

### 1. Girdi denetimi
- `80-model/inputs/*.yaml` yüklenir.
- Her sayının `evidence_id` ve `status` alanı kontrol edilir.
- **evidence_id'si olmayan sayı modele girmez.**
- Status dağılımı raporlanır: kaç `FACT` / `ESTIMATE` / `ASSUMPTION` / `UNKNOWN`.

### 2. Vergi kilidi kontrolü
`80-model/inputs/vergi.yaml` içindeki oranlar A1 seviyesinde (T1/T2) doğrulanmış mı?
Doğrulanmamışsa vergi hesabı çalışmaz, `UNKNOWN` döner.
**Engine'de hiçbir oran hard-code edilmez.**

### 3. Matrah sırası
`30-vergi-gumruk/matrah-sirasi.md` → `80-model/engine/matrah_sirasi.py`
Vergi sırası bu dosyadan okunur, kodda sabitlenmez.

### 4. İleri model
`L0 EXW → L1 FOB → L2 CIF → L3 PRE-TAX LANDED → L4 POST-TAX LANDED
→ L5 IMPORTER COST → L6 IMPORTER SELLING → L7 RETAILER PURCHASE
→ L8 CONSUMER SHELF`

Her katman geçişinde hangi kalemin eklendiği satır satır gösterilir.

### 5. Ters model
`target shelf price (L8) → max ödenebilir EXW/FOB (L0/L1)`

Hedef raf fiyatı olarak benchmark kullanılır — **ama OPEN QUESTION #001
kapanmamışsa** benchmark hem KDV dahil hem KDV hariç varsayımıyla
**iki ayrı senaryo** olarak çalıştırılır ve fark gösterilir.

### 6. Hacim senaryoları
`5.000` · `10.000` · `25.000` · `50.000` · `100.000` şişe/yıl

Her hacim için: konteyner sayısı, MOQ uyumu, sabit maliyet dağılımı,
birim maliyet, contribution margin, nakit ihtiyacı.

### 7. Finansal metrikler
- sabit / değişken maliyet ayrımı
- gross margin, contribution margin
- break-even (adet ve TL)
- EBITDA katkısı
- işletme sermayesi, inventory turnover, inventory days
- cash conversion cycle
- **peak_cash_requirement**

### 8. KDV — iki perspektif (ZORUNLU)
- **A) ekonomik maliyet / indirilebilirlik**
- **B) nakit akışında fiili ödeme zamanı** (`cash_tax_timing`)

ÖTV için de ödeme anı ile tahsilat anı arasındaki gecikme modellenir.

### 9. Duyarlılık
`FX` · `freight` · `ÖTV` · `price`
Her biri için min/base/max ve tornado. Tek sayı sunulmaz.

### 10. Gate kontrolü
`impact: CRITICAL` açık ticket varsa çıktı **`DRAFT`**'tır, `APPROVED` olamaz.
Bu, çıktının en üstüne yazılır.

## ÇIKTI

- `80-model/outputs/` altına senaryo ve duyarlılık tabloları
- Çıktı başlığında: durum (`DRAFT`/`APPROVED`), kullanılan evidence_id listesi,
  status dağılımı, eksik girdiler
- `_SABLON-ajan-raporu.md` formatında rapor
