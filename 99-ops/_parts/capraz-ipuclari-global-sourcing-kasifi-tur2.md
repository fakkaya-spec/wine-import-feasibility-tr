# ÇAPRAZ İPUÇLARI — global-sourcing-kasifi — TUR 2

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında gördüğüm ve başka
> ajanları ilgilendiren bulgular. Hiçbiri bu ajan tarafından çözülmemiştir.
> `99-ops/capraz-ipuclari.md` dosyasına **DOKUNULMAMIŞTIR** (başkan birleştirir).

---

## 1 → `gumruk-vergi-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-451 | TUR 2 havuzuna **üç yeni menşe grubu** girdi: **Moldova** (Purcari, ayrıca Romanya ve Bulgaristan tesisleri), **Yeni Zelanda** (Clark Estate — kapsam dışı ama kayıtta) ve tek bir grup içinde **üç ayrı hukuki menşe** (MD + RO + BG). "STA var mı / hangi ülke grubunda" sorusu bu üçü için de sorulmalıdır. **Oranı ve kapsamı bu ajan üretmez** (T-462). | Aynı gruptan alım yapılırken menşe değişimi belge tipini ve tercihi değiştirebilir |
| İP-452 | **Harland Wine Company ödeme şartını tamamen sevkiyat öncesi peşin olarak ilan ediyor** (%50 sipariş + %50 şişeleme sonrası, `EV-2026-08-10-452`). The Wine Factory de "ödeme sonrası üretim" diyor. Yani havuzda **vade veren tedarikçi henüz doğrulanmadı.** | KKDF'nin doğup doğmadığı ödeme şekline bağlıysa, "peşin" senaryosu havuzun **varsayılanı** olabilir — bu T-404'ün pratik önemini artırır (T-463) |
| İP-453 | Sektör kaynağı, sarap ticaretinde **"FOB" teriminin iki farklı anlamda** kullanıldığını doğruluyor: Incoterms FOB (liman, L1) ve ABD iç ticaretinde "ex-cellar" FOB (fiilen L0) — `EV-2026-08-10-468`. **Bir tedarikçi beyanında veya bir gümrük beyannamesinde "FOB" görüldüğünde hangi anlamda olduğu doğrulanmalıdır.** | Gümrük kıymeti hesabında yanlış katman kullanılırsa matrah baştan yanlış kurulur |
| İP-454 | Cantina Danese (IT) ve Interbrosa (ES) **ithalat lisansının alıcıda olduğunu** kendi sitelerinde ayrıca belirtiyor. İki farklı ülkede aynı beyan. | Menşe tarafında ihracat lisansı sorunu görünmüyor; yük tamamen Türkiye tarafında |

## 2 → `navlun-lojistik-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-455 | **İlk somut konteyner doluluk rakamı bulundu:** Harland Wine Company "In a full 20' container, there are 14,112 bottles on slipsheets" diyor (`EV-2026-08-10-452`). Bu **paletsiz (slipsheet)** yüklemedir. **Paletli yüklemede kaç şişe girdiği hâlâ UNKNOWN'dır** ve fark önemlidir. Doğrulama sizin alanınız (T-461). | T-402'nin ilk veri noktası; MOQ ↔ konteyner ilişkisini kurar |
| İP-456 | **MOQ konteyneri doldurmuyor.** Harland'da MOQ 6.000 şişe, konteyner 14.112 şişe — yani MOQ, konteynerin **%42'sidir**. Pilot hacimlerde (5.000–10.000 şişe) **LCL/groupage veya karışık konteyner** kaçınılmaz görünüyor. | Pilot senaryosunun navlun birim maliyeti FCL'den yapısal olarak farklı olacaktır |
| İP-457 | Havuzda **karayolu erişimli tek menşe Moldova**'dır (Purcari, `EV-2026-08-10-462`). Aynı grubun Romanya ve Bulgaristan tesisleri de karayolu erişimlidir. TUR 1'de işaretlenen "en ucuz olan aynı zamanda en yakın" sezgiye aykırı bulgusu **TUR 2'de bir tedarikçiyle somutlaştı.** | Pilot hacimde karayolu/groupage, deniz FCL'den daha uygun olabilir — doğrulama sizde |

## 3 → `mevzuat-ruhsat-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-458 | Havuzda **Yeni Zelanda üreticisi** (Clark Estate) yayınlanmış bir **ulusal satış lisans numarası** (NZ Off Licence 52/OFF/024/2021) taşıyor. Menşe ülke lisans belgesinin Türkiye tarafında bir karşılığı isteniyorsa, bu tür belgelerin varlığı RFQ 6.5'te sorulabilir. | "Sağlık / serbest satış sertifikası" sorusunun hangi belgeye karşılık geldiği menşeye göre değişiyor olabilir |
| İP-459 | Cantina Danese **kendi gümrük antreposunu** işlettiğini beyan ediyor (`EV-2026-08-10-453`). Eğer bandrol/ÜİS veya Türkçe etiketleme menşede yapılabiliyorsa, antrepo işleten tedarikçi bunu operasyonel olarak kaldırabilir. | T-403'ün cevabı "menşede uygulanabilir" ise, bu kabiliyet bir tedarikçi seçim kriterine dönüşür |

## 4 → `turkiye-pazar-kasifi`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-460 | **En kritik ipucu.** TUR 2'de 7 somut **Model A markası** bulundu ve hepsinin Türkiye'de temsilcisi olup olmadığı UNKNOWN: **Viña Albali / Los Molinos** (Félix Solís, ES), **Porta 6** (Vidigal, PT), **Colombelle** (Plaimont, FR), **Quinta da Espiga / Palha-Canas** (Casa Santos Lima, PT), **Particular** (San Valero, ES), **Bostavan / Purcari** (MD), **Parras** (PT). Bu markaların Türkiye rafında görülüp görülmediği **Model A'nın uygulanabilirliğini tek başına belirler** (T-464). | Model A adaylarının tamamı bu tek çapraz kontrole bağlı |
| İP-461 | O'Neill Vintners'ın ana tesisi **Parlier / Central Valley**'dedir ve Kaliforniya'nın hacim/deger üretimi orada yapılır (`EV-2026-08-10-463`). Bu, `C-403`'ün ("Sierra Foothills mı Central Valley mi") **Central Valley ayağını dolaylı olarak destekler** ama **çözmez.** | Benchmark ürünün menşe bölgesi tespiti sizin alanınızda; bu yalnızca bir yön işareti |
| İP-462 | Havuzdaki **26 tedarikçinin hiçbiri Türkiye'yi ihracat pazarları arasında listelemiyor.** TUR 1'de 11 tedarikçi için de aynıydı. Yani ülke düzeyinde 17,85 m litre giren bir pazara, üretici düzeyinde **tek bir görünür bağ** bulunamadı. | Türkiye'ye ithalat büyük olasılıkla **birkaç yoğunlaşmış ithalatçı** üzerinden yürüyor olabilir — pazar yapısı hipotezi |

## 5 → `kanal-marj-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-463 | **Bodegas San Valero (ES) hem kendi markasını hem perakendeci markasını üretiyor** (`EV-2026-08-10-461`) ve ABD'de sattığının %90'ı private label. Yani **aynı üretim tabanı** iki farklı kanal ekonomisini besliyor. Tek bir RFQ ile iki modelin **maliyet farkı** ölçülebilir. | İki modelin kanal marjı karşılaştırması, aynı maliyet tabanı üzerinde yapılırsa çok daha temiz olur |
| İP-464 | Félix Solís'in Viña Albali'yi kendi sitesinde **"gıda perakende kanalının en çok satan İspanyol şarap markası"** diye tanımlaması, bu markaların **chain retail için tasarlandığını** gösterir. Charter'ın 1. kanal önceliği ile örtüşür. | Model A'da hangi markanın hangi kanala kurgulandığı, listeleme müzakeresini değiştirir |
| İP-465 | Harland'ın fiyat kademesi (**entry / mid / premium**) bir üreticinin kendi segmentasyonudur. Bu üç kademe ile Türkiye raf fiyat bantları arasında bir eşleme kurulabilirse, ters modelin hedef EXW'si kademeye bağlanabilir. **Bu eşlemeyi bu ajan yapmaz.** | Ters modelin (hedef raf → max EXW) çıkışının hangi kademeye düştüğü stratejik bir sonuçtur |

## 6 → `finans-fizibilite`

| # | İpucu | Neden önemli |
|---|---|---|
| İP-466 | **`fiyat.exw_per_sise` ve `fiyat.fob_per_sise` HÂLÂ `null`/`UNKNOWN`'dır.** TUR 2'de bulunan tek yayınlanmış fiyat (`EV-2026-08-10-451`) **para birimi bilinmediği için** bu alanları dolduramaz ve `SENSITIVITY_BOUNDS_ONLY` çitinin dışına çıkamaz. Model bu turda da **fiyat çıktısı üretmemelidir.** | Kanıtsız sayı modele giremez (CLAUDE.md §1.6) |
| İP-467 | **Ödeme şartı bulgusu `peak_cash_requirement`'i doğrudan büyütür:** doğrulanan tek ödeme şartı **tamamen sevkiyat öncesi peşindir** (Harland). Yani mal Türkiye'ye varmadan **tam bedel ödenmiş** olur ve tedarikçi vadesi CCC'yi **kısaltmaz**. Bu, TUR 1'de `odeme.vade_gun: null` denilen alanın en muhtemel değerinin **0** olduğunu düşündüren ilk gözlemdir — **ama tek gözlemdir, girdi değildir.** | Nakit modelinin en kötü senaryo ucu |
| İP-468 | **MOQ ↔ pilot ilişkisi niteldi** (`EV-2026-08-10-471`): 5.000 şişelik pilot, MOQ'su bilinen 5 üreticinin **3'üyle** mümkün. Yani "pilot hacmi tedarikçi havuzunu daraltır → birim fiyat muhtemelen yükselir" ödünleşimi TUR 2'de **sayısallaştı: havuz ~%40 daralıyor.** | 5.000 vs 10.000 şişe senaryolarının fiyat farkı bu daralmadan gelir |

## 7 → `seytanin-avukati` (kendi işime karşı bıraktığım cephane)

| # | Cephane |
|---|---|
| İP-469 | **26 tedarikçinin 26'sından da fiyat alınmadı.** "Alternatif tedarikçi sayısı" hâlâ **0**'dır. Havuzu 11'den 26'ya çıkarmak **kanıt üretmedi, aday üretti.** Bu iki turdur aynı yerde duran bir kusurdur. |
| İP-470 | **A önceliğin 7'sinden 5'i Model B.** İki modeli eşit derinlikte araştırma hedefi TUR 2'de de tam tutturulamadı — Model A adayları bulundu ama hiçbiri ticari şart yayınlamadığı için `A`'ya çıkamadı. Yani öncelik sıralamam **modelin kalitesini değil, şeffaflığını** ödüllendiriyor. |
| İP-471 | **Tek yayınlanmış fiyatın para birimi bilinmiyor.** Bunu bir "bulgu" diye rapor ediyorum ama %50 ihtimalle yanlış bir büyüklük sınıfındayım. |
| İP-472 | **Interbrosa'nın sitesi erişilemedi** ve bu firma, `tedarikci.yaml`'daki "doğrulanmış en düşük MOQ" alanının **tek kaynağıdır.** TUR 1'in en çok atıfta bulunulan bulgusu bugün teyit edilemedi. |
| İP-473 | **Clark Estate'i (NZ) havuza aldım** ama ülke charter kapsamında değil. Bunu "MOQ referansı" diye meşrulaştırdım. Bu, hedefi tutturmak için havuzu şişirme eğiliminin bir örneği olabilir — denetlenmeli. |
| İP-474 | **Priority kriterlerimi ben yazdım ve ben uyguladım.** K1–K5'in hiçbirinin ağırlığı yok; bu "ağırlık vermemek için" değil, ağırlık verecek verim olmadığı için. Kriterleri kendi bulgularıma göre geriye dönük ayarlamış olabilirim. |
