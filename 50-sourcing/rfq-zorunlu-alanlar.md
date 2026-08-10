# RFQ ZORUNLU CEVAP ALANLARI — M1…M8

```yaml
belge:                 rfq-zorunlu-alanlar
sahibi:                global-sourcing-kasifi
tur:                   TUR 3A — RFQ ZORUNLU TEKNIK ALANLAR
tarih:                 2026-08-10
uygulandigi_surum:     50-sourcing/rfq-template.md v2.2
zorunlu_alan_sayisi:   8   (M1…M8)
yeni_supplier_arama:   YOK
web_arama:             YOK
dis_iletisim:          NONE — hicbir ureticiye e-posta/form/mesaj GONDERILMEDI
yeni_evidence:         YOK — 10-evidence/ dokunulmadi
```

---

## 0. BU BELGE NE YAPAR, NE YAPMAZ

**Yapar:** RFQ v2.1'de **sorulan ama cevapsız bırakılabilen** 8 teknik alanı,
**boş bırakılamaz** hâle getirir. Her biri için (a) neden zorunlu, (b) kabul
edilebilir cevap formatı, (c) reddedilecek cevap kalıpları, (d) cevapsızlık
kuralı, (e) beslediği model girdisi ve boş kalırsa `UNKNOWN` dönen hesap yazılır.

**Yapmaz:** Yeni tedarikçi/ülke/fiyat araştırması yapmaz. Vergi oranı, navlun
tutarı, ruhsat sonucu veya kanal marjı **üretmez**. Bu belgedeki vergi, lojistik
ve mevzuat referanslarının **tamamı** ilgili ajanların çıktılarından **alıntıdır**
ve kaynağı satır satır gösterilmiştir.

---

## 1. NEDEN BU 8 ALAN — ÖLÇÜLMÜŞ BOŞLUK

RFQ v2.1 bu 8 alanı **zaten soruyordu** (`rfq-alan-kontrolu.md`, 25/25 "soruluyor").
Sorun soru eksikliği değil, **doluluk**: soru var, veri yok. Mevcut kayıtlardaki
fiili doluluk:

| # | Alan | `supplier-shortlist-v2.csv` (26 satır) | `tedarikci-havuzu.csv` (11 satır) |
|---|---|---|---|
| M1 | ABV | kolon yok | **11/11 `UNKNOWN`** (`abv_pct`) |
| M2 | Bottle weight | **26/26 `UNKNOWN`** | 11/11 kolon yok (yeni kolon planlı) |
| M3 | Case configuration | **25/26 `UNKNOWN`** | **11/11 `UNKNOWN`** (`bottles_per_case`, `case_gross_weight_kg`, `case_dims_cm`) |
| M4 | Pallet configuration | **25/26 `UNKNOWN`** | **11/11 `UNKNOWN`** (`cases_per_pallet`, `pallet_gross_weight_kg`) |
| M5 | Label requirements | `label_cost` 21/26 `UNKNOWN`; uyarlama kabiliyeti kolon yok | `label_customization` kısmen |
| M6 | Origin document | kolon yok | **11/11 `UNKNOWN`** (`origin_proof_doc`) |
| M7 | Certificate set | **24/26 `UNKNOWN`** | **11/11 `UNKNOWN`** (`analysis_certificates`) |
| M8 | Turkey export experience | **23/26 `UNKNOWN`** | **10/11 `UNKNOWN`** (`exported_to_turkey_before`) |

> **26 tedarikçi kaydının hiçbirinde bu 8 alanın tamamı doğrulanmamıştır.**
> M2 (şişe ağırlığı) **26/26**, M6 (menşe belgesi) **11/11** boştur.

Bu boşluk TUR 2.5'te 10 negotiation card'ın **`Critical unknowns`** bloklarında
tekrar tekrar göründü ve iki ajanın açık ticket'ının konusudur:
`T-302` (case & pallet spec sheet — `navlun-lojistik-uzmani`, HIGH, OPEN) ve
`T-312` (menşe local charge / rota asimetrisi — HIGH, OPEN).

---

## 2. ZORUNLULUK MEKANİĞİ — ŞABLONDA NASIL UYGULANIR

RFQ v2.2'de üç katmanlı bir zorlama vardır:

| Katman | Ne | Nerede |
|---|---|---|
| **1. Görsel işaret** | `[MANDATORY]` etiketi + satırın koyu yazılması | SUMMARY SHEET satırı ve detay sorusu |
| **2. Format kısıtı** | "Unit / format" sütununda **kabul edilen birim ve biçim**; belirsiz ifadelerin açıkça reddi | SUMMARY SHEET §0 tablosu |
| **3. Sonuç kuralı** | Eksik cevabın teklife ne yaptığı üreticiye **önceden yazılı olarak** bildirilir | §0'ın hemen altındaki `MANDATORY FIELDS` kutusu |

**Paralel liste yaratılmamıştır.** M1…M8 kodları SUMMARY SHEET satırlarının
üzerine bindirilmiştir; ikinci bir soru bloğu **yoktur**:

| Kod | SUMMARY SHEET satırı | Durum |
|---|---|---|
| **M1** ABV | **S5** | mevcut satır → `[MANDATORY]` |
| **M2** Bottle weight | **S7** | mevcut satır genişletildi (boş **ve** dolu ağırlık) → `[MANDATORY]` |
| **M3** Case configuration | **S8** | mevcut satır → `[MANDATORY]` |
| **M4** Pallet configuration | **S9** | mevcut satır → `[MANDATORY]` |
| **M5** Label requirements | **S26** | **yeni satır** (v2.1'de özet tabloda karşılığı yoktu; detayda 4.6/6.8/6.9 vardı) |
| **M6** Origin document | **S27** | **yeni satır** (v2.1'de S23'ün içine gömülüydü; ayrıştırıldı) |
| **M7** Certificate set | **S23** | mevcut satır daraltıldı (menşe belgesi S27'ye taşındı) → `[MANDATORY]` |
| **M8** Turkey export experience | **S24** | mevcut satır → `[MANDATORY]` |

SUMMARY SHEET **S1–S27**'ye çıkmıştır. S26 ve S27 **yeni soru değildir** —
detay bölümlerinde (4.6, 6.8, 6.9, 6.1) zaten sorulan içeriğin özet tabloya
taşınmasıdır. Amaç, üreticinin kaçırmasının **zorlaştırılmasıdır**.

---

## 3. ALAN KARTLARI

Her kart aynı 6 bloktan oluşur:
`NEDEN ZORUNLU` · `KABUL EDİLEBİLİR FORMAT` · `REDDEDİLEN CEVAP` ·
`BESLEDİĞİ MODEL GİRDİSİ` · `BOŞ KALIRSA UNKNOWN DÖNEN HESAP` · `CEVAPSIZLIK`

---

### M1 — ABV (alkol derecesi) · `[MANDATORY]` · S5 · detay 1.4

**NEDEN ZORUNLU**

Üç ayrı zincir ABV'ye bağlıdır — **ve bunların hiçbiri ÖTV tutarı değildir:**

1. **Etiket.** `mevzuat-ruhsat-uzmani`'nın bulgusu (alıntı, `EV-2026-08-09-221`):
   şarap etiketinde ABV karakter büyüklüğü **≥3 mm** (20–100 cl kaplarda) ve
   ABV toleransı **±%0,5**. Etiket tasarımı ABV rakamı olmadan kapatılamaz;
   menşe etiketinin Türkiye kuralına uyup uymadığı da bu rakama bakılarak
   değerlendirilir.
2. **Beyan satırı.** `gumruk-vergi-uzmani`'nın bulgusu (alıntı,
   `EV-2026-08-09-101`): 2204.21 içindeki **12 haneli kırılım ABV ve PDO/PGI'ye
   dayanır.** Beyanname bu kırılım olmadan doldurulamaz.
3. **Ürün uygunluğu.** ABV, ürünün modelde varsayılan yapının (durgun şarap,
   ≤2 lt kap) içinde olduğunun teyididir.

> ⚠ **ABV ÖTV TUTARINI DEĞİŞTİRMEZ.** `gumruk-vergi-uzmani`, ÖTV maktu tutarının
> **her bir LİTRE** üzerinden olduğunu ve **ABV'den bağımsız** olduğunu
> `FACT` olarak tespit etmiştir (`EV-2026-08-09-113`). Aynı şekilde 12 haneli
> alt kod **vergi yükünü değiştirmez** (`EV-2026-08-09-102`).
> **Bu alanı "vergiyi etkiliyor" diye gerekçelendirmek yanlış olurdu ve
> burada yapılmamıştır.**

**KABUL EDİLEBİLİR FORMAT**

```
<sayı> % vol  — bir ondalık basamak — teklif edilen HASAT YILI için
örn: "12,5 % vol (2025 hasadı)"
+ zorunlu ek: "Bu rakam etikette basılacak rakamdır: EVET / HAYIR"
+ birden fazla hasat yılı teklif ediliyorsa HER YIL için ayrı satır
```

Aralık **yalnızca** şu koşulla kabul edilir: iki uç da yazılır **ve** üst uç
"sözleşmeye yazılabilecek azami değer" olarak beyan edilir
(örn. `12,0–13,0 % vol; sözleşme azamisi 13,0`).

**REDDEDİLEN CEVAP**

`"yaklaşık 12"` · `"standart"` · `"genelde 12–13"` · `"tipik olarak"` ·
`"vintage'a göre değişir"` (rakamsız) · `"analiz sertifikasında yazacak"`
(teklif anında rakam verilmeden) · sadece `"12"` (birim yok).

**BESLEDİĞİ MODEL GİRDİSİ**

`80-model/inputs/urun.yaml → urun.abv_pct` (bugün `null` / `UNKNOWN`)
`80-model/inputs/ruhsat.yaml → urun_uygunlugu.*`
`50-sourcing/tedarikci-havuzu.csv → abv_pct` (**11/11 `UNKNOWN`**)

**BOŞ KALIRSA `UNKNOWN` DÖNEN HESAP**

- Etiket tasarım kapatma → `ruhsat.yaml → urun_uygunlugu` zinciri açılamaz;
  `20-mevzuat/t0-takvimi.md`'deki ilk satışa kadar geçen süre **`UNKNOWN`** kalır.
- **Vergi bacağı `UNKNOWN` DÖNMEZ** — ÖTV litre bazlıdır. Bu, dürüstlük gereği
  yazılmıştır: M1'in maliyet modeline doğrudan sayısal etkisi yoktur.

**CEVAPSIZLIK** → `INCOMPLETE`. Tek takip. Gelmezse teklif **fiyat karşılaştırma
tablosuna girer** (fiyat ABV'den bağımsızdır) ama **ürün uygunluk hattına girmez**;
tedarikçi `PRODUCT_SPEC_UNVERIFIED` işaretlenir.

---

### M2 — Şişe ağırlığı (boş **ve** dolu) · `[MANDATORY]` · S7 · detay 1.14, 1.15

**NEDEN ZORUNLU**

`navlun-lojistik-uzmani` şu anda **bant** kullanıyor: şişe başına paketli hacim
`0,00223 / 0,00239 / 0,00360 m³` (`T-302`, `EV-2026-08-09-307`) ve bu bant bir
**tedarikçi verisinden değil**, üçüncü taraf bir palet spec sheet'inden **geri
hesaplanmıştır**. Boş cam ağırlığı olmadan koli brüt ağırlığı (M3) **çapraz
kontrol edilemez** — yani tedarikçinin verdiği koli ağırlığının doğru olup
olmadığını anlamanın başka yolu yoktur.

Ayrıca ağırlık, konteynerin **hacim-kısıtlı mı ağırlık-kısıtlı mı** yükleneceğini
belirler; `lojistik.yaml → karayolu_agirlik` bloğu buna bağlıdır.

**KABUL EDİLEBİLİR FORMAT**

```
(a) Boş cam ağırlığı  : <sayı> g   — cam tedarikçisinin beyanı; tolerans ± <sayı> g
(b) Dolu şişe brüt    : <sayı> g   — şarap + cam + kapak + kapsül + etiketler
(c) Şişe formu        : Bordeaux / Burgundy / Alsace / özel kalıp
(d) Şişe dış çapı     : <sayı> mm  (gövdenin en geniş noktası)
(e) Şişe yüksekliği   : <sayı> mm
```

(c)(d)(e) `T-302`'nin 1–3 numaralı maddelerinin doğrudan karşılığıdır ve
**ağırlıkla birlikte zorunludur**: Burgundy formu şişe, aynı ağırlıkta bile
konteyner kapasitesini **%38 düşürür**.

**REDDEDİLEN CEVAP**

`"standart Bordeaux şişe"` (rakamsız) · `"hafif şişe"` · `"yaklaşık 400 g"` ·
`"1,2 kg dolu"` (hangi bileşenler dahil belirtilmeden) · yalnızca (a) verilip
(b) verilmemesi · yalnızca "12'li koli 15 kg" denip şişe bazına inilmemesi.

**BESLEDİĞİ MODEL GİRDİSİ**

`urun.yaml → sise_spesifikasyonu.bos_sise_agirligi_g`, `.dolu_sise_brut_agirligi_g`
`lojistik.yaml → urun_fizik.bos_cam_agirlik_g`, `.dolu_sise_brut_agirlik_kg`,
`.paketli_sise_agirlik_kg`

**BOŞ KALIRSA `UNKNOWN` DÖNEN HESAP**

- `lojistik.yaml → konteyner.sise_kapasitesi_*` bant kalır → **şişe başına navlun
  bant kalır** → CIF bant kalır → `MAX_FOB`/`MAX_EXW` köprüsü kurulamaz.
- `karayolu_agirlik` kontrolü (yüklü konteynerin karayolu ağırlık sınırını aşıp
  aşmadığı) **yapılamaz**.

**CEVAPSIZLIK** → `INCOMPLETE`. Tek takip. Gelmezse **teklif fiyat karşılaştırmasına
girmez**: şişe başına navlun hesaplanamadığı için EXW/FOB fiyatı CIF'e
çevrilemez ve `RFQ TARGET CEILING X/Y` ile karşılaştırılamaz.
**Bu, teklifi değerlendirme dışı bırakan 3 alandan biridir (M2, M3, M4).**

---

### M3 — Koli konfigürasyonu · `[MANDATORY]` · S8 · detay 2.1, 2.2, 2.3, 2.4

**NEDEN ZORUNLU**

`T-302`'nin (HIGH, OPEN) tam konusu budur: *"Konteyner kapasitesi hesabımın tek
en kırılgan girdisi, şişe başına paketli hacimdir… 0,00223 → 0,00360 geçişi tüm
konteyner kapasitelerini **%38 düşürür**."*

%38'lik bir kapasite sapması, şişe başına navlunu **aynı oranda** değiştirir ve
bu doğrudan CIF'e, CIF de `MAXIMUM STRUCTURAL BUY PRICE` karşılaştırmasına girer.

**KABUL EDİLEBİLİR FORMAT**

```
(a) Şişe/koli          : 6 / 12 / <diğer>  + "değiştirilebilir mi: EVET/HAYIR"
(b) Koli DIŞ ölçüsü    : <U> × <G> × <Y> mm   (iç ölçü DEĞİL)
(c) Koli brüt ağırlığı : <sayı> kg
(d) Koli net ağırlığı  : <sayı> kg
(e) Katman düzeni      : <koli/katman> × <katman sayısı>
(f) Ara bölme/insert   : var / yok  (hacme etkisi için)
```

Ölçü birimi mm veya cm olabilir, **ama birim yazılmalıdır**. Üç boyutun
**hepsi** gereklidir; iki boyut kabul edilmez.

**REDDEDİLEN CEVAP**

`"standart 12'li koli"` · `"normal karton"` · `"yaklaşık 30×25×35"` (birimsiz) ·
`"koli ölçüsü spec sheet'te"` (spec sheet eklenmeden) · iç ölçü verilmesi ·
brüt/net ayrımı yapılmadan tek ağırlık verilmesi.

**BESLEDİĞİ MODEL GİRDİSİ**

`lojistik.yaml → urun_fizik.koli_formati`, `.koli_brut_agirlik_kg`,
`.paketli_sise_hacim_m3`, `.paketli_sise_agirlik_kg`
`tedarikci-havuzu.csv → bottles_per_case`, `case_gross_weight_kg`, `case_dims_cm`

**BOŞ KALIRSA `UNKNOWN` DÖNEN HESAP**

`konteyner.sise_kapasitesi_hacim_kisitli_paletli` → **şişe başına navlun (USD)**
→ **CIF** → tedarikçinin tavan bandına göre konumu. Zincirin tamamı düşer.

**CEVAPSIZLIK** → `INCOMPLETE` → takip → **değerlendirme dışı** (M2 ile aynı
gerekçe). `T-302`'nin kapanması bu alana bağlıdır.

---

### M4 — Palet konfigürasyonu · `[MANDATORY]` · S9 · detay 2.5, 2.6, 2.7, 2.8, 2.9

**NEDEN ZORUNLU**

Koli ölçüsü tek başına yetmez: konteynere **paletli** yüklemede belirleyici olan
palet ayak izi, yüklü palet yüksekliği ve konteyner başına palet adedidir.
`lojistik.yaml → konteyner.palet_sayisi` bugün dört ayrı senaryo
(`dv20_std`, `dv20_euro`, `hc40_std`, `hc40_euro`) taşıyor — hangisinin geçerli
olduğu **tedarikçinin palet tipine** bağlıdır. `T-461` (paletsiz/slipsheet
14.112 şişe iddiası) da aynı belirsizliğin sonucudur.

ISPM-15 (ısıl işlem) sorusu ayrıca zorunludur: ısıl işlemsiz ahşap palet
**sevkiyatı durdurabilir**; bu bir maliyet değil, bir **teslim riski** kalemidir.

**KABUL EDİLEBİLİR FORMAT**

```
(a) Palet tipi          : EUR 800×1200 / STD 1000×1200 / GMA / diğer <ölçü mm>
(b) ISPM-15 ısıl işlem  : EVET / HAYIR  (+ damga var mı)
(c) Koli/palet          : <sayı>       (d) Şişe/palet : <sayı>
(e) Katman sayısı       : <sayı>
(f) Yüklü palet brüt    : <sayı> kg
(g) Yüklü palet yüksek. : <sayı> mm  (palet dahil, toplam)
(h) 20' DV'ye kaç palet / kaç koli, 40' HC'ye kaç palet / kaç koli
(i) Paletsiz (floor-loaded) yükleme mümkün mü: EVET/HAYIR + 20' DV'ye kaç koli
```

**REDDEDİLEN CEVAP**

`"Euro palet"` (koli/palet ve yükseklik verilmeden) · `"konteynere 20 palet
girer"` (palet tipi belirtilmeden) · `"kapasite yükleme planına göre değişir"` ·
(h)'nin cevapsız bırakılması · (b)'nin cevapsız bırakılması.

**BESLEDİĞİ MODEL GİRDİSİ**

`lojistik.yaml → urun_fizik.palet_basina_sise.*`, `.yuklu_palet_brut_kg.*`,
`.yuklu_palet_yukseklik_mm`, `konteyner.palet_sayisi.*`
`tedarikci-havuzu.csv → cases_per_pallet`, `pallet_gross_weight_kg`

**BOŞ KALIRSA `UNKNOWN` DÖNEN HESAP**

- Konteyner doluluk hesabı **paletli senaryoda** kurulamaz → `T-402`
  (20DV/40HC'ye kaç şişe) cevaplanamaz.
- LCL'de **W/M (hacim/ağırlık) ücretlendirme tabanı** hesaplanamaz.
- `T-461` çelişkisi (paletli ↔ paletsiz kapasite) çözülemez.

**CEVAPSIZLIK** → `INCOMPLETE` → takip → **değerlendirme dışı** (M2/M3 ile aynı).

---

### M5 — Etiket gereksinimleri (uyarlama kabiliyeti) · `[MANDATORY]` · S26 · detay 4.6, 6.8, 6.9

**NEDEN ZORUNLU**

Bu alan **etiket maliyeti değildir** (o S19). Bu alan, **Türkiye'nin zorunlu
etiket unsurlarının menşede uygulanabilir olup olmadığıdır** ve cevabı
ithalatçının maliyet yapısını **bir kalemi tamamen kaldıracak veya ekleyecek**
biçimde değiştirir.

`mevzuat-ruhsat-uzmani`'nın bulguları (**alıntı**, bu ajan mevzuat sonucu
üretmez):

| Bulgu | Kaynak | RFQ'ya etkisi |
|---|---|---|
| Türkçe etiket **menşede** basılabiliyorsa yasaklayıcı hüküm bulunamadı; ancak **bandrol yine Türkiye'de antrepoda** uygulanır | `EV-2026-08-09-212`, `-219` | Şişe/etiket üzerinde **bandrol için boş alan** taahhüdü gerekir |
| Sağlık uyarısı 750 ml şişede **≥18 cm²** yer kaplar (3 grafik + 1 yazılı, ≥10 punto) | `EV-2026-08-09-220` | Arka etiketin **fiziksel boyutu** buna yetmelidir — bu bir tasarım değil, **kalıp/kesim bıçağı** sorusudur |
| ABV karakter büyüklüğü **≥3 mm** | `EV-2026-08-09-221` | Menşe etiketi uyumsuzsa **ayrı Türkçe etiket** zorunlu olur |

Kritik olan şudur: eğer üretici Türkçe arka etiketi **kendi tesisinde**
uygulayabiliyorsa, Türkiye'deki etiketleme operasyonu (**L5 kalemi**) **tamamen
kalkar**. Uygulayamıyorsa, L5'e bugün **ölçülmemiş** bir kalem eklenir.
İki senaryo arasındaki fark ölçülmemiştir — ve ancak bu cevapla ölçülebilir.

> ⚠ **Bu satırdaki mevzuat gereklilikleri `mevzuat-ruhsat-uzmani`'nın
> alanıdır ve RFQ'ya konmadan önce onun teyidini gerektirir → `T-881`.**
> Buradaki listenin RFQ'da tedarikçiye **hangi kesinlikte** yazılacağı
> (özellikle ≥18 cm² alan ve bandrol boş alanı) o ticket'a bağlıdır.

**KABUL EDİLEBİLİR FORMAT** — beş alt soru, **her biri EVET/HAYIR + açıklama**

```
(a) Bizim sağladığımız artwork ile TÜRKÇE ARKA ETİKETİ kendi tesisinizde
    uygulayabilir misiniz?                      EVET / HAYIR
    EVET ise: şişe başı bedel <para birimi + tutar>, lead time'a etkisi <gün>
(b) Arka etikette en az 18 cm² BASILABİLİR ALAN sağlayabilir misiniz?
                                                EVET / HAYIR + mevcut etiket ölçüsü <mm × mm>
(c) Şişe veya etiket üzerinde, ithalatçı tarafından uygulanacak bir bandrol/şerit
    için BOŞ ALAN bırakabilir misiniz?          EVET / HAYIR + alan ölçüsü <mm × mm> + konumu
(d) Etiketi ithalatçı ülkenin zorunlu beyanlarına (alerjen, ithalatçı bilgisi,
    sağlık uyarısı) göre uyarlayabilir misiniz? EVET / HAYIR + revizyon süresi <gün>
(e) ABV'yi ≥3 mm karakter yüksekliğiyle basabilir misiniz? EVET / HAYIR
```

**REDDEDİLEN CEVAP**

`"etiket konusunda esnekiz"` · `"müşteri talebine göre"` · `"tabii ki"` ·
`"her türlü etiket yapılır"` · EVET/HAYIR verilip **ölçü/bedel/süre**
verilmemesi · (c)'nin cevapsız bırakılması (bandrol Türkiye tarafında
uygulanacağı için **fiziksel alan taahhüdü** gerekir).

**BESLEDİĞİ MODEL GİRDİSİ**

`80-model/inputs/tedarikci.yaml → private_label.turkce_arka_etiket_menside_uygulanabilir_mi`
`80-model/inputs/ruhsat.yaml → urun_uygunlugu.*`
`80-model/inputs/lojistik.yaml → bandrolleme_operasyonu.*` (boş alan ön koşulu)
`tedarikci-havuzu.csv → label_customization`

**BOŞ KALIRSA `UNKNOWN` DÖNEN HESAP**

- **L5 (importer cost)** içindeki Türkiye etiketleme operasyonu kalemi:
  var mı yok mu bilinmez → L5 → L6 zinciri bant kalır.
- Bandrolleme operasyonu fizibilitesi (`lojistik.yaml → bandrolleme_operasyonu`)
  **fiziksel ön koşulu doğrulanmadan** hesaplanmış olur.
- `T-403` (Türkçe arka etiket menşede mi Türkiye'de mi — `mevzuat-ruhsat-uzmani`,
  OPEN) tedarikçi tarafı **cevapsız** kalır.

**CEVAPSIZLIK** → `INCOMPLETE`. Tek takip. Gelmezse teklif fiyat
karşılaştırmasına **girer** ama `LABEL_PATH_UNVERIFIED` işaretlenir ve
L5 hesabında Türkiye etiketleme kalemi **`UNKNOWN` olarak taşınır** —
sıfır kabul edilmez.

---

### M6 — Menşe ispat belgesi taahhüdü · `[MANDATORY]` · S27 · detay 6.1, 6.2 + OD-1…OD-5

**NEDEN ZORUNLU — BU, LİSTEDEKİ EN PAHALI ALANDIR**

`gumruk-vergi-uzmani`'nın tespiti (**alıntı**, `mense-tarife-eslemesi.md` §1/§5,
`EV-2026-08-09-103/-104/-105`, `EV-2026-08-10-165`): tercihli oran
**koşulludur** ve koşulun iki bacağı (**K2 menşe kuralı**, **K3 geçerli belge**)
**tedarikçiye bağlıdır**.

`finans-fizibilite`'nin ters modelinden (alıntı, `reverse-price-model.md` §4.2):

```
MAX_CIF(g=0,70) / MAX_CIF(g=0,50) = 1,50 / 1,70 = 0,88235
```

> **Tercihli rejimi kaybetmek azami alım fiyatını TAM %11,765 düşürür.**
> 799 TL / CHAIN / BASE / 5.000 şişe çapasında bu **−32,10 TRY/şişe**'dir
> (`rfq-negotiation-cards.md` §0.4). Bu, kartlardaki **tek en büyük pazarlık
> kalemidir** ve `UNKNOWN`'a bağlı değildir.

Yani: M6 cevapsız kalırsa, P grubundaki **7 tedarikçinin tamamı** için tavan
**DOC_FAIL** varsayımıyla hesaplanmak zorundadır — yani tercihli menşe
avantajı **karar aşamasında yok sayılır**.

**KABUL EDİLEBİLİR FORMAT** — OD-1…OD-5'in RFQ karşılığı, **taahhüt olarak**

```
(a) Hangi belgeyi düzenleyebiliyorsunuz? (BELGE ADI — "evet" kabul edilmez)
    ☐ EUR.1 dolaşım belgesi   ☐ fatura beyanı   ☐ REX menşe beyanı
    ☐ A.TR   ☐ yalnızca tercihsiz menşe şahadetnamesi   ☐ hiçbiri
(b) HER SEVKİYAT için düzenlemeyi SÖZLEŞMEYLE taahhüt eder misiniz? EVET/HAYIR   [OD-1]
(c) "Onaylanmış ihracatçı" statünüz var mı; fatura beyanının değer eşiği
    aşılırsa EUR.1'e geçer misiniz?                                  EVET/HAYIR   [OD-2]
(d) Şarap TAMAMEN menşe ülkede mi üretildi ve şişelendi; dökme ithal
    bileşen var mı?                            YOK / VAR → <ülke, oran %>          [OD-3]
(e) Sevkiyat hangi ÜLKENİN limanından çıkacak; üçüncü ülkede konsolide
    edilecek mi?                               <liman + ülke> / konsolidasyon YOK  [OD-4]
(f) Belge düzenlenemez veya gümrükte reddedilirse, sözleşmeye bir FİYAT
    DÜZELTME maddesi kabul eder misiniz?                             EVET/HAYIR   [OD-5]
```

**Grup N (tercihsiz menşe — ör. AU, MD) için:** `(a) = hiçbiri` **tam ve kabul
edilebilir bir cevaptır**. Bu tedarikçilerde (b)(c)(f) `N/A`'dır. **Ancak
tedarikçi "belgeleri biz hallederiz" gerekçesiyle prim isteyemez** — düzenlenecek
tercihli belge yoktur (`rfq-negotiation-cards.md` §0.6).

**REDDEDİLEN CEVAP**

`"evet, menşe belgesi veririz"` (belge adı yok) · `"gerekli tüm evrakı
sağlarız"` · `"gümrük müşavirimiz halleder"` · `"AB menşeli olduğu için
sorun yok"` · (d)'nin cevapsız bırakılması (dökme ithal bileşen K2'yi bozar —
**private label'da yüksek risk**) · (e)'nin cevapsız bırakılması.

**BESLEDİĞİ MODEL GİRDİSİ**

`tedarikci.yaml → belgeler.mense_ispat_belgesi`
`tedarikci-havuzu.csv → origin_proof_doc` (**11/11 `UNKNOWN`**)
`vergi.yaml → gumruk_vergisi` oranının **hangi senaryoda** uygulanacağı
(oranın kendisi `gumruk-vergi-uzmani`'nındır — biz yalnızca **belge
düzenlenebilirliğini** kaydederiz)

**BOŞ KALIRSA `UNKNOWN` DÖNEN HESAP**

`MAX_CIF_TRY` → tedarikçi başına tavan **DOC_FAIL** kolonundan okunur:
P grubu için **290,51 → 256,34 TRY/şişe** (Y köşesi). Yani cevapsızlık
**doğrudan −%11,765 tavan daralması** olarak modele girer — bu, `UNKNOWN`
değil, **cezalı varsayımdır** ve modelin **aleyhimize** çalışmasını sağlar.

**CEVAPSIZLIK** → `INCOMPLETE`. Tek takip. Gelmezse teklif **elenmez** ama
**`DOC_FAIL` varsayımıyla** değerlendirilir. Bu, listedeki tek "cezalandır ama
eleme" kuralıdır ve bilinçlidir: eleme, tedarikçiye tercih kaybını sessizce
bize yükleme fırsatı verirdi.

---

### M7 — Sertifika seti · `[MANDATORY]` · S23 · detay 6.3, 6.4, 6.5, 6.10, 6.11

**NEDEN ZORUNLU**

`mevzuat-ruhsat-uzmani`'nın bulgusu (**alıntı**): şişelenmiş üründe rejim dosya
üzerinden yürür, kontroller risk esaslıdır; **talep hâlinde üretici analiz
raporu 3 hafta içinde ibraz edilir** (`20-mevzuat/ruhsat-sureci.md`, Ticaret
Yön. m.13). Ayrıca `T-206` (şişelenmiş ithal şarapta zorunlu analiz var mı,
parti başı mı — OPEN) hâlâ açıktır ve `analiz_maliyeti_per_parti` model girdisi
bilinçli olarak `null` bırakılmıştır.

Yani: analiz sertifikasının **hangi parametreleri içerdiği** ve **akredite bir
laboratuvardan** gelip gelmediği, ithalat dosyasının kapanıp kapanmayacağını
belirler. "Sertifikamız var" cümlesi bu soruyu cevaplamaz.

**KABUL EDİLEBİLİR FORMAT**

```
(a) Analiz sertifikası PARAMETRE LİSTESİ (işaretleyiniz):
    ☐ ABV  ☐ toplam asit  ☐ uçucu asit  ☐ kalıntı şeker  ☐ toplam SO₂
    ☐ metanol  ☐ yoğunluk  ☐ kuru ekstrakt  ☐ diğer: ______
(b) Sertifikayı düzenleyen laboratuvar adı + akreditasyon (ISO 17025 / OIV):
(c) Sertifika PARTİ BAZINDA mı düzenlenir, yoksa ürün bazında mı?  PARTİ / ÜRÜN
(d) Sağlık / serbest satış sertifikası (ulusal makam onaylı): EVET/HAYIR + belge adı
(e) Gıda güvenliği sertifikaları: ☐ BRCGS ☐ IFS ☐ ISO 22000 ☐ HACCP ☐ yok
    → geçerlilik tarihi ve **kopyası ekte** (ek yoksa cevap eksiktir)
(f) İzlenebilirlik: şişe lot → tank → hasat bağlantısı belgelenebilir mi? EVET/HAYIR
```

**REDDEDİLEN CEVAP**

`"tüm sertifikalarımız mevcuttur"` · `"AB standartlarına uygundur"` ·
`"analiz raporu veriyoruz"` (parametre listesi yok) · (e)'de kutu işaretlenip
**belge kopyası eklenmemesi** · (b)'de laboratuvar adı verilmemesi.

**BESLEDİĞİ MODEL GİRDİSİ**

`tedarikci.yaml → belgeler.analiz_sertifikasi`
`tedarikci-havuzu.csv → analysis_certificates` (**11/11 `UNKNOWN`**)
`ruhsat.yaml → urun_uygunlugu.*`, `analiz_laboratuvar.*` (bugün `null`)

**BOŞ KALIRSA `UNKNOWN` DÖNEN HESAP**

- `ruhsat.yaml → analiz_laboratuvar.*` doldurulamaz → `T-206` tedarikçi tarafı
  cevapsız → **parti başı analiz maliyeti `UNKNOWN` kalır** (5.000 şişelik
  pilotta şişe başına anlamlı olabilecek bir kalem).
- `20-mevzuat/t0-takvimi.md` → ilk sevkiyatın gümrükten çıkış süresi
  **`UNKNOWN`** kalır → `peak_cash_requirement`'ın süresi bilinmez.

**CEVAPSIZLIK** → `INCOMPLETE`. Tek takip. Gelmezse teklif fiyat
karşılaştırmasına girer, ancak **pilot sevkiyat adayı olamaz**
(`PILOT_INELIGIBLE`): dosyası kapanmayacak bir tedarikçiyle ilk sevkiyat
yapılmaz. Karşılaştırmadan çıkarılmaz çünkü fiyat bilgisi yine de bilgidir.

---

### M8 — Türkiye'ye ihracat geçmişi · `[MANDATORY]` · S24 · detay 6.6 (+5.2, 5.3)

**NEDEN ZORUNLU**

**26 tedarikçi kaydının hiçbirinde doğrulanmamıştır** (`supplier-shortlist-v2.csv`
`turkey_export_experience` 23/26 `UNKNOWN`; `tedarikci-havuzu.csv`
`exported_to_turkey_before` 10/11 `UNKNOWN`). `turkiye-pazar-kasifi`'nin `T-464`
cevabı da **"bulunamadı ≠ yok"** ile kapanmıştır — yani dışarıdan bakarak
öğrenilemeyeceği kanıtlanmıştır. **Bu alanı yalnızca tedarikçinin kendisi
cevaplayabilir.**

Neden önemli: Türkiye'ye daha önce ihracat yapmış bir üretici, bandrol için
boş alan, Türkçe arka etiket, TADAB dosyası ve ödeme/akreditif pratiğini
**daha önce görmüştür**. Görmemişse, ilk sevkiyatta bunların her biri bir
gecikme kaynağıdır.

> ⚠ **DÜRÜSTLÜK NOTU: M8 hiçbir hesabı `UNKNOWN` döndürmez.** Sayısal bir model
> girdisi beslemez. Bu alan bir **yürütme riski göstergesidir** ve tam da bu
> nedenle "cevapsızlık = eleme" kuralı M8'e **uygulanmaz.** Bunu yazmak, listenin
> geri kalanının ciddiyetini korur — her alana `CRITICAL` demek hiçbir alanı
> `CRITICAL` yapmaz.

**KABUL EDİLEBİLİR FORMAT**

```
(a) Türkiye'ye daha önce ihracat yaptınız mı?   EVET / HAYIR
    EVET ise zorunlu: ithalatçı adı, yıllar (<yyyy>–<yyyy>), yıllık hacim (şişe veya lt)
    HAYIR ise zorunlu: "Türkiye'ye ilk sevkiyat için ek şartınız var mı?" → EVET/HAYIR + açıklama
(b) Türkiye'de hâlihazırda bir ithalatçınız/distribütörünüz var mı? EVET/HAYIR + bölge kapalı mı
(c) (Model A ise) Bu marka Türkiye'de daha önce satıldı mı; kim, hangi yıllar,
    hangi hacim, neden durdu?
```

**`HAYIR` tam ve kabul edilebilir bir cevaptır.** Eksik olan tek şey **sessizliktir.**

**REDDEDİLEN CEVAP**

`"birçok ülkeye ihracat yapıyoruz"` (Türkiye'ye özel cevap yok) ·
`"Orta Doğu'ya satıyoruz"` · `"sanırım vardı"` · EVET denip ithalatçı/yıl/hacim
verilmemesi · sorunun tamamen atlanması.

**BESLEDİĞİ MODEL GİRDİSİ**

`tedarikci.yaml → risk.turkiyeye_ihracat_gecmisi`
`tedarikci-havuzu.csv → exported_to_turkey_before`
`supplier-shortlist-v2.csv → turkey_export_experience`
**Sayısal model girdisi yoktur** — `seytanin-avukati` ve tedarikçi risk
sıralaması girdisidir.

**BOŞ KALIRSA `UNKNOWN` DÖNEN HESAP**

**Hiçbiri.** Etkisi niteliksel: tedarikçi `EXECUTION_RISK_UNVERIFIED` işaretlenir
ve pilot sevkiyat sıralamasında **geriye** düşer. Ayrıca Model A'da (b)/(c)
cevapsızsa **münhasırlık müzakeresi başlatılamaz** — `T-465` açık kalır.

**CEVAPSIZLIK** → `INCOMPLETE`. Tek takip. Gelmezse teklif **elenmez**,
`EXECUTION_RISK_UNVERIFIED` etiketiyle taşınır.

---

## 4. CEVAPSIZLIK KURALI — TEK YERDE, KADEMELİ

### 4.1 Kademeler

| Kademe | Tetikleyici | Sonuç |
|---|---|---|
| **K0 — kabul** | M1…M8'in **hepsi** kabul edilebilir formatta | Teklif `COMPLETE`; `tedarikci-havuzu.csv`'ye işlenir |
| **K1 — eksik** | Bir veya daha fazla zorunlu alan boş / `TBC` / reddedilen kalıpta | Teklif `INCOMPLETE`. **Tek** takip e-postası, **7 takvim günü** süre. Eksik alan `UNKNOWN` yazılır — **tahminle doldurulmaz** (`CLAUDE.md` §1.1) |
| **K2 — cevapsız** | Takip sonrası hâlâ eksik | Alan bazında sonuç uygulanır (§4.2). Tedarikçi havuzdan **silinmez**; `UNKNOWN` ile kalır |

### 4.2 Alan bazında K2 sonucu — **hepsi aynı değildir**

| Alan | K2 sonucu | Gerekçe |
|---|---|---|
| **M2** şişe ağırlığı | **DEĞERLENDİRME DIŞI** — fiyat karşılaştırmasına girmez | EXW/FOB → CIF köprüsü kurulamaz; teklif tavanla **karşılaştırılamaz** |
| **M3** koli konfig. | **DEĞERLENDİRME DIŞI** | aynı — %38'e varan kapasite sapması |
| **M4** palet konfig. | **DEĞERLENDİRME DIŞI** | aynı — paletli yükleme planı kurulamaz |
| **M6** menşe belgesi | **CEZALI DEĞERLENDİRME** — `DOC_FAIL` varsayımıyla (**−%11,765 tavan**) | Eleme, tedarikçiye tercih riskini sessizce bize yükleme fırsatı verir |
| **M7** sertifika seti | Karşılaştırmaya girer, **`PILOT_INELIGIBLE`** | Dosyası kapanmayacak tedarikçiyle ilk sevkiyat yapılmaz |
| **M1** ABV | Karşılaştırmaya girer, **`PRODUCT_SPEC_UNVERIFIED`** | Fiyat ABV'den bağımsızdır (ÖTV litre bazlı — `EV-2026-08-09-113`) |
| **M5** etiket gereksinimi | Karşılaştırmaya girer, **`LABEL_PATH_UNVERIFIED`**; L5 etiketleme kalemi `UNKNOWN` taşınır — **sıfır kabul edilmez** | Kalem var mı yok mu bilinmiyor; yok saymak projeyi lehine saptırır |
| **M8** TR ihracat geçmişi | Karşılaştırmaya girer, **`EXECUTION_RISK_UNVERIFIED`** | Sayısal model girdisi yok; eleme orantısız olurdu |

### 4.3 Değişmez kurallar

1. **Hiçbir zorunlu alan bizim tarafımızdan tahminle doldurulmaz.** Ne
   `ESTIMATE`, ne "sektör ortalaması", ne başka tedarikçinin verisi.
   (`CLAUDE.md` §1.1, §1.2)
2. **Takip e-postası bir kere gönderilir.** İkinci takip, tedarikçiyi
   fiyat konusunda değil **süreç** konusunda eğitmeye başlar ve pazarlık
   pozisyonunu zayıflatır.
3. **`N/A` ile `TBC` aynı şey değildir.** `N/A` = "bende yok/uygulanmaz" → geçerli
   cevaptır. `TBC` = "henüz bilmiyorum" → K1 sayılır.
4. **`HAYIR` bir eksiklik değildir.** M6 (Grup N), M5(a), M8(a) için `HAYIR`
   tam cevaptır. Eksik olan **sessizliktir.**
5. **Eleme kararı tek başına bu ajanın kararı değildir.** §4.2'nin
   "DEĞERLENDİRME DIŞI" satırları, bugünkü doluluk oranıyla (M2: 26/26 boş)
   uygulanırsa **havuzun tamamını eleyebilir**. Kuralın gönderim öncesi
   onayı başkandadır → **`T-884`**.

### 4.4 Ölçülecek metrik (TUR 7)

Gönderim başına: **M-doluluk oranı = (kabul edilebilir formatta gelen M alanı) / (8 × cevap veren tedarikçi)**.
`rfq-alan-kontrolu.md` §5.1'in uyarısı burada da geçerlidir: ilk 8 gönderimde
M-doluluk %50'nin altındaysa **sorun tedarikçide değil şablondadır** ve
zorunlu alan sayısı düşürülür (öncelik sırası: M2, M3, M4, M6 kalır; M1, M5,
M7, M8 ikinci aşamaya bırakılır).

---

## 5. REDDEDİLEN CEVAP SÖZLÜĞÜ — ORTAK KALIPLAR

Aşağıdaki ifadeler **hiçbir zorunlu alanda** kabul edilmez ve otomatik olarak
K1 tetikler. Bu liste RFQ v2.2'nin `MANDATORY FIELDS` kutusunda üreticiye
**önceden** bildirilir:

| Reddedilen kalıp (TR) | RFQ'daki İngilizce karşılığı |
|---|---|
| yaklaşık / civarında | *approximately, around, circa* |
| standart | *standard* (rakam veya ölçü olmadan) |
| genelde / tipik olarak | *usually, typically* |
| değişir / duruma göre | *varies, depends* (aralık ve uç değer verilmeden) |
| talebe göre | *upon request* (bedel ve süre verilmeden) |
| spec sheet'te yazıyor (ek yok) | *see attached spec* (ek gönderilmeden) |
| evet / mümkün (rakamsız) | *yes / possible* (birim, ölçü veya bedel olmadan) |
| sorun değil | *no problem* |

**Tek istisna:** açıkça `TBC` yazılması. `TBC` reddedilen bir kalıp değildir —
dürüst bir eksikliktir ve K1'e girer. Şablonun kendi ifadesiyle:
*"an honest 'TBC' is more valuable than an approximation."*

---

## 6. MODEL GİRDİSİ EŞLEMESİ — TEK TABLO

| Kod | S satırı | Detay soru | `tedarikci-havuzu.csv` | `80-model/inputs/*` | Boş kalırsa `UNKNOWN` dönen |
|---|---|---|---|---|---|
| M1 | S5 | 1.4 | `abv_pct` | `urun.yaml → urun.abv_pct` | ürün uygunluk hattı, etiket kapanışı (**vergi bacağı DEĞİL**) |
| M2 | S7 | 1.14, 1.15 | `empty_bottle_weight_g`, `filled_bottle_weight_g` *(yeni)* | `urun.yaml → sise_spesifikasyonu.*`; `lojistik.yaml → urun_fizik.bos_cam_agirlik_g`, `.dolu_sise_brut_agirlik_kg` | konteyner ağırlık kısıtı, `karayolu_agirlik`, koli ağırlığı çapraz kontrolü |
| M3 | S8 | 2.1–2.4 | `bottles_per_case`, `case_gross_weight_kg`, `case_dims_cm` | `lojistik.yaml → urun_fizik.paketli_sise_hacim_m3`, `.koli_brut_agirlik_kg`, `.koli_formati` | `konteyner.sise_kapasitesi_*` → **şişe başına navlun** → CIF |
| M4 | S9 | 2.5–2.9 | `cases_per_pallet`, `pallet_gross_weight_kg` | `lojistik.yaml → urun_fizik.palet_basina_sise.*`, `.yuklu_palet_brut_kg.*`, `konteyner.palet_sayisi.*` | paletli konteyner planı, LCL W/M tabanı, `T-402`, `T-461` |
| M5 | **S26** | 4.6, 6.8, 6.9 | `label_customization` | `tedarikci.yaml → private_label.turkce_arka_etiket_menside_uygulanabilir_mi`; `ruhsat.yaml → urun_uygunlugu.*`; `lojistik.yaml → bandrolleme_operasyonu.*` | **L5** içindeki TR etiketleme kalemi → L5→L6 zinciri |
| M6 | **S27** | 6.1, 6.2 | `origin_proof_doc` | `tedarikci.yaml → belgeler.mense_ispat_belgesi` | `MAX_CIF_TRY` **DOC_OK/DOC_FAIL** ayrımı → **±%11,765** |
| M7 | S23 | 6.3–6.5, 6.10, 6.11 | `analysis_certificates` | `tedarikci.yaml → belgeler.analiz_sertifikasi`; `ruhsat.yaml → analiz_laboratuvar.*` | parti başı analiz maliyeti (`T-206`), gümrük çıkış süresi |
| M8 | S24 | 6.6, 5.2, 5.3 | `exported_to_turkey_before` | `tedarikci.yaml → risk.turkiyeye_ihracat_gecmisi` | **hiçbiri** (niteliksel risk göstergesi) |

---

## 7. BU KURALIN KENDİ RİSKLERİ

| # | Risk | Neden gerçek | Ne yaparız |
|---|---|---|---|
| 1 | **Havuzun tamamı elenebilir.** M2 bugün 26/26 boş; kural gönderim öncesi değil **cevap sonrası** işlese bile, cevap oranı düşükse elde teklif kalmaz | Eleme kuralı `DEĞERLENDİRME DIŞI` diyor; ama alternatif "bant kullan" da modeli bozuyordu | Kural **başkan onayına** bağlandı (`T-884`); §4.4 metriği ile şablon kısaltma yolu açık bırakıldı |
| 2 | **Soru sayısı arttı.** v2.2 ile SUMMARY SHEET 25 → 27 satır, M5/M6 alt sorularıyla birlikte ~15 yeni cevap alanı | `rfq-alan-kontrolu.md` §5.1 zaten uyarmıştı: uzun RFQ = daha az cevap | M5/M6 alt soruları **onay kutusu** formatında yazıldı; serbest metin yazma yükü minimum |
| 3 | **M5'in içeriği mevzuat teyidi bekliyor** | ≥18 cm² ve bandrol boş alanı `mevzuat-ruhsat-uzmani`'nın bulgusudur; RFQ'ya hangi kesinlikte yazılacağı onun kararıdır | `T-881` açıldı; kutu metni **teyide kadar "en az" ifadesiyle** yazıldı |
| 4 | **M6'nın cezalı değerlendirme kuralı hukuki değil ticari bir seçimdir** | OD-5 (fiyat düzeltme maddesi) hukuken uygulanabilir mi — `T-872` açık | Kural yalnızca **bizim iç değerlendirmemizdir**; sözleşme sonucu iddiası içermez |
| 5 | **Zorunlu alan sayısını artırmak cevabı zorlaştırdığı gibi, yalan cevabı da kolaylaştırabilir** | Boş bırakılamayan alan, tedarikçiyi "bir şey yazmaya" iter; `"standart"` yerine uydurma bir rakam gelebilir | M2/M3'te **çapraz kontrol** yapısı korundu: boş cam + dolu şişe + koli brüt üçlüsü birbirini doğrular; tutmuyorsa `99-ops/celiskiler.md`'ye taşınır |

---

## 8. SÜRÜM

| Sürüm | Tarih | Değişiklik | Ajan |
|---|---|---|---|
| v1.0 | 2026-08-10 (TUR 3A) | 8 zorunlu alan (M1…M8) tanımlandı; RFQ v2.2'ye entegre edildi | `global-sourcing-kasifi` |
