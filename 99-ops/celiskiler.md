# ÇELİŞKİLER

Format: `C-###`

> **KURAL (CLAUDE.md §1.13): Kaynaklar çelişirse SESSİZCE SEÇİM YAPILMAZ.**
> Çelişki buraya kaydedilir ve `yatirim-komitesi-baskani`'na taşınır.
> Başkan tier, yürürlük tarihi ve kanıt kalitesine bakarak çözer;
> çözemezse çelişki `CONFLICT` olarak karara taşınır.

---

## DURUM — TUR 1 SONU: 14 ÇELİŞKİ → 8 KAPANDI, 6 AÇIK

> **GÜNCELLEME 2026-08-09 — `yatirim-komitesi-baskani` kanıt kalitesi denetimi.**
> Aşağıdaki tablo **güncel durumu** gösterir. Çözüm gerekçelerinin tamamı bu
> dosyanın sonundaki **§TUR 1 SONU — BAŞKAN ÇÖZÜM KAYITLARI** bölümündedir.
> Denetim raporu: `90-karar/tur-1-kanit-kalitesi-denetimi.md` §4.

| conflict_id | Konu | impact | Açan ajan | **durum** |
|---|---|---|---|---|
| C-101 | Asgari maktu ÖTV: 61,3914 vs 71,2692 TL/lt (mevzuat.gov.tr konsolide metin vs GİB güncel liste) | **CRITICAL** | `gumruk-vergi-uzmani` | **RESOLVED** (71,2692; koşullu — T-901) |
| C-201 | 4250 m.1/3 — 1.000.000 lt/yıl eşiği durgun şarap ithalatına uygulanıyor mu (muafiyet fıkrası yalnız viski ve tabiî köpüren şarabı sayıyor) | **CRITICAL** | `mevzuat-ruhsat-uzmani` | **RESOLVED — NON_MATERIAL** (2026-08-10, başkan; kalan ayak → C-252) |
| C-202 | Bildirim ↔ dağıtım yetki belgesi ↔ ithalat sıralama döngüsü | HIGH | `mevzuat-ruhsat-uzmani` | **OPEN** |
| C-203 | 7584 s.K. satış noktası marka/ambalaj görseli yasağının raf kapsamı | ~~CRITICAL~~ → **CONSTRAINT** | `mevzuat-ruhsat-uzmani` | **ACCEPTED BUSINESS CONSTRAINT** (2026-08-10, kurucu kararı; G0'ı bloke ETMEZ) |
| C-204 | TGK Şarap Tebliği'nin mülga kanuna dayanması; etiket kuralı hangi metinden okunacak | LOW | `mevzuat-ruhsat-uzmani` | **OPEN** (TUR 5 → mevzuat) |
| C-301 | Konteyner başına palet adedi (aynı kaynağın iki yayını çelişiyor) | MEDIUM | `navlun-lojistik-uzmani` | **OPEN** (band zorunlu) |
| C-302 | Valencia/ABD → İstanbul transit süresi (7–10 gün vs 32–35 gün) | HIGH | `navlun-lojistik-uzmani` | **RESOLVED** |
| C-303 | 20DV azami payload (28.300 / 28.200 / 26.000 kg) | LOW | `navlun-lojistik-uzmani` | **RESOLVED** |
| C-401 | Private label MOQ: 300–1.200 vs 3.000–3.600 vs 1 konteyner | HIGH | `global-sourcing-kasifi` | **RESOLVED** |
| C-402 | ABD menşeli ithalatın birim değeri (25,19 USD/lt) benchmark segmentiyle bağdaşmıyor | MEDIUM | `global-sourcing-kasifi` | **RESOLVED** (sahte çelişki) |
| C-403 | Benchmark ürünün California alt bölgesi | LOW | `global-sourcing-kasifi` | **UNRESOLVABLE** |
| C-501 | Aynı feed'de stokta olan/olmayan SKU fiyatları arasında 10 kat fark | HIGH | `turkiye-pazar-kasifi` | **OPEN** |
| C-502 | Metro'nun KDV dili: etikette KDV dahil, ticari koşullarda KDV hariç | MEDIUM (izleme) | `turkiye-pazar-kasifi` | **RESOLVED** (sahte çelişki) |
| C-503 | T5 medya fiyat listesi ile gözlemlenen bant uyumu (üç site aynı tabloyu kopyalamış) | MEDIUM | `turkiye-pazar-kasifi` | **RESOLVED** |

> **Not (2026-08-09, TUR 1 sonu — TARİHSEL KAYIT, SİLİNMEDİ):** C-201 ve C-203
> **CRITICAL ve OPEN**'dır. CLAUDE.md §5 uyarınca kritik
> çelişki/ticket açıkken finans modeli `APPROVED` olamaz.
> C-101 kapanmıştır, ancak bağlı ticket `T-104` (**CRITICAL**) açık kalmaya
> devam eder — çelişkinin çözülmesi ÖTV'nin zaman içinde değişkenliğini ortadan
> kaldırmaz.

> **GÜNCELLEME 2026-08-10 — TUR 2 PRE-FLIGHT (`yatirim-komitesi-baskani`).**
> Yukarıdaki not **artık güncel değildir** ama tarihsel kayıt olarak durmaktadır.
> Güncel durum: **C-201 `RESOLVED — NON_MATERIAL`**, **C-203 `ACCEPTED BUSINESS
> CONSTRAINT`**. Gerekçeler bu dosyanın sonundaki
> **§TUR 2 PRE-FLIGHT — BAŞKAN KAYITLARI** bölümündedir.
> Karar kaydı: `90-karar/tur-2-preflight-housekeeping.md`.
> `T-104` (**CRITICAL, OPEN**) hakkındaki uyarı **aynen geçerlidir.**

---

## ÇELİŞKİ KAYIT FORMATI

```yaml
conflict_id:        C-###
acilis_tarihi:      YYYY-MM-DD
acan_ajan:
konu:               # Neyle ilgili celiski

kaynak_a:
  evidence_id:
  iddia:
  value:
  tier:             # T1..T5
  publication_date:
  effective_date:
  source_name:

kaynak_b:
  evidence_id:
  iddia:
  value:
  tier:
  publication_date:
  effective_date:
  source_name:

celiski_turu:       # DEGER | TARIH | TANIM | KAPSAM | KATMAN
etki:               # Bu celiski cozulmezse model nerede kirilir
impact:             # CRITICAL | HIGH | MEDIUM | LOW
durum:              # OPEN | RESOLVED | UNRESOLVABLE
cozum:              # Baskanin gerekcesi
cozum_evidence_id:
cozen:              # yatirim-komitesi-baskani
cozum_tarihi:
```

---

## ÇÖZÜM HİYERARŞİSİ (BAŞKAN İÇİN)

Çelişki çözülürken şu sıra uygulanır:

1. **Tier** — T1 > T2 > T3 > T4 > T5.
   T1'e karşı T5 çelişkisinde T1 kazanır, ama bu **sessizce** değil,
   gerekçeli olarak kaydedilir.
2. **Yürürlük tarihi** — aynı tier'da daha güncel `effective_date` kazanır.
   Dikkat: `publication_date` değil, `effective_date`.
3. **Model hedef tarihi** — hangi değer modelin hedef tarihinde
   yürürlükte olacaksa o kullanılır.
4. **Kapsam uyumu** — kaynaklardan biri farklı bir GTİP/ürün/kanal için
   konuşuyor olabilir. Bu bir çelişki değil, **kapsam farkıdır** —
   `celiski_turu: KAPSAM` olarak işaretlenir.
5. **Katman uyumu** — iki sayı farklı maliyet katmanına (L0–L8) aitse
   bu da çelişki değil, **katman farkıdır** — `celiski_turu: KATMAN`.
   Bu, en sık yapılan sahte-çelişki türüdür; önce bunu ele.
6. Yukarıdakiler çözmezse → ilgili ajana ek doğrulama ticket'ı.
7. Hiçbiri çözmezse → `durum: UNRESOLVABLE`, değer `CONFLICT` statüsünde
   kalır ve modele **girmez**. Karara taşınır.

---

## BEKLENEN ÇELİŞKİ NOKTALARI (ÖNCEDEN İŞARETLENDİ)

Bu noktalarda çelişki çıkması muhtemeldir; ajanlar dikkatli olsun:

| Konu | Neden çelişir | İlgili ajan |
|------|---------------|-------------|
| Maktu ÖTV tutarı | Periyodik güncellenir; farklı tarihli kaynaklar dolaşır | `gumruk-vergi-uzmani` |
| Gümrük vergisi oranı | Ülke grubuna göre değişir; kaynak hangi grubu kastettiğini yazmayabilir | `gumruk-vergi-uzmani` |
| Tercihli tarifenin kapsamı | Gümrük vergisini mi, ÖTV'yi de mi etkiliyor | `gumruk-vergi-uzmani` |
| Navlun | Spot vs kontrat; all-in vs base | `navlun-lojistik-uzmani` |
| Konteyner şişe kapasitesi | Hacim kısıtı mı ağırlık kısıtı mı esas alınmış | `navlun-lojistik-uzmani` |
| Raf fiyatı | Online vs mağaza; promosyonlu vs normal; şehir farkı | `turkiye-pazar-kasifi` |
| Benchmark fiyat statüsü | KDV dahil/hariç, L7/L8 — bkz. OQ-001 | `turkiye-pazar-kasifi` |
| MOQ | Gösterge vs gerçek teklif | `global-sourcing-kasifi` |
| Kanal marjı | Brüt/net, KDV dahil/hariç, margin/markup | `kanal-marj-uzmani` |
| Ruhsat süreleri | Mevzuattaki yasal süre vs pratikte gerçekleşen süre | `mevzuat-ruhsat-uzmani` |

---

# TUR 1 ÇELİŞKİ KAYITLARI (ajan fragment'lerinden birleştirildi)

> Aşağıdaki bölümler ajanların `99-ops/_parts/celiskiler-*.md` dosyalarından
> **değiştirilmeden** aktarılmıştır. Başlık seviyeleri bir kademe indirilmiştir.
>
> ⚠️ **OKUMA UYARISI:** Fragment metinlerinin içindeki `Durum: OPEN` /
> `status: OPEN` satırları **TUR 1 tarihlidir ve dondurulmuştur** (ajan metni
> değiştirilmez). **Güncel durum** için yukarıdaki özet tabloya ve bu dosyanın
> sonundaki **§TUR 1 SONU — BAŞKAN ÇÖZÜM KAYITLARI** bölümüne bakınız.

## gumruk-vergi-uzmani

> CLAUDE.md §1.13: Kaynaklar çelişirse **sessizce seçim yapılmaz.**
> Aşağıdaki çelişki başkana taşınmıştır.

---

### C-101 — Şarapta asgari maktu ÖTV tutarı: 61,3914 TL/lt mi, 71,2692 TL/lt mi?

| Alan | Değer |
|------|-------|
| conflict_id | **C-101** |
| Açan | `gumruk-vergi-uzmani` |
| Açılış | 2026-08-09 |
| Durum | **OPEN — çözüm önerisi sunuldu, başkan onayı bekleniyor** |
| Etkilenen model girdisi | `80-model/inputs/vergi.yaml` → `matrah_sirasi[OTV].asgari_maktu_tutar` |
| Etki | **CRITICAL** — projenin tek en kritik sayısı |

#### Kaynak A
- **Kaynak:** T.C. Cumhurbaşkanlığı Mevzuat Bilgi Sistemi — 4760 sayılı ÖTV
  Kanunu **konsolide metin**, ekli (III) sayılı liste, 22.04 satırı
- **Tier:** T1
- **Erişim:** 2026-08-09 · `https://www.mevzuat.gov.tr/mevzuatmetin/1.5.4760.pdf`
- **Değer:** **61,3914 TL/litre**
- **Dipnot 58:** Tutar, 31/12/2025 tarihli ve 10799 sayılı Cumhurbaşkanı Kararı
  ile yayımı tarihinde yürürlüğe girmek üzere metne işlenmiştir; aynı Karar ile
  ÖTVK 12/3'ün **2026 Ocak–Haziran** dönemi için uygulanmayacağı hükme bağlanmıştır.
- **evidence_id:** EV-2026-08-09-112

#### Kaynak B
- **Kaynak:** Gelir İdaresi Başkanlığı — "(III) SAYILI LİSTE — 4760 sayılı ÖTV
  Kanununun (12/3) maddesi uyarınca güncellenen liste — **Yürürlük: 3/7/2026**"
- **Tier:** T2 (dayanağı T1: ÖTVK md.12/3 otomatik yeniden belirleme)
- **Erişim:** 2026-08-09 · GİB CDN
- **Değer:** **71,2692 TL/litre**
- **evidence_id:** EV-2026-08-09-111

#### Neden çelişiyor (görünüşte)
İki resmî kaynak aynı GTİP için farklı tutar gösteriyor. Naif bir okuyucu
mevzuat.gov.tr'yi (T1) esas alıp 61,3914 kullanır ve **şişe başına ~7,4 TL**
eksik ÖTV hesaplar.

#### Önerilen çözüm (başkan onayına)
Çelişki **gerçek değil, mekanizma kaynaklıdır**:

1. ÖTVK md.12/3 (EV-2026-08-09-114) uyarınca (III) sayılı listedeki asgari maktu
   tutarlar Ocak ve Temmuz'da Yİ-ÜFE değişimi oranında **"yeniden belirlenmiş
   sayılır"** — yani ayrı bir Cumhurbaşkanı Kararı olmadan kendiliğinden değişir.
2. Kendiliğinden değişen tutarlar kanun metnine **işlenmez** (işlenecek bir
   düzenleme yoktur), bu yüzden mevzuat.gov.tr konsolide metni son CBK tutarını
   göstermeye devam eder.
3. CBK 10799'un 12/3'ü askıya alması yalnızca **2026 Ocak–Haziran** dönemi
   içindi. Temmuz 2026 için askıya alma yapılmamıştır — 3/7/2026 tarihli CBK
   11489 yalnızca **(III) sayılı listenin (B) cetveli** (tütün) mallarına ilişkin
   olup 12/3'ü **onlar için** Temmuz–Aralık 2026 döneminde askıya almıştır
   (kanun metni dipnot 60). Şarap (A cetveli) askı kapsamında **değildir**.
4. Dolayısıyla 3/7/2026 itibarıyla şarapta 12/3 otomatik güncellemesi işlemiş
   ve tutar 61,3914 → 71,2692 (+%16,09) olmuştur. GİB listesinin başlığı bunu
   açıkça yazmaktadır.

**Öneri:** Modelde **71,2692 TL/litre** (EV-2026-08-09-111) kullanılsın;
EV-2026-08-09-112 `SUPERSEDED` olarak kalsın.

#### Bu çözümü ne çürütür
- 3/7/2026 sonrasında şarap için 12/3'ü askıya alan veya tutarı yeniden tespit
  eden bir Cumhurbaşkanı Kararı çıkmışsa (bu turda tespit edilmedi).
- GİB'in yayımladığı listenin hesaplama hatası içermesi (Yİ-ÜFE 6 aylık değişim
  oranının %16,09 olduğu **TÜİK kaynağından bağımsız olarak doğrulanmadı** —
  bu, çözümün en zayıf halkasıdır).

#### Kapanış için gereken
- TÜİK Yİ-ÜFE Aralık 2025 → Haziran 2026 değişim oranının %16,09 civarında
  olduğunun doğrulanması, **veya**
- Bir gümrük müşaviri / GİB üzerinden güncel beyanname örneğinde uygulanan
  TL/lt tutarının teyidi.

---

## mevzuat-ruhsat-uzmani

> Kaynaklar çeliştiğinde **sessizce seçim yapılmaz.** Başkana taşınır.

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|-------------|----------------------|----------------------|-----------------|-------|
| **C-201** | 4250 s.K. m.1/3 (T1, eff. 11/1/2001): ithalatçı için "her satıcıya ülke genelinde yerinde teslim" şartı + 1.000.000 litre/yıl fiyat serbestisi eşiği; şartı sağlayamayan firmanın fiyatlandırma/satış/dağıtımı **Tekel Genel Müdürlüğü eliyle** yapılır | 4250 s.K. m.1/5 (T1, aynı tarih): "Bira ve her türlü şarap ... **üretimi**, fiyatlandırılması, dağıtılması ve satılması ile **viski ve tabii köpüren şarapların ithali** ... bu maddede öngörülen şartlar aranmaksızın serbesttir" + fiilî durum: Tekel Genel Müdürlüğü artık mevcut değil | Muafiyet fıkrası, **durgun şarap ithalatını** açıkça saymıyor (yalnızca viski ve tabiî köpüren şarap). Lafzî okumada durgun şarap ithalatı 1 milyon litre eşiğine tabi kalıyor. Yaptırım mercii (Tekel GM) ise ortadan kalkmış durumda. 4619 s.K. Geçici m.1 eşiği kademeli indirmiş, sıfıra indirme yetkisini Bakanlar Kuruluna vermiş; böyle bir karar bulunamadı. | **OPEN** → `T-201` |
| **C-202** | Ticaret Yön. m.10/a (T1, eff. 22/2/2008): dağıtım yetki belgesi başvurusunda "alkollü içki ithalatçıları için **alkollü içki bildirimi**" istenir | Ticaret Yön. m.12/1 (T1, eff. 31/12/2015): "**Dağıtım yetki belgesi olmadan** ... **ithalat yapılamaz**" | Sıralama döngüsü: bildirim için ithalat niyeti, dağıtım yetki belgesi için bildirim, ithalat için dağıtım yetki belgesi. Bildirim ile fiilî ithalatın ayrıştığı (dosya önce, sevkiyat sonra) varsayıldı ama **doğrulanmadı**. T0 takviminin adım sırasını etkiler. | **OPEN** → `T-202` |
| **C-203** | 7584 s.K. m.2 ile 4250 m.6/1 (T1, eff. 20/6/2026): "arz ambalajında yer alan ifade, şekil, isim, işaret ve görseller iş yerlerinin içinde, dışında, vitrinlerinde, **satış ünitelerinde** ... bulundurulamaz" | Aynı kanunun genel yapısı ve 4250 m.6/7 (T1): alkollü içkilerin satışı **serbest**, yalnızca "işletme **dışından görülecek şekilde**" arz yasak; Satış Yön. m.7 satış faaliyetini düzenliyor | Lafzî okumada ürünün ambalajı da "arz ambalajında yer alan görsel"dir ve "satış ünitesinde bulundurulamaz". Bu, ürünün rafta bulundurulmasını imkânsız kılar — kanunun kendi sistematiğiyle çelişir. Dar yorum (markalı teşhir materyali yasağı) makul ama **doğrulanmamıştır**. | **OPEN** → `T-205` |
| **C-204** | TGK Şarap Tebliği 2008/67 (T1, TADAB yayını): dayanağı **5179 sayılı Kanun**; atıf yaptığı etiketleme tebliği RG 25/8/2002-24857 | 5179 s.K. **mülga** (5996 s.K. ile); atıf yapılan etiketleme tebliği de mülga (yerine TGK Gıda Etiketleme ve Tüketicileri Bilgilendirme Yönetmeliği, RG 26/1/2017-29960 mükerrer) | TADAB tebliği hâlâ yürürlükteki mevzuat olarak yayımlıyor; ancak dayanak ve atıflar güncel değil. Şarap etiket kurallarının hangi metinden okunacağı belirsiz. Tebliğin **yayım tarihi de doğrulanamadı**. | **OPEN** — düşük etki, `EV-2026-08-09-221` notunda işaretlendi |

---

## navlun-lojistik-uzmani

> Kaynaklar çeliştiğinde sessizce seçim yapılmaz. Aşağıdaki üç çelişki
> **çözülmemiştir** ve başkana taşınmaktadır. Hesaplarda çelişkinin **bandı**
> kullanılmıştır, bir taraf seçilmemiştir.

---

### C-301 — Konteyner başına palet adedi

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

### C-302 — Valencia/ABD → İstanbul transit süreleri

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

### C-303 — 20DV azami payload

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

---

## global-sourcing-kasifi

> Kaynaklar çeliştiğinde **sessizce seçim yapılmaz.** Çelişki kaydedilir ve başkana taşınır.
> ID bloğu: `C-401` … `C-499`

---

### C-401 — Private label MOQ büyüklüğü

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

#### Neden çelişiyor
A, B ve C arasında **10 kata varan** bir fark var. D ise farklı bir birimde
(konteyner) ölçüyor ve şişe cinsinden karşılığı bilinmiyor (T-402).

#### Neden sessizce çözülemez
- A'yı seçersek pilot çok ucuz görünür ve `IMPORT PILOT` kararı yapay olarak kolaylaşır.
- D'yi seçersek pilot imkânsız görünür ve proje yapay olarak ölür.
- B/C'yi seçersek pilot tam sınırda çıkar.
**Seçim, kararın kendisini belirler.** Bu yüzden çözüm başkana bırakılmıştır.

#### Bu ajanın değerlendirmesi (öneri, karar değil)
B, C ve D **birincil kaynaklardır** (üreticinin kendi sitesi, tier T4).
A bir **agregatör içeriğidir** (tier T5) ve hangi üreticilere dayandığı belirtilmemiştir.
CLAUDE.md §2 uyarınca T5 tek başına sonuç üretemez.
Ayrıca A ile B/C/D arasındaki fark bir "hata" olmayabilir: **iki farklı tedarikçi
sınıfı** olabilir (butik/kontrat şişeleyici vs konteyner satan endüstriyel üretici).

#### Çözüm yolu
Gerçek RFQ cevapları (RFQ soru 3.6 ve 4.2, en az 5 tedarikçiden). TUR 7.
Model, çözülene kadar **her iki uçta da senaryo çalıştırmalıdır.**

---

### C-402 — Türkiye'nin ABD menşeli şişelenmiş şarap ithalatının birim değeri

| Alan | Değer |
|---|---|
| conflict_id | **C-402** |
| status | **OPEN** |
| impact | **MEDIUM** — benchmark ürünün menşei ile veri uyuşmuyor |

| Kaynak | Tier | İddia |
|---|---|---|
| A — `00-charter/benchmark.md` (foto gözlemi) | FACT_FROM_PHOTO | Metro rafında California menşeli bir şarap 599,90 TL'ye satılıyor (fiyat/performans segmenti) |
| B — UN Comtrade (EV-2026-08-09-405) | T3 | Türkiye 2025'te ABD'den yalnızca **18.298 litre** şişelenmiş şarap ithal etti, ortalama CIF **25,19 USD/litre** |

#### Neden çelişiyor
25,19 USD/litre = ~18,89 USD/750 ml CIF. Bu, fiyat/performans segmentiyle
**bağdaşmaz** — bir premium/lüks fiyat seviyesidir. Yani Comtrade'e göre
ABD'den Türkiye'ye giren mal, benchmark ürünün olması gereken segmentte değil.

#### Olası açıklamalar (hiçbiri doğrulanmadı)
1. Benchmark ürün **ABD'den doğrudan değil**, bir AB ülkesi üzerinden (re-export/transit)
   geliyor olabilir ve menşe kaydı farklı görünüyor olabilir.
2. Benchmark ürün **eski bir partiden** kalma olabilir (2023 hasat, 2024 ithalatı).
3. 18.298 litrelik hacim içinde ucuz bir parti olabilir ama ortalama birim değer
   birkaç premium parti tarafından yukarı çekilmiş olabilir (ağırlıklı ortalama etkisi).
4. Comtrade partner kodu ayrıştırması hatalı olabilir (`842` kodu ABD alt kırılımı olarak
   yorumlandı).

#### Kim çözer
- `turkiye-pazar-kasifi` → benchmark ürünün ithalatçısı ve ithalat yılı (T-405)
- `gumruk-vergi-uzmani` → menşe vs sevk ülkesi ayrımının Türkiye kayıtlarına yansıması

#### Bu turdaki etkisi
Ülke karşılaştırma tablosunda ABD'nin L2 CIF değeri **"temsili değil"** olarak
işaretlenmiştir ve ülke sıralamasında kullanılmamıştır.

---

### C-403 — Benchmark ürünün California içindeki menşe bölgesi

| Alan | Değer |
|---|---|
| conflict_id | **C-403** |
| status | **OPEN** |
| impact | **LOW** — model çıktısını değiştirmez, tedarikçi aramasını yönlendirir |

| Kaynak | Tier | İddia |
|---|---|---|
| A — Perakendeci/agregatör açıklaması | T5 | "Gold Country" **Sierra Foothills** bölgesinde üretiliyor |
| B — Başka perakendeci/agregatör açıklaması | T5 | Ürün California **Central Valley**'den geliyor |

#### Neden önemli (sınırlı)
Sierra Foothills küçük ve görece pahalı bir bölgedir; Central Valley ise Californiya'nın
hacim/değer segmentinin merkezidir. Fiyat/performans konumlandırması **Central Valley**
ile tutarlıdır. Ancak her iki kaynak da T5'tir ve marka adı ("Gold Country" =
California Gold Rush bölgesi, yani Sierra Foothills'in takma adı) pazarlama amaçlı
bir çağrışım olabilir.

#### Çözüm yolu
Şişenin arka etiketindeki üretici/şişeleyici bilgisi (`turkiye-pazar-kasifi` raf
ziyaretinde okuyabilir) veya ABD TTB COLA kayıtları. → T-405

---

### ÖZET

| conflict_id | Konu | impact | status | Kim çözer |
|---|---|---|---|---|
| C-401 | Private label MOQ 300–1.200 vs 3.000–3.600 vs 1 konteyner | HIGH | OPEN | RFQ (TUR 7) + başkan |
| C-402 | ABD menşeli ithalatın birim değeri benchmark segmentiyle bağdaşmıyor | MEDIUM | OPEN | `turkiye-pazar-kasifi` (T-405) |
| C-403 | Benchmark ürünün California alt bölgesi | LOW | OPEN | `turkiye-pazar-kasifi` (T-405) |

---

## turkiye-pazar-kasifi

> Ana `99-ops/celiskiler.md`'ye başkan tarafından birleştirilecektir.

---

### C-501 — Aynı kanalda stokta olan ve olmayan SKU'ların fiyatları tutarsız

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

### C-502 — Metro'nun KDV dili iki farklı yerde iki farklı

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

### C-503 — T5 medya fiyat listesi ile gözlemlenen bant arasındaki uyum sorunu

| Alan | Değer |
|---|---|
| `conflict_id` | **C-503** |
| **Kaynak A** | T5 içerik siteleri (Ocak/Temmuz 2026): Metro'da Doluca 75 cl **630 TL**, Grand Reserve Boğazkere **570 TL** — `EV-512` |
| **Kaynak B** | Online uzman perakende (T4, Ağustos 2026): benzer segmentteki yerli şaraplar **649–800 TL** — `EV-510` |
| **Neden problem** | İki kaynak birbirine yakın ama **A kaynağı T5'tir ve üç site aynı tabloyu kopyalamıştır** — bağımsız doğrulama değildir. Yakınlık, doğruluk kanıtı sayılamaz. Ayrıca A kaynağı Ocak 2026 tarihli; Ağustos 2026 fiyatı olarak kullanılamaz. |
| **Nasıl ele alındı** | `EV-512` satırları CSV'ye `status: UNKNOWN` ile girildi ve **"MODELE GİREMEZ"** notu düşüldü. |
| **Durum** | `OPEN` — fiziksel gözlemle kapanır (`OQ-502`) |

---

# TUR 1 SONU — BAŞKAN ÇÖZÜM KAYITLARI

```yaml
cozen:          yatirim-komitesi-baskani
cozum_tarihi:   2026-08-09
dayanak:        90-karar/tur-1-kanit-kalitesi-denetimi.md §4
kural:          bu dosyadaki "ÇÖZÜM HİYERARŞİSİ (BAŞKAN İÇİN)" 7 adımı
```

> Bu bölüm yalnızca `durum` / `cozum` / `cozen` / `cozum_tarihi` alanlarını
> doldurur. Yukarıdaki ajan fragment'lerinin **hiçbir cümlesi silinmemiş veya
> değiştirilmemiştir.**

---

## C-101 — Asgari maktu ÖTV: 61,3914 vs 71,2692 TL/lt

```yaml
conflict_id:      C-101
celiski_turu:     TARIH        # DEGER degil — ayni hukmun iki farkli zamandaki hali
impact:           CRITICAL
durum:            RESOLVED
cozum_evidence_id: EV-2026-08-09-111
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-09
```

**Karar:** `gumruk-vergi-uzmani`'nın çözüm önerisi **ONAYLANDI.**
Modelde **71,2692 TL/litre** (`EV-2026-08-09-111`) kullanılır.
`EV-2026-08-09-112` (61,3914) `SUPERSEDED` olarak kalır.

**Gerekçe (çözüm hiyerarşisi sırasıyla):**

1. **Kural 1 (tier) tek başına yetmez.** Naif okuma T1 (mevzuat.gov.tr) lehinedir.
   Ancak çelişen şey iki ayrı *iddia* değil, **aynı hükmün iki farklı
   zamandaki hâlidir** → `celiski_turu: TARIH`.
2. **Kural 2 (yürürlük tarihi) belirleyicidir.** ÖTVK md.12/3 (T1,
   `EV-2026-08-09-114`) asgari maktu tutarların Ocak/Temmuz'da Yİ-ÜFE oranında
   *"yeniden belirlenmiş sayılır"* olduğunu söyler — ayrı bir CBK gerekmediği
   için değişiklik **konsolide kanun metnine işlenmez.** GİB listesi (T2), bu
   otomatik mekanizmanın **yayımıdır**, rakip bir iddia değildir; başlığında
   dayanağını (md.12/3) ve yürürlüğünü (3/7/2026) açıkça yazar.
3. **Askı kontrolü:** CBK 10799 md.12/3'ü yalnız **2026 Ocak–Haziran** için,
   CBK 11489 yalnız **(III) sayılı listenin (B) cetveli (tütün)** için askıya
   almıştır. Şarap ((III)/A) askı kapsamı **dışındadır.**
4. **Kural 3 (model hedef tarihi):** `20-mevzuat/t0-takvimi.md`'ye göre ilk
   konteynerin izinlerinin tamamlanması **2026-12 → 2027-05** bandındadır; yani
   her senaryoda 3/7/2026'dan **sonrasıdır.** 61,3914 hiçbir senaryoda geçerli
   değildir.

**İki bağlayıcı koşul:**

- **K1 —** Bu değer modele **sabit sayı olarak giremez.** `model_hedef_tarihi`
  2027-01-01 veya sonrasıysa ÖTV **Yİ-ÜFE'ye endeksli bir değişken** olarak
  modellenir. **Ticket `T-104` (CRITICAL) AÇIK KALIR**; C-101'in çözülmesi
  T-104'ü kapatmaz.
- **K2 —** Çözümün en zayıf halkası (+%16,09 artışın TÜİK Yİ-ÜFE'den bağımsız
  doğrulanmamış olması) **`T-901`** ile takip edilir.

**Bu çözümü ne çürütür:** 3/7/2026 sonrasında şarap için md.12/3'ü askıya alan
veya tutarı yeniden tespit eden bir Cumhurbaşkanı Kararı; veya GİB listesinin
hesap hatası içermesi.

---

## C-302 — Valencia/ABD → İstanbul transit süreleri

```yaml
conflict_id:      C-302
celiski_turu:     DEGER
impact:           HIGH
durum:            RESOLVED
cozum_evidence_id: EV-2026-08-09-325, EV-2026-08-09-326
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-09
```

**Karar:** Kaynak B (`EV-2026-08-09-329`, `EV-2026-08-09-333`, BR Logistics)
**bütünüyle diskalifiye edilmiştir.**

**Gerekçe:** Kural 1 (tier) — Kaynak A, T3 (Maersk SLR Marmara Sea A servis
tarifesi) + T4 (JSV Logistic) olmak üzere **iki bağımsız kaynaktır**; Kaynak B
T5'tir. Ayrıca Kaynak B **kendi içinde tutarsızdır** (LA→İstanbul 15 gün
fiziksel olarak imkânsız; Valencia→İstanbul 32–35 gün Akdeniz içi bir rota için
absürt) — bu, kaynağın tamamının güvenilirliğini ortadan kaldırır.

- **Akdeniz transit süresi 7–10 gün olarak geçerlidir.**
- **ABD / California rotası bir ÇELİŞKİ DEĞİLDİR — `UNKNOWN`'dır.** Ortada tek
  bir kullanılabilir kaynak kalmamıştır. `T-304` ile takip edilir.
- `navlun-lojistik-uzmani`'nın bu turdaki davranışı (ABD sayılarını modele
  almamak) **doğrulanmıştır.**

---

## C-303 — 20DV azami payload

```yaml
conflict_id:      C-303
celiski_turu:     DEGER
impact:           LOW
durum:            RESOLVED
cozum_evidence_id: EV-2026-08-09-302
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-09
```

**Karar:** **28.300 kg** (Maersk, T3, `EV-2026-08-09-302`) kullanılır.

**Gerekçe:** Kural 1 (tier): T3 > T4 (iContainers, 28.200) > T5 (26.000 —
kanıt kartı **açılmamıştır**, dolayısıyla CLAUDE.md §2 uyarınca sonuç
üretemez).

**Model etkisi: SIFIR.** 20DV'de bağlayıcı kısıt zaten **hacimdir**
(payload'ın %30–60'ı kullanılmaz); 26.000 kg iddiası doğru olsa bile bağlayıcı
olmazdı. Çözüm kayıt düzenidir, sayı değişikliği değildir.

---

## C-401 — Private label MOQ büyüklüğü

```yaml
conflict_id:      C-401
celiski_turu:     KAPSAM      # tedarikci sinifi farki — deger celiskisi degil
impact:           HIGH
durum:            RESOLVED
cozum_evidence_id: EV-2026-08-09-408, EV-2026-08-09-409, EV-2026-08-09-410
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-09
```

**Karar iki adımlıdır:**

1. **Kaynak A elenir.** `EV-2026-08-09-424` (usetorg.com agregatörü, 300–1.200
   şişe) **T5**'tir ve hangi üreticilere dayandığı belirtilmemiştir.
   CLAUDE.md §2: T5 tek başına sonuç üretemez. Kural 1 uygulanır.
   Bu, `global-sourcing-kasifi`'nın uyardığı *"A'yı seçersek pilot yapay olarak
   kolaylaşır"* riskini ortadan kaldırır.
2. **Geriye kalan fark bir çelişki DEĞİLDİR.** 3.000 şişe (Interbrosa) /
   3.600 şişe (The Wine Factory) / 1 × 20ft konteyner (Viña Maria) — üç **ayrı
   tedarikçinin ayrı iş modelidir**, aynı soruya verilmiş çelişkili cevaplar
   değildir. Kural 4 (kapsam uyumu). Bu zaten raporda `B-2` olarak **FACT**
   niteliğinde tespit edilmiştir: *"MOQ bir sayı değil, bir yapıdır."*

**Geriye kalan gerçek boşluk bir `UNKNOWN`'dır, `CONFLICT` değil:** bize
uygulanacak gerçek MOQ (`OQ-402`, CRITICAL) yalnızca RFQ ile öğrenilir.

**Bağlayıcı model kuralı:** `finans-fizibilite`, MOQ'nun **her iki yapısını**
(SKU bazlı ~3.000–3.600 şişe **ve** konteyner bazlı) ayrı senaryo olarak
çalıştırır. Tek bir MOQ değerine kilitlenmek **yasaktır** — seçim kararın
kendisini belirler.

---

## C-402 — ABD menşeli ithalatın birim değeri vs benchmark

```yaml
conflict_id:      C-402
celiski_turu:     KATMAN + KAPSAM     # sahte celiski
impact:           MEDIUM
durum:            RESOLVED
cozum_evidence_id: EV-2026-08-09-405
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-09
```

**Karar: GERÇEK ÇELİŞKİ DEĞİLDİR.**

**Gerekçe (kural 5 → kural 4, "en sık yapılan sahte-çelişki türü"):**

| | Kaynak A | Kaynak B |
|---|---|---|
| Ne ölçüyor | **tek bir SKU'nun raf fiyatı** | **tüm ABD menşeinin yıllık ortalaması** |
| Katman | **L8** | **L2 (CIF)** |
| Popülasyon | 1 ürün | 18.298 litrelik toplam |

İki sayı **ne aynı katmanda ne aynı popülasyondadır**; birbirini çürütemez.
18.298 litrelik küçük bir toplamda ortalama birim değer, birkaç premium parti
tarafından kolayca yukarı çekilir (ağırlıklı ortalama etkisi).

**Bağlayıcı kural:** Comtrade ABD ortalama CIF birim değeri (25,19 USD/litre)
benchmark ürünün maliyet proxy'si olarak **KULLANILAMAZ.**
`global-sourcing-kasifi`'nın bu değeri "temsili değil" işaretleyip ülke
sıralamasında kullanmama kararı **doğrulanmıştır.**

**Kapanmayan kısım bir `UNKNOWN`'dır:** benchmark ürünün gerçek menşe/rota/
ithalat yılı → `T-405`.

---

## C-403 — Benchmark ürünün California alt bölgesi

```yaml
conflict_id:      C-403
celiski_turu:     DEGER
impact:           LOW
durum:            UNRESOLVABLE
cozum_evidence_id: null
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-09
```

**Karar:** Her iki kaynak da **T5**'tir. Kural 1 (tier) uygulanamaz — eşit ve
ikisi de yetersiz. Kural 2/3/4/5 de uygulanamaz. **Kural 7 devreye girer:**

- Değer `UNKNOWN` olarak kalır ve **modele girmez.**
- impact `LOW` olduğu için **karara taşınmaz** (model çıktısını değiştirmez,
  yalnızca tedarikçi aramasını yönlendirirdi).
- `T-405` (şişenin arka etiketi / TTB COLA kaydı) ile kapanabilir.

---

## C-502 — Metro'nun KDV dili

```yaml
conflict_id:      C-502
celiski_turu:     KAPSAM      # sahte celiski
impact:           MEDIUM
durum:            RESOLVED
cozum_evidence_id: EV-2026-08-09-503, EV-2026-08-09-508
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-09
```

**Karar:** `turkiye-pazar-kasifi`'nın değerlendirmesine **KATILIYORUM** —
gerçek bir çelişki değildir.

**Gerekçe (kural 4):** İki kaynak **aynı şey hakkında konuşmamaktadır.**
- Kaynak A (broşür, her fiyatta `KDV'li`) = **müşteriye ilan edilen raf
  fiyatı** → brüt.
- Kaynak B ("alım hedeflerinize KDV dahil değildir") = **ciro/hedef
  muhasebesi** → net.

Aynı şirketin iki farklı amaç için iki farklı matrah kullanması olağandır ve
cash & carry formatında beklenir. Benchmark bir **raf etiketi gözlemidir** →
brüt taraf geçerlidir.

**ÜÇ BAĞLAYICI SINIR (bu çözüm fazla okunmasın diye):**

1. Bu çözüm **OQ-001'i KAPATMAZ** ve **G3'ü AÇMAZ.**
2. Çözülen tek şey "Metro kendi içinde tutarsız" itirazıdır. **Şarap
   reyonundaki fiziksel etiketin** de `KDV'li` yazdığı **görülmemiştir** —
   tüm sonuç broşürden rafa yapılmış bir **çıkarımdır** (`T-501`, `T-504`).
3. `EV-2026-08-09-506`'nın (Fiyat Etiketi Yönetmeliği) T1 etiketi, ajanın kendi
   itirafıyla **ikincil veritabanından** okunmuştur; `T-501` ile
   doğrulatılmadan bu çözümün hukuki ayağı tamamlanmış sayılmaz.

---

## C-503 — T5 medya fiyat listesi vs gözlemlenen bant

```yaml
conflict_id:      C-503
celiski_turu:     DEGER
impact:           MEDIUM
durum:            RESOLVED
cozum_evidence_id: EV-2026-08-09-510
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-09
```

**Karar:** Kaynak A (`EV-2026-08-09-512`) **elenir**; kayıt kapanır.

**Gerekçe:** Kural 1 (tier) — Kaynak A **T5**'tir ve üç site aynı tabloyu
kopyalamıştır (bağımsız doğrulama değildir). Kural 2 (tarih) — Ocak 2026
tarihlidir, Ağustos 2026 fiyatı olarak kullanılamaz. CLAUDE.md §2 uyarınca
T5 bir kaynak, T4 bir gözlemle **çelişki oluşturamaz**; yalnızca "nereye
bakılacağını" gösterir.

`EV-512` zaten `status: UNKNOWN` + **"MODELE GİREMEZ"** notuyla işaretlenmiştir;
bu doğrulanmıştır.

**Bu çözüm `EV-2026-08-09-510`'u DOĞRULAMAZ.** Yerli rakip fiyat bandı hâlâ tek
bir ticari sitenin feed'ine dayanmaktadır ve `C-501` açıktır.

---

## AÇIK KALAN 6 ÇELİŞKİ — NEDEN ÇÖZÜLEMEDİ

| id | impact | durum | Çözülememe nedeni | Kim/ne kapatır |
|---|---|---|---|---|
| **C-201** | **CRITICAL** | OPEN | T1 ↔ T1, aynı kanun, aynı yürürlük tarihi, ikisi de yürürlükte. Çözüm hiyerarşisinin **1–5. kuralları uygulanamıyor**. Bu bir **hukuki yorum** sorunudur; başkanın kendi yorumuyla çözmesi CLAUDE.md §1.16 ihlali olur | `T-201` — TADAB yazılı görüşü / hukuk bürosu mütalaası / Yetkili Dağıtım Firmaları Listesinde küçük ithalatçı tespiti |
| **C-202** | HIGH | OPEN | T1 ↔ T1, aynı yönetmeliğin iki maddesi. `celiski_turu` **`TANIM`** olarak yeniden sınıflandırıldı (değer çelişkisi değil, sıralama sorunu). `t0-takvimi.md`'de A7→A8 sırasının `ASSUMPTION` etiketiyle işaretlenmiş olması **doğru davranıştır** | `T-202` — TADAB'a doğrudan soru |
| **C-203** | **CRITICAL** | OPEN | T1 ↔ T1; kanun **9 haftalıktır**, ikincil düzenleme **henüz yoktur**. Çözmek için var olmayan bir metni okumak gerekir | `T-205` — TADAB ikincil düzenlemesi/rehberi |
| **C-204** | LOW | OPEN | Mülga dayanaklı bir tebliğin yürürlük durumu bir **mevzuat yorumudur**; `mevzuat-ruhsat-uzmani`'nın alanıdır, başkan kendi yorumunu koyamaz. Etki düşük olduğu için **yeni ticket açılmadı** | TUR 5 → `mevzuat-ruhsat-uzmani` |
| **C-301** | MEDIUM | OPEN | T4 ↔ T4, aynı firmanın iki yayını. Kural 2 (daha güncel kazanır) teknik olarak uygulanabilirdi (2025 > 2022) — **bilinçli olarak uygulanmadı**, çünkü daha güncel olanı seçmek kapasite bandını %11 daraltır ve modeli **gerekçesiz iyimser** yapar. Farkın kaynağı büyük olasılıkla **palet standardı tanımıdır** (`TANIM`) | `T-304` — forwarder'dan yazılı stowage planı |
| **C-501** | HIGH | OPEN | T4 ↔ T4, **aynı feed**, aynı erişim tarihi, aynı `updated_at`. Tier, tarih, kapsam ve katman ayrımlarının **hiçbiri** uygulanamıyor | `OQ-502` — fiziksel mağaza gözlemi |

### BAŞKAN DİREKTİFİ — C-301

**9–11 (20ft) / 20–24 (40ft) palet bandı korunur. Tek bir değer seçilmesi
YASAKTIR.** Tüm kapasite sonuçları aralık olarak taşınır.
`navlun-lojistik-uzmani`'nın bu turdaki band kullanımı **doğrulanmıştır.**

---

# TUR 1.5 ÇELİŞKİ KAYITLARI

TUR 1.5'te üç yeni çelişki açıldı:

| conflict_id | Konu | impact | Açan |
|---|---|---|---|
| **C-551** | Metro'nun **şarap** kataloglarında (2008/2009/2010 arşiv) fiyatlar fiilen ÇİFT gösteriliyor (KDV hariç + KDV'li). TUR 1'in KDV sonucu, içinde sıfır alkol bulunan broşürlerden çıkarılmıştı. | ~~CRITICAL~~ **HIGH** ¹ | `turkiye-pazar-kasifi` |

> ¹ **Başkan düzeltmesi 2026-08-10:** Bu satırda `CRITICAL` yazıyordu; aynı
> çelişkinin kendi `yaml` bloğunda (aşağıda) ve `T-551` ticket'ında `impact:
> HIGH` yazmaktadır. Bu bir **kayıt tutarsızlığıdır**, yeni bir değerlendirme
> değildir. Ajanın kendi bloğundaki değer (**HIGH**) esas alınmıştır; başkan
> impact'i **yükseltmemiş veya düşürmemiştir**.
| C-251 | Fiyat serbestisi ölçüsü 600.000 mi 1.000.000 litre/yıl mı | LOW (maddi değil) | `mevzuat-ruhsat-uzmani` |
| C-252 | 4250 m.1/5 muafiyet fıkrasının ithal durgun şarabı kapsayıp kapsamadığı (C-201'in kalan lafzî ayağı) | LOW (model etkisi yok) | `mevzuat-ruhsat-uzmani` |

**C-201 durumu:** üç ayağından ikisi kanıtla düştü; kalan ayak C-252 olarak
yeniden numaralandı. `mevzuat-ruhsat-uzmani` önerisi: `RESOLVED — NON_MATERIAL`.
Kapatma yetkisi başkandadır.

> **C-551 uyarısı:** `pazar.yaml`'daki `kdv_durumu = KDV_DAHIL` değeri
> DEĞİŞTİRİLMEDİ, yalnızca `conflict_id: C-551` ile nitelendi. Sessiz seçim
> yapılmadı; `T-551` ile başkana taşındı.

## mevzuat-ruhsat-uzmani (TUR 1.5)

> Bu dosya `99-ops/celiskiler.md`'ye **konsolide edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu turda **DOKUNULMAMIŞTIR** (tur mandası).
> CLAUDE.md §1.13: kaynaklar çelişirse **sessiz seçim yapılmaz.**

---

### A) MEVCUT ÇELİŞKİNİN DURUMU — C-201

```yaml
conflict_id:      C-201
onceki_durum:     OPEN (CRITICAL)
onerilen_durum:   RESOLVED — NON_MATERIAL
oneren:           mevzuat-ruhsat-uzmani
oneri_tarihi:     2026-08-10
karar_yetkisi:    yatirim-komitesi-baskani   # bu ajan KAPATMAZ
```

C-201 üç ayak üzerinde duruyordu. **İkisi bu turda düştü:**

| Ayak | Durum | Kanıt |
|---|---|---|
| **(1)** "Eşik 1.000.000 litre/yıl'dır" | ✅ **DÜZELDİ.** Kademeli indirim 2006 sonunda **600.000**'de bitmiştir. Kanun metnindeki 1.000.000 bugün uygulanan rakam değildir. | `EV-2026-08-10-204` (T1), `EV-2026-08-10-205` (T1) |
| **(2)** "Yaptırım mercii Tekel GM artık yok, hüküm fiilen uygulanamaz" | ✅ **ÇÜRÜDÜ** (proje aleyhine). 4733 m.4/B(b) 4250'nin uygulanmasını açıkça Bakanlığa vermiştir; 4733 m.8 artık fıkrası belge iptali yolunu açık tutar. | `EV-2026-08-10-208` (T1), `EV-2026-08-10-210` (T1) |
| **(3)** "Muafiyet fıkrası ithal durgun şarabı kapsamıyor olabilir" | ⚠️ **AÇIK** — ama **maddi değil**. Yeniden numaralandırıldı: **C-252** | `EV-2026-08-10-202` (T1) |

**Neden `NON_MATERIAL` öneriliyor:** C-201'in G0'ı bloke etme gerekçesi
*"beş hacim senaryosunun hukuki geçerliliği"* idi. Eşiğin **türü** (fiyatlandırma
serbestisi koşulu) ve **büyüklüğü** (600.000 L) kesinleştikten sonra, beş
senaryonun beşi de eşiğin **8–160 katı altındadır** ve eşik senaryolar arasında
ayrım yaratmamaktadır. Ayrıca eşiğin bağlı olduğu mekanizma ikincil mevzuata
aktarılmamıştır (`EV-2026-08-10-206`, `-209`).

**Bu ajan C-201'i KAPATMAMIŞTIR.** Kapatma başkanın yetkisindedir.

---

### B) YENİ ÇELİŞKİ — C-251

```yaml
conflict_id:        C-251
acilis_tarihi:      2026-08-10
acan_ajan:          mevzuat-ruhsat-uzmani
konu:               "2007 yilindan itibaren uygulanacak olcu 600.000 mi, kanun metnindeki 1.000.000 mi"
celiski_turu:       TANIM
impact:             LOW
model_girdisi_etkisi: YOK
durum:              OPEN

kaynak_a:
  evidence_id:      EV-2026-08-10-205
  iddia:            "Kademeli takvim 2006 sonunda 600.000 litre ile biter; '2007 yilindan itibaren uygulanacak olcuyu sifira indirmeye Bakanlar Kurulu yetkilidir' ifadesi, 2007'den itibaren UYGULANAN olcunun 600.000 oldugunu varsayar"
  value:            600000
  tier:             T1
  effective_date:   2003-06-06
  source_name:      "Alkol ve Alkollu Ickilerin Ic ve Dis Ticaretine Iliskin Usul ve Esaslar Hakkinda Yonetmelik Gecici m.6"

kaynak_b:
  evidence_id:      EV-2026-08-10-201
  iddia:            "Gecici hukmun kademeli takvimi tuketilmistir; asil kanun hukmu (m.1/3) 1.000.000 litre/yil demeye devam eder ve gecici hukum sona erdiginde asil hukum canlanir"
  value:            1000000
  tier:             T1
  effective_date:   2001-01-20
  source_name:      "4250 s.K. m.1 ucuncu fikra"
```

**Neden çözülemedi:** T1 ↔ T1, aynı kanun ailesi, ikisi de yürürlükte. Geçici
hükmün *"altıncı yıldan itibaren uygulanacak olan bu ölçü"* ifadesindeki *"bu
ölçü"*nün 600.000'e mi yoksa asıl hükümdeki 1.000.000'e mi gönderme yaptığı
lafzen belirsizdir. Tier, tarih, kapsam ve katman kurallarının hiçbiri
uygulanamıyor. Bu bir **hukuki yorum** sorunudur.

**Neden acele edilmesine gerek yok:** Bu proje için **maddi değildir.** Beş
senaryonun en büyüğü 75.000 litre/yıl'dır; her iki ölçüde de eşiğin çok
altındadır (%7,5 / %12,5). `EV-2026-08-10-215`.

**Kapanış yolu:** TADAB yazılı görüşü. Öncelik: **DÜŞÜK.**

---

### C) YENİ ÇELİŞKİ — C-252 *(C-201'in kalan ayağı)*

```yaml
conflict_id:        C-252
acilis_tarihi:      2026-08-10
acan_ajan:          mevzuat-ruhsat-uzmani
konu:               "4250 m.1 son fikrasindaki muafiyet ITHAL durgun sarabin fiyatlandirilmasi/dagitilmasi/satilmasini da kapsiyor mu"
celiski_turu:       TANIM
impact:             LOW
model_girdisi_etkisi: YOK   # her iki okumada da bes senaryo esigin altinda
durum:              OPEN
onceki_kayit:       "C-201'in ucuncu ayagi; bu turda ayri kayda alindi"
```

Fıkra metni (`EV-2026-08-10-202`, T1, yürürlük 2001-01-20):

> *"Bira ve her türlü şarap ve meyve şaraplarının üretimi, fiyatlandırılması,
> dağıtılması ve satılması ile viski ve tabii köpüren şarapların ithali,
> fiyatlandırılması, dağıtılması ve satılması bu maddede öngörülen şartlar
> aranmaksızın, bu Kanun hükümlerine göre serbesttir."*

| | Okuma A | Okuma B |
|---|---|---|
| **İddia** | Muafiyet **ürüne** bağlıdır: *her türlü şarabın* fiyatlandırılması, dağıtılması ve satılması — ithal olsun olmasın — m.1 şartlarından muaftır. Listede olmayan tek şey *ithal etme eylemi*dir; m.1/3'ün yaptırımı ise tam olarak fiyatlandırma/satış/dağıtımdır → **ithal şaraba uygulanamaz.** | Muafiyet yalnızca **yurt içinde üretilen** şaraba ilişkindir; kanun koyucu ithal yönünden bilinçli olarak yalnızca **viski ve tabiî köpüren şarabı** saymıştır → durgun şarap ithalatı m.1/3'e tabidir. |
| **Lafzî dayanak** | Tamlayan **ürün gruplarıdır** ("her türlü şarap"), "üretilen şaraplar" denmemiştir | "ile" bağlacıyla gelen ikinci kolda *ithal* ayrıca ve **sınırlı** sayılmıştır |
| **tier** | T1 (metin) | T1 (metin) |

**Neden çözülemedi:** Aynı cümlenin iki lafzî okuması. Tier/tarih/kapsam/katman
kurallarının hiçbiri uygulanamıyor. TUR 1 raporum yalnızca **B**'yi görmüştü;
**A** bu turda tespit edilmiştir ve en az B kadar lafzîdir. **Sessiz seçim
yapılmamıştır.**

**Neden karar açısından kritik değil:** B okuması doğru olsa bile, (i) beş
senaryonun beşi de eşiğin altındadır ve eşik bir *yasak* değil, bir *serbestlik
kazanma çizgisi*dir; (ii) eşiği aşamayanlar için öngörülen mekanizmanın ikincil
mevzuatta karşılığı yoktur (`EV-2026-08-10-206`, `-209`); (iii) o mekanizmanın
bugünkü ticari muhatabı `UNKNOWN`'dır (`EV-2026-08-10-214`).

**G0'ı yeniden bloke etmesi için gereken:** C-252'nin **B lehine** kapanması
**VE** aynı anda "Tekel GM eliyle" işlev için bir halef merci belirlendiğinin
tespiti. **İkisi birden** gerekir; tek başına hiçbiri bloke etmez.

**Kapanış yolu:** TADAB yazılı görüşü / alkol mevzuatında uzman hukuk bürosu
mütalaası. Öncelik: **DÜŞÜK.**

---

### D) DEĞİŞMEYENLER

`C-202` (HIGH, sıralama döngüsü), `C-203` (**CRITICAL**, 7584 s.K. raf kapsamı)
ve `C-204` (LOW, mülga dayanaklı TGK Şarap Tebliği) bu turda **ele alınmamıştır**
— tur mandası dışıdır. Durumları **değişmemiştir.**

---

## turkiye-pazar-kasifi (TUR 1.5)

> Bu dosya `99-ops/celiskiler.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından DOKUNULMAMIŞTIR.

---

### C-551 — Metro'nun ŞARAP kategorisinde çiftli KDV gösterimi (2010) vs genel broşürde tekli gösterim (2026)

```yaml
conflict_id:     C-551
acan_ajan:       turkiye-pazar-kasifi
acilis_tarihi:   2026-08-10
celiski_turu:    TARIH | KAPSAM  (hangisi olduğu BAŞKAN KARARI — T-551)
impact:          HIGH
durum:           OPEN
ticket:          T-551
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **evidence_id** | `EV-2026-08-09-503`, `EV-2026-08-09-504` | `EV-2026-08-10-503` |
| **tier / tarih** | T4 / 2026-08-01 – 2026-08-11 | T4 / 2008-12-04, 2009-12-03, **2010-12-09** |
| **Ne diyor** | Metro Türkiye broşürlerinde her fiyat **tek** sayıdır ve yanında `KDV'li` yazar; 58 sayfada tek bir "KDV hariç" ibaresi **yoktur**; ikinci küçük sayı **birim fiyattır** | Metro Türkiye **şarap** kataloglarının künyesi: *"Bu Metropost'taki fiyatlar **KDV Hariç ve KDV'li** olarak verilmiştir"*; fiyat kutuları **çifttir** (131,36 / 155,00 `KDV'li`; oran 1,18) |
| **Kapsam** | **Genel** broşür — içinde **0 alkol SKU'su** var (`EV-2026-08-09-514`) | **Şarap kategorisi** kataloğu |

#### Neden çelişki olarak kaydedildi

TUR 1, OQ-001'in kurucu hipotezini (*"Metro etiketinde KDV hariç + KDV dahil
birlikte gösterilebilir"*) **çürüdü** ilan etti. `EV-2026-08-10-503` bu
hipotezin Metro Türkiye'nin **şarap kategorisinde fiilen uygulanmış bir
format** olduğunu gösteriyor. Sonuç aynı kalabilir, ama gerekçe artık
"böyle bir format yoktur" olamaz.

#### Neden bu ajan tarafından ÇÖZÜLMEDİ

1. CLAUDE.md §1.13 — sessizce seçim yapılmaz.
2. TUR 1.5 görev tanımı KDV sonucunu **korunacak doğrulama** ilan etti;
   yeniden araştırma ve yeniden tartışma yasaklandı. Bulgu **T-504'ün**
   peşine düşerken ortaya çıktı; saklamak da ihlal olurdu.
3. `pazar.yaml`'da değer **DEĞİŞTİRİLMEDİ**; yalnızca `conflict_id: C-551`
   işareti kondu.

#### Çözüm hiyerarşisi hangi kuralı işaret ediyor

- **Kural 1 (tier):** uygulanamaz — ikisi de T4, ikisi de Metro'nun **kendi**
  künyeli yayını.
- **Kural 2 (tarih):** **A lehine** — 16 yıl fark; 2013 alkol reklam yasağı
  arada bir kırılma noktasıdır.
- **Kural 4 (kapsam):** **B lehine** — A, ilgilenilen kategoriyi (**şarap**)
  hiç içermez; B tam o kategoridir.

Kural 2 ve kural 4 **zıt yönü işaret ediyor.** Karar başkanındır → `T-551`.

#### Bu ajanın önerisi (karar değildir)

`benchmark_*.kdv_durumu` **`KDV_DAHIL` kalsın** (tarih kuralı + fiyat sonu
deseni), **ancak** `confidence` `HIGH`→`MEDIUM`'a çekilsin ve **BM_B
senaryosu ELENMESİN**. Kesin çözüm için gereken şey değişmiyor:
**şarap reyonundaki fiziksel etiketin fotoğrafı** (`T-504`).

---

---

# TUR 2 PRE-FLIGHT — BAŞKAN KAYITLARI

```yaml
tarih:      2026-08-10
yazan:      yatirim-komitesi-baskani
belge:      90-karar/tur-2-preflight-housekeeping.md
kapsam:     KAYIT BAKIMI — arastirma turu DEGILDIR, yatirim karari ICERMEZ
kural:      HICBIR CELISKI METNI SILINMEDI. Yalnizca 'durum' alanlari guncellendi.
```

---

## C-201 — **RESOLVED — NON_MATERIAL**

```yaml
conflict_id:      C-201
onceki_durum:     OPEN (CRITICAL)
yeni_durum:       RESOLVED — NON_MATERIAL
cozen:            yatirim-komitesi-baskani
cozum_tarihi:     2026-08-10
oneren:           mevzuat-ruhsat-uzmani (TUR 1.5) — oneri AYNEN kabul edildi
kalan_ayak:       C-252 (LOW)
bagli_ticket:     T-201 (RESOLVED)
```

**Karar:** `mevzuat-ruhsat-uzmani`'nın `RESOLVED — NON_MATERIAL` önerisi
**aynen kabul edilmiştir.** Öneriye hiçbir ekleme veya çıkarma yapılmamıştır.

**Gerekçe.** C-201'in G0'ı bloke etme sebebi *"beş hacim senaryosunun hukuki
geçerliliği"* idi. Üç ayağından ikisi TUR 1.5'te **kanıtla** düşmüştür:

| Ayak | Durum | Kanıt |
|---|---|---|
| (1) "Eşik 1.000.000 litre/yıl'dır" | **DÜZELDİ** — uygulanan ölçü en çok **600.000** | `EV-2026-08-10-204`, `EV-2026-08-10-205` (T1) |
| (2) "Yaptırım mercii yok, hüküm ölü" | **ÇÜRÜDÜ** (proje **aleyhine**) — 4250'nin uygulanması Bakanlığa devredilmiştir | `EV-2026-08-10-208`, `EV-2026-08-10-210` (T1) |
| (3) "Muafiyet fıkrası ithal durgun şarabı kapsamıyor olabilir" | **AÇIK** — ayrı kayda alındı → **C-252** | `EV-2026-08-10-202` (T1) |

Kalan ayak (3) **maddi değildir**: beş senaryonun beşi de eşiğin altındadır
(3.750–75.000 L vs 600.000 L; `EV-2026-08-10-215`) ve eşik **her iki okumada
da** model girdisini değiştirmez.

**Bu çözümün en zayıf yeri (dürüstlük kaydı):** Ayak (2) proje **aleyhine**
kapanmıştır — "hüküm fiilen uygulanamaz" argümanı **geçersizdir**. C-201'i
kapatan şey hükmün ölü olması değil, **ölçeğimizin ölçünün 8–160 katı altında
olmasıdır**. Bu ayrım korunmalıdır.

---

## C-251 — **OPEN (LOW) — AÇIK KALIR**

```yaml
conflict_id:      C-251
durum:            OPEN
impact:           LOW
model_girdisi_etkisi: YOK
baskan_notu_tarihi: 2026-08-10
```

**Karar: AÇIK KALIR. Kapatılmamıştır ve kapatılması için acele edilmeyecektir.**

**Gerekçe — neden kapatmıyorum:** C-251 (2007'den itibaren uygulanan ölçü
600.000 mi 1.000.000 mi) T1 ↔ T1 bir **hukuki yorum** sorunudur. Çözüm
hiyerarşisinin 1–5. kurallarının hiçbiri uygulanamaz. Kendi yorumumla kapatmam
CLAUDE.md §1.16 ihlali olur.

**Gerekçe — neden bloke etmiyor:** Beş senaryonun en büyüğü **75.000 litre/yıl**;
**600.000** ölçüsünün %12,5'i, **1.000.000** ölçüsünün %7,5'i. İki değerin
**hangisi doğru olursa olsun cevap aynıdır** (`EV-2026-08-10-215`). Bu, bir
çelişkinin *çözülmeden* zararsızlaştırıldığı meşru bir durumdur: sonuç
**girdi değerine duyarsızdır**.

**Ne zaman maddi hâle gelir:** Hacim **800.001 şişe/yıl**'a (600.000 L) yaklaşırsa.
Bu, en büyük senaryonun (S5, 100.000 şişe) **8 katıdır** ve bu projede
`SCALE` kararı bile böyle bir hacmi öngörmemektedir. `SCALE` tartışması
800.000 şişe/yıl'ı aşarsa **C-251 otomatik olarak yeniden gündeme gelir.**

---

## C-252 — **OPEN (LOW) — AÇIK KALIR**

```yaml
conflict_id:      C-252
durum:            OPEN
impact:           LOW
model_girdisi_etkisi: YOK
baskan_notu_tarihi: 2026-08-10
```

**Karar: AÇIK KALIR. Okuma A veya B lehine SEÇİM YAPILMAMIŞTIR.**

**Gerekçe — neden seçmiyorum:** Aynı cümlenin iki lafzî okuması; ikisi de T1,
ikisi de aynı yürürlük tarihli. `mevzuat-ruhsat-uzmani` TUR 1'de yalnızca B'yi
görmüş, TUR 1.5'te A'yı tespit etmiş ve **sessiz seçim yapmamıştır** — doğru
davranıştır. Ben de yapmıyorum.

**Gerekçe — neden bloke etmiyor:** B okuması (proje aleyhine olan) doğru olsa
**bile** eşik bir *yasak* değil, bir *serbestlik kazanma çizgisidir*; beş
senaryo zaten çizginin altındadır; ve çizginin altında kalanlar için öngörülen
mekanizmanın **ikincil mevzuatta karşılığı yoktur** (`EV-2026-08-10-206`,
`EV-2026-08-10-209`).

**G0'ı yeniden bloke etme koşulu (İKİSİ BİRDEN gerekir):**
1. C-252'nin **B lehine** kapanması, **VE**
2. "Tekel GM eliyle" işlev için yürürlükte bir **halef merci** tespiti
   (`EV-2026-08-10-214` bugün `UNKNOWN`).

Tek başına hiçbiri yetmez.

---

## C-203 — **ACCEPTED BUSINESS CONSTRAINT**

```yaml
conflict_id:      C-203
onceki_durum:     OPEN (CRITICAL)
yeni_durum:       ACCEPTED BUSINESS CONSTRAINT
onceki_impact:    CRITICAL
yeni_impact:      CONSTRAINT
karar_kaynagi:    KURUCU KARARI (baglayici) — arastirma bulgusu DEGILDIR
karar_tarihi:     2026-08-10
g0_etkisi:        BLOKE ETMEZ
bagli_ticket:     T-205 (RESOLVED — ACCEPTED_BUSINESS_CONSTRAINT)
yeniden_arastirilacak_mi: HAYIR
```

**Karar.** Kurucu kararı bağlayıcıdır:

> *"Alkol ürünlerine ilişkin reklam / görsel / tanıtım kısıtları bu projede
> **bilinçli olarak kabul edilen bir BUSINESS CONSTRAINT**'tir."*

**Bu, çelişkinin ÇÖZÜLDÜĞÜ anlamına gelmez.** 7584 s.K. m.2'nin dar/geniş
yorumu arasındaki lafzî gerilim **aynen durmaktadır** ve metni **silinmemiştir**
(bkz. yukarıda `mevzuat-ruhsat-uzmani` bölümü, C-203 satırı). Değişen şey
kaydın **statüsüdür**: bir *çözülmesi gereken belirsizlik* olmaktan çıkıp bir
*kabul edilmiş çerçeve şartı* olmuştur.

**Ne anlama geliyor:**

| Şudur | Şu DEĞİLDİR |
|---|---|
| Kısıt **doğrulanmış** (T1, `EV-2026-08-09-223`) ve **kabul edilmiştir** | Kısıt yok sayılmıştır |
| `kanal-marj-uzmani` için bir **VERİ / GİRDİ**'dir | `kanal-marj-uzmani` için bir belirsizliktir |
| Planlama, kısıtın **var olduğu** dünyaya göre yapılır | Kapsam belirsizliği çözülmüştür |

**Yön uyarısı — bu kabul MUHAFAZAKÂRDIR.** Reklam/tanıtım kaldıraçlarının
**yok** sayılması, kapsamın ileride **dar yorum** lehine netleşmesi hâlinde
proje **lehine** bir sürpriz bırakır. Bu sınıflandırma bir iyimserlik riski
taşımaz.

**Yeniden açılma koşulu:** TADAB'ın (veya bir yargı kararının) yasağı **ürünün
satış ünitesinde fiziksel olarak bulundurulmasını** kapsayacak şekilde yorumlayan
bağlayıcı bir metni. Bu durumda C-203 `OPEN`'a döner ve konu **G0 kapsamına**
girer — çünkü o zaman soru pazarlama değil, **kanalın varlığı** sorusudur.

---

## C-551 — **OPEN (HIGH) — `NON_BLOCKING_TUR2`**

```yaml
conflict_id:        C-551
durum:              OPEN
impact:             HIGH
celiski_turu:       TARIH | KAPSAM   # BELIRSIZ BIRAKILDI — secim yapilmadi
blocking_status:    NON_BLOCKING_TUR2
blocking_karari:    yatirim-komitesi-baskani, 2026-08-10
bagli_ticket:       T-551 (RESOLVED — DIRECTIVE_ISSUED)
kapanis_yolu:       T-504 (sarap reyonundaki fiziksel etiket fotografi)
```

**Karar: ÇÖZEMİYORUM — açık kalır; ama TUR 2'yi BLOKE ETMEZ.**

**Neden çözemiyorum (sessiz seçim yapmama gerekçesi):** Çözüm hiyerarşisinde
**kural 2 (tarih) A lehine**, **kural 4 (kapsam) B lehine** işaret ediyor ve
aralarında öncelik kuran bir üst kural yok. Kural 1 (tier) uygulanamıyor —
ikisi de T4 ve ikisi de Metro'nun **kendi künyeli** yayını. Bir tarafı seçmek
kanıta değil tercihe dayanırdı.

**Neden TUR 2'yi bloke etmiyor:** Kurucu kararı uyarınca benchmark
(`599,90 TL`) modelde **tek gerçek piyasa fiyatı olarak kullanılamaz** ve
**Metro cash & carry gözlemi** olduğu her kullanımda belirtilir. Bu kullanım
kuralı, C-551'in modele sızma yolunu kapatır. Ayrıca etki yönü **muhafazakârdır**:
sonuç "KDV hariç" çıkarsa benchmark'ın tüketici karşılığı **yukarı** kayar ve
proje **daha kolay** görünür — yani mevcut `KDV_DAHIL` etiketi projeyi
kayırmıyor, sıkıyor.

**Uygulanan tedbirler:**
1. `pazar.yaml` → `benchmark_1/2.kdv_durumu.confidence`: **HIGH → MEDIUM**
   (değer `KDV_DAHIL` **DEĞİŞTİRİLMEDİ**).
2. `pazar.yaml` → benchmark kayıtlarına **kullanım kuralı** (K5/K6) eklendi.
3. **BM_B senaryosu ELENMEZ** (başkan onayı, `T-551` S3).
4. Denetim §5.5'in "çiftli gösterim YOK" satırı **nitelendi** (`T-551` S4).

**Kapanış yolu (değişmedi):** `T-504` — şarap reyonundaki fiziksel etiketin
fotoğrafı. `C-551` ve `T-504` **aynı tek eylemle** kapanır.

---

## BU TURDA DEĞİŞMEYEN ÇELİŞKİLER

`C-202` (HIGH, sıralama döngüsü), `C-204` (LOW, TGK Şarap Tebliği dayanağı),
`C-301` (MEDIUM, palet bandı — **başkan direktifi aynen geçerli: band korunur**),
`C-501` (HIGH, feed tutarsızlığı) bu turda **ele alınmamıştır.**
Durumları **değişmemiştir** ve hiçbiri bu turda çözülmüş sayılmaz.

---

# TUR 2 ÇELİŞKİ KAYITLARI

TUR 2'de 8 yeni çelişki açıldı:

| conflict_id | Konu | impact | Açan |
|---|---|---|---|
| **C-311** | FCL base ocean navlunu: 295–650 USD vs 1.200–2.500 EUR — 4–5 kat fark | **CRITICAL** | `navlun-lojistik-uzmani` |
| C-312 | Terminal ardiye free time 0 gün mü 5 gün mü | MEDIUM | `navlun-lojistik-uzmani` |
| C-313 | Taşıyıcı THD ile terminal kapı-çıkış ücreti çift sayılıyor olabilir | MEDIUM | `navlun-lojistik-uzmani` |
| C-461 | "FOB" terimi kaynakta iki ayrı katmana işaret ediyor (FCL'de L1, MOQ siparişinde L0) | HIGH | `global-sourcing-kasifi` |
| C-462 | Düşük MOQ bandı 3.000–6.000 şişe; 5.000'lik pilot tam ortada | HIGH | `global-sourcing-kasifi` |
| C-561 | Stok dışı listeleme havuzu iki modlu — C-501 nitelendi, kapatılmadı | MEDIUM | `turkiye-pazar-kasifi` |
| **C-601** | Vade: yasal tavan 60 gün vs gözlenen Migros DPO ~93 gün | HIGH | `kanal-marj-uzmani` |
| C-602 | Tekel ve HoReCa marjı kaynaklarda tanımsız ve kendi içinde çelişkili | HIGH | `kanal-marj-uzmani` |
| C-161 | GTS menşe belgesi Form A mı REX mi (şarapta GTS uygulanmıyor, model etkisi yok) | LOW | `gumruk-vergi-uzmani` |

`navlun-lojistik-uzmani` ayrıca **C-302** için A lehine kapatma önerdi
(3. bağımsız kaynak bulundu); kapatmadı, başkana bıraktı.

## gumruk-vergi-uzmani (TUR 2)

> CLAUDE.md §1.13: Kaynaklar çelişirse **sessizce seçim yapılmaz.**
> Çelişki kayda geçirilir ve başkana taşınır.

---

### C-161 — GTS menşe belgesi: **Form A** mı, **REX Menşe Beyanı** mı?

```yaml
conflict_id:        C-161
acan:               gumruk-vergi-uzmani
tarih:              2026-08-10
impact:             LOW
model_girdisi_etkisi: YOK
status:             OPEN
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **Kaynak** | T.C. Ticaret Bakanlığı **Gümrük Rehberi** — "Menşe ispat ve dolaşım belgeleri nelerdir?" ve "Tercihli Ticaret Anlaşmaları" | GGM **BİLGE Sistemi Menşe Kontrol Tablosu**, `EAGZ` / `GYU` / `OTDU` satırları |
| **Tier** | T2 | T3 (belge GGM'nin, host İGMD) |
| **Tarih** | Yayın/yürürlük tarihi **yok** | 14.04.2026 · yürürlük **1/1/2026** |
| **İddia** | GTS kapsamındaki tavizden yararlanmak için **"Form A Menşe Belgesi"** ithalat sırasında gümrük idaresine sunulur | Aranacak belge **"1049 REX Menşe Beyanı"** |
| **evidence_id** | EV-2026-08-10-155 (aynı sayfa), EV-2026-08-10-163 | EV-2026-08-10-161 (aynı tablo) |

#### Neden çelişiyor

Muhtemel açıklama: AB'nin GTS'de **Form A'dan REX sistemine geçişi**ne uyum
sağlanmış, Gümrük Rehberi metni **güncellenmemiş**. Ancak bu bir **yorumdur**,
kanıt değildir — bu yüzden çelişki olarak kaydediyorum.

#### Neden **çözmüyorum**

Çözüm hiyerarşisinin tarih kuralı (B lehine: 1/1/2026 yürürlük) ile tier kuralı
(A lehine: T2 > T3) **zıt yönü** işaret ediyor. Kendi yorumumla kapatmam
CLAUDE.md §1.13 ihlali olur.

#### Neden **modeli bloke etmiyor**

**GTS şarapta hiçbir koşulda uygulanmaz** — üç bağımsız kanıtla
(`EV-2026-08-10-151`, `-153`, `-154`). Dolayısıyla GTS'de hangi belgenin
arandığı sorusunun `mense_tarife_eslemesi` üzerinde **etkisi yoktur.**
`model_girdisi_etkisi: YOK`.

#### Ne zaman maddi olur

Kapsam **22.05 (vermut/aromatize)** veya GTS sütunu bulunan başka bir
II sayılı Liste ürününe genişlerse. O durumda hem GTS uygulanabilir hâle gelir
hem bu çelişki maddileşir.

#### Ayrıca kayda geçirilen ikincil gözlem

Gümrük Rehberi'nin **hiçbir sayfasında yayın veya güncelleme tarihi
yayımlanmıyor.** Bu, T2 kaynağın **tazeliğinin ölçülemez** olduğu anlamına
gelir. Bu turda Gümrük Rehberi'nden alınan **tüm** kanıtlara `ttl: 180d` ve
`effective_date: -` yazılmıştır. Bu, C-161'in ötesinde **yapısal bir kaynak
zayıflığıdır** ve TUR 1'de `EV-2026-08-09-126` için not edilen sorunun
(revizyon 2018, KDV %18 yazıyordu) aynısıdır.

---

## navlun-lojistik-uzmani (TUR 2)

```yaml
ajan:  navlun-lojistik-uzmani
tur:   TUR 2
tarih: 2026-08-10
not:   "Bu dosya 99-ops/celiskiler.md'ye BASKAN tarafindan islenir. Ben ana dosyaya dokunmadim."
```

**Hiçbir çelişkide sessizce taraf seçilmemiştir.**

---

### C-311 — FCL base okyanus navlunu: yüzlerce USD mi, binlerce EUR mu?

```yaml
conflict_id:      C-311
konu:             "Ispanya/Avrupa -> Turkiye FCL base okyanus navlunu"
impact:           CRITICAL
status:           OPEN
model_girdisi_etkisi: VAR — bandin genisligi 4 kat
etkiledigi_alan:  lojistik.yaml -> tur2.fcl_navlun.ispanya_turkiye_20dv_base_ocean
```

#### Kaynak A — marketplace "from" fiyatları (düşük)

| Değer | Rota | tier | tarih | evidence_id |
|---|---|---|---|---|
| **295 USD** | Rotterdam → İzmir (13 gün) | T4 | **YOK** | `EV-2026-08-10-322` |
| **350 USD** | London Gateway → Mersin (13 gün) | T4 | YOK | `EV-2026-08-10-322` |
| **500 USD** | İstanbul → Barcelona (14 gün) | T4 | YOK | `EV-2026-08-10-322` |
| **650 USD** | Aarhus → İstanbul (19 gün) | T4 | YOK | `EV-2026-08-10-322` |

#### Kaynak B — blog/rehber bantları (yüksek)

| Değer | Rota | tier | tarih | evidence_id |
|---|---|---|---|---|
| **1.200–2.500 EUR** (20ft, ort. 1.800) | İspanya → Türkiye | **T5** | 2025 | `EV-2026-08-10-324` |
| **1.200–2.500 EUR** (20ft) | İspanya → Türkiye | **T5** | yok | `EV-2026-08-09-333` (TUR 1) |

#### Kaynak C — yayınlanmış taşıyıcı tarifesi (orta-yüksek, ama yanlış yön ve yıl)

| Değer | Rota | tier | yürürlük | evidence_id |
|---|---|---|---|---|
| **785–1.030 EUR** (20') | Türkiye → Trieste (**ihracat**) | T4 | **2025-01-01** | `EV-2026-08-10-320` |

#### Neden çelişiyor — üç olası açıklama, hiçbiri doğrulanmadı

| # | Hipotez | Lehine | Aleyhine |
|---|---|---|---|
| **H1** | Düşük rakamlar **yalnızca base ocean**, yüksek rakamlar **quasi-all-in** | TUR 2'de origin locals (349–554 EUR) ve destination locals (165–298 USD) ölçüldü; toplamları farkın **büyük kısmını açıklıyor** | Kaynak B "base rate" diyor ve üstüne %15–25 yakıt eklediğini yazıyor — yani kendisi de base olduğunu iddia ediyor |
| **H2** | Kaynak B **eski/geri dönüştürülmüş** veri | İki T5 kaynak **birebir aynı bandı** veriyor (1.200–2.500 EUR) → bağımsız değiller, biri diğerinden kopyalamış olabilir | Doğrulanamadı |
| **H3** | "from" fiyatları **gerçekleşmeyen taban fiyatlar** (pazarlama) | Marketplace'lerde yaygın pratik | Doğrulanamadı |

#### Bu turda ne yaptım

- **Taraf seçmedim.** Bandı olduğu gibi taşıdım: **300–1.200 USD**,
  `status: ESTIMATE`, `confidence: LOW`, `ttl: 14d`.
- `lojistik.yaml`'a "**merkezî varsayım olarak KULLANILAMAZ**" notu düştüm.
- LCL/FCL kırılma noktası bandının (2.200–9.800 şişe) **genişliğinin
  tamamının** bu çelişkiden geldiğini açıkça yazdım.

#### Nasıl çözülür

**Tek yolu var: bir forwarder'dan yazılı kotasyon** — kalem kalem
`included/excluded` listesiyle (`T-304`). Masabaşında çözülemez.

---

### C-312 — Terminal ardiye free time: 0 gün mü 5 gün mü?

```yaml
conflict_id:      C-312
konu:             "Turkiye ithalatinda terminal ardiye free time"
impact:           MEDIUM
status:           OPEN
model_girdisi_etkisi: VAR — 60 gunluk bekleme senaryosunda ~200 USD/konteyner
etkiledigi_alan:  lojistik.yaml -> tur2.terminal_tarifeleri.ardiye_free_time_gun
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **İddia** | Free time **0 gün** | Free time **5 gün** |
| **Metin** | "İthalat ardiye günleri **geminin yanaştığı günden itibaren** başlar" | "Ardiye 40–60 USD/gün, **6. günden itibaren**" |
| **Kaynak** | SafiPort 2026 konteyner ithalat tarifesi | Gümrük müşavirliği 2026 maliyet rehberi |
| **tier** | T4 (terminalin kendi tarifesi) | T4 (meslek uygulayıcısı) |
| **evidence_id** | `EV-2026-08-10-317` | `EV-2026-08-10-325` |

#### Değerlendirme

Çözüm hiyerarşisinin hiçbir kuralı uygulanamıyor: **ikisi de T4, ikisi de
2026.** Ayrıca **ikisi de doğru olabilir** — free time terminale göre
değişebilir ve Kaynak B bir *ortalama uygulama* anlatıyor olabilir.

#### Bu turda ne yaptım

Muhafazakâr olanı (**0 gün**) kullandım — TUR 1 ile aynı. **Bu bir seçim
değil, ihtiyattır** ve `lojistik.yaml`'da öyle etiketlendi.
Yön uyarısı: yanılıyorsam gecikme maliyeti tahminim **yüksektir**, yani hata
proje **lehine** değil aleyhine çalışıyor.

#### Nasıl çözülür

Kumport / Marport / Mardaş tarife PDF'lerinin doğrudan okunması veya
terminale yazılı soru (`T-313`).

---

### C-313 — Taşıyıcı THD'si ile terminal kapı-çıkış ücreti aynı olayı mı fiyatlıyor?

```yaml
conflict_id:      C-313
konu:             "Varis terminal ellecleme ucreti cift sayiliyor mu"
impact:           MEDIUM
status:           OPEN
model_girdisi_etkisi: VAR — konteyner basina ~115 USD (0,008-0,010 USD/sise)
etkiledigi_alan:  lojistik.yaml -> tur2.destination_charges_turkiye.thd_limana_gore
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **Kalem** | THD (Terminal Handling Charge Destination) | Kapı çıkış / terminal elleçleme |
| **Değer** | **165–298 USD** (limana göre) | **113–116 USD** |
| **Kesen** | Armatör (Hapag-Lloyd) | Terminal (Beldeport / SafiPort) |
| **tier** | **T3** (taşıyıcının resmî tarifesi) | T4 (terminalin tarifesi) |
| **evidence_id** | `EV-2026-08-10-315` | `EV-2026-08-10-319`, `-317` |

#### Neden bu bir çelişki

Fiziksel olay tektir: konteyner gemiden indirilir, sahada elleçlenir, kapıdan
çıkar. Ama **iki farklı taraf iki farklı tarife yayınlıyor.** Üç senaryo:

1. **Armatör terminale öder, importer'a THD olarak yansıtır** → tek kalem
   (165–298 USD), terminal tarifesi importer'ı ilgilendirmez.
2. **İkisi ayrı faturalanır** → toplam 278–414 USD.
3. **Merchant haulage / carrier haulage'a göre değişir** → duruma bağlı.

**TUR 1, Kaynak B'yi (113 USD) tek kalem olarak modele koymuştu.** Bu, Senaryo
1 doğruysa **%32–62 düşük** bir tahmindir.

#### Bu turda ne yaptım

Muhafazakâr olarak **yalnızca taşıyıcı THD'sini** (165–298 USD) hesaba kattım
ve çift sayım yapmadım. Terminal tarifesini ayrı bir bilgi olarak kayda
geçirdim. **Sessiz seçim değildir**: gerekçesi budur — taşıyıcı tarifesi T3,
terminal tarifesi T4 ve ithalatçının faturasını genellikle taşıyıcı keser.

#### Nasıl çözülür

Bir gerçek ithalat faturası örneği veya forwarder'ın kalem listesi (`T-304`
RFQ'suyla aynı temasta, `T-313`).

---

### TUR 1 ÇELİŞKİLERİNİN TUR 2 SONRASI DURUMU

#### C-302 — Akdeniz transit süresi → **A LEHİNE KAPATILMASI ÖNERİLİR**

```yaml
conflict_id:      C-302
tur2_onerisi:     "A tarafi lehine RESOLVED"
karar_yetkisi:    yatirim-komitesi-baskani
oneri_sahibi:     navlun-lojistik-uzmani
```

**Yeni kanıt:** Flexport (T4, tarihli 2026-08-10, geçerlilik 2026-08-16)
Valencia/Barcelona → İstanbul için **4 gün** veriyor (`EV-2026-08-10-301`,
`-302`).

| Taraf | İddia | Kaynak sayısı | Durum |
|---|---|---|---|
| **A** | İspanya → İstanbul **4–10 gün** | **3** (JSV T4 + Maersk servis tarifesi T3 + **Flexport T4**) | ✅ güçlendi |
| **B** | Valencia → İstanbul **32–35 gün**; LA → İstanbul **15 gün** | 1 (BR Logistics T5) | ❌ tek başına |

**Ek olarak B'nin ikinci ayağı da yanlışlandı:** LA → İstanbul gerçek süre
**20 gün** (kara aktarmalı) veya **44 gün** (deniz aktarmalı)
(`EV-2026-08-10-309`). **15 gün hiçbir kaynakla doğrulanmadı.**

**Önerim:** `C-302` → `RESOLVED (A lehine)`; B kaynağının (BR Logistics)
tüm transit iddiaları `REJECTED` sayılsın. **Kapatma yetkisi bende değildir.**

#### C-301 (palet sayısı) — **DEĞİŞMEDİ**, TUR 2'de yeni kanıt bulunamadı, `OPEN`.

#### C-303 (20DV payload) — **DEĞİŞMEDİ**, düşük etkili, `OPEN`.

---

### TUR 1'İN BİR TAHMİNİNİN DÜZELTİLMESİ *(çelişki değil, hata)*

Bu bir çelişki değil, **kendi TUR 1 tahminimin yanlışlanmasıdır** ve kayda
geçirilmesi gerekir:

| | TUR 1 | **TUR 2 (doğru)** |
|---|---|---|
| G. Afrika → Türkiye transit | **~26 gün** | **49 gün** |
| Dayanak | Türkiye → Cape Town **ters yön** ölçümü | Cape Town → İstanbul doğrudan kotasyon, Hamburg aktarmalı |
| evidence_id | `EV-2026-08-09-327` | `EV-2026-08-10-307` |

**TUR 1 tahmini yaklaşık 2 kat iyimserdi.** Sebep: ters yön ölçümü, aktarma
yapısını yansıtmaz. Bu, **ters yön verisinin neden kullanılmaması gerektiğinin
somut örneğidir** ve `EV-2026-08-09-327`'nin `SUPERSEDED` sayılması önerilir.

---

## global-sourcing-kasifi (TUR 2)

> `99-ops/celiskiler.md` dosyasına **DOKUNULMAMIŞTIR** (başkan birleştirir).
> **Hiçbiri sessizce çözülmemiştir.**
> TUR 1'de açılan `C-401`, `C-402`, `C-403` bu turda da **OPEN** kalmıştır.

---

### C-461 — "FOB" terimi iki farklı katmana işaret ediyor

```yaml
conflict_id:      C-461
opened_by:        global-sourcing-kasifi
opened_date:      2026-08-10
impact:           HIGH
status:           OPEN
model_girdisi_etkisi: VAR — L0/L1 ayrımı
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **İddia** | "FOB" = Incoterms® 2020 FOB, **adı belirtilen yükleme limanı bordası** → **L1** | "FOB" = şarap ticaretinde üreticinin ithalatçıya verdiği **ex-cellar** fiyat → fiilen **L0** |
| **Kaynak** | Incoterms® 2020 (genel kabul) + Harland sayfasının kendi açıklaması ("...until your container is loaded onto the ship") | WineWiki (Wine with Seth) — "FOB — Free on Board" maddesi, `EV-2026-08-10-468` |
| **Tier/tarih** | T4 / 2026-08-10 | T4 / 2026-08-10 |

**Neden çelişiyor:** Aynı üç harf, maliyet merdiveninin **iki farklı basamağını**
adlandırıyor ve aralarında iç nakliye + liman + ihracat gümrüklemesi farkı var.

**Somut tetikleyici:** `EV-2026-08-10-451` — Harland aynı fiyatı ("$2.85+") tam
konteyner siparişinde **FOB**, MOQ siparişinde **ex factory** olarak tanımlıyor.
Yani **tek yayınlanmış sayı, sipariş büyüklüğüne göre L0 veya L1 oluyor.**

**Bu ajanın uyguladığı geçici kural:** Incoterm metinde açıkça tanımlanmadan
hiçbir fiyat L0 veya L1 diye etiketlenmez; `supplier-shortlist-v2.csv`'de
`price_layer` kolonu ayrı tutulur ve belirsizse belirsizliği yazar.

**Nasıl kapanır:** RFQ 3.1 (EXW + **yer**) ve 3.2 (FOB + **adı belirtilen liman**)
cevaplarıyla, tedarikçi bazında. Genel olarak kapanmaz — **her teklif için ayrı ayrı** kapanır.

**Kime taşınıyor:** `gumruk-vergi-uzmani` (gümrük kıymeti matrahı), `finans-fizibilite` (katman disiplini).

---

### C-462 — Doğrulanmış private label MOQ aralığı, pilot hacmini hem kapsıyor hem aşıyor

```yaml
conflict_id:      C-462
opened_by:        global-sourcing-kasifi
opened_date:      2026-08-10
impact:           HIGH
status:           OPEN
iliskili:         C-401 (TUR 1, OPEN — kapatılmadı)
model_girdisi_etkisi: VAR — pilot senaryosunun uygulanabilirliği
```

| | Kaynak A | Kaynak B | Kaynak C |
|---|---|---|---|
| **İddia** | MOQ **3.000–3.600** şişe | MOQ **6.000** şişe | MOQ **300–1.200** şişe |
| **Kaynak** | Interbrosa (ES) `EV-2026-08-09-408`; The Wine Factory (FR) `EV-2026-08-09-410`; Clark Estate (NZ) `EV-2026-08-10-455` | Cantina Danese (IT) `EV-2026-08-10-453`; Harland (AU) `EV-2026-08-10-452` | usetorg.com agregatörü `EV-2026-08-09-424` |
| **Tier** | T4 (üretici beyanı) | T4 (üretici beyanı) | T5 (agregatör) |

**Neden çelişiyor:** Üst uç ile alt uç arasında **20 kat** fark var. Daha kritiği:
**charter'ın 5.000 şişelik pilot hacmi tam bu aralığın ortasına düşüyor.**
Yani MOQ, pilotu ne kesin olarak mümkün ne kesin olarak imkânsız kılıyor —
**tedarikçiye göre değişiyor.**

**TUR 1'in ifadesinin nitelenmesi (`EV-2026-08-10-471`):**
TUR 1 raporu B-1'de *"3.000–3.600 şişe … charter'ın 5.000 şişelik pilot hacmiyle
UYUMLUDUR"* diyordu. Bu **hâlâ doğru ama artık eksiktir**: MOQ'su bilinen beş
üreticinin **üçüyle** pilot mümkün, **ikisiyle değil.**

**Bu bir CONFLICT'tir, ortalama alınamaz.** 3.000 ile 6.000'in ortalamasını
almak (4.500) hiçbir üreticinin gerçek MOQ'su değildir ve modele giremez.

**Nasıl kapanır:** RFQ 3.6a/3.6b + 4.2/4.3 ile, **tedarikçi bazında**.
Genel bir "sektör MOQ'su" yoktur — bu turun bulgusu tam olarak budur:
**MOQ ülke veya sektör özelliği değil, firma özelliğidir.**

**Kime taşınıyor:** `finans-fizibilite` (5.000 vs 10.000 şişe senaryolarının
tedarikçi havuzu farkı), `seytanin-avukati` (pilot mantığının kırılganlığı).

---

### TUR 1'DEN DEVREDEN VE HÂLÂ AÇIK OLANLAR

| conflict_id | Konu | TUR 2'de ne oldu |
|---|---|---|
| **C-401** | T5 agregatör MOQ 300–1.200 vs doğrulanmış üretici beyanları | **AÇIK.** TUR 2'de doğrulanmış üst sınır 3.600'den 6.000'e çıktı → makas **genişledi**. C-462 bu genişlemeyi kaydeder, C-401'i kapatmaz |
| **C-402** | Benchmark California menşeli ama ABD→TR ithalatı 18.298 l / ort. CIF 25,19 USD/l | **AÇIK.** TUR 2'de iki ABD private label sağlayıcısı daha bulundu (O'Neill, Bronco adayı) ama **hiçbiri Türkiye'ye ihracat kabiliyeti beyan etmedi** — çelişki derinleşti, çözülmedi |
| **C-403** | Benchmark ürünün California alt bölgesi: Sierra Foothills mı Central Valley mi | **AÇIK.** `EV-2026-08-10-463` (O'Neill ana tesisi Parlier/Central Valley) "Central Valley" ayağını **dolaylı** destekler ama iki T5 kaynağı arasındaki çelişkiyi **çözmez** |

---

## turkiye-pazar-kasifi (TUR 2)

> Bu dosya `99-ops/celiskiler.md` içine **başkan tarafından** merge edilir.
> Bu ajan ana dosyaya dokunmamıştır.

---

### C-561 — Stokta olmayan ithal listelemeler tek bir "geçersiz" havuz mudur?

```yaml
conflict_id:   C-561
opened_by:     turkiye-pazar-kasifi
opened_date:   2026-08-10
status:        OPEN
ticket:        T-561
ilgili:        C-501 (TUR 1, OPEN) — bu çelişki onun NİTELENMESİDİR, yerine geçmez
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **Kayıt** | `EV-2026-08-09-509` / `EV-2026-08-10-501` (T4, 2026-08-09) | `EV-2026-08-10-552` (T4, 2026-08-10) |
| **İddia** | Stokta olmayan ithal listelemelerde "70–450 TL gibi 2026 için gerçeklik dışı fiyatlar" vardır → havuz **bütünüyle** dışlanır (`C-501`) | Aynı havuz sayıldığında **iki modludur**: 44 kayıt < 500 TL (gerçeklik dışı), **62 kayıt 500–1.000 TL** (2026 için makul), 243 kayıt > 1.000 TL |
| **Tier / tarih** | T4 / 2026-08-09 | T4 / 2026-08-10 |

#### Neden çelişki

`C-501`'in gerekçesi **düşük uçtaki** kayıtlardan türetilmiş, ama sonucu **tüm**
stokta-olmayan havuza uygulanmıştır. TUR 2 sayımı gösteriyor ki düşük uç havuzun
yalnızca **%12,6**'sıdır (44/349). Geri kalan kayıtlar için "bakımsız eski fiyat"
gerekçesi **doğrudan kanıtlanmamıştır**.

Bu, `pazar.yaml → segment.ithal_sku_400_800_uzman_kanal = 0` değerinin dayanağını
doğrudan etkiler.

#### Çözüm hiyerarşisi bu vakada ne diyor

- **Tarih kuralı:** B daha yenidir (2026-08-10) → B'yi işaret eder.
- **Kaynak otoritesi:** ikisi de T4, ikisi de aynı feed → ayırt etmiyor.
- **Kapsam kuralı:** B daha dar ve daha ölçülmüş bir iddiadır → B'yi işaret eder.

**Ama:** B, A'nın *sonucunu* çürütmez. Her iki durumda da **stokta olmayan bir fiyat
satın alınabilir bir fiyat değildir** ve raf fiyatı sayılamaz. Çelişki, "0 ithal SKU"
cümlesinin **anlamı** hakkındadır: *yok* mu, *var ama satılmıyor* mu?

#### Bu ajanın yaptığı / yapmadığı

- **Yapmadım:** `pazar.yaml`'da hiçbir değeri değiştirmedim; C-501'i kapatmadım;
  62 listelemeyi raf fiyatı saymadım.
- **Yaptım:** Sayımı kanıtladım (`EV-2026-08-10-552`), 62 satırı
  `raf-fiyat-gozlemleri.csv`'ye `gozlem_yontemi = ONLINE_LISTING_STOKTA_YOK` ve
  `status = UNKNOWN` ile ekledim, `T-561` ile başkana taşıdım.

#### Karar kime ait

`yatirim-komitesi-baskani` — `T-561`.

---

### İZLEME — TUR 1/1.5'ten devreden ve TUR 2'de ELE ALINMAYANLAR

| conflict_id | Durum | TUR 2 notu |
|---|---|---|
| `C-501` | OPEN | `C-561` ile **nitelendi**, çözülmedi |
| `C-502` | OPEN (izleme) | Ele alınmadı |
| `C-503` | RESOLVED (başkan) | Ele alınmadı |
| `C-551` | OPEN / NON_BLOCKING_TUR2 | **Kasten ele alınmadı** — TUR 2 kapsam sınırı: benchmark KDV/promosyon araştırması yasaklandı |

---

### POTANSİYEL ÇELİŞKİ — AÇILMADI, İZ BIRAKILDI

**J.P. Chenet'nin Türkiye ithalatçısı kim?**
`EV-2026-08-10-562` (T5) **Baron Şarapçılık** diyor. Ancak `interaytrading.com`
adlı başka bir firma da sitesinde "J.P. CHENET Ürünleri" sayfası tutmaktadır.
Bu bir alt-bayilik mi, eski bir ithalatçı mı, yoksa gerçek bir çelişki mi
**doğrulanamadı**. Her iki kaynak da T5/T4-zayıftır ve modele girmemektedir;
bu nedenle **çelişki kaydı AÇILMAMIŞ**, `OQ-551` altında açık soru olarak
bırakılmıştır.

---

## kanal-marj-uzmani (TUR 2)

> Bu bir **parça dosyasıdır**. `99-ops/celiskiler.md` ana dosyasına
> `yatirim-komitesi-baskani` tarafından birleştirilir. Bu ajan ana dosyaya
> **DOKUNMAMIŞTIR**.
>
> CLAUDE.md §1.13: kaynaklar çelişirse **sessizce seçim yapılmaz.**
> Aşağıdaki iki çelişkide de **seçim yapılmamıştır.**

---

### C-601 — Zincir market ödeme vadesi: yasal tavan vs gözlenen pratik

```yaml
conflict_id:  C-601
acan_ajan:    kanal-marj-uzmani
tarih:        2026-08-10
durum:        OPEN
etki:         CRITICAL   # peak_cash_requirement'in en buyuk tek surucusu
```

| | Kaynak A | Kaynak B | Kaynak C |
|---|---|---|---|
| **İddia** | Ödeme süresi **60 günü geçemez** | Organize kanal ortalama vadesi **70 gün** | Migros ticari borçlarının **%34,4'ü 3–12 ay** vadeli; DPO **~93 gün** |
| **evidence** | `EV-2026-08-10-602` | `EV-2026-08-10-609` | `EV-2026-08-10-617` |
| **tier** | T3 (içerik T1) | T2 | T4 (denetimden geçmiş) |
| **tarih** | yürürlük **2024-01-01** | veri **2020** | veri **2025-12-31** |
| **kategori** | tarım-gıda ürünleri (şarap kapsamı **?**) | **süt ürünleri** | tüm kategoriler, tüm coğrafya |

#### Neden çelişiyor

- **Zaman:** Kaynak B, 60 gün tavanının yürürlüğe girdiği 01.01.2024'ten **önceki**
  dönemi ölçer. Yani B, A'yı çürütmez — A'nın **niçin çıkarıldığını** açıklar.
- **Ama Kaynak C 2025 verisidir**, yani **tavan yürürlükteyken** alınmıştır ve
  borçların üçte biri 3–12 ay vadelidir. Bu, üç şeyden biri anlamına gelir:
  1. Şarap/gıda **tavan kapsamında değildir** (→ `T-601`),
  2. Kapsamdadır ama **ölçek testi** (küçük/orta alacaklı + orta/büyük borçlu)
     ya da **KOBİ Vasfı Belgesi değişimi** (`EV-2026-08-10-607`) yapılmadığı için
     tavan işlemiyordur,
  3. Migros'un ticari borçları büyük ölçüde **gıda dışı** ve **yurt dışı** kalemlerden
     oluşuyordur (bu ayrıştırma finansallarda **yoktur**).
- Ayrıca Kaynak B'nin **dipnot 69'u** bizzat şunu söyler: bildirilen süreler bazı
  firmalarda **sözleşmedeki standart sürelerdir** ve *"fiili süreler aslında
  sözleşmede yer alan sürelerden çok daha uzun olabilmektedir."*

#### Bu ajanın YAPMADIĞI

Sessiz seçim yapılmamış, tek bir vade değeri **modele yazılmamıştır**.
`kanal.yaml → zincir_market.odeme_vadesi_gun = null / UNKNOWN`.
Bunun yerine **dört ayrı senaryo** tanımlanmıştır: 45 / **60** / 90 / **120** gün.

#### Nasıl kapanır

`T-601` (şarap "tarım ve gıda ürünü" müdür?) + `T-604` (gerçek yıllık anlaşma
görüşmesi). İkisi de kapanmadan bu çelişki **çözülemez**.

---

### C-602 — Tekel bayii ve HoReCa marjı: kaynaklar hem çelişiyor hem tanımsız

```yaml
conflict_id:  C-602
acan_ajan:    kanal-marj-uzmani
tarih:        2026-08-10
durum:        OPEN
etki:         MEDIUM   # kanal 2 ve 3; charter oncelik sirasi 2 ve 3
```

#### Tekel bayii

| İddia | Kaynak tipi | Sorun |
|---|---|---|
| "alkolde ~%17" | T5 içerik sitesi | margin mi markup mı **belirtilmemiş** |
| "rakı %8" | T5 içerik sitesi | ürün kategorisi farklı; taban belirtilmemiş |
| "brüt %10–15" | T5 forum | katman çifti belirtilmemiş |
| "ciro üzerinden %18–30" | T5 içerik sitesi | "ciro üzerinden" ifadesi **tanımsız** |

`evidence`: `EV-2026-08-10-620` (negatif kayıt)

#### HoReCa

| İddia | Kaynak | Sorun |
|---|---|---|
| "perakende fiyatının **2 katı**" | Milliyet / Murat Bozok, 2012 | Çarpan **L8** üzerine |
| "toptan fiyatının **2,5 katı**" | **aynı yazı** | Çarpan **L7** üzerine |
| "market fiyatının **4–5 katı**" | **aynı yazı** | Yine **L8** üzerine, ve "gözlenen üst uç" |

`evidence`: `EV-2026-08-10-618`

#### Neden bu bir "çelişki" olarak kaydedildi, "veri yok" olarak değil

Çünkü çelişki **kaynaklar arasında değil, kaynakların KENDİ İÇİNDEDİR.**
Tek bir yazı çarpanı **iki farklı katmandan** verir. Bu, sayının kendisinden
daha bilgilendirici bir bulgudur: **bu alanda konuşulan "marj" rakamları
tanımsız konuşulmaktadır** — ki `M1` kuralının varlık sebebi tam olarak budur.

#### Bu ajanın YAPMADIĞI

Bu sayıların **hiçbiri** `kanal.yaml`'a `value` olarak yazılmamıştır.
`tekel_bayi.marj_pct` ve `horeca.fiyat_carpani` **UNKNOWN**'dır.
Duyarlılık bantları `ASSUMPTION` olarak ve **kanıtlı çapası olmadığı açıkça
yazılarak** ayrı blokta tutulmuştur.

#### Nasıl kapanır

Yalnızca gerçek bayi/HoReCa görüşmesi veya gerçek bir fiyat listesi (`T-604`).
Masabaşı ile kapanmaz.

---

# TUR 2 SONU — BAŞKAN ÇÖZÜM KAYITLARI

```yaml
cozen:          yatirim-komitesi-baskani
cozum_tarihi:   2026-08-10
dayanak:        90-karar/tur-2-konsolidasyon.md §3
kural:          bu dosyadaki "COZUM HIYERARSISI (BASKAN ICIN)" 7 adimi
kapsam:         TUR 2'de acilan 9 celiski + C-302 kapatma onerisi
sonuc:          "COZULEN 6 · ACIK KALAN 3"
```

> Bu bölüm yalnızca `durum` / `cozum` / `cozen` / `cozum_tarihi` alanlarını
> doldurur. Yukarıdaki ajan fragment'lerinin **hiçbir cümlesi silinmemiş veya
> değiştirilmemiştir.**
>
> **Başkan hiçbir çelişkinin `impact` değerini yükseltmemiş veya
> düşürmemiştir.** Başkan hiçbir yeni sayı üretmemiştir.

---

## ÖZET TABLO — TUR 2 ÇELİŞKİLERİ

| conflict_id | Konu | impact | **durum (2026-08-10)** | Uygulanan kural |
|---|---|---|---|---|
| **C-302** | Akdeniz/ABD transit süresi | HIGH | **RESOLVED — TEYİT EDİLDİ** *(2026-08-09'da kapanmıştı)* | Kural 1 |
| **C-311** | FCL base ocean 295–650 USD vs 1.200–2.500 EUR | **CRITICAL** | **OPEN — KISMEN DARALTILDI** | Kural 1 → Kural 6 |
| **C-312** | Ardiye free time 0 gün mü 5 gün mü | MEDIUM | **RESOLVED — KAPSAM** | Kural 4 |
| **C-313** | THD ↔ terminal kapı-çıkış çift sayımı | MEDIUM | **OPEN — NON-MATERIAL (TUR 3)** | Kural 6 |
| **C-461** | "FOB" iki farklı katmana işaret ediyor | HIGH | **RESOLVED — KATMAN** | Kural 5 |
| **C-462** | MOQ 3.000–6.000; pilot tam ortada | HIGH | **RESOLVED — KAPSAM** | Kural 4 |
| **C-561** | Stok dışı listeleme havuzu iki modlu | MEDIUM | **RESOLVED — TANIM** | Kural 2 + 4 |
| **C-601** | Vade: yasal tavan 60 vs Migros DPO ~93 gün | HIGH | **OPEN — İKİ KAYNAK YENİDEN KAPSAMLANDI** | Kural 2 + 4 → Kural 6 |
| **C-602** | Tekel/HoReCa marjı tanımsız | HIGH | **RESOLVED — SAHTE ÇELİŞKİ** | Kural 1 |
| **C-161** | GTS'te Form A mı REX mi | LOW | **RESOLVED — NON_MATERIAL (kapsam dışı)** | Kural 4 |

---

## C-302 — **RESOLVED — TEYİT EDİLDİ** *(yeni bir kapanış DEĞİLDİR)*

```yaml
conflict_id:       C-302
durum:             RESOLVED            # DEGISMEDI — 2026-08-09'da kapanmisti
cozum_evidence_id: EV-2026-08-09-325, EV-2026-08-09-326, EV-2026-08-10-301, EV-2026-08-10-302, EV-2026-08-10-309
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-09          # ILK KAPANIS
teyit_tarihi:      2026-08-10          # TUR 2 teyidi
oneri_sahibi:      navlun-lojistik-uzmani (TUR 2) — KABUL EDILDI
```

**Karar:** `navlun-lojistik-uzmani`'nın *"A lehine kapatılmasını öneriyorum"*
önerisi **kabul edilmiştir** — ancak bir **kayıt notuyla**: `C-302`
**2026-08-09'da zaten `RESOLVED` yapılmıştı** (Kaynak B, BR Logistics, T5,
bütünüyle diskalifiye edilmişti). TUR 2 önerisi bir **yeni kapanış değil, bir
teyittir** ve öyle kaydedilir.

**TUR 2'nin eklediği iki şey:**

1. **Üçüncü bağımsız kaynak.** Flexport (T4, tarihli 2026-08-10, geçerlilik
   2026-08-16) Valencia/Barcelona → İstanbul için **4 gün** veriyor
   (`EV-2026-08-10-301`, `-302`). A tarafı artık **3 bağımsız kaynaktır**
   (JSV T4 + Maersk servis tarifesi T3 + Flexport T4) ve Akdeniz transit
   bandı **7–10 günden 4–10 güne** genişlemiştir *(aşağı yönde)*.
2. **Kaynak B'nin ikinci ayağı POZİTİF OLARAK yanlışlandı.** 2026-08-09'da
   *"LA → İstanbul 15 gün"* iddiası yalnızca **modele alınmamıştı**
   (kaynak yok diye `UNKNOWN`). TUR 2'de gerçek süre ölçüldü: **20 gün**
   (kara aktarmalı, Atlanta→Kumport) veya **44 gün** (deniz aktarmalı, Savannah)
   — `EV-2026-08-10-309`. **15 gün iddiası artık `REJECTED`'dır**, `UNKNOWN`
   değil.

**Bağlı kayıt — `EV-2026-08-09-327` (G. Afrika ~26 gün):**
`navlun-lojistik-uzmani` kendi TUR 1 tahmininin **~2 kat iyimser** olduğunu
tespit etmiş ve kartın `SUPERSEDED` sayılmasını önermiştir (gerçek: **49 gün**,
Hamburg aktarmalı, `EV-2026-08-10-307`). **Öneri kabul edilmiştir.**
⚠ **Kartın `status` alanını başkan değiştirmez** — kanıt kartları immutable'dır
ve `supersedes` bağı kartı açan ajan tarafından kurulur. Bu, ters yön
ölçümünün neden kullanılmaması gerektiğinin **somut örneği** olarak kayda
geçirilmiştir.

---

## C-311 — **OPEN (CRITICAL) — KISMEN DARALTILDI, BAND DARALMADI**

```yaml
conflict_id:       C-311
durum:             OPEN                # CEKIRDEK COZULMEDI
impact:            CRITICAL            # DEGISMEDI
kismi_karar:       T5_BACAGI_ELENDI
elenen_kartlar:    [EV-2026-08-10-324, EV-2026-08-09-333]
band_degisti_mi:   HAYIR               # 300-1.200 USD AYNEN KALIR
cozen:             yatirim-komitesi-baskani
karar_tarihi:      2026-08-10
kapanis_yolu:      T-304 (3 forwarder'dan yazili, kalem kirilimli FCL kotasyonu)
bloke_ettigi_gate: G2-L
```

### Yapabildiğim — Kaynak B elendi (Kural 1)

`EV-2026-08-10-324` (FreightAmigo) ve `EV-2026-08-09-333` (BR Logistics) **her
ikisi de T5**'tir ve **birebir aynı bandı** verirler: `1.200–2.500 EUR`.
İki kaynağın **aynı sayı çiftini** vermesi bağımsız doğrulama değil, **kopya
göstergesidir** — biri diğerinden alınmış olabilir ve hiçbiri kendi kaynağını
belirtmez.

**CLAUDE.md §2:** T5 tek başına sonuç üretemez.
**Karar: bu iki kart, SONUÇ ÜRETEN kaynak olarak ELENMİŞTİR.** Yalnızca
"nereye bakılacağını gösteren ipucu" olarak kayıtta kalırlar.

*(Not: `EV-2026-08-09-333`, `C-302`'de aynı ajanın — BR Logistics — transit
iddiaları nedeniyle **zaten diskalifiye edilmiş** bir kaynaktır. Aynı kaynağın
navlun bandının hâlâ kullanılıyor olması bir **tutarlılık boşluğuydu** ve bu
kararla kapanmıştır.)*

### Yapamadığım — bandı daraltmak

Eleme sonrası geriye kalan **Kaynak A** (`EV-2026-08-10-322`, Freightify
marketplace *"from"* fiyatları: 295 / 350 / 500 / 650 USD):
- **tarihi YOKTUR**,
- **konteyner boyu belirtilmemiştir**,
- bir **"from" teaser fiyatıdır** (H3 hipotezi: gerçekleşmeyen taban fiyat).

Bu üç eksik nedeniyle Kaynak A **kendi başına bir `FACT` üretemez** ve bandın
alt ucunu **sabitleyemez**.

**Bandın üst ucu yeniden temellendirilmiştir:** artık T5 bloglara değil,
`EV-2026-08-10-320`'ye (**DFDS yayınlanmış tarifesi, T4, tarihli, yürürlük
2025-01-01**) dayanır — ki o da **ters yön (ihracat)** ve **2025**'tir ve
yalnızca **mertebe çapası** olarak kullanılabilir.

### Sonuç

```
20DV base ocean freight  =  300 – 1.200 USD    [DEGISMEDI]
status: ESTIMATE · confidence: LOW · ttl: 14d
```

**Kaynak temizlendi, belirsizlik daralmadı.** Bir bandın **gerekçesini**
iyileştirmek onu **daraltmakla aynı şey değildir** ve öyle sunulmamalıdır.

**Bağlayıcı model kuralı (M-6):** Bandın **ortalaması alınamaz.**
300 USD ve 1.200 USD **ayrı ayrı** çalıştırılır. `lojistik.yaml`'daki
*"merkezî varsayım olarak KULLANILAMAZ"* notu **yürürlüktedir**.

**LCL/FCL kırılma bandının (2.200–9.800 şişe) genişliğinin TAMAMI bu
çelişkiden gelmektedir.** `T-304` kapanmadan bu band daralmaz.

---

## C-312 — **RESOLVED — KAPSAM (sahte çelişki)**

```yaml
conflict_id:       C-312
celiski_turu:      KAPSAM              # DEGER celiskisi DEGIL
durum:             RESOLVED
impact:            MEDIUM
cozum_evidence_id: EV-2026-08-10-317   # SafiPort kendi tarifesi
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-10
model_degeri_degisti_mi: HAYIR         # 0 gun (muhafazakar) AYNEN KALIR
```

**Karar: Bu bir değer çelişkisi değil, bir KAPSAM farkıdır (Kural 4).**

| | Kaynak A | Kaynak B |
|---|---|---|
| Ne ölçüyor | **SafiPort'un KENDİ tarifesi** — bir terminalin kendi resmî fiyatlandırması | Bir gümrük müşavirliğinin **genel maliyet rehberi** — terminal adı **belirtilmemiş**, ortalama bir uygulama anlatıyor |
| Popülasyon | **1 terminal** | **belirsiz sayıda terminal** |

İki kaynak **aynı şey hakkında konuşmamaktadır.** SafiPort'un tarifesi
SafiPort için bağlayıcıdır; müşavirlik rehberi başka bir terminali veya bir
ortalamayı tarif ediyor olabilir. Günlük ücretlerin de birbirine yakın olması
(SafiPort 39–53 USD/20' ↔ rehber 40–60 USD) bu okumayı desteklemektedir.

**Çözümün içeriği:**

> **`ardiye_free_time_gun` ulusal bir sabit DEĞİLDİR; TERMİNALE ÖZGÜ bir
> parametredir** ve varış terminali seçilmeden tek bir değere bağlanamaz.

**Bu çözüm ŞUNU İDDİA ETMEZ:** Gerçek varış terminalinde free time'ın 0 gün
olduğunu. **İddia ettiği tek şey**, "0 mı 5 mi" sorusunun **yanlış kurulmuş**
olduğudur.

**Model değeri değişmedi:** Muhafazakâr **0 gün** kullanılmaya devam eder.
**Yön uyarısı:** Yanılıyorsak gecikme maliyeti tahminimiz **yüksektir** — hata
proje **lehine değil, aleyhine** çalışır. Bu, çözümün iyimserlik riski
taşımadığı anlamına gelir.

**Kalan iş:** Varış terminali belirlendiğinde o terminalin kendi tarifesi
okunur → **`T-313`** ve **`OQ-911`** (antrepo/bandrolleme tesisi yeri, dolayısıyla
varış limanı).

---

## C-313 — **OPEN (MEDIUM) — ama TUR 3 için NON-MATERIAL**

```yaml
conflict_id:       C-313
celiski_turu:      TANIM               # "kim kime fatura kesiyor" sorusu
durum:             OPEN
impact:            MEDIUM
materyallik:       NON_MATERIAL_TUR3
cozen:             yatirim-komitesi-baskani
karar_tarihi:      2026-08-10
kapanis_yolu:      T-313 / T-304 (gercek ithalat faturasi veya forwarder kalem listesi)
```

**Neden çözemiyorum:** Bu bir **tier sorusu değildir.** İki kaynak da
gerçektir ve ikisi de kendi tarifesini doğru yayınlar. Soru şudur:
**bu iki kalem AYNI faturaya birlikte girer mi?** Bu bir `TANIM` sorusudur ve
çözüm hiyerarşisinin 1–5. kurallarının **hiçbiri** uygulanamaz. **Kural 6**
devreye girer: gerçek bir fatura veya forwarder kalem listesi gerekir.

**Ajanın davranışı DOĞRULANMIŞTIR** — çift sayım yapılmamış, yalnızca taşıyıcı
THD'si (T3, 165–298 USD) hesaba katılmış, terminal tarifesi ayrı bir bilgi
olarak kaydedilmiştir.

**Ancak bir yön uyarısı kayda geçirilir:** Ajan bu seçimi *"muhafazakâr"* diye
nitelemiştir. **Maliyet açısından muhafazakâr olan üst uçtur** (278–414 USD),
alt uç değil. Yani kalan hata **proje LEHİNE** çalışmaktadır — maliyet en fazla
**115 USD/konteyner** eksik tahmin edilmiş olabilir.

**Neden yine de NON-MATERIAL:** 115 USD/konteyner ≈ **0,008 – 0,010 USD/şişe**.
Aynı modeldeki navlun belirsizliği **±0,15 USD/şişe** mertebesindedir — yani
**~15 kat büyüktür**. Bu çelişki TUR 3'te hiçbir sonucu değiştiremez.

**Model kuralı:** Çift sayım senaryosu (**+113–116 USD/konteyner**) bir
**duyarlılık ekseni** olarak taşınır, base case'e eklenmez.

---

## C-461 — **RESOLVED — KATMAN (sahte çelişki) + BAĞLAYICI ADLANDIRMA KURALI**

```yaml
conflict_id:       C-461
celiski_turu:      KATMAN              # Kural 5 — "en sik yapilan sahte-celiski turu"
durum:             RESOLVED
impact:            HIGH
cozum_evidence_id: EV-2026-08-10-468, EV-2026-08-10-451
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-10
kalan_unknown:     "Harland $2.85+ sayisinin katmani — ORNEK duzeyi UNKNOWN, celiski DEGIL"
```

**Karar: Bu bir çelişki değil, bir KATMAN farkıdır (Kural 5).**

Çözüm hiyerarşisi bu türü açıkça tarif eder: *"iki sayı farklı maliyet
katmanına aitse bu çelişki değil, katman farkıdır. Bu, en sık yapılan
sahte-çelişki türüdür; önce bunu ele."*

Incoterms® 2020 FOB (**L1**, adı belirtilen yükleme limanı bordası) ile şarap
ticaretindeki *"FOB = ex-cellar üretici fiyatı"* kullanımı (fiilen **L0**)
**birbirini çürütmez** — her ikisi de kendi bağlamında doğrudur. Çelişen şey
kaynaklar değil, **terimin kendisidir**.

### BAĞLAYICI ADLANDIRMA KURALI (proje geneli, tüm ajanlar)

> **Kaynağında Incoterm açıkça yazılmayan — EXW için *yer*, FOB için *adı
> belirtilen liman* belirtilmeyen — hiçbir fiyat `L0` veya `L1` diye
> etiketlenemez. Böyle bir fiyatın `price_layer` alanı `UNKNOWN`'dır ve
> modele giremez.**

Bağlayıcı olduğu ajanlar: `global-sourcing-kasifi` (RFQ 3.1 / 3.2),
`gumruk-vergi-uzmani` (gümrük kıymeti matrahı — yanlış katmanla kurulursa
**baştan hatalıdır**), `navlun-lojistik-uzmani` (L1→L2 geçişi),
`finans-fizibilite` (katman disiplini).

`global-sourcing-kasifi`'nin `supplier-shortlist-v2.csv`'de `price_layer`
kolonunu **ayrı tutması ve belirsizse belirsizliği yazması** — bu kuralın
kendiliğinden uygulanmış hâlidir ve **doğrulanmıştır.**

### Bu çözümün AÇIKÇA kapatmadığı şey

**Harland'ın `$2.85+` sayısının hangi katmanda olduğu.** Aynı sayı tam konteyner
siparişinde **FOB**, MOQ siparişinde **ex factory** olarak tanımlanmıştır.
Bu bir **örnek düzeyi `UNKNOWN`**'dır, bir kaynak çelişkisi değil, ve
**tedarikçi bazında** RFQ 3.1/3.2 cevaplarıyla kapanır — **genel olarak
kapanmaz.** `OQ-451` ve **`T-466` (CRITICAL, OPEN)** altında izlenir.

---

## C-462 — **RESOLVED — KAPSAM (sahte çelişki)**, `C-401` ile aynı gerekçe

```yaml
conflict_id:       C-462
celiski_turu:      KAPSAM              # tedarikci sinifi / firma ozelligi farki
durum:             RESOLVED
impact:            HIGH
cozum_evidence_id: EV-2026-08-09-408, EV-2026-08-09-410, EV-2026-08-10-453, EV-2026-08-10-455, EV-2026-08-10-471
elenen_kaynak:     EV-2026-08-09-424   # usetorg.com, T5 — C-401'de zaten elenmisti
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-10
kalan:             "OQ-402 (CRITICAL) — bize uygulanacak GERCEK MOQ. Bu bir UNKNOWN'dir, CONFLICT degil."
```

**Karar iki adımlıdır ve `C-401`'in 2026-08-09 kararıyla BİREBİR AYNIDIR.**

**1 — Kaynak C elenir (Kural 1).** `EV-2026-08-09-424` (usetorg.com agregatörü,
300–1.200 şişe) **T5**'tir ve hangi üreticilere dayandığı belirtilmemiştir.
Bu kaynak **`C-401`'de 2026-08-09'da zaten elenmiştir**; aynı kaynak aynı
gerekçeyle burada da elenir. Yeni bir değerlendirme yapılmamıştır.

**2 — Geriye kalan fark bir çelişki DEĞİLDİR (Kural 4).**
3.000 (Interbrosa, ES) · 3.000 (Clark Estate, NZ) · 3.600 (The Wine Factory, FR)
· 6.000 (Cantina Danese, IT) · 6.000 (Harland, AU) — bunlar **beş ayrı firmanın
kendisi hakkındaki beyanlarıdır**, aynı soruya verilmiş çelişkili cevaplar
değildir. **MOQ bir ülke veya sektör özelliği değil, FİRMA ÖZELLİĞİDİR** —
bu, `global-sourcing-kasifi`'nin kendi TUR 2 bulgusudur ve **aynen kabul
edilmiştir.**

### Ajanın maddi bulgusu KORUNUR ve çelişki etiketi kaldırılırken SİLİNMEZ

> **5.000 şişelik pilot, MOQ'su bilinen beş üreticinin ÜÇÜYLE mümkün,
> İKİSİYLE değildir.** (`EV-2026-08-10-471`)
> Pilot hacmi tedarikçi havuzunu **~%40 daraltır** ve daralan havuz tipik olarak
> daha yüksek birim fiyat demektir.

Ayrıca ajanın kendi aleyhine yaptığı tespit kayda geçirilir: TUR 1'de
doğrulanmış aralık 3.000–3.600 idi ve pilot **uyumlu** görünüyordu; TUR 2'de
aralık 3.000–6.000 oldu ve pilot uyumu **koşullu** hâle geldi. **Daha fazla
veri, daha net değil daha bulanık bir tablo üretti.**

### Bağlayıcı model kuralı (M-4) — `C-401`'den devralınır ve genişletilir

> **MOQ tek bir değere kilitlenemez.** `finans-fizibilite` **üç yapıyı ayrı
> senaryo** olarak çalıştırır: (a) SKU bazlı 3.000–3.600, (b) SKU bazlı 6.000,
> (c) konteyner bazlı (Viña María: 1 × 20ft karışık). **Ortalama alınamaz** —
> 3.000 ile 6.000'in ortalaması (4.500) **hiçbir üreticinin gerçek MOQ'su
> değildir.**

### Neden bu, riski kayıttan silmek DEĞİLDİR

Silinen şey **risk değil, YANLIŞ ETİKETTİR.** Risk aynen durmaktadır — ama
artık `CONFLICT` olarak değil, **`OQ-402` (CRITICAL `UNKNOWN`)** ve **M-4
bağlayıcı model kuralı** olarak. Bir çelişki etiketi, bir belirsizliği
**saklamak için** kullanılmamalıdır.

---

## C-561 — **RESOLVED — TANIM**; `C-501` **AÇIK KALIR**

```yaml
conflict_id:       C-561
celiski_turu:      TANIM
durum:             RESOLVED
impact:            MEDIUM
cozum_evidence_id: EV-2026-08-10-552
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-10
model_girdisi_etkisi: YOK
bagli_kayit:       "C-501 -> OPEN (DEGISMEDI). C-561 onu NITELER, YERINE GECMEZ."
```

**Karar: Kaynak B'nin ÖLÇÜMÜ kabul edilir, Kaynak A'nın SONUCU korunur.**

**Kural 2 (tarih) ve Kural 4 (kapsam) aynı yönü işaret ediyor** — ikisi de
Kaynak B lehine: B daha yenidir (2026-08-10) ve daha dar, **fiilen sayılmış**
bir iddiadır.

**Kabul edilen ölçüm (`EV-2026-08-10-552`, FACT — katalog hakkında):**
stok dışı ithal listeleme havuzu **iki modludur**: 44 kayıt `<500 TL`
(2026 için gerçeklik dışı) · **62 kayıt 500–1.000 TL** · 243 kayıt `>1.000 TL`.
`C-501`'in *"bakımsız eski fiyat"* gerekçesi **yalnızca düşük kuyruk için
(44/349 = %12,6)** gösterilmiştir; **havuzun tamamı için gösterilmemiştir.**

**Korunan sonuç:** **Stokta olmayan bir fiyat, satın alınabilir bir fiyat
değildir ve `L8` olarak modele giremez.** Kaynak B, Kaynak A'nın bu sonucunu
**çürütmez** — nitekim ajanın kendisi de bunu yazmıştır.

### Çözümün ayırdığı iki soru

| Soru | Cevap |
|---|---|
| **Model girdisi:** 400–800 TL bandında modele girebilecek bir `L8` gözlemi var mı? | **HAYIR.** Her iki okumada da aynı. **`model_girdisi_etkisi: YOK`** |
| **Talep okuması:** "bu bantta ithal şarap **yok**" mu, "**var ama dönmüyor**" mu? | **`UNKNOWN` KALIR.** Bu bir G3 sorusudur ve ikinci okuma **daha kötüdür** (assortmanda dolu, stokta boş) |

**`pazar.yaml`'a DOKUNULMAMIŞTIR.** `segment.ithal_sku_400_800_uzman_kanal = 0`
değeri geçerlidir ve **"stokta 0"** olarak okunur. Ajanın 62 satırı
`raf-fiyat-gozlemleri.csv`'ye `gozlem_yontemi = ONLINE_LISTING_STOKTA_YOK` ve
`status = UNKNOWN` ile eklemesi **doğrulanmıştır.**

**`C-501` `OPEN` KALIR.** Sorusu farklıdır: *o düşük fiyatlar gerçek mi?*
Yalnızca fiziksel gözlemle kapanır (`OQ-502`, **`T-917`**).

---

## C-601 — **OPEN (HIGH) — İKİ KAYNAK YENİDEN KAPSAMLANDI, ÇEKİRDEK AÇIK**

```yaml
conflict_id:       C-601
durum:             OPEN                # CEKIRDEK COZULMEDI
impact:            HIGH                # bkz. IMPACT OKUMA KURALI (asagida)
kismi_karar:       KAYNAK_B_ELENDI + KAYNAK_C_YENIDEN_KAPSAMLANDI
cozen:             yatirim-komitesi-baskani
karar_tarihi:      2026-08-10
kapanis_yolu:      T-601 (CRITICAL, mevzuat-ruhsat-uzmani) + T-604
model_degeri:      "null — dort senaryo 45/60/90/120 gun (DEGISMEDI)"
```

### Kaynak A — 6585 m.7/3, vade ≤60 gün → **GEÇERLİ**

Yasal tavanın **metni** tartışmalı değildir (T3, içerik T1, yürürlük
**2024-01-01**, yaptırımı da tanımlı: günlük binde 5, sonra günlük %1).

### Kaynak B — RK, organize kanal 70 gün → **ELENDİ** (Kural 2 + Kural 4)

| Test | Sonuç |
|---|---|
| **Kural 2 (tarih)** | Veri **2020**'dir — tavanın yürürlüğe girdiği **01.01.2024'ten ÖNCE**. Yürürlükte olmayan bir kuralın ihlalini ölçemez |
| **Kural 4 (kapsam)** | **Süt ürünleri**dir, şarap değildir |

**Kaynak B, Kaynak A'yı ÇÜRÜTMEZ — A'nın NİÇİN ÇIKARILDIĞINI açıklar.**
Ajanın kendisi de bunu tespit etmiştir. Bu kaynak, "kanun var ama uygulanmıyor"
argümanının **dayanağı olamaz.**

### Kaynak C — Migros DPO ~93 gün → **ELENMEDİ ama YENİDEN KAPSAMLANDI** (Kural 4)

Kaynak C **2025 verisidir**, yani **tavan yürürlükteyken** alınmıştır — bu
nedenle B gibi elenemez. **Ancak kapsamı uyuşmuyor:** rakam *"tüm kategoriler,
tüm coğrafya"* konsolide bir DPO'dur ve finansallarda **gıda / gıda dışı** ile
**yurt içi / yurt dışı** ayrıştırması **YOKTUR** (ajanın kendi tespiti).

**Karar:** Kaynak C bir **şarap ödeme vadesi ölçümü olarak okunamaz.**
**`STRESS` senaryo çapası** olarak kalır (120 gün), **base case değildir.**

### Çekirdek soru — çözemiyorum

> **Şişelenmiş şarap, 6585 m.7/3 anlamında "tarım ve gıda ürünü" müdür?**

Bu bir **hukuki nitelemedir.** `kanal-marj-uzmani` bunun kendi alanı olmadığını
**açıkça yazmış** ve `ASSUMPTION` olarak işaretleyip **`T-601` ile devretmiştir**
— doğru davranıştır. Benim kendi yorumumla kapatmam **CLAUDE.md §1.16
ihlali** olurdu.

**Kapanış yolu:** **`T-601` (CRITICAL, OPEN, `mevzuat-ruhsat-uzmani`)**.
Bu ajan TUR 2'de çalışmamıştır.

**Etki büyüklüğü:** Cevap *"hayır, şarap kapsam dışı"* ise 60 günlük tavan düşer,
vade base case'i **60 → 90 güne** kayar ve `peak_cash_requirement` alacak
tarafında **~%50 artar**. Bu, *"kârlı ama finanse edilemez"* tuzağının ta
kendisidir ve `C-601` bunu **açık** bırakmaktadır.

**Model kuralı değişmedi:** `kanal.yaml → zincir_market.odeme_vadesi_gun` =
**`null`**; dört senaryo **45 / 60 / 90 / 120** gün **ayrı ayrı** çalıştırılır.

---

## C-602 — **RESOLVED — SAHTE ÇELİŞKİ** (çözüm veri ÜRETMEZ)

```yaml
conflict_id:       C-602
celiski_turu:      "kaynak kalitesi — celiski kaynaklar arasinda DEGIL, kaynaklarin KENDI ICINDE"
durum:             RESOLVED
impact:            HIGH                # bkz. IMPACT OKUMA KURALI (asagida)
cozum_evidence_id: EV-2026-08-10-620, EV-2026-08-10-618   # ikisi de NEGATIF kayit
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-10
sonuc:             "CONFLICT -> UNKNOWN. Hicbir sayi uretilmedi."
```

**Karar: Tüm kaynaklar elenir (Kural 1 + CLAUDE.md §2). Geriye çelişecek bir şey
kalmaz.**

| Alan | Elenen iddialar | Neden |
|---|---|---|
| **Tekel bayii marjı** | %6 · %8 · %10–15 · %17 · %18–30 | **Hepsi T5**; hiçbiri margin/markup ayrımını, KDV tabanını veya katman çiftini belirtmiyor → **`M1` gereği tanımsız** |
| **HoReCa çarpanı** | 2× (L8 üzerine) · 2,5× (L7 üzerine) · 4–5× (L8 üzerine) | **Tek T5 yazı**, **2012** tarihli, ve **kendi içinde üç farklı katman** veriyor |

**CLAUDE.md §2:** T5 tek başına sonuç üretemez. Tanımsız bir sayı, tanımsız
başka bir sayıyla **çelişemez** — ikisi de sayı değildir.

### ⚠ BU BİR VERİ KAZANIMI DEĞİLDİR

> Bir **`CONFLICT` kaydı**, bir **`UNKNOWN` kaydına** dönüştürülmüştür.
> **Hiçbir sayı üretilmemiştir.**

`kanal.yaml → tekel_bayi.marj_pct` ve `horeca.fiyat_carpani` **`UNKNOWN`**
kalır. Duyarlılık bantları (tekel 12/18/25 · HoReCa 2,0/3,0/5,0×)
**`ASSUMPTION` / `SENSITIVITY_ONLY`** olarak ve **"bandın hiçbir noktasının
kanıtı yoktur"** açıkça yazılarak durur.

`kanal-marj-uzmani`'nın davranışı **doğrulanmıştır**: hiçbir T5 sayısını
`value` alanına yazmamış, `EV-2026-08-10-618`'e `ttl: 0d` vermiş ve kaynağa en
az güvendiğini **kendisi itiraf etmiştir.**

**Bu çözümün ortaya çıkardığı asıl bulgu, ajanın kendi tespitidir ve korunur:**
*"Bu alanda konuşulan 'marj' rakamları **tanımsız konuşulmaktadır**"* — `M1`
kuralının varlık sebebi budur.

**Gerçek kapanış yolu:** Gerçek bayi/HoReCa görüşmesi veya gerçek bir fiyat
listesi (`T-604`). **Masabaşı ile kapanmaz.**

---

## C-161 — **RESOLVED — NON_MATERIAL (KAPSAM DIŞI)**

```yaml
conflict_id:       C-161
celiski_turu:      KAPSAM
durum:             RESOLVED
impact:            LOW
model_girdisi_etkisi: YOK
cozum_evidence_id: EV-2026-08-10-151, EV-2026-08-10-153, EV-2026-08-10-154
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-10
yeniden_acilma:    "Kapsam 22.05 (vermut/aromatize) veya GTS sutunu bulunan baska bir II sayili Liste urunune genislerse OTOMATIK olarak yeniden acilir."
```

**Karar: Soru bu projenin kapsamında DOĞMUYOR (Kural 4).**

`gumruk-vergi-uzmani`, GTS'nin 2204.21'de **hiçbir koşulda** uygulanamayacağını
**üç bağımsız pozitif yapısal gözlemle** göstermiştir:
(1) I sayılı Liste 21–22. Fasıllar tablosunda **GTS sütunu yoktur**,
(2) **2204, GTS sütunu bulunan II sayılı Liste'de yer almaz**,
(3) EK-1 GTS ülkeleri listesinde kapsamdaki **9 ülkenin hiçbiri yoktur**.

Bu, *"gözetim tebliği bulunamadı"* tipi **zayıf bir negatif arama değildir** —
üç gözlem de **pozitiftir**: sütun yok, satır yok, ülke yok.

Dolayısıyla "GTS'de Form A mı REX mi aranır" sorusunun
`mense_tarife_eslemesi` üzerinde **etkisi yoktur**. Tier kuralı (A lehine,
T2 > T3) ile tarih kuralının (B lehine, yürürlük 1/1/2026) zıt yönü işaret
etmesi **maddi bir sorun değildir**, çünkü soru bizim GTİP'imizde **sorulmaz**.

**Ajanın kendi yorumuyla kapatmama kararı DOĞRULANMIŞTIR.**

### Kayda geçirilen ikincil yapısal zayıflık (bu çelişkiden bağımsız)

`gumruk-vergi-uzmani`'nın tespiti: **Ticaret Bakanlığı Gümrük Rehberi'nin
hiçbir sayfasında yayın veya güncelleme tarihi yayımlanmamaktadır.** Bu, o T2
kaynağın **tazeliğinin ölçülemez** olduğu anlamına gelir ve TUR 1'de
`EV-2026-08-09-126` için not edilen sorunun (revizyon 2018, KDV %18 yazıyordu)
**aynısıdır**. Ajan tüm ilgili kartlara `ttl: 180d` ve `effective_date: -`
yazmıştır — **doğru davranıştır** ve bu yapısal zayıflık `G1` altında
izlemede kalır.

---

## KAYIT DÜZELTMELERİ

### 1) `C-401` / `C-402` / `C-403` — statü kaydı düzeltmesi

`50-sourcing/rapor-tur2-global-sourcing.md` §4, bu üç çelişkiyi **"AÇIK"**
olarak raporlamaktadır. **Bu kayıt yanlıştır.**

| id | Ajanın TUR 2 ifadesi | **Kayıttaki gerçek durum** | Karar tarihi |
|---|---|---|---|
| `C-401` | "AÇIK" | **`RESOLVED`** (T5 elendi + kapsam farkı) | 2026-08-09 |
| `C-402` | "AÇIK" | **`RESOLVED`** (sahte çelişki: L8 ↔ L2, farklı katman **ve** farklı popülasyon) | 2026-08-09 |
| `C-403` | "AÇIK" | **`UNRESOLVABLE`** (iki T5; LOW; modele girmez) | 2026-08-09 |

**Bu bir değerlendirme değişikliği değil, bir tutarsızlık düzeltmesidir.**
Ajanın **bulgusuna dokunulmamıştır**; yalnızca statü kaydı düzeltilmiştir.
→ **`T-918`**.

### 2) `impact` alanı okuma kuralı (BAĞLAYICI)

`C-601` ve `C-602`'nin `yaml` bloklarında severity, `impact:` alanına değil
**`etki:` alanına** yazılmıştır. Bu dosyanın kayıt formatına göre
**`etki:` = "bu çelişki çözülmezse model nerede kırılır"**,
**`impact:` = `CRITICAL | HIGH | MEDIUM | LOW`**.

> **Kural:** Ajan **`impact:` alanını doğru kullanmışsa o değer esastır**
> (`C-551` → **HIGH**). **Yalnızca `etki:` yazılmışsa** blok bir `impact`
> beyan etmiş sayılmaz ve **özet tablosundaki değer esastır**
> (`C-601` → **HIGH**, `C-602` → **HIGH**).

**Başkan hiçbir çelişkinin `impact` değerini yükseltmemiş veya
düşürmemiştir.** Bu, `C-551`'in 2026-08-10'daki düzeltmesiyle **aynı sınıf**
bir kayıt işlemidir.

---

## TUR 2 SONUNDA AÇIK KALAN ÇELİŞKİLER — TAM LİSTE

| id | impact | Neden çözülemedi | Kim/ne kapatır |
|---|---|---|---|
| **C-311** | **CRITICAL** | T5 bacağı elendi ama kalan T4 kaynak tarihsiz ve "from" fiyatı — bandı **daraltamaz**. Masabaşında çözülemez | **`T-304`** — 3 forwarder'dan kalem kırılımlı yazılı FCL kotasyonu |
| **C-601** | HIGH | Çekirdek bir **hukuki nitelemedir**; başkan kendi yorumuyla kapatamaz (§1.16) | **`T-601`** (CRITICAL) + `T-604` |
| **C-313** | MEDIUM | `TANIM` sorusu; kuralların hiçbiri uygulanamaz. **TUR 3 için NON-MATERIAL** (~0,01 USD/şişe) | `T-313` / `T-304` — gerçek fatura veya forwarder kalem listesi |
| **C-202** | HIGH | *(TUR 1'den devir — TUR 2'de ele alınmadı, durumu değişmedi)* | `T-202` |
| **C-204** | LOW | *(TUR 1'den devir — değişmedi)* | TUR 5 → `mevzuat-ruhsat-uzmani` |
| **C-251** | LOW | *(TUR 1.5'ten devir — değişmedi; model girdisi etkisi YOK)* | TADAB yazılı görüşü |
| **C-252** | LOW | *(TUR 1.5'ten devir — değişmedi; G0 izleme listesinde R1)* | TADAB yazılı görüşü / hukuk mütalaası |
| **C-301** | MEDIUM | *(TUR 1'den devir — TUR 2'de yeni kanıt bulunamadı. **Başkan direktifi aynen geçerli: 9–11 / 20–24 palet bandı korunur, tek değer seçmek YASAKTIR**)* | `T-304` — forwarder stowage planı |
| **C-303** | LOW | *(TUR 1'den devir — düşük etkili)* | — |
| **C-501** | HIGH | *(TUR 1'den devir — `C-561` ile **nitelendi**, çözülmedi)* | `OQ-502` / **`T-917`** — fiziksel mağaza gözlemi |
| **C-502** | MEDIUM (izleme) | *(TUR 1'den devir — değişmedi)* | `T-501` |
| **C-551** | HIGH | *(TUR 1.5'ten devir — `NON_BLOCKING_TUR2`, **G3'ü bloke etmeye devam eder**)* | **`T-504`** / **`T-917`** — şarap reyonundaki fiziksel etiket fotoğrafı |

**Tek bir fiziksel eylem — bir mağaza turu — `C-501`, `C-551`, `T-504`, `T-603`
ve `OQ-001`'in kalan iki ayağını AYNI ANDA kapatır** (**`T-917`**).
**Projedeki en yüksek bilgi/maliyet oranına sahip eylem olmaya devam
etmektedir** ve iki turdur yapılmamıştır.

---
---

# TUR 2.5 ÇELİŞKİ KAYITLARI VE BAŞKAN ÇÖZÜMLERİ (2026-08-10)

```yaml
tur:        TUR 2.5 — REVERSE TARGET MODEL
acan:       finans-fizibilite  (99-ops/_parts/celiskiler-finans-fizibilite-tur25.md)
cozen:      yatirim-komitesi-baskani
tarih:      2026-08-10
belge:      90-karar/tur-25-konsolidasyon.md §4
not:        "Ajanin PARCA kaydindaki hicbir metin silinmemis veya
             degistirilmemistir. Asagidakiler BASKAN COZUM KAYITLARIDIR."
```

## ÖZET TABLO — TUR 2.5 ÇELİŞKİLERİ

| id | Konu | impact | **Durum** | Uygulanan kural |
|---|---|---|---|---|
| **C-851** | `L3` katman tanımı — `CLAUDE.md` §6 ↔ ters model spesifikasyonu (çift sayım riski) | HIGH | **RESOLVED — TANIM** | Kural 5 (katman/tanım — sahte çelişki) |
| **C-852** | *"`fx` olmadan `CIF_TRY`'ye kadar çalışır"* ↔ USD cinsli varış masrafları | HIGH | **RESOLVED — TANIM (NİTELEME)** | Kural 5 + başkanın kendi hükmünün düzeltilmesi |

---

## C-851 — **RESOLVED — TANIM (SAHTE ÇELİŞKİ)**

```yaml
conflict_id:       C-851
celiski_turu:      TANIM / KATMAN
durum:             RESOLVED
impact:            HIGH
model_girdisi_etkisi: YOK    # model zaten dogru davraniyordu
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-10
takip_ticket:      T-945
yeniden_acilma:    "l3_pre_tax_landed_max'i bir CIKARMA isleminde kullanan bir
                    model ciktisi gorulurse OTOMATIK olarak yeniden acilir."
```

### Çelişki

| | **Kaynak A** | **Kaynak B** |
|---|---|---|
| Belge | `CLAUDE.md` §6 (proje anayasası) | `30-vergi-gumruk/ters-model-vergi-bacagi.md` §4.3 + `R6` |
| Der ki | `L3 PRE-TAX LANDED = CIF + vergi öncesi yurt içi masraflar` | Ordino · antrepo · elleçleme · iç nakliye · müşavirlik: hepsi **`L5` kalemidir** |

**Risk:** aynı kalemler iki farklı katmana yerleştiriliyor → iki tanım aynı
anda uygulanırsa **iki kez düşülür**, hiçbiri uygulanmazsa **hiç düşülmez.**
Büyüklük: 5.000 şişede ±5,32 TL/şişe (799 TL hedefte %1,95).

### Karar: **Bu bir DEĞER çelişkisi değil, bir TANIM çelişkisidir (Kural 5).**

1. **`CLAUDE.md` §6 bir MALİYET KATMANI TAKSONOMİSİDİR, bir ÇIKARMA SIRASI DEĞİLDİR.** §6'nın başlığı *"MALİYET KATMANLARI (KARIŞTIRILAMAZ)"*tır ve tek talebi *"Bir katmandan diğerine geçiş açıkça gösterilir (hangi kalem eklendi/çıktı)"*dır. **Bir kalemin hangi ADIMDA düşüleceğini §6 belirlemez.**
2. **Ters model spesifikasyonu §6'yı ihlal etmiyor, UYGULUYOR.** `L3` katmanı ortadan kalkmıyor; `L3 = CIF + o kalemler` özdeşliği **korunuyor** ve `reverse-price-model.md` `L3`'ü **bilgi amaçlı türev alan** olarak raporluyor.
3. **Fiilî davranış zaten doğrudur:** kalemler `R6`'da **tam bir kez** düşülmüştür. Çift sayım **olmamıştır**, hiç saymama da **olmamıştır**.

### BAĞLAYICI OKUMA KURALI — `L3-K`

> `L3 PRE-TAX LANDED`, ters modelde **bilgi amaçlı bir türev katmandır.**
> `L2 → L3` artışını oluşturan kalemler, `L4 → L5` geçişinde **ikinci kez
> düşülemez.** Her kalem zincirde **tam bir kez** düşülür ve hangi adımda
> düşüldüğü `ters_model_vergi_bacagi.adimlar`'da yazılıdır.
> `l3_pre_tax_landed_max` **hiçbir çıkarma işleminde kullanılamaz.**

**`CLAUDE.md` DEĞİŞTİRİLMEMİŞTİR.** Bu kural §6'ya bir **niteleme** ekler,
onunla çelişmez. Kuralın `30-vergi-gumruk/matrah-sirasi.md`'ye ve
`vergi.yaml`'a yazılması `CLAUDE.md` §1.8 gereğidir → **`T-945` (MEDIUM)**.

### Ajanın davranışı — **DOĞRULANDI**

`finans-fizibilite` **sessiz seçim yapmamıştır:** iki tanımı da göstermiş,
hangisini esas aldığını yazmış, `L3`'ü ayrı ve kullanılmayan bir alan olarak
tutmuş ve çelişkiyi başkana taşımıştır. **Bu, `CLAUDE.md` §1.13'ün tam
uygulamasıdır.**

### Kayda geçirilen ikincil gözlem

Ajanın kendi uyarısı **yerindedir ve korunur:** *"katman sınırlarındaki
belirsizlikler küçük görünüp büyük çıkabilir; bu turda kanal bacağında benzer
yapıda bir eksik sayım bulundu ve büyüklüğü **28,95 TL/şişe** çıktı."*
`C-851` bu nedenle mertebesi küçük olduğu hâlde `HIGH` işaretlenmiştir ve
**işaretleme korunmaktadır.**

---

## C-852 — **RESOLVED — TANIM (NİTELEME)**

```yaml
conflict_id:       C-852
celiski_turu:      TANIM / KAPSAM
durum:             RESOLVED
impact:            HIGH
model_girdisi_etkisi: CIKTININ STATUSU  # sayi -> UST SINIR
cozen:             yatirim-komitesi-baskani
cozum_tarihi:      2026-08-10
kalan_is:          "Bir celiski degil, bir VERI eksikligi: T-852 (fx)"
yeniden_acilma:    "fx doldurulup USD/EUR kalemleri dusuldukten SONRA hala
                    'ust sinir' etiketi tasiniyorsa yeniden acilir."
```

### Çelişki

| | **Kaynak A** | **Kaynak B** |
|---|---|---|
| Belge | `90-karar/master-commercial-input-table.md` §5.3 (**başkan belgesi**) | TUR 2.5 ters model çalıştırması + `40-lojistik/lojistik-senaryolari-tur25.md` §2.4 |
| Der ki | *"`fx` olmadan bile ters model **`CIF_TRY`'ye kadar** çalışır"* | `L2` ile `L5` arasında **USD cinsli kalemler** vardır ve `fx` `null` iken düşülemezler: varış THD, devanning, CFS, terminal ardiye, drop-off, LCL varış sabit masrafı, dokümantasyon, **müşavirlik CIF kademesi** |

### Karar: **`finans-fizibilite` HAKLIDIR. Bu, bir ajanın bulgusunun reddi değil, BAŞKANIN KENDİ HÜKMÜNÜN DÜZELTİLMESİDİR.**

1. §5.3'ün türetmesi **eksiktir**: `L5 → L4` geçişindeki kalemlerin **hepsinin TL cinsinden olduğunu** varsayar. Gerçekte varış tarafı masraflarının büyük kısmı **USD** cinsindendir (`EV-2026-08-10-315`…`-319`, `EV-2026-08-09-324`).
2. Düşülemeyen kalemlerin **hepsi pozitiftir** → `0` alınmaları tavanı **yükseltir**.
3. Dolayısıyla `fx` olmadan hesaplanan şey `CIF_TRY` **değil**, onun bir **ÜST SINIRIDIR.**

### DÜZELTİLMİŞ HÜKÜM (bağlayıcı)

> ~~*"`fx` olmadan ters model `CIF_TRY`'ye kadar çalışır."*~~
>
> **→ *"`fx` olmadan ters model `CIF_TRY`'nin bir ÜST SINIRINA
> (`cif_try_max_UPPER_BOUND`) kadar çalışır. `L2` ile `L5` arasındaki döviz
> cinsli kalemler düşülemediği için gerçek tavan bundan DÜŞÜKTÜR."***

**Eski metin silinmemiştir**; `master-commercial-input-table.md` §5.3'e
niteleme kutusu eklenmiştir.

### Ajanın çıktı adlandırması — **ONAYLANIR**

`cif_try_max_UPPER_BOUND` (`cif_try_max` **değil**). Ajan ayrıca:
(1) USD/EUR kalemlerini **ayrı satırlar** olarak taşımış,
(2) her birini `0` alıp **her çalıştırmada uyarı basmış**,
(3) **iki bağımsız üst-sınır nedenini** (λ=1 **ve** sıfır alınan kalemler)
ayrı ayrı listelemiştir. **Sessiz seçim YAPILMAMIŞTIR.**

### Kalan iş bir çelişki değildir

**`T-852` (`fx`, CRITICAL) kapandığı anda** USD kalemleri düşülebilir ve
`cif_try_max_UPPER_BOUND` gerçek bir `cif_try_max`'a döner. Bu bir **veri
eksikliğidir**, bir çelişki değil.

---

## TUR 2.5'TE DEĞİNİLEN AMA DEĞİŞMEYEN MEVCUT ÇELİŞKİLER

| id | Sahibi | TUR 2.5'teki durum |
|---|---|---|
| **`C-311`** (FCL bandı 4–5 kat) | navlun-lojistik | **`OPEN` — ama KAPSAMI DARALDI:** ters model üzerindeki etkisi **SIFIRDIR** (navlun CIF'in içindedir; `reverse-price-model.md` §8.3). **İleri model ve FOB pazarlığı için blokerliği aynen sürüyor** (`T-304`). **Band DARALMADI.** |
| `C-501` (`available` filtresi) | türkiye-pazar | `OPEN` — sweet-spot §2 alıntısının tabanı; **modelin sayılarını değiştirmez** |
| `C-551` (Metro KDV sunumu) | türkiye-pazar | `OPEN` — `OBSERVED_BENCHMARK` bu turda **hiç kullanılmadı** → **etkisiz** |
| `C-561` (bantta ürün var, dönmüyor) | türkiye-pazar | *(TUR 2'de `RESOLVED — TANIM`)* — `T-857`'nin ikinci bacağı olarak izlemede |
| `C-601` (yasal vade 60 ↔ gözlenen ~93 gün) | kanal-marj | `OPEN` — `peak_cash` hesaplanmadığı için bu turda **etkisiz**; **TUR 3B'de belirleyici** (`D-13`, `T-601`) |
| `C-602` (tekel marjı) | kanal-marj | *(TUR 2'de `RESOLVED — SAHTE ÇELİŞKİ`)* — **ama boşluk duruyor:** `m_tekel` bandının hiçbir noktasının kanıtı yok; `T-856`'nın tabanı |
| `C-202` · `C-203` · `C-252` | mevzuat-ruhsat | `OPEN` — **`G0 PASS` bu ikisinin (`C-252`, `C-203`) üzerinde duruyor** ve **dört turdur test edilmedi** |
| `C-301` · `C-313` · `C-204` · `C-251` · `C-502` | çeşitli | `OPEN` — değişmedi |

## TUR 2.5'TE TESPİT EDİLEN DESEN (çelişki değil, ama buraya kayda geçer)

> **Üç bağımsız olayın ortak yapısı:** her katman sınırında, kalemin bir
> **NİTELİĞİ** (ödeyeni / katmanı / para birimi) belirsiz bırakıldığında,
> model o kalemi **SESSİZCE ATLAR** ve tavan **YUKARI** sapar.

| Olay | Katman geçişi | Belirsiz nitelik | Yön | Büyüklük |
|---|---|---|---|---|
| **`R5` hatası** *(çelişki değil, model hatası)* | `L6 ↔ L7_eff ↔ L5` | kalemin **ödeyeni** (`d`, `f`) | ↑ | **−28,95 TL/şişe** |
| **`C-851`** | `L2 ↔ L3 ↔ L5` | kalemin **katmanı** | belirsiz | ±5,32 TL/şişe |
| **`C-852`** | `L2 ↔ L5` | kalemin **para birimi** | ↑ | `UNKNOWN` |
| *(13 maliyet kaleminin `0` alınması)* | çeşitli | tutarın **`UNKNOWN`** olması | ↑ (13/13) | `UNKNOWN` |

**Dördünün de yönü aynıdır: PROJENİN LEHİNE.**
`seytanin-avukati` TUR 4'te bu desenden başlamalıdır → **`T-946`**.

---

# TUR 2.5 ÇELİŞKİ FRAGMENT'LERİ

> Ajanların `99-ops/_parts/*-tur25.md` fragment'lerinden değiştirilmeden aktarıldı.

## finans-fizibilite (TUR 2.5)

```yaml
ajan:   finans-fizibilite
tur:    TUR 2.5 — REVERSE TARGET MODEL
tarih:  2026-08-10
not:    "99-ops/celiskiler.md DOKUNMA listesindedir ve DEGISTIRILMEMISTIR.
         Bu dosya, baskanin merge edecegi PARCA kayittir."
```

---

### C-851 — `L3` KATMAN TANIMI: AYNI KALEM İKİ FARKLI KATMANDA

```yaml
conflict_id: C-851
acan:        finans-fizibilite
tarih:       2026-08-10
durum:       OPEN
impact:      HIGH        # cift sayim riski dogrudan MAX_CIF'i degistirir
```

| | **Kaynak A** | **Kaynak B** |
|---|---|---|
| Belge | **`CLAUDE.md` §6** (proje anayasası) | **`30-vergi-gumruk/ters-model-vergi-bacagi.md`** §4.3 + R6 + `vergi.yaml → ters_model_vergi_bacagi` |
| Tier | — (iç kural) | — (ajan spesifikasyonu, T1 kanıtlara dayalı) |
| Tarih | TUR 0 | 2026-08-10 |
| Der ki | **L3 PRE-TAX LANDED = CIF + vergi öncesi yurt içi masraflar** | Ordino · antrepo · elleçleme · iç nakliye · **müşavirlik**: hepsi **`L5` kalemidir**, vergi matrahına girmez; `L4_econ_max = L5_max − Σ(L5_kalemleri)` |

#### Neden çelişiyor

**Aynı maliyet kalemleri iki farklı katmana yerleştiriliyor.**

- `CLAUDE.md` §6'ya göre bu kalemler **L2 ile L3 arasındadır.**
- Ters model spesifikasyonuna göre **L4 ile L5 arasındadır.**

Zincir tek yönlüdür (`L2 → L3 → L4 → L5`), dolayısıyla **iki tanım aynı anda
uygulanırsa kalem İKİ KEZ düşülür; hiçbiri uygulanmazsa HİÇ düşülmez.**

#### Büyüklük

5.000 şişede TR-içi kalemler **3,99 TL/şişe** (LCL BASE) →
`MAX_CIF` üzerindeki etkisi **2,66 TL/şişe**. Çift sayım hâlinde
`MAX_CIF` **5,32 TL** eksik çıkar (799 TL hedefinde **%1,95**).
**Mertebe küçüktür ama yön belirsizdir ve kural düzeyinde bir boşluktur.**

> **Uyarı — mertebe yanıltıcı olabilir:** bu turda **kanal bacağında** benzer
> yapıda bir eksik sayım bulundu ve büyüklüğü **28,95 TL/şişe** çıktı
> (`reverse-price-model.md` §2.2). Katman sınırlarındaki belirsizlikler
> **küçük görünüp büyük çıkabilir**; `C-851` bu nedenle `HIGH` işaretlenmiştir.

#### Bu turda ne yapıldı

**Sessiz seçim YAPILMADI.** Model, ters model spesifikasyonunu **esas aldı**
(kalemler `L5`'te bir kez düşüldü) ve `L3`'ü **yalnızca bilgi amaçlı** bir
türev alan olarak raporladı:

```python
l3_pre_tax_landed_max = cif_try_max + (TR_ ile baslayan TRY kalemlerin toplami)
# BU DEGER HICBIR CIKARMA ISLEMINDE KULLANILMAZ.
```

`reverse-price-model.md` §2.2'de **açıkça yazılmıştır.**

#### Çözüm için gereken

Başkan kararı: `CLAUDE.md` §6'daki `L3` tanımına bir **niteleme** eklenmesi —
*"L3, vergi matrahına girmeyen yurt içi masrafları içerdiğinde bu kalemler
`L4 → L5` geçişinde İKİNCİ KEZ düşülemez"* — veya ters model
spesifikasyonunun `L3`'ü açıkça **atlayan** bir zincir tanımladığının kayda
geçirilmesi.

---

### C-852 — *"fx OLMADAN CIF_TRY'YE KADAR ÇALIŞIR"* HÜKMÜ FAZLA KESİN

```yaml
conflict_id: C-852
acan:        finans-fizibilite
tarih:       2026-08-10
durum:       OPEN
impact:      HIGH        # ciktinin STATUSUNU degistirir: sayi -> ust sinir
```

| | **Kaynak A** | **Kaynak B** |
|---|---|---|
| Belge | **`90-karar/master-commercial-input-table.md`** §5.3 (+ §7 "en kırılgan hüküm") | **Bu ters model çalıştırması** (TUR 2.5) + `40-lojistik/lojistik-senaryolari-tur25.md` §2.4 |
| Der ki | *"`fx` olmadan bile ters model **`CIF_TRY`'ye kadar** çalışır."* Gerekçe: L8 → KDV → L7 → L6 → L5 → L4 → ÖTV ve bandrol düşülür, geriye `CIF + GV` kalır | **L2 ile L5 arasında USD cinsli kalemler vardır** ve `fx` `null` iken düşülemezler: varış THD (165–298 USD/kont.), devanning (257–475 USD), CFS (30–80 USD/CBM), terminal ardiye (90–300 USD), drop-off (50 USD), LCL varış sabit masrafı (200–500 USD), dokümantasyon (50–100 USD), **müşavirlik CIF kademesi (%0,3)** |

#### Neden çelişiyor

§5.3'ün türetmesi **eksiktir**: L5'ten L4'e geçerken düşülmesi gereken
kalemlerin **hepsinin TL cinsinden olduğunu** varsayar. Gerçekte
**varış tarafı masraflarının büyük kısmı USD cinsindendir**
(`EV-2026-08-10-315`…`-319`, `EV-2026-08-09-324`).

**Sonuç:** `fx` olmadan hesaplanabilen şey `CIF_TRY` **değil**,
`CIF_TRY`'nin bir **ÜST SINIRIDIR** — çünkü düşülemeyen tüm kalemler
**pozitiftir** ve sıfır alınmaları tavanı **yükseltir**.

#### Büyüklük — `UNKNOWN`, ama alt sınırı verilebilir

5.000 şişelik İspanya LCL BASE senaryosunda USD bacağı **0,450 USD/şişe**
(`lojistik-senaryolari-tur25.md` §4.1) — bunun **bir kısmı** CIF içindedir
(okyanus navlunu), **bir kısmı** varış tarafındadır (CFS, varış sabit
masrafı, dokümantasyon). **Ayrıştırma bu belgede yapılmamıştır** ve
`fx` olmadan **TL karşılığı hesaplanamaz.**

> **Yani çelişkinin büyüklüğü de `fx`'e bağlıdır.** Bu, `T-852`'nin
> (CRITICAL) neden yalnızca bir "birim dönüşümü" olmadığını gösterir.

#### Bu turda ne yapıldı

**Sessiz seçim YAPILMADI.** Model:
1. USD/EUR cinsli `L5` kalemlerini **ayrı satırlar** olarak taşıdı,
2. her birini **`0` aldı** ve bunu **her çalıştırmada uyarı olarak bastı**,
3. çıktı alanını **`cif_try_max_UPPER_BOUND`** olarak adlandırdı,
4. `reverse-price-model.md` §3.4'te **iki bağımsız üst-sınır nedenini**
   (λ=1 **ve** sıfır alınan kalemler) ayrı ayrı listeledi.

#### Çözüm için gereken

`T-852` (fx) kapanması **yeterlidir** — kur geldiği anda USD kalemleri
düşülebilir ve `cif_try_max_UPPER_BOUND` gerçek bir `cif_try_max`'a döner.
`master-commercial-input-table.md` §5.3'ün hükmü ise **nitelenmeli**:
*"`fx` olmadan ters model `CIF_TRY`'nin bir **ÜST SINIRINA** kadar çalışır."*

---

### BU TURDA ÇÖZÜLMEYEN AMA DEĞİNİLEN MEVCUT ÇELİŞKİLER

| conflict_id | Sahibi | Ters modeldeki etkisi |
|---|---|---|
| `C-311` (FCL bandı 4 kat) | navlun-lojistik | **SIFIR** — navlun CIF'in içindedir, tavanı değiştirmez (`reverse-price-model.md` §8.3) |
| `C-501` (`available` filtresi) | türkiye-pazar | Sweet-spot §2 alıntısının tabanı; **modelin sayılarını değiştirmez** |
| `C-551` (Metro KDV sunumu) | türkiye-pazar | `OBSERVED_BENCHMARK` kullanılmadı → **etkisiz** |
| `C-561` (bantta ürün var, dönmüyor) | türkiye-pazar | `T-857`'nin ikinci bacağı |
| `C-601` (yasal vade 60 vs fiili 70–93 gün) | kanal-marj | `peak_cash` hesaplanmadığı için **bu turda etkisiz**; TUR 3'te belirleyici |
| `C-602` (tekel marjı) | kanal-marj | `T-856`'nın tabanı |

---

---

# TUR 3A ÇELİŞKİ FRAGMENT'LERİ

> Ajanların `99-ops/_parts/*-tur3a.md` fragment'lerinden değiştirilmeden aktarıldı.

## gumruk-vergi-uzmani (TUR 3A)

---

### KAYNAKLAR ARASI ÇELİŞKİ: **YOK**

Bu turda taranan tüm T1/T2 kaynaklar **birbiriyle tutarlıdır**:

| Kaynak A | Kaynak B | Sonuç |
|---|---|---|
| RG 24/11/2023-32379, 7846 s. CBK tam metni (OCR) | KDVGUT III/C-2.6'daki resmî alıntı | **KELİME KELİME AYNI** — çapraz doğrulama sağlandı |
| KDVK md.29/1-b (kanun) | KDVGUT III/C-1 (tebliğ) | Aynı sonuç |
| KDVK md.30 tahdidi liste | GİB özelgesi 20/08/2011 | Aynı sonuç |
| TUR 1 gözetim araması (`EV-2026-08-09-125`, mevzuat.gov.tr) | TUR 3A gözetim taraması (`EV-2026-08-10-860`, RG) | **Farklı yöntem, aynı sonuç** |

Bu nedenle `C-171 … C-189` bloğundan **hiçbir conflict_id açılmamıştır.**

---

### PROJE İÇİ TUTARSIZLIK (çelişki değil, **düzeltme**) — kayda geçirilir

#### D-1 · TUR 1.5'in olasılık değerlendirmesi YANLIŞ ÇIKTI

`EV-2026-08-10-114` ve `T-151` şunu yazıyordu:

> *"Olasılık **DÜŞÜK** değerlendirilmiştir — böyle bir kısıtlama sektörde
> bilinir olurdu ve md.30'un tahdidi listesiyle sistematik olarak çelişirdi."*

**Gerçek:** md.36'ya dayanan bir Cumhurbaşkanı Kararı **vardır** (7846 s.,
yürürlük 2023-11-24) ve md.30'un tahdidi listesiyle **hiç çelişmez** —
çünkü md.30 değil, **md.36 ayrı bir yetki hükmüdür.**

**Ders (yöntemsel):** *"böyle bir şey olsa duyulurdu"* bir kanıt değildir ve
bu projede bir kez daha yanlış çıkmıştır. `EV-2026-08-10-114`'ün `status`
alanı `UNKNOWN` kalır (kanıt kartları immutable'dır) ancak artık
`EV-2026-08-10-852` ile **cevaplanmıştır.**

#### D-2 · `finans-fizibilite`'nin %22,7 rakamı FAZLA KÖTÜMSER

`rapor-tur25-finans.md` §9.1 ve `T-947`, kısıt hâlinde `MAX_CIF_TRY`'nin
**%22,7** düşeceğini yazmıştı. Bu **tam kısıt** varsayımıdır.

7846 **kısmi kısıt** getirir (`EV-2026-08-10-854`): yalnız tevsik edilemeyen
artış kısmına isabet eden KDV indirilemez.

**Bu bir çelişki değil, bir varsayım düzeltmesidir** → `T-171` ile
`finans-fizibilite`'ye bildirildi. Rakamın kendisi **onun alanıdır**;
ben yeni bir tavan hesaplamadım.

#### D-3 · Ters modelin gözetim uyarı metni ARTIK YANLIŞ

`ters-model-vergi-bacagi.md` §11 ve `vergi.yaml`'daki eski `cikti_kurali`:

> *"gözetim eşiği doğrulanmamıştır; `CIF_TRY_max` bir alt sınırla test
> EDİLMEMİŞTİR"*

**Artık test edilmiştir ve alt sınır YOKTUR.** `vergi.yaml` güncellendi;
`ters-model-vergi-bacagi.md` §11 metni bu turda **değiştirilmemiştir**
(TUR 2.5 belgesidir, tarihsel kayıt olarak durur) — güncel otorite
`vergi.yaml` ve `gozetim-kiymet-kontrolu.md`'dir. Bu ayrım `T-171`'de
açıkça yazılmıştır.

---

## kanal-marj-uzmani (TUR 3A)

<!-- 99-ops/celiskiler.md'ye BASKAN tarafindan birlestirilir. Bu dosya bir PART'tir. -->

### C-611 — DIŞ DİSTRİBÜTÖR MARJININ MODELDEKİ YERİ, KANAL BELGESİYLE ÇELİŞİYOR

```yaml
conflict_id:   C-611
acan:          kanal-marj-uzmani
tarih:         2026-08-10
durum:         OPEN
impact:        HIGH
```

| | **Kaynak A** | **Kaynak B** |
|---|---|---|
| Belge | `70-kanal/kanal-marj-yapisi.md` §6 (TUR 2, **bu ajan**) | `80-model/outputs/reverse-price-model.md` §7.1 + `ters_model.py:392` (TUR 2.5) |
| Tier | repo-içi spesifikasyon | repo-içi model uygulaması |
| İddia | *"distribütör marjı **`L6` ile `L7` arasına girer**"* — yani distribütör **bir katman olarak araya girer** ve zincir bedellerini **kendisi üstlenir** | Distribütör marjı, ithalatçının `L5` bütçesinden **`m_dist × L6`** olarak düşülür; **`d` ve `f` aynı anda ithalatçıda kalır** ve *"aynı anda ikisi birden uygulanırsa **TOPLANIRLAR**"* |

#### Neden çelişiyor

İki okuma **aynı ekonomik dünyayı tarif etmiyor**:

- **A**: distribütör → perakendeci ilişkisini distribütör yönetir; zincirle
  yıllık anlaşmayı (`EV-2026-08-10-612`) o imzalar; ciro primini ve
  listeleme bedelini **o öder**. Bizim yükümüz `m_dist`'tir, `d` **değildir**.
- **B**: her iki yük de bizde. Yani zincire hem `d·L6 + f` ödüyoruz hem
  distribütöre `m_dist·L6` ödüyoruz.

**Bu bir hesap farkı değil, bir DÜNYA farkıdır.** Üstelik `B` altında
distribütörün ne sattığı belirsizdir: `L6` hem *bizim* fatura fiyatımız
hem *distribütörün* fatura fiyatı gibi kullanılmaktadır — **modelde
distribütör için ayrı bir katman YOKTUR.**

#### Büyüklük

`TGT_799 · CHAIN BASE · d = %8`: `d·L6 = 43,4239 TL/şişe`
→ `MAX_CIF`'te **28,95 TL/şişe** (g=0,50).
**`R5` hatasıyla tam olarak aynı büyüklük, ters yön** — bu kez model
**aşırı kötümser** olabilir.

#### Bu ajan sessizce seçim YAPMAMIŞTIR

Distribütörün zincir bedellerini üstlenip üstlenmediği **sözleşmeye
bağlıdır ve hiçbir kanıtımız yoktur** (`kanal.yaml`: *"TUR 2'DE HİÇBİR
KANITLI DEĞER BULUNAMAMIŞTIR"*). Bu ajan bir taraf **seçmemiş**, iki alt
senaryo tanımlamıştır:

```
A1 : d ve f BIZDE          + m_dist    (modelin bugunku davranisi)
A2 : d ve f DISTRIBUTORDE  + m_dist    (m_dist buyur, d ve f sifirlanir)
```

#### Çözüm yolu

`T-617` (`finans-fizibilite`) — iki alt senaryonun **ayrı ayrı**
koşulması ve §7.1'deki *"özdeştir / toplanırlar"* ifadesinin
kaldırılması veya koşullandırılması. **Nihai çözüm ancak gerçek bir
distribütör görüşmesiyle gelir** (`T-604`, TUR 7).

---

### C-602'YE EKLEME — TEKEL BAYİ MARJININ **MATRAH** BOYUTU

```yaml
conflict_id:   C-602 (mevcut — kapatilmadi, GENISLETILDI)
ekleyen:       kanal-marj-uzmani
tarih:         2026-08-10
```

`C-602` bugüne kadar **seviye** çelişkisiydi (T5 kaynaklar birbiriyle
çelişiyor: *"alkolde ~%17"*, *"rakı %8"*, *"brüt %10–15"*,
*"ciro üzerinden %18–30"*).

**TUR 3A eklemesi — bu bir MATRAH çelişkisidir de:** bağımsız alkollü içki
noktasında ticari dil üç farklı olabilir ve **ikisi aynı, biri farklı sonuç
verir** (`L8_net = 665,83`, oran %18 illüstratif):

| Konuşma biçimi | Matrah | `L7_eff` |
|---|---|---|
| *"marjım %18"* (margin on selling price) | `L8_net` | **546,00** |
| *"tavsiye fiyattan %18 iskonto"* | `L8_net` | **546,00** *(aynı)* |
| *"maliyetin üstüne %18 koyarım"* (markup) | `L7_eff` | **564,27** *(+18,28)* |

`MAX_CIF` farkı **+12,19 TL/şişe** (g=0,50).

**Model bugün birinci okumayı kullanıyor ve bunu gerekçelendirmiyor.**
`kanal.yaml → tekel_bayi.marj_pct.margin_mi_markup_mi` alanı **`null`**'dır
— yani M1 kuralı gereği o sayı zaten geçersizdir.
→ `kanal-katman-matrah-haritasi.md` §4.1, `B-10`.

---

### C-551'E NOT — kapatılmadı, hatırlatılıyor

`C-551` (599,90 TL'nin KDV dahil olup olmadığı) **açıktır** ve bu turda
**ele alınmamıştır.** `kanal-katman-matrah-haritasi.md` bu sayıyı hiçbir
yerde kullanmamıştır (`M2`/`M3` gereği).

---
