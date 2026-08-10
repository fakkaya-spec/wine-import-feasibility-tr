# ÇELİŞKİLER — turkiye-pazar-kasifi / TUR 2

> Bu dosya `99-ops/celiskiler.md` içine **başkan tarafından** merge edilir.
> Bu ajan ana dosyaya dokunmamıştır.

---

## C-561 — Stokta olmayan ithal listelemeler tek bir "geçersiz" havuz mudur?

```yaml
conflict_id:   C-561
opened_by:     turkiye-pazar-kasifi
opened_date:   2026-08-10
status:        OPEN
ticket:        T-561
ilgili:        C-501 (TUR 1, OPEN) — bu çelişki onun NİTELENMESİDİR, yerine geçmez
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **Kayıt** | `EV-2026-08-09-509` / `EV-2026-08-10-501` (T4, 2026-08-09) | `EV-2026-08-10-552` (T4, 2026-08-10) |
| **İddia** | Stokta olmayan ithal listelemelerde "70–450 TL gibi 2026 için gerçeklik dışı fiyatlar" vardır → havuz **bütünüyle** dışlanır (`C-501`) | Aynı havuz sayıldığında **iki modludur**: 44 kayıt < 500 TL (gerçeklik dışı), **62 kayıt 500–1.000 TL** (2026 için makul), 243 kayıt > 1.000 TL |
| **Tier / tarih** | T4 / 2026-08-09 | T4 / 2026-08-10 |

### Neden çelişki

`C-501`'in gerekçesi **düşük uçtaki** kayıtlardan türetilmiş, ama sonucu **tüm**
stokta-olmayan havuza uygulanmıştır. TUR 2 sayımı gösteriyor ki düşük uç havuzun
yalnızca **%12,6**'sıdır (44/349). Geri kalan kayıtlar için "bakımsız eski fiyat"
gerekçesi **doğrudan kanıtlanmamıştır**.

Bu, `pazar.yaml → segment.ithal_sku_400_800_uzman_kanal = 0` değerinin dayanağını
doğrudan etkiler.

### Çözüm hiyerarşisi bu vakada ne diyor

- **Tarih kuralı:** B daha yenidir (2026-08-10) → B'yi işaret eder.
- **Kaynak otoritesi:** ikisi de T4, ikisi de aynı feed → ayırt etmiyor.
- **Kapsam kuralı:** B daha dar ve daha ölçülmüş bir iddiadır → B'yi işaret eder.

**Ama:** B, A'nın *sonucunu* çürütmez. Her iki durumda da **stokta olmayan bir fiyat
satın alınabilir bir fiyat değildir** ve raf fiyatı sayılamaz. Çelişki, "0 ithal SKU"
cümlesinin **anlamı** hakkındadır: *yok* mu, *var ama satılmıyor* mu?

### Bu ajanın yaptığı / yapmadığı

- **Yapmadım:** `pazar.yaml`'da hiçbir değeri değiştirmedim; C-501'i kapatmadım;
  62 listelemeyi raf fiyatı saymadım.
- **Yaptım:** Sayımı kanıtladım (`EV-2026-08-10-552`), 62 satırı
  `raf-fiyat-gozlemleri.csv`'ye `gozlem_yontemi = ONLINE_LISTING_STOKTA_YOK` ve
  `status = UNKNOWN` ile ekledim, `T-561` ile başkana taşıdım.

### Karar kime ait

`yatirim-komitesi-baskani` — `T-561`.

---

## İZLEME — TUR 1/1.5'ten devreden ve TUR 2'de ELE ALINMAYANLAR

| conflict_id | Durum | TUR 2 notu |
|---|---|---|
| `C-501` | OPEN | `C-561` ile **nitelendi**, çözülmedi |
| `C-502` | OPEN (izleme) | Ele alınmadı |
| `C-503` | RESOLVED (başkan) | Ele alınmadı |
| `C-551` | OPEN / NON_BLOCKING_TUR2 | **Kasten ele alınmadı** — TUR 2 kapsam sınırı: benchmark KDV/promosyon araştırması yasaklandı |

---

## POTANSİYEL ÇELİŞKİ — AÇILMADI, İZ BIRAKILDI

**J.P. Chenet'nin Türkiye ithalatçısı kim?**
`EV-2026-08-10-562` (T5) **Baron Şarapçılık** diyor. Ancak `interaytrading.com`
adlı başka bir firma da sitesinde "J.P. CHENET Ürünleri" sayfası tutmaktadır.
Bu bir alt-bayilik mi, eski bir ithalatçı mı, yoksa gerçek bir çelişki mi
**doğrulanamadı**. Her iki kaynak da T5/T4-zayıftır ve modele girmemektedir;
bu nedenle **çelişki kaydı AÇILMAMIŞ**, `OQ-551` altında açık soru olarak
bırakılmıştır.
