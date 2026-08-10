# AJAN RAPORU — kanal-marj-uzmani, TUR 2

```yaml
ajan:   kanal-marj-uzmani
tur:    TUR 2
tarih:  2026-08-10
durum:  SUBMITTED
```

---

## 1. YÖNETİCİ ÖZETİ

Türkiye'de bir ithal şarabın **hangi fiyata satılabileceğini** belirleyen
L6 → L7 → L8 merdiveninin **yapısı** çıkarıldı; **sayısal olarak kapatılamadı** ve
kapatılmış gibi gösterilmedi. En kritik tek bulgu şudur: **Türkiye'de kanal ticari
koşullarının VARLIĞI kanıtlanabilir, TUTARLARI kanıtlanamaz** — Rekabet Kurumu'nun
kendi sektör raporunda bile bedellerin ciroya oranı ve zincirlerin brüt marjı
**ticari sır olarak karartılmıştır**, üstelik o analiz **"alkol ve tütün hariç"**
tanımlıdır (`EV-2026-08-10-610`, `EV-2026-08-10-611`).

Buna karşılık **alkollü içkiye özgü** bir kanıt bulundu: Rekabet Kurulu kararı
21-51/708-351, MİGROS/CARREFOUR/ÖZDİLEK/**METRO**/TESPO ile imzalanan **yıllık satış
anlaşmalarının** kalem listesini açıkça yazar — *CRM, B2B (kasa çıkışı cirosu), alan
kullanımı, **kırık ürün bedeli**, lojistik bedeli, soğutucu enerji bedeli* ve **geri
ödeme vadesi** (`EV-2026-08-10-612`). Bu, "zincire kaç para ödeyeceğiz" sorusunun
**satır adlarını** kanıtlar, tutarlarını değil.

İkinci kritik bulgu **ödeme vadesidir**: 6585 s.K. m.7/3 (yürürlük **01.01.2024**)
30 günde bozulmayan tarım-gıda ürünlerinde vadeyi **60 günle** sınırlar
(`EV-2026-08-10-602`), yaptırımı da vardır (`EV-2026-08-10-603`). Buna karşılık
Migros'un 2025 denetlenmiş finansallarında ticari borçların **%34,4'ü 3–12 ay
vadelidir** ve DPO **~93 gündür** (`EV-2026-08-10-617`). Bu **`C-601`** olarak açık
bırakılmıştır ve şarabın "tarım ve gıda ürünü" sayılıp sayılmadığı sorusu
(`T-601`, CRITICAL) cevaplanmadan çözülemez.

Üçüncü bulgu **kabul edilmiş reklam kısıtının kanal ekonomisine yaptığı yapısal
etkidir**: Perakende Yönetmeliği m.5/2(d), perakendecinin bedel karşılığı
verebileceği hizmetleri **iki gruba** ayırır — *tanıtım hizmeti* ve *teşhir
ünitelerinde özel konumlandırma* (`EV-2026-08-10-605`). Alkolde birincisi fiilen
satın alınamaz (`İP-2001`). **Yani ödeyeceğimiz listeleme bedelinin karşılığında
alabileceğimiz tek şey fiziksel raf konumudur** — ve aynı anda tüketiciye ulaşmanın
başka yolu da yoktur.

---

## 2. BULGULAR

### B-1: Alkollü içki zincir yıllık anlaşmasının kalem listesi kanıtlıdır

```yaml
claim:          "Ulusal zincirlerle (Migros, Carrefour, Ozdilek, Metro, Tespo) alkollu ickide BIRER YILLIK satis anlasmasi imzalanir; icerikte CRM, B2B (kasa cikisi cirosu), alan kullanimi, kirik urun bedeli, lojistik bedeli, sogutucu enerji bedeli ve geri odeme vadesi yazilidir."
value:          "6 bedel kalemi + vade; sure 1 yil"
unit:           "-"
status:         FACT
tier:           T2
evidence_id:    EV-2026-08-10-612
effective_date: 2021-10-21
katman:         "L6 -> L7 gecisini belirleyen kalemler"
```

**Gerekçe:** Bu, projenin bulabildiği **tek alkole özgü kanal sözleşmesi kanıtıdır**
ve FMCG genellemesi değildir. Dört ayrı model sonucu üretir:
(1) Metro dahil **her zincirle yıllık anlaşma** imzalanır — Metro "tek fiyat listesi"
değildir (`İP-501`/`İP-505` ile tutarlı, `T-506`'ya kanal tarafının cevabı);
(2) **kırık ürün bedeli** kalemi, cam şişede kırılma riskinin sözleşmeyle
tedarikçiye yansıtıldığını gösterir; (3) **lojistik bedeli**, zincirin depo/dağıtım
kesintisi aldığını gösterir → zincir kanalında "kendi dağıtım" tasarrufu daha
küçüktür; (4) vade sözleşmede yazılıdır, teamül değildir.
**Tutarlar kararda karartılmıştır → tutarlar UNKNOWN.**

---

### B-2: Listeleme bedeli yasaldır ama şarapta karşılığı yapısal olarak dardır

```yaml
claim:          "Perakendeci, urun talebini dogrudan etkileyen bir hizmet verdigi ve hizmetin turu + bedelin tutar/orani sozlesmede yazili oldugu surece prim/bedel alabilir. Bedel karsiligi verilebilecek hizmetler IKI gruptur: tanitim hizmeti VEYA teshir unitelerinde ozel konumlandirma. Alkolde birincisi fiilen satin alinamaz."
value:          "gecerli hizmet kategorisi sayisi: 2 -> sarapta fiilen 1"
unit:           adet
status:         FACT (hukum) + ESTIMATE (sarapta daralma)
tier:           T3
evidence_id:    [EV-2026-08-10-601, EV-2026-08-10-605]
effective_date: 2024-01-01
katman:         "L6 -> L7"
```

**Gerekçe:** "Zincir listeleme bedeli isteyemez" varsayımı **yanlış** olurdu;
bedel mesrudur. Ancak bedel **sözleşmeye yazılmak zorundadır** → gizli kalem olamaz,
pazarlıkta görünür olur. Şarapta daralmanın kaynağı `İP-2001`/`T-205` ile kabul
edilmiş iş kısıtıdır — **kısıt yeniden araştırılmamış, veri olarak kullanılmıştır**.

**Türetme zinciri (ESTIMATE kısmı):** Yönetmelik m.5/2(d) iki hizmet grubu sayar
(`EV-605`) → alkolde reklam/tanıtım/anons kabul edilmiş kısıt gereği yoktur
(`EV-2026-08-09-222`, `-223`) → geriye yalnızca fiziksel konumlandırma kalır.

---

### B-3: Ödeme vadesinde yasal tavan ile gözlenen pratik çelişiyor

```yaml
claim:          "6585 m.7/3: 30 gunde bozulmayan tarim-gida urunlerinde odeme suresi (alacakli kucuk/orta + borclu orta/buyuk ise) ALTMIS GUNU GECEMEZ; ihlalinde gunluk binde 5 / %1 idari para cezasi vardir. Buna karsilik Migros 2025 finansallarinda ticari borclarin %34,4'u 3-12 ay vadelidir (DPO ~93 gun)."
value:          "yasal tavan 60; gozlenen 70 (sut, 2020) / ~93 (Migros DPO, 2025)"
unit:           gun
status:         CONFLICT
tier:           "T3 (hukum) / T2 (RK) / T4 (Migros)"
evidence_id:    [EV-2026-08-10-602, EV-2026-08-10-603, EV-2026-08-10-609, EV-2026-08-10-617]
effective_date: 2024-01-01
conflict_id:    C-601
katman:         "L7 tahsilat zamanlamasi -> CCC / peak_cash_requirement"
```

**Türetme zinciri (DPO):** 79.822.747 / 312.409.547 × 365 = **93,3 gün**.
Daha güçlü ve türetmesiz gözlem: vade tablosunda 27.612.023 / 80.203.283 = **%34,4**
üç aydan uzun vadelidir.

**Sessiz seçim yapılmadı.** `kanal.yaml → zincir_market.odeme_vadesi_gun = null`.
Yerine dört senaryo: **45 / 60 / 90 / 120 gün**.

---

### B-4: Şarapta iade ve fire riski hukuken korumasızdır

```yaml
claim:          "Satilamama gerekcesiyle iade yasagi YALNIZCA 30 gun icinde bozulabilen tarim-gida urunleri icin; %5 iade siniri ise YALNIZCA azami fiyati tarifeyle belirlenen mallar icindir. Sarap her ikisinin de disindadir -> sarapta iade tamamen SOZLESMESELDIR."
value:          "yasal iade korumasi: YOK"
unit:           "-"
status:         FACT
tier:           T3
evidence_id:    EV-2026-08-10-606
effective_date: 2024-01-01
katman:         "L6 -> L7 (iade), L5 (fire)"
```

**Gerekçe:** Süt/ekmek gibi ürünleri koruyan hükümler şarabı **korumaz**. Buna
`EV-2026-08-10-612`'deki **kırık ürün bedeli** ve `Cİ-15.1`'deki **zayi olan mala ait
KDV'nin indirilememesi** eklenince, cam şişede fire üç ayrı kanaldan maliyet üretir:
malın kendisi + indirilemeyen KDV + sözleşmesel kırık ürün bedeli.
**"İade riski yoktur" varsayımı yanlıştır.**

---

### B-5: Kanal evreni resmî olarak biliniyor; ciro dağılımı bilinmiyor

```yaml
claim:          "Alkollu icecek satan nokta sayisi (2020, TADB): GK (geleneksel kapali nokta) 48.956; ASN/YT (HoReCa) 29.218. Modern kanal (zincir) nokta sayisi ayni tabloda KASTEN yoktur (merkezi alim)."
value:          {GK: 48956, ASN: 29218, MK: null}
unit:           adet
status:         FACT
tier:           T2
evidence_id:    EV-2026-08-10-613
effective_date: 2020-12-31
katman:         "-"
```

**Gerekçe:** Charter'ın üç kanalı bu resmî taksonomiye oturur: chain retail = **MK**,
independent/tekel = **GK**, HoReCa = **ASN/YT**. **Nokta sayısı ciro payı değildir**
ve öyle kullanılmamıştır → `kanal_karmasi` üç alanı da `null` (`T-603`).

---

### B-6: Zincir perakende brüt marjı için tek çapa vardır ve şarap değildir

```yaml
claim:          "Migros 2025 konsolide: net satis 412.756.429 bin TL, satislarin maliyeti 312.409.547 bin TL -> brut marj %24,31."
value:          24.31
unit:           "%"
status:         FACT (Migros) / ESTIMATE (sarap icin proxy)
tier:           T4
evidence_id:    EV-2026-08-10-616
effective_date: 2025-12-31
katman:         "L7 -> L8"
```

**Marj disiplini:** **MARGIN on selling price** · **BRÜT** · **KDV HARİÇ** ·
**L7 → L8**. Markup karşılığı **%32,12**.

**Üç ayrı hata kaynağı (modelde belirtilmelidir):** (1) tüm kategori karmasıdır;
(2) alkol resmî marj analizinin kapsamı dışıdır (`EV-611`); (3) **raporlanan brüt
marj tedarikçiden alınan bedelleri içerir** — Rekabet Kurumu metodolojisi satın alım
maliyetinden ciro primi + aktivite primi + iade tutarı + ürün imha bedeli + iskonto
faturalarını düşer. Yani `tedarikçi_toplam_yükü = m_retail + d + f/L6` ve bunlar
**üst üste binmez, toplanır**.

---

### B-7: Şarapta satış noktalarıyla beş yıllık sözleşmeler var

```yaml
claim:          "Mal Alim Sozlesmeleri, Kurul muafiyet karari sonrasinda YALNIZCA SARAP kategorisinde ve BES YILLIGINA imzalanmaktadir."
value:          5
unit:           yil
status:         FACT
tier:           T2
evidence_id:    EV-2026-08-10-614
effective_date: 2021-10-21
katman:         "-"
```

**Gerekçe:** Bu bir **münhasırlık iddiası değildir** — aynı karar şarapta
münhasırlık olmadığının beyan edildiğini kaydeder (para.90). Ancak yeni bir
ithalatçı için **noktaların bir kısmının çok yıllık bağlı olması** gerçek bir erişim
riskidir. **Kaç noktanın bağlı olduğu UNKNOWN** (tablolar karartılmış) → `OQ-607`.
Bu, listeleme bedelinden **daha ölümcül** bir engel olabilir.

---

### B-8: Kendi dağıtımın ekonomik mantığı, charter'ın kanal önceliğiyle ters yönde

```yaml
claim:          "Zincir market merkezi alim yapar ve zaten lojistik bedeli alir -> zincir kanalinda kendi dagitimin marjinal faydasi dusuktur. Kendi dagitimin gercek degeri GK (48.956) ve ASN (29.218) kanallarindadir."
value:          "kanal karmasi -> dagitim modeli (tersi degil)"
unit:           "-"
status:         ESTIMATE
tier:           T2
evidence_id:    [EV-2026-08-10-612, EV-2026-08-10-613]
katman:         "L5 (dagitim maliyeti)"
```

**Türetme zinciri:** `EV-613` dipnot 14 → zincirler merkezi alım yapar, teslimat
noktası sayısı azdır → basit nakliyeci yeterli. `EV-612` → zincir zaten lojistik
bedeli alır, yani dağıtım maliyetinin bir kısmı **zaten bize fatura edilmektedir**.
Charter'ın kanal önceliği 1 = zincir; ama kendi dağıtımın değeri öncelik 2 ve 3'te.
**Dağıtım modeli bağımsız bir karar değişkeni değil, kanal karmasının türevidir.**

---

### B-9: 5.000 şişe/yıl senaryosunda kendi dağıtım aritmetik olarak imkânsız

```yaml
claim:          "5.000 sise/yil = ayda ~417 sise. Tek kisinin 2026 asgari ucret ISVEREN MALIYETI tabani (40.214,03 TL/ay, imalat disi) tek basina 96,4 TL/sise eder."
value:          96.4
unit:           TRY/sise
status:         ESTIMATE
tier:           T2
evidence_id:    EV-2026-08-10-621
effective_date: 2026-01-01
katman:         "L5"
```

**Türetme zinciri:** 40.214,03 / (5.000/12) = 40.214,03 / 416,67 = **96,5 TL/şişe**.
Bu, `pazar.yaml`'ın fiyat/performans bandının (600–900 TL) **%11–16'sıdır** — ve
**yalnızca bir kişinin asgari ücret tabanıdır**: araç, yakıt, depo, prim, back-office
**hariç**. Bir hesap değil, bir **büyüklük mertebesi kontrolüdür**.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | Zincirin **şarap kategorisi** brüt marjı | Resmî analiz "alkol ve tütün hariç"; tüm oranlar karartılmış (`EV-611`) | **CRITICAL** | Gerçek yıllık anlaşma müzakeresi (`T-604`) |
| 2 | Listeleme / giriş bedeli **tutarı ve birimi** | Güncel kamu kaynağı yok; tek iz 2004 T5 (`EV-619`) | **CRITICAL** | `T-604` |
| 3 | **Dış distribütör marj oranı** | Ne T4 ne T5, **hiçbir kanıt yok** | **CRITICAL** | `T-604` — A/B kararı bunsuz verilemez |
| 4 | `L8_CHAIN_RETAIL` | Alkol online satılamıyor; zincirde sıfır gözlem | **CRITICAL** | `T-603` — fiziksel mağaza turu |
| 5 | Kanal bazında **ciro dağılımı** | Kamuya açık veri yok; elde yalnızca nokta sayısı | **CRITICAL** | `T-603` |
| 6 | Şarap "tarım ve gıda ürünü" mü (60 gün tavanı) | Hukuki niteleme bu ajanın alanı değil | **CRITICAL** | `T-601` |
| 7 | Ciro primi **oranı** ve kademeleri | Karartılmış (`EV-610`) | HIGH | `T-604` |
| 8 | Alan kullanımı / kırık ürün / lojistik / enerji bedeli **tutarları** | Karartılmış (`EV-612`) | HIGH | `T-604` |
| 9 | Tekel bayii marjı | Yalnızca çelişen, tanımsız T5 (`EV-620`) | HIGH | `T-604` |
| 10 | HoReCa çarpanı | Tek kaynak T5 ve 2012; kendi içinde iki katman veriyor (`EV-618`) | HIGH | Fiziksel menü örneklemi |
| 11 | **İade oranı** | Yasal düzenleme yok; sözleşmesel | HIGH | `T-604` |
| 12 | Kaç nokta 5 yıllık sözleşmeyle bağlı | Tablolar karartılmış (`EV-614`) | HIGH | Saha gözlemi |
| 13 | Metro mağaza vs sevkiyat fiyatı farkı | Metro fiyatları müşteriye özel (`İP-505`) | HIGH | `T-604` |
| 14 | 2015'teki "raf garantisi" 2024'te var mı | T1 doğrulaması yapılamadı (`EV-622`) | HIGH | `T-601` |
| 15 | Modern kanal alkol satan nokta sayısı | TADB tablosunda kasten yok | MEDIUM | TADAB listeleri |
| 16 | Zincirin şaraba ayırdığı raf/SKU kotası | Kamu kaynağı yok | MEDIUM | Mağaza turu |
| 17 | Kendi dağıtım maliyet kalemleri (48 alan) | Şirket verisi ve teklif gerektirir | HIGH | Kurucu + 3PL teklifleri |
| 18 | Tadım/aktivasyon kaleminin modellenmesi | Kabul edilmiş kısıtın kapsam belirsizliği; **yeniden araştırılmadı** | MEDIUM | Başkan kararı (`T-604`) |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-601** | 6585 m.7/3 — vade **≤60 gün** (T3, yür. 2024-01-01) `EV-602` | RK On Rapor — organize kanal **70 gün** (T2, 2020) `EV-609` **+** Migros — borçların **%34,4'ü 3–12 ay**, DPO **~93 gün** (T4, 2025) `EV-617` | Yasal tavan yürürlükteyken bile gözlenen vade tavanın üstünde. Üç açıklama mümkün: şarap kapsam dışı / ölçek testi & KOBİ belgesi işlemiyor / Migros verisi gıda dışı+yurt dışı içeriyor. Ayrıca `EV-609` dipnot 69: "fiili süreler sözleşmedekinden çok daha uzun olabilmektedir." | **OPEN** |
| **C-602** | Tekel bayii marjı: T5 iddiaları **%6 / %8 / %10-15 / %17 / %18-30** (`EV-620`) · HoReCa çarpanı: **aynı yazı** çarpanı hem L8 hem L7 üzerinden veriyor (`EV-618`) | — | Çelişki kaynaklar arasında değil, **kaynakların kendi içinde**: hiçbiri margin/markup, KDV tabanı ve katman çiftini belirtmiyor → `M1` gereği hepsi geçersiz | **OPEN** |

`99-ops/_parts/celiskiler-kanal-marj-uzmani-tur2.md` dosyasına ayrıntılı yazıldı.
**Ana `celiskiler.md` dosyasına dokunulmadı.**

---

## 5. MODEL GİRDİLERİ

| YAML | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| `kanal.yaml` | `zincir_market.tum_kategori_proxy_marj_pct` | 24,31 (markup 32,12) | % | FACT (proxy) | `EV-2026-08-10-616` |
| `kanal.yaml` | `zincir_market.ticari_kosul_kalemleri` | 6 kalem listesi | — | FACT | `EV-2026-08-10-612` |
| `kanal.yaml` | `zincir_market.odeme_vadesi_yasal_tavan_gun` | 60 | gün | FACT (kural) | `EV-2026-08-10-602`, `-604` |
| `kanal.yaml` | `...yasal_tavan.yaptirim` | binde 5/gün, sonra %1/gün | % | FACT | `EV-2026-08-10-603` |
| `kanal.yaml` | `zincir_market.odeme_vadesi_gozlenen_gun` | 70 (süt, 2020) | gün | FACT (proxy) | `EV-2026-08-10-609` |
| `kanal.yaml` | `zincir_market.zincir_dpo_gun` | 93 | gün | ESTIMATE | `EV-2026-08-10-617` |
| `kanal.yaml` | `zincir_market.iade_kosullari` | "yasal sınır yok" | — | FACT | `EV-2026-08-10-606` |
| `kanal.yaml` | `zincir_market.kirik_urun_sorumlulugu` | "sözleşmeyle tedarikçiye" | — | FACT | `EV-2026-08-10-612` |
| `kanal.yaml` | `tekel_bayi.nokta_sayisi` | 48.956 | adet | FACT | `EV-2026-08-10-613` |
| `kanal.yaml` | `tekel_bayi.listeleme_bedeli` | 0 | TRY | ESTIMATE | `EV-2026-08-10-601` |
| `kanal.yaml` | `horeca.nokta_sayisi` | 29.218 | adet | FACT | `EV-2026-08-10-613` |
| `kanal.yaml` | `horeca.kanal_yatirim_destegi_var_mi` | true | bool | FACT | `EV-2026-08-10-615` |
| `kanal.yaml` | `horeca.sarap_alim_sozlesmesi_suresi_yil` | 5 | yıl | FACT | `EV-2026-08-10-614` |
| `kanal.yaml` | `kanal_gucu_riski.alici_gucu_esigi_pct` | 22 | % | FACT | `EV-2026-08-10-609` |
| `kanal.yaml` | `kendi_dagitimimiz.personel_taban_maliyeti_aylik` | 40.214,03 | TRY/ay/kişi | FACT | `EV-2026-08-10-621` |
| `kanal.yaml` | `kendi_dagitimimiz.3pl_yasal_olarak_mumkun_mu` | true | bool | FACT (mevzuat ajanı) | `EV-2026-08-09-204` |
| `kanal.yaml` | `tekel_bayi.ulusal_dagitim_yukumlulugu` | "nitelendi" | — | FACT (mevzuat ajanı) | `EV-2026-08-10-212` |

**Duyarlılık bantları** (`ASSUMPTION`, `modele_girme_kurali: SENSITIVITY_ONLY`):

| Alan | LOW | BASE | HIGH | STRESS |
|---|---|---|---|---|
| `m_retail_zincir_pct` (margin, KDV hariç, L7→L8) | 18 | **25** | 35 | — |
| `m_tekel_pct` (margin, KDV hariç, L7→L8) | 12 | **18** | 25 | — |
| `k_horeca_carpan` (L7 üzerine) | 2,0× | **3,0×** | 5,0× | — |
| `d` geri akan bedeller (% fatura cirosu) | 3 | **8** | 18 | — |
| `f` listeleme (TL/şişe) | **UNKNOWN** — yalnızca yapısal senaryo | | | |
| vade — zincir (gün) | 45 | **60** | 90 | **120** |
| vade — tekel (gün) | 0 | **30** | 60 | 90 |
| vade — HoReCa (gün) | 15 | **45** | 90 | 120 |

**evidence_id'si olmayan hiçbir satır `value` alanına yazılmamıştır.**

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `turkiye-pazar-kasifi` | **KM-1**: 2020'de iç piyasa şarap arzının **%96'sı üretim, %4'ü ithalat** (TADB, `EV-2026-08-10-624`) | `pazar.yaml → ithal_pay_pct` TUR 1'in en büyük UNKNOWN'ıydı; bu bir T2 aday kaynaktır. **Ben doldurmadım.** |
| `turkiye-pazar-kasifi` | **KM-2**: Alkol satan nokta sayısı GK 48.956 / ASN 29.218 (2020, TADB); **modern kanal yok** | Pazar haritasının kanal boyutu |
| `turkiye-pazar-kasifi` | **KM-3**: Metro alkolde **yıllık anlaşma** imzalıyor → tek "raf fiyatı" kanal fiyatı değildir | `İP-501`/`İP-505`'i güçlendirir; `T-506`'ya kanal cevabı |
| `finans-fizibilite` | **KM-4**: Migros ticari borçlarını **yıllık %38,6** ile iskonto ediyor (`EV-617`) | `makro.yaml → finansman_orani` için denetlenmiş çapa. **Ben doldurmadım.** |
| `finans-fizibilite` | **KM-5**: Listeleme bedeli sabit, hacim değişken → 5.000 vs 100.000 şişede **20 kat** fark | Üç ajan (kanal, sourcing `İP 6.3`, navlun `F-1`) **bağımsız olarak** küçük hacmin orantısız pahalı olduğunu buldu |
| `finans-fizibilite` | **KM-6**: Dağıtım modeli, kanal karmasının **türevidir** | Modelde bağımsız karar değişkeni gibi durmamalı |
| `gumruk-vergi-uzmani` | **KM-7**: Üretici pazarlama katkısı **fatura** ile mi **iskonto** ile mi veriliyor — gümrük kıymetini değiştirebilir | `T-605`'te RFQ'ya sorulması sağlandı; **vergisel sonuç sizindir** |
| `gumruk-vergi-uzmani` | **KM-8**: **Kırık ürün bedeli** + indirilemeyen KDV (`Cİ-15.1`) birleşiyor | Fire maliyetinin üçüncü kalemi kanal tarafında doğrulandı |
| `mevzuat-ruhsat-uzmani` | **KM-9**: `K3` (promosyon yasağı) + Yönetmelik m.5/2(d) → şarapta bedelin karşılığı yalnızca fiziksel konumlandırma | Kanal maliyet yapısının yapısal sonucu |
| `mevzuat-ruhsat-uzmani` | **KM-10**: 2015'teki "sözleşme süresince rafta satışa sunulma zorunluluğu" 2024 metninde **görünmüyor** | `T-601` üçüncü sorusu |
| `seytanin-avukati` | **KM-11**: Kendi işime karşı 7 maddelik cephane | §9'da da tekrarlandı |
| `yatirim-komitesi-baskani` | **KM-12/13**: index birleştirme notu + `T-205` kullanım kaydı | Bakım |

`99-ops/_parts/capraz-ipuclari-kanal-marj-uzmani-tur2.md`'ye yazıldı.
**Ana `capraz-ipuclari.md` dosyasına dokunulmadı.**

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|---|---|---|---|---|
| `T-601` | `mevzuat-ruhsat-uzmani` | Şarap 6585 m.7/3 anlamında "tarım ve gıda ürünü" mü? (+ TTK 1530 metni, + 2015 raf garantisi 2024'te var mı, + T1 doğrulaması) | **CRITICAL** | OPEN |
| `T-602` | `finans-fizibilite` | `kanal.yaml` senaryo olarak çalıştırılmalı; L6/L7 bu turda çözülemez → model `UNKNOWN` dönmeli | HIGH | OPEN |
| `T-603` | `turkiye-pazar-kasifi` | `L8_CHAIN_RETAIL` + kanal ciro dağılımı olmadan merdiven kapanmıyor | HIGH | OPEN |
| `T-604` | `yatirim-komitesi-baskani` | 12 alan yalnızca gerçek kanal görüşmesiyle kapanır — TUR 7 kapsam/yetki talebi | HIGH | OPEN |
| `T-605` | `global-sourcing-kasifi` | RFQ 5.6/5.7 ile listeleme bedeli çift sayım riski + markup/margin format zorunluluğu | MEDIUM | OPEN |

**Bana açılmış ticket:**

| ticket_id | Durum | Ne yapıldı |
|---|---|---|
| `T-205` | `RESOLVED` / `ACCEPTED_BUSINESS_CONSTRAINT` — **statüsü değiştirilmedi** | Kısıt bir **girdi** olarak 8 ayrı yerde kullanıldı; kullanım kaydı `T-205.md` sonuna eklendi. Kapsam **yeniden araştırılmadı**. |
| `T-506` | Bana yönelikti | Kanal tarafından kısmen cevaplandı: ciro primi mekaniği alkolde **vardır** (`EV-612`); Metro'nun alkolü çek/sadakat kampanyalarından hariç tutması **tüketici** mekaniğidir, tedarikçiden alınan ticari bedellerle aynı şey değildir. Metro mağaza/sevkiyat **fark büyüklüğü** hâlâ UNKNOWN (`OQ-612`). Statüsünü **değiştirmedim** (başkanın işi). |

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-10-601` … `-607` (mevzuat) | 180d | 2027-02-06 |
| `EV-2026-08-10-608` (TBMM, orijinal metin) | 180d | 2027-02-06 (zaten `SUPERSEDED`) |
| `EV-2026-08-10-609` … `-615`, `-624` (Rekabet Kurumu) | 1y | 2027-08-10 |
| `EV-2026-08-10-616`, `-617` (Migros finansalları) | 1y | 2027-08-10 |
| `EV-2026-08-10-621` (asgari ücret) | 1y | 2027-08-10 — **fiilen 2026-12-31'de eskir** |
| `EV-2026-08-10-622` (erişim günlüğü) | 30d | 2026-09-09 |
| `EV-2026-08-10-618`, `-619`, `-620`, `-623` (T5) | **0d** | **ZATEN STALE** — modele giremez |

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Gerçek bir zincir yıllık anlaşması.** Tek bir imzalı sözleşme, bu raporun
UNKNOWN bıraktığı 8 alanı (listeleme bedeli, ciro primi oranı, alan kullanımı,
kırık ürün bedeli, lojistik bedeli, vade, iade oranı, minimum sipariş) **aynı anda**
kapatır ve bu raporun duyarlılık bantlarının çoğunu **anlamsız** hâle getirir.

İkincil olarak: **`T-601` "şarap tarım ve gıda ürünü değildir" cevabı verirse**,
60 günlük yasal tavan düşer, `C-601` "kanun uygulanmıyor" değil "kanun kapsamıyor"
olarak çözülür ve vade base case'i 60'tan 90'a kayar → `peak_cash_requirement`
**%50 artar**.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**`d` bandı (%3 / %8 / %18).** Tek dayanağı `EV-2026-08-10-612`'deki **kalem
sayısıdır** — yani "en az 6 kalem var, öyleyse toplamları anlamlıdır" akıl
yürütmesi. Bu **bir seviye kanıtı değildir.** Gerçek `d` %2 de olabilir %25 de.
`d`'nin %18 yerine %25 olması, aynı hedef `L8`'de `L6`'yı **%9 aşağı** çeker ve
tedarikçiye ödeyebileceğimiz maksimum fiyatı doğrudan düşürür.

İkinci en kırılgan: **`m_retail` BASE = %25 seçimi.** Savunulabilir ama keyfî.
Tek çapa Migros'un tüm-kategori %24,31'i ve o da şarap değil.

### 9.3 Hangi kaynağıma en az güveniyorum?

**`EV-2026-08-10-618`** (HoReCa çarpanı, Milliyet/Murat Bozok, **2012**).
T5, 14 yıllık, ve **kendi içinde tutarsız** — çarpanı bir yerde perakende fiyatının
2 katı, başka yerde toptan fiyatının 2,5 katı, üçüncü bir yerde market fiyatının
4–5 katı olarak verir. Bunlar **üç farklı katmandır**. Bu kartı yalnızca bir bant
üretmek için kullandım ve `ttl: 0d` verdim.

Yakın ikinci: **`EV-2026-08-10-623`** (TTK m.1530). Tam metni birincil kaynaktan
**doğrulayamadım** (mevzuat.gov.tr erişilemedi) ve CLAUDE.md §2 gereği mevzuat
sonucu için T5 tek başına kullanılamaz. Kartı `UNKNOWN` statüsünde bıraktım.

**Ayrıca dürüstlük kaydı:** `EV-601`…`-607`'nin içeriği T1 kanun/yönetmelik metnidir
ama **erişim T3 ticari veri tabanı üzerindendir**. Tier'ı T1 değil **T3** verdim ve
`T-601` ile doğrulama istedim. Metnin yanlış olduğunu düşünmüyorum; tier'ın hak
edilmemiş olduğunu düşünüyorum.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlış çıkan | Değişen karar |
|---|---|
| **Listeleme bedeli tahmininin 3x çıkması** | Düşük hacim senaryoları (5.000 / 10.000 şişe) **tek başına ölür**. Bedel şişe başına maliyetin sabit parçasıdır; 3x, pilot ekonomisini `KILL`'e taşır. 50.000+ şişede etki seyrelir. Yani **pilot ile ölçek kararı ayrışır**: "TEST" kararı verilemez, doğrudan "IMPORT PILOT (büyük)" veya "KILL" olur. |
| **Zincir vadesinin 120 güne çıkması** | `peak_cash_requirement` alacak tarafında **yaklaşık ikiye katlanır**. `maximum_total_capital_try` eşiği (`TBD`) aşılırsa senaryo **uygulanamaz** hâle gelir — marj pozitif olsa bile. Bu, "kârlı ama finanse edilemez" tipik tuzağıdır ve `C-601` bunu **açık** bırakmaktadır. |
| **Dış distribütör marjının beklenenden 10 puan yüksek olması** | `L6` sabitken `L5` marjı 10 puan daralır. Ölen senaryolar: **düşük hacim + dış distribütör** kombinasyonunun tamamı (çünkü orada zaten kendi dağıtım imkânsız — B-9). Ayakta kalanlar: yüksek hacim + kendi dağıtım. Yani yüksek distribütör marjı, projeyi **büyük ölçekli ve sermaye yoğun** olmaya zorlar; "küçük başlayıp büyüyelim" yolu kapanır. |
| **`m_retail` gerçekte %35 çıkması** | Aynı hedef `L8`'de `L6` **%13 düşer** → tedarikçiye ödeyebileceğimiz maksimum EXW/FOB düşer → `global-sourcing-kasifi`'nin aday havuzu daralır (`İP 6.3` ile birleşince MOQ kısıtı daha da bağlayıcı olur). |
| **`OQ-607`: noktaların çoğu 5 yıllık sözleşmeyle bağlıysa** | Bu, marjdan **daha ölümcüldür**: kanal erişimi yoksa marj hesabının konusu kalmaz. GK ve HoReCa kanalları fiilen kapanır, geriye yalnızca zincir kalır ve zincirde de `İP-2001` gereği raf dışında kaldıraç yoktur. |

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| Ne | Kim | Nasıl | Süre |
|---|---|---|---|
| Zincir yıllık anlaşma koşulları | Kurucu / ticari direktör | 2–3 zincir kategori yöneticisiyle **yüz yüze** görüşme; taslak sözleşme talebi | 4–8 hafta (kategori planlama takvimine bağlı) |
| Dış distribütör marjı | Kurucu | 2–3 distribütör görüşmesi; **margin mi markup mı** açıkça sorulacak | 2–4 hafta |
| `L8_CHAIN_RETAIL` | `turkiye-pazar-kasifi` | Fiziksel mağaza turu, ≥2 şehir, ≥20 SKU, etiket fotoğrafı + KDV ibaresi | 1–2 hafta |
| HoReCa çarpanı | `turkiye-pazar-kasifi` veya kurucu | 15–20 restoran şarap listesi örneklemi (fiziksel/PDF menü) | 1–2 hafta |
| Tekel bayii marjı | Kurucu | 3–5 bayi görüşmesi + varsa toptancı fiyat listesi | 2–3 hafta |
| Şarabın hukuki nitelemesi (`T-601`) | `mevzuat-ruhsat-uzmani` | T1 kaynaktan 6585 + Yönetmelik + TTK 1530; gerekirse Ticaret Bakanlığı görüşü | 1 tur |
| Kendi dağıtım maliyetleri | Kurucu + 3PL | Şirket bordro/kira verisi + 2–3 3PL teklifi | 2–4 hafta |

**Toplam:** Bu raporun UNKNOWN'larının kapanması için gereken süre **6–10 hafta** ve
**gerçek ticari temas** gerektirir. Masabaşı araştırmayla kapanmaz — ve bu turda
kapanmış gibi **gösterilmemiştir**.
