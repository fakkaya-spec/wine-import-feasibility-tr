# RFQ TEMPLATE — Request for Quotation

> **Sahibi:** `global-sourcing-kasifi`
> **Sürüm:** v2.2 — TUR 3A: **8 teknik alan zorunlu cevap alanına çevrildi (M1…M8)**
> **Durum:** `READY_TO_SEND` (içerik olarak). **BU TURDA GÖNDERİLMEDİ VE GÖNDERİLMEZ.**
> Fiili gönderim yalnızca karar `TEST` veya `IMPORT PILOT` ise, TUR 7'de yapılır.
>
> `<>` içindeki alanlar gönderim öncesi doldurulur. Doldurulmadan gönderilirse RFQ geçersizdir.
>
> **v2.2'de değişen:** 8 teknik alan — **ABV · şişe ağırlığı · koli konfigürasyonu ·
> palet konfigürasyonu · etiket gereksinimleri · menşe belgesi · sertifika seti ·
> Türkiye ihracat geçmişi** — cevapsız bırakılabilir sorular olmaktan çıkarılıp
> **`[MANDATORY]` boş bırakılamaz alan** hâline getirildi. Bunlar **yeni soru
> değildir**; mevcut soruların kabul edilebilir cevap formatı tanımlandı ve
> cevapsızlığın teklife ne yaptığı üreticiye **önceden yazılı olarak** bildirildi.
> SUMMARY SHEET **S1–S27**'ye çıktı (S26 ve S27 eklendi; ikinci bir paralel liste
> **yaratılmadı**).
> Gerekçe, kabul formatı ve cevapsızlık kuralı: **`50-sourcing/rfq-zorunlu-alanlar.md`**.
>
> **v2.1'de eklenen/genişletilen alanlar:** boş ve dolu şişe ağırlığı (1.14, 1.15),
> Incoterms® 2020 kabiliyeti (3.16), lead time'ın üretim/evrak/gemi kırılımı (3.17),
> kuru malzeme birim maliyet kırılımı — **karton/koli ve etiket dahil** (3.18, 3.19),
> private label etiket maliyeti tek seferlik + tekrarlayan (4.13), ve cevabın CSV'ye
> birebir oturmasını sağlayan **SUMMARY SHEET**.
> Alan alan denetim (v2.1 dönemi, S1–S25 numaralandırmasına göre yazılmıştır):
> `50-sourcing/rfq-alan-kontrolu.md`.

---

## 0. İÇ KULLANIM — GÖNDERİM ÖNCESİ KONTROL (BU BÖLÜM GÖNDERİLMEZ)

1. Şablon **İngilizce**dir. Türkçe gönderilmez.
2. Fiyat **EXW ve FOB olarak AYRI AYRI** istenir. Tek bir "price" cevabı, Incoterm'i
   açıkça yazılmamışsa `UNKNOWN`'dır ve `tedarikci-havuzu.csv`'ye **girilmez**.
3. Cevabın `INDICATIVE` mi `FIRM_OFFER` mi olduğu **soru 3.4** ile netleştirilir.
   Bu ayrım yapılmadan hiçbir fiyat modele giremez.
4. Koli/palet ölçü ve ağırlıkları (Bölüm 2) `navlun-lojistik-uzmani`'nın konteyner ve
   navlun hesabı için **zorunludur**. Bu alanlar boş dönerse teklif eksiktir.
5. Menşe ispat belgesi sorusu (Bölüm 6) tercihli tarife için kritiktir. Cevap
   `gumruk-vergi-uzmani`'na ham hâliyle iletilir — bu ajan tarife yorumu yapmaz.
6. Ödeme vadesi cevabı (3.8–3.9) KKDF ve cash conversion cycle girdisidir.
7. Eksik alan **tahminle doldurulmaz**. Takip e-postası gönderilir, alan `UNKNOWN` kalır.
8. Aynı RFQ **tüm tedarikçilere aynı metinle** gönderilir. Metin değiştirilirse
   teklifler karşılaştırılamaz hâle gelir.
9. Gönderim öncesi hedef hacim (`<VOLUME>`) `00-charter/kapsam.md`'deki hacim
   basamaklarından seçilir: 5.000 / 10.000 / 25.000 / 50.000 / 100.000 şişe/yıl.
10. **Bölüm 0'daki SUMMARY SHEET (v2.2'de S1–S27) kaldırılmaz.** Bu tablo, gelen cevabın
    `tedarikci-havuzu.csv` ve `80-model/inputs/tedarikci.yaml` alanlarına birebir
    oturmasını sağlayan yapıdır. Serbest metin cevap, yapılandırılmış cevap değildir.
11. **Etiket ve karton maliyetinin EXW'ye dahil olup olmadığı ayrı sorulur** (3.18,
    4.13, 4.14). Dahil/hariç belirsizse fiyat karşılaştırılamaz — `UNKNOWN` yazılır.
    Bu, L0'ın ne kapsadığını tanımlayan sorudur; katman disiplininin bir parçasıdır.
12. **Üretim süresi ile toplam lead time ayrı alanlardır** (3.17a vs 3.11). TUR 1'de
    gözlenen 28–42 gün **yalnızca üretim** süresidir; navlun hariçtir. İkisi
    karıştırılırsa `peak_cash_requirement` yanlış hesaplanır.
13. **`[MANDATORY]` işaretli 8 alan (M1…M8) boş bırakılamaz.** Bunlar SUMMARY
    SHEET'in **S5, S7, S8, S9, S23, S24, S26, S27** satırlarıdır. Kabul edilebilir
    format, reddedilen cevap kalıpları ve **cevapsızlık kuralı** tek yerde
    tanımlıdır: **`50-sourcing/rfq-zorunlu-alanlar.md`**. Bu dosya bu şablonun
    ayrılmaz parçasıdır; şablon onsuz değerlendirilemez.
14. **Cevapsızlık kuralı gönderimden ÖNCE başkan onayı gerektirir** (`T-884`).
    Kural, bugünkü doluluk oranıyla (M2 şişe ağırlığı: 26/26 `UNKNOWN`) uygulanırsa
    **kısa listenin tamamını değerlendirme dışı bırakabilir.** Bu bir tasarım
    tercihidir, ama bedeli olan bir tercihtir ve tek başına bu ajanın kararı değildir.
15. **Eleme kuralı 8 alanın hepsinde aynı değildir.** M2/M3/M4 cevapsızsa teklif
    **karşılaştırılamaz** (EXW/FOB → CIF köprüsü kurulamaz). M6 cevapsızsa teklif
    elenmez, **`DOC_FAIL` varsayımıyla cezalı** değerlendirilir. M1/M5/M7/M8
    cevapsızsa teklif karşılaştırmaya girer, **etiketlenir**. Ayrıntı:
    `rfq-zorunlu-alanlar.md` §4.2.

### Soru → CSV kolonu / YAML alanı eşlemesi (denetim için)

Sol sütun = üreticiye giden soru numarası. Orta sütun = `50-sourcing/tedarikci-havuzu.csv`
kolonu. Sağ sütun = `80-model/inputs/tedarikci.yaml` alanı (boşsa: bu alan CSV'de kalır,
modele yalnızca **seçili tedarikçi** belirlendikten sonra taşınır).

| RFQ sorusu | `tedarikci-havuzu.csv` kolonu | `tedarikci.yaml` alanı |
|---|---|---|
| S-blok (özet) | tüm satır — çapraz kontrol | — |
| 1.1 | `product_type`, `brand_name` | — |
| 1.2 | `grape_blend` | — |
| 1.3 | `vintage` | — |
| **1.4 · `[MANDATORY]` M1** | `abv_pct` | `urun.yaml → urun.abv_pct` |
| 1.7 | `volume_ml` | — |
| **1.14 · `[MANDATORY]` M2** | `empty_bottle_weight_g` *(yeni kolon)* | `urun.yaml → sise_spesifikasyonu.bos_sise_agirligi_g` |
| **1.15 · `[MANDATORY]` M2** | `filled_bottle_weight_g` *(yeni kolon)* | `urun.yaml → sise_spesifikasyonu.dolu_sise_brut_agirligi_g` |
| **1.17 · `[MANDATORY]` M2** | `bottle_form_dims` *(yeni kolon)* | `lojistik.yaml → urun_fizik.paketli_sise_hacim_m3` (girdi) |
| **2.1 · `[MANDATORY]` M3** | `bottles_per_case` | `lojistik.yaml → urun_fizik.koli_formati` |
| **2.2 · `[MANDATORY]` M3** | `case_gross_weight_kg` | `lojistik.yaml → urun_fizik.koli_brut_agirlik_kg` |
| **2.3 · `[MANDATORY]` M3** | `case_dims_cm` | `lojistik.yaml → urun_fizik.paketli_sise_hacim_m3` |
| **2.5 · `[MANDATORY]` M4** | `cases_per_pallet` | `lojistik.yaml → urun_fizik.palet_basina_sise.*` |
| **2.6 · `[MANDATORY]` M4** | `pallet_type_ispm15` *(yeni kolon)* | `lojistik.yaml → konteyner.palet_sayisi.*` (hangi senaryo) |
| **2.7 · `[MANDATORY]` M4** | `pallet_gross_weight_kg` | `lojistik.yaml → urun_fizik.yuklu_palet_brut_kg.*`, `.yuklu_palet_yukseklik_mm` |
| **2.8 · `[MANDATORY]` M4** | — (konteyner başına koli) | `lojistik.yaml → konteyner.sise_kapasitesi_*` çapraz kontrol |
| 2.10 | `loading_port` *(yeni kolon)* | `fiyat.fob_per_sise.yukleme_limani` |
| 3.1 | `price_value` + `price_currency`, `price_unit` (incoterm = **EXW**) | `fiyat.exw_per_sise` (**L0**) |
| 3.2 | `price_value` + `price_currency`, `price_unit` (incoterm = **FOB**) | `fiyat.fob_per_sise` (**L1**) |
| 3.3 | — (CIF ayrı satıra yazılır, L0/L1 ile **karıştırılmaz**) | — (**L2**) |
| 3.4 | `quote_type` | `fiyat.quote_type` |
| 3.5 | `quote_valid_until` | `fiyat.quote_valid_until` |
| 3.6 | `moq_bottles`, `moq_containers` | `siparis_kosullari.moq_sise`, `.moq_konteyner` |
| 3.7 | — | `fiyat.hacim_bazli_fiyat_kirilimi.*` |
| 3.8 / 3.9 | `payment_terms` | `odeme.odeme_sekli` |
| 3.10 | `payment_days` | `odeme.vade_gun` |
| 3.11 | `lead_time_days` | `siparis_kosullari.lead_time_gun` |
| 3.12 | `annual_capacity_bottles` | `siparis_kosullari.yillik_kapasite_sise` |
| **3.16** | `incoterm` | `fiyat.incoterm` |
| **3.17** | `production_time_days` *(yeni kolon)* | `arastirma_bulgulari.uretim_lead_time_gun` karşılığı |
| **3.18** | `carton_cost_per_bottle`, `label_cost_per_bottle` *(yeni kolonlar)* | — |
| **3.19** | — (koli konfigürasyonu değişikliğinin fiyat etkisi) | — |
| 4.1 / 4.2 | `private_label_capable` | `private_label.mumkun_mu`, `.min_siparis_sise` |
| 4.4 / 4.5 | `label_customization` | — |
| **4.6 · `[MANDATORY]` M5** | `label_customization` | `private_label.turkce_arka_etiket_menside_uygulanabilir_mi` |
| **4.7 / 4.13** | `label_cost_per_bottle` *(yeni kolon)* | `private_label.etiket_tasarim_maliyeti` |
| 4.11 | — | `private_label.ek_lead_time_gun` |
| **6.1 · `[MANDATORY]` M6** | `origin_proof_doc` | `belgeler.mense_ispat_belgesi` |
| **6.13 · `[MANDATORY]` M6** | `origin_commitment` *(yeni kolon)* | `belgeler.mense_ispat_belgesi` (taahhüt bacağı) |
| 6.2 | `origin_proof_doc` (tercihsiz) | — |
| **6.3 / 6.4 / 6.5 / 6.10 / 6.11 · `[MANDATORY]` M7** | `analysis_certificates` | `belgeler.analiz_sertifikasi`; `ruhsat.yaml → analiz_laboratuvar.*` |
| **6.6 · `[MANDATORY]` M8** | `exported_to_turkey_before` | `risk.turkiyeye_ihracat_gecmisi` |
| 6.7 | `export_markets` | — |
| **6.8 / 6.9 · `[MANDATORY]` M5** | `label_customization` | `ruhsat.yaml → urun_uygunlugu.*`; `lojistik.yaml → bandrolleme_operasyonu.*` |
| 7.1 | `sample_sent` | — |
| 8.1 / 8.7 | `supplier_name`, `contact_channel`, `country`, `region` | `secili_tedarikci.supplier_name`, `.ulke` |
| 8.3 | `annual_capacity_bottles` (çapraz kontrol: 3.12 ile aynı olmalı) | `siparis_kosullari.yillik_kapasite_sise` |

> **Yeni CSV kolonları:** `empty_bottle_weight_g`, `filled_bottle_weight_g`,
> `bottle_form_dims`, `pallet_type_ispm15`, `origin_commitment`, `loading_port`,
> `production_time_days`, `carton_cost_per_bottle`, `label_cost_per_bottle`.
> Bu kolonlar **teklif geldiğinde** `tedarikci-havuzu.csv`'ye eklenir; teklif
> yokken tüm satırlar `UNKNOWN` olacağı için bu turda eklenmemiştir.

### Zorunlu alan haritası — M1…M8 (özet)

| Kod | Alan | SUMMARY SHEET | Detay soru | Cevapsızlık sonucu |
|---|---|---|---|---|
| **M1** | ABV | **S5** | 1.4 | `PRODUCT_SPEC_UNVERIFIED` (elenmez) |
| **M2** | Şişe ağırlığı (boş + dolu + form/ölçü) | **S7** | 1.14, 1.15, 1.17 | **DEĞERLENDİRME DIŞI** |
| **M3** | Koli konfigürasyonu | **S8** | 2.1–2.4 | **DEĞERLENDİRME DIŞI** |
| **M4** | Palet konfigürasyonu | **S9** | 2.5–2.9 | **DEĞERLENDİRME DIŞI** |
| **M5** | Etiket gereksinimleri (uyarlama kabiliyeti) | **S26** | 4.6, 6.8, 6.9 | `LABEL_PATH_UNVERIFIED`; L5 kalemi `UNKNOWN` taşınır |
| **M6** | Menşe ispat belgesi **taahhüdü** | **S27** | 6.1, 6.13 | **CEZALI** — `DOC_FAIL` varsayımı (**−%11,765 tavan**) |
| **M7** | Sertifika seti | **S23** | 6.3–6.5, 6.10, 6.11 | `PILOT_INELIGIBLE` (elenmez) |
| **M8** | Türkiye ihracat geçmişi | **S24** | 6.6, 5.2, 5.3 | `EXECUTION_RISK_UNVERIFIED` (elenmez) |

> **M8 hiçbir hesabı `UNKNOWN` döndürmez** — sayısal model girdisi beslemez,
> yürütme riski göstergesidir. Bu bilinçli olarak yazılmıştır: her alana aynı
> ağırlığı vermek, gerçekten hesap kıran alanların (M2/M3/M4/M6) ağırlığını yok eder.

---

## 1. E-POSTA GÖVDESİ — KOPYALA / YAPIŞTIR (İNGİLİZCE)

**Subject:** Request for Quotation — Wine supply to Türkiye — <MODEL A: brand distribution / MODEL B: private label> — <VOLUME> bottles/year — <COMPANY>

---

Dear <CONTACT NAME / Export Sales Team>,

My name is <NAME> and I am writing on behalf of <COMPANY>, a company based in
Türkiye that is currently evaluating the launch of a value-segment still wine
programme for the Turkish market.

We are at the supplier-selection stage and are building a shortlist of producers
who can supply **bottled finished product** on a recurring basis. Your company was
identified as a potential partner.

We would be grateful if you could complete the questionnaire below. We are sending
an identical questionnaire to every producer on our shortlist so that offers can be
compared on a like-for-like basis. Please answer every line; where a question does
not apply to you, please write **"N/A"** rather than leaving it blank, and where you
do not yet know the answer, please write **"TBC"**. Estimated answers are of no use
to us — an honest "TBC" is more valuable than an approximation.

**Eight lines are marked `[MANDATORY]`.** They are the eight figures without which
we physically cannot turn a price into a delivered cost, and therefore cannot
compare your offer with any other. They are listed together at the top of the
Summary Sheet in Section 0, with the exact format we need and with an explanation
of what happens if they are left blank. Three of them (bottle weight, case
configuration, pallet configuration) are pure packaging data that your production
or logistics colleague can normally supply in a few minutes from an existing
specification sheet — please do involve them before replying.

**We are evaluating two business models in parallel and have no preference between
them at this stage:**

- **Model A — Existing brand distribution:** we import and distribute one of your
  existing brands in Türkiye under your label.
- **Model B — Private label:** you produce under our own brand and label.

Please indicate in Section 3.0 which model(s) you are able to support. If you can
support both, please quote for both.

### Target product profile

| Item | Requirement |
|---|---|
| Category | Still white wine, dry (a still red and a rosé SKU may follow) |
| Style reference | Comparable to a Colombard–Chardonnay style blend; fresh, fruit-forward, low oak |
| Format | **750 ml glass bottle** |
| Positioning | Value / mainstream retail segment |
| Destination | Türkiye — chain retail as primary channel |
| Indicative annual volume | <VOLUME> bottles/year, ramping over <N> months |
| First (pilot) order | <PILOT VOLUME> bottles |

---

### 0. SUMMARY SHEET — please complete this table first

This one-page table is what we compare across suppliers. Sections 1–8 below ask for
the same information in more detail; if the two ever disagree, **this table governs**.
Please fill every row. Use `N/A` if it does not apply and `TBC` if it is not yet known.

> ## ⚠ EIGHT ROWS MARKED `[MANDATORY]` CANNOT BE LEFT BLANK
>
> Rows **S5, S7, S8, S9, S23, S24, S26, S27** are marked `[MANDATORY]`.
> We are not asking these out of curiosity: without them we physically cannot
> convert your price into a landed cost, and your offer therefore cannot be
> compared with any other offer. Please read the three rules below before you start.
>
> **Rule 1 — the format column is binding.** Each mandatory row states the unit and
> the form of the answer. An answer that does not match the stated format counts as
> a blank answer.
>
> **Rule 2 — the following words are not answers** in a mandatory row, and we will
> come back to you if we see them:
> *approximately · around · circa · standard · usually · typically · varies ·
> depends · upon request · see attached spec (with nothing attached) ·
> yes / possible (with no figure, unit or amount) · no problem.*
> A figure without its unit is also a blank answer ("400" is not a weight).
>
> **Rule 3 — "NO" and "N/A" are complete answers; silence is not.**
> If you cannot issue a preferential origin document, if you cannot apply a
> Turkish back label, or if you have never exported to Türkiye — please say so
> plainly. That is useful information and it does **not** count against you.
> `TBC` is also acceptable and honest, but it will trigger one follow-up e-mail.
>
> **What happens if a mandatory row stays empty after our single follow-up:**
> - **S7, S8, S9** (bottle weight, case, pallet): we cannot calculate how many
>   bottles fit in a container, so we cannot calculate freight per bottle, so we
>   cannot convert your EXW/FOB price into a delivered cost. **Your offer will not
>   enter the price comparison.** This is the one outcome we would most like to avoid.
> - **S27** (origin document): we will have to assume that no preferential origin
>   proof will be available for any shipment. That assumption **reduces the price we
>   are able to pay**, so it is in your interest to answer it precisely.
> - **S5, S23, S24, S26**: your offer stays in the comparison, but it is flagged as
>   unverified on product specification, certification, market experience or
>   labelling respectively, and it will rank behind complete offers for the first
>   (pilot) shipment.

| # | Field | Unit / format | Your answer | Detail question |
|---|---|---|---|---|
| S1 | Winery / supplier legal name | text | | 8.1 |
| S2 | Product name / reference quoted | text | | 1.1 |
| S3 | Grape variety or blend | % by variety | | 1.2 |
| S4 | Vintage quoted | year | | 1.3 |
| **S5** | **ABV** `[MANDATORY]` | **`__ , _ % vol`** — one decimal, **for the vintage quoted**; a separate line per vintage if you quote more than one. Add: *"this is the figure that will be printed on the label: YES / NO"*. A range is accepted **only** if both ends are given **and** the upper end is stated as the contractual maximum | | 1.4 |
| **S6** | Bottle size | ml | | 1.7 |
| **S7** | **Bottle weight and shape** `[MANDATORY]` | (a) empty glass weight **`___ g`** (+ tolerance ± g), (b) filled gross weight **`___ g`** (wine + glass + closure + capsule + labels), (c) bottle shape (Bordeaux / Burgundy / Alsace / custom mould), (d) max body diameter **`___ mm`**, (e) total height **`___ mm`**. **All five.** | | 1.14, 1.15, 1.17 |
| **S8** | **Case configuration** `[MANDATORY]` | (a) bottles/case, (b) **external** case dimensions `L × W × H` **with the unit written** (mm or cm — internal dimensions are not accepted), (c) gross weight `___ kg`, (d) net weight `___ kg`, (e) cases per layer × layers, (f) dividers/inserts yes/no | | 2.1, 2.2, 2.3, 2.4 |
| **S9** | **Pallet configuration** `[MANDATORY]` | (a) pallet type (EUR 800×1200 / 1000×1200 / GMA / other → give mm), (b) **ISPM-15 heat treated: YES/NO**, (c) cases/pallet, (d) bottles/pallet, (e) number of layers, (f) loaded pallet gross `___ kg`, (g) **total loaded height `___ mm` (pallet included)**, (h) pallets **and** cases per 20' DV and per 40' HC, (i) floor-loading possible YES/NO + cases per 20' DV | | 2.5, 2.6, 2.7, 2.8, 2.9 |
| S10 | MOQ | (a) bottles per SKU, (b) containers per shipment | | 3.6 |
| S11 | **EXW price per bottle** | currency + amount + EXW &lt;place&gt; | | 3.1 |
| S12 | **FOB price per bottle** | currency + amount + FOB &lt;named port&gt; | | 3.2 |
| S13 | Incoterms® 2020 rule(s) you can trade under | list + your default | | 3.16 |
| S14 | Port of loading | port name + country | | 2.10 |
| S15 | Lead time, PO → goods ready for loading | calendar days | | 3.11 |
| S16 | Of which: production / bottling time | calendar days | | 3.17 |
| S17 | Payment terms — first order | text (e.g. 50% T/T advance, balance against B/L) | | 3.8 |
| S18 | Private label available? | YES / NO | | 4.1 |
| S19 | Label cost | one-off (artwork/plates) + per bottle or per 1,000; state currency; **state whether already included in S11** | | 3.18, 4.13 |
| S20 | Carton / case cost | per bottle or per case; state currency; **state whether already included in S11** | | 3.18 |
| S21 | Samples | can send YES/NO; number of bottles; cost; days | | 7.1–7.3 |
| S22 | Annual capacity available to us | bottles/year | | 3.12, 8.3 |
| **S23** | **Certificate set** `[MANDATORY]` *(origin documents moved to S27)* | (a) analysis certificate — **tick the parameters actually reported**: ☐ ABV ☐ total acidity ☐ volatile acidity ☐ residual sugar ☐ total SO₂ ☐ methanol ☐ density ☐ dry extract ☐ other ___ ; (b) **name of the laboratory** + accreditation (ISO 17025 / OIV): ___ ; (c) issued **per batch or per product**: BATCH / PRODUCT; (d) health / free sale certificate: YES/NO + exact document name; (e) food safety: ☐ BRCGS ☐ IFS ☐ ISO 22000 ☐ HACCP ☐ none → **attach a copy** (a ticked box with no copy attached is an incomplete answer); (f) batch traceability bottle lot → tank → harvest: YES/NO | | 6.3, 6.4, 6.5, 6.10, 6.11 |
| **S24** | **Have you exported to Türkiye before?** `[MANDATORY]` | **YES / NO.** If YES: importer name, years `<yyyy>–<yyyy>`, annual volume (bottles or litres). If NO: *"any additional condition you would require for a first shipment to Türkiye?"* YES/NO + explanation. **"We export to many countries" is not an answer to this question.** | | 6.6, 5.2, 5.3 |
| S25 | **Quotation type and validity** | INDICATIVE or FIRM OFFER, valid until &lt;date&gt; | | 3.4, 3.5 |
| **S26** | **Label adaptation capability** `[MANDATORY]` *(this is about capability, not cost — cost is S19)* | Five YES/NO answers, each with the figure asked for: (a) can you **apply a Turkish-language back label at your own facility** from artwork we supply? YES/NO → if YES: cost per bottle (currency) + days added to lead time; (b) can you provide **at least 18 cm² of printable area** on the back label? YES/NO + current label size `mm × mm`; (c) can you leave a **blank area for an importer-applied strip/stamp**? YES/NO + area `mm × mm` + its position on the bottle; (d) can you adapt the label to the importing country's mandatory statements (allergens, importer details, health warning)? YES/NO + revision turnaround in days; (e) can you print the ABV at a **character height of at least 3 mm**? YES/NO | | 4.6, 6.8, 6.9 |
| **S27** | **Origin document — capability AND commitment** `[MANDATORY]` | (a) **which document can you issue — write the document name, "yes" is not an answer**: ☐ EUR.1 movement certificate ☐ invoice declaration ☐ REX statement on origin ☐ A.TR ☐ non-preferential certificate of origin only ☐ none; (b) will you **commit contractually to issuing it for every shipment**? YES/NO; (c) are you an "approved exporter", and will you switch to EUR.1 if the invoice-declaration value threshold is exceeded? YES/NO; (d) is the wine **wholly produced and bottled in the country of origin**, or does it contain imported bulk wine? NONE / YES → country + %; (e) **from which country's port will the shipment leave**, and will it be consolidated in a third country? port + country / no consolidation; (f) would you accept a **price-adjustment clause** if the document cannot be issued or is rejected at import? YES/NO | | 6.1, 6.2, 6.13 |

> **Three things we must ask you to be strict about, because they decide whether your
> offer can be compared at all:**
> 1. **S11 and S12 are different prices.** Please do not answer only "our price is X".
>    An EXW price must name the place of delivery; an FOB price must name the port.
> 2. **S19 and S20:** please tell us whether label and carton are *inside* the EXW
>    price or charged separately. A price that silently excludes dry goods is not
>    comparable with one that includes them.
> 3. **S7, S8 and S9 must be internally consistent.** We cross-check them:
>    *(filled bottle weight × bottles per case) + packaging ≈ case gross weight*, and
>    *(case gross weight × cases per pallet) + pallet ≈ loaded pallet gross weight*.
>    If they do not reconcile we will come back to you rather than guess, so please
>    take the figures from your actual packaging specification sheet.

---

### 1. Product specification

| # | Question | Your answer |
|---|---|---|
| 1.1 | Product name / internal reference | |
| 1.2 | Grape variety or exact blend composition (% by variety) | |
| 1.3 | Vintage(s) currently available and approximate stock per vintage | |
| **1.4** | **`[MANDATORY]` ABV (% vol)** — the exact figure that will appear on the label, to one decimal, **for the vintage you are quoting**. If you quote more than one vintage, give one figure per vintage. If you can only give a range, give both ends **and** state the upper end as the contractual maximum. *"Approximately", "standard" and "depends on the vintage" are not answers.* | |
| 1.5 | Residual sugar (g/L) | |
| 1.6 | Total acidity (g/L) and pH | |
| 1.7 | Bottle volume — we require **750 ml**. Confirm availability. | |
| 1.8 | Bottle type / mould reference and glass colour (flint, antique green, dead leaf, etc.) | |
| 1.9 | Closure type (natural cork / technical cork / screw cap / synthetic) | |
| 1.10 | Total sulphur dioxide level (mg/L) | |
| 1.11 | Is the wine fined with animal-derived agents? (vegan status) | |
| 1.12 | Recommended shelf life from bottling (months) | |
| 1.13 | Is the wine produced from your own vineyards, purchased grapes, purchased must, or purchased finished wine? | |
| **1.14** | **`[MANDATORY]` Empty bottle weight (g)** — weight of the glass alone, as stated by your glass supplier, **with tolerance (± g)**. *"Lightweight bottle" or "standard Bordeaux" without a figure is not an answer.* | |
| **1.15** | **`[MANDATORY]` Filled bottle gross weight (g)** — wine + glass + closure + capsule + labels. Please state which components are included if your figure differs. | |
| 1.16 | Do you offer a lighter-weight bottle for the same wine? If yes, state its weight (g) and the price difference per bottle. | |
| **1.17** | **`[MANDATORY]` Bottle shape and dimensions** — (a) shape: Bordeaux / Burgundy / Alsace / custom mould; (b) maximum body diameter (mm); (c) total bottle height (mm). *We ask because bottle shape alone changes how many bottles fit into a container by up to 38%, which changes the freight cost per bottle — and therefore the price we can pay you.* | |

### 2. Packaging and logistics data — **`[MANDATORY]` BLOCK: 2.1–2.9 cannot be left blank**

> **Why this whole block is mandatory.** Everything we can pay you depends on the
> delivered cost per bottle, and the delivered cost per bottle depends on how many
> bottles fit into one container. We cannot estimate that: the same 750 ml wine
> occupies between 0.00223 m³ and 0.00360 m³ per bottle depending on bottle shape
> and case format — a **38% swing** in container capacity, and therefore in freight
> per bottle. If 2.1–2.9 come back empty, we are not able to compare your price with
> anyone else's, however good your price is.
>
> The fastest way to answer this block is to **attach your packaging specification
> sheet** (case and pallet drawing) *and* still fill in the table, so that we know
> which figures you consider binding.

| # | Question | Your answer |
|---|---|---|
| **2.1** | **`[MANDATORY]` Bottles per case** — and can this be changed (6 ↔ 12)? YES/NO | |
| **2.2** | **`[MANDATORY]` Case gross weight (kg) AND net weight (kg)** — both figures; a single unlabelled weight is not accepted | |
| **2.3** | **`[MANDATORY]` Case EXTERNAL dimensions L × W × H — with the unit written (mm or cm).** Internal dimensions are not accepted. All three dimensions required. | |
| **2.4** | **`[MANDATORY]` Cases per layer × number of layers per pallet**; are dividers/inserts used? YES/NO | |
| **2.5** | **`[MANDATORY]` Cases per pallet AND bottles per pallet** | |
| **2.6** | **`[MANDATORY]` Pallet type** (EUR 800×1200 / industrial 1000×1200 / GMA / other → give mm) **and whether heat-treated (ISPM-15): YES/NO**, and whether the stamp is present | |
| **2.7** | **`[MANDATORY]` Loaded pallet gross weight (kg) and total loaded height including the pallet (mm or cm — state the unit)** | |
| **2.8** | **`[MANDATORY]` How many pallets AND how many cases you load into a 20' DV, and into a 40' HC** — from your own loading experience | |
| **2.9** | **`[MANDATORY]` Can you load floor-loaded (non-palletised)? YES/NO.** If YES, cases per 20' DV. | |
| 2.10 | Nearest loading port / your usual port of departure | |
| 2.11 | Distance from your winery to that port (km) | |
| 2.12 | Do you offer temperature-controlled (reefer) or thermal-liner loading, and at what surcharge? | |
| 2.13 | Case marking capability (barcode EAN-13 on bottle and case, batch/lot code, best-before) | |

### 3. Commercial terms

**3.0 — Which model(s) can you support?**
☐ Model A (existing brand distribution)  ☐ Model B (private label)  ☐ Both

| # | Question | Your answer |
|---|---|---|
| 3.1 | **EXW price per bottle** — state currency and the exact place of delivery (EXW <place>) | |
| 3.2 | **FOB price per bottle** — state currency and the **named port** (FOB <port>) | |
| 3.3 | CIF price per bottle to Ambarlı / Mersin / İzmir, if you are able to quote it | |
| 3.4 | **Is this an INDICATIVE quotation or a FIRM OFFER?** | |
| 3.5 | **Quotation validity date** | |
| 3.6 | **MOQ** — please state both: (a) minimum bottles per SKU, (b) minimum number of containers per shipment | |
| 3.7 | Price breaks by annual volume: 5,000 / 10,000 / 25,000 / 50,000 / 100,000 bottles | |
| 3.8 | Payment terms you require for a **first order** (T/T in advance %, L/C at sight, L/C usance, documentary collection D/P or D/A, open account) | |
| 3.9 | Payment terms you would consider from the **second order** onwards, and after how many shipments | |
| 3.10 | If deferred payment is possible: number of days and any price surcharge for it | |
| 3.11 | Lead time from confirmed PO to goods ready for loading (calendar days) | |
| 3.12 | Annual volume you can reserve for us (bottles) without a new harvest commitment | |
| 3.13 | Currency of invoicing and whether you accept EUR / USD | |
| 3.14 | Which costs are **not** included in the EXW price (pallets, export documents, labelling, etc.)? | |
| 3.15 | Do you require a written annual volume commitment? | |
| 3.16 | **Which Incoterms® 2020 rules can you trade under** (EXW / FCA / FOB / CFR / CIF / CPT / CIP / DAP)? Which one is your standard for a first-time buyer, and which do you recommend for Türkiye? | |
| 3.17 | Please split the lead time you gave in 3.11 into: (a) production / bottling days, (b) label printing and application days, (c) export documentation days, (d) days waiting for a vessel or truck booking | |
| 3.18 | **Dry goods cost breakdown per bottle** — please state the amount and currency for each, and mark clearly whether each one is ALREADY INCLUDED in the EXW price in 3.1: (a) glass bottle, (b) closure, (c) capsule, (d) **label set (front + back)**, (e) **carton / case**, (f) dividers or inserts, (g) pallet, stretch wrap and palletising labour | |
| 3.19 | If we required a different case configuration (for example 6 × 750 ml instead of 12 × 750 ml), what would the cost impact per bottle be? | |
| 3.20 | Do you charge separately for export documentation (certificate of origin, EUR.1, health certificate, legalisation)? If yes, how much per shipment? | |

### 4. Model B — Private label

| # | Question | Your answer |
|---|---|---|
| 4.1 | Do you produce under a customer's own brand? | |
| 4.2 | **Minimum order quantity for private label**, per SKU and per shipment | |
| 4.3 | Is the private label MOQ different from your standard MOQ? By how much? | |
| 4.4 | Can you adjust the blend / style to a target sensory profile? What is the minimum batch for a bespoke blend? | |
| 4.5 | Do you print and apply labels in-house, or through a third party? | |
| **4.6** | **`[MANDATORY]` Can you apply a Turkish-language back label at your facility, using artwork we supply? YES / NO.** If YES: cost per bottle (state currency) and how many days it adds to the lead time. If NO: say so plainly — we will then apply it in Türkiye and we need to know that now, not later. *(This is the capability question. The cost of the label itself is 4.13.)* | |
| 4.7 | Number of label revisions / mock-ups included in the price, and how many working days each revision cycle takes | |
| 4.8 | Custom bottle mould, capsule colour, embossing or screen printing — availability and MOQ impact | |
| 4.9 | Who owns the brand, the artwork and the blend recipe? Please state explicitly. | |
| 4.10 | Would you undertake **not** to sell the same blend under another brand into Türkiye? | |
| 4.11 | Additional lead time for private label versus your standard product (days) | |
| 4.12 | Minimum quantity for a **pre-production sample run** (e.g. 6–12 labelled bottles) | |
| 4.13 | **Label cost for private label.** Please split into: (a) one-off charges — artwork/origination, plates or clichés, cutting dies, colour proofing; (b) recurring cost per bottle or per 1,000 bottles for the label set (front + back), and separately for a printed capsule or branded closure. State the currency, and state whether (b) is already inside the EXW price you gave in 3.1. | |
| 4.14 | **Carton cost for private label.** Cost per case for a printed/branded carton versus your standard plain or generic carton, and the minimum print run for a branded carton. | |
| 4.15 | If we cancel or change artwork after plates are made, what is the charge? | |

### 5. Model A — Existing brand distribution

| # | Question | Your answer |
|---|---|---|
| 5.1 | Which of your existing brands/SKUs are available for Türkiye, in the value segment? | |
| 5.2 | Do you currently have an importer or distributor in Türkiye? If yes, is the territory closed? | |
| 5.3 | Has this brand been sold in Türkiye before? By whom, in what years, at what volume, and why did it stop? | |
| 5.4 | Would you grant **exclusivity** for Türkiye? Under what conditions and for what term? | |
| 5.5 | Minimum annual volume commitment required to obtain and to retain exclusivity | |
| 5.6 | Marketing / listing support offered (budget, POS material, sampling stock, co-funding %) | |
| 5.7 | Do you impose a resale price or margin ceiling on the importer? | |
| 5.8 | Notice period and termination conditions; treatment of unsold stock on termination | |
| 5.9 | Do you register your trademark in Türkiye, or is that the importer's responsibility? | |
| 5.10 | Price revision mechanism and frequency; how much advance notice of a price increase? | |

### 6. Documentation, certification and compliance

| # | Question | Your answer |
|---|---|---|
| **6.1** | **`[MANDATORY]` Which preferential origin proof can you issue for Türkiye — EUR.1 movement certificate, invoice declaration, REX statement on origin, or A.TR? Please write the document name.** "Yes", "we provide all documents" and "our customs agent handles it" are **not** answers. If none of these is available for your country, please answer **"none"** — that is a complete and perfectly acceptable answer. | |
| 6.2 | Can you issue a non-preferential **Certificate of Origin** (chamber of commerce certified)? | |
| **6.3** | **`[MANDATORY]` Analysis certificate — tick the parameters actually reported** (ABV, total acidity, volatile acidity, residual sugar, total SO₂, methanol, density, dry extract, other). A statement that "an analysis report is provided" without the parameter list is not an answer. Is it issued **per batch** or **per product**? | |
| **6.4** | **`[MANDATORY]` Which laboratory issues it — name the laboratory — and is it accredited (ISO 17025 / OIV method)?** | |
| **6.5** | **`[MANDATORY]` Can you provide a health / free sale certificate issued or endorsed by your national authority? YES/NO + the exact document name.** | |
| **6.6** | **`[MANDATORY]` Have you exported to Türkiye before? YES / NO.** If YES: which importer, which years, what annual volume. If NO: do you have any additional condition for a first shipment to Türkiye? **"We export to many countries" does not answer this question. "No" does, and it does not count against you.** | |
| 6.7 | Which export markets do you currently serve, and what is your total annual export volume? | |
| **6.8** | **`[MANDATORY]` Can you adapt the label to the importing country's legal requirements (mandatory statements, allergen declaration, importer details, health warnings)? YES/NO + how many days a revision cycle takes.** Two specific points we must confirm now: (a) can the back label carry **at least 18 cm² of printable area**? YES/NO + your current label size in mm × mm; (b) can the ABV be printed at a **character height of at least 3 mm**? YES/NO | |
| **6.9** | **`[MANDATORY]` Can you leave a defined blank area on the label or bottle for an importer-applied strip/stamp? YES/NO + the area in mm × mm + its position on the bottle.** This strip is applied in Türkiye, not by you — but the physical space has to exist on the bottle you ship. | |
| **6.10** | **`[MANDATORY]` Food safety / quality certifications held (BRCGS, IFS, ISO 22000, HACCP) — tick and ATTACH a copy with its expiry date.** A ticked box with no attachment is an incomplete answer. If you hold none, answer "none". | |
| **6.11** | **`[MANDATORY]` Traceability: can you supply batch-level records linking bottle lot → tank → harvest? YES/NO** | |
| 6.12 | Do you hold liability insurance covering exported product? | |
| **6.13** | **`[MANDATORY]` Origin commitment.** Four separate answers: (a) will you **commit contractually to issuing the document named in 6.1 for every shipment**? YES/NO; (b) are you an **"approved exporter"**, and will you switch to a EUR.1 if the invoice-declaration value threshold is exceeded? YES/NO; (c) is the wine **wholly produced and bottled in the country of origin**, or does it contain **imported bulk wine**? NONE / YES → state country and %; (d) **from which country's port will the shipment physically leave**, and will it be consolidated in a third country on the way? Port + country / no consolidation. | |
| **6.14** | Would you accept a **price-adjustment clause** in the contract for the case where the origin document cannot be issued, or is rejected at import? YES / NO + on what terms | |

> **Note to supplier:** we ask about origin documentation because the importing
> country's treatment of the consignment depends on it. We are **not** asking you to
> advise on Turkish duties or taxes — only to confirm which documents you can issue
> and whether you will commit to issuing them. To be transparent about why we press
> on this: whether a valid origin document accompanies each shipment changes the
> maximum price we are able to pay you by **around 12%**. It is therefore in your
> commercial interest, not only ours, that 6.1 and 6.13 are answered precisely.
> If your country has no preferential arrangement with Türkiye, "none" is the right
> answer and costs you nothing — but please note that in that case no premium can be
> justified for "handling the paperwork", because there is no preferential document
> to handle.

### 7. Samples

| # | Question | Your answer |
|---|---|---|
| 7.1 | Can you send samples to Türkiye? | |
| 7.2 | Number of bottles you can send and any cost (product + freight) | |
| 7.3 | Lead time for sample dispatch | |
| 7.4 | Can you send samples of the **exact** batch you would ship, or a representative batch? | |
| 7.5 | Do you provide the analysis certificate together with the sample? | |

### 8. Company background

| # | Question | Your answer |
|---|---|---|
| 8.1 | Legal company name, registration number and full address | |
| 8.2 | Year established; ownership (family / cooperative / group) | |
| 8.3 | Annual production capacity (bottles and litres) | |
| 8.4 | Bottling line capacity (bottles/hour) and whether owned or contracted | |
| 8.5 | Storage capacity and whether temperature-controlled | |
| 8.6 | Two trade references in export markets we may contact | |
| 8.7 | Name, position, direct e-mail and phone of the person responsible for this account | |

---

We would be grateful for your response by **<DEADLINE DATE>**. Please return this
document with your answers inserted — **including the Summary Sheet in Section 0** —
together with:

- a current price list,
- product technical sheets,
- a sample analysis certificate,
- a packaging specification sheet (case and pallet drawing),
- your food-safety certificates.

We are happy to sign a mutual non-disclosure agreement before you share commercial
terms, if you prefer.

Thank you for your time.

Kind regards,

<NAME>
<POSITION>
<COMPANY>
<ADDRESS>
<EMAIL> · <PHONE>

---

## 2. CEVAP DEĞERLENDİRME KONTROL LİSTESİ (İÇ KULLANIM)

Teklif geldiğinde, `tedarikci-havuzu.csv`'ye işlenmeden **önce** kontrol et:

### 2.0 ZORUNLU ALAN KAPISI — ÖNCE BU (M1…M8)

Bu kapı geçilmeden aşağıdaki genel liste işletilmez. Kural seti:
`50-sourcing/rfq-zorunlu-alanlar.md` §4.

- [ ] **M1 (S5) ABV** — tek rakam + birim + hasat yılı var mı? Aralıksa üst uç
      sözleşme azamisi olarak beyan edilmiş mi?
- [ ] **M2 (S7) şişe ağırlığı** — boş cam **ve** dolu brüt **ve** form/çap/yükseklik,
      beşi birden var mı?
- [ ] **M3 (S8) koli** — şişe/koli + **dış** ölçü (birimli, 3 boyut) + brüt **ve** net kg?
- [ ] **M4 (S9) palet** — palet tipi + ISPM-15 + koli/palet + yüklü brüt kg +
      **toplam yükseklik** + 20'DV/40'HC adetleri?
- [ ] **M5 (S26) etiket kabiliyeti** — 5 alt sorunun her biri EVET/HAYIR **ve**
      istenen ölçü/bedel/süre ile mi?
- [ ] **M6 (S27) menşe belgesi** — **belge adı** var mı ("evet" yeterli değil)?
      Her sevkiyat taahhüdü, dökme bileşen, çıkış limanı ülkesi cevaplı mı?
- [ ] **M7 (S23) sertifika seti** — analiz **parametre listesi** + laboratuvar adı +
      parti/ürün ayrımı + gıda güvenliği belgesinin **kopyası ekli** mi?
- [ ] **M8 (S24) Türkiye geçmişi** — EVET/HAYIR net mi? EVET ise ithalatçı/yıl/hacim var mı?
- [ ] **Çapraz tutarlılık:** (dolu şişe g × şişe/koli) + ambalaj ≈ koli brüt kg?
      (koli brüt × koli/palet) + palet ≈ yüklü palet brüt kg? **Tutmuyorsa sayı
      kullanılmaz**, `99-ops/celiskiler.md`'ye taşınır ve üreticiye sorulur.
- [ ] **Reddedilen kalıp taraması:** zorunlu alanlarda *approximately / standard /
      usually / varies / upon request / yes* (rakamsız) geçiyor mu? Geçiyorsa
      o alan **boş sayılır**.
- [ ] Eksik varsa → **tek** takip e-postası, **7 takvim günü**. Sonrasında alan bazında
      sonuç uygulanır (`rfq-zorunlu-alanlar.md` §4.2): M2/M3/M4 → **değerlendirme dışı**;
      M6 → **`DOC_FAIL` cezalı**; M1/M5/M7/M8 → etiketlenir, elenmez.
- [ ] **Hiçbir zorunlu alan bizim tarafımızdan tahminle doldurulmadı** (`CLAUDE.md` §1.1).

### 2.1 GENEL KONTROL LİSTESİ

- [ ] **Summary Sheet (S1–S27) dolu mu?** 27 satırın kaçı boş kaldı? Boş kalan her
      satır `UNKNOWN`'dır ve takip e-postasına girer.
- [ ] **Summary Sheet ile Bölüm 1–8 çelişiyor mu?** Çelişiyorsa sayı **kullanılmaz**;
      `99-ops/celiskiler.md`'ye taşınır ve üreticiye sorulur. (Şablon "S bloğu esastır"
      diyor, ama tedarikçi kendi belgesinde kendisiyle çelişiyorsa bu bir veri
      kalitesi sinyalidir, sessizce seçim yapılmaz.)
- [ ] Incoterm **açıkça** yazılmış mı? EXW ise yer, FOB ise liman adı var mı?
      (Yer/liman yoksa fiyat `UNKNOWN`'dır — EXW Bordeaux ile EXW Languedoc aynı şey değildir.)
- [ ] EXW ve FOB **ayrı ayrı** verilmiş mi? Tek fiyat varsa hangisi olduğu yazılı mı?
- [ ] Fiyat birimi net mi (şişe mi, koli mi, litre mi)?
- [ ] Para birimi yazılı mı?
- [ ] `INDICATIVE` mi `FIRM_OFFER` mi? (3.4 cevapsızsa → `INDICATIVE` kabul edilir)
- [ ] Geçerlilik tarihi var mı? (Bu, kanıt kartının `ttl`'i olur.)
- [ ] MOQ hem **şişe** hem **konteyner** bazında verilmiş mi? (3.6a ve 3.6b)
- [ ] Private label MOQ'su standart MOQ'dan farklı mı? (4.3)
- [ ] Koli **ve** palet ölçü/ağırlık verileri tam mı? (2.1–2.8) — eksikse konteyner hesabı yapılamaz
- [ ] Menşe ispat belgesi hangisi? (6.1) — "yes" yeterli değil, **belge adı** gerekir
- [ ] Ödeme vadesi net mi? İlk sipariş ve sonraki siparişler ayrı ayrı mı? (3.8/3.9)
- [ ] Türkiye'ye ihracat geçmişi sorusu (6.6) cevaplanmış mı?
- [ ] ABV rakamı verilmiş mi? (1.4)
- [ ] **Boş şişe ağırlığı (1.14) verilmiş mi?** Verilmemişse koli brüt ağırlığı
      doğrulanamaz ve `navlun-lojistik-uzmani` ağırlık/hacim kontrolünü yapamaz.
- [ ] **Etiket maliyeti (3.18d / 4.13) EXW'nin İÇİNDE mi DIŞINDA mı?** "Var" cevabı
      yetersiz — dahil/hariç yazmıyorsa fiyat karşılaştırılamaz, `UNKNOWN` işaretlenir.
- [ ] **Karton/koli maliyeti (3.18e / 4.14) EXW'nin İÇİNDE mi DIŞINDA mı?** Aynı kural.
- [ ] **Üretim süresi (3.17a) toplam lead time'dan (3.11) ayrı verilmiş mi?**
      İkisi karıştırılırsa `siparis_kosullari.lead_time_gun` yanlış dolar.
- [ ] Incoterm kabiliyeti (3.16) listelenmiş mi ve tedarikçinin **standardı** hangisi?
- [ ] Türkçe arka etiket menşede uygulanabiliyor mu? (4.6)
- [ ] Marka/reçete IP sahipliği açıkça yazılmış mı? (4.9)
- [ ] Eksik alanlar `UNKNOWN` olarak mı işaretlendi, yoksa tahmin mi edildi?

**Eksik alan tahminle doldurulmaz. Takip sorusu gönderilir.**

---

## 3. TAKİP E-POSTASI — KISA ŞABLON

> Subject: Follow-up — RFQ <REF> — missing data points

Dear <NAME>,

Thank you for your reply. To be able to compare your offer with the others on a
like-for-like basis, we still need the following:

**Mandatory fields still outstanding** *(Summary Sheet rows)*:

- <S-ROW — FIELD — the exact format we need>
- <S-ROW — FIELD — the exact format we need>

Other outstanding items:

- <MISSING ITEM — RFQ question number>

Please note we would rather record "not available" than an estimate — an
approximate figure that later changes is worse for us than a blank. Equally,
"no" is a complete answer wherever the question is a yes/no one.

We would be grateful for these by **<DATE — 7 calendar days>**. After that date we
will have to evaluate your offer with those fields recorded as unknown, which in
the case of the packaging figures (bottle weight, case and pallet configuration)
means we cannot calculate a delivered cost for your product at all.

Kind regards,
<NAME>

> **İç not (gönderilmez):** Bu takip **bir kere** gönderilir. İkinci takip,
> tedarikçiyi fiyat yerine süreç konusunda eğitmeye başlar ve pazarlık
> pozisyonunu zayıflatır (`rfq-zorunlu-alanlar.md` §4.3/2).

---

## 4. SÜRÜM GEÇMİŞİ

| Sürüm | Tarih | Değişiklik | Ajan |
|---|---|---|---|
| v1.0 | 2026-08-09 (TUR 0) | İskelet oluşturuldu | kurulum |
| v2.0 | 2026-08-09 (TUR 1) | Gönderilebilir profesyonel taslağa dönüştürüldü; soru→CSV eşlemesi, ambalaj/palet bloğu, Model A/B ayrımı, IP sahipliği, takip şablonu eklendi | `global-sourcing-kasifi` |
| **v2.2** | **2026-08-10 (TUR 3A)** | **8 teknik alan zorunlu cevap alanına çevrildi (M1…M8):** ABV (S5), şişe ağırlığı+form (S7), koli konfigürasyonu (S8), palet konfigürasyonu (S9), sertifika seti (S23), Türkiye ihracat geçmişi (S24), **etiket uyarlama kabiliyeti (S26 — YENİ)**, **menşe belgesi kabiliyet+taahhüt (S27 — YENİ)**. SUMMARY SHEET S1–S25 → **S1–S27**; paralel liste yaratılmadı. **Eklendi:** §0 kural 13/14/15, `MANDATORY FIELDS` üretici kutusu (kabul formatı + reddedilen kelime listesi + cevapsızlık sonucu), 1.17 (şişe formu/çap/yükseklik), 6.13 (menşe taahhüdü OD-1…OD-4), 6.14 (fiyat düzeltme maddesi / OD-5), §2.0 zorunlu alan kapısı + çapraz tutarlılık kontrolü, takip e-postasına 7 gün süre ve zorunlu alan bloğu. **Genişletildi:** 1.4, 1.14, 1.15, 2.1–2.9, 4.6, 6.1, 6.3–6.6, 6.8–6.11 kabul formatı ile. Kural seti: `50-sourcing/rfq-zorunlu-alanlar.md`. Cevapsızlık/eleme kuralı **başkan onayı bekliyor** (`T-884`) | `global-sourcing-kasifi` |
| v2.1 | 2026-08-10 (TUR 1.5) | 25 zorunlu alan kontrolü yapıldı. **Eklendi:** SUMMARY SHEET (S1–S25), 1.14/1.15/1.16 şişe ağırlığı, 3.16 Incoterms® 2020 kabiliyeti, 3.17 lead time kırılımı (üretim süresi ayrı), 3.18 kuru malzeme birim maliyeti (**karton + etiket**, EXW'ye dahil mi sorusu ile), 3.19 koli konfigürasyonu değişim etkisi, 3.20 evrak ücretleri, 4.13 private label etiket maliyeti (tek seferlik + tekrarlayan), 4.14 markalı karton maliyeti, 4.15 klişe iptal ücreti. **Genişletildi:** soru→CSV+YAML eşleme tablosu, cevap değerlendirme kontrol listesi. Denetim: `50-sourcing/rfq-alan-kontrolu.md` | `global-sourcing-kasifi` |
