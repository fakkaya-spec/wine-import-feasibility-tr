# ÇAPRAZ İPUÇLARI — kanal-marj-uzmani, TUR 2

> Bu bir **parça dosyasıdır**. `99-ops/capraz-ipuclari.md` ana dosyasına
> `yatirim-komitesi-baskani` tarafından birleştirilir. Bu ajan ana dosyaya
> **DOKUNMAMIŞTIR**.
>
> **Bunlar SONUÇ DEĞİL, İPUCUDUR.** Hedef ajan kendi alanında doğrulamadan
> modele giremez (CLAUDE.md §1.10–1.11).

---

## → `turkiye-pazar-kasifi`

### KM-1 — İthal şarabın hacim payı için resmî bir sayı buldum (sizin alanınız, ben sonuç üretmedim)

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

### KM-2 — Alkollü içki satan nokta sayısı resmî olarak biliniyor

`EV-2026-08-10-613` (aynı karar, Tablo 5, kaynak **TADB**), 2020:
**GK (geleneksel kapalı nokta) 48.956** · **YT/ASN (HoReCa) 29.218**.

Modern kanal (zincir market) nokta sayısı bu tabloda **kasten yoktur** (merkezi alım
nedeniyle dışarıda bırakılmış). Yani "Türkiye'de kaç zincir market noktası şarap
satıyor" sorusu **hâlâ açıktır** ve pazar haritanızın bir boşluğudur.

### KM-3 — Metro alkolde yıllık anlaşma imzalıyor; "tek fiyat listesi" değil

`EV-2026-08-10-612`: Mey İçki'nin **MİGROS, CARREFOUR, ÖZDİLEK, METRO ve TESPO** ile
**birer yıllık satış anlaşması** imzaladığı, kararda ismen yazılıdır.

Bu, sizin `İP-501` ve `İP-505`'inizle **tutarlıdır ve onları güçlendirir**:
Metro'da tek bir "raf fiyatı" bir kanal fiyatı değildir; müşteriye ve sözleşmeye
bağlı fiyatlar vardır. `T-506`'ya kanal tarafından verebildiğim en somut cevap budur.

---

## → `finans-fizibilite`

### KM-4 — TL ticari kredinin piyasa fiyatı için denetlenmiş bir çapa var (makro.yaml sizin alanınız)

`EV-2026-08-10-617` (Migros 2025 bağımsız denetimden geçmiş konsolide finansallar,
ticari borçlar notu):

> *"Ticari borçların vadesi genel olarak 3 aydan kısadır ve 31 Aralık 2025 tarihi
> itibarıyla **yıllık %38,6** (2024: **%46,2**) oranı kullanılarak iskonto edilmiştir."*

**Neden önemli:** Bu, Türkiye'de **TL ticari kredinin fiilen fiyatlandığı orandır**
ve bir denetim raporunda yer alır. `makro.yaml → finansman_orani` şu an
`null`/`UNKNOWN`. `Cİ-15.4` (gümrük-vergi ajanı) devreden KDV'nin finansman
maliyetinin `L5`'te ayrı satır olması gerektiğini söylemişti — o hesabın **oranı**
buradan gelebilir. **Ben doldurmadım.**

### KM-5 — Listeleme bedeli, hacim senaryolarını asimetrik kırar

`kanal.yaml → duyarlilik_senaryolari.f_listeleme_bedeli_sise_basi`:
Listeleme bedeli **sabit**, hacim **değişkendir**. Aynı mutlak bedel,
5.000 şişe/yıl senaryosunda 100.000 şişe senaryosunun **20 katı** şişe başına
maliyet üretir.

Bu, `global-sourcing-kasifi`'nin `İP 6.3`'ü (MOQ hacim senaryolarını asimetrik
kısıtlar) ve `navlun-lojistik-uzmani`'nın `F-1`'i (5.000 şişe LCL'dir, birim maliyet
yüksektir) ile **aynı yönde** birikir. **Üç ajan da bağımsız olarak küçük hacmin
orantısız pahalı olduğunu buldu.** Bu, ölçek eğrisinin **doğrusal olmadığının** üçüncü
bağımsız kanıtıdır.

### KM-6 — Kanal karması kararı, dağıtım modeli kararını belirler (tersi değil)

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

## → `gumruk-vergi-uzmani`

### KM-7 — Üretici pazarlama katkısının BİÇİMİ vergi matrahını değiştirebilir

`T-605`'te `global-sourcing-kasifi`'den RFQ 5.6'nın cevabında şu ayrımın zorunlu
kılınmasını istedim: üreticinin pazarlama/listeleme katkısı **fatura ile mi**
yoksa **fiyat iskontosu ile mi** veriliyor?

**Neden size ipucu bırakıyorum:** iskonto ile verilirse `L0/L1` düşer ve dolayısıyla
gümrük kıymeti de düşer; fatura ile verilirse `L5`'te bir gelir kalemidir ve kıymeti
etkilemez. **Bu benim alanım değil ve bir sonuç üretmedim** — yalnızca ayrımın
sorulmasını sağladım. Vergisel sonuç sizindir.

### KM-8 — Kırık ürün bedeli, indirilemeyen KDV ile birleşiyor

`EV-2026-08-10-612`: **"kırık ürün bedeli"** alkollü içki zincir yıllık anlaşmasında
"müşteriye ödenecek bedeller" arasında **ismen** vardır — yani kırılma maliyeti
sözleşmeyle **tedarikçiye** dönmektedir.

Sizin `Cİ-15.1`'iniz KDVK md.30/c uyarınca **zayi olan mala ait KDV'nin
indirilemediğini** kaydetmişti. İki bulgu birleşince fire maliyeti:
`f × L4_per_şişe + f × KDV_per_şişe` **artı** sözleşmesel kırık ürün bedeli olur.
Üçüncü kalemin varlığını kanal tarafında doğruladım; **tutarı UNKNOWN**.

---

## → `mevzuat-ruhsat-uzmani`

### KM-9 — TUR 1'deki `K3` ipucunuz kanal tarafında bir yapısal sonuç doğuruyor

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

### KM-10 — 2015'teki "raf garantisi" 2024 metninde görünmüyor — sizin alanınız

`EV-2026-08-10-608` (TBMM, 6585 orijinal 2015 metni, m.6/2):

> *"...prim ya da bedel talebine konu olan ürünün sözleşme süresince **rafta satışa
> sunulması zorunludur**."*

Bulabildiğim **2024 konsolide metninde** (`EV-2026-08-10-601`) bu cümle
**görünmemektedir**. Doğruysa, "listeleme bedelini ödedik ama raftan çıkarıldık"
riski hukuken korumasız hâle gelmiştir. **T-601**'in üçüncü sorusudur.

---

## → `seytanin-avukati`

### KM-11 — Kendi işime karşı hazırladığım cephane

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

## → `yatirim-komitesi-baskani`

### KM-12 — İki bakım işi

1. **`index.csv` birleştirmesi:** `10-evidence/_index-parts/kanal-marj-uzmani-tur2.csv`
   (başlıksız, 24 satır, `index.csv` kolon sırasında) hazırdır. Bu ajan `index.csv`'ye
   **dokunmamıştır**.
2. **`EV-2026-08-10-608` kartının `status` alanı `SUPERSEDED`'dır** (6585 orijinal
   2015 metni; 7435 ile değişmiştir). Kartı bilerek açtım — çünkü değişikliğin
   **kendisi** bir bulgudur (`KM-10`). `supersedes` alanı boştur çünkü bu kart yeni
   metni değil **eski metni** taşır; onu geçersiz kılan `EV-2026-08-10-601`'dir.
   Bu ters yönlü bağ `index.csv`'de otomatik görünmez; birleştirmede dikkat edilmeli.

### KM-13 — `T-205` nasıl kullanıldı

`T-205` **açılmamış, statüsü değiştirilmemiştir.** `ACCEPTED BUSINESS CONSTRAINT`
olarak bir **girdi** gibi kullanılmıştır. Nerede kullanıldığı `T-205.md` sonuna
eklenen "KULLANIM KAYDI" bölümünde satır satır gösterilmiştir.
