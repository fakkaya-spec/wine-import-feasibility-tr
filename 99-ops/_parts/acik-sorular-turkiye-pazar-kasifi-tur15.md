# AÇIK SORULAR — `turkiye-pazar-kasifi` / TUR 1.5

> `99-ops/acik-sorular.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından DOKUNULMAMIŞTIR.

---

## OQ-001 — durum güncellemesi (TUR 1.5)

**`PARTIALLY_RESOLVED` OLARAK KALIR. KAPANMADI.**

| Ayak | TUR 1 | TUR 1.5 |
|---|---|---|
| KDV dahil mi? | KAPANDI — KDV DAHİL | **KAPALI (korundu)** — ama `C-551` / `T-551` ile *nitelendi*: gerekçe artık "çiftli gösterim yoktur" olamaz |
| Tüketici fiyatı mı / cash&carry mi? | KAPANDI — ikisi de | KAPALI (değişmedi) |
| Etiketteki ikinci sayı | KAPANDI — **birim (litre) fiyatı** | KAPALI (değişmedi) |
| Katman | `L8_METRO_CASH_CARRY` | KAPALI (başkan onaylı) |
| **Promosyon mu, normal mi?** | **UNKNOWN** | **UNKNOWN — 8 masabaşı yolu denendi, hepsi kapalı** (`EV-2026-08-10-504`) |
| Zincir market gerçek L8'i | UNKNOWN | UNKNOWN (araştırılmadı — kapsam dışı) |
| Şarap reyonu fiziksel etiketi | GÖRÜLMEDİ | GÖRÜLMEDİ |

**OQ-001'i kapatan tek şey değişmedi ve fizikseldir:**
şarap reyonundaki etiketin küçük puntolu satırları okunacak fotoğrafı +
2–4 hafta arayla ikinci fiyat gözlemi.

---

## OQ-551 — Metro Türkiye'nin şarap assortman büyüklüğü (DOĞRULANMADI)

```yaml
oq_id:        OQ-551
sorumlu:      turkiye-pazar-kasifi
tur:          TUR 1.5 (yan bulgu)
durum:        OPEN
impact:       MEDIUM
```

TUR 1.5'te `T-504` araştırması sırasında bir web araması özetinde
*"Metro Türkiye'de üzümden elde edilen 502 çeşit içecek var; 342 yerli,
160 yabancı"* biçiminde bir ifadeye rastlandı.

- **Birincil kaynağa ULAŞILAMADI.** Hangi Metro yayınından/basın bülteninden
  geldiği doğrulanamadı.
- **Kanıt kartı AÇILMADI**, çünkü doğrulanamayan bir sayı için kart açmak
  onu meşrulaştırır.
- **MODELE GİREMEZ.**

Neden yine de kaydediliyor: doğruysa, Metro'nun şarap reyonunda **160 ithal
SKU** olduğu anlamına gelir; bu, benchmark'ın "tek başına duran bir ürün"
değil, geniş bir ithal assortmanın parçası olduğunu gösterir ve
`ithal_sku_400_800_uzman_kanal = 0` bulgusunun **kanal spesifik** olduğunu
kuvvetle destekler. TUR 2'de fiziksel mağaza turunda **sayılarak**
doğrulanmalıdır.

---

## Devam eden UNKNOWN'lar (TUR 1'den, TUR 1.5'te DEĞİŞMEDİ)

Bu tur **dar kapsamlıydı**; aşağıdakiler araştırılmadı ve `pazar.yaml`'da
`null` + `UNKNOWN` olarak durmaktadır:

| # | Alan | impact |
|---|---|---|
| 1 | `l8_chain_retail.deger_try` — zincir market gerçek tüketici raf fiyatı | HIGH |
| 2 | `pazar_hacmi.*` — Türkiye şarap ithalat hacmi / menşe kırılımı / trend | HIGH |
| 3 | `ithalatci_haritasi.*` — 1 doğrulanmış ithalatçı bir harita değildir | HIGH |
| 4 | `horeca.fiyat_carpani`, `horeca.hacim_payi_pct` | HIGH |
| 5 | `kanal_yapisi.tekel_bayii_fiyatlari` | HIGH |
| 6 | `benchmark_1.magaza` / `.sehir` / `.abv_pct` / `.ithalatci_distributor` | MEDIUM |
| 7 | `benchmark_2.hacim_ml` (750 ml **doğrulanmadı**) | MEDIUM |
| 8 | `kanal_yapisi.bim_a101_sok_sarap_var_mi`, `bizim_toptan_fiyatlari`, `duty_free` | MEDIUM |
