# VERGİ MATRAH SIRASI

> **DURUM: TUR 1'DE `gumruk-vergi-uzmani` TARAFINDAN DOLDURULDU (2026-08-09)**
>
> Bu dosya `80-model/engine/matrah_sirasi.py` için **tek doğruluk kaynağıdır.**
> Kod bu dosyadan okur; kodda sıra veya oran sabitlenmez.
>
> Doldurulmayan satırlar bilinçli olarak `UNKNOWN` bırakılmıştır.
> Her `FACT` satırın arkasında T1/T2 kanıt kartı vardır.

---

## 0. ÖZET — TEK CÜMLE

750 ml şişelenmiş köpüksüz şarapta vergi yükünün **belirleyici kalemi oransal
değil maktu**dur: gümrük vergisi menşeye göre %50 (AB/BK/Şili) veya %70 (ABD,
Şili dışı Yeni Dünya) CIF üzerinden, ÖTV ise **fiyattan tamamen bağımsız**
olarak **71,2692 TL/litre** (750 ml için **53,4519 TL/şişe**), KDV ise
bu toplamın üzerine %20'dir.

---

## 1. NEDEN BU DOSYA KRİTİK

Vergi hesabında en sık yapılan hata **matrahların karıştırılmasıdır.**

Yanlış soru: "ÖTV yüzde kaç?"
Doğru soru: **"ÖTV neyin üzerinden, hangi sırada, hangi tutarla?"**

Şarapta bu sorunun cevabı özellikle önemlidir çünkü **nispi (oransal) ÖTV oranı
%0'dır** ve vergi tamamen **asgari maktu tutar** üzerinden alınır. Yani ucuz
şarap ile pahalı şarap **aynı TL tutarında ÖTV** öder. Bu, fiyat/performans
segmentinin ekonomisini doğrudan belirleyen tek yapısal gerçektir.

---

## 2. GÜMRÜK KIYMETİ (VERGİLENDİRMENİN BAŞLANGICI)

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Gümrük kıymeti hangi Incoterm bazında belirlenir? | Fiilen **CIF** esaslı (satış bedeli + md.27 ilaveleri) | FACT | EV-2026-08-09-120, EV-2026-08-09-126 |
| Navlun kıymete dahil mi? | **EVET** — Türkiye'deki giriş liman/yerine kadar (GK md.27/1-e) | FACT | EV-2026-08-09-120 |
| Sigorta kıymete dahil mi? | **EVET** — giriş yerine kadar (GK md.27/1-e) | FACT | EV-2026-08-09-120 |
| Yükleme/boşaltma/elleçleme? | Giriş yerine kadar olan **yükleme ve elleçleme DAHİL**; giriş yerinden sonrası **HARİÇ** | FACT | EV-2026-08-09-120, EV-2026-08-09-121 |
| Royalti / lisans bedeli? | **Satış koşulu ise DAHİL** (md.27/1-c). Türkiye'de çoğaltma hakkı ve satış koşulu olmayan dağıtım/tekrar satış hakkı ödemeleri **HARİÇ** (md.27/5) | FACT | EV-2026-08-09-120 |
| Alım komisyonu / satım komisyonu? | **Satın alma komisyonu HARİÇ** (md.28/e). Diğer komisyonlar ve tellaliye **DAHİL** (md.27/1-a-i) | FACT | EV-2026-08-09-120, EV-2026-08-09-121 |
| Ambalaj/etiket bedeli? | Kaplar ve **işçilik+malzeme dahil ambalaj bedeli DAHİL** (md.27/1-a-ii,iii) | FACT | EV-2026-08-09-120 |
| Yurt içi masraflar kıymete dahil mi? | **HAYIR** — giriş yerine varıştan sonraki nakliye/sigorta hariç (md.28/a); Türkiye'de ödenecek ithalat vergileri de hariç (md.28/f) | FACT | EV-2026-08-09-121 |
| Finansman faizi? | Yazılı finansman anlaşması + md.28/c koşulları sağlanırsa **HARİÇ** | FACT | EV-2026-08-09-121 |

> **Uyarı:** md.28 hariç tutmaları ancak bu giderler fiilen ödenen/ödenecek
> fiyattan **ayırt edilebiliyorsa** uygulanır. Faturada ayrıştırılmamış yurt içi
> masraf kıymete girer.

**Gözetim / referans kıymet**

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Bu GTİP'te ithalatta gözetim uygulaması var mı? | **Tespit edilemedi** — 2204.21/2204.29/22.04 için yürürlükte gözetim tebliği bulunamadı | UNKNOWN | EV-2026-08-09-125 |
| Birim kıymet eşiği var mı? | UNKNOWN (tebliğ bulunamadığı için eşik de yok) | UNKNOWN | EV-2026-08-09-125 |
| Eşiğin altında beyan edilirse ne olur? | N/A (eşik tespit edilemedi). Ancak gümrük idaresinin GK md.23-31 kapsamında **kıymet araştırması** yetkisi saklıdır. | UNKNOWN | — |

> ⚠️ Arama yöntemi doğrulandı (bilinen bir gözetim GTİP'i ile kontrol edildi ve
> ilgili tebliğ bulundu), ancak **negatif arama sonucu yokluğun kanıtı değildir.**
> Bu satır `TEST` / `IMPORT PILOT` kararından önce bir gümrük müşaviri
> teyidiyle kapatılmalıdır. Bkz. `99-ops/_parts/acik-sorular-gumruk-vergi-uzmani.md`.

---

## 3. GTİP

| Alan | Değer | status | evidence_id |
|------|-------|--------|-------------|
| GTİP kodu (750 ml köpüksüz şarap) | **2204.21.xx.xx.xx** — "Muhtevası 2 litreyi geçmeyen kaplarda olanlar" | FACT | EV-2026-08-09-101 |
| Alt kırılım kriteri (ABV / hacim / köpüklü) | 1) Köpüklü ⇒ **2204.10** (ayrı ÖTV: 481,5146 TL/lt). 2) Köpüksüzde ambalaj hacmi: ≤2 lt ⇒ **2204.21**, 2–10 lt ⇒ 2204.22, diğer ⇒ 2204.29. 3) 2204.21 içindeki 12 haneli kırılım ABV ve PDO/PGI'ye dayanır | FACT (2204.21 seviyesi) / UNKNOWN (12 hane) | EV-2026-08-09-101 |
| 12 haneli alt kod vergi yükünü değiştirir mi? | **HAYIR.** 2204.21/22/29 altındaki 113 GTİP satırının tamamında AB,BK=%50 ve DÜ=%70 aynıdır; ÖTV ise 22.04 pozisyon seviyesinde belirlenmiştir | FACT | EV-2026-08-09-102, EV-2026-08-09-110 |
| Alternatif GTİP ihtimali | 2204.10 (köpüklü), 2205 (aromatize/vermut), 2206.00 (diğer fermente içecek) — hepsinin ÖTV'si farklı | FACT | EV-2026-08-09-110 |

> GTİP yanlışsa **her şey yanlıştır.** Ancak bu üründe kritik ayrım
> **12 hanede değil, 4/6 hanededir**: köpüklü mü değil mi, hacim ≤2 lt mi.

---

## 4. MATRAH ZİNCİRİ — DOLDURULMUŞ ŞEMA

Sıra numarası **hesaplama sırasıdır.**

| Sıra | Vergi / yükümlülük | Matrah (neyin üzerinden) | Oran / tutar | Tip | status | evidence_id | effective_date |
|------|--------------------|--------------------------|--------------|-----|--------|-------------|----------------|
| 1 | Gümrük Vergisi | CIF gümrük kıymeti | AB+BK: %50 · Şili: %50 · K.Makedonya: %35 · B-Hersek/G.Kore/Singapur/Kosova: %0 · Venezuela: %35 · BAE: %49 · **DÜ (ABD, G.Afrika, Avustralya, Arjantin): %70** | ORANSAL | FACT | EV-2026-08-09-103, -104, -105, -106 | 2026-01-01 |
| 2 | İlave Gümrük Vergisi (İGV) | — | **YOK** (2204 İGV listelerinde yer almıyor) | YOK | FACT | EV-2026-08-09-107 | 2026-01-01 |
| 3 | KKDF | Vadeli ödenen ithalat bedeli (**tam matrah tanımı UNKNOWN**) | Kabul kredili / vadeli akreditif / mal mukabili ⇒ **%6**. Peşin ödemede **doğmaz** | ORANSAL (koşullu) | FACT (oran) / UNKNOWN (matrah) | EV-2026-08-09-119 | 2011-10-13 |
| 4 | ÖTV | CIF + Gümrük Vergisi + ithalat sırasında ödenen diğer vergi/resim/harç/pay (KKDF dahil) + tescile kadarki diğer giderler — **ÖTV ve KDV hariç** | Nispi **%0**; asgari maktu **71,2692 TL/litre** ⇒ 750 ml için **53,4519 TL/şişe** | KARMA — kanunen "asgari maktudan az olmamak üzere yalnızca nispi"; nispi %0 olduğu için **fiilen MAKTU** | FACT | EV-2026-08-09-110, -111, -113, -115, -116 | 2026-07-03 |
| 5 | KDV | CIF + Gümrük Vergisi + KKDF + **ÖTV** + tescile kadarki diğer gider ve ödemeler | **%20** | ORANSAL | FACT | EV-2026-08-09-117, -118 | 2023-07-10 (oran) |
| 6 | Damga vergisi (gümrük beyannamesi) | Beyanname başına maktu | UNKNOWN (2026 tutarı doğrulanmadı) | MAKTU | UNKNOWN | — | — |
| 6b | TRT bandrolü / diğer fonlar | — | UNKNOWN (şarapta uygulanabilirliği doğrulanmadı; TRT bandrolü radyo-TV cihazlarına özgüdür) | UNKNOWN | UNKNOWN | — | — |

**`Tip` sütunu:** `ORANSAL` | `MAKTU` | `KARMA (yüksek olan)` | `YOK`

> **Not — sıra 3 ve 4 ilişkisi:** KKDF, "ithalat sırasında ödenen bir pay"
> niteliğiyle ÖTV ve KDV matrahına girer. Bu, KDV Kanunu md.21/b'nin lafzından
> türetilmiş bir sonuçtur; KKDF'nin bu bende dahil olduğuna dair ayrı bir
> T1 kanıt kartı açılmamıştır. Peşin ödeme senaryosunda KKDF = 0 olduğu için
> bu belirsizlik **baz senaryoyu etkilemez**; vadeli senaryoda etkiler.
> Bkz. ticket **T-105**.

### Zincirin açık yazılması

```
CIF (gümrük kıymeti)      = C                        [EV-...-120, -121, -126]
Gümrük Vergisi matrahı    = C                        [EV-...-126]
Gümrük Vergisi (GV)       = C × gv_oran              [EV-...-103, -104, -105, -106]
                            gv_oran: AB/BK/Şili 0,50 | DÜ 0,70
İlave Gümrük Vergisi      = 0                        [EV-...-107]
KKDF matrahı              = vadeli ödenen ithalat bedeli   ← peşin ödemede YOK
KKDF                      = matrah × 0,06 (yalnız kabul kredili/vadeli
                            akreditif/mal mukabili)  [EV-...-119]
ÖTV matrahı               = C + GV + KKDF + diğer    ← Gümrük Vergisi DAHİL,
                                                       ÖTV ve KDV HARİÇ
                                                     [EV-...-115]
ÖTV                       = max( 0,00 × ÖTV matrahı ; 71,2692 TL/lt × 0,75 lt )
                          = 53,4519 TL/şişe          [EV-...-110, -111, -113, -116]
KDV matrahı               = C + GV + KKDF + ÖTV + diğer  ← ÖTV DAHİL
                                                     [EV-...-117]
KDV                       = KDV matrahı × 0,20       [EV-...-118]
─────────────────────────────────────────────────────
L4 POST-TAX LANDED        = C + GV + KKDF + ÖTV + KDV
                            (KDV ayrıca §8'deki iki perspektifle gösterilir)
```

### İllüstratif hesap — **GERÇEK VERİ DEĞİLDİR, YALNIZCA ZİNCİR GÖSTERİMİDİR**

CIF = 100,00 TL/şişe (keyfî, sadece zinciri göstermek için), peşin ödeme (KKDF=0):

| Kalem | AB/BK/Şili menşeli (%50) | DÜ menşeli — ABD/Avustralya/Arjantin/G.Afrika (%70) |
|-------|--------------------------|------------------------------------------------------|
| CIF | 100,0000 | 100,0000 |
| + Gümrük Vergisi | 50,0000 | 70,0000 |
| = ÖTV matrahı | 150,0000 | 170,0000 |
| + ÖTV (maktu, matrahtan bağımsız) | 53,4519 | 53,4519 |
| = KDV matrahı | 203,4519 | 223,4519 |
| + KDV %20 | 40,6904 | 44,6904 |
| **= L4 POST-TAX LANDED** | **244,1423** | **268,1423** |
| L4 / CIF | 2,44× | 2,68× |

> ⚠️ Bu tablo **model çıktısı değildir.** Gerçek CIF `navlun-lojistik-uzmani` ve
> `global-sourcing-kasifi` girdileriyle `finans-fizibilite` tarafından kurulur.
> Tablonun tek amacı zincirin ve sıranın doğrulanabilir olmasıdır.

> **Maktu ÖTV'nin asimetrik etkisi:** CIF düştükçe ÖTV'nin göreli ağırlığı artar.
> CIF = 50 TL ise ÖTV tek başına CIF'in %107'si; CIF = 300 TL ise %18'i.
> Yani **ucuz şarap ithal etmek vergi açısından orantısız biçimde cezalandırılır.**
> Bu, projenin çekirdek hipotezine (fiyat/performans segmenti) doğrudan tehdittir.

---

## 5. ÖTV — ÖZEL DİKKAT

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Hangi liste/cetvel? | **(III) sayılı liste, (A) cetveli** — 22.04 satırı. *(NOT: görev tanımındaki "IV sayılı liste" ifadesi hatalıdır; alkollü içkiler (III)/A'dadır.)* | FACT | EV-2026-08-09-110 |
| Oransal (nispi) ÖTV oranı | **%0** | FACT | EV-2026-08-09-110 |
| Asgari maktu vergi tutarı | **71,2692 TL** | FACT | EV-2026-08-09-111 |
| Maktu tutar birimi (litre / şişe / ABV bazlı?) | **Her bir LİTRE** (ABV'den ve şişe adedinden bağımsız). Karşılaştırma: bira 1 litredeki her bir alkol derecesi; distile içkiler içerdiği alkolün her bir litresi | FACT | EV-2026-08-09-113 |
| Oransal mı maktu mu uygulanır? | Kanunen: "asgari maktu tutara göre hesaplanacak vergiden az olmamak üzere **yalnızca nispi** vergi". Nispi %0 olduğu için **her zaman maktu bağlayıcıdır** | FACT | EV-2026-08-09-113 |
| Maktu tutarın son güncelleme tarihi | **3/7/2026** (ondan önce 31/12/2025 · 61,3914 TL/lt) | FACT | EV-2026-08-09-111, EV-2026-08-09-112 |
| Güncelleme periyodu / endeksleme mekanizması | **ÖTVK md.12/3**: Ocak ve Temmuz aylarında, TÜİK ÜFE'de son 6 ayda meydana gelen değişim oranında, değişimin ilanı gününden geçerli olmak üzere **kendiliğinden yeniden belirlenmiş sayılır**. Cumhurbaşkanı uygulanmamasına karar verebilir | FACT | EV-2026-08-09-114 |
| Son gerçekleşen artış | 61,3914 → 71,2692 = **+%16,09** (6 ayda) | FACT (türetme) | EV-2026-08-09-111, -112 |
| Sonraki beklenen güncelleme | **Ocak 2027** (CB aksine karar vermezse) | ASSUMPTION | EV-2026-08-09-114 |
| ÖTV ithalatçı tarafından indirilebilir mi? | **HAYIR.** ÖTV tek aşamalıdır; indirim yalnızca aynı listedeki başka bir malın imalinde kullanım halinde mümkündür. Şişelenmiş bitmiş ürünü ithal edip satan için **ÖTV doğrudan maliyettir** | FACT | EV-2026-08-09-124 |
| ÖTV ödeme anı | İthalat vergileri ile **aynı zamanda**, gümrükte | FACT | EV-2026-08-09-123 |

> ⚠️ **`ttl: 30d`.** Bu tutar model hedef tarihinde geçerli olan hâliyle
> kullanılmalıdır. Model 2027'ye uzanan bir dönemi kapsıyorsa ÖTV tutarı
> **enflasyona endeksli bir değişken** olarak modellenmelidir, sabit değil.
> Bkz. ticket **T-104**.

### Diğer şarap tiplerinin ÖTV tutarları (aynı liste, yürürlük 3/7/2026)

| GTİP | Mal | Nispi oran | Asgari maktu (TL/litre) | 750 ml için (TL) |
|------|-----|-----------|--------------------------|------------------|
| 22.04 | Taze üzüm şarabı (köpüklü ve üzüm şırası hariç) | %0 | **71,2692** | 53,4519 |
| 2204.10 | Köpüklü şaraplar | %0 | **481,5146** | 361,1360 |
| 22.05 | Vermut ve aromatize üzüm şarapları | %0 | 726,7254 | 545,0441 |
| 2205.10.10.00.00 | ABV ≤ %18 olanlar | %0 | 577,1023 | 432,8267 |
| 2206.00 | Diğer fermente içecekler | %0 | 157,2270 | 117,9203 |

*(Kaynak: EV-2026-08-09-110 / -111 aynı liste. 750 ml sütunu türetmedir.)*

---

## 6. TERCİHLİ TARİFE

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Hangi ülkeler için STA/tercihli tarife var? | Şarapta **sıfır oran yalnız** Bosna-Hersek, Güney Kore, Singapur, Kosova için. AB/BK ve Şili **indirimli ama sıfır değil (%50)**. K.Makedonya %35, Venezuela %35, BAE %49 | FACT | EV-2026-08-09-103, -105, -106 |
| **Gümrük Birliği şarabı kapsıyor mu?** | **HAYIR.** Şarap tarım ürünüdür ve İthalat Rejimi Kararı **I sayılı Liste (Tarım Ürünleri)** içindedir; AB menşeli şarapta %50 gümrük vergisi vardır | FACT | EV-2026-08-09-103 |
| Menşe ispat belgesi türü (EUR.1 / fatura beyanı / REX / A.TR) | **UNKNOWN** — bu turda anlaşma bazında doğrulanamadı. A.TR'nin (serbest dolaşım belgesi) tarım ürünlerinde tercihli tarife sağlamayacağı, indirimli oranın **menşe** esaslı olduğu yapısal olarak açıktır ancak belge türü belgelenmedi | UNKNOWN | — |
| Tarife kontenjanı var mı? | **Köpüksüz şarapta AB için YOK.** AB kontenjanı yalnız 2204.10 köpüklü (750 hl, %35); BK yalnız 2204.10 (125 hl, %35); İsviçre/Lihtenştayn 2204.21 için 30.000 lt (DÜ oranının %50'si = %35) | FACT | EV-2026-08-09-108, -109 |
| Tercihli tarife hangi vergiyi etkiler, hangisini etkilemez? | **Yalnızca gümrük vergisini** etkiler. ÖTV, ÖTV Kanunu'na ekli listeye göre belirlenir ve menşeye göre değişmez; KDV oranı da menşeye göre değişmez. Ancak gümrük vergisi ÖTV ve KDV matrahına girdiği için **dolaylı** olarak ikisini de düşürür | FACT (türetme) | EV-2026-08-09-110, -115, -117, -118 |

---

## 7. ANTREPO REJİMİNİN VERGİ ETKİSİ

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Vergiler antrepoya girişte mi, çıkışta mı doğar? | **Çıkışta.** İthalatta gümrük yükümlülüğü, **serbest dolaşıma giriş beyannamesinin tescil tarihinde** başlar (GK md.181/1-a). Antrepo rejimi ithalat vergilerine tabi tutulmamış eşyaya ilişkindir (GK md.93/1-a) | FACT | EV-2026-08-09-122 |
| Antrepoda bekletme vergi yükünü değiştirir mi? | **Toplam yükü değiştirmez** — ancak oran/tutar tescil tarihindekidir; ÖTV maktu tutarı Ocak/Temmuz'da değiştiği için **bekletme ÖTV artışı riskini taşır** | FACT + ESTIMATE | EV-2026-08-09-122, EV-2026-08-09-114 |
| Antrepoda bekletme **nakit akışını** nasıl etkiler? | Vergi ödemesini satış takvimine yaklaştırır; `peak_cash_requirement`'ı düşürür. Antrepo teminatı ve depo maliyeti karşı kalemdir | FACT (yön) / UNKNOWN (tutar) | EV-2026-08-09-122 |
| Antrepoda kalış süresi | **Sınırsız** (GK md.101/1); gümrük idaresi gerekli görürse süre belirleyebilir | FACT | EV-2026-08-09-122 |
| Kısmi çekiş (partial release) mümkün mü? | **UNKNOWN** — bu turda T1/T2 ile doğrulanamadı | UNKNOWN | — · ticket **T-101** |

> Kısmi çekiş mümkünse, `peak_cash_requirement` dramatik biçimde düşebilir.
> Bu, `finans-fizibilite` için birinci derecede önemli bir girdidir ve
> **antrepo operasyonu `navlun-lojistik-uzmani` alanında** olduğu için
> ticket **T-101** ile o ajana devredilmiştir.

---

## 8. KDV — İKİ PERSPEKTİF

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| İthalatta ödenen KDV indirilebilir mi? | **UNKNOWN (bu turda doğrulanmadı).** KDV Kanunu md.29 vd. genel indirim mekanizması mevcuttur ancak alkollü içki ticaretine özgü bir sınırlama olup olmadığı doğrulanmadı | UNKNOWN | — |
| İndirilebiliyorsa ne zaman mahsup edilir? | UNKNOWN | UNKNOWN | — |
| Devreden KDV oluşur mu, iade süreci nedir? | UNKNOWN | UNKNOWN | — |
| ÖTV indirilebilir mi? | **HAYIR** — ithalatçı-satıcı için ÖTV maliyettir | FACT | EV-2026-08-09-124 |
| KDV ödeme anı | Gümrükte, gümrük vergisi ile birlikte | FACT (yapısal) | EV-2026-08-09-126 |

**A) Ekonomik maliyet:** KDV indirilebiliyorsa P&L'e girmez → L4'te gösterilir
ama L5'e taşınmaz. **Bu, doğrulanmadığı sürece modelde iki senaryo olarak
çalıştırılmalıdır.**
**B) Nakit akışı (`cash_tax_timing`):** Gümrükte ödeme anı ile mahsup/tahsilat
anı arasındaki gecikme `peak_cash_requirement`'ı büyütür. Gecikme gün sayısı
**UNKNOWN**.

Bu ikisi **asla tek satırda** gösterilmez.

---

## 9. MODEL İÇİN DOLDURULAN / DOLDURULMAYAN

| Alan | Durum |
|------|-------|
| GTİP (2204.21 seviyesi) | ✅ FACT |
| Gümrük vergisi oranı (9 hedef ülke) | ✅ FACT |
| İGV | ✅ FACT (yok) |
| ÖTV oranı + maktu tutar + birim + hesap kuralı | ✅ FACT |
| ÖTV güncelleme mekanizması | ✅ FACT |
| KDV oranı + matrah | ✅ FACT |
| KKDF oranı ve tetikleyicisi | ✅ FACT |
| KKDF matrahının tam tanımı | ❌ UNKNOWN (T-105) |
| Gümrük kıymeti dahil/hariç kalemleri | ✅ FACT |
| Gözetim / referans kıymet | ❌ UNKNOWN (negatif arama) |
| Menşe ispat belgesi türü | ❌ UNKNOWN |
| Antrepo vergi doğuş anı | ✅ FACT |
| Antrepo kısmi çekiş | ❌ UNKNOWN (T-101) |
| İthalat KDV'sinin indirilebilirliği | ❌ UNKNOWN |
| Damga vergisi tutarı | ❌ UNKNOWN |

---

## 10. BU BULGUYU NE ÇÜRÜTÜR?

### Hangi GTİP itirazı tüm yapıyı değiştirir?
- **Ürünün köpüklü sayılması (2204.10):** ÖTV 71,2692 → 481,5146 TL/lt, yani
  750 ml'de 53,45 → 361,14 TL. Projeyi tek başına öldürür. Aromatize/tatlandırılmış
  ürün 22.05'e kaçarsa (726,7254 TL/lt) sonuç daha da kötüdür.
- **Ambalajın 2 litreyi aşması (bag-in-box 3 lt):** 2204.22'ye geçer; gümrük
  vergisi aynı kalır ama ürün 750 ml benchmark'ının dışına çıkar.
- 12 haneli alt kod itirazı **vergi yükünü değiştirmez** (EV-2026-08-09-102) —
  bu, yapının en dayanıklı kısmıdır.

### Maktu ÖTV güncellenirse hangi senaryolar ölür?
- Ocak 2027'de benzer bir Yİ-ÜFE artışı (+%16) gelirse ÖTV 750 ml'de ~62 TL'ye
  çıkar. Şişe başı katkı payı bu artıştan düşükse tüm düşük-CIF senaryoları ölür.
- ÖTV TL cinsindendir ve CIF döviz cinsindendir. **TL reel olarak değer
  kazanırsa ÖTV'nin göreli yükü artar, kaybederse azalır** — bu, modelin
  duyarlılık analizinde ayrı bir eksen olmalıdır.

### Gözetim/kıymet itirazı gelirse beyan stratejisi ne olur?
- Yürürlükte gözetim tebliği **bulunamadı**, ancak bu yokluğun kanıtı değildir.
  Gözetim getirilirse veya gümrük idaresi GK md.23-31 kapsamında kıymet
  araştırması yaparsa, düşük CIF beyanı fiilen kullanılamaz; gümrük vergisi
  ve KDV matrahı yukarı çekilir. ÖTV maktu olduğu için bundan **etkilenmez** —
  yani kıymet itirazının etkisi diğer ürünlere göre daha sınırlıdır.

### Tercihli tarifenin ÖTV'yi etkilemediği doğrulanırsa ülke seçimi değişir mi?
- Evet, ama beklenenden az. AB (%50) ile DÜ (%70) arasındaki 20 puanlık fark
  yalnızca CIF'in %20'si kadar bir avantaj yaratır; ÖTV+KDV'nin ağırlığı
  karşısında bu fark ürün maliyetinin küçük bir kısmıdır. Buna karşılık
  **Bosna-Hersek ve Kosova menşeli şarapta gümrük vergisi %0**'dır — bu, menşe
  seçiminin en büyük tek kaldıracıdır ve `global-sourcing-kasifi`'ne
  ipucu olarak bırakılmıştır.

### Bu dosyayı geçersiz kılacak tek bulgu
- ÖTV (III)/A cetvelinde 22.04 için **nispi oranın %0'dan farklı** belirlendiğinin
  tespiti. O durumda "yüksek olan" kuralı devreye girer ve zincirdeki 4. sıra
  matrahı gerçekten önem kazanır.
