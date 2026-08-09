# RFQ TEMPLATE — Request for Quotation

> **Sahibi:** `global-sourcing-kasifi`
> **Durum:** v1.0 — kullanıma hazır iskelet. TUR 7'de (karar TEST veya
> IMPORT PILOT ise) gerçek üreticilere gönderilecektir.
>
> **BU TURDA GÖNDERİLMEZ.**
>
> `<>` içindeki alanlar gönderim öncesi doldurulur.
> Cevaplar `50-sourcing/tedarikci-havuzu.csv` kolonlarına birebir oturur.

---

## KULLANIM NOTLARI (İÇ KULLANIM — GÖNDERİLMEZ)

1. Şablon **İngilizce**dir; çoğu üretici Türkçe okumaz.
2. Gelen cevap `/teklif-gir` komutu ile sisteme işlenir.
3. Cevap `INDICATIVE` mi `FIRM_OFFER` mi — **mutlaka** netleştirilir.
4. Eksik cevap **tahminle tamamlanmaz**; takip e-postası gönderilir.
5. Fiyat sorulurken **EXW ve FOB ayrı ayrı** istenir. Tek bir "price" cevabı
   hangi Incoterm olduğu belirsizse `UNKNOWN`'dır.
6. Koli/palet ölçüleri `navlun-lojistik-uzmani`'nın konteyner hesabı için
   zorunludur — bu alanlar boş dönerse teklif eksiktir.

---

## E-POSTA GÖVDESİ (KOPYALA-YAPIŞTIR)

**Subject:** Wine supply inquiry — Turkey import — <BRAND/PRIVATE LABEL> — <VOLUME> bottles/year

---

Dear <CONTACT NAME / Sales Team>,

We are a Turkey-based importer evaluating the launch of a value-segment wine
program for the Turkish retail market. We are currently building a shortlist of
producers and would like to request a quotation.

We are evaluating **two models in parallel** and are open to either:
- **Model A —** distribution of an existing brand of yours in Turkey
- **Model B —** private label production under our own brand

Please indicate which model(s) you can support.

### 1. Product specification

Please quote for a dry white wine in the value/mainstream segment,
comparable in style to a Colombard–Chardonnay blend.

| # | Question |
|---|----------|
| 1.1 | Product name / reference |
| 1.2 | Grape variety or blend composition |
| 1.3 | Vintage available |
| 1.4 | ABV (% vol) |
| 1.5 | Residual sugar (g/L) |
| 1.6 | Total acidity |
| 1.7 | Bottle volume (ml) — we require **750 ml** |
| 1.8 | Bottle type and weight (g) |
| 1.9 | Closure type (cork / screw cap / synthetic) |
| 1.10 | Shelf life / recommended consumption window |

### 2. Packaging and logistics data (required for container calculation)

| # | Question |
|---|----------|
| 2.1 | Bottles per case |
| 2.2 | Case gross weight (kg) |
| 2.3 | Case dimensions (L × W × H, cm) |
| 2.4 | Cases per layer / layers per pallet |
| 2.5 | Cases per pallet |
| 2.6 | Pallet type (EUR / standard) and dimensions |
| 2.7 | Pallet gross weight (kg) and height (cm) |
| 2.8 | Maximum cases per 20'DV and per 40'HC |
| 2.9 | Can you load floor-loaded (non-palletized)? |
| 2.10 | Nearest loading port |

### 3. Commercial terms

| # | Question |
|---|----------|
| 3.1 | **EXW price** per bottle — currency and validity |
| 3.2 | **FOB price** per bottle — named port, currency and validity |
| 3.3 | CIF price to Turkey (Ambarlı / Mersin / İzmir), if you can quote it |
| 3.4 | Is this quotation **indicative** or a **firm offer**? |
| 3.5 | Quotation validity date |
| 3.6 | **MOQ** — in bottles and in containers |
| 3.7 | Price breaks by volume (e.g. 5k / 10k / 25k / 50k / 100k bottles/year) |
| 3.8 | Payment terms (TT in advance, L/C, open account) |
| 3.9 | Payment days offered |
| 3.10 | Lead time from PO to loading (days) |
| 3.11 | Annual production capacity available to us (bottles) |

### 4. Private label (Model B)

| # | Question |
|---|----------|
| 4.1 | Do you offer private label production? |
| 4.2 | Minimum order quantity for private label |
| 4.3 | Can you adjust the blend / style to a target profile? |
| 4.4 | Do you support custom label design and printing? |
| 4.5 | Can you apply a **Turkish-language back label** at your facility? |
| 4.6 | Custom bottle / closure options and their MOQ impact |
| 4.7 | Who owns the brand and recipe IP? |
| 4.8 | Additional lead time for private label vs. standard product |

### 5. Existing brand distribution (Model A)

| # | Question |
|---|----------|
| 5.1 | Which of your brands are available for Turkey? |
| 5.2 | Do you currently have an importer or distributor in Turkey? |
| 5.3 | Would you grant exclusivity? Under what conditions? |
| 5.4 | Required annual volume commitment |
| 5.5 | Marketing / listing support offered |
| 5.6 | Has this brand been sold in Turkey before? |

### 6. Documentation and compliance

| # | Question |
|---|----------|
| 6.1 | Can you issue a **preferential origin document** (EUR.1 / invoice declaration / REX)? |
| 6.2 | Analysis certificate — which parameters are included? |
| 6.3 | Which accredited laboratory issues it? |
| 6.4 | Can you provide a Certificate of Origin? |
| 6.5 | Can you provide health / free sale certificates? |
| 6.6 | Have you exported to Turkey before? If yes, with which importer? |
| 6.7 | Which export markets do you currently serve? |
| 6.8 | Are you able to adapt labels to importer-country legal requirements? |

### 7. Samples

| # | Question |
|---|----------|
| 7.1 | Can you send samples to Turkey? |
| 7.2 | Sample cost and shipping cost |
| 7.3 | Lead time for samples |

---

We would appreciate your response in the structure above so that we can
compare offers consistently across suppliers.

Kind regards,
<NAME>
<COMPANY>
<EMAIL> · <PHONE>

---

## CEVAP DEĞERLENDİRME KONTROL LİSTESİ (İÇ KULLANIM)

Teklif geldiğinde `/teklif-gir` çalıştırılmadan önce kontrol et:

- [ ] Incoterm **açıkça** belirtilmiş mi? (EXW mi FOB mu — belirsizse `UNKNOWN`)
- [ ] Fiyat birimi net mi? (şişe mi koli mi)
- [ ] Para birimi yazılı mı?
- [ ] `INDICATIVE` mi `FIRM_OFFER` mi?
- [ ] Geçerlilik tarihi var mı? (bu, kanıt kartının `ttl`'i olacak)
- [ ] MOQ hem şişe hem konteyner bazında mı?
- [ ] Koli ve palet ölçü/ağırlık verileri tam mı? (konteyner hesabı için zorunlu)
- [ ] Menşe ispat belgesi sorusu cevaplanmış mı? (tercihli tarife için kritik)
- [ ] Ödeme vadesi net mi? (KKDF etkisi için `gumruk-vergi-uzmani`'na ipucu)
- [ ] Eksik alanlar `UNKNOWN` olarak mı işaretlendi, yoksa tahmin mi edildi?

**Eksik alan tahminle doldurulmaz. Takip sorusu gönderilir.**
