# RFQ MAIL — VARYANT A: EXISTING BRAND DISTRIBUTION

```yaml
belge:                rfq-mail-existing-brand
varyant:              A — Model A (mevcut marka distribütörlüğü)
sahibi:               global-sourcing-kasifi
tur:                  TUR 3.25 §8 — SUPPLIER RFQ PAKETİ
tarih:                2026-08-10
sablon_temeli:        50-sourcing/rfq-template.md v2.2 (SUMMARY SHEET S1–S27)
ek:                   50-sourcing/rfq-response-sheet.md
kelime_sayisi_govde:  319 (P bloğu ile) / 284 (N bloğu ile)   # hedef ≤350
kelime_sayimi_tanimi: "Subject, 'Dear …' ve imza bloğu HARİÇ; yalnızca gövde
                       paragrafları. [P] ve [N] blokları BİRLİKTE gönderilmez —
                       menşe grubuna göre YALNIZCA BİRİ gövdede kalır."
gonderildi_mi:        HAYIR
dis_iletisim:         NONE — hiçbir üreticiye e-posta/form/mesaj GÖNDERİLMEDİ
```

> ## ⛔ BU METİN GÖNDERİLMEDİ
>
> Gönderim, kurucuya **RECIPIENT + SUBJECT + PREVIEW** gösterilip **açık onay**
> alınmadan yapılmaz (`T-885`). Bu dosya bir **taslaktır**.

---

## 0. İÇ KULLANIM — GÖNDERİM ÖNCESİ (BU BÖLÜM GÖNDERİLMEZ)

### 0.1 Doldurulacak alanlar

| Alan | Kim doldurur | Durum |
|---|---|---|
| `<COMPANY>` `<NAME>` `<POSITION>` `<ADDRESS>` `<EMAIL>` `<PHONE>` | kurucu / başkan | **AÇIK** → `T-892` |
| `<DEADLINE>` | başkan | **AÇIK** → `T-892` |
| `<CONTACT NAME>` | tedarikçi bazında; **kişi adı public değilse** `Export Sales Team` | 10/10 tedarikçide kişi adı **YOK** (TWF hariç) |
| **§6 bloğu** | menşe grubuna göre **P** veya **N** metni seçilir | `top-10-contact-pack.md` §3 kolonu |

### 0.2 Hangi tedarikçiye gider

`Casa Santos Lima` · `Vidigal Wines` · `Plaimont` · `Purcari Wineries Group`
· `Bodegas San Valero` (A+B — **iki varyant birlikte**) · `Cantina Danese`
(**yalnızca existing-brand kolu** — bkz. `top-10-contact-pack.md` §5.1)

### 0.3 Menşe bloğu seçimi — **belge adı `gumruk-vergi-uzmani`'nın doğruladığı hâliyle**

| Grup | Ülkeler | §6'da hangi metin |
|---|---|---|
| **P** | ES · PT · IT · FR · CL | **`[P]` bloğu** — *EUR.1 movement certificate* **veya** *invoice declaration*. **A.TR yazılmaz** (`mense-tarife-eslemesi.md` §2.2: BİLGE 2204 için A.TR'yi kabul etmez) |
| **N** | AU · MD | **`[N]` bloğu** — tercihli belge yoktur; yalnızca *non-preferential certificate of origin* sorulur |

### 0.4 §7 SIZINTI DENETİMİ (bu metin için)

| Yasaklı bilgi | Metinde var mı |
|---|---|
| 799 / 699 / 899 TRY hedef raf | **YOK** |
| `MAX CIF` · `MAXIMUM STRUCTURAL BUY PRICE` (272,83 / 240,73) | **YOK** |
| `RFQ TARGET CEILING X/Y` (200,98 / 290,51 / 256,34) | **YOK** |
| walk-away price | **YOK** |
| ithalatçı / perakendeci hedef marjı | **YOK** |
| tedarikçi sıralaması ("siz 7. sıradasınız") | **YOK** |
| rakip tedarikçi fiyatı | **YOK** |
| **%11,765 / 32,10 TRY menşe belgesi ekonomik etkisi** | **YOK** — v2.2 şablonundaki *"changes the maximum price we are able to pay by around 12%"* cümlesi **bu varyanttan ÇIKARILMIŞTIR** (§6 talimatı) |
| Söylenmesine izin verilen | *"long-term import and distribution programme … value/price-performance segment"* — **var, tek cümle** |

---
---

# ✉️ GÖNDERİLECEK METİN — BURADAN AŞAĞISI KOPYALANIR

**Subject:** Wine supply to Türkiye — distribution enquiry — `<COMPANY>`

---

Dear `<CONTACT NAME / Export Sales Team>`,

We are a company based in Türkiye evaluating a long-term import and
distribution programme for still wine in the price-performance segment of the
Turkish market. We are building a producer shortlist and would like to know
whether one of your existing brands could form part of it.

Our target is a **750 ml still dry white** in the value/entry export tier —
Chardonnay, Colombard-Chardonnay, Sauvignon Blanc, Verdejo, Airén-Chardonnay,
Trebbiano, or an equivalent white blend you would recommend. Please quote **two
quality levels**: (1) your cheapest commercially acceptable, export-ready white,
and (2) the best-value option one level above it.

Please do not quote a single volume. We need a price per bottle at **5,000 /
10,000 / 25,000 / 50,000 bottles per year, and for one full 20' container.**
For each line please state **EXW and FOB separately** — EXW naming the place,
FOB naming the port — together with currency, price per case, MOQ, Incoterm and
validity date.

As this is a distribution enquiry, please also confirm: whether **Türkiye
distribution rights are available**; whether you already have an importer or
distributor there; whether **exclusivity** is possible and against what
territory and annual commitment; any marketing obligations; your recommended
export price; what distributor support you provide; and whether **samples** can
be sent.

**`[P]`** For customs formalities, please confirm which **preferential origin
document** you can issue for shipments to Türkiye — a **EUR.1 movement
certificate** or an **invoice declaration**. Write the document name;
*"yes, we export"* does not answer this. Please also confirm whether you would
**commit contractually to issuing it for every shipment**, whether the wine is
wholly produced and bottled in your country, and **from which country's port**
the goods will leave.

**`[N]`** For customs formalities, please confirm whether you can issue a
**non-preferential certificate of origin**, whether the wine is wholly produced
and bottled in your country, and **from which country's port** the goods will
leave.

The attached **response sheet** repeats these questions and adds the packaging
data (bottle weight, case and pallet configuration) we need to calculate a
delivered cost. Completing it is the fastest route to a comparable offer.

We would be grateful for your reply by `<DEADLINE>`.

Kind regards,

`<NAME>`
`<POSITION>`
`<COMPANY>`
`<ADDRESS>`
`<EMAIL>` · `<PHONE>`

---

# ⬆️ GÖNDERİLECEK METİN BURADA BİTER

---

## 1. TEDARİKÇİYE ÖZEL EK SORU — GÖVDEYE **TEK CÜMLE** OLARAK EKLENİR

Charter kuralı `rfq-template.md` §0.8 *"aynı metin herkese gider"* korunur:
aşağıdaki cümleler gövdeyi **değiştirmez**, gövdenin sonuna **ek bir satır**
olarak girer ve response sheet'in **Q-SPECIAL** satırına oturur.

| Tedarikçi | Eklenecek cümle (İngilizce, birebir) |
|---|---|
| **Cantina Danese** | *"We understand at least one of your wines has been listed in Türkiye. Is that relationship still active, does it carry exclusivity, and would it restrict a separate arrangement with us?"* |
| **Purcari** | *"Could the same or an equivalent wine be produced and shipped from your Romanian or Bulgarian wineries instead of Moldova — and if so, what is the price difference per bottle and which origin document would each site issue?"* |
| **Bodegas San Valero** | *"For the same white wine, what is your EXW price (a) under your own brand and (b) under our brand?"* |
| **Casa Santos Lima** | *"Has any of your brands been sold in Türkiye before — by whom, in which years, and why did it stop?"* |
| **Vidigal Wines** | *"Do you have a 750 ml dry WHITE value SKU at all — variety and ABV?"* |
| **Plaimont** | *"Please quote specifically IGP Côtes de Gascogne Colombard or Colombard-Chardonnay."* |

> **Neden ek cümle, neden ayrı metin değil:** tek bir cümle karşılaştırılabilirliği
> bozmaz; gövdeyi yeniden yazmak bozar. Ek cümlelerin hiçbiri fiyat hedefi,
> tavan veya sıralama bilgisi içermez (§0.4 denetimi bu cümleleri de kapsar).

## 2. NE **SORULMADI** — BİLİNÇLİ

| Sorulmayan | Neden |
|---|---|
| **100.000 şişe kademesi** | §0 talimatı: ilk RFQ'da sorulmaz. Talep edilen hacim, sahip olmadığımız bir taahhüdü ima eder ve ilk teklifte güvenilirlik kaybettirir |
| Hedef fiyatımız | §7 — açıklanırsa her teklif tavana yapışır |
| Vergi/ÖTV/KDV yorumu | Alan dışı (`gumruk-vergi-uzmani`) — üreticiye Türk vergisi sorulmaz, yalnızca **belge düzenleyebilirliği** sorulur |
| Navlun tutarı | Alan dışı (`navlun-lojistik-uzmani`) — FOB liman adı sorulur, navlun fiyatı sorulmaz |
