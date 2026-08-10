# TICKET İNDEKSİ — TUR 2.5 PRE-FLIGHT SONRASI

> Güncellendi: **2026-08-10, TUR 2.5 pre-flight** (`yatirim-komitesi-baskani`).
> Kaynak: `99-ops/tickets/T-*.md`. Tek doğruluk kaynağı ticket dosyalarının kendisidir.
> Karar kayıtları: `90-karar/tur-2-konsolidasyon.md` → `90-karar/tur-25-preflight.md`

**Toplam: 76 ticket** — impact: CRITICAL 8, HIGH 40, MEDIUM 27, CONSTRAINT 1

**status:** ANSWERED 8, OPEN 64, RESOLVED 4

**Açık CRITICAL: 7** *(TUR 2 sonu 6 → `T-921` eklendi; hiçbiri kapatılmadı, hiçbirinin impact'i indirilmedi)*

| ticket | status | hedef | konu |
|---|---|---|---|
| `T-104` | ANSWERED | `finans-fizibilite` | ÖTV maktu tutarı Yİ-ÜFE ile 6 ayda bir kendiliğinden artar; modelde sabit sayı olamaz. **Veri yapısı ayağı kabul edildi. `model_hedef_tarihi` 2026-08-10'da girildi; engine + makro varsayım ayakları AÇIK → `T-921`** |
| `T-921` | OPEN | `finans-fizibilite` | **YENİ (TUR 2.5)** — Engine `otv_maktu_zaman_serisi`'ni **hiç okumuyor**; `model_hedef_tarihi` dolduğu için `matrah_sirasi.py:217`'deki **tek uyarı sustu**; ufuk denetimi yok. **Bu ticket kapanmadan hiçbir ÖTV sayısı üretilemez** |
| `T-301` | OPEN | `mevzuat-ruhsat-uzmani` | Ruhsat/analiz/bandrol nedeniyle gümrükte + antrepoda bekleme süresi. **TUR 2'de kapsamı genişledi: artık konteyner modu (LCL↔FCL) blokeri** |
| `T-304` | OPEN | `yatirim-komitesi-baskani` | Hiçbir rota için doğrulanmış navlun yok. **LCL ayağı `ANSWERED`; çekirdek (FCL) açık — `C-311`** |
| `T-466` | OPEN | `finans-fizibilite` | Tek yayınlanmış fiyat modele giremez; `exw`/`fob` `null` kalmalı. **İndirim YAPILMADI** |
| `T-601` | OPEN | `mevzuat-ruhsat-uzmani` | Şişelenmiş şarap 6585 m.7/3 anlamında "tarım ve gıda ürünü" mü? **`C-601`'in çekirdeği buna bağlı** |
| `T-912` | OPEN | `finans-fizibilite` | **YENİ** — `makro.yaml → fx` `null`; kur olmadan modelin **her parasal çıktısı** `UNKNOWN` döner. **Projedeki en ucuz CRITICAL bloker** |

> **CLAUDE.md §5:** Kritik açık ticket varken finans modeli `APPROVED` olamaz.
> **TUR 2.5 / TUR 3 çıktısı en fazla `DRAFT` olabilir.**
>
> **`T-921` özel bir statüdedir:** diğer altı CRITICAL çıktının **statüsünü**
> sınırlar (`DRAFT`); `T-921` ise **hesabın kendisini** yasaklar — engine seriyi
> okumadan basılan her ÖTV değeri **geçersizdir, `DRAFT` bile olamaz.**
> Bkz. `90-karar/tur-25-preflight.md` §4 kapı **P-1**.

---

## TUR 2.5 PRE-FLIGHT'TA AÇILAN TICKET'LAR (2026-08-10)

| ticket | hedef | impact | konu |
|---|---|---|---|
| `T-921` | `finans-fizibilite` | **CRITICAL** | Engine `otv_maktu_zaman_serisi`'ni okumuyor; `model_hedef_tarihi` dolunca `is None` uyarısı sustu; ufuk denetimi yok. **`T-104`'ün birinci ayağı + `T-153`'ü kapsar** |
| `T-922` | `finans-fizibilite` | HIGH | `TARGET_SHELF_PRICE` merdiveni (599/699/799/899/999 TL, KDV dahil) kaydedildi; ters model kuralları `L1`–`L7`; KDV hariç türetmesi; 5×3×4 çapraz çarpım |
| `T-923` | `navlun-lojistik-uzmani` | HIGH | **Kayıt düzeltmesi:** "11 LCL kartı" → **10**. `EV-2026-08-10-304` bir LCL kotasyonu değil, **negatif bulgu** kartıdır (`ttl: 14d`, `UNKNOWN`). Yenileme penceresi: **6 gün** |
| `T-924` | `navlun-lojistik-uzmani` | MEDIUM | `lojistik.yaml → urun_fizik.sise_hacmi_ml` = 750 **`FACT`** + `evidence_id` yok → §1.5/§1.6 ihlali (`vergi.yaml` bunu `T-906(a)` ile düzeltmişti). `dara_kg` bandı yapısal değil |
| `T-925` | `global-sourcing-kasifi` | MEDIUM | `urun.yaml → urun.hacim_ml` `evidence_id` eksik; kart mevcut (`EV-2026-08-10-116`) |

**TUR 2.5'te statüsü değişen ticket: 0.** Hiçbir CRITICAL kapatılmadı,
hiçbirinin impact'i indirilmedi.

---

## TUR 2 KONSOLİDASYONUNDA YAPILAN STATÜ DEĞİŞİKLİKLERİ (2026-08-10)

| ticket | önce | sonra | gerekçe |
|---|---|---|---|
| `T-464` | OPEN | **ANSWERED** | `turkiye-pazar-kasifi` cevapladı: 7 Model A markasının hiçbirinin TR ithalatçısı **bulunamadı**. `RESOLVED` değil — **`BULUNAMADI` ≠ `YOK`**; kapanış için `T-505` gerekir |
| `T-401` | OPEN | **ANSWERED** | `mense-tarife-eslemesi.md` 9 ülkeyi eşledi. `RESOLVED` değil — birincil kaynaklara **erişilemedi**; Şili satırının **belgesi T3** |
| `T-462` | OPEN | **ANSWERED** | Moldova T1 ile kapatıldı (%70; STA var, 2204.21'i kapsamıyor). `RESOLVED` değil — **Yeni Zelanda ayağı cevaplanmadı** |
| `T-506` | OPEN | **ANSWERED** | Ciro primi mekaniği alkolde **vardır**; Metro kampanya mekaniği ayrı şeydir. `RESOLVED` değil — **fark büyüklüğü hâlâ `UNKNOWN`** (`OQ-612`) |
| `T-104` · `T-301` · `T-304` · `T-466` · `T-601` | — | **statü DEĞİŞMEDİ** | Beşine de **başkan kaydı eklendi**; hiçbiri kapatılamadı, hiçbirinin impact'i düşürülmedi |

## TUR 2 KONSOLİDASYONUNDA AÇILAN YENİ TICKET'LAR

| ticket | hedef | impact | konu |
|---|---|---|---|
| `T-911` | `gumruk-vergi-uzmani` | HIGH | İthalatta hangi kur uygulanır — **gümrük kuru mu piyasa kuru mu**? `fx.gumruk_kuru_kullanilir_mi` `UNKNOWN` |
| `T-912` | `finans-fizibilite` | **CRITICAL** | `makro.yaml → fx` **`null`** — her parasal çıktı `UNKNOWN` döner |
| `T-913` | `navlun-lojistik-uzmani` | HIGH | 11 LCL kotasyon kartı **2026-08-16'da STALE** — projedeki tek gerçek navlun verisi |
| `T-914` | `gumruk-vergi-uzmani` | HIGH | **Şili × Barcelona aktarması**: `SIL` rejiminin "çıkış ülkesi yalnızca Şili" kuralı bozulur mu? Bozulursa **+24 TL/şişe** |
| `T-915` | `navlun-lojistik-uzmani` | HIGH | **Fransız adaylarının limanı eşleşmiyor** — tek kotasyon Marsilya, tedarikçiler Bordeaux/Gaskonya |
| `T-916` | `navlun-lojistik-uzmani` | HIGH | **İtalya'da yanlış kıyı** — test edilen 4 liman Tirren, A-öncelikli tedarikçi Veneto; DFDS Trieste hattı elde ama değerlendirilmemiş |
| `T-917` | `turkiye-pazar-kasifi` | HIGH | **TEK FİZİKSEL GÖZLEM PAKETİ** — bir mağaza turu `T-504`+`T-603`+`C-551`+`C-501`'i aynı anda kapatır. **P1–P10 protokolü** |
| `T-918` | `global-sourcing-kasifi` | MEDIUM | `C-401`/`C-402`/`C-403` statü kaydı düzeltmesi (rapor "AÇIK" diyor, gerçek: RESOLVED/RESOLVED/UNRESOLVABLE) |

## TÜM TICKET'LAR

| ticket_id | açan | hedef | impact | status | claim |
|---|---|---|---|---|---|
| `T-104` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **CRITICAL** | ANSWERED | Şarapta ÖTV maktu tutarı Ocak ve Temmuz aylarında Yİ-ÜFE ile kendiliğinden artar (son artış +%1 |
| `T-201` | `mevzuat-ruhsat-uzmani` | `yatirim-komitesi-baskani` | **CRITICAL** | RESOLVED | 4250 s.K. m.1/3'teki "1.000.000 litre/yıl dış alım" eşiği ve "ülke genelinde her satıcıya yerin |
| `T-301` | `navlun-lojistik-uzmani` | `mevzuat-ruhsat-uzmani` | **CRITICAL** | OPEN | "Ruhsat / uygunluk / analiz / bandrol nedeniyle malin gumrukte + antrepoda bekleyecegi sure kac |
| `T-304` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | **CRITICAL** | OPEN | "Hicbir rotamiz icin dogrulanmis navlun YOKTUR. Model tek bir navlun rakamina kilitlenemez; TUR |
| `T-466` | `global-sourcing-kasifi` | `finans-fizibilite` | **CRITICAL** | OPEN | "TUR 2'de bulunan TEK yayinlanmis sise fiyati (2.85+/sise) PARA BIRIMI BILINMEDIGI ve KATMANI B |
| `T-601` | `kanal-marj-uzmani` | `mevzuat-ruhsat-uzmani` | **CRITICAL** | OPEN | "Siselenmis sarap, 6585 s. Perakende Ticaretin Duzenlenmesi Hakkinda Kanun m.7/3 anlaminda 'tar |
| `T-101` | `gumruk-vergi-uzmani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | Gümrük antreposuna alınan bir konteyner şaraptan kısmi (parti parti) serbest dolaşıma giriş yap |
| `T-102` | `gumruk-vergi-uzmani` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | 31.12.2025 tarihli "Tütün, Tütün Mamulleri, Alkol ve Alkollü İçkilerin İthalat Denetimi Tebliği |
| `T-103` | `gumruk-vergi-uzmani` | `global-sourcing-kasifi` | **HIGH** | OPEN | Kapsamdaki 9 tedarik ülkesinin hiçbiri şarapta %0 gümrük vergili değil; Bosna-Hersek ve Kosova  |
| `T-152` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "KDVK md.39/1'e gore KANUNI vergilendirme donemi UCER AYLIKTIR; birer aylik donem ancak Bakanli |
| `T-161` | `gumruk-vergi-uzmani` | `global-sourcing-kasifi` | **HIGH** | OPEN | AB ve Şili menşeli şarapta %50 gümrük vergisi KOŞULLUDUR. Koşul tedarikçiye bağlıdır: tedarikçi |
| `T-163` | `gumruk-vergi-uzmani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | BİLGE sistemi tercihli tarifede menşe ülke kontrolünün YANI SIRA ÇIKIŞ ÜLKESİ kontrolü yapar. Ş |
| `T-202` | `mevzuat-ruhsat-uzmani` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | Dağıtım yetki belgesi başvurusunun sonuçlanma süresi mevzuatta TANIMSIZDIR; ayrıca belge bedeli |
| `T-204` | `mevzuat-ruhsat-uzmani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | İthal alkollü içkide bandrol ZORUNLU olarak ANTREPODA şişe başına uygulanır; bu operasyonun ant |
| `T-302` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | **HIGH** | OPEN | "RFQ'ya 'case & pallet spec sheet' zorunlu maddesi eklenmelidir; sise formu/olcusu ve koli geom |
| `T-311` | `navlun-lojistik-uzmani` | `finans-fizibilite` | **HIGH** | OPEN | "Lojistik maliyeti UC PARA BIRIMINDEDIR (USD okyanus + EUR mense local charge + TRY Turkiye ope |
| `T-312` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | **HIGH** | OPEN | "Italya rotasi lojistik olarak TAMAMEN UNKNOWN'dir (LCL de FCL de). Ayrica Ispanya disindaki hi |
| `T-314` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "Antrepo ici operasyon (elleclleme, yeniden paletleme, bandrolleme) ve cam kirilma orani iki tu |
| `T-401` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **HIGH** | ANSWERED | "Aday mense ulkeleri icin GTIP 2204.21'de Turkiye ile tercihli tarife rejimi var mi ve hangi me |
| `T-402` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "20'DV / 40'HC konteynere kac sise 750 ml sarap yuklenir ve aday yukleme limanlarindan Turkiye' |
| `T-403` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | "Turkce arka etiket menside (uretici tesisinde) uygulanabilir mi, yoksa Turkiye'de mi uygulanma |
| `T-404` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "Tedarikciye pesin odeme ile vadeli odeme arasindaki secim, ithalatta KKDF veya baska bir vergi |
| `T-461` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "Bir uretici 20ft konteynere PALETSIZ (slipsheet) 14.112 sise girdigini ilan ediyor; PALETLI yu |
| `T-462` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **HIGH** | ANSWERED | "TUR 2 havuzuna giren YENI menseler (Moldova, Romanya, Bulgaristan ayni grup icinde; Yeni Zelan |
| `T-464` | `global-sourcing-kasifi` | `turkiye-pazar-kasifi` | **HIGH** | ANSWERED | "TUR 2'de bulunan 7 somut MODEL A markasinin Turkiye'de halihazirda ithalatcisi/distributoru VA |
| `T-467` | `global-sourcing-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "G2 gate'i 'gercek RFQ cevabi (>=5 tedarikci)' ile aciliyor; RFQ gonderimi ise DIS ILETISIM ger |
| `T-501` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | "Fiyat Etiketi Yonetmeligi (RG 28.06.2014/29044) uyarinca perakende satisa arz edilen malin eti |
| `T-504` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "OQ-001'in promosyon ayagi (Soru 5/6) kapatilamadi. Ayni SKU icin ikinci bir Metro magaza gozle |
| `T-505` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | "TADAB'in yayinladigi 'ithalat/dagitim uygunluk belgesi' sahipleri listesi veya alkollu icki pi |
| `T-506` | `turkiye-pazar-kasifi` | `kanal-marj-uzmani` | **HIGH** | ANSWERED | "Metro magaza (cash&carry) fiyati ile Metro sevkiyat/HoReCa teslimat fiyati FARKLIDIR (Metro'nu |
| `T-551` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | RESOLVED | "TUR 1'de 'Metro etiketinde KDV haric/dahil CIFTLI gosterim YOKTUR' sonucuna varildi (EV-2026-0 |
| `T-563` | `turkiye-pazar-kasifi` | `kanal-marj-uzmani` | **HIGH** | OPEN | Turkiye ithal sarap dagitiminda 4 ithalatci grubu ISMEN tespit edildi ve bunlardan biri (Kavakl |
| `T-602` | `kanal-marj-uzmani` | `finans-fizibilite` | **HIGH** | OPEN | "kanal.yaml'daki marj, vade, geri akan bedel ve listeleme bedeli alanlari TEK SAYI DEGIL SENARY |
| `T-603` | `kanal-marj-uzmani` | `turkiye-pazar-kasifi` | **HIGH** | OPEN | "L8_CHAIN_RETAIL UNKNOWN oldugu surece L7 ve L6 SAYISAL OLARAK KURULAMAZ. Kanal marj denklemi h |
| `T-604` | `kanal-marj-uzmani` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "Kanal ticari kosullarinin TUTARLARI Turkiye'de SISTEMATIK OLARAK TICARI SIRDIR ve masabasi ara |
| `T-901` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **HIGH** | ANSWERED | "C-101 baskan tarafindan 71,2692 TL/lt lehine cozulmustur; ancak cozumun dayandigi +%16,09'luk  |
| `T-902` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | **HIGH** | ANSWERED | "tedarikci.yaml'da iki alanin 'L1' (FOB) katman etiketi KANITLANMAMIS ve kendi verisiyle CELISK |
| `T-903` | `yatirim-komitesi-baskani` | `turkiye-pazar-kasifi` | **HIGH** | RESOLVED | "Raporunuzun §5 'Model Girdileri' tablosu 14 satirin tamamini 80-model/inputs/pazar.yaml dosyas |
| `T-105` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | KKDF oranı (%6) ve tetikleyici ödeme şekilleri T1 ile doğrulandı; ancak KKDF MATRAHININ tanımı  |
| `T-151` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Ithalat KDV'sinin indirilebilirligi KDVK md.29/1-b, md.34/1 ve md.30 TAM METNI ile T1 seviyesi |
| `T-153` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **MEDIUM** | OPEN | "80-model/engine/matrah_sirasi.py:217 meta.model_hedef_tarihi alanini SADECE 'is None' ile dene |
| `T-162` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | Menşe ispat belgelerinin iki usul detayı T1 ile doğrulanamadı: (a) fatura beyanının değer eşiği |
| `T-203` | `mevzuat-ruhsat-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | Bandrol bedeli (2,36073 TL/şişe, KDV hariç) ve TADAB hizmet bedeli (0,1587 TL/şişe) hangi vergi |
| `T-206` | `mevzuat-ruhsat-uzmani` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | Şişelenmiş ithal şarap için zorunlu laboratuvar analizi (parametreler, akredite lab şartı, part |
| `T-303` | `navlun-lojistik-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Navlun ve sigortanin gumruk kiymetine hangi kurallarla girdigi tanimlanmalidir; ayrica Incoter |
| `T-305` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | "Incoterm secimi (EXW/FOB vs CIF) lojistik kontrolunu ve sigorta teminatini belirler; CIF alimd |
| `T-313` | `navlun-lojistik-uzmani` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | "Terminal ardiye tarifeleri ve free time hala kesinlesmedi: Kumport (Ambarli) degerleri arama o |
| `T-405` | `global-sourcing-kasifi` | `turkiye-pazar-kasifi` | **MEDIUM** | OPEN | "Benchmark markalari 'Gold Country' (California) ve 'Central Creek' (Avustralya) uretici markas |
| `T-406` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Turkiye 2025'te dokme sarap (GTIP 2204.29) ithalatini pratikte hic yapmamis (628 litre). Bunun |
| `T-463` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Dogrulanan TEK odeme sarti TAMAMEN SEVKIYAT ONCESI PESINDIR (%50 siparis + %50 siseleme sonras |
| `T-465` | `global-sourcing-kasifi` | `kanal-marj-uzmani` | **MEDIUM** | OPEN | "Model A adaylarinin munhasirlik icin yillik hacim taahhudu ve ithalatciya markup/yeniden satis |
| `T-468` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | "Havuzdaki menseler UC AYRI hukuki gruba dagiliyor (AB / AB disi Avrupa / okyanus otesi) ve bir |
| `T-502` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | "Turkiye'de alkollu ickinin tuketiciye internetten satisi yasaktir; bu nedenle zincir market on |
| `T-503` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | "Alkollu icki reklami/kampanya tanitimi yasagi nedeniyle Metro dahil hicbir perakendeci sarap f |
| `T-561` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | **MEDIUM** | OPEN | C-501 ("stokta olmayan listelemelerin fiyatlari gerceklik disi") stokta-olmayan havuzun TAMAMIN |
| `T-562` | `turkiye-pazar-kasifi` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | TUR 1 kisa listesindeki 11 tedarikcinin ve 15 markanin HICBIRI Turkiye'de bulunamadi; private l |
| `T-564` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | Artik ISIMLERI BILINEN 4 ithalatci uzerinden TADAB dagitim/ithalat uygunluk belgesi sahipleri l |
| `T-565` | `turkiye-pazar-kasifi` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | "top-10-rfq-targets.md siradaki #2 hedefi Cantina Danese s.r.l. (SUP-452) KENDI MARKASIYLA Turk |
| `T-605` | `kanal-marj-uzmani` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | "RFQ 5.6 (ureticiden pazarlama/listeleme katkisi) ile kanal tarafindaki LISTELEME BEDELI ayni s |
| `T-904` | `yatirim-komitesi-baskani` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | "Iki katman/etiket sorunu: (a) ruhsat.yaml'daki HICBIR maliyet kaleminde 'katman' alani yoktur; |
| `T-905` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | "EV-2026-08-09-310 bir MEVZUAT kanitidir (Karayollari Trafik Yonetmeligi md.128, 44 ton), tier  |
| `T-906` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **MEDIUM** | ANSWERED | "Iki model girdisi hijyen sorunu: (a) vergi.yaml -> urun_parametreleri.sise_hacmi_litre = 0.75  |
| `T-205` | `mevzuat-ruhsat-uzmani` | `kanal-marj-uzmani` | **CONSTRAINT** | RESOLVED | 20/06/2026'da yürürlüğe giren 7584 s.K. m.2 ile alkollü içki marka/logo/ambalaj görsellerinin i |
| `T-911` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | Ithalatta hangi KUR uygulanir — gumruk kuru mu serbest piyasa kuru mu? makro.yaml -> fx.gumruk_kuru_kul |
| `T-912` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **CRITICAL** | OPEN | makro.yaml -> fx (usd_try, eur_try, eur_usd) NULL'dur. Kur TARIHLI ve KANITLI doldurulmadan modelin HER |
| `T-913` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | EV-2026-08-10-301...-311 (11 LCL kotasyon karti) ttl 6d'dir ve 2026-08-16'da STALE olur. Projedeki EN K |
| `T-914` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | Sili menseli sarapta BARCELONA AKTARMASI, SIL rejiminin 'cikis ulkesi YALNIZCA SILI' kuralini bozar mi |
| `T-915` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | Fransiz adaylarinin LIMANI ESLESMIYOR. Tek FR kotasyonu MARSILYA; tedarikciler Bordeaux/Gaskonya'da |
| `T-916` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | Italya rotasi test edilen limanlarin TAMAMINDA TIRRENYA'dir; A-oncelikli tedarikci VENETO'dadir. DFDS T |
| `T-917` | `yatirim-komitesi-baskani` | `turkiye-pazar-kasifi` | **HIGH** | OPEN | TEK FIZIKSEL GOZLEM PAKETI: bir magaza turu T-504 + T-603 + C-551 + C-501/OQ-502'yi AYNI ANDA kapatir |
| `T-918` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | rapor-tur2-global-sourcing.md §4, C-401/C-402/C-403'u 'ACIK' raporluyor; gercek: RESOLVED/RESOLVED/UNRE |
| `T-921` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **CRITICAL** | OPEN | Engine otv_maktu_zaman_serisi blogunu HIC OKUMUYOR; model_hedef_tarihi dolunca matrah_sirasi.py:217'deki tek uyari SUSTU; ufuk denetimi yok |
| `T-922` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **HIGH** | OPEN | TARGET_SHELF_PRICE merdiveni (599/699/799/899/999 TL, KDV dahil) kaydedildi; ters model kurallari L1-L7; TARGET != OBSERVED (K7) |
| `T-923` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | KAYIT DUZELTMESI: '11 LCL karti' YANLIS, dogru sayi 10. EV-2026-08-10-304 bir LCL kotasyonu degil, negatif bulgu karti (ttl 14d, UNKNOWN) |
| `T-924` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | lojistik.yaml urun_fizik.sise_hacmi_ml = 750 FACT + evidence_id YOK -> §1.5/§1.6 ihlali; vergi.yaml ayni olguyu T-906(a) ile ASSUMPTION'a duzeltmisti |
| `T-925` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | urun.yaml urun.hacim_ml = 750 ASSUMPTION ama evidence_id NULL; kart ZATEN VAR (EV-2026-08-10-116) |
