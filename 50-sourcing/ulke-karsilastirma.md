# ÜLKE KARŞILAŞTIRMA

> **DURUM: BOŞ İSKELET — TUR 1'DE `global-sourcing-kasifi` TARAFINDAN DOLDURULACAK**
>
> Bu turda hiçbir hücre doldurulmaz. Tüm değerler `UNKNOWN`'dır.

---

## 1. KAPSANAN ÜLKELER

Öncelikli: California (ABD), İspanya, İtalya, Fransa, Şili, Güney Afrika,
Portekiz, Avustralya, Arjantin.

Ekonomik olarak anlamlıysa eklenecek: Moldova, Gürcistan, Kuzey Makedonya,
Bulgaristan, Romanya, Yunanistan, diğer.

---

## 2. ANA KARŞILAŞTIRMA TABLOSU

| Ülke | Tipik FOB (750ml, f/p segment) | Para birimi | STA/tercihli tarife var mı | Menşe ispat belgesi | Navlun mesafesi | Private label ekosistemi | İhracat hacmi/sürekliliği | Tedarikçi sayısı (bulunan) | Genel not |
|------|-------------------------------|-------------|---------------------------|---------------------|-----------------|--------------------------|---------------------------|---------------------------|-----------|
| California (ABD) | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | Benchmark ürünün menşei |
| İspanya | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | |
| İtalya | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | |
| Fransa | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | |
| Şili | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | |
| Güney Afrika | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | |
| Portekiz | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | |
| Avustralya | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | Komşu benchmark menşei |
| Arjantin | UNKNOWN | — | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | 0 | |

> **Not:** `STA/tercihli tarife` sütununda `global-sourcing-kasifi` yalnızca
> **"var mı / hangi ülke grubunda"** sorusunu işaretler. **Oranı yazmaz** —
> oran `gumruk-vergi-uzmani`'nın alanıdır.
>
> `Navlun mesafesi` sütununda yalnızca rota/mesafe işaretlenir.
> **Navlun tutarı** `navlun-lojistik-uzmani`'nın alanıdır.

---

## 3. İŞ MODELİ BAZLI DEĞERLENDİRME

`00-charter/karar-esikleri.md` uyarınca iki model **eşit önceliklidir.**

### Model A — Mevcut marka distribütörlüğü

| Ülke | Türkiye'de temsilcisi olmayan f/p markalar | Münhasırlık şartı | Hacim taahhüdü | Pazarlama katkısı | status |
|------|-------------------------------------------|-------------------|----------------|-------------------|--------|
| | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

### Model B — Private label

| Ülke | Bottler/üretici bulunabilirliği | Min. private label MOQ | Blend esnekliği | Etiket/tasarım desteği | Lead time | status |
|------|--------------------------------|------------------------|-----------------|------------------------|-----------|--------|
| | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

---

## 4. BULK ALTERNATİFİ — ARAŞTIRMA HİPOTEZİ (BU TURDA ÇÖZÜLMEZ)

**Hipotez:** Dökme (bulk) şarap ithal edip Türkiye'de şişelemek, şişelenmiş
ürün ithal etmekten ekonomik olarak daha avantajlı olabilir mi?

**Durum:** `HYPOTHESIS — NOT INVESTIGATED`

Bu hipotez `00-charter/kapsam.md` uyarınca **kapsam dışıdır** ve bu projede
çözülmez. `global-sourcing-kasifi` yalnızca şunu yapar:
- Hipotezi burada kaydeder
- İlgili ajanlara `99-ops/capraz-ipuclari.md` üzerinden ipucu bırakır:
  - `gumruk-vergi-uzmani` → bulk şarabın GTİP'i ve vergi rejimi farklı mı?
  - `mevzuat-ruhsat-uzmani` → Türkiye'de şişeleme ayrı ruhsat gerektirir mi?
  - `navlun-lojistik-uzmani` → flexitank/ISO tank lojistiği nasıl işler?

**Kendisi bu soruları çözmez.**

---

## 5. ELEME KRİTERLERİ (DOLDURULACAK)

Bir ülke şu durumlarda elenir — kriterler TUR 1'de kanıtla netleşir:

| # | Eleme kriteri | Eşik | status |
|---|---------------|------|--------|
| 1 | FOB fiyatı ters modelin verdiği max EXW/FOB'un üzerinde | TBD (`finans-fizibilite` verecek) | UNKNOWN |
| 2 | MOQ pilot hacmi (5.000–10.000 şişe) ile uyumsuz | TBD | UNKNOWN |
| 3 | Türkiye'ye ihracat deneyimi / lojistik hattı yok | TBD | UNKNOWN |
| 4 | Menşe ispat belgesi verilemiyor (tercihli tarife kaybı) | TBD | UNKNOWN |
| 5 | Private label kapasitesi yok **ve** distribütörlük fırsatı yok | TBD | UNKNOWN |

---

## 6. BU BULGUYU NE ÇÜRÜTÜR?

*(Doldurulduğunda `global-sourcing-kasifi` tarafından yazılacak)*

- Gösterge fiyat ile gerçek teklif arasındaki sapma ne kadar?
- MOQ gerçekte 3x çıkarsa hangi ülkeler elenir?
- Tercihli tarifenin ÖTV'yi etkilemediği doğrulanırsa ülke sıralaması değişir mi?
- En ucuz ülke aynı zamanda en uzun lead time'a sahipse net etki ne?
