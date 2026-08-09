# RFQ TEMPLATE — Request for Quotation

> **Sahibi:** `global-sourcing-kasifi`
> **Sürüm:** v2.0 — TUR 1'de gönderilebilir profesyonel taslağa dönüştürüldü
> **Durum:** `READY_TO_SEND` (içerik olarak). **BU TURDA GÖNDERİLMEDİ VE GÖNDERİLMEZ.**
> Fiili gönderim yalnızca karar `TEST` veya `IMPORT PILOT` ise, TUR 7'de yapılır.
>
> `<>` içindeki alanlar gönderim öncesi doldurulur. Doldurulmadan gönderilirse RFQ geçersizdir.

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

### Soru → CSV kolonu eşlemesi (denetim için)

| RFQ sorusu | `tedarikci-havuzu.csv` kolonu |
|---|---|
| 1.2 | `grape_blend` |
| 1.3 | `vintage` |
| 1.4 | `abv_pct` |
| 1.7 | `volume_ml` |
| 2.1 | `bottles_per_case` |
| 2.2 | `case_gross_weight_kg` |
| 2.3 | `case_dims_cm` |
| 2.5 | `cases_per_pallet` |
| 2.7 | `pallet_gross_weight_kg` |
| 3.1 | `price_value` + `price_currency` (incoterm = EXW) |
| 3.2 | `price_value` + `price_currency` (incoterm = FOB) |
| 3.4 | `quote_type` |
| 3.5 | `quote_valid_until` |
| 3.6 | `moq_bottles`, `moq_containers` |
| 3.8 / 3.9 | `payment_terms`, `payment_days` |
| 3.10 | `lead_time_days` |
| 3.11 | `annual_capacity_bottles` |
| 4.1 / 4.2 | `private_label_capable` |
| 4.4 / 4.5 | `label_customization` |
| 6.1 | `origin_proof_doc` |
| 6.2 | `analysis_certificates` |
| 6.6 | `exported_to_turkey_before` |
| 6.7 | `export_markets` |
| 7.1 | `sample_sent` |

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

### 1. Product specification

| # | Question | Your answer |
|---|---|---|
| 1.1 | Product name / internal reference | |
| 1.2 | Grape variety or exact blend composition (% by variety) | |
| 1.3 | Vintage(s) currently available and approximate stock per vintage | |
| 1.4 | **ABV (% vol)** — please state the exact figure that will appear on the label | |
| 1.5 | Residual sugar (g/L) | |
| 1.6 | Total acidity (g/L) and pH | |
| 1.7 | Bottle volume — we require **750 ml**. Confirm availability. | |
| 1.8 | Bottle type/mould, glass colour and **empty bottle weight (g)** | |
| 1.9 | Closure type (natural cork / technical cork / screw cap / synthetic) | |
| 1.10 | Total sulphur dioxide level (mg/L) | |
| 1.11 | Is the wine fined with animal-derived agents? (vegan status) | |
| 1.12 | Recommended shelf life from bottling (months) | |
| 1.13 | Is the wine produced from your own vineyards, purchased grapes, purchased must, or purchased finished wine? | |

### 2. Packaging and logistics data — **mandatory for container and freight calculation**

| # | Question | Your answer |
|---|---|---|
| 2.1 | Bottles per case | |
| 2.2 | Case **gross** weight (kg) and net weight (kg) | |
| 2.3 | Case external dimensions L × W × H (cm) | |
| 2.4 | Cases per layer × number of layers per pallet | |
| 2.5 | **Cases per pallet** and bottles per pallet | |
| 2.6 | Pallet type (EUR 120×80 / industrial 120×100 / other) and whether heat-treated (ISPM-15) | |
| 2.7 | Pallet **gross** weight (kg) and total pallet height (cm) | |
| 2.8 | Maximum number of cases you load into a **20' DV** and into a **40' HC** | |
| 2.9 | Can you load floor-loaded (non-palletised)? If yes, cases per 20' DV. | |
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

### 4. Model B — Private label

| # | Question | Your answer |
|---|---|---|
| 4.1 | Do you produce under a customer's own brand? | |
| 4.2 | **Minimum order quantity for private label**, per SKU and per shipment | |
| 4.3 | Is the private label MOQ different from your standard MOQ? By how much? | |
| 4.4 | Can you adjust the blend / style to a target sensory profile? What is the minimum batch for a bespoke blend? | |
| 4.5 | Do you print and apply labels in-house, or through a third party? | |
| 4.6 | Can you apply a **Turkish-language back label** at your facility, using artwork we supply? | |
| 4.7 | Number of label revisions / mock-ups included, and any one-off artwork or plate/cliché charge | |
| 4.8 | Custom bottle mould, capsule colour, embossing or screen printing — availability and MOQ impact | |
| 4.9 | Who owns the brand, the artwork and the blend recipe? Please state explicitly. | |
| 4.10 | Would you undertake **not** to sell the same blend under another brand into Türkiye? | |
| 4.11 | Additional lead time for private label versus your standard product (days) | |
| 4.12 | Minimum quantity for a **pre-production sample run** (e.g. 6–12 labelled bottles) | |

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
| 6.1 | Can you issue a **preferential origin proof** for Türkiye — EUR.1 movement certificate, invoice declaration, REX statement on origin, or A.TR? Please state exactly which. | |
| 6.2 | Can you issue a non-preferential **Certificate of Origin** (chamber of commerce certified)? | |
| 6.3 | Analysis certificate — which parameters are included (ABV, total/volatile acidity, RS, total SO₂, methanol, density, dry extract)? | |
| 6.4 | Which laboratory issues it, and is it accredited (ISO 17025 / OIV method)? | |
| 6.5 | Can you provide a **health / free sale certificate** issued or endorsed by your national authority? | |
| 6.6 | **Have you exported to Türkiye before?** If yes: which importer, which years, what annual volume? | |
| 6.7 | Which export markets do you currently serve, and what is your total annual export volume? | |
| 6.8 | Can you adapt the label to the importing country's legal requirements (mandatory statements, allergen declaration, importer details, health warnings)? | |
| 6.9 | Are you able to leave a defined blank area on the label or bottle for an importer-applied stamp/strip? | |
| 6.10 | Food safety / quality certifications held (BRCGS, IFS, ISO 22000, HACCP) — please attach certificates | |
| 6.11 | Traceability: can you supply batch-level records linking bottle lot → tank → harvest? | |
| 6.12 | Do you hold liability insurance covering exported product? | |

> **Note to supplier:** we ask about origin documentation because the importing
> country's treatment of the consignment depends on it. We are **not** asking you to
> advise on Turkish duties or taxes — only to confirm which documents you can issue.

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
document with your answers inserted, together with:

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

- <MISSING ITEM 1 — RFQ question number>
- <MISSING ITEM 2 — RFQ question number>

Please note we would rather record "not available" than an estimate — an
approximate figure that later changes is worse for us than a blank.

Kind regards,
<NAME>

---

## 4. SÜRÜM GEÇMİŞİ

| Sürüm | Tarih | Değişiklik | Ajan |
|---|---|---|---|
| v1.0 | 2026-08-09 (TUR 0) | İskelet oluşturuldu | kurulum |
| v2.0 | 2026-08-09 (TUR 1) | Gönderilebilir profesyonel taslağa dönüştürüldü; soru→CSV eşlemesi, ambalaj/palet bloğu, Model A/B ayrımı, IP sahipliği, takip şablonu eklendi | `global-sourcing-kasifi` |
