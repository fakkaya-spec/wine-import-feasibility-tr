# AÇIK SORULAR — turkiye-pazar-kasifi / TUR 2

> Ana dosyaya (`99-ops/acik-sorular.md`) **başkan** merge eder.

---

## OQ-551 — İthalatçı kodlarının 13/17'sinin karşılığı kim?

```yaml
id:          OQ-551
opened_by:   turkiye-pazar-kasifi
opened_date: 2026-08-10
status:      OPEN
impact:      MEDIUM
evidence:    EV-2026-08-10-557
```

**Soru:** Perakendeci feed'indeki şu kodların hangi tüzel kişiye karşılık geldiği
doğrulanmadı: `LUCE`, `frosta`, `Midas`, `demglobal`, `Future`, `MALTİTHAL`,
`küregıdaithal`, `ADT`, `piramitgıda`, `PiyasaGıda`, `INANC`, `Vinist`, `Nadiya`.

Doğrulananlar: `KVKLDR` = Kavaklıdere (FACT), `KDT` = Karagözoğlu Dış Ticaret (FACT),
`ADCO` = Adco Gıda (kimlik FACT, portföy ESTIMATE), `BRN` = Baron Şarapçılık (ESTIMATE).

**Neden açık:** Bandımıza en yakın markaları taşıyan kodlar (`PiyasaGıda`,
`piramitgıda`, `Vinist`, `frosta`) tam da **çözülemeyenler** arasında.

**Nasıl kapanır:** (a) Üretici sitelerinin "distributors" sayfaları (Antinori
yöntemi — çalışıyor); (b) şişe arka etiketinde ithalatçı satırının fiziksel
gözlemi; (c) TADAB belge sahipleri listesi (`T-564`).

**Alt soru (çelişki izi):** J.P. Chenet'yi Baron Şarapçılık mı getiriyor, yoksa
`interaytrading.com` mu? İkisi de sitesinde bu markayı gösteriyor. Çelişki kaydı
**açılmadı** çünkü ikisi de T5/zayıf ve modele girmiyor.

---

## OQ-552 — 500–1.000 TL bandı "boş" mu, "stoksuz" mu?

```yaml
id:          OQ-552
opened_by:   turkiye-pazar-kasifi
opened_date: 2026-08-10
status:      OPEN
impact:      HIGH
evidence:    EV-2026-08-10-551, EV-2026-08-10-552
ticket:      T-561
```

**Soru:** İncelenen kanalda bu bantta **62 ithal ürün tanımlı** ama **0 tanesi
stokta**. Bu:

- **(a)** Bu ürünlerin Türkiye'de artık satılmadığı anlamına mı geliyor?
- **(b)** Yoksa bu perakendecinin bu bandı **kasten taşımadığı** (düşük marj /
  düşük ortalama sepet) anlamına mı geliyor?
- **(c)** Yoksa bunlar başka kanallarda (Metro, tekel bayii, zincir market)
  **normal olarak satılıyor** ve sadece bu online kanalda mı yok?

**Neden kritik:** (a) ise hedef bandımızda talep sorunu vardır → `KILL` yönü.
(b) veya (c) ise bandımız sağlamdır ve gözlem aracımız yanlıştır → yalnızca
**kanal seçimi** sorunudur.

**Nasıl kapanır:** Fiziksel mağaza turu. Aranacak somut SKU listesi hazır:
Santa Helena 677 · M. Chapoutier Belleruche 680 · Hans Baer Pinot Noir 702 ·
Henkell 746 · Terra Mater Reserve 770 · Botter Caleo 838 · Luccarelli Primitivo 864 ·
Barone Montalto 950 · La Vieille Ferme 979 · Alpaca 429 · Imperial Vin 512.
Bu isimlerin Metro / Migros / tekel bayii rafında **var olup olmadığı ve fiyatı**,
`OQ-502` ile aynı ziyarette toplanabilir.

---

## OQ-553 — Kısa listedeki üreticiler Türkiye'ye daha önce ihracat yaptı mı?

```yaml
id:          OQ-553
opened_by:   turkiye-pazar-kasifi
opened_date: 2026-08-10
status:      OPEN
impact:      MEDIUM
evidence:    EV-2026-08-10-553
ticket:      T-562
```

**Soru:** 11 tedarikçinin hiçbirinin ürünü Türkiye'de bulunamadı. Ama private label
üreticileri için bu **beklenen** sonuçtur. Doğru soru: *"Türkiye'ye daha önce
ihracat yaptınız mı, kime, ne zaman, ne hacimde?"*

`tedarikci-havuzu.csv → exported_to_turkey_before` alanı **11/11 satırda UNKNOWN**.

**Nasıl kapanır:** RFQ (`global-sourcing-kasifi`). Masabaşından kapanmaz: ticari
veri sağlayıcıları (volza, exportgenius) bu oturumda **403** döndü.

---

## DEVREDEN AÇIK SORULAR — TUR 2'DE ELE ALINMADI

| id | Konu | TUR 2 notu |
|---|---|---|
| `OQ-001` | Benchmark KDV / promosyon | **Kasten ele alınmadı** — TUR 2 kapsam sınırı (`T-504` açık, fiziksel gözlem gerektiriyor) |
| `OQ-502` | Zincir market / tekel bayii raf fiyatı | Kapanmadı. `OQ-552` ile **aynı ziyarette** kapanabilir hâle geldi |
| `OQ-503` | Gold Country / Central Creek ithalatçısı | Kapanmadı. "Gold Country" markasının üretici/sahibi de bulunamadı |
| `T-505` | Resmî ithalat hacmi + ithalatçı listesi | Kapanmadı; `T-564` ile somut isim listesi eklendi |
