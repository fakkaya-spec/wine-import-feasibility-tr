# AJAN RAPORU — navlun-lojistik-uzmani · TUR 3.25

```yaml
ajan:                  navlun-lojistik-uzmani
tur:                   TUR 3.25 — FORWARDER RFQ PAKETI (§9, §10, §15)
tarih:                 2026-08-10
durum:                 SUBMITTED
dis_iletisim_yapildi:  false
mesaj_gonderildi:      false
yeni_kanit_karti:      0   # 10-evidence/index.csv bu turda DOKUNMA listesinde
yeni_navlun_arastirmasi: HAYIR   # gorev tanimi geregi
```

---

## 1. YÖNETİCİ ÖZETİ

Bu turda **hiçbir forwarder'a temas edilmedi** ve **hiçbir yeni navlun
araştırması yapılmadı**. Üretilen şey bir veri değil, bir **araçtır**: üç
bağımsız forwarder'a aynı anda, aynı metinle gönderilebilecek, **20 zorunlu
kalemli** bir RFQ; **5 hedeflik** doğrulanmış iletişim listesi; ve forwarder'ın
dolduracağı **34 zorunlu alanlı** yapılandırılmış cevap sayfası.

**En kritik tek bulgu şudur:** `T-304` artık bir araştırma eksiği değildir.
Kapanması için gereken her şey hazırdır; eksik olan tek şey **gönderim
iznidir**. Bu, başkanın `T-304` §5'te yazdığı hükmün (*"`G2-L` masabaşı
araştırmayla açılamaz"*) somut olarak doğrulanmasıdır — TUR 3.25 bu hükmü test
etti ve **kırmadı**.

İkinci bulgu daha rahatsız edicidir: doğrudan e-posta ile ulaşılabilen forwarder
sayısı **3**, `T-304`'ün kapanma koşulu da **3 yazılı kotasyon**. **Hata payı
sıfırdır.** Bir sessizlik, koşulu düşürür.

---

## 2. BULGULAR

### B-1: RFQ metni — "all-in" reddi bir üslup değil, bir veri kalitesi kuralıdır

```yaml
claim:          "Tek bir all-in rakam, bu rotalarda maliyet yapisini GIZLER ve iki forwarder'i karsilastirilamaz kilar; bu yuzden RFQ metninde acikca reddedilmistir."
value:          "EUR 349/konteyner (Ispanya origin, minimum) > ~USD 300 (ayni lane base ocean, alt uc)"
unit:           EUR / USD per konteyner
status:         FACT (origin) + ESTIMATE (ocean)
tier:           T3 (origin, Hapag-Lloyd yayimlanmis tarife) / T4 (ocean)
evidence_id:    EV-2026-08-10-313, EV-2026-08-10-314, EV-2026-08-10-322, EV-2026-08-10-324
effective_date: 2026-04-01 (THO) / 2026-01-01 (B/L)
katman:         L1 -> L2 gecisi (FOB -> CIF)
```

**Gerekçe:** TUR 2'nin tek cümlelik en önemli bulgusu, menşe local
charge'larının base okyanus navlununun **alt ucunu aşabildiğiydi**. Bu, "navlun
kaç para?" sorusunun tek başına yanıltıcı olduğu anlamına gelir. RFQ §5.3 bunu
forwarder'a **gerekçesiyle birlikte** söyler ve şu yaptırımı koyar:

> *"If a lane is quoted as a single lump sum without the breakdown in §5.1, we
> will record that lane as **'no quotation received'**."*

**Bunun bir bedeli vardır ve kabul edilmiştir:** kalem dökümü isteyen bir RFQ,
daha yavaş cevaplanır ve bazı forwarder'lar hiç cevaplamayabilir. Hızlı ama
karşılaştırılamaz üç rakam yerine, yavaş ama karşılaştırılabilir üç tablo
tercih edilmiştir.

---

### B-2: Kargo parametreleri `ASSUMPTION`'dır ve bu forwarder'a AÇIKÇA söylenmiştir

```yaml
claim:          "RFQ'daki kargo konfigurasyonu tedarikci teyitli DEGILDIR; teklif bu varsayima kosullanmalidir."
value:          "12'li koli 15,1 kg · paketli sise 1,26 kg / 0,00223-0,00239 m3 · std palet 720 sise / 927 kg / 1.480 mm"
unit:           karisik
status:         ASSUMPTION (koli formati) + ESTIMATE (agirlik/hacim) + FACT (palet spec)
tier:           —
evidence_id:    EV-2026-08-09-306, EV-2026-08-09-307, EV-2026-08-09-308, EV-2026-08-09-320, EV-2026-08-09-321, EV-2026-08-09-310
katman:         —
```

**Varsayım gerekçesi:** Parametresiz kotasyon istenemez. Ama parametre
uydurulup **sanki kesinmiş gibi** verilirse, gelen teklif sahte bir kesinlik
kazanır. RFQ §2 bu yüzden şunu yazar:

> *"We would rather see a conditional quotation than an unconditional one that
> silently breaks later."*

**Bu turun en önemli tasarım kararı budur:** teklifin **hangi varsayıma bağlı
olduğu**, response sheet §A'da (8 zorunlu alan: `case weight`, `pallet weight`,
`number of pallets` dâhil) ve §A9'da (*"is your quotation conditional on
A1–A8?"*) **ayrı bir alan** olarak kaydedilir. Tedarikçi gerçek konfigürasyonu
verdiğinde, hangi tekliflerin yeniden alınması gerektiği **belirsiz kalmaz**.
→ `T-822`

**Şişe formu duyarlılığı hatırlatması:** Burgundy formu şişe, paketli hacmi
0,0036 m³'e çıkarır → **kapasite %38 düşer**. Navlun değişmez; **böleceğimiz
şişe sayısı** değişir.

---

### B-3: 12 lane × 3 mod = 32 kombinasyon; 15'i zorunlu

```yaml
claim:          "RFQ, 12 lane icin 32 rota x konteyner tipi kombinasyonu fiyatlatir; Block A'nin 15'i zorunludur."
value:          "Block A 5 lane x 3 mod = 15 · Block B 4 lane x 2 mod = 8 · Block C 3 lane x 3 mod = 9"
unit:           kombinasyon
status:         —  (tasarim karari)
tier:           —
evidence_id:    —
```

**Gerekçe:** Kapsam bilinçli olarak **kademelendirilmiştir**. Tek seferde 45
kombinasyon istemek (5 öncelikli menşe × 3 varış × 3 mod) cevap oranını
düşürürdü. Block A (öncelikli menşe → İstanbul) zorunlu, Block B (ES/IT →
İzmir/Mersin) yüksek değerli, Block C (2. öncelik menşe) opsiyoneldir.

**İtalya özel notu:** İtalya `EV-2026-08-10-304`'te **dört limanda da 0
offerings** ile UNKNOWN'dır ve öncelikli menşe olmasına rağmen hiçbir turda
fiyatlanamamıştır. RFQ §4 bu yüzden şunu ister: *"if you cannot serve a lane,
write 'not served' rather than omitting the row."* **Boş satır belirsizdir;
'not served' bilgidir** — ve İtalya'nın gerçekten servis edilmediğini
öğrenmek, `T-312`'yi kapatır.

---

### B-4: RFQ, üç `ASSUMPTION`/`CONFLICT` kaydını doğrudan hedefler

| Açık kayıt | RFQ alanı | Kapanırsa ne olur |
|---|---|---|
| `çekici + şasi darası 13–16 t` — **ASSUMPTION, kanıt YOK** | §7 D1–D2 | 40HC kargo tavanı `ESTIMATE`'ten çıkar; `40HC vs 2×20DV` kararı sağlamlaşır |
| `C-301` — 20DV'ye 9 mu 10 mu palet | EK-1 A7 | Kapasite bandı daralır; şişe başı maliyet bandı daralır |
| `C-313` — armatör THD'si ↔ terminal kapı-çıkış çift sayımı | §5.1 B7 + B8 itemisation | 278–414 USD'lik bir çift sayım riski çözülür |

**Gerekçe:** Bunların hiçbiri "navlun" değildir, ama üçü de şişe başı maliyeti
navlunla **aynı mertebede** etkiler. RFQ yalnızca fiyat sormak için değil,
**açık kayıtları kapatmak için** tasarlanmıştır.

---

### B-5: `T-913` Ayak A — cevap iki parçalıdır

```yaml
claim:          "Ayni kaynaktan yeniden OKUMA dis temas degildir; T-304'un istedigi BAGLAYICI YAZILI KOTASYON dis temastir. Ikisi ayni is DEGILDIR."
status:         ESTIMATE   # hukuki tespit degil, TUR 2'deki erisim biciminin degerlendirmesi
evidence_id:    —
```

**Gerekçe:** TUR 2'de 10 LCL kotasyonu **hiçbir mesaj gönderilmeden** elde
edilmiştir; işlem bir okumadır. Ama o okuma yalnızca **LCL bacağını** ve
yalnızca **base ocean freight** kalemini tazeler. `C-311` (FCL), `T-312`
(origin charges), çekici darası ve sigorta **yeniden okumayla kapanmaz.**

**Riskli nokta:** `P-3b-DATED` §B-4 damganın geri alınabilir olduğunu söylüyor.
Yeniden okuma yapılıp damga **topluca** kaldırılırsa, FCL hâlâ `UNKNOWN` iken
çıktı "taze" görünür — bu, `P-3b`'nin yasakladığı şeyin daha sinsi biçimidir:
**bayat veriyle değil, eksik veriyle sessizce koşmak.** → `T-823`

**Bu turda yeniden okuma YAPILMAMIŞTIR** (görev tanımı gereği) ve
`veri-tazeligi.md` ile `index.csv` dokunma listesindedir.

---

### B-6: Hedef listesi — 5 forwarder, 3 doğrulanmış doğrudan kanal

```yaml
claim:          "5 forwarder hedefi belirlendi; 3'unde dogrudan e-posta dogrulandi, 1'i yalnizca web formu, 1'i NEEDS_CONTACT."
value:          "F-1 Hillebrand Gori (form) · F-2 Arkas (e-posta) · F-3 Sertrans (e-posta) · F-4 Flexport (e-posta) · F-5 Mars Logistics (NEEDS_CONTACT)"
status:         FACT (iletisim bilgisi, kurumsal sayfadan okundu) / UNKNOWN (F-1 dogrudan e-posta, F-5 tumu)
tier:           T4 (kurumsal kaynak)
evidence_id:    —   # index.csv bu turda DOKUNMA listesinde; kart acilmadi -> T-821
```

**Gerekçe — çeşitlilik bilinçlidir:** liste üç tip forwarder içerir:
**şarap ihtisas** (F-1), **Türk forwarder** (F-2, F-3, F-5 — varış tarafı,
antrepo ve iç nakliye bilgisi güçlü), **dijital/global** (F-4 — TUR 2
kotasyonlarının kaynağı, uzak menşelerde fiyat verebilen tek kanal).
Aynı tipten 5 firma seçmek, **aynı yanlılığı 5 kez satın almak** olurdu.

**Uydurulmayanlar:** F-1'in doğrudan e-postası (İstanbul ofis sayfası
2026-08-10'da HTTP 404) ve F-5'in tüm iletişim bilgileri (site HTTP 403)
**bulunamadı ve tahmin edilmedi.** `info@…` kalıbı türetmek bu repoda veri
uydurmakla aynı şeydir.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | **FCL base ocean freight** (tüm rotalar) | Kamuya açık kotasyon yok (14/14 lane); bu turda yeni tarama **yasaktı** | **CRITICAL** | RFQ §5.1 B1 — gönderim izni (`T-821`) |
| 2 | İspanya dışı **6 menşenin origin charge'ları** | Taşıyıcı local tarifeleri taranmadı | HIGH | RFQ §5.2 (yayımlanmış tarife talebi) |
| 3 | **İtalya** — LCL ve FCL, her ikisi | 4 limanda 0 offerings | HIGH | RFQ §4 Block A3 |
| 4 | **Çekici + şasi darası** | Nakliyeciden alınmalı | HIGH | RFQ §7 D1 |
| 5 | **Thermal liner birim maliyeti** | Kamuya açık fiyat yok | HIGH | RFQ §9 E3 |
| 6 | **Sigorta primi** (kırılma + termal teminatlı, gerçek kotasyon) | Sigortacıya sorulmadı | HIGH | RFQ §9 E1 |
| 7 | **Beklenen kırılma / fire oranı (%)** | RFQ **çözmez** — forwarder kendi hasar istatistiğinde yanlıdır | HIGH | Sigortacı hasar geçmişi veya pilot sevkiyat |
| 8 | **Bandrolleme** birim maliyeti / kapasitesi | Forwarder alanı değil | HIGH | `T-314` — antrepo/bandrol operatörü |
| 9 | F-1 doğrudan e-posta, F-5 tüm iletişim | Sayfalar 404 / 403 döndü | MEDIUM | Alternatif kurumsal kanal araması |
| 10 | Ruhsat/analiz **bekleme gün sayısı** | Benim alanım değil | **CRITICAL** | `T-301` — `mevzuat-ruhsat-uzmani` |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

Bu turda **yeni çelişki açılmadı** (yeni veri toplanmadı). Mevcut çelişkilerin
RFQ'daki karşılığı:

| conflict_id | Kaynak A | Kaynak B | Durum | RFQ'da nerede test edilecek |
|---|---|---|---|---|
| `C-311` | Marketplace "from" 295–650 USD | T5 blog 1.200–2.500 EUR | **OPEN** | §5.1 B1 (base) + §5.3 (all-in reddi) |
| `C-301` | 20DV'ye 9 palet | 20DV'ye 10 palet | **OPEN** | EK-1 A7 |
| `C-312` | Ardiye free time 0 gün (SafiPort) | 6. günden itibaren (müşavirlik kaynağı) | **OPEN** | §10.3 |
| `C-313` | Armatör THD 165–298 USD | Terminal kapı-çıkış 113–116 USD | **OPEN** | §5.1 B7 + B8 itemisation |

`99-ops/celiskiler.md` bu turda **dokunma listesindedir**; yukarıdaki tablo
yalnızca izlenebilirlik içindir.

---

## 5. MODEL GİRDİLERİ

**Bu turda `80-model/inputs/lojistik.yaml`'a giren YENİ sayı YOKTUR.**
`80-model/` dokunma listesindedir ve zaten bu turda üretilmiş yeni bir ölçüm
yoktur. RFQ cevapları geldiğinde hangi alanın dolacağı
`forwarder-response-sheet.md` "EK: CEVAP GELDİĞİNDE NE YAPILACAK" bölümünde
alan alan tanımlıdır.

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|--------------|------|-------|-------|--------|-------------|
| — | — | *(bu turda değişiklik yok)* | — | — | — |

---

## 6. ÇAPRAZ İPUÇLARI

Ayrıntı: `99-ops/_parts/capraz-ipuclari-navlun-lojistik-uzmani-tur325.md`

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `global-sourcing-kasifi` | Forwarder RFQ'su ile tedarikçi RFQ'su **aynı 5 fiziksel alanı** sorar; eşzamanlı gönderim çapraz doğrulama sağlar | Sıra yanlışsa aynı teklif iki kez istenir |
| `gumruk-vergi-uzmani` | Teklifler **FOB/FCA** bazlı istendi; tedarikçiden CIF gelirse **çift sayım** riski | Navlun hem gider hem CIF bileşeni sayılamaz |
| `mevzuat-ruhsat-uzmani` | RFQ §10.4, 15/30/60 gün bekleme maliyetini soruyor — **gün sayısı sende** (`T-301`) | 30+ gün çıkarsa FCL önerisi tersine döner |
| `finans-fizibilite` | Üç teklif **ortalanmamalı**; fark, duyarlılık bandının ilk kanıtlı dayanağıdır | TUR 2'de aynı port pair'de %31 ve %110 fark ölçüldü |
| `yatirim-komitesi-baskani` | Doğrudan kanal sayısı 3, kapanma koşulu 3 → **hata payı sıfır** | 5 hedefin hepsine gönderilmeli |
| `seytanin-avukati` | §5.3'te forwarder'a **kendi kanıtımızı** gösteriyoruz — çapa etkisi yaratabilir mi? | Bilinçli tasarım kararı, saldırıya açık |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| **T-821** | `yatirim-komitesi-baskani` | RFQ paketi hazır; `T-304`'ün kapanma koşulu artık **gönderim izni** | HIGH | **OPEN** |
| **T-822** | `global-sourcing-kasifi` | Forwarder teklifleri **bizim kargo varsayımımıza bağlı**; tedarikçi konfigürasyonu gelince yeniden doğrulanmalı | HIGH | **OPEN** |
| **T-823** | `yatirim-komitesi-baskani` | `T-913` Ayak A: yeniden **okuma** ≠ **bağlayıcı kotasyon**; `P-3b-DATED` damgası bu ayrım yapılmadan kaldırılamaz | MEDIUM | **OPEN** |

**Kapanan ticket: YOK.** `T-304` `OPEN`/`CRITICAL`, `G2-L` `BLOCKED` kalmıştır.
Bu turda hiçbir ticket'ın statüsü tek taraflı değiştirilmemiştir.

---

## 8. TAZELİK

Bu turda **yeni kanıt kartı açılmamıştır** (`10-evidence/index.csv` dokunma
listesinde). Mevcut tazelik takvimi değişmemiştir:

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| `EV-2026-08-10-301, -302, -303, -305 … -311` (10 LCL kotasyonu) | **6d** | **2026-08-17** ⚠ |
| `EV-2026-08-10-304`, `-312`, `-322`, `-323`, `-324`, `-329`, `-330`, `-331` | 14d | 2026-08-25 |
| `EV-2026-08-09-330`, `-331`, `-333` | 14d | 2026-08-24 |
| `EV-2026-08-10-313 … -319`, `-325 … -328`, `-332` | 90d | 2026-11-09 |

**RFQ'nun tazelik tasarımı:** §8, forwarder'dan **geçerlilik tarihi** ve
*"validity 14 günden kısaysa açıkça söyleyin"* talebi içerir. Gelen her teklifin
`ttl`'i **teklifin kendi validity'sine eşit** alınacaktır — TUR 2'de LCL
kartlarında yapıldığı gibi. Ayrıca §8, BAF/ETS'in geçerlilik süresi **içinde**
değişip değişmediğini sorar: değişiyorsa teklif aslında sabit değildir ve
`ttl` daha da kısadır.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Forwarder'ların bu formatta cevap vermemesi.** RFQ'nun tüm değeri, 20 kalemin
ayrı ayrı doldurulacağı varsayımına dayanır. Üç forwarder da "ekteki tarifemize
bakın, all-in şu kadar" derse, elimizde kalan şey `T-304` §5'in *"tek all-in
rakam kabul edilmez"* kuralı gereğince **"kotasyon alınamadı"** kaydıdır — yani
üç ay sonra bugünkü noktadayız, ama artık *"forwarder'lar da veremiyor"*
bilgisiyle. Bu bir bilgi kazancıdır ama `G2-L`'yi **açmaz**.

İkinci çürütücü: bu paketin **hiç gönderilmemesi**. Gönderilmeyen bir RFQ,
`T-304` için sıfır değer üretir. Bu turun çıktısı bir **opsiyondur**, bir
sonuç değil.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**Kargo konfigürasyonu (B-2).** Koli formatı `UNKNOWN`, şişe boyutları
`UNKNOWN`, palet/konteyner sayısı `CONFLICT`. Forwarder'a somut sayı verdim
çünkü vermeden fiyat alınamaz — ama bu sayılar **tedarikçi tarafından
doğrulanmadı**. Burgundy formu bir şişe kapasiteyi **%38** düşürür; bu tek
başına şişe başı navlunu ~1,6 katına çıkarır ve **hiçbir forwarder pazarlığı
bu farkı telafi etmez.**

Bu kırılganlığı gizlemedim: RFQ §2 forwarder'a varsayım olduğunu söylüyor,
response sheet §A9 teklifin buna bağlı olup olmadığını **ayrı alan** olarak
soruyor, `T-822` bağımlılığı kayda geçiriyor. Ama **kırılganlığı yönetmek onu
ortadan kaldırmaz.**

İkinci kırılgan varsayım: **çekici + şasi darası 13–16 t**. Kanıt yok, ve 40HC
kargo tavanını doğrudan belirliyor.

### 9.3 Hangi kaynağıma en az güveniyorum?

Bu turda **veri kaynağı kullanmadım** — kullandığım tek "kaynak" sınıfı,
forwarder'ların **kendi kurumsal iletişim sayfalarıdır** (T4). İkisi
(Hillebrand Gori İstanbul ofisi, Mars Logistics iletişim sayfası) erişilemedi
(404 / 403) ve **tahmin üretilmedi**.

Metin içinde forwarder'a aktarılan sayılar arasında en az güvendiğim
`≈USD 300` base ocean alt ucudur (`C-311`'in bir tarafı, marketplace "from"
fiyatı, tarihsiz). §5.3'te bu sayı **"indicative"** olarak sunulmuştur, iddia
olarak değil — ama yine de forwarder'a bir çapa vermiş oluyorum (bkz. İ-3256).

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

Doğrudan hiçbiri — çünkü bu tur **sayı üretmedi.** Dolaylı olarak:

| Yanlışlık | Değişen karar |
|---|---|
| RFQ formatı cevaplanamaz çıkarsa | `G2-L` masabaşıyla da forwarder'la da açılamaz → TUR 6'da seçenek kümesi **(b) gate kapalıyken karar** veya **(c) HOLD**'a daralır |
| Gelen FCL fiyatı bandın **üst ucunda** (1.200 USD) çıkarsa | 5.000 şişelik pilotta FCL, LCL ile eşitlenir → `lcl-vs-fcl-pilot.md` §6'nın FCL önerisi **yalnızca kırılganlık argümanına** dayanır |
| Gelen FCL fiyatı bandın **alt ucunda** (300 USD) çıkarsa | 25.000+ şişede FCL, LCL'e karşı net kazanır; `EV-2026-08-10-330` kırılma noktası **2.200 şişeye** doğru kayar |
| Çekici darası 16 t'nin **üstünde** çıkarsa | 40HC kargo tavanı düşer → `40HC ≥19.000 şişe` önerisi zayıflar, `2×20DV` güçlenir |

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| Kim | Ne | Süre |
|---|---|---|
| **Kurucu / başkan** | `forwarder-rfq.md` preview + gönderim onayı + `<PLACEHOLDER>` doldurma | 1 gün |
| **Kurucu** | F-2, F-3, F-4'e e-posta + EK-1; F-1'e web formu; F-5 için kanal tespiti | 1 gün |
| **Forwarder'lar** | Kalem dökümlü yazılı kotasyon | **10 iş günü** (48 saatlik deadline "all-in" cevabını davet eder) |
| `navlun-lojistik-uzmani` | Gelen teklifleri kanıt kartına çevirme + `lojistik.yaml` güncelleme + `T-304` cevap bölümü | 1 gün — **`index.csv` yazma izni gerekir** |
| **Toplam** | | **~12–14 iş günü** |

> ⚠ **Zamanlama uyarısı:** Bu takvim, LCL kartlarının STALE olduğu
> **2026-08-17**'yi **aşar**. Yani RFQ bugün gönderilse bile, cevaplar
> geldiğinde model bir süre `STALE_LOGISTICS` damgasıyla koşacaktır
> (`P-3b-DATED` §B-2). Bu kaçınılmazdır ve **gizlenmemelidir**.

---

## EK — BU TURDA YAPILMAYANLAR *(kayıt için)*

| Yapılmadı | Neden |
|---|---|
| Forwarder'a e-posta / form / mesaj | **Görev tanımı: gönderim yasak.** Kurucu preview + açık onay bekliyor |
| Yeni navlun araştırması / yeni lane taraması | Görev tanımı: paket hazırlığı yeterli |
| LCL kotasyonlarının yeniden çekilmesi | `index.csv` ve `veri-tazeligi.md` dokunma listesinde → `T-823` |
| Yeni kanıt kartı | `10-evidence/index.csv` dokunma listesinde → `T-821` |
| `80-model/inputs/lojistik.yaml` güncellemesi | Dokunma listesinde; ayrıca yeni ölçüm yok |
| Vergi / ruhsat / kanal marjı / tedarikçi fiyatı hakkında sonuç | Kapsam dışı — ipuçları `_parts/capraz-ipuclari-…-tur325.md`'ye bırakıldı |
| `git` komutu | Yasak |
