# VERGİ MATRAH SIRASI

> **DURUM: BOŞ İSKELET — TUR 1'DE `gumruk-vergi-uzmani` TARAFINDAN DOLDURULACAK**
>
> Bu dosyada **hiçbir oran, tutar veya matrah tanımı** T1/T2 resmî kaynakla
> doğrulanmadan yazılmaz. Aşağıdaki tablolar bilinçli olarak `UNKNOWN`'dır.
>
> Bu dosya `80-model/engine/matrah_sirasi.py` için **tek doğruluk kaynağıdır.**
> Kod bu dosyadan okur; kodda sıra veya oran sabitlenmez.

---

## 1. NEDEN BU DOSYA KRİTİK

Vergi hesabında en sık yapılan hata **matrahların karıştırılmasıdır.**

Yanlış soru: "ÖTV yüzde kaç?"
Doğru soru: **"ÖTV neyin üzerinden, hangi sırada, hangi tutarla?"**

Bir verginin matrahına başka bir verginin girip girmediği, toplam vergi yükünü
dramatik biçimde değiştirir. Bu dosya o zinciri kesin olarak tanımlar.

---

## 2. GÜMRÜK KIYMETİ (VERGİLENDİRMENİN BAŞLANGICI)

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Gümrük kıymeti hangi Incoterm bazında belirlenir? | UNKNOWN | UNKNOWN | — |
| Navlun kıymete dahil mi? | UNKNOWN | UNKNOWN | — |
| Sigorta kıymete dahil mi? | UNKNOWN | UNKNOWN | — |
| Yükleme/boşaltma/elleçleme? | UNKNOWN | UNKNOWN | — |
| Royalti / lisans bedeli? | UNKNOWN | UNKNOWN | — |
| Alım komisyonu / satım komisyonu? | UNKNOWN | UNKNOWN | — |
| Ambalaj/etiket bedeli? | UNKNOWN | UNKNOWN | — |
| Yurt içi masraflar kıymete dahil mi? | UNKNOWN | UNKNOWN | — |

**Gözetim / referans kıymet**

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Bu GTİP'te ithalatta gözetim uygulaması var mı? | UNKNOWN | UNKNOWN | — |
| Birim kıymet eşiği var mı? | UNKNOWN | UNKNOWN | — |
| Eşiğin altında beyan edilirse ne olur? | UNKNOWN | UNKNOWN | — |

> ⚠️ Gözetim uygulaması varsa, **beyan edilen düşük kıymet fiilen
> kullanılamaz** ve tüm ucuz sourcing stratejisi çöker. Bu bir
> `CRITICAL` kontrol noktasıdır.

---

## 3. GTİP

| Alan | Değer | status | evidence_id |
|------|-------|--------|-------------|
| GTİP kodu (750 ml köpüksüz şarap) | UNKNOWN | UNKNOWN | — |
| Alt kırılım kriteri (ABV / hacim / köpüklü) | UNKNOWN | UNKNOWN | — |
| Alternatif GTİP ihtimali | UNKNOWN | UNKNOWN | — |

> GTİP yanlışsa **her şey yanlıştır.** Vergi oranı, ÖTV, gözetim, tercihli
> tarife — hepsi GTİP'e bağlıdır.

---

## 4. MATRAH ZİNCİRİ — DOLDURULACAK ŞEMA

`gumruk-vergi-uzmani` bu tabloyu doldurur. Sıra numarası **hesaplama sırasıdır.**

| Sıra | Vergi / yükümlülük | Matrah (neyin üzerinden) | Oran / tutar | Tip | status | evidence_id | effective_date |
|------|--------------------|--------------------------|--------------|-----|--------|-------------|----------------|
| 1 | Gümrük Vergisi | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | — | — |
| 2 | İlave Gümrük Vergisi (varsa) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | — | — |
| 3 | ÖTV | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | — | — |
| 4 | KKDF (varsa) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | — | — |
| 5 | KDV | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | — | — |
| 6 | Diğer (TRT bandrol, damga, fon vb.) | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | — | — |

**`Tip` sütunu:** `ORANSAL` | `MAKTU` | `KARMA (yüksek olan)` | `YOK`

### Zincirin açık yazılması

Doldurulduğunda şu formda net olmalı — **her `?` bir evidence_id ile
kapatılacak:**

```
CIF                       = ?
Gümrük Vergisi matrahı    = ?
Gümrük Vergisi            = ?
ÖTV matrahı               = ?   ← Gümrük Vergisi dahil mi?  UNKNOWN
ÖTV                       = ?   ← oransal mı maktu mu, asgari maktu var mı? UNKNOWN
KKDF matrahı              = ?   ← hangi ödeme şeklinde doğar? UNKNOWN
KKDF                      = ?
KDV matrahı               = ?   ← ÖTV dahil mi? Gümrük Vergisi dahil mi? UNKNOWN
KDV                       = ?
─────────────────────────────
L4 POST-TAX LANDED        = ?
```

---

## 5. ÖTV — ÖZEL DİKKAT

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Hangi liste/cetvel? | UNKNOWN | UNKNOWN | — |
| Oransal ÖTV oranı | UNKNOWN | UNKNOWN | — |
| Asgari maktu vergi tutarı | UNKNOWN | UNKNOWN | — |
| Maktu tutar birimi (litre / şişe / ABV bazlı?) | UNKNOWN | UNKNOWN | — |
| Oransal mı maktu mu uygulanır (hangisi yüksekse mi)? | UNKNOWN | UNKNOWN | — |
| Maktu tutarın son güncelleme tarihi | UNKNOWN | UNKNOWN | — |
| Güncelleme periyodu / endeksleme mekanizması | UNKNOWN | UNKNOWN | — |

> ⚠️ Maktu ÖTV tutarları **periyodik olarak güncellenir.** Hangi tarihli
> tutarın kullanıldığı belirtilmezse bulgu geçersizdir. Bu, `ttl` süresi
> en kısa verilerden biridir.
>
> Fiyat/performans segmentinde maktu ÖTV, ucuz üründe **oransal ÖTV'den
> daha ağır** basabilir ve düşük fiyatlı ithalatın ekonomisini tek başına
> öldürebilir. Bu, projenin en kritik tek sorusudur.

---

## 6. TERCİHLİ TARİFE

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Hangi ülkeler için STA/tercihli tarife var? | UNKNOWN | UNKNOWN | — |
| Menşe ispat belgesi türü (EUR.1 / fatura beyanı / REX) | UNKNOWN | UNKNOWN | — |
| Tarife kontenjanı var mı? | UNKNOWN | UNKNOWN | — |
| Tercihli tarife hangi vergiyi etkiler, hangisini etkilemez? | UNKNOWN | UNKNOWN | — |

> Not: Tercihli tarife genellikle **gümrük vergisini** etkiler. ÖTV ve KDV'yi
> etkileyip etkilemediği ayrıca doğrulanmalıdır — varsayılmamalıdır.

---

## 7. ANTREPO REJİMİNİN VERGİ ETKİSİ

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| Vergiler antrepoya girişte mi, çıkışta mı doğar? | UNKNOWN | UNKNOWN | — |
| Antrepoda bekletme vergi yükünü değiştirir mi? | UNKNOWN | UNKNOWN | — |
| Antrepoda bekletme **nakit akışını** nasıl etkiler? | UNKNOWN | UNKNOWN | — |
| Kısmi çekiş (partial release) mümkün mü? | UNKNOWN | UNKNOWN | — |

> Kısmi çekiş mümkünse, `peak_cash_requirement` dramatik biçimde düşebilir.
> Bu, `finans-fizibilite` için birinci derecede önemli bir girdidir.

---

## 8. KDV — İKİ PERSPEKTİF

| Soru | Cevap | status | evidence_id |
|------|-------|--------|-------------|
| İthalatta ödenen KDV indirilebilir mi? | UNKNOWN | UNKNOWN | — |
| İndirilebiliyorsa ne zaman mahsup edilir? | UNKNOWN | UNKNOWN | — |
| Devreden KDV oluşur mu, iade süreci nedir? | UNKNOWN | UNKNOWN | — |
| ÖTV indirilebilir mi? | UNKNOWN | UNKNOWN | — |

**A) Ekonomik maliyet:** KDV indirilebiliyorsa P&L'e girmez.
**B) Nakit akışı (`cash_tax_timing`):** Gümrükte ödeme anı ile mahsup/tahsilat
anı arasındaki gecikme `peak_cash_requirement`'ı büyütür.

Bu ikisi **asla tek satırda** gösterilmez.

---

## 9. DOLDURMA KURALLARI (`gumruk-vergi-uzmani` İÇİN)

1. Her satır **T1/T2** kaynağa dayanmalı. T5 tek başına yetmez.
2. Her satırda **`effective_date`** olmalı.
3. Bir matrahın içine başka bir vergi giriyorsa bu **açıkça** yazılmalı.
4. Emin olmadığın satırı `UNKNOWN` bırak. **Boşluğu tahminle doldurma.**
5. Her doldurulan satır için `10-evidence/raw/` altında kanıt kartı aç.
6. Tamamlandığında `80-model/inputs/vergi.yaml` bu dosyadan doldurulur.
7. Bu dosya tamamlanmadan `finans-fizibilite` vergi hesabı **çalıştırmaz.**

---

## 10. BU BULGUYU NE ÇÜRÜTÜR?

*(Doldurulduğunda `gumruk-vergi-uzmani` tarafından yazılacak)*

- Hangi GTİP itirazı tüm yapıyı değiştirir?
- Maktu ÖTV güncellenirse hangi senaryolar ölür?
- Gözetim/kıymet itirazı gelirse beyan stratejisi ne olur?
- Tercihli tarifenin ÖTV'yi etkilemediği doğrulanırsa ülke seçimi değişir mi?
