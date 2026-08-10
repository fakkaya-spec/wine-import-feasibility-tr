# FORWARDER CONTACT PACK — hedef listesi, gönderilmedi

```yaml
sahibi:                navlun-lojistik-uzmani
tur:                   TUR 3.25 — FORWARDER RFQ PAKETI (§15)
tarih:                 2026-08-10
hedef_sayisi:          5
gonderim_durumu:       HAZIR — GONDERILMEDI
dis_iletisim_yapildi:  false
mesaj_gonderildi:      false
rfq_metni:             40-lojistik/forwarder-rfq.md (v1.0)
response_sheet:        40-lojistik/forwarder-response-sheet.md
hedef_ticket:          T-304 (CRITICAL, OPEN)
```

> ## ⛔ HİÇBİR FİRMAYA TEMAS EDİLMEDİ
>
> Aşağıdaki iletişim bilgileri **firmaların kendi kamuya açık kurumsal
> sayfalarından** okunmuştur (erişim tarihi 2026-08-10). Hiçbirine e-posta,
> form veya telefon teması yapılmamıştır.
>
> **Sahte firma / sahte kişi / sahte e-posta üretilmemiştir.** Doğrulanamayan
> alan `NEEDS_CONTACT` olarak işaretlidir ve **boş bırakılmıştır** — tahmin
> edilmemiştir.

---

## 0. HEDEF SEÇİM KRİTERİ

`T-304`'ün kapanma koşulu **3 forwarder'dan yazılı kotasyondur.** Bu yüzden
hedef sayısı geniş tutulmadı; **5 kaliteli hedef** seçildi. Seçim kriterleri:

| Kriter | Neden |
|---|---|
| **Türkiye varışlı deniz ithalatı** yapıyor olması | RFQ'nun tamamı TR varışlı |
| **LCL konsolidasyonu** yapabilmesi | Q1 (5.000 şişe) bu olmadan fiyatlanamaz |
| **Akdeniz menşei** (ES/PT/IT) kapsaması | Block A'nın 3 lane'i |
| **Uzak menşe** (CL/ZA/US/AU) kapsayabilmesi | Block A4/A5 ve Block C |
| **Gıda / içki / şarap** yükü tecrübesi | kırılma, sıcaklık, Food Quality Container kalemi |
| Kanal kalitesi (doğrudan e-posta > form > telefon) | gönderim hızı |

**Bilinçli çeşitlilik:** liste üç tip forwarder içerir —
(a) **şarap ihtisas** forwarder'ı, (b) **Türk** forwarder (varış tarafı ve
antrepo/iç nakliye bilgisi güçlü), (c) **dijital/global** forwarder (TUR 2
kotasyonlarının kaynağıyla süreklilik). Aynı tipten 5 firma seçmek, aynı
yanlılığı 5 kez satın almak olurdu.

---

## 1. HEDEF LİSTESİ

| # | company | contact | routes | quote requested | status |
|---|---|---|---|---|---|
| **F-1** | **Hillebrand Gori** *(DHL grubu; şarap/içki ihtisas forwarder'ı; İstanbul ofisi mevcut)* | Kotasyon formu: `hillebrandgori.com/forms/transport-quote-request` · Destek: `hillebrandgori.com/support` · **Doğrudan e-posta/telefon: `NEEDS_CONTACT`** (İstanbul ofis sayfası 2026-08-10'da HTTP 404 döndü) | Block A (ES·PT·IT·CL·ZA) + Block B + Block C — küresel şarap ağı | Q1 LCL · Q2 20DV · Q3 40HC · §9 thermal liner + reefer + sigorta | **READY — NOT SENT** (kanal: web formu) |
| **F-2** | **Arkas Lojistik A.Ş.** *(TR; ~100.000+ TEU/yıl; LCL konsolidasyonu Shipeedy ile; İstanbul·İzmir·Mersin ofisleri)* | `info@arkaslojistik.com.tr` · +90 216 560 0060 (İstanbul-Orhanlı) · çağrı merkezi 0850 222 7527 | Block A (Akdeniz güçlü) + **Block B (İzmir/Mersin karşılaştırması için en uygun hedef)** | Q1 · Q2 · Q3 · §7 çekici/şasi darası · §9 antrepo | **READY — NOT SENT** (kanal: doğrudan e-posta) |
| **F-3** | **Sertrans Logistics** *(TR; FCL + LCL; Arnavutköy/İstanbul)* | `info@sertrans.com.tr` · +90 212 703 3500 · 0850 288 8181 | Block A + Block B | Q1 · Q2 · Q3 · §9 antrepo + devanning | **READY — NOT SENT** (kanal: doğrudan e-posta) |
| **F-4** | **Flexport** *(dijital forwarder; TUR 2'deki 10 LCL kotasyonunun kaynağı)* | `hello@flexport.com` · +1 415 231 5252 · `flexport.com/company/contact/` | Block A + Block C (**CL·ZA·US-CA·AU uzak menşelerde TUR 2'de fiyat verebilen tek kaynak**) | Q1 · Q2 · Q3 — **ayrıca TUR 2 LCL kotasyonlarının yazılı teyidi** (`T-913` Ayak A) | **READY — NOT SENT** (kanal: doğrudan e-posta / portal) |
| **F-5** | **Mars Logistics** *(TR; kendi ofisleri Barcelona · Madrid · Trieste; Mersin/İskenderun/İzmir şubeleri)* | İletişim sayfası: `marslogistics.com/tr/iletisim` (EN: `/en/contact-us`) · **e-posta/telefon: `NEEDS_CONTACT`** (site 2026-08-10'da HTTP 403 döndü, doğrulanamadı) | **Block A1 (ES) ve A3 (IT) için en güçlü hedef** — İspanya ve İtalya'da kendi ofisi var | Q1 · Q2 · Q3 · §5.2 origin local charges tarifesi (ES + IT) | **NEEDS_CONTACT — NOT SENT** |

---

## 2. DURUM ÖZETİ

| status | adet | firmalar |
|---|---|---|
| **READY — NOT SENT** (doğrulanmış doğrudan e-posta) | **3** | F-2 Arkas · F-3 Sertrans · F-4 Flexport |
| **READY — NOT SENT** (yalnızca web formu) | **1** | F-1 Hillebrand Gori |
| **NEEDS_CONTACT** (kanal doğrulanamadı) | **1** | F-5 Mars Logistics |
| Toplam hedef | **5** | |

> **`T-304` için kritik okuma:** doğrudan e-posta ile ulaşılabilen **3** hedef
> vardır ve ticket'ın kapanma koşulu tam olarak **3 yazılı kotasyondur.**
> Yani **hata payı sıfırdır**: bu üçünden biri cevap vermezse koşul sağlanmaz.
> Bu yüzden F-1 (form) ve F-5 (`NEEDS_CONTACT`) yedek değil, **planın parçası**
> olarak listelenmiştir; F-5'in kanalı gönderim öncesi bulunmalıdır.

---

## 3. KANAL DOĞRULAMA KAYDI

Aşağıdaki bilgiler **firmaların kendi kurumsal sayfalarından** 2026-08-10
tarihinde okunmuştur. Bu tur `10-evidence/index.csv` **dokunma listesindedir**;
bu nedenle kanıt kartı **açılmamıştır**. Gönderim onayı çıkarsa her satır için
kart açılmalıdır (`tier: T4` — kurumsal kaynak, `ttl: 180d`) → **`T-821`**.

| # | Doğrulanan alan | Kaynak sayfa | Erişim | Sonuç |
|---|---|---|---|---|
| F-1 | Kotasyon formu URL'si; İstanbul ofisinin varlığı | hillebrandgori.com (ofis bulucu + form) | 2026-08-10 | Form URL **doğrulandı**; İstanbul ofis sayfası **HTTP 404** → doğrudan e-posta/telefon **alınamadı** |
| F-2 | E-posta + telefon + ofis | arkaslojistik.com/en/contact | 2026-08-10 | **Doğrulandı** |
| F-3 | E-posta + telefon + adres | sertrans.com.tr/en/contact-us | 2026-08-10 | **Doğrulandı** |
| F-4 | E-posta + telefon + iletişim sayfası | flexport.com/company/contact/ | 2026-08-10 | **Doğrulandı** |
| F-5 | İletişim sayfası URL'si | marslogistics.com/tr/iletisim | 2026-08-10 | Sayfa **HTTP 403** → e-posta/telefon **alınamadı** → `NEEDS_CONTACT` |

> **Dürüstlük notu:** F-1 ve F-5 için "muhtemelen `info@…`" biçiminde bir adres
> **türetilmemiştir.** Kurumsal e-posta kalıbı tahmin etmek bu repoda veri
> uydurmakla aynı şeydir.

---

## 4. GÖNDERİM PLANI *(uygulanmadı — onay bekliyor)*

| Adım | İçerik | Ön koşul |
|---|---|---|
| 0 | **Kurucu preview + açık onay** | — |
| 1 | `<PLACEHOLDER>` alanlarının doldurulması (firma, imza, tarih, deadline) | onay |
| 2 | F-2, F-3, F-4'e **aynı anda, aynı metinle** e-posta + EK-1 | adım 1 |
| 3 | F-1'e web formu üzerinden kısa tanıtım + RFQ'nun e-posta ile gönderilmesi talebi | adım 1 |
| 4 | F-5 için kanal tespiti (`NEEDS_CONTACT` → kanal), sonra adım 2 | adım 1 |
| 5 | Gelen her teklif → kanıt kartı + `99-ops/veri-tazeligi.md` girişi | teklif |
| 6 | En az 3 kalem dökümlü yazılı teklif → `T-304` cevap bölümü doldurulur | adım 5 |

**Önerilen cevap süresi:** 10 iş günü. Gerekçe: kalem dökümlü kotasyon,
forwarder'ın menşe ofisinden local charge tarifesi toplamasını gerektirir;
48 saatlik bir deadline "all-in tek rakam" cevabını **davet eder** — ki §5.3
tam olarak onu reddediyor.

---

## 5. HEDEF SEÇİLMEYENLER VE NEDENİ

Bu bir **kapsamlı tarama değildir** (görev tanımı: *"az sayıda kaliteli hedef
yeterli"*). Aşağıdakiler bilinçli olarak **bu listeye alınmadı**, ama gönderim
onayı çıkar ve 3 cevap toplanamazsa **ikinci dalga adayıdır**:

| Aday tipi | Örnek | Neden ilk dalgada değil |
|---|---|---|
| Global 3PL Türkiye ofisleri | Kuehne+Nagel TR, DB Schenker TR, DSV TR | Kanal doğrulaması yapılmadı; ilk dalga için gerekmedi |
| Diğer büyük Türk forwarder'lar | Ekol, Barsan, Omsan, Borusan | Aynı |
| Menşe ülke konsolidatörleri (ES/IT çıkışlı) | — | Türkiye varış tarafını bilmiyorlar; varış kalemleri eksik gelir |
| Armatör doğrudan (Hapag-Lloyd, MSC, Arkas Line) | — | Armatör **origin/destination local charge tarifesini zaten yayımlıyor** (`EV-2026-08-10-313 … -319`) — bizde eksik olan **navlunun kendisi** ve **kalem birleşimi**, o da forwarder işi |

> **Armatör notu:** İspanya origin charge'larını (349–554 EUR) zaten
> **yayımlanmış armatör tarifesinden** biliyoruz. Yani armatöre sormanın
> marjinal getirisi düşüktür; forwarder'a sormanın getirisi yüksektir.
