# RFQ CONTACT PACK — gönderime hazır, önceliklendirilmiş tedarikçi iletişim listesi

```yaml
sahibi:               global-sourcing-kasifi
tur:                  TUR 2 — COMMERCIAL VALIDATION
tarih:                2026-08-10
kayit_sayisi:         26
gonderim_durumu:      HAZIR — GÖNDERİLMEDİ
dis_iletisim_yapildi: false
sablon:               50-sourcing/rfq-template.md (v2.1)
```

> ## ⛔ BU TURDA HİÇBİR ÜRETİCİYE TEMAS EDİLMEDİ
>
> Bu dosya bir **hazırlıktır**. Aşağıdaki e-posta adresleri, telefonlar ve formlar
> **herkese açık kurumsal kanallardan** toplanmıştır. Hiçbirine e-posta, mesaj veya
> form gönderilmemiştir ve `yatirim-komitesi-baskani` onayı olmadan gönderilmeyecektir.
>
> **Gönderim koşulu:** karar `TEST` veya `IMPORT PILOT` **ve** başkan onayı **ve**
> `T-401`/`T-462` (menşe belgesi grubu) kapalı **ve** `<VOLUME>` alanları doldurulmuş.

---

## 0. KANAL KALİTESİ SINIFLANDIRMASI

| Sınıf | Anlamı | Gönderim davranışı |
|---|---|---|
| **K-A** | Doğrudan **ihracat/uluslararası** e-posta adresi | RFQ doğrudan gönderilir |
| **K-B** | Genel kurumsal e-posta (info@…) | RFQ gönderilir, konu satırına "Export Sales" eklenir |
| **K-C** | Yalnızca telefon | Önce telefonla e-posta adresi istenir, sonra RFQ |
| **K-D** | Yalnızca web formu | Form üzerinden kısa tanıtım + RFQ'yu e-posta ile isteme talebi |
| **K-E** | Yalnızca fuar / üçüncü taraf dizin profili | Fuar platformu mesajlaşması veya dizin üzerinden kurumsal kanal tespiti |
| **K-X** | Doğrulanmış kanal **yok** | RFQ **gönderilemez** — önce kanal bulunmalı |

---

## 1. DALGA 1 — A ÖNCELİK (7 tedarikçi, TOP 10'un çekirdeği)

| # | Tedarikçi | Ülke | Model | Kanal sınıfı | İletişim | Not |
|---|---|---|---|---|---|---|
| 1 | **Harland Wine Company Pty Ltd** | AU | B | **K-B** | hello@harlandwineco.com.au | Fiyat kademesi yayınlı → RFQ'da "gösterge fiyatınızı teyit eder misiniz" sorusu eklenir |
| 2 | **Cantina Danese s.r.l.** | IT | B | **K-A** | international@cantinadanese.com · +39 045 746 0060 | Havuzdaki **en iyi kanal**: uluslararası satışa ayrılmış adres |
| 3 | **Interbrosa Family Wines** | ES | B | **K-B** | info@interbrosa.es · +34 952 929 521 | ⚠️ **Site 2026-08-10'da HTTP 503** — site linki gönderilmez, doğrudan e-posta |
| 4 | **The Wine Factory (SARL)** | FR | B | **K-C** | +33 5 56 61 91 12 (Bordeaux) · +33 4 67 76 50 24 (Valros) | E-posta bulunamadı → önce telefon; **hangi tesis** olduğu fiyatı değiştirir |
| 5 | **Corta Hojas Export Wine** | CL | B | **K-B** | info@cortahojas.com · +56 75 2315 328 | Beyaz çeşitler eşleşiyor; MOQ/fiyat hiç yayınlanmamış |
| 6 | **Bodegas San Valero** | ES | **A+B** | **K-E** | https://wineparis.com/exhibitor/bodega-san-valero · https://www.sanvalero.com/ | Doğrudan ihracat adresi bulunamadı; fuar profili üzerinden |
| 7 | **Casa Santos Lima** | PT | A | **K-D** | https://www.casasantoslima.com/en/contact/ | Yalnızca form → önce kısa tanıtım, sonra RFQ |

**Dalga 1 kanal kalitesi:** K-A 1 · K-B 3 · K-C 1 · K-D 1 · K-E 1 · K-X 0

---

## 2. DALGA 2 — B ÖNCELİK (10 tedarikçi)

| # | Tedarikçi | Ülke | Model | Kanal sınıfı | İletişim | Not |
|---|---|---|---|---|---|---|
| 8 | **Vidigal Wines S.A.** | PT | A | **K-E** | https://wineparis.com/newfront/exhibitor/vidigal-wines-sa | Kurumsal site yaş duvarı arkasında (porta6.com'a yönlendiriyor) |
| 9 | **Plaimont** | FR | A | **K-D / K-C** | https://www.plaimont.com/en/contact · +33 5 62 69 62 87 | **En güçlü ürün eşleşmesi** (Colombard-Chardonnay) |
| 10 | **Purcari Wineries Group** | MD | A | **K-B** | purcari@purcari.wine · +373 22 856 022 | Halka açık şirket → yatırımcı ilişkileri ikinci kanal olarak kullanılabilir |
| 11 | **Félix Solís Avantis** | ES | A | **K-D** | https://www.felixsolis.com/en/contact/ | Doğrudan ihracat adresi yayınlanmamış |
| 12 | **Viña Maria** | ES | B | **K-D** | https://www.vinamaria.es/private-label-oem-wine | Fiyat listesi "talep edilebilir" → RFQ'da doğrudan istenir |
| 13 | **Vinicola Vedovato Mario SRL** | IT | B | **K-B** | info@vinicolavedovato.com · +39 049 5796432 | Incoterm esnekliği → RFQ 3.16'nın en iyi test adayı |
| 14 | **Antawara Vineyards** | CL | B | **K-D** | https://antawara-wines.cl/contact/ | Yalnızca form |
| 15 | **Origin Wine** | ZA | B | **K-B** | info@originwine.co.za · +44 1295 221 340 | UK merkezli → İngilizce yanıt hızı yüksek olabilir |
| 16 | **Parras Wines** | PT | A | **K-D** | https://parras.wine/en/ | Grup içinde kendi şişeleme tesisi (Goanvi) |
| 17 | **Zidela Worldwide Wines** | ZA | B | **K-C** | +27 21 880 2936 (dizin kaydı) | ⚠️ E-posta doğrulanamadı; kurumsal site yaş duvarı arkasında |

---

## 3. DALGA 3 — C ÖNCELİK (9 tedarikçi — RFQ öncesi ek doğrulama)

| # | Tedarikçi | Ülke | Kanal sınıfı | İletişim | RFQ'dan ÖNCE cevaplanması gereken |
|---|---|---|---|---|---|
| 18 | **Scheid Family Wines** | US | K-B | contact_sfw@scheidfamilywines.com · +1 831 455 9990 | ABD→TR hattı açılabilir mi |
| 19 | **O'Neill Vintners & Distillers** | US | K-D | https://oneillwine.com/contact | İhracat departmanı var mı |
| 20 | **Bronco Wine Company** | US | K-D | https://www.broncowine.com/connect/contact | **Private label programı var mı** (`EV-2026-08-10-466` — kanıtlanamadı) |
| 21 | **Geo Vino Wines** | US/çok menşeli | K-B | info@geovinowines.com · +1 415 332 8466 | ABD dışına ihracat yapıyor mu |
| 22 | **Kingston Estate Wines** | AU | K-C | +61 8 8583 0500 | Şişelenmiş bitmiş ürün MOQ'su nedir (dökme ağırlıklı) |
| 23 | **Viña Luis Felipe Edwards** | CL | K-E | https://www.winesofchile.org/member/luis-felipe-edwards/ · +56 2 2433 5700 | ⚠️ Kurumsal site **HTTP 404** — güncel adres bulunmalı |
| 24 | **FMS Wine Marketing** | ZA | K-B | info@fms-wine-marketing.co.za | Hangi üretici adına çalışıyor, marj nerede |
| 25 | **Spanish Origin** | ES | K-B | info@spanishorigin.es | **Üretici mi aracı mı** |
| 26 | **Clark Estate** | NZ | K-B | info@clarkestate.com · +64 3 579 4752 | RFQ **gönderilmemeli** — ülke kapsam dışı; kayıt bir MOQ referansıdır |

---

## 4. GÖNDERİM PLANI (öneri — karar başkanındır)

| Aşama | Kim | Adet | Amaç | Beklenen süre |
|---|---|---|---|---|
| **Ön koşul** | `gumruk-vergi-uzmani` | — | `T-401`/`T-462` kapanışı → RFQ 6.1 daraltılır | ? |
| **Ön koşul** | `turkiye-pazar-kasifi` | — | `T-464` → Model A adaylarının TR'de temsilcisi var mı | ? |
| **Dalga 1** | `global-sourcing-kasifi` | 7 | A önceliğe RFQ v2.1; hedef ≥4 cevap | 2–3 hafta |
| **Takip 1** | `global-sourcing-kasifi` | 7 | Eksik alanlar için takip e-postası (şablon §3) | +1 hafta |
| **Dalga 2** | `global-sourcing-kasifi` | 10 | Dalga 1'den <4 cevap gelirse **veya** karşılaştırma tabanını genişletmek için | +2 hafta |
| **Dalga 3** | `global-sourcing-kasifi` | 9 | Yalnızca ön doğrulaması yapılanlara | koşullu |

**Hedef:** `90-karar/tur-2-preflight-housekeeping.md` §D.3'e göre **G2 gate'i
"gerçek RFQ cevabı (≥5 tedarikçi)" ile açılır.** Dalga 1'in 7 hedefi bu eşiği
karşılamak üzere seçilmiştir; %70 cevap oranı varsayımıyla ~5 cevap eder.
**Bu bir `ASSUMPTION`'dır** — cevap oranı hakkında hiçbir kanıtımız yoktur ve
`rfq-alan-kontrolu.md` §5.1 uzun şablonun cevap oranını **düşürebileceğini**
zaten uyarmaktadır.

---

## 5. GÖNDERİM DİSİPLİNİ (bağlayıcı)

1. **Aynı metin, herkese.** Metin değişirse teklifler karşılaştırılamaz (`rfq-template.md` §0.8).
2. **Fiyat EXW ve FOB olarak AYRI istenir**; tek fiyat gelirse ve Incoterm yazılı
   değilse `UNKNOWN` yazılır, tahmin edilmez.
3. **Gelen her cevap için ayrı kanıt kartı** açılır, `quote_type` = `INDICATIVE`
   veya `FIRM_OFFER` olarak işaretlenir. Teklif geçerlilik tarihi kartın `ttl`'i olur.
4. **Kişisel/özel iletişim kanalı kullanılmaz.** Yalnızca kurumsal kanallar.
   Üçüncü taraf dizinlerden toplanan e-postalar (ör. `ignacio.edwards@lfewines.com`)
   **doğrulanmış kurumsal kanal sayılmaz** ve önce firma sitesinden teyit edilir.
5. **Cevap gelmezse "cevap gelmedi" yazılır**, tahmin üretilmez.
6. **Numune talebi ayrı adımdır** — RFQ 7.1–7.5 cevapları gelmeden numune sipariş edilmez.

---

## 6. BU LİSTENİN ZAYIF NOKTALARI (dürüst envanter)

| # | Zayıflık | Etki |
|---|---|---|
| 1 | **26 kaydın yalnızca 1'inde doğrudan ihracat e-postası var** (Cantina Danese) | Cevap oranı düşebilir; genel `info@` adresleri satın alma taleplerinde kaybolur |
| 2 | **6 kayıtta yalnızca web formu var** | Form karakter limiti nedeniyle RFQ eklenemez; iki aşamalı temas gerekir |
| 3 | **3 kurumsal site erişilemedi** (Interbrosa 503, LFE 404, Zidela/Vidigal yaş duvarı) | Kanal doğrulaması üçüncü taraf kaynaklara dayanıyor; adres eskimiş olabilir |
| 4 | **Hiçbir kayıtta muhatap kişi adı yok** | RFQ "Dear Export Sales Team" ile gider; kişisel muhatapsız RFQ'ların cevap oranı tipik olarak düşüktür (**bu bir sektör beklentisidir, kanıt değildir**) |
| 5 | **Türkiye'ye ihracat geçmişi 26 kaydın hiçbirinde doğrulanmadı** | İlk temasta "Türkiye" bilinmeyen bir pazar olarak karşılanabilir; RFQ 6.6 bunu ölçer |
