# AJAN RAPORU — GLOBAL SOURCING KÂŞİFİ · TUR 3A

```yaml
ajan:               global-sourcing-kasifi
tur:                TUR 3A — RFQ ZORUNLU TEKNIK ALANLAR
tarih:              2026-08-10
durum:              SUBMITTED
yeni_arastirma:     YOK — yeni tedarikci/ulke/fiyat arastirmasi YAPILMADI
web_arama:          YOK — WebSearch/WebFetch kullanilmadi
dis_iletisim:       NONE — hicbir ureticiye e-posta/form/mesaj GONDERILMEDI
yeni_evidence:      YOK — 10-evidence/ acilmadi, index.csv'ye dokunulmadi
yazilan_dosyalar:   50-sourcing/rfq-template.md  (v2.1 -> v2.2)
                    50-sourcing/rfq-zorunlu-alanlar.md  (YENI)
                    50-sourcing/rapor-tur3a-global-sourcing.md
                    99-ops/tickets/T-881.md, T-882.md, T-883.md, T-884.md
                    99-ops/_parts/capraz-ipuclari-global-sourcing-kasifi-tur3a.md
                    99-ops/_parts/acik-sorular-global-sourcing-kasifi-tur3a.md
dokunulmayanlar:    10-evidence/index.csv, 99-ops/{capraz-ipuclari,celiskiler,
                    acik-sorular}.md, 99-ops/tickets/INDEX.md, 80-model/,
                    60-pazar/, 70-kanal/, 30-vergi-gumruk/, 40-lojistik/,
                    50-sourcing/rfq-alan-kontrolu.md (v2.1 donemi denetim kaydi)
```

---

## 1. YÖNETİCİ ÖZETİ

TUR 2.5'in 10 negotiation card'ında tekrar tekrar `Critical unknowns` olarak
görünen **8 teknik ürün alanı** — ABV, şişe ağırlığı, koli konfigürasyonu, palet
konfigürasyonu, etiket gereksinimleri, menşe belgesi, sertifika seti, Türkiye
ihracat geçmişi — RFQ şablonunda **cevapsız bırakılabilir soru** olmaktan
çıkarılıp **`[MANDATORY]` boş bırakılamaz alan** hâline getirildi (`M1…M8`).

Bunlar **yeni soru değildir**: `rfq-alan-kontrolu.md`'nin tespit ettiği gibi
v2.1 bu 8 alanı zaten soruyordu. Değişen şey **cevabın kabul kriteri**: her alan
için (a) kabul edilebilir birim ve biçim, (b) reddedilen cevap kalıpları
(*"yaklaşık" / "standart" / "genelde" / "talebe göre"*), (c) cevapsızlığın
teklife ne yaptığı tanımlandı ve **üreticiye önceden yazılı olarak bildirildi**.

**En kritik tek bulgu:** cevapsızlık kuralı 8 alanda **aynı olamaz**. Üç alan
(M2 şişe ağırlığı, M3 koli, M4 palet) cevapsızsa teklif **karşılaştırılamaz** —
EXW/FOB → CIF köprüsü kurulamaz, çünkü konteynere kaç şişe girdiği bilinmez
(`T-302`: %38'e varan kapasite sapması). Bu üçü için sonuç **değerlendirme
dışıdır**. M6 (menşe belgesi) için sonuç eleme değil **cezadır** (`DOC_FAIL`
varsayımı = **−%11,765 tavan**), çünkü eleme tedarikçiye tercih riskini sessizce
bize yükleme fırsatı verirdi. M1/M5/M7/M8 için sonuç yalnızca **etiketlemedir**.

**İkinci bulgu — dürüstlük kaydı:** M8 (Türkiye ihracat geçmişi) **hiçbir hesabı
`UNKNOWN` döndürmez.** Sayısal model girdisi beslemez; yürütme riski
göstergesidir. Bu rapor bunu açıkça yazıyor, çünkü 8 alana aynı ağırlığı vermek
gerçekten hesap kıran dört alanın (M2/M3/M4/M6) ağırlığını yok ederdi.

**RFQ v2.2 gerçek gönderime hazır mı: HAYIR** — içerik olarak hazır, ama üç
onay/teyit gönderimden önce gerekli (§6, §7).

---

## 2. BULGULAR

### B-1: 8 alanın hiçbiri 26 tedarikçi kaydının hiçbirinde doğrulanmamış

```yaml
claim:          "Kisa listedeki 26 tedarikcinin hicbirinde M1...M8'in tamami
                 dogrulanmamistir; M2 (sise agirligi) 26/26 bostur."
value:          26/26 (M2) · 25/26 (M3, M4) · 24/26 (M7) · 23/26 (M8)
unit:           satir
status:         FACT                  # kendi dosyalarimizin sayimi
tier:           -                     # ic veri sayimi, dis kaynak degil
evidence_id:    -                     # yeni kanit acilmadi; kaynak repo dosyalari
katman:         -
```

**Gerekçe:** `50-sourcing/supplier-shortlist-v2.csv` (26 satır) ve
`50-sourcing/tedarikci-havuzu.csv` (11 satır) kolon bazında sayıldı:

| Alan | shortlist-v2 (26) | tedarikci-havuzu (11) |
|---|---|---|
| M1 ABV | kolon yok | **11/11 `UNKNOWN`** |
| M2 bottle weight | **26/26 `UNKNOWN`** | kolon yok (planlı) |
| M3 case configuration | **25/26** | **11/11** |
| M4 pallet configuration | **25/26** | **11/11** |
| M6 origin document | kolon yok | **11/11** (`origin_proof_doc`) |
| M7 certificate set | **24/26** | **11/11** (`analysis_certificates`) |
| M8 Turkey export experience | **23/26** | **10/11** |

Bu, **soru eksikliği değil doluluk sorunudur** — v2.1 sekizini de soruyordu
(`rfq-alan-kontrolu.md`, 25/25 "soruluyor"). Dolayısıyla TUR 3A'nın müdahalesi
soru eklemek değil, **cevap kriterini tanımlamak** oldu.

---

### B-2: Cevapsızlık kuralı 8 alanda aynı olamaz — üç farklı sonuç

```yaml
claim:          "Zorunlu alanlarin cevapsizlik sonucu uc gruba ayrilir:
                 DEGERLENDIRME DISI (M2/M3/M4), CEZALI (M6), ETIKETLENIR (M1/M5/M7/M8)."
value:          3 grup / 8 alan
unit:           kural
status:         ASSUMPTION            # ticari kural, olculmus bir sonuc degil
tier:           -
evidence_id:    -
katman:         -
```

**Varsayım gerekçesi:** Tek tip kural iki yönden de hatalı olurdu.

- **Hepsi elenirse:** M8 (Türkiye ihracat geçmişi) sayısal bir model girdisi
  beslemiyor; onun yüzünden teklif elemek orantısızdır ve havuzu gereksiz
  daraltır.
- **Hiçbiri elenmezse:** M2/M3/M4 eksikken teklif **matematiksel olarak
  karşılaştırılamaz**. Fiyatı CIF'e çeviremediğimiz bir teklifi "değerlendirdik"
  demek, bandı gerçek sayı yerine koymak olurdu.

**M6'nın ayrı tutulması bilinçlidir.** Eleme yerine **cezalı değerlendirme**
seçildi: cevapsızlık `DOC_FAIL` varsayımıyla modele girer, yani tavan
**290,51 → 256,34 TRY/şişe** (Y köşesi, P grubu) okunur. Eleme, tedarikçiye
tercih riskini sessizce bize yükleme fırsatı verirdi; ceza ise riski
**fiyatlandırır** ve pazarlık kaldıracını bizde tutar.

**Alıntılanan sayı:** `%11,765` ve `−32,10 TRY/şişe`
`finans-fizibilite`'nin ters modelinden gelir (`reverse-price-model.md` §4.2,
`rfq-negotiation-cards.md` §0.4) ve **bu ajanın ürettiği bir sayı değildir.**

---

### B-3: M2/M3/M4 birlikte `T-302`'nin RFQ tarafını kapatıyor

```yaml
claim:          "T-302'nin 14 maddelik paketleme veri listesinin 12'si RFQ v2.2'de
                 zorunlu alan; 2'si (yaz yukleme politikasi, tercih edilen Incoterm)
                 soruluyor ama zorunlu degil."
value:          12/14 zorunlu · 2/14 zorunlu degil
unit:           madde
status:         FACT                  # sablon metninin kendi sayimi
tier:           -
evidence_id:    -
katman:         -
```

**Gerekçe:** Madde eşlemesi `T-882`'de tam tabloyla verildi. Zorunlu yapılmayan
iki madde:

| T-302 md. | Konu | Neden zorunlu yapılmadı |
|---|---|---|
| 13 | yaz yükleme / thermal liner / reefer | `lojistik.yaml → sicaklik_riski` bloğunun girdisi; **zorunlu alan sayısını kendi başıma artırmadım** — her ek zorunlu alan cevap oranını düşürüyor. Karar `navlun-lojistik-uzmani`'nın (`T-882`) |
| 14 | tercih edilen Incoterm + liman | v2.1'den beri soruluyor (3.16, 2.10, S13, S14); **fiyat karşılaştırmasını tek başına kırmıyor** çünkü EXW ve FOB zaten ayrı ayrı isteniyor |

**Ek olarak eklenen ve `T-302`'de olmayan tek şey:** çapraz tutarlılık kuralı —
`(dolu şişe × şişe/koli) + ambalaj ≈ koli brüt` ve
`(koli brüt × koli/palet) + palet ≈ yüklü palet brüt`. Tutmuyorsa sayı
**kullanılmaz**, `99-ops/celiskiler.md`'ye taşınır. Bu kural, zorunlu alan
baskısının **uydurma rakamı** teşvik etmesine karşı tek savunmadır.

---

### B-4: M5 ve M6 özet tabloda karşılığı olmayan iki alandı — S26 ve S27 eklendi

```yaml
claim:          "SUMMARY SHEET S1-S25, etiket uyarlama kabiliyetini ve mense belgesi
                 TAAHHUDUNU ayri satir olarak tasimiyordu; ikisi eklendi (S26, S27)."
value:          S1-S25 -> S1-S27
unit:           satir
status:         FACT
tier:           -
evidence_id:    -
katman:         -
```

**Gerekçe:**
- **M5 (etiket gereksinimleri)** v2.1'de yalnızca **detay** bölümlerde vardı
  (4.6, 6.8, 6.9). Özet tabloda tek etiket satırı **S19 idi ve o maliyettir**,
  kabiliyet değil. Kabiliyet ile maliyet karıştırılırsa "etiket yaparız,
  şu kadar" cevabı Türkçe arka etiket sorusunu **cevaplamış gibi** görünür.
- **M6 (menşe belgesi)** v2.1'de **S23'ün içine gömülüydü** ("Certificates you
  can issue: list (analysis, **origin proof type**, health/free sale, …)").
  Liste içinde geçen bir kalem, **taahhüt** olarak sorulamaz. Ayrıştırıldı;
  S23 sertifika setine daraltıldı, S27 kabiliyet **+ taahhüt** olarak yazıldı.

**Paralel liste yaratılmadı.** M1…M8 kodları mevcut S satırlarının üzerine
bindirildi; S26/S27 yeni **soru** değil, mevcut detay sorularının özet tabloya
taşınmasıdır.

---

### B-5: M1 (ABV) vergi gerekçesiyle zorunlu yapılamaz — ve yapılmadı

```yaml
claim:          "ABV OTV tutarini degistirmez; M1'in zorunlulugu etiket, beyan
                 satiri ve urun uygunlugu gerekcelerine dayanir."
value:          OTV = maktu, LITRE basina, ABV'den bagimsiz
unit:           -
status:         FACT                  # gumruk-vergi-uzmani'nin bulgusu — ALINTI
tier:           T1/T2 (kaynak ajanin tespiti)
evidence_id:    EV-2026-08-09-113 (OTV litre bazli) · EV-2026-08-09-102 (12 haneli
                alt kod vergi yukunu degistirmez) · EV-2026-08-09-101 (12 haneli
                kirilim ABV'ye dayanir) · EV-2026-08-09-221 (etikette ABV >=3 mm,
                tolerans +-%0,5 — mevzuat-ruhsat-uzmani)
katman:         -
```

**Gerekçe:** Bu alanı "vergiyi etkiliyor" diye gerekçelendirmek **yanlış olurdu**.
`gumruk-vergi-uzmani` ÖTV maktu tutarının **her bir litre** üzerinden ve
**ABV'den bağımsız** olduğunu tespit etmiş (`EV-2026-08-09-113`), ayrıca
2204.21 altındaki 12 haneli kırılımın **vergi yükünü değiştirmediğini**
göstermiştir (`EV-2026-08-09-102`).

M1 üç başka nedenle zorunludur: (a) etiket kapanışı (ABV karakter yüksekliği
≥3 mm, tolerans ±%0,5 — `EV-2026-08-09-221`), (b) beyanname satırı
(12 haneli kırılım ABV'ye dayanır — `EV-2026-08-09-101`), (c) ürünün modelde
varsayılan yapı içinde olduğunun teyidi.

**Sonuç olarak M1'in cevapsızlığı hiçbir maliyet hesabını `UNKNOWN` döndürmez**
ve bu nedenle eleme kuralı uygulanmaz — yalnızca `PRODUCT_SPEC_UNVERIFIED`
etiketi konur.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| U-881 | **Zorunlu alan kuralının cevap oranına etkisi** | Ölçmek gerçek gönderim gerektirir; dış iletişim bu turda yasak (`T-467` açık) | **MEDIUM** | ≥8 gönderim + M-doluluk oranı (`rfq-zorunlu-alanlar.md` §4.4). 2–4 hafta, TUR 7 |
| U-882 | **M5'in mevzuat tarafındaki kesin ölçüleri** (≥18 cm² yeterli mi; bandrol boş alanının tanımlı bir asgarisi var mı) | `mevzuat-ruhsat-uzmani`'nın alanı; bu ajan mevzuat sonucu üretmez | **HIGH** — yanlış ölçü sorulursa hata **antrepoda** ortaya çıkar | `T-881` |
| U-883 | **M6 kabul kriteri** — dört koşulun (belge adı + her sevkiyat taahhüdü + dökme bileşen yok + çıkış limanı) hepsi gerekli mi | `gumruk-vergi-uzmani`'nın alanı | **HIGH** — fazla sıkıysa model gereksiz yere aleyhimize sapar | `T-883` |
| U-884 | **Fatura beyanı değer eşiği** — RFQ 6.13(b) eşiği rakamsız soruyor | `T-162` zaten `UNKNOWN` ve `gumruk-vergi-uzmani`'nın alanında açık | MEDIUM | `T-162` kapanışı |
| U-885 | **Kaç tedarikçi cevabı `paketli_sise_hacim_m3` bandını kapatır** | `navlun-lojistik-uzmani`'nın alanı | MEDIUM | `T-882` |
| U-886 | **Zorunlu alan baskısının yanlış rakam üretip üretmediği** | Beyanla fiziksel gerçeğin karşılaştırılması numune gerektirir | MEDIUM | Numune şişenin fiilen tartılması/ölçülmesi (RFQ 7.1–7.5), TUR 7 |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A | Kaynak B | Neden çelişiyor | Durum |
|---|---|---|---|---|
| — | — | — | **Bu turda yeni çelişki üretilmedi.** Yeni araştırma yapılmadı, yeni kaynak okunmadı; çelişki üretecek ikinci bir kaynak yok. `C-881…C-899` bloğu **kullanılmadı**. | — |

**Not:** RFQ v2.2, gelecekte çelişki üretecek bir mekanizma **ekledi**: koli ↔ şişe
↔ palet çapraz tutarlılık kontrolü. Tedarikçinin kendi verdiği üç sayı birbirini
doğrulamazsa bu bir `CONFLICT`'tir ve `99-ops/celiskiler.md`'ye taşınır — sessizce
seçim yapılmaz.

---

## 5. MODEL GİRDİLERİ

**Bu turda `80-model/inputs/*.yaml` dosyalarına giden hiçbir değer üretilmemiştir.**
`80-model/` DOKUNMA listesindeydi ve zaten dolduracak veri yok: teklif alınmadı.

Aşağıdaki tablo, **teklif geldiğinde** hangi zorunlu alanın hangi model girdisine
gideceğini gösterir — bir **eşleme taahhüdüdür**, veri değildir:

| Kod | YAML dosyası | Alan | Bugünkü değer |
|---|---|---|---|
| M1 | `urun.yaml` | `urun.abv_pct` | `null` / `UNKNOWN` |
| M2 | `urun.yaml` | `sise_spesifikasyonu.bos_sise_agirligi_g`, `.dolu_sise_brut_agirligi_g` | `null` / `UNKNOWN` |
| M2 | `lojistik.yaml` | `urun_fizik.bos_cam_agirlik_g`, `.dolu_sise_brut_agirlik_kg` | bant / geri hesap |
| M3 | `lojistik.yaml` | `urun_fizik.paketli_sise_hacim_m3`, `.koli_brut_agirlik_kg`, `.koli_formati` | **bant** (0,00223 / 0,00239 / 0,00360) |
| M4 | `lojistik.yaml` | `urun_fizik.palet_basina_sise.*`, `.yuklu_palet_brut_kg.*`, `.yuklu_palet_yukseklik_mm`, `konteyner.palet_sayisi.*` | 4 senaryo, hangisi geçerli `UNKNOWN` |
| M5 | `tedarikci.yaml` / `ruhsat.yaml` / `lojistik.yaml` | `private_label.turkce_arka_etiket_menside_uygulanabilir_mi` · `urun_uygunlugu.*` · `bandrolleme_operasyonu.*` | `UNKNOWN` |
| M6 | `tedarikci.yaml` | `belgeler.mense_ispat_belgesi` | `UNKNOWN` (11/11) |
| M7 | `tedarikci.yaml` / `ruhsat.yaml` | `belgeler.analiz_sertifikasi` · `analiz_laboratuvar.*` | `null` / `UNKNOWN` |
| M8 | `tedarikci.yaml` | `risk.turkiyeye_ihracat_gecmisi` | `UNKNOWN` (10/11) |

**evidence_id'si olmayan satır modele giremez** — ve bu tablodaki hiçbir satırın
bugün evidence_id'si yoktur, çünkü hiçbirinin verisi yoktur.

---

## 6. AÇILAN TICKET'LAR

| ticket | hedef ajan | impact | konu |
|---|---|---|---|
| **`T-881`** | `mevzuat-ruhsat-uzmani` | HIGH | M5'in üç ölçüsü (≥18 cm², bandrol boş alanı, ABV ≥3 mm) üreticiye **taahhüt olarak** sorulmadan önce teyit |
| **`T-882`** | `navlun-lojistik-uzmani` | HIGH | `T-302`'nin 14 maddesinin RFQ karşılığı tam mı; 13. madde zorunlu olmalı mı; bant ne zaman kapanır |
| **`T-883`** | `gumruk-vergi-uzmani` | HIGH | M6 **kabul kriteri**; `T-162` eşiği RFQ'ya rakam olarak yazılabilir mi; OD-4 menşe grubuna göre farklılaşmalı mı |
| **`T-884`** | `yatirim-komitesi-baskani` | HIGH | **Cevapsızlık/eleme kuralının onayı** — M2/M3/M4 "değerlendirme dışı" kuralı kısa listeyi boşaltabilir; 4 seçenek sunuldu |

`99-ops/tickets/INDEX.md` DOKUNMA listesindeydi; **güncellenmedi.** Dört ticket
dosyası açıldı, indeks satırları **başkan tarafından** eklenecektir.

---

## 7. RFQ v2.2 GERÇEK GÖNDERİME HAZIR MI

# HAYIR

İçerik olarak tamamlandı; **gönderim koşulları sağlanmadı.** Eksikler:

| # | Engel | Sahibi | Ticket |
|---|---|---|---|
| 1 | **Dış iletişim izni yok** — RFQ gönderimi `G2` kapısına bağlı | `yatirim-komitesi-baskani` | `T-467` (OPEN) |
| 2 | **`<VOLUME>` doldurulmadı** — şablon §0.9 gereği doldurulmadan gönderilen RFQ **geçersizdir**; hangi hacim basamağı ve hangi kanal olduğu karar bekliyor | `yatirim-komitesi-baskani` | `T-871` (OPEN) |
| 3 | **Cevapsızlık/eleme kuralı onaylanmadı** — üreticiye §0'da yazdığımız sonuçlar ile iç kuralımızın aynı olması gerekir | `yatirim-komitesi-baskani` | **`T-884`** (YENİ) |
| 4 | **M5'in ölçüleri mevzuatça teyit edilmedi** — ≥18 cm² ifadesi teyide kadar "en az" olarak yazıldı; teyit gelmezse o cümle **gönderilmez** | `mevzuat-ruhsat-uzmani` | **`T-881`** (YENİ) |
| 5 | **M6 kabul kriteri belirsiz** — soru gönderilebilir, ama gelen cevabın `DOC_OK` sayılıp sayılmayacağı kriter olmadan uygulanamaz | `gumruk-vergi-uzmani` | **`T-883`** (YENİ) |
| 6 | Karar `TEST` / `IMPORT PILOT` değil | `yatirim-komitesi-baskani` | TUR 6 |

**1, 2 ve 3 kapanmadan hiçbir üreticiye gönderim yapılmaz.** 4 ve 5 kapanmadan
gönderilebilir (sorular yine de değerli), ama gelen cevap **değerlendirilemez** —
yani gönderim erken olur.

---

## 8. BU BULGUYU NE ÇÜRÜTÜR?

### 8.1 "8 alanı zorunlu yapmak veri kalitesini artırır" iddiasını ne çürütür?

**Cevap oranının çökmesi.** Bu, en olası çürütme yoludur ve **kendi
dosyalarımızda zaten uyarı olarak duruyor**: `rfq-alan-kontrolu.md` §5.1,
v2.1 için *"uzun RFQ'nun tipik sonucu daha eksiksiz cevap değil, **daha az
cevap** olabilir"* demişti. **TUR 3A bu riski azaltmadı — artırdı.** SUMMARY
SHEET 25 → 27 satır, M5/M6 alt sorularıyla ~15 yeni cevap alanı.

Somut çürütme senaryosu: üretici formu doldurmak yerine kendi standart PDF
fiyat listesini gönderir. O PDF'te M2/M3/M4 **yoktur** (hiçbir üreticinin fiyat
listesinde palet yüksekliği yazmaz). Bizim kuralımız o teklifi **değerlendirme
dışı** bırakır. Sonuç: kural teknik olarak çalışır, **ticari olarak elimizde
hiçbir teklif kalmaz.**

**Erken uyarı göstergesi:** ilk 8 gönderimde **M-doluluk oranı < %50** ise sorun
tedarikçide değil şablondadır ve zorunlu alan sayısı düşürülür (öncelik:
M2/M3/M4/M6 kalır; M1/M5/M7/M8 ikinci aşamaya). Bu metrik
`rfq-zorunlu-alanlar.md` §4.4'te tanımlandı ve TUR 7'de ölçülecek.

### 8.2 "Zorunlu alan doğru veri getirir" iddiasını ne çürütür?

**Boş bırakılamayan alan, tedarikçiyi bir şey yazmaya iter.** `"standart"`
cevabını reddetmek, o cevabı **uydurma bir rakama** dönüştürebilir — ve uydurma
bir rakam, boş bir alandan **daha tehlikelidir**, çünkü modele girer ve
`UNKNOWN` uyarısı üretmez.

Kısmi savunma var: koli ↔ şişe ↔ palet çapraz tutarlılık kontrolü. Ama bu
kontrol **tek bir tutarlı ama yanlış** paketleme setini yakalayamaz — üretici
gerçekte kullanacağı ambalajı değil, kataloğundaki başka bir ambalajı verirse
üç sayı da birbirini doğrular ve hepsi yanlıştır.

**Tek gerçek doğrulama:** numune sevkiyatında gelen şişenin **fiilen tartılıp
ölçülmesi** (RFQ 7.1–7.5). Bu TUR 7'de yapılmalıdır ve bugün yapılmamıştır.

### 8.3 "M2/M3/M4 cevapsızsa teklif karşılaştırılamaz" iddiasını ne çürütür?

**Bandın yeterli olduğunun gösterilmesi.** Eğer `navlun-lojistik-uzmani`
`T-882`'de *"paketli şişe hacmi bandı karar için yeterli, %38 sapma sonucu
değiştirmiyor"* derse, eleme kuralının **tüm gerekçesi düşer** ve kural
`T-884` seçenek B'ye (bant + `FREIGHT_BAND_ESTIMATE` etiketi) inmelidir.

Bunu ölçmenin yolu var: bandın iki ucuyla (0,00223 ve 0,00360) hesaplanan şişe
başı navlunun, `RFQ TARGET CEILING X` (200,98) ile `Y` (290,51/256,34) arasındaki
**89,53 TRY/şişe**'lik bandı aşıp aşmadığına bakılır. Aşmıyorsa eleme kuralı
gereksiz sertliktir. **Bu hesabı ben yapamam — navlun tutarı benim alanım
değildir.**

### 8.4 "M6 cezalı değerlendirme doğru kurgu" iddiasını ne çürütür?

**Kabul kriterinin fazla sıkı olduğunun gösterilmesi.** Bugünkü kural dört
koşulu birden arıyor. `gumruk-vergi-uzmani` `T-883`'te *"belge adı + her sevkiyat
taahhüdü yeterlidir, dökme bileşen ve çıkış limanı ayrı kontrol edilir"* derse,
bugünkü kural belgesi gerçekten düzenlenebilecek tedarikçileri de
**−%11,765 ile cezalandırıyor** demektir — yani model **gereksiz yere**
aleyhimize sapıyor ve iyi tedarikçileri kötü gösteriyor.

Ayrıca `T-872` (OD-5'in hukuki geçerliliği) açıktır: fiyat düzeltme maddesi
uygulanamıyorsa, RFQ 6.14 **cevap alsa bile** işe yaramaz.

### 8.5 Bu turun en zayıf noktası

**Bu kuralları kendi yazdığım şablon üzerinde kendim tanımladım ve hiçbirini
tek bir gerçek tedarikçi cevabıyla test etmedim.** `rfq-alan-kontrolu.md` §5.3
aynı öz-değerlendirme sorununu v2.1 için yazmıştı; TUR 3A'da **aynı sorun
devam ediyor**, üstelik artık ortada bir **eleme kuralı** var — yani
öz-değerlendirmenin bedeli daha yüksek.

En temiz bağımsız kontrol: `seytanin-avukati` şablonu **bir tedarikçi gibi**
doldurup, 8 zorunlu alanın kaçının **kaçamak ama biçimsel olarak geçerli**
cevapla geçilebildiğini göstermeli. Örneğin S24'e *"Yes — Middle East region
including Turkey, since 2019, various volumes"* yazılırsa: format kabul edilebilir
görünür, ithalatçı adı yoktur, hacim yoktur ve bizim tarama kuralımız bunu
yakalar mı — **test edilmedi.**

### 8.6 Kim, nasıl, ne kadar sürede doğrular?

| # | Ne | Kim | Nasıl | Süre |
|---|---|---|---|---|
| 1 | Kaçamak cevaba açık zorunlu alanlar | `seytanin-avukati` | Tedarikçi rolüyle 8 alanı doldurup boşlukları göstermek | 1 gün |
| 2 | Bandın karar için yeterli olup olmadığı | `navlun-lojistik-uzmani` | Bandın iki ucuyla şişe başı navlun → X/Y bandını aşıyor mu (`T-882`) | 1 gün |
| 3 | M6 kabul kriteri | `gumruk-vergi-uzmani` | `T-883` | T-161/T-162 sonrası |
| 4 | M5 ölçülerinin doğruluğu | `mevzuat-ruhsat-uzmani` | `T-881` | 1–2 gün |
| 5 | Eleme kuralının ticari kabulü | `yatirim-komitesi-baskani` | `T-884` — 4 seçenek | karar turu |
| 6 | Gerçek M-doluluk oranı | `global-sourcing-kasifi` | ≥8 gönderim, doluluk ölçümü | 2–4 hafta (TUR 7) |
| 7 | Beyan ↔ fiziksel gerçek | `global-sourcing-kasifi` | Numune şişenin tartılması/ölçülmesi | TUR 7 |
