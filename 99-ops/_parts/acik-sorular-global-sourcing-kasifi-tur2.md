# AÇIK SORULAR — global-sourcing-kasifi — TUR 2

> `99-ops/acik-sorular.md` dosyasına **DOKUNULMAMIŞTIR** (başkan birleştirir).
> **UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## A. YALNIZCA GERÇEK RFQ İLE ÖĞRENİLEBİLECEK ALANLAR

Bu, bu turun **en önemli çıktılarından biridir**: hangi bilginin açık kaynak
araştırmasıyla **prensipte** elde edilemeyeceğinin alan alan listesi.
Aşağıdaki 21 alan için **daha fazla web araştırması yapmak kaynak israfıdır.**

| # | Alan | CSV kolonu | Neden açık kaynakta yok | RFQ sorusu |
|---|---|---|---|---|
| 1 | **EXW şişe fiyatı** | `EXW` | Fiyat listesi ticari sırdır; 26 tedarikçinin **1'i** kademeli gösterge yayınladı | 3.1 / S11 |
| 2 | **FOB şişe fiyatı + adı belirtilen liman** | `FOB`, `port` | Aynı | 3.2 / S12 |
| 3 | **Para birimi** | `currency` | Yayınlanan tek fiyatta bile yazılı değil | 3.13 / S11 |
| 4 | **Hacim bazlı fiyat kırılımı** (5k/10k/25k/50k/100k) | — | Müzakereye açık; hiçbir üretici yayınlamaz | 3.7 |
| 5 | **Teklifin INDICATIVE mi FIRM mi olduğu** | `price_source_class` | Web sayfası tanım gereği teklif değildir | 3.4 / S25 |
| 6 | **Teklif geçerlilik tarihi** | `quote_publication_date` | Aynı | 3.5 / S25 |
| 7 | **Gerçek MOQ** (SKU **ve** konteyner bazında) | `MOQ` | 26'nın **5'i** yayınladı; ikisi farklı birimde | 3.6a/3.6b, 4.2, 4.3 |
| 8 | **Ödeme şartı — ilk sipariş** | `payment_terms` | 26'nın **1'i** yayınladı (Harland) | 3.8 |
| 9 | **Ödeme şartı — sonraki siparişler + vade günü** | `payment_terms` | Hiçbiri | 3.9, 3.10 |
| 10 | **Toplam lead time** (PO → yüklemeye hazır) | `lead_time` | Yalnızca **üretim** süresi yayınlanıyor, toplam değil | 3.11 / S15 |
| 11 | **Üretim süresinin kırılımı** (şişeleme / etiket / evrak / gemi bekleme) | `production_time` | Hiçbiri | 3.17 |
| 12 | **Koli konfigürasyonu ve brüt/net ağırlık + dış ölçü** | `case_configuration` | 26'nın **1'i** (Harland, kısmen) | 2.1–2.3 / S8 |
| 13 | **Palet konfigürasyonu, tipi, ISPM-15, yükseklik** | `pallet_configuration` | Hiçbiri | 2.4–2.7 / S9 |
| 14 | **Boş ve dolu şişe ağırlığı** | `bottle_weight` | Hiçbiri — cam tedarikçisi verisidir | 1.14, 1.15 / S7 |
| 15 | **Etiket maliyeti — tek seferlik (klişe/kalıp) + şişe başı** | `label_cost` | Hiçbiri; bir üretici yalnızca "tasarım ücretsiz" diyor | 4.13 / S19 |
| 16 | **Karton/koli maliyeti ve EXW'ye dahil olup olmadığı** | `carton_cost` | Hiçbiri | 3.18e, 4.14 / S20 |
| 17 | **Numune politikası** (adet, maliyet, süre, aynı parti mi) | `sample_policy` | Hiçbiri | 7.1–7.5 / S21 |
| 18 | **Bize ayrılabilecek yıllık kapasite** | `annual_capacity` | Toplam kapasite bazen var; **bize ayrılabilir** olan hiç yok | 3.12, 8.3 / S22 |
| 19 | **Menşe ispat belgesi tipi** (EUR.1 / fatura beyanı / REX / A.TR) | `certificates` | Hiçbiri | 6.1 / S23 |
| 20 | **Türkiye'ye ihracat geçmişi** (ithalatçı, yıl, hacim) | `turkey_export_experience` | **26'nın hiçbiri Türkiye'yi ihracat pazarları arasında listelemiyor** | 6.6 / S24 |
| 21 | **Marka / reçete / artwork IP sahipliği** | — | Sözleşme maddesidir, web'de olmaz | 4.9 |

**Ek olarak yalnızca Model A'da, yalnızca RFQ ile öğrenilebilecekler:**
münhasırlık koşulları (5.4), münhasırlığı korumak için gereken yıllık hacim (5.5),
pazarlama/listeleme desteği (5.6), **ithalatçıya markup/yeniden satış fiyatı tavanı
uygulanıp uygulanmadığı (5.7)**, fesih ve stok koşulları (5.8), marka tescilinin
kimde olduğu (5.9), fiyat revizyon mekanizması (5.10).

---

## B. AÇIK SORULAR (RFQ dışı yollarla da kapanabilecekler)

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| OQ-451 | **Harland'ın yayınladığı fiyatın para birimi (AUD mi USD mi)** | Kaynakta yalnızca "$" sembolü var | **CRITICAL** | RFQ 3.1/3.13; veya firmanın başka bir sayfasında para birimi beyanı |
| OQ-452 | **Model A adaylarının Türkiye'de temsilcisi olup olmadığı** — 7 marka | İki yönlü kesişim; ikinci yön `turkiye-pazar-kasifi`'nda | **CRITICAL** | T-464 + raf gözlemi + ithalatçı listesi |
| OQ-453 | **Hiçbir tedarikçi için EXW/FOB** | Fiyat listeleri yayınlanmaz; dış iletişim bu turda yasaktı | **CRITICAL** | RFQ v2.1, Dalga 1 (7 hedef), 2–3 hafta |
| OQ-454 | **Interbrosa'nın MOQ'sunun bugün hâlâ 3.000 olup olmadığı** | Site 2026-08-10'da HTTP 503 (`EV-2026-08-10-467`) | HIGH | E-posta/telefon (site erişimine bağlı kalmadan) |
| OQ-455 | **Havuzda vade veren tedarikçi var mı** | Doğrulanan tek ödeme şartı tamamen peşin | HIGH | RFQ 3.8/3.9/3.10 |
| OQ-456 | **Côtes de Gascogne'un fiyat seviyesi** — Fransa ortalamasının (6,27 USD/l) altında mı | Bölgesel birim değer verisi bulunamadı; OIV ülke bazında raporluyor | HIGH | RFQ 3.1 (Plaimont) veya FranceAgriMer bölgesel ihracat verisi |
| OQ-457 | **Zidela'nın kendi kurumsal beyanları** (MOQ, e-posta, kapasite teyidi) | Kurumsal site yaş doğrulama duvarının arkasında | MEDIUM | Doğrudan telefon; veya IBWSS/WorldBulkWine katılımcı profili |
| OQ-458 | **Parras Wines private label yapıyor mu** | Grup içinde şişeleme tesisi var ama hizmet ilan edilmemiş — bu bir **çıkarımdır** | MEDIUM | RFQ 4.1; Goanvi Bottling ayrı kurumsal kanalı |
| OQ-459 | **Bronco Wine private label programı var mı** | Kurumsal sitede yok; T5 iddiası doğrulanamadı (`EV-2026-08-10-466`) | MEDIUM | broncowine-trade.com (bu turda okunmadı) |
| OQ-460 | **Arjantin'de üretici seviyesinde private label** | Kaynak önceliği TIER A ülkelerine verildi (`EV-2026-08-10-469`) | MEDIUM | Wines of Argentina üye dizini; Bodegas de Argentina; ProWein AR katılımcı listesi |
| OQ-461 | **Luis Felipe Edwards'ın güncel kurumsal sitesi** | lfewines.com/en/ HTTP 404 | LOW | Wines of Chile üzerinden; veya ana domain kök dizini |
| OQ-462 | **Cantine Sgarzi (IT) private label şartları** | Sayfa iki denemede de boş içerik döndürdü | LOW | Yeniden deneme / doğrudan e-posta |
| OQ-463 | **Purcari'nin şişe bazında satış hacmi** | Gelir RON cinsinden yayınlanıyor, hacim kırılımı yok | LOW | BVB'ye sunulan yıllık faaliyet raporu |
| OQ-464 | **Paletli yüklemede 20ft/40HC konteyner doluluğu** | Yalnızca paletsiz (slipsheet) rakam bulundu | HIGH | T-461 + RFQ 2.8/2.9 — alan `navlun-lojistik-uzmani`'nda |

---

## C. TUR 1'DEN DEVREDEN VE HÂLÂ AÇIK OLANLAR

`OQ-401` … `OQ-415`'in **tamamı açıktır.** TUR 2'de kısmen ilerleyenler:

| TUR 1 sorusu | TUR 2'de ne değişti |
|---|---|
| OQ-401 (gerçek EXW/FOB) | Bir tedarikçide **gösterge** fiyat bulundu; gerçek teklif hâlâ **0**. Açık |
| OQ-402 (gerçek MOQ ve yapısı) | Doğrulanan üretici sayısı 3'ten **5'e** çıktı; aralık genişledi (`C-462`). Açık |
| OQ-404 (Türkiye'de temsilcisi olmayan f/p markalar) | **7 somut marka adayı** bulundu ama temsilci durumu UNKNOWN. **İlerleme var, kapanmadı** (T-464) |
| OQ-405 (ilk siparişte ödeme vadesi) | Bir tedarikçide ödeme şartı bulundu (%50+%50 peşin). n=1. Açık |
| OQ-407 (konteynere kaç şişe girer) | **İlk somut rakam bulundu**: 14.112 şişe/20ft (paletsiz). Paletli UNKNOWN (T-461). Kısmen ilerledi |
| OQ-411 (bize ayrılabilecek kapasite) | Toplam kapasiteler bulundu; **bize ayrılabilir** olan hâlâ hiçbir tedarikçide yok. Açık |
| OQ-412 (MD/GE/BG tedarikçi tabanı) | **Moldova'da ilk tedarikçi doğrulandı** (Purcari). Gürcistan ve Bulgaristan hâlâ **0**. Kısmen ilerledi |
| OQ-413 (Les Grands Chais de France) | Bu turda **denenmedi** — kaynak Plaimont'a yönlendirildi. Açık |
