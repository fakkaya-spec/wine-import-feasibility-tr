# FORWARDER RFQ — gönderime hazır İngilizce kotasyon talebi

```yaml
sahibi:                navlun-lojistik-uzmani
tur:                   TUR 3.25 — FORWARDER RFQ PAKETI (§9, §10, §15)
tarih:                 2026-08-10
durum:                 HAZIR — GONDERILMEDI
dis_iletisim_yapildi:  false
mesaj_gonderildi:      false
hedef_ticket:          T-304 (CRITICAL, OPEN) · G2-L gate
ek_dosyalar:
  - 40-lojistik/forwarder-contact-pack.md      # kime
  - 40-lojistik/forwarder-response-sheet.md    # nasil cevaplanacak (EK-1)
surum:                 v1.0
```

> ## ⛔ BU TURDA HİÇBİR FORWARDER'A TEMAS EDİLMEDİ
>
> Bu dosya bir **taslak metindir**, bir gönderim kaydı değildir. Hiçbir
> e-posta, form veya mesaj gönderilmemiştir. Gönderim, **kurucunun açık
> onayı** (preview + onay) olmadan yapılamaz.
>
> **Gönderim ön koşulları:**
> 1. Kurucu/başkan **preview onayı** (bu metnin kendisi görülerek),
> 2. `<PLACEHOLDER>` alanlarının doldurulması (firma adı, imza, hacim, tarih),
> 3. `50-sourcing` tarafından **koli formatı** (`T-302`) teyidi — teyit
>    gelmeden gönderilirse teklif bizim varsayımımıza bağlı kalır (§2 uyarısı).
>
> **Ön koşul 3 sağlanmasa da RFQ gönderilebilir** — ama o zaman §2'deki
> `ASSUMPTION` bloğu metinden **çıkarılmaz**; forwarder teklifini o varsayıma
> koşullamak zorunda kalır. Bu bilinçli bir tasarımdır.

---

## 0. BU RFQ NEYİ ÇÖZMEK İÇİN YAZILDI

| Açık kayıt | RFQ'nun hangi bölümü kapatır |
|---|---|
| `T-304` çekirdeği — **FCL navlunu 14 lane'in 14'ünde UNKNOWN** (`EV-2026-08-10-312`) | §4 Block A/B/C, 20DV + 40HC satırları |
| `C-311` — FCL base ocean 300 vs 1.200 USD (4–5 kat çelişki) | §5 kalem dökümü + §6 excluded charges |
| `T-312` — İspanya dışı **6 menşenin origin charge'ları** UNKNOWN | §5.2 "published local charges tariff" talebi |
| `T-913` Ayak A — LCL kotasyonları **2026-08-16'da STALE** | §8 validity + §4 LCL satırları (yazılı, tarihli kotasyon) |
| `karayolu_agirlik.cekici_sasi_darasi_kg` — **ASSUMPTION, kanıt yok** | §7 tractor+chassis tare + max payload talebi |
| `C-301` — palet/konteyner sayısı çelişkisi (9 mu 10 mu) | EK-1 §A "number of pallets" zorunlu alanı |
| `OQ-2501` — LCL fiyatına **CFS dahil mi** | §5.1 kalem listesi + §6 |
| `sicaklik_riski.thermal_liner_ek_maliyet` — UNKNOWN | §9 opsiyon fiyatlaması |
| `sigorta` — Türk/uluslararası **gerçek prim** UNKNOWN | §9 opsiyon fiyatlaması (hesap bizde değil) |

---

## 1. GÖNDERİM KURALLARI (Türkçe — bu bölüm gönderilmez)

1. **Metin aynen gönderilir.** Kalem listesi kısaltılamaz; kısaltılırsa
   `T-304`'ün kapanma koşulu (kalem dökümlü yazılı kotasyon) sağlanmaz.
2. **EK-1 (response sheet) mutlaka eklenir.** Serbest formatta gelen cevap
   karşılaştırılamaz.
3. **En az 3, tercihen 5 forwarder'a aynı anda ve aynı metinle** gönderilir.
   Farklı metin → karşılaştırılamaz teklif.
4. Gelen her teklif **kanıt kartına** dönüştürülür (`tier: T4`,
   `ttl: teklifin kendi validity süresi`), `99-ops/veri-tazeligi.md`'ye eklenir.
5. **Tek bir "all-in" rakam gelirse o rota için "kotasyon alınamadı" yazılır.**
   Bu kural §5.3'te forwarder'a da açıkça bildirilmiştir.

---

# ▼▼▼ GÖNDERİLECEK METİN — İNGİLİZCE ▼▼▼

*(Aşağıdaki bölüm, `<PLACEHOLDER>` alanları doldurulduktan sonra olduğu gibi
gönderilir. Türkçe açıklamalar bu çizginin üstünde kalır.)*

---

**Subject:** RFQ — Ocean freight quotation, bottled wine, multiple origins → Turkey (LCL / 20DV / 40HC) — itemised breakdown required

**To:** `<FORWARDER CONTACT>`
**From:** `<COMPANY NAME>` · `<CONTACT NAME>`, `<TITLE>` · `<EMAIL>` · `<PHONE>`
**Date:** `<SEND_DATE>`
**Our reference:** `<RFQ_REF>`
**Response requested by:** `<RESPONSE_DEADLINE>`

---

## 1. WHO WE ARE AND WHAT THIS IS

We are `<COMPANY NAME>`, a `<Turkey-based>` company currently completing the
feasibility study for a **commercial import programme of bottled still wine
into Turkey**. We are at the stage where indicative desk research must be
replaced by **written, dated, itemised quotations**.

This is a **request for quotation, not a booking**. No obligation arises for
either side. We will, however, use the quotations received as the freight
basis of an investment decision, so we need them to be **complete and
comparable** rather than fast.

We are contacting a small number of forwarders in parallel with **identical
wording**, so that the offers can be compared line by line.

---

## 2. CARGO — AND AN EXPLICIT WARNING ABOUT OUR ASSUMPTIONS

**Commodity:**

```
Commodity      : 750 ml bottled still wine, glass bottles
Packing        : cartons on pallets (or floor-loaded — please quote both, see §3)
Nature         : NON-HAZARDOUS. Not IMO/DG. Not temperature-controlled by default.
Purpose        : commercial import to Turkey (duty-paid / bonded warehouse route)
HS code        : to be confirmed by our customs broker before booking
                 (2204.21 expected; this RFQ does not depend on it)
Incoterm       : quote on FOB / FCA basis unless stated otherwise per lane
```

> ### ⚠ THE FOLLOWING CARGO FIGURES ARE **ASSUMPTIONS**, NOT CONFIRMED SUPPLIER DATA
>
> Our supplier configuration is **not yet fixed**. The case format (6 × 750 ml
> vs 12 × 750 ml), the exact bottle dimensions and the glass weight are still
> open. The figures below are derived from published pallet specifications and
> are used **only so that you can quote something concrete**.
>
> **Please quote on the basis below, and please state in your offer the case
> weight, pallet weight and number of pallets you actually used.** If your
> quotation depends on these figures, we need to know it now — because when the
> supplier confirms the real configuration, your quotation may have to change.
> We would rather see a conditional quotation than an unconditional one that
> silently breaks later.

**Assumed packing (please confirm or correct):**

| Parameter | Value used | Basis |
|---|---|---|
| Bottle, packed (incl. carton share) | **1.26 kg** (range 1.21 – 1.38) | derived |
| Bottle, packed volume | **0.00223 – 0.00239 m³** | 12-pack / 6-pack |
| Case, 12 × 750 ml — gross weight | **15.1 kg** (range 13.6 – 18.0) | derived |
| Case, 12 × 750 ml — volume | **≈ 0.0268 m³** | derived |
| Case, 6 × 750 ml — gross weight | **7.59 kg** | derived |
| Pallet type A | standard **1200 × 1000 mm**, 4 layers | — |
| Bottles per standard pallet | **720** (60 cases of 12) | — |
| Gross weight per loaded standard pallet | **927 kg** | — |
| Loaded pallet height | **1,480 mm** (incl. pallet) | 4 layers |
| Pallet type B | **EUR 1200 × 800 mm**, 4 layers | alternative |
| Bottles per EUR pallet | **576** (48 cases of 12) | — |
| Gross weight per loaded EUR pallet | **≈ 745 kg** | derived |

**Assumed shipment sizes (per shipment, one origin, one destination):**

| Quote type | Bottles | Cargo volume | Cargo gross weight | Notes |
|---|---|---|---|---|
| **LCL** | **5,000** | **11.2 – 12.0 m³** loose cases · **≈ 12.4 m³** if palletised (7 std pallets) | **≈ 6,300 kg** | density ≈ 0.53 t/m³ → volume-based, not weight-based |
| **20DV FCL — palletised** | 6,480 – 7,200 | 9 – 10 std pallets | 8,350 – 9,270 kg | pallet count is exactly what we want you to confirm |
| **20DV FCL — floor loaded** | 11,800 – 13,700 | full | 14,870 – 17,260 kg | |
| **40HC FCL — palletised** | 14,400 – 15,120 | 20 – 21 std pallets | 18,540 – 19,470 kg | |
| **40HC FCL — floor loaded** | 19,100 – 21,500 | full | 24,070 – 27,090 kg | see §7 — Turkish road weight limit |

**Please state clearly on which of these bases you priced.** If you believe a
figure is wrong (for example, if you load 11 pallets in a 20DV, or if you would
never floor-load glass), please say so — a correction from you is more valuable
to us than a quotation that silently assumes something else.

**LCL charging basis question (please answer explicitly):** for the LCL
shipment, do you charge on **loose case volume (11.2 – 12.0 m³)** or on
**palletised footprint volume (≈ 12.4 m³)**? The difference is roughly 5–10 %
of the freight and we cannot infer it from a lump sum.

---

## 3. WHAT WE ARE ASKING FOR — THREE SEPARATE QUOTATIONS

Please quote the following **three shipment types separately**. Do not merge
them and do not quote only the one you consider most likely.

| # | Quote type | Basis |
|---|---|---|
| **Q1** | **LCL** | 5,000 bottles ≈ 11.2 – 12.4 m³ / ≈ 6,300 kg |
| **Q2** | **20' Dry Van (20DV) FCL** | one container, palletised **and** floor-loaded if the price differs |
| **Q3** | **40' High Cube (40HC) FCL** | one container, palletised **and** floor-loaded if the price differs |

---

## 4. ROUTES — PLEASE QUOTE PER LANE

### Block A — PRIORITY ORIGINS → İSTANBUL *(mandatory: this block is the core of the RFQ)*

Discharge: **Ambarlı / İstanbul** (Kumport, Marport or Mardaş — please state which terminal you would use).

| Lane | Origin port(s) | Q1 LCL | Q2 20DV | Q3 40HC |
|---|---|---|---|---|
| A1 | **Valencia (ESVLC)** and/or **Barcelona (ESBCN)**, Spain | ☐ | ☐ | ☐ |
| A2 | **Lisboa (PTLIS)** and/or **Leixões (PTLEI)**, Portugal | ☐ | ☐ | ☐ |
| A3 | **Genova (ITGOA) / La Spezia (ITSPE) / Livorno (ITLIV) / Napoli (ITNAP)**, Italy | ☐ | ☐ | ☐ |
| A4 | **San Antonio (CLSAI)** and/or **Valparaíso (CLVAP)**, Chile | ☐ | ☐ | ☐ |
| A5 | **Cape Town (ZACPT)**, South Africa | ☐ | ☐ | ☐ |

> **Italy is our single largest information gap.** No public quotation exists
> for any Italian port to Turkey in the sources we could access. Even a
> "we do not serve this lane" answer for A3 is useful to us — please do not
> leave it blank.

### Block B — ALTERNATIVE TURKISH DISCHARGE PORTS *(high value)*

For **Spain (A1)** and **Italy (A3)** only, please also quote:

| Lane | Origin | Discharge | Q2 20DV | Q3 40HC |
|---|---|---|---|---|
| B1 | Spain | **Aliağa / İzmir** | ☐ | ☐ |
| B2 | Spain | **Mersin** | ☐ | ☐ |
| B3 | Italy | **Aliağa / İzmir** | ☐ | ☐ |
| B4 | Italy | **Mersin** | ☐ | ☐ |

We are comparing discharge ports economically. Our own desk work suggests the
**terminal tariff difference between Turkish ports is small relative to inland
haulage**, so please quote the sea leg cleanly and let us do that comparison —
but if you see a routing reason why one discharge port is materially better for
a given origin, please tell us.

### Block C — SECOND-PRIORITY ORIGINS → İstanbul *(optional but welcome)*

| Lane | Origin port(s) | Q1 LCL | Q2 20DV | Q3 40HC |
|---|---|---|---|---|
| C1 | **Marseille / Fos (FRMRS)**, France | ☐ | ☐ | ☐ |
| C2 | **Melbourne (AUMEL)**, Australia | ☐ | ☐ | ☐ |
| C3 | **Oakland (USOAK)** and/or **Los Angeles (USLAX)**, USA (California) | ☐ | ☐ | ☐ |

**If you cannot serve a lane, please write "not served" rather than omitting the
row.** A blank row is ambiguous; "not served" is information.

---

## 5. HOW THE PRICE MUST BE PRESENTED — ITEMISED, PER LANE

### 5.1 Mandatory line items

For **every lane and every container type quoted**, please state each of the
following as a **separate amount with its own currency**:

| # | Line item |
|---|---|
| 1 | **Ocean freight (base)** — excluding all surcharges |
| 2 | **Surcharges applied to the base** — BAF / CAF / ETS / PSS / war risk / peak season, each named separately with its current amount and its adjustment mechanism |
| 3 | **Origin charges** — full list |
| 4 | **THC origin** |
| 5 | **Documentation fee** |
| 6 | **B/L fee** (and whether EDI or manual SI pricing applies) |
| 7 | **Destination THC** |
| 8 | **Destination charges** — full list (incl. delivery order / ordino, terminal handling, drop-off, ISPS/security if any) |
| 9 | **Customs-related carrier charges** — anything the carrier or you invoice in connection with customs formalities (this is **not** a request for customs brokerage; we have our own broker) |
| 10 | **Demurrage free time** (days, and from which event it starts) |
| 11 | **Detention free time** (days, and from which event it starts) |
| 12 | **Demurrage and detention daily rates** after free time, by tier |
| 13 | **Transit time** (port to port, in days) |
| 14 | **Routing** — full sea/land routing as you would actually move it |
| 15 | **Transshipment** — yes/no, and at which port(s), and how many times the box is handled |
| 16 | **Validity** — from date, to date |
| 17 | **Spot or contract rate** — say which |
| 18 | **Container type** offered and **maximum payload** of that equipment |
| 19 | **Insurance — optional price** (see §9) |
| 20 | **Sailing frequency** (weekly / fortnightly / etc.) and the next 2–3 realistic sailing dates |

### 5.2 Please also attach your published local charges tariff

If you or your carrier publish a **local charges tariff** for any of the origin
countries in §4 (Spain, Portugal, Italy, Chile, South Africa, France,
Australia, USA), please attach it. For most origins in this RFQ we have **no
origin-charge data at all**, and a published tariff sheet closes that gap far
better than a single quoted figure.

### 5.3 **A SINGLE "ALL-IN" NUMBER WILL NOT BE ACCEPTED**

> **Please do not answer with one all-in figure.**
>
> If a lane is quoted as a single lump sum without the breakdown in §5.1, we
> will record that lane as **"no quotation received"** and it will not enter our
> comparison. This is not a negotiating posture — it is a data-quality rule we
> have written into our own methodology.
>
> **The reason, concretely:** in our desk research on the Spain → Turkey lane,
> the *published* origin local charges alone (Terminal Handling EUR 287 +
> B/L EUR 62 = **EUR 349 minimum per container**, rising to ≈ EUR 554 with
> optional items) **exceeded the lower end of the indicative base ocean freight
> for the same lane** (≈ USD 300). We also found published indications for the
> same lane ranging from ≈ USD 295 to EUR 2,500 — a four- to five-fold spread —
> which we believe is largely explained by some figures being base ocean freight
> and others being quasi-all-in.
>
> An all-in number hides exactly the structure we need to see, and makes two
> forwarders' offers mathematically incomparable. **We would rather receive an
> honest, itemised, expensive quotation than a cheap-looking single number.**

---

## 6. EXCLUDED CHARGES — PLEASE STATE THEM EXPLICITLY

Please include a section headed **`EXCLUDED CHARGES`** listing everything that
is **not** in your quoted amounts, including but not limited to:

- customs duties, VAT, excise and any other Turkish import taxes
- customs brokerage and declaration fees
- terminal storage / demurrage / detention beyond free time
- inspection, scanning (X-ray), sampling, laboratory analysis
- bonded warehouse (antrepo) entry, storage, handling and exit
- devanning / unstuffing and re-palletising
- inland haulage in Turkey
- cargo insurance (unless quoted as an option under §9)
- any charge that is subject to change between quotation and booking

If a line item in §5.1 is **included** in another line, please say so
explicitly (e.g. *"terminal security fee is included in THC origin"*) rather
than omitting it. Silence is our biggest source of error.

---

## 7. EQUIPMENT, PAYLOAD AND THE TURKISH ROAD WEIGHT LIMIT *(important)*

For each container type quoted, please state:

1. **Maximum payload** of the equipment you would supply (kg).
2. **Container tare weight** (kg).
3. The **tractor + chassis tare weight** (kg) that your Turkish haulage partner
   typically uses for a container move from the discharge port.
4. The **maximum cargo weight** you can legally deliver by road in Turkey for
   a 20DV and for a 40HC, given the **44-tonne gross combination weight limit**
   applicable to ISO-container road transport in Turkey.

**Why we ask:** for a 40HC our loading plan is limited by the Turkish road
weight limit rather than by the container's own payload. We currently have to
*assume* a tractor+chassis tare of 13–16 tonnes and we have no evidence for
that figure. It directly determines how many bottles we can put in a 40HC, and
therefore our cost per bottle. **A single number from you removes an assumption
from our model.**

Please also confirm whether an **overweight / heavy-load surcharge** applies at
any of the cargo weights in §2, and at what threshold.

---

## 8. VALIDITY, RATE TYPE AND FX

Please state:

- **Validity period** of each quoted rate (from / to). If your rates are
  valid for less than 14 days, please say so plainly — we need to know the
  shelf life of the number, not just the number.
- Whether the rate is **spot** or **contract**, and if contract, the minimum
  volume commitment that would be required.
- The **currency** of each line, and whether any line is converted at a rate
  you set (and if so, which rate and when it is fixed).
- The **adjustment mechanism** for BAF / ETS / CAF: fixed for the validity
  period, or updated monthly/quarterly? If it can move during the validity
  period, the quotation is not really fixed and we need that stated.
- Whether a **rate increase (GRI/PSS)** is currently announced on any of these
  trades for the next 60 days.

---

## 9. OPTIONS — PLEASE PRICE SEPARATELY, DO NOT BUNDLE

| Option | What we need |
|---|---|
| **Cargo insurance** | Premium rate (%) on **CIF + 10 %**, cover basis (we require ICC (A) **including breakage** and, for long-transit lanes, temperature/thermal damage), deductible/excess, and any exclusions for glass or for wine specifically. Please quote it as a **separate, optional price** — we will decide separately whether to buy it from you. |
| **Reefer container** | Price premium vs dry container, per lane, plus the destination terminal storage tariff difference for a reefer box in Turkey. |
| **Thermal liner / insulated liner (dry box)** | Unit price per container, expected internal temperature performance, and which lanes you would recommend it on. |
| **Palletised vs floor-loaded** | Freight difference, plus your view on breakage risk for glass in a floor-loaded box, and whether you would decline to carry it floor-loaded. |
| **Devanning / unstuffing at destination** | Price per 20DV / 40HC, and whether you can deliver directly into a **bonded warehouse (antrepo)** in İstanbul / İzmir / Mersin. |
| **Bonded warehouse (antrepo)** | If you operate or partner with one: entry handling, storage per pallet per day, exit handling, minimum storage period, and whether the facility is licensed for **alcoholic beverages**. |
| **Summer sailing** | Any seasonal recommendation or restriction you apply to wine in dry containers between June and September. |

---

## 10. TIMING QUESTIONS

1. **Transit time** per lane, port to port (§5.1 item 13).
2. For LCL: **consolidation waiting time** at origin — how many days does cargo
   typically wait at the origin CFS before the box sails?
3. Typical **port-to-gate time** at the Turkish discharge terminal (vessel
   berthing → container available for pick-up).
4. If our cargo has to wait in Turkey for a **regulatory/licensing step of 15,
   30 or 60 days before it can leave a bonded warehouse**, what would you
   recommend operationally, and what would it cost? *(We are trying to price
   the risk of a licensing delay; we are not asking for legal advice.)*

---

## 11. HOW TO REPLY

Please reply **using the attached response sheet (EK-1)**, or reproduce its
structure in your own format. A quotation that follows the sheet can be
compared line by line against the others we receive; one that does not, cannot.

Please send your reply to `<EMAIL>` by **`<RESPONSE_DEADLINE>`**. If you cannot
meet that date, a short note telling us when you can is genuinely helpful.

We are happy to answer questions about the cargo, and if your operational
experience contradicts any assumption in §2, **please tell us** — that
correction is worth more to us than a lower price.

Thank you for your time.

`<CONTACT NAME>`
`<TITLE>` · `<COMPANY NAME>`
`<EMAIL>` · `<PHONE>`

---

*This request for quotation creates no obligation for either party. Information
you provide will be used for internal feasibility evaluation only and will not
be shared with your competitors. If any part of your quotation is confidential,
please mark it as such.*

# ▲▲▲ GÖNDERİLECEK METNİN SONU ▲▲▲

---

## 12. METİN İSTATİSTİĞİ VE İZLENEBİLİRLİK *(gönderilmez)*

| Ölçüm | Değer |
|---|---|
| Gönderilecek İngilizce metin | **§1–§11 arası (başlıktan imzaya)** |
| Kelime sayısı — tablolar dâhil toplam | **2.889 kelime** |
| Kelime sayısı — yalnızca düz metin (tablo satırları hariç) | **1.820 kelime** |
| Zorunlu kalem sayısı (§5.1) | **20** |
| Fiyat istenen lane sayısı | Block A 5 · Block B 4 · Block C 3 = **12 lane** |
| Fiyat istenen lane × mod kombinasyonu | Block A 5×3 = 15 · Block B 4×2 = 8 · Block C 3×3 = 9 = **32** |
| Zorunlu (Block A) kombinasyon | **15** |
| `<PLACEHOLDER>` sayısı | 9 (`COMPANY NAME`, `CONTACT NAME`, `TITLE`, `EMAIL`, `PHONE`, `SEND_DATE`, `RFQ_REF`, `RESPONSE_DEADLINE`, `FORWARDER CONTACT`) |

### Metindeki `ASSUMPTION` bloklarının kaynakları

| RFQ'daki varsayım | Kaynak kanıt | Repo statüsü |
|---|---|---|
| Paketli şişe 1,26 kg | `EV-2026-08-09-307` | ESTIMATE |
| Paketli şişe 0,00223–0,00239 m³ | `EV-2026-08-09-307` | ESTIMATE |
| 12'li koli 15,1 kg | `EV-2026-08-09-306` | ESTIMATE |
| 6'lı koli 7,59 kg | `EV-2026-08-09-307` | ESTIMATE |
| Std palet 720 şişe / 927 kg / 1.480 mm | `EV-2026-08-09-307` | FACT (spec) |
| EUR palet 576 şişe / ~745 kg | `EV-2026-08-09-307` + türetme (927 − 60×15,1 = 21 kg palet darası) | ESTIMATE |
| 20DV 9–10 palet, 40HC 20–21 palet | `EV-2026-08-09-308` | **CONFLICT `C-301`** — bu yüzden forwarder'a soruluyor |
| 20DV/40HC şişe kapasiteleri | `EV-2026-08-09-320`, `-321` | ESTIMATE |
| 44 t karayolu limiti | `EV-2026-08-09-310` | FACT (T2) |
| Çekici+şasi darası 13–16 t | — | **ASSUMPTION, kanıt YOK** → §7 bunu kapatmak için var |
| İspanya origin 349–554 EUR (§5.3'te kullanıldı) | `EV-2026-08-10-313`, `-314` | FACT (T3) |
| İspanya base ocean ≈300 USD / 295–2.500 spread (§5.3) | `EV-2026-08-10-322`, `-324` | ESTIMATE, `C-311` |

> **Not:** §5.3'te forwarder'a söylenen iki sayı (EUR 349 ve ≈USD 300) bizim
> **kanıtlı** verimizdir ve bilinçli olarak paylaşılmıştır. Bu bir pazarlık
> kozu değil, **teklifin doğru formatta gelmesini sağlayan gerekçedir.**
> Tedarikçi fiyatı, hedef hacim ve marj beklentisi **paylaşılmamıştır.**
