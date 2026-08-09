# KARAR EŞİKLERİ

> **Bu turda değer UYDURULMAZ.** Aşağıdaki eşikler bilinçli olarak `TBD`'dir.
> Eşikler yatırımcının risk iştahına aittir ve araştırmadan türetilemez.
> Model, eşikler `TBD` iken çalışabilir — ama **nihai karar** eşikler
> belirlenmeden verilemez. Başkan bu durumu kararında açıkça belirtir.

---

## 1. FİNANSAL EŞİKLER (TBD)

| Eşik | Değer | Birim | Kim belirler |
|------|-------|-------|--------------|
| `target_gross_margin_pct` | **TBD** | % | Yatırımcı |
| `minimum_contribution_try_per_bottle` | **TBD** | TL/şişe | Yatırımcı |
| `maximum_total_capital_try` | **TBD** | TL | Yatırımcı |
| `maximum_acceptable_pilot_loss_try` | **TBD** | TL | Yatırımcı |
| `target_inventory_days` | **TBD** | gün | Yatırımcı |
| `target_payback_months` | **TBD** | ay | Yatırımcı |

### Her eşiğin ne işe yaradığı

- **`target_gross_margin_pct`** — brüt marj hedefi. Modelin ürettiği marj bunun
  altındaysa senaryo elenir. *(Hangi katmanlar arası marj olduğu eşik
  belirlenirken netleştirilmeli: L5→L6 mı, L5→L8 mi?)*
- **`minimum_contribution_try_per_bottle`** — şişe başına minimum katkı payı.
  Sabit maliyetleri karşılamaya yetip yetmediğini test eder.
- **`maximum_total_capital_try`** — projeye konulabilecek toplam sermaye tavanı.
  `peak_cash_requirement` bunu aşıyorsa senaryo uygulanamaz.
- **`maximum_acceptable_pilot_loss_try`** — pilot başarısız olursa kabul
  edilebilir maksimum kayıp. IMPORT PILOT kararının büyüklüğünü belirler.
- **`target_inventory_days`** — hedef stok gün sayısı. Aşılırsa nakit kilitlenir.
- **`target_payback_months`** — geri ödeme süresi hedefi.

---

## 2. BAŞLANGIÇ ARAŞTIRMA TERCİHLERİ (BELİRLENDİ)

Bunlar eşik değil, **araştırma yönlendirmesidir.** Bu turda geçerlidir.

### `business_model_priority`

| Model | Öncelik |
|-------|---------|
| Existing brand distribution (mevcut marka distribütörlüğü) | **equal** |
| Private label (kendi markamız) | **equal** |

**İki model eşit önceliklidir.** `global-sourcing-kasifi` ikisini de eşit
derinlikte araştırır. Birini gerekçesiz öne çıkarmak yasaktır.

### `channel_priority`

| Sıra | Kanal |
|------|-------|
| 1 | **Chain retail** (zincir market) |
| 2 | **Independent retail / tekel** (bağımsız satış noktası) |
| 3 | **HoReCa** |

Bu sıralama araştırma derinliğini yönlendirir, kanalları elemez.
`kanal-marj-uzmani` üçünü de inceler, ama kaynağını bu sıraya göre ayırır.

### `scale_intent`

```
pilot economics first,
but test whether 50,000–100,000 bottles/year is scalable.
```

Yani:
- **Önce pilot ekonomisi** — küçük hacimde iş tutuyor mu?
- **Ama aynı anda** 50.000–100.000 şişe/yıl ölçeğinin sürdürülebilir olup
  olmadığı test edilir.
- `finans-fizibilite` her iki ucu da modellemek zorundadır
  (5.000 → 100.000 şişe senaryoları).

---

## 3. EŞİKLER BELİRLENMEDEN NE OLUR

| Faaliyet | Eşik `TBD` iken mümkün mü |
|----------|---------------------------|
| Araştırma (TUR 1–2) | ✅ Evet |
| Model kurulumu ve çalıştırılması (TUR 3) | ✅ Evet |
| Kırmızı takım (TUR 4) | ✅ Evet |
| Senaryo karşılaştırması | ✅ Evet |
| **Nihai yatırım kararı (TUR 6)** | ⚠️ Eksik — başkan bunu kararda belirtir |

Başkan eşiksiz karar veriyorsa, kararın hangi eşik varsayımıyla verildiğini
açıkça yazar ve bunu bir `ASSUMPTION` olarak etiketler.

---

## 4. EŞİK BELİRLEME NE ZAMAN YAPILIR

Önerilen an: **TUR 3 sonrası.** Model ilk çıktısını verdiğinde, yatırımcı
gerçek sayı aralıklarını görür ve eşiği bilinçli belirler. Eşiği modelden
*önce* belirlemek keyfî, *sonra* belirlemek ise sonuca göre eşik ayarlama
(hedef kaydırma) riski taşır — bu risk kararda not edilir.
