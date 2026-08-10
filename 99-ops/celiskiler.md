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
| C-201 | 4250 m.1/3 — 1.000.000 lt/yıl eşiği durgun şarap ithalatına uygulanıyor mu (muafiyet fıkrası yalnız viski ve tabiî köpüren şarabı sayıyor) | **CRITICAL** | `mevzuat-ruhsat-uzmani` | **OPEN** |
| C-202 | Bildirim ↔ dağıtım yetki belgesi ↔ ithalat sıralama döngüsü | HIGH | `mevzuat-ruhsat-uzmani` | **OPEN** |
| C-203 | 7584 s.K. satış noktası marka/ambalaj görseli yasağının raf kapsamı | **CRITICAL** | `mevzuat-ruhsat-uzmani` | **OPEN** |
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

> **Not:** C-201 ve C-203 **CRITICAL ve OPEN**'dır. CLAUDE.md §5 uyarınca kritik
> çelişki/ticket açıkken finans modeli `APPROVED` olamaz.
> C-101 kapanmıştır, ancak bağlı ticket `T-104` (**CRITICAL**) açık kalmaya
> devam eder — çelişkinin çözülmesi ÖTV'nin zaman içinde değişkenliğini ortadan
> kaldırmaz.

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
| **C-551** | Metro'nun **şarap** kataloglarında (2008/2009/2010 arşiv) fiyatlar fiilen ÇİFT gösteriliyor (KDV hariç + KDV'li). TUR 1'in KDV sonucu, içinde sıfır alkol bulunan broşürlerden çıkarılmıştı. | **CRITICAL** | `turkiye-pazar-kasifi` |
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
