---
description: Gerçek tedarikçi teklifini (RFQ cevabı) sisteme kanıtlı olarak girer
---

# TEKLİF GİR

Bir üreticiden/tedarikçiden **gerçek teklif** geldiğinde bu komut çalıştırılır.
Gösterge fiyat ile gerçek teklif aynı şey değildir — bu komut ikisini ayırır.

Yürüten ajan: `global-sourcing-kasifi`
(Navlun teklifi geldiyse: `navlun-lojistik-uzmani`)

## 1. TEKLİF TÜRÜNÜ BELİRLE

| `quote_type` | Anlamı |
|--------------|--------|
| `INDICATIVE` | Web sitesi / katalog / sözlü gösterge fiyat |
| `FIRM_OFFER` | Yazılı, geçerlilik tarihi olan bağlayıcı teklif |
| `PROFORMA` | Proforma fatura |

**Sadece `FIRM_OFFER` ve `PROFORMA` model için "gerçek teklif" sayılır.**

## 2. ZORUNLU ALANLAR

Teklif kaydedilmeden önce şunlar **net** olmalı:

- tedarikçi adı, ülke, iletişim
- ürün: üzüm/blend, hasat yılı, ABV, hacim (ml)
- **Incoterm** (EXW / FOB / CIF — hangisi olduğu açık olmalı)
- **fiyat + para birimi + birim** (şişe mi koli mi)
- **MOQ**
- koli konfigürasyonu (şişe/koli), koli ölçü ve brüt ağırlığı
- palet konfigürasyonu (koli/palet), palet ölçü ve ağırlığı
- ödeme koşulları ve vade
- lead time
- teklifin **geçerlilik tarihi**
- menşe ispat belgesi verilebilir mi (EUR.1 / fatura beyanı / REX)
- private label mümkün mü, etiket uyarlaması yapılır mı
- analiz sertifikaları

Eksik alan → `UNKNOWN` yazılır, **tahmin edilmez**. Eksikse tedarikçiye
`50-sourcing/rfq-template.md` üzerinden tamamlama sorusu gönderilir.

## 3. KANIT KARTI AÇ

`10-evidence/raw/EV-YYYY-MM-DD-###.md`

- `tier`: **T4**
- `source_name`: tedarikçi adı
- `status`: `FACT` (teklif gerçekten alındıysa — teklifin varlığı FACT'tir)
- `ttl`: teklifin geçerlilik süresi
- `snapshot_path`: teklif dosyasının kopyası (PDF/e-posta)
- `collecting_agent`: `global-sourcing-kasifi`

**Teklifin varlığı FACT'tir; teklifin gelecekte de geçerli olacağı FACT değildir.**

## 4. HAVUZA EKLE

`50-sourcing/tedarikci-havuzu.csv` dosyasına satır eklenir veya mevcut satır
**güncellenmez, yeni satır olarak eklenir** ve eski satır `supersedes` ile
bağlanır.

## 5. MODEL GİRDİSİNİ GÜNCELLE

`80-model/inputs/tedarikci.yaml`:
- ilgili alan yeni `evidence_id` ile güncellenir
- `status` `ASSUMPTION`/`ESTIMATE`'ten `FACT`'e yükseltilir
- **Incoterm alanı doğru katmana yazılır**: EXW fiyatı `L0`, FOB fiyatı `L1`.
  Katman karıştırılmaz.

## 6. ÇAPRAZ İPUÇLARI

Teklifte başka ajanları ilgilendiren bilgi varsa
`99-ops/capraz-ipuclari.md` dosyasına bırakılır:
- ödeme vadesi / akreditif → `gumruk-vergi-uzmani` (KKDF etkisi)
- koli/palet ölçüleri ve ağırlık → `navlun-lojistik-uzmani` (konteyner hesabı)
- etiket uyarlama kabiliyeti → `mevzuat-ruhsat-uzmani`
- menşe ispat belgesi → `gumruk-vergi-uzmani` (tercihli tarife)

## 7. MODELİ YENİDEN ÇALIŞTIR

Gerçek teklif geldiyse `finans-fizibilite`'ye ticket açılır:
`/model-calistir` yeniden çalıştırılır, önceki çıktı ile farkı raporlanır.
