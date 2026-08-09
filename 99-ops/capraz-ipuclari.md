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
