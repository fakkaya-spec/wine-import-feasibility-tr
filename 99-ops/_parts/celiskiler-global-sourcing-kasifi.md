# ÇELİŞKİLER — `global-sourcing-kasifi` (TUR 1, 2026-08-09)

> Kaynaklar çeliştiğinde **sessizce seçim yapılmaz.** Çelişki kaydedilir ve başkana taşınır.
> ID bloğu: `C-401` … `C-499`

---

## C-401 — Private label MOQ büyüklüğü

| Alan | Değer |
|---|---|
| conflict_id | **C-401** |
| status | **OPEN** |
| impact | **HIGH** — doğrudan `peak_cash_requirement` ve pilot uygulanabilirliği |

| Kaynak | Tier | İddia | evidence_id |
|---|---|---|---|
| A — usetorg.com (sektör agregatörü) | **T5** | Private label'da tipik MOQ **300–1.200 şişe** (25–100 koli) | EV-2026-08-09-424 |
| B — Interbrosa (üretici kurumsal sitesi, ES) | **T4** | MOQ **3.000 şişe** (4 palet) / şarap | EV-2026-08-09-408 |
| C — The Wine Factory (üretici kurumsal sitesi, FR) | **T4** | MOQ **3.600 şişe** | EV-2026-08-09-410 |
| D — Viña Maria (üretici kurumsal sitesi, ES) | **T4** | MOQ **1 × 20 ft karışık konteyner** (2 SKU) | EV-2026-08-09-409 |

### Neden çelişiyor
A, B ve C arasında **10 kata varan** bir fark var. D ise farklı bir birimde
(konteyner) ölçüyor ve şişe cinsinden karşılığı bilinmiyor (T-402).

### Neden sessizce çözülemez
- A'yı seçersek pilot çok ucuz görünür ve `IMPORT PILOT` kararı yapay olarak kolaylaşır.
- D'yi seçersek pilot imkânsız görünür ve proje yapay olarak ölür.
- B/C'yi seçersek pilot tam sınırda çıkar.
**Seçim, kararın kendisini belirler.** Bu yüzden çözüm başkana bırakılmıştır.

### Bu ajanın değerlendirmesi (öneri, karar değil)
B, C ve D **birincil kaynaklardır** (üreticinin kendi sitesi, tier T4).
A bir **agregatör içeriğidir** (tier T5) ve hangi üreticilere dayandığı belirtilmemiştir.
CLAUDE.md §2 uyarınca T5 tek başına sonuç üretemez.
Ayrıca A ile B/C/D arasındaki fark bir "hata" olmayabilir: **iki farklı tedarikçi
sınıfı** olabilir (butik/kontrat şişeleyici vs konteyner satan endüstriyel üretici).

### Çözüm yolu
Gerçek RFQ cevapları (RFQ soru 3.6 ve 4.2, en az 5 tedarikçiden). TUR 7.
Model, çözülene kadar **her iki uçta da senaryo çalıştırmalıdır.**

---

## C-402 — Türkiye'nin ABD menşeli şişelenmiş şarap ithalatının birim değeri

| Alan | Değer |
|---|---|
| conflict_id | **C-402** |
| status | **OPEN** |
| impact | **MEDIUM** — benchmark ürünün menşei ile veri uyuşmuyor |

| Kaynak | Tier | İddia |
|---|---|---|
| A — `00-charter/benchmark.md` (foto gözlemi) | FACT_FROM_PHOTO | Metro rafında California menşeli bir şarap 599,90 TL'ye satılıyor (fiyat/performans segmenti) |
| B — UN Comtrade (EV-2026-08-09-405) | T3 | Türkiye 2025'te ABD'den yalnızca **18.298 litre** şişelenmiş şarap ithal etti, ortalama CIF **25,19 USD/litre** |

### Neden çelişiyor
25,19 USD/litre = ~18,89 USD/750 ml CIF. Bu, fiyat/performans segmentiyle
**bağdaşmaz** — bir premium/lüks fiyat seviyesidir. Yani Comtrade'e göre
ABD'den Türkiye'ye giren mal, benchmark ürünün olması gereken segmentte değil.

### Olası açıklamalar (hiçbiri doğrulanmadı)
1. Benchmark ürün **ABD'den doğrudan değil**, bir AB ülkesi üzerinden (re-export/transit)
   geliyor olabilir ve menşe kaydı farklı görünüyor olabilir.
2. Benchmark ürün **eski bir partiden** kalma olabilir (2023 hasat, 2024 ithalatı).
3. 18.298 litrelik hacim içinde ucuz bir parti olabilir ama ortalama birim değer
   birkaç premium parti tarafından yukarı çekilmiş olabilir (ağırlıklı ortalama etkisi).
4. Comtrade partner kodu ayrıştırması hatalı olabilir (`842` kodu ABD alt kırılımı olarak
   yorumlandı).

### Kim çözer
- `turkiye-pazar-kasifi` → benchmark ürünün ithalatçısı ve ithalat yılı (T-405)
- `gumruk-vergi-uzmani` → menşe vs sevk ülkesi ayrımının Türkiye kayıtlarına yansıması

### Bu turdaki etkisi
Ülke karşılaştırma tablosunda ABD'nin L2 CIF değeri **"temsili değil"** olarak
işaretlenmiştir ve ülke sıralamasında kullanılmamıştır.

---

## C-403 — Benchmark ürünün California içindeki menşe bölgesi

| Alan | Değer |
|---|---|
| conflict_id | **C-403** |
| status | **OPEN** |
| impact | **LOW** — model çıktısını değiştirmez, tedarikçi aramasını yönlendirir |

| Kaynak | Tier | İddia |
|---|---|---|
| A — Perakendeci/agregatör açıklaması | T5 | "Gold Country" **Sierra Foothills** bölgesinde üretiliyor |
| B — Başka perakendeci/agregatör açıklaması | T5 | Ürün California **Central Valley**'den geliyor |

### Neden önemli (sınırlı)
Sierra Foothills küçük ve görece pahalı bir bölgedir; Central Valley ise Californiya'nın
hacim/değer segmentinin merkezidir. Fiyat/performans konumlandırması **Central Valley**
ile tutarlıdır. Ancak her iki kaynak da T5'tir ve marka adı ("Gold Country" =
California Gold Rush bölgesi, yani Sierra Foothills'in takma adı) pazarlama amaçlı
bir çağrışım olabilir.

### Çözüm yolu
Şişenin arka etiketindeki üretici/şişeleyici bilgisi (`turkiye-pazar-kasifi` raf
ziyaretinde okuyabilir) veya ABD TTB COLA kayıtları. → T-405

---

## ÖZET

| conflict_id | Konu | impact | status | Kim çözer |
|---|---|---|---|---|
| C-401 | Private label MOQ 300–1.200 vs 3.000–3.600 vs 1 konteyner | HIGH | OPEN | RFQ (TUR 7) + başkan |
| C-402 | ABD menşeli ithalatın birim değeri benchmark segmentiyle bağdaşmıyor | MEDIUM | OPEN | `turkiye-pazar-kasifi` (T-405) |
| C-403 | Benchmark ürünün California alt bölgesi | LOW | OPEN | `turkiye-pazar-kasifi` (T-405) |
