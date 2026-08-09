# AJAN RAPORU — GÜMRÜK & VERGİ (TUR 1)

```yaml
ajan:               gumruk-vergi-uzmani
tur:                TUR 1
tarih:              2026-08-09
durum:              SUBMITTED
```

---

## 1. YÖNETİCİ ÖZETİ

750 ml şişelenmiş köpüksüz şarabın Türkiye'ye ithalinde uygulanan tüm vergi
kalemleri, matrahları ve hesap sırası T1/T2 resmî kaynaklarla kurulmuş ve
`30-vergi-gumruk/matrah-sirasi.md` ile `80-model/inputs/vergi.yaml` dosyalarına
işlenmiştir. **En kritik tek bulgu:** şarapta oransal ÖTV **%0**'dır ve vergi
tamamen **asgari maktu tutar** üzerinden alınır — **71,2692 TL/litre**, yani
750 ml şişe başına **53,4519 TL**, yürürlük **3/7/2026** (`EV-2026-08-09-111`).
Bu tutar CIF'ten tamamen bağımsızdır; ucuz şarap ile pahalı şarap aynı ÖTV'yi
öder, dolayısıyla **fiyat/performans segmenti vergi tarafından orantısız biçimde
cezalandırılmaktadır.** İkinci kritik bulgu: **Gümrük Birliği şarabı kapsamaz** —
AB menşeli şarapta gümrük vergisi %50, ABD dâhil "diğer ülkeler"de **%70**'tir
(`EV-2026-08-09-103`, `EV-2026-08-09-104`) ve köpüksüz şarapta AB için tarife
kontenjanı **yoktur** (`EV-2026-08-09-108`). Üçüncüsü: ÖTV maktu tutarı Ocak ve
Temmuz aylarında Yİ-ÜFE ile **kendiliğinden** artmaktadır; son artış 6 ayda
**+%16,09**'dur (`EV-2026-08-09-114`), bu nedenle modelde sabit sayı olarak
kullanılamaz.

---

## 2. BULGULAR

### B-1: GTİP — 750 ml köpüksüz şarap 2204.21'dir ve 12 haneli alt kod vergi yükünü değiştirmez

```yaml
claim:          750 ml şişelenmiş köpüksüz şarap 2204.21 (muhtevası 2 litreyi geçmeyen kaplarda) altındadır; 2204.21/22/29 altındaki 113 GTİP satırının tamamında gümrük vergisi oranları özdeştir
value:          2204.21.xx.xx.xx
unit:           GTİP
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-101, EV-2026-08-09-102
effective_date: 2026-01-01
katman:         —
```

**Gerekçe:** "2204.21 | Muhtevası 2 litre veya daha az kaplarda olanlar" ifadesi
Cumhurbaşkanı Kararı 4559 ekli tabloda birebir yer alıyor. Ayrıca 2026 İthalat
Rejimi Kararı I sayılı Liste'nin 21–22. Fasıllar sayfasındaki 2204.21/22/29
satırları programatik olarak gruplandırıldı: **AB,BK = 50** ve **DÜ = 70**
değerleri 113 satırın tamamında tek değer olarak çıktı. ÖTV ise 22.04 **pozisyon**
seviyesinde belirlenmiştir. Dolayısıyla ABV veya PDO/PGI'ye dayalı 12 haneli alt
kırılım **vergi yükünü değiştirmez** — bu, yapının en dayanıklı kısmıdır.

**Kritik ayrım 12 hanede değil, 4/6 hanededir:** köpüklü mü (2204.10), hacim
≤ 2 lt mi (2204.21), aromatize mi (22.05).

---

### B-2: ÖTV — oransal %0, asgari maktu 71,2692 TL/litre ⇒ 750 ml için 53,4519 TL/şişe

```yaml
claim:          22.04 köpüksüz taze üzüm şarabında nispi ÖTV oranı %0'dır; vergi tamamen asgari maktu tutar üzerinden, her bir litre itibarıyla alınır
value:          71,2692
unit:           TL/litre  (750 ml için 53,4519 TL/şişe)
status:         FACT
tier:           T2  (dayanağı T1: ÖTVK md.11/2-a, md.11/5, md.12/3)
evidence_id:    EV-2026-08-09-111 (tutar), EV-2026-08-09-110 (oran %0), EV-2026-08-09-113 (birim + kural), EV-2026-08-09-116 (750 ml hesap yöntemi)
effective_date: 2026-07-03
katman:         L3→L4 geçişi
```

**Gerekçe:** ÖTV Kanunu md.11/5 (T1): "(III) sayılı listenin (A) cetvelindeki
mallar için asgari maktu vergi tutarlarına göre hesaplanacak vergi tutarından az
olmamak üzere **yalnızca nispi vergi** uygulanır." Nispi oran %0 olduğundan
karşılaştırma her zaman maktu lehine sonuçlanır. md.11/2-a (T1): 22.04 için
asgari maktu tutar "**her bir litre**" itibarıyla uygulanır — ABV'den ve şişe
adedinden bağımsızdır (bira 1 litredeki her alkol derecesi, distile içkiler
içerdiği alkolün her litresi üzerinden vergilenirken şarap düz litre üzerinden).

ÖTV (III)/A Uygulama Genel Tebliği'nin resmî örneği (T1) hesap yöntemini birebir
gösteriyor: *75 cl'lik bir şişe köpüklü şarap → 0,75 lt × asgari maktu tutar*.
Aynı yöntem 22.04 için geçerli: **0,75 × 71,2692 = 53,4519 TL/şişe.**

**Neden bu projenin en kritik sayısı:** Maktu ÖTV, CIF'ten bağımsız olduğu için
ucuz üründe orantısız ağırdır. CIF = 50 TL ise ÖTV tek başına CIF'in %107'si;
CIF = 300 TL ise %18'i. Projenin çekirdek hipotezi (fiyat/performans segmenti)
tam olarak bu asimetriyle çarpışır.

---

### B-3: ÖTV maktu tutarı Ocak ve Temmuz'da kendiliğinden artıyor — son artış +%16,09

```yaml
claim:          (III) sayılı listedeki asgari maktu tutarlar ocak ve temmuz aylarında TÜİK ÜFE'nin son 6 aylık değişimi oranında, ayrı bir karara gerek olmaksızın yeniden belirlenmiş sayılır
value:          61,3914 → 71,2692  (+%16,09, 6 ay)
unit:           TL/litre
status:         FACT
tier:           T1 (mekanizma) / T2 (gerçekleşen tutar)
evidence_id:    EV-2026-08-09-114 (mekanizma), EV-2026-08-09-111 & -112 (tutarlar)
effective_date: 2026-07-03
katman:         —
```

**Gerekçe:** ÖTV Kanunu md.12/3 tutarların "**yeniden belirlenmiş sayılır**"
şeklinde otomatik güncellendiğini söylüyor. GİB'in yayımladığı listenin başlığı
bunu doğruluyor: *"(4760 sayılı Özel Tüketim Vergisi Kanununun (12/3) maddesi
uyarınca güncellenen liste) (Yürürlük: 3/7/2026)"*.

**Türetme zinciri (+%16,09):** 71,2692 ÷ 61,3914 = 1,16092 → +%16,09.

**Model sonucu:** ÖTV tutarı modelde **sabit alınamaz.** Model hedef tarihi
2027 Ocak'ı geçiyorsa bugünkü tutar geçersizdir. Ticket **T-104** açıldı.
Bu kanıtın `ttl` süresi **30 gün**dür — projedeki en kısa TTL'lerden biridir.

---

### B-4: Gümrük vergisi — AB/BK/Şili %50, ABD ve diğer Yeni Dünya %70

```yaml
claim:          2204.21 gümrük vergisi menşeye göre değişir; Gümrük Birliği şarabı kapsamaz
value:          AB+BK %50 · Şili %50 · K.Makedonya %35 · B-Hersek/G.Kore/Singapur/Kosova %0 · Venezuela %35 · BAE %49 · Gürcistan/Malezya/TPS-OIC/D-8 %70 · DÜ (ABD, G.Afrika, Avustralya, Arjantin) %70
unit:           %
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-103, -104, -105, -106
effective_date: 2026-01-01
katman:         L2→L4 geçişi
```

**Gerekçe:** 2026 İthalat Rejimi Kararı (3350) ekli **I sayılı Liste — Tarım
Ürünleri**, 21–22. Fasıllar. Şarap sanayi ürünü değil **tarım ürünüdür**; bu
nedenle Gümrük Birliği'nin sıfır tarife rejimi uygulanmaz. Sütun başlıkları
Ticaret Bakanlığı'nın "İçindekiler ve Kısaltmalar" belgesiyle doğrulandı
(AB = Avrupa Birliği Üyesi Ülkeler, BK = Birleşik Krallık, DÜ = Diğer Ülkeler).

Dipnotlar (aynı sayfada, T1):
- *"(1) Kuzey Makedonya Cumhuriyeti için DÜ sütununda yer alan gümrük vergisinin
  %50'si uygulanır."* → %35
- *"(2) Şili Cumhuriyeti için gümrük vergisi %50 olarak uygulanır."*

**Benchmark ürüne etkisi:** Benchmark (Gold Country, **California/ABD**) DÜ
sütunundadır → **%70**. Yani 599,90 TL'lik rafın arkasında en pahalı gümrük
rejimi vardır.

---

### B-5: Köpüksüz şarapta AB tarife kontenjanı YOKTUR

```yaml
claim:          AB menşeli tarım ürünleri tarife kontenjanı şarapta yalnız 2204.10 (köpüklü) için açılmıştır; 2204.21 köpüksüz şarap için AB, BK veya Şili kontenjanı yoktur
value:          AB 2204.10: 750 hl/yıl @ %35 · BK 2204.10: 125 hl/yıl @ %35 · İsviçre/Lihtenştayn 2204.21: 30.000 lt/yıl @ DÜ'nün %50'si (=%35) · AB 2204.21: YOK
unit:           hl / litre / %
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-108, EV-2026-08-09-109
effective_date: 2007-01-01 (AB Kararı) / 2021-10-01 (İsviçre Kararı)
katman:         —
```

**Gerekçe:** 1/98 sayılı Türkiye-AB Ortaklık Konseyi Kararı çerçevesindeki
2006/11439 sayılı Karar tam metin olarak indirildi ve 22. fasıl satırları
tarandı: tabloda **yalnız 2204.10 "Köpüklü şaraplar — 750 hl — 01.01-31.12 — 35"**
satırı var. 2204.21 satırı **yok**. Aynı tarama Birleşik Krallık (2204.10,
125 hl, %35) ve Şili (hiç şarap satırı yok) kararları için de yapıldı.

Tek istisna İsviçre/Lihtenştayn: 2204.21 için 30.000 lt/yıl kontenjan, dipnot (i)
ile DÜ oranının %50'si. Tüm ithalatçılar için toplam miktardır ve İsviçre şarabı
fiyat/performans segmentinde değildir — kayda geçirildi, pratik değeri düşüktür.

**Sonuç:** AB menşeli 750 ml şarapta indirim yolu yoktur; **%50 tam oran** uygulanır.

---

### B-6: Matrah zinciri — Gümrük Vergisi ÖTV matrahına, ÖTV de KDV matrahına girer

```yaml
claim:          ÖTV matrahı = CIF + Gümrük Vergisi + ithalatta ödenen diğer vergi/resim/harç/pay (ÖTV ve KDV hariç) + tescile kadarki diğer giderler; KDV matrahı ise bunun üzerine ÖTV'yi de ekler
value:          "ÖTV matrahı ⊃ Gümrük Vergisi;  KDV matrahı ⊃ Gümrük Vergisi + ÖTV"
unit:           —
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-115 (ÖTV matrahı), EV-2026-08-09-117 (KDV matrahı)
effective_date: 2015-08-08 (tebliğ) / 1985-01-01 (KDVK md.21)
katman:         L3→L4
```

**Gerekçe:** ÖTV Kanunu md.11/3 (T1), (III) sayılı liste mallarında matrahı
"**hesaplanacak özel tüketim vergisi hariç**, katma değer vergisi matrahını
oluşturan unsurlardan" ibaret sayıyor. ÖTV (III)/A Uygulama Genel Tebliği'nin
"İthalatta Matrah" bölümü bunu üç kalemle açıyor: gümrük vergisi tarhına esas
kıymet + ithalat sırasında ödenen her türlü vergi (**ÖTV ve KDV hariç**), resim,
harç ve paylar + tescile kadar yapılan diğer gider ve ödemeler.

KDV Kanunu md.21/b "ithalat sırasında ödenen **her türlü vergi**, resim, harç ve
paylar" diyor; ÖTV ithalatta ödenen bir vergidir → KDV matrahına dâhildir.
Bunun karşı-kanıtı yine ÖTVK md.11/3'ün kendisidir: ÖTV, kendi matrahından
**açıkça hariç tutulmak zorunda kalınmıştır** — aksi hâlde KDV matrahının
içinde yer alacaktı. İki hüküm birbirini doğruluyor.

**Sıra:** Gümrük Vergisi → (İGV: yok) → KKDF → ÖTV → KDV.

---

### B-7: KDV %20, şarap indirimli oran listelerinde değil

```yaml
claim:          Genel KDV oranı %20'dir ve 2204.21 şarap 2007/13033 sayılı Karara ekli (I) ve (II) sayılı indirimli oran listelerinde yer almaz
value:          20
unit:           %
status:         FACT
tier:           T2 (dayanağı T1: 7346 sayılı CBK, RG 07.07.2023/32241)
evidence_id:    EV-2026-08-09-118
effective_date: 2023-07-10
katman:         L3→L4
```

**Gerekçe:** GİB'in yayımladığı 2007/13033 sayılı Karar konsolide metni,
md.1/a'yı *"(7346 sayılı Cumhurbaşkanı Kararı ile değişen ibare. Yürürlük:
10/07/2023) **% 20**"* olarak gösteriyor. (I) sayılı listenin "A) GIDA MADDELERİ"
bölümünün 22. fasıl satırı yalnızca 22.01, 2202.10.00.00.19, 2202.90, **2204.30**
(üzüm şırası), 2209.00.91/99 ve bazı gazoz GTİP'lerini kapsıyor — **2204.21 yok.**
Konsolide metnin tamamında "2204" yalnızca 2204.30 olarak geçiyor.

**Kaynak zayıflığı — dürüst not:** Dayanak T1 belge (7346 sayılı CBK'nın Resmî
Gazete PDF'i) **taranmış görüntüdür**, metin katmanı yoktur ve OCR aracı
mevcut ortamda kurulu değildir. Bu nedenle oran, T1 belgenin kendisinden değil,
GİB'in (T2) konsolide metninden alınmıştır.

---

### B-8: KKDF — yalnız üç vadeli ödeme şeklinde %6; peşin ödemede doğmaz

```yaml
claim:          Kabul kredili, vadeli akreditif ve mal mukabili ödeme şekillerine göre yapılan ithalatta KKDF kesintisi oranı %6'dır
value:          6
unit:           %
status:         FACT (oran) / UNKNOWN (matrah tanımı)
tier:           T1
evidence_id:    EV-2026-08-09-119
effective_date: 2011-10-13
katman:         L3→L4
```

**Gerekçe:** 12/10/2011 tarihli ve 2011/2304 sayılı Karar eki Karar md.4
(RG 13/10/2011, 28083), tam metin: *"Kabul kredili, vadeli akreditif ve mal
mukabili ödeme şekillerine göre yapılan ithalatta Kaynak Kullanımını Destekleme
Fonu kesintisi oranı % 6 olarak tespit edilmiştir."*

Oran **yalnızca** bu üç ödeme şekli için tanımlanmıştır; peşin ödemede KKDF
doğmaz. **Matrahın tanımı Karar metninde yoktur** — mal bedeli mi, CIF mi,
vadeye bırakılan tutar mı belirsizdir. Peşin ödeme baz senaryosunda etkisizdir;
vadeli senaryoda etkilidir. Ticket **T-105**.

---

### B-9: Gümrük kıymeti CIF esaslıdır — navlun ve sigorta vergilendirilir

```yaml
claim:          Türkiye'deki giriş yerine kadar navlun, sigorta, yükleme ve elleçleme gümrük kıymetine dâhildir; giriş yerinden sonrası, satın alma komisyonu ve Türkiye'de ödenecek ithalat vergileri hariçtir
value:          navlun+sigorta+giriş yerine kadar elleçleme+ambalaj+satış koşulu royalti DAHİL; yurt içi nakliye, satın alma komisyonu, faiz (koşullu), çoğaltma hakkı HARİÇ
unit:           —
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-120, EV-2026-08-09-121
effective_date: 2000-02-05
katman:         L1→L2→L3
```

**Gerekçe:** Gümrük Kanunu md.27/1-e (T1) navlun, sigorta ve giriş yerine kadar
yükleme/elleçlemeyi fiilen ödenen fiyata ekliyor; md.27/1-a ambalaj bedelini ve
satın alma dışındaki komisyonları; md.27/1-c satış koşulu olan royalti/lisans
bedelini. md.28 ise giriş yerinden sonraki nakliye/sigortayı (a), finansman
faizini (c), çoğaltma hakkı ödemelerini (d), satın alma komisyonlarını (e) ve
Türkiye'de ödenecek ithalat vergilerini (f) hariç tutuyor.

**Kritik operasyonel sonuç:** md.28 hariç tutmaları giderlerin fiyattan
**ayırt edilebilir** olmasına bağlıdır. "Door-to-door" tek kalem faturada
liman-sonrası masraf ayrıştırılamaz ve **tamamı vergilendirilir.**
Navlunun her 1 TL'si DÜ menşede ~2,04 TL landed maliyet yaratır
(1 × 1,70 × 1,20). Çapraz ipucu olarak `navlun-lojistik-uzmani`'na bırakıldı.

---

### B-10: Antrepoda vergi doğmaz — vergi serbest dolaşıma giriş beyannamesinin tescilinde doğar

```yaml
claim:          İthalatta gümrük yükümlülüğü serbest dolaşıma giriş beyannamesinin tescil tarihinde başlar; antrepoda kalış süresi sınırsızdır
value:          vergi doğuş anı = serbest dolaşıma giriş beyannamesi tescil tarihi
unit:           —
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-122
effective_date: 2009-07-07 (md.181 değişik hâli)
katman:         cash_tax_timing
```

**Gerekçe:** Gümrük Kanunu md.181/1-a (T1) yükümlülüğü tescil tarihine bağlıyor;
md.93/1-a antrepo rejimini "ithalat vergilerine ve ticaret politikası önlemlerine
tabi tutulmamış ve serbest dolaşıma girmemiş eşya" için tanımlıyor; md.101/1
kalış süresini sınırsız bırakıyor.

**Sonuç:** Antrepo, vergi ödemesini satış takvimine yaklaştırarak
`peak_cash_requirement`'ı düşürür. **Ancak gizli bir karşı risk vardır:** ÖTV
maktu tutarı Ocak/Temmuz'da artar, tescil tarihi ötelendikçe daha yüksek ÖTV
uygulanır. **Kısmi çekiş** (partial release) imkânı bu turda doğrulanamadı —
ticket **T-101** ile `navlun-lojistik-uzmani`'na devredildi.

---

### B-11: ÖTV ithalatçı için indirilemez — doğrudan maliyettir

```yaml
claim:          (III) sayılı liste malları bir defaya mahsus ÖTV'ye tabidir; indirim yalnız verginin aynı listedeki başka bir malın imalinde kullanılması hâlinde mümkündür
value:          ÖTV indirilemez ⇒ ekonomik maliyettir
unit:           —
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-124, EV-2026-08-09-123 (ödeme anı)
effective_date: 2002-08-01
katman:         L4 → L5 (ÖTV L5'e taşınır)
```

**Gerekçe:** ÖTV Kanunu md.1/1-c + md.1/1 son cümlesi: (III) sayılı liste
mallarının ithalatı "**bir defaya mahsus olmak üzere**" ÖTV'ye tabidir. md.9:
indirim yalnızca "malların, yer aldığı listedeki başka bir malın imalinde
kullanılması hâlinde" mümkündür. Şişelenmiş bitmiş ürünü ithal edip yurt içinde
satan bir ithalatçı imalatçı değildir → **ÖTV'yi indiremez.** Bu, ÖTV'nin KDV'den
temel farkıdır ve KDV gibi iki perspektifle gösterilemez.

md.14/3: ithalatta ÖTV gümrük idaresince hesaplanır ve **ithalat vergileri ile
aynı zamanda ödenir.**

---

### B-12: İlave Gümrük Vergisi yok; gözetim uygulaması tespit edilemedi

```yaml
claim:          2204, İGV Kararı (3351) ekli tablolarında yer almaz; 2204.21/2204.29/22.04 için yürürlükte bir İthalatta Gözetim Uygulanmasına İlişkin Tebliğ bulunamadı
value:          İGV: YOK (FACT) · Gözetim: bulunamadı (UNKNOWN)
unit:           —
status:         FACT (İGV) / UNKNOWN (gözetim)
tier:           T1 (İGV) / T2 (gözetim araması)
evidence_id:    EV-2026-08-09-107, EV-2026-08-09-125
effective_date: 2026-01-01 (İGV)
katman:         —
```

**Gerekçe (İGV):** İGV Kararı 3351'in konsolide EK-1, EK-2 ve EK-3 tabloları
indirildi ve tamamı "2204" için programatik tarandı; şarap satırı yoktur.

**Gerekçe (gözetim) — ve neden UNKNOWN:** Mevzuat Bilgi Sistemi tebliğ veri
tabanında "2204.21", "2204.29" ve "22.04" tam metin araması yapıldı; hiçbir
gözetim tebliği eşleşmedi (18 eşleşmenin tamamı TAPDK/Tarım Bakanlığı alkol
tebliğleri). Yöntem, bilinen bir gözetim GTİP'i (8536.20.10.00.11) ile kontrol
edildi ve Tebliğ 2008/11 doğru bulundu — arama çalışıyor. **Buna rağmen negatif
arama sonucu yokluğun kanıtı değildir** ve `UNKNOWN` olarak bırakıldı.

**Not:** ÖTV maktu olduğu için bir kıymet/gözetim itirazından **etkilenmez**;
yalnızca gümrük vergisi ve KDV matrahı yukarı çekilir. Yani kıymet itirazı
riski bu üründe diğer ürünlere göre daha sınırlıdır.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---------------|------------------|-----------|-------------------|
| 1 | İthalatta ödenen KDV indirilebilir mi | KDVK md.29 vd. genel mekanizma var; alkollü içki ticaretine özgü sınırlama olup olmadığı doğrulanmadı | **CRITICAL** | KDVK md.29-34 + KDV Genel Uygulama Tebliği indirim bölümü + GİB özelgeleri |
| 2 | Şarapta gözetim/referans kıymet gerçekten yok mu | Negatif arama sonucu; veri tabanı kapsamı doğrulanamadı | **CRITICAL** | Ticaret Bakanlığı İthalat Genel Müdürlüğü yürürlükteki gözetim tebliğleri listesi; gümrük müşaviri teyidi |
| 3 | Model hedef tarihinde geçerli ÖTV tutarı | `model_hedef_tarihi` TBD; ÖTV Ocak/Temmuz'da otomatik değişiyor | **CRITICAL** | `mevzuat-ruhsat-uzmani` T0 takvimi + T-104 |
| 4 | KKDF matrahının tanımı | 2011/2304 md.4 yalnız oranı belirliyor; GGM genelgelerine erişilemedi | HIGH (vadeli senaryoda) / LOW (peşinde) | GGM KKDF genelgeleri; 88/12944 konsolide metin |
| 5 | Antrepodan kısmi çekiş mümkün mü | Gümrük Yönetmeliği antrepo bölümünde açık genel hüküm bulunamadı | HIGH | T-101 → `navlun-lojistik-uzmani` |
| 6 | Menşe ispat belgesi türü (EUR.1 / fatura beyanı / REX / A.TR) | Anlaşma bazında menşe protokolleri incelenemedi | MEDIUM | 1/98 sayılı OKK menşe protokolü; Gümrük Yönetmeliği tercihli menşe hükümleri |
| 7 | 12 haneli GTİP alt kodu | TGTC 2026 (CBK 10781, RG 30/12/2025) **taranmış görüntü** olarak yayımlanmış, metin katmanı yok; TARA arama motoru CAPTCHA korumalı; ortamda OCR yok | LOW (vergiyi değiştirmiyor) | Gümrük müşaviri; TARA (manuel); AB CN 2026 (8 hane) |
| 8 | Gümrük beyannamesi damga vergisi 2026 tutarı | Araştırılmadı (öncelik düşük) | LOW | Damga Vergisi Kanunu genel tebliği (2026) |
| 9 | KDV mahsup gecikmesi / devreden KDV / iade süresi (gün) | UNKNOWN #1'e bağlı | HIGH | UNKNOWN #1 kapandıktan sonra |
| 10 | TRT bandrolü / diğer fonların şarapta uygulanabilirliği | Doğrulanmadı; TRT bandrolü radyo-TV cihazlarına özgüdür | LOW | 3093 sayılı Kanun kapsam kontrolü |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

### Ulaşılamayan resmî kaynaklar (dürüst kayıt)
- **TGTC 2026** (RG 30/12/2025, CBK 10781): 631 sayfa, **taranmış görüntü**, metin
  katmanı yok. `tesseract`/`ocrmypdf` ortamda kurulu değil.
- **7346 sayılı CBK** (RG 07.07.2023/32241): PDF **taranmış görüntü**. KDV oranı
  bu nedenle GİB konsolide metninden (T2) alındı.
- **TARA Tarife Arama Motoru** (`uygulama.gtb.gov.tr/Tara`): CAPTCHA korumalı.
- **www.gib.gov.tr** ana site: bağlantı reset ediyor; veriler `cdn.gib.gov.tr`
  üzerinden alındı.
- **2007/13033 sayılı Karar** mevzuat.gov.tr'de aranabilir metin olarak yok.
- **Gümrükler Genel Müdürlüğü KKDF genelgeleri**: bulunamadı.

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|-------------|----------------------|----------------------|-----------------|-------|
| **C-101** | mevzuat.gov.tr — 4760 sayılı Kanun konsolide (III) sayılı liste, 22.04 = **61,3914 TL/lt** (T1 / erişim 2026-08-09) | GİB — (III) sayılı liste, md.12/3 uyarınca güncellenmiş, Yürürlük 3/7/2026, 22.04 = **71,2692 TL/lt** (T2 / 2026-07-03) | Kanun metnine işlenmeyen otomatik güncelleme. ÖTVK md.12/3 tutarları "yeniden belirlenmiş sayılır" — ayrı bir CBK olmadığı için konsolide metne işlenmiyor. CBK 10799 md.12/3'ü yalnız **2026 Ocak-Haziran** için askıya almıştı; CBK 11489 (3/7/2026) ise yalnız **(B) cetveli tütün** malları için Temmuz-Aralık askısı getirdi — şarap kapsam dışı | **OPEN** (çözüm önerildi: 71,2692 kullanılsın) |

Ayrıntı: `99-ops/_parts/celiskiler-gumruk-vergi-uzmani.md`

**Çözüm önerisinin en zayıf halkası:** TÜİK Yİ-ÜFE Aralık 2025 → Haziran 2026
değişim oranının gerçekten ~%16,09 olduğu **bağımsız olarak doğrulanmadı**.

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|--------------|------|-------|-------|--------|-------------|
| vergi.yaml | `gtip.kod` | 2204.21 | GTİP | FACT | EV-2026-08-09-101 |
| vergi.yaml | `matrah_sirasi[1].oran_pct` (Gümrük Vergisi) | menşeye bağlı | % | FACT | EV-2026-08-09-103 |
| vergi.yaml | `gumruk_vergisi_oranlari_by_mense.AB_uyesi_ulkeler` | 50 | % | FACT | EV-2026-08-09-103 |
| vergi.yaml | `gumruk_vergisi_oranlari_by_mense.diger_ulkeler_DU` | 70 | % | FACT | EV-2026-08-09-104 |
| vergi.yaml | `gumruk_vergisi_oranlari_by_mense.Sili` | 50 | % | FACT | EV-2026-08-09-105 |
| vergi.yaml | `gumruk_vergisi_oranlari_by_mense.*` (B-Her/Kosova/K.Makedonya/VNZ/BAE…) | 0/0/35/35/49 | % | FACT | EV-2026-08-09-106 |
| vergi.yaml | `matrah_sirasi[2].oran_pct` (İGV) | 0 | % | FACT | EV-2026-08-09-107 |
| vergi.yaml | `matrah_sirasi[3].oran_pct` (KKDF) | 6 | % | FACT | EV-2026-08-09-119 |
| vergi.yaml | `matrah_sirasi[3].matrah_tanimi` | **null** | — | **UNKNOWN** | — |
| vergi.yaml | `matrah_sirasi[4].oran_pct` (ÖTV nispi) | 0 | % | FACT | EV-2026-08-09-110 |
| vergi.yaml | `matrah_sirasi[4].asgari_maktu_tutar` | **71,2692** | TL/litre | FACT | EV-2026-08-09-111 |
| vergi.yaml | `matrah_sirasi[4].maktu_birim` | litre | — | FACT | EV-2026-08-09-113 |
| vergi.yaml | `matrah_sirasi[4].hesap_kurali` | max(nispi; maktu×litre) | — | FACT | EV-2026-08-09-113 |
| vergi.yaml | `matrah_sirasi[4].hesaplanan_otv_try_per_750ml` | **53,4519** | TL/şişe | FACT (türetme) | EV-2026-08-09-111 + -116 |
| vergi.yaml | `matrah_sirasi[4].matrah_tanimi` | CIF+GV+KKDF (ÖTV/KDV hariç) | — | FACT | EV-2026-08-09-115 |
| vergi.yaml | `matrah_sirasi[5].oran_pct` (KDV) | 20 | % | FACT | EV-2026-08-09-118 |
| vergi.yaml | `matrah_sirasi[5].matrah_tanimi` | CIF+GV+KKDF+ÖTV+diğer | — | FACT | EV-2026-08-09-117 |
| vergi.yaml | `gumruk_kiymeti.*` | CIF esaslı, dahil/hariç kalemleri | — | FACT | EV-2026-08-09-120, -121 |
| vergi.yaml | `antrepo_rejimi.vergi_dogus_ani` | serbest dolaşıma giriş beyannamesi tescili | — | FACT | EV-2026-08-09-122 |
| vergi.yaml | `antrepo_rejimi.kismi_cekis_mumkun_mu` | **null** | — | **UNKNOWN** | — |
| vergi.yaml | `kdv_perspektifleri.a.otv_indirilebilir_mi` | false | — | FACT | EV-2026-08-09-124 |
| vergi.yaml | `kdv_perspektifleri.a.ithalat_kdv_indirilebilir_mi` | **null** | — | **UNKNOWN** | — |
| vergi.yaml | `gozetim.uygulama_var_mi` | **null** | — | **UNKNOWN** | EV-2026-08-09-125 |
| vergi.yaml | `tercihli_tarife.mense_ispat_belgesi` | **null** | — | **UNKNOWN** | — |
| vergi.yaml | `tercihli_tarife.tarife_kontenjani_var_mi` | köpüksüzde AB yok | — | FACT | EV-2026-08-09-108, -109 |
| vergi.yaml | `meta.model_hedef_tarihi` | **null** | — | **UNKNOWN** | — |

**evidence_id'si olmayan satır modele giremez.** Yukarıdaki `null` alanlar
bilinçli olarak boş bırakılmıştır.

---

## 6. ÇAPRAZ İPUÇLARI

`99-ops/_parts/capraz-ipuclari-gumruk-vergi-uzmani.md`'ye yazıldı.

| Hedef ajan | İpucu | Neden önemli |
|------------|-------|--------------|
| `global-sourcing-kasifi` | Bosna-Hersek ve Kosova menşeli şarapta gümrük vergisi **%0**; K.Makedonya %35. Bu ülkeler kapsamda hiç yok | Kapsamdaki 9 ülkenin en iyisi %50. Batı Balkanlar hem şarap üretiyor hem yakın |
| `global-sourcing-kasifi` | Şili'nin STA'sı şarapta **sıfır getirmiyor**, %70→%50 indiriyor | "STA var, ucuzdur" varsayımı yanlış |
| `global-sourcing-kasifi` | Köpüklü şarapta ÖTV **481,5146 TL/lt** = 361 TL/şişe | Köpüklü SKU genişletmesi vergiden ölür |
| `navlun-lojistik-uzmani` | Navlun+sigorta gümrük kıymetine giriyor; DÜ menşede navlunun **vergi çarpanı ~2,04×** | Navlun optimizasyonunun vergi kaldıracı var |
| `navlun-lojistik-uzmani` | Liman-sonrası masraf **ayrıştırılmazsa** tamamı vergilenir (GK md.28/a koşulu) | Forwarder faturasının yapısı doğrudan vergi kalemi |
| `navlun-lojistik-uzmani` | Antrepoda 1 Ocak/1 Temmuz'u geçirmek şişe başı ÖTV'yi ~%16 artırabilir | Antrepo nakit avantajının karşı riski |
| `mevzuat-ruhsat-uzmani` | Alkollü İçkilerin İthalat Denetimi Tebliği (ÜGD 2026/…) 22.04'ü kapsıyor | T0 takvimi ve maliyet |
| `mevzuat-ruhsat-uzmani` | ÖTVK md.14/5 bandrol usulüyle **vergi tahsiline** yetki veriyor | Bandrol ÖTV ödeme anını etkileyebilir |
| `mevzuat-ruhsat-uzmani` | TAPDK tebliğ serisi her yıl aralık sonunda yenileniyor, 2204.21'i anıyor | Yıllık tekrarlayan uyum yükü |
| `turkiye-pazar-kasifi` | Benchmark ürün **ABD menşeli** → %70, en pahalı gümrük rejimi | Raf fiyatının agresifliğini değerlendirirken sinyal; rakip menşe kırılımı toplanmalı |
| `kanal-marj-uzmani` | ÖTV şişe başı **sabit** — indirim yapılınca ÖTV düşmez | Kampanya maliyeti tamamen marjdan çıkar |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|-----------|--------------|-------|--------|--------|
| T-101 | `navlun-lojistik-uzmani` | Antrepodan kısmi çekiş mümkün mü, koşulu ve maliyeti nedir | HIGH | OPEN |
| T-102 | `mevzuat-ruhsat-uzmani` | Alkollü içki ithalat denetimi tebliği + bandrol usulü ÖTV tahsili | HIGH | OPEN |
| T-103 | `global-sourcing-kasifi` | Kapsamdaki 9 ülkenin hiçbiri %0 değil; B-Hersek/Kosova %0 ve kapsamda yok | HIGH | OPEN |
| T-104 | `finans-fizibilite` | ÖTV maktu tutarı Ocak/Temmuz'da otomatik artıyor; sabit sayı kullanılamaz | **CRITICAL** | OPEN |
| T-105 | `gumruk-vergi-uzmani` (kendime) | KKDF matrahının tanımı doğrulanmadı | MEDIUM | OPEN |

> **Gate uyarısı:** T-104 `CRITICAL` ve `OPEN`'dır. CLAUDE.md §5 ve
> `_SABLON-ticket.md` gate kuralı uyarınca bu ticket açıkken finans modeli
> çıktısı `APPROVED` olamaz.

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|-------------|-----|---------------------|
| EV-2026-08-09-111 (**ÖTV 71,2692 TL/lt**) | 30d | **2026-09-08** |
| EV-2026-08-09-110 (ÖTV nispi oran %0) | 30d | 2026-09-08 |
| EV-2026-08-09-125 (gözetim araması) | 30d | 2026-09-08 |
| EV-2026-08-09-102, -103, -104, -105, -106 (gümrük vergisi oranları) | 90d | 2026-11-07 |
| EV-2026-08-09-107 (İGV yok) | 90d | 2026-11-07 |
| EV-2026-08-09-118 (KDV %20) | 90d | 2026-11-07 |
| EV-2026-08-09-126 (Gümrük Rehberi yapısal) | 90d | 2026-11-07 |
| EV-2026-08-09-119 (KKDF %6) | 180d | 2027-02-05 |
| EV-2026-08-09-108, -109 (tarife kontenjanları) | 180d | 2027-02-05 |
| EV-2026-08-09-101 (GTİP), -113, -114, -115, -116, -117, -120, -121, -122, -123, -124 (kanun/tebliğ hükümleri) | 1y | 2027-08-09 |
| EV-2026-08-09-112 | 0d | **SUPERSEDED** |

> **En kısa TTL projedeki en kritik sayıdadır.** ÖTV tutarı bir sonraki
> Ocak/Temmuz güncellemesinde değişecektir; 2026-09-08'den sonra yeniden
> doğrulanmalıdır.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**ÖTV (III) sayılı liste (A) cetvelinde 22.04 için nispi oranın %0'dan farklı
belirlendiğinin tespiti.** Bu durumda "asgari maktudan az olmamak üzere yalnızca
nispi vergi" kuralı gerçekten devreye girer, ÖTV matrahı (CIF + gümrük vergisi)
önem kazanır ve yüksek CIF'li ürünlerde ÖTV maktu tutarı aşabilir. Tüm matrah
zinciri mantığım aynı kalır ama sayısal sonuçların tamamı değişir.

İkinci sıradaki geçersiz kılıcı: **ürünün 2204.10 (köpüklü) sayılması** — ÖTV
53,45 TL'den 361,14 TL'ye çıkar ve proje tek kalemde ölür.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"3/7/2026 tarihli 71,2692 TL/lt tutarı şu anda yürürlüktedir" varsayımı.**

Kırılganlığın kaynağı: bu tutar bir Cumhurbaşkanı Kararı ile değil, ÖTVK
md.12/3'ün **otomatik mekanizmasıyla** oluşmuştur ve bu nedenle T1 kanun metnine
işlenmemiştir. Ben GİB'in (T2) yayımladığı listeye güveniyorum. Ayrıca artışın
dayandığı **TÜİK Yİ-ÜFE 6 aylık değişim oranını (%16,09) bağımsız olarak
doğrulamadım** — yalnızca iki GİB listesi arasındaki oranı hesaplayarak geriye
doğru türettim. Bu, C-101'in çözüm önerisinin en zayıf halkasıdır.

İkinci kırılgan varsayım: **peşin ödeme baz senaryosu.** Peşin ödemede KKDF = 0
olduğu için KKDF matrahının bilinmemesini "önemsiz" saydım. Tedarikçiler vade
dayatırsa bu belirsizlik modele girer.

### 9.3 Hangi kaynağıma en az güveniyorum?

Üç sıra hâlinde:

1. **`EV-2026-08-09-125` (gözetim yok)** — Bu bir **negatif arama sonucudur** ve
   epistemik olarak en zayıf iddiam. Yöntemi kontrol GTİP'i ile doğrulamış olsam
   bile, veri tabanının yürürlükteki tüm gözetim tebliğlerini kapsadığını
   kanıtlayamam. `UNKNOWN` olarak bıraktım ama bir okuyucu bunu "gözetim yok"
   diye okuyabilir.
2. **`EV-2026-08-09-118` (KDV %20)** — T1 dayanak belge (7346 sayılı CBK)
   taranmış görüntü olduğu için okunamadı; oran GİB'in konsolide metninden (T2)
   alındı. Oranın doğruluğundan şüphem yok ama **T1 doğrulaması eksiktir.**
3. **`EV-2026-08-09-126` (Gümrük Rehberi)** — Sayfanın revizyon tarihi 26.10.2018
   ve KDV genel oranını hâlâ %18 olarak gösteriyor. **Bayat bir kaynaktır.**
   Yalnızca yapısal ifade ("gümrük vergisi matrahı = CIF") için kullandım,
   hiçbir oran bu kaynaktan alınmadı. Yine de kanıt setimde en düşük kaliteli
   kayıttır.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

- **ÖTV yanlışsa (aşağı yönlü):** Şişe başı ~53 TL vergi yükü hafifler,
  fiyat/performans segmenti yeniden yaşanabilir hâle gelir → `KILL`/`HOLD`
  eğilimi `TEST`'e döner.
- **ÖTV yanlışsa (yukarı yönlü, örn. 2026 Ocak'ta bir sıçrama daha):** Düşük CIF
  senaryolarının tamamı ölür → `KILL`.
- **Gümrük vergisi yanlışsa (AB gerçekten %0 olsaydı):** Menşe stratejisi tamamen
  AB'ye kayar, sourcing kapsamı daralır ve maliyet ~%50 CIF kadar düşer.
- **Gözetim varsa:** Ucuz beyan/ucuz sourcing stratejisi çöker; ancak ÖTV maktu
  olduğu için etki diğer ürünlere göre sınırlıdır — yine de `IMPORT PILOT`
  kararı ertelenir.
- **KDV indirilemiyorsa:** Şişe başı ~40–45 TL daha ekonomik maliyet eklenir;
  bu tek başına marj eşiğini kırabilir.
- **Kısmi çekiş mümkün değilse:** `peak_cash_requirement` ~2 milyon TL
  mertebesine çıkar; `maximum_total_capital_try` eşiği aşılırsa 100.000 şişe/yıl
  senaryosu elenir.

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| Ne | Kim | Nasıl | Süre |
|----|-----|-------|------|
| ÖTV 71,2692 TL/lt teyidi | Gümrük müşaviri veya GİB | Güncel bir şarap ithalat beyannamesinde uygulanan TL/lt tutarı; alternatif olarak TÜİK Yİ-ÜFE Ara.2025→Haz.2026 değişimi | 1–3 gün |
| Gözetim var mı | Gümrük müşaviri | GTİP bazlı yürürlükteki gözetim/korunma önlemi sorgusu | 1–2 gün |
| 12 haneli GTİP | Gümrük müşaviri | Numune etiketi + ABV + PDO/PGI bilgisiyle bağlayıcı tarife bilgisi (BTB) başvurusu da mümkün | BTB: 30–60 gün · müşavir görüşü: 1 gün |
| KDV indirilebilirliği | YMM/SMMM | KDVK md.29-34 + GİB özelgeleri | 2–5 gün |
| KKDF matrahı | Gümrük müşaviri | GGM genelgeleri | 1–2 gün |
| Antrepo kısmi çekiş | `navlun-lojistik-uzmani` + antrepo işletmecisi | Ticket T-101 | 3–7 gün |
| Menşe ispat belgesi | Gümrük müşaviri + AB'li tedarikçi | EUR.1 / fatura beyanı düzenlenebilirliği teyidi | 3–5 gün |

**Toplam:** Bir gümrük müşaviri ile tek oturumda bu listenin **6/7'si** kapanabilir.
`TEST` veya `IMPORT PILOT` kararından önce bu oturum yapılmalıdır.
