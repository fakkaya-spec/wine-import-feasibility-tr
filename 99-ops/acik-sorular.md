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
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            TUR 0 kurulum
sorumlu_ajan:    mevzuat-ruhsat-uzmani (T0 takvimi) -> yatirim-komitesi-baskani
impact:          HIGH
bloke_ettigi:    vergi.yaml/meta.model_hedef_tarihi
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

> Ajanlar farklı ID şemaları kullanmıştır (`OQ-###`, `OQ-G##`, gruplu liste).
> Başkan bunları yeniden numaralandırmamıştır; ajan raporları bu ID'lere
> atıf yapmaktadır. Detay için aşağıdaki ajan bölümlerine bakınız.

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
