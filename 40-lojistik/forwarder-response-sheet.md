# FORWARDER RESPONSE SHEET (EK-1) — forwarder'ın dolduracağı yapılandırılmış sayfa

```yaml
sahibi:        navlun-lojistik-uzmani
tur:           TUR 3.25 — FORWARDER RFQ PAKETI
tarih:         2026-08-10
rol:           "forwarder-rfq.md v1.0 EKI (EK-1). RFQ ile BIRLIKTE gonderilir."
durum:         HAZIR — GONDERILMEDI
dil:           EN (gonderilecek kisim)
```

> **Neden ayrı bir sayfa?** Serbest formatta gelen üç teklif karşılaştırılamaz.
> Bu sayfa, üç forwarder'ın cevabını **aynı satırlara** oturtur. Boş bırakılan
> her hücre bizim için `UNKNOWN`'dır ve o hâliyle kaydedilir — **doldurulmaz.**
>
> **Zorunlu alan sayısı: 34** (§A 8 · §B 20 · §C 1 · §D 3 · §F 2).
> §B'nin 20 kalemi her lane × konteyner tipi için ayrı ayrı istenir.
>
> ⛔ **§A doldurulmadan gelen bir teklif geçerli sayılmaz.** Sebep: teklifin
> hangi kargo konfigürasyonuna bağlı olduğu bilinmezse, tedarikçi gerçek
> konfigürasyonu verdiğinde teklifin **hâlâ geçerli olup olmadığı
> anlaşılamaz.**

---

# ▼▼▼ GÖNDERİLECEK BÖLÜM — İNGİLİZCE ▼▼▼

# QUOTATION RESPONSE SHEET — bottled wine, multiple origins → Turkey

*Please complete one copy of Sections B–D for **each lane and each container
type** you quote. Sections A, E and F are completed once.*

*If a value is not applicable, please write **"n/a"**. If it is not known,
please write **"not known"**. Please do not leave cells blank — a blank cell is
recorded by us as "no information", which is worse for you than "n/a".*

```
Forwarder / company      : ______________________________________
Contact person / title   : ______________________________________
E-mail / phone           : ______________________________________
Your quotation reference : ______________________________________
Date of quotation        : ______________________________________
Our RFQ reference        : <RFQ_REF>
```

---

## SECTION A — CARGO CONFIGURATION YOU USED *(MANDATORY — 8 fields)*

> **This section is the most important one for us.** Our cargo figures are
> assumptions, not confirmed supplier data. If your price depends on them, we
> need to know exactly which figures you used, so that we can re-open the
> quotation when the supplier confirms the real configuration.

| # | Field | Your value | Unit |
|---|---|---|---|
| **A1** | **Case weight (gross) used in your quotation** | | kg |
| **A2** | Case format assumed (6 × 750 ml / 12 × 750 ml / other) | | — |
| **A3** | Case dimensions or case volume used | | mm / m³ |
| **A4** | **Pallet weight (gross, loaded) used in your quotation** | | kg |
| **A5** | Pallet type and footprint used (1200×1000 / 1200×800 / other) | | mm |
| **A6** | Loaded pallet height used (incl. pallet) | | mm |
| **A7** | **Number of pallets you loaded per container** — state separately for 20DV and 40HC | 20DV: ___ · 40HC: ___ | pallets |
| **A8** | Total cargo gross weight per container implied by A1–A7 | 20DV: ___ · 40HC: ___ | kg |

**A9 — Is your quotation conditional on A1–A8?**
☐ Yes — if the actual cargo configuration differs, the rate must be re-quoted
☐ No — the rate holds regardless, within the equipment limits
Comment: _______________________________________________

**A10 — LCL charging basis** (RFQ §2): we charge on
☐ loose case volume ☐ palletised footprint volume ☐ weight/measure, whichever is greater ☐ other: ______
Chargeable quantity you used for the 5,000-bottle LCL shipment: ______ m³ / ______ kg

**A11 — Would you accept this cargo floor-loaded (not palletised)?**
☐ Yes ☐ Yes, with conditions: ______ ☐ No, we would decline glass floor-loaded

---

## SECTION B — PRICE, PER LANE AND PER CONTAINER TYPE *(MANDATORY — 20 items)*

```
Lane (origin port → discharge port) : ______________________ → ______________________
Discharge terminal you would use    : ______________________
Quote type                          : ☐ Q1 LCL   ☐ Q2 20DV FCL   ☐ Q3 40HC FCL
Loading method priced               : ☐ palletised   ☐ floor loaded
```

| # | Line item | Amount | Currency | Per (container / B/L / shipment / CBM) | Notes |
|---|---|---|---|---|---|
| **B1** | **Ocean freight — BASE only** | | | | |
| **B2a** | Surcharge: BAF | | | | adjustment mechanism? |
| **B2b** | Surcharge: CAF | | | | |
| **B2c** | Surcharge: ETS / emissions | | | | |
| **B2d** | Surcharge: PSS / GRI / peak season | | | | announced for next 60 days? |
| **B2e** | Surcharge: war risk / security / other (name it) | | | | |
| **B3** | **Origin charges — total** *(itemise below or attach tariff)* | | | | |
| **B4** | **THC origin** | | | | |
| **B5** | **Documentation fee** | | | | |
| **B6** | **B/L fee** | | | | EDI or manual SI? |
| **B7** | **Destination THC** | | | | |
| **B8** | **Destination charges — total** *(itemise: delivery order/ordino, terminal handling, drop-off, ISPS, other)* | | | | |
| **B9** | **Customs-related carrier charges** | | | | not brokerage |
| **B10** | **Demurrage free time** | | days | | starts from: ______ |
| **B11** | **Detention free time** | | days | | starts from: ______ |
| **B12** | Demurrage / detention daily rates after free time, by tier | | | | |
| **B13** | **Transit time, port to port** | | days | | |
| **B14** | **Routing** (full, as actually moved) | | — | | |
| **B15** | **Transshipment** — yes/no, port(s), number of box handlings | | — | | |
| **B16** | **Validity** — from / to | | date | | |
| **B17** | **Spot or contract** | ☐ spot ☐ contract | — | | if contract: min. volume ______ |
| **B18** | **Container type offered** | | — | | |
| **B19** | **Maximum payload of that equipment** | | kg | | container tare: ______ kg |
| **B20** | **Sailing frequency + next 2–3 sailing dates** | | — | | |

**B3 itemisation (origin charges):**

| Charge name | Code | Amount | Currency | Mandatory or optional |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

**B8 itemisation (destination charges):**

| Charge name | Amount | Currency | Mandatory or optional |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

> **Reminder from the RFQ (§5.3):** a lane returned as a **single all-in
> figure**, without B1–B20, is recorded by us as **"no quotation received"**
> for that lane. Published origin local charges alone can exceed the base
> ocean freight on the lanes in this RFQ, so a lump sum is not comparable
> between forwarders.

---

## SECTION C — EXCLUDED CHARGES *(MANDATORY — 1 field, free text)*

**C1 — Please list everything NOT included in Section B:**

```
EXCLUDED CHARGES:
- ____________________________________________
- ____________________________________________
- ____________________________________________
- ____________________________________________
```

**C2 — Which line items in Section B are included inside another line?**
*(e.g. "terminal security fee is included in THC origin")*

```
- ____________________________________________
```

---

## SECTION D — EQUIPMENT, ROAD WEIGHT AND TIMING *(MANDATORY — 3 fields)*

| # | Field | Your value | Unit |
|---|---|---|---|
| **D1** | **Tractor + chassis tare weight** used by your Turkish haulage partner | | kg |
| **D2** | **Maximum cargo weight deliverable by road in Turkey** under the 44 t gross combination limit — state for 20DV and 40HC | 20DV: ___ · 40HC: ___ | kg |
| **D3** | **Overweight / heavy-load surcharge** — does it apply at our cargo weights, and from which threshold? | | — |

**D4 — LCL only:** typical consolidation waiting time at origin CFS: ______ days
**D5:** typical time from vessel berthing to container available for pick-up at the Turkish discharge terminal: ______ days
**D6:** if the cargo must wait in Turkey for a regulatory step before release (15 / 30 / 60 days), what do you recommend operationally and what would it cost?

```
15 days: ______________________________________
30 days: ______________________________________
60 days: ______________________________________
```

---

## SECTION E — OPTIONS *(price separately; do not bundle into Section B)*

| Option | Price | Currency | Basis | Notes / conditions |
|---|---|---|---|---|
| **E1 — Cargo insurance** | | | % of CIF + 10 % | cover basis: ☐ ICC (A) ☐ ICC (B) ☐ ICC (C) · **breakage included?** ☐ yes ☐ no · **temperature/thermal damage included?** ☐ yes ☐ no · deductible: ______ · exclusions for glass/wine: ______ |
| **E2 — Reefer container** | | | per container, per lane | destination terminal storage tariff for reefer vs dry: ______ |
| **E3 — Thermal / insulated liner (dry box)** | | | per container | expected performance: ______ · recommended on which lanes: ______ |
| **E4 — Floor-loaded vs palletised** | | | difference per container | your view on breakage risk for glass: ______ |
| **E5 — Devanning / unstuffing at destination** | | | per 20DV / 40HC | can you deliver directly into a bonded warehouse? ☐ yes ☐ no |
| **E6 — Bonded warehouse (antrepo)** | entry: ___ · storage: ___ /pallet/day · exit: ___ | | | minimum storage period: ______ · **licensed for alcoholic beverages?** ☐ yes ☐ no ☐ not known |
| **E7 — Summer sailing (June–September)** | — | — | — | any seasonal restriction or recommendation you apply to wine in dry containers: ______ |

---

## SECTION F — DECLARATIONS *(MANDATORY — 2 fields)*

**F1 — Rate stability during validity:** do any of the amounts in Section B
change during the validity period stated in B16 (e.g. monthly BAF/ETS revision)?
☐ No, all amounts are fixed for the validity period
☐ Yes — which ones and how: ______________________________________

**F2 — Currency:** are any lines converted at a rate you set? If yes, which
rate, and when is it fixed?
☐ No conversion applied
☐ Yes: ______________________________________

**F3 (optional but welcome):** if any assumption in RFQ §2 conflicts with your
operational experience, please tell us here. A correction is worth more to us
than a lower price.

```
____________________________________________________________
```

---

**Attachments requested:** your published **local charges tariff** for the
origin country/countries quoted (RFQ §5.2).

# ▲▲▲ GÖNDERİLECEK BÖLÜMÜN SONU ▲▲▲

---

## EK: CEVAP GELDİĞİNDE NE YAPILACAK *(gönderilmez)*

| Gelen alan | Nereye işlenir | Not |
|---|---|---|
| B1 + B2a-e | `lojistik.yaml → tur2.fcl_navlun.*` (yeni `tur325` bloğu) | `C-311`'i kapatabilecek tek veri |
| B3, B4, B5, B6 | `origin_charges_<mense>` — **İspanya dışı 6 menşe için ilk veri** | `T-312` |
| B7, B8 | `liman_ve_gumrukleme.*` | `C-313` (THD ↔ terminal kapı çıkışı çift sayımı) test edilir |
| B10, B11, B12 | `demurrage_detention.*` | armatör bazlı free time farkı → `T-313` |
| B13, B14, B15 | `sure.transit_gun_port_to_port.*` + sıcaklık/kırılma risk modeli | aktarma sayısı = elleçleme sayısı |
| B16, B17 | kanıt kartının `ttl`'i ve `navlun_tipi` alanı | **teklifin kendi validity'si `ttl` olur** |
| B19, D1, D2 | `karayolu_agirlik.cekici_sasi_darasi_kg` — **ASSUMPTION'dan çıkar** | 40HC kapasitesini doğrudan belirler |
| A1, A4, A7 | `urun_fizik.*` ve `konteyner.palet_sayisi.*` — **`C-301` çelişkisi** | forwarder'ın kendi sayısı üçüncü bağımsız kaynak olur |
| A9 = "Yes" | **teklif tedarikçi konfigürasyonuna bağımlıdır** → `T-822` | `T-302` kapanınca teklif yenilenir |
| E1 | `sigorta.prim_orani_pct` | **CIF etkisi bizde değil** → `gumruk-vergi-uzmani` / `finans-fizibilite` |
| E3 | `sicaklik_riski.thermal_liner_ek_maliyet` | uzun transit rotalarda karar verilebilir hâle gelir |
| E6 | `antrepo.*` | alkol yetkisi sorusu **mevzuat tarafı değildir** — yalnızca tesisin beyanı kaydedilir |
| C1 | her kanıt kartının `excluded_charges` alanı | **boş bırakılamaz** (rota-maliyet-matrisi.md kural 2) |

> **Kayıt kuralı:** gelen her teklif için ayrı kanıt kartı açılır
> (`tier: T4`, `status: FACT` yalnızca teklifin validity'si boyunca,
> `ttl = validity`), `99-ops/veri-tazeligi.md`'ye eklenir. **Üç teklif
> ortalanmaz** — üçü ayrı satır olarak taşınır; aralarındaki fark
> `senaryolar.yaml`'daki navlun duyarlılık bandının **ilk kanıtlı dayanağı**
> olur (`T-913` §B-5).
