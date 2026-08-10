# SAHA GÖREV PAKETİ — ŞARAP RAFI OPERASYONU

```yaml
belge:            60-pazar/saha-gorev-paketi.md
ajan:             turkiye-pazar-kasifi
tur:              TUR 3.25 §11
tarih:            2026-08-10
nitelik:          OPERASYON GOREVI — VERI ICERMEZ, GOZLEM URETMEZ
uygulayici:       kurucu / insan gozlemci (SAHADA)
onceki_surum:     60-pazar/saha-kontrol-listesi.md (TUR 3A) — YURURLUKTE, EK olarak okunur
bagli_sablon:     60-pazar/saha-veri-sablonu.csv (44 kolon)
kapatmayi_hedefledigi: [T-917, T-504, T-603, T-701, C-501, C-551, C-561, OQ-001, OQ-502, OQ-552, OQ-503, T-405]
```

> **BU BELGE BİR BULGU DEĞİLDİR.** Hiçbir fiyat, hiçbir SKU, hiçbir sayım içermez.
> **SAHA TURU YAPILMAMIŞTIR.** Bu belge, turun kendisi değil, **görev emridir**.
> Doldurulmadan hiçbir modele girdi üretmez.

---
---

# ⬛ ÖN SAYFA — EYLEM

## GÖREVİN TEK CÜMLESİ

> **799 TL'nin (PRIMARY) zincir market rafında karşılığı var mı, o bantta kim
> duruyor, ithal mi yerli mi — ve Metro'daki 599,90 TL etiketi promosyonlu muydu?**

Sabitlenen yatırımcı kararı: **PRIMARY 799 · SECONDARY 699 · STRETCH 899 TRY**
(`INVESTOR_TARGET` — bir **hedef**tir, bir gözlem değildir; K7).
Bugün bu üç hedefin karşılığı olan katman (`L8_CHAIN_RETAIL`) projede
**SIFIR gözlemlidir**. Bu tur onu sıfır olmaktan çıkarır.

**Odak:** `500–1.200 TL` · **BEYAZ ŞARAP** · **ithal + yerli** · **750 ml öncelikli**

---

## 0 · ÇIKMADAN ÖNCE — 10 DAKİKA

```
[ ] Bu sayfanın çıktısı (veya telefonda açık) + kalem
[ ] Telefon: şarj ≥%80 · boş alan ≥3 GB · EXIF tarih/saat AÇIK · flaş KAPALI
[ ] ~600 TL nakit/kart  → 1–2 şişe alınacak (kasa fişi = en güçlü KDV kanıtı)
[ ] Metro giriş kartı (yoksa: ücretsiz günlük kart girişte alınır)
[ ] saha-veri-sablonu.csv'yi AÇMA — sahada CSV doldurulmaz, kağıda/nota yazılır
```

---

## 1 · ROTA VE SÜRE BÜTÇESİ

**Kural: ≥4 mağaza · ≥2 kanal · ≥2 şehir VEYA aynı şehirde ≥2 bölge.**

| Sıra | Mağaza | Bölge/Şehir | Süre | Neden bu sırada |
|---|---|---|---|---|
| **1** | **METRO** (mümkünse benchmark fotoğrafının çekildiği şube) | Bölge/Şehir **1** | **40 dk** | Gün en taze burada başlamalı: `T-504`+`C-551`+`OQ-001` **yalnızca burada** kapanır. Kasa fişi burada alınır. |
| **2** | **MİGROS 5M** *(veya Macrocenter)* | Bölge/Şehir **1** | **30 dk** | `L8_CHAIN_RETAIL` — projenin **en büyük kanıt boşluğu** (`T-701`, `T-603`) |
| **3** | **CARREFOURSA** (hiper) | Bölge/Şehir **2** | **30 dk** | Tek zincire bağlı kalmamak + zincirler arası fark |
| **4** | **MACROCENTER** *(sırada kalan zincir)* | Bölge/Şehir **2** | **30 dk** | Macrocenter üst-segment ağırlıklıdır: bandın **üst** ucunu o gösterir |
| 5 *(P1)* | **Tekel bayii** (şarap ağırlıklı bağımsız) | Bölge/Şehir 2 | 20 dk | `L8_TEKEL_BAYII` = 0 gözlem; alt bandı asıl bu kanal taşıyor olabilir |
| 6 *(P2)* | **Metro — 2. şehir** | Şehir 2 | 30 dk | Metro "tek fiyat" varsayımının testi |

**Toplam:** 4 zorunlu mağaza = **2 saat 10 dk raf** + yol ≈ **yarım gün.**
5–6 eklenirse ≈ 5 saat.

**SKU hedefi (satır sayısı):**

| | Hedef | Asgari |
|---|---|---|
| Metro | 20–25 satır | 15 |
| Her zincir market | 12–18 satır | 10 |
| Tekel bayii | 10–15 satır | — |
| **TOPLAM İTHAL satır** | 25–35 | **≥ 20** |
| **Bunların ZİNCİR MARKET'ten geleni** | 12–20 | **≥ 8** |

---

## 2 · HER MAĞAZADA 30 DAKİKA (Metro 40)

| Dk | İş |
|---|---|
| **0–2** | **F0** fotoğrafı (tabela/reyon künyesi) + mağaza başlığını doldur (§3A) |
| **2–5** | **F1**: şarap reyonunu baştan sona, **%30 örtüşmeli** ardışık kareler |
| **5–10** | **SAYIM FORMU** (§5) — sadece **say**, fiyat yazma |
| **10–26** | **SKU satırları**: 12 zorunlu alan + **F2 etiket** (SKU başına ~45 sn) |
| **26–29** | **F3 arka etiket** (ithalatçı adı) + **§6 arama listesi** işaretle |
| **29–30** | **KAPANIŞ KONTROLÜ**: her satırın F2'si var mı? Yoksa satırı **çiz, sil.** |
| *Metro +10* | Kasa: **1–2 şişe satın al** → **F4 kasa fişi** (KDV satırı görünecek) |

---

## 3 · HER SKU İÇİN **12 ZORUNLU ALAN**

> **Bu 12'den biri eksikse satır GEÇERSİZDİR.** Sahada **az yaz, çok fotoğrafla**:
> 6 alan elle yazılır, 6 alan masabaşında **fotoğraftan** doldurulur.

### 3A · MAĞAZA BAŞLIĞI — mağaza başına 1 kez (12'nin 2'si buradadır)

```
[ ] ⑪ MAĞAZA adı/şube : ______________________  (F0 fotoğrafı çekildi mi?  E / H)
[ ] ⑫ TARİH           : ____/____/2026   Saat: ______
[ ] Şehir / ilçe / bölge : ______________________
[ ] Kanal tipi        : ( ) CASH_CARRY ( ) CHAIN_RETAIL ( ) TEKEL ( ) DİĞER
[ ] Gözlemci          : ______________________
[ ] Reyonda genel "kampanya/indirim" afişi var mı?  ( ) E  ( ) H   → varsa F1'de görünsün
```

### 3B · SKU SATIRI

**SAHADA ELLE YAZILAN 6:**

| # | Zorunlu alan | Nasıl yazılır |
|---|---|---|
| **③** | **FİYAT** | Etiketteki **büyük punto** sayı, kuruşuyla: `_____ , ___ TL` |
| **④** | **PROMOSYON İŞARETİ** | `E` / `H` / `OKUNMADI` — E ise §4'teki (a)(c)(e)'den hangisi |
| **⑥** | **MENŞE** | `İTH` / `YRL`; emin değilsen `?` — arka etiket fotoğrafı karar verir |
| **⑧** | **HACİM — 750 mi?** | `750` / `375` / `1000` / `diğer` — **750 dışıysa MUTLAKA yaz** |
| **①** | **FOTO no** | Etiket foto no + arka etiket foto no |
| **②** | **RAF ETİKETİ** | F2 fotoğrafı çekildi mi? → `✓` *(metin masabaşında okunur)* |

*(+ operasyonel tutkal: **sıra no** `01, 02…` ve **SKU adı** kısaltması —
fotoğrafla satırı eşleştiren tek şey budur.)*

**MASABAŞINDA FOTOĞRAFTAN DOLDURULAN 6:**

| # | Zorunlu alan | Kaynağı |
|---|---|---|
| **⑤** | **MARKA** | F2 / F5 ön etiket |
| **⑦** | **ÜZÜM / BLEND** | F2 ön etiket veya F3 arka etiket |
| **⑨** | **ABV %** | **F3 arka etiket** |
| **⑩** | **İTHALATÇI** | **F3 arka etiket** — ithal SKU'da firma ünvanı; yerlide `YERLI URETICI` + üretici ünvanı |
| **②** | **RAF ETİKETİ okuması** | F2'den 4 metin: **KDV ibaresi tam metni** · **birim fiyat satırı** · **üstü çizili eski fiyat** · **kampanya tarihi** |
| **⑥** | **MENŞE (tam ülke)** | F3 arka etiket |

> **OKUNABİLİRLİK (BAĞLAYICI):** Fotoğraf, ekranda **%100 zoom'da etiketin
> EN KÜÇÜK yazısı okunuyorsa** geçerlidir. Okunmuyorsa alan **`OKUNMADI`**
> yazılır — **TAHMİN EDİLMEZ.**

---

## 4 · ⚠ EN KRİTİK TEK İŞ — RAF ETİKETİNİN ANATOMİSİ (`T-504` · `C-551` · `OQ-001`)

**F2 fotoğrafında şu beş şeyin görünüp görünmediği tek tek işaretlenir.**
*"Bakmadım"* ile *"baktım, yoktu"* **AYNI ŞEY DEĞİLDİR.**

```
┌───────────────────────────────────────────────┐
│  6̶9̶9̶,̶9̶0̶ ̶T̶L̶      ← (a) ÜSTÜ ÇİZİLİ ESKİ FİYAT    │ → VAR ise PROMOSYON = FACT
│                                               │
│   599 , 90 TL     ← ANA FİYAT (büyük punto)   │ → alan ③
│           KDV'li  ← (b) KDV İBARESİ           │ → C-551'in DOĞRUDAN cevabı
│                                               │
│  [AVANTAJLI FİYAT] ← (c) KIRMIZI ROZET        │ → VAR ise PROMOSYON = FACT
│  L fiyatı: 799,87 TL ← (d) BİRİM FİYAT SATIRI │ → "ikinci sayı" bu mu?
│  Geçerlilik: __.__ – __.__ ← (e) KAMPANYA TARİHİ│ → varsa fiyat SÜRESİZ DEĞİL
└───────────────────────────────────────────────┘
```

| İşaret | Sahada yazılacak | Ne kanıtlar |
|---|---|---|
| **(a)** üstü çizili eski fiyat | `VAR` (+ eski fiyatı yaz) / `YOK` / `OKUNMADI` | VAR → fiyat **promosyonludur**, `T-504` **tek ziyarette kapanır** |
| **(b)** KDV ibaresi — **TAM METİN** | `KDV'li` / `KDV Hariç` / **ÇİFT SATIR (iki sayıyı da yaz)** / `İbare yok` / `OKUNMADI` | **`C-551`** |
| **(c)** "AVANTAJLI FİYAT" rozeti | `VAR` / `YOK` / `OKUNMADI` | `T-504` — Metro'nun promosyon etiket anatomisi |
| **(d)** birim fiyat satırı | tam metin (`L fiyatı: …`) | `OQ-001 §7` — "ikinci sayı birim fiyat mı" sorusu **rafta** kapanır |
| **(e)** kampanya geçerlilik tarihi / "stoklarla sınırlıdır" | `VAR` (tarihi yaz) / `YOK` | Tarih varsa fiyat **süresiz raf fiyatı değildir** |

> ### 🔒 T-504 ASİMETRİ KURALI (BAĞLAYICI)
> `T-504`, promosyon işareti **BULUNURSA** kapanır.
> **BULUNMAZSA KAPANMAZ.** "İşaret yok" **normal fiyat kanıtı DEĞİLDİR** —
> o `UNKNOWN`'dır. Bu durumda **2–4 hafta sonra, yalnızca Metro, yalnızca
> 2 SKU, 10 dakikalık İKİNCİ ZİYARET** gerekir (§9).

---

## 5 · SAYIM FORMU — mağaza başına 1 kez, 5 dakika

> SKU kaydından **ayrıdır**. Fiyat yazılmaz, **etiket sayılır** (facing değil).

| Bant (TL) | BEYAZ ithal | BEYAZ yerli | TÜM renk ithal | TÜM renk yerli |
|---|---|---|---|---|
| 500 – 600 | | | | |
| 600 – 700 | | | | |
| 700 – 800 | | | | |
| 800 – 900 | | | | |
| 900 – 1.000 | | | | |
| 1.000 – 1.200 | | | | |
| **500–1.200 TOPLAM** | | | | |

```
[ ] Rafta EN UCUZ İTHAL şarap         : ______________  ______ TL
[ ] Rafta EN UCUZ şarap (yerli dahil) : ______________  ______ TL
[ ] Reyonda toplam şarap SKU (kaba)   : ______
[ ] 500 TL ALTINDA hiç şarap var mı?  : ( ) E  ( ) H   → varsa en ucuzunu yaz: ______
[ ] 1.200 TL ÜSTÜ ithal SKU çok mu?   : ( ) E  ( ) H
[ ] Köpüklü/şampanya sayıma dahil mi? : ( ) E  ( ) H   ← AYRI işaretle
```

---

## 6 · HANGİ ALT BANT HANGİ HEDEFİ TEST EDİYOR

> **Bandı yukarıdan aşağı değil, AŞAĞIDAN YUKARI tara.** B1 en riskli ve en
> hızlı biten banttır; süre biterse üstü kaybetmek daha ucuzdur.

| Kod | Bant | Test ettiği hedef | Bu bant **boş çıkarsa** ne demek |
|---|---|---|---|
| **B1** | **500–629 TL** | **Taban / downside (599)** + `OBSERVED_BENCHMARK` bölgesi (599,90 · 649,90) | 699 SECONDARY'nin altında ithal ürün yok → 599 senaryosu **`TOO_LOW`**'a döner |
| **B2** | **629–769 TL** | **SECONDARY 699** (±%10 penceresi) | 699 whitespace **teyit** olur *ama* "boşluk mu, dönmeme mi" sorusu §7 stok alanıyla ayrışır |
| **B3** | **719–879 TL** | **PRIMARY 799** (±%10 penceresi) — **turun ASIL bandı** | PRIMARY'nin zincir rafında karşılığı yok demektir; `l8_chain_retail` bu bandın **üstünde** kurulur |
| **B4** | **809–989 TL** | **STRETCH 899** (±%10) + "ithal rekabet 875 TL'de başlar" iddiasının testi | 875 TL ithal tabanı bir **kanal artefaktıdır** |
| **B5** | **990–1.200 TL** | Kontrol bandı: `segment.fiyat_performans_ust_try = 900` ESTIMATE'i doğru mu | Segment tavanı yukarı revize edilmeli |

*(B2–B3 ve B3–B4 pencereleri **kasten örtüşür** — ±%10 pencereler örtüşür.
Bir SKU birden çok banda düşebilir; satıra **tek** bant kodu yaz, en yakın
hedefinkini seç.)*

**Beyaz odak kuralı:** Tam satır **yalnızca beyaz şaraplar** için doldurulur.
Kırmızı/rosé yalnızca **§5 sayım formunda** sayılır.
**İstisna:** bir bantta **beyaz ithal 0** çıkarsa, o bantta **kırmızı bir ithal**
SKU'nun tam satırı alınır ve `notes` alanına **`RENK_ISTISNASI`** yazılır —
bandın "yapısal olarak boş" görünmesini engellemek için.

---

## 7 · HER SATIRDA AYRICA İŞARETLENEN 4 TİKET-KRİTİK ALAN

> 12 zorunlunun **dışındadır** ama bu 4'ü olmadan tur yapılır, **ticketlar
> kapanmaz.** Yazması 5 saniyedir.

| Alan | Değerler | Kapattığı |
|---|---|---|
| **KANAL TİPİ** | `CASH_CARRY` / `CHAIN_RETAIL` / `TEKEL` | **K1** — Metro fiyatı zincir fiyatıyla **aynı sütuna yazılamaz** |
| **ŞEHİR / BÖLGE** | metin | `T-917 P1` — şehir farkı riski |
| **STOK** | `DOLU` / `AZ` (1–2 şişe) / `BOŞ` (etiket var, şişe yok) | **`C-561`** — *"yok"* mu, *"var ama dönmüyor"* mu |
| **HEDEF BANT** | `B1`…`B5` | Satırı doğrudan 699/799/899 hedefine bağlar |

---

## 8 · ARKA ETİKET — İTHALATÇI (`OQ-503` · `T-405` · `İP-008`)

**Her ithal SKU için şişeyi eline al ve çevir. Raf fotoğrafı arka etiketi göstermez.**

```
[ ] İthalatçı / dağıtıcı firma ünvanı : ______________________  ← ASIL HEDEF (alan ⑩)
[ ] Üretici / şişeleyici              : ______________________
[ ] Alkol derecesi (% vol)            : ______                  ← alan ⑨
[ ] Net hacim                         : ______ ml               ← alan ⑧
[ ] Menşe ülke (arka etiket yazımı)   : ______________________  ← alan ⑥
```

Bugün projede **doğrulanmış ithalatçı sayısı: 1**.
**Gold Country ve Central Creek'in arka etiketi ÖNCELİKLİDİR.**

---

## 9 · HEDEF SKU ARAMA LİSTESİ — "yok" mu, "var ama dönmüyor" mu

Her mağazada **tek tek ara ve işaretle. Bulunmayan da bir veridir.**

| Aranan SKU | Bulundu? | Fiyat | Stok |
|---|---|---|---|
| **Gold Country** (California) — *benchmark, BEYAZ* | V / Y | | |
| **Central Creek** (Avustralya) — *benchmark* | V / Y | | |
| Santa Helena | V / Y | | |
| M. Chapoutier Belleruche | V / Y | | |
| Babich | V / Y | | |
| Hans Baer | V / Y | | |
| Henkell | V / Y | | |
| Terra Mater Reserve | V / Y | | |
| Botter Caleo | V / Y | | |
| Luccarelli | V / Y | | |
| Barone Montalto | V / Y | | |
| La Vieille Ferme | V / Y | | |
| Alpaca | V / Y | | |
| Tesori Prosecco | V / Y | | |

---

## 10 · FOTOĞRAF PROTOKOLÜ (kısa)

| Kod | Ne | Kaç | Zorunlu |
|---|---|---|---|
| **F0** | Mağaza tabelası / reyon künyesi | 1 / mağaza | **EVET** |
| **F1** | Raf geneli, %30 örtüşmeli kareler | 3–5 / mağaza | **EVET** |
| **F2** | **Etiket yakın çekim** — fiyat + KDV ibaresi + birim fiyat + varsa üstü çizili + rozet + tarih | **HER satır için 1** | **EVET — bu foto yoksa SATIR GEÇERSİZ** |
| **F3** | **Arka etiket** — ithalatçı + ABV + hacim | Her ithal SKU | **EVET** |
| **F4** | **Kasa fişi** — ürün adı + tutar + **KDV satırı** | 1–2 şişe | **Metro'da şiddetle önerilir** |
| F5 | Ön etiket (marka/vintage okunmuyorsa) | gerektiğinde | Hayır |

**Çekim:** 20–30 cm · kadraja **paralel** · **flaş kapalı** · ESL ekranda ~**30° açı** ve
**2 kare** · şişe **rafında dururken** · **EXIF açık**.

**Dosya adı:** `YYYYMMDD_KANAL_SEHIR_SUBE_SIRANO_TIP.jpg`
→ `20260812_METRO_IST_BAYRAMPASA_007_ETIKET.jpg` · `..._007_ARKA.jpg` · `..._000_F0.jpg`

**Tahmini:** mağaza başına ≈ 1+4+18+8 = **~31 kare** · 4 mağazalık tur ≈ **125 kare**

---

## 11 · NE ZAMAN DURULUR (STOP KURALLARI)

| Durum | Ne yap |
|---|---|
| Mağazada **30 dk doldu**, bant bitmedi | **DUR.** Nereye kadar taradığını yaz (`taranan_son_bant`). Eksik tarama **kaydedilebilir**; uydurma **kaydedilemez**. |
| Mağazada 500–1.200 TL'de **hiç ithal şarap yok** | F1 + sayım formu + en ucuz ithal fiyatı al, **15 dk'da çık**. Bu **bulgudur**, kayıp değil. |
| Bir SKU'nun etiketi **okunmuyor** (ESL parlaması vb.) | 2 kare daha dene; hâlâ olmuyorsa alanı `OKUNMADI` yaz ve **geç.** Tahmin etme. |
| **4 mağaza bitti**, ithal satır **≥20** ve zincir-ithal **≥8** | **TUR TAMAM. DUR.** 5. ve 6. mağaza opsiyoneldir. |
| **4 mağaza bitti**, ithal satır **<20** | **Tekel bayii ekle** (5. durak). Ondan sonra da tutmuyorsa **DUR** ve eksiği raporla — mağaza sayısını şişirme. |
| Promosyon işareti (a)(c)(e) **hiçbir SKU'da bulunamadı** | Tur biter ama **`T-504` KAPANMAZ** → §12 ikinci ziyaret takvime alınır. |
| Bir mağaza şarap satmıyor / reyon kapalı | F0 çek, "şarap yok" diye kaydet, **çık.** Bu da veridir. |

---

## 12 · İKİNCİ ZİYARET (yalnızca gerekirse) — 10 DAKİKA

**Tetikleyici:** ilk turda promosyon işareti bulunamadı (`H` / `OKUNMADI`).
**Ne zaman:** ilk turdan **2–4 hafta sonra**.
**Nerede:** yalnızca **1. duraktaki Metro**, **aynı şube**.
**Ne:** yalnızca **Gold Country** ve **Central Creek** → **F2 + fiyat + tarih.**
**Neden:** fiyat değişmişse ilk gözlem **promosyonluydu**; değişmemişse
`T-504` "normal fiyat" yönünde **iki tarihli** kanıtla kapanır.

---

## 13 · TURU GEÇERSİZ KILAN 6 HATA

1. **F2'siz satır** — etiket fotoğrafı olmayan fiyat kayda geçmez.
2. **İnce yazıyı "hatırlayarak" doldurmak** — okunmuyorsa `OKUNMADI`.
3. **Promosyon işareti yokluğunu "normal fiyat" diye yazmak** — o `UNKNOWN`'dır.
4. **Metro fiyatını zincir market fiyatıyla aynı sütunda toplamak** — **K1 ihlali.**
5. **Sadece ilgi çekici SKU'ları kaydetmek** — bandın **tamamı** taranır, yoksa sayım yanlıdır.
6. **Şişeyi rafından çıkarıp başka yere koymak** — fiyat/ürün eşleşmesi bozulur.

---

## 14 · DÖNÜNCE — VERİ NEREYE GİRER

1. Fotoğrafları **dosya adlandırma kuralıyla** tek klasöre aktar.
2. `60-pazar/saha-veri-sablonu.csv`'yi doldur (44 kolon; `TEST_FIXTURE` satırını **silme**,
   yeni satırları altına ekle). **`evidence_id` alanını BOŞ BIRAK** — ajan doldurur.
3. `turkiye-pazar-kasifi` ajanına haber ver: satırlar `raf-fiyat-gozlemleri.csv`'ye
   taşınır, **her mağaza için ayrı kanıt kartı** açılır (`tier: T4`, `ttl: 30d`),
   fotoğraflar `10-evidence/snapshots/` altına konur.
4. `pazar.yaml` güncellemesi **öneri** olarak sunulur; merge kararı **başkanındır**.

---
---

# ⬜ EK — GEREKÇE (sahada okunması gerekmez)

## EK-A · 23 ALAN → 12 ZORUNLU ALAN HİZALAMASI

TUR 3A'nın 23 alanı (8 sahada + 10 masabaşı + 5 mağaza başlığı) bu turda
**parent'ın 12 zorunlu alanıyla** hizalanmıştır. **Hiçbir alan silinmemiştir**;
bazıları **opsiyonele indirilmiştir**.

| # | 12 ZORUNLU (parent) | TUR 3A'daki karşılığı | İşlem |
|---|---|---|---|
| ① | **photo** | (8) foto no + §H F2/F3 | Korundu — **satır geçerlilik kapısı** |
| ② | **shelf label** | (15) KDV ibaresi + (16) birim fiyat satırı + (17) üstü çizili fiyat | Korundu — **tek alan değil, 4 okumalı bir nesne** olarak yeniden tanımlandı (§4) |
| ③ | **price** | (3) raf fiyatı | Korundu |
| ④ | **promotion marker** | (6) PROMO? + (17) + §D(c)(e) | Korundu + **asimetri kuralı** öne alındı |
| ⑤ | **brand** | (9) marka | Masabaşı alanıydı → **ZORUNLU'ya yükseltildi** |
| ⑥ | **origin** | (4) İTH/YRL + (10) menşe tam | Korundu (sahada kaba, masabaşında tam) |
| ⑦ | **grape/blend** | (13) üzüm/blend | Masabaşı "doldurulabilirse" alanıydı → **ZORUNLU'ya yükseltildi** |
| ⑧ | **750 ml?** | (5) hacim | Korundu — "750 dışıysa mutlaka yaz" kuralı sürüyor |
| ⑨ | **ABV** | (11) ABV % | Masabaşı alanıydı → **ZORUNLU'ya yükseltildi**; **F3 artık YERLİ SKU için de çekilir** |
| ⑩ | **importer** | (18) ithalatçı firma adı | **Yalnızca ithal SKU'da zorunluydu → TÜM SKU'da zorunlu** (yerlide `YERLI URETICI` + üretici ünvanı) |
| ⑪ | **store** | (19) mağaza adı/şube | Korundu (mağaza başlığı) |
| ⑫ | **date** | (22) tarih | Korundu (mağaza başlığı) |

**12'ye girmeyen ama PROJE ZORUNLUSU olarak korunan 5 alan** (§7 + operasyonel tutkal):

| TUR 3A # | Alan | Neden korundu |
|---|---|---|
| (21) | kanal tipi | **K1** — Metro cash&carry ile zincir perakende aynı sütuna yazılamaz. 12'de yok ama K1 bağlayıcı. |
| (20) | şehir / bölge | `T-917 P1` — asgari protokolün maddesi |
| (7) | stok durumu | **`C-561`** — turun ikinci en değerli çıktısı; yazması 1 saniye |
| (1) | sıra no | Fotoğrafı satıra bağlayan **tek** mekanizma |
| (2) | SKU adı | Satır kimliği; kanallar arası aynı SKU takibi (`T-701`) |

**Opsiyonele indirilen 3 alan:**

| TUR 3A # | Alan | Neden indirildi |
|---|---|---|
| (12) | vintage | F2/F5 fotoğrafında zaten var; sahada yazmak süre yiyor. Modelde hiçbir yeri yok. |
| (14) | ürün tipi | Tur **beyaz şarap odaklıdır** → varsayılan "sakin beyaz". Yalnızca **köpüklü/tatlı** ise işaretlenir. |
| (23) | gözlemci | Mağaza başlığında **1 kez**; satır başına tekrarlanmaz |

**Yeni eklenen 2 alan** (12'de örtük, TUR 3A'da yoktu):

| Alan | Neden |
|---|---|
| `saha_hedef_bant` (B1–B5) | Sabitlenen `INVESTOR_TARGET` (699/799/899) geldi; her satır artık **hangi hedefi test ettiğini** kendi üstünde taşımalı |
| `saha_zorunlu_12_tam` | Satır geçerlilik kapısının **makinede okunabilir** hâli: `EVET` değilse satır modele giremez |

**Net:** 23 alan → **12 zorunlu + 5 proje zorunlusu + 3 opsiyonel + 2 yeni = 22 aktif alan**
(gözlemci satır seviyesinden mağaza seviyesine taşındığı için satır başına yazılan
alan sayısı **azalmıştır**).

---

## EK-B · ALT BANTLARIN HEDEFLERE BAĞLANMA GEREKÇESİ

Sabitlenen karar `PRIMARY 799 · SECONDARY 699 · STRETCH 899`'dur.
Odak bandı bu **üç hedefin etrafını** kapsayacak şekilde `500–1.200 TL` kurulmuştur:
alt uç, en riskli senaryonun (599 downside) **altına**; üst uç, projenin kendi
segment tavanı ESTIMATE'inin (900 TL) **belirgin üstüne** taşırılmıştır — sınır
görülmeden bandın *içi* okunamaz.

| Bant | Neden bu sınır | Hangi kaydı kırar |
|---|---|---|
| B1 500–629 | `OBSERVED_BENCHMARK` 599,90 tam buraya düşer; ayrıca 599 downside senaryosunun tek dayanağı burasıdır | `T-504`, `C-551`, `OQ-001`, 599 sınıflandırması |
| B2 629–769 | SECONDARY 699 ±%10 = 629–769; 649,90 benchmark'ı da içerir | 699 `ATTRACTIVE` sınıflandırması, `C-561` |
| B3 719–879 | **PRIMARY 799 ±%10**; `l8_chain_retail` çapası öncelikle burada aranır | **`T-701`**, `T-603`, 799 sınıflandırması |
| B4 809–989 | STRETCH 899 ±%10; "stokta ithal taban 875 TL" iddiası burada test edilir | 899 `PREMIUM_EDGE`, `segment.ithal_min_*` |
| B5 990–1.200 | Segment tavanı 900 TL **ESTIMATE**'inin dışı — tavanın doğru yerde olup olmadığı ancak dışarıdan görülür | `segment.fiyat_performans_ust_try` |

---

## EK-C · BU TUR YAPILIRSA KAPANACAK KAYITLAR

| Kayıt | Bugün | Tur sonrası | Koşul |
|---|---|---|---|
| **`T-917`** | OPEN | **RESOLVED** | §1 asgari kapsam tutturulursa |
| **`T-504`** | OPEN (HIGH) | **RESOLVED** *(promosyon işareti bulunursa)* / **ikinci ziyaret** *(bulunmazsa)* | §4 (a)(c)(e) + §12 |
| **`C-551`** | OPEN (HIGH) | **RESOLVED** | §4(b) okunabilir F2'de görülürse |
| **`OQ-001`** | PARTIALLY_RESOLVED | **RESOLVED** | KDV + mağaza/şehir + promosyon **üçü birlikte** kapanırsa |
| **`T-701` / `T-603`** | OPEN (HIGH) | **ANSWERED** — `l8_chain_retail` **dağılım** olarak dolar | ≥8 ithal zincir SKU |
| **`OQ-502`** | OPEN (HIGH) | **RESOLVED** | Zincir + tekel bayii gözlemi |
| **`C-501`** | OPEN (HIGH) | **RESOLVED veya ÇÜRÜTÜLÜR** | Fiziksel raf, `available` filtresinden **bağımsız** ikinci ölçümdür |
| **`C-561` / `OQ-552`** | OPEN | **RESOLVED** | §9 arama listesi + §7 stok alanı |
| **`OQ-503` / `T-405`** | OPEN | **RESOLVED** | Benchmark SKU'ların arka etiketi okunursa |
| `pazar.yaml` | `null`/`UNKNOWN` | Dolabilir: `l8_chain_retail`, `benchmark_*.promosyon_durumu`, `kdv_durumu.confidence`, `benchmark_*.magaza/sehir`, `benchmark_1.abv_pct`, `benchmark_2.hacim_ml`, `segment.*`, `ithalatci_haritasi.*`, `kanal_yapisi.tekel_bayii_fiyatlari` | Doldurmayı **ajan** yapar, gözlemci değil |

> **`kanal.yaml → m_retail`** bu turdan **beslenir ama burada hesaplanmaz.**
> Raf fiyatı gözlenir; **marj `kanal-marj-uzmani`nın işidir (K4).**

---

## EK-D · BU GÖREVİN KENDİ SINIRLARI

1. **Beyaz odak** → kırmızı/rosé için segment haritası **üretilmez**; yalnızca
   sayım formundan kaba yoğunluk çıkar. Kırmızı bir ürün ithal edilecekse
   **ayrı bir tur** gerekir.
2. **4–6 mağaza istatistiksel temsil DEĞİLDİR** ve öyle raporlanmayacaktır.
   Amaç temsil değil, **sıfır gözlemi sıfır olmaktan çıkarmaktır**.
3. **Tek tur `T-504`'ü asimetrik kapatır** — negatif sonuç kanıt değildir (§4).
4. **Metro fiyatı ≠ zincir fiyatı ≠ tekel fiyatı.** Üçü ayrı katmandır ve
   ortalaması alınamaz (K1).
5. Gözlemci **fiyat/performans yorumu yapmaz**, marj hesaplamaz, KDV durumunu
   **varsaymaz**. Yalnızca **okur, yazar, fotoğraflar.**
