# AÇIK SORULAR

Format: `OQ-###` · Durum: `OPEN` | `ANSWERED` | `CLOSED` | `BLOCKED`

---

## OPEN QUESTION #001 — Metro benchmark fiyatının KDV ve kanal statüsü

```yaml
id:              OQ-001
durum:           PARTIALLY_RESOLVED   # TUR 1'de guncellendi (onceki: OPEN)
acilis_tarihi:   2026-08-09
guncelleme:      2026-08-09 (TUR 1, turkiye-pazar-kasifi)
acan:            TUR 0 kurulum
sorumlu_ajan:    turkiye-pazar-kasifi
oncelik:         1 (EN YUKSEK)
impact:          CRITICAL
bloke_ettigi:    G3 (Pazar gate'i), ters modelin hedef fiyati
```

### Soru

Metro Türkiye'de **09.08.2026** tarihinde görülen
**Gold Country California Colombard-Chardonnay 2023, 750 ml — 599,90 TL**
etiket fiyatı:

1. **KDV dahil mi, KDV hariç mi?**
2. **Tüketici satış fiyatı mı, profesyonel/cash & carry fiyatı mı?**
3. Hangi fiyat katmanına karşılık geliyor — **L7** (perakendeci alış) mi,
   **L8** (tüketici raf) mi?
4. Promosyonlu bir fiyat mıydı, normal fiyat mıydı?

Aynı sorular komşu benchmark için de geçerlidir:
**Central Creek (Avustralya) — 649,90 TL**

### Neden kritik

Metro bir **cash & carry** formatıdır. Bu formatta etikette KDV hariç
profesyonel fiyat ile KDV dahil fiyat birlikte gösterilebilir.

Bu doğrulanmazsa:
- Ters model (`target shelf price → max EXW/FOB`) **yanlış hedefle** çalışır.
- KDV oranı kadar bir sapma tüm fiyat merdivenini kaydırır.
- Sapma doğrudan **üreticiye ödeyebileceğimiz maksimum fiyata** yansır —
  yani projenin asıl çıktısını bozar.
- 599,90 TL bir L8 değil L7'ye yakın bir sayıysa, tüketici raf fiyatı
  belirgin biçimde daha yüksektir ve segment tanımı değişir.

### Kapanana kadar geçerli kural

`finans-fizibilite` bu benchmark'ı **tek bir sayı olarak kullanamaz.**
Model iki senaryoyu **ayrı ayrı** çalıştırır ve farkı raporlar:
- **BM_A:** 599,90 TL = KDV **dahil**
- **BM_B:** 599,90 TL = KDV **hariç**

(bkz. `80-model/inputs/senaryolar.yaml` → `benchmark_senaryolari`)

### Nasıl kapatılır

| # | Yöntem | Not |
|---|--------|-----|
| 1 | Mağazada etiketin tam fotoğrafı (küçük punto KDV satırı dahil) | En güçlü kanıt |
| 2 | Metro kasa fişi | Fiilen ödenen tutarı gösterir |
| 3 | Metro Türkiye online/kurumsal fiyat gösterim politikası | T2/T4 |
| 4 | Aynı SKU'nun zincir markette (Migros/CarrefourSA) tüketici fiyatı | Karşılaştırma sağlar |

### Kapanış kaydı

```yaml
durum:              PARTIALLY_RESOLVED
cevap_kapanan: >
  Metro Turkiye raf/brosur fiyati KDV DAHIL'dir; ayni fiyat hem bireysel
  tuketiciye hem profesyonel musteriye uygulanir (Metro'da tek fiyat).
  OQ-001'in kurucu hipotezi (etikette KDV haric + KDV dahil CIFTLI gosterim)
  incelenen materyalde karsiligini BULMAMISTIR; etiketteki ikinci sayi
  birim fiyattir. Katman: L8_METRO_CASH_CARRY (zincir market L8'i DEGIL).
cevap_acik_kalan: >
  (a) Fiyat promosyonlu mu normal mi - CRITICAL, T-504.
  (b) Sarap reyonundaki FIZIKSEL etiket gorulmedi (kanit brosurden).
  (c) Zincir market tuketici fiyati (gercek L8) alinamadi - alkol online
      satilamiyor.
  (d) Metro'da uyelik tipine gore ozel fiyat olup olmadigi.
evidence_id:        EV-2026-08-09-503, -504, -505, -506, -507, -508, -511
kapanis_tarihi:     null
kapatan_ajan:       null
engel:              T-504 (CRITICAL) cozulmeden CLOSED yapilamaz
```

### TUR 1 sonrası model kuralı (öneri — kararı başkan verir)

```yaml
BM_A (599,90 = KDV dahil):    BASE CASE      # kanitli
BM_B (599,90 = KDV haric):    SENSITIVITY    # kanitsiz, ama elenmedi
BM_C (599,90 = promosyonlu):  YENI SENARYO   # OQ-001'in kapanmayan ayagi
BM_D (zincir L8 > Metro L8):  YENI SENARYO   # katman ayrimi
```

---

## OPEN QUESTION #002 — Model hedef tarihi

```yaml
id:              OQ-002
durum:           INPUT_RECORDED        # 2026-08-10 — KAPANMADI
onceki_durum:    OPEN
acilis_tarihi:   2026-08-09
guncelleme:      2026-08-10 (TUR 2.5 PRE-FLIGHT)
acan:            TUR 0 kurulum
sorumlu_ajan:    mevzuat-ruhsat-uzmani (T0 takvimi) -> yatirim-komitesi-baskani
impact:          HIGH
bloke_ettigi:    vergi.yaml/meta.model_hedef_tarihi
kayit_belgesi:   90-karar/tur-25-preflight.md
```

### Soru

İlk konteynerin gümrükten çekileceği tahmini tarih nedir?

### Neden önemli

Vergi ve mevzuat verileri **bugünkü** hâliyle değil, **model hedef
tarihinde yürürlükte olacak** hâliyle kullanılmalıdır. Özellikle maktu ÖTV
tutarları periyodik olarak güncellenir. Bugünkü tutarla yapılan hesap,
ithalat anında geçersiz olabilir.

Bu, `seytanin-avukati`'nın **regülasyon şoku** vektörünün doğrudan konusudur.

### Nasıl kapatılır

`mevzuat-ruhsat-uzmani`'nın T0 → ilk konteyner takviminden türetilir.

---

### GÜNCELLEME — 2026-08-10, TUR 2.5 PRE-FLIGHT (`yatirim-komitesi-baskani`)

#### Yatırımcı girdisi KAYDEDİLDİ

```
BASE_TARGET_DATE = 2027-04-01
status           = INVESTOR_ASSUMPTION      # FACT DEGILDIR

EARLY = 2027-01-01
BASE  = 2027-04-01
LATE  = 2027-07-01
```

Yazıldığı yerler: `80-model/inputs/vergi.yaml → meta.model_hedef_tarihi` +
`meta.tarih_senaryolari` · `80-model/inputs/senaryolar.yaml →
tarih_senaryolari`.

#### ⚠ NEDEN `CLOSED` DEĞİL — üç gerekçe

**1. Kaydedilen şey bir olgu değil, bir beyandır.** `2027-04-01`
ölçülmemiş, türetilmemiş ve bir T0 takviminden çıkarılmamıştır. Sorunun
orijinal kapanış yolu (*"`mevzuat-ruhsat-uzmani`'nın T0 → ilk konteyner
takviminden türetilir"*) **kullanılmamıştır**; o takvim hâlâ
`ASSUMPTION` sıralamasına dayanmaktadır (`C-202`, `T-202` açık) ve
dağıtım yetki belgesinin **işlem süresi mevzuatta tanımsızdır**.
Yani tarihin **gerçekçiliği** doğrulanmamıştır.

**2. Sorunun asıl blokeri tarih değil, o tarihteki ÖTV tutarıydı.** Üç
senaryonun **üçü de** `otv_maktu_zaman_serisi.son_gozlem_gecerlilik_ufku`
(**2026-12-31**) ötesindedir. Yani tarih dolduruldu ama **hiçbiri için
doğrulanmış bir ÖTV tutarı yoktur.** `OQ-G08` bu yüzden **aynen açıktır**.

**3. Tarih kaydı modeli güvenlileştirmedi — tehlikeyi artırdı.**
`80-model/engine/matrah_sirasi.py:217` bu alanı yalnızca `is None` ile
denetliyordu; alan dolduğu için **o tek uyarı sustu**, yerine hiçbir
denetim gelmedi ve engine `otv_maktu_zaman_serisi`'ni **hiç okumuyor**.
→ **`T-921` (CRITICAL, OPEN)** bu yüzden açıldı ve `OQ-002`'nin kapanışı
artık ona bağlıdır.

#### ÖTV rejimi eşlemesi (tarih senaryosu → hangi rejim)

| Senaryo | Tarih | ÖTV rejimi | Rejim netliği | Tutar |
|---|---|---|---|---|
| **EARLY** | 2027-01-01 | Ocak 2027 revizyonu | ❌ **SINIR TARİHİ** — belirsiz | `FUTURE_UNKNOWN` |
| **BASE** | 2027-04-01 | Ocak 2027 revizyonu | ✅ **NET** — iki revizyonun tam arasında | `FUTURE_UNKNOWN` |
| **LATE** | 2027-07-01 | Temmuz 2027 revizyonu | ❌ **SINIR TARİHİ** — belirsiz | `FUTURE_UNKNOWN` |

**Sınır belirsizliğinin gerekçesi (gözlem, tahmin değil):** doğrulanmış iki
yürürlük tarihi **2025-12-31** ve **2026-07-03**'tür — yani revizyonlar
1 Ocak / 1 Temmuz'a **birebir oturmaz** (ÖTVK md.12/3 *"değişimin ilanı
gününden geçerli olmak üzere"* der, `EV-2026-08-09-114`, T1). Bu nedenle
`EARLY` ve `LATE` **iki ayrı rejim altında ayrı ayrı** çalıştırılmalıdır.

#### Bilinen tek gerçek değer ve yasak

```
CURRENT_CONFIRMED : 71,2692 TL/lt · eff 2026-07-03 · EV-2026-08-09-111 · T2
                    gecerlilik bitisi 2026-12-31 · ttl 30d (STALE: 2026-09-08)

FUTURE_UNKNOWN    : 2027 tutarlari BILINMIYOR. SAYI YAZILMAZ.
                    Yalnizca duyarlilik ekseni olarak temsil edilir
                    (senaryolar.yaml -> duyarlilik_eksenleri[OTV]).
```

**YASAK:** `CURRENT_CONFIRMED`, üç hedef tarihin **hiçbiri** için "geçerli
tutar" olarak kullanılamaz. Kullanılırsa çıktı **geçersizdir**
(CLAUDE.md §1.1 + §12).

#### `OQ-002`'yi ne kapatır

| # | Koşul |
|---|---|
| 1 | **`T-921` `RESOLVED`** — engine seriyi okur ve ufuk denetimi yapar |
| 2 | Tarihin **T0 takviminden doğrulanması** — `T-202`/`C-202` kapanışı (dağıtım yetki belgesi işlem süresi) |
| 3 | Hedef tarihte geçerli ÖTV tutarının **fiilen yayımlanması** (yani takvimin o noktaya gelmesi) — **veya** kararın açıkça `PROJEKSIYON` üzerine kurulduğunun kabulü |

**1 ve 2 olmadan `OQ-002` kapanmaz.** 3 bu araştırmayla kapanamaz.

---

## KURAL

- Yeni açık soru bu dosyaya `OQ-###` ile eklenir.
- Kritik bir açık soru (`impact: CRITICAL`) ilgili gate'i bloke eder.
- **Kritik UNKNOWN nihai kararı bloke edebilir** — bu bir başarısızlık değil,
  tasarımın parçasıdır (CLAUDE.md §1.14).
- Bir soru **sessizce** kapatılmaz; kapanış `evidence_id` ile kanıtlanır.

---

## TUR 1 SONU — AÇIK SORU DURUMU

| id | Konu | durum | impact |
|---|---|---|---|
| OQ-001 | Metro benchmark fiyatının KDV ve kanal statüsü | **PARTIALLY_RESOLVED** | CRITICAL |
| OQ-002 | Model hedef tarihi | **OPEN** | HIGH |
| OQ-G01…G08 | Gümrük/vergi açık soruları (KDV indirilebilirliği, gözetim, KKDF matrahı, kısmi çekiş, menşe ispatı, 12 hane GTİP, damga vergisi, hedef tarihte ÖTV) | OPEN | 3'ü CRITICAL |
| `mevzuat` soruları | 13 soru (dağıtım yetki belgesi süresi, 1M lt eşiği, 7584 raf kapsamı, analiz zorunluluğu, teminat, TGK etiket metni vb.) | OPEN | 3'ü CRITICAL |
| `navlun` soruları | KRİTİK/YÜKSEK/ORTA/DÜŞÜK gruplu liste (rota navlunu, California rotası, toplam lead time, bandrolleme kapasitesi vb.) | OPEN | 4'ü CRITICAL |
| OQ-401…OQ-415 | Sourcing açık soruları (gerçek EXW/FOB, MOQ yapısı, menşe ispat kabiliyeti vb.) | OPEN | 3'ü CRITICAL |
| OQ-501, OQ-502, OQ-503 | Pazar açık soruları (ithalat hacmi, fiziksel raf gözlemi, benchmark ürünün ithalatçısı) | OPEN | — |
| **OQ-901** | **Karar eşiklerinin tamamı `TBD`** — nihai karar eşiksiz verilemez (sahibi: **yatırımcı**) | **OPEN** | **CRITICAL** |
| **OQ-902** | **İki iş modeli (A/B) eşit derinlikte araştırılamadı** — karar kanıtla değil arama yöntemiyle Model B'ye kayabilir | **OPEN** | HIGH |

> Ajanlar farklı ID şemaları kullanmıştır (`OQ-###`, `OQ-G##`, gruplu liste).
> Başkan bunları yeniden numaralandırmamıştır; ajan raporları bu ID'lere
> atıf yapmaktadır. Detay için aşağıdaki ajan bölümlerine bakınız.
> `OQ-901`/`OQ-902` başkan tarafından TUR 1 kanıt kalitesi denetiminde
> açılmıştır; kayıtları bu dosyanın **sonundadır**.

---

# TUR 1 AÇIK SORULARI (ajan fragment'lerinden birleştirildi)

> Aşağıdaki bölümler ajanların `99-ops/_parts/acik-sorular-*.md` dosyalarından
> **değiştirilmeden** aktarılmıştır. Başlık seviyeleri bir kademe indirilmiştir.


## gumruk-vergi-uzmani

> Bu turda cevaplanamayan, cevabı modeli veya kararı etkileyen sorular.
> Kritiklik sırasına göre.

---

### OQ-G01 — İthalatta ödenen KDV indirilebilir mi? (CRITICAL)
**Neden kritik:** CLAUDE.md §6 KDV'yi iki perspektifle göstermeyi zorunlu kılıyor.
İndirilebiliyorsa KDV L5'e taşınmaz ve yalnız nakit akışını etkiler; indirilemiyorsa
şişe başına ~40–45 TL doğrudan ekonomik maliyettir. Bu, tüm marj hesabını değiştirir.
**Bu turda neden çözülemedi:** KDV Kanunu md.29 vd. genel indirim mekanizması
mevcut, ancak alkollü içki ticaretine özgü bir sınırlama olup olmadığı
T1/T2 ile doğrulanamadı.
**Nasıl bulunur:** 3065 sayılı Kanun md.29–34 ve KDV Genel Uygulama Tebliği'nin
indirim bölümü; GİB özelgeleri.
**Sorumlu:** `gumruk-vergi-uzmani` (TUR 5).
**Geçici çözüm:** Model iki senaryo (A1 indirilebilir / A2 indirilemez) ile çalıştırılır.

---

### OQ-G02 — Şarapta ithalatta gözetim uygulaması gerçekten yok mu? (CRITICAL)
**Neden kritik:** Gözetim varsa birim kıymet eşiğinin altında beyan fiilen
kullanılamaz ve ucuz sourcing stratejisi çöker (`matrah-sirasi.md` §2).
**Bu turda ne yapıldı:** Mevzuat Bilgi Sistemi tebliğ veri tabanında
"2204.21", "2204.29", "22.04" tam metin araması yapıldı — hiçbir gözetim tebliği
eşleşmedi. Yöntem, bilinen bir gözetim GTİP'i (8536.20.10.00.11) ile kontrol
edildi ve ilgili tebliğ (2008/11) doğru bulundu.
**Neden yeterli değil:** Negatif arama sonucu yokluğun kanıtı değildir; veri
tabanı kapsamı ve mülga/geçici tebliğler doğrulanmadı.
**Nasıl kapanır:** Ticaret Bakanlığı İthalat Genel Müdürlüğü'nün yürürlükteki
gözetim tebliğleri listesi veya bir gümrük müşavirinden GTİP bazlı teyit.
**evidence_id:** EV-2026-08-09-125

---

### OQ-G03 — KKDF matrahı tam olarak nedir? (HIGH — vadeli senaryoda CRITICAL)
**Neden önemli:** 2011/2304 sayılı Karar md.4 yalnızca **oranı** (%6) ve
tetikleyici ödeme şekillerini tanımlıyor; matrahın mal bedeli mi, CIF mi,
yoksa vadeli ödenen kısım mı olduğu Karar metninde yok.
**Baz senaryoya etkisi:** Peşin ödemede KKDF = 0 olduğu için **etkisiz**.
Vadeli ödeme senaryosunda CIF üzerinden %6, şişe başı maliyeti anlamlı ölçüde
değiştirir.
**Nasıl bulunur:** Gümrükler Genel Müdürlüğü KKDF genelgeleri; Hazine ve Maliye
Bakanlığı KKDF tebliğleri.
**Ticket:** T-105

---

### OQ-G04 — Antrepodan kısmi çekiş (partial release) mümkün mü ve maliyeti nedir? (HIGH)
**Neden önemli:** Mümkünse `peak_cash_requirement` dramatik biçimde düşer.
Bir konteyner (≈10.000–13.000 şişe) tek seferde vergilendirilirse şişe başı
~150–200 TL vergi × 12.000 şişe = 2 milyon TL mertebesinde peşin nakit gerekir.
**Bu turda ne bulundu:** Gümrük Kanunu md.101/1 antrepoda sınırsız kalış süresi
tanıyor; md.181/1-a vergiyi serbest dolaşıma giriş beyannamesinin tesciline
bağlıyor. Kısmi çekişe dair açık bir T1 hüküm bu turda bulunamadı.
**Ticket:** T-101 → `navlun-lojistik-uzmani` (antrepo onun alanında)

---

### OQ-G05 — Menşe ispat belgesi türü nedir? (MEDIUM)
**Neden önemli:** AB/BK/Şili için %50 indirimli oranın kullanılabilmesi belge
şartına bağlıdır. Belge alınamazsa DÜ %70 uygulanır — 20 puanlık fark.
**Bu turda çözülemedi:** EUR.1 / fatura beyanı / REX / A.TR ayrımı anlaşma
bazında doğrulanamadı. Şarap tarım ürünü olduğu için A.TR'nin (serbest dolaşım
belgesi) tek başına yeterli olmayacağı, menşe ispatı gerekeceği yapısal olarak
beklenir ancak **belgelenmedi**.
**Nasıl bulunur:** Türkiye-AB 1/98 sayılı Ortaklık Konseyi Kararı menşe
protokolü; Gümrük Yönetmeliği tercihli menşe hükümleri.

---

### OQ-G06 — 12 haneli GTİP alt kırılımı hangisi? (LOW — vergiyi değiştirmiyor)
**Neden düşük öncelikli:** 2204.21/22/29 altındaki 113 GTİP satırının tamamında
AB=%50, DÜ=%70 aynı; ÖTV 22.04 pozisyon seviyesinde. Alt kod **vergi yükünü
değiştirmiyor** (EV-2026-08-09-102).
**Neden yine de gerekli:** Gümrük beyannamesi 12 haneli kod ister.
**Bu turda neden çözülemedi:** 2026 Türk Gümrük Tarife Cetveli (CBK 10781,
RG 30/12/2025) PDF'i **taranmış görüntü** olarak yayımlanmış, metin katmanı yok;
TARA tarife arama motoru CAPTCHA korumalı.
**Nasıl bulunur:** Gümrük müşaviri, TARA (manuel), veya AB Kombine Nomenklatürü
2026 (8 hane için) + TGTC (son 4 hane için).

---

### OQ-G07 — Gümrük beyannamesi damga vergisi 2026 tutarı? (LOW)
Maktu ve küçük bir kalem, ancak `UNKNOWN` bırakıldı. Beyanname başına düşer,
şişe başına etkisi ihmal edilebilir düzeyde olması beklenir — ancak
**varsayılmadı**.

---

### OQ-G08 — Model hedef tarihinde hangi ÖTV tutarı geçerli olacak? (CRITICAL — zamanlama)
`00-charter/kapsam.md` model hedef tarihini TBD bırakmış. ÖTV maktu tutarı
**Ocak ve Temmuz'da otomatik artıyor** (EV-2026-08-09-114). İlk konteynerin
gümrükten çıkış tarihi 2027 Ocak'ı geçerse, bugünkü 71,2692 TL/lt **geçersizdir**.
**Bağımlılık:** `mevzuat-ruhsat-uzmani`'nın T0 takvimi.
**Ticket:** T-104 → `finans-fizibilite`

---

## mevzuat-ruhsat-uzmani

> `UNKNOWN` yazmak başarısızlık değildir. Uydurmak başarısızlıktır.

| # | Soru | Neden bulunamadı | Kritiklik | Nasıl bulunabilir | Ticket |
|---|------|------------------|-----------|-------------------|--------|
| Q-201 | **Dağıtım yetki belgesi başvurusu kaç günde sonuçlanır?** | Ticaret Yön. m.12'de azami süre **tanımlı değil**; yalnızca "yerinde ve/veya kayıtlar üzerinde incelenerek" deniyor. | **CRITICAL** (kritik yolun %25–35'i) | TADAB Alkol ve Alkollü İçkiler Daire Başkanlığına yazılı/KEP sorusu; son 2 yılda belge almış firma referansı | `T-202` |
| Q-202 | 4250 m.1/3'teki **1.000.000 litre/yıl** eşiği durgun şarap ithalatına bugün uygulanıyor mu? | Kanun lafzı ile muafiyet fıkrası çelişiyor; sıfıra indirme yetkisi kullanıldığına dair BKK bulunamadı. | **CRITICAL** (G0 önerisini değiştirir) | TADAB görüş talebi; Yetkili Dağıtım Firmaları Listesindeki küçük ölçekli ithalatçıların varlığı; hukuk bürosu görüşü | `T-201` |
| Q-203 | Dağıtım yetki belgesi bedelinde **maktu asgari** ile **hacim bedeli** max mı, toplam mı? | Tebliğ 2025/39 lafzı ("en az") her iki yoruma açık. | HIGH (sabit maliyette ~32.000 TL sapma) | TADAB portal bedel hesaplama ekranı; TADAB'a doğrudan soru | `T-202` |
| Q-204 | **7584 s.K. satış noktası marka yasağı** zincir market rafında ürünün kendisini kapsıyor mu? | Kanun 20/6/2026'da yürürlüğe girdi; ikincil düzenleme/rehber henüz yayımlanmamış. | **CRITICAL** (pazarlama modelini çökertebilir) | TADAB ikincil düzenlemesinin/rehberinin takibi; TADAB görüş talebi; ilk denetim uygulamaları | `T-205` |
| Q-205 | Şişelenmiş ithal şarapta **zorunlu analiz** var mı? Parametreler, akredite lab, parti başına tekrar, süre, maliyet? | Ticaret Yön. m.7 analiz hükmü dökme alkol içindir; gıda ithalat kontrolleri risk esaslıdır. | MEDIUM | Bitkisel Gıda ve Yem İthalatının Resmî Kontrollerine Dair Yönetmelik (RG 17/12/2011-28145) tam metni; GGBS uygulama talimatı; akredite lab teklifi | `T-206` |
| Q-206 | **TADAB ürün onayı için ayrı bir bedel** var mı? | Tebliğ 2025/39'da ürün onayı bedeli yok; TADAB duyurusunda da bedel geçmiyor. | MEDIUM | TADAB portal başvuru ekranı; TADAB'a soru | — |
| Q-207 | **Türkçe etiket menşede mi antrepoda mı** uygulanmalı? Yasaklayıcı hüküm var mı? | Mevzuatta konumu belirleyen açık hüküm bulunamadı. | MEDIUM (maliyet yeri değişir) | TADAB görüş talebi; mevcut ithalatçı uygulaması (T4) | — |
| Q-208 | Sağlık uyarı mesajlarının **birebir yazılı metni** nedir? | Tebliğ Ek-1 görsel olarak yayımlanmış; metin çıkarılamadı. T5 basın "Alkol dostunuz değildir" diyor — doğrulanmadı. | MEDIUM (etiket tasarımı) | Tebliğ Ek-1 PDF/görselinin temini; TADAB'dan resmî örnek | — |
| Q-209 | **TGK Gıda Etiketleme ve Tüketicileri Bilgilendirme Yönetmeliği** (RG 26/1/2017-29960 mükerrer) tam metni ve şaraba özgü zorunlu bilgiler | resmigazete.gov.tr ve mevzuat.gov.tr bu oturumda TLS/503 nedeniyle erişilemedi. | HIGH (etiket uyumu) | FAO FAOLEX aynası veya Bakanlık kılavuzu; farklı ağdan resmigazete.gov.tr | — |
| Q-210 | **ÜGD 2026/19** ithalat denetimi tebliğinin tam metni ve Ek-1/Ek-2 GTİP listeleri | Aynı erişim sorunu; yalnızca ikincil kaynaklardan özet alınabildi. | MEDIUM (yükümlülük zaten T1 düzeyde sabit) | Resmî Gazete 31/12/2025-33124 (4. mükerrer) | — |
| Q-211 | **Teminat** — TADAB veya başka bir merci alkollü içki ithalatçısından teminat istiyor mu? | İncelenen metinlerde teminat hükmü yok; negatif ispat yapılamaz. | MEDIUM | TADAB görüş talebi; gümrük/antrepo teminatı için `gumruk-vergi-uzmani` ve `navlun-lojistik-uzmani` | — |
| Q-212 | Bandrol talebi için **TADAB uygunluk onayı** kaç günde verilir? | ÜİS Tebliği 3.3.2 "TADAB tarafından belirlenen usul ve esaslara göre" der; süre yok. İlgili genelgeye erişilemedi (404). | HIGH (T0 takviminde 5–15 gün ASSUMPTION) | "Alkollü İçki İthalatında Bandrol Talebinde Bulunulması, İncelenmesi ve Onaylanmasında Uyulacak Usul ve Esaslara İlişkin Genelge"nin güncel URL'sinden temini | `T-204` |
| Q-213 | Ana sözleşmede **faaliyet konusu** olarak neyin yazması gerekiyor? Özel bir NACE/faaliyet kodu şartı var mı? | Yönetmelik yalnızca "ana sözleşme" istiyor, içerik şartı belirtmiyor. | LOW | TADAB uygulaması / mali müşavir | — |

---

## navlun-lojistik-uzmani

> **UNKNOWN yazmak başarısızlık değildir; uydurmak başarısızlıktır.**
> Aşağıdaki sorular TUR 1'de kapatılamadı.

---

### KRİTİK (nihai kararı bloke edebilir)

| # | Soru | Neden kritik | Kim / nasıl çözer | Ticket |
|---|---|---|---|---|
| **NL-Q1** | **Bizim rotalarımız için gerçek FCL navlunu kaç USD/EUR?** (İspanya/İtalya/Fransa/California/Şili/G.Afrika → Ambarlı/Mersin/İzmir; 20DV ve 40HC; all-in) | Hiçbir rotamız için doğrulanmış navlun yok. Bu, CIF'in ve dolayısıyla tüm vergi matrahının girdisidir. Navlun 2× olursa şişe başı maliyet ~0,10–0,20 USD artar. | 3 forwarder'dan yazılı kotasyon (geçerlilik tarihi ve dahil kalemler yazılı) | `T-304` |
| **NL-Q2** | **Ruhsat / analiz / uygunluk / bandrol beklemesi kaç gün sürer?** | Demurrage/detention (20DV'de 60 günde ~8.000 USD) ve toplam lead time bu sayıdan türer. Toplam lead time UNKNOWN olduğu sürece işletme sermayesi ve `peak_cash_requirement` hesaplanamaz. | `mevzuat-ruhsat-uzmani` T0 takvimi | `T-301` |
| **NL-Q3** | **Toplam lead time (PO → satışa hazır) kaç gün?** | CCC, stok gün sayısı, `peak_cash_requirement`. Yalnız transiti lead time sanmak modeli sistematik iyimser yapar. | NL-Q1 + NL-Q2 + sourcing üretim süresi birleşince türetilir | `T-301`, `T-304` |
| **NL-Q4** | **California → İstanbul transit süresi ve navlunu nedir?** | Benchmark ürünün (Gold Country) rotası tam budur ve tamamen UNKNOWN. Kaynaklar birbiriyle çelişiyor (`C-302`). | Armatör servis tarifesi + forwarder kotasyonu | `T-304` |

---

### YÜKSEK

| # | Soru | Neden önemli | Kim / nasıl çözer | Ticket |
|---|---|---|---|---|
| NL-Q5 | Tedarikçinin **gerçek şişe formu, çapı, koli dış ölçüsü, koli brüt ağırlığı, palet konfigürasyonu, cam ağırlığı** nedir? | Şişe başı hacim 0,00223 → 0,0036 m³'e çıkarsa **tüm konteyner kapasiteleri %38 düşer.** Bu, hesabın en kırılgan girdisidir. | `global-sourcing-kasifi` — RFQ'ya "case & pallet spec sheet" maddesi eklenmeli | `T-302` |
| NL-Q6 | **Çekici + şasi darası** kaç kg? | 40HC'de Türkiye karayolu kargo tavanını (24,1–27,1 t) doğrudan belirler. 17 t dara ise 5 katmanlı paletli 40HC yüklemesi imkânsız hale gelir. | Türk nakliyeciden ruhsat/tartı bilgisi | `T-304` |
| NL-Q7 | **Terminal ardiye free time** kaç gündür? | Demurrage senaryosunda 0 gün varsaydım (muhafazakâr). Gerçekte 3–7 gün olabilir → gecikme maliyeti düşer. | Ambarlı terminallerinden (Marport/Kumport/Mardaş) tarife | `T-304` |
| NL-Q8 | **Ambarlı terminallerinin** kendi tarifesi nedir? | Beldeport/Asyaport tarifelerini gösterge olarak kullandım. Ambarlı gerçek varış limanı olacaksa kendi tarifesi gerekir. | Terminal tarife sayfaları / acente | `T-304` |
| NL-Q9 | **Bandrolleme operasyonunun birim maliyeti (şişe başı) ve kapasitesi (şişe/gün)** nedir? | 100.000 şişe/yıl senaryosunda operasyonel darboğaz adayı. Birim maliyet doğrudan L5'e girer. | Antrepo işletmecisinden hizmet teklifi | `T-304` |
| NL-Q10 | **Sıcaklık kaynaklı beklenen fire/leakage oranı (%)** nedir? | Bu sayı olmadan liner/reefer kararı finansal olarak verilemez. | Sigortacı hasar istatistiği veya Hillebrand Gori benzeri uzman | `T-304` |
| NL-Q11 | **Thermal liner birim maliyeti** nedir? | Reefer'a alternatif olarak sunuluyor ama fiyatı hiçbir kaynakta yok. | Forwarder / liner tedarikçisi | `T-304` |

---

### ORTA

| # | Soru | Neden önemli | Ticket |
|---|---|---|---|
| NL-Q12 | Limandan depoya konteyner çekme ücreti (Ambarlı → İstanbul depo) | Bulunan band (3.000–30.000 TL) modele girecek kadar dar değil | `T-304` |
| NL-Q13 | Antrepo giriş/çıkış elleçleme ücreti ve minimum süre taahhüdü | Antrepo maliyetinin depolamadan büyük olabilecek kısmı | `T-304` |
| NL-Q14 | Türk sigortacıdan gerçek kargo sigortası kotasyonu (ICC A + kırılma + termal şok), muafiyet dahil | Prim bandı %0,1–1,5 çok geniş | `T-304` |
| NL-Q15 | Ordino, ISPS, doc fee, BAF/CAF tutarları | "All-in" ile "base" arasındaki farkın büyüklüğü | `T-304` |
| NL-Q16 | Paletsiz (floor loaded) yüklemede gerçek kırılma oranı ve antrepoda yeniden paletleme maliyeti | Paletli/paletsiz kararının net finansal farkı UNKNOWN kaldı | `T-304` |
| NL-Q17 | İtalya ve Fransa → Türkiye transit süreleri | Sourcing alternatiflerinin karşılaştırması eksik | `T-304` |
| NL-Q18 | Şili → Türkiye rota yapısı (direkt servis var mı, aktarma nerede) | Şili sourcing senaryosu değerlendirilemiyor | `T-304` |
| NL-Q19 | Diğer armatörlerin (MSC, CMA CGM, Arkas, Hapag-Lloyd) Türkiye ithalat D&D free time'ı | Yalnızca Maersk tarifesi elimde; 7 gün genelleştirilebilir mi bilinmiyor | `T-304` |

---

### DÜŞÜK

| # | Soru | Ticket |
|---|---|---|
| NL-Q20 | 40HC gerçek dara ağırlığı (ASSUMPTION 3.900 kg kullanıldı) | `T-304` |
| NL-Q21 | LCL konsolidasyon beklemesinin transit süreye kaç gün eklediği | `T-304` |
| NL-Q22 | Şarap konteynerinin IMO/tehlikeli yük sınıfına girip girmediği (terminal %20 surprim) | `T-301` (mevzuat) |

---

## global-sourcing-kasifi

> **UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**
> Aşağıdakiler bu ajanın kendi alanında **çözemediği** sorulardır.

---

### KRİTİK (nihai kararı bloke edebilir)

#### OQ-401 — Gerçek EXW/FOB fiyatı hiçbir tedarikçi için bilinmiyor
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

#### OQ-402 — Gerçek MOQ ve MOQ yapısı
**Ne bilinmiyor:** Tedarikçi bazında gerçek MOQ; ve MOQ'nun SKU bazlı mı konteyner
bazlı mı olduğu. Kaynaklar 300 şişe ile 1 konteyner arasında değişiyor (`C-401`).
**Neden bulunamadı:** Üreticilerin çoğu MOQ'yu web'de yayınlamıyor; yayınlayan üç
üretici birbiriyle uyumsuz birimlerde ölçüyor.
**Nasıl bulunur:** RFQ 3.6 (a: şişe, b: konteyner) ve 4.2/4.3.
**Kritiklik:** **CRITICAL.** Pilot senaryonun (5.000 şişe) uygulanabilirliği doğrudan
buna bağlı.

#### OQ-403 — Menşe ispat belgesi kabiliyeti
**Ne bilinmiyor:** Hangi üretici hangi menşe ispat belgesini (EUR.1 / fatura beyanı /
REX / A.TR) düzenleyebiliyor.
**Neden bulunamadı:** Hiçbir üretici sitesinde bu bilgi yok; ayrıca hangi belgenin
gerektiği `gumruk-vergi-uzmani`'nın cevabına bağlı (T-401).
**Nasıl bulunur:** Önce T-401 kapanmalı, sonra RFQ 6.1.
**Kritiklik:** **CRITICAL** — tercihli tarife kaybı birim maliyeti anlamlı ölçüde
değiştirebilir.

---

### YÜKSEK

#### OQ-404 — Türkiye'de temsilcisi olmayan fiyat/performans markaları
**Ne bilinmiyor:** Model A için somut marka adları. Bu turda **tek bir marka bile**
"Türkiye'de temsilcisi yok" diye doğrulanamadı.
**Neden bulunamadı:** Bu bilgi iki yönlü bir kesişimdir: (a) markanın var olduğu,
(b) Türkiye'de dağıtılmadığı. (b) ancak Türkiye raf/ithalatçı verisinden bilinir —
`turkiye-pazar-kasifi`'nın alanı.
**Nasıl bulunur:** `turkiye-pazar-kasifi`'nın rakip/ithalatçı listesi ile bu ajanın
üretici portföy listesinin çaprazlanması (TUR 2).
**Kritiklik:** HIGH — Model A bu olmadan değerlendirilemez ve iki modelin
**eşit öncelikli** karşılaştırması eksik kalır.

#### OQ-405 — Ödeme vadesi ve ilk sipariş pratiği
**Ne bilinmiyor:** Tedarikçilerin Türk bir alıcıya ilk siparişte hangi ödeme şartını
dayatacağı.
**Elde olan:** Yalnızca genel sektör rehberi (`EV-2026-08-09-420`), tedarikçi taahhüdü
değil.
**Nasıl bulunur:** RFQ 3.8–3.10.
**Kritiklik:** HIGH — `peak_cash_requirement` ve CCC doğrudan etkilenir.

#### OQ-406 — Türkçe arka etiket menşede uygulanabilir mi
**Ne bilinmiyor:** Hiçbir üretici için doğrulanmadı; ayrıca hukuken mümkün mü,
bilinmiyor (T-403).
**Kritiklik:** HIGH — L5 (importer cost) katmanında bir operasyon kalemini
tamamen ortadan kaldırabilir veya ekleyebilir.

#### OQ-407 — Konteyner başına şişe sayısı
**Ne bilinmiyor:** 20' DV ve 40' HC'ye kaç şişe 750 ml yüklenir; ağırlık mı hacim mi
bağlayıcı.
**Neden bulunamadı:** Alan dışı — `navlun-lojistik-uzmani` (T-402). Ayrıca üreticilerin
koli/palet ölçüleri de bilinmiyor (RFQ 2.1–2.8).
**Kritiklik:** HIGH — konteyner bazlı MOQ'lu tedarikçilerin pilot uyumu bunsuz
hesaplanamaz.

---

### ORTA

#### OQ-408 — Marka ve reçete IP sahipliği (private label)
**Ne bilinmiyor:** Private label'da harmanın ve markanın hukuken kimde olduğu.
**Neden önemli:** IP üreticideyse "tedarikçi değiştirilebilir" iddiası çöker ve
tek tedarikçiye bağımlılık riski gerçekleşir.
**Nasıl bulunur:** RFQ 4.9 ve 4.10.

#### OQ-409 — Etiket klişe / kalıp tek seferlik maliyeti
**Ne bilinmiyor:** Bir üretici tasarımı "ücretsiz" sunduğunu beyan ediyor
(`EV-2026-08-09-408`) ama baskı klişesi, kalıp veya minimum baskı adedi maliyeti
bilinmiyor. Küçük pilot hacimde bu, şişe başına anlamlı olabilir.
**Nasıl bulunur:** RFQ 4.7.

#### OQ-410 — ABV
**Ne bilinmiyor:** Aday ürünlerin hiçbirinin ABV'si bilinmiyor. Benchmark ürünün ABV'si
de `00-charter/benchmark.md`'de UNKNOWN.
**Neden önemli:** ABV, GTİP alt kırılımı veya ÖTV eşiği ile ilişkiliyse tedarikçi
seçimini değiştirir; ayrıca private label'da **ayarlanabilir** bir parametredir.
**Nasıl bulunur:** RFQ 1.4 + `gumruk-vergi-uzmani`'nın eşik cevabı.

#### OQ-411 — Yıllık kapasite ve süreklilik
**Ne bilinmiyor:** Hiçbir aday tedarikçinin bize ayırabileceği yıllık hacim.
100.000 şişe/yıl senaryosunun (charter'ın üst ucu) hangi tedarikçilerle mümkün
olduğu bilinmiyor.
**Nasıl bulunur:** RFQ 3.12 ve 8.3.

#### OQ-412 — Moldova / Gürcistan / Bulgaristan tedarikçi tabanı
**Ne bilinmiyor:** Bu üç ülke Türkiye'ye anlamlı hacimde ve düşük birim değerle mal
gönderiyor, ancak bu turda **tek bir üretici doğrulanmadı.**
**Neden bulunamadı:** Zaman/kaynak önceliği charter'ın öncelikli 9 ülkesine verildi.
**Nasıl bulunur:** Wine of Moldova (ONVV), Georgian Wine Association, Bulgarian
Association of Independent Winegrowers üye listeleri — bir sonraki tur.
**Kritiklik:** MEDIUM — ama fiyat sinyali en güçlü grup burada olduğu için
gözden kaçırılması pahalıya mal olabilir.

---

### DÜŞÜK

#### OQ-413 — Les Grands Chais de France doğrulaması
Kurumsal site (groupegcf.com) 2026-08-09'da HTTP 503 döndü; firma tedarikçi havuzuna
alınmadı (`EV-2026-08-09-428`). Bir sonraki turda yeniden denenmeli.

#### OQ-414 — Ciatti dökme fiyat grid'i
Ciatti Global Market Report'un ülke bazlı dökme fiyat tablosu **abonelik arkasında**;
yalnızca yorum metni erişilebildi. Ülke bazlı dökme fiyat tabanı bu nedenle
yalnızca OIV dünya ortalamasıyla (`EV-2026-08-09-402`) temsil ediliyor.

#### OQ-415 — OEMV birincil verisi
İspanya ihracat fiyatları basından okundu (T5); OEMV'nin kendi sayfası doğrudan
doğrulanmadı (`EV-2026-08-09-427`). Modele girmedi.

---

### ÖZET TABLO

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

---

## turkiye-pazar-kasifi

> Bu dosya ana `99-ops/acik-sorular.md`'ye başkan tarafından birleştirilecektir.

---

### OQ-001 — GÜNCEL DURUM

```yaml
id:              OQ-001
onceki_durum:    OPEN
YENI_DURUM:      PARTIALLY_RESOLVED
guncelleyen:     turkiye-pazar-kasifi
guncelleme_tar:  2026-08-09
```

#### Kapanan kısımlar

| Alt soru | Cevap | Güven | evidence |
|---|---|---|---|
| KDV dahil mi, hariç mi? | **KDV DAHİL** | HIGH | `EV-2026-08-09-503`, `-504`, `-505`, `-506` |
| Tüketici satış fiyatı mı? | **EVET** (Metro TR bireysel müşteriye ücretsiz kartla açık) | HIGH | `EV-2026-08-09-505` |
| Profesyonel / cash & carry fiyatı mı? | **EVET, aynı anda** (Metro'da tek fiyat) | HIGH | `EV-505`, `EV-507`, `EV-508` |
| Metro etiketi nasıl okunur? | **KDV hariç/dahil ÇİFTLİ gösterim YOK.** İkinci sayı **birim fiyattır** (kg/L/adet). Büyük punto = güncel satış fiyatı + `KDV'li`. Promosyonda üstü çizili eski fiyat + "AVANTAJLI FİYAT" rozeti. | HIGH | `EV-503`, `EV-504` |

**OQ-001'in kurucu hipotezi kısmen ÇÜRÜMÜŞTÜR:** "Metro etiketinde KDV hariç
profesyonel fiyat ile KDV dahil fiyat birlikte gösterilebilir" varsayımı,
incelenen Metro Türkiye materyalinde **karşılığını bulmamıştır.**

#### AÇIK KALAN kısımlar (bu yüzden `CLOSED` değil)

| # | Ne kapanmadı | Neden | Kritik mi |
|---|---|---|---|
| a | **Promosyon mu, normal fiyat mı?** | Tek gözlem var; etiketin promosyon rozeti/üstü çizili fiyat içerip içermediği bilinmiyor | **CRITICAL** — `T-504` |
| b | **Şarap reyonundaki fiziksel etiket** görüntülenmedi | Kanıt Metro'nun broşürlerinden; broşür ≠ raf etiketi | HIGH |
| c | **Zincir market tüketici fiyatı (gerçek L8)** | Alkol online satılamadığı için Migros/CarrefourSA'da fiyat yok | HIGH — `EV-511` |
| d | Metro'da üyelik tipine göre **özel fiyat** olup olmadığı | `guncelfiyatlar.metro-tr.com` "size özel fiyat" diyor ve giriş istiyor | MEDIUM |

#### Model kuralı (güncellenmiş öneri — kararı başkan verir)

```yaml
BM_A (599,90 = KDV dahil):   BASE CASE      # kanitli
BM_B (599,90 = KDV haric):   SENSITIVITY    # kanitsiz, ama elenmedi
BM_C (599,90 = promosyonlu): YENI SENARYO   # OQ-001'in kapanmayan ayagi
BM_D (zincir L8 > Metro L8): YENI SENARYO   # katman ayrimi
```

**OQ-001 `CLOSED` yapılamaz.** Kapanması için `T-504` çözülmelidir.

---

### OQ-501 *(YENİ)* — Türkiye şarap ithalat hacmi ve pazar büyüklüğü

```yaml
id:              OQ-501
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            turkiye-pazar-kasifi
sorumlu_ajan:    mevzuat-ruhsat-uzmani (TADAB erisimi) -> yatirim-komitesi-baskani
oncelik:         2
impact:          HIGH
bloke_ettigi:    hacim senaryolarinin (5.000-100.000 sise) gercekcilik testi
ticket:          T-505
evidence:        EV-2026-08-09-515
```

**Soru:** Türkiye'ye yıllık kaç litre / kaç dolar şarap ithal ediliyor, menşe kırılımı
ve trend nedir?

**Neden kritik:** Pazar hacmi bilinmeden "100.000 şişe/yıl ölçeklenebilir mi" sorusu
cevaplanamaz. TADAB'ın *Resmî İstatistikler* sayfası **yalnızca yakıt biyoetanolü**
yayınlıyor; Ticaret Bakanlığı ve mevzuat.gov.tr bu turda HTTP 503 döndü.

---

### OQ-502 *(YENİ)* — Zincir market ve tekel bayii kanalında sıfır gözlem

```yaml
id:              OQ-502
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            turkiye-pazar-kasifi
sorumlu_ajan:    turkiye-pazar-kasifi (TUR 2/7'de fiziksel gozlem)
impact:          HIGH
bloke_ettigi:    segment bantlarinin kanal capraz dogrulamasi
evidence:        EV-2026-08-09-511, EV-2026-08-09-514
```

**Soru:** Migros / Macrocenter / CarrefourSA / tekel bayii raflarında fiyat/performans
segmentindeki şarap fiyatları nedir?

**Neden kritik:** Charter kanal önceliği `1) chain retail 2) independent/tekel`.
Bu turda ikisinde de **sıfır** gözlem alınabildi. Segment bantlarının %87'si
(45/52 gözlem) **tek bir online kanaldan** gelmektedir. Bu bir örnekleme yanlılığıdır.

**Nasıl kapanır:** Fiziksel mağaza turu (İstanbul'da 1 gün): Metro + Migros/Macrocenter
+ CarrefourSA + 2 tekel bayii, her birinde 600–1.200 TL bandındaki tüm şarap SKU'larının
etiket fotoğrafı.

---

### OQ-503 *(YENİ)* — Gold Country ve Central Creek'i kim ithal ediyor?

```yaml
id:              OQ-503
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            turkiye-pazar-kasifi
sorumlu_ajan:    turkiye-pazar-kasifi
impact:          MEDIUM
bloke_ettigi:    rakip maliyet yapisi anlayisi
```

**Soru:** Benchmark SKU'larının Türkiye ithalatçısı kim? Metro'nun kendi ithalatı
(private/exclusive import) mı, bağımsız bir ithalatçı mı?

**Neden önemli:** İncelenen online uzman perakende kanalında **ABD ve Avustralya
menşeli hiç şarap yok** (`EV-509`). Eğer Metro bu SKU'ları doğrudan ithal ediyorsa,
599,90 TL bir **ithalatçı marjı içermeyen** fiyattır ve bizim rekabet edeceğimiz
maliyet yapısı bir kademe daha alçaktır. Bu, projenin en kötü senaryosudur.

**Nasıl kapanır:** Şişenin arka etiketindeki "İthalatçı:" satırının fotoğrafı.
(Aynı mağaza ziyaretinde alınabilir — `T-504` ile birleştirilebilir.)

---

---

# BAŞKAN TARAFINDAN AÇILAN AÇIK SORULAR (OQ-901 …)

> Açan: `yatirim-komitesi-baskani` · 2026-08-09
> Dayanak: `90-karar/tur-1-kanit-kalitesi-denetimi.md`
> Bu iki soru **hiçbir ajanın alanına girmez**; biri yatırımcıya, diğeri iki
> ajanın kesişimine aittir. Bu yüzden ajan bloklarında değil, burada durur.

---

## OQ-901 — Karar eşiklerinin tamamı `TBD`

```yaml
oq_id:        OQ-901
acan:         yatirim-komitesi-baskani
acilis:       2026-08-09
sahibi:       YATIRIMCI        # hicbir ajan bunu kapatamaz
durum:        OPEN
impact:       CRITICAL
bloke_ettigi: TUR 6 (nihai karar)
```

> ## ⚠ GÜNCELLEME — 2026-08-10 (TUR 2.5 KAPANIŞ)
>
> **`durum: OPEN` → `OPEN — SPECIFIED`.** **KAPATILMAMIŞTIR.**
> Aşağıdaki orijinal metin **aynen korunmuştur**; kapsam **genişlemiştir**:
>
> - **6 eşik → 16 eşik** (`D-01`…`D-16`) **+ 8 eşik dışı yatırımcı girdisi** (`I-1`…`I-8`)
> - Tam liste: **`90-karar/investor-decisions-required.md`**
> - Ayrıca `bloke_ettigi` genişledi: **TUR 3B (ileri model)** + TUR 6
>
> Ayrıntı için bu dosyanın **sonundaki** *"TUR 2.5 KAPANIŞ"* bölümüne bakınız.

### Soru

`00-charter/karar-esikleri.md` içindeki **altı finansal eşiğin tamamı `TBD`**'dir:

| Eşik | Değer |
|---|---|
| `target_gross_margin_pct` | TBD |
| `minimum_contribution_try_per_bottle` | TBD |
| `maximum_total_capital_try` | TBD |
| `maximum_acceptable_pilot_loss_try` | TBD |
| `target_inventory_days` | TBD |
| `target_payback_months` | TBD |

### Neden kritik

Charter'ın kendi ifadesiyle: *"Model, eşikler `TBD` iken çalışabilir — ama
**nihai karar** eşikler belirlenmeden verilemez."*

Bu, **araştırmayla kapanmayan tek CRITICAL açık sorudur.** Beş ajan da mükemmel
çalışsa, TUR 7'de gerçek RFQ ve gerçek navlun gelse, model pozitif contribution
üretse bile — hangi contribution'ın "yeterli" olduğunu söyleyen bir eşik yoksa
`IMPORT PILOT` ile `HOLD` arasındaki seçim **keyfî** olur.

İki eşik özellikle belirleyicidir:
- **`maximum_total_capital_try`** — `peak_cash_requirement` bunu aşarsa senaryo
  uygulanamaz. Bandrol peşin ödemesi (100.000 şişe = 236.073 TL), ruhsat sabit
  maliyeti (151–253 bin TL) ve gümrükte peşin ödenen ÖTV+KDV nedeniyle bu
  projede nakit ihtiyacı yapısal olarak yüksektir.
- **`maximum_acceptable_pilot_loss_try`** — `IMPORT PILOT` kararının
  **büyüklüğünü** belirler; olmadan pilot hacmi seçilemez.

### Ne zaman kapatılmalı

Charter'ın önerisi **TUR 3 sonrası**dır: model ilk çıktısını verdiğinde
yatırımcı gerçek sayı aralıklarını görür ve eşiği bilinçli belirler.

**Bu bir tuzak taşır ve kayda geçirilmiştir:** eşiği modelden *sonra*
belirlemek, **sonuca göre eşik ayarlama (hedef kaydırma)** riski yaratır.
Bu risk `seytanin-avukati` tarafından TUR 4'te bir saldırı vektörü olarak
kullanılmalıdır.

### Kapanmazsa ne olur

Başkan, kararın **hangi eşik varsayımıyla** verildiğini açıkça yazar ve bunu
`ASSUMPTION` olarak etiketler (`00-charter/karar-esikleri.md` §3). Bu, karara
gömülü ve doğrulanmamış bir eşik demektir — **kararın en zayıf halkası olur.**

---

## OQ-902 — İki iş modeli eşit derinlikte araştırılamadı

```yaml
oq_id:        OQ-902
acan:         yatirim-komitesi-baskani
acilis:       2026-08-09
sahibi:       global-sourcing-kasifi + turkiye-pazar-kasifi (kesisim)
durum:        OPEN
impact:       HIGH
bloke_ettigi: G2, is modeli secimi
kaynak:       50-sourcing/rapor-tur1-global-sourcing.md §9.2 (ajanin kendi itirafi)
```

### Soru

`00-charter/karar-esikleri.md`: *"**İki model eşit önceliklidir.**
`global-sourcing-kasifi` ikisini de eşit derinlikte araştırır. Birini
gerekçesiz öne çıkarmak yasaktır."*

TUR 1 sonucu:

| Model | Doğrulanmış aday |
|---|---|
| **B — Private label** | **10** |
| **A — Mevcut marka distribütörlüğü** | **1** |

`global-sourcing-kasifi` bunu §9.2'de **kendisi itiraf etmiştir** ve nedenini
doğru teşhis etmiştir:

> *"Private label sağlayıcıları kendilerini web'de 'private label wine' diye
> pazarlar ve bu yüzden aranabilirler. Mevcut marka sahipleri distribütör
> arayışını fuarlarda, ihracat destek kurumlarında ve doğrudan temasla
> yürütür — web'de aranmazlar. … Bu asimetri **Model B'nin daha iyi olduğunu
> göstermez; açık kaynakta daha görünür olduğunu gösterir.**"*

### Neden HIGH

Bu bir veri eksikliği değil, **sistematik arama yanlılığıdır.** Tehlike şudur:
model B lehine hiçbir kanıt üretilmeden, yalnızca **B hakkında daha çok kanıt
bulunduğu için** karar B'ye kayar. Ajanın kendi uyarısı:

> *"Bu kayma **kanıtla değil, arama yöntemiyle** üretilmiş olur.
> `yatirim-komitesi-baskani`'nın bu noktayı özellikle denetlemesi gerekir."*

Bu denetim yapılmış ve uyarı **haklı bulunmuştur.**

### Neden tek bir ajan kapatamaz

"Türkiye'de temsilcisi olmayan f/p markası" **iki yönlü bir kesişimdir**:
- Yön 1 (üretici portföyleri, fuar katılımcı listeleri) → `global-sourcing-kasifi`
- Yön 2 (Türkiye raf/ithalatçı haritası) → `turkiye-pazar-kasifi`

İkinci yön şu anda `UNKNOWN`'dır: ithalatçı/distribütör haritası çıkarılamamış,
TADAB alkol istatistiği yayınlamıyor, yalnızca Diageo doğrulanabilmiştir
(`OQ-404`, `T-505`, `T-405`).

### Nasıl kapatılır

| # | Ne | Kim | Süre |
|---|---|---|---|
| 1 | Türkiye'deki ithal SKU / ithalatçı listesi ile üretici portföylerinin çaprazlanması | `turkiye-pazar-kasifi` + `global-sourcing-kasifi` | 1–2 hafta (TUR 2) |
| 2 | ProWein / Wine Paris katılımcı listelerinin f/p segmenti için taranması | `global-sourcing-kasifi` | 1 hafta |
| 3 | Şişe arka etiketlerinden ithalatçı satırının okunması (raf ziyaretinde) | `turkiye-pazar-kasifi` | `T-504` ziyaretiyle birlikte |

### Başkan direktifi

Model A için **en az 5 somut aday marka** doğrulanana kadar, hiçbir ajan ve
hiçbir model çıktısı iki iş modeli arasında **tercih sıralaması** üretemez.
`finans-fizibilite` her iki modeli de çalıştırmak zorundadır; birinin girdisi
eksikse sonuç o model için `UNKNOWN` döner — **"veri yok" ile "sonuç kötü"
aynı şey değildir.**

### Bu soruyu ne çürütür

Model A'nın Türkiye'de **yapısal olarak** uygulanamaz olduğunun gösterilmesi
(örneğin distribütörlük sözleşmelerinde ithalatçının markup tavanının bu
segmentte ekonomiyi imkânsız kıldığının kanıtlanması). O durumda asimetri bir
yanlılık değil, **doğru bir eleme** olur ve OQ-902 gerekçeli olarak kapanır.

---

# TUR 1.5 AÇIK SORULARI

TUR 1.5 sonunda ana açık soruların durumu:

| id | Durum | Not |
|---|---|---|
| **OQ-001** | `PARTIALLY_RESOLVED` (kapanmadı) | Promosyon ayağı `UNKNOWN`; ayrıca KDV ayağı C-551 ile nitelendi. **G3 açılamaz.** |
| **OQ-002** | `OPEN` — yatırımcı girdisi | `model_target_date` TBD kalır. Yerine `BASE_DATE = 2026-08-10` tanımlandı; BASE_DATE senaryosunda yalnızca 2026-08-10'da yürürlükte olan doğrulanmış mevzuat kullanılır, gelecek ÖTV/kur tahmini yapılmaz. |
| **OQ-G01** (ithalat KDV'si) | **KAPANDI** | KDVK md.29/1-b + md.30 taraması, T1. |

## gumruk-vergi-uzmani (TUR 1.5)

> Bu dosya TUR 1'deki `acik-sorular-gumruk-vergi-uzmani.md` dosyasının
> **EKİDİR**, onun yerine geçmez. TUR 1 dosyasına DOKUNULMAMIŞTIR.

---

### KAPANAN SORU

#### ✅ OQ-G01 — İthalatta ödenen KDV indirilebilir mi? — **KAPANDI**

**Cevap: EVET, indirilebilir.**
KDVK **md.29/1-b** (T1, yürürlük 1985-01-01) + **md.34/1** belge şartı +
**md.30** tahdidi yasak listesinde alkole ilişkin hüküm **yok**.

| evidence_id | tier | ne kanıtlıyor |
|---|---|---|
| `EV-2026-08-10-101` | T1 | md.29/1-b — ithalatta ödenen KDV indirilir |
| `EV-2026-08-10-102` | T1 | md.34/1 — gümrük makbuzu + defter kaydı şartı |
| `EV-2026-08-10-103` | T1 | md.30 tam metin — alkole özgü yasak YOK (tahdidi liste) |
| `EV-2026-08-10-104` | T1 | md.29/2 — devreden KDV **iade edilmez** |
| `EV-2026-08-10-105` | T1 | md.29/3 — indirim hakkı süresi (VDO yılı + 1 yıl) |

Tam analiz: `30-vergi-gumruk/kdv-ekonomik-maliyet-vs-nakit.md`

**Modele etkisi:** `A1/A2 iki senaryo` zorunluluğu **kalktı**. A1 baz senaryodur;
KDV'nin ekonomik maliyeti **0,00 TL/şişe**'dir.

---

### YENİ AÇILAN SORULAR

#### OQ-G09 — Fiili KDV vergilendirme dönemi 1 ay mı 3 ay mı? (HIGH)

**Neden kritik:** KDVK md.39/1'in **kanuni varsayılanı 3 aydır**; 1 aylık dönem
bir Bakanlık tespitine dayanır. Model 1 ay varsayıyor (`ASSUMPTION`).
3 aylık dönemde ithalat KDV'sinin mahsup gecikmesi **28–59 gün → 28–~118 gün**'e
çıkar ve `peak_cash_requirement` ciddi biçimde büyür.
**Bu turda neden çözülemedi:** GİB'in mükellef gruplarını belirleyen tespiti/
tebliği bulunamadı; GİB sayfaları JS ile render ediliyor.
**evidence_id:** `EV-2026-08-10-111` (kanun metni, T1) · **Ticket:** `T-152`

---

#### OQ-G10 — KDVGUT III/C ve md.36 CB kararları taranmadı (MEDIUM)

**Neden önemli:** KDVK **md.36** Cumhurbaşkanı'na indirim hakkını kısmen/tamamen
**kaldırma** yetkisi verir. Şarap için böyle bir karar olup olmadığı
**aranmamıştır.** Bulunursa OQ-G01'in cevabı tersine döner.
**Neden düşük olasılık:** md.30'un tahdidi listesiyle sistematik çelişki
yaratırdı ve sektörde bilinir olurdu. Ama bu bir **argüman**, kanıt değil.
**evidence_id:** `EV-2026-08-10-114` (`status: UNKNOWN`) · **Ticket:** `T-151`

---

#### OQ-G11 — 149 No.lu VUK Sirküleri'nin tarihi (LOW)

GİB, KDV beyannamesi verme süresini kanuni 24. günden (KDVK md.41/1) **28. güne**
uzatmıştır. Bu uzatmanın `effective_date`'i doğrulanamadı → `EV-2026-08-10-109`
`effective_date: UNKNOWN`. Model **muhafazakâr** olan 28'i kullanır; 24/26
kullanılsaydı gecikme **2–4 gün kısalırdı** (yön lehte, büyüklük ihmal edilebilir).

---

#### OQ-G12 — KVK md.11/1-(ı) %50 oranı yürürlükte değiştirilmiş mi? (LOW)

Alkollü içki **ilan/reklam** giderlerinin %50'si KKEG'dir (T1, `EV-2026-08-10-113`)
ve KDVK md.30/d uyarınca o kısma ait KDV indirilemez. Cumhurbaşkanı bu oranı
%0–%100 arası değiştirmeye yetkilidir; yürürlükte bir değiştirme kararı olup
olmadığı **doğrulanmadı.**
**Neden düşük:** malın kendisine ait KDV'yi etkilemez; ayrıca alkolde reklamın
hukuken mümkün olup olmadığı `mevzuat-ruhsat-uzmani` alanıdır ve bu turda
kapalıdır. Reklam yapılamıyorsa etki **sıfırdır.**

---

### DEVAM EDEN SORULAR (TUR 1'den)

`OQ-G02` (gözetim), `OQ-G03` (KKDF matrahı), `OQ-G04` (antrepo kısmi çekiş),
`OQ-G05` (menşe ispat belgesi), `OQ-G06` (12 haneli GTİP), `OQ-G07` (damga
vergisi), `OQ-G08` (model hedef tarihi ÖTV'si) **AÇIK KALMAKTADIR**.
Bu turun kapsamı dar olduğu için bunlara dokunulmamıştır.

`T-901` (TÜİK Yİ-ÜFE doğrulaması) **ANSWERED / DOĞRULANAMADI** olarak
kapatılmıştır — sonuç `UNKNOWN`'dır, `RESOLVED` değildir.

---

## mevzuat-ruhsat-uzmani (TUR 1.5)

> `99-ops/acik-sorular.md`'ye konsolide edilmek üzere. Ana dosyaya bu turda
> **DOKUNULMAMIŞTIR.**

---

### Bu turda AÇILAN / DARALTILAN sorular

| id | Soru | status | Yön (proje açısından) | Kritik mi | Kapanış yolu |
|---|---|---|---|---|---|
| **OQ-251** | 2007'den itibaren 4250 m.1/3 ölçüsünü **sıfıra indiren** yürürlükte bir BKK/CBK var mı? | `UNKNOWN` | **LEHİNE** — varsa eşik tamamen kalkar | HAYIR | Farklı ağdan `resmigazete.gov.tr` / `mevzuat.gov.tr` taraması (bu oturumda TLS ile erişilemedi) |
| **OQ-252** | 4250 m.1/3 c.3'teki "**Tekel Genel Müdürlüğü eliyle** fiyatlandırma/satış/dağıtım" **ticari** işlevinin bugünkü halefi kim? | `UNKNOWN` | **ALEYHİNE** — varsa mekanizma canlanır | HAYIR (senaryolar eşiğin altında) | TADAB'a KEP ile yazılı görüş talebi |
| **OQ-253** | 4250 m.1/3'teki "**ülke genelinde her satıcıya yerinde teslim**" şartının **fiilî ölçütü** nedir? (kaç gün, hangi coğrafya, minimum sipariş var mı) | `UNKNOWN` | **ALEYHİNE** — doğrudan dağıtım maliyeti | HAYIR (G0 için); **kanal modeli için önemli** | TADAB uygulaması + faal ithalatçı görüşmesi → `kanal-marj-uzmani` |
| **OQ-254** | 4733 m.8 artık yaptırımının (uyarı → belge iptali) 4250 m.1/3 bağlamında **fiilen uygulandığı** bir örnek var mı? | `UNKNOWN` | **ALEYHİNE** | HAYIR | TADAB "İdari Yaptırımlar ve Teminatlar" arşivi (yıl bazında 4250 İPC listeleri yayımlanıyor) |

---

### Bu turda KAPANAN sorular

| Önceki soru | Yeni durum | Kanıt |
|---|---|---|
| "Eşik 1.000.000 mi ve durgun şaraba uygulanıyor mu?" (`T-201` çekirdeği) | **CEVAPLANDI** — uygulanan ölçü en çok 600.000; eşik bir ithalat/dağıtım/bedel eşiği değil, fiyatlandırma serbestisi koşulu | `EV-2026-08-10-201` … `-216` |
| "Yaptırım mercii ortadan kalktığına göre hüküm uygulanabilir mi?" | **CEVAPLANDI (proje aleyhine)** — 4250'nin uygulanması T1 ile Bakanlığa devredilmiştir; "hüküm ölü" argümanı geçersiz | `EV-2026-08-10-208`, `-210` |
| "Yetkili Dağıtım Firmaları Listesinden eşik altı ithalatçı tespit edilebilir mi?" | **KAPALI YOL** — TADAB firma bazında hacim yayımlamıyor; Resmî İstatistikler yalnızca yakıt biyoetanolü içeriyor | `EV-2026-08-10-213` |

---

### Bu turda TESPİT EDİLEN ama ARAŞTIRILMAYAN ipucu *(kapsam dışı bırakıldı)*

TADAB sitesinde **"İdari Yaptırımlar ve Teminatlar"** başlıklı bir bölüm
bulunmaktadır (`https://www.tarimorman.gov.tr/TADAB/Link/140/...`). TUR 1'de
`teminat` alanı `UNKNOWN` bırakılmıştı (`EV-2026-08-09-229`). **Bu tur dar
kapsamlı olduğu için bölüm İNCELENMEMİŞTİR ve hakkında hiçbir sonuç
üretilmemiştir.** Gelecek turda `teminat.*` alanlarının doldurulması için
birincil aday kaynaktır.

---

## global-sourcing-kasifi (TUR 1.5)

```yaml
ajan:  global-sourcing-kasifi
tur:   TUR 1.5 — BLOCKER REMEDIATION (T-902)
tarih: 2026-08-10
```

> Parça dosyadır. `99-ops/acik-sorular.md` ana dosyasına başkan birleştirir.
> Bu ajan ana dosyaya dokunmadı.

---

### Yeni açık soru

| # | Ne bilinmiyor | Neden bu turda çözülmedi | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| **OQ-451** | **OIV ihracat birim değeri serisinin gerçek katmanı nedir?** (`tedarikci.yaml → ihracat_ort_birim_degeri_EUR_per_litre`) TUR 1'de L1 (FOB) varsayılmıştı; T-902 ile bu iddia geri çekildi ve katman `UNKNOWN` yapıldı. | TUR 1.5 bir **düzeltme turudur**, araştırma turu değildir; yeni kaynak araması bu turda açıkça yasaklandı. | **MEDIUM** — modele fiyat girdisi olarak girmiyor (çit var), ama ülke sıralamasını kaba düzeyde etkiliyor | OIV'in "export value" tanımının birincil kaynaktan (OIV metodoloji notu) okunması. ~1 gün. |

**Neden CRITICAL değil:** bu seri `SENSITIVITY_BOUNDS_ONLY` çitinin arkasındadır ve
`kullanim_yasagi` bloğu onu L1 girdisi olarak kullanmayı açıkça yasaklar. Katmanı
bilinmese bile model yanlış bir sayı okumaz — sadece bu seriden çıkarım yapamaz.

**Neden LOW da değil:** eğer serinin gerçekten FOB olduğu doğrulanırsa, L1 > L2
tersliği bir etiket sorunu olmaktan çıkıp **veri sorununa** dönüşür ve o zaman ya
Comtrade birim yorumu (bkz. TUR 1 raporu §9.1) ya da OIV türetmesi hatalıdır.
Yani bu soru, iki farklı kaynağın güvenilirliğini test eden bir düğümdür.

---

### TUR 1'den devreden ve bu turda DEĞİŞMEYEN açık sorular

`OQ-401` … `OQ-415` (bkz. `99-ops/_parts/acik-sorular-global-sourcing-kasifi.md`)
**hiçbiri kapanmamıştır.** Özellikle:

- `OQ-401` (gerçek EXW/FOB — **CRITICAL**) — bu turda üreticiye temas yasaktı.
- `OQ-402` (gerçek MOQ yapısı — **CRITICAL**) — aynı.
- `OQ-403` (menşe ispat belgesi — **CRITICAL**) — `T-401`'e bağlı.

**T-902'nin kapanması bu üç kritik UNKNOWN'ı kapatmaz.** Katman etiketinin
düzeltilmesi bir kanıt kalitesi iyileştirmesidir, bir fiyat bulgusu değildir.

---

### Bu turda yeni ÇELİŞKİ (`C-4xx`) açılMAdı — gerekçe

L1 > L2 tersliği ilk bakışta bir `CONFLICT` gibi görünür, ama değildir:

- `CONFLICT` = **iki kaynak aynı iddia hakkında çelişiyor** (CLAUDE.md §1.13).
- Burada OIV ile Comtrade **aynı iddiada bulunmuyor**: biri ülkelerin dünyaya
  ihracatını, diğeri Türkiye'nin ithalatını ölçüyor. Çelişen kaynaklar değil,
  **bu ajanın iki seriye aynı ölçeği atfeden etiketiydi** — ve o etiket geri çekildi.

Terslik yine de kaydedilmiştir: `EV-2026-08-10-401` ve
`tedarikci.yaml → karsilastirilamazlik_kaniti`. Sessizce geçilmemiştir.

**Ne zaman gerçek bir çelişkiye dönüşür:** `OQ-451` cevaplanır ve OIV serisinin
gerçekten FOB olduğu doğrulanırsa. O noktada iki T3 kaynak aynı ölçekte çelişiyor
demektir ve bir `C-` numarası hak eder.

---

## turkiye-pazar-kasifi (TUR 1.5)

> `99-ops/acik-sorular.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından DOKUNULMAMIŞTIR.

---

### OQ-001 — durum güncellemesi (TUR 1.5)

**`PARTIALLY_RESOLVED` OLARAK KALIR. KAPANMADI.**

| Ayak | TUR 1 | TUR 1.5 |
|---|---|---|
| KDV dahil mi? | KAPANDI — KDV DAHİL | **KAPALI (korundu)** — ama `C-551` / `T-551` ile *nitelendi*: gerekçe artık "çiftli gösterim yoktur" olamaz |
| Tüketici fiyatı mı / cash&carry mi? | KAPANDI — ikisi de | KAPALI (değişmedi) |
| Etiketteki ikinci sayı | KAPANDI — **birim (litre) fiyatı** | KAPALI (değişmedi) |
| Katman | `L8_METRO_CASH_CARRY` | KAPALI (başkan onaylı) |
| **Promosyon mu, normal mi?** | **UNKNOWN** | **UNKNOWN — 8 masabaşı yolu denendi, hepsi kapalı** (`EV-2026-08-10-504`) |
| Zincir market gerçek L8'i | UNKNOWN | UNKNOWN (araştırılmadı — kapsam dışı) |
| Şarap reyonu fiziksel etiketi | GÖRÜLMEDİ | GÖRÜLMEDİ |

**OQ-001'i kapatan tek şey değişmedi ve fizikseldir:**
şarap reyonundaki etiketin küçük puntolu satırları okunacak fotoğrafı +
2–4 hafta arayla ikinci fiyat gözlemi.

---

### OQ-551 — Metro Türkiye'nin şarap assortman büyüklüğü (DOĞRULANMADI)

```yaml
oq_id:        OQ-551
sorumlu:      turkiye-pazar-kasifi
tur:          TUR 1.5 (yan bulgu)
durum:        OPEN
impact:       MEDIUM
```

TUR 1.5'te `T-504` araştırması sırasında bir web araması özetinde
*"Metro Türkiye'de üzümden elde edilen 502 çeşit içecek var; 342 yerli,
160 yabancı"* biçiminde bir ifadeye rastlandı.

- **Birincil kaynağa ULAŞILAMADI.** Hangi Metro yayınından/basın bülteninden
  geldiği doğrulanamadı.
- **Kanıt kartı AÇILMADI**, çünkü doğrulanamayan bir sayı için kart açmak
  onu meşrulaştırır.
- **MODELE GİREMEZ.**

Neden yine de kaydediliyor: doğruysa, Metro'nun şarap reyonunda **160 ithal
SKU** olduğu anlamına gelir; bu, benchmark'ın "tek başına duran bir ürün"
değil, geniş bir ithal assortmanın parçası olduğunu gösterir ve
`ithal_sku_400_800_uzman_kanal = 0` bulgusunun **kanal spesifik** olduğunu
kuvvetle destekler. TUR 2'de fiziksel mağaza turunda **sayılarak**
doğrulanmalıdır.

---

### Devam eden UNKNOWN'lar (TUR 1'den, TUR 1.5'te DEĞİŞMEDİ)

Bu tur **dar kapsamlıydı**; aşağıdakiler araştırılmadı ve `pazar.yaml`'da
`null` + `UNKNOWN` olarak durmaktadır:

| # | Alan | impact |
|---|---|---|
| 1 | `l8_chain_retail.deger_try` — zincir market gerçek tüketici raf fiyatı | HIGH |
| 2 | `pazar_hacmi.*` — Türkiye şarap ithalat hacmi / menşe kırılımı / trend | HIGH |
| 3 | `ithalatci_haritasi.*` — 1 doğrulanmış ithalatçı bir harita değildir | HIGH |
| 4 | `horeca.fiyat_carpani`, `horeca.hacim_payi_pct` | HIGH |
| 5 | `kanal_yapisi.tekel_bayii_fiyatlari` | HIGH |
| 6 | `benchmark_1.magaza` / `.sehir` / `.abv_pct` / `.ithalatci_distributor` | MEDIUM |
| 7 | `benchmark_2.hacim_ml` (750 ml **doğrulanmadı**) | MEDIUM |
| 8 | `kanal_yapisi.bim_a101_sok_sarap_var_mi`, `bizim_toptan_fiyatlari`, `duty_free` | MEDIUM |

---

---

# TUR 2 AÇIK SORULARI

TUR 2 sonunda kapanamayan yapısal boşluk, ajanların ortak tespitidir:
**gerçek teklif olmadan kapanmayacak alanlar** artık tek tek listelenmiştir.

| Kaynak | Alan sayısı | Nasıl kapanır |
|---|---|---|
| `global-sourcing-kasifi` | **21 alan** (+ Model A'ya özgü 7) | Gerçek RFQ gönderimi (T-467) |
| `kanal-marj-uzmani` | **12 alan** | Gerçek kanal görüşmesi (T-604) |
| `navlun-lojistik-uzmani` | FCL navlunu, İtalya rotası, sigorta, bandrolleme | 3 forwarder yazılı kotasyonu (T-304) |

Üçünün ortak özelliği: **daha fazla web araştırması bu alanları kapatmaz.**
Bu bir veri eksikliği değil, izin/zamanlama sorunudur.

## gumruk-vergi-uzmani (TUR 2)

> Kapsam: menşe → tarife eşlemesi. TUR 1 ve TUR 1.5'in açık soruları
> `acik-sorular-gumruk-vergi-uzmani.md` ve `…-tur15.md` dosyalarında durmaktadır
> ve **kapanmamıştır**.

---

### OQ-G12 — 1/98 sayılı Karar'ın **ürün listesi** 2204.21'i gerçekten içeriyor mu?

```yaml
id:        OQ-G12
impact:    MEDIUM
blocks:    -            # G1'i bloke ETMEZ (oran T1 ile sabit)
sahibi:    gumruk-vergi-uzmani
```

GGM Menşe Kontrol Tablosu'nun `ATRM` satırı, GTİP kapsamını *"**3 — Yalnızca
Tarım ürünleri listesindeki** tüm ürünler esas alınacaktır"* diye tanımlıyor
(`EV-2026-08-10-158`). **O "tarım ürünleri listesi"nin kendisini görmedim.**

2204.21'in o listede olduğunu, İthalat Rejimi Kararı'nın AB sütununda **%50
taviz bulunmasından türettim**. Türetme mantıklıdır (taviz varsa dayanağı
1/98'dir) ama **doğrudan gözlem değildir.**

**Neden G1'i bloke etmiyor:** `applicable_customs_rate = 50` değeri
`EV-2026-08-09-103` (T1, İthalat Rejimi Kararı) ile **doğrudan** sabittir.
Bu soru oranı değil, **oranın hukuki dayanağının adını** ve dolayısıyla
belge satırının doğruluğunu ilgilendirir.

**Nasıl kapanır:** 1/98 sayılı OKK'nın ekli ürün listesi (mevzuat.gov.tr /
ticaret.gov.tr — bu oturumda erişilemedi) veya gümrük müşaviri teyidi.
Bu, `mense-tarife-eslemesi.md`'nin **en zayıf halkasıdır.**

---

### OQ-G13 — Fatura beyanının değer eşiği ve "onaylanmış ihracatçı" koşulu

```yaml
id:        OQ-G13
impact:    LOW
blocks:    -
sahibi:    gumruk-vergi-uzmani
ticket:    T-162
```

Fatura beyanının belirli bir değer eşiği altında **her** ihracatçıya, üstünde
ise yalnızca **"onaylanmış ihracatçı"**ya açık olup olmadığı T1/T2 ile
doğrulanamadı. **Model etkisi yok:** EUR.1 her hâlükârda düzenlenebilir; bu
yalnızca tedarikçinin hangi belgeyi tercih edeceğini etkiler.

---

### OQ-G14 — DÜ menşede menşe şahadetnamesi **zorunlu** mu?

```yaml
id:        OQ-G14
impact:    LOW
blocks:    -
sahibi:    gumruk-vergi-uzmani
ticket:    T-162
```

Gümrük Rehberi (T2), menşe şahadetnamesinin ibrazını **ticaret politikası
önlemi** bağlamına bağlıyor (`EV-2026-08-10-162`). 2204.21'de yürürlükte bir
önlem tespit edilemedi (İGV yok — `EV-2026-08-09-107`; gözetim `UNKNOWN` —
`EV-2026-08-09-125`). Gümrük Yönetmeliği **md.205** T1 metnine erişilemedi.

**Model etkisi yok:** DÜ'de oran zaten %70; belge oranı değiştirmez.

---

### OQ-G15 — Transhipment ≠ çıkış ülkesi değişimi mi?

```yaml
id:        OQ-G15
impact:    HIGH
blocks:    -            # G1 degil, G2-L / G4 tarafinda
sahibi:    navlun-lojistik-uzmani
ticket:    T-163
```

BİLGE çıkış ülkesi kontrolü (`EV-2026-08-10-158`, `-160`) ile "doğrudan
nakliyat" koşulu (`EV-2026-08-10-163`) arasındaki tam ilişki bende
`UNKNOWN`'dır: **bir limanda gemi aktarması yapmak, o ülkeden "çıkış yapmak"
sayılır mı?**

**Neden HIGH:** Sayılıyorsa, Şili rotasında herhangi bir aktarma tercihli oranı
düşürür ve şişe başına **+24 TL** getirir. Sayılmıyorsa etki yoktur.
İki cevap arasındaki fark, tüm Şili senaryosunun ekonomisini değiştirir.

---

### OQ-G16 — Tercihli oran **sonradan geri alınabilir mi**?

```yaml
id:        OQ-G16
impact:    MEDIUM
blocks:    -
sahibi:    gumruk-vergi-uzmani
```

Gümrük Rehberi, menşe şahadetnamesinde *"ciddi bir şüphe durumunda gümrük
idareleri ek kanıtlar istemeye yetkilidir"* diyor. **Tercihli** belgelerde de
sonradan kontrol (subsequent verification) mekanizması olduğu biliniyor
(Rehber'de "Menşe ve dolaşım belgeleri üzerinde yapılan kontroller" başlığı
var) ancak **usulü ve sonucu bu turda incelenmedi.**

**Neden önemli:** İthalat anında ödenmeyen 20 puanın, aylar sonra **cezalı**
olarak istenmesi senaryosudur. Bu, bir maliyet kalemi değil bir **kuyruk
riskidir** ve `seytanin-avukati` için hedeftir.

---

### Ulaşılamayan resmî kaynaklar (2026-08-10 — dürüst kayıt)

| Host | Sonuç | Etkilenen soru |
|---|---|---|
| `mevzuat.gov.tr` | TLS handshake / connection reset | Gümrük Yönetmeliği md.205, Türkiye-Şili menşe yönetmeliği (No 14805), 1/98 OKK |
| `resmigazete.gov.tr` | Aynı | Aynı |
| `ticaret.gov.tr`, `ggm.ticaret.gov.tr`, `ab.ticaret.gov.tr` | Sunucu ara sertifika göndermiyor → TLS zinciri kurulamıyor; WebFetch 503 | STA listesi, Menşe Kontrol Tablosu'nun **resmî** kopyası |
| `gumrukrehberi.gov.tr` | ✅ Erişildi | T2 kanıtların kaynağı |
| `files.igmd.org.tr` | ✅ Erişildi | GGM Menşe Kontrol Tablosu PDF'i (T3 host) |

Bu, TUR 1'deki "TGTC taranmış görüntü" ve TUR 1.5'teki "TÜİK erişilemedi"
kayıtlarıyla aynı türden bir sınırlamadır ve **gizlenmemiştir.**

---

## navlun-lojistik-uzmani (TUR 2)

```yaml
ajan:  navlun-lojistik-uzmani
tur:   TUR 2
tarih: 2026-08-10
not:   "Bu dosya 99-ops/acik-sorular.md'ye BASKAN tarafindan islenir. Ana dosyaya dokunmadim."
```

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

### 1. TUR 1'DEN KAPANANLAR *(şeffaflık için)*

| TUR 1 UNKNOWN # | Konu | **TUR 2 durumu** | evidence_id |
|---|---|---|---|
| 2 | California → İstanbul transit + navlun | ✅ **KAPANDI** (LCL): 20 gün, 0,505–0,574 USD/şişe | `EV-...-308`, `-309` |
| 7 | Terminal ardiye free time gün sayısı | ⚠ **KISMEN** — SafiPort 0 gün, ama `C-312` çelişkisi | `EV-...-317` |
| 8 | Ambarlı terminallerinin tarifesi | ⚠ **KISMEN** — Kumport ardiye bulundu ama `confidence: LOW` | `EV-...-318` |
| 12 | Origin THC, BAF/CAF, doc fee, ordino | ✅ **KAPANDI**: THO 287 EUR, B/L 62 EUR, ordino 2.000–5.000 TL, BAF %15–25 | `EV-...-313`, `-314`, `-325`, `-324` |
| 13 | Limandan depoya çekme ücreti | ✅ **DARALDI**: 10.000–15.000 TL (İstanbul içi, 20') | `EV-...-326` |
| 14 | Antrepo minimum süre | ✅ **KAPANDI**: 7 gün | `EV-...-327` |
| 17 | İtalya / Fransa → Türkiye transit | ⚠ **YARIM**: Fransa 12–15 gün ✅ / **İtalya UNKNOWN** ❌ | `EV-...-305`, `-304` |
| 18 | Şili → Türkiye rota yapısı | ✅ **KAPANDI**: 43–49 gün, Barcelona/Hamburg aktarmalı | `EV-...-306` |

**Ayrıca TUR 1'de sorulmamış ama TUR 2'de kapanan:**
40HC/20DV navlun oranı (**1,37–1,48**, `EV-...-328`) — TUR 1'in tek noktalı
1,54 eşiğini bir **banda** (1,39–1,82) çevirdi ve karşılaştırmayı mümkün kıldı.

---

### 2. HÂLÂ AÇIK — ÖNCELİK SIRASIYLA

| # | Soru | Neden bulunamadı | Kritik mi | Nasıl kapanır | Ticket |
|---|---|---|---|---|---|
| **U-1** | **Rota bazlı FCL navlunu (all-in kalem listesiyle)** | 14 Türkiye varışlı lane'in hiçbirinde kamuya açık FCL kotasyonu yok (`EV-...-312`); dolaylı çapalar 4–5 kat çelişiyor (`C-311`) | **CRITICAL** | 3 forwarder'dan yazılı RFQ | `T-304` |
| **U-2** | **İtalya → Türkiye navlunu (LCL ve FCL)** | Dört İtalyan limanında "0 offerings"; bulunan tek veri ters yön + 2025 | **HIGH** | Forwarder / armatör servis tarifesi | `T-312` |
| **U-3** | **İspanya dışı menşelerin origin local charge'ları** | Yalnızca Hapag-Lloyd İspanya tarifesi tarandı | **HIGH** | Menşe başına taşıyıcı local tarifesi | `T-312` |
| **U-4** | **Beklenen cam kırılma / fire oranı (%)** | Sektör hasar istatistiği kamuya açık değil | **HIGH** | Sigortacı + forwarder | `T-314` |
| **U-5** | **Bandrolleme birim maliyeti + kapasite (şişe/gün)** | Antrepo hizmet teklifi gerekiyor | **HIGH** | Antrepo işletmecisi teklifi | `T-314` |
| **U-6** | **Antrepo giriş/çıkış elleçleme (hammaliye)** | Antrepo siteleri fiyat yayınlamıyor (403) | **HIGH** | Aynı teklif | `T-314` |
| **U-7** | **Çekici + şasi darası (kg)** | Türk nakliyeci verisi kamuya açık değil; TUR 2'de de aranmadı/bulunamadı | **HIGH** | Nakliyeciden ruhsat bilgisi | `T-304` |
| **U-8** | **Terminal ardiye free time: 0 mı 5 mi** | İki T4 kaynak çelişiyor | MEDIUM | Terminal tarife PDF'i / yazılı soru | `T-313` / `C-312` |
| **U-9** | **THD ↔ terminal kapı-çıkış çift sayımı** | Taşıyıcı ve terminal ayrı tarife yayınlıyor | MEDIUM | Gerçek fatura örneği | `T-313` / `C-313` |
| **U-10** | **Kumport/Marport/Mardaş tarifelerinin doğrulanması** | PDF'lere doğrudan erişilemedi | MEDIUM | Terminal/acente | `T-313` |
| **U-11** | **Thermal liner birim maliyeti** | Hiçbir kaynakta fiyat yok (TUR 1'de de yoktu) | MEDIUM | Forwarder | `T-304` |
| **U-12** | **Türk sigortacıdan gerçek kotasyon + muafiyet** | Kotasyon gerekli | MEDIUM | Sigorta brokerı | `T-304` |
| **U-13** | **LCL konsolidasyon beklemesi (gün)** | Veri yok; lead time'a doğrudan giriyor | MEDIUM | Forwarder | `T-304` |
| **U-14** | **LCL per-CBM fiyatının 5 CBM'den 12 CBM'e doğrusal ölçeklenip ölçeklenmediği** | Flexport yalnızca 5 CBM için kotasyon veriyor | MEDIUM | Forwarder'dan 12 CBM kotasyonu | `T-304` |
| **U-15** | **Portekiz → İstanbul gerçek transit** | Kaynak "4 gün" diyor ama routing Barcelona aktarmalı → iç tutarsız | MEDIUM | Armatör servis tarifesi | `T-312` |
| **U-16** | **Şarap "Food Quality Container" (115 EUR) gerektirir mi** | Taşıyıcı tarifesinde kalem var, zorunluluğu belirsiz | LOW | Forwarder / tedarikçi | `T-312` |
| **U-17** | **Veteriner/fitosaniter kontrol (126 USD/BL) şarapta uygulanır mı** | Mevzuat alanı | LOW | `mevzuat-ruhsat-uzmani` (İP-2312) | — |
| **U-18** | **Depolama (serbest dolaşım sonrası) m²/palet maliyeti** | Teklif gerekiyor | MEDIUM | Depo işletmecisi | `T-314` |
| **U-19** | **Depodan kanala dağıtım (şişe başı)** | Kanal modeli belirsiz | MEDIUM | `kanal-marj-uzmani` ile birlikte | — |
| **U-20** | **FX kuru (USD/TRY, EUR/TRY) ve kur tarihi** | `makro.yaml` boş; benim alanım değil | **HIGH** | `finans-fizibilite` | `T-311` |
| **U-21** | **Ruhsat/bandrol bekleme süresi (gün)** | Mevzuat alanı | **CRITICAL** | `mevzuat-ruhsat-uzmani` | `T-301` |
| **U-22** | **Toplam lead time** | U-13 + U-21 + gümrükleme + üretim süresinden türetilir | **CRITICAL** | `T-301` + `T-304` + sourcing | — |
| **U-23** | Tedarikçinin gerçek koli/palet spec'i | Tedarikçi seçilmedi | HIGH | RFQ spec sheet | `T-302` |
| **U-24** | Paletsiz yüklemede yeniden paletleme maliyeti | Veri yok (TUR 1'de de yoktu) | MEDIUM | Antrepo teklifi | `T-314` |
| **U-25** | Diğer armatörlerin (MSC/CMA CGM/Arkas) D&D free time'ı | Sayfalar erişilemedi | MEDIUM | Armatör local info | `T-313` |

---

### 3. BU TURDA DENENİP BAŞARISIZ OLAN YOLLAR *(tekrar denenmesin diye)*

| # | Denenen | Sonuç |
|---|---|---|
| 1 | Flexport Rate Explorer — **FCL**, 14 farklı Türkiye lane'i | Hepsinde "0 offerings" |
| 2 | Flexport — İtalya (ITGOA, ITSPE, ITLIV, ITNAP) → İstanbul | Hepsinde "0 offerings", LCL dahil |
| 3 | Flexport — Valencia → **Mersin** | "0 offerings" (yalnızca İstanbul lane'leri kotasyonlanıyor) |
| 4 | Freightos route sayfaları | 302 redirect → `ship.freightos.com` (giriş gerekli) |
| 5 | SeaRates `/routes/` | 403 |
| 6 | Globy freight calculator (Türkiye ve Valencia→İstanbul) | 403 |
| 7 | Hapag-Lloyd Türkiye import charges **web formu** | 403 — **ama PDF tarifesi bulundu ve çalıştı** ✅ |
| 8 | Kumport tarife sayfası | Yalnızca başlıklar; PDF'lere erişilemedi |
| 9 | FixAntrepo 2026 fiyat sayfası | 403 — değerler yalnızca arama özetinden |
| 10 | Erciyes Lojistik 2026 konteyner fiyatları | 403 |
| 11 | Suaid Global 2026 navlun tabloları | Akdeniz / Türkiye rotaları **yok** |
| 12 | MoverDB konteyner fiyat tablosu | Veri **2023 sonu**, Türkiye satırı yok |
| 13 | Nakliyerehberim rota fiyatları (İspanya, Şili) | Yalnızca **Türkiye çıkışlı** (ihracat) satırlar |

> **Kalıp:** Türkiye **ithalat** yönü için kamuya açık FCL fiyatı sistematik
> olarak yayınlanmıyor. Türkiye **ihracat** yönü için yayınlanıyor. Bu bir
> arama başarısızlığı değil, **piyasa yapısı**dır: Türk forwarder'ları ihracat
> odaklı fiyat yayınlıyor; ithalat fiyatı yabancı taraftan geliyor ve
> kotasyona bağlı.

---

### 4. AÇIK SORULARIN GATE ETKİSİ

| Gate | Sahibi | Bu turdan sonra |
|---|---|---|
| **G2-L** — L1→L2→L3 geçişi kanıtla kurulabiliyor mu? | `navlun-lojistik-uzmani` | **BLOCKED — değişmedi.** Açan tek koşul (`T-304`: 3 forwarder kotasyonu) karşılanmadı. **Ama kapsamı daraldı:** L2→L3 geçişinin masraf kalemleri artık büyük ölçüde biliniyor; kilitli olan yalnızca **L1→L2 (ocean freight)**. |

**G2-L'nin bugünkü tam durumu:**

```
L1 (FOB)  →  L2 (CIF)   : ocean freight UNKNOWN (band 4 kat)  ❌  ← TEK KİLİT
                           origin locals BİLİNİYOR (İspanya)   ✅
                           sigorta ESTIMATE (%0,3–0,6)         ⚠
L2 (CIF)  →  L3 (pre-tax landed) : THD BİLİNİYOR              ✅
                                   ardiye BİLİNİYOR             ✅
                                   ordino BİLİNİYOR             ✅
                                   müşavirlik BİLİNİYOR         ✅
                                   iç nakliye DARALDI           ⚠
                                   antrepo bekleme UNKNOWN      ❌ (T-301)
                                   bandrolleme UNKNOWN          ❌ (T-314)
```

---

## global-sourcing-kasifi (TUR 2)

> `99-ops/acik-sorular.md` dosyasına **DOKUNULMAMIŞTIR** (başkan birleştirir).
> **UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

### A. YALNIZCA GERÇEK RFQ İLE ÖĞRENİLEBİLECEK ALANLAR

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

### B. AÇIK SORULAR (RFQ dışı yollarla da kapanabilecekler)

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

### C. TUR 1'DEN DEVREDEN VE HÂLÂ AÇIK OLANLAR

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

---

## turkiye-pazar-kasifi (TUR 2)

> Ana dosyaya (`99-ops/acik-sorular.md`) **başkan** merge eder.

---

### OQ-551 — İthalatçı kodlarının 13/17'sinin karşılığı kim?

```yaml
id:          OQ-551
opened_by:   turkiye-pazar-kasifi
opened_date: 2026-08-10
status:      OPEN
impact:      MEDIUM
evidence:    EV-2026-08-10-557
```

**Soru:** Perakendeci feed'indeki şu kodların hangi tüzel kişiye karşılık geldiği
doğrulanmadı: `LUCE`, `frosta`, `Midas`, `demglobal`, `Future`, `MALTİTHAL`,
`küregıdaithal`, `ADT`, `piramitgıda`, `PiyasaGıda`, `INANC`, `Vinist`, `Nadiya`.

Doğrulananlar: `KVKLDR` = Kavaklıdere (FACT), `KDT` = Karagözoğlu Dış Ticaret (FACT),
`ADCO` = Adco Gıda (kimlik FACT, portföy ESTIMATE), `BRN` = Baron Şarapçılık (ESTIMATE).

**Neden açık:** Bandımıza en yakın markaları taşıyan kodlar (`PiyasaGıda`,
`piramitgıda`, `Vinist`, `frosta`) tam da **çözülemeyenler** arasında.

**Nasıl kapanır:** (a) Üretici sitelerinin "distributors" sayfaları (Antinori
yöntemi — çalışıyor); (b) şişe arka etiketinde ithalatçı satırının fiziksel
gözlemi; (c) TADAB belge sahipleri listesi (`T-564`).

**Alt soru (çelişki izi):** J.P. Chenet'yi Baron Şarapçılık mı getiriyor, yoksa
`interaytrading.com` mu? İkisi de sitesinde bu markayı gösteriyor. Çelişki kaydı
**açılmadı** çünkü ikisi de T5/zayıf ve modele girmiyor.

---

### OQ-552 — 500–1.000 TL bandı "boş" mu, "stoksuz" mu?

```yaml
id:          OQ-552
opened_by:   turkiye-pazar-kasifi
opened_date: 2026-08-10
status:      OPEN
impact:      HIGH
evidence:    EV-2026-08-10-551, EV-2026-08-10-552
ticket:      T-561
```

**Soru:** İncelenen kanalda bu bantta **62 ithal ürün tanımlı** ama **0 tanesi
stokta**. Bu:

- **(a)** Bu ürünlerin Türkiye'de artık satılmadığı anlamına mı geliyor?
- **(b)** Yoksa bu perakendecinin bu bandı **kasten taşımadığı** (düşük marj /
  düşük ortalama sepet) anlamına mı geliyor?
- **(c)** Yoksa bunlar başka kanallarda (Metro, tekel bayii, zincir market)
  **normal olarak satılıyor** ve sadece bu online kanalda mı yok?

**Neden kritik:** (a) ise hedef bandımızda talep sorunu vardır → `KILL` yönü.
(b) veya (c) ise bandımız sağlamdır ve gözlem aracımız yanlıştır → yalnızca
**kanal seçimi** sorunudur.

**Nasıl kapanır:** Fiziksel mağaza turu. Aranacak somut SKU listesi hazır:
Santa Helena 677 · M. Chapoutier Belleruche 680 · Hans Baer Pinot Noir 702 ·
Henkell 746 · Terra Mater Reserve 770 · Botter Caleo 838 · Luccarelli Primitivo 864 ·
Barone Montalto 950 · La Vieille Ferme 979 · Alpaca 429 · Imperial Vin 512.
Bu isimlerin Metro / Migros / tekel bayii rafında **var olup olmadığı ve fiyatı**,
`OQ-502` ile aynı ziyarette toplanabilir.

---

### OQ-553 — Kısa listedeki üreticiler Türkiye'ye daha önce ihracat yaptı mı?

```yaml
id:          OQ-553
opened_by:   turkiye-pazar-kasifi
opened_date: 2026-08-10
status:      OPEN
impact:      MEDIUM
evidence:    EV-2026-08-10-553
ticket:      T-562
```

**Soru:** 26 tedarikçinin 25'inin ürünü Türkiye'de bulunamadı. Ama private label
üreticileri için bu **beklenen** sonuçtur. Doğru soru: *"Türkiye'ye daha önce
ihracat yaptınız mı, kime, ne zaman, ne hacimde?"*

`tedarikci-havuzu.csv → exported_to_turkey_before` alanı **11/11 satırda UNKNOWN**;
`supplier-shortlist-v2.csv → turkey_export_experience` alanı da **26/26 satırda
UNKNOWN** (bir satırda "ABD-TR hattı fiilen yok" notu var, ama tedarikçi düzeyinde
cevap değil).

**TUR 2'nin somut katkısı:** `SUP-452` Cantina Danese için cevap artık kısmen
biliniyor — **Türkiye'de kendi markasıyla listelidir** (`EV-2026-08-10-564`).
Yani en az bir tedarikçide `turkey_export_experience` `UNKNOWN` olmamalıdır.

**Nasıl kapanır:** RFQ (`global-sourcing-kasifi`, `T-562` + `T-565`). Masabaşından
kapanmaz: ticari veri sağlayıcıları (volza, exportgenius) bu oturumda **403** döndü.

---

### DEVREDEN AÇIK SORULAR — TUR 2'DE ELE ALINMADI

| id | Konu | TUR 2 notu |
|---|---|---|
| `OQ-001` | Benchmark KDV / promosyon | **Kasten ele alınmadı** — TUR 2 kapsam sınırı (`T-504` açık, fiziksel gözlem gerektiriyor) |
| `OQ-502` | Zincir market / tekel bayii raf fiyatı | Kapanmadı. `OQ-552` ile **aynı ziyarette** kapanabilir hâle geldi |
| `OQ-503` | Gold Country / Central Creek ithalatçısı | Kapanmadı. "Gold Country" markasının üretici/sahibi de bulunamadı |
| `T-505` | Resmî ithalat hacmi + ithalatçı listesi | Kapanmadı; `T-564` ile somut isim listesi eklendi |

---

## kanal-marj-uzmani (TUR 2)

> Bu bir **parça dosyasıdır**. `99-ops/acik-sorular.md` ana dosyasına
> `yatirim-komitesi-baskani` tarafından birleştirilir. Bu ajan ana dosyaya
> **DOKUNMAMIŞTIR**.
>
> Ticket'a dönüşmeyen, ama kapanmadan modelin güvenilir olmayacağı sorular.

---

| # | Soru | Neden açık kaldı | Kritiklik | Nasıl kapanır |
|---|---|---|---|---|
| **OQ-601** | Türkiye'de zincir marketin **şarap kategorisi** brüt marjı nedir? | Rekabet Kurumu'nun beş büyük zincir analizi **"alkol ve tütün hariç"** tanımlıdır ve yayımlanan tüm marj oranları **ticari sır olarak karartılmıştır** (`EV-2026-08-10-611`) | **CRITICAL** | Yalnızca gerçek yıllık anlaşma müzakeresi (`T-604`) |
| **OQ-602** | Şarapta zincir **listeleme / giriş bedeli** tutarı nedir ve birimi nedir (SKU mu, mağaza mı, zincir mi)? | Güncel kamu kaynağı yok; tek iz 2004 tarihli T5 dergi haberi (`EV-2026-08-10-619`) | **CRITICAL** | `T-604` |
| **OQ-603** | HoReCa çarpanı hangi katmandan hesaplanır ve gerçek değeri nedir? | Tek kaynak 2012 tarihli köşe yazısı ve **kendi içinde iki farklı katman** verir (`EV-2026-08-10-618`, `C-602`) | HIGH | Gerçek restoran menü örneklemi (fiziksel) + HoReCa görüşmesi |
| **OQ-604** | Tekel bayii alış-satış farkı nedir? | Yalnızca çelişen T5 kaynaklar; hiçbiri margin/markup ve KDV tabanını belirtmiyor (`EV-2026-08-10-620`, `C-602`) | HIGH | Gerçek bayi görüşmesi / gerçek fiyat listesi |
| **OQ-605** | Dış distribütör marj oranı nedir? | **Hiçbir kanıt bulunamadı.** Ne T4 ne T5. | **CRITICAL** | Distribütör görüşmesi (`T-604`) — A/B dağıtım kararı bunsuz verilemez |
| **OQ-606** | Şarapta zincir **iade oranı** ve iade koşulları nedir? | Yasal düzenleme yok (`EV-2026-08-10-606`); tamamen sözleşmesel | HIGH | `T-604` |
| **OQ-607** | Kaç satış noktası, rakiplerin **5 yıllık şarap alım sözleşmeleri** ile bağlı? | Rekabet Kurulu kararındaki sözleşme sayısı tabloları **karartılmış** (`EV-2026-08-10-614`) | HIGH | Saha gözlemi / bayi görüşmesi. **Bu, listeleme bedelinden daha ölümcül bir erişim engeli olabilir.** |
| **OQ-608** | Zincirlerin şaraba ayırdığı **raf/SKU kotası** nedir? | Hiçbir kamu kaynağı yok. `EV-2026-08-10-624`: ithalat, iç piyasa şarap arzının **%4'ü** (2020, TADB) → ithal şaraba ayrılan raf da dar olmalı, ama **ölçülmedi** | MEDIUM | Fiziksel mağaza turu (`T-603` ile birlikte) |
| **OQ-609** | Zincir market **modern kanal** nokta sayısı (alkol satan) kaçtır? | TADB tablosunda modern kanal **kasten yoktur** (merkezi alım) (`EV-2026-08-10-613`) | MEDIUM | TADAB satış belgesi listeleri / zincirlerin kendi beyanı |
| **OQ-610** | Şarap, 6585 m.7/3 anlamında "tarım ve gıda ürünü" müdür? | Hukuki niteleme bu ajanın alanı değil | **CRITICAL** | `T-601` (`mevzuat-ruhsat-uzmani`) |
| **OQ-611** | 2015'teki "prim/bedele konu ürün sözleşme süresince rafta satışa sunulmalıdır" koruması 2024 metninde var mı? | Konsolide metinde görünmüyor ama **T1 doğrulaması yapılamadı** (`EV-2026-08-10-622`) | HIGH | `T-601` |
| **OQ-612** | Metro **mağaza fiyatı** ile **sevkiyat (Gastro Servis) fiyatı** arasındaki fark nedir? | `İP-501` / `T-506`; Metro fiyatları müşteri numarasına özel (`İP-505`) | HIGH | Metro müşteri kaydı + gerçek teklif (`T-604`) |
| **OQ-613** | HoReCa'da **tadım / eğitim etkinliği** kanal maliyeti olarak modellenebilir mi? | Kabul edilmiş iş kısıtının (`İP-2001`) kapsam belirsizliği; **bu ajan kısıtı yeniden araştırmamıştır** (kurucu kararı) | MEDIUM | Başkan kararı (`T-604` içinde soruldu) — modelleme kararıdır, hukuki soru değildir |
| **OQ-614** | Satış temsilcisi ücret çarpanı (× asgari ücret), araç maliyeti, 3PL birim fiyatı? | Şirket verisi ve gerçek teklif gerektirir | HIGH | Kurucu + 3PL teklifleri (`kendi-dagitim-senaryosu.md` §11) |
| **OQ-615** | Şarabın kanal bazında **ciro dağılımı** (zincir / tekel / HoReCa) nedir? | Kamuya açık veri bulunamadı; elde yalnızca **nokta sayısı** var ve nokta sayısı ciro payı değildir | **CRITICAL** | `T-603` — **ağırlıklı ortalama marj bu olmadan hesaplanamaz** |

---

### Bu turda BİLİNÇLİ OLARAK YAPILMAYANLAR

- 7584 s.K. / reklam kısıtının **kapsamı yeniden araştırılmadı** (kurucu kararı,
  `T-205`, `İP-2001`). Kısıt bir **veri** olarak kullanıldı.
- Hiçbir perakendeciye, distribütöre, HoReCa işletmesine **e-posta / form / mesaj
  gönderilmedi** (görev kısıtı).
- Vergi oranı, navlun tutarı, ruhsat prosedürü, tedarikçi fiyatı konularında
  **sonuç üretilmedi**.
- `599,90 TL`'den **geriye marj türetilmedi** (`pazar.yaml` K2/K4).
- `pazar.yaml`, `10-evidence/index.csv`, `99-ops/*.md` ana dosyaları,
  `99-ops/tickets/INDEX.md` ve diğer ajanların yaml dosyalarına **dokunulmadı**.
- `T-205`'in statüsü **değiştirilmedi**; yalnızca sonuna bir **kullanım kaydı** eklendi.

---

---

# TUR 2 KONSOLİDASYONU — BAŞKAN TARAFINDAN AÇILAN SORULAR

```yaml
acan:    yatirim-komitesi-baskani
tarih:   2026-08-10
belge:   90-karar/tur-2-konsolidasyon.md §5.2
not:     "Bu sorular ARASTIRMA sonucu degildir; iki ajanin ciktisinin kesistigi
          ve hicbirinin sahiplenmedigi bosluklardir."
```

---

## OQ-911 — Antrepo / bandrolleme tesisi nerede olacak?

| Alan | İçerik |
|---|---|
| **Soru** | Bandrolleme ve antrepo operasyonu **hangi şehirde/limanda** yapılacak? Bu belirlenmeden **varış limanı seçilemez.** |
| **Sahibi** | **kurucu / yatırımcı** *(+ `navlun-lojistik-uzmani` maliyet tarafı)* |
| **Neden açıldı** | `EV-2026-08-10-332` (varış limanı kuralı) bir **büyüklük mertebesi karşılaştırması** yapmış ve şu sonuca varmıştır: varış limanı **terminal tarifesine göre değil**, **antrepo/bandrolleme tesisinin ve hedef pazarın yerine göre** seçilir. Ama o tesisin yeri **hiçbir yerde tanımlı değildir.** |
| **Sayısal kaldıraç** | THD farkı (İzmir 165 ↔ Mersin 40' 298 USD) = **max 133 USD/konteyner = 0,006–0,011 USD/şişe**. İç nakliye farkı (Ambarlı→İzmir 37.500 TL) = **2,7–3,2 TRY/şişe**. **~2 kat mertebe farkı.** |
| **Neyi kilitliyor** | (1) `lojistik.yaml → ic_lojistik.*` — TRY bacağının **en büyük tek kalemi**; (2) `C-312`'nin hangi terminalin tarifesine göre okunacağı (**bu turda `RESOLVED — KAPSAM`**: free time terminale özgüdür); (3) `T-313`'ün hedefi; (4) bandrolleme kapasitesi ve süresi (`T-314`, `T-301`) |
| **Nasıl kapanır** | Yatırımcı beyanı veya 2–3 antrepo/3PL teklifi. **Araştırmayla kapanmaz.** |
| **Kritik mi** | **HIGH** — modeli bloke etmez ama TRY bacağının en büyük kalemini belirsiz bırakır |

---

## OQ-912 — TUR 3 hangi tarihte çalıştırılacak?

| Alan | İçerik |
|---|---|
| **Soru** | Finans modeli **hangi tarihte** çalıştırılacak? Projenin kanıt tabanı **dar bir tazelik penceresi** içindedir ve bu soru şimdiye kadar **hiç sorulmamıştır.** |
| **Sahibi** | **`yatirim-komitesi-baskani`** *(karar)* |
| **Tazelik penceresi** | `EV-2026-08-10-301…311` (**11 LCL kotasyonu**, `ttl: 6d`) → **2026-08-16** · `EV-2026-08-10-312`, `-322`, `-323`, `-324`, `-329`, `-330`, `-331` (`ttl: 14d`) → **2026-08-24** · `EV-2026-08-09-111` (**ÖTV 71,2692 TL/lt**, `ttl: 30d`) → **2026-09-08** |
| **Neden önemli** | **2026-08-16'dan sonra** çalıştırılan bir model, **projedeki tek gerçek navlun verisini bayatlatarak** çalışır: 9 rotanın navlun bacağı `UNKNOWN`'a döner, `T-304`'ün LCL ayağı **yeniden açılır** ve LCL/FCL kırılma noktası hesabının **kanıtlı tarafı da** kaybolur. **2026-09-08'den sonra** ÖTV serisi yeniden doğrulanmalıdır. |
| **İkinci sıra etkisi** | Model bayat girdiyle çalışırsa `seytanin-avukati` TUR 4'te **haklı olarak** tüm çıktıyı reddedebilir. |
| **Nasıl kapanır** | Başkan kararı: **(a)** TUR 3'ü 2026-08-16'dan önce çalıştır, **(b)** `T-913` ile kotasyonları yeniden doğrulat, veya **(c)** navlun bacağını bilinçli olarak `UNKNOWN` kabul ederek çalıştır ve bunu çıktıda **açıkça yaz.** |
| **Kritik mi** | **HIGH** — bir zamanlama kararıdır, bir veri eksiği değildir |

---

## TUR 2 KONSOLİDASYONUNDA KAYDA GEÇİRİLEN — YATIRIMCI GİRDİSİ BEKLEYEN İKİ SORU

Bu ikisi **yeni değildir**, ama TUR 3/TUR 6 blokeri oldukları için burada
tekrar işaretlenir:

| id | Soru | Sahibi | Neyi bloke ediyor |
|---|---|---|---|
| **`OQ-002`** | ~~`model_hedef_tarihi` **`null`**~~ → **2026-08-10: `INPUT_RECORDED`** (`2027-04-01`, `INVESTOR_ASSUMPTION`) | **yatırımcı** | **TUR 3 blokeri KALKMADI, YER DEĞİŞTİRDİ.** Tarih artık dolu; ama üç senaryonun üçü de `2026-12-31` ufkunun ötesinde ve engine seriyi **hiç okumuyor** → **`T-921` (CRITICAL)** |
| **`OQ-901`** | `00-charter/karar-esikleri.md`'deki karar eşiklerinin **tamamı `TBD`** | **yatırımcı** | **TUR 6** — eşik yoksa "yeterli mi?" sorusu cevaplanamaz. **Araştırmayla kapanmaz.** |

---

## TUR 2.5 PRE-FLIGHT — AÇIK SORU DURUMU DEĞİŞİKLİKLERİ (2026-08-10)

| id | Önce | Sonra | Not |
|---|---|---|---|
| **`OQ-002`** | `OPEN` | **`INPUT_RECORDED`** | Yatırımcı girdisi kaydedildi; **kapanmadı** (gerekçe yukarıda, §OQ-002 güncellemesi) |
| **`OQ-G08`** | `OPEN` | **`OPEN` — DEĞİŞMEDİ** | Sorunun kendisi *"hedef tarihte hangi ÖTV tutarı geçerli olacak"*tır. Tarih girildi, **tutar hâlâ `UNKNOWN`**. Bu soru tarih girilerek kapanmaz |
| **`OQ-912`** | `OPEN` | **`OPEN` — KISMEN CEVAPLANDI** | Model çalıştırma tarihi: **2026-08-16'dan önce**. Gerekçe: 10 canlı LCL kotasyonu o gün STALE olur (**6 gün kaldı**). Kart sayısı düzeltmesi: 11 değil **10** → `T-923` |
| **`OQ-901`** | `OPEN` | **`OPEN` — DEĞİŞMEDİ** | Karar eşikleri `TBD`; TUR 6 blokeri. Bu turda **ele alınmadı** |

---
---

# TUR 2.5 KAPANIŞ — AÇIK SORU DURUMU (2026-08-10)

```yaml
yazan:  yatirim-komitesi-baskani
tarih:  2026-08-10
belge:  90-karar/tur-25-konsolidasyon.md
not:    "Hicbir orijinal soru metni silinmemis veya degistirilmemistir."
```

## OQ-901 — **`OPEN — SPECIFIED`** (KAPATILMADI)

```yaml
oq_id:              OQ-901
onceki_durum:       OPEN
yeni_durum:         OPEN — SPECIFIED       # KAPATILMADI
guncelleme:         2026-08-10 (TUR 2.5 kapanis)
sahibi:             YATIRIMCI              # degismedi — hicbir ajan kapatamaz
impact:             CRITICAL               # degismedi
ana_belge:          90-karar/investor-decisions-required.md
kapsam_degisikligi: "6 finansal esik -> 16 esik (D-01...D-16)
                     + 8 esik disi yatirimci girdisi (I-1...I-8)"
bloke_ettigi:       "TUR 3B (ileri model)  +  TUR 6 (nihai karar)"
ilgili_ticket:      [T-851, T-852, T-912, T-604, T-857, T-859, T-944, T-467, T-304]
```

### Neden kapatılmadı

`OQ-901` bir **soru**dur, bir belge değil. `investor-decisions-required.md`
soruyu **görünür ve cevaplanabilir** hâle getirir; **cevaplamaz.**
**Hiçbir ajan — başkan dahil — `OQ-901`'i kapatamaz.**

### Bu turda ne değişti

| # | Değişiklik |
|---|---|
| **1** | Eşikler **6'dan 16'ya** çıktı. Yeni 10 eşiğin hiçbiri başkanın icadı değildir; hepsi ajan raporlarında **modelin duraksadığı noktalar** olarak zaten kayıtlıdır |
| **2** | Her eşik için **hangi katmanlar arasında** tanımlanması gerektiği yazıldı. `00-charter/karar-esikleri.md`'nin açık bıraktığı *"L5→L6 mı, L5→L8 mi?"* sorusu, verinin gösterdiği **üçüncü seçenekle** (`L5 → L7_eff`) birlikte kayda geçti |
| **3** | **Eşik dışı yatırımcı girdileri ayrı bölümde toplandı** (`I-1`…`I-8`): `fx`, `model_hedef_tarihi`, ÖTV `λ` varsayımı, **dış temas izni**, antrepo/bandrolleme tesisi yeri, finansman maliyeti, iş modeli önceliği, çalıştırma tarihi |
| **4** | **`fx` bir eşik DEĞİLDİR** — bir kayıttır ve üç turdur bekliyor (`T-852`, `T-912`) |
| **5** | **Dış temas izni (`T-467`, `T-304`) bir VERİ EKSİKLİĞİ DEĞİLDİR** — bir izin ve zamanlama sorunudur. `G2` ve `G2-L`, *"tedarik kaynağı yok"* diye değil, **"henüz sorulmadı"** diye kapalıdır |
| **6** | **`bloke_ettigi` genişledi:** artık yalnız TUR 6'yı değil, **TUR 3B'yi** (ileri model) de bloke ediyor. Sebep: modelin **en büyük iki belirsizlik ekseni** bir veri değil, bir **karar** eksikliğidir (her biri 0→%30 aralığında **−108,56 TL/şişe**) |
| **7** | `finans-fizibilite`'nin `TARGET`/`ACCEPTABLE`/`WALK-AWAY` fiyatlarını **üretmeme** kararı **onaylandı** — keyfî yüzdelerle üretmek *"modelin en sinsi uydurma noktası"* olurdu |

### Kapanış koşulu

`investor-decisions-required.md` §6'daki **MİNİMUM AÇILIŞ SETİ**'nin
cevaplanması **VEYA** her eşik için *"belirlemiyorum"* beyanı **ve** o
beyanın sonucunun kabulü.

Minimum set: **`I-1` (fx)** · **`D-03` (μ + matrahı)** · **`D-01` (brüt marj +
katman çifti)** · **`D-05` (sermaye tavanı)** · **`I-4` (dış temas izni)** ·
**`D-14` (PRIMARY basamak)**

### Kayıtlı tuzak — değişmedi ve güçlendi

Charter eşiklerin **TUR 3 sonrası** belirlenmesini önerir; bu **sonuca göre
eşik ayarlama (hedef kaydırma)** riski taşır. `investor-decisions-required.md`
tam da bu riski azaltmak için eşiklerin **ileri model çıktısından önce**
yazılmasını mümkün kılar.

> **Ama bu bir ödünleşmedir, bir üstünlük değildir:** önce yazılan eşik
> **bilgisiz** olabilir ve gerçekçi olmayan bir tabanı sabitleyerek projeyi
> **haksız yere öldürebilir.** Hangisinin seçildiği `karar-gunlugu.md`'ye
> yazılmalı ve `seytanin-avukati` TUR 4'te bunu bir saldırı vektörü olarak
> kullanmalıdır.

---

## DİĞER AÇIK SORULARIN TUR 2.5 KAPANIŞ DURUMU

| id | Önce | **Sonra** | Not |
|---|---|---|---|
| **`OQ-001`** | `PARTIALLY_RESOLVED` | **DEĞİŞMEDİ** | Promosyon ayağı (`T-504`) açık → **`G3` geçilemez.** TUR 2.5'te `OBSERVED_BENCHMARK` **hiç kullanılmadı**; `TARGET` merdiveni onun **yerine geçmez** (`K7`) |
| **`OQ-002`** | `INPUT_RECORDED` | **DEĞİŞMEDİ** | Kapanış iki koşula bağlıydı: `T-921` `RESOLVED` **VE** tarihin `t0-takvimi`nden doğrulanması. **Birincisi bu turda gerçekleşti** (`T-921` → `RESOLVED`); **ikincisi olmadı** (`T-202`/`C-202` açık) → **`OQ-002` AÇIK KALIR** |
| **`OQ-G08`** | `OPEN` | **DEĞİŞMEDİ** | *"Hedef tarihte hangi ÖTV tutarı geçerli olacak"* — üç hedef tarihin üçü de `2026-12-31` ufkunun ötesinde. `T-921` kapandı ama **tutar hâlâ `FUTURE_UNKNOWN`**. Bu soru tarih girilerek veya engine düzeltilerek **kapanmaz** |
| **`OQ-G10`** | `OPEN` | ⚠ **YÜKSELTİLDİ — `T-947` (CRITICAL) açıldı** | KDVK md.36 CB kararı **üç turdur aranmamıştır.** Varsa ters modelin **TÜM sayıları ~%22,7 düşer.** **TUR 3A'nın birinci işi.** Etki değerlendirmesi başkanın değil, **`finans-fizibilite`'nin** türetmesidir |
| **`OQ-502`** | `OPEN` | **DEĞİŞMEDİ** | Fiziksel mağaza gözlemi — `C-501`, `C-551`, `T-504`, `T-603` ile birlikte **tek eylemle** kapanır (`T-917`). **Üç turdur yapılmadı** |
| **`OQ-902`** | `OPEN` | **DEĞİŞMEDİ** *(→ `I-7`)* | İki iş modeli eşit derinlikte araştırılamadı. Yatırımcının bu önceliği koruyup korumadığı **`investor-decisions-required.md` `I-7`**'de kayıtlı |
| **`OQ-911`** | `OPEN` | **DEĞİŞMEDİ** *(→ `I-5`)* | Antrepo/bandrolleme tesisinin yeri. TRY bacağının **en büyük tek kalemini** belirsiz bırakıyor |
| **`OQ-912`** | `OPEN — KISMEN CEVAPLANDI` | ✅ **TUR 2.5 İÇİN CEVAPLANDI** | Model **2026-08-10'da** koşuldu → `P-3` **sağlandı**, LCL bacağı çalıştırma anında **kanıtlıydı**. ⚠ **Ama soru TUR 3A/3B için YENİDEN AÇILIR:** yeni bir **`P-3b`** kapısı konmuştur (`tur-25-konsolidasyon.md` §5) — **2026-08-16'dan sonra** çalıştırılırsa ya `T-913` ile kotasyonlar yenilenir, ya da lojistik bacağı bilinçli olarak `ESTIMATE/LOW`'a düşürülüp **çıktıda açıkça yazılır.** Sessizce bayat veriyle koşmak **yasaktır** |

---

# TUR 2.5 AÇIK SORULARI

> Ajanların `99-ops/_parts/*-tur25.md` fragment'lerinden değiştirilmeden aktarıldı.

## gumruk-vergi-uzmani (TUR 2.5)

> Bu tur **sınırlı bir model destek turudur**; yeni genel araştırma yapılmamıştır.
> Aşağıdakiler ters modelin vergi bacağı kurulurken **açık kalan** veya
> **yeni görünür hâle gelen** sorulardır. Devralınan açık sorular
> (`…-tur15.md`, `…-tur2.md`) burada tekrarlanmamıştır.

---

### OQ-G25-01 — `λ` (2027 ÖTV artış katsayısı) kim tarafından, nerede tanımlanacak?

**Kritiklik:** HIGH · **Bloke ettiği:** üç hedef tarih senaryosunun birbirinden
ayrışması

ÖTV, ÖTVK md.12/3 uyarınca Ocak ve Temmuz'da Yİ-ÜFE ile **kendiliğinden**
yeniden belirlenir (`EV-2026-08-09-114`). Üç hedef tarihin (2027-01-01 /
2027-04-01 / 2027-07-01) **üçü de** en az bir ayarlamanın ötesindedir.

`vergi.yaml → BASE_DATE_kurali` gelecek değer yazılmasını **yasaklar** ve bu
doğrudur. Ancak sonuç şudur: **üç senaryo da `λ=1` ile çalışacağı için ÖTV
açısından birbirinden ayrışmayacaktır.** Hedef tarih seçiminin ÖTV etkisi model
çıktısında **görünmeyecektir.**

**Kim cevaplamalı:** `yatirim-komitesi-baskani` (karar) + `finans-fizibilite`
(`makro.yaml`'da Yİ-ÜFE `ASSUMPTION`'ı, `senaryolar.yaml`'da duyarlılık ekseni).
**`gumruk-vergi-uzmani` bu sayıyı vermez ve veremez.**

---

### OQ-G25-02 — `g` (gümrük vergisi oranı) için neden ÖTV ile aynı titizlik uygulanmıyor?

**Kritiklik:** HIGH · **Tip:** metodolojik asimetri itirafı

`g = 0,50 / 0,70` değerleri **2026 İthalat Rejimi Kararı**'na aittir
(`effective_date: 2026-01-01`, `ttl: 90d`). Karar **her yıl 1 Ocak'ta
yenilenir.** Üç hedef tarihin üçü de **2027'dedir.**

Yani `g`, ÖTV ile **tamamen aynı yapısal durumdadır** ama:
- ÖTV için `otv_maktu_zaman_serisi` + `gelecek_deger_kurali` + `son_gozlem_gecerlilik_ufku` var,
- `g` için **hiçbiri yok** — model `0,50`'yi 2027'de de geçerli sayacak.

Bu bir çelişki değil, **kabul edilmiş bir tutarsızlıktır** ve gizlenmemiştir
(`ters-model-vergi-bacagi.md` §13.1, `rapor-tur25` §4).

**Neden bu turda kapatılmadı:** 2027 Kararı henüz **yayımlanmamıştır**
(2026 Aralık'ta beklenir). Yani `g` için doğrulanmış bir 2027 değeri **fiziksel
olarak mevcut değildir**. Yapılabilecek tek şey `g`'ye de bir
`gecerlilik_ufku: 2026-12-31` alanı eklemektir.

**Öneri (karar başkanındır):** `mense_tarife_eslemesi` bloğuna
`son_gozlem_gecerlilik_ufku: 2026-12-31` eklenmesi ve engine'in
`t > 2026-12-31` iken `g`'yi de `UPPER_BOUND`/`ANCHOR` etiketiyle raporlaması.
**Tarihsel yön ipucu yok:** oranların 2027'de artacağını da azalacağını da
gösteren bir kanıt bulunmamaktadır → yön bile `UNKNOWN`'dır.

---

### OQ-G25-03 — `X_pre` gerçekten sıfır mı? (damga vergisi ve md.21/c'nin idari yorumu)

**Kritiklik:** LOW (tutar) / MEDIUM (yöntem) · **Ticket:** `T-151`

Ters modelin R7 adımı `X_pre = 0` varsayar. Türetme: tescile kadarki tüm yurt
içi kalemler KDV'ye tabidir → md.21/c'nin "vergilendirilmeyenler" şartını
sağlamazlar (`EV-2026-08-10-108`).

**İki açık nokta:**
1. **Gümrük beyannamesi damga vergisi** md.21/b uyarınca KDV matrahına **girer**;
   tutarı `UNKNOWN`'dır (beyanname başına maktu → şişe başına ihmal edilebilir).
2. md.21/c'nin **idari yorumu (KDVGUT III/A)** okunmamıştır (`T-151`).

**En ucuz kapanış:** tek bir gerçekleşmiş gümrük beyannamesinde KDV matrahı
satırının `CIF + GV + ÖTV` toplamına **eşit** olup olmadığının gözlenmesi.
Bu, `master-commercial-input-table.md` §7'nin işaret ettiği yolla **aynı**dır.

---

### OQ-G25-04 — `T-911` (gümrük kuru) bu turda kapatılmadı

**Kritiklik:** HIGH · **Ticket:** `T-911` (OPEN, target: bu ajan)

Ters model `CIF_TRY_max` ve `FOB_TRY_max` üretebilir ama **döviz cinsinden
azami satın alma fiyatını üretemez.** Bunun için iki ayrı şey gerekir:
- `makro.yaml → fx` (`T-912`, `finans-fizibilite`/başkan),
- **gümrük beyanında hangi kurun, hangi tarihte esas alınacağı** (`T-911`, bu ajan).

`T-911` bu turda **bilinçli olarak kapsam dışı bırakılmıştır** (TUR 2.5 görev
tanımı: "yeni genel araştırma yapma"). **Bu, bir eksiklik olarak kayda geçmiştir**
ve ters modelin R11 adımını bloke eder.

> ⚠️ **T-911, ters modelin "segment matematiksel olarak mümkün mü" sorusunu
> cevaplamasının önündeki SON vergi engelidir.** `CIF_TRY_max` hesaplandıktan
> sonra onu gözlenen menşe CIF birim değerleriyle (USD/lt) karşılaştırmak
> için kur kuralı gerekir.

---

### OQ-G25-05 — ÖTV nispi oranının %0 olduğu tekrar doğrulanmalı mı?

**Kritiklik:** MEDIUM · **Tip:** tek nokta bağımlılığı

Ters formülün **tamamı** `nispi ÖTV = %0` üzerine kuruludur
(`EV-2026-08-09-110`, `effective_date: 2026-07-03`). Oran > 0 olsaydı denklem
parçalı-doğrusal olur ve tek bölmeyle çözülemezdi.

Bu tek kanıt, ters modelin **en yüksek kaldıraçlı tek girdisidir** — yanlışsa
sadece bir sayı değil, **formülün yapısı** yanlış olur.

**Öneri:** `EV-2026-08-09-110`'a `ttl: 30d` ve **yüksek öncelikli yeniden
doğrulama** etiketi. (Kanıt kartları immutable'dır; yeniden doğrulama yeni bir
kart ile yapılır.)

---

### OQ-G25-06 — Gözetim eşiği `null` iken ters modelin çıktısı ne kadar güvenilir?

**Kritiklik:** MEDIUM · **Ticket:** yok (TUR 1'den devir, `EV-2026-08-09-125`)

Ters model bir **üst sınır** üretir. Gözetim bir **alt sınır** dayatır. İkisi
kesişmezse proje **fiyat pazarlığıyla kurtarılamaz** (`ters-model-vergi-bacagi.md` §11).

Eşik `UNKNOWN` olduğu için ters modelin çıktısı **alt sınırla test
edilmemiştir.** Model bu uyarıyı basmak zorundadır, ama uyarı bir çözüm
değildir. **Bu, bir gümrük müşavirine sorulacak ilk üç sorudan biridir.**

---

## navlun-lojistik-uzmani (TUR 2.5)

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2.5
tarih:  2026-08-10
not:    "99-ops/acik-sorular.md bu turda DOKUNMA listesindedir."
```

> Bu turda **yeni araştırma yapılmadı**; aşağıdakiler TUR 2'nin açık
> sorularının **daralmış / keskinleşmiş** hâlidir. Yeni soru numaraları
> yalnızca bu dosya içindedir.

| # | Soru | Neden bu turda cevaplanamadı | Kritiklik | Bağlı ticket |
|---|---|---|---|---|
| **OQ-2501** | LCL kotasyonundaki fiyat **CFS'i içeriyor mu?** | Kotasyon metni "hariç" diyor ama tutar vermiyor; forwarder'a sorulmadan bilinemez (dış temas yasak) | **HIGH** — LCL BASE'imi ±%15 kaydırır | `T-304` |
| **OQ-2502** | FCL kotasyonu **hangi kanaldan** alınabilir? Marketplace'ler Türkiye varışını hiç fiyatlamıyor | 14 lane test edildi, 0 sonuç (`EV-2026-08-10-312`); yeni tarama bu turda yasaktı | **CRITICAL** | `T-304` |
| **OQ-2503** | LCL birim fiyatı 50+ CBM'de **kademeli olarak düşüyor mu?** | 5 CBM kotasyonu doğrusal uzatıldı; kademe yapısı bilinmiyor | HIGH — §5.1 üst sınır iddiasının dayanağı | `T-802` |
| **OQ-2504** | 25.000+ şişede LCL **iç nakliyesi** gerçekte kaça mal olur? | Senaryoda "küçük araç" (5.000–10.000 TL) varsayımı kullanıldı; büyük hacimde tam kamyona yakınsaması beklenir → **LCL TRY bacağım bu hacimlerde İYİMSER** | MEDIUM | `T-304` |
| **OQ-2505** | Bir sevkiyattaki çoklu konteyner **tek beyannamede** birleşiyor mu? | Tarifede İTH-14 ("ek konteyner") kalemi var, bu birleşmeyi ima ediyor ama teyit edilmedi | MEDIUM — 8 konteynerde 6.020×8 mi 6.020+7×1.350 mi (fark ~33.000 TL) | `T-304` |
| **OQ-2506** | 2026-08-16'dan sonra aynı kaynak **aynı fiyatları** verecek mi? | Yeniden doğrulama bu turda yapılmadı (görev tanımı gereği) | **HIGH** | `T-802` |

---

## turkiye-pazar-kasifi (TUR 2.5)

> Bu dosya `99-ops/acik-sorular.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından **dokunulmamıştır**.

---

### OQ-701 — Zincir market / tekel bayii rafında giriş segmenti şarap fiyatı nedir?

```yaml
soru_id:      OQ-701
acan:         turkiye-pazar-kasifi
tarih:        2026-08-10
durum:        OPEN
oncelik:      HIGH
ilgili:       T-701, OQ-502, EV-2026-08-10-703, EV-2026-08-09-511
```

**Soru:** Migros / Macrocenter / CarrefourSA ve tekel bayii rafında, 2026'da
750 ml giriş segmenti şarabın (yerli ve ithal) tüketici raf fiyatı nedir?

**Neden açık:** Türkiye'de alkol tüketiciye internetten satılamadığı için bu
katmanda **hiç gözlem yoktur** (`EV-2026-08-09-511`). Projenin
`l8_chain_retail.deger_try` alanı **null / UNKNOWN**'dır.

**Neden şimdi kritik oldu:** TUR 2.5'te üretilen hedef raf fiyatı merdiveni
(599–999 TL) tam da bu katmanı hedeflemektedir. Merdivenin **göreli** sıralaması
yapılabilmiş, **mutlak** konumu doğrulanamamıştır.

**Elimizdeki tek (ZAYIF) sinyal:** `EV-2026-08-10-703` — T5 içerik çiftlikleri
"Migros ve tekelde 75 cl şarap ortalama 450–650 TL" demektedir.
**DOĞRULANMAMIŞTIR, MODELE GİREMEZ** (`C-503` ile aynı kaynak sınıfı).
Ama **yönü önemlidir**: doğruysa, gözlenen online uzman kanalın
(stokta yerli medyan **1.410 TL**, `EV-2026-08-10-702`) **tersini** söyler ve
hedef merdivenin üst basamaklarını (899 / 999 TL) çok daha zor bir rekabet
konumuna düşürür.

**Nasıl kapanır:** Fiziksel mağaza turu — `T-504` / `OQ-502` / `OQ-552` ile
**aynı ziyarette**, ek maliyetsiz.

---

### OQ-702 — Gözlenen online uzman kanal, giriş segmentini hiç taşımıyor mu, yoksa şu an mı stoksuz?

```yaml
soru_id:      OQ-702
acan:         turkiye-pazar-kasifi
tarih:        2026-08-10
durum:        OPEN
oncelik:      MEDIUM
ilgili:       C-501, C-561, T-561, EV-2026-08-10-702
```

**Soru:** iyisarap.plus'ın tüm stokta katalogunda (471 SKU) 600 TL altında
**yalnızca 1** SKU vardır ve stokta yerli medyan **1.410 TL**'dir. Bu, kanalın
**kalıcı assortman politikası** mıdır, yoksa **geçici bir stok durumu** mudur?

**Neden önemli:** Eğer kalıcı politikaysa, "500–1.000 TL bandında ithal şarap
yok" bulgusunun **büyük kısmı kanal artefaktıdır** ve pazar boşluğu olarak
okunamaz. Bu, `C-501` ve `C-561`'in **her ikisini de** yeniden çerçeveler.

**Nasıl kapanır:** Aynı kanalın 2–3 farklı tarihte (örn. +30 gün, +60 gün)
ölçülmesi; veya kanalın kendi "en ucuz şaraplar" koleksiyonunun incelenmesi.
Bu ajan tarafından yapılabilir, ek kaynak gerektirmez.

---

### OQ-703 — 599 TL hedefi bir pazar fiyatı mı, yoksa tek bir promosyonun izdüşümü mü?

```yaml
soru_id:      OQ-703
acan:         turkiye-pazar-kasifi
tarih:        2026-08-10
durum:        OPEN
oncelik:      HIGH
ilgili:       T-504 (CRITICAL, OPEN), OQ-001
```

**Soru:** `TARGET_SHELF_PRICE = 599 TL` basamağının **tek** destekleyici gözlemi
`OBSERVED_BENCHMARK = 599,90 TL`'dir. O gözlemin promosyon durumu `UNKNOWN`'dır.
Promosyonluysa 599 TL hedefinin **hiçbir** gözlemsel dayanağı kalmaz.

**Durum:** Bu, `T-504`'ün (CRITICAL, OPEN) hedef tarafındaki sonucudur.
**Yeni bir araştırma açılmamıştır** — TUR 2.5 kapsamı gereği Gold Country
promosyon araştırmasına dönülmemiştir. Burada yalnızca **hedef merdivene olan
bağı** kayda geçirilmektedir.

**Etkisi:** `T-504` "promosyonlu" diye kapanırsa
`60-pazar/target-shelf-price-analysis.md` §3.1'deki `AGGRESSIVE` etiketi
**`TOO_LOW`**'a döner ve PRIMARY/SECONDARY önerisi **yukarı** kaymaz — ama
599 TL downside senaryosu **elenir**.

---

---

# TUR 3A AÇIK SORULARI

> Ajanların `99-ops/_parts/*-tur3a.md` fragment'lerinden değiştirilmeden aktarıldı.

## gumruk-vergi-uzmani (TUR 3A)

---

### KAPANAN AÇIK SORULAR

| Kod | Soru | Durum | Kanıt |
|---|---|---|---|
| **OQ-G10** | md.36'ya dayanan bir CB kararı var mı? | ✅ **KAPANDI** — **VAR** (7846 + 8000), ama önlem bazlı; 2204.21'de tetiklenmiyor | `EV-2026-08-10-852`, `-853`, `-856` |
| **U1** *(kdv-…-nakit.md §4)* | KDVGUT III/C tam metni taranmadı | ✅ **KAPANDI** — belgenin **tamamı** (397 s.) tarandı | `EV-2026-08-10-854`, `-855`, `-859` |
| **Gözetim** *(matrah-sirasi.md §2)* | 2204.21'de gözetim var mı? | ✅ **KAPANDI** — **YOK**, pozitif taramayla | `EV-2026-08-10-860` |
| — | Korunma önlemi / damping var mı? | ✅ **KAPANDI** — **YOK** | `EV-2026-08-10-861`, `-862` |
| — | Alkolde özel matrah şekli var mı? | ✅ **KAPANDI** — **YOK** (TEKEL'e özgüydü, fiilen kalktı) | `EV-2026-08-10-857` |

---

### YENİ / DEVAM EDEN AÇIK SORULAR

| # | Soru | Kritiklik | Neden kapanmadı | Nasıl kapanır | Ticket |
|---|---|---|---|---|---|
| **OQ-G20** | Yıllık pakete girmemiş, daha eski ve hâlâ yürürlükte bir gözetim tebliği var mı? | **MEDIUM** | Yöntem yalnız yıllık paketi görüyor; `mevzuat.gov.tr` erişilemedi | TARA ekranından tek GTİP sorgusu **veya** gümrük müşaviri | `T-172` |
| **OQ-G21** | Gözetim OLMAKSIZIN, GK md.23–31 kıymet araştırmasıyla artan matraha 7846 uygulanır mı? | **MEDIUM** | Karar ve KDVGUT metinlerinden çıkmıyor; iki okuma mümkün | YMM / gümrük müşaviri | `T-173` |
| **OQ-G22** | `mevzuat.gov.tr` ile ikinci bağımsız doğrulama | **LOW** | Site bu oturumda tamamen erişilemedi | erişim geri geldiğinde tekrar | `EV-…-864` (ttl 7d) |
| **OQ-G23** | GVK md.41 (şahıs işletmesi, KVK md.11/1-ı muadili) | **LOW** | `mevzuat.gov.tr` erişilemedi | ithalatçı sermaye şirketi ise **gereksiz** | `T-151` md.4 |
| **OQ-G24** | 7846 kapsamındaki YMM raporu / bildirim eşiği (46 Sıra No.lu SMMM-YMM Genel Tebliği md.3/1-a tutarı) | **LOW** | Baz senaryoda tetiklenmiyor | tetiklenirse aranır | — |
| **OQ-G02** *(devam)* | KKDF matrahının tam tanımı | MEDIUM | TUR 1'den beri açık; peşin ödemede etkisiz | gümrük müşaviri | `T-105` |
| **OQ-G03** *(devam)* | Gümrük beyannamesi damga vergisi 2026 tutarı | LOW | doğrulanmadı; şişe başına ihmal edilebilir | GİB tarifeleri | — |
| **OQ-G05** *(devam)* | Gümrük beyanında esas alınacak kur kuralı | HIGH | TUR 2.5'te kapatılamadı, TUR 3A kapsamı dışıydı | gümrük müşaviri | `T-911` |

---

### TAZELİK UYARISI — bu turda üretilen bulguların ömrü

| evidence_id | ttl | STALE tarihi | Neden kısa |
|---|---|---|---|
| `EV-2026-08-10-860` (gözetim) | **30d** | **2026-09-09** | Gözetim tebliği **yıl içinde de** çıkabilir |
| `EV-2026-08-10-861` (korunma) | 90d | 2026-11-08 | Soruşturmalar yıl içinde sonuçlanır |
| `EV-2026-08-10-862` (damping) | 90d | 2026-11-08 | Liste 13/07/2026 tarihli, düzenli güncelleniyor |
| `EV-2026-08-10-864` (erişim) | **7d** | **2026-08-17** | Site erişimi geri gelebilir |

> ⚠ **Model hedef tarihlerinin üçü de 2027'dedir.** Gözetim bulgusu — tıpkı ÖTV
> maktu tutarı ve gümrük vergisi oranı gibi — **hedef tarihte doğrulanmış
> değildir.** `ters-model-vergi-bacagi.md` §13.1'deki asimetri uyarısı
> **gözetim için de geçerlidir** ve bu turda o listeye eklenmiştir.

---

## kanal-marj-uzmani (TUR 3A)

<!-- 99-ops/acik-sorular.md'ye BASKAN tarafindan birlestirilir. Bu dosya bir PART'tir. -->

> TUR 3A **sınırlı bir denetim turudur** — yeni araştırma yapılmamıştır.
> Aşağıdaki sorular yeni bulgular değil, **denetimin ortaya çıkardığı
> yapısal boşluklardır.**

| # | Soru | Kime | Neden kritik | Ticket |
|---|---|---|---|---|
| **OQ-611** | `f` ve `d` hizmet faturalarındaki KDV **indirilebilir mi**? Ciro primi KDV'de iskonto mu hizmet mi? | `gumruk-vergi-uzmani` | İndirilemezse `f`+`d`'nin ekonomik maliyeti **1,20 katı** | `T-611` |
| **OQ-612** | HoReCa **menü fiyatındaki** KDV oranı, ürün KDV oranıyla aynı mı? | `gumruk-vergi-uzmani` | `reverse-price-model.md` §3.2'nin **15 HoReCa hücresinin 15'i** bu doğrulanmamış orandan geçiyor | `T-612` |
| **OQ-613** | `d` sepetinin kaç puanı gerçekten **oransal**, kaç puanı **sabit TL**? | TUR 7 (kanal görüşmesi) | Hacim plandan saparsa tek-`d` temsili gerçek yükü **göremiyor** | `T-613` |
| **OQ-614** | Ciro primi **kademeli (tiered)** mi? | TUR 7 | Kademeliyse `d` hacme bağlıdır, sabit oran olarak taşınamaz | `T-613` |
| **OQ-615** | `f`'nin birimi **SKU × zincir** mi, **SKU × mağaza** mı? | TUR 7 | Mağaza bazlıysa `f_per_bottle` bir mertebe büyür (`B-9`) | `T-604` |
| **OQ-616** | **CRM/B2B "kasa çıkışı cirosu"** kaleminin matrahı `L6` mı `L8` mi? | TUR 7 | `L8 > L6` → `L6` matrahıyla yazmak **sistematik eksik sayım** | `T-613` |
| **OQ-617** | İade edilen şişenin **geri kazanılabilir değeri** nedir (0 mı, `L5` mi)? | TUR 7 | İadenin bedeli `L6 − geri_kazanım`; şu an `0` alınıyor | `T-615` |
| **OQ-618** | `EV-2026-08-10-329`'un TR-içi lojistiği **hangi teslim noktasına** kadar? | `navlun-lojistik-uzmani` | Zincirin lojistik bedeliyle **çift/eksik sayım** riski | `T-618` |
| **OQ-619** | Dış distribütör, zincir bedellerini (`d`, `f`) **üstlenir mi**? | TUR 7 / **başkan** | `A1` mi `A2` mi — 28,95 TL/şişe fark | `T-617` · `C-611` |
| **OQ-620** | Yatırımcı `μ`'yü **hangi matrahtan** tanımlıyor? | **yatırımcı** (`D-03`) | Matrahsız `μ` yüzdesi **anlamsızdır**; fark `μ=%30`'da 31,73 TL | `T-616` |
| **OQ-621** | Tekel bayii marjı **margin / iskonto / markup** hangisi olarak konuşuluyor? | TUR 7 | `C-602`'nin matrah boyutu; +12,19 TL fark | `C-602` |
| **OQ-622** | **Kanal karması** (zincir / tekel / HoReCa ciro payları) nedir? | `turkiye-pazar-kasifi` / TUR 7 | Üç alan da `null`; birleşik tavan **hesaplanamaz**; tavan 3,5 kat oynayabilir | `T-603` · `K9c` |

---

## global-sourcing-kasifi (TUR 3A)

```yaml
ajan:  global-sourcing-kasifi
tur:   TUR 3A — RFQ ZORUNLU TEKNIK ALANLAR
tarih: 2026-08-10
```

> Parça dosyadır. `99-ops/acik-sorular.md` ana dosyasına başkan birleştirir.
> Bu ajan ana dosyaya dokunmadı.

---

### Yeni açık sorular

| # | Ne bilinmiyor | Neden bu turda çözülmedi | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| **OQ-881** | **Zorunlu alan kuralı cevap oranını ne kadar düşürür?** RFQ v2.2 ile SUMMARY SHEET 25 → 27 satıra çıktı ve M5/M6 alt sorularıyla ~15 yeni cevap alanı eklendi. Zorunluluğun **cevap kalitesini artırıp toplam cevabı azaltma** takası ölçülmedi. | Ölçmek için **gerçek gönderim** gerekir; bu turda dış iletişim yasak (`T-467` açık). | **MEDIUM** — model çıktısını değiştirmez, ama TUR 7'nin verimini belirler | ≥8 üreticiye gönderim + **M-doluluk oranı** ölçümü (`rfq-zorunlu-alanlar.md` §4.4). %50'nin altındaysa M1/M5/M7/M8 ikinci aşamaya bırakılır. 2–4 hafta. |
| **OQ-882** | **M2/M3/M4 için kaç tedarikçi cevabı `paketli_sise_hacim_m3` bandını kapatmaya yeter?** Bugün bant üçüncü taraf palet spec sheet'inden geri hesap (0,00223 / 0,00239 / 0,00360). Tek bir tedarikçi cevabı **kendi ürünü için** kesin değer verir — ama **hangi ürünü alacağımız belli olmadan** bandın kapanıp kapanmadığı bir lojistik sorusudur. | `navlun-lojistik-uzmani`'nın alanı; `T-882` ile soruldu. | **MEDIUM** | `T-882` cevabı. |
| **OQ-883** | **Zorunlu alan baskısı yanlış rakam üretir mi?** Boş bırakılamayan alan, tedarikçiyi "bir şey yazmaya" iter. Çapraz tutarlılık kuralı (koli↔şişe↔palet) bunu kısmen yakalar, ama **tek bir tutarlı ama yanlış** paketleme setini yakalayamaz. | Ancak gerçek cevaplar + fiziksel numune/spec sheet karşılaştırmasıyla ölçülebilir. | **MEDIUM** | Numune sevkiyatında (RFQ 7.1–7.5) gelen şişenin **fiilen tartılması ve ölçülmesi**; beyanla karşılaştırma. TUR 7. |
| **OQ-884** | **M6 kabul kriteri fazla mı sıkı?** Bugünkü kural dört koşulu birden arıyor (belge adı + her sevkiyat taahhüdü + dökme bileşen yok + çıkış limanı menşe ülkesinde). Dördü birden gerekli mi, bilinmiyor. | `gumruk-vergi-uzmani`'nın alanı; `T-883` ile soruldu. | **MEDIUM** — fazla sıkıysa model **gereksiz yere aleyhimize** sapar (−%11,765'i hak etmeyen tedarikçilere de uygular) | `T-883` cevabı. |

---

### Bu turda KAPANMAYAN, önceki turlardan devreden ve RFQ'yu doğrudan etkileyen

| # | Soru | Sahibi | Neden RFQ'yu etkiliyor |
|---|---|---|---|
| `T-467` | RFQ gönderimi dış iletişim izni gerektiriyor | `yatirim-komitesi-baskani` | İzin yoksa v2.2 hiç test edilmez; zorunlu alan kuralı **kâğıt üzerinde** kalır |
| `T-871` | Pazarlık çapası hangi basamak / hangi kanal | `yatirim-komitesi-baskani` | `<VOLUME>` doldurulmadan RFQ **geçersizdir** (şablon §0.9) |
| `T-162` | Fatura beyanı değer eşiği `UNKNOWN` | `gumruk-vergi-uzmani` | RFQ 6.13(b) eşiği **rakamsız** soruyor; bağlayıcılığı düşük |
| `T-403` | Türkçe arka etiket menşede mi Türkiye'de mi | `mevzuat-ruhsat-uzmani` | M5'in **neden** sorulduğunun cevabı; kabul kriteri `T-881`'e bağlı |
| `T-206` | Şişelenmiş ithal şarapta zorunlu analiz var mı, parti başı mı | `mevzuat-ruhsat-uzmani` | M7'nin (sertifika seti) parametre listesinin **yeterli olup olmadığı** buna bağlı |

---

## finans-fizibilite (TUR 3A)

<!-- 99-ops/acik-sorular.md'ye BASKAN tarafindan birlestirilir. Bu dosya bir PART'tir. -->

```yaml
ajan:   finans-fizibilite
tur:    TUR 3A — MODEL AUDIT + ROUND-TRIP ASSERTIONS
tarih:  2026-08-10
not:    "99-ops/acik-sorular.md DOKUNMA listesindedir ve DEGISTIRILMEMISTIR.
         Bu dosya baskanin merge edecegi PARCA kayittir.
         Bu tur YENI ARASTIRMA yapmamistir; asagidaki sorular DENETIMIN
         ortaya cikardigi YAPISAL bosluklardir."
```

| # | Soru | Kime | Neden kritik | Ticket |
|---|---|---|---|---|
| **OQ-F31** | `L7_eff = L6·(1−d) − f` denklemi **ticari gerçekte** böyle mi işliyor? | `kanal-marj-uzmani` / TUR 7 | Bu turda kurulan **30 testin 30'u** bu denklemi test etmez, **onunla test eder**. Denklem yanlışsa testler yanlış bir dünyayı **tutarlı biçimde** doğrular. | `T-862` |
| **OQ-F32** | Aynı ekonomik olayın **iki farklı adla** iki satırda durması nasıl yakalanır? | `kanal-marj-uzmani` | `LEDGER_UNIQUENESS` **isim tabanlıdır**; `K6a` (`d` içindeki lojistik ↔ `L5` TR-içi lojistik) bu denetimden **görünmez geçer** | `T-861` |
| **OQ-F33** | `BLOCKED_INPUT_COUNT` kaç olduğunda çıktı `APPROVED` olabilir? | **başkan** | Bugün 26/29/31; kalemlerin **hepsi tavanı aşağı çeker**; eşik **tanımsız** | `T-864` |
| **OQ-F34** | `kanal.yaml`'daki `f_listeleme_bedeli_sise_basi` alanı **dönem toplamına** çevrilecek mi? | `kanal-marj-uzmani` | Engine artık `f_per_bottle`'ı **girdi olarak reddediyor**; alan doldurulsa bile **okunamaz** | `T-863` |
| **OQ-F35** | md.36 tetiklenirse `D` (tevsik edilemeyen tutar) **nasıl hesaplanır**? | `gumruk-vergi-uzmani` | Koşullu dal kodlandı ve `false`'ta duruyor; tetiklenirse `D` yok → model **`UNKNOWN`** dönecek, sayı **üretemeyecek** | `T-171` (`ANSWERED`) · `T-173` |
| **OQ-F36** | `makro.yaml → finansman_orani` ne zaman dolacak? | **yatırımcı** | `L6_gross` matrahı **kuruldu ve test edildi** (`651,3587` vs `L6 542,7989`) ama finansman satırı `BLOCKED_INPUT`. `K12`: 60 gün → **−27,55 TL/şişe** | `T-614` |
| **OQ-F37** | `μ` matrahı (`L6` / `L7_EFF` / `L5_MARKUP`) hangisi? | **yatırımcı** (`D-03`) | Üçü **kodlandı ve test edildi**; `μ≠0` & matrah `null` → engine **`UNKNOWN`** döner. `μ=%20`'de yayılım **16,89 TL**, `μ=%50`'de **69,96 TL** | `T-616` · `T-851` |
| **OQ-F38** | `peak_cash_requirement` hangi turda hesaplanacak? | **başkan** | Matrah (`L6_gross`) hazır, vade bandı (`kanal.yaml`) hazır, **finansman oranı yok** → sayı üretilmedi. Bu turda bilinçli olarak **yapılmadı**. | `T-614` · `OQ-F36` |

> ### BU TURUN AÇMADIĞI SORULAR (bilerek)
> Contribution margin, break-even, EBITDA, ROI, IRR ve tedarikçi tavsiyesi
> **sorulmadı ve üretilmedi.** Bu bir model bütünlüğü turuydu.

---
