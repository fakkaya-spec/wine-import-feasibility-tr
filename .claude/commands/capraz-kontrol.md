---
description: Ajanlar arası çapraz kontrol — çelişki, boşluk ve kanıt kalitesi denetimi
---

# ÇAPRAZ KONTROL

Bu komut ajanların birbirinden bağımsız ürettiği bulguları karşılaştırır ve
tutarsızlıkları yüzeye çıkarır. `yatirim-komitesi-baskani` yürütür.

## 1. KANIT BÜTÜNLÜĞÜ

- `10-evidence/index.csv` içindeki her satırın `10-evidence/raw/` altında
  kartı var mı?
- Kartı olup index'te olmayan kanıt var mı?
- `evidence_id` formatı doğru mu (`EV-YYYY-MM-DD-###`)?
- Aynı `evidence_id` iki kez kullanılmış mı?
- `supersedes` zincirleri kopuk mu? Superseded kart hâlâ modelde kullanılıyor mu?
- `ttl` dolmuş kanıt modelde kullanılıyor mu? → `99-ops/veri-tazeligi.md`

## 2. TIER DENETİMİ

- Vergi/mevzuat sonucu **T5'e mi dayanıyor**? → geçersiz, ticket aç.
- T4 verisi `FACT` diye mi sunulmuş? → `ESTIMATE`/`ASSUMPTION`'a indir.
- `effective_date` yazılmamış vergi/mevzuat bulgusu var mı? → geçersiz.

## 3. KATMAN KARIŞMASI KONTROLÜ

`CLAUDE.md` §6'daki L0–L8 katmanları üzerinden:
- Bir ajanın "maliyet" dediği sayı hangi katman? Belirtilmiş mi?
- EXW ile FOB karışmış mı?
- CIF ile landed cost karışmış mı?
- Raf fiyatı (L8) ile perakendeci alış fiyatı (L7) karışmış mı?
- **Çift sayım**: navlun hem CIF içinde hem ayrı lojistik gideri olarak
  sayılmış mı? Sigorta? Gümrük müşavirliği?

## 4. VERGİ MATRAH KONTROLÜ

- `30-vergi-gumruk/matrah-sirasi.md` net mi?
- Her verginin matrahı açıkça yazılmış mı?
- Bir verginin matrahına başka bir vergi giriyorsa bu açıkça belirtilmiş mi?
- KDV iki perspektifte (ekonomik maliyet / cash timing) ayrılmış mı?

## 5. ALAN İHLALİ KONTROLÜ

Her ajan raporunda:
- Kendi kapsamı dışında **sonuç** üretmiş mi? → o kısım geçersiz, sil/işaretle.
- Alan dışı bulgusunu `99-ops/capraz-ipuclari.md`'ye bırakmış mı?

## 6. ÇELİŞKİ TESPİTİ

İki ajan veya iki kaynak aynı konuda farklı şey söylüyorsa:
- `99-ops/celiskiler.md` dosyasına `C-###` ile kaydet.
- Her iki kaynağın tier'ını ve tarihini yaz.
- **Sessizce birini seçme.**
- İlgili ajana doğrulama ticket'ı aç.

Tipik çelişki noktaları:
- ÖTV maktu tutarının hangi tarihli versiyonu
- Navlun spot vs kontrat
- Raf fiyatı online vs mağaza
- MOQ gösterge vs gerçek teklif
- Marj brüt vs net, KDV dahil vs hariç

## 7. BOŞLUK TESPİTİ

`80-model/inputs/` altındaki her YAML için:
- Hangi alanlar hâlâ `null` / `UNKNOWN`?
- Bu alan hangi ajanın sorumluluğunda?
- Model için **kritik** mi? Kritikse ticket aç, `impact` belirle.

## 8. "BU BULGUYU NE ÇÜRÜTÜR?" DENETİMİ

Her ajan raporunda bu bölüm var mı? Yoksa rapor eksiktir — geri gönder.
Bölüm varsa içi dolu mu, yoksa formalite mi?

## ÇIKTI

- Güncellenmiş `99-ops/celiskiler.md`
- Güncellenmiş `99-ops/acik-sorular.md`
- Yeni ticket'lar (`99-ops/tickets/T-###.md`)
- Çapraz kontrol özet raporu: neyi geçti, neyi geçmedi, ne bloke
