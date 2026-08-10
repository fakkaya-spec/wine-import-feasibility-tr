# TUR 3.25 — SUPPLIER RFQ PAKETİ — `global-sourcing-kasifi` RAPORU

```yaml
ajan:                  global-sourcing-kasifi
tur:                   TUR 3.25 §2–§8, §14 — SUPPLIER RFQ PAKETİ
tarih:                 2026-08-10
durum:                 SUBMITTED
yeni_tedarikci_arama:  YOK — TOP 10 sabit; yeni supplier/ülke/fiyat araştırması YAPILMADI
web_erisimi:           YALNIZCA iletişim doğrulaması (10 kurumsal sayfa okundu)
dis_iletisim:          NONE — hiçbir üreticiye e-posta / form / mesaj GÖNDERİLMEDİ
yeni_evidence:         EV-2026-08-10-901 … -910 (10 adet)
yeni_ticket:           T-885 … T-893 (9 adet)
uretilen_dosya:        top-10-contact-pack.md · rfq-mail-existing-brand.md ·
                       rfq-mail-private-label.md · rfq-response-sheet.md
dokunulmayan:          10-evidence/index.csv · 99-ops/{capraz-ipuclari,celiskiler,acik-sorular}.md ·
                       99-ops/tickets/INDEX.md · 80-model/ · 60-pazar/ · 70-kanal/ ·
                       30-vergi-gumruk/ · 40-lojistik/ · git
```

---

## 1. YÖNETİCİ ÖZETİ

TOP 10 tedarikçinin **hiçbirine temas edilmeden**, gönderime hazır bir RFQ
paketi kuruldu: iki mail varyantı (A — existing brand distribution, B — private
label), tek bir yapılandırılmış response sheet ve §14 formatında bir contact
pack. **10 hedefin iletişim kanalı 2026-08-10'da tek tek yeniden doğrulandı**
(`EV-2026-08-10-901…-910`): **7 `READY_TO_SEND`, 3 `NEEDS_CONTACT`, 0 `BLOCKED`**.

En kritik tek bulgu **ürün veya fiyat tarafında değil, kanal tarafındadır**:
`Bodegas San Valero` ve `Casa Santos Lima` için ilk kez **doğrudan kurumsal
e-posta** doğrulandı (K-E→K-B ve K-D→K-B), buna karşılık `Vidigal Wines`'ın
statüsü **K-E'den K-X'e düştü** — havuzdaki tek doğrulanmış kanalsız hedef.
`Interbrosa`, havuzun **en düşük doğrulanmış MOQ'suna sahip tedarikçisi**
(3.000 şişe), iki gün üst üste iki domainde **HTTP 503** vermektedir
(`T-889`, HIGH).

**Bu turda hiçbir fiyat, hiçbir MOQ, hiçbir teklif üretilmedi.** Havuzda hâlâ
**0 adet `FIRM_OFFER`** vardır ve bu paketin tek işi o sayıyı 0'dan yukarı
çıkarmanın önünü açmaktır.

---

## 2. BULGULAR

### B-1: Bodegas San Valero — doğrudan kurumsal e-posta doğrulandı (kanal yükselmesi)

```yaml
claim:          "Bodegas San Valero kurumsal iletişim sayfasında bsv@sanvalero.com genel kurumsal e-postası yayında; RFQ fuar profili üzerinden dolaylı gönderilmek zorunda değil"
value:          "bsv@sanvalero.com · +34 976 620 400"
unit:           iletisim_kanali
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-906
effective_date: -
katman:         -
```

**Gerekçe:** `rfq-contact-pack.md` §1'de bu tedarikçi **K-E** (yalnızca Wine
Paris fuar profili) olarak kayıtlıydı ve bu, havuzdaki **tek ikili aday**
(Model A + Model B) için en zayıf halkaydı. Kurumsal sayfada ihracat
departmanına **ayrılmış** bir adres yok, ama genel kurumsal adres var — bu
`K-B`'dir ve RFQ doğrudan gönderilebilir.

### B-2: Casa Santos Lima — doğrudan kurumsal e-posta doğrulandı (kanal yükselmesi)

```yaml
claim:          "Casa Santos Lima kurumsal iletişim sayfasında geral@casasantoslima.com yayında; iki aşamalı form teması gerekmiyor"
value:          "geral@casasantoslima.com · +351 263 760 621"
unit:           iletisim_kanali
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-907
```

**Gerekçe:** Önceki kayıt **K-D** (yalnızca web formu) idi ve Model A'nın **en
olgun** adayına RFQ eki gönderilememesi anlamına geliyordu. Artık response sheet
ek olarak gönderilebilir.

### B-3: Vidigal Wines — doğrulanmış iletişim kanalı YOK (statü düşüşü)

```yaml
claim:          "Vidigal Wines için hiçbir kurumsal kanaldan iletişim bilgisi doğrulanamadı; alan adı porta6.com'a yönleniyor, fuar profili veri döndürmüyor, IWSC profili 403"
value:          "ILETISIM KANALI DOGRULANAMADI"
unit:           iletisim_kanali
status:         UNKNOWN
tier:           T4
evidence_id:    EV-2026-08-10-908
```

**Gerekçe:** Dört bağımsız kanal denendi (kurumsal alan adı, porta6.com,
Wine Paris katılımcı sayfası ×2, IWSC profili). Üçüncü taraf dizinlerde telefon
ve adres görünüyor **ama kullanılmadı**: `rfq-contact-pack.md` §5/4 bunları
doğrulanmış kanal saymıyor. **Bu bir negatif bulgudur, eksik araştırma
değildir** — ama Vidigal'ın **beyaz value portföyü de zaten `UNKNOWN`**
olduğu için, kanal bulunsa bile kart ürün uyumundan düşebilir. `T-888`.

### B-4: Interbrosa — iki domainde kesintisiz erişilemezlik

```yaml
claim:          "Interbrosa kurumsal sitesi 2026-08-10'da www.interbrosa.es → 301 → www.interbrosa.com yönlendirmesiyle birlikte HER İKİ DOMAINDE de HTTP 503 dönüyor"
value:          "HTTP 503 (iki domain, iki gün üst üste)"
unit:           iletisim_kanali
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-903
```

**Gerekçe:** `EV-2026-08-10-467` (TUR 2) zaten 503 kaydetmişti; bugünkü gözlem
bunu **genişletiyor** — `.es`'in `.com`'a yönlendiği ve o domainin de kapalı
olduğu ilk kez görüldü. Firmanın kapandığı **iddia edilmiyor**; ama
`info@interbrosa.es` adresi **bugün teyit edilemedi** ve bounce riski gerçektir.
Etkisi büyüktür: **havuzun doğrulanmış en düşük MOQ'su (3.000 şişe) buradadır**.
`T-889` (HIGH).

### B-5: The Wine Factory — iki tesis müdürünün adı public, ama e-posta yok

```yaml
claim:          "The Wine Factory iletişim sayfasında yayınlanmış e-posta adresi yoktur; kanal Google Forms formu + iki tesis telefonudur; iki tesis müdürünün adı kamuya açıktır"
value:          "Mr Romain Roux (Gornac) · Mr Laurent Gauzi (Valros) — Google Form + 2 telefon"
unit:           iletisim_kanali
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-904
```

**Gerekçe:** Havuzda **muhatap kişi adının public olduğu tek tedarikçidir** —
ve aynı anda **e-postası olmayan** tedarikçidir. İkisi bir arada iki aşamalı
temas gerektirir (`T-886`). Sitede *"minimum 3600 bottles"* ve *"48h içinde
dönüş"* beyanları **hâlâ yayında** — `EV-2026-08-09-410` bu turda dolaylı
olarak teyit edilmiş oldu.

### B-6: Harland — yayınlanmış fiyat kademeleri ve MOQ 2026-08-10'da hâlâ yayında

```yaml
claim:          "Harland'ın /private-label sayfasında Entry $2.85+ / Mid $5.00+ / Premium $8.50+ kademeleri, 6.000 şişe MOQ ve '20ft konteynerde 14.112 şişe (slipsheet)' beyanı 2026-08-10 itibarıyla hâlâ yayında"
value:          "2.85+ / 5.00+ / 8.50+ · MOQ 6.000 şişe · 14.112 şişe/20ft"
unit:           "para birimi BELİRTİLMEMİŞ ($) / şişe · adet"
status:         FACT   # sayfanın yayında olduğu FACT'tir — FİYATIN KENDİSİ hâlâ PUBLIC_INDICATIVE
tier:           T4
evidence_id:    EV-2026-08-10-901   # (fiyatın kendisi: EV-2026-08-10-451/-452)
katman:         "BELİRSİZ — L0 veya L1 (C-461 açık)"
```

**Gerekçe:** Bu bir **fiyat teyidi değildir**. Yalnızca gösterge fiyatın
**hâlâ yayında olduğu** doğrulanmıştır. `quote_class` hâlâ `PUBLIC_INDICATIVE`,
para birimi hâlâ `UNKNOWN`, katman hâlâ `C-461` ile açık. **Bu ayrım korunmuştur
ve mailde Harland'a fiyat rakamı tekrar edilmemiştir** — yalnızca *"her fiyat
için para birimi ve Incoterm belirtin"* denmiştir.

### B-7: Purcari — iki e-posta public, biri RFQ için kullanılamaz

```yaml
claim:          "Purcari kurumsal iletişim sayfasında purcari@purcari.wine ve investor.relations@purcari.wine yayında"
value:          "purcari@purcari.wine (RFQ) · investor.relations@purcari.wine (KULLANILMAZ)"
unit:           iletisim_kanali
status:         FACT
tier:           T4
evidence_id:    EV-2026-08-10-910
```

**Gerekçe:** `rfq-contact-pack.md` §2 *"halka açık şirket → yatırımcı ilişkileri
ikinci kanal olarak kullanılabilir"* demişti. **Bu turda o öneriyi
uygulamıyorum:** yatırımcı ilişkileri kanalı **denetlenmiş şirketin yatırımcı
iletişim yükümlülüğü** için vardır; oraya ticari bir satın alma talebi
göndermek uygun değildir ve firmayı yanlış departmana yönlendirir. Kayıtta
**eskalasyon kanalı** olarak tutuldu, gönderim listesine **konmadı**.

### B-8: RFQ paketinin kendisi — v2.2 disiplini korunarak hacim merdivenine genişletildi

```yaml
claim:          "RFQ v2.2'nin SUMMARY SHEET S1–S27 yapısı ve M1…M8 zorunlu alanları korunarak, tek hacimli fiyat sorusu 5 kademeli bir price-volume curve sorusuna genişletildi ve iki kalite seviyesi (Q1/Q2) eklendi"
value:          "5 kademe × 2 Incoterm × 2 kalite seviyesi = 20 fiyat hücresi"
unit:           soru_yapisi
status:         FACT
tier:           -
evidence_id:    -   # kendi üretimimiz, kanıt değil
```

**Gerekçe:** §0 talimatı tek hacim fiyatı istemeyi yasakladı. `rfq-template.md`
soru 3.7 zaten kademe soruyordu ama **SUMMARY SHEET'te tek satır (S11/S12)**
olarak duruyordu — yani tedarikçinin tek fiyat vermesi **yapısal olarak
kolaydı**. Response sheet'te `BLOCK V` bunu **doldurulacak bir matrise**
çevirdi. **100.000 şişe kademesi §0 gereği çıkarıldı.**

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | **10 hedefin 9'unda muhatap kişi adı** | Kurumsal sitelerde yayınlanmıyor | MEDIUM | Yalnızca temas sonrası (S/C-7 sorusu: *"name, position, direct e-mail of the person responsible"*) |
| 2 | **Vidigal Wines'ın doğrulanmış iletişim kanalı** | 4 kanal denendi, hiçbiri veri döndürmedi | MEDIUM | `T-888` — yaş duvarı arkası okuma / fuar kataloğu kaydı / ihracat kurumu dizini; **üçü de onay gerektirir** |
| 3 | **Interbrosa'nın faal olup olmadığı** | İki domain de 503 | **HIGH** | `T-889` — gönderim denemesi bir testtir; bounce sonucu kanıta yazılır |
| 4 | **TWF ve Plaimont'un kurumsal e-postası** | Yayınlanmıyor | MEDIUM | `T-886` / `T-887` — iki aşamalı temas, ayrı onay |
| 5 | **Tüm 10 tedarikçinin fiyatı, MOQ'su (5'inde), ödeme şartı, lead time'ı** | **Teklif alınmadı — bu turda alınamazdı** | **CRITICAL** | Yalnızca gerçek RFQ cevabı |
| 6 | **Cevap oranı** | Hiçbir gönderim yapılmadı; sektör beklentisi kanıt değildir | HIGH | İlk dalganın kendisi ölçer (`rfq-zorunlu-alanlar.md` §4.4 metriği) |
| 7 | **Cantina Danese'nin Türkiye ilişkisinin canlı olup olmadığı ve münhasırlık içerip içermediği** | Tek bir online perakendeci kataloğu; ürün stokta değil | HIGH | `T-565` (`turkiye-pazar-kasifi`) + mailin özel sorusu |
| 8 | **Purcari'nin tek konteynerde iki menşe birleştirmesinin gümrük sonucu** | **Benim alanım değil** | MEDIUM | `T-891` (`gumruk-vergi-uzmani`) |
| 9 | **Gönderen tüzel kişilik ve tüm `<>` alanları** | Yatırımcı kararı | **HIGH** | `T-892` |

---

## 4. ÇELİŞKİLER

Bu turda **yeni bir kaynak çelişkisi tespit edilmedi.** Ancak bir **iç
tutarsızlık** üretildi ve gizlenmedi:

| id | Kaynak A | Kaynak B | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **(iç)** | `rfq-template.md` v2.2 §6 notu: menşe belgesinin *"around 12%"* etkisi **üreticiye açıkça yazılır** | **TUR 3.25 §6 talimatı:** %11,765 etkisi **açıklanmaz** | v2.2 o cümleyi M6 doluluğunu artırmak için **bilerek** koymuştu; §7 disiplini onu yasaklıyor. İki kural aynı anda uygulanamaz | **Talimat uygulandı** (cümle çıkarıldı), çelişki `T-890` ile başkana taşındı |

> `99-ops/celiskiler.md` dosyasına **yazmadım** — dokunulmaması söylenen
> dosyalar arasında. Çelişki `T-890` ticket'ı üzerinden taşınmıştır.

**Devam eden (bu turda çözülmeyen) çelişkiler:** `C-461` (Harland'ın tek
fiyatının L0 mu L1 mi olduğu) ve `C-462`/`C-401` (MOQ birimi) hâlâ açıktır ve
RFQ'nun cevaplaması hedeflenen sorulardır.

---

## 5. MODEL GİRDİLERİ

**Bu rapordan `80-model/inputs/*.yaml` dosyalarına giden HİÇBİR DEĞER YOKTUR.**

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

**Gerekçe:** Bu tur bir **hazırlık turudur**. İletişim kanalı bilgisi modele
girmez; fiyat/MOQ/ödeme/lead time verisi ise **hâlâ yoktur** (0 `FIRM_OFFER`).
`80-model/` dizinine dokunulmadı.

**Teklif geldiğinde nereye gireceği** `rfq-template.md` §0 eşleme tablosunda ve
`rfq-response-sheet.md` §0.3'te tanımlıdır — o eşleme **değiştirilmedi**.

---

## 6. §7 SIZINTI DENETİMİ — GÖNDERİLECEK HER METİN İÇİN

Denetlenen üç metin: **varyant A gövdesi**, **varyant B gövdesi**,
**response sheet'in gönderilecek kısmı** (ayrıca 13 adet tedarikçiye özel
tek cümle).

| # | Yasaklı bilgi (§7) | Varyant A | Varyant B | Response sheet | Özel cümleler |
|---|---|---|---|---|---|
| 1 | **799 TL hedef raf** | YOK | YOK | YOK | YOK |
| 2 | **699 / 899 merdiveni** | YOK | YOK | YOK | YOK |
| 3 | **MAX CIF / `MAXIMUM STRUCTURAL BUY PRICE`** (272,83 · 240,73) | YOK | YOK | YOK | YOK |
| 4 | **`RFQ TARGET CEILING X/Y`** (200,98 · 290,51 · 256,34) | YOK | YOK | YOK | YOK |
| 5 | **walk-away price** | YOK | YOK | YOK | YOK |
| 6 | **importer target margin** | YOK | YOK | YOK | YOK |
| 7 | **retailer margin varsayımları** | YOK | YOK | YOK | YOK |
| 8 | **internal contribution target** | YOK | YOK | YOK | YOK |
| 9 | **tedarikçi sıralaması** ("siz N. sıradasınız") | YOK | YOK | YOK | YOK |
| 10 | **rakip tedarikçi fiyatları** | YOK | YOK | YOK | YOK |
| 11 | **%11,765 / 32,10 TRY menşe belgesi etkisi** | **ÇIKARILDI** (v2.2'den geri adım) | **ÇIKARILDI** | **KONMADI** | YOK |
| 12 | **`IMPLIED_BREAKEVEN_USDTRY` değerleri** | YOK | YOK | YOK | YOK |
| 13 | Harland'ın kendi yayınladığı **2,85** rakamı | — | **tekrar edilmedi** — teyit sorusu rakamsız soruldu | — | rakamsız |

**Yöntem:** metinler regex ile tarandı
(`799|699|899|272,83|240,73|200,98|290,51|256,34|11,765|32,10|walk.?away|MAX_CIF|ceiling`).
**Tüm eşleşmeler dosyaların GÖNDERİLMEYEN iç denetim bölümlerindedir**; hiçbiri
"GÖNDERİLECEK METİN" bloklarının içinde değildir.

### 6.1 Söylenmesine izin verilen tek şey — ve fiilen söylenen

> *"a company based in Türkiye evaluating a long-term import (and distribution)
> programme for still wine in the price-performance segment of the Turkish
> market"*

**Tek cümle, her iki varyantta da ilk paragrafta.** Şirket hakkında başka
hiçbir detay verilmemiştir (§8 talimatı).

### 6.2 Dolaylı sızıntı riski — dürüst not

**Hacim merdiveninin kendisi bir bilgi verir:** 5.000'den başlayıp 50.000'de
duran bir merdiven, karşı tarafa *"bu alıcı büyük değil"* der. Bunu gizlemenin
yolu yoktur — hacim sorulmadan fiyat eğrisi öğrenilemez. **100.000'in
sorulmaması** bu sinyali biraz daha güçlendirir; ama alternatifi (sahip
olmadığımız bir hacmi ima etmek) hem yanlış hem de ilk teklifte güvenilirlik
kaybettirir. **Bu bilinçli bir takastır ve burada yazılmıştır.**

---

## 7. NE **YAPILMADI** — SINIRLAR

| Yapılmayan | Neden |
|---|---|
| **Hiçbir e-posta gönderilmedi** | §0 — gönderim `T-885` onayına bağlı |
| **Hiçbir web formuna hiçbir şey yazılmadı** | Forma yazılan her cümle bir dış temastır (TWF, Plaimont, Vidigal) |
| **Hiçbir fuar platformu mesajı açılmadı** | aynı |
| **Yeni tedarikçi / ülke / fiyat araştırması** | §0 yasağı — TOP 10 sabit |
| **Vergi oranı, tercihli tarife sonucu** | Alan dışı — `gumruk-vergi-uzmani`; belge adları onun doğruladığı hâliyle **alıntılandı** |
| **Navlun tutarı** | Alan dışı — `navlun-lojistik-uzmani`; yalnızca FOB **liman adı** soruldu |
| **Kanal marjı, raf fiyatı** | Alan dışı |
| **Sahte e-posta veya kişi adı** | **Yasak.** Public olmayan her yerde `UNKNOWN` / `NEEDS_CONTACT` yazıldı |
| **Üçüncü taraf dizinlerden alınan Vidigal telefonu/adresi kullanımı** | `rfq-contact-pack.md` §5/4 — doğrulanmış kanal sayılmaz |
| **`investor.relations@purcari.wine`'a gönderim** | Yatırımcı kanalına ticari talep uygun değil |
| **Bulk (dökme) ithalat seçeneğinin üreticiye sorulması** | Hipotez hâlâ mevzuat/vergi tarafında çözülmedi; cevabını değerlendiremeyeceğimiz bir teklife bağlanmayız |
| **`99-ops/celiskiler.md`, `capraz-ipuclari.md`, `index.csv`, `80-model/` vb.** | Dokunma listesi |

---

## 8. AÇILAN TICKET'LAR

| Ticket | Hedef | Impact | Konu |
|---|---|---|---|
| **T-885** | başkan | **CRITICAL** | **Gönderim onayı** — 8 mailin RECIPIENT + SUBJECT + PREVIEW listesi |
| T-886 | başkan | MEDIUM | TWF — e-posta yok; iki aşamalı temas onayı |
| T-887 | başkan | MEDIUM | Plaimont — e-posta yok; departman formu üzerinden temas onayı |
| T-888 | başkan | MEDIUM | Vidigal — doğrulanmış kanal yok; 4 seçenek |
| **T-889** | başkan | **HIGH** | Interbrosa — iki domain 503; en düşük MOQ çapası risk altında |
| T-890 | başkan | MEDIUM | **v2.2'den geri adım:** menşe belgesinin %12 etkisi artık üreticiye söylenmiyor — M6 doluluğu düşebilir |
| T-891 | `gumruk-vergi-uzmani` | MEDIUM | Purcari — tek konteynerde MD + RO/BG karışık menşe sorulursa gümrük sonucu ne |
| **T-892** | başkan | **HIGH** | `<COMPANY>` `<NAME>` … `<DEADLINE>` + RFQ referans şeması — **gönderim ön koşulu** |
| T-893 | başkan | LOW | Numune bütçesi + numunenin gümrük/ÖTV durumu (ayrı adım) |

---

## 9. ÜRETİLEN DOSYALAR

| Dosya | İçerik |
|---|---|
| `50-sourcing/top-10-contact-pack.md` | **Ana çıktı** — §14 tablosu, iletişim doğrulaması, menşe sorusu tam metni, Danese/Purcari özel muameleleri, `NEEDS_CONTACT` gerekçeleri |
| `50-sourcing/rfq-mail-existing-brand.md` | Varyant A tam metni (**319/284 kelime**) + iç §7 denetimi + tedarikçiye özel cümleler |
| `50-sourcing/rfq-mail-private-label.md` | Varyant B tam metni (**350/310 kelime**) + iç §7 denetimi + tedarikçiye özel cümleler |
| `50-sourcing/rfq-response-sheet.md` | Q · V · S1–S27 · OD · PL · EB · SP · C blokları |
| `10-evidence/raw/EV-2026-08-10-901…-910.md` | 10 iletişim doğrulama kanıt kartı |
| `10-evidence/_index-parts/global-sourcing-kasifi-tur325.csv` | Aynı 10 kaydın index parçası (**`index.csv`'ye dokunulmadı**) |
| `99-ops/tickets/T-885…T-893.md` | 9 ticket (**`INDEX.md`'ye dokunulmadı**) |

---

## 10. BU BULGUYU NE ÇÜRÜTÜR?

### 10.1 MOQ gerçekte 3x çıkarsa hangi ülkeler/hedefler elenir?

Bugün **doğrulanmış** MOQ'su olan 4 tedarikçi var. 3x senaryosunda:

| Tedarikçi | Ülke | Bilinen MOQ | **3x** | 5.000'lik pilotla uyum |
|---|---|---|---|---|
| Interbrosa | ES | 3.000 | **9.000** | ❌ düşer |
| The Wine Factory | FR | 3.600 | **10.800** | ❌ düşer |
| Harland | AU | 6.000 | **18.000** | ❌ düşer |
| Cantina Danese | IT | 6.000 | **18.000** | ❌ düşer |
| Corta Hojas · San Valero · Casa Santos Lima · Vidigal · Plaimont · Purcari | CL·ES·PT·PT·FR·MD | **`UNKNOWN`** | — | **ölçülemiyor** |

**Sonuç: 5.000 şişelik pilot, bilinen MOQ'ların hiçbiriyle uyumlu kalmaz.**
Pilot ya 10.000'e çıkar (V bloğunun ikinci kademesi tam da bu yüzden var), ya
tek SKU yerine tek tedarikçide **tek parti** olarak tasarlanır.

**Ülke bazında elenme yanıltıcı olur:** MOQ bir **firma özelliğidir**, ülke
özelliği değil. İspanya "elenmez" — *Interbrosa* elenir. Bu ayrım korunmalıdır,
aksi hâlde 3.000'lik bir İspanyol üreticinin kaybı tüm İspanya hattının
kaybı gibi okunur ki bu yanlıştır.

**Asıl kırılganlık başka yerde:** 10 hedefin **5'inde MOQ hiç bilinmiyor**.
3x senaryosunu test edecek sayıya sahip olduğumuz hedef sayısı **4**.

### 10.2 Tek tedarikçiye bağımlılık riski nedir?

Bu paket **8 mail** üretiyor ve gönderim onaylanırsa gerçekçi cevap beklentisi
`rfq-contact-pack.md` §4'ün %70 `ASSUMPTION`'ıyla **≈5,6 cevap**'tır — G2
gate'inin *"≥5 tedarikçi gerçek RFQ cevabı"* eşiğinin **tam sınırında**.
Yani **tek bir bounce veya tek bir sessizlik eşiği düşürür**.

Somut bağımlılık noktaları:

1. **Interbrosa (T-889):** havuzun tek düşük-MOQ çapası. Düşerse kalan en düşük
   doğrulanmış MOQ 3.600'e (TWF) çıkar — **ve TWF'nin e-postası yok**. Yani
   pilot hacmini mümkün kılan iki tedarikçinin **ikisi de** kanal riski taşıyor.
2. **Bodegas San Valero:** iki iş modelinin fiyat farkını **aynı maliyet
   tabanında** ölçen **tek** hedef. Cevap vermezse, charter'ın "iki model eşit
   öncelikli" kuralı **kanıtla** değil yalnızca kaynak dağıtımıyla test edilmiş olur.
3. **Plaimont:** Colombard-Chardonnay eşleşmesini taşıyan **tek** hedef —
   ve `NEEDS_CONTACT`.
4. **Purcari:** menşe **değiştirilebilen** tek tedarikçi (MD→RO/BG).

**Bu paket bu riski azaltmıyor**, yalnızca görünür kılıyor. Azaltmanın tek yolu
Dalga 2'yi (10 ek hedef, `rfq-contact-pack.md` §2) açmaktır — **bu turda
yasaktı**.

### 10.3 Gösterge fiyat ile gerçek teklif arasındaki sapma tarihsel olarak ne kadar?

**`UNKNOWN` — ve bu tur da onu ölçmedi.**

Havuzda **tek** `PUBLIC_INDICATIVE` fiyat vardır (Harland: $2.85+ entry) ve
karşılığında **sıfır** `FIRM_OFFER` vardır. Sapmayı ölçmek için gereken
eşleştirme (**aynı üründe, aynı hacimde, aynı Incoterm'de, yayınlanmış fiyat ↔
alınmış teklif**) bu projede **hiç kurulmamıştır** — TUR 1 §7.1'den beri açıktır.

Üstelik Harland'ın gösterge fiyatı bugün **üç bağımsız nedenle** teklifle
karşılaştırılamaz durumdadır: (a) para birimi `UNKNOWN` (AUD/USD ≈ 1,5x),
(b) katman `UNKNOWN` (L0 mu L1 mi — `C-461`), (c) etiket baskısı fiyata dahil
değil. Yani **teklif gelse bile** sapma ancak (a) ve (b) kapandıktan sonra
hesaplanabilir.

**Sektör genellemesi yazmayı reddediyorum.** "Gösterge fiyatlar tipik olarak
%10–20 iyimserdir" cümlesi bu repoda `T5`'tir ve tek başına kullanılamaz.
Doğru cevap: **ölçülmedi, ölçmenin yolu bu RFQ'dur, ve Harland tek ölçüm
noktasıdır.**

### 10.4 Bu paketi çürütecek **tek** bulgu

**Cevap oranının çok düşük çıkması.** `rfq-alan-kontrolu.md` §5.1 ve
`rfq-zorunlu-alanlar.md` §7/2 zaten uyarmıştı: uzun ve zorunlu-alanlı bir RFQ'nun
tipik sonucu **daha eksiksiz cevap değil, daha az cevap**tır. Bu turda paket
**daha da uzadı** (5 hacim kademesi × 2 Incoterm × 2 kalite seviyesi = 20 fiyat
hücresi).

Eğer ilk 8 gönderimden **2'den az** cevap gelirse, sorun tedarikçilerde değil
**bu pakette**tir ve doğru tepki daha çok hedef eklemek değil, paketi
**kısaltmaktır** (öncelik sırası `rfq-zorunlu-alanlar.md` §4.4'te tanımlı:
M2/M3/M4/M6 kalır, M1/M5/M7/M8 ikinci aşamaya bırakılır; buna ek olarak Q2
kalite seviyesi ve 50.000 kademesi ilk maildan çıkarılabilir).

### 10.5 İletişim doğrulamasını çürütecek bulgu

Bu turda doğrulanan adreslerin tamamı **T4**'tür (üreticinin kendi sitesi) ve
`ttl: 90d` ile kaydedilmiştir. **Bir e-postanın sitede yazıyor olması, o kutuya
bakıldığı anlamına gelmez.** `info@` ve `geral@` tipi genel kutular satın alma
taleplerinde kaybolabilir — `rfq-contact-pack.md` §6/1 bunu zaten zayıflık
olarak listelemişti ve bu tur **o zayıflığı gidermedi**: 10 hedefin 9'unda
muhatap kişi adı hâlâ `UNKNOWN`'dır.
