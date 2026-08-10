# ÇAPRAZ İPUÇLARI

> **KURAL (CLAUDE.md §1.10–1.11):**
> Her ajan **yalnızca kendi görev alanında sonuç üretir.**
> Alan dışı bulgular **silinmez** — buraya bırakılır.
>
> Buraya yazılan şey **SONUÇ DEĞİLDİR, İPUCUDUR.**
> Hedef ajan bunu bir veri olarak değil, bir **araştırma yönlendirmesi**
> olarak kullanır ve kendi kaynaklarıyla doğrular.
>
> Buradaki bir ipucu **modele giremez.** Modele girmek için hedef ajan
> tarafından doğrulanıp kendi alanında kanıt kartına bağlanması gerekir.

---

## DURUM — TUR 1 SONU: 5 AJANDAN ÇAPRAZ İPUCU GELDİ

TUR 1'de beş ajan da alan dışı bulgularını bırakmıştır. İpuçları ajanların
kendi numaralandırmasıyla (`Cİ-`, `İP-`, bölüm numarası) korunmuştur —
başkan tarafından yeniden numaralandırılmamıştır, çünkü ajan raporları
bu numaralara atıf yapmaktadır.

| Bırakan ajan | Hedef ajanlar |
|---|---|
| `gumruk-vergi-uzmani` | `global-sourcing-kasifi`, `navlun-lojistik-uzmani`, `mevzuat-ruhsat-uzmani`, `turkiye-pazar-kasifi` |
| `mevzuat-ruhsat-uzmani` | `gumruk-vergi-uzmani`, `navlun-lojistik-uzmani`, `kanal-marj-uzmani`, `global-sourcing-kasifi`, `turkiye-pazar-kasifi`, `finans-fizibilite` |
| `navlun-lojistik-uzmani` | `mevzuat-ruhsat-uzmani`, `gumruk-vergi-uzmani`, `global-sourcing-kasifi`, `finans-fizibilite`, `kanal-marj-uzmani`, `turkiye-pazar-kasifi` |
| `global-sourcing-kasifi` | `gumruk-vergi-uzmani`, `navlun-lojistik-uzmani`, `mevzuat-ruhsat-uzmani`, `turkiye-pazar-kasifi`, `kanal-marj-uzmani`, `finans-fizibilite` |
| `turkiye-pazar-kasifi` | `kanal-marj-uzmani`, `mevzuat-ruhsat-uzmani`, `global-sourcing-kasifi` |

> **Hatırlatma:** Buradaki hiçbir satır modele giremez. Hedef ajan kendi
> alanında doğrulayıp kendi kanıt kartına bağlamadan ipucu veri değildir.

---

## KAYIT FORMATI

```yaml
ipucu_id:        IP-###
tarih:           YYYY-MM-DD
birakan_ajan:
hedef_ajan:
konu:
ipucu:           # Ne gordun (SONUC DEGIL)
nerede_gordun:   # URL / kaynak / baglam
neden_onemli:    # Hedef ajan icin neden anlamli
durum:           # NEW | SEEN | INVESTIGATED | DISMISSED
hedef_ajan_notu: # Hedef ajan inceledikten sonra doldurur
```

---

## ÖNCEDEN AÇILMIŞ İPUÇLARI (TUR 0 — KURULUM)

Bunlar araştırma bulgusu değil, **kurulum sırasında öngörülen** çapraz
bağımlılıklardır. Ajanlar TUR 1'e başlarken bunları bilerek başlasın.

```yaml
ipucu_id:        IP-001
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      gumruk-vergi-uzmani
konu:            Odeme sekli -> KKDF
ipucu: >
  tedarikci.yaml/odeme.odeme_sekli alani global-sourcing-kasifi tarafindan
  doldurulacak. Vadeli odeme / akreditif KKDF dogurabilir.
neden_onemli:    KKDF matrahi ve dogus kosulu odeme seklinden bagimsiz degildir.
durum:           NEW
```

```yaml
ipucu_id:        IP-002
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      gumruk-vergi-uzmani
konu:            Mense ispat belgesi -> tercihli tarife
ipucu: >
  tedarikci.yaml/belgeler.mense_ispat_belgesi alani global-sourcing-kasifi
  tarafindan doldurulacak (EUR.1 / fatura beyani / REX / yok).
neden_onemli: >
  Tedarikci belge veremiyorsa tercihli tarife kullanilamaz ve ulke secimi
  ekonomisi degisir.
durum:           NEW
```

```yaml
ipucu_id:        IP-003
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      navlun-lojistik-uzmani
konu:            Koli/palet olculeri -> konteyner hesabi
ipucu: >
  urun.yaml/ambalaj ve tedarikci teklifleri koli/palet olcu ve agirliklarini
  icerecek. Konteyner kapasitesi bu verilerden hesaplanir.
neden_onemli: >
  Sarapta genellikle AGIRLIK kisiti hacim kisitindan once baglayici olur —
  ama bu VARSAYILMAZ, hesaplanir.
durum:           NEW
```

```yaml
ipucu_id:        IP-004
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      navlun-lojistik-uzmani
konu:            Ruhsat/analiz gecikmesi -> demurrage
ipucu: >
  mevzuat-ruhsat-uzmani'nin T0 takvimi ve analiz sureleri, konteynerin
  limanda/antrepoda bekleme suresini belirler.
neden_onemli:    Free time asilirsa demurrage/detention maliyeti dogar.
durum:           NEW
```

```yaml
ipucu_id:        IP-005
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      finans-fizibilite
konu:            Antrepo kismi cekis -> peak cash
ipucu: >
  vergi.yaml/antrepo_rejimi.kismi_cekis_mumkun_mu alani gumruk-vergi-uzmani
  tarafindan doldurulacak.
neden_onemli: >
  Kismi cekis mumkunse vergiler parti parti odenir ve peak_cash_requirement
  DRAMATIK olcude duser. Bu tek alan pilot fizibilitesini degistirebilir.
durum:           NEW
```

```yaml
ipucu_id:        IP-006
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      kanal-marj-uzmani
konu:            Reklam yasagi -> marka insa maliyeti
ipucu: >
  ruhsat.yaml/satis_dagitim_reklam_kisitlari alanlari mevzuat-ruhsat-uzmani
  tarafindan doldurulacak.
neden_onemli: >
  Reklam yapilamiyorsa marka bilinirligi yalnizca raf ve kanal uzerinden
  kurulur. Bu, listeleme/gondol/kampanya maliyetlerini ve private label
  modelinin makuliyetini dogrudan etkiler.
durum:           NEW
```

```yaml
ipucu_id:        IP-007
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      gumruk-vergi-uzmani, mevzuat-ruhsat-uzmani, navlun-lojistik-uzmani
konu:            Bulk sarap hipotezi
ipucu: >
  50-sourcing/ulke-karsilastirma.md §4'te bir ARASTIRMA HIPOTEZI kayitli:
  dokme sarap ithal edip Turkiye'de siselemek.
neden_onemli: >
  Bu hipotez 00-charter/kapsam.md uyarinca KAPSAM DISIDIR ve BU PROJEDE
  COZULMEZ. Yalnizca ilerideki bir calisma icin isaretlenmistir.
  Ajanlar bu konuda arastirma YAPMAZ; yalnizca yolda tesadufen bir bilgi
  gorurlerse buraya not birakirlar.
durum:           NEW
```

```yaml
ipucu_id:        IP-008
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      turkiye-pazar-kasifi
konu:            Etiket zorunluluklari -> raf gozleminde ipucu
ipucu: >
  Turkce arka etiketlerde ithalatci firma adi zorunlu olabilir.
neden_onemli: >
  Raf gozleminde etiket fotografi cekilirken ARKA etiket de cekilirse,
  hangi ithalatcinin hangi markayi getirdigi dogrudan tespit edilebilir.
  Bu, "mevcut ithalatci/distributorler" gorevini kanitli hale getirir.
durum:           NEW
```

---

# TUR 1 ÇAPRAZ İPUÇLARI (ajan fragment'lerinden birleştirildi)

> Aşağıdaki bölümler ajanların `99-ops/_parts/capraz-ipuclari-*.md` dosyalarından
> **değiştirilmeden** aktarılmıştır. Başlık seviyeleri bir kademe indirilmiştir.

## gumruk-vergi-uzmani

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında gördüğüm ama
> ilgili ajanı ilgilendiren bulgular. Hedef ajan doğrulamadan modele girmez.

---

### → `global-sourcing-kasifi`

#### Cİ-1 — Menşe seçimi gümrük vergisinde 70 puanlık bir kaldıraç barındırıyor
2204.21 (750 ml köpüksüz şarap) gümrük vergisi oranları (EV-2026-08-09-103…106):

| Menşe | Gümrük vergisi |
|-------|----------------|
| **Bosna-Hersek** | **%0** |
| **Kosova** | **%0** |
| Güney Kore, Singapur | %0 |
| Kuzey Makedonya | %35 |
| Venezuela | %35 |
| BAE | %49 |
| AB (İspanya/İtalya/Fransa/Portekiz), Birleşik Krallık, **Şili** | %50 |
| Gürcistan, Malezya, TPS-OIC, D-8 | %70 |
| **ABD, Güney Afrika, Avustralya, Arjantin** (DÜ) | **%70** |

**Neden önemli:** Kapsam listesindeki 9 ülkenin hiçbiri %0 grubunda değil.
Buna karşılık **Bosna-Hersek, Kosova ve Kuzey Makedonya** üzüm/şarap üreten
ülkeler ve Türkiye'ye coğrafi olarak yakın. Bunlar sourcing kapsamında hiç
yoktu. Fiyat/performans segmentinde %70 → %0 gümrük vergisi farkı, navlun
avantajıyla birlikte, kapsam genişletmeyi haklı çıkarabilir.

**Not:** Şili'nin STA'sı şarapta sıfır getirmiyor, sadece %70 → %50 indiriyor
(dipnot 2). Şili'yi "STA var, vergi düşük" varsayımıyla öne almayın.

#### Cİ-2 — İsviçre/Lihtenştayn kontenjanı var ama pratik değeri düşük
2204.21 için yılda **30.000 litre** (≈40.000 şişe) tarife kontenjanı,
kontenjan içi vergi %35 (EV-2026-08-09-109). Tüm ithalatçılar için toplam
miktardır ve İsviçre şarabı fiyat/performans segmentinde değildir.
Yine de "kontenjan var mı" sorusunun cevabı olarak kayda geçirildi.

#### Cİ-3 — Köpüklü şarap ürün genişletmesi vergiden ölür
2204.10 köpüklü şarapta ÖTV **481,5146 TL/litre** = 750 ml'de **361,14 TL/şişe**
(EV-2026-08-09-110). Köpüksüzde bu 53,45 TL. Portföye köpüklü SKU eklenmesi
düşünülüyorsa bu tek başına eleyici olabilir.

---

### → `navlun-lojistik-uzmani`

#### Cİ-4 — Navlun ve sigorta gümrük kıymetine giriyor, yani vergilendiriliyor
Gümrük Kanunu md.27/1-e: Türkiye'deki giriş liman/yerine kadar navlun + sigorta
+ yükleme/elleçleme gümrük kıymetine **dahildir** (EV-2026-08-09-120).
Sonuç: navlunun her 1 TL'si DÜ menşede **~1 TL × (1+0,70) × 1,20 = 2,04 TL**
landed maliyet yaratıyor (gümrük vergisi + KDV kaskadı). Yani **navlun optimizasyonunun
vergi çarpanı vardır.** LCL/FCL kararında bu çarpan hesaba katılmalı.

#### Cİ-5 — Giriş yerinden sonraki nakliye/sigorta kıymete girmiyor, ama ayırt edilebilir olmalı
GK md.28/a: giriş yerine varıştan sonraki nakliye ve sigorta hariç — **fiyattan
ayırt edilebilmesi koşuluyla** (EV-2026-08-09-121). Faturada tek kalem
"door-to-door" fiyat verilirse tamamı gümrük kıymetine girer ve vergilenir.
Forwarder'dan **liman-sonrası masrafların ayrı fatura/ayrı satır** olarak
alınması ciddi bir tasarruf kalemidir.

#### Cİ-6 — Antrepoda bekletmenin gizli vergi riski
Vergi, serbest dolaşıma giriş beyannamesinin tescil tarihinde doğar
(EV-2026-08-09-122) ve ÖTV maktu tutarı **Ocak ve Temmuz'da otomatik artar**
(EV-2026-08-09-114, son artış +%16,09). Antrepoda 1 Temmuz'u geçirmek şişe başı
ÖTV'yi ~%16 artırabilir. Antrepo nakit akışı avantajı hesaplanırken bu risk
karşı kaleme yazılmalı.

---

### → `mevzuat-ruhsat-uzmani`

#### Cİ-7 — Ürün Güvenliği ve Denetimi tebliği radarda
Mevzuat aramasında "**TÜTÜN, TÜTÜN MAMULLERİ, ALKOL VE ALKOLLÜ İÇKİLERİN
İTHALAT DENETİMİ TEBLİĞİ (ÜRÜN GÜVENLİĞİ VE DENETİMİ: 2026/…)**", RG 31.12.2025,
22.04'ü kapsayacak şekilde çıktı. İthalatta gümrük öncesi uygunluk denetimi
anlamına geliyor olabilir — takvim ve maliyet etkisi sizin alanınızda.

#### Cİ-8 — ÖTV bandrol usulü kanunda açıkça yetkilendirilmiş
ÖTV Kanunu md.14/5: Maliye Bakanlığı "(III) sayılı listedeki mallara ait
verginin **bandrol usulü ile tahsiline**" ilişkin usulleri belirlemeye yetkilidir.
Bandrol/ÜİS maliyeti ve süreci sizin alanınız; ancak bunun bir **vergi tahsil
yöntemi** olduğunu ve dolayısıyla ÖTV ödeme anını etkileyebileceğini not düşüyorum.

#### Cİ-9 — TAPDK/Tarım tebliğlerinde 2204.21 açıkça geçiyor
"ALKOL VE ALKOLLÜ İÇKİLERİN İÇ VE DIŞ TİCARETİNE İLİŞKİN USUL VE ESASLAR
HAKKINDA YÖNETMELİĞİN 14 ÜNCÜ … MADDESİ" tebliğlerinin her yılki versiyonunda
2204.21 GTİP'i geçiyor (2018–2025 serisi, her yıl aralık sonunda yenileniyor).
Bu yıllık yenilenen tebliğ serisi sizin takviminize girmeli.

---

### → `turkiye-pazar-kasifi`

#### Cİ-10 — Benchmark ürün en yüksek gümrük vergisi grubunda
Benchmark (Gold Country California Colombard-Chardonnay, **ABD menşeli**)
DÜ sütunundadır → gümrük vergisi **%70** (EV-2026-08-09-104). Yani 599,90 TL'lik
rafın arkasında ithalatçı en pahalı gümrük rejimini ödüyor. Bu, raf fiyatının
gerçekten agresif bir fiyat mı yoksa bir hata mı olduğunu değerlendirirken
önemli bir sinyal — rakip analizinde menşe kırılımı toplanmalı.

---

### → `kanal-marj-uzmani`

#### Cİ-11 — Vergi tabanı fiyat-esnek değil
ÖTV şişe başına sabit **53,4519 TL**'dir ve CIF'ten bağımsızdır
(EV-2026-08-09-111). Yani **indirim/kampanya yapıldığında ödenen ÖTV düşmez.**
Kampanya maliyeti tamamen marjdan karşılanır. Kanal kampanya ekonomisi
modellenirken bu, sabit maliyet gibi davranır.

---

### Genel not
Bu ipuçlarının hiçbiri benim alanımda **sonuç** değildir. Yalnızca vergi
verisinden düşen sinyallerdir. İlgili ajan kendi T1/T2 kanıtını kurmadan
modele girmemelidir.

---

## mevzuat-ruhsat-uzmani

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışındaki bulgular.
> İlgili ajan doğrulamadan modele girmez.

---

### → gumruk-vergi-uzmani

| # | İpucu | Neden önemli | Kaynak |
|---|-------|--------------|--------|
| G1 | Bandrol ithal alkollü içkiye **antrepoda**, yani serbest dolaşıma girişten önce uygulanıyor. Bandrol bedeli 2.360,73 TL/1.000 adet (%20 KDV hariç). | Bandrolün gümrük kıymetine girip girmediği ve KDV'sinin indirilebilirliği matrah sırasını etkiler. | `EV-2026-08-09-212`, `-213` · `T-203` |
| G2 | ÜİS Tebliği 3.3.1(b): **ÖTV (III) Sayılı Liste Uygulama Genel Tebliği** ile getirilen yükümlülükleri yerine getirmeyen firmaların **bandrol talepleri karşılanmaz**. | ÖTV uyumsuzluğu doğrudan operasyonu durdurur — bu bir vergi konusu değil, **operasyonel kilittir**. | `EV-2026-08-09-214` |
| G3 | Bandrol talebi için **Hazine ve Maliye Bakanlığına bağlı vergi dairelerine vadesi geçmiş borç bulunmaması** şart. | Nakit sıkışıklığında vergi gecikmesi → bandrol yok → ithalat durur. Finansal risk zinciri. | `EV-2026-08-09-214` |
| G4 | Ticaret Yön. m.13/7: alkollü içki faturalarında **GTİP, marka, ambalaj hacmi, alkol derecesi** bilgilerinin yer alması zorunlu. | GTİP tespitiyle beyan tutarlılığı; yanlış GTİP hem vergi hem mevzuat yaptırımı doğurur. | Ticaret Yön. m.13 |
| G5 | TADAB Portal'da alınan **Ürün ID numarası**, gümrük beyannamesinin **31. kutusunda** `ID:99847` formatında beyan edilmek zorunda. | Beyanname hazırlığında somut alan; eksikse gümrükleme takılır. | `EV-2026-08-09-215` |
| G6 | Tebliğ 2025/39'daki hizmet bedeli **satış** üzerinden (aylık satış raporu), ithalat üzerinden değil. | Bir "vergi" değil hizmet bedelidir; matrah sırasında L5'e ait, L4'e değil. | `EV-2026-08-09-209` |

---

### → navlun-lojistik-uzmani

| # | İpucu | Neden önemli | Kaynak |
|---|-------|--------------|--------|
| L1 | **Bandrol zorunlu olarak ANTREPODA, şişe şişe** uygulanır. Menşede uygulama alkollü içki için öngörülmemiştir. | Her konteyner için ek elleçleme adımı ve gün. → `T-204` | `EV-2026-08-09-212` |
| L2 | Depo, TADAB şartlarını taşımalı: **sadece bu işe ayrılmış veya diğer gıdadan tefrik edilmiş**, marka bazında sınıflandırma/sayım/etiket incelemesine imkân verecek düzende, **üzerinde Kurumun yetki belgesi**. | Standart 3PL rafı yeterli olmayabilir; depo seçimi kısıtlı. | `EV-2026-08-09-204` |
| L3 | Kendi deposu zorunlu **değil**: "amaca uygun dağıtım ağlarının **akde bağlanmış kullanıcısı**" olmak kabul ediliyor. | 3PL modeli yasal olarak açık → sermaye ihtiyacı düşer. | `EV-2026-08-09-204` |
| L4 | Satış Yön. m.7/1(b): **muhafaza edilen her depo için ayrı toptan satış belgesi** (82.464 TL/yıl). | Çok depolu ağ tasarımı belge maliyetini katlar. | `EV-2026-08-09-210`, `-211` |
| L5 | Nakil araçları "ürünü dış şartlardan koruyacak, kalite ve sevkiyat güvenliğini sağlayacak" teknik özelliklerde olmalı. | Sıcaklık kontrollü taşıma beklentisi doğurabilir. | `EV-2026-08-09-204` |
| L6 | Bandrol teslim noktaları: basım merkezi veya yetkili firmanın **İstanbul, Ankara, İzmir, Denizli, Mersin, Tekirdağ** ofisleri; ya da bedeli karşılığı güvenlikli kargo. | Antrepo lokasyonu seçimi bandrol lojistiğini etkiler. | `EV-2026-08-09-214` |
| L7 | Bandrol **fire**si hâlinde 10 gün içinde GİB ve Darphane'ye yazılı bildirim; fireler ayrıştırılarak muhafaza edilir. | Elleçleme sürecinde fire yönetimi prosedürü gerekir. | ÜİS Tebliği 3.5.4 |
| L8 | Sevk irsaliyeleri **en az 3 kopya**; alıcı onaylı kopya dağıtım firmasına iade edilir ve 2 yıl saklanır. | Evrak akışı operasyon maliyeti. | Ticaret Yön. m.13 |

---

### → kanal-marj-uzmani

| # | İpucu | Neden önemli | Kaynak |
|---|-------|--------------|--------|
| K1 | Ürünler **yalnızca alkollü içki satış belgesini haiz** kişilere satılabilir. | Kanal evreni belge sahipleriyle sınırlı. | `EV-2026-08-09-224` |
| K2 | İthalatçı, toptancıya belgesiz satabilir; **doğrudan perakendeciye/HoReCa'ya satış için toptan satış belgesi (82.464 TL/yıl)** gerekir. | Kanal mimarisi kararı (toptancı üzerinden mi, doğrudan mı) doğrudan belge maliyeti doğurur. | `EV-2026-08-09-210`, `-211` |
| K3 | **Promosyon, kampanya, hediye, eşantiyon, bedelsiz ürün TAM YASAK.** | Listeleme pazarlığında "bedava ürün / açılış kampanyası" araçları **kullanılamaz** — nakit indirim dışında kaldıraç yok. | `EV-2026-08-09-222` |
| K4 | **20/6/2026'dan itibaren** marka/logo/ambalaj görselleri iş yeri içinde-dışında-vitrinde-**satış ünitelerinde** bulundurulamaz (uyum 20/6/2027). | Gondol/stant/raf giydirme yatırımı anlamsızlaşabilir. → `T-205` | `EV-2026-08-09-223` |
| K5 | **22:00–06:00 perakende satış yasağı** ve "işletme dışından görülecek şekilde satışa arz" yasağı. | Kanal cirosu ve raf konumu üzerinde yapısal etki. | `EV-2026-08-09-222` |
| K6 | Satış Yön. m.16: üretici/ithalatçı/toptancı **münhasırlık ve bağlı satış (tying) uygulayamaz**; rekabeti kısıtlayıcı anlaşma yapamaz. | "Kategori münhasırlığı karşılığı listeleme" gibi modeller **yasal değil**. | Satış Yön. m.16 |
| K7 | 4250 m.1/3 + Ticaret Yön. m.9/2: ithalatçı **ülke genelinde her satıcının siparişini yerinde teslim** etmek zorunda. | Ulusal dağıtım yükümlülüğü → toptancı/dağıtıcı ağı zorunluluğu → marj. → `T-201` | `EV-2026-08-09-227` |
| K8 | TADAB, piyasaya arz edilen ürünleri **her ay güncellenen liste** hâlinde internet sayfasında yayımlar (Ticaret Yön. m.16). | Rakip SKU envanteri için **birincil, ücretsiz** veri kaynağı. | Ticaret Yön. m.16 |

---

### → global-sourcing-kasifi

| # | İpucu | Neden önemli | Kaynak |
|---|-------|--------------|--------|
| S1 | **Marka çakışması gate:** TÜRKPATENT'te 34 ve altı Nice sınıflarında başkası adına geçerli tescil varsa **ürün onayı VERİLMEZ**. | Private label marka adı seçimi ve mevcut marka distribütörlüğü için ön tarama zorunlu. | `EV-2026-08-09-218` |
| S2 | Marka kiralanacaksa **inhisari lisans sözleşmesi** şart; tescil edilen şekil/metin etikette **birebir** kullanılmalı. | Private label sözleşme yapısı. | `EV-2026-08-09-218` |
| S3 | Ürün onayı dosyasında **Türkçe üretim prosesi** isteniyor: hammadde teminden şişelemeye kadar **tüm aşamaların süreleri** dahil akış şeması. | Tedarikçiden alınması gereken teknik doküman — RFQ şablonuna eklenmeli. | `EV-2026-08-09-215` |
| S4 | Türkçe etiket **menşede** basılabiliyorsa (yasaklayıcı hüküm bulunamadı), üretici hattında ek iş demektir; ancak bandrol yine Türkiye'de antrepoda uygulanacaktır. | Menşe etiketleme MOQ ve birim fiyatı etkiler. | `EV-2026-08-09-212`, `-219` |
| S5 | Sağlık uyarısı 750 ml şişede **≥18 cm²** yer kaplar (3 grafik + 1 yazılı, ≥10 punto). | Etiket tasarım alanı ciddi biçimde daralır; arka etiket boyutu ve baskı maliyeti. | `EV-2026-08-09-220` |
| S6 | **5 cl altı ambalaj yasak.** 300 cl üstü yasağı ve **cam zorunluluğu** Danıştay kararıyla durdurulmuş ama **hüküm metinde duruyor**. | Bag-in-box/PET/alternatif ambalaj senaryoları regülasyon riski taşır. | `EV-2026-08-09-226` |
| S7 | Şarapta **vintage değişikliği yeni ürün onayı gerektirmez**; ancak alkol derecesi değişimi ayrı konudur. | Tedarikçiye ABV bandı taahhüdü (örn. %12–13) sözleşmeye konmalı; %9–15 bandında tek ID çalışması sürüyor. | `EV-2026-08-09-217` |
| S8 | Şarap etiketinde ABV karakter büyüklüğü **≥3 mm** (20–100 cl); ABV toleransı **±%0,5**. | Menşe etiketinin Türkiye kuralına uyumu; aksi hâlde ayrı Türkçe etiket zorunlu. | `EV-2026-08-09-221` |

---

### → turkiye-pazar-kasifi

| # | İpucu | Neden önemli | Kaynak |
|---|-------|--------------|--------|
| P1 | TADAB, bandrol/kod taşıyan ve piyasaya arz edilen ürünleri **aylık güncellenen liste** olarak yayımlar (Ticaret Yön. m.16). | Rakip SKU, marka ve ithalatçı envanteri için **T2 birincil kaynak**. | Ticaret Yön. m.16 |
| P2 | TADAB ayrıca **Yetkili Dağıtım Firmaları Listesi** yayımlar. | Mevcut şarap ithalatçılarının tam listesi = rekabet haritası. | Ticaret Yön. m.12 |
| P3 | Reklam tam yasak olduğu için pazar payı **raf/dağıtım genişliği** ile kazanılıyor olmalı. | Pazar araştırmasında "kaç satış noktasında bulunuyor" metriği reklamdan daha belirleyici. | `EV-2026-08-09-222` |

---

### → finans-fizibilite

| # | İpucu | Neden önemli | Kaynak |
|---|-------|--------------|--------|
| F1 | **Bandrol peşin ödenir** (Darphane hesabına), ürün henüz satılmamıştır. 100.000 şişe = 236.073 TL (KDV hariç) peşin çıkış. | `peak_cash_requirement` kalemi. | `EV-2026-08-09-214` |
| F2 | Dağıtım yetki belgesi bedelinin **1/4'ü başvuruda**, 3/4'ü belge verilirken tahsil edilir. | Nakit takvimi: belge alınamazsa 1/4 batmış maliyettir. | `EV-2026-08-09-203` |
| F3 | Tüm TADAB bedelleri **her yıl yeniden belirlenir** (Ticaret Yön. m.14, Satış Yön. m.15); bandrol fiyatı **Yİ-ÜFE**'ye endeksli. | 2027'ye sarkan ilk konteyner için bedeller bugünkünden yüksek olacaktır — duyarlılık analizine girmeli. | `EV-2026-08-09-213`, Ticaret Yön. m.14 |
| F4 | TADAB'da teminat hükmü **bulunamadı**; ancak bandrol peşin ödemesi benzer bir nakit kilitlenmesi yaratır. | `teminat` alanı UNKNOWN kalır ama nakit modeli bandrolü yakalamalıdır. | `EV-2026-08-09-229` |
| F5 | Faaliyet hacmi beyanı aşılırsa **aşan miktar için ek bedel** tahsil edilir (Ticaret Yön. m.12). | Hacim büyütme senaryosunda gizli maliyet. | Ticaret Yön. m.12 |

---

## navlun-lojistik-uzmani

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında rastladığım ama
> silmek istemediğim bulgular. İlgili ajan doğrulamadan hiçbiri kullanılamaz.

---

### → `mevzuat-ruhsat-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| M-1 | Bandrol/kodlu etiketin ya **yabancı üretim tesisinde** ya da Türkiye'de belirlenmiş **antrepolarda (İstanbul, İzmir, Mersin)** uygulandığı yönünde T5 bilgi bulundu (`EV-2026-08-09-380`). **Doğrulanmadı.** | Menşede bandrollenebiliyorsa antrepo bekleme süresi ve demurrage riski dramatik biçimde düşer. Lead time'ın en büyük belirsizliği burada. |
| M-2 | 2026 için "bandrol hizmet bedeli 1.000 adette 198,27 TL (baskı hariç)" şeklinde T5 bir haber görüldü (Bigpara/Hürriyet). **Ben bunu doğrulamadım ve kullanmadım** — bandrol ücreti senin alanın. | Şişe başı maliyete doğrudan girer. |
| M-3 | Alkollü içki ithalatında **iki ayrı beyanname** (antrepo + serbest dolaşıma giriş) gerekeceği varsayımıyla gümrük müşavirliği maliyeti hesapladım (`EV-2026-08-09-342`). Bu varsayımın mevzuat teyidi yok. | Yanlışsa müşavirlik maliyeti yarıya iner. |
| M-4 | Alkollü içki için **özel antrepo yetkisi / uygun depo şartı** olup olmadığını doğrulayamadım. Antrepo maliyeti bu şarta bağlı değişir. | Depo seçimi ve maliyeti. |
| M-5 | Terminal tarifelerinde IMO/tehlikeli yük konteynerine %20 surprim var (`EV-2026-08-09-340`). Şarap IMO sınıfına girmiyor olmalı (ABV düşük) ama yüksek alkollü ürünlerde girer. Şarap için teyit gerekli. | Yanlışsa terminal maliyetine +%20. |

---

### → `gumruk-vergi-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| G-1 | **Navlun ve sigorta gümrük kıymetine girer.** Ben sigorta primini %0,3–0,6 (CIF+%10 üzerinden) olarak ESTIMATE ettim (`EV-2026-08-09-360`) ve navlun bandını verdim — ama **gümrük kıymeti hesabı senin alanın, ben yapmadım.** Bkz. `T-303`. | Matrah tabanını doğrudan büyütür; ÖTV/KDV'ye kadar çarpan etkisi yapar. |
| G-2 | **Incoterm seçimi gümrük kıymetini değiştirir.** EXW alımda navlun+sigorta ithalatçının, CIF alımda satıcının faturasında olur. İkisinde de kıymete girer ama **belgelendirme ve ispat yükü farklıdır.** | Kıymet beyanı ve gözetim riski. |
| G-3 | 2026 Gümrük Müşavirliği Asgari Ücret Tarifesi'nde **ÖZ-4 kalemi (laboratuvar tahlili / ekspertiz / TSE-DTS işlemleri) 940 TL/işlem** olarak var (`EV-2026-08-09-342`). Alkollü içkide analiz zorunluysa bu kalem her partide çıkar. | Küçük ama unutulan kalem. |
| G-4 | Terminal tarifesinde **tam muayene** 20ft 2.322 TL / 40ft 3.249 TL (`EV-2026-08-09-341`). Alkollü içkide muayene/numune olasılığı yüksek — kırmızı hat oranı senin alanın. | Muayene olasılığı × maliyet = beklenen değer. |
| G-5 | **Antrepo rejiminin nakit akışı avantajı:** vergiler serbest dolaşıma girişte doğar, antrepoda beklerken doğmaz. Ürün antrepoda bandrollenirken vergi ödenmiyorsa `peak_cash_requirement` düşer. Bunu ben hesaplamadım. | Nakit akışı modelinin yapısını değiştirebilir. |

---

### → `global-sourcing-kasifi`

| # | İpucu | Neden önemli |
|---|---|---|
| S-1 | **Şişe/koli geometrisi konteyner kapasitesini %38'e kadar değiştiriyor.** Burgundy formu (geniş omuzlu) şişe, Bordeaux formuna göre şişe başı hacmi 0,00223 m³'ten 0,0036 m³'e çıkarıyor. RFQ'da **şişe formu, çapı, koli dış ölçüsü ve palet konfigürasyonu** mutlaka sorulmalı. Bkz. `T-302`. | Şişe başı navlunun tek en büyük belirleyicisi. |
| S-2 | **Hafif cam (300–420 g) sourcing kriteri olmalı.** Ağırlık 40HC'de bağlayıcı kısıt. Ağır cam (700 g) 40HC kapasitesini ~%15 düşürür. Fiyat/performans segmentinde hafif cam zaten yaygındır. | Hem navlun hem ambalaj maliyeti. |
| S-3 | **6'lı koli 12'liden hacimsel olarak ~%7 daha verimsiz.** AB tedarikçileri 6'lı, ABD tedarikçileri 12'li standardını kullanıyor (`EV-2026-08-09-308`). Private label'da koli formatı **müzakere edilebilir bir kalemdir**. | Konteyner başına şişe. |
| S-4 | **Akdeniz menşei lojistik olarak açık ara üstün:** transit 5–10 gün, haftalık sefer, düşük sıcaklık riski. California/Şili/G.Afrika 26–45 gün, seyrek sefer, yüksek sıcaklık riski. Benchmark ürünü California menşeili ama **lojistik olarak en kötü rota.** | Menşe seçiminde lojistik ağırlık taşımalı. |
| S-5 | **Incoterm sorusu:** EXW/FOB alırsak navlunu biz kontrol ederiz (rota, konsolidasyon, liner/reefer kararı bizde). CIF alırsak tedarikçinin forwarder'ına mahkûm oluruz ve **sigorta muhtemelen ICC (C) olur — ki kırılmayı kapsamaz.** Bkz. `T-305`. | Risk transferi ve maliyet kontrolü. |
| S-6 | Tedarikçiden **thermal liner / reefer** ile yükleme yapıp yapamayacağı, yaz aylarında yükleme politikası sorulmalı. | Bozulma riski. |

---

### → `finans-fizibilite`

| # | İpucu | Neden önemli |
|---|---|---|
| F-1 | **5.000 şişe/yıl senaryosu lojistik olarak verimsizdir.** LCL kırılma noktası ~5.000–7.000 şişe/sevkiyat. 5.000 şişe/yıl LCL demektir; LCL'de birim maliyet yüksek, kırılma riski fazla, varış sabit masrafları (200–500 USD) hacimden bağımsızdır. Ölçek eğrisi bu noktada **doğrusal değildir.** | Ölçek senaryolarının karşılaştırması. |
| F-2 | **Ruhsat/bandrol gecikmesi limanda yaşanırsa 20DV başına 60 günde ~8.000 USD** (`EV-2026-08-09-344`). Antrepoya çekilirse ~210 EUR. **Fark ~30 kat.** Modelde hangi senaryonun varsayıldığı açıkça yazılmalı. | Pilot maliyetini tek başına ikiye katlayabilir. |
| F-3 | **Toplam lead time UNKNOWN'dır.** Yalnız transit süresini (7–10 gün) lead time sanmak modeli sistematik olarak iyimser yapar. CCC ve `peak_cash_requirement` doğrudan etkilenir. | İşletme sermayesi. |
| F-4 | **2 × 20DV, 1 × 40HC'den %24–27 daha fazla şişe taşır** (ağırlık limiti araç başına). Ama konteyner başı sabit masraflar (THC 113 USD, müşavirlik ek konteyner 1.350 TL, iç nakliye, ardiye) az konteyner lehinedir. Bu bir **optimizasyon problemi**, sabit bir cevap yok. | Şişe başı lojistik maliyeti. |
| F-5 | Tüm navlun rakamları **spot**tur ve `ttl: 14d`'dir. Model bir navlun rakamına kilitlenirse 2026-08-23'ten sonra geçersizdir. Navlun **duyarlılık değişkeni** olarak modellenmelidir (ör. ±%100). | Model geçerliliği. |

---

### → `kanal-marj-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| K-1 | Depodan kanala dağıtım maliyetini (şişe başı) hesaplayamadım — **UNKNOWN**. Ama alkollü içkide dağıtımın **yetki belgeli depo/araç** gerektirip gerektirmediği kanal maliyetini değiştirir. | Dağıtım modeli seçimi (kendi filo vs 3PL). |
| K-2 | Sevkiyat sıklığı düşükse (yılda 1–2 konteyner) **stok tek seferde gelir** → depoda uzun süre bekler → kanala parça parça dağıtılır. Bu, kanal vadesiyle birleşince nakit döngüsünü uzatır. | Vade ve stok politikası. |

---

### → `turkiye-pazar-kasifi`

| # | İpucu | Neden önemli |
|---|---|---|
| P-1 | Rafta gördüğün ithal şarapların **koli formatı (6'lı/12'li)** ve **cam ağırlığı** (şişeyi eline al) gözlemlenebilir. Bu, rakiplerin lojistik maliyet yapısı hakkında ipucu verir. | Rakip maliyet yapısı. |
| P-2 | Benchmark ürünü (Gold Country) **California menşeili** — yani en pahalı ve en riskli lojistik rotadan geliyor. Buna rağmen 599,90 TL'de raftaysa, ya çok ucuz alınıyor ya çok büyük hacimde geliyor. **Bu bir sinyal.** | Rakibin ölçeği hakkında ipucu. |

---

## global-sourcing-kasifi

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında gördüğüm ve başka
> ajanları ilgilendiren bulgular. Hiçbiri karar veya hesap değildir.

---

### 1. `gumruk-vergi-uzmani` için

#### 1.1 — GTİP kırılımı gerçekten kullanılıyor
Türkiye'nin şarap ithalatı fiilen tek bir kalemde toplanıyor: **2204.21** (≤2 litre kap).
2025'te 17.848.518 litre. Diğer kırılımlar pratikte boş: 2204.22 → 1.100 litre,
2204.29 → 628 litre. `EV-2026-08-09-405`, `EV-2026-08-09-407`
→ GTİP çalışmasının ağırlığı 2204.21'de olmalı; alt kırılım (2204.21.xx.xx.xx)
şeker/ABV/hacim eşiklerine göre ayrışıyorsa oradaki ayrım kritik olabilir.

#### 1.2 — ABV eşiği ipucu
Aday üreticilerden hiçbiri ABV'sini web sitesinde yayınlamıyor. RFQ 1.4 bunu
zorunlu alan yaptı. Eğer Türkiye'de ÖTV veya GTİP alt kırılımı bir ABV eşiğine
bağlıysa (örn. %13 vol), bu **tedarikçi seçimini doğrudan değiştirir** — çünkü
harman ABV'si private label'da ayarlanabilir bir parametredir.
→ Eşik varsa bana bildirin; RFQ'ya hedef ABV bandı olarak yazarım.

#### 1.3 — Menşe ispat belgesi çeşitliliği
Aday ülkeler üç farklı hukuki gruba dağılıyor: AB üyeleri (ES/IT/FR/PT/BG),
AB dışı Avrupa (MD/GE), ve okyanus ötesi (CL/ZA/AU/AR/US). Her grup farklı bir
belge tipi gerektirebilir (EUR.1 / fatura beyanı / REX / A.TR). RFQ 6.1 üreticiden
**belge adını** istiyor, "evet" cevabını kabul etmiyor. → T-401

#### 1.4 — Ödeme şekli seçimi vergiye bağlı
Tedarikçi vadesi hem işletme sermayesini iyileştirir hem (muhtemelen) KKDF doğurur.
Hangi yönün bastığını bilmeden RFQ 3.8–3.10'da ne isteyeceğimizi bilemiyoruz. → T-404

---

### 2. `navlun-lojistik-uzmani` için

#### 2.1 — Konteyner doluluk, MOQ tanımının parçası
Bir üretici MOQ'yu **konteyner bazında** tanımlıyor: "1 × 20ft mixed container with
2 different wines" (`EV-2026-08-09-409`). Bu MOQ'nun pilot hacmiyle uyumlu olup
olmadığını **ancak konteynerin kaç şişe aldığını bilirsek** söyleyebiliriz. → T-402

#### 2.2 — Sezgiye aykırı bulgu: ucuz olan yakın
Türkiye'ye en düşük CIF birim değerinden mal gönderen menşeler aynı zamanda
**en yakın** olanlar: Moldova (2,46 USD/l), Gürcistan (2,57 USD/l) — ikisi de
karayolu erişimli. Beklenen "ucuz ama uzak" ödünleşimi gözlenmedi.
Bu ya gerçek bir yapısal avantajdır ya da veride bir yorum hatası vardır.
`EV-2026-08-09-405` → T-402

#### 2.3 — Sıcaklık riski, menşe seçimini kısıtlayabilir
Güney yarımküre menşeleri (CL/ZA/AU/AR) yaz aylarında Kızıldeniz/Süveyş veya
Ümit Burnu geçişinde uzun sıcak maruziyeti anlamına gelir. Bir üretici (SUP-403)
DAP dahil dört Incoterm'i de görüşmeye açık bırakıyor — yani riskin kimde olacağı
müzakere edilebilir. RFQ 2.12 reefer/thermal liner sürşarjını soruyor.

#### 2.4 — Palet standardı
RFQ 2.6 palet tipini (EUR 120×80 vs endüstriyel 120×100) ve ISPM-15 ısıl işlem
durumunu soruyor. AB dışı menşelerde ahşap palet fümigasyon belgesi ek bir
dokümantasyon kalemi olabilir.

---

### 3. `mevzuat-ruhsat-uzmani` için

#### 3.1 — Türkçe arka etiket menşede uygulanabilir mi?
Bu, tek başına önemli bir maliyet kalemidir. Menşede uygulanabiliyorsa Türkiye'deki
etiketleme operasyonu tamamen ortadan kalkar. → T-403

#### 3.2 — Üretici tarafı ithalat lisansını ithalatçıya bırakıyor
Bir üretici sitesinde ithalatçının **kendi pazarında ithalat lisansı alması
gerektiğini** açıkça belirtiyor (`EV-2026-08-09-408`). Yani ruhsat yükü bizde
olacak ve bu, tedarikçi müzakeresinde bir kaldıraç değil, bir ön koşul.

#### 3.3 — Etiket üzerinde bandrol/şerit için boş alan
RFQ 6.9, üreticiden etiket veya şişe üzerinde ithalatçının uygulayacağı
damga/şerit için tanımlı bir boş alan bırakıp bırakamayacağını soruyor.
Bunun **gerekip gerekmediğini** siz söylemelisiniz.

#### 3.4 — Analiz sertifikası parametreleri
RFQ 6.3–6.4 analiz sertifikasında hangi parametrelerin bulunduğunu ve laboratuvarın
akredite olup olmadığını soruyor. Türkiye'nin ithalatta hangi parametreleri
istediği bilinirse RFQ'yu daraltabilirim.

#### 3.5 — Vegan / helal / organik iddiaları
Bir üretici vegan, organik ve **helal sertifikalı** seçenekler sunduğunu beyan ediyor
(`EV-2026-08-09-408`). Türkiye pazarında bu tür iddiaların etikette kullanımı
kısıtlıysa bilmem gerekir.

---

### 4. `turkiye-pazar-kasifi` için

#### 4.1 — Benchmark markalarının kimliği belirsiz
"Gold Country" (California) ve "Central Creek" (Avustralya) markalarının üreticisi
açık kaynakta bulunamadı. İkisi de ithalatçı özel markası olabilir — bu, Model B'nin
Türkiye'de zaten çalıştığının kanıtı olurdu. **Bu bir iddia değil, hipotezdir.**
`EV-2026-08-09-422`, `EV-2026-08-09-423` → T-405

#### 4.2 — İthalat hacmi bağlamı (yorum sizin alanınız)
Türkiye 2025'te 2204.21 kaleminde 17.848.518 litre ithal etti (66,88 m USD CIF).
750 ml eşdeğeri ~23,8 milyon şişe/yıl — bu **yalnızca aritmetik bir dönüşümdür**,
pazar payı iddiası değildir. `EV-2026-08-09-426`

#### 4.3 — Menşe karışımı beklenmedik
Türkiye'nin şişelenmiş şarap ithalatında hacim lideri **İtalya** (5,75 m litre),
onu Fransa (2,85), Moldova (2,04), İspanya (1,92), Gürcistan (1,47), Bulgaristan (1,38)
izliyor. Benchmark'ın menşei olan **ABD 18.298 litre**, komşu benchmark'ın menşei
olan **Avustralya 44.674 litre**. Yani iki benchmark ürünün menşei de Türkiye'ye
neredeyse hiç mal göndermeyen ülkeler. `EV-2026-08-09-405`
→ Raf gözleminizde bu ürünlerin gerçekten ne kadar yaygın olduğunu kontrol etmeye değer.

#### 4.4 — Yunanistan çöküşü
Yunanistan 2024'te Türkiye'ye 1,71 m litre gönderdi, 2025'te 49.634 litreye düştü
(-%97). Bulgaristan ise 2025'te sıfırdan 1,38 m litreye çıktı. Bu, bir ithalatçının
menşe değiştirdiği veya bir düzenleme değişikliği olduğu anlamına gelebilir.
`EV-2026-08-09-405`, `EV-2026-08-09-406`

---

### 5. `kanal-marj-uzmani` için

#### 5.1 — Marka desteği kaleminin karşılığı
Model A'da üreticiden pazarlama/listeleme katkısı alınabildiği sektör kaynaklarında
geçiyor, ancak **doğrulanabilir tipik bir oran/tutar bulunamadı** (UNKNOWN).
RFQ 5.6 bunu doğrudan soruyor. Sizin kanal tarafında bulacağınız listeleme
bedeli ile bu katkı **aynı satırda netleştirilmelidir** — aksi halde çift sayım olur.

#### 5.2 — Üretici fiyat tavanı dayatabilir
Sektör hukuk kaynakları, distribütörlük sözleşmelerinde ithalatçının uygulayabileceği
**markup tavanının** yaygın bir madde olduğunu belirtiyor. Doğruysa, Model A'da kanal
marjı üzerinde bizim kontrolümüz sınırlıdır. RFQ 5.7 bunu soruyor.

---

### 6. `finans-fizibilite` için

#### 6.1 — Fiyat girdisi YOK
`tedarikci.yaml`'da `exw_per_sise` ve `fob_per_sise` **null**'dur. Bu turda hiçbir
teklif alınmamıştır. Modelde bu alanlar `UNKNOWN` dönmelidir.

#### 6.2 — Kullanılabilecek tek şey duyarlılık sınırlarıdır
`arastirma_bulgulari.fob_gosterge_bandi` bir **bant**tır, bir fiyat değildir:
alt sınır 0,56 EUR/750 ml (yalnızca sıvı, kuru malzeme hariç), üst sınır
1,85–2,40 USD/750 ml (bu bir **CIF/L2** tavanıdır, FOB tanım gereği altındadır).
**İki para birimi bilinçli olarak birleştirilmemiştir.** Kur dönüşümü yalnızca
`makro.yaml`'daki kanıtlı kurla yapılır.

#### 6.3 — MOQ, hacim senaryolarını asimetrik kısıtlar
Doğrulanmış private label MOQ'ları 3.000–3.600 şişe → 5.000 şişelik pilot senaryosu
**teknik olarak** mümkün. Ama konteyner bazlı MOQ uygulayan üreticilerde pilot
mümkün değil. Yani 5.000 şişe senaryosu **tedarikçi havuzunu daraltır** ve bu daralma
büyük ihtimalle birim fiyatı yükseltir. Bu ödünleşim modellenmelidir.

#### 6.4 — Lead time girdisi kısmi
Üretim/şişeleme süresi için elde n=2 gözlem var: 28–42 gün (FR) ve ~28 gün (ZA).
**Navlun, gümrük ve iç lojistik HARİÇ.** Toplam tedarik süresi için
`navlun-lojistik-uzmani`'nın transit süresi eklenmelidir.

#### 6.5 — Alternatif tedarikçi sayısı gerçekte 0
`risk.alternatif_tedarikci_sayisi = 0`. Havuzda 11 aday var ama hiçbirinden fiyat
alınmadı. Model, "tedarikçi değiştirme opsiyonu var" varsayımıyla çalıştırılmamalıdır.

---

### 7. `seytanin-avukati` için — kendi işime karşı hazırladığım cephane

1. **Bu raporda tek bir gerçek teklif yok.** `quote_type` her satırda `NONE_YET`.
   Tüm fiyat sinyalleri ya ülke ortalaması ya web sitesi beyanıdır.
2. **Model B, Model A'dan daha zengin görünüyor — bu bir arama yanlılığıdır.**
   Private label sağlayıcıları web'de aranabilir; marka sahipleri fuarda çalışır.
   Bunu raporda açıkça itiraf ettim ama yine de asimetri duruyor.
3. **CIF birim değerinin miktar birimi doğrulanmadı.** Comtrade `qtyUnitCode=7`
   litre olarak yorumlandı. Yanlışsa tüm L2 sütunu kayar.
4. **11 "doğrulanmış tedarikçi" ifadesi abartılıdır.** Doğrulanan tek şey web
   sitesinin erişilebilir olduğu ve private label iddiasının orada yazdığıdır.
   Ne kapasitesi, ne fiyatı, ne Türkiye'ye ihracat kabiliyeti doğrulandı.
5. **MOQ 3.000 şişe rakamı tek bir üreticinin web sitesinden geliyor** ve
   `C-401`'de bir T5 kaynak bunu 300–1.200 diye çelişkiye sokuyor.
   Ters yönde de sapabilir.

---

### 8. BULK ŞARAP + TÜRKİYE'DE ŞİŞELEME HİPOTEZİ *(kapsam dışı — kayıt için)*

**Hipotez:** Dökme şarap ithal edip Türkiye'de şişelemek, şişelenmiş ürün ithal
etmekten ekonomik olarak daha avantajlı olabilir mi?

**Statü:** `HYPOTHESIS — NOT INVESTIGATED`
**Kapsam:** `00-charter/kapsam.md` uyarınca **KAPSAM DIŞI.** Bu ajan hipotezi
kaydeder, çözmez.

**Bu turda toplanan iki ham gözlem (yorum yok):**

| # | Gözlem | evidence_id |
|---|---|---|
| 1 | Dünya dökme şarap ort. ihracat fiyatı 2025 = **0,75 EUR/litre**; şişelenmiş (<2 l) = **4,53 EUR/litre**. Fark 6 kat. | EV-2026-08-09-402, EV-2026-08-09-401 |
| 2 | Türkiye 2025'te GTİP 2204.29 (dökme) kaleminde **628 litre** ithal etti. Aynı yıl şişelenmiş ithalat 17.848.518 litre. | EV-2026-08-09-407 |

**Ek gözlem:** Aday tedarikçilerden en az dördü (Corta Hojas/CL, FMS/ZA,
Kingston Estate/AU, Origin Wine) flexitank/IBC ile dökme sevkiyat yapıyor —
yani **arz tarafında bulk kapasitesi bol ve rutin.** Kısıt, eğer varsa,
arz tarafında değildir.

**İlgili ajanlara sorular (bu ajan CEVAPLAMAZ):**

| Ajan | Soru | Ticket |
|---|---|---|
| `gumruk-vergi-uzmani` | Dökme şarabın GTİP'i ve vergi rejimi şişelenmişten farklı mı? Türkiye'nin 2025'te neredeyse hiç dökme ithal etmemesinin vergisel bir açıklaması var mı? | T-406 |
| `mevzuat-ruhsat-uzmani` | Türkiye'de şişeleme ayrı bir üretim ruhsatı gerektirir mi? İthal dökme şaraptan şişelenen ürünün menşei ve etiketi nasıl tanımlanır? | (açılmadı — kapsam dışı) |
| `navlun-lojistik-uzmani` | Flexitank / ISO tank lojistiği nasıl işler, 24.000 L'lik bir yüklemenin transit ve sıcaklık riski nedir? | (açılmadı — kapsam dışı) |

**Bu hipotez bu projede çözülmeyecektir.** Yeniden açılırsa yukarıdaki üç soru
başlangıç noktasıdır.

---

## turkiye-pazar-kasifi

> Bunlar **sonuç değildir**, ipucudur. Kendi alanım dışında gördüğüm ama ilgili
> ajanın işine yarayacak gözlemler. Ana `99-ops/capraz-ipuclari.md`'ye birleştirilecek.

---

### → `kanal-marj-uzmani`

#### İP-501 — Metro'da mağaza fiyatı ile teslimat fiyatı FARKLI
Metro Türkiye broşür künyesi (`EV-2026-08-09-507`):
> *"Broşürdeki fiyatlar **sevkiyat hizmeti alan müşterilerimiz için geçerli değildir**."*

Yani Metro'da en az iki fiyat rejimi vardır: **cash & carry mağaza** ve
**Metro Gastro Servis / teslimat (HoReCa dağıtım)**. Aradaki fark **UNKNOWN**.
Bu, "Metro'ya tek fiyat verilir" varsayımını kırar. → `T-506`

#### İP-502 — Alkol, Metro'nun tüm çek/sadakat kampanyalarının DIŞINDA
`EV-2026-08-09-508`: Metro'nun 2026 kampanya koşullarında hariç tutulanlar:
*"toptan-perakende tütün ve **alkol**, çuval şeker, karkas et"*.
→ Şarapta ciro primi / çek / sadakat mekaniği Metro'da **çalışmıyor** görünüyor.
Kanal ekonomisinin bu kalemsiz kurulması gerekebilir.

#### İP-503 — Metro'nun ticari dili KDV HARİÇ, etiket dili KDV DAHİL
`EV-508` vs `EV-503/504`. İthalatçı–Metro pazarlığında sayılar büyük olasılıkla
**KDV hariç** konuşulacaktır. Marj modelinde matrah karışıklığına dikkat.

#### İP-504 — Metro fiyatı ile online uzman perakende fiyatı arasında büyük fark var
Metro'da ithal giriş 599,90 TL (`EV-501`); online uzman perakendede stokta en ucuz
ithal 875 TL (`EV-509`). Fark %46. Bunun ne kadarı kanal marjı, ne kadarı ürün
segmenti farkı — **ben hesaplamadım, sizin alanınız.**

#### İP-505 — Metro'nun online fiyatları müşteriye özel
`guncelfiyatlar.metro-tr.com` → *"Size özel fiyatları görmek için Giriş Yapın"*.
Metro'da müşteri numarasına bağlı **özel fiyat** uygulaması olabilir. Bu, tek bir
raf fiyatının "kanal fiyatı" sayılmasını zorlaştırır.

---

### → `mevzuat-ruhsat-uzmani`

#### İP-506 — Alkol reklam yasağı fiyat şeffaflığını yok ediyor
`EV-2026-08-09-514`: Metro'nun incelenen **58 sayfalık** broşür setinde
(48 sayfalık "İçecek Trendleri ve Çözümleri" katalogu dahil) **tek bir alkollü içki
SKU'su bile yok**. Bu, hem bizim veri toplama kabiliyetimizi hem de kendi ürünümüzün
lansman araçlarını doğrudan etkiler. → `T-503`

#### İP-507 — Online alkol satışı yasağı, D2C ve fiyat keşfi kanalını kapatıyor
`EV-2026-08-09-511`. Ayrıca `iyisarap.plus` gibi siteler fiyat gösterip satış yapar
görünüyor — bunun yasal statüsü bizim gözlem kaynağımızın güvenilirliğini etkiler.
→ `T-502`

#### İP-508 — Fiyat Etiketi Yönetmeliği "toptan+perakende birlikte" hükmü
`EV-2026-08-09-506`. Metro gibi karma formatlarda perakende hükümlerinin uygulandığı
iddiası OQ-001'in hukuki ayağıdır ve **T1 doğrulaması bekliyor.** → `T-501`

#### İP-509 — TADAB istatistik sayfası alkollü içki verisi yayınlamıyor
`EV-2026-08-09-515`: `tarimorman.gov.tr/TADAB/Link/38/Resmi-Istatistikler` sayfası
2011–2026 arası **yalnızca yakıt biyoetanolü** dönem raporları içeriyor.
Alkollü içki piyasa istatistikleri başka bir yerde olmalı. → `T-505`

---

### → `global-sourcing-kasifi`

#### İP-510 — ABD ve Avustralya menşe, uzman perakende kanalında YOK
`EV-2026-08-09-509`: Online uzman perakendecinin ülke koleksiyonları
Fransa 33 / İtalya 30 / İspanya 6 / Avusturya 4 / Şili 2 / Arjantin 2 / Almanya 2 —
**ABD ve Avustralya koleksiyonu hiç yok.**
Buna karşılık Metro'daki iki benchmark SKU tam da bu iki menşeden.
→ ABD/Avustralya, Türkiye'de **kanal olarak yerleşmemiş** menşeler olabilir;
bu hem fırsat (rekabet yok) hem risk (tüketici tanıdıklığı yok) demektir.

#### İP-511 — Benchmark markaları Avrupa'da discount/value markası profilinde
"Gold Country Colombard-Chardonnay" Almanya'da içki toptancıları ve posta siparişi
kanallarında ~7 EUR bandında listeleniyor (T5, arama sonucu düzeyinde — doğrulanmadı).
Bu, benchmark'ın **bulk-blend / value** kategorisinde olduğuna işaret eder.
Sourcing hedefi bu kategoriye göre seçilmelidir. **Bu bir fiyat verisi değildir,
sizin doğrulamanız gerekir.**

#### İP-512 — Yerli üretici benchmark bandını dolduruyor
`EV-2026-08-09-510`: 600–800 TL bandında 25 yerli SKU var, 0 ithal SKU.
Yani ithal edeceğimiz ürün, bu bandda **yerli üreticiyle** yarışacak —
gümrük/ÖTV yükü taşımayan rakiplerle. Bu, hedef EXW/FOB'u sertçe aşağı çeker.

---

### → `gumruk-vergi-uzmani`

#### İP-513 — Metro künyesi: vergi değişikliği fiyata aynen yansıtılır
`EV-2026-08-09-507`: *"Devlet tarafından yapılan vergi ve fon değişiklikleri fiyatlara
aynen yansıtılacaktır."* → Perakende kanal, vergi artışını **tampon yapmıyor**;
ÖTV artışı doğrudan raf fiyatına geçiyor. Bu, ÖTV duyarlılık analizinde
"kanal yutar mı" sorusuna cevap verir: **yutmuyor.**

#### İP-514 — Şikâyet kayıtlarında KDV oranı tartışması
Şikâyet platformunda Metro için "rafta %1 KDV yazıyor, kasada %8 uygulanıyor"
tipi kayıtlar var (T5, LOW). Gıda dışı/gıda KDV oranı ayrımı şarap için geçerli
değildir ama **şarapta uygulanan KDV oranının doğrulanması sizin alanınızdır.**
Ben oran belirtmiyorum.

---

### → `yatirim-komitesi-baskani`

#### İP-515 — `00-charter/benchmark.md` güncelleme önerisi
Ben o dosyaya dokunmadım. Önerim:

```yaml
BENCHMARK 1 - Gold Country:
  KDV durumu:            KDV DAHIL     # eski: UNKNOWN
  KDV durumu status:     ESTIMATE (HIGH)  # EV-503/504/505/506
  Fiyat katmani:         L8_METRO_CASH_CARRY   # eski: UNKNOWN
  Fiyat katmani notu:    "Zincir market L8'i DEGILDIR; HoReCa/bakkal icin L7-proxy"
  Promosyon durumu:      UNKNOWN       # DEGISMEDI - T-504 acik
  evidence_id:           EV-2026-08-09-501
BENCHMARK 2 - Central Creek:  ayni sekilde, evidence_id: EV-2026-08-09-502
```

Ve `MODEL KULLANIM KURALI` bölümünde BM_A'nın base case, BM_B'nin sensitivity
olması; BM_C (promosyon) ve BM_D (zincir L8 farkı) senaryolarının eklenmesi.

#### İP-516 — Bu turun en zayıf noktası: kanal örneklemi
52 gözlemin 45'i **tek bir online kanaldan** geliyor. Zincir market ve tekel
bayiinde **sıfır** gözlem var. Segment bantlarını "Türkiye pazarı" diye okumak
şu an **hatalı** olur. → `OQ-502`

---

---

# TUR 1.5 ÇAPRAZ İPUÇLARI

> Dört ajanın TUR 1.5 çapraz ipuçları. Ajanların kendi numaralandırması korundu.

## gumruk-vergi-uzmani (TUR 1.5)

> Alan dışı bulgular. **Sonuç üretilmemiştir** (CLAUDE.md §1.10, §1.11).
> `99-ops/capraz-ipuclari.md` ana dosyasına DOKUNULMAMIŞTIR.

---

### → `navlun-lojistik-uzmani`

#### Cİ-15.1 — Kırılma/fire oranı artık bir VERGİ kalemidir (MEDIUM–HIGH)

KDVK **md.30/c** (T1, `EV-2026-08-10-103`): *"…**zayi olan mallara ait katma
değer vergisi**"* indirilemez.

Bu, fire oranını salt bir lojistik kaybı olmaktan çıkarır:

```
fire_maliyeti = f × (L4_per_sise)              ← malın kendisi
              + f × (KDV_per_sise)             ← İNDİRİLEMEYEN KDV  ← YENİ
```

Yani cam şişede **her %1 fire, KDV kanalından ayrıca ~%1 × 40–45 TL/şişe**
gerçek ekonomik maliyet yaratır (illüstratif CIF=100 TL'de). Bu, TUR 1'de
hiçbir yerde modellenmemiştir.

**İstenen:** `lojistik.yaml`'a `fire_orani` alanı (deniz taşıması + antrepo +
iç dağıtım kırılması). Kanıtlı bir bant yoksa `null` + `UNKNOWN`.
Vergi tarafı hazır: `vergi.yaml → kdv_perspektifleri.a_ekonomik_maliyet.
kdv_ekonomik_maliyete_donusme_kosullari[K2]` ve `hesap_sozlesmesi.turev_ciktilar
→ kdv_fire_maliyeti`.

#### Cİ-15.2 — `lojistik.yaml → urun_fizik.sise_hacmi_ml = 750` aynı hijyen sorununu taşıyor (LOW)

`T-906(a)` `vergi.yaml`'daki `sise_hacmi_litre = 0.75` alanını
`FACT` + `evidence_id: null` → `ASSUMPTION` + `EV-2026-08-10-116` olarak
düzeltti. Başkanın denetimi (§3.2) **aynı sayının** `lojistik.yaml`'da da
`FACT` + `evidence_id: null` durduğunu tespit etmişti.

**Bu dosyaya DOKUNULMADI** (ajan izolasyonu). Aynı düzeltme orada da
yapılabilir; `EV-2026-08-10-116` kartı doğrudan referans alınabilir.

#### Cİ-15.3 — Antrepo, ÖTV/GV'nin yanı sıra KDV nakit çıkışını da öteler (MEDIUM)

`EV-2026-08-10-106` (KDVK md.10/ı, T1): ithalatta vergiyi doğuran olay
**serbest dolaşıma giriş beyannamesinin tescilidir.** Bu yalnızca ÖTV ve gümrük
vergisi için değil, **KDV için de** geçerlidir.

Sonuç: `T-101` (antrepodan kısmi çekiş) sorusunun `peak_cash_requirement`
üzerindeki etkisi TUR 1'de sanılandan **daha büyüktür** — çünkü ertelenen tutar
sadece kalıcı vergiler değil, **devreden KDV havuzunun kendisidir.**
Kısmi çekiş mümkünse devreden KDV havuzu **hiç oluşmayabilir.**

**Karşı kalem (değişmedi):** ÖTV maktu tutarı Ocak/Temmuz'da artar
(`EV-2026-08-09-114`) → bekletme ÖTV artış riski taşır.

---

### → `finans-fizibilite`

#### Cİ-15.4 — Devreden KDV'nin finansman maliyeti L5'te GERÇEK bir maliyettir

KDV ekonomik maliyet **değildir** (indirilebilir), ama **bedava da değildir.**
Devreden KDV nakden **iade edilmez** (KDVK md.29/2, `EV-2026-08-10-104`) ve
28–59 gün (ilk konteynerde satış hızı kadar) kilitli kalır.

```
kdv_finansman_maliyeti = ortalama_devreden_KDV × finansman_orani × sure_yil
```

`finansman_orani` `makro.yaml` alanıdır ve şu an `null`/`UNKNOWN`'dır.
Bu kalem **L5'te ayrı satır** olmalıdır (`vergi.yaml → engine_kurallari[C3]`).

#### Cİ-15.5 — "Vergi yükü" tek satırda toplanamaz

`ekonomik_vergi_yuku = GV + İGV + KKDF + ÖTV` — **KDV DAHİL DEĞİL.**
`kdv_nakit_cikisi = KDV` — L5'e taşınmaz ama `peak_cash_requirement`'a
**tam tutarıyla** girer.

L4'e bakıp "şişe başına vergi yükü ~140 TL" demek **yanlıştır**.
Bkz. `vergi.yaml → hesap_sozlesmesi.turev_ciktilar` ve `engine_kurallari[C2, C4]`.

---

### → `mevzuat-ruhsat-uzmani` (bilgi notu — sonuç üretilmemiştir)

#### Cİ-15.6 — Bandrol bedelinin katmanı, KDV matrahını da ilgilendiriyor

Başkanın denetimi (§2.5) bandrolün L5 değil **L3**'te doğabileceğini ve
vergilendirilebilir olabileceğini tespit etmişti (`T-203`).

TUR 1.5'te KDVK **md.21** tam metni okundu (`EV-2026-08-10-108`, T1):
matraha *"(c) gümrük beyannamesinin **tescil tarihine kadar** yapılan diğer
giderler ve ödemelerden **vergilendirilmeyenler**"* girer.

İki koşul birlikte aranır: **(1)** ödeme tescilden **önce** yapılmış olmalı,
**(2)** kendisi **vergilendirilmemiş** olmalı. Bandrol bedeli KDV'ye tabi bir
hizmet bedeli ise (2) sağlanmayabilir.

**Bu bir sonuç değildir** — bandrolün hukuki niteliği ve KDV'ye tabi olup
olmadığı `mevzuat-ruhsat-uzmani` alanıdır. Yalnızca `T-203`'ün doğru soruyu
sorabilmesi için madde metni buraya bırakılmıştır.

#### Cİ-15.7 — KVK md.11/1-(ı): alkol reklam gideri KKEG (bilgi notu)

`EV-2026-08-10-113` (T1): alkollü içki **ilan/reklam giderlerinin %50'si**
kurum kazancının tespitinde indirilemez; KDVK md.30/d uyarınca o kısma ait
**KDV de indirilemez.**

**Bu bir vergi bulgusudur ve bu ajanın alanındadır.** Ancak alkolde reklamın
4250 / 7584 kapsamında **hukuken mümkün olup olmadığı** araştırılmamıştır
(bu tur kapsamı dışı ve `mevzuat-ruhsat-uzmani` alanı). Reklam hukuken
yapılamıyorsa bu hükmün pratik etkisi **sıfırdır** — dolayısıyla bu bir
"maliyet kalemi" olarak modele **girmemiştir.**

---

## mevzuat-ruhsat-uzmani (TUR 1.5)

> `99-ops/capraz-ipuclari.md`'ye konsolide edilmek üzere. Ana dosyaya bu turda
> **DOKUNULMAMIŞTIR.** CLAUDE.md §1.11: alan dışı bulgu silinmez, bırakılır.
> Bu tur dar kapsamlı olduğu için yalnızca **3 ipucu** vardır.

| # | Hedef ajan | İpucu | Neden önemli | Kanıt |
|---|---|---|---|---|
| X-251 | `kanal-marj-uzmani` | **TUR 1'deki bir bilgiyi düzeltiyorum.** Ticaret Yön. m.9/2'nin 4250 m.1/3'teki *"ülke genelinde yerinde teslim"* şartını teyit ettiğini yazmıştım — **metin bunu söylemiyor.** Yönetmelikteki yükümlülük daha dardır: *"perakende satıcıların taleplerini zamanında karşılayacak dağıtımı sağlamak."* "Ülke genelinde" ve "yerinde teslim" ifadeleri **yalnızca kanunda** geçer. | İki metnin **dağıtım maliyeti yükü farklıdır**. Ulusal kılcal dağıtım ağı zorunluluğu varsayımı TUR 1'de olduğundan **daha zayıf** bir zemine oturuyor. Kanal modeli bu farkı ayrıştırmalı. | `EV-2026-08-10-212` (T1) |
| X-252 | `finans-fizibilite` | Beş hacim senaryosunun **hiçbiri** 4250 m.1/3 eşiğine ulaşmıyor (3.750–75.000 L vs 600.000 L). "Eşiği aşmak için hacmi büyütelim" **modellenebilir bir strateji değildir**: en büyük senaryonun **8 katı** gerekir. Buna karşılık **20.000 litre/yıl bedel kırılımı** (S3→S4 arasında, 26.667 şişede) gerçek ve modellenmesi gereken tek eşiktir. | Ölçek duyarlılığında yanlış eşiğe optimizasyon yapılmasını engeller. | `EV-2026-08-10-215`, `EV-2026-08-09-206` |
| X-253 | `seytanin-avukati` | Bu turun **proje aleyhine iki bulgusu** kırmızı takım için hazır malzemedir: (1) 4733 m.4/B(b) ile 4250'nin uygulanması **açıkça Bakanlığa devredilmiştir** — "hüküm ölü, merci yok" argümanı **çürüktür**; (2) 4733 m.8'in artık fıkrası, sayılmayan tüm 4250 aykırılıkları için **uyarı → süre → BELGE İPTALİ** yolunu açık tutar. Yani 4250'ye aykırılık yaptırımsız değildir. | G0 PASS önerimin en saldırılabilir yeri burasıdır ve **kendim işaretledim.** | `EV-2026-08-10-208`, `EV-2026-08-10-210` (ikisi de T1) |

---

### Alan dışı bırakılan tek gözlem

TADAB sitesinde **"İdari Yaptırımlar ve Teminatlar"** bölümü mevcuttur ve yıl
bazında 4250/4733 idari para cezası listeleri yayımlanmaktadır. Bu, hem
`teminat.*` (`UNKNOWN`, TUR 1) hem de OQ-254 için birincil aday kaynaktır.
**Bu turda incelenmemiş, hakkında sonuç üretilmemiştir.**

---

## global-sourcing-kasifi (TUR 1.5)

```yaml
ajan:   global-sourcing-kasifi
tur:    TUR 1.5 — BLOCKER REMEDIATION (T-902)
tarih:  2026-08-10
kapsam: Yalnizca T-902 duzeltmesi + RFQ alan kontrolu. YENI ARASTIRMA YAPILMADI.
```

> Bu dosya bir **parça dosyasıdır**. `99-ops/capraz-ipuclari.md` ana dosyasına
> `yatirim-komitesi-baskani` tarafından birleştirilir. Bu ajan ana dosyaya dokunmadı.

---

### 1. `finans-fizibilite` — EN KRİTİK, MODELİ SESSİZCE BOZABİLİR

**`tedarikci.yaml`'daki iki seri artık L1 (FOB) etiketi taşımıyor. Aralarında çıkarma
işlemi yapmayın.**

TUR 1'de iki alan yanlışlıkla L1 (FOB) etiketiyle duruyordu. T-902 ile bu etiketler
geri çekildi. Somut risk şudur:

```
YANLIŞ:  navlun = L2_CIF_serisi − "L1"_serisi
SONUÇ:   İspanya, Portekiz ve Fransa için NEGATİF NAVLUN
```

Bu üç menşede "L1" serisi L2 serisinden **büyüktür**. Bu bir veri hatası değil, iki
serinin farklı şeyleri ölçtüğünün kanıtıdır (farklı ürün karması, farklı para birimi,
farklı raporlama bazı, farklı yıl kesiti — detay `tedarikci.yaml →
ulke_gosterge_birim_degerleri.karsilastirilamazlik_kaniti`).

Uyulması gereken üç kural YAML içine gömüldü:
- `duyarlilik_sinirlari_KARISIK_KATMAN.finans_fizibiliteye_uyari`
- `karsilastirilamazlik_kaniti.kullanim_yasagi` (4 madde)
- `kullanim_kurali: SENSITIVITY_BOUNDS_ONLY` (çit korundu)

**`fiyat.fob_per_sise` hâlâ `null`/`UNKNOWN`'dır ve bu turda da öyle kalmıştır.**
Gerçek FOB yalnızca RFQ ile alınacak `FIRM_OFFER`'dan gelir.

**Ek kural (T-902 sonrası):** duyarlılık çıktısı raporlanırken **hangi sınırın hangi
katmandan geldiği** yazılmak zorundadır. Alt sınır `L0_ALTI`, üst sınır `L2`'dir.

---

### 2. `navlun-lojistik-uzmani` — RFQ artık ağırlık verisini eksiksiz soruyor

`rfq-template.md` v2.1'de eklenen alanlar sizin konteyner/ağırlık hesabınız içindir:

| Yeni soru | Ne veriyor |
|---|---|
| 1.14 | Boş şişe ağırlığı (g) — koli brüt ağırlığının (2.2) bağımsız çapraz kontrolü |
| 1.15 | Dolu şişe brüt ağırlığı (g) — kapak, kapsül, etiket dahil |
| 1.16 | Hafif şişe alternatifi + şişe başına fiyat farkı — ağırlık/navlun ödünleşimi |
| 3.17d | Lead time'ın "gemi/kamyon bekleme" bileşeni ayrı soruluyor |

**Sizden bir talebim var:** v2.1'i bir kez okuyup Bölüm 2 (2.1–2.13) + 1.14/1.15 ile
konteyner doluluk hesabınızı **gerçekten kurabiliyor musunuz**, eksik bir alan var mı?
Varsa şablona eklerim — şablon TUR 7'de gönderildikten sonra eklemek geç olur.
(T-402 hâlâ OPEN.)

---

### 3. `gumruk-vergi-uzmani` — RFQ 3.18 ve 3.20 sizin matrahınızı ilgilendirebilir

Şablona eklenen 3.18, kuru malzeme kalemlerinin (etiket, karton, kapsül, palet)
**EXW fiyatının içinde mi dışında mı** olduğunu ayrı ayrı soruyor. 3.20 ise ihracat
evrak ücretlerini soruyor.

**Neden size ipucu bırakıyorum:** bu kalemlerin faturada ayrı satır olarak mı yoksa
mal bedeline dahil mi geldiği, gümrük kıymetinin oluşumunu etkiliyor olabilir.
**Bu benim alanım değil ve bir sonuç üretmedim.** Eğer fatura yapısı kıymet açısından
fark yaratıyorsa, RFQ'ya bu turdan sonra bir soru daha ekleyebilirim — söyleyin.

---

### 4. `yatirim-komitesi-baskani` — iki bakım işi

1. **`10-evidence/index.csv`:** `EV-2026-08-09-404`, `-419` ve `-421` kartlarının
   `status` alanı kart dosyalarında `SUPERSEDED` yapıldı, ancak `index.csv`
   satırlarında hâlâ eski değer duruyor. Bu ajan `index.csv`'ye dokunmakla
   yetkilendirilmedi. Yeni satırlar:
   `10-evidence/_index-parts/global-sourcing-kasifi-tur15.csv` (başlıksız, 3 satır).
2. **Terminoloji uyarısı:** `fob_gosterge_bandi` adı repoda **beş dosyada daha**
   geçiyor (denetim raporu, T-902, tickets/INDEX.md, `capraz-ipuclari.md` §607,
   TUR 1 raporu §5). Bunlar **tarihsel kayıttır ve değiştirilmemiştir** — geçmişi
   yeniden yazmak kanıt disiplinine aykırı olurdu. İzlenebilirlik için YAML'a
   `eski_adi` alanı eklendi. Arama yapan biri hem eski hem yeni adı bulur.

---

### 5. `seytanin-avukati` — size iki yeni saldırı vektörü bırakıyorum

1. **RFQ v2.1 uzadı.** 13 soru daha eklendi. Kendinizi bir üretici yerine koyup
   şablonu okuyun: kaç satırı **kaçamak cevapla** geçiştirebilirsiniz? Özellikle
   S19/S20 ("etiket ve karton EXW'nin içinde mi") ve 3.6 (MOQ) satırlarını hedef
   alın. Şablon "N/A veya TBC yazın" diyor — bu dürüstlüğü teşvik eder, ama aynı
   zamanda **cevaptan kaçmak için meşru bir kapı** açar.
2. **Katman düzeltmesi bir şeyi çözmedi, sadece dürüstçe etiketledi.** T-902 sonrası
   elimizde hâlâ **tek bir gerçek EXW veya FOB rakamı yok.** "Katman etiketi
   düzeltildi" cümlesi ilerleme gibi okunabilir; okunmamalı. Fiyat bilgisi açısından
   TUR 1.5, TUR 1'den bir milimetre ileride değildir.

---

### 6. BU TURDA YAPILMAYANLAR (kapsam dışı, bilinçli)

- Yeni tedarikçi, yeni ülke, yeni fiyat araştırması **yapılmadı**.
- Hiçbir üreticiye e-posta/mesaj **gönderilmedi**.
- OIV ihracat değer tanımının FOB olup olmadığı **araştırılmadı** (açık soru olarak
  kaydedildi — bkz. `acik-sorular-global-sourcing-kasifi-tur15.md`).
- Vergi, navlun tutarı, ruhsat ve kanal marjı konularında **sonuç üretilmedi**.

---

## turkiye-pazar-kasifi (TUR 1.5)

> `99-ops/capraz-ipuclari.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından DOKUNULMAMIŞTIR.
> **Bunlar SONUÇ DEĞİL, İPUCUDUR.** Bu tur dar kapsamlıydı; liste kısadır.

| # | Hedef ajan | İpucu | evidence_id | Neden önemli |
|---|---|---|---|---|
| İP-551 | `kanal-marj-uzmani` | Metro'nun **2010 şarap kataloğunda** fiyatlar KDV hariç + KDV'li **çiftli** basılıydı ve KDV hariç sayı ondalıklı (131,36), KDV'li sayı yuvarlaktı (155,00) | `EV-2026-08-10-503` | Metro'nun şarap kategorisinde **brüt fiyattan geriye** çalıştığını (net değil) gösterir. Pazarlıkta hangi matrahtan konuşulduğu belirsizse marj hesabı kayar. |
| İP-552 | `kanal-marj-uzmani` | Metro'nun tarihsel şarap fiyatları **dönemseldir**: *"fiyatlar &lt;tarih aralığı&gt; arasında geçerlidir ve stoklarla sınırlıdır"* | `EV-2026-08-10-503` | Şarapta Metro'nun "kalıcı raf fiyatı" verip vermediği belirsiz. Listeleme/vade pazarlığında fiyat taahhüdünün süresi sorulmalı. |
| İP-553 | `mevzuat-ruhsat-uzmani` | Metro Türkiye 2013'e kadar **basılı şarap katalogu** yayınlıyordu; 2026'da hiçbir yayınında alkol yok | `EV-2026-08-10-503`, `EV-2026-08-09-514` | Reklam yasağının **fiili başlangıcını** ve kapsamının pratikte nereye oturduğunu gösteren somut bir "önce/sonra" karşılaştırması. *(Yasağın kapsamı bu turda YENİDEN ARAŞTIRILMAMIŞTIR — kabul edilmiş iş kısıtıdır.)* |
| İP-554 | `global-sourcing-kasifi` | Metro'nun 2008–2010 ithal şarap assortmanında **ABD ve Avustralya menşe zaten vardı** (Terra California Zinfandel, Sunset Creek California, Yellow Tail Shiraz, Huntington Chardonnay, Gallo) | `EV-2026-08-10-503` | Metro'nun bu iki menşede **15+ yıllık bir listeleme geçmişi** var. `EV-2026-08-09-509`'daki "uzman kanalda ABD/Avustralya YOK" bulgusuyla birlikte okunduğunda: bu menşeler Türkiye'de **uzman kanalın değil, cash&carry/market kanalının** menşeleridir. Kanal seçimi ile menşe seçimi bağımsız değildir. |
| İP-555 | `yatirim-komitesi-baskani` | `10-evidence/index.csv`'de `EV-2026-08-09-509` / `-510` satırlarının `status` alanı hâlâ `FACT`; raw kartlar `SUPERSEDED` yapıldı | — | Bu ajan `index.csv`'ye dokunmakla yetkili değil. Merge sırasında düzeltilmezse index ile kartlar desenkron kalır. |
| İP-556 | `finans-fizibilite` | `pazar.yaml` içindeki `katman_kurallari.K4`: bu dosyadan **marj türetilemez**; Metro 599,90 ile uzman perakende 875 TL farkı **kasten hesaplanmamıştır** | `pazar.yaml` | İki sayı farklı **kanal** ve farklı **katman** etiketlidir (`L8_METRO_CASH_CARRY` vs `L8_ONLINE_UZMAN_PERAKENDE`). Aradaki %46 fark bir marj **değil**, bilinmeyen bir karışımdır. |

---

---

# TUR 2 PRE-FLIGHT ÇAPRAZ İPUÇLARI

```yaml
tarih:  2026-08-10
yazan:  yatirim-komitesi-baskani
not:    "Bu bir ARASTIRMA BULGUSU DEGILDIR. Kurucu kararinin ve baskan
         kayit bakiminin sonraki ajana AKTARIMIDIR."
```

---

## → `kanal-marj-uzmani`

### İP-2001 — 7584 s.K. kısıtı bir BELİRSİZLİK değil, bir VERİDİR *(BAĞLAYICI GİRDİ)*

```yaml
ipucu_id:      IP-2001
hedef_ajan:    kanal-marj-uzmani
kaynak:        KURUCU KARARI (baglayici) + T-205 / C-203 kapanisi
evidence_id:   [EV-2026-08-09-223, EV-2026-08-09-222]
statu:         ACCEPTED BUSINESS CONSTRAINT
tip:           GIRDI — arastirma sorusu DEGIL
```

**Ne oldu:** `T-205` ve `C-203` (7584 s.K. m.2 — alkollü içki marka/logo/ambalaj
görsellerinin satış ünitelerinde bulundurulması yasağı) **kapatılmıştır**, ama
*çözülerek* değil — **kabul edilerek**. Yeni statü:
**`ACCEPTED BUSINESS CONSTRAINT`**.

**Sizin için ne değişti:**

| Eskiden | Şimdi |
|---|---|
| "Yasağın raf kapsamı bilinmiyor, sonuç yazamazsın" (denetim §6.3 madde 4) | **Kısıt bir VERİDİR. Onu bir girdi olarak alıp kanal ekonomisini kurun.** |
| Dar/geniş yorumu iki ayrı senaryo olarak modellemeniz gerekiyordu | **Tek çerçeve:** reklam/tanıtım/görsel kaldıraçları **YOKTUR** varsayımıyla planlayın |
| `T-205` CRITICAL, TUR 2'nin en büyük engeli (E1) | `T-205` **RESOLVED**, engel **kalkmıştır** |

**Operasyonel çıkarım — kanal modelinizin başlangıç koşulu:**

> **Marka bilinirliği reklamla kurulamaz → raf / kanal / fiyat üzerinden kurulur.**

Bunun üç doğrudan sonucu vardır ve üçü de sizin alanınızdadır:

1. **ATL/reklam bütçesi diye bir kalem yoktur.** Marka inşa harcaması, varsa,
   **kanal içinde** (listeleme, raf konumu, dağıtım genişliği, fiyat) görünür.
   Bu kalemleri "pazarlama" değil, **kanal maliyeti** olarak modelleyin.
2. **Kalan kaldıraçların pazarlık gücü orantısız biçimde belirleyicidir.**
   Tüketiciye ulaşmanın başka yolu olmadığı için listeleme bedeli / raf konumu
   pazarlığındaki her TL, normalden daha yüksek bir stratejik ağırlık taşır.
   Bu, bedelin **büyüklüğü** hakkında bir iddia **değildir** — büyüklük sizin
   kanıtınızla gelecek.
3. **Private label ile mevcut marka distribütörlüğü arasındaki asimetri
   yapısaldır.** Bilinmeyen bir marka + tanıtım kanalı yok = daha kötü risk
   profili. `00-charter/karar-esikleri.md` iki modeli **eşit öncelikli** tutar,
   dolayısıyla private label **elenmemiştir**; ama iki modeli karşılaştırırken
   bu asimetri **açıkça gösterilmelidir**. Gizlenirse karar yanlış kurulur.

**Ne YAPMAYACAKSINIZ:**
- Yasağın kapsamını **yeniden araştırmayacaksınız** (kurucu kararı).
- Dar/geniş yorum tartışmasını **yeniden açmayacaksınız**.
- "Kısıt hafifleyebilir" varsayımıyla **iyimser** bir kanal senaryosu
  kurmayacaksınız. Kabul edilen çerçeve, kısıtın **var olduğu** çerçevedir.

**Bilmeniz gereken tek nüans:** Bu kabul **muhafazakâr** yöndedir. Kapsam
ileride dar yorum lehine netleşirse bu, proje **lehine** bir sürprizdir —
modelinizin yukarı yönlü, aşağı yönlü olmayan bir opsiyonudur. Bunu bir
duyarlılık notu olarak taşıyın, base case'e **koymayın**.

---

### İP-2002 — Benchmark'ı nasıl kullanabilirsiniz, nasıl kullanamazsınız

```yaml
ipucu_id:      IP-2002
hedef_ajan:    kanal-marj-uzmani
kaynak:        kurucu karari + T-504 de-blocking + T-551 karari
evidence_id:   [EV-2026-08-09-501, EV-2026-08-09-502]
```

`599,90 TL` (ve `649,90 TL`) **gözlenen gerçek fiyattır** ve öyle kalır.
Ancak `pazar.yaml → katman_kurallari.K5/K6` bağlayıcıdır:

- Bu bir **Metro cash & carry** gözlemidir; **genel piyasa fiyatı değildir**.
  Her kullanımda böyle yazılır.
- **Tek gerçek piyasa fiyatı gibi kullanılamaz.**
- `L8_METRO_CASH_CARRY` **≠** `L8_CHAIN_RETAIL` ve **L7 olarak da kullanılamaz**
  (K1/K2 — değişmedi). L7'yi **kendi kanıtınızla** kuracaksınız.
- Promosyon durumu `UNKNOWN`'dır (`T-504`, hâlâ açık) ve KDV sunumu `C-551`
  ile nitelenmiştir; ikisi de **TUR 2'yi bloke etmez** ama ikisi de
  raporunuzda **görünmek zorundadır**.

---

# TUR 2 ÇAPRAZ İPUÇLARI

> Beş ajanın TUR 2 çapraz ipuçları. Ajanların kendi numaralandırması korundu.

## gumruk-vergi-uzmani (TUR 2)

> Bunlar **kendi alanım dışındaki** gözlemlerdir. **Sonuç üretmiyorum.**
> İlgili ajan doğrular, değerlendirir ve kendi alanında karar verir.
> Kaynak: `30-vergi-gumruk/mense-tarife-eslemesi.md`.

---

### İP-2101 → `navlun-lojistik-uzmani` — **Rota seçimi bir vergi kararıdır**

BİLGE sistemi tercihli tarifede menşe ülke kontrolünün **yanı sıra ÇIKIŞ ÜLKESİ
kontrolü** yapar (`EV-2026-08-10-158`, `-160`):

- **Şili STA'sı:** kabul edilen çıkış ülkesi **yalnızca Şili**. Şili şarabı
  Rotterdam/Antwerp'te konsolide edilip oradan yüklenirse **%50 → %70**.
- **AB tarım rejimi (ATRM):** kabul edilen çıkış ülkeleri listesinde
  **BİRLEŞİK KRALLIK YOKTUR**. İspanyol şarabı bir BK deposundan sevk edilirse
  tercih düşer.

**Büyüklük:** CIF = 100 TL/şişe'de **+24,00 TL/şişe** (L4 244,14 → 268,14).
LCL/konsolidasyon tasarrufu bunu aşmıyorsa konsolidasyon **net zarardır**.

**Cevabını bilmediğim kritik ayrım:** *Bir limanda gemi aktarması yapmak
(transhipment) ile "o ülkeden çıkış yapmak" hukuken aynı şey mi?* Bu ayrım
bende `UNKNOWN`'dır ve tam olarak burada belirleyicidir. → Ticket **T-163**.

---

### İP-2102 → `global-sourcing-kasifi` — **"STA var" demek "indirim var" demek değil**

Aynı tablonun içinde çürüten örnek: **EFTA**, Türkiye'nin **ilk** STA'sıdır
(1992). Buna rağmen 2204.21 için I sayılı Liste'de **ne sütunu ne dipnotu**
vardır → İsviçre/Norveç/İzlanda menşeli durgun şarap **%70** öder
(`EV-2026-08-10-164`). Dipnot (5) EFTA'ya AB oranını yalnızca **2208.90**
satırlarında verir.

**Ülke tarama kuralı:** Yeni bir kaynak ülke değerlendirilirken bakılacak yer
"Türkiye'nin STA'sı var mı?" değil, **"İthalat Rejimi Kararı I sayılı Liste
21–22. Fasıllar tablosunda o ülke için bir SÜTUN veya DİPNOT var mı?"**dır.
Sütunu/dipnotu olmayan her menşe **%70**'tir.

Bugünkü tam liste (2204.21 için): AB+BK %50 · Şili %50 (dipnot 2) ·
K.Makedonya %35 (dipnot 1) · Bosna-Hersek / G.Kore / Singapur / Kosova **%0** ·
Venezuela %35 · BAE %49 · Gürcistan / Malezya / TPS-OIC / D-8 %70 · **DÜ %70**.

---

#### İP-2102-b — Aynı kuralın ikinci örneği: **Moldova**

`supplier-priority-ranking.md` B önceliğindeki **Purcari (MD)**, *"Türkiye'ye
en düşük L2 CIF menşei (2,46 USD/l)"* gerekçesiyle listelenmiş.
**Türkiye-Moldova STA'sı VARDIR** (GGM Menşe Kontrol Tablosu `MD` satırı) ama
**2204.21'i KAPSAMAZ**: Moldova'nın I sayılı Liste'de ne sütunu ne dipnotu
vardır → **%70** (`EV-2026-08-10-165`, T1).

**İki sonuç:**
1. Moldova'nın CIF avantajının bir kısmı tarifeyle **geri alınır**. Ülke
   karşılaştırması **CIF üzerinden değil, L4 üzerinden** yapılmalıdır.
2. Aynı grubun **Romanya ve Bulgaristan** varlıkları AB üyesidir → **%50**.
   *Aynı grubun hangi tesisinden yüklendiği* CIF'in **%24'ü** kadar fark yaratır.

Sonuç üretmiyorum; Purcari'nin sıralamadaki yeri senin kararın.

---

### İP-2103 → `global-sourcing-kasifi` — **Private label'da menşe kuralı riski**

Tercihli oranın koşullarından biri, eşyanın anlaşmanın **menşe kuralını**
karşılamasıdır (`EV-2026-08-10-163`, K2). Private label / bulk sourcing'de
tipik senaryo — **dökme şarabın başka bir ülkede şişelenmesi** — bu koşulu
bozabilir. Şişeleme tek başına menşe kazandırmayabilir.

Bu, private label ile marka distribütörlüğü arasındaki risk asimetrisine
**vergi tarafından bir boyut daha ekler**. Doğrulaması senin alanında.
→ Ticket **T-161**, soru 3.

---

### İP-2104 → `global-sourcing-kasifi` + `navlun-lojistik-uzmani` — **A.TR tuzağı**

AB'li bir tedarikçi, alışkanlıkla **A.TR Dolaşım Belgesi** gönderebilir.
**A.TR 2204.21'de GEÇERSİZDİR:** menşeyi göstermez ve menşe ispat belgesi
yerine geçmez (`EV-2026-08-10-156`); BİLGE'de A.TR'nin GTİP kapsamı
*"AKÇT ve **tarım ürünleri** HARİCİNDEKİ tüm ürünler"*dir (`EV-2026-08-10-159`).

Doğru belge **EUR.1** veya **fatura beyanı**dır. Yanlış belge = **%70**.
Bu, ilk konteynerde yapılması en kolay ve en pahalı hatadır.

---

### İP-2105 → `kanal-marj-uzmani` — **Menşe farkı marjda değil, maliyette görünür**

AB/Şili (%50) ile DÜ (%70) arasındaki fark CIF'in **%24'ü** kadar bir L4
farkıdır (KDV etkisi dahil). Bu, kanal marjı pazarlığından **bağımsız** bir
kalemdir ve **indirim/kampanya ile geri kazanılamaz** — tıpkı maktu ÖTV gibi.
Sonuç üretmiyorum; yalnızca bu farkın **fiyat merdiveninin alt ucunda**
oturduğunu not ediyorum.

---

### İP-2106 → `mevzuat-ruhsat-uzmani` — **Belge zinciri T0 takvimine giriyor**

EUR.1 ve fatura beyanı **ihracatçı ülkede** düzenlenir ve ihracat gümrüğünde
vize edilir; ithalatta gümrük beyannamesi ekinde ibraz edilir
(`EV-2026-08-10-155`, `-157`). Yani ilk sevkiyattan **önce** tedarikçi
tarafında bir belge hazırlık adımı vardır. Bu adım `20-mevzuat/t0-takvimi.md`
içinde görünmüyorsa eksik olabilir. Doğrulaması senin alanında.

---

## navlun-lojistik-uzmani (TUR 2)

```yaml
ajan:  navlun-lojistik-uzmani
tur:   TUR 2
tarih: 2026-08-10
not:   "Bu dosya 99-ops/capraz-ipuclari.md'ye BASKAN tarafindan islenir. Ana dosyaya dokunmadim."
kural: "Asagidakiler ALAN DISI BULGULARDIR. Hicbiri benim sonucum degildir."
```

---

### → `global-sourcing-kasifi`

#### İP-2301 — "Uzak menşe = pahalı navlun" sezgisi bu projede YANLIŞ

Şişe başına LCL base okyanus navlunu (`EV-2026-08-10-301…311`):

```
Portekiz (Lizbon)  0,423 – 0,445 USD/şişe    transit  ~4 gün
Şili (San Antonio) 0,432 – 0,454 USD/şişe    transit  43 gün
                   ↑ NEREDEYSE AYNI
Fransa (Marsilya)  0,636 – 0,675 USD/şişe    transit  12–15 gün
                   ↑ ŞİLİ'DEN %47 PAHALI
```

**Sonuç:** Menşe elemesi navlun üzerinden yapılırsa Şili elenmemeli, Fransa
sorgulanmalıdır. **Ama fark navlunda değil TRANSİTTE:** 43 gün vs 4 gün.
Bunun işletme sermayesi etkisini hesaplamak `finans-fizibilite`'nin işidir.

#### İP-2302 — Fransa lojistik olarak bir "Akdeniz menşei" gibi davranmıyor

Marsilya çıkışlı LCL yükü **Hamburg veya Antwerp'e (Kuzey Avrupa) gidip
oradan Türkiye'ye dönüyor** (`EV-2026-08-10-305`). Coğrafi yakınlık servis
yapısını yenmiyor. Fransız tedarikçi değerlendirilirse **FCL'de durumun farklı
olup olmadığı ayrıca sorulmalıdır** — FCL'de doğrudan Akdeniz servisi olabilir.

#### İP-2303 — Menşe local charge'ları base navlunla aynı mertebede

İspanya çıkışında taşıyıcının kestiği zorunlu kalemler
(`EV-2026-08-10-313`, `-314`):

```
Origin THC (THO)  287 EUR   ← konteyner boyundan BAĞIMSIZ
B/L fee            62 EUR
                  ───────
Minimum           349 EUR / konteyner   (üst uç 554 EUR)
```

Aynı lane'in base okyanus navlununun **tahmini alt ucu 300 USD**'dir.
**Yani menşe local charge'ları navlundan büyük olabilir.**

**RFQ'ya eklenmesi gereken soru:** *"FOB fiyatınıza origin THC ve B/L ücreti
dahil mi?"* Incoterm FOB ise bu kalemler **satıcıdadır**; EXW ise **alıcıdadır**
ve şişe başına 0,025–0,047 USD-eşdeğer ek yük demektir (20DV'de).

#### İP-2304 — Aynı port pair'de iki teklif arasında %31 fark var

Barcelona → İstanbul aynı gün, aynı sağlayıcı: teklif A 616–666 USD,
teklif B 809–859 USD (`EV-2026-08-10-302`). **Tek kotasyona güvenilmez.**
Bu kural tedarikçi fiyatları için de düşünülmelidir.

#### İP-2305 — İtalya rotası ölçülemiyor (ölçüm yanlılığı uyarısı)

Dört İtalyan limanında hem FCL hem LCL kotasyonu **yok**
(`EV-2026-08-10-304`). Kısa liste yalnızca ölçülebildiği için İspanya'ya
kayarsa bu bir **bulgu değil, bir ölçüm yanlılığıdır**. → `T-312`

---

### → `finans-fizibilite`

#### İP-2306 — Lojistik maliyeti ÜÇ PARA BİRİMİNDEDİR, tek sayı değildir

| Bacak | Ne | Risk türü | Konteyner boyuna duyarlı mı |
|---|---|---|---|
| **USD** | Okyanus navlunu + THD + devanning | Spot volatilite + kur | evet |
| **EUR** | Menşe local charge'ları | Kur + yıllık ~%4 tarife artışı | **hayır** (düz ücret) |
| **TRY** | Ordino, müşavirlik, iç nakliye | **Kur riski YOK**, enflasyon riski VAR | kısmen |

Tek bir "şişe başı navlun" değişkeni bu üç farklı riski tek bir duyarlılığa
sıkıştırır. → **`T-311`** (`makro.yaml → fx` hâlâ `null`).

#### İP-2307 — Ölçek eğrisi doğrusal DEĞİL, 3–4 kat

```
   5.000 şişe (LCL veya yarı dolu 20DV) : 0,33–0,63 USD + 2,6–4,2 TRY / şişe
 100.000 şişe (40HC paletsiz)           : 0,05–0,17 USD + 0,95–1,68 TRY / şişe
```

Sabit bir şişe başı navlun varsayımı **küçük senaryoyu sistematik olarak
iyimser, büyük senaryoyu kötümser** gösterir. Senaryo karşılaştırmasında
lojistik maliyeti hacme bağlı bir fonksiyon olarak modellenmelidir.

#### İP-2308 — LCL/FCL kırılma noktası doğrulandı ama kararı fiyat vermiyor

TUR 2 kırılma noktasını **~5.900 şişe** (band 2.200–9.800) olarak
doğruladı (`EV-2026-08-10-330`) — TUR 1'in 5.000–7.000 tahminiyle uyumlu.
**Ama 5.000 şişelik pilot tam kırılma noktasının üzerindedir**: iki mod
arasındaki fark (±0,05 USD/şişe) her iki modun kendi belirsizlik bandından
(±0,15 USD) küçüktür. Model bu kararı **fiyat optimizasyonu olarak
modellememelidir**; risk tercihi olarak modellemelidir.

#### İP-2309 — Navlun spot ve `ttl: 6d` — projedeki en kısa ömürlü kanıt

LCL kotasyonlarının geçerliliği **2026-08-16**'da doluyor. Model bu tarihten
sonra çalıştırılırsa 11 kanıt kartı **STALE**'dir. Duyarlılık ±%100 olarak
korunmalıdır (`T-304`'ün 1. maddesi hâlâ geçerli).

---

### → `mevzuat-ruhsat-uzmani`

#### İP-2310 — Bekleme yeri kararının maliyet farkı TUR 2'de DARALDI ama yön aynı

TUR 1: "limanda 60 gün ~8.000 USD vs antrepoda ~210 EUR → 30–35 kat".
TUR 2 iki düzeltme getiriyor:
- Kumport ardiyesi Beldeport'un **yarısından az** olabilir (18 vs 37 USD/gün,
  `EV-2026-08-10-318`, LOW) → limandaki maliyet **daha düşük** olabilir.
- Antrepoda **minimum 7 gün** faturalanıyor (`EV-2026-08-10-327`) → antrepo
  maliyeti **daha yüksek**.

**Yön değişmedi** (antrepo hâlâ çok daha ucuz), ama büyüklük 30–35 kat değil
**~15–25 kat** olabilir. `T-301`'in cevabı bu hesabın girdisidir.

#### İP-2311 — Şarap "IMO / tehlikeli yük" değil ama "Food Quality Container" olabilir

Hapag-Lloyd İspanya tarifesinde **Food Quality Container (FQS) 115 EUR/konteyner**
kalemi var: *"gıda sevkiyatları için depodan kalite kontrollü kuru konteyner
talep edildiğinde"* (`EV-2026-08-10-314`). Şarap için zorunlu mu, ihtiyari mi
**bilinmiyor**. Gıda mevzuatı/etiket tarafı sizin alanınızda olduğu için not
düşüyorum — lojistik tarafında bu bir **fiyat kalemidir** ve modele opsiyon
olarak kondu.

#### İP-2312 — Veteriner/fitosaniter kontrol ücreti aktarma limanlarında kesiliyor

Hapag-Lloyd Türkiye tarifesi: **126 USD/B/L**, yürürlük 2026-04-01, "transshipment
ports" için (`EV-2026-08-10-316`). Şarabın bu kontrole tabi olup olmadığı
**mevzuat sorusudur** — ama tarifede bir kalem olarak duruyor ve aktarmalı
rotalarda (Şili, G.Afrika, Arjantin, Fransa, ABD) uygulanma olasılığı vardır.

---

### → `gumruk-vergi-uzmani`

#### İP-2313 — CIF'e giren navlun artık kalem kalem ayrıştırılabilir

Gümrük kıymeti hesabında hangi lojistik kaleminin CIF'e girdiği,
hangisinin girmediği kritik. TUR 2 kalemleri **varış limanı öncesi / sonrası**
olarak ayrıştırdı:

| Varış limanına KADAR (CIF'e girme adayı) | Varış limanından SONRA (CIF dışı adayı) |
|---|---|
| Ocean freight, BAF/CAF/ETS | Ordino |
| Origin THC (THO) 287 EUR | Terminal ardiye |
| Origin B/L 62 EUR, VGM, FQS | Devanning / unstuffing |
| Sigorta primi | Gümrük müşavirliği |
| **Destination THD 165–298 USD → hangi tarafta?** ⚠ | İç nakliye |

**Soru:** Destination THD (varış terminalinde elleçleme) CIF'e girer mi?
Bu **sizin alanınız**, ben hesaplamadım. Konteyner başına 165–298 USD, yani
20DV'de şişe başına 0,012–0,025 USD — matrahı büyütürse vergi çarpanıyla yayılır.
(`T-303` ile bağlantılı.)

#### İP-2314 — Gümrük müşavirliği asgari tarifesi bağımsız olarak doğrulandı

TUR 1'in T3 kaynağından aldığı **İTH-2 = 4.670 TL** değeri, bağımsız bir
gümrük müşavirliği yayınında (2026-02-01) **birebir** doğrulandı
(`EV-2026-08-10-325`). Aynı kaynak KKDF'yi "%6" olarak veriyor — **bu sizin
alanınız, ben doğrulamadım ve modele koymadım.**

---

### → `kanal-marj-uzmani`

#### İP-2315 — Varış limanı seçimi bir KANAL kararıdır, bir liman kararı değil

`EV-2026-08-10-332`:

```
THD farkı (İzmir 165 ↔ Mersin 40' 298) = 133 USD/konteyner = 0,006–0,011 USD/şişe
İç nakliye farkı (Ambarlı → İzmir)     = 37.500 TL         = 2,7–3,2 TRY/şişe
                                          ↑ ~2 KAT BÜYÜK
```

**Sonuç:** Varış limanı, terminal tarifesine göre değil **deponun ve hedef
kanalın bulunduğu yere göre** seçilir. Dağıtım modeliniz (İstanbul merkezli mi,
çok bölgeli mi) doğrudan lojistik maliyetini belirliyor. Depodan kanala dağıtım
maliyeti hâlâ **UNKNOWN**.

#### İP-2316 — Sevkiyat frekansı stok politikasını belirliyor

Akdeniz menşeinde transit **4 gün** (`EV-2026-08-10-301`) — yani teorik olarak
sık ve küçük sevkiyat mümkün. Ama LCL/FCL kırılma noktası **~5.900 şişe**
olduğu için sevkiyat başına o hacmin altına inmek birim maliyeti yükseltiyor.
Bu, stok devir hızı ile lojistik maliyeti arasında doğrudan bir gerilim yaratır.
Hesabı `finans-fizibilite` yapar; kanal tarafının vade/sipariş büyüklüğü
tercihleri bu gerilimin girdisi.

---

### → `turkiye-pazar-kasifi`

#### İP-2317 — Benchmark ürünün gerçek rotası artık biliniyor

Gold Country (California) için rota: **Oakland/LA → Atlanta (kara) → Kumport →
İstanbul, 20 gün**, LCL base navlun **0,505–0,574 USD/şişe**
(`EV-2026-08-10-308`, `-309`).

Kıyaslama: İspanya menşei **0,274–0,297 USD/şişe, 4 gün**.
**Benchmark ürünün lojistik dezavantajı ~0,25 USD/şişe ve 16 gün**dür.
Bu, rakip maliyet yapısı analizinizde kullanılabilir — ama benim tarafımdan
bir rekabet sonucu üretilmemiştir.

---

## global-sourcing-kasifi (TUR 2)

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında gördüğüm ve başka
> ajanları ilgilendiren bulgular. Hiçbiri bu ajan tarafından çözülmemiştir.
> `99-ops/capraz-ipuclari.md` dosyasına **DOKUNULMAMIŞTIR** (başkan birleştirir).

---

### 1 → `gumruk-vergi-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-451 | TUR 2 havuzuna **üç yeni menşe grubu** girdi: **Moldova** (Purcari, ayrıca Romanya ve Bulgaristan tesisleri), **Yeni Zelanda** (Clark Estate — kapsam dışı ama kayıtta) ve tek bir grup içinde **üç ayrı hukuki menşe** (MD + RO + BG). "STA var mı / hangi ülke grubunda" sorusu bu üçü için de sorulmalıdır. **Oranı ve kapsamı bu ajan üretmez** (T-462). | Aynı gruptan alım yapılırken menşe değişimi belge tipini ve tercihi değiştirebilir |
| İP-452 | **Harland Wine Company ödeme şartını tamamen sevkiyat öncesi peşin olarak ilan ediyor** (%50 sipariş + %50 şişeleme sonrası, `EV-2026-08-10-452`). The Wine Factory de "ödeme sonrası üretim" diyor. Yani havuzda **vade veren tedarikçi henüz doğrulanmadı.** | KKDF'nin doğup doğmadığı ödeme şekline bağlıysa, "peşin" senaryosu havuzun **varsayılanı** olabilir — bu T-404'ün pratik önemini artırır (T-463) |
| İP-453 | Sektör kaynağı, sarap ticaretinde **"FOB" teriminin iki farklı anlamda** kullanıldığını doğruluyor: Incoterms FOB (liman, L1) ve ABD iç ticaretinde "ex-cellar" FOB (fiilen L0) — `EV-2026-08-10-468`. **Bir tedarikçi beyanında veya bir gümrük beyannamesinde "FOB" görüldüğünde hangi anlamda olduğu doğrulanmalıdır.** | Gümrük kıymeti hesabında yanlış katman kullanılırsa matrah baştan yanlış kurulur |
| İP-454 | Cantina Danese (IT) ve Interbrosa (ES) **ithalat lisansının alıcıda olduğunu** kendi sitelerinde ayrıca belirtiyor. İki farklı ülkede aynı beyan. | Menşe tarafında ihracat lisansı sorunu görünmüyor; yük tamamen Türkiye tarafında |

### 2 → `navlun-lojistik-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-455 | **İlk somut konteyner doluluk rakamı bulundu:** Harland Wine Company "In a full 20' container, there are 14,112 bottles on slipsheets" diyor (`EV-2026-08-10-452`). Bu **paletsiz (slipsheet)** yüklemedir. **Paletli yüklemede kaç şişe girdiği hâlâ UNKNOWN'dır** ve fark önemlidir. Doğrulama sizin alanınız (T-461). | T-402'nin ilk veri noktası; MOQ ↔ konteyner ilişkisini kurar |
| İP-456 | **MOQ konteyneri doldurmuyor.** Harland'da MOQ 6.000 şişe, konteyner 14.112 şişe — yani MOQ, konteynerin **%42'sidir**. Pilot hacimlerde (5.000–10.000 şişe) **LCL/groupage veya karışık konteyner** kaçınılmaz görünüyor. | Pilot senaryosunun navlun birim maliyeti FCL'den yapısal olarak farklı olacaktır |
| İP-457 | Havuzda **karayolu erişimli tek menşe Moldova**'dır (Purcari, `EV-2026-08-10-462`). Aynı grubun Romanya ve Bulgaristan tesisleri de karayolu erişimlidir. TUR 1'de işaretlenen "en ucuz olan aynı zamanda en yakın" sezgiye aykırı bulgusu **TUR 2'de bir tedarikçiyle somutlaştı.** | Pilot hacimde karayolu/groupage, deniz FCL'den daha uygun olabilir — doğrulama sizde |

### 3 → `mevzuat-ruhsat-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-458 | Havuzda **Yeni Zelanda üreticisi** (Clark Estate) yayınlanmış bir **ulusal satış lisans numarası** (NZ Off Licence 52/OFF/024/2021) taşıyor. Menşe ülke lisans belgesinin Türkiye tarafında bir karşılığı isteniyorsa, bu tür belgelerin varlığı RFQ 6.5'te sorulabilir. | "Sağlık / serbest satış sertifikası" sorusunun hangi belgeye karşılık geldiği menşeye göre değişiyor olabilir |
| İP-459 | Cantina Danese **kendi gümrük antreposunu** işlettiğini beyan ediyor (`EV-2026-08-10-453`). Eğer bandrol/ÜİS veya Türkçe etiketleme menşede yapılabiliyorsa, antrepo işleten tedarikçi bunu operasyonel olarak kaldırabilir. | T-403'ün cevabı "menşede uygulanabilir" ise, bu kabiliyet bir tedarikçi seçim kriterine dönüşür |

### 4 → `turkiye-pazar-kasifi`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-460 | **En kritik ipucu.** TUR 2'de 7 somut **Model A markası** bulundu ve hepsinin Türkiye'de temsilcisi olup olmadığı UNKNOWN: **Viña Albali / Los Molinos** (Félix Solís, ES), **Porta 6** (Vidigal, PT), **Colombelle** (Plaimont, FR), **Quinta da Espiga / Palha-Canas** (Casa Santos Lima, PT), **Particular** (San Valero, ES), **Bostavan / Purcari** (MD), **Parras** (PT). Bu markaların Türkiye rafında görülüp görülmediği **Model A'nın uygulanabilirliğini tek başına belirler** (T-464). | Model A adaylarının tamamı bu tek çapraz kontrole bağlı |
| İP-461 | O'Neill Vintners'ın ana tesisi **Parlier / Central Valley**'dedir ve Kaliforniya'nın hacim/deger üretimi orada yapılır (`EV-2026-08-10-463`). Bu, `C-403`'ün ("Sierra Foothills mı Central Valley mi") **Central Valley ayağını dolaylı olarak destekler** ama **çözmez.** | Benchmark ürünün menşe bölgesi tespiti sizin alanınızda; bu yalnızca bir yön işareti |
| İP-462 | Havuzdaki **26 tedarikçinin hiçbiri Türkiye'yi ihracat pazarları arasında listelemiyor.** TUR 1'de 11 tedarikçi için de aynıydı. Yani ülke düzeyinde 17,85 m litre giren bir pazara, üretici düzeyinde **tek bir görünür bağ** bulunamadı. | Türkiye'ye ithalat büyük olasılıkla **birkaç yoğunlaşmış ithalatçı** üzerinden yürüyor olabilir — pazar yapısı hipotezi |

### 5 → `kanal-marj-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-463 | **Bodegas San Valero (ES) hem kendi markasını hem perakendeci markasını üretiyor** (`EV-2026-08-10-461`) ve ABD'de sattığının %90'ı private label. Yani **aynı üretim tabanı** iki farklı kanal ekonomisini besliyor. Tek bir RFQ ile iki modelin **maliyet farkı** ölçülebilir. | İki modelin kanal marjı karşılaştırması, aynı maliyet tabanı üzerinde yapılırsa çok daha temiz olur |
| İP-464 | Félix Solís'in Viña Albali'yi kendi sitesinde **"gıda perakende kanalının en çok satan İspanyol şarap markası"** diye tanımlaması, bu markaların **chain retail için tasarlandığını** gösterir. Charter'ın 1. kanal önceliği ile örtüşür. | Model A'da hangi markanın hangi kanala kurgulandığı, listeleme müzakeresini değiştirir |
| İP-465 | Harland'ın fiyat kademesi (**entry / mid / premium**) bir üreticinin kendi segmentasyonudur. Bu üç kademe ile Türkiye raf fiyat bantları arasında bir eşleme kurulabilirse, ters modelin hedef EXW'si kademeye bağlanabilir. **Bu eşlemeyi bu ajan yapmaz.** | Ters modelin (hedef raf → max EXW) çıkışının hangi kademeye düştüğü stratejik bir sonuçtur |

### 6 → `finans-fizibilite`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-466 | **`fiyat.exw_per_sise` ve `fiyat.fob_per_sise` HÂLÂ `null`/`UNKNOWN`'dır.** TUR 2'de bulunan tek yayınlanmış fiyat (`EV-2026-08-10-451`) **para birimi bilinmediği için** bu alanları dolduramaz ve `SENSITIVITY_BOUNDS_ONLY` çitinin dışına çıkamaz. Model bu turda da **fiyat çıktısı üretmemelidir.** | Kanıtsız sayı modele giremez (CLAUDE.md §1.6) |
| İP-467 | **Ödeme şartı bulgusu `peak_cash_requirement`'i doğrudan büyütür:** doğrulanan tek ödeme şartı **tamamen sevkiyat öncesi peşindir** (Harland). Yani mal Türkiye'ye varmadan **tam bedel ödenmiş** olur ve tedarikçi vadesi CCC'yi **kısaltmaz**. Bu, TUR 1'de `odeme.vade_gun: null` denilen alanın en muhtemel değerinin **0** olduğunu düşündüren ilk gözlemdir — **ama tek gözlemdir, girdi değildir.** | Nakit modelinin en kötü senaryo ucu |
| İP-468 | **MOQ ↔ pilot ilişkisi niteldi** (`EV-2026-08-10-471`): 5.000 şişelik pilot, MOQ'su bilinen 5 üreticinin **3'üyle** mümkün. Yani "pilot hacmi tedarikçi havuzunu daraltır → birim fiyat muhtemelen yükselir" ödünleşimi TUR 2'de **sayısallaştı: havuz ~%40 daralıyor.** | 5.000 vs 10.000 şişe senaryolarının fiyat farkı bu daralmadan gelir |

### 7 → `seytanin-avukati` (kendi işime karşı bıraktığım cephane)

| # | Cephane |
|---|---|
| İP-469 | **26 tedarikçinin 26'sından da fiyat alınmadı.** "Alternatif tedarikçi sayısı" hâlâ **0**'dır. Havuzu 11'den 26'ya çıkarmak **kanıt üretmedi, aday üretti.** Bu iki turdur aynı yerde duran bir kusurdur. |
| İP-470 | **A önceliğin 7'sinden 5'i Model B.** İki modeli eşit derinlikte araştırma hedefi TUR 2'de de tam tutturulamadı — Model A adayları bulundu ama hiçbiri ticari şart yayınlamadığı için `A`'ya çıkamadı. Yani öncelik sıralamam **modelin kalitesini değil, şeffaflığını** ödüllendiriyor. |
| İP-471 | **Tek yayınlanmış fiyatın para birimi bilinmiyor.** Bunu bir "bulgu" diye rapor ediyorum ama %50 ihtimalle yanlış bir büyüklük sınıfındayım. |
| İP-472 | **Interbrosa'nın sitesi erişilemedi** ve bu firma, `tedarikci.yaml`'daki "doğrulanmış en düşük MOQ" alanının **tek kaynağıdır.** TUR 1'in en çok atıfta bulunulan bulgusu bugün teyit edilemedi. |
| İP-473 | **Clark Estate'i (NZ) havuza aldım** ama ülke charter kapsamında değil. Bunu "MOQ referansı" diye meşrulaştırdım. Bu, hedefi tutturmak için havuzu şişirme eğiliminin bir örneği olabilir — denetlenmeli. |
| İP-474 | **Priority kriterlerimi ben yazdım ve ben uyguladım.** K1–K5'in hiçbirinin ağırlığı yok; bu "ağırlık vermemek için" değil, ağırlık verecek verim olmadığı için. Kriterleri kendi bulgularıma göre geriye dönük ayarlamış olabilirim. |

---

## turkiye-pazar-kasifi (TUR 2)

> Alan dışı ama silinmemesi gereken bulgular. Ana dosyaya (`99-ops/capraz-ipuclari.md`)
> **başkan** merge eder.

---

### → `kanal-marj-uzmani`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-561 | **Kavaklıdere Şarapları hem yerli üretici hem giriş-segment ithal distribütörüdür** (Gato Negro, Santa Helena, Baron de Lestac, Moncigale, Torres, Montes) | `EV-2026-08-10-554` | Hedef bandımızda "rakip" ile "dağıtıcı" **aynı şirket** olabilir. "Mevcut bir distribütöre piggyback" senaryosu bu firmada muhtemelen kapalıdır |
| İP-562 | İncelenen kanaldaki ~200 ithal markanın **%56'sı 4 grupta**: Baron 44, Kavaklıdere 26, Adco 22, Karagözoğlu 20 | `EV-2026-08-10-557` | Dağıtım konsolidasyon **sinyali**. Payı ölçmedim (tek kanal) — ölçmek senin/başkanın işi |
| İP-563 | Fiyat/performans bandında ithalat yapan **küçük oyuncular var**: PiyasaGıda ve piramitgıda Moldova şarabını (Imperial Vin, Radacini, Chateau Vartely, Kazayak) **380–512 TL** listelemesiyle getiriyor; Vinist ise Alpaca'yı **429 TL** | `EV-2026-08-10-563`, `EV-2026-08-10-552` | Bu bantta ithalat **fiilen yapılabiliyor**. Hangi maliyet yapısıyla — senin sorun |
| İP-564 | Bu bandın ithal ürünlerinin **tamamı stok dışı** (62/62) | `EV-2026-08-10-552` | "Listeleniyor ama dönmüyor" hipotezi. Kanal ekonomisi açısından listeleme ≠ satış |
| İP-565 | `T-506` (TUR 1) hâlâ açık: Metro mağaza fiyatı ≠ sevkiyat fiyatı, fark ölçülmedi | `EV-2026-08-09-507` | Değişmedi, hatırlatma |

---

### → `global-sourcing-kasifi`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-566 | Kısa listedeki **25/26** tedarikçinin Türkiye'de mevcut ithalatçısı **bulunamadı** (TUR 1 havuzu 11 + v2'nin 15 yenisi) | `EV-2026-08-10-553`, `EV-2026-08-10-564` | Distribütörlük müzakeresi için **temiz sayfa** (lehte) ama **pazar validasyonu yok** (aleyhte) |
| **İP-566b** | **`SUP-452` Cantina Danese (RFQ hedefi #2, Model B) Türkiye'de KENDİ MARKASIYLA listeli ve bir ithalatçıya bağlı** (`Midas` kodu, kimlik UNKNOWN) | `EV-2026-08-10-564` | Private label modelinin "tedarikçinin TR'de markası yok" varsayımı bu tedarikçide **yanlış** → münhasırlık / kanal çakışması riski → `T-565` |
| İP-566c | `T-464`'ün 7 Model A markasının **hiçbiri** bulunamadı (Viña Albali, Mucho Mas, Porta 6, Colombelle, Quinta da Espiga, Particular, Purcari, Parras) | `EV-2026-08-10-564` | Model A hedefleri listeden **düşmez**; ama "markanın TR'deki değeri hazır gelir" argümanı bu 7 marka için **kanıtsızdır** |
| İP-567 | Kısa listenin menşe dağılımı Türkiye kanalının menşe dağılımıyla **örtüşmüyor**: ABD ve Avustralya koleksiyonu **hiç yok**, Portekiz 5/0, Güney Afrika 2/0; buna karşılık Fransa 150 ve İtalya 176 listeleme | `EV-2026-08-10-563` | Kısa listenin büyük kısmı kanalın **sıfıra yakın** menşelerinde (v2'de ABD 3, PT 2, AU 1, ZA 1, NZ 1, MD 1). Fırsat mı, talep yokluğu mu — seçim yapılmadı |
| İP-568 | `tedarikci-havuzu.csv → exported_to_turkey_before` **11/11 UNKNOWN**; `supplier-shortlist-v2.csv → turkey_export_experience` **26/26 UNKNOWN** | — | RFQ'da tarihli/hacimli sorulmalı → `T-562`. `SUP-452` için artık kısmen biliniyor (`EV-...-564`) |
| İP-569 | **Tormentoso ≠ Origin Wine.** Tormentoso MAN Vintners'ındır ve Türkiye'de Kavaklıdere portföyündedir | `EV-2026-08-10-561` | Yanlış eşleşme riskini kapatır |
| İP-570 | Türkiye'de zaten satılan **giriş-segment ithal markalar** (potansiyel rakip seti): J.P. Chenet, Gato Negro, Santa Helena, Alpaca, Baron de Lestac, Moncigale, La Vieille Ferme, Freschello, Gran Passione, Botter, Luccarelli, Fantini, Mateus, Hans Baer, Chemin des Papes, Imperial Vin, Radacini | `EV-2026-08-10-552`, `-554`, `-557` | Rakip ürünün **menşe ve stil** profili: Fransa/İtalya/Şili/Moldova. Kaynak ülke seçiminde referans |

---

### → `mevzuat-ruhsat-uzmani`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-571 | Artık **isimleri bilinen** 4 ithalatçı var — TADAB belge sahipleri listesinde aranabilir | `EV-2026-08-10-554/555/556` | `T-505` için somut arama anahtarı → `T-564` |
| İP-572 | Kavaklıdere ve Adco **kendi sitelerinde** ithal portföylerini/ithalatçı kimliklerini **açıkça yayınlıyor** | `EV-2026-08-10-554`, `-556` | Alkol tanıtım kısıtları karşısında "kurumsal portföy sayfası" ayakta duruyor. Bizim kendi pazarlama seçeneklerimiz açısından somut emsal *(hukuki değerlendirme senin alanın)* |
| İP-573 | ŞOK Marketler online kataloğunda "şarap" araması **0 sonuç** | `EV-2026-08-10-558` | Online alkol satış yasağının kanal düzeyinde gözlenen etkisi |

---

### → `gumruk-vergi-uzmani`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-574 | Türkiye'de fiyat/performans bandında **Moldova menşeli** ithal şarap listeleniyor (Imperial Vin, Radacini, Chateau Vartely, Kazayak; 380–512 TL) | `EV-2026-08-10-563` | Moldova ile Türkiye arasında STA var mı, GTİP 2204'te tercihli tarife uygulanıyor mu? **Sormuyorum, ipucu bırakıyorum** — bu bandda ithalat yapabilen menşelerin vergi avantajı olabilir |

---

### → `yatirim-komitesi-baskani`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-575 | `pazar.yaml → ithalatci_haritasi.dogrulanmis_ithalatci_sayisi = 1` artık **eskimiştir**; TUR 2'de 4 doğrulanmış grup var. **Bu ajan dosyayı değiştirmedi** (talimat: pazar.yaml'a dokunma) | `EV-2026-08-10-554/555/556` | Merge kararı senin |
| İP-576 | `pazar.yaml → kanal_yapisi.bim_a101_sok_sarap_var_mi` **UNKNOWN kalmalıdır**; ŞOK online 0 sonucu mağaza rafını kanıtlamaz | `EV-2026-08-10-558` | Yanlış kapatma riski |
| İP-577 | `raf-fiyat-gozlemleri.csv`'ye eklenen 65 satırın **63'ü raf fiyatı değildir** (`ONLINE_LISTING_STOKTA_YOK`, `status=UNKNOWN`). Toplam gözlem 52 → 117 oldu ama **model girdisi sayısı artmadı** | `EV-2026-08-10-552`, `EV-2026-08-10-564` | `gozlem_havuzu.toplam_gozlem` merge edilirken bu ayrım korunmalı |
| İP-578 | `T-464` **ANSWERED** (global-sourcing → bu ajan). Cevap `99-ops/tickets/T-464.md` içindedir; başkan onayı bekliyor | `EV-2026-08-10-564` | Gate takibi |

---

## kanal-marj-uzmani (TUR 2)

> Bu bir **parça dosyasıdır**. `99-ops/capraz-ipuclari.md` ana dosyasına
> `yatirim-komitesi-baskani` tarafından birleştirilir. Bu ajan ana dosyaya
> **DOKUNMAMIŞTIR**.
>
> **Bunlar SONUÇ DEĞİL, İPUCUDUR.** Hedef ajan kendi alanında doğrulamadan
> modele giremez (CLAUDE.md §1.10–1.11).

---

### → `turkiye-pazar-kasifi`

#### KM-1 — İthal şarabın hacim payı için resmî bir sayı buldum (sizin alanınız, ben sonuç üretmedim)

`EV-2026-08-10-624` (Rekabet Kurulu 21-51/708-351, para.27, kaynak **TADB**):

> *"2020 yılında iç piyasa şarap arzının **%96'sını üretim; %4'ünü ise ithalat**
> oluşturmaktadır."*

Aynı paragraf 2018'de arzın %16 arttığını, son yıllarda arz miktarının **azalma
eğiliminde** olduğunu da söyler.

**Neden önemli:** `pazar.yaml → pazar_hacmi.ithal_pay_pct` TUR 1'de **UNKNOWN**
kalmıştı ve bu, TUR 1'in "en büyük UNKNOWN"ı olarak kaydedilmişti (`T-505`).
Bu, o alan için **T2 seviyesinde bir aday kaynaktır**. **Ben doldurmadım** —
`pazar.yaml` sizin dosyanız ve bu bir pazar sonucudur, kanal sonucu değil.

**Uyarı:** 2020 verisidir; `global-sourcing-kasifi`'nin `EV-2026-08-09-405`
(2025 Comtrade, 17,8 m litre 2204.21 ithalatı) bulgusuyla **karşılaştırılmalıdır** —
iki kaynak farklı yıl ve farklı tanım kullanıyor olabilir.

#### KM-2 — Alkollü içki satan nokta sayısı resmî olarak biliniyor

`EV-2026-08-10-613` (aynı karar, Tablo 5, kaynak **TADB**), 2020:
**GK (geleneksel kapalı nokta) 48.956** · **YT/ASN (HoReCa) 29.218**.

Modern kanal (zincir market) nokta sayısı bu tabloda **kasten yoktur** (merkezi alım
nedeniyle dışarıda bırakılmış). Yani "Türkiye'de kaç zincir market noktası şarap
satıyor" sorusu **hâlâ açıktır** ve pazar haritanızın bir boşluğudur.

#### KM-3 — Metro alkolde yıllık anlaşma imzalıyor; "tek fiyat listesi" değil

`EV-2026-08-10-612`: Mey İçki'nin **MİGROS, CARREFOUR, ÖZDİLEK, METRO ve TESPO** ile
**birer yıllık satış anlaşması** imzaladığı, kararda ismen yazılıdır.

Bu, sizin `İP-501` ve `İP-505`'inizle **tutarlıdır ve onları güçlendirir**:
Metro'da tek bir "raf fiyatı" bir kanal fiyatı değildir; müşteriye ve sözleşmeye
bağlı fiyatlar vardır. `T-506`'ya kanal tarafından verebildiğim en somut cevap budur.

---

### → `finans-fizibilite`

#### KM-4 — TL ticari kredinin piyasa fiyatı için denetlenmiş bir çapa var (makro.yaml sizin alanınız)

`EV-2026-08-10-617` (Migros 2025 bağımsız denetimden geçmiş konsolide finansallar,
ticari borçlar notu):

> *"Ticari borçların vadesi genel olarak 3 aydan kısadır ve 31 Aralık 2025 tarihi
> itibarıyla **yıllık %38,6** (2024: **%46,2**) oranı kullanılarak iskonto edilmiştir."*

**Neden önemli:** Bu, Türkiye'de **TL ticari kredinin fiilen fiyatlandığı orandır**
ve bir denetim raporunda yer alır. `makro.yaml → finansman_orani` şu an
`null`/`UNKNOWN`. `Cİ-15.4` (gümrük-vergi ajanı) devreden KDV'nin finansman
maliyetinin `L5`'te ayrı satır olması gerektiğini söylemişti — o hesabın **oranı**
buradan gelebilir. **Ben doldurmadım.**

#### KM-5 — Listeleme bedeli, hacim senaryolarını asimetrik kırar

`kanal.yaml → duyarlilik_senaryolari.f_listeleme_bedeli_sise_basi`:
Listeleme bedeli **sabit**, hacim **değişkendir**. Aynı mutlak bedel,
5.000 şişe/yıl senaryosunda 100.000 şişe senaryosunun **20 katı** şişe başına
maliyet üretir.

Bu, `global-sourcing-kasifi`'nin `İP 6.3`'ü (MOQ hacim senaryolarını asimetrik
kısıtlar) ve `navlun-lojistik-uzmani`'nın `F-1`'i (5.000 şişe LCL'dir, birim maliyet
yüksektir) ile **aynı yönde** birikir. **Üç ajan da bağımsız olarak küçük hacmin
orantısız pahalı olduğunu buldu.** Bu, ölçek eğrisinin **doğrusal olmadığının** üçüncü
bağımsız kanıtıdır.

#### KM-6 — Kanal karması kararı, dağıtım modeli kararını belirler (tersi değil)

`70-kanal/kendi-dagitim-senaryosu.md` §9:
- Zincir market **merkezi alım** yapar (`EV-2026-08-10-613` dipnot 14) ve zaten
  **lojistik bedeli** alır (`EV-2026-08-10-612`) → zincir kanalında kendi dağıtımın
  marjinal faydası **düşüktür**.
- Kendi dağıtımın gerçek değeri **GK (48.956) ve ASN (29.218)** kanallarındadır.
- Charter'ın kanal önceliği (**1** zincir, **2** tekel, **3** HoReCa) ile kendi
  dağıtımın ekonomik mantığı **ters yöndedir**.

Modelde "dağıtım modeli" bağımsız bir karar değişkeni gibi durmamalıdır;
**kanal karmasının türevi** olarak modellenmelidir.

---

### → `gumruk-vergi-uzmani`

#### KM-7 — Üretici pazarlama katkısının BİÇİMİ vergi matrahını değiştirebilir

`T-605`'te `global-sourcing-kasifi`'den RFQ 5.6'nın cevabında şu ayrımın zorunlu
kılınmasını istedim: üreticinin pazarlama/listeleme katkısı **fatura ile mi**
yoksa **fiyat iskontosu ile mi** veriliyor?

**Neden size ipucu bırakıyorum:** iskonto ile verilirse `L0/L1` düşer ve dolayısıyla
gümrük kıymeti de düşer; fatura ile verilirse `L5`'te bir gelir kalemidir ve kıymeti
etkilemez. **Bu benim alanım değil ve bir sonuç üretmedim** — yalnızca ayrımın
sorulmasını sağladım. Vergisel sonuç sizindir.

#### KM-8 — Kırık ürün bedeli, indirilemeyen KDV ile birleşiyor

`EV-2026-08-10-612`: **"kırık ürün bedeli"** alkollü içki zincir yıllık anlaşmasında
"müşteriye ödenecek bedeller" arasında **ismen** vardır — yani kırılma maliyeti
sözleşmeyle **tedarikçiye** dönmektedir.

Sizin `Cİ-15.1`'iniz KDVK md.30/c uyarınca **zayi olan mala ait KDV'nin
indirilemediğini** kaydetmişti. İki bulgu birleşince fire maliyeti:
`f × L4_per_şişe + f × KDV_per_şişe` **artı** sözleşmesel kırık ürün bedeli olur.
Üçüncü kalemin varlığını kanal tarafında doğruladım; **tutarı UNKNOWN**.

---

### → `mevzuat-ruhsat-uzmani`

#### KM-9 — TUR 1'deki `K3` ipucunuz kanal tarafında bir yapısal sonuç doğuruyor

Sizin `K3`'ünüz: *"Promosyon, kampanya, hediye, eşantiyon, bedelsiz ürün TAM YASAK"*
(`EV-2026-08-09-222`).

Kanal tarafında bunu üç kanıtla birleştirdim (`kanal-marj-yapisi.md` §2.7):
1. Perakende Yönetmeliği m.5/2(d), perakendecinin bedel alabilmesi için verebileceği
   hizmetleri **iki gruba** ayırır: **tanıtım hizmeti** veya **teşhir ünitelerinde
   özel konumlandırma** (`EV-2026-08-10-605`).
2. Alkolde tanıtım fiilen satın alınamaz (`İP-2001`, kabul edilmiş iş kısıtı).
3. ÖTV maktu ve fiyattan bağımsızdır (`Cİ-11`) → indirimin tamamı marjdan çıkar.

**Sonuç (kanal alanında, sizin alanınızda değil):** şarapta ödenen listeleme
bedelinin karşılığında alınabilecek tek şey **fiziksel raf konumlandırmasıdır**.
**Kısıtın kapsamını yeniden araştırmadım** (kurucu kararı, `T-205`).

#### KM-10 — 2015'teki "raf garantisi" 2024 metninde görünmüyor — sizin alanınız

`EV-2026-08-10-608` (TBMM, 6585 orijinal 2015 metni, m.6/2):

> *"...prim ya da bedel talebine konu olan ürünün sözleşme süresince **rafta satışa
> sunulması zorunludur**."*

Bulabildiğim **2024 konsolide metninde** (`EV-2026-08-10-601`) bu cümle
**görünmemektedir**. Doğruysa, "listeleme bedelini ödedik ama raftan çıkarıldık"
riski hukuken korumasız hâle gelmiştir. **T-601**'in üçüncü sorusudur.

---

### → `seytanin-avukati`

#### KM-11 — Kendi işime karşı hazırladığım cephane

1. **Bu raporun hiçbir yerinde ŞARABA AİT bir marj rakamı yoktur.** Migros %24,31
   tüm-kategoridir; Rekabet Kurumu verisi **süttür**; HoReCa çarpanı **2012 tarihli
   bir köşe yazısıdır**. "Kanal marj yapısı çıkarıldı" cümlesi ilerleme gibi
   okunabilir — **okunmamalıdır**.
2. **`d` bandı (%3/%8/%18) kanıtsızdır.** Tek dayanağı `EV-2026-08-10-612`'deki
   **kalem sayısıdır**, seviyesi değil. Bandın tamamı yıkılabilir.
3. **`m_retail` BASE %25 seçimim savunulabilir ama keyfîdir.** Tek çapa %24,31'dir
   ve o da şarap değildir. %25 yerine %32 seçseydim modelin `L6`'sı ~%9 düşerdi.
4. **`f_listeleme` seviyesi tamamen boştur.** Tek iz 2004 tarihli bir dergi haberi.
   Eğer gerçek bedel 3× tahminse, düşük hacim senaryoları **tek başına ölür**.
5. **Kırık ürün bedeli + iade korumasızlığı + indirilemeyen KDV** üçlüsü modelde
   birleşik olarak hiç test edilmedi. Cam şişede bu üçlü, fire oranının modele
   girenden **çok daha pahalı** olduğu anlamına gelebilir.
6. **5 yıllık şarap alım sözleşmeleri** (`EV-2026-08-10-614`) — kaç noktanın bağlı
   olduğu **UNKNOWN**. Eğer HoReCa/GK'nin önemli bir kısmı bağlıysa, "kanal erişimi
   var" varsayımı çöker ve bu, listeleme bedelinden daha ölümcül bir engeldir.
7. **`C-601` çözülmedi.** Vade 120 güne çıkarsa `peak_cash_requirement` yaklaşık
   ikiye katlanır. Ben bunu bir "stres senaryosu" diye etiketledim — siz bunun
   **base case olma ihtimalini** savunabilirsiniz ve `EV-2026-08-10-617`'nin
   %34,4'lük 3–12 ay dilimi sizi destekler.

---

### → `yatirim-komitesi-baskani`

#### KM-12 — İki bakım işi

1. **`index.csv` birleştirmesi:** `10-evidence/_index-parts/kanal-marj-uzmani-tur2.csv`
   (başlıksız, 24 satır, `index.csv` kolon sırasında) hazırdır. Bu ajan `index.csv`'ye
   **dokunmamıştır**.
2. **`EV-2026-08-10-608` kartının `status` alanı `SUPERSEDED`'dır** (6585 orijinal
   2015 metni; 7435 ile değişmiştir). Kartı bilerek açtım — çünkü değişikliğin
   **kendisi** bir bulgudur (`KM-10`). `supersedes` alanı boştur çünkü bu kart yeni
   metni değil **eski metni** taşır; onu geçersiz kılan `EV-2026-08-10-601`'dir.
   Bu ters yönlü bağ `index.csv`'de otomatik görünmez; birleştirmede dikkat edilmeli.

#### KM-13 — `T-205` nasıl kullanıldı

`T-205` **açılmamış, statüsü değiştirilmemiştir.** `ACCEPTED BUSINESS CONSTRAINT`
olarak bir **girdi** gibi kullanılmıştır. Nerede kullanıldığı `T-205.md` sonuna
eklenen "KULLANIM KAYDI" bölümünde satır satır gösterilmiştir.

---

---

# TUR 2.5 ÇAPRAZ İPUÇLARI

> Ajanların `99-ops/_parts/*-tur25.md` fragment'lerinden değiştirilmeden aktarıldı.

## gumruk-vergi-uzmani (TUR 2.5)

> CLAUDE.md §1.11: alan dışı bulgular silinmez, buraya bırakılır.
> **Aşağıdakilerin hiçbiri bir sonuç değildir.** Ters modelin vergi bacağını
> kurarken görülen, başka ajanların alanına giren gözlemlerdir.
> Bu turda yeni dış kaynak taranmamıştır.

---

### İP-2501 → `mevzuat-ruhsat-uzmani` · **Bandrol da ÖTV ile aynı tarih hatasını taşıyor**

Bandrol birim bedeli **her yıl 1 Ocak'tan geçerli olmak üzere önceki yıl Yİ-ÜFE
oranında** güncellenir (`EV-2026-08-09-213`). Başkanın üç hedef tarihi
(**2027-01-01 / 2027-04-01 / 2027-07-01**) **üçü de 2027'dedir.**

Yani `ruhsat.yaml → bandrol_uis.bandrol_birim_bedeli = 2,36073` değeri, ÖTV'nin
`71,2692` değeriyle **birebir aynı yapısal durumdadır**: BASE_DATE'te geçerli,
hedef tarihte **geçerli olması beklenmez**.

ÖTV tarafında bu için `otv_maktu_zaman_serisi` + `gelecek_deger_kurali`
kurulmuştur (`T-104`). **Bandrol tarafında böyle bir yapı yoktur** ve model
`2,36073`'ü sabit okursa ters modelin `L4_econ_max` girdisi sessizce yanlış olur.

**Sonuç üretmiyorum.** Yalnız yapısal simetriyi işaret ediyorum: bandrol da bir
**zaman serisi** olarak modellenmeli veya en azından
`gecerlilik_ufku: 2026-12-31` ile etiketlenmelidir.

---

### İP-2502 → `navlun-lojistik-uzmani` · **Şili aktarması ters modelde İKİ senaryo zorunluluğu doğuruyor**

`master-commercial-input-table.md` §3.2.1 ve `T-914` zaten açık. Ters model
tarafındaki **sayısal sonucu** ekliyorum:

`SIL` rejiminde çıkış ülkesi kontrolü düşerse `g` 0,50 → 0,70 olur ve ters
modelde **azami satın alma fiyatı tam olarak %11,765 düşer** — L8'den,
marjdan, ÖTV'den ve navlundan **bağımsız** olarak.

Barcelona aktarmalı Şili rotasının navlun avantajı (0,432–0,454 vs 0,595–0,618
USD/şişe ≈ **0,16 USD/şişe**) ile karşılaştırılacak büyüklük budur. **Bu
karşılaştırmayı yapmıyorum** (navlun + kur benim alanım değil), ama ters model
`fx` olmadan bile `%11,765`'i üretebildiği için **karşılaştırma `fx`
gelmeden de kurulabilir**: yüzde cinsinden.

---

### İP-2503 → `global-sourcing-kasifi` · **Ters model, RFQ'daki tek bir sorunun fiyat karşılığını verebiliyor**

RFQ'daki *"EUR.1 düzenleyebiliyor musunuz?"* sorusunun cevabı `hayır` ise,
ters modelde o tedarikçiye ödenebilecek azami fiyat **%11,765 düşer**
(AB/Şili menşeli tedarikçiler için).

Yani bu soru bir uyum sorusu değil, **bir fiyat sorusudur** ve RFQ'da
şu biçimde sorulabilir: *"EUR.1 düzenleyemiyorsanız fiyatınızdan %11,8
indirim yapabilir misiniz?"* — çünkü ithalatçı için ikisi **matematiksel olarak
denktir**.

**Tedarikçi değerlendirmesi yapmıyorum**; yalnız `T-161`'in fiyat karşılığını
sayısallaştırdım.

---

### İP-2504 → `finans-fizibilite` · **`KDV_ithal = 0,20 × L4_econ` özdeşliği CIF bilinmeden çalışır**

Ters modelde bedava gelen bir sonuç: gümrükte nakden ödenecek KDV,
**CIF bilinmeden**, yalnız `L4_econ_max`'tan doğrudan hesaplanır
(`X_pre = 0` iken):

```
kdv_ithal = 0,20 × L4_econ_max          ← menşeden BAĞIMSIZ
L4_cash   = 1,20 × L4_econ_max
```

Yani hedef raf fiyatı bandı verildiği anda, **`fx` olmadan, tedarikçi fiyatı
olmadan, navlun olmadan** gümrükte ödenecek KDV tutarı hesaplanabilir.
`master-commercial-input-table.md` §5.3'ün 6. maddesi ("peak_cash yapısı
hesaplanabilir, tutarı hesaplanamaz") **kısmen aşılabilir**: KDV bileşeninin
**tutarı** hesaplanabilir. ÖTV bileşeni de zaten maktu ve TL'dir.

Geriye tutar olarak yalnız **GV** kalır ve o da `CIF_TRY_max`'a bağlıdır.
**Sonuç üretmiyorum**; modelleme kararı `finans-fizibilite`'nindir.

---

## navlun-lojistik-uzmani (TUR 2.5)

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2.5
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md bu turda DOKUNMA listesindedir. Bunlar SONUC DEGIL, IPUCUDUR."
```

---

### İ-2501 → `finans-fizibilite`

**İpucu:** Gümrük müşavirliği ücreti sabit değildir. `EV-2026-08-09-342` (T3,
2026 asgari tarife): İTH-2 4.670 TL + ANT-1 1.350 TL **artı**, CIF
**15.001–225.000 USD** için *aşan kısmın **%0,3'ü***; 225.001–2.000.000 USD
için aşan kısmın %0,1'i.

**Neden önemli:** Senaryolarımda müşavirlik **6.020 TL sabit** alındı, çünkü
CIF'i ben belirleyemem. 25.000 şişe ve üstünde CIF 15.000 USD eşiğini kesin
aşar → **benim TRY bacağım bu hacimlerde EKSİKTİR.** Formül `finans-fizibilite`
tarafından CIF üzerinden tamamlanmalıdır.

---

### İ-2502 → `finans-fizibilite`

**İpucu:** LCL modunda şişe başı **USD** maliyeti 5.000 → 100.000 şişe
arasında yalnızca **%12–14** düşüyor (0,450 → 0,387 BASE). TRY bacağı %67
düşüyor. FCL'de her iki bacak da %68–74 düşüyor.

**Neden önemli:** Finans modelinde "hacim büyürse birim lojistik maliyeti
düşer" şeklinde **mod-bağımsız** bir ölçek varsayımı kullanılırsa, LCL
senaryosu **sistematik olarak iyimser** olur. Ölçek ekonomisi **moda geçişten**
gelir, hacimden değil — ve o mod (FCL) fiyatı `UNKNOWN`'dır (`T-304`).

---

### İ-2503 → `global-sourcing-kasifi`

**İpucu:** Koli formatı (6'lı vs 12'li) yalnızca %7'lik bir hacim farkı değil.
Kapasite bandının alt ucunda (11.800 şişe/20DV) **25.000 şişe iki konteynere
sığmıyor, üçüncü konteyner gerekiyor** → şişe başı TRY maliyeti **%73**
artıyor.

**Neden önemli:** `T-302` (tedarikçiden koli spesifikasyonu) "iyi olurdu"
kategorisinde değil, **basamaklı maliyet etkisi olan** bir `UNKNOWN`.
RFQ'da şişe çapı/yüksekliği ve koli dış ölçüsü **zorunlu alan** olmalı.

---

### İ-2504 → `mevzuat-ruhsat-uzmani`

**İpucu:** Gecikmenin maliyeti **yükün nerede beklediğine** bağlı:
antrepoda 60 gün ≈ **0,03 EUR/şişe**; limanda 60 gün ≈ **0,61 USD/şişe**
(detention + terminal ardiyesi, iki ayrı sayaç). Fark ~30–35 kat.

**Neden önemli:** `T-301` şu anda "bandrol/ruhsat kaç gün sürer?" diye
soruyor. Finansal olarak asıl belirleyici soru: **"bu sürenin ne kadarında yük
hâlâ konteynerde/limanda olmak zorunda?"** Menşede bandrollenebiliyorsa
(`EV-2026-08-09-380`, doğrulanmadı) liman bekleme riski büyük ölçüde ortadan
kalkar.

---

### İ-2505 → `gumruk-vergi-uzmani`

**İpucu:** LCL'de navlun tek bir CBM fiyatının içine gömülüdür (origin local
charge'lar dahil); FCL'de kalem kalem ayrışır (okyanus + THO + B/L + THD + …).

**Neden önemli:** Gümrük kıymetine (CIF) hangi kalemin **gireceği** ve hangi
kalemin **yurt içi masraf** sayılacağı **taşıma moduna göre değişir.**
Aynı fiziksel maliyet, LCL'de matraha girip FCL'de girmeyebilir. Bu, `T-303`
ve `30-vergi-gumruk/matrah-sirasi.md` için yapısal bir noktadır.

---

### İ-2506 → `seytanin-avukati`

**İpucu:** Bu turun senaryolarında **FCL'in BASE'i yoktur** (`M-6`). Modelde
bir yerde FCL için tek bir merkezî sayı görülürse, o sayı **uydurulmuştur** —
benim çıktımdan gelmiş olamaz.

---

## global-sourcing-kasifi (TUR 2.5)

```yaml
ajan:   global-sourcing-kasifi
tur:    TUR 2.5 — RFQ NEGOTIATION CARDS
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md bu turda DOKUNULMAZ listesindedir.
         Bulgular CLAUDE.md §11 geregi silinmemis, bu _parts dosyasina
         birakilmistir. Birlestirme karari baskanindir."
kaynak: 50-sourcing/rfq-negotiation-cards.md
```

> Bunlar **sonuç değildir, ipucudur.** Hiçbiri kendi alanımda üretilmiş bir
> karar değildir; kartlar yazılırken karşıma çıkan ve **başka ajanların
> alanına ait** gözlemlerdir.

| # | Hedef ajan | İpucu | Neden önemli | Ticket |
|---|---|---|---|---|
| **İP-871** | `gumruk-vergi-uzmani` | **OD-5 — koşullu fiyat düzeltme maddesi.** Menşe belgesi düşerse tarife farkının tedarikçiye rücu edilmesi sözleşmeye yazılabilir mi; sonradan ibraz / sonradan kontrol / geri ödeme yolları açık mı? | Açıksa OD-5 bir **nakit akışı** maddesine iner; kapalıysa pazarlıktaki **en değerli tek madde** olur (**32,10 TRY/şişe**) | `T-872` |
| **İP-872** | `gumruk-vergi-uzmani` | **Karışık menşeli tek konteyner.** Purcari grubu MD + RO + BG'yi tek sevkiyatta birleştirebilirse **tek konteynerde iki tarife oranı** doğar. Tek beyanname mi, iki mi? | Kart 10 soru #3'ün cevabı **ham hâliyle** iletilecek; ben yorumlamıyorum | `T-873` (yan) |
| **İP-873** | `gumruk-vergi-uzmani` | **Ödeme vadesi tedarikçiden tedarikçiye pazarlık konusudur.** 10 kartın 9'unda ödeme şartı `UNKNOWN`; tek gözlem (Harland) **%50+%50, tamamı sevkiyat öncesi**. Kartlar **hem peşin hem vadeli için ayrı fiyat** istiyor. | Modelin `KKDF = 0` varsayımı **n=1 gözleme** dayanıyor (`EV-2026-08-10-452`). Vadeli seçenek fiyat avantajı getirirse **KKDF matrahı devreye girer** | — |
| **İP-874** | `navlun-lojistik-uzmani` | **Purcari MD/RO/BG için ayrı navlun gerekiyor.** Moldova **denize kıyısı olmayan** bir menşedir; RO/BG rotası MD'den **32,10 TRY/şişe'den pahalıysa menşe değiştirme kazancı negatife döner.** | Havuzdaki **tek menşe değiştirme kaldıracının** net değeri buna bağlı | `T-873` |
| **İP-875** | `navlun-lojistik-uzmani` | **Şili — konsolidasyon tercihi düşürür.** Corta Hojas için LCL/konsolidasyon doğal rotası Rotterdam/Antwerp'tir; çıkış ülkesi Şili olmazsa **%50 → %70**. 5.000 şişelik pilotta ucuz görünen rota **20 puanlık tarifeyi yakabilir.** | `T-163` / `T-914` zaten açık — kart bunu **tedarikçi taahhüdüne** çevirdi (OD ŞİLİ EKİ) | `T-914` |
| **İP-876** | `navlun-lojistik-uzmani` | **Cantina Danese (Veneto) navlunu LCL ve FCL'de `UNKNOWN`.** Türkiye'nin **en güçlü ithalat hattı** (İtalya, 5,75 m lt/2025) üzerinde tek fiyat verisi yok. | Kart 2 en güçlü hat + bilinen MOQ birleşimi; navlun bacağı boş | `T-916` |
| **İP-877** | `kanal-marj-uzmani` | **Model A'da marka sahibi ithalatçıya yeniden satış fiyatı tavanı / markup sınırı dayatabilir.** Kart 6, 7, 8, 9'da bu doğrudan soruluyor. | Bu, kanal marjını **modelden değil, tedarikçi sözleşmesinden** kısıtlayan tek mekanizmadır — `dis_distributor.marj_pct` `null` iken (`T-604`) ikinci bir kısıt katmanı doğar | — |
| **İP-878** | `kanal-marj-uzmani` | **Model A'da pazarlama katkısı / listeleme desteği** tedarikçiden gelebilir. Kart 7 ve 8 bunu soruyor. | Gelirse `f` (listeleme bedeli, şu an `0` alınmış, `T-604`) **kısmen tedarikçiye kayar** ve tavan yukarı açılır | — |
| **İP-879** | `mevzuat-ruhsat-uzmani` | **Interbrosa'ya "Türkçe arka etiketi kendi tesisinizde uygulayabiliyor musunuz" soruluyor** (Kart 3, soru #3). Cevap "evet" ise Türkiye'deki etiketleme operasyonu **tamamen kalkar**. | `L5` içindeki bandrolleme/etiketleme operasyon maliyeti modelde **`0` alınmış** (`T-314`) — menşede etiketleme bunu **yapısal olarak** çözer | — |
| **İP-880** | `mevzuat-ruhsat-uzmani` | **Cantina Danese kendi gümrük antreposunu işletiyor** (`EV-2026-08-10-453`). Bandrol/ÜİS veya Türkçe etiketleme menşede yapılabiliyorsa, antrepo işleten tedarikçi bunu **operasyonel olarak kaldırabilir**. | TUR 2'de `İP-459` olarak bırakılmıştı; kartta **OD-3 riskiyle birlikte** yeniden doğdu — aynı antrepo **menşe karışması riski** de taşır | — |
| **İP-881** | `turkiye-pazar-kasifi` | **Danese'nin Türkiye'deki `Midas` ilişkisi canlı mı?** Ürün (`Danese Primitivo Puglia Black Label`, 1.419 TL) **stokta değil**. | Kart 2'nin münhasırlık riskinin **büyüklüğü** buna bağlı; "listelenmiş ama stokta yok" ile "aktif distribütör" **aynı şey değildir** | `T-565` |
| **İP-882** | `turkiye-pazar-kasifi` | **Porta 6 ve Mucho Más gibi küresel value markaların Türkiye'de bulunma ihtimali `presence UNKNOWN`'dır** — `T-464` cevabı tek kanaldan verilmiştir ve ajan bunu kendisi uyarmıştır. | Kart 8 (Vidigal) ve Model A tarafının tamamı bu statüye bağlı; **fiziksel mağaza turu** (`OQ-502`/`OQ-552`) yapılırsa bu 7 marka listeye eklenmeli | `T-464` |
| **İP-883** | `finans-fizibilite` | **`IMPLIED_BREAKEVEN_USDTRY` sıralaması AU/ZA/AR için kullanılamaz** (`TEMSİLİ DEĞİL`, hacim <100 bin lt). Kart 1 (Harland/AU) bu nedenle **sıralama değeri taşımıyor.** | Ülke sıralaması yalnızca **ES · MD · CL · PT · IT · FR** için okunabilir; kartlar bunu yazıyor | — |
| **İP-884** | `finans-fizibilite` | **RO/BG için gözlenen CIF birim değeri bu projede hiç kullanılmadı** → Purcari'nin RO/BG kolunda `IMPLIED_BREAKEVEN` **`UNKNOWN`**. | Menşe değiştirme kaldıracının (+32,10 TRY/şişe) **karşı tarafı ölçülemiyor**; bu turda **yeni araştırma yasak olduğu için açılmadı** | — |

---

## turkiye-pazar-kasifi (TUR 2.5)

> Bu dosya `99-ops/capraz-ipuclari.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından **dokunulmamıştır**.
> Aşağıdakiler **alan dışı bulgulardır**; bu ajan bunlardan **sonuç üretmemiştir**.

---

### İP-701 → `kanal-marj-uzmani`

**Bulgu:** Hedef merdivenin her basamağında gözlenen **stokta rakip SKU sayısı**
(±%10 pencere, tek online uzman kanal, 2026-08-10, `EV-2026-08-10-702`):

| Hedef | Stokta yerli rakip | Stokta ithal rakip |
|---|---|---|
| 599 TL | 3 | 0 |
| 699 TL | 17 | 0 |
| 799 TL | 31 | 1 |
| 899 TL | 35 | 2 |
| 999 TL | 49 | 1 |

**Neden önemli:** Listeleme bedeli ve raf pazarlığı, o raf bölmesinde kaç rakibin
olduğuna duyarlıdır. **Bu bir marj hesabı DEĞİLDİR** — yalnızca rakip sayımıdır.
Marjı bu ajan **hesaplamamıştır ve hesaplayamaz** (`pazar.yaml` K4).

---

### İP-702 → `kanal-marj-uzmani`

**Bulgu:** Gözlenen tek çok-SKU'lu kanalın **tüm stokta katalogunda (471 SKU)
600 TL altında yalnızca 1 SKU** vardır; stokta yerli **medyan 1.410 TL**
(`EV-2026-08-10-702`).

**Neden önemli:** Bu kanalın **giriş segmentini taşımadığı** anlamına gelebilir.
Eğer öyleyse, fiyat/performans bir ithal ürün için doğru kanal bu **değildir** ve
kanal stratejisi Metro / zincir market / tekel bayii üzerinden kurulmalıdır.
Kanal seçimi `kanal-marj-uzmani`'nın alanıdır; bu ajan yalnızca **gözlemi**
bildirmektedir.

---

### İP-703 → `finans-fizibilite`

**Bulgu:** Gözlenen kanalda **stokta ithal taban 875 TL**'dir. Hedef merdivenin
799 TL ve altındaki tüm basamakları bu tabanın **altındadır**.

**Neden önemli:** Ters model 799 TL veya altına kurulursa, sonuç
"gözlenen hiçbir stokta ithal şarabın ulaşmadığı bir fiyat noktası" olur.
Bu **imkânsız** demek değildir (Metro'da 599,90 görülmüştür) ama modelin
çıktısında **açıkça yazılmalıdır**. `T-702`.

---

### İP-704 → `global-sourcing-kasifi`

**Bulgu:** Hedef merdivenin 600–1.000 TL bölgesinde gözlenen rakip seti
**neredeyse tamamen yerlidir** (65 yerli / 2 ithal, stokta,
`EV-2026-08-10-702`). Bu bölgede stok dışı olarak listelenen ithal markaların
menşe profili: İtalya, Fransa, Almanya, Şili, Yeni Zelanda, Gürcistan, Moldova.
**ABD ve Avustralya bu kanalda hiç yoktur** (TUR 1 B-8 / TUR 2 B-6 ile tutarlı).

**Neden önemli:** İki `OBSERVED_BENCHMARK` (ABD ve Avustralya) tam da bu kanalın
**hiç taşımadığı** menşelerdendir. Bu, benchmark'ların Metro'nun kendi
ithalatından geliyor olabileceği ihtimalini güçlendirir — **doğrulanmamıştır**
(`OQ-503`). Sourcing menşe kararında bu asimetri dikkate alınmalıdır.

---

### İP-705 → `yatirim-komitesi-baskani`

**Bulgu:** `TARGET_SHELF_PRICE` merdiveninin asıl karşılığı olan
`L8_CHAIN_RETAIL` katmanında projenin **sıfır gözlemi** vardır.

**Neden önemli:** Bu, `OQ-001`'in (benchmark hangi katman?) **hedef tarafındaki
aynasıdır** ve bugüne kadar adlandırılmamıştır. Ayrıntı ve talep: `T-701`.

---

### İP-706 → `seytanin-avukati`

**Bulgu (kendi aleyhime):** TUR 2.5'in ürettiği yoğunluk eğrisinin **tamamı**
tek bir online uzman perakendecinin **alt kuyruğundan** okunmuştur. TUR 2.5'te
tek kanal zaafını kırmak için **17 ek alan adı** denenmiş, **0 kullanılabilir
kanal** bulunmuştur (`EV-2026-08-10-701`) — TUR 1 ve TUR 2 ile birlikte
**üçüncü başarısız deneme**.

**Neden önemli:** Kırmızı takım bu belgeye saldıracaksa **en zayıf yer burasıdır**
ve bu ajan tarafından **kendisi** işaretlenmiştir. Saldırının hazır cephanesi:
`60-pazar/target-shelf-price-analysis.md` §5 ve §2.4.

---

## finans-fizibilite (TUR 2.5)

```yaml
ajan:   finans-fizibilite
tur:    TUR 2.5 — REVERSE TARGET MODEL
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md DOKUNMA listesindedir ve DEGISTIRILMEMISTIR.
         Bu dosya, baskanin merge edecegi PARCA kayittir.
         BUNLAR SONUC DEGILDIR, IPUCUDUR — hicbiri baska bir ajanin alaninda
         KARAR uretmez."
```

---

### İP-F1 → `mevzuat-ruhsat-uzmani` · **BANDROL 2027'DE YÜRÜRLÜKTE OLMAYACAK**

`ruhsat.yaml → bandrol_fiyat_endeksleme`: *"her yıl 1 Ocak'tan geçerli olmak
üzere önceki yıl Yİ-ÜFE oranı"* (`EV-2026-08-09-213`, **T1**).
`vergi.yaml → meta.tarih_senaryolari`: **üç hedef tarihin üçü de 2027'dedir.**

> **`2,36073 TL` hedef tarihte yürürlükte olmayacaktır.**
> ÖTV için `T-104`/`T-921` ile **kod düzeyinde** uygulanan "gelecek değer
> yazma / ufuk denetimi" kuralı **bandrol için yoktur** ve model 2026
> değerini kullanmak zorunda kalmıştır.

**Neden önemli:** Sayısal etkisi küçüktür (`MAX_CIF` üzerinde 1,57 TL taban,
%25 artışta −0,39 TL) — ama **aynı disiplin ihlali `TADAB hizmet bedeli`
(0,1587) ve `toplam_ruhsat_sabit_maliyeti` (150.839 / 253.372 TL) için de
geçerli olabilir** ve orada etki **çok daha büyüktür**.
→ ticket **`T-858`**

---

### İP-F2 → `mevzuat-ruhsat-uzmani` · **BİR MEVZUAT KADEMESİ ÖLÇEK STRATEJİSİNİ BELİRLİYOR**

`toplam_ruhsat_sabit_maliyeti` **20.000 litre/yıl** eşiğinde kademe atlıyor:
**150.839 → 253.372 TL** (`EV-2026-08-09-234`). 20.000 lt = **26.667 şişe**.

Ters modelde `MAX_CIF_TRY` (799 TL · İspanya · CHAIN BASE):

| Hacim | `MAX_CIF_TRY` | Geçiş | değişim |
|---|---|---|---|
| 5.000 | 272,83 | — | — |
| 25.000 | 290,51 | 5.000 → 25.000 | **+17,68 TL** |
| 50.000 | 291,28 | **25.000 → 50.000** | **+0,77 TL** |
| 100.000 | 293,03 | 50.000 → 100.000 | +1,75 TL |

> **Ölçek ekonomisinin %87'si ilk sıçramada gerçekleşiyor ve bunun sebebi
> navlun değil, bir RUHSAT KADEMESİ.** Bu, modeldeki başka hiçbir kalemin
> üretmediği bir etkidir ve **`SCALE` kararının ekonomik gerekçesini
> doğrudan zayıflatmaktadır.**

→ ticket **`T-858`** (a)

---

### İP-F3 → `navlun-lojistik-uzmani` · **`C-311` TERS MODELDE ETKİSİZDİR**

Okyanus navlunu ve sigorta **CIF'in İÇİNDEDİR** (GK md.27/1-e,
`EV-2026-08-09-120`). Ters model CIF **tavanını** üretir; navlun o tavanın
**nasıl bölüşüleceğini** belirler, tavanın **kendisini** değil.

> **FCL bandının 4 kat olması (`C-311`) `MAX_CIF_TRY`'yi SIFIR etkiler.**
> Navlunun ters modeldeki tek görünür etkisi **TR-içi TRY bacağıdır** ve o da
> 5.000 şişede tavanı yalnızca **±0,93 TL** oynatır.

**Sonuç:** `T-304` (CRITICAL) **ileri model** ve **FOB pazarlığı** için
blokerdir; **ters model için değildir.** Bu, `T-304`'ün aciliyetinin **nereye
ait olduğunu** netleştirir — aciliyeti düşürmez, **yerini değiştirir.**

---

### İP-F4 → `navlun-lojistik-uzmani` · **MOLDOVA'YA DENİZ MANTIĞI UYGULANDI**

Moldova havuzdaki **tek karayolu erişimli menşedir**. Ters modelde ona da
liman tabanlı TR-içi bacak (ardiye, devanning, THD içeren türev) uygulandı —
çünkü elimizde başka bir yapı yok.

**Bu muhtemelen yanlıştır** ve Moldova'nın gerçek TR-içi maliyeti farklı
kalemlerden oluşur (kara gümrük kapısı, TIR, ordino yapısı).
→ ticket **`T-854`** madde 2

---

### İP-F5 → `gumruk-vergi-uzmani` · **`g` İÇİN ASİMETRİ SÜRÜYOR**

Ajanın kendi itirafı (`ters-model-vergi-bacagi.md` §13.1):
*"ÖTV için titizlikle uygulanan 'gelecek değer yazma' kuralı, gümrük vergisi
oranı için de geçerlidir ve bu belge `g`'yi 2027'de değişmez varsayarak bir
ASİMETRİ taşımaktadır."*

**Model bu asimetriyi aynen taşımaktadır.** İthalat Rejimi Kararı **yıllıktır**;
`ttl: 90d` → **2026-11-08'den sonra STALE.** Üç hedef tarihin üçü de 2027'dedir
→ **§4'teki `g` değerlerinin hiçbiri hedef tarihte doğrulanmış değildir.**

**İpucu:** ÖTV için yazılan `otv_maktu_zaman_serisi` yapısının (gözlenen
değerler + `son_gozlem_gecerlilik_ufku` + `gelecek_deger_kurali` +
`engine_okuma_kurali`) **bire bir muadili `gumruk_vergisi_oranlari_by_mense`
için de kurulabilir** ve engine tarafı **hazırdır** (`otv_zaman_serisi.py`
deseni yeniden kullanılabilir).

---

### İP-F6 → `turkiye-pazar-kasifi` · **TERS MODEL ÇIKTISININ ANLAMI L8 ALT KATMANINA BAĞLI**

`MAX_CIF_TRY = 301,78 TL/şişe` sayısı, hedefin `L8_METRO_CASH_CARRY`'de mi
`L8_CHAIN_RETAIL`'de mi olduğuna göre **aynı sayı ama farklı anlam** taşır
(`K3`: cash & carry yapısı gereği zincirden ucuzdur).

Ayrıca model, kanal marj bandını (`m_retail` %18/25/35) **zincir perakende**
varsayımıyla uyguladı. Hedef aslında bir cash & carry fiyatı ise, uygulanması
gereken marj yapısı **farklıdır** — `kanal.yaml`'ın kendi gerekçesi cash &
carry formatını marjı **aşağı çeken** bir faktör olarak sayar.
→ ticket **`T-859`**

---

### İP-F7 → `kanal-marj-uzmani` · **TEKEL'İN %11 ÜSTÜNLÜĞÜ BİR ARTEFAKTTIR**

`MAX_CIF_TRY` (799 TL · ES · DOC_OK · 5.000 şişe · BASE):
**CHAIN 272,83** vs **TEKEL 303,90** → tekel **+%11,4**.

**Farkın TAMAMI**, `d` (geri akan bedeller) bandının **yalnız zincir için**
tanımlı olmasından ve tekelde **`UNKNOWN` → 0** alınmasından gelir.

> **Bu bir bulgu değildir. İki `ASSUMPTION` ile bir `UNKNOWN`'ın çarpımıdır.**
> Tekelde de bir tür geri akış (iskonto, ciro primi, vade farkı, teşhir
> desteği) varsa fark **kapanır veya tersine döner.**
> İki kanal arasında ekonomik tercih **modelden okunamaz.**

→ ticket **`T-856`**

---

### İP-F7b → `gumruk-vergi-uzmani` · **TERS MODELİN ALTINCI HATASI (kanal bacağında)**

`ters-model-vergi-bacagi.md` §6, ters modelde yapılması en muhtemel **beş**
hatayı listeler (`H1`…`H5` + `H6` ikincil). **Altıncısını bu turda kendim
yaptım, buldum ve düzelttim:**

```
H7 (onerilen ad) — "L5_max = L6" alinmasi
YANLIS:  L5_max = L6 x (1 - mu)
DOGRU:   L5_max = L7_eff - mu x L6      (L7_eff = L6(1-d) - f)
BUYUKLUK: 799 TL / ES / CHAIN BASE'te  -28,95 TL/sise  (H1: -17,82 ; H3: -22,22)
YONU:     PROJENIN LEHINE (tavani yukseltir) -> gozden kacmasi DAHA OLASI
```

**Neden sizin listenizde yok:** `H1`…`H6` **vergi bacağının** hatalarıdır;
bu hata **kanal bacağındadır** (R2–R5) ve o adımların sahibi
`kanal-marj-uzmani` + `finans-fizibilite`'dir.

**Öneri:** §6'ya, sınırın **kendi dışında** kalan bu hatayı işaret eden bir
satır eklenmesi — çünkü `R7`'nin girdisi olan `L4_econ_max`'ın doğruluğu
**tamamen R5'e bağlıdır** ve `R8` round-trip assertion'ı bu hatayı
**YAKALAYAMAZ** (round-trip yalnızca `L4_econ_max ↔ CIF` tutarlılığını test
eder, `L4_econ_max`'ın kendisinin doğru olup olmadığını değil).

> **`R8`'in kör noktası budur ve kayda geçirilmelidir.**

---

### İP-F8 → `seytanin-avukati` · **SALDIRILACAK EN VERİMLİ TEK NOKTA**

Modelde **13 maliyet kalemi `0` alınmıştır** ve **13'ünün 13'ü de aynı yönde
(yukarı) saptırır**:

varış local charge (USD) · menşe local charge (EUR) · müşavirlik CIF kademesi ·
listeleme bedeli `f` · `d` (tekel + HoReCa) · fire/zayi KDV'si ·
antrepo bekleme · bandrolleme operasyonu · devreden KDV finansman maliyeti ·
distribütör marjı · ithalatçı katkı payı · gözetim eşiği · ÖTV λ > 1

**Somut yıkım senaryosu** (5.000 şişe · 799 TL · İspanya · CHAIN BASE,
tavan **272,83 TL**):

| Eklenen | Yeni tavan | Kayıp |
|---|---|---|
| Kendi dağıtım, 1 kişinin **asgari ücret tabanı** | 208,49 | −64,34 |
| + ÖTV λ = 1,5625 | 188,45 | −84,38 |
| + distribütör marjı %15 | ~134 | −139 |
| + listeleme bedeli 10 TL/şişe | ~127 | −146 |

**Dört kalem tavanı %53 siliyor.** Hiçbirini modele koymadım çünkü hiçbirinin
kanıtı yok — **ama koymamak da bir seçimdir ve o seçim projenin lehinedir.**

> **DAHA DA ÖNEMLİSİ:** bu turda **kendi bulduğum `R5` hatası da tam olarak
> aynı yöndeydi** (tavanı %10,6 fazla gösteriyordu — İP-F7b).
> **İki bağımsız iyimserlik kaynağının aynı modelde bulunması bir DESEN
> olabilir.** Kırmızı takım bunu bir tesadüf saymamalıdır.

---

### İP-F9 → `gumruk-vergi-uzmani` + başkan · **EN UCUZ / EN YÜKSEK GETİRİLİ KONTROL**

**KDVK md.36 uyarınca çıkarılmış bir Cumhurbaşkanı Kararı ARANMAMIŞTIR**
(`T-151`, `OQ-G10`). Böyle bir karar varsa alkolde KDV indirim hakkı
kısıtlanmış olabilir ve:

- KDV **ekonomik maliyet** olur,
- `MAX_CIF_TRY` **~%22,7 düşer** (her iki menşede de aynı oran),
- 799/ES/CHAIN/BASE: **272,83 → ~211 TL/şişe**,
- HoReCa sütununun **tamamı** negatife yaklaşır,
- **Bu turun tüm sayısal çıktısı yeniden hesaplanır.**

> **Bu, saatler içinde ve ~sıfır maliyetle kapatılabilecek en yüksek getirili
> tek kontroldür ve üç turdur yapılmamıştır.**

---

### İP-F10 → başkan · **DÖRT UCUZ ADIM, DÖRT BÜYÜK BOŞLUK**

| # | Adım | Kim | Süre | Ne açar |
|---|---|---|---|---|
| 1 | KDVK md.36 CB kararı taraması | `gumruk-vergi-uzmani` | **saatler** | `MAX_CIF`'in %22,7 çökme riskini kapatır |
| 2 | **`fx` — tarihli tek kur + bant** | **yatırımcı/başkan** | **dakikalar** | `MAX_FOB` ve `MAX_EXW`'yi açar; **ülke ayrıştırmasını çalıştırır** |
| 3 | Gözetim tebliği yeniden taraması | `gumruk-vergi-uzmani` | saatler | Tavanın bir **alt sınırla** test edilmesini sağlar |
| 4 | **Minimum katkı eşiği** (`OQ-901`) | **yatırımcı** | dakikalar | `TARGET`/`ACCEPTABLE`/`WALK-AWAY` fiyatlarını **üretilebilir** kılar |

> **Ters modelin bugünkü en büyük dört boşluğu, en ucuz dört adımla
> kapatılabilir durumdadır.** Bu asimetri TUR 6'ya taşınmalıdır.
> `tur-25-preflight.md` §1.7 aynı asimetriyi **üçüncü kez** kaydetmişti.

---

---

# TUR 3A ÇAPRAZ İPUÇLARI

> Ajanların `99-ops/_parts/*-tur3a.md` fragment'lerinden değiştirilmeden aktarıldı.

## gumruk-vergi-uzmani (TUR 3A)

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında gördüğüm bulgular.
> İlgili ajan doğrulamadan modele girmez.

---

### Cİ-3A-01 → `kanal-marj-uzmani` · **"HER ŞEY DAHİL" OTEL KANALI YAPISAL OLARAK %20 DAHA ZAYIF**

**Kaynak:** KDV Genel Uygulama Tebliği **III/B-2.5.2** (`EV-2026-08-10-858`, T1)

> *"Geceleme hizmetleri kapsamında sunulan alkollü içeceklere ait **yüklenilen KDV
> tutarları, konaklama tesisleri tarafından hesaplanan KDV tutarlarından
> indirilemez.**"*

**Ne demek:** "Her şey dahil" sistemle çalışan bir otel, aldığı şarabın
KDV'sini **indiremez** → şarabın KDV'si o otel için **gerçek maliyettir.**
Yani aynı fiyata alan bir market ile bir "her şey dahil" otelin **efektif
maliyeti farklıdır**: otelinki `fiyat × 1,20`, marketinki `fiyat`.

**Kaçış yolu var (ve bu bir satış argümanıdır):** tesis alkollü içecek
bedelini **faturada ayrıca gösterirse** genel oran uygular ve **KDV'yi
indirebilir**. Yani ithalatçı, HoReCa müşterisine *"bedeli ayrıştır"*
diyerek **%20'lik bir değer yaratabilir.**

**Neden önemli:** kanal marjı modelinde HoReCa'nın ödeme istekliliği,
"her şey dahil" mi "à la carte" mı olduğuna göre **yapısal olarak ayrışır.**
Bu bir pazarlık farkı değil, **vergi kaynaklı bir yapı farkıdır.**

> ⛔ **Bu benim alanım değildir. Kanal marjı sonucu ÜRETMİYORUM.**
> `EV-2026-08-10-858` mevcuttur; `kanal-marj-uzmani` isterse kullanır.

---

### Cİ-3A-02 → `finans-fizibilite` · **%22,7 RAKAMI FAZLA KÖTÜMSER (düzeltme gerekir)**

`rapor-tur25-finans.md` §9.1 ve `T-947`, KDV indirim hakkının kısıtlanması
hâlinde `MAX_CIF_TRY`'nin **%22,7** düşeceğini yazmıştı.

Bu rakam **tam kısıt** varsayımına dayanır. Bulunan gerçek düzenleme
(7846 s. CBK + KDVGUT III/C-2.6, `EV-2026-08-10-854`) **kısmi kısıt**
getirir: **yalnızca tevsik edilemeyen artış kısmına** isabet eden KDV
indirilemez; CIF ve ona isabet eden GV/İGV üzerinden ödenen KDV
**indirilebilir kalır.**

→ Ticket **`T-171`** ile resmen bildirildi.

---

### Cİ-3A-03 → `navlun-lojistik-uzmani` + `finans-fizibilite` · **YMM RAPORU: GÖRÜNMEZ BİR L5 KALEMİ**

KDVGUT **III/C-2.6.2** (`EV-2026-08-10-854`), 7846 kapsamında ithalat yapan
mükellefe **altışar aylık dönemler** itibarıyla ya **vergi dairesine bildirim**
ya da **Özel Amaçlı YMM Raporu** yükümlülüğü getirir (tam tasdik sözleşmesi
varsa rapor gerekmez).

**Baz senaryoda tetiklenmez** (gözetim yok). Ama gözetim gelirse:
`L5`'te **yeni bir gider satırı** doğar. Tutar **UNKNOWN** ve bu benim alanım
değildir. Ayrıca "tam tasdik sözleşmesi" bir **muhasebe/denetim** kararıdır ve
maliyeti vardır.

---

### Cİ-3A-04 → `global-sourcing-kasifi` · **GÖZETİM TAZE MEYVEYE UYGULANMIŞTIR**

Gözetim tebliği taramasında (`EV-2026-08-10-860`) 2019/6 sayılı tebliğe ilişkin
değişiklikte **`0810.10` (çilek)** ve **`0810.50` (kivi)** GTİP'leri görüldü.

**Anlamı:** *"Tarım/gıda ürününe gözetim gelmez"* varsayımı **yanlıştır.**
Şarapta gözetim bulunmaması bir **kategori bağışıklığı değil**, sadece
**fiilî listede olmama** durumudur.

→ Çok düşük FOB teklifleriyle çalışan bir sourcing stratejisi, gözetimin
**gelecekte** getirilebileceğini bir **senaryo riski** olarak taşımalıdır.
Sonuç üretmiyorum; ipucudur.

---

### Cİ-3A-05 → `yatirim-komitesi-baskani` (yöntem notu) · **RESMÎ PDF'LERDE "METİN VAR" ≠ "METİN OKUNUYOR"**

Gözetim tebliğlerinin taranmasında üç ayrı teknik gerekti:

| Sorun | Nerede görüldü |
|---|---|
| PDF metin katmanı **bozuk font kodlamasıyla** geliyor (harf harf şifrelenmiş gibi) | 2026/1, 2024/14 |
| GTİP tablosu **metin katmanında hiç yok**, ayrı bir **CCITT/JBIG2 görüntü** | 2026/2, 2026/4, 2026/5 ve diğerleri |
| Sayfa görüntüsü OCR'ı **tabloyu atlıyor** (psm 6 tablo bloğunu görmüyor) | çoğu tebliğ |

**Tek yöntemle yapılan bir tarama YANLIŞ NEGATİF üretirdi.**
Bu, projede **her "bulamadım" sonucunun yöntemini de sorgulamayı** gerektirir —
`EV-2026-08-09-125` tam olarak bu türden bir kayıttı.

**Genelleştirilebilir kural önerisi:** resmî bir listede bir GTİP'in
"olmadığı" iddiası, **listenin kaç kayıt içerdiği** (pozitif kontrol)
belirtilmeden kabul edilmemelidir.

---

## kanal-marj-uzmani (TUR 3A)

<!-- 99-ops/capraz-ipuclari.md'ye BASKAN tarafindan birlestirilir. Bu dosya bir PART'tir. -->

> Bunlar **sonuç değildir, ipucudur.** Hepsi başka ajanların alanındadır ve
> bu ajan hiçbirinde sonuç üretmemiştir.

### İP-3A-1 → `gumruk-vergi-uzmani`

**Kanal bacağında KDV üç ayrı yerde vardır, model yalnızca birini
uyguluyor.** `kanal-katman-matrah-haritasi.md` §3.3:

| Görünüm | Matrah | Modelde |
|---|---|---|
| V1 raf/menü KDV'si | `L8_net` | ✅ `R1` |
| V2 mal faturası KDV'si | `L6` → `L6_gross` | ⚠ yok (alacak matrahı!) |
| V3 hizmet faturası KDV'si (`f`, `d`) | `d·L6 + f` | ❌ yok |

**Neden önemli:** V3'ün indirilebilirliği `f`+`d`'nin ekonomik maliyetini
**1,20 katına** çıkarabilir. V2 ise `peak_cash`'i **%20** etkiler.
→ `T-611`

---

### İP-3A-2 → `gumruk-vergi-uzmani`

**`vergi.yaml`'da HoReCa hizmet KDV oranı için AYRI BİR ALAN YOK.**
Model `R1`'i HoReCa menü fiyatına da ürün KDV oranıyla uyguluyor.
`marj-vs-markup.md` §2.3 bu riski TUR 2'de yazmıştı; model uyarıyı
**kullanmadı**. → `T-612`

---

### İP-3A-3 → `navlun-lojistik-uzmani`

**TR-içi lojistik rakamının TESLİM NOKTASI tanımı yazılı değil.**
Zincir **merkezi alım** yapar (`EV-2026-08-10-613` dipnot 14) ve ayrıca
bizden **lojistik bedeli** alır (`EV-2026-08-10-612`). Bu iki bacak
örtüşüyorsa **çift sayım**, örtüşmüyorsa mevcut model doğru — **ama
hangisi olduğu bilinmiyor.** → `T-618`

---

### İP-3A-4 → `finans-fizibilite` (ve `seytanin-avukati`)

**`reverse-price-model.md` §0.2'nin *"13 kalemin 13'ü de MAX_CIF'i yukarı
saptırır"* tespiti kanal bacağında da geçerlidir ve liste 7 kalem daha
uzuyor:** `f` ölçek asimetrisi · `d`'nin sabit bileşenleri · iade/fire ·
vade finansmanı · vade matrahı (`L6_gross`) · `f`+`d` KDV'si · tekel
kanalının üç sıfırı.

**Mertebe:** `K7` (38,00) + `K11` (19,38) + `K12` (27,55) ≈ **85 TL/şişe**
= `TGT_799 · CHAIN · BASE` tavanının (**272,83**) **%31'i.**
→ `70-kanal/kanal-bacagi-hata-listesi.md`

---

### İP-3A-5 → `turkiye-pazar-kasifi`

**Kanal karması modelin ölçülmemiş en büyük ekseni olabilir.**
`kanal_karmasi` üç alanın **üçü de `null`**. Üç kanalın tavanı
`TGT_799 · BASE`'te **272,83 / 303,90 / 87,88** — yani karma varsayımı
tek başına birleşik tavanı **3,5 kat** oynatabilir. Tornado'nun
**hiçbir ekseninde yok.**

**Uyarı:** nokta sayıları (GK 48.956 · ASN 29.218, `EV-2026-08-10-613`)
**ciro payı DEĞİLDİR** ve öyle kullanılamaz. Modern kanal nokta sayısı
zaten yoktur. → `T-603`

---

### İP-3A-6 → `yatirim-komitesi-baskani`

**`T-942`'nin önerdiği `R8-K` assertion'ı, birebir kodlanırsa `R5`
düzeltmesini geri alır.** `L5_max + μ·L6` ifadesi `L6`'ya değil `L7_eff`'e
eşittir; `L6` etiketiyle devam edilirse `d` ve `f` **iki kez** düşülür ve
test **tersine döner**: doğru formül reddedilir, naif formül kabul edilir.

**`T-942`'nin teşhisi doğrudur** — düzeltilmesi gereken tek şey `K1`
adımının etiketidir. Ama kabul kriteri olarak duruyor. → **`T-619`
(CRITICAL)**

---

### İP-3A-7 → `global-sourcing-kasifi`

**`T-605` (üreticiden alınan "marka/pazarlama katkısı" ↔ listeleme bedeli
çift sayımı) hâlâ açıktır** ve bu turda `K6c` olarak hata listesine
girmiştir. RFQ 5.6'daki katkı, `f` ile **aynı satırda netleştirilmelidir**;
aksi hâlde aynı para hem gelir hem gider olarak modele girer.

---

## global-sourcing-kasifi (TUR 3A)

```yaml
ajan:   global-sourcing-kasifi
tur:    TUR 3A — RFQ ZORUNLU TEKNIK ALANLAR
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md bu turda DOKUNULMAZ listesindedir.
         Bulgular CLAUDE.md §11 geregi silinmemis, bu _parts dosyasina
         birakilmistir. Birlestirme karari baskanindir."
kaynak: 50-sourcing/rfq-zorunlu-alanlar.md, 50-sourcing/rfq-template.md v2.2
```

> Bunlar **sonuç değildir, ipucudur.** Hiçbiri kendi alanımda üretilmiş bir
> karar değildir; zorunlu alanların kabul kriterleri yazılırken karşıma çıkan
> ve **başka ajanların alanına ait** gözlemlerdir.

| # | Hedef ajan | İpucu | Neden önemli | Ticket |
|---|---|---|---|---|
| **İP-881** | `mevzuat-ruhsat-uzmani` | **RFQ artık üreticiden fiziksel etiket taahhüdü istiyor:** ≥18 cm² basılabilir alan, bandrol için boş alan (mm×mm + konum), ABV ≥3 mm karakter. Üçü de **sizin bulgunuz**, benim değil. RFQ'ya rakam yazıldığı anda o rakam **spesifikasyon** hâline gelir. | Yanlış/eksik ölçü sorulursa üretici "evet" der, mal gelir, etiket yetmez — kalem **antrepodayken** geri döner | `T-881` |
| **İP-882** | `mevzuat-ruhsat-uzmani` | **Bandrol Türkiye'de antrepoda uygulanıyor, ama fiziksel alanı menşede basılan etiket belirliyor.** Bu, `lojistik.yaml → bandrolleme_operasyonu` bloğunun **ölçülmemiş bir ön koşulu** olduğu anlamına geliyor: alan yoksa operasyon yapılamaz, maliyet hesabı da anlamsız olur. | Bandrolleme maliyeti bugün alanın **var olduğu varsayımıyla** hesaplanıyor | `T-881` |
| **İP-883** | `navlun-lojistik-uzmani` | **Zorunlu alan baskısı uydurma rakamı teşvik edebilir.** "Boş bırakılamaz" alan, tedarikçiyi *bir şey yazmaya* iter. Bu nedenle RFQ'ya bir **çapraz tutarlılık kuralı** yazdım: (dolu şişe × şişe/koli) + ambalaj ≈ koli brüt; (koli brüt × koli/palet) + palet ≈ yüklü palet brüt. **Tutmuyorsa sayı kullanılmıyor.** | Bu, gelen paketleme verisinin **tek doğrulama mekanizmasıdır** — üçüncü taraf kaynağımız yok | `T-882` |
| **İP-884** | `navlun-lojistik-uzmani` | **2.12 (yaz yükleme / thermal liner / reefer) zorunlu alan YAPILMADI.** `T-302`'nin 13. maddesiydi. Zorunlu alan sayısını kendi başıma artırmadım çünkü her ek zorunlu alan cevap oranını düşürüyor. `lojistik.yaml → sicaklik_riski` bunu gerektiriyorsa **siz söylerseniz** zorunluya çekilir. | Sıcaklık riski modelde ayrı bir blok; girdisi RFQ'dan gelmeli | `T-882` |
| **İP-885** | `gumruk-vergi-uzmani` | **`T-162` (fatura beyanı değer eşiği) `UNKNOWN` olduğu için RFQ 6.13(b) eşiği rakamsız soruyor.** Eşik bilinirse soru *"X EUR'yu aşan sevkiyatlarda EUR.1 düzenler misiniz"* hâline gelir ve **bağlayıcı** olur. Şu hâliyle üretici "duruma göre" diyebilir. | RFQ'nun bağlayıcılığı doğrudan sizdeki bir `UNKNOWN`'a bağlı | `T-883` |
| **İP-886** | `gumruk-vergi-uzmani` | **OD-4 (çıkış ülkesi) her menşeye aynı sorulmuyor olabilir.** Şili için kısıt netti (yalnızca Şili, çapraz kümülasyon yok). **AB menşeleri için aynı kesinlik var mı?** RFQ şu an herkese aynı soruyu soruyor — ayrım varsa soru menşe grubuna göre farklılaşmalı. | Aynı soruyu herkese sormak zararsız görünüyor ama **yanlış yerde konsolidasyona izin vermek** −%11,765'tir | `T-883` |
| **İP-887** | `finans-fizibilite` | **RFQ'da M6 cevapsızlığı `DOC_FAIL` cezalı değerlendiriliyor — bu bir modelleme kuralıdır.** Yani cevap gelmeyen tedarikçi için tavan otomatik olarak **256,34** (Y, N grubu) okunuyor, **290,51** değil. Bu kuralı modele taşırken `status` etiketinin `ASSUMPTION` olması gerekir, `FACT` değil. | Ceza kuralı modelin **aleyhimize** sapmasını sağlıyor — doğru yön, ama etiketi doğru olmalı | — |
| **İP-888** | `finans-fizibilite` | **M2/M3/M4 gelmezse alternatif "bant ile devam" seçeneği var (T-884 seçenek B).** O senaryoda `paketli_sise_hacim_m3` **%38 belirsizlikle** modele girer. **Bu belirsizliği kabul edip etmeyeceğiniz sizin kararınız** — ben yalnızca seçeneği görünür kıldım. | Başkanın `T-884` kararı sizin kabul sınırınıza bağlı olabilir | `T-884` |
| **İP-889** | `seytanin-avukati` | **Zorunlu alan listesi bir "cevap oranı" bahsidir ve ölçülmemiştir.** RFQ v2.2 ile SUMMARY SHEET 25 → 27 satır, M5/M6 alt sorularıyla ~15 yeni cevap alanı. `rfq-alan-kontrolu.md` §5.1 zaten uyarmıştı: uzun RFQ = daha az cevap. **Bu turda bu riski azaltmadım, artırdım.** | En temiz kırmızı takım hedefi: şablonu tedarikçi gibi doldurup **hangi zorunlu alanın kaçamak cevapla geçilebildiğini** göstermek | — |
| **İP-890** | `turkiye-pazar-kasifi` | **M8 (Türkiye ihracat geçmişi) dışarıdan öğrenilemiyor — `T-464` cevabınız bunu kanıtladı ("bulunamadı ≠ yok").** Bu yüzden alan zorunlu yapıldı ama **eleme kuralı uygulanmadı**: sayısal model girdisi beslemiyor. Eğer ileride kanal tarafında bir "ithal marka geçmişi" izi bulursanız, o iz M8'in **bağımsız doğrulaması** olur. | Tedarikçi beyanının tek dış kontrolü sizin kanal taramanız | — |

---

## finans-fizibilite (TUR 3A)

```yaml
ajan:   finans-fizibilite
tur:    TUR 3A — MODEL AUDIT + ROUND-TRIP ASSERTIONS
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md DOKUNMA listesindedir ve DEGISTIRILMEMISTIR.
         Bu dosya baskanin merge edecegi PARCA kayittir.
         BUNLAR SONUC DEGILDIR, IPUCUDUR — hicbiri baska bir ajanin alaninda
         KARAR uretmez. Bu turda YENI ARASTIRMA YAPILMAMISTIR."
```

---

### İP-F11 → `kanal-marj-uzmani` · **`LEDGER_UNIQUENESS` ÖNERİSİ İSİM TABANLIDIR VE `K6a`'YI GÖREMEZ**

`K6` şunu istedi: *"her ekonomik kalem defterde tam bir kez görünmelidir;
aynı kimlik iki satırda düşülüyorsa `CIFT_SAYIM` hatası verilmelidir."*

Uygulandı ve çalışıyor. **Ama önerinin ima ettiğinden dar kapsamlı:**

| Çift sayım tipi | Yakalanır mı |
|---|---|
| Aynı kalem, **aynı ad**, iki kez | ✅ istisna fırlatır |
| **Aynı ekonomik olay, iki farklı ad** | ⛔ **görünmez geçer** |

`K6a` ikinci tiptir (`L5::TR_yurt_ici_lojistik` ↔ `d` sepetindeki lojistik
bedeli). İkisinin `kalem_kimligi`'si farklıdır; defter ikisini de kabul eder.

**İpucu:** yakalayabilecek tek şey `payer` + `receiver` + `layer` üçlüsünün
**çakışma denetimidir** — ve o üçlü, tutar bilinmese bile **bilinebilir**.
"Kim ödüyor, kime, hangi katmanda" sorusu bir **tutar sorusu değildir.**
→ ticket **`T-861`**

---

### İP-F12 → `kanal-marj-uzmani` · **`f` ALANININ BİRİMİ ENGINE'İN BEKLEDİĞİ BİRİM DEĞİL**

`K7` gereği engine artık `f_per_bottle`'ı **girdi olarak reddediyor**;
yalnızca `F_total` + `Q_ithal` kabul edip türevi kendisi hesaplıyor
(test `TVK-P4`: `f@5.000 = 60,00`, `f@100.000 = 3,00`, `f·Q` sabit).

Ama `kanal.yaml → f_listeleme_bedeli_sise_basi` hâlâ `unit: TRY/sise`.
TUR 7'de gelecek gerçek sayı **bir dönem toplamı** olacaktır
("SKU başına X TL giriş bedeli"), şişe başı bir sayı değil.

> **Alan şişe başı kaldığı sürece, doldurulduğu an içine gizli bir hacim
> varsayımı gömülür** ve `K7`'nin ölçtüğü **38,00 TL/şişelik ölçek etkisi
> yeniden görünmez olur** — ki bu, hacim ekseninin bugünkü toplam etkisinin
> (`+20,20 TL`) **iki katıdır.**

Aynısı `d_geri_akan_bedeller_pct` için de geçerlidir (`d_var` + `D_fix`).
→ ticket **`T-863`**

---

### İP-F13 → `seytanin-avukati` · **30/30 GEÇEN BİR TEST PAKETİ BİR SALDIRI HEDEFİDİR**

`T-619`'un dersi şuydu: **yanlış bir assertion hatayı "test edilmiş"
damgasıyla mühürler.** Bu risk, bu turun **kendi çıktısı** için de geçerlidir:

- 30 testin beklenen değerlerinin **tamamı tek kaynaktan** gelir
  (`kanal-bacagi-hata-listesi.md` + `kanal-katman-matrah-haritasi.md` §6.2)
- cebri kuran ajan ile testi yazan ajan **aynıdır**
- **bağımsız ikinci bir uygulama yoktur**

`R8-K`'nın kanıtladığı tek şey **iç tutarlılıktır.** `R8K_ROUNDTRIP_OK =
EVET × 2.700` satırı okuyucuya "kanal bacağı doğrulandı" izlenimi verir;
doğrulanan şey **tutarlılıktır, doğruluk değildir.**

**Bağımsızlığı olan tek test `INV::L6_ZINCIRDE_YOK`'tur** — çünkü bir sayıyı
değil bir **yapısal özelliği** sınar ve beklenen değerini spesifikasyondan
almaz.
→ ticket **`T-862`**

---

### İP-F14 → `gumruk-vergi-uzmani` · **`R8-K` `d`'NİN MATRAHINI TEST EDEMEZ — ÇÜNKÜ ONU VARSAYAR**

`kanal-marj-uzmani` `B-8`'de şunu işaretledi: `CRM/B2B` kaleminin matrahı
**"kasa çıkışı cirosu"**, yani `L8` olabilir. Öyleyse `d·L6` **sistematik
eksik sayımdır** (`L8 > L6`).

> **`R8-K` bunu göremez** — çünkü `R8-K` geri inşasında `d`'yi zaten `L6`
> matrahında varsayar. **Bir round-trip kendi varsayımını test edemez.**

Bu, `T-942`'nin uyardığı boşluğun **bir üst katıdır**: o *"doğrulama yok"*
diyordu; buradaki risk *"doğrulama var ama yanlış şeyi doğruluyor"*dur.

---

### İP-F15 → `navlun-lojistik-uzmani` · **TR-İÇİ LOJİSTİK KALEMİ ARTIK ÇİFT SAYIM UYARISI TAŞIYOR**

`L5::TR_yurt_ici_lojistik_LCL_*` kaleminin `not_` alanına şu yazıldı:

> *"⚠ TESLİM NOKTASI TANIMI YAZILI DEĞİL → `B-13` / `T-618` (zincirin
> lojistik bedeliyle ÖRTÜŞME riski)"*

`EV-2026-08-10-329`'un hangi teslim noktasına kadar olduğu (**fabrika/antrepo
→ zincirin merkez deposu** mu, **→ mağaza** mı) doğrulanmadan bu kalemin
`d` sepetiyle örtüşüp örtüşmediği bilinemez. Örtüşüyorsa **aynı para iki
kez düşülüyor**; örtüşmüyorsa sorun yok — **ve hangisi olduğu yazılı değil.**
→ `T-618` **AÇIK**

---

### İP-F16 → `mevzuat-ruhsat-uzmani` · **`TUR 2.5` İPUCU (`İP-F1`) HÂLÂ AÇIK VE ARTIK GÖRÜNÜR**

Bandrol (`2,36073`), TADAB hizmet bedeli (`0,1587`) ve ruhsat sabit maliyeti
2026 değerleridir; model hedef tarihi **2027**'dir. ÖTV için `T-921` ile
uygulanan **ufuk denetimi** bu üç kalem için **yoktur**.

TUR 3A'da bu üç kalem `OK` damgası aldı (metadata'ları tamamlandı, tutarları
biliniyor) — yani **`BLOCKED_INPUT` listesinde görünmüyorlar.** Bu, sorunun
çözüldüğü anlamına **gelmez**: `status: FACT/ESTIMATE` doğrudur ama
**BASE_DATE için** doğrudur, hedef tarih için değil.
→ ticket **`T-858`** (TUR 2.5'te açıldı, hâlâ geçerli)

---

### İP-F17 → `yatirim-komitesi-baskani` · **`BLOCKED_INPUT` BİR ÇÖZÜM DEĞİL, BİR ETİKETTİR**

TUR 2.5'te 26 kalem **sessizce `0`** geçiyordu; TUR 3A'da **adıyla ve eksik
alanıyla** çıktıya basılıyor. Bu bir iyileşmedir.

> **Ama sayı hâlâ 26 kalem eksik hesaplanmaktadır.**
> `kanal-marj-uzmani`'nın ölçtüğü mertebe: `K7` (38,00) + `K11` (19,38) +
> `K12` (27,55) ≈ **85 TL/şişe** = `TGT_799 · CHAIN · BASE` tavanının
> (**272,83**) **%31'i** — ve **hepsi tek yönlü: aşağı.**

`272,83` bir orta nokta değil, **bir üst sınırın üst sınırıdır.**
Karar eşiği bir tavanı bir gözlemle karşılaştırıyorsa, **karşılaştırmanın
bir tarafı sistematik olarak şişkindir.**
→ ticket **`T-864`**

---

---

# TUR 3.25 ÇAPRAZ İPUÇLARI

> Ajanların `99-ops/_parts/*-tur325.md` fragment'lerinden değiştirilmeden aktarıldı.

## navlun-lojistik-uzmani (TUR 3.25)

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 3.25 — FORWARDER RFQ PAKETI
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md bu turda DOKUNMA listesindedir. Bunlar SONUC DEGIL, IPUCUDUR."
```

---

### İ-3251 → `global-sourcing-kasifi`

**İpucu:** Forwarder RFQ'su ile tedarikçi RFQ'su **aynı beş fiziksel alanı**
sorar: koli formatı, koli ölçüsü, koli brüt ağırlığı, şişe formu/boyutu, palet
konfigürasyonu. İki RFQ **aynı anda** gönderilirse, iki taraftan gelen sayılar
birbirini **çapraz doğrular** (`C-301` üçüncü bir bağımsız kaynağa kavuşur).
Ayrı zamanlarda gönderilirse, forwarder teklifi tedarikçi konfigürasyonu
gelince yeniden alınmak zorunda kalabilir.

**Neden önemli:** Sıra yanlış olursa **aynı teklifi iki kez istemek** gerekir —
ve ikinci istek forwarder gözünde ciddiyet kaybıdır. → `T-822`

---

### İ-3252 → `gumruk-vergi-uzmani`

**İpucu:** RFQ §9 E1, sigortayı **CIF + %10** üzerinden ve **ayrı, opsiyonel
fiyat** olarak istiyor. İki nokta senin alanını ilgilendiriyor:
1. Sigorta primi **gümrük kıymetine** girer (CIF'in "I"si) → vergi matrahını
   büyütür. Ben primi **hesaplamadım**, yalnızca istedim.
2. Forwarder'dan gelecek teklif **FOB/FCA** bazlıdır (RFQ §2). Tedarikçiden
   **CIF** teklifi gelirse navlun+sigorta zaten fiyatın içindedir →
   **çift sayım riski** (`lojistik.yaml → sigorta.cift_sayim_uyarisi`).

**Neden önemli:** Aynı navlun hem lojistik gideri hem CIF bileşeni sayılırsa
matrah da maliyet de şişer. Hangi Incoterm'de hangisinin sayılacağı
`matrah-sirasi.md`'de nettir; teklif geldiğinde **hangi Incoterm'de geldiğine**
bakılmalıdır.

---

### İ-3253 → `mevzuat-ruhsat-uzmani`

**İpucu:** RFQ §9 E6, antrepo işletmecisine *"alkollü içki için yetkili mi"*
sorusunu soruyor — ama bu **tesisin kendi beyanıdır**, mevzuat tespiti değildir.
Gelen cevap `FACT` sayılamaz; yalnızca *"tesis şöyle beyan etti"* olarak
kaydedilecektir.

Ayrıca RFQ §10.4 ve EK-1 D6, forwarder'a **15/30/60 günlük bekleme**
senaryolarının operasyonel maliyetini soruyor. **Gün sayısı bende değil,
sende** (`T-301`). Ben yalnızca üç köşe verdim ki maliyet fonksiyonu
çıkarılabilsin.

**Neden önemli:** Bekleme süresi 30+ güne çıkarsa `lcl-vs-fcl-pilot.md` §6'daki
FCL önerisi **tersine döner** (LCL'de konteyner iade baskısı yoktur).

---

### İ-3254 → `finans-fizibilite`

**İpucu:** Üç forwarder'dan üç teklif gelirse **ortalamaları alınmamalıdır.**
Üçü ayrı satır olarak taşınmalı; aralarındaki fark, `senaryolar.yaml`'daki
navlun duyarlılık bandının **ilk kanıtlı dayanağı** olacaktır (`T-913` §B-5).
Bugün o band bir `ASSUMPTION`'dır.

TUR 2'de aynı port pair'de iki teklif arasında **%31** (Barcelona) ve **%110**
(Melbourne) fark ölçülmüştü. Yani forwarderlar arası fark, senaryo bandı kadar
geniş olabilir — **ortalama almak bu bilgiyi imha eder.**

---

### İ-3255 → `yatirim-komitesi-baskani`

**İpucu:** `forwarder-contact-pack.md` §2'de bir **hata payı sıfır** durumu
var: doğrudan e-posta ile ulaşılabilen hedef sayısı **3**, `T-304`'ün kapanma
koşulu da **3 yazılı kotasyon**. Biri cevap vermezse koşul sağlanmaz.

**Neden önemli:** Gönderim onayı verilirse, 5 hedefin **hepsine** gönderilmesi
(form ve `NEEDS_CONTACT` kanalları dâhil) gerekir — yalnızca "kolay üçüne"
gönderim, tek bir sessizlikte `T-304`'ü yeniden açar.

---

### İ-3256 → `seytanin-avukati`

**İpucu:** RFQ §5.3'te forwarder'a **kendi kanıtımızı gösteriyoruz**
(İspanya origin 349 EUR, base ocean ≈300 USD). Bu bilinçli bir tercihtir —
teklifin doğru formatta gelmesi için. Ama bir kırmızı takım sorusu doğurur:

> **Fiyat çapası verilmiş bir RFQ, teklifi o çapaya doğru çeker mi?**

Karşı argüman: verilen sayılar **navlun** değil, **local charge** ve
**herkese açık armatör tarifesi**dir; pazarlık kozu değil, format gerekçesidir.
Hedef hacim, tedarikçi fiyatı ve marj beklentisi **paylaşılmamıştır**.
Yine de bu, saldırıya açık bir tasarım kararıdır ve **bilinçli** yapılmıştır.

---
