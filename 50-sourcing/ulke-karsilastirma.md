# ÜLKE KARŞILAŞTIRMA

> **Durum:** TUR 1 — `global-sourcing-kasifi` tarafından dolduruldu (2026-08-09)
> **Kaynak disiplini:** Her sayının `evidence_id`'si vardır. Sayısı olmayan hücre `UNKNOWN`'dır.
>
> **UYARI — KATMAN AYRIMI:**
> Bu dosyada **üç farklı fiyat katmanı** yan yana durur ve **birbirinin yerine kullanılamaz**:
> - **L1 (FOB)** — ülkelerin ihracat istatistiklerinden türetilmiş birim değerler
> - **L2 (CIF)** — Türkiye gümrük istatistiklerinden okunan, Türkiye sınırındaki birim değerler
> - **L0 (EXW)** — bu turda **hiçbir ülke için bilinmiyor**. Gerçek teklif yok.
>
> **Bu turda hiçbir üreticiden teklif alınmamıştır.** Tüm fiyat bilgisi ya kamu
> istatistiği ya da web sitesi beyanıdır. `quote_type` her satır için `NONE_YET`'tir.

---

## 1. KAPSANAN ÜLKELER

**Öncelikli (charter):** California (ABD), İspanya, İtalya, Fransa, Şili, Güney Afrika,
Portekiz, Avustralya, Arjantin.

**Bu turda EKLENEN (gerekçeli):** Moldova, Gürcistan, Bulgaristan.

**Ekleme gerekçesi (tek cümle):** UN Comtrade verisine göre bu üç ülke 2025'te
Türkiye'ye **fiilen ve anlamlı hacimde** şişelenmiş şarap ihraç etmiştir
(Moldova 2,04 m litre, Gürcistan 1,47 m litre, Bulgaristan 1,38 m litre) ve
CIF birim değerleri (2,46–3,89 USD/l) benchmark segmentine öncelikli ülkelerin
çoğundan daha yakındır — `EV-2026-08-09-405`.

Bu, öncelikli ülkeleri elemez. Yalnızca **veri kanıtı olan bir rakip küme** ekler.

---

## 2. ANA KARŞILAŞTIRMA TABLOSU

### 2.A — Fiyat sinyalleri (KATMANLAR AYRI)

| Ülke | Şişel. ort. ihracat birim değeri **L1** (EUR/l) | L1 → EUR/750 ml | Türkiye'ye **L2 CIF** 2025 (USD/l) | L2 → USD/750 ml | Türkiye'ye 2025 hacim (litre) | evidence_id |
|---|---|---|---|---|---|---|
| **İspanya** | 2,87 | 2,15 | **2,71** | **2,03** | 1.916.118 | EV-404 / EV-405 |
| **Şili** | 2,68 | 2,01 | **2,89** | **2,17** | 946.350 | EV-404 / EV-405 |
| **Portekiz** | 3,43 | 2,57 | **3,20** | **2,40** | 324.828 | EV-404 / EV-405 |
| **İtalya** | 4,39 | 3,29 | **3,65** | **2,74** | 5.749.972 | EV-404 / EV-405 |
| **Güney Afrika** | 2,72 | 2,04 | 7,03 *(18.026 l — temsili değil)* | 5,27 | 18.026 | EV-404 / EV-405 |
| **Arjantin** | 3,75 | 2,81 | 13,87 *(69.612 l — temsili değil)* | 10,40 | 69.612 | EV-404 / EV-405 |
| **Avustralya** | 4,99 | 3,74 | 7,33 *(44.674 l — temsili değil)* | 5,50 | 44.674 | EV-404 / EV-405 |
| **Fransa** | 7,79 | 5,84 | 6,27 | 4,70 | 2.851.454 | EV-404 / EV-405 |
| **ABD (California)** | 7,89 | 5,92 | 25,19 *(18.298 l — temsili değil, C-402)* | 18,89 | 18.298 | EV-404 / EV-405 |
| **Moldova** | UNKNOWN *(OIV tablosunda yok)* | — | **2,46** | **1,85** | 2.038.906 | EV-405 / EV-419 |
| **Gürcistan** | UNKNOWN | — | **2,57** | **1,93** | 1.470.052 | EV-405 |
| **Bulgaristan** | UNKNOWN | — | 3,89 | 2,92 | 1.377.058 | EV-405 |

**Nasıl okunmalı:**
- L1 sütunu **ülke ortalamasıdır**, segment fiyatı değildir. Premium SKU'lar ortalamayı yukarı çeker.
- L2 sütunu **Türkiye'ye fiilen giren mal karışımının** ortalamasıdır; bu yüzden segmentimize daha yakındır.
- L2 < L1 olan ülkelerde (İspanya, İtalya, Portekiz, Fransa, Moldova) Türkiye'ye giden mal,
  o ülkenin ortalamasından **daha ucuz uçtandır** — bu bizim segmentimizle uyumlu bir sinyaldir.
- **Hacmi 100.000 litrenin altındaki menşelerde birim değer temsili değildir** ve bunlarla
  ülke elemesi yapılamaz (tek bir premium parti tüm ortalamayı bozar).

### 2.B — Yapısal faktörler

| Ülke | STA / tercihli tarife | Menşe ispat belgesi | Navlun rotası (yalnızca rota) | Private label ekosistemi | İhracat hacmi & süreklilik | Doğrulanmış tedarikçi |
|---|---|---|---|---|---|---|
| İspanya | **KONTROL EDİLMELİ — T-401** | KONTROL EDİLMELİ — T-401 | Batı Akdeniz, deniz, kısa | **Çok güçlü** — ihracatının %57'si dökme → sanayi ölçekli şişeleme altyapısı (EV-403) | 19,6 mhl / 3,0 bn EUR (EV-403) | 2 (SUP-401, SUP-402) |
| İtalya | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | Orta Akdeniz, deniz, kısa | Güçlü — Veneto/Puglia private label yoğun | 21,0 mhl / 7,8 bn EUR (EV-403) | 1 (SUP-403) |
| Fransa | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | Batı Akdeniz / Atlantik, deniz | Güçlü ama üst segment ağırlıklı; Languedoc entry kanadı var | 12,5 mhl / 11,2 bn EUR (EV-403) | 1 (SUP-404) |
| Portekiz | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | Atlantik, deniz, orta | Orta — doğrulanan firma private label'ı ilan etmiyor | 3,4 mhl / 956 m EUR (EV-403) | 1 (SUP-411, Model A) |
| Şili | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | Pasifik → Süveyş/Ümit Burnu, uzun | **Güçlü** — ihracatçı-private label uzmanı firmalar mevcut | 7,1 mhl / 1,4 bn EUR (EV-403) | 2 (SUP-405, SUP-406) |
| Güney Afrika | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | Ümit Burnu → Akdeniz, uzun | **Çok güçlü** — sektör private label ihracatı üzerine kurulu (EV-412) | 3,2 mhl / 556 m EUR (EV-403) | 2 (SUP-407, SUP-408) |
| Avustralya | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | Hint Okyanusu → Süveyş, en uzun | Güçlü ama **dökme ağırlıklı** (ihracatın %64'ü bulk) | 6,1 mhl / 1,3 bn EUR (EV-403) | 1 (SUP-409) |
| Arjantin | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | Atlantik, uzun | Orta — Mendoza'da kapasite var, doğrulama zayıf | 1,9 mhl / 596 m EUR (EV-403) | 0 (SUP-407 üzerinden dolaylı) |
| ABD / California | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | Atlantik veya Pasifik, uzun | Var — full-service private label programları mevcut (EV-414) | 2,0 mhl / 757 m EUR; **2025'te hacim -%17,9, değer -%35,9** (EV-403) | 1 (SUP-410) |
| Moldova | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | **Karayolu/Karadeniz — en kısa** | UNKNOWN — bu turda doğrulanmadı | Türkiye'ye 2,04 m litre/yıl, 2 yıl üst üste (EV-405/406) | 0 |
| Gürcistan | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | **Karayolu — komşu ülke, en kısa** | UNKNOWN | Türkiye'ye 1,47 m litre/yıl, 2 yıl üst üste (EV-405/406) | 0 |
| Bulgaristan | KONTROL EDİLMELİ — T-401 | KONTROL EDİLMELİ — T-401 | **Karayolu — komşu ülke, en kısa** | UNKNOWN | Türkiye'ye 1,38 m litre (2025); 2024'te ilk 18'de yok — **süreklilik şüpheli** | 0 |

> **STA sütunu kuralı:** `global-sourcing-kasifi` yalnızca "kontrol edilmeli" bayrağını koyar.
> Hangi ülkenin hangi anlaşma kapsamında olduğu, oranı ve ÖTV/KDV etkisi
> **`gumruk-vergi-uzmani`'nın alanıdır.** Bu turda hiçbir STA iddiası yapılmamıştır;
> T.C. Ticaret Bakanlığı'nın STA sayfasına erişim 2026-08-09'da başarısız oldu (HTTP 503).
>
> **Navlun sütunu kuralı:** Yalnızca rota/mesafe niteliksel olarak işaretlenmiştir.
> **Navlun tutarı `navlun-lojistik-uzmani`'nın alanıdır** (T-402).

---

## 3. İŞ MODELİ BAZLI DEĞERLENDİRME

`00-charter/karar-esikleri.md` uyarınca iki model **eşit önceliklidir.**
Aşağıda ikisi de aynı derinlikte değerlendirilmiştir. **Bu turda hiçbiri öne çıkarılmamıştır.**

### 3.1 Model A — Mevcut marka distribütörlüğü

**Modelin nasıl işlediği (T3/T5 hukuk ve sektör kaynaklarından, `ESTIMATE`):**

| Boyut | Bulgu | status |
|---|---|---|
| Kim kimi arar | Üreticiler ithalatçı arayışını fuar (ProWein, Wine Paris, IBWSS), ihracat destek kurumları ve B2B platformları (Beverage Trade Network gibi) üzerinden yürütür | ESTIMATE / T5 |
| Münhasırlık | Belirli bir bölge veya müşteri grubu için verilebilir; genelde hacim taahhüdü karşılığıdır | ESTIMATE / T5 |
| Sözleşme süresi | Sektör kaynakları ~5 yıl + yenileme diyor; tedarikçi kısa, distribütör uzun süre ister | ESTIMATE / T5 |
| Fiyat maddesi | İki ayrı unsur: ithalatçının ödediği fiyat **ve** ithalatçının uygulayabileceği markup tavanı | ESTIMATE / T5 |
| Pazarlama katkısı | Doğrulanabilir tipik oran/tutar **bulunamadı** | **UNKNOWN** |
| Türkiye'de temsilcisi olmayan f/p markalar | Bu turda **isim bazında doğrulanmadı** | **UNKNOWN** |

**Model A'nın avantajı (mekanik):** marka geliştirme maliyeti ve zamanı yok; üreticinin
etiketi hazır; analiz/sertifika dosyası hazır.
**Model A'nın dezavantajı (mekanik):** markanın Türkiye'deki değeri bize ait değil;
üretici fiyatı tek taraflı revize edebilir; sözleşme biterse yatırım sıfırlanır;
IP bizde değil.

**Kritik açık:** Türkiye'de temsilcisi olmayan, fiyat/performans segmentinde **hangi
markaların** mevcut olduğu bu turda çıkarılamadı. Bu, `turkiye-pazar-kasifi`'nın raf
çalışmasıyla kesişir (T-405).

### 3.2 Model B — Private label

**Doğrulanmış üretici beyanları:**

| Ülke | Üretici | Private label MOQ | MOQ yapısı | Lead time | evidence_id |
|---|---|---|---|---|---|
| İspanya | Interbrosa | **3.000 şişe** (4 palet) | **SKU bazlı** | UNKNOWN | EV-408 |
| Fransa | The Wine Factory | **3.600 şişe** | **SKU bazlı** | **4–6 hafta** (ödeme sonrası) | EV-410 |
| İspanya | Viña Maria | **1 × 20 ft karışık konteyner** (2 SKU) | **Konteyner bazlı** | UNKNOWN | EV-409 |
| Güney Afrika | FMS Wine Marketing | UNKNOWN | UNKNOWN | **~4 hafta** | EV-411 |
| Şili | Antawara | UNKNOWN ("convenient") | UNKNOWN | UNKNOWN | EV-415 |
| Şili | Corta Hojas | UNKNOWN | UNKNOWN | UNKNOWN | EV-416 |
| G. Afrika | Origin Wine | UNKNOWN | UNKNOWN | UNKNOWN | EV-412 |
| Avustralya | Kingston Estate | UNKNOWN (şişelenmiş için) | UNKNOWN | UNKNOWN | EV-413 |
| California | Scheid Family Wines | UNKNOWN | UNKNOWN | UNKNOWN | EV-414 |
| İtalya | Vinicola Vedovato | UNKNOWN | UNKNOWN | UNKNOWN | EV-417 |

**En kritik tek bulgu:**
Doğrulanabilen en düşük private label MOQ'ları **3.000–3.600 şişe**'dir ve bu,
charter'daki **5.000 şişelik pilot hacmiyle uyumludur.** Yani private label modeli
pilot ölçekte teknik olarak uygulanabilir görünmektedir.

**Ancak:** Viña Maria'nın konteyner bazlı MOQ'su bunun tersini gösterir. **MOQ yapısı
tedarikçiye göre yapısal olarak farklıdır** (SKU bazlı vs konteyner bazlı) ve bu fark
`peak_cash_requirement`'i doğrudan değiştirir. Bu bir `CONFLICT` değil, bir
**segmentasyon bulgusudur**: "küçük parti bottler" ile "konteyner satan büyük üretici"
iki ayrı tedarikçi sınıfıdır.

**Model B'nin avantajı (mekanik):** marka ve reçete IP'si bizde olabilir (RFQ 4.9 ile
teyit edilecek); fiyat ve konumlandırma kontrolü bizde; tedarikçi değiştirilebilir.
**Model B'nin dezavantajı (mekanik):** marka bilinirliği sıfırdan inşa edilir; etiket
tasarım/klişe maliyeti ve zamanı bizde; kalite tutarlılığı riski bizde;
listeleme için markanın hikâyesi yok.

### 3.3 İki modelin karşılaştırması — **karar VERİLMEDİ**

| Kriter | Model A | Model B | Bu turdaki kanıt durumu |
|---|---|---|---|
| Pilot ölçekte uygulanabilirlik | UNKNOWN | **Doğrulandı (3.000–3.600 şişe)** | B lehine tek yönlü kanıt — çünkü A tarafında MOQ verisi hiç toplanamadı |
| MOQ verisi | UNKNOWN | 3 üreticide doğrulandı | Asimetri **kanıt eksikliğinden**, modelin üstünlüğünden değil |
| IP sahipliği | Üreticide | Muhtemelen bizde (teyit gerekli) | RFQ 4.9 |
| Fiyat kontrolü | Sınırlı | Yüksek | ESTIMATE |
| Kuruluş hızı | Muhtemelen daha hızlı | 4–6 hafta üretim + tasarım | Kısmi |
| Doğrulanmış tedarikçi sayısı | 1 (SUP-411) | 10 | **Bu bir arama yanlılığıdır** — bkz. §7.2 |

> **UYARI — ARAMA YANLILIĞI İTİRAFI:**
> Private label sağlayıcıları kendilerini web'de "private label" diye pazarlar ve
> aranabilirler. Mevcut marka sahipleri distribütör arayışını fuar ve doğrudan temasla
> yürütür ve web'de aranmaz. Bu nedenle **Model B'nin bu raporda daha zengin görünmesi,
> modelin daha iyi olduğunu değil, açık kaynakta daha görünür olduğunu gösterir.**
> Charter'ın "birini gerekçesiz öne çıkarma" kuralı bu nedenle burada özellikle
> vurgulanmıştır.

---

## 4. BULK ALTERNATİFİ — ARAŞTIRMA HİPOTEZİ (BU TURDA ÇÖZÜLMEDİ)

**Hipotez:** Dökme (bulk) şarap ithal edip Türkiye'de şişelemek, şişelenmiş ürün
ithal etmekten ekonomik olarak daha avantajlı olabilir mi?

**Durum:** `HYPOTHESIS — NOT INVESTIGATED` (kapsam dışı, `00-charter/kapsam.md`)

**Bu turda toplanan iki ilgili gözlem (yalnızca gözlem, sonuç değil):**

1. Dünya dökme şarap ortalama ihracat fiyatı 2025'te **0,75 EUR/litre**; şişelenmiş
   (<2 l) ise **4,53 EUR/litre**. Aradaki fark 6 kattır. (`EV-402`, `EV-401`)
   → Fark, kuru malzeme + şişeleme + üreticinin şişelenmiş ürün marjını içerir.
   Bu kalemlerin tutarı **UNKNOWN**'dır.
2. Türkiye 2025'te GTİP 2204.29 (dökme) kaleminde **628 litre** ithalat yaptı —
   yani pratikte sıfır. Aynı yıl şişelenmiş ithalat 17,85 milyon litredir. (`EV-407`)
   → Model piyasada uygulanmıyor. **Neden uygulanmadığı bu ajanın alanı değildir.**

**Bırakılan ipuçları** → `99-ops/_parts/capraz-ipuclari-global-sourcing-kasifi.md`

---

## 5. ELEME KRİTERLERİ — TUR 1 SONU DURUMU

| # | Eleme kriteri | Eşik | Bu turdaki durum |
|---|---|---|---|
| 1 | FOB fiyatı ters modelin verdiği max EXW/FOB'un üzerinde | TBD (`finans-fizibilite`) | **Uygulanamaz** — ne max FOB ne gerçek FOB var |
| 2 | MOQ pilot hacmiyle (5.000–10.000 şişe) uyumsuz | pilot hacmi | Private label'da **3 üretici geçti** (3.000/3.600 şişe); konteyner bazlı MOQ'lu üreticiler için **UNKNOWN** |
| 3 | Türkiye'ye ihracat deneyimi / lojistik hattı yok | — | Ülke düzeyinde: İtalya, Fransa, İspanya, Moldova, Gürcistan, Bulgaristan, Şili, Portekiz **geçti**. ABD, Avustralya, G. Afrika, Arjantin hattı **çok zayıf** (<100 bin litre/yıl) |
| 4 | Menşe ispat belgesi verilemiyor | — | **Tüm ülkeler için UNKNOWN** (T-401) |
| 5 | Private label kapasitesi yok **ve** distribütörlük fırsatı yok | — | Hiçbir ülke bu kritere göre elenmedi |

**Bu turda HİÇBİR ÜLKE ELENMEMİŞTİR.** Eleme için gereken iki girdi (max ödenebilir
FOB ve gerçek teklif) henüz yoktur.

---

## 6. ÖN GRUPLANDIRMA (KARAR DEĞİL — ARAŞTIRMA ÖNCELİĞİ)

Aşağıdaki gruplama bir **eleme değil**, bir sonraki turun kaynak dağılımı önerisidir.

**Grup 1 — Hem fiyat sinyali hem Türkiye hattı güçlü:**
İspanya, Şili, Moldova, Gürcistan, Portekiz, İtalya
*(L2 CIF ≤ 3,65 USD/l ve Türkiye'ye 2 yıl üst üste >300 bin litre)*

**Grup 2 — Private label ekosistemi güçlü ama Türkiye hattı zayıf:**
Güney Afrika, Avustralya, Arjantin
*(Türkiye'ye 2025 ihracatı <100 bin litre → lojistik/dokümantasyon rutini kurulmamış)*

**Grup 3 — Benchmark eşleşmesi var ama yapısal olarak zor:**
ABD / California
*(Benchmark ürünün menşei; ancak Türkiye'ye ihracat neredeyse yok, 2025'te ABD ihracatı
değer bazında -%35,9 daralmış, birim değerler segment üstü — `EV-403`, `EV-405`)*

**Grup 4 — Fiyat/performans segmentinde yapısal olarak zorlayıcı:**
Fransa *(L1 7,79 EUR/l, L2 6,27 USD/l — Languedoc entry kanadı hariç)*

**Grup 5 — Veri var ama süreklilik şüpheli:**
Bulgaristan *(2024'te ilk 18'de yok, 2025'te 1,38 m litre — tek yıllık sıçrama)*

---

## 7. BU BULGUYU NE ÇÜRÜTÜR?

### 7.1 Gösterge fiyat ile gerçek teklif arasındaki sapma ne kadar?
**Bilmiyoruz — ve bu dosyadaki en büyük zayıflık budur.** Bu turda **tek bir gerçek
teklif alınmamıştır.** Tabloların tamamı ya kamu ticaret istatistiğinden türetilmiştir
(ülke ortalaması, segment değil) ya da üretici web sitesi beyanıdır. Tarihsel sapma
oranını ölçebilmek için elimizde **hiçbir eşleştirilmiş çift (gösterge ↔ gerçek teklif)
yoktur.** Bu nedenle sapma büyüklüğü hakkında bir sayı vermek uydurma olurdu.
Ölçülebilir hâle gelmesi için TUR 7'de en az 5 gerçek teklif gerekir.

### 7.2 MOQ gerçekte 3× çıkarsa hangi ülkeler elenir?
MOQ 3.000 → 9.000 şişe olursa:
- Pilot hacmi 5.000 şişe ise **doğrulanmış üreticilerin tamamı pilot için elenir**;
  yalnızca 10.000 şişe ve üzeri senaryolar ayakta kalır.
- Ülke bazında eleme olmaz; **iş modeli bazında** eleme olur: private label pilot
  mantığı çöker, Model A'ya (mevcut markadan küçük parti alma) doğru kayar.
- Konteyner bazlı MOQ uygulayan üreticiler (Viña Maria tipi) zaten pilot dışıdır;
  3× senaryosunda tüm tedarikçi havuzu o sınıfa iner.
- `EV-424` (T5 agregatör iddiası: 300–1.200 şişe) ters yönde bir risk taşır: MOQ
  gerçekte **daha düşük** de çıkabilir. Belirsizlik iki yönlüdür (`C-401`).

### 7.3 Tek tedarikçiye bağımlılık riski nedir?
- Doğrulanmış tedarikçi sayısı **11**, ancak hiçbirinden fiyat alınmadığı için
  gerçek alternatif sayısı **fiilen 0**'dır. "11 aday" ile "11 alternatif" aynı şey değildir.
- Ülke yoğunlaşma riski: Grup 1'in fiyat cazibesi ağırlıkla **İspanya ve Şili**'de.
  İspanya 2025'te üretimini %7,7 düşürdü ve üç yıl üst üste kuraklık yaşadı (`EV-403` bağlamı).
  Tek harman/tek üretici bağımlılığı, kötü bir hasatta doğrudan fiyat şoku demektir.
- Private label'da özel bir risk var: **reçete ve marka IP'sinin kimde olduğu
  doğrulanmamıştır** (RFQ 4.9). IP üreticide ise tedarikçi değiştirmek ürünü değiştirmek
  anlamına gelir ve "alternatif tedarikçi" iddiası çöker.
- Origin Wine tipi çok-menşeli tedarikçiler (ZA + AR + CH) bu riski azaltabilir ama
  bir aracı katmanı ekler.

### 7.4 Tercihli tarifenin ÖTV'yi etkilemediği doğrulanırsa ülke sıralaması değişir mi?
Bu sorunun cevabı **bu ajanın alanı değildir** (`gumruk-vergi-uzmani`, T-401).
Sourcing tarafından söylenebilecek tek şey: eğer tercihli tarife nihai maliyette
belirleyici değilse, Grup 1'deki **AB dışı** ülkeler (Şili, Moldova, Gürcistan)
AB ülkelerine göre görece güçlenir; belirleyiciyse tersi olur. **Sıralama bu turda
verilmemiştir çünkü verilemez.**

### 7.5 En ucuz ülke aynı zamanda en uzun lead time'a sahipse net etki ne?
Net etkiyi hesaplamak için gereken iki girdi de bende yok: navlun tutarı
(`navlun-lojistik-uzmani`) ve sermaye maliyeti (`finans-fizibilite`).
Sourcing tarafından işaretlenen ham gerçek şudur: Grup 1'in en ucuz iki menşei
(Moldova, Gürcistan) aynı zamanda **en kısa** rotaya sahiptir (karayolu/Karadeniz),
Grup 2'nin tamamı ise en uzun rotalardadır. Yani bu turda "ucuz ama uzak" ödünleşimi
**gözlenmemiştir** — tersine ucuz olanlar yakındır. Bu, sezgiye aykırı olduğu için
`navlun-lojistik-uzmani`'nın doğrulaması ayrıca önemlidir (T-402).

### 7.6 Bu tablonun tamamını geçersiz kılacak tek bulgu
`EV-2026-08-09-405`'in miktar biriminin litre **olmadığı** (örneğin kilogram olduğu)
ortaya çıkarsa, tüm L2 sütunu ve ona dayanan `EV-421` bandı kayar. Comtrade
`qtyUnitCode=7` alanı litre olarak yorumlanmıştır ve `netWgt` ile neredeyse birebir
örtüştüğü için (şarap yoğunluğu ≈ 1 kg/l) sapma küçük olsa da, bu **doğrulanmamış bir
yorumdur** ve raporun en teknik kırılganlığıdır.
