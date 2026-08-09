---
description: Kanıt tazeliği denetimi — TTL dolmuş verileri bulur ve yeniden doğrulatır
---

# TAZELİK KONTROLÜ

Bu proje **hızlı bozulan** veriler üzerine kuruludur. Bir kanıt kartı bugün
doğru olsa da üç ay sonra yanlış olabilir.

## HIZLI BOZULAN VERİLER

| Veri | Tipik TTL | Sorumlu ajan |
|------|-----------|--------------|
| ÖTV maktu tutarı | Çok kısa — periyodik güncellenir | `gumruk-vergi-uzmani` |
| Gümrük vergisi oranı / İthalat Rejimi | Yıllık + ara değişiklik | `gumruk-vergi-uzmani` |
| KKDF oranı | Değişebilir | `gumruk-vergi-uzmani` |
| Gözetim / referans kıymet | Tebliğ bazlı, sık değişir | `gumruk-vergi-uzmani` |
| Navlun (spot) | Haftalar | `navlun-lojistik-uzmani` |
| Demurrage / terminal ücretleri | Aylar | `navlun-lojistik-uzmani` |
| Raf fiyatı gözlemi | Haftalar | `turkiye-pazar-kasifi` |
| FX kuru | Günler | `finans-fizibilite` girdisi (`makro.yaml`) |
| Tedarikçi gösterge fiyatı | Aylar | `global-sourcing-kasifi` |
| Kanal ticaret koşulları | Yıllık müzakere | `kanal-marj-uzmani` |
| Ruhsat prosedürü / harçlar | Yıllık | `mevzuat-ruhsat-uzmani` |

## ADIMLAR

1. `10-evidence/index.csv` taranır.
2. `access_date + ttl < bugün` olan kanıtlar listelenir → **STALE**.
3. Her STALE kanıt için:
   - Modelde kullanılıyor mu?
   - Kullanılıyorsa → sorumlu ajana yeniden doğrulama ticket'ı açılır.
   - Kullanılmıyorsa → sadece işaretlenir.
4. Yeniden doğrulama sonucu:
   - **Değer aynı** → yeni kanıt kartı açılır (yeni `access_date`),
     eskisi `supersedes` ile bağlanır.
   - **Değer değişmiş** → yeni kart açılır, eski kart `status: SUPERSEDED`
     olur, `finans-fizibilite`'ye modeli yeniden çalıştırma ticket'ı açılır.
   - **Doğrulanamıyor** → `status: UNKNOWN`, başkana bildirilir.

**Kanıt kartları immutable'dır — mevcut kart düzenlenmez, yenisi açılır.**

## ÖZEL KONTROL — YÜRÜRLÜK TARİHİ

Vergi ve mevzuat kanıtlarında `effective_date` kontrolü ayrıca yapılır:
- Kanıtın dayandığı düzenleme hâlâ yürürlükte mi?
- Yerine geçen yeni bir tebliğ/karar var mı?
- Modelde kullanılan tutar, **modelin hedef tarihi** için geçerli olan tutar mı?

## ÇIKTI

- `99-ops/veri-tazeligi.md` güncellenir:
  - STALE kanıt listesi
  - Yeniden doğrulanan kanıtlar ve sonuçları
  - Değişen değerler ve modele etkisi
  - Açılan ticket'lar
- Model etkilenmişse `yatirim-komitesi-baskani`'na bildirim
