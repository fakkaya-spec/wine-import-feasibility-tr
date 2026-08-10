# AÇIK SORULAR — turkiye-pazar-kasifi / TUR 2.5

> Bu dosya `99-ops/acik-sorular.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından **dokunulmamıştır**.

---

## OQ-701 — Zincir market / tekel bayii rafında giriş segmenti şarap fiyatı nedir?

```yaml
soru_id:      OQ-701
acan:         turkiye-pazar-kasifi
tarih:        2026-08-10
durum:        OPEN
oncelik:      HIGH
ilgili:       T-701, OQ-502, EV-2026-08-10-703, EV-2026-08-09-511
```

**Soru:** Migros / Macrocenter / CarrefourSA ve tekel bayii rafında, 2026'da
750 ml giriş segmenti şarabın (yerli ve ithal) tüketici raf fiyatı nedir?

**Neden açık:** Türkiye'de alkol tüketiciye internetten satılamadığı için bu
katmanda **hiç gözlem yoktur** (`EV-2026-08-09-511`). Projenin
`l8_chain_retail.deger_try` alanı **null / UNKNOWN**'dır.

**Neden şimdi kritik oldu:** TUR 2.5'te üretilen hedef raf fiyatı merdiveni
(599–999 TL) tam da bu katmanı hedeflemektedir. Merdivenin **göreli** sıralaması
yapılabilmiş, **mutlak** konumu doğrulanamamıştır.

**Elimizdeki tek (ZAYIF) sinyal:** `EV-2026-08-10-703` — T5 içerik çiftlikleri
"Migros ve tekelde 75 cl şarap ortalama 450–650 TL" demektedir.
**DOĞRULANMAMIŞTIR, MODELE GİREMEZ** (`C-503` ile aynı kaynak sınıfı).
Ama **yönü önemlidir**: doğruysa, gözlenen online uzman kanalın
(stokta yerli medyan **1.410 TL**, `EV-2026-08-10-702`) **tersini** söyler ve
hedef merdivenin üst basamaklarını (899 / 999 TL) çok daha zor bir rekabet
konumuna düşürür.

**Nasıl kapanır:** Fiziksel mağaza turu — `T-504` / `OQ-502` / `OQ-552` ile
**aynı ziyarette**, ek maliyetsiz.

---

## OQ-702 — Gözlenen online uzman kanal, giriş segmentini hiç taşımıyor mu, yoksa şu an mı stoksuz?

```yaml
soru_id:      OQ-702
acan:         turkiye-pazar-kasifi
tarih:        2026-08-10
durum:        OPEN
oncelik:      MEDIUM
ilgili:       C-501, C-561, T-561, EV-2026-08-10-702
```

**Soru:** iyisarap.plus'ın tüm stokta katalogunda (471 SKU) 600 TL altında
**yalnızca 1** SKU vardır ve stokta yerli medyan **1.410 TL**'dir. Bu, kanalın
**kalıcı assortman politikası** mıdır, yoksa **geçici bir stok durumu** mudur?

**Neden önemli:** Eğer kalıcı politikaysa, "500–1.000 TL bandında ithal şarap
yok" bulgusunun **büyük kısmı kanal artefaktıdır** ve pazar boşluğu olarak
okunamaz. Bu, `C-501` ve `C-561`'in **her ikisini de** yeniden çerçeveler.

**Nasıl kapanır:** Aynı kanalın 2–3 farklı tarihte (örn. +30 gün, +60 gün)
ölçülmesi; veya kanalın kendi "en ucuz şaraplar" koleksiyonunun incelenmesi.
Bu ajan tarafından yapılabilir, ek kaynak gerektirmez.

---

## OQ-703 — 599 TL hedefi bir pazar fiyatı mı, yoksa tek bir promosyonun izdüşümü mü?

```yaml
soru_id:      OQ-703
acan:         turkiye-pazar-kasifi
tarih:        2026-08-10
durum:        OPEN
oncelik:      HIGH
ilgili:       T-504 (CRITICAL, OPEN), OQ-001
```

**Soru:** `TARGET_SHELF_PRICE = 599 TL` basamağının **tek** destekleyici gözlemi
`OBSERVED_BENCHMARK = 599,90 TL`'dir. O gözlemin promosyon durumu `UNKNOWN`'dır.
Promosyonluysa 599 TL hedefinin **hiçbir** gözlemsel dayanağı kalmaz.

**Durum:** Bu, `T-504`'ün (CRITICAL, OPEN) hedef tarafındaki sonucudur.
**Yeni bir araştırma açılmamıştır** — TUR 2.5 kapsamı gereği Gold Country
promosyon araştırmasına dönülmemiştir. Burada yalnızca **hedef merdivene olan
bağı** kayda geçirilmektedir.

**Etkisi:** `T-504` "promosyonlu" diye kapanırsa
`60-pazar/target-shelf-price-analysis.md` §3.1'deki `AGGRESSIVE` etiketi
**`TOO_LOW`**'a döner ve PRIMARY/SECONDARY önerisi **yukarı** kaymaz — ama
599 TL downside senaryosu **elenir**.
