# ÇELİŞKİLER — `turkiye-pazar-kasifi` / TUR 1.5

> Bu dosya `99-ops/celiskiler.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından DOKUNULMAMIŞTIR.

---

## C-551 — Metro'nun ŞARAP kategorisinde çiftli KDV gösterimi (2010) vs genel broşürde tekli gösterim (2026)

```yaml
conflict_id:     C-551
acan_ajan:       turkiye-pazar-kasifi
acilis_tarihi:   2026-08-10
celiski_turu:    TARIH | KAPSAM  (hangisi olduğu BAŞKAN KARARI — T-551)
impact:          HIGH
durum:           OPEN
ticket:          T-551
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **evidence_id** | `EV-2026-08-09-503`, `EV-2026-08-09-504` | `EV-2026-08-10-503` |
| **tier / tarih** | T4 / 2026-08-01 – 2026-08-11 | T4 / 2008-12-04, 2009-12-03, **2010-12-09** |
| **Ne diyor** | Metro Türkiye broşürlerinde her fiyat **tek** sayıdır ve yanında `KDV'li` yazar; 58 sayfada tek bir "KDV hariç" ibaresi **yoktur**; ikinci küçük sayı **birim fiyattır** | Metro Türkiye **şarap** kataloglarının künyesi: *"Bu Metropost'taki fiyatlar **KDV Hariç ve KDV'li** olarak verilmiştir"*; fiyat kutuları **çifttir** (131,36 / 155,00 `KDV'li`; oran 1,18) |
| **Kapsam** | **Genel** broşür — içinde **0 alkol SKU'su** var (`EV-2026-08-09-514`) | **Şarap kategorisi** kataloğu |

### Neden çelişki olarak kaydedildi

TUR 1, OQ-001'in kurucu hipotezini (*"Metro etiketinde KDV hariç + KDV dahil
birlikte gösterilebilir"*) **çürüdü** ilan etti. `EV-2026-08-10-503` bu
hipotezin Metro Türkiye'nin **şarap kategorisinde fiilen uygulanmış bir
format** olduğunu gösteriyor. Sonuç aynı kalabilir, ama gerekçe artık
"böyle bir format yoktur" olamaz.

### Neden bu ajan tarafından ÇÖZÜLMEDİ

1. CLAUDE.md §1.13 — sessizce seçim yapılmaz.
2. TUR 1.5 görev tanımı KDV sonucunu **korunacak doğrulama** ilan etti;
   yeniden araştırma ve yeniden tartışma yasaklandı. Bulgu **T-504'ün**
   peşine düşerken ortaya çıktı; saklamak da ihlal olurdu.
3. `pazar.yaml`'da değer **DEĞİŞTİRİLMEDİ**; yalnızca `conflict_id: C-551`
   işareti kondu.

### Çözüm hiyerarşisi hangi kuralı işaret ediyor

- **Kural 1 (tier):** uygulanamaz — ikisi de T4, ikisi de Metro'nun **kendi**
  künyeli yayını.
- **Kural 2 (tarih):** **A lehine** — 16 yıl fark; 2013 alkol reklam yasağı
  arada bir kırılma noktasıdır.
- **Kural 4 (kapsam):** **B lehine** — A, ilgilenilen kategoriyi (**şarap**)
  hiç içermez; B tam o kategoridir.

Kural 2 ve kural 4 **zıt yönü işaret ediyor.** Karar başkanındır → `T-551`.

### Bu ajanın önerisi (karar değildir)

`benchmark_*.kdv_durumu` **`KDV_DAHIL` kalsın** (tarih kuralı + fiyat sonu
deseni), **ancak** `confidence` `HIGH`→`MEDIUM`'a çekilsin ve **BM_B
senaryosu ELENMESİN**. Kesin çözüm için gereken şey değişmiyor:
**şarap reyonundaki fiziksel etiketin fotoğrafı** (`T-504`).
