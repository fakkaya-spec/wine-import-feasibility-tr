# ÇELİŞKİLER

Format: `C-###`

> **KURAL (CLAUDE.md §1.13): Kaynaklar çelişirse SESSİZCE SEÇİM YAPILMAZ.**
> Çelişki buraya kaydedilir ve `yatirim-komitesi-baskani`'na taşınır.
> Başkan tier, yürürlük tarihi ve kanıt kalitesine bakarak çözer;
> çözemezse çelişki `CONFLICT` olarak karara taşınır.

---

## DURUM — TUR 1 SONU: 14 AÇIK ÇELİŞKİ

Tümü `OPEN`. Hiçbiri sessizce çözülmedi. Çözüm yetkisi `yatirim-komitesi-baskani`'ndadır.

| conflict_id | Konu | impact | Açan ajan |
|---|---|---|---|
| C-101 | Asgari maktu ÖTV: 61,3914 vs 71,2692 TL/lt (mevzuat.gov.tr konsolide metin vs GİB güncel liste) | **CRITICAL** | `gumruk-vergi-uzmani` |
| C-201 | 4250 m.1/3 — 1.000.000 lt/yıl eşiği durgun şarap ithalatına uygulanıyor mu (muafiyet fıkrası yalnız viski ve tabiî köpüren şarabı sayıyor) | **CRITICAL** | `mevzuat-ruhsat-uzmani` |
| C-202 | Bildirim ↔ dağıtım yetki belgesi ↔ ithalat sıralama döngüsü | HIGH | `mevzuat-ruhsat-uzmani` |
| C-203 | 7584 s.K. satış noktası marka/ambalaj görseli yasağının raf kapsamı | **CRITICAL** | `mevzuat-ruhsat-uzmani` |
| C-204 | TGK Şarap Tebliği'nin mülga kanuna dayanması; etiket kuralı hangi metinden okunacak | LOW | `mevzuat-ruhsat-uzmani` |
| C-301 | Konteyner başına palet adedi (aynı kaynağın iki yayını çelişiyor) | MEDIUM | `navlun-lojistik-uzmani` |
| C-302 | Valencia/ABD → İstanbul transit süresi (7–10 gün vs 32–35 gün) | HIGH | `navlun-lojistik-uzmani` |
| C-303 | 20DV azami payload (28.300 / 28.200 / 26.000 kg) | LOW | `navlun-lojistik-uzmani` |
| C-401 | Private label MOQ: 300–1.200 vs 3.000–3.600 vs 1 konteyner | HIGH | `global-sourcing-kasifi` |
| C-402 | ABD menşeli ithalatın birim değeri (25,19 USD/lt) benchmark segmentiyle bağdaşmıyor | MEDIUM | `global-sourcing-kasifi` |
| C-403 | Benchmark ürünün California alt bölgesi | LOW | `global-sourcing-kasifi` |
| C-501 | Aynı feed'de stokta olan/olmayan SKU fiyatları arasında 10 kat fark | HIGH | `turkiye-pazar-kasifi` |
| C-502 | Metro'nun KDV dili: etikette KDV dahil, ticari koşullarda KDV hariç | MEDIUM (izleme) | `turkiye-pazar-kasifi` |
| C-503 | T5 medya fiyat listesi ile gözlemlenen bant uyumu (üç site aynı tabloyu kopyalamış) | MEDIUM | `turkiye-pazar-kasifi` |

> **Not:** C-101, C-201 ve C-203 CRITICAL'dır. CLAUDE.md §5 uyarınca kritik
> çelişki/ticket açıkken finans modeli `APPROVED` olamaz.

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
