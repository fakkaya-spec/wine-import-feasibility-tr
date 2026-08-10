# RFQ RESPONSE SHEET — tedarikçinin dolduracağı yapılandırılmış sayfa

```yaml
belge:            rfq-response-sheet
sahibi:           global-sourcing-kasifi
tur:              TUR 3.25 §8 — SUPPLIER RFQ PAKETİ
tarih:            2026-08-10
temel:            50-sourcing/rfq-template.md v2.2 — SUMMARY SHEET S1–S27
zorunlu_alanlar:  M1…M8  (50-sourcing/rfq-zorunlu-alanlar.md)
ek_bloklar:       V (hacim merdiveni) · Q (iki kalite seviyesi) · PL (private label) ·
                  EB (existing brand) · OD (menşe belgesi) · SP (tedarikçiye özel tek soru)
gonderildi_mi:    HAYIR
dil:              İngilizce (gönderilecek kısım) — Türkçe satırlar İÇ NOTTUR
```

> ## ⛔ GÖNDERİLMEDİ
> Bu sayfa iki mail varyantının **ekidir**. Gönderim `T-885` onayına bağlıdır.

---

## 0. İÇ KULLANIM — YAPININ MANTIĞI (BU BÖLÜM GÖNDERİLMEZ)

### 0.1 Neden ayrı bir sayfa

Mail gövdesi **≤350 kelime** tutulmak zorundadır (§8). 27 satırlık SUMMARY
SHEET + hacim merdiveni + iki kalite seviyesi + private label bloğu bir mail
gövdesine sığmaz. Bu sayfa, v2.2'nin **S1–S27 yapısını aynen taşır** — yeni bir
paralel liste **yaratmaz** (`rfq-zorunlu-alanlar.md` §2 kuralı).

### 0.2 v2.2'ye göre **ne eklendi, ne değişti**

| Blok | v2.2'de | Bu sayfada |
|---|---|---|
| **S1–S27** | var | **birebir korundu** — numaralar değişmedi |
| **S10–S12 (MOQ + EXW + FOB)** | tek hacim | **V-bloğuna genişletildi**: 5 kademe × (EXW, FOB) |
| Kalite seviyesi | tek ürün | **Q-bloğu**: iki seviye (Q1 / Q2) — her biri kendi V-bloğunu doldurur |
| Private label detayı | 4.1–4.15 | **PL-bloğu** — özet tabloya taşındı |
| Existing brand detayı | 5.1–5.10 | **EB-bloğu** — özet tabloya taşındı |
| Menşe belgesi | S27 | **OD-bloğu** = S27, `OD-1…OD-5` taahhütleriyle **birebir** |
| 100.000 şişe | v2.2 soru 3.7'de vardı | **ÇIKARILDI** (§0 talimatı — ilk RFQ'da sorulmaz) |

### 0.3 Doldurma kuralı → CSV eşlemesi

`rfq-template.md` §0'daki soru → `tedarikci-havuzu.csv` → `tedarikci.yaml`
eşleme tablosu **değişmedi**; V-bloğunun her hücresi
`fiyat.hacim_bazli_fiyat_kirilimi.*` altına, Q1/Q2 ise **iki ayrı satır**
olarak `tedarikci-havuzu.csv`'ye girer (aynı tedarikçi, iki `supplier_sku` satırı).

### 0.4 §7 sızıntı denetimi

Bu sayfada **hiçbir** hedef fiyat, tavan, marj varsayımı, kanal marjı veya
tedarikçi sıralaması yoktur. Tek "sayısal beklenti" hacim kademeleridir ve
onlar **talep** değil **fiyat eğrisi sorusudur** — sayfada açıkça öyle yazar.

---
---

# 📄 GÖNDERİLECEK SAYFA — BURADAN AŞAĞISI EKE KOPYALANIR

# RFQ RESPONSE SHEET
### `<COMPANY>` — wine supply to Türkiye — reference `RFQ-TR-<YYYYMM>-<NN>`

Please complete every row. **`N/A`** if it does not apply to you, **`TBC`** if
you do not yet know. An honest `TBC` is more useful to us than an approximation.

**Eight rows are marked `[MANDATORY]`** (S5, S7, S8, S9, S23, S24, S26, S27).
Without them we physically cannot convert a price into a delivered cost, and
your offer cannot be compared with any other.

> **The following are not answers in a mandatory row:** *approximately · around ·
> circa · standard · usually · typically · varies · depends · upon request ·
> see attached spec (with nothing attached) · yes / possible (with no figure,
> unit or amount) · no problem.* A figure without its unit is also blank
> ("400" is not a weight).
>
> **"NO" and "N/A" are complete answers. Silence is not.** If you cannot issue
> a preferential origin document, cannot apply a Turkish back label, or have
> never exported to Türkiye — please say so plainly. It does **not** count
> against you.

---

## BLOCK Q — WE ASK FOR **TWO** QUALITY LEVELS

Please answer the whole sheet **twice**, once per column, or return two copies.

| | **Q1** | **Q2** |
|---|---|---|
| Definition | Your **cheapest commercially acceptable, export-ready** 750 ml still dry white | The **best-value option one level above** Q1 |
| Q-a Product / reference name | | |
| Q-b Grape variety or blend (% by variety) | | |
| Q-c Vintage quoted | | |
| Q-d Why you would recommend it for a value retail listing (1–2 lines) | | |

Acceptable varieties or an equivalent you recommend: **Chardonnay ·
Colombard-Chardonnay · Sauvignon Blanc · Verdejo · Airén-Chardonnay ·
Trebbiano** — or your own suggestion for the same position.

---

## BLOCK V — PRICE / VOLUME CURVE (**this is the core of our request**)

We are **not** asking for one price. We are asking how your price behaves with
volume. Please fill **every cell you can**; write `N/A` where a tier is below
your MOQ.

**Currency used in this block:** `____________`  (EUR / USD / other)

### V.1 — EXW price per 750 ml bottle · **EXW place: `_______________________`**

| Annual volume | Q1 — EXW / bottle | Q2 — EXW / bottle | Price per case | MOQ applying at this tier | Incoterm | Valid until |
|---|---|---|---|---|---|---|
| **5,000 bottles** | | | | | EXW | |
| **10,000 bottles** | | | | | EXW | |
| **25,000 bottles** | | | | | EXW | |
| **50,000 bottles** | | | | | EXW | |
| **1 × full 20' container** *(state how many bottles you load)* — `______ bottles` | | | | | EXW | |

### V.2 — FOB price per 750 ml bottle · **FOB named port: `_______________________`**

| Annual volume | Q1 — FOB / bottle | Q2 — FOB / bottle | Price per case | MOQ applying at this tier | Incoterm | Valid until |
|---|---|---|---|---|---|---|
| **5,000 bottles** | | | | | FOB | |
| **10,000 bottles** | | | | | FOB | |
| **25,000 bottles** | | | | | FOB | |
| **50,000 bottles** | | | | | FOB | |
| **1 × full 20' container** — `______ bottles` | | | | | FOB | |

> **V.1 and V.2 are different prices.** An EXW price must name the place of
> delivery; an FOB price must name the port. A single price with no Incoterm
> cannot be used by us at all.
>
> **V.3 — Is this quotation `INDICATIVE` or a `FIRM OFFER`?** ☐ INDICATIVE ☐ FIRM OFFER
> **V.4 — Are label and carton costs already inside the prices above?**
> Label: ☐ included ☐ charged separately · Carton: ☐ included ☐ charged separately
> **V.5 — CIF per bottle to Ambarlı / Mersin / İzmir, if you can quote it:** `________`

---

## BLOCK S — SUMMARY SHEET (S1–S27)

| # | Field | Unit / format required | Your answer |
|---|---|---|---|
| S1 | Winery / supplier legal name | text | |
| S2 | Product name / reference quoted | text (Q1 and Q2) | |
| S3 | Grape variety or blend | % by variety | |
| S4 | Vintage quoted | year | |
| **S5** | **ABV** `[MANDATORY]` | `__,_ % vol`, one decimal, **for the vintage quoted**; one line per vintage. Add: *"this is the figure that will be printed on the label: YES / NO"*. A range only if both ends are given **and** the upper end is stated as the contractual maximum | |
| S6 | Bottle size | ml (we require 750) | |
| **S7** | **Bottle weight and shape** `[MANDATORY]` | (a) empty glass `___ g` (± tolerance), (b) filled gross `___ g` (wine + glass + closure + capsule + labels), (c) shape (Bordeaux / Burgundy / Alsace / custom mould), (d) max body diameter `___ mm`, (e) total height `___ mm`. **All five.** | |
| **S8** | **Case configuration** `[MANDATORY]` | (a) bottles/case, (b) **external** case `L × W × H` **with unit** (internal not accepted), (c) gross `___ kg`, (d) net `___ kg`, (e) cases per layer × layers, (f) dividers/inserts YES/NO | |
| **S9** | **Pallet configuration** `[MANDATORY]` | (a) pallet type (EUR 800×1200 / 1000×1200 / GMA / other → mm), (b) **ISPM-15 heat treated YES/NO** + stamp present, (c) cases/pallet, (d) bottles/pallet, (e) layers, (f) loaded pallet gross `___ kg`, (g) **total loaded height `___ mm` incl. pallet**, (h) pallets **and** cases per 20' DV and per 40' HC, (i) floor-loading possible YES/NO + cases per 20' DV | |
| S10 | MOQ | (a) bottles per SKU, (b) containers per shipment | |
| S11 | EXW price per bottle | → **BLOCK V.1** (all five tiers) | see V.1 |
| S12 | FOB price per bottle | → **BLOCK V.2** (all five tiers) | see V.2 |
| S13 | Incoterms® 2020 rules you can trade under | list + your default + the one you recommend for Türkiye | |
| S14 | Port of loading | port name + country | |
| S15 | Lead time, PO → goods ready for loading | calendar days | |
| S16 | Of which: production / bottling time | calendar days | |
| S17 | Payment terms — **first** order | e.g. 50% T/T advance, balance against B/L | |
| S17b | Payment terms — **from the second order**, and after how many shipments | text + days | |
| S17c | If deferred payment is possible: days + any price surcharge per bottle | days + amount | |
| S18 | Private label available? | YES / NO → if YES complete **BLOCK PL** | |
| S18b | Existing-brand distribution available for Türkiye? | YES / NO → if YES complete **BLOCK EB** | |
| S19 | Label cost | one-off (artwork/plates) + per bottle or per 1,000; currency; **state whether already inside V.1** | |
| S20 | Carton / case cost | per bottle or per case; currency; **state whether already inside V.1** | |
| S21 | Samples | can send YES/NO; number of bottles; cost; days | |
| S22 | Annual capacity available to us | bottles/year | |
| **S23** | **Certificate set** `[MANDATORY]` | (a) analysis certificate — tick parameters **actually reported**: ☐ ABV ☐ total acidity ☐ volatile acidity ☐ residual sugar ☐ total SO₂ ☐ methanol ☐ density ☐ dry extract ☐ other ___; (b) **laboratory name** + accreditation (ISO 17025 / OIV); (c) issued per **BATCH** or per **PRODUCT**; (d) health / free sale certificate YES/NO + exact document name; (e) food safety ☐ BRCGS ☐ IFS ☐ ISO 22000 ☐ HACCP ☐ none → **attach a copy**; (f) traceability bottle lot → tank → harvest YES/NO | |
| **S24** | **Have you exported to Türkiye before?** `[MANDATORY]` | **YES / NO.** If YES: importer name, years `<yyyy>–<yyyy>`, annual volume. If NO: *"any additional condition you would require for a first shipment to Türkiye?"* YES/NO + explanation. **"We export to many countries" is not an answer.** | |
| S25 | Quotation type and validity | → **V.3** + valid until `<date>` | see V.3 |
| **S26** | **Label adaptation capability** `[MANDATORY]` *(capability, not cost — cost is S19)* | (a) can you **apply a Turkish-language back label at your own facility** from artwork we supply? YES/NO → if YES: cost per bottle + days added; (b) can you provide **at least 18 cm² of printable area** on the back label? YES/NO + current label size `mm × mm`; (c) can you leave a **blank area for an importer-applied strip/stamp**? YES/NO + area `mm × mm` + position on the bottle; (d) can you adapt the label to the importing country's mandatory statements (allergens, importer details, health warning)? YES/NO + revision turnaround in days; (e) can you print the ABV at **≥3 mm character height**? YES/NO | |
| **S27** | **Origin document — capability AND commitment** `[MANDATORY]` | → **BLOCK OD** | see OD |

> **S7, S8 and S9 must reconcile.** We cross-check:
> *(filled bottle weight × bottles per case) + packaging ≈ case gross weight*, and
> *(case gross weight × cases per pallet) + pallet ≈ loaded pallet gross weight.*
> If they do not reconcile we will come back to you rather than guess — please
> take the figures from your actual packaging specification sheet.

---

## BLOCK OD — ORIGIN DOCUMENT (= S27) `[MANDATORY]`

| # | Question | Your answer |
|---|---|---|
| **OD-a** | **Which document can you issue for shipments to Türkiye? Write the document name — "yes" is not an answer.** ☐ EUR.1 movement certificate ☐ invoice declaration ☐ REX statement on origin ☐ non-preferential certificate of origin only ☐ none | |
| **OD-b** | Will you **commit contractually to issuing it for every shipment**? YES / NO | |
| **OD-c** | Are you an **"approved exporter"**, and will you switch to a EUR.1 if the invoice-declaration value threshold is exceeded? YES / NO | |
| **OD-d** | Is the wine **wholly produced and bottled in the country of origin**, or does it contain **imported bulk wine**? NONE / YES → country + % | |
| **OD-e** | **From which country's port will the shipment physically leave**, and will it be consolidated in a third country on the way? port + country / no consolidation | |
| **OD-f** | Would you accept a **price-adjustment clause** for the case where the document cannot be issued or is rejected at import? YES / NO + on what terms | |

> **If your country has no preferential arrangement with Türkiye, "none" in OD-a
> is the correct and complete answer and costs you nothing.** We are not asking
> you to advise on Turkish duties — only to confirm which documents you can
> issue and whether you will commit to issuing them.

---

## BLOCK PL — PRIVATE LABEL *(complete only if S18 = YES)*

| # | Question | Your answer |
|---|---|---|
| PL-1 | **Private label MOQ** — per SKU **and** per shipment | |
| PL-2 | Is the private label MOQ different from your standard MOQ? By how much? | |
| PL-3 | **Is the wine included** in the price quoted in BLOCK V? YES / NO | |
| PL-4 | **Is the bottle included?** YES / NO + glass colour and mould reference | |
| PL-5 | **Is the closure included?** YES / NO + type (natural cork / technical cork / screw cap / synthetic) | |
| PL-6 | **Are the front and back labels included?** YES / NO | |
| PL-7 | **Is the carton included?** YES / NO — plain or printed; cost of a **printed/branded** carton per case + minimum print run | |
| PL-8 | **Design / artwork set-up fee** — one-off amount + currency; number of revisions included; working days per revision cycle | |
| PL-9 | **Printing plate / cliché / cutting-die set-up fee** — one-off amount + currency. *If you state that design is free, please confirm separately whether plates and dies are invoiced in addition.* | |
| PL-10 | **Turkish-language back label** applied at your facility? YES / NO + cost per bottle + days added *(same as S26a)* | |
| PL-11 | **Lead time** for private label, and how many **additional** days versus your standard product | |
| PL-12 | **Sample cost** — product + freight to Türkiye, and lead time for dispatch | |
| PL-13 | **Pre-production sample run** — minimum quantity of labelled bottles (e.g. 6–12) and cost | |
| PL-14 | **Annual minimum** you would require to keep the SKU open | |
| PL-15 | **Exclusivity** — would you undertake **not** to sell the same blend under another brand into Türkiye? YES / NO + conditions | |
| PL-16 | **Territory availability — Türkiye:** is Türkiye open for a private label programme? YES / NO / conditional → explain | |
| PL-17 | Who owns the **brand, the artwork and the blend recipe**? Please state explicitly. | |
| PL-18 | Can you adjust the blend / style to a target sensory profile? Minimum batch for a bespoke blend? | |
| PL-19 | Charge if we cancel or change artwork after plates are made | |
| PL-20 | Custom bottle mould, capsule colour, embossing or screen printing — availability and MOQ impact | |

---

## BLOCK EB — EXISTING BRAND DISTRIBUTION *(complete only if S18b = YES)*

| # | Question | Your answer |
|---|---|---|
| EB-1 | **Are Türkiye distribution rights available?** YES / NO | |
| EB-2 | **Do you already have an importer or distributor in Türkiye?** YES / NO → if YES, is the territory closed? | |
| EB-3 | Has this brand been **sold in Türkiye before**? By whom, in which years, at what volume, and why did it stop? | |
| EB-4 | **Is exclusivity possible?** YES / NO + term + conditions | |
| EB-5 | **Territory** offered (whole of Türkiye / part / channel-limited) | |
| EB-6 | **Minimum annual volume commitment** to obtain and to retain exclusivity | |
| EB-7 | **Annual MOQ** for the brand, and MOQ per SKU | |
| EB-8 | **Marketing obligations** you would place on the distributor (spend, activity, listings) | |
| EB-9 | **Your recommended export / resale price**, and do you impose a resale price or margin ceiling on the importer? | |
| EB-10 | **Distributor support offered** — budget, POS material, sampling stock, co-funding %, staff training | |
| EB-11 | **Sample availability** — how many bottles, cost, dispatch time | |
| EB-12 | Which of your existing SKUs are suitable for a **value retail** position in Türkiye? | |
| EB-13 | Notice period, termination conditions, treatment of unsold stock on termination | |
| EB-14 | Do you register your trademark in Türkiye, or is that the importer's responsibility? | |
| EB-15 | Price revision mechanism and frequency; notice period for a price increase | |

---

## BLOCK SP — ONE ADDITIONAL QUESTION FOR YOU

> `<TEDARİKÇİYE ÖZEL TEK CÜMLE — mail dosyalarının §1 tablosundan alınır>`

| Your answer |
|---|
| |

---

## BLOCK C — COMPANY

| # | Question | Your answer |
|---|---|---|
| C-1 | Legal company name, registration number, full address | |
| C-2 | Year established; ownership (family / cooperative / group) | |
| C-3 | Annual production capacity (bottles and litres) | |
| C-4 | Bottling line capacity (bottles/hour); owned or contracted | |
| C-5 | Storage capacity; temperature-controlled YES/NO | |
| C-6 | Two trade references in export markets we may contact | |
| C-7 | Name, position, direct e-mail and phone of the person responsible for this account | |

---

Please return this sheet with your answers, together with a current price list,
product technical sheets, a sample analysis certificate, a **packaging
specification sheet (case and pallet drawing)** and your food-safety
certificates. We are happy to sign a mutual non-disclosure agreement before you
share commercial terms.

# ⬆️ GÖNDERİLECEK SAYFA BURADA BİTER

---

## 1. İÇ NOT — BU SAYFANIN ZAYIF NOKTALARI

| # | Zayıflık | Etki |
|---|---|---|
| 1 | **Sayfa uzun.** Q × V matrisi tek başına 10 fiyat hücresi, S bloğu 28 satır, PL 20 satır | `rfq-alan-kontrolu.md` §5.1'in uyarısı burada da geçerli: uzun form **cevap oranını düşürür**. Ölçülecek metrik `rfq-zorunlu-alanlar.md` §4.4'tedir |
| 2 | **İki kalite seviyesi (Q1/Q2) cevap yükünü iki katına çıkarır** | Tedarikçi büyük olasılıkla yalnızca Q1'i dolduracaktır; bu **bir veri değil, bir sinyaldir** ve öyle kaydedilmelidir |
| 3 | **V bloğu MOQ'nun altındaki kademeleri de soruyor** | 6.000 MOQ'lu bir üreticiye 5.000 sorulması "ciddiyetsiz alıcı" izlenimi verebilir; bu yüzden satırda açıkça *"write N/A where a tier is below your MOQ"* denmiştir |
| 4 | **`RFQ-TR-<YYYYMM>-<NN>` referans numarası henüz tanımsız** | Numaralandırma şeması başkan onayıyla sabitlenmeli; yoksa gelen cevaplar eşleştirilemez |
| 5 | **PL-16 (territory availability Türkiye) private label'da alışılmadık bir sorudur** | Cantina Danese örneği (`T-565`) bunun **gerçek** bir risk olduğunu gösterdi: üreticinin Türkiye'de mevcut markası, private label işini kısıtlayabilir |
