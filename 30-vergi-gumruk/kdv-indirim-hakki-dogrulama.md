# İTHALAT KDV'Sİ — İNDİRİM HAKKININ DOĞRULANMASI (T-947)

```yaml
belge:            kdv-indirim-hakki-dogrulama
ajan:             gumruk-vergi-uzmani
tur:              TUR 3A — KDV CRITICAL CHECK
tarih:            2026-08-10
kapsam:           T-947 (CRITICAL) + T-151 (MEDIUM) — KDVK md.36 / KDVGUT III/C taramasi
BASE_DATE:        2026-08-10
durum:            SUBMITTED
```

---

## 0. SONUÇ — ÜÇ SEÇENEKTEN HANGİSİ

> ## **A) KDV İNDİRİMİ CONFIRMED — koşullu bir istisna ile**
>
> **Baz senaryoda (2204.21, 750 ml şişelenmiş köpüksüz şarap) ithalatta ödenen
> KDV'nin indirim hakkını sınırlayan bir düzenleme YOKTUR.**
>
> **ANCAK** TUR 1.5'te varsayıldığı gibi "hiç kısıt yok" da **değildir.**
> KDVK md.36'ya dayanan **yürürlükte bir Cumhurbaşkanı Kararı BULUNMUŞTUR**
> (**7846 sayılı CBK**, `EV-2026-08-10-852`, yürürlük **2023-11-24**) ve bu karar
> **ithalatta gözetim / korunma önlemi / dampinge karşı vergi** kapsamındaki
> matrah artışlarına ait KDV'nin indirim hakkını **kaldırmaktadır.**
>
> Bu karar **alkole özgü değildir; ÖNLEME özgüdür.** Şarapta uygulanmasının
> tek koşulu, 2204.21'in bu üç önlemden birine tabi olmasıdır —
> ve **hiçbirine tabi değildir** (`gozetim-kiymet-kontrolu.md`).
>
> **Yani cevap `A`'dır, ama `A`'nın dayanağı TUR 1.5'tekinden farklıdır:**
> "md.36 kararı yok" değil, **"md.36 kararı VAR ama bu ürüne değmiyor."**

**Sonucun model etkisi:** `ters-model-vergi-bacagi.md` §8'in **A sütunu ayaktadır**;
`R7-K2` (`kdv_ekonomik_maliyet = 0`) **geçerlidir**; `MAX_CIF_TRY` değerlerinde
**hiçbir değişiklik gerekmez.** `finans-fizibilite`'nin `%22,7` düşüş senaryosu
**gerçekleşmemiştir.**

**Ama bir KOŞUL eklenmiştir** ve modelde bir **kilit** olarak durmalıdır (§5).

---

## 1. NE SORULDU

`T-947` (opened_by: `yatirim-komitesi-baskani`, impact: **CRITICAL**):

> *"KDVK md.36 uyarınca çıkarılmış ve ALKOLLÜ İÇKİDE ithalat KDV'sinin indirim
> hakkını kısıtlayan bir Cumhurbaşkanı Kararı olup olmadığı üç turdur
> aranmamıştır."*

`T-151` (kendi kaydım, MEDIUM) iki boşluk işaretlemişti:
1. **KDV Genel Uygulama Tebliği (KDVGUT) III/C** tam metni — taranmadı
2. **md.36'ya dayanan CB/BKK kararları** — sistematik taranmadı

**İkisi de bu turda tarandı. Sonuçlar aşağıdadır.**

---

## 2. TARAMA — NE YAPILDI, NE BULUNDU

### 2.1 KDVK md.36 — yetkinin tam kapsamı (T1)

`EV-2026-08-10-851` · tier **T1** · effective_date **2018-07-02** (700 s. KHK ile
"Bakanlar Kurulu" → "Cumhurbaşkanı") · kaynak: 3065 s.K. konsolide metin

> *"**Madde 36** – Cumhurbaşkanı **indirim veya iade hakkını kısmen veya tamamen
> kaldırmaya** veya yeniden koymaya ve bu şekilde indirim veya iade hakkı
> kısıtlanan **mal veya hizmetleri belirlemeye**, … yetkilidir."*

**Üç bulgu:**

| # | Bulgu | Önemi |
|---|---|---|
| M36-1 | Yetki **mal bazında** kullanılabilir ("mal veya hizmetleri belirlemeye"). Yani teorik olarak "şarap" diye bir karar çıkarılabilir. | `T-947`'nin sorusu **hukuken meşrudur**, spekülatif değildir |
| M36-2 | Yetki **fiilen kullanılmıştır** (7846 · 8000) — §2.2 | TUR 1.5'in "böyle bir karar sektörde bilinir olurdu, olasılık düşük" gerekçesi **kısmen yanlıştı**: karar var, sadece kapsamı farklı |
| M36-3 | **Anayasa Mahkemesi** 22/7/2025 tarih, E.2024/54, K.2025/163 sayılı kararıyla md.36'daki *"…veya **iade**…"* ibarelerini **iptal etmiştir**; iptal **9/9/2026**'da yürürlüğe girer. **"İndirim" yetkisi İPTAL EDİLMEMİŞTİR.** | İndirim kısıtlama yetkisi **9/9/2026 sonrasında da ayaktadır** → risk kapanmadı, §6.1 |

### 2.2 md.36'ya dayanan Cumhurbaşkanı / Bakanlar Kurulu kararları — **TAM LİSTE TARAMASI**

`EV-2026-08-10-856` · tier **T2** · kaynak: GİB Mevzuat veri tabanı (kanun id 436 = 3065 s. KDVK)

Tarama **örnekleme değil, tam sayımdır**: KDV Kanunu'na bağlı olarak GİB'in
mevzuat veri tabanında kayıtlı **32 Cumhurbaşkanı Kararı** ve **86 Bakanlar
Kurulu Kararı**nın **tamamının başlığı** çekilmiş ve md.36 geçen/indirim
kısıtlayan kayıtlar ayıklanmıştır.

| Kategori | Adet | md.36 dayanaklı indirim/iade **kısıtı** içeriyor mu |
|---|---|---|
| CBK — "Mal ve Hizmetlere Uygulanacak KDV Oranlarının Tespiti…" (md.28) | 24 | **HAYIR** — oran kararları |
| CBK — geçici madde süre uzatımı (Gç.37, Gç.39) | 2 | **HAYIR** |
| CBK — hasılat esaslı vergilendirme (718), iade asgari tutarı | 2 | **HAYIR** |
| CBK — 6775 s. Karar değişikliği (9582) | 1 | **HAYIR** |
| **CBK — 7846 (RG 24/11/2023-32379)** | **1** | ✅ **EVET** |
| **CBK — 8000 (RG 28/12/2023-32413) — 7846'yı değiştiren** | **1** | ✅ **EVET (geçici madde)** |
| BKK — başlığında "36 ncı madde" geçen (id 1504, 1505, 1507) | 3 | **HAYIR** — üçü de **KDV ORANI** kararıdır; md.36 yalnız md.28 ile birlikte **usul dayanağı** olarak anılmıştır |
| BKK — diğer | 83 | **HAYIR** |

> **Bu, `EV-2026-08-09-125` tipi bir "negatif arama" DEĞİLDİR.**
> Kaynak, GİB'in **kanun bazında kürasyonlu** mevzuat kaydıdır; 32+86 kaydın
> **tamamı** listelenmiş ve okunmuştur. Sınırı §4'te açıkça yazılmıştır.

### 2.3 7846 sayılı CB Kararı — tam metin (T1)

`EV-2026-08-10-852` · **T1** · RG **24/11/2023**, sayı **32379** ·
effective_date **2023-11-24** (yayımı tarihi) · dayanak: **KDVK md.36**

> **MADDE 1-** *(1) İthalatta **gözetim uygulanması** hakkında ilgili mevzuat
> uyarınca, gözetim uygulamasına tabi tutulan mallara ilişkin gümrük
> beyannamelerinde **beyan olunan ve tevsik edilemeyen tutarlar** ile bu tutarlar
> nedeniyle doğan ve katma değer vergisi matrahına dâhil olan her türlü vergi,
> resim, harç ve paylar dolayısıyla ödenen katma değer vergisinin **indirim hakkı
> kaldırılmıştır.***
>
> *(2) İthalatta **korunma önlemleri** … korunma önlemi olarak uygulanan gümrük
> vergisi ve/veya ek mali mükellefiyetler, ithalatta **haksız rekabetin
> önlenmesi** … **dampinge karşı vergi ve telafi edici vergiler** ile bu tutarlar
> nedeniyle doğan ve KDV matrahına dâhil olan her türlü vergi, resim, harç ve
> paylar dolayısıyla ödenen katma değer vergisinin **indirim hakkı
> kaldırılmıştır.***

**8000 sayılı CBK** (`EV-2026-08-10-853`, T1, RG 28/12/2023-32413) yalnızca bir
**geçici madde** eklemiştir: 24/11/2023 öncesi bankacılık sistemi üzerinden
ödenmiş ve en geç **1/4/2024**'e kadar ithal edilen mallar Karar kapsamı
dışındadır. **Bu geçiş hükmünün süresi dolmuştur; bugün etkisizdir.**

### 2.4 KDVGUT III/C — **TAM METİN TARANDI** (T-151'in asıl boşluğu)

`EV-2026-08-10-854`, `-855`, `-858`, `-859` · kaynak: **GİB konsolide KDVGUT PDF,
397 sayfa**, `cdn.gib.gov.tr`, dosya tarihi 2026-04-15 (57 Seri No.lu Tebliğ
değişiklikleri **dahil**).

| Bölüm | İçerik | Şarap ithalatçısına etkisi |
|---|---|---|
| **III/C-1 Vergi İndirimi** (`EV-…-855`, T1) | *"…veya **ithal ettikleri mal ve hizmetler dolayısıyla ödedikleri KDV'yi** … indirebilirler."* md.29/3'ün iki takvim yılı sınırı ayrıca açıklanmış | **Genel kural teyit edildi.** Şarap ithalatçısı için istisna yok |
| **III/C-2 İndirilemeyecek KDV** | md.30/a–e uygulaması; binek otomobil, zayi mal, transfer fiyatlandırması, değersiz alacak | Alkole/şaraba **atıf yok** |
| **III/C-2.6** *(YENİ — 57 Seri No.lu Tebliğ, yürürlük **31/1/2026**)* (`EV-…-854`, T1) | 7846'nın **idari uygulaması**: indirilemeyecek KDV matrahının hesabı, sayısal örnek, ve **YMM raporu / vergi dairesine bildirim yükümlülüğü** | **Yalnızca gözetim/korunma/damping kapsamındaki mallarda** devreye girer |
| **III/B-2.5.2 Konaklama İşletmelerinde Kullanılan Alkollü İçecekler** (`EV-…-858`, T1) | *"…geceleme hizmetleri kapsamında sunulan alkollü içeceklere ait yüklenilen KDV tutarları, **konaklama tesisleri tarafından** hesaplanan KDV'den **indirilemez**."* | **İTHALATÇIYA DEĞMEZ.** Mükellefi **otel**dir. → §3.2 ve çapraz ipucu |
| KDVGUT **tam metin** "alkol / içki / şarap" taraması (`EV-…-859`) | 397 sayfada alkol geçen tüm yerler tarandı: (a) konaklama III/B-2.5.2, (b) lokanta/HoReCa oran ayrımı (alkollü kısım %20), (c) biracılık posası istisnası | **Şarap İTHALATÇISININ indirim hakkına ilişkin TEK BİR kısıt yoktur** |

> **57 Seri No.lu Tebliğ'in yürürlük tarihi 31/1/2026'dır** — yani 7846'nın
> uygulama usulü **BASE_DATE'ten yalnızca 6 ay önce** netleşmiştir. Bu, konunun
> canlı ve hareketli olduğunun göstergesidir.
>
> **Dürüstlük kaydı:** kullanılan konsolide PDF 2026-04-15 tarihlidir ve
> **58 Seri No.lu Tebliğ'i (RG 16/6/2026-33282) içermez.** 58 No.lu Tebliğ'in
> **tam metni ayrıca okunmuş** ve **III/C bölümünü değiştirmediği** teyit
> edilmiştir (II/B-15.1.3, II/F, IV/A3-1.1 maddelerini değiştirir).

### 2.5 GİB özelgesi — idari görüş (T2)

`EV-2026-08-10-857` · **T2** · GİB Zonguldak VDB, sayı
`B.07.1.GİB.4.67.15.01-2010-KDV-23-34`, tarih **20/08/2011**

Soru: *alkollü içkilerin perakende satışını yapan mükellefin bu ürünlerin
alımlarında yüklendiği KDV'yi indirim konusu yapıp yapamayacağı.*

> Cevap: *"…alkollü içkilerin perakendeci bayiler tarafından nihai tüketicilere
> teslimi, **genel esaslara göre** KDV'ye tabi tutulacak, alkollü içki alımları
> nedeniyle yüklenilen KDV, **Kanunun 29 uncu maddesi uyarınca indirim konusu
> yapılabilecektir**."*

Ayrıca: alkollü içkide **özel matrah şekli** yalnız TEKEL işletmelerine
uygulanıyordu ve **özelleştirme ile fiilen ortadan kalkmıştır**
(93 Seri No.lu KDV Genel Tebliği, VIII. bölüm).

> **Bu, `T-151`'in "GİB özelgesi aranmadı" boşluğunu kapatan doğrudan idari
> görüştür ve sonucu TEYİT eder.** Özelge ticaret aşamasına ilişkindir; ithalat
> aşamasına *a fortiori* uygulanır (md.29/1-b ithalatı ayrıca sayar).

---

## 3. NE **BULUNMADI** — ve bunun anlamı

### 3.1 Alkole/şaraba özgü indirim yasağı: **YOK**

Dört bağımsız katmanda arandı, dördünde de bulunamadı:

| Katman | Kaynak | Sonuç | tier |
|---|---|---|---|
| **Kanun** | KDVK md.30 tam metin (TUR 1.5) | tahdidi liste, alkol yok | T1 · `EV-2026-08-09/10-103` |
| **CB Kararı** | md.36 dayanaklı CBK/BKK **tam liste** | yalnız 7846/8000, **ürün değil ÖNLEM bazlı** | T2 · `EV-2026-08-10-856` |
| **Tebliğ** | KDVGUT 397 sayfa tam metin | ithalatçıya kısıt yok | T1 · `EV-2026-08-10-859` |
| **Özelge** | GİB 20/08/2011 | *"indirim konusu yapılabilecektir"* | T2 · `EV-2026-08-10-857` |

### 3.2 Alkole özgü **TEK** KDV indirim kısıtı — ve neden bizi vurmaz

**KDVGUT III/B-2.5.2** (konaklama tesisleri). Kapsamı:

```
mükellef        : KONAKLAMA TESİSİ (otel)      -> ithalatçı DEĞİL
işlem           : "her şey dahil" geceleme hizmeti (indirimli oran)
sonuç           : otelin alkollü içecek alımına ait YÜKLENİLEN KDV indirilemez
kaçış yolu      : alkollü içecek bedelini faturada AYRICA gösterirse
                  %20 hesaplar ve yüklenilen KDV'yi İNDİREBİLİR
```

**İthalatçı zinciri:** ithalatçı → toptancı/otel satışında **%20 hesaplanan KDV**
düzenler; kendi yüklendiği ithalat KDV'sini indirir. Kısıt **alıcı otelde**
doğar, **satıcı ithalatçıda** doğmaz.

> ⚠ **Bu bir VERGİ sonucu değil, bir KANAL sonucu doğurur:** "her şey dahil"
> otelde şarabın KDV'si otel için **gerçek maliyettir** → o kanalın ödeme
> istekliliği yapısal olarak **%20 daha düşüktür**. Bu benim alanım değildir →
> `kanal-marj-uzmani`'ye **çapraz ipucu** bırakıldı (`T-171` değil, ipucu).

### 3.3 KVK md.11/1-(ı) (TUR 1.5 bulgusu) — değişmedi

Alkollü içki **ilan/reklam** giderlerinin %50'si KKEG'dir; md.30/d üzerinden o
giderin KDV'si indirilemez. Malın kendisine ait ithalat KDV'sini **etkilemez**
(`EV-2026-08-10-113`). Bu turda yeni bir bulgu yoktur.

---

## 4. TARAMANIN SINIRLARI — "aradım bulamadım" ile "yok" ayrımı

Bu bölüm zorunludur ve `EV-2026-08-09-125`'in düştüğü tuzağa düşmemek içindir.

### 4.1 Erişilebilen ve **tam** taranan kaynaklar

| Kaynak | Kapsam | Yöntem |
|---|---|---|
| 3065 s. KDVK konsolide metin | md.29, 30, 34, 35, **36**, 46, 47 | tam metin |
| KDVGUT konsolide (397 s., 2026-04-15) | **tüm belge** | tam metin + anahtar kelime |
| 58 Seri No.lu KDVGUT değişikliği | tam metin | III/C'ye dokunmadığı teyit edildi |
| GİB CBK listesi — kanun 436 | **32/32 kayıt** | başlık + içerik |
| GİB BKK listesi — kanun 436 | **86/86 kayıt** | başlık; md.36 geçen 3'ünün içeriği |
| GİB özelge arama | "alkollü içki" | en yüksek skorlu kayıt okundu |
| RG 24/11/2023-32379 (7846) | tam metin (OCR) | T1 doğrudan |
| RG 28/12/2023-32413 (8000) | tam metin (OCR) | T1 doğrudan |

### 4.2 **ERİŞİLEMEYEN** kaynaklar — `EV-2026-08-10-864`

| Kaynak | Neden | Etki |
|---|---|---|
| `mevzuat.gov.tr` (tüm uç noktalar) | Bu oturumda **tamamen erişilemedi** (TCP bağlantı kuruluyor, HTTP yanıt yok; 60–280 sn timeout, 5 ayrı deneme). *Ek not: sunucu TLS zincirinde ara sertifika göndermiyor; bu ayrıca giderildi ama sorun çözmedi.* | Mevzuat Bilgi Sistemi'nin **tam metin arama**sı kullanılamadı — `EV-2026-08-09-125`'in yöntemi **tekrar edilemedi** |
| `kms.kaysis.gov.tr` (KAYSİS) | erişilemedi (timeout) | ikinci tam metin arama alternatifi kayboldu |
| `uygulama.gtb.gov.tr/Tara` (Tarife Arama Motoru) | **CAPTCHA** — otomatik sorgulanamaz | GTİP bazında "tüm önlemler" sorgusu yapılamadı |
| GİB **özelge tam metin** araması, tüm sonuç sayfaları | arama motoru skorlu ilk sayfayla sınırlı kullanıldı | başka bir özelge olabilir; **olasılık düşük** (bulunan özelge doğrudan konuya isabet ediyor) |

> **Bu dört satır, bu belgenin dürüstlük payıdır.** Sonucu `A` yapan kanıtlar
> yukarıdaki §4.1 listesinden gelmektedir ve **hiçbiri erişilemeyen kaynağa
> dayanmamaktadır.**

---

## 5. MODEL SÖZLEŞMESİ — SONUCUN KODA/YAML'A YANSIMASI

### 5.1 Değişmeyenler (ters modelin ekonomik dalı **ayakta**)

```
kdv_ekonomik_maliyet          = 0                       [DEĞİŞMEDİ]
R7-K2  (KDV ekonomik dalda hiçbir çıkarmada kullanılmaz) [GEÇERLİ]
CIF_TRY_max = (L4_econ_max − O − k − X_pre) / (1 + g)    [DEĞİŞMEDİ]
MAX_CIF_TRY üzerindeki etki                              = 0,00 TL/şişe
```

### 5.2 **YENİ**: koşullu indirim kısıtı — `kdv_indirim_kisiti_7846`

`vergi.yaml → kdv_perspektifleri.a_ekonomik_maliyet.md36_indirim_kisiti` bloğu
eklenmiştir. Engine için bağlayıcı kural:

```
tetikleyici(gtip, mense) =
      gozetim.uygulama_var_mi            == true
   OR korunma_onlemi.uygulama_var_mi     == true
   OR dampinge_karsi_vergi.var_mi        == true

EĞER tetikleyici == false  (2204.21 baz senaryo — EV-2026-08-10-860/-861/-862)
     -> kdv_ekonomik_maliyet = 0                      [A1 BAZ SENARYO]

EĞER tetikleyici == true
     -> indirilemeyen_kdv = v × ( tevsik_edilemeyen_tutar
                                  + o tutara isabet eden GV/İGV/EMY
                                  + o tutarlara isabet eden diğer vergi/resim/harç/pay )
     -> bu tutar EKONOMİK MALİYETTİR ve L5'e TAŞINIR
     -> ters modelde: L4_econ_max'tan ÇIKARILIR (maktu kalem gibi,
        yani (1+g) BÖLMESİNDEN ÖNCE — R7-K1 ile aynı sıra)
```

**Kısmi kısıt formülü (KDVGUT III/C-2.6 örneğinden birebir):**

```
indirilebilir_kdv_matrahi   = CIF + CIF×g + CIF×igv
indirilemeyen_kdv_matrahi   = D + D×g + D×igv           , D = gözetim eşiği − CIF
indirilemeyen_kdv           = v × indirilemeyen_kdv_matrahi
```

> **Kritik:** kısıt **KDV'nin tamamını** değil, **yalnız tevsik edilemeyen
> artış kısmına isabet edeni** kaldırır. `finans-fizibilite`'nin `T-947`'de
> yazdığı **"%22,7 düşüş"** senaryosu **tam kısıt** varsayımıdır ve
> **7846 tam kısıt getirmez.** Tetikleyici doğsa bile etki `%22,7`'den
> **belirgin biçimde küçüktür**.

### 5.3 Uyum yükü — modelde **maliyet satırı** (nakit değil, gerçek gider)

KDVGUT III/C-2.6.2, 7846 kapsamında ithalat yapan mükellefe **altışar aylık
dönemler itibarıyla**:
- ithalat bedeli eşiğin **altındaysa** → vergi dairesine **bildirim**,
- **üstündeyse** → **Özel Amaçlı YMM Raporu** (tam tasdik sözleşmesi varsa gerek yok)

yükümlülüğü getirir. **2204.21 baz senaryoda tetiklenmez**; tetiklenirse
`L5` içinde **YMM raporu ücreti** adında yeni bir satır doğar. Tutar **UNKNOWN**
ve bu ajanın alanı değildir.

---

## 6. BU BULGUYU NE ÇÜRÜTÜR?

### 6.1 Tek cümlelik çürütücü

**2204.21 için bir gözetim / korunma önlemi / dampinge karşı vergi getirilmesi.**
O anda 7846 **kendiliğinden** devreye girer — yeni bir KDV kararı gerekmez,
ilan edilmez, "sektörde duyulmaz". Bu, `gozetim-kiymet-kontrolu.md`'yi
**KDV belgesinin de dayanağı** hâline getirir: iki dosya artık **tek bir
kırılma noktasını** paylaşmaktadır.

### 6.2 Mevzuat değişikliği riski — azalmadı, **adresi değişti**

- md.36'nın **"indirim"** yetkisi AYM iptalinden **kurtulmuştur** (`M36-3`).
  Yani Cumhurbaşkanı, **yarın** alkollü içki ithalatında indirim hakkını
  kaldıran bir karar çıkarabilir ve bu **anayasal olarak tartışmasız** olur.
  7846 bu yetkinin **fiilen kullanıldığının kanıtıdır** — yani bu artık
  "teorik" bir risk değildir.
- **Aksi yön:** AYM'nin 9/9/2026'da yürürlüğe girecek iptali **iade** yetkisini
  kaldırmaktadır. Şarapta iade hakkı zaten yoktur (md.29/2, `EV-2026-08-10-104`)
  → **etkisiz**.

### 6.3 En kırılgan halka

**7846'nın "tevsik edilemeyen tutar" tanımının fiilî yorumu.** KDVGUT örneği
gözetim bedeli ile CIF farkını *yurt dışı gider* olarak beyan eden bir senaryo
kurar. Gerçek beyanda idarenin bunu nasıl kodladığı (BİLGE alanı, 
"yurt dışı gider" mi "kıymet artışı" mı) **doğrulanmamıştır.** Bu, tetikleyici
doğduğunda hesabın büyüklüğünü değiştirir.

### 6.4 GTİP itirazı

GTİP itirazı bu belgeyi **değiştirmez** — md.29/1-b tüm ithal mallar içindir.
**Ama** GTİP değişikliği ürünü **gözetim kapsamındaki başka bir pozisyona**
taşırsa 7846 tetiklenir. Şu an bilinen alternatiflerin (2204.10, 22.05, 2206.00)
**hiçbiri** gözetim/korunma/damping listelerinde değildir
(`EV-2026-08-10-860/-861/-862`).

### 6.5 Kaynağıma en az güvendiğim yer

`EV-2026-08-10-856` (GİB'in kanun bazlı CBK/BKK kürasyonu). **Tam sayım**dır ama
GİB'in **kendi** eşleştirmesine dayanır: md.36 dayanaklı bir kararın GİB veri
tabanında KDV Kanunu ile **ilişkilendirilmemiş** olması teorik olarak mümkündür.
`mevzuat.gov.tr` erişilebilir olsaydı bu ikinci bir bağımsız kaynakla
çaprazlanabilirdi — **olmadı** (`EV-2026-08-10-864`).

### 6.6 Bunu kesinleştirmek için ne gerekir

Tek soru, tek muhatap, ~0 TL:

> *"Şarap (GTİP 2204.21) ithalatında 7846 sayılı Cumhurbaşkanı Kararı kapsamında
> indirimi kabul edilmeyen bir KDV doğuyor mu? Bu GTİP gözetim, korunma önlemi
> veya dampinge karşı vergi kapsamında mı?"*

Muhatap: gümrük müşaviri **veya** YMM. `T-901` / `T-151` ile **aynı oturumda**
kapanır.
