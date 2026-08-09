# ÇELİŞKİLER — turkiye-pazar-kasifi (TUR 1)

> Ana `99-ops/celiskiler.md`'ye başkan tarafından birleştirilecektir.

---

## C-501 — Aynı kanalda stokta olan ve olmayan SKU'ların fiyatları tutarsız

| Alan | Değer |
|---|---|
| `conflict_id` | **C-501** |
| **Kaynak A** | `iyisarap.plus` ürün feed'i, `available: true` satırlar (T4, 2026-08-09) — stokta en ucuz **ithal** şarap **875 TL**, en ucuz **yerli** şarap **460 TL** |
| **Kaynak B** | Aynı feed'in `available: false` satırları (T4, aynı erişim tarihi) — Terra Mater Paso del Sol **70 TL**, Paiara Puglia Rosso **106 TL**, Lamberti Merlot **138 TL** gibi 2026 Türkiye'si için gerçeklik dışı ithal şarap fiyatları |
| **Neden çelişiyor** | Aynı sitenin aynı anda yayınladığı iki fiyat kümesi arasında **10 kata varan** fark var. Stokta olmayan listelemelerin fiyatları güncellenmemiş eski kayıtlar olduğu değerlendirilmektedir — ancak feed'in `updated_at` alanı bu satırlar için de `2026-08` göstermektedir, yani teknik olarak "eski" görünmüyorlar. |
| **Nasıl ele alındı** | Yalnızca `available: true` satırlar gözlem olarak kabul edildi (`EV-509`, `EV-510`). Stokta olmayanlar CSV'ye **alınmadı**. |
| **Çözüldü mü** | **HAYIR — `OPEN`** |
| **Riski** | Eğer stokta olmayan fiyatlar gerçekse, Türkiye'de 70–450 TL bandında ithal şarap **vardır** ve benchmark bandı analizi tamamen değişir. Bu ihtimal düşük görülmektedir (ÖTV + gümrük yükü bu fiyatı imkânsız kılar) ama **elenmemiştir**. |
| **Nasıl kapanır** | Fiziksel mağazada 400–800 TL bandında ithal şarap olup olmadığının doğrudan gözlemi (`OQ-502`). |

---

## C-502 — Metro'nun KDV dili iki farklı yerde iki farklı

| Alan | Değer |
|---|---|
| `conflict_id` | **C-502** |
| **Kaynak A** | Metro Türkiye resmî broşürleri (T4, 05–11.08.2026 ve 01–31.08.2026): tüm fiyatlar **`KDV'li`** ibaresiyle — `EV-503`, `EV-504` |
| **Kaynak B** | Metro Türkiye resmî kampanya koşulları (T4, 2026): *"Alım hedeflerinize **KDV dahil değildir**"* — `EV-508` |
| **Neden çelişiyor gibi görünüyor** | Aynı şirket, aynı yıl, bir yerde brüt bir yerde net konuşuyor. |
| **Değerlendirme** | **Gerçek bir çelişki DEĞİLDİR.** İki farklı matrah iki farklı amaç için kullanılıyor: müşteriye ilan edilen **raf fiyatı brüt** (KDV'li), ciro/hedef muhasebesi **net** (KDV hariç). Bu ayrım cash & carry formatında olağandır. |
| **Yine de neden kaydediliyor** | Çünkü **OQ-001 şüphesinin kaynağı tam olarak budur** ve `seytanin-avukati` bu noktaya saldıracaktır. Sessizce çözüldü sayılmamalıdır. |
| **Durum** | `OPEN (izleme)` — `T-501` ile birlikte değerlendirilecek |

---

## C-503 — T5 medya fiyat listesi ile gözlemlenen bant arasındaki uyum sorunu

| Alan | Değer |
|---|---|
| `conflict_id` | **C-503** |
| **Kaynak A** | T5 içerik siteleri (Ocak/Temmuz 2026): Metro'da Doluca 75 cl **630 TL**, Grand Reserve Boğazkere **570 TL** — `EV-512` |
| **Kaynak B** | Online uzman perakende (T4, Ağustos 2026): benzer segmentteki yerli şaraplar **649–800 TL** — `EV-510` |
| **Neden problem** | İki kaynak birbirine yakın ama **A kaynağı T5'tir ve üç site aynı tabloyu kopyalamıştır** — bağımsız doğrulama değildir. Yakınlık, doğruluk kanıtı sayılamaz. Ayrıca A kaynağı Ocak 2026 tarihli; Ağustos 2026 fiyatı olarak kullanılamaz. |
| **Nasıl ele alındı** | `EV-512` satırları CSV'ye `status: UNKNOWN` ile girildi ve **"MODELE GİREMEZ"** notu düşüldü. |
| **Durum** | `OPEN` — fiziksel gözlemle kapanır (`OQ-502`) |
