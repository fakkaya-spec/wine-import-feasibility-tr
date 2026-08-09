---
description: TUR 4 — Kırmızı takım saldırısı, projeyi yanlışlama turu
---

# KIRMIZI TAKIM

Yürüten ajan: `seytanin-avukati`

## ÖN KOŞUL

TUR 3 (`/model-calistir`) tamamlanmış, model çıktısı `80-model/outputs/`
altında hazır olmalı.

## AMAÇ

Projeyi **doğrulamak değil, öldürmek.**
Diğer ajanların iyimser tarafta hata yaptığı varsayımıyla başla.
Ama saldırın da kanıtlı olsun — kanıtsız saldırı reddedilir.

## SALDIRI LİSTESİ (HEPSİ TARANIR)

1. Gizli maliyet — modelde satırı olmayan her kalem
2. Regülasyon şoku — ÖTV/maktu tutar artışı, gözetim, etiket/reklam kuralı
3. Kur şoku — TL değer kaybı, fiyat güncelleme gecikmesi
4. MOQ tuzağı — pilot hacim MOQ ile uyumlu mu
5. Yavaş stok — devir hızı, vintage eskimesi, ölü stok
6. Kanal gücü — listeleme, vade, iade dayatması, raf alamama
7. Supplier dependency — tek kaynak riski, kalite tutarsızlığı
8. Rekabet — mevcut ithalatçılar ve yerli üreticilerin tepkisi
9. Nakit akışı — ÖTV/KDV peşin, tahsilat geç; peak cash gerçek mi
10. İthalat riskleri — gecikme, demurrage, kıymet itirazı, bandrol darboğazı
11. **Modelde çift sayım** — aynı maliyet iki katmanda
12. Unutulan maliyet
13. **Yanlış benchmark** — 599,90 TL KDV hariç mi, Metro cash&carry mi,
    tek SKU'dan segment çıkarılabilir mi, promosyon muydu

## TICKET AÇ

Her önemli challenge için `99-ops/tickets/T-###.md`:

```
ticket_id: T-###
opened_by: seytanin-avukati
target_agent: <çözecek ajan>
claim: <ne iddia ediyorsun>
impact: CRITICAL | HIGH | MEDIUM | LOW
status: OPEN
resolution_evidence: <boş>
```

**`impact: CRITICAL` açık ticket varken finans modeli `APPROVED` olamaz.**
Ama her şeyi CRITICAL yapma — enflasyon kaldıracı öldürür.

## HER CHALLENGE İÇİN YAZ

1. İddia
2. Kanıt / gerekçe (evidence_id varsa)
3. Etki — model nerede ve ne kadar kırılır
4. **Bu saldırıyı ne çürütür** (dürüst ol)
5. Ticket ID

## ÇIKTI

- `90-karar/kirmizi-takim-raporu.md`
- `99-ops/tickets/T-###.md` dosyaları
- `99-ops/celiskiler.md` güncellemesi
- `_SABLON-ajan-raporu.md` formatında rapor

## SONRAKİ ADIM

TUR 5 — açılan ticket'lar hedef ajanlara gider, düzeltmeler yapılır.
