# INVESTOR DECISIONS REQUIRED BEFORE TUR 3B

```yaml
belge:                  investor-decisions-required
yazan:                  yatirim-komitesi-baskani
tarih:                  2026-08-10
tur:                    TUR 2.5 KAPANIS
kapsam:                 "OQ-901'in gorunur hale getirilmesi — yatirimcidan gereken
                         ESIKLERIN ve ESIK DISI GIRDILERIN TAM LISTESI"
karar_iceriyor_mu:      false      # YATIRIM karari icermez
esik_degeri_yazildi_mi: false      # HICBIR ESIGE SAYI YAZILMADI
arastirma_yapildi_mi:   false      # CLAUDE.md §1.16
web_aramasi_yapildi_mi: false
ajan_cagrildi_mi:       false
yeni_kanit_uretildi_mi: false
karar_gunlugune_dokunuldu_mu: false
iliskili_oq:            OQ-901
iliskili_ticket:        [T-851, T-852, T-912, T-104, T-604, T-857, T-859, T-467, T-304]
```

> ## BU BELGE BİR KARAR DEĞİL, BİR **KARAR TALEBİDİR**
>
> `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` / `SCALE` kararlarının hiçbiri bu
> belgede verilmemiştir ve verilemez. `90-karar/karar-gunlugu.md` dosyasına
> **DOKUNULMAMIŞTIR.**
>
> ## VE İÇİNDE **TEK BİR EŞİK DEĞERİ YOKTUR**
>
> Bu belge yatırımcıya *"şu marjı hedefleyin"* demez. Eşikler **yatırımcının
> risk iştahına** aittir ve araştırmadan türetilemez
> (`00-charter/karar-esikleri.md`). Başkanın bir eşiğe sayı yazması, projenin
> en sinsi uydurma noktası olurdu — `finans-fizibilite` bunu `T-851`'de
> açıkça reddetmiştir ve **ben de reddediyorum.**
>
> Verilen tek şey **bağlam**tır: her eşiğin ne işe yaradığı, hangi katmanlar
> arasında tanımlanması gerektiği, belirlenmezse hangi çıktının `UNKNOWN`
> kalacağı ve seçim yapılırken hangi **seçenek yapılarının** mevcut olduğu.

---

## 0. NEDEN ŞİMDİ — VE NEDEN "TUR 3B"

`OQ-901` **2026-08-09**'da açıldı ve **iki turdur ele alınmadı**. TUR 2.5'e
kadar bu savunulabilirdi: model henüz sayı üretmiyordu, eşik neyle
karşılaştırılacaktı? **Bu savunma TUR 2.5'te düştü.**

TUR 2.5 ters modeli üç şeyi aynı anda gösterdi:

| # | Bulgu | Kaynak |
|---|---|---|
| 1 | `MAX_CIF_TRY` hesaplanabiliyor ve **pozitif** — segment aritmetik olarak imkânsız değil | `reverse-price-model.md` §3.3 |
| 2 | Modelin **en büyük iki belirsizlik ekseni** bir veri eksikliği değil, **bir karar eksikliğidir** (ithalatçı katkı payı ve distribütör marjı; her biri 0→%30 aralığında **−108,56 TL/şişe**) | `reverse-price-model.md` §8.1, `T-851` |
| 3 | `TARGET` / `ACCEPTABLE` / `WALK-AWAY` fiyatları **üretilemedi** çünkü üretmek keyfî yüzde uydurmak olurdu | `reverse-price-model.md` §9 |

> **Yani model artık eşik yokluğundan dolayı fiilen duruyor.**
> Bu bir başarısızlık değil; CLAUDE.md §1.15'in (*"Finans modeli kanıtsız sayı
> üretmez"*) doğru çalıştığının kanıtıdır.

### Süreç kararı — TUR 3'ün ikiye bölünmesi (başkan kararı, yatırım kararı değil)

| Tur | İçerik | Yatırımcı girdisi gerekir mi |
|---|---|---|
| **TUR 3A** | Masabaşı kapatılabilir boşluklar: spesifikasyon düzeltmeleri, kanal bacağı doğrulaması, KDV indirim hakkı taraması, gözetim taraması, hijyen ticket'ları, fiziksel mağaza turu | **HAYIR** |
| **TUR 3B** | **İleri (forward) model:** contribution margin · break-even · `peak_cash_requirement` · payback · senaryo eleme | **EVET — bu belge onun ön koşuludur** |

**TUR 3A bu belge olmadan başlayabilir. TUR 3B başlayamaz.**

---

## 1. OKUMA KURALLARI (BAĞLAYICI)

| # | Kural |
|---|---|
| **IR-1** | Bu belgedeki hiçbir eşik için **öneri değer** yoktur. Boş bırakılan her alan bilinçlidir. |
| **IR-2** | Bir eşiğe verilen cevap `INVESTOR_DECISION` olarak etiketlenir. **`FACT` değildir, `ESTIMATE` değildir, `evidence_id` almaz** — bir dış olgu değil, bir beyandır. (`model_hedef_tarihi` ve hedef raf fiyatı merdiveniyle aynı sınıf; bkz. `tur-25-preflight.md` §2.1, §3.1.) |
| **IR-3** | Her eşik **hangi katmanlar arasında** tanımlandığı yazılmadan geçerli değildir. `00-charter/karar-esikleri.md` bunu açık uçlu bırakmıştır ve bu bir **eksikliktir**, bir esneklik değil. |
| **IR-4** | Eşikler **modelin çıktısı görüldükten sonra** belirlenirse, "sonuca göre eşik ayarlama (hedef kaydırma)" riski doğar. Bu risk `OQ-901`'de kayıtlıdır ve `seytanin-avukati` TUR 4'te bunu bir saldırı vektörü olarak kullanmalıdır. **Bu belge, eşiklerin ileri model çıktısından ÖNCE yazılmasını mümkün kılmak için üretilmiştir.** |
| **IR-5** | Bir eşik **belirlenmeyebilir.** *"Bu eşiği şimdi koymuyorum"* geçerli bir cevaptır — ama sonucu bu belgede yazılıdır ve karara taşınır. |
| **IR-6** | Eşiklerin tamamı `ters` modelin `UPPER_BOUND` çıktısına karşı okunmalıdır. Ters modelin ürettiği tavanlar **iki bağımsız nedenle üst sınırdır** (λ=1 ve 13 maliyet kaleminin `0` alınması). **Bir eşiği bu tavanlara bakarak koymak, iyimser bir zemine eşik koymaktır.** |

---

# §2 — EŞİKLER (`D-01` … `D-16`)

> Sütun anlamları:
> **Ne işe yarar** = hangi model çıktısını kilitler, hangi senaryoyu eler ·
> **Katman** = eşiğin hangi katmanlar arasında tanımlanması gerektiği ·
> **Belirlenmezse** = hangi çıktı `UNKNOWN` kalır, hangi karar verilemez ·
> **Seçenek yapısı** = değer değil, **karar biçimi** (bir sayı mı, bir oran mı,
> bir kural mı, hangi matrah üzerinden)

---

## GRUP A — KÂRLILIK EŞİKLERİ

### `D-01` — `minimum_gross_margin` (brüt marj tabanı)

| Alan | İçerik |
|---|---|
| **Charter karşılığı** | `target_gross_margin_pct` — `TBD` |
| **Ne işe yarar** | İleri modelde her senaryonun (hedef fiyat × menşe × kanal × hacim) ilk elemesi. Brüt marjı bu tabanın altında kalan senaryo **hesaplanmaya devam edilmez**. Ters modelde ise `MAX_CIF` tavanının **hangi oranda kullanılabileceğini** belirler. |
| **Katman — KARAR GEREKTİRİR** | `00-charter/karar-esikleri.md` bunu açıkça açık bırakmıştır: *"L5→L6 mı, L5→L8 mi?"* **Proje verisi bu soruyu üç seçenekli hâle getirmiştir:** |
| | **(a) `L5 → L6`** — ithalatçı maliyeti → ithalatçı **fatura** fiyatı. Sektörde en yaygın konuşulan tanım. **Sorun:** `L6` ithalatçının fiilen tahsil ettiği tutar **değildir** — `d` (geri akan bedeller) ve `f` (listeleme) `L6`'dan geri akar. Bu tanım marjı **olduğundan yüksek** gösterir. |
| | **(b) `L5 → L7_eff`** — ithalatçı maliyeti → ithalatçının **fiilî net hasılatı** (`L7_eff = L6(1−d) − f`). TUR 2.5'te modelin `R5` düzeltmesinin dayandığı büyüklük tam olarak budur. **En dürüst tanım.** |
| | **(c) `L5 → L8`** — ithalatçı maliyeti → tüketici raf fiyatı. **Bu bir ithalatçı marjı değildir**, zincirin tamamının marjıdır; ithalatçının kontrolünde olmayan perakende marjını içerir. Karşılaştırma amaçlı anlamlıdır, eleme amaçlı **yanıltıcıdır.** |
| **Belirlenmezse** | İleri modelde **senaryo eleme yapılamaz**; 2.700 satırlık çıktı 2.700 satır olarak kalır ve *"hangisi yeterli"* sorusu cevapsızdır. `TARGET BUY PRICE` üretilemez (`T-851`). |
| **Seçenek yapısı** | (i) yüzde mi TL/şişe mi, (ii) **hangi katman çifti** (a/b/c), (iii) KDV hariç mi dahil mi *(proje boyunca KDV hariç kullanılmıştır — sapılırsa yazılmalıdır)*, (iv) tek eşik mi kanal başına ayrı eşik mi *(zincir/tekel/HoReCa marj yapıları modelde farklıdır)* |
| **Bağlı ticket** | `T-851` (CRITICAL), `T-604` |

> ⚠ **Bu belgenin en önemli tek tavsiyesi bir değer değil, bir disiplindir:**
> `D-01`'in katman çifti seçilmeden verilen bir yüzde **anlamsızdır.**
> Aynı ürün, aynı fiyat, aynı maliyetle (a) tanımında ve (b) tanımında
> **farklı marjlar** üretir ve fark `d` + `f` kadardır — TUR 2.5'te bu farkın
> mertebesi `MAX_CIF` üzerinde **28,95 TL/şişe** ölçülmüştür
> (`reverse-price-model.md` §2.2).

---

### `D-02` — `minimum_contribution_margin` (şişe başına asgari katkı payı)

| Alan | İçerik |
|---|---|
| **Charter karşılığı** | `minimum_contribution_try_per_bottle` — `TBD` |
| **Ne işe yarar** | Sabit maliyetleri (ruhsat, personel, depo) karşılamaya yetip yetmediğini test eder. **Break-even hacminin paydasıdır** — bu eşik olmadan break-even hesaplanamaz. |
| **Katman — KARAR GEREKTİRİR** | Katkı payı = **net hasılat − DEĞİŞKEN maliyet**. Kritik soru: **hangi kalemler değişkendir?** Projede bu ayrım henüz yapılmamıştır. |
| | **Kesin değişken (hacimle doğrusal):** CIF, gümrük vergisi, **ÖTV (maktu ama şişe başına)**, bandrol, TADAB, şişe başı iç lojistik |
| | **Kesin sabit:** ruhsat sabit maliyeti *(ve **kademelidir** — 20.000 lt/yıl eşiğinde sıçrar, `EV-2026-08-09-234`, `T-858`)*, kendi dağıtım personeli, depo kirası |
| | **Tartışmalı — karar gerektirir:** listeleme bedeli `f` *(sabit tutar, hacme bölünür → şişe başına **değişken görünür ama değildir**)*, geri akan bedeller `d` *(ciroya oranlı → değişken)*, devreden KDV finansman maliyeti |
| **Belirlenmezse** | `break_even_volume` **`UNKNOWN`**. Pilot hacminin (5.000) ekonomik olarak anlamlı olup olmadığı söylenemez. `IMPORT PILOT` büyüklüğü seçilemez. |
| **Seçenek yapısı** | (i) TL/şişe mi net hasılatın yüzdesi mi, (ii) ruhsat sabit maliyeti **içeride mi dışarıda mı** *(içerideyse katkı payı hacme bağlı olur ve tanım bozulur)*, (iii) ilk yıl mı steady-state mi *(ruhsat ilk yıl maliyeti farklıdır)* |
| **Bağlı ticket** | `T-858` (ruhsat kademesi), `T-851` |

---

### `D-03` — `minimum_importer_contribution` / `REQUIRED_IMPORTER_MARGIN` (μ)

> **BU, MODELİN EN BÜYÜK TEK BELİRSİZLİK EKSENİDİR** ve `D-01`/`D-02`'den
> ayrıdır: `D-01` bir **eleme** eşiği, `D-03` ise ters modele **giren bir
> parametredir**.

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | Ters modelde `R5` adımının parametresidir: `L5_max = L7_eff − μ × L6`. Doğrudan `MAX_CIF`'i belirler → doğrudan **tedarikçiye ödenebilecek azami fiyatı** belirler → doğrudan **RFQ hedefini** belirler. |
| **Ölçülmüş kaldıraç** | `0 → %30` aralığı **−108,56 TL/şişe** (799 TL · ES · CHAIN · BASE · 5.000 şişe). Gümrük vergisi riskinin (−32,10) **üç katı**, ÖTV λ şokunun (−20,04) **beş katı**. |
| **Katman — KARAR GEREKTİRİR (ÇÖZÜLMEMİŞ)** | Model bugün μ'yü **`L6` cirosu üzerinden** almaktadır (`ters_model.py:392`). Bu bir **tanım seçimidir ve hiçbir yerde gerekçelendirilmemiştir.** Üç seçenek: **(a) `L6` (fatura cirosu)** — model bugün bunu kullanıyor; **(b) `L7_eff` (fiilî net hasılat)** — `d` ve `f` çıktıktan sonra; **(c) `L5` (maliyet üzerine markup)**. Üçü aynı μ değeri için **farklı `MAX_CIF`** üretir. |
| **Ölçülmemiş olması** | ⚠ Tüm baz koşularda **μ = 0** alınmıştır. Yani μ'nün matrahı **hiç test edilmemiştir**; `reverse-price-model.md` §9.2 ve §7.1 gridlerinin tamamı bu tanımsız matraha dayanır → **`T-944`** (bu turda açıldı). |
| **Belirlenmezse** | `TARGET BUY PRICE`, `ACCEPTABLE BUY PRICE`, `WALK-AWAY PRICE` **üretilemez.** RFQ'ya hedef fiyat yazılamaz. `MAXIMUM STRUCTURAL BUY PRICE` (kâr sıfır) tek çıktı olarak kalır ve **hiçbir RFQ'da kullanılamaz** — çünkü tedarikçiye *"kârımı sıfırlayan fiyatı ver"* denmez. |
| **Seçenek yapısı** | (i) **matrah** (a/b/c), (ii) yüzde mi TL/şişe mi, (iii) yıl bazında mı SKU bazında mı, (iv) pilot ve ölçek için **ayrı** mı |
| **Bağlı ticket** | **`T-851` (CRITICAL)**, `T-944` |

---

### `D-04` — `maximum_acceptable_distributor_margin` (dış distribütör marjı tavanı)

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | `MODEL A` (3. taraf distribütör) ile `MODEL B` (kendi dağıtım) arasındaki kararın **ekonomik eşiğidir.** Bu tavanın üstünde bir distribütör talebi geldiğinde `MODEL A` elenir. |
| **Katman** | `L6` cirosu üzerinden kesinti *(model bugün böyle uyguluyor)* — **`D-03` ile aynı matrah sorusuna tabidir ve ikisi aynı anda uygulanırsa TOPLANIRLAR** (`reverse-price-model.md` §7.1). |
| **Belirlenmezse** | `MODEL A ↔ MODEL B` karşılaştırması **yapılamaz** — bugünkü durum budur. `kanal.yaml → dis_distributor.marj_pct` `null`/`UNKNOWN`'dır ve `kanal-marj-uzmani` TUR 2'de *"hiçbir kanıtlı değer bulunamamıştır ve uydurulmamıştır"* demiştir. Model yalnızca **parametrik grid** üretebilir. |
| **Not — bu bir eşik, veri değil** | Distribütör marjının **gerçek piyasa seviyesi** bir araştırma konusudur (`T-604`, ticari sır olduğu tespit edilmiş). **Tavan** ise bir yatırımcı kararıdır. İkisi karıştırılmamalıdır. |
| **Bağlı ticket** | `T-604` (HIGH), `T-851` |

---

## GRUP B — SERMAYE VE NAKİT EŞİKLERİ

### `D-05` — `maximum_total_capital` (toplam sermaye tavanı)

| Alan | İçerik |
|---|---|
| **Charter karşılığı** | `maximum_total_capital_try` — `TBD` |
| **Ne işe yarar** | `peak_cash_requirement` bu tavanı aşan **her senaryo uygulanamaz** — kârlı olsa bile. Bu, kârlılıktan bağımsız tek eleme kriteridir. |
| **Katman / perspektif — KARAR GEREKTİRİR** | CLAUDE.md §6 KDV'yi **iki ayrı perspektifle** modellemeyi zorunlu kılar. Sermaye tavanı **B perspektifine (nakit)** karşı okunur, A'ya (ekonomik maliyet) değil. Yani karşılaştırma nesnesi `l4_cash`, `l4_econ` değil. |
| **Bu projede neden yapısal olarak yüksek** | Bandrol **hem gümrükten hem satıştan önce** peşin (`EV-2026-08-09-214`) · ÖTV **ve** KDV beyanname tescilinde **peşin** (`EV-2026-08-09-122`) · KDV **iade edilmez**, yalnızca satış hızına bağlı mahsup (`EV-2026-08-10-104`) · kanal vadesi BASE 60 / STRESS 120 gün · tedarikçi vadesi **0 (peşin)**. **Nakit çıkışının tamamı girişten önce.** |
| **Belirlenmezse** | `peak_cash_requirement` hesaplansa bile *"karşılanabilir mi"* sorusu cevapsız kalır. `IMPORT PILOT` ile `HOLD` arasındaki seçim **keyfî** olur (`OQ-901`). |
| **Seçenek yapısı** | (i) tek tutar mı yoksa **taahhüt + koşullu ikinci dilim** mi, (ii) özkaynak mı borç dahil mi, (iii) ruhsat/kuruluş sabit maliyeti dahil mi hariç mi, (iv) **kaç aylık** azami süre için |
| **Bağlı ticket** | `T-851`, `T-601` (vade), `T-301` (antrepo bekleme → nakit kilitlenme süresi) |

---

### `D-06` — `maximum_working_capital` (azami işletme sermayesi)

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | `D-05`'ten **ayrıdır**: `D-05` kuruluş dahil toplam sermaye tavanı, `D-06` **sürekli bağlı kalan** işletme sermayesi tavanıdır. Ölçek kararının (`SCALE`) gerçek kısıtı genellikle budur. |
| **Katman** | Stok (`L5` maliyetiyle değerlenmiş) + kanal alacağı (`L6` fatura değeriyle) + devreden KDV bakiyesi − tedarikçi borcu *(bu projede **sıfır**, peşin ödeme)* |
| **Belirlenmezse** | Hacim senaryoları (5.000 → 100.000) **finansal olarak sıralanamaz.** `scale_intent` (charter: *"50.000–100.000 şişe/yıl ölçeklenebilir mi"*) test edilemez — çünkü ölçeklenebilirliğin kısıtı marj değil, işletme sermayesidir. |
| **Seçenek yapısı** | (i) TL tavanı mı yoksa **ciroya oran** mı, (ii) devreden KDV bakiyesi dahil mi *(kâr değil, kilitli nakittir)* |
| **Bağlı ticket** | `T-851`, `T-601`, `C-601` (yasal 60 gün ↔ gözlenen ~93 gün vade çelişkisi — açık) |

---

### `D-07` — `maximum_payback` (azami geri ödeme süresi)

| Alan | İçerik |
|---|---|
| **Charter karşılığı** | `target_payback_months` — `TBD` |
| **Ne işe yarar** | Zaman boyutundaki tek eleme kriteri. Bir senaryo kârlı, sermayeye sığar **ve** yine de çok yavaş olabilir. |
| **Katman** | Kümülatif net nakit akışının işarete döndüğü an — **nakit perspektifi (B)**, muhasebe kârı değil. |
| **Belirlenmezse** | `SCALE` ile `IMPORT PILOT` arasındaki tercih **zamansız** kalır. Ruhsat sabit maliyetinin ilk yıl mı yoksa çok yıla mı yayıldığı sorusu cevapsız kalır. |
| **Seçenek yapısı** | (i) ay mı yıl mı, (ii) pilot için ayrı / ölçek için ayrı mı, (iii) **hangi tarihten** başlar — ilk ödeme mi (bandrol/ruhsat), ilk konteyner mi, ilk satış mı *(bu projede aralarında aylar var, `t0-takvimi`)* |
| **Bağlı ticket** | `T-851`, `T-202`/`C-202` (T0 takvimi hâlâ `ASSUMPTION` sıralamaya dayanıyor) |

---

### `D-08` — `maximum_acceptable_inventory_days` (azami stok gün sayısı)

| Alan | İçerik |
|---|---|
| **Charter karşılığı** | `target_inventory_days` — `TBD` |
| **Ne işe yarar** | Nakit kilitlenmesinin **en büyük tek bileşenidir** ve bu projede **kısmen ithalatçının kontrolünde değildir.** |
| **Katman** | `L5` maliyetiyle değerlenmiş stok; gümrük tescilinden satış faturasına kadar geçen süre |
| **Kontrol dışı bileşen — kritik** | Ruhsat/analiz/bandrol nedeniyle malın **gümrükte + antrepoda zorunlu bekleme süresi `UNKNOWN`**'dır (`T-301`, **CRITICAL**, iki turdur açık). Yani bu eşiğin **alt sınırı bile bilinmiyor.** Bandrol antrepoda şişe başına uygulanır (`T-204`). |
| **Belirlenmezse** | `D-06` (işletme sermayesi) hesaplanamaz; LCL↔FCL modu seçimi ekonomik olarak karşılaştırılamaz *(FCL daha ucuz birim maliyet, daha büyük parti, daha uzun stok)*. |
| **Seçenek yapısı** | (i) gün sayısı, (ii) **hangi andan** sayılır (varış / tescil / antrepo çıkışı), (iii) zorunlu bekleme **dahil mi hariç mi** — dahilse eşik ithalatçının kontrolünde olmayan bir süreyi cezalandırır |
| **Bağlı ticket** | **`T-301` (CRITICAL)**, `T-204`, `T-314` |

---

### `D-09` — `maximum_acceptable_pilot_loss` (kabul edilebilir azami pilot kaybı)

| Alan | İçerik |
|---|---|
| **Charter karşılığı** | `maximum_acceptable_pilot_loss_try` — `TBD` |
| **Ne işe yarar** | **`IMPORT PILOT` kararının BÜYÜKLÜĞÜNÜ belirler.** Bu eşik olmadan pilot hacmi seçilemez — 5.000 mi 25.000 mi sorusu bir ekonomi sorusu değil, bir **kayıp toleransı** sorusudur. |
| **Katman** | Toplam nakit çıkışı − geri kazanılan nakit; **`L5` maliyetiyle stokta kalan mal dahil mi** ayrıca kararlaştırılmalıdır *(alkollü içki stoku ruhsat sınırlı bir alıcı kitlesine satılabilir — likidite varsayımı `UNKNOWN`)* |
| **Belirlenmezse** | Pilot hacmi keyfî seçilir. **5.000 şişe seçimi bugün bir varsayımdır, bir karar değildir** ve MOQ verisiyle **çelişmektedir**: doğrulanmış tedarikçi MOQ bandı 3.000–6.000 şişe/SKU'dur (`C-462`); 5.000'lik pilot iki büyük adayın (R1 Harland, R2 Danese, 6.000 MOQ) **altındadır** ve o adaylarla çalışılamaz. |
| **Seçenek yapısı** | (i) TL tutarı, (ii) toplam sermayenin yüzdesi, (iii) **stok değeri dahil mi**, (iv) tek pilot mu iki dalga mı |
| **Bağlı ticket** | `T-851`, `C-462`, `T-855` (10.000 şişe senaryosu **çalıştırılamadı** — lojistik satırı yok) |

---

## GRUP C — HACİM VE ÖLÇEK EŞİKLERİ

### `D-10` — `minimum_annual_volume` (asgari yıllık hacim)

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | Bunun altında işin **kurulmaya değmediği** hacim. Sabit maliyet yığınının şişe başına payını belirler ve doğrudan `D-02`'ye bağlanır. |
| **Katman** | Şişe/yıl **ve** litre/yıl — **ikisi birden gerekir** (aşağıya bakınız) |
| **⚠ MEVZUAT KAYNAKLI KIRILMA NOKTASI** | `ruhsat.yaml → toplam_ruhsat_sabit_maliyeti` **20.000 litre/yıl** eşiğinde kademe atlar (`EV-2026-08-09-234`). 0,75 lt şişe `ASSUMPTION`'ı üzerinden bu **26.667 şişe**'dir. Ters model bu yüzden **25.000'den sonra düzleşiyor**: 5k→25k geçişi `MAX_CIF`'e **+17,68 TL**, 25k→50k geçişi yalnızca **+0,77 TL** katıyor. **Ölçek ekonomisinin %87'si ilk sıçramada gerçekleşiyor ve sebebi navlun değil, bir ruhsat kademesidir.** |
| **Belirlenmezse** | `scale_intent` test edilemez. Ölçek eğrisinin **hangi noktasında durulacağı** kararı verilemez — ve model bugün *"25.000'in üstünde büyümek `MAX_CIF`'i neredeyse hiç değiştirmiyor"* diyor, bu da `SCALE` kararının ekonomik gerekçesini **zayıflatıyor.** |
| **Seçenek yapısı** | (i) şişe/yıl, (ii) **litre/yıl** *(ruhsat kademesi litre bazlıdır; eşiğin tam tanımı `UNKNOWN` → `T-858`)*, (iii) yıl-1 mi steady-state mi, (iv) SKU sayısı ile birlikte mi *(MOQ SKU başınadır)* |
| **Bağlı ticket** | `T-858` (HIGH), `T-855`, `C-462` |

---

### `D-11` — `maximum_SKU_count` / SKU stratejisi eşiği

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | MOQ **SKU başınadır** (3.000–6.000 şişe). Yani "5.000 şişelik pilot" ile "3 SKU'lu bir başlangıç ürün gamı" **aynı anda mümkün değildir.** Bu bir ekonomi sorusu değil, bir kapsam kararıdır. |
| **Katman** | Tedarik (`L0`/`L1`) tarafında MOQ; kanal tarafında listeleme bedeli `f` **SKU başına** doğar |
| **Belirlenmezse** | Pilot hacmi ile ürün gamı arasındaki çelişki modelde görünmez kalır. Zincir listelemesi tek SKU ile gerçekçi mi sorusu sorulamaz. |
| **Seçenek yapısı** | (i) SKU adedi, (ii) tek menşe mi çok menşe mi *(çok menşe = çok konteyner = LCL zorunluluğu)* |
| **Bağlı ticket** | `C-462`, `T-604`, `T-605` |

---

## GRUP D — KANAL VE TİCARİ KOŞUL EŞİKLERİ

### `D-12` — `maximum_acceptable_channel_deductions` (`d` + `f` tavanı)

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | Zincir perakende ile masaya oturulduğunda **hangi noktada kalkılacağını** belirler. TUR 2.5'te `d`'nin modele doğru girmesi (`R5` düzeltmesi) kanal marjı eksenini tornadonun **3. büyük eksenine** çıkardı (−45,06 / +32,00 TL). |
| **Katman** | `L6 → L7_eff` geçişi: `L7_eff = L6(1−d) − f`. **İkisi de ithalatçının ödediği bedellerdir** (`EV-2026-08-10-612`, Rekabet Kurulu 21-51/708-351 para.82). |
| **Belirlenmezse** | Kanal müzakeresinde walk-away noktası yoktur. Model `d` için bir `ASSUMPTION` bandı (`3/8/18 %`) taşır ve `kanal-marj-uzmani` bu bandın **seviye kanıtı olmadığını** açıkça yazmıştır — yani müzakerede kullanılamaz. |
| **Seçenek yapısı** | (i) `d` için yüzde tavanı, (ii) `f` için SKU başına TL tavanı, (iii) **birleşik** tavan mı ayrı mı, (iv) kanal başına farklı mı |
| **Bağlı ticket** | `T-604` (HIGH), `T-856` (HIGH) |

---

### `D-13` — `maximum_acceptable_payment_terms` (azami kanal vadesi)

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | `peak_cash_requirement`'ın **zaman eksenini** belirler. Bu projede vergi çıkışı (ÖTV+KDV+bandrol) **girişten önce** olduğu için vade doğrudan sermaye ihtiyacına çevrilir. |
| **Katman** | `L6` faturasının tahsil süresi |
| **AÇIK ÇELİŞKİ** | **`C-601` (HIGH, OPEN):** yasal vade tavanı 60 gün ↔ gözlenen zincir ödeme süresi ~93 gün. Ayrıca `T-601` (**CRITICAL**) açık: şişelenmiş şarabın 6585 s.K. m.7/3 anlamında *"tarım ve gıda ürünü"* olup olmadığı — **yasal tavanın hangi olduğu buna bağlı.** |
| **Belirlenmezse** | Modelin nakit bacağı `BASE 60 / STRESS 120` gün varsayımıyla koşar ve **hangisinin kabul edilebilir olduğu bilinmez.** |
| **Seçenek yapısı** | (i) gün, (ii) kanal başına ayrı mı, (iii) vade × iskonto ödünleşimi kabul ediliyor mu |
| **Bağlı ticket** | **`T-601` (CRITICAL)**, `C-601`, `T-604` |

---

## GRUP E — HEDEF VE MANDA EŞİKLERİ

### `D-14` — `PRIMARY_TARGET_SHELF_PRICE` (merdivenin hangi basamağı)

| Alan | İçerik |
|---|---|
| **Durum** | Merdivenin **kendisi** kaydedildi (`599/699/799/899/999`, KDV dahil, `INVESTOR_ASSUMPTION`, `tur-25-preflight.md` §3). **Hangi basamağın `PRIMARY` olduğu kaydedilmedi.** |
| **Ne işe yarar** | İleri modelin baz senaryosunu seçer; RFQ hedef fiyatını, ürün spesifikasyonunu ve kanal konumlandırmasını kilitler. |
| **Model ne dedi (ÖNERİDİR, KARAR DEĞİL)** | `finans-fizibilite`: `PRIMARY 799` · `SECONDARY 699` · `STRETCH 899` · `599 FLOOR/DOWNSIDE` · `999 OUT OF MANDATE`. Genel confidence **`LOW-MEDIUM`**; ajanın kendi uyarısı: *"göreli sıralama MEDIUM, mutlak çıpalama LOW — `L8_CHAIN_RETAIL` hiç gözlenmemiştir."* |
| **Katman — AÇIK `UNKNOWN`** | Hedefin **hangi `L8` alt katmanı** olduğu tanımsızdır (`T-859`, HIGH): `L8_CHAIN_RETAIL` mi, `L8_METRO_CASH_CARRY` mi, `L8_ONLINE_UZMAN_PERAKENDE` mi? Elimizdeki 473 gözlemin **`L8_CHAIN_RETAIL`'deki sayısı SIFIRDIR.** Aynı sayı farklı alt katmanda **farklı zorluktadır.** |
| **Belirlenmezse** | İleri model **beş basamağı da** taşımak zorunda kalır; senaryo sayısı beşe katlanır ve *"bu iş tutuyor mu"* sorusu beş ayrı cevap üretir. |
| **Seçenek yapısı** | (i) tek basamak mı bant mı, (ii) **hangi `L8` alt katmanı**, (iii) launch fiyatı ile steady-state fiyatı aynı mı |
| **Bağlı ticket** | `T-859`, `T-701`, `T-603`, **`T-504`** *(599 sınıflandırmasının tek dayanağı olan gözlemin promosyon durumu `UNKNOWN`)* |

---

### `D-15` — `segment_ceiling` (fiyat/performans segmentinin üst sınırı)

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | `CLAUDE.md §0` projeyi **fiyat/performans segmenti** olarak tanımlar. `pazar.yaml → segment.fiyat_performans_ust_try` bir **`ESTIMATE`**'tir ve tek kanala dayanır (`C-501` açık). Model, **mandanın dışında kalan basamağın ekonomik olarak en dayanıklı olduğunu** ölçmüştür. |
| **Neden bir yatırımcı kararı** | Bu bir araştırma sorusu değil, bir **manda sorusudur.** Ajanın ürettiği `ESTIMATE`'i modelin çıktısına bakarak yükseltmek, **mandayı model çıktısıyla değiştirmek** olur. `finans-fizibilite` bunu açıkça reddedip başkana devretmiştir. |
| **Belirlenmezse** | `999` basamağı `OUT OF MANDATE` olarak kalır ve modelin **en dayanıklı** senaryosu hiç değerlendirilmez. |
| **Seçenek yapısı** | (i) tavanı teyit et, (ii) revize et, (iii) mandayı fiyat bandı yerine **başka bir ölçütle** tanımla *(ör. fiyat/kalite oranı, rakip konumu)* |
| **Bağlı ticket** | **`T-857` (HIGH)**, `C-501`, `C-561` |

---

### `D-16` — `abort_rule` (durdurma kuralı — bir sayı değil, bir KURAL)

| Alan | İçerik |
|---|---|
| **Ne işe yarar** | `D-09` *"ne kadar kaybedebilirim"* sorusunu cevaplar; `D-16` *"neyi görürsem dururum"* sorusunu. İkisi **aynı şey değildir** ve ikincisi genellikle yazılmaz. |
| **Neden bu projede özellikle gerekli** | Bu projede kayıp **kademeli değil, basamaklıdır**: ruhsat sabit maliyeti + bandrol peşin ödemesi + gümrükte peşin ÖTV/KDV, **ilk satıştan önce** batmış maliyet hâline gelir. Durdurma kararı ancak **belirli olaylara** bağlanabilir. |
| **Belirlenmezse** | `IMPORT PILOT` kararı verilse bile pilotun **başarı/başarısızlık kriteri** olmaz — ve bu, `CLAUDE.md §9`'un `IMPORT PILOT` tanımının açıkça istediği şeydir (*"hacim, bütçe, başarı kriteri ve durdurma kriteri yazılır"*). |
| **Seçenek yapısı** | Gözlemlenebilir olaylara bağlı kurallar: (i) belirli bir sürede belirli bir satış hızına ulaşılamaması, (ii) zincir listelemesinin reddedilmesi, (iii) gerçek RFQ fiyatlarının tavanın üstünde çıkması, (iv) tercihli menşe belgesinin sağlanamaması (`g` %50→%70), (v) ÖTV artışının belirli bir eşiği aşması |
| **Bağlı ticket** | `T-851` |

---

## §2.9 — EŞİK ÖZETİ

| id | Eşik | Charter'da var mı | Katman kararı gerekli mi | Belirlenmezse bloke olan |
|---|---|---|---|---|
| `D-01` | minimum gross margin | ✅ (`TBD`) | **EVET — a/b/c** | Senaryo eleme; `TARGET BUY PRICE` |
| `D-02` | minimum contribution margin | ✅ (`TBD`) | **EVET — sabit/değişken ayrımı** | `break_even_volume` |
| `D-03` | required importer margin (μ) | ❌ **YENİ** | **EVET — μ matrahı** | `TARGET`/`WALK-AWAY`; **RFQ hedefi** |
| `D-04` | max distributor margin | ❌ **YENİ** | EVET (μ ile aynı) | `MODEL A ↔ B` karşılaştırması |
| `D-05` | maximum total capital | ✅ (`TBD`) | EVET — nakit perspektifi | `peak_cash` yorumu; `IMPORT PILOT`/`HOLD` |
| `D-06` | maximum working capital | ❌ **YENİ** | EVET | Hacim senaryolarının sıralanması; `SCALE` |
| `D-07` | maximum payback | ✅ (`TBD`) | EVET — başlangıç anı | `SCALE` ↔ `PILOT` tercihi |
| `D-08` | max inventory days | ✅ (`TBD`) | EVET — sayım başlangıcı | `D-06`; LCL↔FCL karşılaştırması |
| `D-09` | max acceptable pilot loss | ✅ (`TBD`) | EVET — stok değeri | **Pilot hacminin seçimi** |
| `D-10` | minimum annual volume | ❌ **YENİ** | **EVET — şişe mi litre mi** | `scale_intent` testi |
| `D-11` | SKU sayısı / gam | ❌ **YENİ** | — | MOQ ↔ pilot hacmi çelişkisi |
| `D-12` | max channel deductions (`d`,`f`) | ❌ **YENİ** | EVET | Kanal müzakere walk-away'i |
| `D-13` | max payment terms | ❌ **YENİ** | EVET | Nakit zaman ekseni |
| `D-14` | PRIMARY target shelf price | kısmen | **EVET — `L8` alt katmanı** | İleri modelin baz senaryosu |
| `D-15` | segment ceiling | ❌ **YENİ** | — | `999` senaryosunun değerlendirilmesi |
| `D-16` | abort rule | ❌ **YENİ** | — | `IMPORT PILOT`'ın durdurma kriteri |

> **Charter'daki 6 eşiğin 6'sı da hâlâ `TBD`'dir. TUR 2.5, listeye 10 eşik
> daha eklemiştir.** Bunların hiçbiri başkanın icadı değildir; hepsi
> `finans-fizibilite`, `kanal-marj-uzmani` ve `global-sourcing-kasifi`'nın
> raporlarında **modelin duraksadığı noktalar** olarak zaten kayıtlıdır.

---

# §3 — EŞİK DIŞI YATIRIMCI GİRDİLERİ (`I-1` … `I-8`)

> Bunlar **eşik değildir** — bir risk iştahı ifade etmezler. Ama yine de
> yatırımcıdan gelirler ve hiçbir ajan bunları araştırarak kapatamaz.

### `I-1` — `fx` (USD/TRY, EUR/TRY, EUR/USD + kur tarihi) · **CRITICAL**

```yaml
durum:        makro.yaml -> fx = null   (UC TURDUR: TUR 0, TUR 2, TUR 2.5)
ticket:       T-852 (CRITICAL, target: yatirim-komitesi-baskani)
              T-912 (CRITICAL, target: finans-fizibilite)
maliyet:      ~0 TL, dakikalar
```

| Soru | Cevap |
|---|---|
| **Neden ajan kapatamıyor** | `finans-fizibilite`'nin araştırma aracı **yoktur — kasıtlı tasarımdır** (CLAUDE.md §7). `T-852` bunu `T-912`'nin hedef düzeltmesi olarak açmıştır: kur, bu ajanın **araştırabileceği** değil, kendisine **verilmesi gereken** bir girdidir. |
| **Model tam olarak nerede duruyor** | `MAX_CIF_TRY` ✅ hesaplandı (2.700 satır) · **`MAX_FOB_TRY` ❌ `UNKNOWN`** · **`MAX_EXW_TRY` ❌ `UNKNOWN`** · döviz karşılıklarının tamamı `UNKNOWN`. |
| **Neden sadece bir birim dönüşümü değil** | Ters modelde **9 ülke için 9 farklı sayı YOKTUR — 2 farklı sayı vardır** (`g = 0,50` veya `0,70`). Ülkeler arası gerçek ayrışma **FOB seviyesinde** doğar ve o bacak `fx` olmadan hesaplanamaz. **`fx`, modelin ülke ayrıştırma gücünün ön koşuludur.** |
| **Açtığı şey — tek adımda** | Navlun USD/şişe **9 rotanın 9'unda elimizdedir** (`EV-2026-08-10-301…-311`). `fx` girdiği an `MAX_FOB` **anında** hesaplanır ve *"bu segment matematiksel olarak mümkün mü"* sorusunun **asıl testine** ulaşılır. |
| **İkinci etkisi** | `C-852` gereği bugünkü `cif_try_max` bir **üst sınırdır**, çünkü L2–L5 arasındaki **USD cinsli varış masrafları** düşülememiştir. `fx` geldiğinde üst sınır gerçek bir tavana döner. |
| **Gereken tam girdi** | `usd_try`, `eur_try`, `eur_usd` — her biri **`kur_tarihi` + kaynak** ile; ayrıca **LOW/BASE/HIGH bandı** (`senaryolar.yaml → duyarlilik_eksenleri[FX]` üçü de `null`). |
| **Uyarı** | **Gümrük beyan kuru** serbest piyasa kurundan farklı olabilir; kural `UNKNOWN`'dır (`T-911`, `gumruk-vergi-uzmani`). Yatırımcı kuru verse bile bu ayrı bir açık kalır. |

> **Bu, projede üç turdur kapanmayan, maliyeti ~sıfır olan ve en çok çıktı
> açan tek girdidir.** Bunu üçüncü kez kayda geçiriyorum.

---

### `I-2` — `model_hedef_tarihi` · **KAYDEDİLDİ, `INVESTOR_ASSUMPTION`**

```yaml
BASE  = 2027-04-01   (EARLY 2027-01-01 / LATE 2027-07-01)
status = INVESTOR_ASSUMPTION      # FACT DEGIL, evidence_id YOK ve OLMAYACAK
oq     = OQ-002  ->  INPUT_RECORDED (KAPATILMADI)
```

- Kaydedilen bir **olgu değil, bir beyandır**; kanıt kartı açılmamıştır ve açılmayacaktır.
- **Üç hedef tarihin üçü de** ÖTV serisinin `son_gozlem_gecerlilik_ufku`'nun (2026-12-31) **ötesindedir** → hiçbiri için doğrulanmış ÖTV tutarı yoktur.
- `BASE` üç aday içinde **rejim açısından tek net olanıdır** (iki revizyonun tam arasında). Bu bir tespittir, bir tavsiye değil.
- **Kapanış koşulu:** `T-921` `RESOLVED` **VE** tarihin `t0-takvimi`nden doğrulanması (`T-202`/`C-202`). Birincisi bu turda gerçekleşti; **ikincisi olmadı** → `OQ-002` açık kalır.

---

### `I-3` — ÖTV `λ` projeksiyon varsayımı (Yİ-ÜFE ekseni) · **HIGH**

```yaml
durum:   makro.yaml -> enflasyon.* = UNKNOWN
ticket:  T-104 (CRITICAL) ikinci ayagi
sonuc:   varsayim yoksa cikti UPPER_BOUND olarak KALIR
```

| Soru | Cevap |
|---|---|
| **Neden bir yatırımcı girdisi** | ÖTV maktu tutarı Ocak/Temmuz'da Yİ-ÜFE ile **kendiliğinden** artar (ÖTVK md.12/3, T1). **Gelecek Yİ-ÜFE bilinemez.** Hiçbir ajan bunu araştırarak bulamaz; yalnızca bir **`ASSUMPTION`** olarak konulabilir ve o varsayımın sahibi yatırımcıdır. |
| **Bugünkü durum — doğru davranış** | Engine, hedef tarih ufku aştığında ve **açık senaryo bayrağı yoksa `UNKNOWN` döner** (`T-921` ile eklendi, tarafımdan doğrulandı). Çıktı üretmek için `UPPER_BOUND_LAMBDA_1` bayrağı kullanılmıştır: **λ=1, yani ÖTV 2026-07-03 çapasında donduruldu.** |
| **Yönü tek taraflı** | **λ ≥ 1** olduğu için gerçek ÖTV **daha yüksek**, gerçek `MAX_CIF` **daha düşüktür**. Vergi tarafında **yukarı sürpriz yoktur.** |
| **Belirlenmezse** | Tüm parasal çıktılar `UPPER_BOUND` etiketli kalır. Bu **kabul edilebilir bir durumdur** ve `KILL` kararını destekleyebilir *(tavan bile yetmiyorsa)*, ama `IMPORT PILOT` kararını **destekleyemez** *(tavan yetiyor demek, gerçeğin yettiği anlamına gelmez)*. |
| **Seçenek yapısı** | (i) bir Yİ-ÜFE bandı `ASSUMPTION`'ı (min/base/max), veya (ii) **hiçbir varsayım koymamak** ve tüm çıktıyı bilinçli olarak `UPPER_BOUND` kabul etmek. **İkisi de meşrudur; birini seçmek gerekir.** |

> ⚠ **Aynı tarih riski bandrol, TADAB ve ruhsat kalemlerinde de vardır** ve
> orada **kod düzeyinde korunmamaktadır**: bandrol her 1 Ocak'ta Yİ-ÜFE ile
> güncellenir, hedef tarihlerin üçü de 2027'dedir → model 2026 değerini
> kullanmak zorunda kalmıştır (`T-858`, `mevzuat-ruhsat-uzmani`).

---

### `I-4` — **DIŞ TEMAS İZNİ** · **CRITICAL** *(bir veri eksikliği DEĞİL)*

> ## Bu, bu belgedeki en yanlış anlaşılan maddedir.

```yaml
ticket:  T-467 (RFQ gonderimi — global-sourcing-kasifi -> baskan)
         T-304 (FCL navlun kotasyonu — navlun-lojistik -> baskan)
nitelik: IZIN ve ZAMANLAMA sorunu ; VERI EKSIKLIGI DEGIL
```

| | RFQ (`T-467`) | Forwarder kotasyonu (`T-304`) |
|---|---|---|
| **Ne bloke ediyor** | **`G2`** — gerçek EXW/FOB fiyatı yok; `T-466` (CRITICAL) `exw`/`fob`'u `null` tutuyor | **`G2-L`** — hiçbir rotada doğrulanmış FCL navlunu yok; `C-311` bandı **4–5 kat** |
| **Havuz hazır mı** | ✅ **26 tedarikçi tanımlı**, RFQ şablonu hazır | ✅ 3 forwarder'dan kalem kırılımlı yazılı kotasyon isteniyor |
| **Neden kapanmıyor** | **Dış iletişim izni verilmedi** | **Dış iletişim izni verilmedi** |
| **Masabaşıyla açılabilir mi** | ❌ **HAYIR** — açıkça kayıtlı | ❌ **HAYIR** — TUR 2'de denendi, band daraltılamadı |
| **Ters model üzerindeki etkisi** | Yüksek (tavanın **kullanılıp kullanılamayacağı**) | **SIFIR** — navlun CIF'in içindedir, tavanı değiştirmez (`§8.3`). **İleri model ve FOB pazarlığı için blokerdir.** |

> **Kayıt:** `G2` ve `G2-L`, üç turdur *"veri bulunamadı"* diye değil,
> **temas edilmediği için** kapalıdır. Bu ayrım TUR 6 kararında açıkça
> yazılmalıdır: *"tedarik kaynağı yok"* ile *"tedarikçilere henüz sorulmadı"*
> aynı şey değildir ve **ikincisi bir KILL gerekçesi olamaz.**

---

### `I-5` — Antrepo / bandrolleme tesisinin yeri (`OQ-911`) · **HIGH**

- Varış limanı **terminal tarifesine göre değil**, bandrolleme tesisinin ve hedef pazarın yerine göre seçilir (`EV-2026-08-10-332`) — **ama o tesisin yeri hiçbir yerde tanımlı değildir.**
- Mertebe farkı: THD farkı ≈ 0,006–0,011 USD/şişe; **iç nakliye farkı 2,7–3,2 TRY/şişe** → **~2 kat mertebe farkı.**
- `lojistik.yaml → ic_lojistik.*` TRY bacağının **en büyük tek kalemidir.**
- **Araştırmayla kapanmaz** — yatırımcı beyanı veya 2–3 antrepo/3PL teklifi gerekir (bu da `I-4` iznine bağlıdır).

---

### `I-6` — Finansman maliyeti / sermaye maliyeti (`makro.finansman`) · **MEDIUM**

- `RC4`: devreden KDV'nin **kilitlendiği sürenin finansman maliyeti** gerçek bir maliyettir ve ters modelde `L5` satırı olarak durur — **tutarı `UNKNOWN`, `0` alınmıştır** (13 sıfırlanan kalemden biri).
- KDV'nin kendisi maliyet değildir (indirilebilir); **bekleme süresinin bedeli** maliyettir.
- Piyasa faizi bir araştırma konusudur; **şirketin kendi sermaye maliyeti bir yatırımcı girdisidir.** İkisi karıştırılmamalıdır.

---

### `I-7` — İş modeli önceliği (`business_model_priority`) · **KAYITLI, AMA UYGULANMADI**

- Charter: *"Existing brand distribution ve Private label **eşit önceliklidir**; birini gerekçesiz öne çıkarmak yasaktır."*
- **`OQ-902` (HIGH, OPEN):** `global-sourcing-kasifi` TUR 1'de ikisini eşit derinlikte araştıramadığını **kendisi itiraf etmiştir.**
- Yatırımcı bu önceliği **koruyor mu, değiştiriyor mu** — bu bir araştırma sonucu değil, bir kapsam kararıdır ve `D-11` (SKU) ile doğrudan bağlıdır.

---

### `I-8` — TUR 3A / TUR 3B çalıştırma tarihi (`OQ-912`) · **HIGH**

- Projenin kanıt tabanı **dar bir tazelik penceresi** içindedir: **10 canlı LCL kotasyonu 2026-08-16'da `STALE`** olur (bugün itibarıyla **6 gün**).
- TUR 2.5 modeli **2026-08-10'da koşulmuştur → navlun bacağı bugün geçerlidir** (`P-3` sağlandı).
- **Bir sonraki çalıştırma bu pencerenin dışına düşerse** `T-913` ile kotasyonlar yenilenmeli veya navlun bacağı bilinçli olarak `UNKNOWN` kabul edilip **çıktıda açıkça yazılmalıdır.**
- Bu bir **zamanlama kararıdır**, bir veri eksiği değil.

---

# §4 — HANGİ EŞİK HANGİ ÇIKTIYI AÇIYOR (BAĞIMLILIK HARİTASI)

| Model çıktısı | Bugünkü durum | Açan girdi(ler) |
|---|---|---|
| `MAX_CIF_TRY` | ✅ **var** (`UPPER_BOUND`) | — |
| `MAX_FOB_TRY` / `MAX_EXW_TRY` | ❌ `UNKNOWN` | **`I-1` (fx)** |
| Ülkeler arası gerçek ayrışma | ❌ 9 ülke → **2 sayı** | **`I-1` (fx)** |
| `TARGET BUY PRICE` | ❌ üretilmedi | **`D-03`** (+ `D-01`) |
| `WALK-AWAY PRICE` | ❌ üretilmedi | **`D-03`** + `D-16` |
| `MODEL A ↔ MODEL B` kararı | ❌ karşılaştırılamıyor | **`D-04`** (+ `T-604`) |
| `break_even_volume` | ❌ hesaplanmadı | **`D-02`** + `D-10` |
| `peak_cash_requirement` **tutarı** | ❌ yalnız yapısı var | `I-1` + `T-466` + **`T-301`** + `D-13` |
| `peak_cash` **kabul edilebilir mi** | ❌ | **`D-05`**, `D-06` |
| Senaryo eleme (2.700 satır → kısa liste) | ❌ | **`D-01`** + `D-14` |
| Pilot hacmi | ❌ 5.000 bir varsayım | **`D-09`** + `D-10` + `C-462` |
| `IMPORT PILOT` başarı/durdurma kriteri | ❌ | **`D-16`** |
| `λ` çıktı etiketinin `UPPER_BOUND`'dan çıkması | ❌ | **`I-3`** |

> **Okuma:** Eşiklerin **hiçbiri** ters modelin bugünkü çıktısını değiştirmez.
> Hepsi **ileri modeli** ve **karar verilebilirliği** açar. Bu yüzden TUR 3A
> bu belge olmadan yürüyebilir, TUR 3B yürüyemez.

---

# §5 — YATIRIMCIYA **SORULMAMASI** GEREKENLER (SINIR BEYANI)

Aşağıdakiler yatırımcı kararı **değildir** ve bu belgede yer almazlar.
Bunları yatırımcıya sormak, bir araştırma boşluğunu bir karara dönüştürerek
gizlemek olurdu:

| Sorulmaz | Neden | Sahibi |
|---|---|---|
| Gerçek zincir raf fiyatı (`l8_chain_retail`) | Bir **gözlemdir**; bir mağaza turuyla ölçülür | `turkiye-pazar-kasifi` (`T-603`, `T-917`) |
| Gerçek distribütör marjı **seviyesi** | Bir piyasa olgusudur *(tavanı `D-04`'tür — ikisi farklıdır)* | `kanal-marj-uzmani` (`T-604`) |
| Gerçek EXW/FOB fiyatı | RFQ ile ölçülür *(izni `I-4`'tür)* | `global-sourcing-kasifi` (`T-466`) |
| KDV indirim hakkının alkolde kısıtlı olup olmadığı | Bir **mevzuat olgusudur** — ~sıfır maliyetle taranabilir | `gumruk-vergi-uzmani` (`T-947`, `T-151`) |
| Gözetim eşiğinin varlığı | Bir mevzuat olgusudur | `gumruk-vergi-uzmani` |
| Antrepo zorunlu bekleme süresi | Bir mevzuat/operasyon olgusudur | `mevzuat-ruhsat-uzmani` (`T-301`) |
| 2027 ÖTV **tutarı** | **Bilinemez** — yalnızca bir `ASSUMPTION` konulabilir (`I-3`) ve o bir tutar değil, bir **artış varsayımıdır** | — |

---

# §6 — MİNİMUM AÇILIŞ SETİ

> Yatırımcı **hepsini** cevaplamak zorunda değildir. TUR 3B'nin **başlaması**
> için gereken asgari set aşağıdadır; kalanı TUR 3B çıktısı görüldükten sonra
> verilebilir — **ama o durumda `IR-4` (hedef kaydırma) riski kayda geçer.**

| Sıra | Girdi | Neden asgari | Maliyet |
|---|---|---|---|
| **1** | **`I-1` — fx** | Modelin ülke ayrıştırma gücünün ön koşulu; `MAX_FOB`/`MAX_EXW`'yi tek adımda açar | dakikalar, ~0 TL |
| **2** | **`D-03` — μ ve MATRAHI** | `TARGET`/`WALK-AWAY` üretilemiyor; **RFQ'ya yazılacak hedef fiyat bunsuz yok** | karar |
| **3** | **`D-01` — brüt marj tabanı + KATMAN ÇİFTİ** | 2.700 satırlık çıktı bunsuz elenemez | karar |
| **4** | **`D-05` — sermaye tavanı** | `peak_cash` hesaplandığında karşılaştırılacak nesne | karar |
| **5** | **`I-4` — dış temas izni** | `G2` ve `G2-L` üç turdur **temas edilmediği için** kapalı | izin |
| **6** | **`D-14` — PRIMARY basamak** | İleri modelin baz senaryosu | karar |

> **1 ve 5 birer karar bile değildir** — biri bir kayıt, diğeri bir izindir.
> **İkisi de üç turdur bekliyor.**

---

# §7 — `OQ-901` GÜNCELLEMESİ

```yaml
oq_id:            OQ-901
onceki_durum:     OPEN
yeni_durum:       OPEN — SPECIFIED        # KAPATILMADI
guncelleme:       2026-08-10 (TUR 2.5 kapanis)
belge:            90-karar/investor-decisions-required.md
kapsam_degisikligi: "6 esik -> 16 esik + 8 esik disi yatirimci girdisi"
kapanis_kosulu:   "§6'daki MINIMUM ACILIS SETI'nin cevaplanmasi
                   VEYA her esik icin 'belirlemiyorum' beyani + sonucunun kabulu"
bloke_ettigi:     "TUR 3B (ileri model) + TUR 6 (nihai karar)"
```

**Neden kapatılmadı:** `OQ-901` bir **soru**dur, bir **belge** değil. Bu belge
soruyu **görünür ve cevaplanabilir** hâle getirir; **cevaplamaz.** Kapanışı
yalnızca yatırımcı yapabilir — hiçbir ajan, başkan dahil, `OQ-901`'i
kapatamaz.

---

## Bu kararı ne çürütür?

*(Bu belge bir yatırım kararı içermez. Aşağıdaki soru bu belgenin tek
hükmüne ilişkindir: **"TUR 3B'nin blokeri bir veri eksikliği değil, bir karar
eksikliğidir."**)*

### En güçlü tek çürütücü bulgu

> ### **KDV indirim hakkının alkolde kısıtlanmış olması.**

Bu tek mevzuat olgusu bu belgenin hükmünü doğrudan çürütür: eğer ithalatta
ödenen KDV **indirilemiyorsa**, ters modelin ekonomik dalının tamamı geçersiz
olur ve **tüm tavanlar ~%22,7 düşer** (`rapor-tur25-finans.md` §9.1). O
durumda TUR 3B'nin blokeri bir karar eksikliği **değil**, bir veri hatasıdır —
ve eşiklerin hiçbiri o hatayı kurtaramaz. Yatırımcıdan 16 eşik istemiş
olurduk, oysa yapılması gereken **bir saatlik bir mevzuat taramasıydı.**

`gumruk-vergi-uzmani` KDVK md.36 uyarınca çıkarılmış bir Cumhurbaşkanı
Kararının **aranmadığını** kendisi işaretlemiştir (`T-151`, `OQ-G10`) ve bu
kontrol **üç turdur yapılmamıştır.**

**Nasıl ararız:** `T-947` (bu turda **CRITICAL** olarak açıldı) — TUR 3A'nın
**birinci işidir**, saatler sürer, maliyeti ~sıfırdır ve bu belgenin
gönderilmesini beklemez.

### İkinci en güçlü çürütücü (farklı hükmü hedefler)

> **Gerçek RFQ fiyatlarının, katkı payı sıfır alınmış `MAXIMUM STRUCTURAL BUY
> PRICE` tavanının bile ÜSTÜNDE çıkması.**

Bu durumda `D-01`…`D-16`'nın hiçbiri anlam taşımaz: hangi marjı hedeflediğiniz
önemsizdir, çünkü **sıfır marjda bile kapanmıyordur.** Eşik sormak, cevabı
zaten belli olan bir soruyu süslemek olurdu. Bu, `I-4` (dış temas izni)
maddesinin **neden eşiklerden önce geldiğini** gösterir.

### Bu belgenin en kırılgan hükmü

**"Eşikler ileri model çıktısından ÖNCE yazılabilir ve yazılmalıdır."**

Charter'ın kendi önerisi bunun **tersidir** (*"önerilen an: TUR 3 sonrası —
yatırımcı gerçek sayı aralıklarını görsün"*). Ben eşiklerin **önce**
yazılmasını savunuyorum çünkü sonra yazmak hedef kaydırma riski taşır
(`IR-4`). **Ama bu bir ödünleşmedir, bir üstünlük değildir:** önce yazılan
eşik **bilgisiz** olabilir ve gerçekçi olmayan bir tabanı sabitleyerek
projeyi haksız yere öldürebilir.

**Bu ödünleşmeyi çözecek şey yok** — yalnızca hangisinin seçildiğinin
**kayda geçirilmesi** var. Yatırımcı eşikleri model çıktısını gördükten
sonra vermeyi seçerse, bu tercih `karar-gunlugu.md`'ye yazılmalı ve
`seytanin-avukati` TUR 4'te bunu bir saldırı vektörü olarak kullanmalıdır.

### Bu belgenin kör noktası

Bu belge de **hiçbir yeni kanıt üretmemiştir.** Yaptığı şey, beş ajanın
raporlarında **modelin duraksadığı noktaları** toplayıp yatırımcıya tek bir
listede sunmaktır. Eğer o raporlardan biri bir boşluğu **hiç fark etmediyse**,
o boşluk bu listede de yoktur. En muhtemel adayı: **talep tarafı.** Projede
talep elastikiyeti için **tek bir veri yoktur** ve bu belgede **tek bir eşik
de yoktur** — çünkü hiçbir ajanın modeli talebe duraksamamıştır. *"Kaç şişe
satılır"* sorusu, `D-10`'da bir **hedef** olarak duruyor; bir **tahmin**
olarak hiçbir yerde durmuyor.
