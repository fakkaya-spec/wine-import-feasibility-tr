# AJAN RAPORU — MEVZUAT & RUHSAT (TUR 1.5 — BLOCKER REMEDIATION)

```yaml
ajan:    mevzuat-ruhsat-uzmani
tur:     TUR 1.5
tarih:   2026-08-10
durum:   SUBMITTED
kapsam:  "TEK SORU — 4250 s.K. m.1/3 hacim esiginin 750 ml siselenmis durgun
          sarap ithalatina gercek hukuki etkisi (T-201 / C-201)"
ana_cikti: 20-mevzuat/1m-litre-esigi.md
```

> Bu rapor **dar kapsamlıdır.** TUR 1'in genel ruhsat/etiket/bandrol taraması
> tekrarlanmamıştır. `C-203` / `T-205` (7584 s.K. raf/marka yasağı) tur mandası
> gereği **ele alınmamıştır.**

---

## 1. YÖNETİCİ ÖZETİ

Aranan tek şey, 4250 s.K. m.1/3'teki "1.000.000 litre/yıl" eşiğinin bu proje için
ne olduğuydu. **Bulunan şey, eşiğin sorulduğu haliyle mevcut olmadığıdır:**
kanun metnindeki 1.000.000 rakamı, 4619 s.K. Geçici m.1 ve Ticaret Yönetmeliği
Geçici m.6 uyarınca **2006 yılı sonunda 600.000 litre/yıl**'a inmiş ve kademeli
takvim orada sona ermiştir (`EV-2026-08-10-204`, `EV-2026-08-10-205`, ikisi de T1).

**Eşiğin türü kesinleşmiştir:** bir **ithalat**, **dağıtım yetkisi** veya
**teminat/bedel** eşiği **değildir**; 4250 m.1/3 metnindeki bir **fiyat belirleme
serbestisi koşuludur**. İthalat ve dağıtım yetkisi için yürürlükteki Yönetmelikte
**hiçbir asgari hacim şartı yoktur**; hacim yalnızca **bedel matrahıdır** ve
şaraptaki tek bedel kırılımı **20.000 litre/yıl**'dır (`EV-2026-08-10-207`;
`EV-2026-08-09-206`). Dahası, kanun koyucunun eşiği aşamayan firmaların
fiyatlandırılmasını düzenlemek üzere verdiği yetki (4733 m.9/B) ilgili
Yönetmelikte **kullanılmamıştır** — metinde "fiyat" kökünü içeren **tek bir
kelime bile geçmez** (`EV-2026-08-10-206`, `-209`).

**Beş hacim senaryosunun tamamı (3.750–75.000 litre/yıl) eşiğin çok altındadır**
ve senaryolar arasında ayrım yaratmaz; eşiğe ulaşmak **800.001–1.333.334 şişe/yıl**
gerektirir — en büyük senaryonun **8–13,3 katı** (`EV-2026-08-10-215`).

**Proje aleyhine iki bulgu gizlenmemiştir:** (a) "yaptırım mercii ortadan kalktı"
argümanı **çürüktür** — 4733 m.4/B(b) 4250'nin uygulanmasını açıkça Bakanlığa
vermiştir (`EV-2026-08-10-208`); (b) 4733 m.8'in artık fıkrası, sayılmayan tüm
4250 aykırılıkları için **uyarı → süre → belge iptali** yolunu açık tutar
(`EV-2026-08-10-210`).

**G0 önerisi: `G0 PASS`** (T-201/C-201 boyutu yönünden koşulsuz). **T-201:
`ANSWERED`.** Bkz. §10.

---

## 2. BULGULAR

### B-1: Uygulanan ölçü 1.000.000 değil, en çok 600.000 litre/yıl

```yaml
claim:          4250 m.1/3'teki hacim olcusu, 4619 s.K. Gecici m.1 ve Ticaret Yonetmeligi Gecici m.6 uyarinca kademeli olarak indirilmis ve takvim 2006 yili sonunda 600.000 litre/yil'da sona ermistir.
value:          600000
unit:           litre/yil
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-204, EV-2026-08-10-205
effective_date: 2001-01-20 (4619 Gec. m.1) / 2003-06-06 (Yonetmelik Gec. m.6)
katman:         -
```

**Gerekçe:** İki metin birbirini doğruluyor. 4619 Geçici m.1, 4250'ye
**işlenemeyen hüküm** olarak konsolide metnin sonundadır ve "beşinci takvim yılı
sonuna kadar altı yüz bin litre/yıl olarak uygulanır" der. Ticaret Yönetmeliği
Geçici m.6 aynı takvimi **somut yıllarla** sabitler: "2006 yılı sonuna kadar
altıyüzbin litre". Yönetmeliğin son değişikliği RG 2/2/2023-32092'dir ve Geçici
m.6 **hiç değiştirilmemiştir**.

> **Bu, TUR 1 raporumun bir düzeltmesidir.** TUR 1'de eşik 1.000.000 olarak
> sunulmuştu. `EV-2026-08-09-227` bu kartla `SUPERSEDED` yapılmıştır.

---

### B-2: Eşik bir ithalat / dağıtım yetkisi / bedel eşiği DEĞİLDİR

```yaml
claim:          Yururlukteki Yonetmeligin esas maddelerinde ithalat veya dagitim yetki belgesi icin hicbir asgari hacim sarti yoktur; beyan edilen yillik faaliyet hacmi yalnizca bedel matrahidir.
value:          "asgari hacim sarti: YOK"
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-207, EV-2026-08-10-206
effective_date: 2015-12-31
katman:         -
```

**Gerekçe:** Yönetmelik m.10/b, dağıtım yetki belgesi başvurusunda *"planladığı
yıllık faaliyet hacmini gösteren faaliyet dosyası"* ister — bir **asgari** değil.
m.12/1 hacmi bedelle ilişkilendirir ve *"Yıllık faaliyet hacminin, o yıl için
öngörülen litre miktarını aşması halinde ise aşan miktara ilişkin bedel Kurum
tarafından ayrıca tahsil edilir"* der. Yani hacim **cezalandırılan değil
faturalanan** bir değişkendir.

Ayrıca Yönetmeliğin tam metin taramasında *"bir milyon"* ifadesi **yalnızca
Geçici m.6'da** (1 eşleme) geçer; esas maddelerde **0**.

---

### B-3: Eşiğin tek işlevi — fiyat belirleme serbestisi; mekanizma ikincil mevzuata aktarılmamış

```yaml
claim:          4250 m.1/3'teki olcu, esigi asan firmaya 'fiyat belirlemekte serbestlik' taniyan bir kosuldur; asamayanlar icin ongorulen 'Tekel Genel Mudurlugu eliyle fiyatlandirma/satis/dagitim' mekanizmasi, 4733 m.9/B ile yetkilendirilmis olmasina ragmen ilgili Yonetmelikte KURULMAMISTIR.
value:          "esik turu: FIYATLANDIRMA SERBESTISI KOSULU"
status:         ESTIMATE
tier:           T2
evidence_id:    EV-2026-08-10-216 (turetme); girdi metinleri EV-2026-08-10-201, -202, -206, -209, -210 (T1)
effective_date: 2001-01-20 (4250 m.1/3) / 2017-12-24 (4733 m.9/B)
katman:         -
```

**Türetme zinciri:**
1. 4250 m.1/3 c.2–3: eşiği aşan **serbesttir**; aşamayanın ürünü **Tekel GM
   eliyle** fiyatlandırılır/satılır/dağıtılır (`EV-...-201`, T1).
2. 4250 m.7: idari para cezası bentlerinin tamamı **yalnızca m.6'ya** atıf yapar;
   m.1 ihlaline bağlı İPC **yoktur** (`EV-...-211`, T1) → bu bir ceza değil,
   bir **rejim atamasıdır**.
3. 4733 m.9/B: *"üretim şartını karşılamayan firma mamullerinin fiyatlandırılması,
   dağıtılması, satışı ve kontrolü"* **açıkça bir Bakanlık yönetmeliğine**
   bırakılmıştır (`EV-...-209`, T1).
4. Alkol tarafındaki o yönetmelik (7.5.6203) yürürlüktedir ve içinde **"fiyat"
   kökünü içeren hiçbir kelime yoktur (0 eşleme)** (`EV-...-206`, T1)
   → devredilen yetki **kullanılmamıştır**.
5. 4250 m.1 son fıkrası *"her türlü şarabın"* **fiyatlandırılmasını, dağıtılmasını
   ve satılmasını** m.1 şartlarından muaf tutar — ki m.1/3'ün mekanizması tam
   olarak bu üç faaliyettir (`EV-...-202`, T1). *(Bu adımın ithal şarabı kapsayıp
   kapsamadığı `C-252` olarak açıktır — bkz. §4.)*

**tier gerekçesi:** Girdi metinlerinin tamamı T1'dir; **sonuç bu ajanın hukuki
analizidir** ve bir idari makam yorumu değildir. Başkanın T-904 kuralına uyarak
türetmeye T1 verilmemiş, **T2** verilmiştir.

---

### B-4: "Yaptırım mercii yok" argümanı ÇÜRÜDÜ *(proje aleyhine)*

```yaml
claim:          4733 s.K. m.4/B(b), '4250 sayili Kanunun uygulanmasina yonelik islemleri' acikca Tarim ve Orman Bakanligina (TADAB) vermistir; ayrica 4733 m.8'in artik fikrasi 4250'ye aykiriliklar icin uyari-sure-BELGE IPTALI yolunu acik tutar.
value:          "4250 uygulama mercii: Tarim ve Orman Bakanligi"
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-208, EV-2026-08-10-210
effective_date: 2017-12-24 (KHK-696) / 2018-03-08 (7079 aynen kabul)
katman:         -
```

**Gerekçe:** TUR 1'de *"yaptırım mercii Tekel GM artık mevcut değildir,
dolayısıyla hükmün bugün nasıl uygulandığı belirsizdir; uygulanamaz hâle geldiği
yorumu makul"* yazmıştım. **Bu yorumun dayanağı çürümüştür.** Görev devri T1
düzeyinde açıktır. Bu bulgu G0 önerimin **aleyhinedir** ve raporun en görünür
yerine konmuştur.

**Ne çürümedi:** m.1/3 c.3'teki **ticari** işlevi (ürünü fiilen fiyatlandıracak,
satacak, dağıtacak merci) belirleyen bir düzenleme **bulunamamıştır** — bu ayrı
bir `UNKNOWN`'dır (`EV-2026-08-10-214`) ve **negatif ispat yapılmamıştır**.

---

### B-5: Beş senaryonun tamamı eşiğin çok altında

```yaml
claim:          5.000-100.000 sise/yil senaryolari 3.750-75.000 litre/yil'a karsilik gelir; en buyugu bile 600.000 L olcusunun %12,5'i, 1.000.000 L olcusunun %7,5'idir.
value:          "3750 | 7500 | 18750 | 37500 | 75000"
unit:           litre/yil
status:         ESTIMATE
tier:           T2
evidence_id:    EV-2026-08-10-215
effective_date: -
katman:         -
```

**Türetme zinciri:** hacim = şişe adedi × **0,75 litre** (750 ml,
`00-charter/kapsam.md` proje kapsam tanımı).

| Senaryo | Şişe/yıl | Litre/yıl | 1.000.000 L'nin %'si | 600.000 L'nin %'si |
|---|---|---|---|---|
| S1 | 5.000 | **3.750** | %0,375 | %0,625 |
| S2 | 10.000 | **7.500** | %0,75 | %1,25 |
| S3 | 25.000 | **18.750** | %1,875 | %3,125 |
| S4 | 50.000 | **37.500** | %3,75 | %6,25 |
| S5 | 100.000 | **75.000** | %7,5 | **%12,5** |

Eşiğe ulaşmak için: **1.333.334 şişe/yıl** (1.000.000 L) veya **800.001 şişe/yıl**
(600.000 L). En büyük senaryonun **13,3 / 8,0 katı**.

**tier gerekçesi:** Girdi eşikleri T1'dir; ancak türetme, tier atanamayan bir
proje tanımını (750 ml) da kullandığı için **T2** verilmiştir.

---

### B-6: TUR 1'in "yerinde teslim teyitlidir" iddiası yanlıştı

```yaml
claim:          Ticaret Yonetmeligi m.9/2, 4250 m.1/3'teki 'ulke genelinde yerinde teslim' sartini TEYIT ETMEZ; ikincil mevzuattaki yukumluluk daha dardir ve 'perakende saticilarin taleplerini zamaninda karsilayacak dagitimi saglamak' seklindedir.
value:          "Yon. m.9/2 'ulke genelinde' ve 'yerinde teslim' ifadelerini ICERMEZ"
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-212
effective_date: 2007-07-24
katman:         -
```

**Gerekçe:** Öz-düzeltme. Bu, eşikle ilgili değildir ama **T-201'in ikinci
ayağıydı** ("ülke geneli yerinde teslim şartı bağımsız olarak da geçerli
görünmektedir ve Ticaret Yön. m.9/2 ile teyitlidir"). Yükümlülük **kanunda
vardır** ve hacimden bağımsızdır; ancak ikincil mevzuattaki karşılığı **daha
zayıftır**. Bu fark dağıtım maliyeti tahminini etkiler → `kanal-marj-uzmani`
(X-251).

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Yön | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|---|
| 1 | 2007'den itibaren ölçüyü **sıfıra indiren** BKK/CBK var mı (`EV-...-214`) | `mevzuat.gov.tr` ve `resmigazete.gov.tr` bu oturumda TLS doğrulaması nedeniyle erişilemedi (`unable to get local issuer certificate`); tarama TADAB aynası + web araması ile sınırlı kaldı | **LEHİNE** (varsa eşik tamamen kalkar) | **HAYIR** | Farklı ağdan Resmî Gazete taraması |
| 2 | 2007+ uygulanan ölçü 600.000 mi 1.000.000 mi (**C-251**) | Geçici hükümdeki *"bu ölçü"* ifadesinin göndergesi lafzen belirsiz | nötr | **HAYIR — maddi değil** | TADAB yazılı görüşü |
| 3 | Muafiyet fıkrasının ithal durgun şarabı kapsayıp kapsamadığı (**C-252**) | Aynı cümlenin iki eşit lafzî okuması | belirsiz | HAYIR | TADAB görüşü / hukuk bürosu mütalaası |
| 4 | "Tekel GM eliyle" **ticari** işlevin bugünkü halefi (`EV-...-214`) | Belirleyici düzenleme bulunamadı; negatif ispat yapılamaz | **ALEYHİNE** | HAYIR | TADAB'a KEP ile yazılı görüş |
| 5 | Eşik altındaki ithalatçıların **fiilî** durumu — ampirik doğrulama (`EV-...-213`) | TADAB Resmî İstatistikleri **yalnızca yakıt biyoetanolü** içeriyor; firma bazında hacim yayımlanmıyor. **T-201'in önerilen doğrulama yollarından biri bu turda kapandı.** | nötr | HAYIR | Faal küçük ölçekli şarap ithalatçısıyla görüşme |
| 6 | "Ülke genelinde yerinde teslim" şartının fiilî ölçütü ve maliyeti | Mevzuatta ölçüt tanımlı değil; ayrıca bu turun kapsamı dışı | **ALEYHİNE** | HAYIR (G0 için); kanal modeli için önemli | `kanal-marj-uzmani` + TADAB uygulaması |
| 7 | 4733 m.8 artık yaptırımının 4250 m.1/3 bağlamında fiilen uygulandığı örnek | Aranmadı (kapsam) | ALEYHİNE | HAYIR | TADAB "İdari Yaptırımlar" arşivi |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-201** | — | — | Üç ayağından **ikisi düştü** (B-1, B-4). Kalan ayak C-252 olarak yeniden numaralandı. **Öneri: `RESOLVED — NON_MATERIAL`** | **başkana taşındı** (bu ajan kapatmaz) |
| **C-251** *(YENİ)* | Yön. Geç. m.6 (T1, 2003-06-06): ölçü 600.000'de biter, 2007'den itibaren "bu ölçü" devam eder | 4250 m.1/3 (T1, 2001-01-20): asıl hüküm 1.000.000 demeye devam eder | Geçici hükümdeki *"bu ölçü"*nün göndergesi belirsiz. T1↔T1, tier/tarih/kapsam/katman kurallarının hiçbiri uygulanamıyor | **OPEN** — impact **LOW**, model etkisi **YOK** |
| **C-252** *(YENİ, C-201'in kalanı)* | 4250 m.1 son fıkra, **Okuma A** (T1, 2001-01-20): muafiyet ürüne bağlıdır, *her türlü şarabın* fiyatlandırılması/dağıtımı/satışı muaftır | Aynı fıkra, **Okuma B** (T1, 2001-01-20): muafiyet yalnızca yurt içinde üretilen şaraba ilişkindir | Aynı cümlenin iki lafzî okuması. TUR 1 raporum yalnızca B'yi görmüştü | **OPEN** — impact **LOW**, model etkisi **YOK** |

Detaylı kayıtlar: `99-ops/_parts/celiskiler-mevzuat-ruhsat-uzmani-tur15.md`.
`99-ops/celiskiler.md` ana dosyasına bu turda **DOKUNULMAMIŞTIR** (tur mandası).

> **C-252'nin G0'ı yeniden bloke etmesi için** şu **iki koşul birlikte** gerekir:
> (i) C-252'nin **B lehine** kapanması, **VE** (ii) "Tekel GM eliyle" işlev için
> bir halef merci belirlendiğinin tespiti. Tek başına hiçbiri bloke etmez.

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | tier | evidence_id |
|---|---|---|---|---|---|---|
| ruhsat.yaml | `esikler.hacim_esigi_turu` | FIYATLANDIRMA_SERBESTISI_KOSULU | — | ESTIMATE | T2 | EV-2026-08-10-216 |
| ruhsat.yaml | `esikler.kanun_metnindeki_olcu_litre_yil` | 1.000.000 | litre/yıl | FACT | T1 | EV-2026-08-10-201 |
| ruhsat.yaml | `esikler.uygulanan_olcu_litre_yil` | **600.000** | litre/yıl | FACT | T1 | EV-2026-08-10-204, -205 |
| ruhsat.yaml | `esikler.olcuyu_sifira_indiren_karar_var_mi` | null | — | **UNKNOWN** | T2 | EV-2026-08-10-214 |
| ruhsat.yaml | `esikler.ithalat_izni_esigi_mi` | false | — | FACT | T1 | EV-2026-08-10-207 |
| ruhsat.yaml | `esikler.dagitim_yetkisi_esigi_mi` | false | — | FACT | T1 | EV-2026-08-10-207 |
| ruhsat.yaml | `esikler.uretim_tesisi_kapasite_sarti_ithalatciya_uygulanir_mi` | false | — | FACT | T1 | EV-2026-08-10-201, -202 |
| ruhsat.yaml | `esikler.bedel_sinifi_esigi_litre_yil` | 20.000 | litre/yıl | FACT | T1 | EV-2026-08-09-206 |
| ruhsat.yaml | `esikler.senaryo_litre_yil` | [3750, 7500, 18750, 37500, 75000] | litre/yıl | ESTIMATE | T2 | EV-2026-08-10-215 |
| ruhsat.yaml | `esikler.senaryolarin_hicbiri_esigi_asiyor_mu` | false | — | ESTIMATE | T2 | EV-2026-08-10-215 |
| ruhsat.yaml | `esikler.esige_ulasmak_icin_gereken_sise_yil` | 800.001 / 1.333.334 | şişe/yıl | ESTIMATE | T2 | EV-2026-08-10-215 |
| ruhsat.yaml | `esikler.hacimden_bagimsiz_canli_yukumluluk` | ülke geneli yerinde teslim | — | FACT | T1 | EV-2026-08-10-201 |
| ruhsat.yaml | `esikler.artik_yaptirim_mekanizmasi` | uyarı → süre → belge iptali | — | FACT | T1 | EV-2026-08-10-210 |
| ruhsat.yaml | `esikler.4250_uygulama_mercii` | Tarım ve Orman Bakanlığı | — | FACT | T1 | EV-2026-08-10-208 |
| ruhsat.yaml | `g0_onerisi.value` | **G0_PASS** (koşulsuz — T-201 yönünden) | — | ESTIMATE | T2 | yukarıdaki set |
| ruhsat.yaml | `satis_dagitim_reklam_kisitlari.dagitim_yukumlulugu` | **DÜZELTİLDİ** (bkz. B-6) | — | FACT | T1 | EV-2026-08-10-201, -212 |

**Bu turda DEĞİŞTİRİLMEYEN girdiler:** belge bedelleri, bandrol, etiket, analiz,
teminat, T0 takvimi, toplam ruhsat maliyetleri. Tur dar kapsamlıydı.

---

## 6. ÇAPRAZ İPUÇLARI

Tam liste: `99-ops/_parts/capraz-ipuclari-mevzuat-ruhsat-uzmani-tur15.md`.

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `kanal-marj-uzmani` | **TUR 1 düzeltmesi:** Yön. m.9/2 "ülke genelinde yerinde teslim" **demiyor**; daha dar bir yükümlülük getiriyor | Ulusal kılcal dağıtım zorunluluğu varsayımı TUR 1'dekinden **daha zayıf** zeminde |
| `finans-fizibilite` | Hacim duyarlılığında **yanlış eşiğe optimize etme**: 600.000 L eşiği erişilemez; modellenecek tek gerçek eşik **20.000 L (26.667 şişe)** bedel kırılımıdır | Ölçek senaryolarının doğru kırılımı |
| `seytanin-avukati` | G0 PASS önerimin en saldırılabilir iki yeri: 4733 m.4/B(b) görev devri ve 4733 m.8 belge iptali yolu — **ikisini de kendim işaretledim** | Kırmızı takıma hazır malzeme |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | önceki | **yeni** |
|---|---|---|---|---|---|
| `T-201` | yatirim-komitesi-baskani | 1.000.000 L/yıl eşiği durgun şarap ithalatına uygulanıyor mu | **CRITICAL** | OPEN | **ANSWERED** |

**Yeni ticket AÇILMAMIŞTIR.** Kalan `UNKNOWN`'ların hiçbiri bir ticket'ı hak
edecek ölçüde modeli bloke etmemektedir; hepsi `OQ-251`…`OQ-254` olarak açık
soru kaydına bırakılmıştır
(`99-ops/_parts/acik-sorular-mevzuat-ruhsat-uzmani-tur15.md`).

`T-202` (HIGH, dağıtım yetki belgesi süresi/bedel yapısı) **OPEN kalmaya devam
eder** — bu turda ele alınmadı.

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| EV-2026-08-10-201 … -212 (T1 mevzuat hükümleri) | 180d | **2027-02-06** |
| EV-2026-08-10-213 (TADAB istatistik kapsamı) | 90d | 2026-11-08 |
| EV-2026-08-10-214 (negatif arama — BKK/CBK, halef merci) | 90d | 2026-11-08 |
| EV-2026-08-10-215 (senaryo aritmetiği) | 180d | 2027-02-06 |
| EV-2026-08-10-216 (hukuki türetme) | **90d** | **2026-11-08** — kısa TTL: türetme, mevzuat değişikliğine ve TADAB görüşüne duyarlıdır |

**Aralık: `EV-2026-08-10-201` → `EV-2026-08-10-216` (16 kanıt kartı).**
Bloğun kalanı (`-217` … `-249`) kullanılmamıştır.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**TADAB'ın veya bir yargı kararının, 4250 m.1/3'ün "Tekel Genel Müdürlüğü eliyle"
mekanizmasının bugün *bir halef merci üzerinden* uygulandığını teyit etmesi —
ve aynı anda m.1 son fıkrasındaki muafiyetin ithal durgun şarabı kapsamadığının
(C-252 / Okuma B) tespiti.**

Bu **iki koşul birlikte** gerçekleşirse, 3.750–75.000 litre/yıl ölçeğindeki bir
şarap ithalatçısı **fiyat belirlemekte serbest olmaz** ve projenin ters modeli
(`target shelf price → max EXW/FOB`) anlamsızlaşır. Öneri `G0 PASS` → `G0
BLOCKED`'a döner.

**Tek başına hiçbiri yetmez:**
- Yalnızca Okuma B doğrulanırsa → mekanizmanın uygulayıcısı hâlâ yok
  (`EV-...-214`, `EV-...-206`).
- Yalnızca halef merci bulunursa → şarap muafiyeti (Okuma A) hâlâ savunulabilir.

**İkinci sıradaki çürütücü:** 4733 m.8'in artık yaptırımının (belge iptali)
4250 m.1/3'e **fiilen uygulandığı** bir TADAB kararı örneği. Bu, "hüküm kâğıt
üzerinde kaldı" varsayımımı doğrudan yıkar. Aramadım (OQ-254).

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"Kanun koyucunun 4733 m.9/B ile devrettiği fiyatlandırma yetkisinin ilgili
Yönetmelikte kullanılmamış olması, mekanizmanın uygulanamaz olduğunu gösterir"
çıkarımı** (`EV-2026-08-10-216`).

Bu bir **çıkarımdır, hüküm değildir.** Karşı argüman güçlüdür: ikincil düzenleme
yapılmamış olması, **kanun hükmünü ortadan kaldırmaz** — Türk hukukunda kanun
hükmü doğrudan uygulanabilir olabilir ve yönetmelik boşluğu bir "yürürlükten
kalkma" değildir. Ben yalnızca *"idare bu yetkiyi 23 yıldır kullanmamıştır"*
gözlemini yapabiliyorum; *"dolayısıyla uygulanamaz"* demek bir yorumdur ve bu
raporda **FACT olarak yazılmamıştır** (status: ESTIMATE, tier: T2, confidence:
MEDIUM).

**İkinci en kırılgan:** m.1 son fıkrasının **Okuma A**'sı. Dilbilgisel olarak
savunulabilir ama **hiçbir resmî kaynakla desteklenmemiştir**; bunu ben
okudum. `C-252` açık bırakılmasının sebebi tam olarak budur.

### 9.3 Hangi kaynağıma en az güveniyorum?

Sıralı:

1. **`EV-2026-08-10-214` (negatif arama).** Bu turun en zayıf kartı. `mevzuat.gov.tr`
   ve `resmigazete.gov.tr` bu oturumda **hiç açılamadı** (TLS: `unable to get
   local issuer certificate`). Yani BKK/CBK araması ve halef merci araması
   **birincil kaynakta yapılamamıştır**; TADAB aynası + web araması ile
   sınırlıdır. Bu, bir "arama yapıldı" kaydıdır, bir "yoktur" kanıtı değildir —
   ve kartta bu açıkça yazılıdır.
2. **`EV-2026-08-10-216` (hukuki türetme).** §9.2'deki gerekçe.
3. **4250 ve 4733 konsolide metinleri (TADAB aynası).** Bunlar `tarimorman.gov.tr`
   üzerinden alınmış, mevzuat.gov.tr Düstur dizgisiyle birebir aynı görünen
   PDF'lerdir ve **TADAB'ın kendi yürürlükteki mevzuat sayfasında** yayımlanır —
   bu yüzden T1 saydım. **Ancak birincil `mevzuat.gov.tr` kopyasıyla çapraz
   doğrulama bu oturumda yapılamamıştır.**
   > Dürüstlük notu: elimdeki 4250 konsolide PDF'i, **7584 s.K.'nın m.6'ya
   > eklediği cümleyi içermiyor** — yani bu ayna metin **20/6/2026 değişikliği
   > yönünden güncel değildir.** Bu, kullandığım m.1 ve m.7 hükümlerini
   > etkilemez (onlar 2001/2020 tarihlidir), ama aynanın güncellenme gecikmesi
   > olduğunu gösterir ve kaydedilmelidir.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Yanlış çıkan bulgu | Değişen şey |
|---|---|
| Eşik gerçekten ithalatı/fiyatlandırmayı bağlıyor (C-252 B + halef merci) | `G0 PASS` → **`G0 BLOCKED`**. Ters model çöker. Başkan muhtemelen `HOLD`/`KILL`. |
| Uygulanan ölçü 600.000 değil 1.000.000 (**C-251**) | **Hiçbir şey.** Beş senaryo her iki ölçüde de altta. |
| Muafiyet Okuma B doğru ama mekanizmanın muhatabı yok | **Hiçbir şey** — teorik bir aykırılık, pratik sonucu yok. |
| Sıfıra indiren bir BKK/CBK bulunursa | **Hiçbir şey kötüleşmez** — tersine, kalan tüm belirsizlik kapanır. |
| 4733 m.8 belge iptalinin m.1/3'e uygulandığı örnek bulunursa | G0 önerisi `BLOCKED`'a döner; ayrıca **iş sürekliliği riski** (belge iptali) risk kaydına girer. |
| "Yerinde teslim" ölçütü ağır çıkarsa (OQ-253) | G0 değişmez; **kanal ve dağıtım maliyeti modeli** değişir → `kanal-marj-uzmani`. |

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| Ne | Kim | Nasıl | Süre | Maliyet |
|---|---|---|---|---|
| **C-252 + OQ-252 (tek soruda)** | Yatırımcı → TADAB Alkol ve Alkollü İçkiler Daire Başkanlığı | KEP ile yazılı görüş: *"Yıllık dış alım hacmi 20.000 litrenin altında olan bir şarap ithalatçısı, 4250 s.K. m.1/3 uyarınca ürünlerinin fiyatını serbestçe belirleyebilir mi? Belirleyemiyorsa fiyatlandırma/satış/dağıtım hangi merci eliyle yapılır?"* — **tek soru her iki UNKNOWN'ı da kapatır** | 2–6 hafta | ~0 |
| OQ-251 (sıfıra indiren BKK/CBK) | Bu ajan | Farklı ağdan `resmigazete.gov.tr` / `mevzuat.gov.tr` taraması | 1 gün | ~0 |
| OQ-254 (fiilî yaptırım örneği) | Bu ajan | TADAB "İdari Yaptırımlar ve Teminatlar" arşivi (yıl bazında 4250 İPC listeleri) | 1 gün | ~0 |
| Konsolide metin çapraz doğrulaması | Bu ajan | `mevzuat.gov.tr/MevzuatMetin/1.3.4250.pdf` ve `1.5.4733.pdf` ile TADAB aynasının karşılaştırılması | 1 gün | ~0 |
| **En hızlı ve en yüksek getirili doğrulama** | Yatırımcı | **Faal, küçük ölçekli bir şarap ithalatçısıyla 1 saatlik görüşme.** "Fiyatınızı kendiniz mi belirliyorsunuz?" sorusunun cevabı C-252, OQ-252 ve OQ-253'ü **birlikte** aydınlatır. Böyle bir firmanın varlığı bile eşik itirazını pratikte bitirir. | 1 hafta | ~0 |

---

## 10. T-201 / C-201 / G0 — ZORUNLU ÇIKTI

```yaml
T_201_yeni_status:  ANSWERED
C_201_durum:        "daraltildi; kapatma onerisi RESOLVED-NON_MATERIAL (karar baskanda)"
G0_onerisi:         G0 PASS
G0_kosullu_mu:      false   # YALNIZCA T-201/C-201 boyutu icin
```

**T-201 → `ANSWERED` (RESOLVED değil).** Gerekçe: ticket'ın `target_agent`'ı
başkandır; CLAUDE.md §5 akışı `OPEN → ANSWERED → RESOLVED/REJECTED`'dır ve
**kapanış yetkisi başkandadır.** Bu ajan cevabı üretmiş, kapanışı üretmemiştir.

**C-201 → çözülmedi, DARALTILDI.** Üç ayağından ikisi kanıtla düştü (B-1, B-4);
kalan ayak `C-252` olarak yeniden numaralandı ve impact'i **LOW / model etkisi
YOK**'a indi. **Kapatma önerim: `RESOLVED — NON_MATERIAL`.** Bu ajan
kapatmamıştır (CLAUDE.md §1.13).

**G0 → `G0 PASS`.** Gerekçe:

1. Başkanın G0'ı `BLOCKED` bırakma gerekçesi **tekti**: eşiğin senaryoları
   geçersiz kılma ihtimali. Bu ihtimal ortadan kalkmıştır — eşik ne ithalatı,
   ne dağıtım yetkisini, ne belge bedelini şarta bağlar; yalnızca fiyatlandırma
   serbestisi koşuludur ve beş senaryo eşiğin **8–160 katı** altındadır.
2. Yürürlükteki resmî tarife (Tebliğ 2025/39, yürürlük 1/1/2026) **≤20.000
   litre/yıl** faaliyet gösteren şarap ithalatçısı için ayrı ve **fiyatlanmış**
   bir sınıf öngörür — idare bu ölçeği **olağan bir muhatap** sayar.
3. `G0 FAIL` için dayanak yoktur; **kaldırılamaz bir engel** tespit edilmemiştir.

**Bu öneri şunları İDDİA ETMEZ:** "eşik hükmü ölüdür" (U-4 açıktır);
"4250'ye aykırılık yaptırımsızdır" (`EV-2026-08-10-210` kayıtlıdır).

**Başkana uyarı:** Bu öneri **yalnızca T-201/C-201 boyutundadır.**
`C-203` / `T-205` **CRITICAL ve OPEN** kalmaya devam etmektedir ve bu turda
mandası gereği **ele alınmamıştır**. Başkan C-203'ü G0 kapsamında sayarsa G0
**başka bir gerekçeyle** BLOCKED kalır — bu bir karar meselesidir ve bu ajanın
yetkisinde değildir.

**Bu bir KARAR DEĞİLDİR.** `KILL` · `HOLD` · `TEST` · `IMPORT PILOT` · `SCALE`
kararlarının hiçbiri bu raporda verilmemiştir. Nihai karar
`yatirim-komitesi-baskani`'na aittir.

---

## EK — ÜRETİLEN / DEĞİŞTİRİLEN DOSYALAR

**Yeni:**
- `20-mevzuat/1m-litre-esigi.md` *(ana çıktı — 6 sorunun her birine ayrı cevap)*
- `20-mevzuat/rapor-tur15-mevzuat-ruhsat.md` *(bu dosya)*
- `10-evidence/raw/EV-2026-08-10-201.md` … `EV-2026-08-10-216.md` (16 kart)
- `10-evidence/raw/snapshots/EV-2026-08-10-2xx_4733-sayili-kanun.pdf`
- `10-evidence/raw/snapshots/EV-2026-08-10-2xx_tadab-resmi-istatistik-2026-1c.pdf`
- `10-evidence/_index-parts/mevzuat-ruhsat-uzmani-tur15.csv` *(başlıksız, 16 satır)*
- `99-ops/_parts/celiskiler-mevzuat-ruhsat-uzmani-tur15.md`
- `99-ops/_parts/acik-sorular-mevzuat-ruhsat-uzmani-tur15.md`
- `99-ops/_parts/capraz-ipuclari-mevzuat-ruhsat-uzmani-tur15.md`

**Değiştirilen:**
- `80-model/inputs/ruhsat.yaml` — `esikler` bölümü eklendi; `g0_onerisi` ve
  `satis_dagitim_reklam_kisitlari.dagitim_yukumlulugu` güncellendi
- `99-ops/tickets/T-201.md` — `status: OPEN → ANSWERED`, CEVAP bölümü dolduruldu
  (**geçmiş içerik silinmedi**)
- `10-evidence/raw/EV-2026-08-09-227.md` — yalnızca `status: UNKNOWN → SUPERSEDED`
  (CLAUDE.md §4'ün tek istisnası) + açıklama notu

**DOKUNULMAYAN:** `10-evidence/index.csv`, `99-ops/celiskiler.md`,
`99-ops/capraz-ipuclari.md`, `99-ops/acik-sorular.md`, diğer ajanların dosyaları.

> **Başkan için konsolidasyon notu:** `EV-2026-08-09-227`'nin `status` alanı kart
> dosyasında `SUPERSEDED`, `index.csv`'de hâlâ `UNKNOWN`'dır. Bu fark bilinçlidir
> (index.csv'ye dokunulmaması talimatı) ve konsolidasyonda giderilmelidir.
