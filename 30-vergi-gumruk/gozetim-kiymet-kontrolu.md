# GÖZETİM / REFERANS KIYMET KONTROLÜ — 2204.21

```yaml
belge:            gozetim-kiymet-kontrolu
ajan:             gumruk-vergi-uzmani
tur:              TUR 3A — GÖZETİM / KIYMET
tarih:            2026-08-10
kapsam:           GTİP 2204.21 (750 ml şişelenmiş köpüksüz şarap)
BASE_DATE:        2026-08-10
durum:            SUBMITTED
```

---

## 0. SONUÇ

> ## **NO APPLICABLE MEASURE** — *ama tek kelimeyle değil, dört kanıtla*
>
> 2204.21 için **BASE_DATE 2026-08-10 itibarıyla**:
>
> | Önlem | Durum | Kanıt | tier |
> |---|---|---|---|
> | **İthalatta gözetim** (birim kıymet eşiği) | **YOK** | `EV-2026-08-10-860` | T1 |
> | **Korunma önlemi** (safeguard) | **YOK** | `EV-2026-08-10-861` | T2 |
> | **Dampinge karşı / telafi edici vergi** | **YOK** | `EV-2026-08-10-862` | T2 |
> | **Şarabı konu alan ithalat tebliği** | **YOK** | `EV-2026-08-10-863` | T2 |
>
> **Dolayısıyla `gozetim_esigi = null` kalır ve ters modelin ürettiği
> `CIF_TRY_max` bir ALT SINIRLA ÇAKIŞMAZ.**
>
> **AMA:** kıymet riski **sıfır değildir.** Gözetim yokluğu, gümrük idaresinin
> **GK md.23–31 kıymet belirleme/araştırma yetkisini** ortadan kaldırmaz (§4).
> Bu ikisi **farklı mekanizmalardır** ve modelde **ayrı** durmalıdır.

---

## 1. NEDEN SORULDU — ters modelin alt sınır problemi

`ters-model-vergi-bacagi.md` §11:

```
ters model üretir :  CIF_TRY_max          ← ÜST SINIR (ticari olarak mümkün azami)
gözetim dayatır   :  CIF_beyan ≥ eşik     ← ALT SINIR (hukuken beyan edilebilir asgari)

eşik > CIF_TRY_max   ⇒  ÇÖZÜM KÜMESİ BOŞ — pazarlıkla kurtarılamaz
```

TUR 1'de bu satır `UNKNOWN` (negatif arama) idi (`EV-2026-08-09-125`).
**Bu turda pozitif kanıta çevrilmiştir.**

> **TUR 3A'da ortaya çıkan YENİ ve daha sert bağ:** gözetim artık yalnız bir
> **alt sınır** sorunu değil, aynı zamanda bir **KDV sorunudur.**
> **7846 sayılı Cumhurbaşkanı Kararı** (`EV-2026-08-10-852`) gözetim kapsamındaki
> malda *"beyan olunan ve **tevsik edilemeyen** tutarlar"*a ait KDV'nin
> **indirim hakkını kaldırmaktadır.** Yani gözetim gelirse:
> **(a)** alt sınır doğar, **(b)** KDV kısmen ekonomik maliyete dönüşür,
> **(c)** altı aylık **YMM raporu** uyum yükü doğar.
> Üçü aynı anda. Ayrıntı: `kdv-indirim-hakki-dogrulama.md`.

---

## 2. YÖNTEM — negatif aramadan pozitif taramaya

### 2.1 Gözetim tebliğleri — **tam metin taraması** (`EV-2026-08-10-860`, T1)

Türk gözetim rejiminde tebliğler **iki ayrı seride** yayımlanır ve karıştırılırsa
yanlış yerde aranır (`EV-2026-08-10-863`):

| Seri | Örnek | RG | Konu |
|---|---|---|---|
| `İthalat: 2026/x` | 2026/1…2026/19 | 31/12/2025-33124 **3. mükerrer** | fuar, silah, GTS, gübre, askıya alma… |
| **`İthalatta Gözetim … Tebliğ (No: 2026/x)`** | 2026/1…2026/36 + 11 değişiklik | 31/12/2025-33124 **4. mükerrer** | **birim kıymet eşikleri** |

**4. mükerrerdeki 47 tebliğin tamamı** indirildi ve GTİP tabloları çıkarıldı.

**Neden üç ayrı çıkarım yöntemi gerekti (bu kritik bir metodoloji notudur):**

```
(a) PDF metin katmanı           -> bazı tebliğlerde tablo BURADA, bazılarında YOK
                                   (ayrıca bazı PDF'lerde metin katmanı ŞİFRELİ/bozuk
                                    font kodlamasıyla geliyor → tek başına GÜVENİLMEZ)
(b) sayfa görüntüsü OCR         -> tabloyu bazen atlıyor (psm 6 tablo bloğunu görmüyor)
(c) GÖMÜLÜ TABLO GÖRÜNTÜSÜ OCR  -> tablo çoğu tebliğde ayrı bir CCITT/JBIG2 GÖRÜNTÜDÜR
                                   ve metin katmanında HİÇ YOKTUR
──────────────────────────────────────────────────────────────────────
KULLANILAN = (a) ∪ (b) ∪ (c)
```

> **Tek yöntemle yapılsaydı sonuç YANLIŞ NEGATİF olurdu.** Örneğin (a) tek başına
> kullanılsaydı 2026/2 sayılı tebliğin `3824.99.92.00.34` satırı hiç görülmezdi.

**Sonuç:**

| Ölçüt | Değer |
|---|---|
| Taranan tebliğ | **47/47** |
| GTİP çıkarılabilen | **46/47** *(kalan 1'i — 2024/14 değişikliği — ayrıca tam OCR edildi: GTİP tablosu YOK, yalnız Ek-2 form maddesi kaldırılmış)* |
| Bulunan farklı GTİP | **305** |
| Kapsanan fasıllar | 08, 20, 25, 28, 29, 34, 37, 38, 39, 40, 46, 48, 54, 67, 68, 69, 70, 71, 73, 79, 82, 83, 84, 85, 87, 90, 94, 95, 96 |
| **22. fasıl (içecekler)** | **HİÇ YOK** |
| **2204 / 2205 / 2206** | **0** |
| Tümünde kullanılan belge kodu | **TPS-0964 — Gözetim Belgesi SANAYİ** |

### 2.2 Korunma önlemleri — idarenin kendi "yürürlüktekiler" listesi (`EV-…-861`, T2)

Ticaret Bakanlığı'nın **Yürürlükteki Önlemler (Safeguard Measures in Force)**
sayfası, **11** önlem listeler (sayfalama 1/1, tam liste):

PET Resin · Naylon İplik · Öğütücü Bilya · Etil Asetat · Düz Cam (İran) ·
Polyester Elyaf · Kâğıt · Filmaşin · Diş Fırçaları · Pet Cips · Polyester Elyaf (İran)

**Hepsi sanayi ürünü. Şarap yok, tarım/gıda ürünü yok.**

### 2.3 Dampinge karşı vergi — idarenin 13/07/2026 tarihli tam listesi (`EV-…-862`, T2)

`Yürürlükteki Önlemler 13.07.2026.xlsx` içinde **1015** GTİP kaydı var.
`2204` / `2205` / `2206` / `şarap` sayısı: **0**.
*(1015 GTİP bulunması, aramanın anlamlı olduğunun **pozitif kontrolüdür**.)*

---

## 3. BU SONUCUN SINIRI — dürüstlük bölümü

### 3.1 Kapatılamayan artık risk

| # | Ne kapanmadı | Neden | Etki |
|---|---|---|---|
| **R1** | 31/12/2025 paketinde **ne yeniden yayımlanan ne de değiştirilen**, daha eski ve hâlâ yürürlükte bir gözetim tebliği olabilir | Bu yöntem yalnız yıllık paketi görür | **Ticket `T-172`** |
| **R2** | `mevzuat.gov.tr` bu oturumda **tamamen erişilemedi** → TUR 1'deki tam metin araması **tekrarlanamadı** | `EV-2026-08-10-864` | ikinci bağımsız doğrulama yapılamadı |
| **R3** | `uygulama.gtb.gov.tr/Tara` (Tarife Arama Motoru) **CAPTCHA**lı | otomatik sorgulanamıyor | GTİP bazlı "tüm önlemler" sorgusu yapılamadı |

### 3.2 R1'i **kısmen** kapatan iki bağımsız argüman

1. **TUR 1'in bağımsız kanıtı (`EV-2026-08-09-125`):** Mevzuat Bilgi Sistemi
   **tebliğler tam metin araması**, `2204.21` / `2204.29` / `22.04` için
   **hiçbir gözetim tebliği** döndürmemiştir — ve o arama **yıl sınırı
   taşımaz**, ayrıca **bilinen bir gözetim GTİP'iyle pozitif kontrol
   edilmiştir** (`8536.20.10.00.11` → Tebliğ 2008/11 doğru bulunmuştur).
   **Farklı yöntem, farklı yıl kapsamı, aynı sonuç.**
2. Yıllık paketin **11 eski tebliği aynı pakette değiştirmiş** olması, idarenin
   yürürlükteki eski tebliğleri **aynı anda elden geçirdiğini** gösterir.
   *(Bu bir `ESTIMATE`'tir, kanıt değildir.)*

> **İki bağımsız negatif + iki pozitif kontrol.** Bu, `EV-2026-08-09-125`'in
> yalnız başına taşıdığı "negatif arama" zayıflığından **yapısal olarak
> farklıdır** — ama **mutlak kanıt değildir.**

### 3.3 ⚠ "Şarap tarım ürünüdür, gözetim gelmez" argümanı **GEÇERSİZDİR**

Taramada **2019/6 sayılı tebliğe** ilişkin değişiklikte **`0810.10` (çilek) ve
`0810.50` (kivi)** GTİP'leri görülmüştür. Yani **gözetim taze meyveye de
uygulanabilmektedir.** Sonuç yalnızca **fiilî listede bulunmamaya** dayanır,
bir "kategori bağışıklığına" değil.

---

## 4. GÖZETİM ≠ KIYMET ARAŞTIRMASI — modelin karıştırmaması gereken iki şey

| | **GÖZETİM** | **KIYMET ARAŞTIRMASI / ŞÜPHE** |
|---|---|---|
| Dayanak | İthalatta Gözetim Uyg. Tebliği (GTİP bazlı) | **GK md.23–31**, Gümrük Yönetmeliği |
| Tetikleyici | **önceden ilan edilmiş birim kıymet eşiği** | idarenin **beyana şüphesi** (BİLGE risk kriterleri, emsal veri) |
| Belge | Gözetim Belgesi (TPS-0964) — **beyanname tescilinde ARANIR** | belge yok; **ek bilgi/belge talebi**, gerekirse **teminatla** teslim |
| 2204.21'de durumu | **YOK** — `EV-2026-08-10-860` | **YETKİ HER ZAMAN SAKLIDIR** — `UNKNOWN` |
| Öngörülebilirlik | **Tam** (eşik yayımlanmış) | **Yok** (idari takdir) |
| 7846 KDV kısıtı doğurur mu | **EVET** (tevsik edilemeyen tutar) | **Metinde ANILMAMAKTADIR** — §4.1 |
| Modeldeki karşılığı | `gozetim.birim_kiymet_esigi` = **null** | `kiymet_arastirmasi_riski` = **UNKNOWN, senaryo** |

### 4.1 Açık hukuki soru — sessizce çözmüyorum

7846 sayılı Karar'ın lafzı *"**gözetim uygulamasına tabi tutulan mallara** ilişkin
gümrük beyannamelerinde beyan olunan ve tevsik edilemeyen tutarlar"* der.
**GK md.23–31 kapsamında (gözetim olmaksızın) yapılan bir kıymet artırımının**
bu kapsama girip girmediği **metinden çıkmamaktadır** ve KDVGUT III/C-2.6 de
bunu açıklamamaktadır.

- **Lafzî yorum:** girmez (gözetim yoksa Karar da uygulanmaz).
- **Riskli yorum:** idare "tevsik edilemeyen tutar" kavramını genişletebilir.

→ **`T-173` (MEDIUM)** olarak kayda alındı; sessiz seçim yapılmamıştır.
Baz senaryoda **lafzî yorum** kullanılmakta ve `kdv_ekonomik_maliyet = 0`
korunmaktadır.

---

## 5. MODEL SÖZLEŞMESİ

### 5.1 `vergi.yaml → gozetim` — güncellenen alanlar

```yaml
gozetim.uygulama_var_mi        : false        # UNKNOWN -> false  (EV-2026-08-10-860)
gozetim.birim_kiymet_esigi     : null         # DEĞİŞMEDİ — ölçülecek bir eşik YOK
gozetim.otv_gozetimden_etkilenir_mi : false   # DEĞİŞMEDİ (maktu)
korunma_onlemi.uygulama_var_mi : false        # YENİ (EV-2026-08-10-861)
dampinge_karsi_vergi.var_mi    : false        # YENİ (EV-2026-08-10-862)
```

### 5.2 Engine kuralı — çıktı uyarısı **DEĞİŞTİ**

**ESKİ (TUR 2.5):**
> *"gözetim eşiği doğrulanmamıştır; `CIF_TRY_max` bir alt sınırla test EDİLMEMİŞTİR"*

**YENİ (TUR 3A) — bu satır artık şu olmalıdır:**
> *"2204.21 için gözetim / korunma önlemi / dampinge karşı vergi **taranmış ve
> bulunmamıştır** (EV-2026-08-10-860/-861/-862, BASE_DATE 2026-08-10, ttl 30d).
> `CIF_TRY_max` üzerinde **hukuki bir alt sınır yoktur.** Kalan kıymet riski
> GK md.23–31 idari takdiridir ve **modellenmemiştir.**"*

### 5.3 `ttl` ve tazelik

`gozetim` bulgusunun `ttl`'i **30 gündür** → **2026-09-09**'dan sonra STALE.
Gözetim tebliği **yıl içinde de** yayımlanabilir. Model hedef tarihleri
**2027**'dedir; yani bu bulgu **hedef tarihte doğrulanmış değildir** —
tıpkı ÖTV ve gümrük vergisi oranı gibi (`ters-model-vergi-bacagi.md` §13.1'deki
asimetri uyarısı **gözetim için de geçerlidir**).

### 5.4 Gözetim **doğarsa** ne olur — hazır parametrik şema (model için)

Kullanılmıyor ama tanımlı olmalı (`vergi.yaml → gozetim.tetiklenirse`):

```
girdi : esik_birim_kiymet (USD/lt veya USD/kg), CIF_beyan
D     = max(0, esik × miktar − CIF_beyan)          # tevsik edilemeyen tutar
GV    = (CIF_beyan + D) × g                        # GV eşik üzerinden doğar
ÖTV   = maktu — DEĞİŞMEZ                           # EV-2026-08-09-113
KDV   = v × (CIF_beyan + D + GV + ÖTV)
indirilemeyen_KDV = v × (D + D×g)                  # 7846 + KDVGUT III/C-2.6
ekonomik_ek_yuk   = D + D×g + indirilemeyen_KDV    # ÜÇÜ BİRDEN
uyum_yuku         = YMM raporu / 6 aylık bildirim  # tutar UNKNOWN
ters modelde      : eşik, CIF_TRY_max üzerinde MUTLAK ALT SINIRDIR
```

---

## 6. BU BULGUYU NE ÇÜRÜTÜR?

### 6.1 Tek bulgu

**2204 (veya 2204.21 alt satırlarından biri) için yürürlükte, benim taramamın
dışında kalmış bir gözetim tebliği.** Bu, `T-172`'nin tam olarak sorduğu şeydir
ve tek bir gümrük müşaviri sorgusuyla (veya TARA ekranından tek bir GTİP
sorgusuyla) **dakikalar içinde** kesinleşir.

### 6.2 Hangi mevzuat değişikliği geçersiz kılar

- **Yıl içinde yayımlanacak yeni bir gözetim tebliği.** Gözetim tebliğleri
  yalnız 31 Aralık'ta değil, **yıl boyunca** çıkabilir. `ttl: 30d` bu yüzden.
- **31/12/2026'da yayımlanacak 2027 paketi** — üç model hedef tarihinin **üçü de
  2027'dedir**, yani bu bulgu **hedef tarihte doğrulanmamıştır.**
- **7846'nın kapsam genişletilmesi** (md.36 yetkisi ayakta — `EV-2026-08-10-851`).

### 6.3 GTİP itirazı

GTİP itirazı bu sonucu **doğrudan** değiştirmez: taranan 305 GTİP içinde
**hiçbir 22. fasıl kaydı yoktur**, yani 2204.10 / 22.05 / 2206.00'a kayma da
gözetim doğurmaz. Ancak ürün **22. fasıl dışına** çıkarsa (ör. aromatize
karışım olarak 2106'ya) tarama **yeniden yapılmalıdır**.

### 6.4 En zayıf halkam

**Yöntemin kendisi.** 47 PDF, üç farklı çıkarım tekniği ve OCR üzerinden
çalıştım. OCR bir GTİP'i **yanlış okuyabilir** (ör. `2204` → `2704`). Bunu
azaltmak için üç yöntemin **birleşimi** alındı ve 22. fasıl **hiçbir yöntemde**
görünmedi; ayrıca "şarap/wine" kelime araması da negatif çıktı. Yine de
**%100 değildir.**

### 6.5 Kıymet itirazı senaryosunda ne olur

Gözetim yoksa bile idare GK md.23–31 ile kıymeti yukarı çekebilir. O hâlde:
- **GV artar** → `L4_econ` artar → ters modelde `CIF_TRY_max` **düşmez**
  (üst sınır ticari; artan sadece fiilî maliyettir) ama **fiilî marj erir**;
- **ÖTV değişmez** (maktu, `EV-2026-08-09-113`);
- **KDV nakit çıkışı artar**, ekonomik maliyet **0 kalır** — *7846 lafzî yorumu
  geçerliyse* (§4.1, `T-173`).

**Yani kıymet riskinin en tehlikeli kanalı hâlâ gümrük vergisidir ve
DÜ menşede (%70) AB/Şili'ye (%50) göre 1,4 kat ağırdır.**
