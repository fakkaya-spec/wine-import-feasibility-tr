# VERİ TAZELİĞİ

> Bu proje **hızlı bozulan** veriler üzerine kuruludur. Bugün doğru olan bir
> kanıt üç ay sonra yanlış olabilir. `/tazelik-kontrol` komutu bu dosyayı
> yönetir.

---

## DURUM: BOŞ

Bu turda (TUR 0) kanıt toplanmadığı için henüz izlenecek veri yoktur.
`10-evidence/index.csv` boştur.

> ⚠ **GÜNCEL DEĞİL — 2026-08-10 itibarıyla bu bölüm aşılmıştır.**
> TUR 1 ve TUR 2'de kanıt toplanmıştır. Aktif tazelik durumu için bkz.
> **§TAZELİK KONTROLÜ — 2026-08-10 (TUR 2.5, `navlun-lojistik-uzmani`)**
> (bu dosyanın sonu). Bu bölüm tarihsel kayıt olarak silinmemiştir.

---

## TTL REFERANS TABLOSU

Kanıt kartı açılırken kullanılacak önerilen `ttl` değerleri:

| Veri türü | Önerilen TTL | Sorumlu ajan | Neden |
|-----------|--------------|--------------|-------|
| **ÖTV maktu tutarı** | **30d** | `gumruk-vergi-uzmani` | Periyodik güncellenir; f/p segmentte en öldürücü değişken |
| Gümrük vergisi oranı | 90d | `gumruk-vergi-uzmani` | İthalat Rejimi yıllık + ara değişiklik |
| KKDF oranı | 90d | `gumruk-vergi-uzmani` | Değişebilir |
| Gözetim / referans kıymet | 30d | `gumruk-vergi-uzmani` | Tebliğ bazlı, sık değişir |
| KDV oranı | 180d | `gumruk-vergi-uzmani` | Nispeten stabil |
| **Navlun (spot)** | **14d** | `navlun-lojistik-uzmani` | Çok volatil |
| Navlun (kontrat) | 90d | `navlun-lojistik-uzmani` | Sözleşme süresince stabil |
| Demurrage / terminal ücretleri | 90d | `navlun-lojistik-uzmani` | Tarife bazlı |
| **Raf fiyatı gözlemi** | **30d** | `turkiye-pazar-kasifi` | Enflasyon + promosyon döngüsü |
| **FX kuru** | **7d** | `finans-fizibilite` (makro.yaml) | Günlük değişir |
| Tedarikçi gösterge fiyatı | 90d | `global-sourcing-kasifi` | Hasat/sezon bazlı |
| Tedarikçi firm offer | teklifin geçerlilik süresi | `global-sourcing-kasifi` | Teklifte yazılı |
| Kanal ticaret koşulları | 365d | `kanal-marj-uzmani` | Yıllık müzakere |
| Ruhsat prosedürü / harçlar | 180d | `mevzuat-ruhsat-uzmani` | Yıllık güncelleme |
| İthalat hacmi istatistiği | 365d | `turkiye-pazar-kasifi` | Yıllık yayın |

---

## STALE KANIT TABLOSU

`/tazelik-kontrol` bu tabloyu doldurur.

| evidence_id | claim | access_date | ttl | STALE tarihi | modelde kullanılıyor mu | sorumlu ajan | ticket | durum |
|-------------|-------|-------------|-----|--------------|------------------------|--------------|--------|-------|
| *(boş)* | | | | | | | | |

---

## YENİDEN DOĞRULAMA KAYDI

| tarih | eski evidence_id | yeni evidence_id | değer değişti mi | modele etkisi | modeli yeniden çalıştırma ticket'ı |
|-------|------------------|------------------|------------------|---------------|-----------------------------------|
| *(boş)* | | | | | |

---

## KURALLAR

1. **Kanıt kartları immutable'dır.** Yeniden doğrulamada eski kart
   **düzenlenmez**; yeni kart açılır, `supersedes` ile bağlanır, eskinin
   `status` alanı `SUPERSEDED` yapılır.
2. `access_date + ttl < bugün` olan kanıt **STALE**'dir.
3. STALE kanıt modelde kullanılıyorsa → sorumlu ajana ticket açılır.
4. Değer değişmişse → `finans-fizibilite`'ye modeli yeniden çalıştırma
   ticket'ı açılır.
5. Yeniden doğrulanamıyorsa → `status: UNKNOWN`, başkana bildirilir.

---

## ÖZEL KONTROL — YÜRÜRLÜK TARİHİ

Vergi ve mevzuat kanıtlarında `ttl` tek başına yetmez. Ayrıca:

- Kanıtın dayandığı düzenleme **hâlâ yürürlükte mi?**
- Yerine geçen yeni bir tebliğ/karar **var mı?**
- Modelde kullanılan tutar, **modelin hedef tarihinde** geçerli olacak tutar mı?
  (bkz. `99-ops/acik-sorular.md` → **OQ-002**)

Bir kanıt `ttl` içinde olabilir ama yine de geçersiz olabilir — çünkü
düzenleme değişmiştir. Bu iki kontrol **ayrı** yapılır.

---
---

# TAZELİK KONTROLÜ — 2026-08-10 (TUR 2.5)

```yaml
kontrol_tarihi:  2026-08-10
yapan_ajan:      navlun-lojistik-uzmani
kapsam:          "YALNIZCA lojistik kanıtları (EV-2026-08-09-3xx, EV-2026-08-10-3xx)"
kapsam_disi:     "vergi, mevzuat, pazar, sourcing, kanal kanıtları — ilgili ajanlar kontrol eder"
detay:           40-lojistik/lojistik-senaryolari-tur25.md §1
```

> **Bu bölüm silinmez, üzerine yazılmaz.** Sonraki kontroller yeni bölüm olarak
> eklenir.

## A) BUGÜN STALE OLAN KANIT — YOK

`2026-08-10` itibarıyla **hiçbir lojistik kanıtı STALE değildir.**
Ancak **en kısa ömürlü set 6 gün içinde ölmektedir** (aşağı bkz.).

## B) EN KRİTİK SET — 10 LCL KOTASYON KARTI (`ttl: 6d`)

```
access_date        = 2026-08-10
ttl                = 6d
kaynagin kendi
gecerlilik tarihi  = 2026-08-16   (Flexport quote validity)
SON GECERLI GUN    = 2026-08-16
STALE              = 2026-08-17   (kural: access_date + ttl < bugun)
BUGUN (2026-08-10) = GECERLI, 6 gun omru kaldi
```

| evidence_id | claim (kısa) | access_date | ttl | **STALE tarihi** | modelde kullanılıyor mu | ticket | durum |
|---|---|---|---|---|---|---|---|
| `EV-2026-08-10-301` | Valencia→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | **EVET — ters modelin BASE rotası** | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-302` | Barcelona→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | EVET | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-303` | Lizbon→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | EVET (rota karş.) | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-305` | Marsilya→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | EVET (rota karş.) | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-306` | San Antonio→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | EVET (rota karş.) | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-307` | Cape Town→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | EVET (rota karş.) | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-308` | Oakland→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | **EVET — benchmark ürün rotası** | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-309` | Los Angeles→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | EVET (benchmark) | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-310` | Buenos Aires→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | EVET (rota karş.) | `T-802` | GEÇERLİ (6 gün) |
| `EV-2026-08-10-311` | Melbourne→İstanbul LCL | 2026-08-10 | 6d | **2026-08-17** | EVET (rota karş.) | `T-802` | GEÇERLİ (6 gün) |

### ⚠ SAYIM DÜZELTMESİ: **11 değil, 10 kart**

`40-lojistik/rota-maliyet-matrisi.md` §8 ve `99-ops/tickets/T-304.md` §4 bu seti
`EV-2026-08-10-301 … -311` = **"11 LCL kartı"** olarak tarif eder.
`10-evidence/index.csv` kontrolü bunu **yanlışlar**:

- `EV-2026-08-10-304` (İtalya) → `ttl: 14d`, `status: UNKNOWN`, **içinde navlun
  rakamı yok** ("0 offerings" bulgusu). 6d setine **ait değildir**.
- Aralıkta `ttl: 6d` olan **10** kart vardır.

Kanıt kartları immutable'dır; `index.csv` bu turda değiştirilmemiştir.
Düzeltme burada kayıt altına alınmıştır → **`T-801`** (impact: LOW).
**Modele etkisi yoktur** (–304 zaten `UNKNOWN`), ama yeniden doğrulamada
aranacak kart sayısını etkiler.

### İKİ AYRI KONTROL, AYNI TARİH

`§ÖZEL KONTROL — YÜRÜRLÜK TARİHİ` gereği iki kontrol ayrı yapılmıştır:

| Kontrol | Sonuç |
|---|---|
| `ttl` kontrolü (`access_date + 6d`) | son geçerli gün **2026-08-16** |
| Kaynağın kendi geçerliliği (quote validity) | **2026-08-16** |

Tesadüf değildir: `ttl`, kotasyonun kendi geçerlilik süresine eşit seçilmişti.
**Sonuç: bu kartlar `ttl` dolduğunda sadece eskimekle kalmaz — kaynak tarafından
geri çekilmiş olur.** İkinci kontrol birinciyi gevşetmez, doğrular.

## C) BAĞLAYICI KURAL — 2026-08-17 SONRASI

> **STALE bir kanıt otomatik olarak geçerli `FACT` gibi KULLANILAMAZ.**

| Tarih | LCL kartlarının statüsü | Sonuç |
|---|---|---|
| **≤ 2026-08-16** | `FACT`, confidence `MEDIUM` | Ters model bu kartlara dayanabilir |
| **≥ 2026-08-17** | `FACT` **düşer** → `ESTIMATE`, confidence `LOW` | `40-lojistik/lojistik-senaryolari-tur25.md` §3, §4 (LCL satırları), §5.1 ve §6 **geçerli FACT olarak kullanılamaz** |

**Türev kartlar da düşer.** `EV-2026-08-10-329` (şişe başı maliyet) ve
`EV-2026-08-10-330` (LCL/FCL kırılma noktası) girdilerini bu 10 karttan alır.
Kendi `ttl`'leri 14d olsa bile **bir türev, kaynağından daha taze olamaz** →
2026-08-17'de bunlar da STALE sayılmalıdır.

**Projedeki tek gerçek navlun verisi budur.** FCL zaten `UNKNOWN`'dır
(`T-304`, `C-311`). 2026-08-17'den sonra model çalıştırılırsa lojistik girdisi
**bütünüyle** `ESTIMATE / LOW`'a düşer.

## D) DİĞER LOJİSTİK KANITLARININ TAKVİMİ

| Kanıt sınıfı | evidence_id | ttl | son geçerli gün | STALE |
|---|---|---|---|---|
| **LCL kotasyonları (10 kart)** | `-301,-302,-303,-305,-306,-307,-308,-309,-310,-311` | **6d** | **2026-08-16** | **2026-08-17** ⚠ |
| İtalya "0 offerings" | `EV-2026-08-10-304` | 14d | 2026-08-24 | 2026-08-25 |
| FCL kotasyon yokluğu | `EV-2026-08-10-312` | 14d | 2026-08-24 | 2026-08-25 |
| FCL dolaylı göstergeler | `EV-2026-08-10-322`, `-323`, `-324`, `-331` | 14d | 2026-08-24 | 2026-08-25 |
| Türetilmiş maliyet / kırılma | `EV-2026-08-10-329`, `-330` | 14d | 2026-08-24 | **fiilen 2026-08-17** (kaynağa bağlı) |
| TUR 1 navlun göstergeleri | `EV-2026-08-09-330`, `-331`, `-333` | 14d | 2026-08-23 | 2026-08-24 |
| TUR 1 LCL yapısı | `EV-2026-08-09-324` | 30d | 2026-09-08 | 2026-09-09 |
| Taşıyıcı / terminal tarifeleri | `EV-2026-08-10-313 … -319`, `-325`, `-326`, `-327`, `-328`, `-332` | 90d | 2026-11-08 | 2026-11-09 |
| Demurrage / D&D (Maersk) | `EV-2026-08-09-343` | 90d | 2026-11-07 | 2026-11-08 |
| Müşavirlik tarifesi 2026 | `EV-2026-08-09-342` | 1y | 2027-08-09 | 2027-08-10 |
| DFDS 2025 tarifesi | `EV-2026-08-10-320` | — | **zaten eski** | yalnızca **oran** çapası olarak kullanılır |
| DFDS 2018 | `EV-2026-08-10-321` | 0d | — | **SUPERSEDED** |

## E) YENİDEN DOĞRULAMA KAYDI — TUR 2.5

| tarih | eski evidence_id | yeni evidence_id | değer değişti mi | modele etkisi | ticket |
|---|---|---|---|---|---|
| 2026-08-10 | — | — | — | **Yeniden doğrulama YAPILMADI.** Bu tur yalnızca *tazelik durumu tespiti* içindir; görev tanımı yeni navlun araştırmasını yasaklamıştır | `T-802` |

**Aksiyon:** Model 2026-08-16'dan **sonra** çalıştırılacaksa, 10 kart yeniden
doğrulanmalı (yeni kart + `supersedes` + eskinin `status: SUPERSEDED`),
**veya** lojistik girdisi `ESTIMATE / LOW` olarak yeniden etiketlenmelidir.
