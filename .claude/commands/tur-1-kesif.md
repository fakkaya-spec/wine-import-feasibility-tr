---
description: TUR 1 — Paralel keşif turunu başlatır (5 ajan eşzamanlı)
---

# TUR 1 — PARALEL KEŞİF

## ÖN KOŞUL (ATLANAMAZ)

Bu komutu çalıştırmadan önce doğrula:

1. `.claude/agents/` altında 9 ajan dosyası var mı?
2. **Mevcut session'ın agent registry'si bu 9 ajanı gerçekten tanıyor mu?**

Registry bu ajanları tanımıyorsa:
- `general-purpose` **KULLANMA**
- `Explore` **KULLANMA**
- başka ajanı **vekil atama**
- görevi başka agent type'a **taşıma**
- ajanların çalıştığını **iddia etme**

Bunun yerine tam olarak şunu yaz ve DUR:

```
SESSION RESTART REQUIRED
```

## ÇALIŞTIRILACAK AJANLAR (PARALEL)

Aşağıdaki 5 ajan **aynı anda** başlatılır:

1. `gumruk-vergi-uzmani`
2. `mevzuat-ruhsat-uzmani`
3. `navlun-lojistik-uzmani`
4. `global-sourcing-kasifi`
5. `turkiye-pazar-kasifi`

`kanal-marj-uzmani` bu turda **çalışmaz** (TUR 2).
`finans-fizibilite` bu turda **çalışmaz** (TUR 3).
`seytanin-avukati` bu turda **çalışmaz** (TUR 4).

## HER AJANA VERİLECEK ORTAK TALİMAT

- `CLAUDE.md` bağlayıcıdır, önce oku.
- `00-charter/` altındaki üç dosyayı oku (benchmark, kapsam, karar-esikleri).
- Yalnızca **kendi görev alanında** sonuç üret.
- Alan dışı bulguyu `99-ops/capraz-ipuclari.md` dosyasına bırak.
- Her önemli sayı için `10-evidence/raw/` altına kanıt kartı aç,
  `10-evidence/index.csv` dosyasına satır ekle.
- Vergi/mevzuat sonucunu **T1/T2** ile doğrula. T5 tek başına yetmez.
- Bulamadığın şeye `UNKNOWN` yaz. **Uydurma.**
- Raporunu `_SABLON-ajan-raporu.md` formatında yaz.
- Raporun sonunda **"Bu bulguyu ne çürütür?"** bölümü zorunludur.

## ÖNCELİKLİ AÇIK SORU

`turkiye-pazar-kasifi` için birinci öncelik:
**OPEN QUESTION #001** — Metro'da görülen 599,90 TL KDV dahil mi, hariç mi;
tüketici fiyatı mı, profesyonel/cash&carry fiyatı mı?

## TUR SONU

Tur bitince:
1. Her ajanın raporunu topla.
2. `99-ops/acik-sorular.md` ve `99-ops/celiskiler.md` dosyalarını güncelle.
3. `10-evidence/index.csv` bütünlüğünü kontrol et (her kanıtın kartı var mı).
4. `yatirim-komitesi-baskani` ajanına kanıt kalitesi kontrolü yaptır.
5. TUR 2'ye geçmeden başkanın onayını al.
