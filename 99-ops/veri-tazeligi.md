# VERİ TAZELİĞİ

> Bu proje **hızlı bozulan** veriler üzerine kuruludur. Bugün doğru olan bir
> kanıt üç ay sonra yanlış olabilir. `/tazelik-kontrol` komutu bu dosyayı
> yönetir.

---

## DURUM: BOŞ

Bu turda (TUR 0) kanıt toplanmadığı için henüz izlenecek veri yoktur.
`10-evidence/index.csv` boştur.

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
