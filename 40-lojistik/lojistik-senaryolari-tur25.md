# LOJİSTİK SENARYOLARI — LOW / BASE / HIGH (TUR 2.5)

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2.5 — TAZELİK KONTROLÜ + TERS MODEL SENARYO HAZIRLIĞI
tarih:  2026-08-10
durum:  DRAFT
amac:   "Ters (reverse) fiyat modeline sise basi lojistik girdisi saglamak"
kanit:  MEVCUT kanitlar (EV-2026-08-09-3xx + EV-2026-08-10-3xx). YENI KANIT ACILMADI.
```

> ## ⛔ BU DOSYAYI KULLANMADAN ÖNCE — 8 KURAL
>
> 1. **Bu turda yeni navlun araştırması yapılmadı.** Bütün sayılar TUR 1 / TUR 2
>    kanıtlarından **türetilmiştir**. Yeni `evidence_id` açılmamıştır.
> 2. **LOW/BASE/HIGH keyfi değildir.** Her kalemin üç değeri de §2'de **kalem
>    kalem kaynağıyla** tanımlıdır. Kaynağı yazılmayan senaryo geçersizdir.
> 3. **FCL'in BASE'i YOKTUR.** `M-6` gereği FCL bandının ortalaması alınamaz.
>    FCL yalnızca **iki köşe** (LOW / HIGH) olarak taşınır. `C-311` açıktır.
> 4. **Para birimleri toplanmamıştır** (`M-5`). USD / EUR / TRY ayrı sütunlardır.
>    `makro.yaml → fx` hâlâ `null`.
> 5. **LCL sayıları gerçek kotasyona dayanır ve 2026-08-16'da ölür.** Bkz. §1.
> 6. Bu dosya **L1 (FOB) → L3 (pre-tax landed)** arası lojistik kalemlerini
>    kapsar. Sigorta, bandrolleme operasyonu, vergiler ve kanal dağıtımı
>    **dahil değildir**.
> 7. **İtalya her senaryoda `UNKNOWN`'dır** ve doldurulmamıştır.
> 8. Bu dosya bir **navlun kotasyonu değildir**; kotasyonlardan türetilmiş bir
>    **senaryo çerçevesidir**. Gerçek RFQ hâlâ `T-304` altında beklemektedir.

---

## 1. TAZELİK KONTROLÜ — LCL KANIT SETİ ÖLÜM SAATİ

### 1.1 Bugünün durumu (2026-08-10)

```
access_date  = 2026-08-10
ttl          = 6d
son gecerli  = 2026-08-16   (kotasyonun KENDI gecerlilik tarihi de 2026-08-16)
STALE        = 2026-08-17 00:00 itibariyle
bugun        = 2026-08-10  ->  GECERLI, 0 gun yaslanmis, 6 gun omru kalmis
```

`99-ops/veri-tazeligi.md` §KURALLAR-2: *"`access_date + ttl < bugün` olan kanıt
STALE'dir."* → `2026-08-10 + 6d = 2026-08-16`. 2026-08-16 tarihinde koşul
sağlanmaz (eşit, küçük değil) → **son geçerli gün 2026-08-16**, STALE
**2026-08-17**.

**İki kontrol de aynı tarihi veriyor** (bkz. `veri-tazeligi.md` §ÖZEL KONTROL):
- `ttl` kontrolü → 2026-08-16 son gün.
- Kaynağın kendi geçerlilik tarihi (Flexport quote validity) → 2026-08-16.

Bu bir tesadüf değildir: `ttl`, kotasyonun kendi geçerlilik süresine eşit
seçilmiştir. **Yani bu kanıtlar `ttl` dolduğunda sadece "eskimez", aynı zamanda
kaynağın kendisi tarafından geri çekilmiş olur.**

### 1.2 Hangi kartlar — tam liste

`ttl: 6d`, `access_date: 2026-08-10`, **son geçerli gün 2026-08-16**,
**STALE 2026-08-17**:

| # | evidence_id | rota | ters modeldeki rolü |
|---|---|---|---|
| 1 | `EV-2026-08-10-301` | Valencia (ES) → İstanbul | **BASE rota** — ters modelin ana lojistik girdisi |
| 2 | `EV-2026-08-10-302` | Barcelona (ES) → İstanbul | BASE rota alternatifi + HIGH ucu (%31 teklif farkı) |
| 3 | `EV-2026-08-10-303` | Lizbon (PT) → İstanbul | rota karşılaştırması |
| 4 | `EV-2026-08-10-305` | Marsilya (FR) → İstanbul | rota karşılaştırması |
| 5 | `EV-2026-08-10-306` | San Antonio (CL) → İstanbul | rota karşılaştırması |
| 6 | `EV-2026-08-10-307` | Cape Town (ZA) → İstanbul | rota karşılaştırması (en pahalı) |
| 7 | `EV-2026-08-10-308` | Oakland (US-CA) → İstanbul | **benchmark ürün rotası** |
| 8 | `EV-2026-08-10-309` | Los Angeles (US-CA) → İstanbul | benchmark ürün rotası |
| 9 | `EV-2026-08-10-310` | Buenos Aires (AR) → İstanbul | rota karşılaştırması |
| 10 | `EV-2026-08-10-311` | Melbourne (AU) → İstanbul | rota karşılaştırması |

> ### ⚠ SAYIM DÜZELTMESİ — "11 kart" DEĞİL, **10 kart**
>
> Hem `40-lojistik/rota-maliyet-matrisi.md` §8 hem `T-304` §4 bu seti
> **"`EV-2026-08-10-301 … -311` = 11 kart"** olarak tarif eder. **Bu yanlıştır.**
> `10-evidence/index.csv` kontrolünde:
>
> - `EV-2026-08-10-304` (İtalya, **status `UNKNOWN`**) → `ttl: 14d`, 6d **değil**.
>   İçinde navlun rakamı yoktur; "kotasyon yok" bulgusudur.
> - Aralıkta **6d ttl'li 10 kart** vardır.
>
> Kanıt kartları immutable'dır ve `index.csv` bu turda **dokunulmaz** listededir;
> düzeltme yalnızca burada ve `veri-tazeligi.md`'de kayda geçirilmiştir →
> **`T-801`**. Modele etkisi yoktur (–304 zaten `UNKNOWN`), ama **kanıt sayımı
> yanlış kalırsa yeniden doğrulamada bir kart fazla aranır.**

### 1.3 Diğer lojistik kanıtlarının tazelik takvimi

| Kanıt sınıfı | evidence_id | ttl | son geçerli gün | STALE |
|---|---|---|---|---|
| **LCL kotasyonları (10 kart)** | `-301,-302,-303,-305,-306,-307,-308,-309,-310,-311` | **6d** | **2026-08-16** | **2026-08-17** ⚠ |
| FCL kotasyon yokluğu | `EV-2026-08-10-312` | 14d | 2026-08-24 | 2026-08-25 |
| İtalya "0 offerings" | `EV-2026-08-10-304` | 14d | 2026-08-24 | 2026-08-25 |
| FCL dolaylı göstergeler | `-322`, `-323`, `-324`, `-331` | 14d | 2026-08-24 | 2026-08-25 |
| Türetilmiş maliyet / kırılma | `-329`, `-330` | 14d | 2026-08-24 | 2026-08-25 |
| TUR 1 navlun göstergeleri | `EV-2026-08-09-330`, `-331`, `-333` | 14d | 2026-08-23 | 2026-08-24 |
| TUR 1 LCL yapısı | `EV-2026-08-09-324` | 30d | 2026-09-08 | 2026-09-09 |
| Taşıyıcı/terminal tarifeleri | `-313 … -319`, `-325`, `-326`, `-327`, `-328`, `-332` | 90d | 2026-11-08 | 2026-11-09 |
| DFDS 2025 tarifesi | `EV-2026-08-10-320` | — | **zaten eski** | yalnızca **oran** çapası |
| DFDS 2018 | `EV-2026-08-10-321` | 0d | — | **SUPERSEDED** |

### 1.4 STALE olduktan sonra ne olur — bağlayıcı kural

> **STALE bir kanıt otomatik olarak geçerli `FACT` gibi KULLANILAMAZ.**

`2026-08-17` ve sonrasında:

| Tarih | LCL kartlarının statüsü | Bu dosyadaki hangi bölüm kullanılamaz |
|---|---|---|
| **≤ 2026-08-16** | `FACT`, confidence `MEDIUM` | — hepsi kullanılabilir |
| **≥ 2026-08-17** | `FACT` **düşer** → en iyi ihtimalle `ESTIMATE / LOW / tarihsel çapa` | §3 (rota × senaryo okyanus tablosu), §4 (hacim tabloları LCL satırları), §5.1 (üst sınır çapası), §6 (ters model girdisi) |

Sonuç: **2026-08-17 itibarıyla bu dosyadaki her LCL sayısı `ESTIMATE`'e düşer**
ve ters modelin lojistik girdisi tek gerçek dayanağını kaybeder — çünkü FCL
zaten `UNKNOWN`'dır. O tarihten sonra model çalıştırılacaksa **10 kart yeniden
doğrulanmalı** (yeni kart + `supersedes`), yoksa lojistik girdisi bütünüyle
`ESTIMATE / LOW` olarak etiketlenmelidir. → `T-802`

**Türetilmiş kartlar da düşer:** `EV-2026-08-10-329` ve `-330` (şişe başı
maliyet ve LCL/FCL kırılma noktası) girdilerini bu 10 karttan alır. Kendi
`ttl`'leri 14d olsa bile, **kaynak kartları STALE olduğunda türev de STALE
sayılmalıdır.** (Kendi `ttl`'i daha uzun olan bir türev, kaynağından daha taze
olamaz.)

---

## 2. SENARYO TANIMI — LOW / BASE / HIGH NEREDEN GELİYOR

**Genel kural:** LOW/BASE/HIGH bir olasılık dağılımı değil, **kanıtlanmış
bandın uçları + gerekçeli orta nokta**dır. Aşağıdaki tablonun her satırı
"bu üç sayı nereden geldi" sorusunu tek başına yanıtlar.

### 2.1 Fiziksel parametreler

| Kalem | LOW | BASE | HIGH | Kaynak / gerekçe |
|---|---|---|---|---|
| Şişe hacmi (paketli) m³ | 0,00223 | 0,00231 | 0,00239 | `EV-2026-08-09-307`. LOW = 12'li koli, HIGH = 6'lı koli, BASE = orta. **Koli formatı `UNKNOWN` (`T-302`)** → bu belirsizlik senaryoya dahil edildi |
| 20DV paletsiz kapasite (şişe) | 13.700 | 12.750 | 11.800 | `EV-2026-08-09-320` bandının uçları; BASE = orta |
| 40HC paletsiz kapasite (şişe) | 21.500 | 20.300 | 19.100 | `EV-2026-08-09-321` (karayolu 44 t ile sınırlı) |
| Sevkiyat/yıl | 5.000→1 · 25.000→2 · 50.000→3 · 100.000→5 | aynı | aynı | `40-lojistik/lcl-vs-fcl-pilot.md` §7 (TUR 2'de yayımlanan kadans) |

> **Not:** TUR 2 matrisi şişe/CBM için sabit **449** kullanıyordu. Burada bunun
> yerine **şişe hacmi bandı** (0,00223–0,00239) kullanıldı; bu, koli formatı
> belirsizliğini senaryonun içine taşır ve bandı bilinçli olarak genişletir.
> Bu bir **düzeltme değil, daha muhafazakâr bir modelleme** tercihidir ve
> TUR 2 sayılarıyla küçük farklar yaratır (LOW ucu aynı, HIGH ucu ~%7 yukarı).

### 2.2 Okyanus navlunu

| Mod | LOW | BASE | HIGH | Kaynak / gerekçe |
|---|---|---|---|---|
| **LCL (9 rota)** | kotasyonun alt ucu | kotasyonun **kendi bandının ortası** | kotasyonun üst ucu / **ikinci teklif** | `EV-2026-08-10-301…-311` (T4, Flexport, tarihli, 2026-08-16 geçerli). HIGH'da aynı port pair'de ikinci teklif varsa (ES-BCN, CL, FR, US-LAX, AU) **pahalı teklif** kullanıldı — `EV-...-302`'nin "%31 fark" bulgusu |
| **FCL 20DV (yalnızca İspanya)** | **300 USD** | **YOK — `UNKNOWN`** | **1.200 USD** | `C-311` **AÇIK**: marketplace "from" 295–650 USD vs T5 blog 1.200–2.500 EUR → **4–5 kat fark, taraf seçilmedi**. `M-6`: bandın ortalaması alınamaz |
| **FCL 40HC (yalnızca İspanya)** | 411 USD | **YOK** | 1.776 USD | 20DV bandı × ampirik oran 1,37–1,48 (`EV-2026-08-10-328`) |
| **FCL — diğer 8 rota** | `UNKNOWN` | `UNKNOWN` | `UNKNOWN` | `EV-2026-08-10-312`: 14 lane'in 14'ünde kotasyon yok |
| BAF/CAF/ETS (FCL) | +%15 | — | +%25 | `EV-2026-08-10-324` (T5, LOW) + DFDS "BAF/ETS hariç" teyidi (`-320`) |

### 2.3 Menşe local charge'ları (EUR — yalnızca İspanya, FCL'de)

| LOW | BASE | HIGH | Kaynak / gerekçe |
|---|---|---|---|
| **349 EUR** | **464 EUR** | **554 EUR** | `EV-2026-08-10-313`, `-314` (T3, Hapag-Lloyd resmî tarifesi, HIGH confidence) |

- **LOW = 349** → yalnızca zorunlu iki kalem: THO 287 + B/L (EDI) 62.
- **BASE = 464** → LOW + **Food Quality Container 115 EUR**. Gerekçe:
  `EV-2026-08-10-314` bu kalemi *"gıda sevkiyatları için… şarapta geçerli
  olabilir"* diye işaretliyor. **Şarap gıdadır**; muhafazakâr BASE bunu içerir.
- **HIGH = 554** → BASE + VGM manuel 50 + equipment assignment 40 (+ manuel SI
  farkı). Yani "her şey manuel/opsiyonlu" köşesi.
- **Konteyner boyundan bağımsızdır** → 40HC'de şişe başına ~1,6 kat seyrelir.
- **LCL'de EUR bacağı sıfırdır** — menşe locali CBM fiyatına gömülüdür.
- **İspanya dışındaki 8 menşe için `UNKNOWN`** (`T-312`).

### 2.4 Varış (USD)

| Kalem | LOW | BASE | HIGH | Kaynak / gerekçe |
|---|---|---|---|---|
| THD 20DV | 165 (İzmir) | **192 (İstanbul)** | 261 (Mersin) | `EV-2026-08-10-315` (T3). **BASE = İstanbul**, çünkü bütün LCL kotasyonları `TRIST` (İstanbul) varışlıdır → rota ile tutarlı tek seçim |
| THD 40HC | 165 | 192 | 298 (Mersin) | aynı; İzmir/İstanbul/Gemlik'te 20ft/40ft ayrımı **yok** |
| Drop-off | 50 | 50 | 50 | `EV-2026-08-10-316` (T3), sabit |
| Terminal ardiye **5 gün** 20DV | 90 | 185 | 195 | `EV-2026-08-10-318` (Kumport 18/gün, **LOW confidence**) → LOW; `-319` (Beldeport 37) → BASE; `-317` (SafiPort 39) → HIGH |
| Terminal ardiye **5 gün** 40HC | 145 | 290 | 300 | aynı kaynaklar, 40ft kademesi |
| Devanning (paletsiz) 20DV | 257 | 275 | 405 | `-319` (Beldeport) / `-317` (SafiPort) / `-317` **manuel** boşaltım |
| Devanning (paletsiz) 40HC | 332 | 365 | 475 | aynı |
| LCL varış sabit masrafı | 200 | 350 | 500 | `EV-2026-08-09-324` bandı, BASE = orta |
| LCL dokümantasyon | 50 | 75 | 100 | `EV-2026-08-09-324` bandı, BASE = orta |
| **LCL CFS (iki taraf), USD/CBM** | **0** | **30** | **80** | `EV-2026-08-09-324` (30–80 USD/CBM). **LOW = 0**, TUR 2'nin "base'e dahil varsayıldı" köşesini korumak için. **BASE ve HIGH'da açıkça eklendi**, çünkü `EV-2026-08-10-301` *"excluded: origin local charges, CFS destination"* diyor |

> ⚠ **TUR 2'DEN BİLİNÇLİ SAPMA — LCL CFS.**
> TUR 2'nin `lcl-vs-fcl-pilot.md` §2.1 tablosu **LOW ucunda CFS'i sıfır** kabul
> etmişti. Bu tur LOW'u aynen korudu ama **BASE ve HIGH'a CFS'i ekledi.** Sebep:
> kotasyonun kendi metni CFS'i **hariç** sayıyor. Etkisi büyüktür: 30–80 USD/CBM,
> 123–133 USD/CBM'lik okyanus navlununun **%25–65'i** kadardır.
> **LCL'in en büyük tek belirsizliği artık okyanus navlunu değil, CFS'in dahil
> olup olmadığıdır.** (`ASSUMPTION`, gerekçe: kotasyon metni.)

### 2.5 Türkiye içi (TRY)

| Kalem | LOW | BASE | HIGH | Kaynak / gerekçe |
|---|---|---|---|---|
| Ordino (sevkiyat/B/L başına) | 2.000 | 3.500 | 5.000 | `EV-2026-08-10-325` bandı, BASE = orta |
| Müşavirlik (beyanname başına) | 6.020 | 6.020 | 6.020 | `EV-2026-08-09-342` (T3, 2026 asgari): ANT-1 1.350 + İTH-2 4.670 |
| Müşavirlik ek konteyner | 1.350 | 1.350 | 1.350 | İTH-14, aynı beyannamedeki ek konteyner |
| Laboratuvar / ekspertiz (ÖZ-4) | 0 | 940 | 940 | `EV-2026-08-09-342`. BASE'de var: alkollü içkide analiz beklenir |
| X-ray | 0 | 2.000 | 3.000 | `EV-2026-08-10-325` bandı. BASE'de var: alkolde muayene olasılığı yüksek (`EV-2026-08-09-341`) |
| Tam muayene | 0 | 0 | 2.322 (20DV) / 3.249 (40HC) | `EV-2026-08-09-341`. Yalnızca HIGH |
| İç nakliye 20DV (İst. içi) | 10.000 | 12.500 | 15.000 | `EV-2026-08-10-326` bandı |
| İç nakliye 40HC | 12.500 | 15.250 | 18.000 | `EV-2026-08-10-326` bandı |
| İç nakliye LCL (CFS→depo) | 5.000 | 7.500 | 10.000 | `EV-2026-08-10-326`'dan türetildi, **LOW confidence** |

**Beyanname sayısı varsayımı (`ASSUMPTION`):** LOW ve BASE'de bir sevkiyatın
tüm konteynerleri **tek beyannamede** birleşir (6.020 + 1.350 × ek konteyner);
HIGH'da kadans aynı kalır. Gerekçe: İTH-14 ("ek konteyner") kaleminin tarifede
ayrıca var olması, tam da bu birleştirmenin standart pratik olduğunu gösterir.

### 2.6 Senaryolara DAHİL EDİLMEYENLER (bilinçli)

| Kalem | Neden yok |
|---|---|
| **Sigorta** | CIF kıymetine bağlı; prim %0,3–0,6 `ESTIMATE`, gerçek kotasyon `UNKNOWN` (`T-304`). Ayrıca CIF ile alımda **çift sayım riski** |
| **Bandrolleme operasyonu** | Birim maliyet ve kapasite `UNKNOWN` (`T-314`) |
| **Antrepo bekleme (7 günün üstü)** | Süre `T-301`'e bağlı, `UNKNOWN`. Ayrı duyarlılık: §5.3 |
| **Demurrage / detention** | Gecikme günü `UNKNOWN`. Ayrı duyarlılık: §5.4 |
| **Kanala dağıtım, depolama** | `UNKNOWN` |
| **Tüm vergiler** | `gumruk-vergi-uzmani` alanı |
| **Müşavirlik CIF kademesi** | CIF 15.001–225.000 USD için aşan kısmın %0,3'ü (`EV-2026-08-09-342`). **CIF bilinmeden hesaplanamaz** — formül `finans-fizibilite`'ye bırakıldı (§7) |

---

## 3. ROTA × SENARYO — LCL BASE OKYANUS NAVLUNU (USD/ŞİŞE)

> **Hacimden bağımsızdır**, çünkü LCL m³ başına fiyatlanır ve doğrusal
> ölçeklenmiştir (`ASSUMPTION`: 5 CBM kotasyonu 11–239 CBM'e doğrusal uzatıldı).
> **Yalnızca base ocean freight** — CFS, local charge ve varış masrafları hariç.

| Rota | LOW | BASE | HIGH | transit (gün) | aktarma | status | conf. | evidence_id |
|---|---|---|---|---|---|---|---|---|
| **İspanya — Valencia** | **0,275** | **0,296** | **0,318** | 4 | 0 | FACT* | MEDIUM | `EV-2026-08-10-301` |
| İspanya — Barcelona | 0,275 | 0,296 | **0,411** | 4 | 0 | FACT* | MEDIUM | `EV-2026-08-10-302` |
| Portekiz — Lizbon | 0,423 | 0,450 | 0,478 | ~4 ⚠ | 1 | FACT* | MEDIUM | `EV-2026-08-10-303` |
| **İtalya** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | UNKNOWN | — | UNKNOWN | — | `EV-2026-08-10-304` |
| Fransa — Marsilya | 0,637 | 0,671 | 0,724 | 12–15 | 1 | FACT* | MEDIUM | `EV-2026-08-10-305` |
| Şili — San Antonio | 0,433 | 0,460 | 0,663 | 43–49 | 1 | FACT* | MEDIUM | `EV-2026-08-10-306` |
| G. Afrika — Cape Town | 0,767 | 0,806 | 0,846 | 49 | 1 | FACT* | MEDIUM | `EV-2026-08-10-307` |
| California — Oakland | 0,553 | 0,584 | 0,616 | 20 | 2 | FACT* | MEDIUM | `EV-2026-08-10-308` |
| California — Los Angeles | 0,505 | 0,535 | 0,631 | 20–44 | 2 | FACT* | MEDIUM | `EV-2026-08-10-309` |
| Arjantin — Buenos Aires | 0,513 | 0,543 | 0,574 | 25 | 1 | FACT* | MEDIUM | `EV-2026-08-10-310` |
| Avustralya — Melbourne | 0,529 | 0,560 | **1,217** | 36–56 | 1 | FACT* | MEDIUM | `EV-2026-08-10-311` |

`*` **FACT yalnızca 2026-08-16'ya kadar.** 2026-08-17'den itibaren tümü
`ESTIMATE / LOW` (§1.4).

**Türetme:** `USD/şişe = USD/CBM × m³/şişe`, m³/şişe senaryoya göre
0,00223 / 0,00231 / 0,00239.

**HIGH ucundaki iki sıçrama gerçektir, hata değildir:**
- Barcelona 0,296 → 0,411: **aynı port pair'de iki teklif arası %31 fark.**
- Melbourne 0,560 → 1,217: iki teklif arası **%110 fark** (36 gün ucuz,
  56 gün pahalı — ters ilişki, muhtemelen farklı konsolidatörler).
→ Tek kotasyona güvenmemek gerektiğinin ölçülmüş kanıtı.

---

## 4. HACİM × MOD × SENARYO — İSPANYA → İSTANBUL (ŞİŞE BAŞINA)

> En iyi kanıtlanmış rota. **Üç para birimi ayrı** (`M-5`).
> Kapsam: L1→L3 lojistik. Sigorta / bandrol / vergi / antrepo bekleme **hariç**.

### 4.1 — 5.000 ŞİŞE (pilot, 1 sevkiyat)

| Mod | Senaryo | konteyner | **USD/şişe** | **EUR/şişe** | **TRY/şişe** | okyanus durumu |
|---|---|---|---|---|---|---|
| **LCL** | LOW | — (11,2 CBM) | **0,325** | 0 | **2,60** | ✅ gerçek kotasyon |
| **LCL** | **BASE** | — (11,6 CBM) | **0,450** | 0 | **3,99** | ✅ gerçek kotasyon |
| **LCL** | HIGH | — (12,0 CBM) | **0,630** | 0 | **4,99** | ✅ gerçek kotasyon |
| 20DV | LOW | 1 (%36 dolu) | 0,112 *(okyanus hariç)* | 0,070 | 3,60 | ⛔ okyanus UNKNOWN |
| 20DV | BASE | 1 | 0,140 *(okyanus hariç)* | 0,093 | 4,99 | ⛔ **BASE YOK** |
| 20DV | HIGH | 1 | 0,182 *(okyanus hariç)* | 0,111 | 6,46 | ⛔ okyanus UNKNOWN |
| 20DV | **köşe-LOW** (okyanus 300 +%15) | 1 | **0,181** | 0,070 | 3,60 | ESTIMATE / LOW |
| 20DV | **köşe-HIGH** (okyanus 1.200 +%25) | 1 | **0,482** | 0,111 | 6,46 | ESTIMATE / LOW |
| 40HC | köşe-LOW | 1 (%25 dolu) | 0,233 | 0,070 | 4,10 | ESTIMATE / LOW |
| 40HC | köşe-HIGH | 1 | 0,669 | 0,111 | 7,24 | ESTIMATE / LOW |

**Okunuş:** 5.000 şişede LCL ile 20DV FCL arasındaki fark **hâlâ gürültü
seviyesindedir** (TUR 2 sonucu **doğrulandı**): FCL'in USD avantajı (0,18–0,48
vs 0,33–0,63), EUR (0,07–0,11) ve TRY (3,6–6,5 vs 2,6–5,0) dezavantajıyla
nötralize olur. **40HC 5.000 şişede her senaryoda kaybeder** — %25 dolu gider.

### 4.2 — 25.000 ŞİŞE (2 sevkiyat)

| Mod | Senaryo | konteyner | **USD/şişe** | **EUR/şişe** | **TRY/şişe** |
|---|---|---|---|---|---|
| **LCL** | LOW | 2 araç (55,8 CBM) | **0,295** | 0 | **1,04** |
| **LCL** | **BASE** | 2 (57,8 CBM) | **0,399** | 0 | **1,60** |
| **LCL** | HIGH | 3 (59,8 CBM) | **0,558** | 0 | **2,57** |
| 20DV | LOW | 2 | 0,045 *(oky. hariç)* | 0,028 | 1,44 |
| 20DV | BASE | 2 | 0,056 *(oky. hariç)* | 0,037 | 2,00 |
| 20DV | HIGH | **3** | 0,109 *(oky. hariç)* | 0,067 | 3,45 |
| 20DV | **köşe-LOW** | 2 | **0,073** | 0,028 | 1,44 |
| 20DV | **köşe-HIGH** | 3 | **0,289** | 0,067 | 3,45 |
| 40HC | köşe-LOW | 2 (%62 dolu) | 0,093 | 0,028 | 1,64 |
| 40HC | köşe-HIGH | 2 | 0,267 | 0,044 | 2,90 |

> **HIGH'da konteyner sayısının 2→3'e çıkması bir hata değildir:** kapasite
> bandının alt ucunda (11.800 şişe/20DV) 25.000 şişe **iki konteynere sığmaz**.
> Bu, kapasite belirsizliğinin maliyete **basamaklı** (doğrusal değil) yansıdığı
> tek yerdir ve şişe başı TRY'yi **%73** artırır. `T-302` (koli formatı) bunu
> doğrudan etkiler.

### 4.3 — 50.000 ŞİŞE (3 sevkiyat)

| Mod | Senaryo | konteyner | **USD/şişe** | **EUR/şişe** | **TRY/şişe** |
|---|---|---|---|---|---|
| **LCL** | LOW | 4 (111,5 CBM) | **0,290** | 0 | **0,91** |
| **LCL** | **BASE** | 4 (115,5 CBM) | **0,391** | 0 | **1,42** |
| **LCL** | HIGH | 5 (119,5 CBM) | **0,546** | 0 | **2,07** |
| 20DV | köşe-LOW | 4 | **0,073** | 0,028 | 1,31 |
| 20DV | köşe-HIGH | 5 | **0,241** | 0,055 | 2,80 |
| **40HC** | köşe-LOW | 3 | **0,070** | 0,021 | 1,23 |
| **40HC** | köşe-HIGH | 3 | **0,201** | 0,033 | 2,17 |
| 40HC | BASE *(oky. hariç)* | 3 | 0,054 | 0,028 | 1,66 |

### 4.4 — 100.000 ŞİŞE (5 sevkiyat)

| Mod | Senaryo | konteyner | **USD/şişe** | **EUR/şişe** | **TRY/şişe** |
|---|---|---|---|---|---|
| **LCL** | LOW | 8 (223 CBM) | **0,287** | 0 | **0,84** |
| **LCL** | **BASE** | 8 (231 CBM) | **0,387** | 0 | **1,32** |
| **LCL** | HIGH | 9 (239 CBM) | **0,540** | 0 | **1,82** |
| 20DV | köşe-LOW | 8 | 0,073 | 0,028 | 1,24 |
| 20DV | köşe-HIGH | 9 | 0,217 | 0,050 | 2,48 |
| **40HC** | köşe-LOW | 5 | **0,058** | **0,018** | **1,03** |
| **40HC** | köşe-HIGH | 6 | **0,201** | 0,033 | 2,07 |
| 40HC | BASE *(oky. hariç)* | 5 | 0,045 | 0,023 | 1,39 |

### 4.5 Ölçek eğrisi — TUR 2'nin "3–4 kat düşer" iddiası TEST EDİLDİ

| Bacak | 5.000 → 100.000 değişimi | Sonuç |
|---|---|---|
| **LCL USD/şişe** | 0,325→0,287 (LOW) · 0,450→0,387 (BASE) | **yalnızca %12–14 düşer** ❌ |
| **LCL TRY/şişe** | 2,60→0,84 (LOW) · 3,99→1,32 (BASE) | **%67 düşer** ✅ |
| FCL USD/şişe (köşe-LOW) | 0,181→0,058 (40HC) | **%68 düşer** ✅ |
| FCL EUR/şişe | 0,070→0,018 | **%74 düşer** ✅ |
| FCL TRY/şişe | 3,60→1,03 | **%71 düşer** ✅ |

> **DÜZELTME — TUR 2'nin ölçek iddiası MODA BAĞLIDIR.**
> `lcl-vs-fcl-pilot.md` §7'deki *"5.000 → 100.000 arasında şişe başı lojistik
> maliyeti 3–4 kat düşer"* ifadesi **yalnızca FCL için doğrudur.**
> **LCL'de USD bacağı neredeyse hiç ölçek ekonomisi göstermez** (%12–14) —
> çünkü LCL maliyeti neredeyse tamamen değişkendir (m³ başına). LCL'de ölçek
> yalnızca TRY (sabit) bacağını seyreltir.
> Bu, ters modelde önemlidir: **LCL varsayımıyla kurulmuş bir "büyürsek navlun
> ucuzlar" beklentisi yanlıştır.**

---

## 5. FCL'İN UNKNOWN KALDIĞI YERLER VE BUNUNLA NE YAPILABİLİR

### 5.1 LCL, FCL için bir ÜST SINIR çapası olarak kullanılabilir mi?

**Evet — koşullu, `ESTIMATE`, confidence `LOW-MEDIUM`.**

```
İDDİA: Kırılma noktasının (~5.900 şişe/sevkiyat, EV-2026-08-10-330) ÜSTÜNDEKİ
       hacimlerde, LCL'in şişe başı maliyeti FCL'in ÜST SINIRIDIR.

GEREKÇE: Kırılma noktası tanımı gereği, o hacmin üstünde FCL ucuzdur. LCL
         fiyatı GERÇEK kotasyondur; FCL fiyatı UNKNOWN'dır. Dolayısıyla
         gerçek bir sayı, bilinmeyen bir sayıyı YUKARIDAN sınırlar.

DOĞRULAMA (EUR/USD 1,00–1,20 ASSUMPTION ile, 25.000 şişe):
  LCL LOW   0,295 USD          vs  FCL köşe-LOW  0,073 + 0,028 EUR ≈ 0,10  ✔
  LCL HIGH  0,558 USD          vs  FCL köşe-HIGH 0,289 + 0,067 EUR ≈ 0,36  ✔
  → Her iki köşede de LCL > FCL. Üst sınır İDDİASI TUTUYOR.

KOŞULLAR (hepsi sağlanmazsa iddia düşer):
  (a) EV-2026-08-10-330 kırılma hesabı doğru olmalı
  (b) EUR/USD 1,00–1,20 aralığında olmalı (fx UNKNOWN — T-311)
  (c) LCL kotasyonu TAZE olmalı → 2026-08-16'dan sonra iddia da ölür
  (d) 5 CBM kotasyonunun 55–239 CBM'e doğrusal uzatımı geçerli olmalı
      (gerçekte LCL birim fiyatı hacimle DÜŞER → uzatım MUHAFAZAKÂRDIR,
       yani üst sınırı daha da güvenli yapar)
```

**Ters model için pratik sonuç:** FCL `UNKNOWN` olmasına rağmen, lojistik
girdisi **sınırsız değildir**. Ters model, lojistik maliyetine
`≤ LCL_BASE` şeklinde bir **tavan** koyarak çalışabilir. Bu, "navlun bilinmiyor
o yüzden model çalışamaz" ile "navlunu uyduralım" arasındaki üçüncü yoldur.

### 5.2 UNKNOWN haritası — hangi hücre gerçekten boş

| Rota | LCL okyanus | FCL okyanus | Origin locals | Destination locals | TR içi |
|---|---|---|---|---|---|
| **İspanya** | ✅ gerçek | ⛔ **band, C-311 AÇIK** | ✅ T3 | ✅ T3 | ✅ |
| Portekiz | ✅ gerçek | ⛔ **UNKNOWN** | ⛔ UNKNOWN | ✅ | ✅ |
| **İtalya** | ⛔ **UNKNOWN** | ⛔ **UNKNOWN** | ⛔ UNKNOWN | ✅ | ✅ |
| Fransa | ✅ gerçek | ⛔ UNKNOWN | ⛔ UNKNOWN | ✅ | ✅ |
| Şili | ✅ gerçek | ⛔ UNKNOWN | ⛔ UNKNOWN | ✅ | ✅ |
| G. Afrika | ✅ gerçek | ⛔ UNKNOWN | ⛔ UNKNOWN | ✅ | ✅ |
| California | ✅ gerçek | ⛔ UNKNOWN | ⛔ UNKNOWN | ✅ | ✅ |
| Arjantin | ✅ gerçek | ⛔ UNKNOWN | ⛔ UNKNOWN | ✅ | ✅ |
| Avustralya | ✅ gerçek | ⛔ UNKNOWN | ⛔ UNKNOWN | ✅ | ✅ |

**FCL senaryosu yalnızca İspanya için yazılabilmiştir ve o bile bir band
değil, iki köşedir.** Diğer 8 rotada FCL hücresi **boş bırakılmıştır** —
LCL'den FCL türetilmemiştir (§5.1 yalnızca **üst sınır** iddiasıdır, fiyat
tahmini değildir).

### 5.3 C-311'in şişe başına maliyeti (okyanus belirsizliğinin fiyatı)

| Hacim | Konteyner | Okyanus+BAF LOW | Okyanus+BAF HIGH | **Belirsizlik (USD/şişe)** |
|---|---|---|---|---|
| 5.000 | 20DV | 0,069 | 0,300 | **0,231** |
| 5.000 | 40HC | 0,095 | 0,444 | **0,350** |
| 25.000 | 20DV | 0,028 | 0,180 | **0,152** |
| 50.000 | 20DV | 0,028 | 0,150 | **0,122** |
| 50.000 | 40HC | 0,028 | 0,133 | **0,105** |
| 100.000 | 40HC | 0,024 | 0,133 | **0,110** |

> **`C-311` tek başına şişe başına 0,10–0,35 USD'lik bir belirsizlik
> üretmektedir.** Bu, ters modelde fiyat tavanını doğrudan aşağı/yukarı
> kaydıran bir kalemdir. **Ölçek büyüdükçe küçülür ama sıfırlanmaz.**

### 5.4 Modelde OLMAYAN iki duyarlılık (ayrı taşınmalı)

**A) Antrepo bekleme süresi** (`T-301` — başka ajanın alanı)

| Kalış | 5.000 şişe | 25.000 | 50.000 | 100.000 |
|---|---|---|---|---|
| 7 gün (minimum) | 0,0034 EUR/şişe | 0,0034 | 0,0034 | 0,0034 |
| 30 gün | 0,0147 | 0,0147 | 0,0147 | 0,0146 |
| 60 gün | 0,0294 | 0,0294 | 0,0294 | 0,0292 |

> **Bulgu:** Antrepo **depolama** ücreti (0,35 EUR/palet/gün) şişe başına
> **ihmal edilebilir** — 60 günde bile 0,03 EUR. **Ruhsat/bandrol gecikmesinin
> maliyeti antrepoda değil, LİMANDA doğar.** Yanlış yere bakılmamalıdır.

**B) Limanda bekleme (demurrage + ardiye, iki sayaç birden)**

`EV-2026-08-09-344`: 20DV, 21 gün ≈ 2.072 USD (~0,157 USD/şişe @13.200);
60 gün ≈ 8.000 USD (~0,61 USD/şişe). **Bu, en pahalı FCL okyanus navlununu
aşar.** Azaltma: free time içinde antrepoya çekmek (~30–35 kat ucuz).

---

## 6. TERS MODELE GİREN LOJİSTİK GİRDİSİ — ÖNERİLEN SET VE CONFIDENCE

> Ters model **tek bir lojistik sayısı** ister. Aşağıdaki set, verilebilecek
> **en dürüst** settir. Hiçbiri `FACT` değildir; hepsi türevdir.

| Hacim | Önerilen girdi | USD/şişe | EUR/şişe | TRY/şişe | status | confidence | gerekçe |
|---|---|---|---|---|---|---|---|
| **5.000** | LCL BASE (İspanya) | **0,450** | 0 | **3,99** | ESTIMATE | **MEDIUM** *(2026-08-16'ya kadar)* | Tek gerçek kotasyona dayanan mod; FCL'in BASE'i yok |
| **25.000** | LCL BASE = **tavan** | **0,399** | 0 | **1,60** | ESTIMATE | LOW-MEDIUM | FCL UNKNOWN; §5.1 üst sınır |
| **25.000** | FCL 20DV köşe-LOW / köşe-HIGH | 0,073 / 0,289 | 0,028 / 0,067 | 1,44 / 3,45 | ESTIMATE | **LOW** | `C-311` açık — **iki köşe ayrı çalıştırılır** (`M-6`) |
| **50.000** | LCL BASE = tavan | **0,391** | 0 | **1,42** | ESTIMATE | LOW-MEDIUM | aynı |
| **50.000** | FCL 40HC köşe-LOW / köşe-HIGH | 0,070 / 0,201 | 0,021 / 0,033 | 1,23 / 2,17 | ESTIMATE | **LOW** | aynı |
| **100.000** | LCL BASE = tavan | **0,387** | 0 | **1,32** | ESTIMATE | LOW-MEDIUM | aynı |
| **100.000** | FCL 40HC köşe-LOW / köşe-HIGH | 0,058 / 0,201 | 0,018 / 0,033 | 1,03 / 2,07 | ESTIMATE | **LOW** | aynı |

**Bağlayıcı kullanım kuralları:**

1. **Üç sütun toplanamaz** (`M-5`). fx `null`.
2. **FCL'in BASE'i yoktur** (`M-6`). Köşeler ayrı ayrı çalıştırılır.
3. **2026-08-17'den sonra** LCL satırlarının confidence'ı `MEDIUM` → `LOW`'a
   düşer ve status `ESTIMATE` olarak **kaynaksızlaşır** → §1.4.
4. Bu sette **sigorta, bandrolleme, antrepo bekleme, demurrage ve vergi
   YOKTUR.** Ters model bunları ayrı satır olarak eklemek zorundadır.
5. İspanya dışı rotalar için **yalnızca §3'ün okyanus bacağı** kullanılabilir;
   origin locals `UNKNOWN` olduğu için **toplam lojistik maliyeti
   hesaplanamaz**.

**Ters modele giren lojistik girdisinin genel confidence'ı: `LOW`.**
Gerekçe: en iyi bacak (LCL okyanus) `MEDIUM` ve 6 günlük ömre sahip; ikinci
bacak (FCL okyanus) `UNKNOWN`; üçüncü bacak (Türkiye içi) `T3` ama ordino /
iç nakliye `ESTIMATE`. **Zincirin gücü en zayıf halkasıdır.**

---

## 7. `finans-fizibilite`'YE BIRAKILAN HESAPLAR

| # | Hesap | Neden bende değil |
|---|---|---|
| 1 | USD + EUR + TRY toplamı | `fx` `null` (`T-311`) |
| 2 | Müşavirlik CIF kademesi: CIF 15.001–225.000 USD → aşan kısmın **%0,3**'ü | CIF, tedarikçi fiyatı + navlun + sigortadan oluşur — üçü de benim tek başıma belirleyeceğim değerler değil |
| 3 | Navlunun **gümrük kıymetine** girmesi ve vergi matrahını büyütmesi | `gumruk-vergi-uzmani` + matrah sırası |
| 4 | Lead time'ın işletme sermayesine etkisi | benim işim süre vermek, etki hesabı `finans-fizibilite` |
| 5 | Sigorta priminin CIF'e etkisi | `T-304` açık; ayrıca çift sayım riski |

---

## 8. BU DOSYADAKİ SAYILARIN ÖZETİ — NE FACT, NE DEĞİL

| Bölüm | En yüksek statü |
|---|---|
| §3 rota okyanus tablosu | `FACT` **2026-08-16'ya kadar**, sonra `ESTIMATE` |
| §2.3 origin charges (İspanya) | `FACT` (T3, 90d) |
| §2.4 THD / drop-off | `FACT` (T3, 90d) |
| §2.5 müşavirlik tarifesi | `FACT` (T3, 1y) |
| §2.4 ardiye, §2.5 ordino / iç nakliye / X-ray | `ESTIMATE` |
| §4 hacim tabloları | `ESTIMATE` (türev) |
| §4 FCL satırları | `ESTIMATE`, confidence `LOW`, `C-311` açık |
| §5.1 üst sınır iddiası | `ESTIMATE`, koşullu |
| İtalya, FCL diğer rotalar, sigorta, bandrol, fire oranı | `UNKNOWN` |
