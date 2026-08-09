# AÇIK SORULAR — `global-sourcing-kasifi` (TUR 1, 2026-08-09)

> **UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**
> Aşağıdakiler bu ajanın kendi alanında **çözemediği** sorulardır.

---

## KRİTİK (nihai kararı bloke edebilir)

### OQ-401 — Gerçek EXW/FOB fiyatı hiçbir tedarikçi için bilinmiyor
**Ne bilinmiyor:** Fiyat/performans segmentinde 750 ml şişelenmiş bir beyaz şarabın
gerçek EXW (L0) ve FOB (L1) fiyatı — hiçbir ülke, hiçbir üretici için.
**Neden bulunamadı:** Tedarikçiler fiyat listelerini web'de yayınlamaz. Bu turda
üreticilere iletişim kurulması **açıkça yasaklanmıştır** (P1 = haritalama turu).
**Elde olan:** Yalnızca kanıtla sınırlandırılmış bir bant
(`EV-2026-08-09-421`): alt sınır 0,56 EUR/750 ml (sadece sıvı), üst sınır
1,85–2,40 USD/750 ml (bu bir **CIF** tavanıdır).
**Nasıl bulunur:** `50-sourcing/rfq-template.md` v2.0'ın en az 8–10 üreticiye
gönderilmesi (TUR 7). Süre: cevap için 2–4 hafta.
**Kritiklik:** **CRITICAL.** Bu olmadan ters model (hedef raf fiyatı → max ödenebilir
FOB) doğrulanamaz, yalnızca hedef üretilebilir.

### OQ-402 — Gerçek MOQ ve MOQ yapısı
**Ne bilinmiyor:** Tedarikçi bazında gerçek MOQ; ve MOQ'nun SKU bazlı mı konteyner
bazlı mı olduğu. Kaynaklar 300 şişe ile 1 konteyner arasında değişiyor (`C-401`).
**Neden bulunamadı:** Üreticilerin çoğu MOQ'yu web'de yayınlamıyor; yayınlayan üç
üretici birbiriyle uyumsuz birimlerde ölçüyor.
**Nasıl bulunur:** RFQ 3.6 (a: şişe, b: konteyner) ve 4.2/4.3.
**Kritiklik:** **CRITICAL.** Pilot senaryonun (5.000 şişe) uygulanabilirliği doğrudan
buna bağlı.

### OQ-403 — Menşe ispat belgesi kabiliyeti
**Ne bilinmiyor:** Hangi üretici hangi menşe ispat belgesini (EUR.1 / fatura beyanı /
REX / A.TR) düzenleyebiliyor.
**Neden bulunamadı:** Hiçbir üretici sitesinde bu bilgi yok; ayrıca hangi belgenin
gerektiği `gumruk-vergi-uzmani`'nın cevabına bağlı (T-401).
**Nasıl bulunur:** Önce T-401 kapanmalı, sonra RFQ 6.1.
**Kritiklik:** **CRITICAL** — tercihli tarife kaybı birim maliyeti anlamlı ölçüde
değiştirebilir.

---

## YÜKSEK

### OQ-404 — Türkiye'de temsilcisi olmayan fiyat/performans markaları
**Ne bilinmiyor:** Model A için somut marka adları. Bu turda **tek bir marka bile**
"Türkiye'de temsilcisi yok" diye doğrulanamadı.
**Neden bulunamadı:** Bu bilgi iki yönlü bir kesişimdir: (a) markanın var olduğu,
(b) Türkiye'de dağıtılmadığı. (b) ancak Türkiye raf/ithalatçı verisinden bilinir —
`turkiye-pazar-kasifi`'nın alanı.
**Nasıl bulunur:** `turkiye-pazar-kasifi`'nın rakip/ithalatçı listesi ile bu ajanın
üretici portföy listesinin çaprazlanması (TUR 2).
**Kritiklik:** HIGH — Model A bu olmadan değerlendirilemez ve iki modelin
**eşit öncelikli** karşılaştırması eksik kalır.

### OQ-405 — Ödeme vadesi ve ilk sipariş pratiği
**Ne bilinmiyor:** Tedarikçilerin Türk bir alıcıya ilk siparişte hangi ödeme şartını
dayatacağı.
**Elde olan:** Yalnızca genel sektör rehberi (`EV-2026-08-09-420`), tedarikçi taahhüdü
değil.
**Nasıl bulunur:** RFQ 3.8–3.10.
**Kritiklik:** HIGH — `peak_cash_requirement` ve CCC doğrudan etkilenir.

### OQ-406 — Türkçe arka etiket menşede uygulanabilir mi
**Ne bilinmiyor:** Hiçbir üretici için doğrulanmadı; ayrıca hukuken mümkün mü,
bilinmiyor (T-403).
**Kritiklik:** HIGH — L5 (importer cost) katmanında bir operasyon kalemini
tamamen ortadan kaldırabilir veya ekleyebilir.

### OQ-407 — Konteyner başına şişe sayısı
**Ne bilinmiyor:** 20' DV ve 40' HC'ye kaç şişe 750 ml yüklenir; ağırlık mı hacim mi
bağlayıcı.
**Neden bulunamadı:** Alan dışı — `navlun-lojistik-uzmani` (T-402). Ayrıca üreticilerin
koli/palet ölçüleri de bilinmiyor (RFQ 2.1–2.8).
**Kritiklik:** HIGH — konteyner bazlı MOQ'lu tedarikçilerin pilot uyumu bunsuz
hesaplanamaz.

---

## ORTA

### OQ-408 — Marka ve reçete IP sahipliği (private label)
**Ne bilinmiyor:** Private label'da harmanın ve markanın hukuken kimde olduğu.
**Neden önemli:** IP üreticideyse "tedarikçi değiştirilebilir" iddiası çöker ve
tek tedarikçiye bağımlılık riski gerçekleşir.
**Nasıl bulunur:** RFQ 4.9 ve 4.10.

### OQ-409 — Etiket klişe / kalıp tek seferlik maliyeti
**Ne bilinmiyor:** Bir üretici tasarımı "ücretsiz" sunduğunu beyan ediyor
(`EV-2026-08-09-408`) ama baskı klişesi, kalıp veya minimum baskı adedi maliyeti
bilinmiyor. Küçük pilot hacimde bu, şişe başına anlamlı olabilir.
**Nasıl bulunur:** RFQ 4.7.

### OQ-410 — ABV
**Ne bilinmiyor:** Aday ürünlerin hiçbirinin ABV'si bilinmiyor. Benchmark ürünün ABV'si
de `00-charter/benchmark.md`'de UNKNOWN.
**Neden önemli:** ABV, GTİP alt kırılımı veya ÖTV eşiği ile ilişkiliyse tedarikçi
seçimini değiştirir; ayrıca private label'da **ayarlanabilir** bir parametredir.
**Nasıl bulunur:** RFQ 1.4 + `gumruk-vergi-uzmani`'nın eşik cevabı.

### OQ-411 — Yıllık kapasite ve süreklilik
**Ne bilinmiyor:** Hiçbir aday tedarikçinin bize ayırabileceği yıllık hacim.
100.000 şişe/yıl senaryosunun (charter'ın üst ucu) hangi tedarikçilerle mümkün
olduğu bilinmiyor.
**Nasıl bulunur:** RFQ 3.12 ve 8.3.

### OQ-412 — Moldova / Gürcistan / Bulgaristan tedarikçi tabanı
**Ne bilinmiyor:** Bu üç ülke Türkiye'ye anlamlı hacimde ve düşük birim değerle mal
gönderiyor, ancak bu turda **tek bir üretici doğrulanmadı.**
**Neden bulunamadı:** Zaman/kaynak önceliği charter'ın öncelikli 9 ülkesine verildi.
**Nasıl bulunur:** Wine of Moldova (ONVV), Georgian Wine Association, Bulgarian
Association of Independent Winegrowers üye listeleri — bir sonraki tur.
**Kritiklik:** MEDIUM — ama fiyat sinyali en güçlü grup burada olduğu için
gözden kaçırılması pahalıya mal olabilir.

---

## DÜŞÜK

### OQ-413 — Les Grands Chais de France doğrulaması
Kurumsal site (groupegcf.com) 2026-08-09'da HTTP 503 döndü; firma tedarikçi havuzuna
alınmadı (`EV-2026-08-09-428`). Bir sonraki turda yeniden denenmeli.

### OQ-414 — Ciatti dökme fiyat grid'i
Ciatti Global Market Report'un ülke bazlı dökme fiyat tablosu **abonelik arkasında**;
yalnızca yorum metni erişilebildi. Ülke bazlı dökme fiyat tabanı bu nedenle
yalnızca OIV dünya ortalamasıyla (`EV-2026-08-09-402`) temsil ediliyor.

### OQ-415 — OEMV birincil verisi
İspanya ihracat fiyatları basından okundu (T5); OEMV'nin kendi sayfası doğrudan
doğrulanmadı (`EV-2026-08-09-427`). Modele girmedi.

---

## ÖZET TABLO

| # | Soru | Kritiklik | Kim çözer | Nasıl |
|---|---|---|---|---|
| OQ-401 | Gerçek EXW/FOB fiyatı | **CRITICAL** | `global-sourcing-kasifi` | RFQ, TUR 7 |
| OQ-402 | Gerçek MOQ ve yapısı | **CRITICAL** | `global-sourcing-kasifi` | RFQ 3.6 / 4.2 |
| OQ-403 | Menşe ispat belgesi | **CRITICAL** | `gumruk-vergi-uzmani` + RFQ | T-401 → RFQ 6.1 |
| OQ-404 | Türkiye'de temsilcisi olmayan markalar | HIGH | `turkiye-pazar-kasifi` çaprazı | TUR 2 |
| OQ-405 | Ödeme vadesi | HIGH | `global-sourcing-kasifi` | RFQ 3.8–3.10 |
| OQ-406 | Türkçe etiket menşede mi | HIGH | `mevzuat-ruhsat-uzmani` | T-403 |
| OQ-407 | Konteyner başına şişe | HIGH | `navlun-lojistik-uzmani` | T-402 |
| OQ-408 | IP sahipliği | MEDIUM | `global-sourcing-kasifi` | RFQ 4.9 |
| OQ-409 | Klişe/kalıp maliyeti | MEDIUM | `global-sourcing-kasifi` | RFQ 4.7 |
| OQ-410 | ABV | MEDIUM | `gumruk-vergi-uzmani` + RFQ | T-401, RFQ 1.4 |
| OQ-411 | Yıllık kapasite | MEDIUM | `global-sourcing-kasifi` | RFQ 3.12 |
| OQ-412 | MD/GE/BG tedarikçi tabanı | MEDIUM | `global-sourcing-kasifi` | Sonraki tur |
| OQ-413 | GCF doğrulaması | LOW | `global-sourcing-kasifi` | Sonraki tur |
| OQ-414 | Ciatti fiyat grid'i | LOW | — | Abonelik gerekir |
| OQ-415 | OEMV birincil verisi | LOW | `global-sourcing-kasifi` | Sonraki tur |
