# ÇELİŞKİLER — navlun-lojistik-uzmani (TUR 1)

> Kaynaklar çeliştiğinde sessizce seçim yapılmaz. Aşağıdaki üç çelişki
> **çözülmemiştir** ve başkana taşınmaktadır. Hesaplarda çelişkinin **bandı**
> kullanılmıştır, bir taraf seçilmemiştir.

---

## C-301 — Konteyner başına palet adedi

| Alan | Kaynak A | Kaynak B | Kaynak C |
|---|---|---|---|
| Kaynak | Hillebrand Gori — *Optimising pallet types* | Hillebrand Gori — *Freight Containers: How They're Used In the Wine Industry* | iContainers — 20-foot Container |
| tier / tarih | T4 / 2025-04-08 | T4 / 2022-10-28 (güncelleme 2023-10-18) | T4 / tarih yok |
| evidence_id | `EV-2026-08-09-308` | `EV-2026-08-09-309` | `EV-2026-08-09-301` |
| 20ft — standart/blok palet | **10** | **9** | 10 (GMA) |
| 20ft — Euro palet | **11** | **10** | 11 |
| 40ft — standart/blok palet | **21** | **20** | — |
| 40ft — Euro palet | **24** | **23** | — |

**Neden çelişiyor:** Aynı firmanın iki farklı yayını birbirini tutmuyor. Olası
sebep: biri "teorik geometrik kapasite", diğeri "pratikte kapıdan yüklenebilen"
sayı. Ayrıca palet standardı farkı (1000×1200 "standart" vs 1200×1000 "VMF blok"
vs 1219×1016 "GMA") ayrımı kaynaklarda net değil.

**Etkisi:** Paletli konteyner kapasitesinde **±%11** belirsizlik.
20DV paletli: 6.480 vs 7.200 şişe.

**Bu turda nasıl ele alındı:** Tek sayı seçilmedi; **9–11 / 20–24 bandı**
kullanıldı ve tüm kapasite sonuçları aralık olarak verildi.

**Nasıl çözülür:** Bir forwarder'dan (veya Hillebrand Gori'den) yazılı stowage
planı istenmesi. `T-304`.

**status:** `OPEN`

---

## C-302 — Valencia/ABD → İstanbul transit süreleri

| Alan | Kaynak A | Kaynak B |
|---|---|---|
| Kaynak | JSV Logistic (İspanya-Türkiye rehberi) + Maersk SLR Marmara Sea A servis tarifesi | BR Logistics — *Ship a container to Turkey [UPDATED 2026]* |
| tier / tarih | T4 / 2026-05-19 ve T3 / — | T5 / 2026 |
| evidence_id | `EV-2026-08-09-325`, `EV-2026-08-09-326` | `EV-2026-08-09-329`, `EV-2026-08-09-333` |
| Valencia → İstanbul | **7 – 10 gün** | **32 – 35 gün** |
| Los Angeles → İstanbul | — | **15 gün** |
| New York → İstanbul | — | 38 gün |

**Neden çelişiyor:** Kaynak B **kendi içinde de tutarsızdır**: Los Angeles →
İstanbul için 15 gün veriyor (Panama veya Süveyş üzerinden fiziksel olarak
mümkün değil; en az ~30 gün), Valencia → İstanbul için ise 32–35 gün veriyor
(Akdeniz içi bir rota için absürt derecede uzun). Muhtemelen door-to-door ve
port-to-port süreleri karışmış veya tablo satırları kaymış.

**Etkisi:** Lead time, işletme sermayesi, sıcaklık riski penceresi. Özellikle
**California rotası** (benchmark ürünün rotası) için kritik.

**Bu turda nasıl ele alındı:** Kaynak A'nın Akdeniz süreleri `FACT` olarak
kullanıldı (iki bağımsız kaynak birbirini doğruluyor: T4 rehber + T3 armatör
servis tarifesi). **ABD rotaları `CONFLICT`/`UNKNOWN` bırakıldı** ve Kaynak B'nin
ABD sayıları modele alınmadı.

**Nasıl çözülür:** Armatör servis tarifelerinden (Maersk/MSC/CMA CGM) doğrudan
port pair transit süresi okunması. `T-304`.

**status:** `OPEN`

---

## C-303 — 20DV azami payload

| Kaynak | Değer | tier | evidence_id |
|---|---|---|---|
| Maersk resmî FAQ | **28.300 kg** | T3 | `EV-2026-08-09-302` |
| iContainers | ~28.200 kg | T4 | `EV-2026-08-09-301` |
| Sektör derlemesi (arama sonucu) | "26.000 kg maksimum payload" | T5 | — (karta alınmadı) |

**Neden çelişiyor:** Konteyner üreticisi/serisi farkı; ayrıca bazı kaynaklar
konteynerin yapısal payload'ı yerine **CSC plakasındaki max gross − dara**
veya ülke bazlı kısıtlanmış değeri veriyor.

**Etkisi:** **Düşük.** Şarapta 20DV zaten hacim kısıtlıdır (payload'ın %30–60'ı
kullanılır), bu yüzden 28.200 ile 28.300 arasındaki fark modelde hiçbir şeyi
değiştirmez. 26.000 kg iddiası bile bağlayıcı olmaz.

**Bu turda nasıl ele alındı:** Maersk (T3) değeri kullanıldı; 26.000 kg iddiası
T5 olduğu için kanıt kartına alınmadı.

**status:** `OPEN` (düşük öncelikli)
