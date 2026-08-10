# TUR 2 KONSOLİDASYONU — GATE, TICKET VE ÇELİŞKİ KARARLARI

```yaml
belge:                  tur-2-konsolidasyon
yazan:                  yatirim-komitesi-baskani
tarih:                  2026-08-10
tur:                    TUR 2 SONU
kapsam:                 GATE GUNCELLEMESI + TICKET DEGERLENDIRMESI + CELISKI KARARLARI
karar_iceriyor_mu:      false      # YATIRIM karari icermez
arastirma_yapildi_mi:   false      # CLAUDE.md §1.16
yeni_kanit_uretildi_mi: false
ana_cikti:              90-karar/master-commercial-input-table.md
```

> ## BU BELGE BİR YATIRIM KARARI DEĞİLDİR
>
> `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` / `SCALE` kararlarının **hiçbiri**
> burada verilmemiştir ve verilemez. Nihai karar **TUR 6**'da,
> `90-karar/karar-gunlugu.md`'de verilir.
> **Bu turda `90-karar/karar-gunlugu.md` dosyasına DOKUNULMAMIŞTIR.**
>
> Bu turda değişen tek şey kayıtların **STATÜSÜDÜR**, **İÇERİĞİ DEĞİL.**
> Hiçbir ajan bulgusu değiştirilmemiş, hiçbir çelişki metni silinmemiştir.

---

## 0. BU TURDA NE YAPILMADI (SINIR BEYANI)

| Yapılmadı | Neden |
|---|---|
| Yeni araştırma, web araması, yeni kanıt kartı | CLAUDE.md §1.16 |
| Herhangi bir **değerin** değiştirilmesi | Başkan, ajanın bulgusunu kendi tahminiyle değiştirmez |
| `finans-fizibilite` çağrılması / model çalıştırılması | TUR 3 |
| Boş ticari hücrenin "tabloyu doldurmak için" doldurulması | CLAUDE.md §1.1 |
| Herhangi bir çelişki **metninin** silinmesi | CLAUDE.md §1.13 / §4 — kayıtlar immutable |
| Dış iletişim izni verilmesi (RFQ / forwarder kotasyonu) | Bu bir **TUR 6 karar kalemidir** — §4.4 |

---

## 1. GATE DURUM TABLOSU — TUR 2 SONU (2026-08-10)

| Gate | Soru | Sahibi | **Durum** | TUR 2'de değişim | Açan **tek** koşul |
|---|---|---|---|---|---|
| **G0** Yasal yol | Bu iş Türkiye'de yasal olarak kurulabilir mi? | `mevzuat-ruhsat-uzmani` önerir → **başkan karar verir** | **`PASS`** | **değişmedi** — geri alma tetikleyicilerinin **hiçbiri** gerçekleşmedi (§1.1) | — *(izleme: R1/R2/R3)* |
| **G1** Vergi yapısı | Vergi yükü kanıtlı ve satır satır hesaplanabilir mi? | `gumruk-vergi-uzmani` | **`BLOCKED`** | ⬆️ **belirgin daralma** — menşe→tarife eşlemesi ve menşe ispat belgesi **kapandı** | `T-104` kapanışı → `model_hedef_tarihi` (**yatırımcı girdisi**) + Yİ-ÜFE varsayımı |
| **G2** Tedarik | Gerçek, ulaşılabilir tedarik kaynağı **ve fiyatı** var mı? | `global-sourcing-kasifi` | **`BLOCKED`** | havuz 11→26, TOP 10 RFQ listesi hazır; **`exw`/`fob` hâlâ `null`** | Gerçek RFQ cevabı (**≥5 tedarikçi**) → **dış iletişim izni** (`T-467`) |
| **G2-L** Lojistik / landed | L1→L2→L3 geçişi kanıtla kurulabiliyor mu? | `navlun-lojistik-uzmani` | **`BLOCKED`** | ⬆️ **LCL 9 rotada kapandı**; FCL **14 lane'in 14'ünde YOK** | `T-304` — **3 forwarder'dan yazılı FCL kotasyonu** |
| **G3** Pazar | Benchmark doğrulandı mı, segment gerçek mi? | `turkiye-pazar-kasifi` | **`BLOCKED`** | ithalatçı haritası açıldı (1→4 isimli grup); **`l8_chain_retail` hâlâ `null`** | **`OQ-001`'in promosyon ayağı** (`T-504`) + `l8_chain_retail` (`T-603`) |
| **G4** Ekonomi | Model kanıtlı girdilerle pozitif contribution veriyor mu? | `finans-fizibilite` | **`NOT_EVALUATED`** | değişmedi — ajan henüz çalışmadı | G1 + G2 + G2-L + G3 |
| **G4-K** *(alt-durum)* Kanal girdisi | L6→L7→L8 merdiveni sayısal olarak kurulabiliyor mu? | `kanal-marj-uzmani` | **`BLOCKED`** | **YENİ** — TUR 2'de ilk kez değerlendirildi. **Yapı kuruldu, sayı yok** | `l8_chain_retail` (`T-603`) + `d`/`f` (`T-604`) + `T-601` |
| **G5** Risk | Kırmızı takımın CRITICAL ticket'ları kapandı mı? | `seytanin-avukati` | **`NOT_EVALUATED`** | değişmedi | TUR 4 |

> **Tablo genişletmesi hakkında not:** `G4-K` satırını **ben ekledim**.
> CLAUDE.md §4'ün gate tablosu altı gate tanımlar; `G2-L` de TUR 1 sonunda aynı
> gerekçeyle eklenmişti. **`G4-K` yeni bir gate değil, `G4`'ün bir alt-durumudur**
> ve `kanal-marj-uzmani`'nın TUR 2'de ilk kez ürettiği çıktının gate karşılığını
> görünür kılmak içindir. Bir gate açma/kapama yetkisi doğurmaz.

> **Gate kuralı (değişmedi):** Kapsamında `impact: CRITICAL` açık ticket veya
> çözülmemiş CRITICAL çelişki bulunan gate `PASS` alamaz.

### 1.1 `G0` — geri alma tetikleyicileri tarandı, **hiçbiri gerçekleşmedi**

| # | Tetikleyici | TUR 2'de gerçekleşti mi | Kanıt / gerekçe |
|---|---|---|---|
| **R1** | `C-252` **B okuması lehine** kapanır **VE** "Tekel GM eliyle" işlev için **halef merci** tespit edilir *(ikisi birden)* | **HAYIR** | `mevzuat-ruhsat-uzmani` TUR 2'de **çalışmadı**; `C-252` durumu **değişmedi** (`OPEN`, LOW). Halef merci `EV-2026-08-10-214` hâlâ `UNKNOWN` |
| **R2** | 7584 s.K. m.2'nin **ürünün rafta bulundurulmasını** kapsadığı bağlayıcı bir metinle ortaya çıkar | **HAYIR** | `kanal-marj-uzmani` kısıtı **veri olarak kullandı** (`İP-2001`), **yeniden araştırmadı** (doğru davranış). Yeni bağlayıcı metin **yok** |
| **R3** | `C-202` sıralama döngüsünün **fiilen kilitlendiği** kanıtlanır | **HAYIR** | Yeni kanıt yok; `C-202` `OPEN` (HIGH), durumu değişmedi |

**`G0` → `PASS` KORUNUR.**

**Ancak bir yeni izleme kalemi kayda geçirilir (G0'ı bloke ETMEZ):**
`kanal-marj-uzmani`, Perakende Yönetmeliği'nin 2015 metnindeki *"prim/bedel
talebine konu ürünün sözleşme süresince **rafta satışa sunulması zorunludur**"*
korumasının **2024 metninde görünmediğini** tespit etti
(`EV-2026-08-10-608`, `EV-2026-08-10-622`, → `T-601`).
Bu bir **yasallık** sorusu değil, bir **ticari koşul riskidir** ("listeleme
bedelini ödedik ama raftan çıkarıldık") ve **G4-K** altında izlenir.
**R2 ile karıştırılmamalıdır** — R2 ürünün rafta *bulundurulabilirliğiyle*,
bu kalem rafta *tutulma garantisiyle* ilgilidir.

### 1.2 `G1` — durum değişikliğinin niteliği (önemli)

TUR 2, G1'de **iki uzun süredir açık `UNKNOWN`'ı kapattı:**

| Kapanan | Sonuç | evidence |
|---|---|---|
| **Menşe → uygulanacak tarife eşlemesi (9 ülke)** | **Hiçbiri `UNKNOWN` kalmadı.** ES/CL/PT/IT/FR **%50**, ZA/AR/US/AU **%70**, MD **%70** *(STA var, 2204.21'i kapsamıyor)* | `EV-2026-08-10-151`…`-165`, **T1** |
| **Menşe ispat belgesi** | **EUR.1 (0302) veya Fatura Beyanı (0538)**; **A.TR GEÇERSİZ**; BİLGE **çıkış ülkesi kontrolü** yapar | `EV-2026-08-10-155`, `-158`, `-159`, `-160` |

**Niteliksel değişim:** G1 artık **bilinmeyen hukukla** bloke değildir.
Kalan blokerler **yatırımcı girdisi** (`model_hedef_tarihi`, `OQ-002`),
**makro varsayım** (Yİ-ÜFE) ve **engine uygulaması**dır — yani üçü de
**araştırma blokeri değildir.** Bu, G1'in doğasının değiştiği anlamına gelir
ve TUR 6'da böyle okunmalıdır.

**G1'in en kırılgan yeri değişmedi:** `OQ-G10` — ithalat KDV'sinin
indirilebilirliği sonucu, **KDVK md.36 uyarınca çıkarılmış bir Cumhurbaşkanı
Kararı ARANMAMIŞ olması kaydıyla** geçerlidir (`T-151`). Master tablonun ters
model tezi **doğrudan bu sonuca dayanmaktadır.**

### 1.3 `G2` ve `G2-L` — **masabaşı araştırmayla AÇILAMAZ** (yapısal tespit)

Bu, TUR 2'nin gate tarafındaki **en önemli tek bulgusudur** ve TUR 6'ya
taşınmalıdır:

| Gate | Açan koşul | Masabaşıyla kapanır mı |
|---|---|---|
| **G2** | ≥5 tedarikçiden gerçek RFQ cevabı | **HAYIR** — `global-sourcing-kasifi` **21 alanı** tek tek sayarak kanıtladı: 26 tedarikçinin **26'sında** FOB fiyatı, para birimi, teklif geçerliliği ve palet konfigürasyonu açık kaynakta **yoktur**. Daha fazla masabaşı araştırma **kaynak israfıdır** |
| **G2-L** | 3 forwarder'dan yazılı FCL kotasyonu | **HAYIR** — **14 lane'in 14'ünde** kamuya açık FCL kotasyonu yoktur (`EV-2026-08-10-312`) |
| **G4-K** | Gerçek zincir yıllık anlaşması / distribütör görüşmesi | **HAYIR** — Rekabet Kurumu'nun **kendi sektör raporunda** bedellerin ciroya oranı ve zincirlerin brüt marjı **ticari sır olarak karartılmıştır**, üstelik analiz *"alkol ve tütün hariç"* tanımlıdır |

**Sonuç: üç gate de yalnızca DIŞ TEMASLA açılır.** Dış temas ise bir kaynak ve
izin kararıdır. **Bu, TUR 6'da karşılaşılacak yapısal seçimi şimdiden
tanımlar:** "daha fazla araştır" seçeneği bu üç gate için **mevcut değildir.**

---

## 2. AÇIK CRITICAL TICKET DEĞERLENDİRMESİ

**Devralınan: 5 açık CRITICAL. Kapatılabilen: 0. Yeni açılan CRITICAL: 1.
Tur sonu: 6.**

| ticket | hedef | konu | TUR 2 durumu | **Karar** | Neden kapatılamadı |
|---|---|---|---|---|---|
| **`T-104`** | `finans-fizibilite` | ÖTV maktu tutarı Yİ-ÜFE ile 6 ayda bir kendiliğinden artar; modelde sabit sayı olamaz | `ANSWERED` (`gumruk-vergi-uzmani`, TUR 2) | **`ANSWERED` KORUNUR · `CRITICAL` KORUNUR** · veri yapısı ayağı **KABUL EDİLDİ** | Üç kalan ayağın **üçü de hedef ajanda veya yatırımcıda**: (1) engine'in `otv_maktu_zaman_serisi`'ni fiilen okuduğu **doğrulanmadı**, (2) `makro.yaml`'da Yİ-ÜFE varsayımı **yok**, (3) `model_hedef_tarihi` **`null`** (`OQ-002`). Ayrıca `EV-2026-08-09-111` **2026-09-08'de STALE** |
| **`T-301`** | `mevzuat-ruhsat-uzmani` | Ruhsat/analiz/bandrol nedeniyle gümrükte + antrepoda bekleme süresi; bandrolün fiziksel yeri | `OPEN` — **ajan TUR 2'de çalışmadı** | **`OPEN` · `CRITICAL` KORUNUR** · **kapsamı GENİŞLEDİ** | Cevap yok. **Yeni bağlantı kayda geçirilir:** `lcl-vs-fcl-pilot.md` §6'ya göre T-301'in cevabı *"30+ gün"* çıkarsa **konteyner modu önerisi TERSİNE DÖNER** (FCL → LCL). Yani T-301 artık yalnızca maliyet değil, **operasyon modu** blokeri |
| **`T-304`** | **`yatirim-komitesi-baskani` (BEN)** | Hiçbir rota için doğrulanmış navlun yok | `OPEN` — TUR 2'de **kısmen adreslendi** | **`OPEN` · `CRITICAL` KORUNUR** · **LCL ayağı `ANSWERED`** · başkan cevabı §2.1'de | Çekirdek (**FCL**) açık. Masabaşıyla kapanmaz |
| **`T-466`** | `finans-fizibilite` | Tek yayınlanmış fiyat modele giremez; `exw`/`fob` `null` kalmalı | `OPEN` | **`OPEN` · `CRITICAL` KORUNUR** — **indirim YAPILMADI** (gerekçe §2.2) | Bir **yasak** ticket'ıdır; ancak TUR 3 çalıştıktan sonra **doğrulanabilir** |
| **`T-601`** | `mevzuat-ruhsat-uzmani` | Şişelenmiş şarap 6585 m.7/3 anlamında "tarım ve gıda ürünü" mü? | `OPEN` — **ajan TUR 2'de çalışmadı** | **`OPEN` · `CRITICAL` KORUNUR** | Cevap yok. **`C-601`'in çekirdeği bu ticket'a bağlıdır** — cevap "hayır" ise vade base case'i 60→90 güne kayar ve `peak_cash_requirement` **~%50 artar** |
| **`T-912`** *(YENİ)* | `finans-fizibilite` | `makro.yaml → fx` **`null`**; kur olmadan **her parasal çıktı `UNKNOWN`** döner | **`OPEN`** | **YENİ · `CRITICAL`** | Açıldı; §5.1 |

**CLAUDE.md §5 yürürlüktedir:** bu altısı açıkken `finans-fizibilite` çıktısı
`APPROVED` **olamaz** — en fazla `DRAFT`.

**Ayrıca `OQ-901` (CRITICAL, sahibi: yatırımcı) açıktır:**
`00-charter/karar-esikleri.md`'deki karar eşiklerinin **tamamı `TBD`**'dir.
Bu araştırmayla kapanmaz ve **TUR 6'da nihai kararı bloke eder.**

### 2.1 `T-304` — başkan cevabı *(bu ticket'ın hedefi benim)*

```yaml
ticket_id:         T-304
target_agent:      yatirim-komitesi-baskani
status:            OPEN          # DEGISMEDI
impact:            CRITICAL      # DEGISMEDI
baskan_cevabi:     2026-08-10
kismi_kabul:       LCL_AYAGI_ANSWERED
```

**1 — İddia bütünüyle KABUL EDİLİYOR.** *"Model tek bir navlun rakamına
kilitlenemez"* hükmü **bağlayıcı bir model kuralı** hâline getirilmiştir
(`master-commercial-input-table.md` → **M-6**): FCL bandının **ortalaması
alınamaz**; 300 ve 1.200 USD **ayrı ayrı** çalıştırılır.

**2 — LCL ayağı `ANSWERED` sayılır.** 9 rota için gerçek, tarihli, geçerlilik
süreli kotasyon alınmıştır ve ticket'ın ⚠ ile işaretlediği
*"California → İstanbul UNKNOWN"* satırı **LCL düzeyinde kapanmıştır** (20 gün).
Ticket'ın **kapsamı daralmıştır**, çekirdeği değil.

**3 — Ticket'ın kalan kapsamı resmen daraltılır:** FCL navlunu · İspanya dışı
menşelerin origin charge'ları · Türk sigortacıdan gerçek kotasyon · thermal liner
birim maliyeti · çekici/şasi darası.
*(Bandrolleme, antrepo elleçleme ve kırılma oranı `T-314`'e; terminal tarifeleri
ve free time `T-313`'e aittir ve orada izlenir.)*

**4 — Yeni ve bağlayıcı bir zamanlama kısıtı kayda geçirilir.**
LCL kotasyonlarının geçerliliği **2026-08-16**'dır (`ttl: 6d`). Model bu
tarihten sonra çalıştırılırsa **11 kanıt kartı STALE**'dir ve **projedeki tek
gerçek navlun verisi `UNKNOWN`'a döner.** → **`T-913`**.

**5 — Dış temas izni bu belgede VERİLMEMİŞTİR.** 3 forwarder kotasyonu talebi
`T-467` (tedarikçi RFQ'su) ve `T-604` (kanal görüşmesi) ile **aynı sınıftadır**:
üçü de bana yöneltilmiş **dış temas izni** taleplerdir ve **TUR 6 karar
kalemidir** (§4.4).

### 2.2 `T-466` — **impact indirimi YAPILMADI** (gerekçe)

TUR 2 pre-flight'ta `T-504`'ün `CRITICAL → HIGH` indirimini yaparken şunu
yazmıştım: *"Bir ticket'ın impact'ini, konusu değişmeden, yalnızca bir kullanım
kuralı koyarak düşürmek, gate kuralını etrafından dolaşmaktır"* — ve bu itirazın
**ciddiye alınması gerektiğini** kendim kaydetmiştim.

**Aynı hamleyi `T-466` için tekrarlamıyorum.** Gerekçe, kolaylık değil, **fark**:

| `T-504` | `T-466` |
|---|---|
| Altındaki veri **vardır** ama **nitelenmiştir** (599,90 gözlendi, statüsü belirsiz) | Altındaki veri **YOKTUR** — `exw`/`fob` `null`, alternatif tedarikçi sayısı **0** |
| Blokladığı gate (`G3`) başka yollarla da beslenebilir | Blokladığı gate (`G2`) **masabaşıyla hiçbir şekilde açılamaz** (§1.3) |
| Kural koymak **arıza modunu** keser | Kural koymak **veriyi yaratmaz** |

`T-466`'yı indirmek, hazırlık seviyesini **yanlış temsil etmek** olurdu.
**`CRITICAL` kalır.**

### 2.3 Kapatılabilen HIGH/MEDIUM ticket'lar

| ticket | Karar | Gerekçe |
|---|---|---|
| **`T-464`** (`global-sourcing` → `turkiye-pazar`) | **`OPEN` → `ANSWERED`** | `turkiye-pazar-kasifi` **cevapladı** (`marka-turkiye-varlik-kontrolu.md` §1B.2, `EV-2026-08-10-553`, `-564`): 7 Model A markasının **hiçbirinin** Türkiye'de ithalatçısı bulunamadı. **`RESOLVED` YAPMIYORUM** — cevap bir **negatif arama sonucudur** (`BULUNAMADI` ≠ `YOK`) ve ajanın kendisi bunu açıkça yazmıştır: tek kanal, Metro görülmedi, resmî ithalatçı listesi alınamadı (`T-505`). Kapanış için **`T-505` gerekir** |
| **`T-401`** (`global-sourcing` → `gumruk-vergi`) | **`OPEN` → `ANSWERED`** | `mense-tarife-eslemesi.md` bu ticket'ın tam sorusunu (9 ülke × tercihli rejim × menşe belgesi) **T1/T2 ile cevaplamıştır**. `RESOLVED` yapmıyorum çünkü ajanın kendi §6 kaydına göre **`mevzuat.gov.tr` / `ggm.ticaret.gov.tr` erişilemedi**; Şili satırının **belgesi T3**'tür ve 1/98 Protokol 3 metni **birincil kaynaktan okunmamıştır** |
| **`T-462`** (yeni menşeler: MD/RO/BG/NZ) | **`OPEN` → `ANSWERED`** | Moldova `EV-2026-08-10-165` (T1) ile kapatıldı: **STA var, 2204.21'i kapsamıyor → %70**; RO/BG **%50**. **NZ cevaplanmadı** → ticket `ANSWERED` ama **eksik**; NZ ayağı açık kalır *(pratikte önemsiz: Clark Estate charter kapsamı dışıdır ve bir **MOQ referansıdır**, tedarikçi adayı değil)* |
| **`T-506`** (`turkiye-pazar` → `kanal-marj`) | **`OPEN` → `ANSWERED`** | `kanal-marj-uzmani` kanal tarafını cevapladı (`EV-2026-08-10-612`): ciro primi mekaniği alkolde **vardır**; Metro'nun alkolü çek/sadakat kampanyalarından hariç tutması **tüketici mekaniğidir**, tedarikçiden alınan ticari bedellerle **aynı şey değildir**. **Metro mağaza ↔ sevkiyat fiyatı FARKI hâlâ `UNKNOWN`** (`OQ-612`) → `RESOLVED` yapılmaz |
| **`T-402`** (konteyner doluluk) | **`OPEN` KALIR** | İlk somut veri geldi (14.112 şişe/20ft, **paletsiz**) ama **paletli rakam `UNKNOWN`** ve `C-301` (palet bandı) açık. → `T-461` |

**Diğer 50+ HIGH/MEDIUM ticket'ta statü değişikliği yapılmamıştır** — hedef
ajanları TUR 2'de çalışmadı veya cevap üretmedi.

---

## 3. ÇELİŞKİ KARARLARI

**TUR 2'de 9 yeni çelişki açıldı + `C-302` için kapatma önerisi geldi.**
**Çözülen: 6 · Açık kalan: 3.**
Tam gerekçeler `99-ops/celiskiler.md` → **§TUR 2 SONU — BAŞKAN ÇÖZÜM KAYITLARI**.

| id | Konu | impact | **Karar** | Kural |
|---|---|---|---|---|
| **`C-302`** | Akdeniz/ABD transit süresi | HIGH | **`RESOLVED` — TEYİT EDİLDİ** *(zaten 2026-08-09'da kapanmıştı)*; B'nin *LA→İstanbul 15 gün* ayağı artık **pozitif olarak yanlışlandı** (gerçek: 20 veya 44 gün) | Kural 1 |
| **`C-311`** | **FCL base ocean: 295–650 USD vs 1.200–2.500 EUR (4–5 kat)** | **CRITICAL** | **`OPEN` — KISMEN DARALTILDI.** T5 bacağı **elendi**; band **daraltılmadı** | Kural 1 → Kural 6 |
| **`C-312`** | Ardiye free time 0 gün mü 5 gün mü | MEDIUM | **`RESOLVED` — KAPSAM (sahte çelişki)**; free time **terminale özgüdür**, ulusal sabit değildir | Kural 4 |
| **`C-313`** | Taşıyıcı THD ↔ terminal kapı-çıkış çift sayımı | MEDIUM | **`OPEN` — ama TUR 3 için `NON-MATERIAL`** (~0,008–0,010 USD/şişe) | Kural 6 |
| **`C-461`** | "FOB" iki farklı katmana işaret ediyor | HIGH | **`RESOLVED` — KATMAN (sahte çelişki)** + **bağlayıcı adlandırma kuralı** | Kural 5 |
| **`C-462`** | MOQ 3.000–6.000; pilot tam ortada | HIGH | **`RESOLVED` — KAPSAM (sahte çelişki)**, `C-401` ile **aynı gerekçe**; kalan bir `UNKNOWN`'dır, `CONFLICT` değil | Kural 4 |
| **`C-561`** | Stok dışı listeleme havuzu iki modlu | MEDIUM | **`RESOLVED` — TANIM**; model girdisi etkisi **YOK**, talep okuması **`UNKNOWN` kalır**; **`C-501` AÇIK KALIR** | Kural 2 + 4 |
| **`C-601`** | **Vade: yasal tavan 60 gün vs Migros DPO ~93 gün** | HIGH | **`OPEN` — İKİ KAYNAK YENİDEN KAPSAMLANDI**, çekirdek **`T-601`'e bağlı** | Kural 2 + 4 → Kural 6 |
| **`C-602`** | Tekel/HoReCa marjı tanımsız ve kendi içinde çelişkili | HIGH | **`RESOLVED` — SAHTE ÇELİŞKİ**; tüm kaynaklar elendi → geriye **`UNKNOWN`** kalır (veri **üretilmedi**) | Kural 1 |
| **`C-161`** | GTS'te Form A mı REX mi | LOW | **`RESOLVED` — NON_MATERIAL (kapsam dışı)**; GTS 2204.21'de **hiçbir koşulda** uygulanmaz | Kural 4 |

### 3.1 `C-311` (CRITICAL) — neden çözemedim, ne yaptım

**Yapabildiğim:** `EV-2026-08-10-324` ve `EV-2026-08-09-333` **T5**'tir ve
**birebir aynı bandı** (1.200–2.500 EUR) verirler — yani **bağımsız değildirler,
biri diğerinden kopyalanmıştır.** CLAUDE.md §2: T5 tek başına sonuç üretemez.
**Bu iki kart, sonuç üreten kaynak olarak ELENMİŞTİR** (yalnızca "nereye
bakılacağı" ipucu olarak kalırlar).

**Yapamadığım:** Bandı daraltmak. Çünkü elemeden sonra geriye kalan Kaynak A
(`EV-2026-08-10-322`, marketplace *"from"* fiyatları) **tarihsizdir**,
**konteyner boyu belirtilmemiştir** ve bir *"from"* teaser fiyatıdır — kendi
başına bir `FACT` üretemez. Bandın üst ucu **artık T5 bloglara değil**,
`EV-2026-08-10-320`'ye (**DFDS yayınlanmış tarifesi, T4, tarihli**) dayanır —
ki o da **ters yön (ihracat)** ve **2025**'tir, yalnızca **mertebe çapası**
olarak kullanılabilir.

**Sonuç:** Band `300 – 1.200 USD` **olduğu gibi kalır** (`ESTIMATE`, `LOW`,
`ttl: 14d`). **Kaynak temizlendi, belirsizlik daralmadı.** Bir bandın
**gerekçesini** iyileştirmek onu **daraltmakla aynı şey değildir** ve öyle
sunulmamalıdır.

**Kapanış yolu tektir:** `T-304` — bir forwarder'dan **kalem kalem
`included/excluded` listeli yazılı kotasyon.** Masabaşında çözülemez.

### 3.2 `C-601` (HIGH) — iki kaynak yeniden kapsamlandı, çekirdek açık

| Kaynak | Karar | Kural |
|---|---|---|
| **A** — 6585 m.7/3, vade ≤60 gün (T3/içerik T1, yürürlük **2024-01-01**) | **GEÇERLİ** — yasal tavanın **metni** tartışmalı değildir | — |
| **B** — RK, organize kanal **70 gün** (T2, veri **2020**, **süt**) | **ELENDİ** — tavanın yürürlüğe girdiği **01.01.2024'ten ÖNCEKİ** dönemi ve **şarap olmayan** bir kategoriyi ölçer. **A'yı çürütemez**; A'nın **niçin çıkarıldığını** açıklar | Kural 2 + Kural 4 |
| **C** — Migros DPO **~93 gün**, borçların **%34,4'ü 3–12 ay** (T4 denetimli, **2025**) | **ELENMEDİ ama YENİDEN KAPSAMLANDI** — *"tüm kategoriler, tüm coğrafya"* konsolide bir rakamdır; finansallarda gıda/gıda dışı ve yurt içi/yurt dışı **ayrıştırması YOKTUR**. **Şarap vadesi olarak okunamaz.** **`STRESS` senaryo çapası** olarak kalır, base case değil | Kural 4 |

**Çekirdek soru açık kalır:** Şarap 6585 m.7/3 anlamında "tarım ve gıda ürünü"
müdür? Bu bir **hukuki nitelemedir**; `kanal-marj-uzmani` bunun kendi alanı
olmadığını **açıkça yazmıştır** ve benim kendi yorumumla kapatmam
**CLAUDE.md §1.16 ihlali** olurdu. → **`T-601` (CRITICAL, OPEN)**.

**Model kuralı değişmedi:** `zincir_market.odeme_vadesi_gun` = **`null`**;
dört senaryo **45 / 60 / 90 / 120** gün ayrı ayrı çalıştırılır.

### 3.3 `C-461` — çözülen NE, çözülmeyen NE

**Çözülen:** *Terminolojik* çelişki. Incoterms® FOB (**L1**) ile şarap
ticaretindeki "FOB = ex-cellar" kullanımı (fiilen **L0**) **birbirini
çürütmez** — ikisi de kendi bağlamında doğrudur. Bu, çözüm hiyerarşisinin
**Kural 5'inin (`KATMAN`) ders kitabı örneğidir**: *"en sık yapılan sahte-çelişki
türü; önce bunu ele."*

**Bağlayıcı kural (proje geneli, tüm ajanlar):**

> **Kaynağında Incoterm açıkça yazılmayan — EXW için *yer*, FOB için *adı
> belirtilen liman* belirtilmeyen — hiçbir fiyat `L0` veya `L1` diye
> etiketlenemez. Böyle bir fiyatın `price_layer` alanı `UNKNOWN`'dır ve
> modele giremez.**

`global-sourcing-kasifi`'nin `supplier-shortlist-v2.csv`'de `price_layer`
kolonunu ayrı tutması **doğrulanmıştır**. Kural ayrıca `gumruk-vergi-uzmani`
(gümrük kıymeti matrahı) ve `finans-fizibilite` (katman disiplini) için de
bağlayıcıdır.

**Çözülmeyen:** Harland'ın `$2.85+` sayısının **hangi katmanda olduğu**.
Bu bir **örnek düzeyi `UNKNOWN`**'dır, bir çelişki değil, ve **tedarikçi
bazında** RFQ 3.1/3.2 ile kapanır. `OQ-451` / `T-466` altında izlenir.

### 3.4 `C-602` — çözüm veri ÜRETMEZ

`C-602` çözüldü, çünkü **çelişecek kaynak kalmadı**: tekel bayii için sayılan
beş iddia (%6 / %8 / %10–15 / %17 / %18–30) ve HoReCa çarpanı için sayılan üç
iddia (2× / 2,5× / 4–5×) **hepsi T5'tir** ve hiçbiri margin/markup ayrımını,
KDV tabanını veya katman çiftini belirtmez — yani `M1` gereği **tanımsızdır**.
CLAUDE.md §2 + Kural 1 uyarınca **tamamı elenir.**

> **Bu bir veri kazanımı DEĞİLDİR.** Bir `CONFLICT` kaydı bir `UNKNOWN` kaydına
> **dönüştürülmüştür**, o kadar. `tekel_bayi.marj_pct` ve
> `horeca.fiyat_carpani` **`UNKNOWN`** kalır; duyarlılık bantları
> `ASSUMPTION` / `SENSITIVITY_ONLY` olarak ve **kanıtlı çapası olmadığı açıkça
> yazılarak** durur. `kanal-marj-uzmani`'nın davranışı **doğrulanmıştır.**

### 3.5 KAYIT DÜZELTMESİ — `C-401` / `C-402` / `C-403`

`50-sourcing/rapor-tur2-global-sourcing.md` §4, bu üç çelişkiyi **"AÇIK"**
olarak raporlamaktadır. **Bu kayıt yanlıştır:**

| id | Ajanın TUR 2 raporundaki ifadesi | **Gerçek durum (kayıt)** | Karar tarihi |
|---|---|---|---|
| `C-401` | "AÇIK" | **`RESOLVED`** — Kaynak A (T5 agregatör) elendi; kalan fark bir **kapsam farkıdır** | 2026-08-09 |
| `C-402` | "AÇIK" | **`RESOLVED`** — **sahte çelişki** (L8 raf fiyatı ↔ L2 CIF ortalaması; farklı katman **ve** farklı popülasyon) | 2026-08-09 |
| `C-403` | "AÇIK" | **`UNRESOLVABLE`** — iki T5 kaynak; `LOW`; modele girmez | 2026-08-09 |

**Bu bir değerlendirme değişikliği değil, bir tutarsızlık düzeltmesidir**
(`C-551` impact düzeltmesiyle aynı sınıf). Ajanın **bulgusuna dokunulmamıştır**;
yalnızca statü kaydı düzeltilmiştir. → **`T-918`** ile ajana bildirilir ve
hiçbir alt sonucun yanlış statüye dayanmadığı teyit ettirilir.

**Not — kalan gerçek boşluk `UNKNOWN`'dır, `CONFLICT` değil:** bize
uygulanacak gerçek MOQ (`OQ-402`, CRITICAL) yalnızca RFQ ile öğrenilir.
Ajanın **maddi bulgusu geçerlidir ve korunur**: 5.000'lik pilot, MOQ'su bilinen
**beş üreticinin üçüyle mümkün, ikisiyle değildir** — MOQ bir ülke veya sektör
özelliği değil, **firma özelliğidir.**

---

## 4. TUR 3'E GEÇMEYE ENGEL VAR MI?

### 4.1 Net cevap

> # **HAYIR — TUR 3'e geçmeye ENGEL YOKTUR.**
>
> Ama **dört bağlayıcı koşulla** ve **çıktısı önceden bilinen** bir turdur.

**Gerekçe:** CLAUDE.md §12 ve §15 `finans-fizibilite`'yi **eksik girdiyle
çalışacak** şekilde tasarlamıştır: *"Model, eksik girdi ile çalıştırıldığında
uydurmaz — `UNKNOWN` döndürür ve hangi girdinin eksik olduğunu raporlar."*
Yani **`UNKNOWN` dönmek TUR 3'ün başarısızlığı değil, doğru çıktısıdır.**
Eksik girdi TUR 3'ü **engellemez**; TUR 3'ün **sonucunu belirler.**

Dahası, TUR 3'ün **gerçek bir kazanımı vardır**: ters modelin TL bacağı
(`L8 → CIF_TRY`) **`fx` olmadan bile** çalışır ve *"bu segment matematiksel
olarak mümkün mü"* sorusunun **ilk gerçek testini** üretir
(`master-commercial-input-table.md` §5.3).

### 4.2 Dört bağlayıcı koşul

| # | Koşul |
|---|---|
| **K-1** | **Çıktı `DRAFT`'tır, `APPROVED` OLAMAZ.** 6 açık CRITICAL ticket (CLAUDE.md §5). |
| **K-2** | **`fx` dolana kadar her parasal toplam `UNKNOWN` döner.** Model bunu **raporlamak** zorundadır, tahmin etmek değil. → `T-912` |
| **K-3** | ⚠ **TAZELİK KAPISI: TUR 3, 2026-08-16'dan ÖNCE çalıştırılmalıdır.** Aksi hâlde 11 LCL kanıt kartı **STALE**'dir ve projedeki **tek gerçek navlun verisi `UNKNOWN`'a döner**. → `T-913`, `OQ-912` |
| **K-4** | **`master-commercial-input-table.md` §5.6'daki M-1…M-10 kuralları bağlayıcıdır.** Özellikle **M-2** (`exw`/`fob` `null`), **M-3** (599,90 tek hedef fiyat değil), **M-5** (para birimleri toplanamaz), **M-6** (FCL bandı ortalanamaz). |

### 4.3 Engel OLMAYAN ama sayılması gereken üç şey

1. **`mevzuat-ruhsat-uzmani` TUR 2'de çalışmadı.** Bu nedenle `T-301` (CRITICAL),
   `T-601` (CRITICAL), `T-102`, `T-403`, `T-505` cevapsızdır. Bu, TUR 3'ü
   engellemez — ama **antrepo bekleme süresi, vade tavanı ve konteyner modu**
   TUR 3'te `UNKNOWN` dönecektir. **`mevzuat-ruhsat-uzmani`'nın TUR 5'te değil,
   TUR 3'e PARALEL çalıştırılması bu üç `UNKNOWN`'ı kapatabilir** ve
   maliyeti düşüktür.
2. **`turkiye-pazar-kasifi`'nin fiziksel gözlem paketi yapılmadı.** Tek bir
   mağaza turu **`T-504` + `T-603` + `C-551` + `C-501`/`OQ-502` + `OQ-001`'in
   promosyon ayağını AYNI ANDA** kapatır. **Projedeki en yüksek bilgi/maliyet
   oranına sahip eylem budur** ve iki turdur yapılmamıştır. → **`T-917`**
3. **`OQ-901` (karar eşikleri `TBD`) ve `OQ-002` (`model_hedef_tarihi`)
   yatırımcı girdisidir.** İkisi de araştırmayla kapanmaz. `OQ-002` **TUR 3'ü**,
   `OQ-901` **TUR 6'yı** bloke eder.

### 4.4 TUR 6'ya taşınan yapısal karar kalemi

`T-304` · `T-467` · `T-604` — üçü de bana yöneltilmiştir ve üçü de aynı şeyi
ister: **dış temas izni** (forwarder kotasyonu · tedarikçi RFQ'su · kanal
görüşmesi).

**Bu turda izin VERİLMEMİŞTİR** — CLAUDE.md §8 gerçek RFQ'yu **TUR 7**'ye ve
`TEST`/`IMPORT PILOT` kararına bağlar.

**Ancak §1.3'te gösterilen yapısal gerçek TUR 6'ya taşınmalıdır:**

> **`G2`, `G2-L` ve `G4-K` masabaşı araştırmayla AÇILAMAZ.**
> TUR 6'da "daha fazla araştıralım" seçeneği bu üç gate için **mevcut
> değildir.** Seçenek kümesi şudur: **(a) dış temasa kaynak ayır**,
> **(b) bu gate'ler kapalıyken karar ver**, **(c) `HOLD`.**
> Bu, kararın **şeklini** şimdiden belirler ve TUR 6'da sürpriz olmamalıdır.

---

## 5. AÇILAN YENİ TICKET'LAR VE AÇIK SORULAR

### 5.1 Yeni ticket'lar (`T-911` … `T-918`)

| ticket | hedef ajan | claim (kısa) | impact |
|---|---|---|---|
| **`T-911`** | `gumruk-vergi-uzmani` | İthalatta hangi kur uygulanır — **gümrük kuru mu serbest piyasa kuru mu**? Hukuki dayanağı, ilan periyodu ve beyanname tescil tarihiyle ilişkisi. `makro.yaml → fx.gumruk_kuru_kullanilir_mi` **`UNKNOWN`** | **HIGH** |
| **`T-912`** | `finans-fizibilite` | `makro.yaml → fx` (**usd_try, eur_try, eur_usd**) **`null`**. Kur **tarihli ve kanıtlı** doldurulmadan modelin **her parasal çıktısı `UNKNOWN`** döner. Ayrıca `fiyat_guncelleme_gecikmesi_gun` **`null`** — alış dövizle, satış TL ile: bu **ayrı bir duyarlılık eksenidir** | **CRITICAL** |
| **`T-913`** | `navlun-lojistik-uzmani` | `EV-2026-08-10-301…311` (11 LCL kartı) **2026-08-16'da STALE**. Projedeki **en kısa ömürlü kanıt seti**. TUR 3 öncesi yeniden doğrulama protokolü gerekir; dış temas gerektirip gerektirmediği belirtilmelidir | **HIGH** |
| **`T-914`** | `gumruk-vergi-uzmani` | **Şili menşeli şarapta Barcelona AKTARMASI, `SIL` rejiminin "çıkış ülkesi yalnızca Şili" kuralını bozar mı?** Tek konşimento altında transshipment ile konsolidasyon/antrepo girişi aynı şey midir? Bozuyorsa en ucuz Şili LCL rotası **%50 → %70** demektir (**CIF 100 TL'de +24 TL/şişe**) — yani navlun avantajının tamamından büyüktür. *(`T-163`'ün somutlaşmış hâli; o ticket LCL rotaları bilinmeden açılmıştı)* | **HIGH** |
| **`T-915`** | `navlun-lojistik-uzmani` | **Fransız adaylarının limanı eşleşmiyor.** Tek FR kotasyonu **Marsilya** (Akdeniz, Hamburg/Antwerp aktarmalı); The Wine Factory **Gornac/Bordeaux** (Atlantik) + Valros/Languedoc, Plaimont **Saint-Mont/Gaskonya** (→ Bordeaux). **Marsilya bu iki tedarikçi için geçerli bir navlun çapası değildir** | **HIGH** |
| **`T-916`** | `navlun-lojistik-uzmani` | **İtalya rotası test edilen limanların tamamında Tirrenya'dır** (Genova/La Spezia/Livorno/Napoli) ve hepsi `UNKNOWN`. A-öncelikli İtalyan tedarikçi **Roncà (VR), Veneto**'dadır → doğal limanları **Trieste/Venedik/Ravenna**. Ayrıca elinizdeki `EV-2026-08-10-320` **DFDS Trieste–Pendik/Mersin tarifesidir** ve yalnızca 40HC/20DV **oranı** için kullanılmıştır — **ithalat rotası adayı olarak hiç değerlendirilmemiştir**. İtalya Türkiye'nin **en güçlü ithalat hattıdır** (5.749.972 L/2025) ve şu anda **lojistik olarak tamamen `UNKNOWN`**'dır | **HIGH** |
| **`T-917`** | `turkiye-pazar-kasifi` | **TEK FİZİKSEL GÖZLEM PAKETİ.** Bir mağaza turu (**≥2 şehir, ≥20 SKU, şarap reyonu raf etiketi fotoğrafı, Metro şarap reyonu dahil, KDV ibaresi ve promosyon rozeti okunacak şekilde**) şunları **aynı anda** kapatır: `T-504` (promosyon ayağı) · `T-603` (`l8_chain_retail`) · `C-551` (KDV gösterimi) · `C-501`/`OQ-502` (stok dışı fiyat gerçekliği) · `OQ-001`'in kalan iki ayağı. **`T-504` ve `T-603`'ün YERİNE GEÇMEZ** — minimum gözlem protokolünü tanımlar. **Projedeki en yüksek bilgi/maliyet oranına sahip eylemdir** | **HIGH** |
| **`T-918`** | `global-sourcing-kasifi` | `rapor-tur2-global-sourcing.md` §4, `C-401` / `C-402` / `C-403`'ü **"AÇIK"** olarak raporluyor; gerçek durum **`RESOLVED` / `RESOLVED` / `UNRESOLVABLE`** (2026-08-09). Kayıt düzeltilsin ve **hiçbir TUR 2 alt sonucunun yanlış statüye dayanmadığı** teyit edilsin | **MEDIUM** |

### 5.2 Yeni açık sorular

| id | Soru | Sahibi | Neden önemli |
|---|---|---|---|
| **`OQ-911`** | **Antrepo / bandrolleme tesisi nerede olacak?** Varış limanı seçimi buna bağlıdır (`EV-2026-08-10-332`) ve TRY bacağının **en büyük tek kalemini** (iç nakliye) **2,7–3,2 TRY/şişe** değiştirir. THD farkı ise yalnızca 0,006–0,011 USD/şişe — yani **~2 kat mertebe farkı** | **kurucu / yatırımcı** (+ `navlun-lojistik-uzmani`) | Varış limanı bir **terminal tarifesi kararı değil, bir tesis yeri kararıdır**. Ayrıca `C-312`'nin (free time) hangi terminale göre okunacağını belirler |
| **`OQ-912`** | **TUR 3 hangi tarihte çalıştırılacak?** Tazelik penceresi: LCL kotasyonları **2026-08-16**, türetilmiş lojistik/FCL kartları **2026-08-24**, ÖTV `EV-2026-08-09-111` **2026-09-08** | **`yatirim-komitesi-baskani`** | Model bu pencerelerin dışında çalışırsa **kendi girdilerini bayatlatarak** çalışır. Bu bir zamanlama kararıdır ve şimdiye kadar hiç sorulmamıştır |

---

## 6. REDDEDİLEN BULGU LİSTESİ

**Bu turda reddedilen ajan bulgusu: 0.**

Kabul edilen öneriler:
- `navlun-lojistik-uzmani`'nın **`C-302`'yi A lehine kapatma önerisi** — **kabul
  edildi** (zaten kapalıydı; öneri **teyit** olarak kayda geçirildi).
- Aynı ajanın **`EV-2026-08-09-327`'nin (G. Afrika ~26 gün, ters yön ölçümü)
  `SUPERSEDED` sayılması önerisi** — **kabul edildi**. ⚠ **Kartın kendisini ben
  değiştirmiyorum**; `status` alanının güncellenmesi kartı açan ajana aittir
  (kanıt kartları immutable'dır, `supersedes` bağı `EV-2026-08-10-307` ile
  kurulur). **Ajanın kendi TUR 1 tahmininin ~2 kat iyimser olduğunu kendisi
  tespit edip kaydetmesi kayda geçirilmiştir.**
- `global-sourcing-kasifi`'nin **`price_layer` kolonunu ayrı tutma** kararı —
  **doğrulandı** ve proje geneli kural hâline getirildi (§3.3).
- `kanal-marj-uzmani`'nın **hiçbir T5 marj sayısını `value` alanına yazmama**
  kararı — **doğrulandı** (§3.4).
- `turkiye-pazar-kasifi`'nin **`BULUNAMADI` ≠ `YOK`** ayrımı ve `pazar.yaml`'a
  dokunmama kararı — **doğrulandı**.
- `gumruk-vergi-uzmani`'nın **`T-104`'ü tek taraflı `RESOLVED` yapmama** kararı —
  **doğrulandı**.

**Düzeltilen kayıt hataları: 4** — `C-401`, `C-402`, `C-403` statüleri (§3.5) ve
`C-601`/`C-602`'de `etki:` alanının `impact:` yerine kullanılması (§6.1).

### 6.1 `impact` alanı kullanımı — bağlayıcı okuma kuralı

`C-601` ve `C-602`'nin `yaml` bloklarında severity, `impact:` alanına değil
**`etki:` alanına** yazılmıştır (`etki: CRITICAL` / `etki: MEDIUM`).
`99-ops/celiskiler.md`'nin kayıt formatına göre **`etki:` = "bu çelişki
çözülmezse model nerede kırılır"**, **`impact:` = `CRITICAL|HIGH|MEDIUM|LOW`**.

**Bağlayıcı kural:** Ajan **`impact:` alanını doğru kullanmışsa o değer esastır**
(`C-551` → **HIGH**, 2026-08-10 kaydı). **Yalnızca `etki:` yazılmışsa** blok bir
`impact` beyan etmiş sayılmaz ve **özet tablosundaki değer esastır**
(`C-601` → **HIGH**, `C-602` → **HIGH**).

**Başkan hiçbir çelişkinin impact'ini yükseltmemiş veya düşürmemiştir.**

---

## Bu değerlendirmeyi ne çürütür?

*(Bu belge bir yatırım kararı içermez. Aşağıdaki soru bu turun **tek hükmüne** —
**"TUR 3'e geçmeye engel yoktur; engel, TUR 3'ün ne üretebileceğindedir"** —
ilişkindir.)*

### En güçlü tek çürütücü bulgu

**`fx`, `l8_chain_retail` ve `model_hedef_tarihi`'nin üçünün de bir günde
kapanabilir olduğunun gösterilmesi** — yani bu turun "hazır değiliz" teşhisinin
**bir araştırma sorunu değil, bir SIRALAMA hatası** olduğunun ortaya çıkması.

Üçü de araştırma gerektirmez: `fx` bir tarihli kur kaydıdır, `l8_chain_retail`
bir mağaza turudur, `model_hedef_tarihi` bir yatırımcı beyanıdır. Eğer bu üçü
TUR 3'ten **önce** kapatılabiliyorsa, TUR 3 `UNKNOWN` döndüren bir tur olmaktan
çıkıp **ters modelin gerçek bir çıktısını** üreten bir tura dönüşür — ve bu
belgenin *"çıktısı önceden bilinen bir tur"* teşhisi **yanlış** olur.

**Bu, kendi değerlendirmemin en zayıf yeridir ve bunu gizlemiyorum:** Ben
gate'leri kapalı ilan ederken, o gate'lerin bir kısmının **ucuz** olduğunu aynı
belgede yazıyorum. İki cümle aynı anda doğruysa, doğru tepki "TUR 3'e geç"
değil, **"TUR 3'ten önce üç ucuz alanı kapat"**tır. Bunu bir **karar** olarak
veremem (bu tur karar turu değildir), ama **kayda geçiriyorum**.

### İkinci en güçlü çürütücü (farklı hükmü hedefler)

**`C-311`'in bir forwarder kotasyonuyla değil, zaten elimizdeki bir kanıtla
kapanabileceğinin gösterilmesi.**
`EV-2026-08-10-320` (DFDS) **yayınlanmış, tarihli, kalem kırılımlı bir taşıyıcı
tarifesidir** ve Trieste–Türkiye hattını fiyatlar. Ben onu "ters yön ve 2025"
diye yalnızca **oran çapası** saydım. Eğer aynı taşıyıcının **ithalat yönlü ve
2026** tarifesi yayınlanıyorsa, `C-311`'in üst ucu **masabaşında** T4 seviyesinde
kapanabilir ve *"G2-L masabaşıyla açılamaz"* hükmüm **kısmen yanlış** olur.
Bu ihtimal `T-916` ile aynı temasta test edilecektir.

### Bu turun en tartışmalı hükmü

**`C-462`'nin `RESOLVED — KAPSAM` yapılması.**

Karşı argüman güçlüdür: *"MOQ 3.000 ile 6.000 arasındaki fark pilotun
uygulanabilirliğini doğrudan belirler; bunu 'firma özelliği' diye çelişki
listesinden çıkarmak, bir karar riskini kayıttan silmektir."*

**Savunmam:** Kayıttan silinen şey **risk değil, YANLIŞ ETİKETTİR.**
Risk aynen durmaktadır — ama artık `CONFLICT` olarak değil, **`UNKNOWN`**
(`OQ-402`, CRITICAL) ve **bağlayıcı model kuralı** (**M-4**: MOQ tek değere
kilitlenemez) olarak. Ayrıca ajanın maddi bulgusu (**5 üreticinin 3'üyle mümkün,
2'siyle değil**) §3.5'te **aynen korunmuştur**. Bir çelişki etiketi, bir
belirsizliği **saklamak için** kullanılmamalıdır.

### Bu turun en kırılgan hükmü

**`G0` → `PASS`'in korunması.**

Kırılgan çünkü bu turda `G0`'ı **kimse test etmedi**: `mevzuat-ruhsat-uzmani`
TUR 2'de çalışmadı. Ben yalnızca **tetikleyicilerin gerçekleşmediğini**
doğruladım — ki bu, "yeni olumsuz kanıt aranmadı" ile **aynı şeydir**.
`G0 PASS` hâlâ **iki açık çelişkinin (`C-252`, `C-203`) üzerinde durmaktadır**
ve TUR 2 bu zeminde **hiçbir şey değiştirmemiştir.** Bunu gizlemiyorum:
`G0`, bu projede **geri alınabilir** bir gate olarak işaretli kalır.

### Bu turun kör noktası

Bu tur **hiçbir yeni kanıt üretmemiştir.** Yaptığım şey, beş ajanın TUR 2
çıktılarını **bir hesaplanabilirlik envanterine** çevirmek ve statüleri
güncellemektir. Eğer TUR 1/1.5/2'nin kanıt tabanı **sistematik olarak** hatalıysa
— özellikle `EV-2026-08-09-405`'in Comtrade birim kodu yorumu, ki
`global-sourcing-kasifi` bunu **iki turdur** doğrulamadığını itiraf etmektedir ve
**bu raporlardaki her "L2 CIF" atfı o yoruma dayanmaktadır** — bu tur o hatayı
**yakalayamaz**; yalnızca üzerine bir hazırlık etiketi yazar.
Panzehir **TUR 4**'tür: `seytanin-avukati` bu belgeyi değil, **altındaki kanıt
kartlarını** hedef almalıdır.
</content>
