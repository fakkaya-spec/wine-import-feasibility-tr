# AJAN RAPORU — MEVZUAT & RUHSAT (TUR 1)

```yaml
ajan:    mevzuat-ruhsat-uzmani
tur:     TUR 1
tarih:   2026-08-09
durum:   SUBMITTED
```

---

## 1. YÖNETİCİ ÖZETİ

Sıfırdan bir yatırımcının Türkiye'ye şişelenmiş şarap ithal edip iç piyasaya arz
etmesinin yasal yolu **açıktır**; incelenen T1/T2 mevzuatta bunu yasaklayan bir
hüküm bulunmamıştır. Zorunlu kilit belge **Dağıtım Yetki Belgesi**'dir —
*"dağıtım yetki belgesi olmadan ithalat yapılamaz"* (Ticaret Yön. m.12,
`EV-2026-08-09-203`) — ve 2026 bedeli şarap kategorisinde **68.375 TL** (≤20.000
litre/yıl) veya **170.908 TL** (>20.000 litre/yıl)'dir (`EV-2026-08-09-206`,
T1, RG 30/12/2025-33123, yürürlük 1/1/2026). Zincir markete doğrudan satış için
ayrıca **82.464 TL/yıl toptan satış belgesi** gerekir (`EV-2026-08-09-211`).
Şişe başına zorunlu ruhsat maliyeti **≈2,52 TL** (bandrol 2,36073 + hizmet bedeli
0,1587; `EV-2026-08-09-235`) olup **bandrol ithal üründe zorunlu olarak ANTREPODA,
şişe şişe uygulanır** (`EV-2026-08-09-212`) — bu, menşede çözülemeyen bir
operasyon adımıdır.

**En kritik tek bulgu mali değil, pazarlamayla ilgilidir:** 4250 s.K. m.6 zaten
reklamı, promosyonu, hediyeyi ve sponsorluğu tamamen yasaklıyordu; **20/06/2026
tarihinde yürürlüğe giren 7584 s.K. m.2** ile marka, logo, amblem ve **arz
ambalajında yer alan görsellerin iş yerlerinin içinde, dışında, vitrinlerinde ve
satış ünitelerinde bulundurulması da yasaklanmıştır** (`EV-2026-08-09-223`,
T1 dayanak RG 20/6/2026-33286; iş yerleri için uyum süresi 20/6/2027). Bu hüküm
projenin yürüdüğü an itibarıyla **9 haftalıktır** ve kapsamı henüz test edilmemiştir.

**G0 önerisi: `G0 PASS` (koşullu).** Bkz. Bölüm 10.

---

## 2. BULGULAR

### B-1: Şarap ithalatında rejim "uygunluk belgesi" değil, "alkollü içki bildirimi"dir

```yaml
claim:          Piyasaya arz edilecek alkollü içki ithalatında firmalar TADAB'a alkollü içki bildirimi yapmak zorundadır; ithalata uygunluk belgesi yalnızca etil alkol ve metanol içindir.
value:          alkollü içki bildirimi
unit:           -
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-201
effective_date: 2008-02-22
katman:         -
```

**Gerekçe:** Ticaret Yönetmeliği m.5/1 Ek-1A'daki alkol ve metanol için uygunluk
belgesi arar; m.5/2 (Ek: RG-22/2/2008-26795) Ek-1B'deki alkollü içkiler için
**bildirim** öngörür. Bu, danışmanlık kaynaklarında sıkça "ithalat izni/uygunluk
belgesi" olarak karıştırılan bir noktadır ve **T5 kaynaklara güvenilmemiştir.**

Bildirim, **ihracatçı ülkede çıkış işlemleri tamamlanmadan önce** yapılmalıdır
ve marka bazındadır (`EV-2026-08-09-202`). Bu, T0 takviminde yüklemeden önce
gelen bir adımdır.

---

### B-2: Dağıtım Yetki Belgesi — ithalatın tek kilidi

```yaml
claim:          Dağıtım yetki belgesi olmadan alkollü içki ithalatı yapılamaz; belge 2 yıl geçerlidir; bedelin 1/4'ü başvuruda, bakiyesi belge verilirken tahsil edilir.
value:          2
unit:           yıl
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-203
effective_date: 2015-12-31
katman:         -
```

**Gerekçe:** Ticaret Yön. m.12/1 (Değişik: RG-31/12/2015-29579) açıkça
*"Dağıtım yetki belgesi olmadan, yenilenmeden veya güncellenmeden, ithalat
yapılamaz, üretime konu ürünler piyasaya arz edilemez"* der. Ön koşulları:
alkollü içki bildirimi + TADAB şartlarına uygun **depo** + **nakil aracı** veya
"amaca uygun dağıtım ağlarının **akde bağlanmış kullanıcısı**" olduğunu kanıtlayan
faaliyet dosyası (m.10, `EV-2026-08-09-204`).

**Kritik boşluk:** Mevzuat bu belgenin **kaç günde verileceğini düzenlemiyor**
(`EV-2026-08-09-228`, `UNKNOWN`). Kritik yolun en büyük takvim belirsizliğidir.

---

### B-3: 2026 belge bedelleri (T1, Resmî Gazete)

```yaml
claim:          2026 dağıtım yetki belgesi maktu bedeli şarap için ≤20.000 L/yıl'da en az 68.375 TL, >20.000 L/yıl'da en az 170.908 TL; hacim bedeli 427,15 TL/1.000 L; yenileme 46.970 TL.
value:          68375 | 170908 | 427.15 | 46970
unit:           TRY
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-206, EV-2026-08-09-207, EV-2026-08-09-208
effective_date: 2026-01-01
katman:         L5 (importer cost — sabit)
```

**Gerekçe:** Tebliğ No 2025/39, RG 30/12/2025-33123, "Bu Tebliğ 1/1/2026 tarihinde
yürürlüğe girer." Yönetmeliğin kendi metnindeki (2018) rakamlar **eskidir** ve
kullanılmamıştır — Geçici m.12: *"14 üncü maddenin ikinci fıkrasında belirlenen
bedeller 2018 yılı için geçerlidir."*

**Türetme (`ESTIMATE`, `EV-2026-08-09-232`):** Bedel = `max(maktu asgari,
faaliyet hacmi/1000 × 427,15)` varsayımıyla:

| Senaryo | Hacim | Hacim bedeli | Maktu asgari | **Uygulanan** |
|---------|-------|--------------|--------------|---------------|
| 5.000 şişe | 3.750 L | 1.602 TL | 68.375 TL | **68.375 TL** |
| 10.000 şişe | 7.500 L | 3.204 TL | 68.375 TL | **68.375 TL** |
| 25.000 şişe | 18.750 L | 8.009 TL | 68.375 TL | **68.375 TL** |
| 50.000 şişe | 37.500 L | 16.018 TL | 170.908 TL | **170.908 TL** |
| 100.000 şişe | 75.000 L | 32.036 TL | 170.908 TL | **170.908 TL** |

Eşik: **20.000 litre = 26.667 adet 750 ml şişe.** Tüm senaryolarda **maktu asgari
bağlayıcıdır** — yani bedel ölçekten büyük ölçüde bağımsızdır. Bu, **küçük ölçeği
orantısız cezalandırır**: 5.000 şişede 13,68 TL/şişe, 100.000 şişede 1,71 TL/şişe.

---

### B-4: Zincir markete doğrudan satış için toptan satış belgesi zorunlu

```yaml
claim:          İthalatçı toptancıya belgesiz satabilir; ancak doğrudan perakende satıcılara veya açık alkollü içki satıcılarına satış için toptan satış belgesi zorunludur ve her depo için ayrı belge alınır.
value:          82464
unit:           TRY/yıl/belge
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-210, EV-2026-08-09-211
effective_date: 2026-01-01
katman:         L5 (importer cost — sabit)
```

**Gerekçe:** Satış ve Sunum Yönetmeliği (RG 7/1/2011-27808) m.7/1(a) verbatim:
*"Bu kişilerin, doğrudan açık alkollü içki satıcılarına, nargilelik tütün mamulü
sunumu yapan kişilere ve/veya perakende satıcılara satış yapmak istemeleri
hâlinde toptan satış belgesi almaları zorunludur."*
m.7/1(b): *"Ürünlerin satışa sunulduğu her bir yer ile muhafaza edildiği **her bir
depo için ayrı satış belgesi** alınması zorunludur."*

Bedel: Tebliğ 2025/35, RG 30/12/2025-33123, yürürlük 1/1/2026.
`00-charter/karar-esikleri.md` kanal önceliği #1 chain retail olduğundan bu belge
bu proje için **fiilen zorunludur** ve **yıllık** tekrarlar.

---

### B-5: Bandrol — antrepoda, şişe başına, peşin

```yaml
claim:          İthal alkollü içkiye bandrol ANTREPODA her bir şişenin kapağı/kapüşonu üzerine uygulanır; 2026 birim fiyatı 2.360,73 TL/1.000 adet (KDV hariç); onay ve ödemeden sonra 15 günde teslim edilir.
value:          2.36073
unit:           TRY/şişe (KDV hariç)
status:         FACT
tier:           T1 (zorunluluk/yer) + T2 (fiyat)
evidence_id:    EV-2026-08-09-212, EV-2026-08-09-213, EV-2026-08-09-214
effective_date: 2020-09-11 (zorunluluk) / 2026-01-01 (fiyat)
katman:         L5 (importer cost — değişken)
```

**Gerekçe:** ÜİS Uygulama Genel Tebliği (RG 11/9/2020-31241) bölüm 3.5.3(iii):
*"Alkollü içkilere, üretim tesislerinde üretim hattında (şişe ve kutu ambalajlı
bira hariç) veya **ithal edilmesi hâlinde antrepoda** her bir şişe ... kapağı veya
kapüşonu üzerine ... yapıştırılacaktır."* Bölüm 3.1(g) tütün için "yurt dışı
üretim mahalli veya antrepoda" derken, alkollü içkinin uygulama yeri 3.5.3'te
**yalnızca antrepo** olarak sayılmıştır.

Fiyat: Darphane BÜİS 2026 Yılı Fiyat Listesi, sıra 5, %20 KDV hariç. Fiyatlar
her yıl **Yİ-ÜFE** oranında artırılır (ÜİS Tebliği 3.5.2).

**Ön koşullar:** TADAB ürün onayı + **vadesi geçmiş vergi borcu bulunmaması** +
ÖTV (III) Sayılı Liste Uygulama Genel Tebliği yükümlülüklerine uyum.
**Ödeme peşindir** ve ürün henüz satılmamıştır → `peak_cash_requirement`.

---

### B-6: Ürün onayı — SKU bazında, 15 iş günü, bandrolün ön koşulu

```yaml
claim:          İthal alkollü içkiler piyasaya arz edilmeden önce TADAB ürün onayı alınmalıdır; başvuru 15 iş gününde karara bağlanır; onay alınmayan ürün için bandrol başvurusunda bulunulamaz.
value:          15
unit:           iş günü
status:         FACT
tier:           T2
evidence_id:    EV-2026-08-09-215, EV-2026-08-09-216
effective_date: 2025-04-11
katman:         -
```

**Gerekçe:** TADAB duyurusu (11/4/2025) — 30/12/2024 tarihli önceki duyuruyu
yürürlükten kaldırmıştır. Sıra: **GGBS Bitkisel Gıda ve Yemin Ürün Bildirim
Formu → (Sevkiyat Bildirim Formu'ndan ÖNCE) Online Hizmetler Portalı ürün onayı
→ bandrol**. Eksik dosyada +15 gün, sonra yeniden 15 iş günü.

İki maliyet-dostu detay:
- **Vintage değişikliği yeni onay gerektirmez** (`EV-2026-08-09-217`) — yıllık
  tekrarlayan SKU maliyeti yoktur.
- **Marka çakışması gate:** TÜRKPATENT'te 34 ve altı Nice sınıflarında başkası
  adına geçerli tescil varsa **ürün onayı verilmez** (`EV-2026-08-09-218`).
  Private label için doğrudan bloke edici; mevcut marka distribütörlüğünde de
  menşe markanın Türkiye'de başkası adına tescilli olmaması gerekir.

---

### B-7: Etiket — Türkçe zorunlu, sağlık uyarısı 750 ml'de ≥18 cm²

```yaml
claim:          Türkçe etiket zorunludur; alkollü içki ambalajında 3 grafik + 1 yazılı uyarı mesajı birlikte kullanılır ve 70–100 cl ambalajda uyarı toplam alanı en az 18,0 cm², punto en az 10'dur.
value:          18.0
unit:           cm² (70–100 cl)
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-219, EV-2026-08-09-220
effective_date: 2013-08-11
katman:         -
```

**Gerekçe:** Ticaret Yön. m.6/d-4 Türkçe etiket örneğini zorunlu kılar ve TGK'nın
ötesinde ek bilgiler ister (Türkçe kategori, temel girdiler, üretim ülkesi,
ambalajlama ülkesi). Uyarı Mesajları Tebliği (RG 11/8/2013-28732) m.2–3 ebatları
belirler: 1 no'lu uyarı 1,6×1,5 cm, 2 ve 3 no'lu uyarılar 1,7 cm çap,
toplam ≥18,0 cm², Helvetica, beyaz üzerine siyah, 1–2 mm bayrak kırmızısı çerçeve.
*"Uyarı mesajı taşımayan alkollü içkiler iç piyasaya arz edilemez ve satılamaz."*

**Etiketin nerede uygulanacağı (menşe/antrepo) mevzuatta düzenlenmemiş görünüyor
→ `UNKNOWN`.** Ancak bandrol zaten antrepoda uygulandığından, birleşik elleçleme
operasyonel olarak makuldur.

---

### B-8: Reklam ve satış kısıtları — zaten sert, 20/6/2026'da daha da sertleşti

```yaml
claim:          Alkollü içkilerde reklam, tanıtım, promosyon, kampanya, hediye ve sponsorluk tamamen yasaktır; 22:00–06:00 perakende satış yasaktır; 20/06/2026'dan itibaren marka/logo/ambalaj görselleri iş yerlerinin içinde, dışında, vitrinlerinde ve satış ünitelerinde bulundurulamaz.
value:          tam reklam yasağı + satış noktası marka görünürlüğü yasağı
unit:           -
status:         FACT
tier:           T1 (4250 m.6) + T2/T1 (7584 s.K.)
evidence_id:    EV-2026-08-09-222, EV-2026-08-09-223
effective_date: 2013-06-11 / 2026-06-20
katman:         -
```

**Gerekçe:** 4250 s.K. m.6 (Yeniden düzenleme: 24/5/2013-6487/2) 13 ayrı kısıt
getirir (tam liste `20-mevzuat/ruhsat-sureci.md` §9). 7584 s.K. m.2
(RG 20/6/2026-33286) m.6/1'e şu cümleyi eklemiştir — TADAB duyurusundan verbatim:

> *"Alkollü içkilerin veya alkollü içkileri üreten, ithal eden ve pazarlayan
> firmaların isim, marka, logo, amblemleri ile arz ambalajında yer alan ifade,
> şekil, isim, işaret ve görseller iş yerlerinin içinde, dışında, vitrinlerinde,
> satış ünitelerinde ve hiçbir etkinlik alanında bulundurulamaz."*

İş yerleri için uyum süresi **20/6/2027**. Açık alkollü içki satış izni olan
işletmelerde **servis materyallerinde** marka kullanılabilir.

**Bu bulgunun ticari anlamı:** Yeni bir marka için kullanılabilir marka inşa
kanalı fiilen **ambalaj + raf konumu + fiyat + kanal ilişkisi** ile sınırlıdır.
Promosyon ve bedelsiz ürün yasak olduğu için listeleme pazarlığında tek kaldıraç
**nakit indirim**dir. → `T-205` (CRITICAL), `kanal-marj-uzmani`.

---

### B-9: Teminat — TADAB mevzuatında bulunamadı

```yaml
claim:          İncelenen mevzuat metinlerinde TADAB'a verilecek bir teminat hükmü bulunamamıştır.
value:          null
unit:           TRY
status:         UNKNOWN
tier:           T1
evidence_id:    EV-2026-08-09-229
effective_date: -
katman:         -
```

**Gerekçe:** Ticaret Yönetmeliği, Satış ve Sunum Yönetmeliği, ÜİS Tebliği, 4250 ve
4733 sayılı Kanunlarda "teminat" kelimesi ithalatçı yükümlülüğü bağlamında
geçmemektedir. **"Teminat yoktur" biçiminde FACT yazılmamıştır** (negatif ispat
yapılamaz). Gümrük/antrepo teminatı bu ajanın alanı dışındadır.

> **Not:** Teminat bulunmasa da **bandrolün peşin ödenmesi** işlevsel olarak
> benzer bir nakit kilitlenmesi yaratır: 100.000 şişe = 236.073 TL (KDV hariç).

---

### B-10: T0 → ilk konteyner mevzuat süresi

```yaml
claim:          Sıfırdan başlayan yatırımcı için T0'dan ilk konteynerin izinlerinin tamamlanmasına kadar geçen mevzuat kaynaklı süre 120–270 takvim günüdür (üretim ve navlun hariç).
value:          120-270
unit:           gün
status:         ESTIMATE
tier:           T1 (sabit süreler) + ASSUMPTION (diğerleri)
evidence_id:    EV-2026-08-09-233
effective_date: -
katman:         -
```

**Türetme zinciri:** Mevzuatla sabit 4 süre (`FACT`): ürün onayı 15 iş günü,
bandrol teslimi 15 gün, bildirim belgeleri 15 gün, dağıtım yetki belgesi
yenilemesi 30 gün. Diğer adımlar `ASSUMPTION`; iki adım (`dağıtım yetki belgesi`,
`bandrol TADAB onayı`) `UNKNOWN`. Senaryolar: iyimser 112, baz 189, kötümser 281
gün. Detay: `20-mevzuat/t0-takvimi.md`.

**Bu sayının %30–50'si UNKNOWN'dan gelmektedir ve FACT değildir.**

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---------------|------------------|-----------|-------------------|
| 1 | Dağıtım yetki belgesi işlem süresi | Ticaret Yön. m.12'de azami süre yok | **CRITICAL** | TADAB'a KEP/telefon; sektör referansı (`T-202`) |
| 2 | 4250 m.1/3 — 1.000.000 L/yıl eşiğinin durgun şarap ithalatına uygulanıp uygulanmadığı | Kanun lafzı ile muafiyet fıkrası çelişiyor; BKK bulunamadı | **CRITICAL** | TADAB görüşü; Yetkili Dağıtım Firmaları Listesi analizi (`T-201`, `C-201`) |
| 3 | 7584 s.K. satış noktası marka yasağının raf kapsamı | Kanun 9 haftalık; ikincil düzenleme yok | **CRITICAL** | TADAB rehberi/ikincil düzenleme takibi (`T-205`, `C-203`) |
| 4 | Belge bedelinde maktu vs. hacim bedeli ilişkisi (max mı toplam mı) | Tebliğ lafzı iki yoruma açık | HIGH | TADAB portal bedel ekranı (`T-202`) |
| 5 | Bandrol için TADAB uygunluk onayı süresi | İlgili genelgeye erişilemedi (404) | HIGH | Genelgenin güncel URL'si (`T-204`) |
| 6 | TGK Gıda Etiketleme Yönetmeliği tam metni | resmigazete.gov.tr / mevzuat.gov.tr TLS-503 | HIGH | Farklı ağ; FAOLEX aynası |
| 7 | Zorunlu analiz: parametre, akredite lab, parti başı tekrar, süre, maliyet | Şişelenmiş üründe rejim dosya üzerinden; kontroller risk esaslı | MEDIUM | Bitkisel Gıda ve Yem İthalatı Resmî Kontrol Yönetmeliği (`T-206`) |
| 8 | TADAB ürün onayı için ayrı bedel var mı | Tebliğ 2025/39'da yok, duyuruda geçmiyor | MEDIUM | TADAB portal / TADAB'a soru |
| 9 | Türkçe etiketin menşede mi antrepoda mı uygulanacağı | Belirleyici hüküm bulunamadı | MEDIUM | TADAB görüşü; mevcut ithalatçı uygulaması |
| 10 | Yazılı sağlık uyarısı mesajının birebir metni | Tebliğ Ek-1 görsel olarak yayımlanmış | MEDIUM | Tebliğ Ek-1 temini |
| 11 | Antrepo türü ve bandrol uygulama operasyon maliyeti | Alan dışı (lojistik) | HIGH | `navlun-lojistik-uzmani` (`T-204`) |
| 12 | Teminat (gümrük/antrepo tarafında) | Alan dışı | MEDIUM | `gumruk-vergi-uzmani`, `navlun-lojistik-uzmani` |
| 13 | ÜGD 2026/19 tam metni ve Ek listeleri | Erişim sorunu | LOW (yükümlülük zaten T1'de sabit) | RG 31/12/2025-33124 (4. mükerrer) |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|-------------|----------------------|----------------------|-----------------|-------|
| **C-201** | 4250 m.1/3 (T1, 2001): ithalatçıya ülke geneli yerinde teslim + 1.000.000 L/yıl fiyat serbestisi eşiği | 4250 m.1/5 (T1, 2001): muafiyet fıkrası ithal yönünden yalnızca **viski ve tabiî köpüren şarap** sayıyor; ayrıca yaptırım mercii Tekel GM artık yok | Durgun şarap ithalatının eşiğe tabi olup olmadığı belirsiz; hüküm fiilen uygulanabilir değil ama yürürlükte | **OPEN** → `T-201` |
| **C-202** | Ticaret Yön. m.10/a (T1, 2008): dağıtım yetki belgesi için alkollü içki bildirimi ön koşul | Ticaret Yön. m.12/1 (T1, 2015): dağıtım yetki belgesi olmadan ithalat yapılamaz | Sıralama döngüsü; bildirim ile fiilî ithalatın ayrıştığı varsayıldı ama doğrulanmadı | **OPEN** → `T-202` |
| **C-203** | 7584 s.K. m.2 (T1, 2026): arz ambalajı görselleri satış ünitelerinde bulundurulamaz | 4250 m.6/7 (T1, 2013) ve Satış Yön. (T1, 2011): perakende satış serbest, yalnızca dışarıdan görünürlük yasak | Lafzî okuma ürünün raf varlığını imkânsız kılar; kanunun kendi sistematiğiyle çelişir | **OPEN** → `T-205` |
| **C-204** | TGK Şarap Tebliği 2008/67 (T1, TADAB yayını): dayanak 5179 s.K., atıf RG 25/8/2002-24857 | 5179 s.K. mülga (5996); atıf yapılan tebliğ mülga (yerine RG 26/1/2017-29960 mükerrer) | Şarap etiket kurallarının hangi metinden okunacağı belirsiz; tebliğin yayım tarihi de doğrulanamadı | **OPEN** (düşük etki) |

`99-ops/_parts/celiskiler-mevzuat-ruhsat-uzmani.md` dosyasına da yazıldı.

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|--------------|------|-------|-------|--------|-------------|
| ruhsat.yaml | `g0_onerisi.value` | G0_PASS (koşullu) | - | ESTIMATE | EV-...-201/203/206/210/212 |
| ruhsat.yaml | `belgeler.ithalat_yetki_belgesi.gerekli_mi` | false | - | FACT | EV-2026-08-09-201 |
| ruhsat.yaml | `belgeler.ithalat_yetki_belgesi.alkollu_icki_bildirimi_gerekli_mi` | true | - | FACT | EV-2026-08-09-201 |
| ruhsat.yaml | `belgeler.dagitim_yetki_belgesi.gerekli_mi` | true | - | FACT | EV-2026-08-09-203 |
| ruhsat.yaml | `...gecerlilik_suresi_yil` | 2 | yıl | FACT | EV-2026-08-09-203 |
| ruhsat.yaml | `...harc_maliyet_maktu_asgari_kucuk_hacim` | 68.375 | TRY | FACT | EV-2026-08-09-206 |
| ruhsat.yaml | `...harc_maliyet_maktu_asgari_buyuk_hacim` | 170.908 | TRY | FACT | EV-2026-08-09-206 |
| ruhsat.yaml | `...hacim_bedeli_per_1000_litre` | 427,15 | TRY/1000 L | FACT | EV-2026-08-09-207 |
| ruhsat.yaml | `...yenileme_bedeli` | 46.970 | TRY | FACT | EV-2026-08-09-208 |
| ruhsat.yaml | `...basvuru_suresi_gun` | null | gün | **UNKNOWN** | EV-2026-08-09-228 |
| ruhsat.yaml | `belgeler.satis_belgesi.toptan_satis_belgesi_bedeli` | 82.464 | TRY/yıl | FACT | EV-2026-08-09-211 |
| ruhsat.yaml | `belgeler.satis_belgesi.her_depo_icin_ayri_mi` | true | - | FACT | EV-2026-08-09-210 |
| ruhsat.yaml | `urun_uygunlugu.basvuru_suresi_gun` | 15 | iş günü | FACT | EV-2026-08-09-216 |
| ruhsat.yaml | `urun_uygunlugu.sku_basina_maliyet` | null | TRY | **UNKNOWN** | - |
| ruhsat.yaml | `urun_uygunlugu.vintage_degisikligi_yeni_onay_gerektirir_mi` | false | - | FACT | EV-2026-08-09-217 |
| ruhsat.yaml | `etiket.turkce_etiket_zorunlu_mu` | true | - | FACT | EV-2026-08-09-219 |
| ruhsat.yaml | `etiket.saglik_uyarisi_min_alan_cm2_750ml` | 18,0 | cm² | FACT | EV-2026-08-09-220 |
| ruhsat.yaml | `etiket.uygulama_yeri` | null | - | **UNKNOWN** | - |
| ruhsat.yaml | `etiket.etiket_basim_maliyeti_per_sise` | null | TRY | **UNKNOWN** | - |
| ruhsat.yaml | `analiz_laboratuvar.*` | null | - | **UNKNOWN** | EV-2026-08-09-230 |
| ruhsat.yaml | `bandrol_uis.bandrol_birim_bedeli` | 2,36073 | TRY/şişe (KDV hariç) | FACT | EV-2026-08-09-213 |
| ruhsat.yaml | `bandrol_uis.bandrol_temin_suresi_gun` | 15 | gün | FACT | EV-2026-08-09-214 |
| ruhsat.yaml | `bandrol_uis.uygulama_yeri` | ANTREPO | - | FACT | EV-2026-08-09-212 |
| ruhsat.yaml | `depo_antrepo_izni.alkol_depo_izni_gerekli_mi` | true | - | FACT | EV-2026-08-09-204 |
| ruhsat.yaml | `depo_antrepo_izni.kendi_deposu_zorunlu_mu` | false | - | FACT | EV-2026-08-09-204 |
| ruhsat.yaml | `depo_antrepo_izni.antrepo_turu` | null | - | **UNKNOWN** | - |
| ruhsat.yaml | `teminat.gerekli_mi` | null | - | **UNKNOWN** | EV-2026-08-09-229 |
| ruhsat.yaml | `satis_dagitim_reklam_kisitlari.*` | (7 alan dolu) | - | FACT | EV-...-222, -223, -224, -226 |
| ruhsat.yaml | `surekli_yukumlulukler.hizmet_bedeli_per_1000_litre` | 211,60 | TRY/1000 L | FACT | EV-2026-08-09-209 |
| ruhsat.yaml | `t0_takvimi.toplam_gun_t0_ilk_konteyner` | [120, 270] | gün | ESTIMATE | EV-2026-08-09-233 |
| ruhsat.yaml | `toplam_ruhsat_sabit_maliyeti.kucuk_hacim_ilk_yil` | 150.839 | TRY | ESTIMATE | EV-2026-08-09-234 |
| ruhsat.yaml | `toplam_ruhsat_sabit_maliyeti.buyuk_hacim_ilk_yil` | 253.372 | TRY | ESTIMATE | EV-2026-08-09-234 |
| ruhsat.yaml | `toplam_ruhsat_degisken_maliyeti_per_sise` | 2,52 | TRY/şişe (KDV hariç) | ESTIMATE | EV-2026-08-09-235 |

**evidence_id'si olmayan satır modele giremez.** Yukarıdaki `UNKNOWN` satırlar
`null` olarak bırakılmıştır.

> **`finans-fizibilite` için uyarı:** `toplam_ruhsat_sabit_maliyeti` **eksiktir** —
> danışmanlık, noter/tercüme, depo kurulum/3PL, etiket tasarım+klişe, analiz ve
> antrepo elleçleme kalemleri UNKNOWN'dur ve bu tutarı **yalnızca yukarı** çeker.

---

## 6. ÇAPRAZ İPUÇLARI

Tam liste: `99-ops/_parts/capraz-ipuclari-mevzuat-ruhsat-uzmani.md` (29 ipucu).
Öne çıkanlar:

| Hedef ajan | İpucu | Neden önemli |
|------------|-------|--------------|
| `gumruk-vergi-uzmani` | Bandrol antrepoda, serbest dolaşımdan önce uygulanıyor; ÖTV (III) Sayılı Liste yükümlülüğü ihlali **bandrol talebini bloke eder** | Matrah sırası + operasyonel kilit |
| `gumruk-vergi-uzmani` | TADAB Ürün ID'si gümrük beyannamesi 31. kutuda beyan edilmek zorunda | Beyanname hazırlığı |
| `navlun-lojistik-uzmani` | Bandrol **şişe şişe antrepoda** uygulanıyor; depo TADAB yetki belgesi taşımalı; her depo için ayrı 82.464 TL | L4→L5 geçişindeki en somut operasyon kalemi |
| `navlun-lojistik-uzmani` | Kendi deposu zorunlu değil — "akde bağlanmış dağıtım ağı kullanıcısı" yeterli | 3PL modeli yasal olarak açık |
| `kanal-marj-uzmani` | Promosyon/hediye/bedelsiz ürün **tam yasak**; münhasırlık ve bağlı satış yasak; 20/6/2026 satış noktası marka yasağı | Listeleme pazarlığında tek kaldıraç nakit indirim |
| `kanal-marj-uzmani` | İthalatçı **ülke genelinde her satıcıya yerinde teslim** yükümlü | Ulusal dağıtım ağı zorunluluğu → marj |
| `global-sourcing-kasifi` | TÜRKPATENT ≤34 Nice sınıfı marka çakışması **ürün onayını bloke eder** | Private label için ön tarama zorunlu |
| `global-sourcing-kasifi` | 750 ml şişede uyarı mesajları **≥18 cm²** yer kaplar | Etiket tasarım alanı ciddi daralıyor |
| `turkiye-pazar-kasifi` | TADAB **aylık güncellenen ürün listesi** ve **Yetkili Dağıtım Firmaları Listesi** yayımlıyor | Rakip SKU ve rekabet haritası için T2 birincil kaynak |
| `finans-fizibilite` | Bandrol **peşin**; belge bedelinin 1/4'ü başvuruda; tüm bedeller yıllık güncelleniyor | `peak_cash_requirement` + 2027 duyarlılığı |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|-----------|--------------|-------|--------|--------|
| `T-201` | yatirim-komitesi-baskani | 4250 m.1/3 — 1.000.000 L/yıl eşiği ve ülke geneli yerinde teslim şartı durgun şarap ithalatına uygulanıyor mu | **CRITICAL** | OPEN |
| `T-202` | yatirim-komitesi-baskani | Dağıtım yetki belgesi süresi tanımsız + bedel yapısı (max mı toplam mı) belirsiz | HIGH | OPEN |
| `T-203` | gumruk-vergi-uzmani | Bandrol ve hizmet bedelinin ÖTV/KDV matrahındaki yeri | MEDIUM | OPEN |
| `T-204` | navlun-lojistik-uzmani | Antrepoda bandrol uygulaması — antrepo türü, birim maliyet, gün, fire | HIGH | OPEN |
| `T-205` | kanal-marj-uzmani | 7584 s.K. satış noktası marka/logo yasağının zincir market rafındaki kapsamı | **CRITICAL** | OPEN |
| `T-206` | mevzuat-ruhsat-uzmani | Şişelenmiş ithal şarapta zorunlu analiz var mı, parti başı mı | MEDIUM | OPEN |

> **Gate uyarısı:** `T-201` ve `T-205` `impact: CRITICAL` ve `OPEN`'dır.
> `CLAUDE.md` §5 uyarınca bunlar açıkken finans modeli `APPROVED` olamaz.

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|-------------|-----|---------------------|
| EV-2026-08-09-201 … 212 (mevzuat hükümleri) | 180d | 2027-02-05 |
| EV-2026-08-09-206, -207, -208, -209, -211 (2026 tarifeleri) | 180d | 2027-02-05 — **ancak 1/1/2027'de yeni tebliğle SUPERSEDED olacağı kesindir** |
| EV-2026-08-09-213 (bandrol 2026 fiyatı) | 180d | 2027-02-05 — **Yİ-ÜFE ile 1/1/2027'de artacaktır** |
| EV-2026-08-09-215, -216, -217, -218 (TADAB duyurusu) | 180d | 2027-02-05 |
| EV-2026-08-09-220 (uyarı mesajları) | 365d | 2027-08-09 |
| EV-2026-08-09-221 (şarap tebliği) | 365d | 2027-08-09 |
| **EV-2026-08-09-223 (7584 s.K. reklam yasağı)** | **90d** | **2026-11-07** — ikincil düzenleme beklendiği için kısa TTL |
| EV-2026-08-09-227, -230, -231 (UNKNOWN'lar) | 90d | 2026-11-07 |
| EV-2026-08-09-232 … 235 (ESTIMATE'ler) | 90–180d | 2026-11-07 / 2027-02-05 |

**Aralık: EV-2026-08-09-201 → EV-2026-08-09-235 (35 kanıt kartı).**

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**4250 s.K. m.1/3'teki 1.000.000 litre/yıl eşiğinin durgun şarap ithalatına
bugün de uygulandığının teyidi.** Bu doğruysa, projenin modellediği tüm hacim
senaryoları (5.000–100.000 şişe = 3.750–75.000 litre) eşiğin **çok** altındadır ve
firma "fiyat belirlemekte serbest" olmayacaktır. Projenin çekirdek sorusu
("üreticiye en fazla kaç dolar ödeyebiliriz?") ters fiyatlandırmaya dayandığı için,
fiyatlandırma serbestisinin bulunmaması raporu değil **projeyi** geçersiz kılar.
Bu durumda G0 önerim `G0 PASS`'ten `G0 BLOCKED`'a döner.

İkinci sıradaki çürütücü: **7584 s.K.'nın satış noktası marka yasağının**, TADAB
ikincil düzenlemesiyle **ürünün raftaki görünürlüğünü de kapsayacak** biçimde
yorumlanması. Bu, mevzuat açısından G0'ı değiştirmez ama kanal modelini çökertir.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**Dağıtım yetki belgesi bedelinin `max(maktu asgari, hacim bedeli)` olarak
hesaplandığı varsayımı** (`EV-2026-08-09-232`).

Tebliğ lafzı "**en az** 68.375 TL" ve ayrıca "faaliyet hacmi üzerinden beher bin
litre başına 427,15 TL" der. Ben bunu bir taban + hacim formülü olarak okudum.
Alternatif okuma (maktu + hacim toplamı) 100.000 şişe senaryosunda bedeli
170.908 → 202.944 TL'ye çıkarır. Bu tek başına kararı değiştirmez ama küçük
ölçekte şişe başına maliyeti bozar.

İkinci en kırılgan: **T0 takviminin `ASSUMPTION` süreleri.** Depo/3PL için
30–90 gün, dağıtım yetki belgesi için 30–90 gün tahminlerinin **hiçbir kanıt
dayanağı yoktur** — bunlar planlama amaçlı yerleştirilmiş sayılardır ve raporda
`ASSUMPTION` olarak açıkça etiketlenmiştir. Toplam sürenin gerçekte 1 yılı aşması
mümkündür.

### 9.3 Hangi kaynağıma en az güveniyorum?

Üç sıralı:

1. **TGK Şarap Tebliği 2008/67** (`EV-2026-08-09-221`). TADAB yürürlükteki mevzuat
   olarak yayımlıyor, ancak dayanağı **mülga 5179 sayılı Kanun**, atıf yaptığı
   etiketleme tebliği de **mülga**. Yayım tarihini bile T1'den doğrulayamadım.
   Bu tebliğden çıkardığım etiket kuralları (3 mm ABV puntosu, ±%0,5 tolerans)
   güncel olmayabilir. `C-204`.
2. **ÜGD 2026/19 ithalat denetimi tebliği** (`EV-2026-08-09-231`). Yalnızca
   ikincil/T5 kaynaklardan okuyabildim; `status: UNKNOWN` bıraktım ve FACT
   saymadım. Şansım, aynı yükümlülüğün zaten Ticaret Yönetmeliği m.5/2 ile T1
   düzeyinde sabit olması.
3. **Uyarı mesajları tebliğinin aynası** (gumruk.com.tr). Metin RG 11/8/2013-28732
   ile birebir uyumlu görünüyor ve "son güncelleme 17/1/2014" notu taşıyor, ancak
   **birincil RG kopyasını göremedim** (resmigazete.gov.tr bu oturumda TLS/503
   verdi). 2014 sonrası bir değişiklik varsa kaçırmış olabilirim.

Ayrıca dürüstlük gereği: `EV-2026-08-09-213` (bandrol fiyatı) PDF'ten OCR ile
okundu ve OCR bazı rakamları bozdu; **2.360,73** değeri bağımsız bir arama
sonucuyla çapraz doğrulandığı için kullanıldı, ancak PDF'in kendisi düşük
kaliteli bir taramadır.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlış çıkan bulgu | Değişen karar |
|--------------------|---------------|
| 1 milyon litre eşiği uygulanıyor (`T-201`) | `G0 PASS` → `G0 BLOCKED`. Başkan muhtemelen `KILL` veya `HOLD` verir. |
| Satış noktası marka yasağı ürünü de kapsıyor (`T-205`) | Private label senaryosu elenir; yalnızca mevcut marka distribütörlüğü kalır. `TEST` yerine `HOLD`. |
| Dağıtım yetki belgesi >6 ay sürüyor (`T-202`) | `IMPORT PILOT` takvimi 2027'ye kayar; 2027 tarifeleriyle model yeniden çalışır. |
| Parti başına zorunlu analiz var (`T-206`) | Şişe başına maliyet artar; 5.000 şişelik pilot ekonomisi bozulabilir. |
| Bandrol antrepo elleçlemesi >2 TL/şişe (`T-204`) | Ruhsat kaynaklı değişken maliyet 2,52 → 4,5+ TL/şişe; fiyat/performans segmentinde marj eridiği için kanal seçimi değişir. |
| Belge bedeli maktu+hacim toplamı | Sadece sayı düzeltmesi; karar değişmez. |

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| Ne | Kim | Nasıl | Süre | Maliyet |
|----|-----|-------|------|---------|
| `T-201` — 1 milyon litre eşiği | Alkol mevzuatında uzman hukuk bürosu + TADAB | Yazılı görüş talebi (KEP) + Yetkili Dağıtım Firmaları Listesindeki küçük ithalatçıların tespiti | 2–6 hafta | hukuki görüş bedeli (UNKNOWN) |
| `T-202` — belge süresi ve bedel yapısı | Yatırımcı / danışman | TADAB Alkol ve Alkollü İçkiler Daire Başkanlığına telefon (0312 218 03 00) + portal bedel ekranı testi | 1–2 hafta | ~0 |
| `T-205` — reklam yasağı kapsamı | TADAB + kanal-marj-uzmani | İkincil düzenleme/rehber takibi; zincir market kategori yöneticisiyle görüşme (T4) | ikincil düzenleme çıkana kadar (belirsiz) | ~0 |
| `T-206` — analiz | Akredite gıda laboratuvarı | Şarap analiz paketi teklifi (T4) + Bakanlık uygulama talimatı | 1–2 hafta | teklif bedelsiz |
| `T-204` — antrepo bandrol operasyonu | Antrepo işletmecisi / gümrük müşaviri | 3 farklı antrepodan yazılı teklif | 1–3 hafta | teklif bedelsiz |
| Q-209 — TGK etiketleme yönetmeliği | Bu ajan | Farklı ağdan resmigazete.gov.tr veya FAOLEX | 1 gün | ~0 |
| **En hızlı ve en yüksek getirili doğrulama** | Yatırımcı | **Sektörde faaliyet gösteren küçük ölçekli bir şarap ithalatçısıyla 1 saatlik görüşme** — T-201, T-202, T-204, T-206'nın dördünü birden aydınlatır | 1 hafta | ~0 |

---

## 10. G0 ÖNERİSİ

```yaml
oneri:          G0 PASS
kosullu:        true
status:         ESTIMATE
evidence_id:    [EV-2026-08-09-201, EV-2026-08-09-203, EV-2026-08-09-206,
                 EV-2026-08-09-210, EV-2026-08-09-212, EV-2026-08-09-222]
```

**Gerekçe:**

1. İncelenen T1/T2 mevzuatta Türkiye'de şarap ithalatçısı olmayı **yasaklayan**
   hiçbir hüküm yoktur. `G0 FAIL` için dayanak bulunamamıştır.
2. Gerekli belgelerin tamamı **tanımlıdır** ve 2026 bedelleri **Resmî Gazete'de
   yayımlanmış tebliğlerle bilinmektedir** (Tebliğ 2025/39 ve 2025/35, yürürlük
   1/1/2026). Belge bedelleri (≈151–253 bin TL) proje ölçeğine göre karşılanabilir
   düzeydedir.
3. En ağır fiziksel ön koşul olan **depo**, "akde bağlanmış dağıtım ağı kullanıcısı"
   olmakla karşılanabilmektedir — yani sermaye yoğun bir depo yatırımı zorunlu değildir.
4. Şu an bloke eden, kaldırılamaz bir engel (verilmeyen bir belge, karşılanamaz bir
   teminat) tespit edilmemiştir; dolayısıyla `G0 BLOCKED` da uygun değildir.

**Bu öneriyi `G0 BLOCKED`'a çevirecek bulgular:**

- `T-201` olumsuz sonuçlanırsa (1.000.000 litre/yıl eşiği durgun şarap ithalatına
  uygulanıyorsa) → **G0 BLOCKED**, muhtemelen `HOLD`/`KILL`.
- `T-202` ile dağıtım yetki belgesi süresinin fiilen 6 ayı aştığı doğrulanırsa →
  **G0 BLOCKED** (kaldırılabilir engel; takvim revizyonu gerekir).

**Bu öneri bir KARAR DEĞİLDİR.** Nihai karar (`KILL` · `HOLD` · `TEST` ·
`IMPORT PILOT` · `SCALE`) yalnızca `yatirim-komitesi-baskani`'na aittir.

---

## EK — ÜRETİLEN DOSYALAR

- `20-mevzuat/ruhsat-sureci.md` — belge/izin haritası
- `20-mevzuat/t0-takvimi.md` — T0 → ilk konteyner, kritik yol işaretli
- `10-evidence/raw/EV-2026-08-09-201.md` … `EV-2026-08-09-235.md` (35 kart)
- `10-evidence/raw/snapshots/` (11 birincil kaynak kopyası)
- `10-evidence/_index-parts/mevzuat-ruhsat-uzmani.csv`
- `80-model/inputs/ruhsat.yaml`
- `99-ops/_parts/capraz-ipuclari-mevzuat-ruhsat-uzmani.md`
- `99-ops/_parts/celiskiler-mevzuat-ruhsat-uzmani.md`
- `99-ops/_parts/acik-sorular-mevzuat-ruhsat-uzmani.md`
- `99-ops/tickets/T-201.md` … `T-206.md`
