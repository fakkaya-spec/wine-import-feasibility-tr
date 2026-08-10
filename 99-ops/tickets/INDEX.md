# TICKET İNDEKSİ — TUR 2 PRE-FLIGHT SONU

> Otomatik üretildi (başkan kayıt bakımı, **2026-08-10**).
> Kaynak: `99-ops/tickets/T-*.md`. **Tek doğruluk kaynağı ticket dosyalarının kendisidir.**
> Önceki sürüm: TUR 1.5 SONU (2026-08-10) — 6 açık CRITICAL.

**Toplam: 38 ticket** — impact: CRITICAL 4, CONSTRAINT 1, HIGH 19, MEDIUM 14

**status dağılımı:** ANSWERED 3, OPEN 31, RESOLVED 4

**AÇIK CRITICAL TICKET: 3** — `T-104` (OPEN), `T-301` (OPEN), `T-304` (OPEN)

> **CLAUDE.md §5:** Kritik (`impact: CRITICAL`) açık ticket varken finans modeli
> `APPROVED` olamaz. **Bu kural yürürlüktedir** — açık CRITICAL sayısı 6'dan 3'e
> inmiştir, sıfıra inmemiştir.

### TUR 2 PRE-FLIGHT'ta ne değişti (2026-08-10)

| ticket | önce | sonra | ne oldu |
|---|---|---|---|
| `T-201` | CRITICAL / ANSWERED | CRITICAL / **RESOLVED** | Başkan kapanışı: `NON_MATERIAL_FOR_SCOPE`. 600.000 L/yıl ölçüsü beş senaryonun 8–160 katı üstünde; ithalat engeli **değil**. |
| `T-205` | CRITICAL / OPEN | **CONSTRAINT** / **RESOLVED** | Kurucu kararı: `ACCEPTED_BUSINESS_CONSTRAINT`. Kısıt yok sayılmadı — **veri** olarak `kanal-marj-uzmani`'na girdi yapıldı (İP-2001). |
| `T-504` | CRITICAL / OPEN | **HIGH** / OPEN + `NON_BLOCKING_TUR2` | **Kapatılmadı.** Fiziksel gözlem hâlâ gerekli. Impact düşürüldü çünkü benchmark artık modelde tek hedef fiyat olarak kullanılamaz (K5/K6). **G3'ü hâlâ bloke eder.** |
| `T-551` | HIGH / OPEN | HIGH / **RESOLVED** + `NON_BLOCKING_TUR2` | Başkan dört soruya da karar verdi (`DIRECTIVE_ISSUED`). Bağlı çelişki **`C-551` OPEN kalır**. |

> **`blocking_status: NON_BLOCKING_TUR2`** = "bu kayıt TUR 2'nin başlamasını
> durdurmaz". **Gate açtığı anlamına GELMEZ.**

| ticket_id | açan | hedef ajan | impact | status | claim |
|---|---|---|---|---|---|
| `T-104` | `gumruk-vergi-uzmani` | `finans-fizibilite` | **CRITICAL** | OPEN | Şarapta ÖTV maktu tutarı Ocak ve Temmuz aylarında Yİ-ÜFE ile kendiliğinden artar (son artış +%1… |
| `T-201` | `mevzuat-ruhsat-uzmani` | `yatirim-komitesi-baskani` | **CRITICAL** | **RESOLVED** | 4250 s.K. m.1/3'teki "1.000.000 litre/yıl dış alım" eşiği ve "ülke genelinde her satıcıya yerin… |
| `T-301` | `navlun-lojistik-uzmani` | `mevzuat-ruhsat-uzmani` | **CRITICAL** | OPEN | Ruhsat / uygunluk / analiz / bandrol nedeniyle malin gumrukte + antrepoda bekleyecegi sure kac … |
| `T-304` | `navlun-lojistik-uzmani` | `yatirim-komitesi-baskani` | **CRITICAL** | OPEN | Hicbir rotamiz icin dogrulanmis navlun YOKTUR. Model tek bir navlun rakamina kilitlenemez; TUR … |
| `T-205` | `mevzuat-ruhsat-uzmani` | `kanal-marj-uzmani` | **CONSTRAINT** | **RESOLVED** | 20/06/2026'da yürürlüğe giren 7584 s.K. m.2 ile alkollü içki marka/logo/ambalaj görsellerinin i… |
| `T-101` | `gumruk-vergi-uzmani` | `navlun-lojistik-uzmani` | HIGH | OPEN | Gümrük antreposuna alınan bir konteyner şaraptan kısmi (parti parti) serbest dolaşıma giriş yap… |
| `T-102` | `gumruk-vergi-uzmani` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | 31.12.2025 tarihli "Tütün, Tütün Mamulleri, Alkol ve Alkollü İçkilerin İthalat Denetimi Tebliği… |
| `T-103` | `gumruk-vergi-uzmani` | `global-sourcing-kasifi` | HIGH | OPEN | Kapsamdaki 9 tedarik ülkesinin hiçbiri şarapta %0 gümrük vergili değil; Bosna-Hersek ve Kosova … |
| `T-152` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | HIGH | OPEN | KDVK md.39/1'e gore KANUNI vergilendirme donemi UCER AYLIKTIR; birer aylik donem ancak Bakanlik… |
| `T-202` | `mevzuat-ruhsat-uzmani` | `yatirim-komitesi-baskani` | HIGH | OPEN | Dağıtım yetki belgesi başvurusunun sonuçlanma süresi mevzuatta TANIMSIZDIR; ayrıca belge bedeli… |
| `T-204` | `mevzuat-ruhsat-uzmani` | `navlun-lojistik-uzmani` | HIGH | OPEN | İthal alkollü içkide bandrol ZORUNLU olarak ANTREPODA şişe başına uygulanır; bu operasyonun ant… |
| `T-302` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | HIGH | OPEN | RFQ'ya 'case & pallet spec sheet' zorunlu maddesi eklenmelidir; sise formu/olcusu ve koli geome… |
| `T-401` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | HIGH | OPEN | Aday mense ulkeleri icin GTIP 2204.21'de Turkiye ile tercihli tarife rejimi var mi ve hangi men… |
| `T-402` | `global-sourcing-kasifi` | `navlun-lojistik-uzmani` | HIGH | OPEN | 20'DV / 40'HC konteynere kac sise 750 ml sarap yuklenir ve aday yukleme limanlarindan Turkiye'y… |
| `T-403` | `global-sourcing-kasifi` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | Turkce arka etiket menside (uretici tesisinde) uygulanabilir mi, yoksa Turkiye'de mi uygulanmak… |
| `T-404` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | HIGH | OPEN | Tedarikciye pesin odeme ile vadeli odeme arasindaki secim, ithalatta KKDF veya baska bir vergi/… |
| `T-501` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | Fiyat Etiketi Yonetmeligi (RG 28.06.2014/29044) uyarinca perakende satisa arz edilen malin etik… |
| `T-504` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | HIGH | OPEN ·<br>`NON_BLOCKING_TUR2` | OQ-001'in promosyon ayagi (Soru 5/6) kapatilamadi. Ayni SKU icin ikinci bir Metro magaza gozlem… |
| `T-505` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | HIGH | OPEN | TADAB'in yayinladigi 'ithalat/dagitim uygunluk belgesi' sahipleri listesi veya alkollu icki piy… |
| `T-506` | `turkiye-pazar-kasifi` | `kanal-marj-uzmani` | HIGH | OPEN | Metro magaza (cash&carry) fiyati ile Metro sevkiyat/HoReCa teslimat fiyati FARKLIDIR (Metro'nun… |
| `T-551` | `turkiye-pazar-kasifi` | `yatirim-komitesi-baskani` | HIGH | **RESOLVED** ·<br>`NON_BLOCKING_TUR2` | TUR 1'de 'Metro etiketinde KDV haric/dahil CIFTLI gosterim YOKTUR' sonucuna varildi (EV-2026-08… |
| `T-901` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | HIGH | ANSWERED | C-101 baskan tarafindan 71,2692 TL/lt lehine cozulmustur; ancak cozumun dayandigi +%16,09'luk Y… |
| `T-902` | `yatirim-komitesi-baskani` | `global-sourcing-kasifi` | HIGH | ANSWERED | tedarikci.yaml'da iki alanin 'L1' (FOB) katman etiketi KANITLANMAMIS ve kendi verisiyle CELISKI… |
| `T-903` | `yatirim-komitesi-baskani` | `turkiye-pazar-kasifi` | HIGH | **RESOLVED** | Raporunuzun §5 'Model Girdileri' tablosu 14 satirin tamamini 80-model/inputs/pazar.yaml dosyasi… |
| `T-105` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | KKDF oranı (%6) ve tetikleyici ödeme şekilleri T1 ile doğrulandı; ancak KKDF MATRAHININ tanımı … |
| `T-151` | `gumruk-vergi-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Ithalat KDV'sinin indirilebilirligi KDVK md.29/1-b, md.34/1 ve md.30 TAM METNI ile T1 seviyesin… |
| `T-153` | `gumruk-vergi-uzmani` | `finans-fizibilite` | MEDIUM | OPEN | 80-model/engine/matrah_sirasi.py:217 meta.model_hedef_tarihi alanini SADECE 'is None' ile denet… |
| `T-203` | `mevzuat-ruhsat-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Bandrol bedeli (2,36073 TL/şişe, KDV hariç) ve TADAB hizmet bedeli (0,1587 TL/şişe) hangi vergi… |
| `T-206` | `mevzuat-ruhsat-uzmani` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | Şişelenmiş ithal şarap için zorunlu laboratuvar analizi (parametreler, akredite lab şartı, part… |
| `T-303` | `navlun-lojistik-uzmani` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Navlun ve sigortanin gumruk kiymetine hangi kurallarla girdigi tanimlanmalidir; ayrica Incoterm… |
| `T-305` | `navlun-lojistik-uzmani` | `global-sourcing-kasifi` | MEDIUM | OPEN | Incoterm secimi (EXW/FOB vs CIF) lojistik kontrolunu ve sigorta teminatini belirler; CIF alimda… |
| `T-405` | `global-sourcing-kasifi` | `turkiye-pazar-kasifi` | MEDIUM | OPEN | Benchmark markalari 'Gold Country' (California) ve 'Central Creek' (Avustralya) uretici markasi… |
| `T-406` | `global-sourcing-kasifi` | `gumruk-vergi-uzmani` | MEDIUM | OPEN | Turkiye 2025'te dokme sarap (GTIP 2204.29) ithalatini pratikte hic yapmamis (628 litre). Bunun … |
| `T-502` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | Turkiye'de alkollu ickinin tuketiciye internetten satisi yasaktir; bu nedenle zincir market onl… |
| `T-503` | `turkiye-pazar-kasifi` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | Alkollu icki reklami/kampanya tanitimi yasagi nedeniyle Metro dahil hicbir perakendeci sarap fi… |
| `T-904` | `yatirim-komitesi-baskani` | `mevzuat-ruhsat-uzmani` | MEDIUM | OPEN | Iki katman/etiket sorunu: (a) ruhsat.yaml'daki HICBIR maliyet kaleminde 'katman' alani yoktur; … |
| `T-905` | `yatirim-komitesi-baskani` | `navlun-lojistik-uzmani` | MEDIUM | OPEN | EV-2026-08-09-310 bir MEVZUAT kanitidir (Karayollari Trafik Yonetmeligi md.128, 44 ton), tier T… |
| `T-906` | `yatirim-komitesi-baskani` | `gumruk-vergi-uzmani` | MEDIUM | ANSWERED | Iki model girdisi hijyen sorunu: (a) vergi.yaml -> urun_parametreleri.sise_hacmi_litre = 0.75 a… |

---

## AÇIK CRITICAL TICKET'LARIN ANLAMI

| ticket | hedef | neyi bloke ediyor |
|---|---|---|
| `T-104` | `finans-fizibilite` | **G1 / G4** — ÖTV modelde sabit sayı olamaz; Yİ-ÜFE endeksli değişken olmalı |
| `T-301` | `mevzuat-ruhsat-uzmani` | **G2-L / G4** — malın gümrükte + antrepoda bekleme süresi ve bandrolün fiziksel yeri |
| `T-304` | `yatirim-komitesi-baskani` | **G2-L / G4** — hiçbir rota için doğrulanmış navlun yok |

**Üçü de masabaşında kapanamaz**: ikisi gerçek kotasyon/uygulama bilgisi,
biri model tasarımı gerektirir. Bu, TUR 7'nin varlık sebebidir.
