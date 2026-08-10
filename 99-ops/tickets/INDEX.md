# TICKET İNDEKSİ — TUR 3A SONU

> Otomatik üretildi (başkan tur sonu derlemesi, 2026-08-10).
> Kaynak: `99-ops/tickets/T-*.md` — dosya sistemi tam sayımı.

**Toplam: 125 ticket** — impact: CRITICAL 14, HIGH 71, MEDIUM 38, LOW 1, CONSTRAINT 1

**status:** ANSWERED 14, OPEN 105, RESOLVED 6

**Açık CRITICAL: 11**

| ticket | status | hedef | konu |
|---|---|---|---|
| `T-104` | ANSWERED | `finans-fizibilite` | Şarapta ÖTV maktu tutarı Ocak ve Temmuz aylarında Yİ-ÜFE ile kend |
| `T-301` | OPEN | `mevzuat-ruhsat-uzmani` | "Ruhsat / uygunluk / analiz / bandrol nedeniyle malin gumrukte +  |
| `T-304` | OPEN | `yatirim-komitesi-baskani` | "Hicbir rotamiz icin dogrulanmis navlun YOKTUR. Model tek bir nav |
| `T-466` | OPEN | `finans-fizibilite` | "TUR 2'de bulunan TEK yayinlanmis sise fiyati (2.85+/sise) PARA B |
| `T-601` | OPEN | `mevzuat-ruhsat-uzmani` | "Siselenmis sarap, 6585 s. Perakende Ticaretin Duzenlenmesi Hakki |
| `T-619` | ANSWERED | `finans-fizibilite` | "T-942'nin onerdigi R8-K assertion'i, BIREBIR KODLANIRSA TERSTEN  |
| `T-851` | OPEN | `yatirim-komitesi-baskani` | "TARGET BUY PRICE / ACCEPTABLE BUY PRICE / WALK-AWAY PRICE URETIL |
| `T-852` | OPEN | `yatirim-komitesi-baskani` | "makro.yaml -> fx UC TURDUR `null`'dir ve bu ajan onu DOLDURAMAZ: |
| `T-912` | OPEN | `finans-fizibilite` | "makro.yaml -> fx (usd_try, eur_try, eur_usd) NULL'dur. Kur TARIH |
| `T-942` | ANSWERED | `finans-fizibilite` | "Ters modelin KANAL BACAGI (R1-R5) icin HICBIR OTOMATIK DOGRULAMA |
| `T-947` | ANSWERED | `gumruk-vergi-uzmani` | "KDVK md.36 uyarinca cikarilmis ve ALKOLLU ICKIDE ITHALAT KDV'SIN |

> **CLAUDE.md §5:** Kritik açık ticket varken finans modeli `APPROVED` olamaz.

## TÜM TICKET'LAR

| ticket_id | açan | hedef | impact | status | claim |
|---|---|---|---|---|---|
| `T-104` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **CRITICAL** | ANSWERED | Şarapta ÖTV maktu tutarı Ocak ve Temmuz aylarında Yİ-ÜFE ile kendiliğinden artar (son artı |
| `T-201` | `mevzuat-ruhsat-uzmani` | `yatirim-komitesi-baskani` | **CRITICAL** | RESOLVED | 4250 s.K. m.1/3'teki "1.000.000 litre/yıl dış alım" eşiği ve "ülke genelinde her satıcıya  |
| `T-301` | `navlun-lojistik-uzmani` | `mevzuat-ruhsat-uzmani` | **CRITICAL** | OPEN | "Ruhsat / uygunluk / analiz / bandrol nedeniyle malin gumrukte + antrepoda bekleyecegi sur |
| `T-304` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | **CRITICAL** | OPEN | "Hicbir rotamiz icin dogrulanmis navlun YOKTUR. Model tek bir navlun rakamina kilitlenemez |
| `T-466` | `global-sourcing-kasifi` | `finans-fizibilite` | **CRITICAL** | OPEN | "TUR 2'de bulunan TEK yayinlanmis sise fiyati (2.85+/sise) PARA BIRIMI BILINMEDIGI ve KATM |
| `T-601` | `kanal-marj-uzmani` | `mevzuat-ruhsat-uzmani` | **CRITICAL** | OPEN | "Siselenmis sarap, 6585 s. Perakende Ticaretin Duzenlenmesi Hakkinda Kanun m.7/3 anlaminda |
| `T-619` | `kanal-marj-uzmani` | `finans-fizibilite` | **CRITICAL** | ANSWERED | "T-942'nin onerdigi R8-K assertion'i, BIREBIR KODLANIRSA TERSTEN CALISIR. Onerilen 'adim K |
| `T-751` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **CRITICAL** | RESOLVED | "Ters (reverse) modelin vergi bacagi SPESIFIKASYONA baglanmistir. Maktu OTV ile oransal gu |
| `T-851` | `finans-fizibilite` | `yatirim-komitesi-baskani` | **CRITICAL** | OPEN | "TARGET BUY PRICE / ACCEPTABLE BUY PRICE / WALK-AWAY PRICE URETILEMEZ. Yatirimci minimum k |
| `T-852` | `finans-fizibilite` | `yatirim-komitesi-baskani` | **CRITICAL** | OPEN | "makro.yaml -> fx UC TURDUR `null`'dir ve bu ajan onu DOLDURAMAZ: finans-fizibilite'nin ar |
| `T-912` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **CRITICAL** | OPEN | "makro.yaml -> fx (usd_try, eur_try, eur_usd) NULL'dur. Kur TARIHLI ve KANITLI doldurulmad |
| `T-921` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **CRITICAL** | RESOLVED | "Engine (80-model/engine/) otv_maktu_zaman_serisi blogunu HIC OKUMAMAKTADIR ve model_hedef |
| `T-942` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **CRITICAL** | ANSWERED | "Ters modelin KANAL BACAGI (R1-R5) icin HICBIR OTOMATIK DOGRULAMA YOKTUR. R8 round-trip ya |
| `T-947` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **CRITICAL** | ANSWERED | "KDVK md.36 uyarinca cikarilmis ve ALKOLLU ICKIDE ITHALAT KDV'SININ INDIRIM HAKKINI KISITL |
| `T-101` | `gumruk-vergi-uzmani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | Gümrük antreposuna alınan bir konteyner şaraptan kısmi (parti parti) serbest dolaşıma giri |
| `T-102` | `gumruk-vergi-uzmani` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | 31.12.2025 tarihli "Tütün, Tütün Mamulleri, Alkol ve Alkollü İçkilerin İthalat Denetimi Te |
| `T-103` | `gumruk-vergi-uzmani` | `global-sourcing-kasifi` | **HIGH** | OPEN | Kapsamdaki 9 tedarik ülkesinin hiçbiri şarapta %0 gümrük vergili değil; Bosna-Hersek ve Ko |
| `T-152` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "KDVK md.39/1'e gore KANUNI vergilendirme donemi UCER AYLIKTIR; birer aylik donem ancak Ba |
| `T-161` | `gumruk-vergi-uzmani` | `global-sourcing-kasifi` | **HIGH** | OPEN | AB ve Şili menşeli şarapta %50 gümrük vergisi KOŞULLUDUR. Koşul tedarikçiye bağlıdır: teda |
| `T-163` | `gumruk-vergi-uzmani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | BİLGE sistemi tercihli tarifede menşe ülke kontrolünün YANI SIRA ÇIKIŞ ÜLKESİ kontrolü yap |
| `T-171` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **HIGH** | ANSWERED | "T-947 KAPANDI ve sonuc (A) KDV INDIRIMI CONFIRMED'dir: MAX_CIF_TRY DEGISMEZ, yeniden hesa |
| `T-202` | `mevzuat-ruhsat-uzmani` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | Dağıtım yetki belgesi başvurusunun sonuçlanma süresi mevzuatta TANIMSIZDIR; ayrıca belge b |
| `T-204` | `mevzuat-ruhsat-uzmani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | İthal alkollü içkide bandrol ZORUNLU olarak ANTREPODA şişe başına uygulanır; bu operasyonu |
| `T-302` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | **HIGH** | OPEN | "RFQ'ya 'case & pallet spec sheet' zorunlu maddesi eklenmelidir; sise formu/olcusu ve koli |
| `T-311` | `navlun-lojistik-uzmani` | `finans-fizibilite` | **HIGH** | OPEN | "Lojistik maliyeti UC PARA BIRIMINDEDIR (USD okyanus + EUR mense local charge + TRY Turkiy |
| `T-312` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | **HIGH** | OPEN | "Italya rotasi lojistik olarak TAMAMEN UNKNOWN'dir (LCL de FCL de). Ayrica Ispanya disinda |
| `T-314` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "Antrepo ici operasyon (elleclleme, yeniden paletleme, bandrolleme) ve cam kirilma orani i |
| `T-401` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **HIGH** | ANSWERED | "Aday mense ulkeleri icin GTIP 2204.21'de Turkiye ile tercihli tarife rejimi var mi ve han |
| `T-402` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "20'DV / 40'HC konteynere kac sise 750 ml sarap yuklenir ve aday yukleme limanlarindan Tur |
| `T-403` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | "Turkce arka etiket menside (uretici tesisinde) uygulanabilir mi, yoksa Turkiye'de mi uygu |
| `T-404` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "Tedarikciye pesin odeme ile vadeli odeme arasindaki secim, ithalatta KKDF veya baska bir  |
| `T-461` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "Bir uretici 20ft konteynere PALETSIZ (slipsheet) 14.112 sise girdigini ilan ediyor; PALET |
| `T-462` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **HIGH** | ANSWERED | "TUR 2 havuzuna giren YENI menseler (Moldova, Romanya, Bulgaristan ayni grup icinde; Yeni  |
| `T-464` | `global-sourcing-kasifi` | `turkiye-pazar-kasifi` | **HIGH** | ANSWERED | "TUR 2'de bulunan 7 somut MODEL A markasinin Turkiye'de halihazirda ithalatcisi/distributo |
| `T-467` | `global-sourcing-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "G2 gate'i 'gercek RFQ cevabi (>=5 tedarikci)' ile aciliyor; RFQ gonderimi ise DIS ILETISI |
| `T-501` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | "Fiyat Etiketi Yonetmeligi (RG 28.06.2014/29044) uyarinca perakende satisa arz edilen mali |
| `T-504` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "OQ-001'in promosyon ayagi (Soru 5/6) kapatilamadi. Ayni SKU icin ikinci bir Metro magaza  |
| `T-505` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | "TADAB'in yayinladigi 'ithalat/dagitim uygunluk belgesi' sahipleri listesi veya alkollu ic |
| `T-506` | `turkiye-pazar-kasifi` | `kanal-marj-uzmani` | **HIGH** | ANSWERED | "Metro magaza (cash&carry) fiyati ile Metro sevkiyat/HoReCa teslimat fiyati FARKLIDIR (Met |
| `T-551` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | RESOLVED | "TUR 1'de 'Metro etiketinde KDV haric/dahil CIFTLI gosterim YOKTUR' sonucuna varildi (EV-2 |
| `T-563` | `turkiye-pazar-kasifi` | `kanal-marj-uzmani` | **HIGH** | OPEN | Turkiye ithal sarap dagitiminda 4 ithalatci grubu ISMEN tespit edildi ve bunlardan biri (K |
| `T-602` | `kanal-marj-uzmani` | `finans-fizibilite` | **HIGH** | OPEN | "kanal.yaml'daki marj, vade, geri akan bedel ve listeleme bedeli alanlari TEK SAYI DEGIL S |
| `T-603` | `kanal-marj-uzmani` | `turkiye-pazar-kasifi` | **HIGH** | OPEN | "L8_CHAIN_RETAIL UNKNOWN oldugu surece L7 ve L6 SAYISAL OLARAK KURULAMAZ. Kanal marj denkl |
| `T-604` | `kanal-marj-uzmani` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "Kanal ticari kosullarinin TUTARLARI Turkiye'de SISTEMATIK OLARAK TICARI SIRDIR ve masabas |
| `T-611` | `kanal-marj-uzmani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "Listeleme bedeli (f) ve ciro primi / geri akan bedeller (d) HIZMET FATURASI ile alinmakta |
| `T-612` | `kanal-marj-uzmani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "Ters modelin R1 adimi (L8_net = L8 / (1+v)) HoReCa satirlarinda da URUN KDV ORANI (%20, E |
| `T-613` | `kanal-marj-uzmani` | `finans-fizibilite` | **HIGH** | OPEN | "`d` (geri akan bedeller) modelde TEK BIR ORANSAL KATSAYI olarak, L6 matrahinda tasinmakta |
| `T-614` | `kanal-marj-uzmani` | `finans-fizibilite` | **HIGH** | OPEN | "IKI AYRI HATA. (a) MATRAH: kanal alacaginin tutari L6 DEGIL L6_gross = L6*(1+v)'dir — fat |
| `T-615` | `kanal-marj-uzmani` | `finans-fizibilite` | **HIGH** | OPEN | "Model, sabit maliyetleri (ruhsat 30,17 TL/sise @5.000, f, D_fix) ITHAL EDILEN sise adedin |
| `T-616` | `kanal-marj-uzmani` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "T-944'un sordugu 'mu'nun matrahi' sorusunun KANAL PRATIGINDEKI cevabi TEK DEGILDIR ve ola |
| `T-617` | `kanal-marj-uzmani` | `finans-fizibilite` | **HIGH** | OPEN | "reverse-price-model.md §7.1: 'bu grid, §9.2'deki ithalatci katki payi gridiyle SAYISAL OL |
| `T-701` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | Hedef raf fiyati merdiveni (599/699/799/899/999 TL) bir TUKETICI raf fiyatidir; ancak proj |
| `T-702` | `turkiye-pazar-kasifi` | `finans-fizibilite` | **HIGH** | OPEN | TARGET_SHELF_PRICE (599/699/799/899/999) ile OBSERVED_BENCHMARK (599,90 / 649,90) AYRI NES |
| `T-802` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "Projedeki TEK gercek navlun verisi (10 LCL kotasyon karti) 2026-08-16'da olur. 2026-08-17 |
| `T-854` | `finans-fizibilite` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "lojistik-senaryolari-tur25.md §4 tablolari 'ISPANYA -> ISTANBUL' basligini tasir. Ters mo |
| `T-856` | `finans-fizibilite` | `kanal-marj-uzmani` | **HIGH** | OPEN | "d (geri akan bedeller) bandi YALNIZCA zincir perakende icin tanimlidir. Tekel/bagimsiz ve |
| `T-857` | `finans-fizibilite` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "Ters model, merdivenin EKONOMIK OLARAK EN DAYANIKLI basamaginin 999 TL oldugunu gostermek |
| `T-858` | `finans-fizibilite` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | "IKI AYRI KONU. (a) toplam_ruhsat_sabit_maliyeti'nin 20.000 litre/yil kademesi (150.839 -> |
| `T-859` | `finans-fizibilite` | `turkiye-pazar-kasifi` | **HIGH** | OPEN | "Hedef raf fiyati merdiveninin HANGI L8 ALT KATMANI oldugu UNKNOWN'dir (T-701). Ters model |
| `T-861` | `finans-fizibilite` | `kanal-marj-uzmani` | **HIGH** | OPEN | "LEDGER_UNIQUENESS (K6) ISIM TABANLIDIR ve K6a tipi cift sayimi YAPISAL OLARAK GOREMEZ. Ay |
| `T-863` | `finans-fizibilite` | `kanal-marj-uzmani` | **HIGH** | OPEN | "kanal.yaml'daki f_listeleme_bedeli_sise_basi alani SISE BASI (TRY/sise) tanimlidir. Engin |
| `T-864` | `finans-fizibilite` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "GATE KURALININ KAPSAMI GENISLETILMELIDIR. CLAUDE.md §5 yalnizca 'impact: CRITICAL acik ti |
| `T-871` | `global-sourcing-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "RFQ pazarlik capasi olarak HANGI hedef raf fiyati basamagi ve HANGI kanal esas alinacak?  |
| `T-881` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | **HIGH** | OPEN | "RFQ v2.2'de M5 (etiket gereksinimleri) zorunlu alan haline getirildi ve ureticiye UC SOMU |
| `T-882` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "T-302'nin RFQ tarafi karsilandi: sise agirligi/formu (M2), koli konfigurasyonu (M3) ve pa |
| `T-883` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "RFQ v2.2'de M6 (mense ispat belgesi) zorunlu alan yapildi ve OD-1...OD-4 taahhut olarak 6 |
| `T-884` | `global-sourcing-kasifi` | `yatirim-komitesi-baskani` | **HIGH** | OPEN | "RFQ v2.2'nin cevapsizlik kurali bir TICARI ELEME kuralidir, teknik bir kural degil: M2/M3 |
| `T-901` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **HIGH** | ANSWERED | "C-101 baskan tarafindan 71,2692 TL/lt lehine cozulmustur; ancak cozumun dayandigi +%16,09 |
| `T-902` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | **HIGH** | ANSWERED | "tedarikci.yaml'da iki alanin 'L1' (FOB) katman etiketi KANITLANMAMIS ve kendi verisiyle C |
| `T-903` | `yatirim-komitesi-baskani` | `turkiye-pazar-kasifi` | **HIGH** | RESOLVED | "Raporunuzun §5 'Model Girdileri' tablosu 14 satirin tamamini 80-model/inputs/pazar.yaml d |
| `T-911` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "Ithalatta hangi KUR uygulanir — gumruk kuru mu serbest piyasa kuru mu? makro.yaml -> fx.g |
| `T-913` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "EV-2026-08-10-301...-311 (11 LCL kotasyon karti) ttl 6d'dir ve 2026-08-16'da STALE olur.  |
| `T-914` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "Sili menseli sarapta BARCELONA AKTARMASI, SIL rejiminin 'cikis ulkesi YALNIZCA SILI' kura |
| `T-915` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "Fransiz adaylarinin LIMANI ESLESMIYOR. Tek FR kotasyonu MARSILYA'dir; The Wine Factory Go |
| `T-916` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "Italya rotasi test edilen limanlarin TAMAMINDA TIRRENYA'dir ve hepsi UNKNOWN. A-oncelikli |
| `T-917` | `yatirim-komitesi-baskani` | `turkiye-pazar-kasifi` | **HIGH** | OPEN | "TEK FIZIKSEL GOZLEM PAKETI: bir magaza turu T-504 + T-603 + C-551 + C-501/OQ-502 + OQ-001 |
| `T-922` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **HIGH** | OPEN | "TARGET_SHELF_PRICE merdiveni (599/699/799/899/999 TL, KDV DAHIL) senaryolar.yaml'a INVEST |
| `T-923` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **HIGH** | OPEN | "KAYIT DUZELTMESI: Proje kayitlarinda tekrarlanan '11 LCL kotasyon karti (EV-2026-08-10-30 |
| `T-941` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **HIGH** | OPEN | "ters-model-vergi-bacagi.md §3'teki R5 adiminin basligi 'R5 — L6 -> L5_max' seklindedir ve |
| `T-943` | `yatirim-komitesi-baskani` | `kanal-marj-uzmani` | **HIGH** | OPEN | "Vergi bacagi icin 'ters modelde yapilmasi en muhtemel 5 hata' listesi (H1-H6) YAZILMIS ve |
| `T-944` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **HIGH** | OPEN | "Ithalatci katki payi (mu) modelde L6 CIROSU uzerinden alinmaktadir (ters_model.py:392: l5 |
| `T-946` | `yatirim-komitesi-baskani` | `seytanin-avukati` | **HIGH** | OPEN | "finans-fizibilite'nin TUR 2.5'te KENDI buldugu R5 duzeltmesi (L5_max = L7_eff - mu x L6)  |
| `T-951` | `yatirim-komitesi-baskani` | `kanal-marj-uzmani` | **HIGH** | OPEN | "d (geri akan bedeller) ve f (listeleme bedeli) MEKANIZMA olarak nasil akiyor: (a) L6 fatu |
| `T-953` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **HIGH** | OPEN | "D-02 (asgari katki payi) bugun yatirimciya soruluyor, ama sorunun BLOKE EDEN parcasi bir  |
| `T-954` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **HIGH** | OPEN | "TUR 3A'da 16 esikten 15,5'i ERTELENDI (CAN DECIDE LATER) cunku model onlari duyarlilik EK |
| `T-105` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | KKDF oranı (%6) ve tetikleyici ödeme şekilleri T1 ile doğrulandı; ancak KKDF MATRAHININ ta |
| `T-151` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | ANSWERED | "Ithalat KDV'sinin indirilebilirligi KDVK md.29/1-b, md.34/1 ve md.30 TAM METNI ile T1 sev |
| `T-153` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **MEDIUM** | OPEN | "80-model/engine/matrah_sirasi.py:217 meta.model_hedef_tarihi alanini SADECE 'is None' ile |
| `T-162` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | Menşe ispat belgelerinin iki usul detayı T1 ile doğrulanamadı: (a) fatura beyanının değer  |
| `T-172` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "2204.21 icin GOZETIM YOKTUR sonucu (EV-2026-08-10-860) RG 31/12/2025-33124 (4. mukerrer)  |
| `T-173` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "7846 sayili CB Kararinin lafzi 'GOZETIM UYGULAMASINA TABI TUTULAN MALLARA iliskin gumruk  |
| `T-203` | `mevzuat-ruhsat-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | ANSWERED | Bandrol bedeli (2,36073 TL/şişe, KDV hariç) ve TADAB hizmet bedeli (0,1587 TL/şişe) hangi  |
| `T-206` | `mevzuat-ruhsat-uzmani` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | Şişelenmiş ithal şarap için zorunlu laboratuvar analizi (parametreler, akredite lab şartı, |
| `T-303` | `navlun-lojistik-uzmani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Navlun ve sigortanin gumruk kiymetine hangi kurallarla girdigi tanimlanmalidir; ayrica In |
| `T-305` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | "Incoterm secimi (EXW/FOB vs CIF) lojistik kontrolunu ve sigorta teminatini belirler; CIF  |
| `T-313` | `navlun-lojistik-uzmani` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | "Terminal ardiye tarifeleri ve free time hala kesinlesmedi: Kumport (Ambarli) degerleri ar |
| `T-405` | `global-sourcing-kasifi` | `turkiye-pazar-kasifi` | **MEDIUM** | OPEN | "Benchmark markalari 'Gold Country' (California) ve 'Central Creek' (Avustralya) uretici m |
| `T-406` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Turkiye 2025'te dokme sarap (GTIP 2204.29) ithalatini pratikte hic yapmamis (628 litre).  |
| `T-463` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Dogrulanan TEK odeme sarti TAMAMEN SEVKIYAT ONCESI PESINDIR (%50 siparis + %50 siseleme s |
| `T-465` | `global-sourcing-kasifi` | `kanal-marj-uzmani` | **MEDIUM** | OPEN | "Model A adaylarinin munhasirlik icin yillik hacim taahhudu ve ithalatciya markup/yeniden  |
| `T-468` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | "Havuzdaki menseler UC AYRI hukuki gruba dagiliyor (AB / AB disi Avrupa / okyanus otesi) v |
| `T-502` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | "Turkiye'de alkollu ickinin tuketiciye internetten satisi yasaktir; bu nedenle zincir mark |
| `T-503` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | "Alkollu icki reklami/kampanya tanitimi yasagi nedeniyle Metro dahil hicbir perakendeci sa |
| `T-561` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | **MEDIUM** | OPEN | C-501 ("stokta olmayan listelemelerin fiyatlari gerceklik disi") stokta-olmayan havuzun TA |
| `T-562` | `turkiye-pazar-kasifi` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | TUR 1 kisa listesindeki 11 tedarikcinin ve 15 markanin HICBIRI Turkiye'de bulunamadi; priv |
| `T-564` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | Artik ISIMLERI BILINEN 4 ithalatci uzerinden TADAB dagitim/ithalat uygunluk belgesi sahipl |
| `T-565` | `turkiye-pazar-kasifi` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | "top-10-rfq-targets.md siradaki #2 hedefi Cantina Danese s.r.l. (SUP-452) KENDI MARKASIYLA |
| `T-605` | `kanal-marj-uzmani` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | "RFQ 5.6 (ureticiden pazarlama/listeleme katkisi) ile kanal tarafindaki LISTELEME BEDELI a |
| `T-618` | `kanal-marj-uzmani` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | "Ters model L5'ten TR-ICI LOJISTIK duser (EV-2026-08-10-329, 5.000 sisede 3,99 TL/sise). A |
| `T-853` | `finans-fizibilite` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Moldova (MD), vergi.yaml -> mense_tarife_eslemesi.ulkeler listesinde SATIR OLARAK YOKTUR. |
| `T-855` | `finans-fizibilite` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | "senaryolar.yaml -> hacim_senaryolari V10K (10.000 sise/yil) TANIMLIDIR ama lojistik-senar |
| `T-862` | `finans-fizibilite` | `seytanin-avukati` | **MEDIUM** | OPEN | "TUR 3A'da yazilan 30 testin 30'u GECMEKTEDIR, ama testlerin tamami TEK BIR AJANIN cebir a |
| `T-872` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "Mense ispat belgesi (EUR.1 / fatura beyani) DUZENLENEMEZ veya gumrukte REDDEDILIRSE tarif |
| `T-873` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | "Purcari Wineries Group (RFQ hedefi #10) AYNI GRUP icinde uc ayri mensede uretim yapiyor:  |
| `T-904` | `yatirim-komitesi-baskani` | `mevzuat-ruhsat-uzmani` | **MEDIUM** | OPEN | "Iki katman/etiket sorunu: (a) ruhsat.yaml'daki HICBIR maliyet kaleminde 'katman' alani yo |
| `T-905` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | "EV-2026-08-09-310 bir MEVZUAT kanitidir (Karayollari Trafik Yonetmeligi md.128, 44 ton),  |
| `T-906` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **MEDIUM** | ANSWERED | "Iki model girdisi hijyen sorunu: (a) vergi.yaml -> urun_parametreleri.sise_hacmi_litre =  |
| `T-918` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | "rapor-tur2-global-sourcing.md §4, C-401 / C-402 / C-403'u 'ACIK' olarak raporluyor; gerce |
| `T-924` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | **MEDIUM** | OPEN | "AYNI OLGU (750 ml = 0,75 litre) UC MODEL GIRDI DOSYASINDA UC FARKLI STATU ile durmaktadir |
| `T-925` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | **MEDIUM** | OPEN | "urun.yaml -> urun.hacim_ml = 750 alani status: ASSUMPTION'dir ama evidence_id NULL'dur. A |
| `T-945` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | **MEDIUM** | OPEN | "C-851 (L3 katman tanimi) baskan tarafindan RESOLVED — TANIM olarak cozulmustur. Cozumun b |
| `T-948` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **MEDIUM** | OPEN | "P-2 kapisi 'TARGET merdiveninin BES BASAMAGI x UC TARIH x DORT OTV NOKTASI AYRI AYRI cali |
| `T-952` | `yatirim-komitesi-baskani` | `finans-fizibilite` | **MEDIUM** | OPEN | "D-01 (brut marj) bugun yatirimciya UC AYRI SORU olarak soruluyor: (i) yuzde kac, (ii) han |
| `T-801` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | **LOW** | OPEN | "TUR 2'nin 6 gunluk LCL kanit seti 11 kart DEGIL, 10 karttir. EV-2026-08-10-304 (Italya) t |
| `T-205` | `mevzuat-ruhsat-uzmani` | `kanal-marj-uzmani` | **CONSTRAINT** | RESOLVED | 20/06/2026'da yürürlüğe giren 7584 s.K. m.2 ile alkollü içki marka/logo/ambalaj görselleri |
