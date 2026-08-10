# ÇAPRAZ İPUÇLARI — turkiye-pazar-kasifi / TUR 2.5

> Bu dosya `99-ops/capraz-ipuclari.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından **dokunulmamıştır**.
> Aşağıdakiler **alan dışı bulgulardır**; bu ajan bunlardan **sonuç üretmemiştir**.

---

## İP-701 → `kanal-marj-uzmani`

**Bulgu:** Hedef merdivenin her basamağında gözlenen **stokta rakip SKU sayısı**
(±%10 pencere, tek online uzman kanal, 2026-08-10, `EV-2026-08-10-702`):

| Hedef | Stokta yerli rakip | Stokta ithal rakip |
|---|---|---|
| 599 TL | 3 | 0 |
| 699 TL | 17 | 0 |
| 799 TL | 31 | 1 |
| 899 TL | 35 | 2 |
| 999 TL | 49 | 1 |

**Neden önemli:** Listeleme bedeli ve raf pazarlığı, o raf bölmesinde kaç rakibin
olduğuna duyarlıdır. **Bu bir marj hesabı DEĞİLDİR** — yalnızca rakip sayımıdır.
Marjı bu ajan **hesaplamamıştır ve hesaplayamaz** (`pazar.yaml` K4).

---

## İP-702 → `kanal-marj-uzmani`

**Bulgu:** Gözlenen tek çok-SKU'lu kanalın **tüm stokta katalogunda (471 SKU)
600 TL altında yalnızca 1 SKU** vardır; stokta yerli **medyan 1.410 TL**
(`EV-2026-08-10-702`).

**Neden önemli:** Bu kanalın **giriş segmentini taşımadığı** anlamına gelebilir.
Eğer öyleyse, fiyat/performans bir ithal ürün için doğru kanal bu **değildir** ve
kanal stratejisi Metro / zincir market / tekel bayii üzerinden kurulmalıdır.
Kanal seçimi `kanal-marj-uzmani`'nın alanıdır; bu ajan yalnızca **gözlemi**
bildirmektedir.

---

## İP-703 → `finans-fizibilite`

**Bulgu:** Gözlenen kanalda **stokta ithal taban 875 TL**'dir. Hedef merdivenin
799 TL ve altındaki tüm basamakları bu tabanın **altındadır**.

**Neden önemli:** Ters model 799 TL veya altına kurulursa, sonuç
"gözlenen hiçbir stokta ithal şarabın ulaşmadığı bir fiyat noktası" olur.
Bu **imkânsız** demek değildir (Metro'da 599,90 görülmüştür) ama modelin
çıktısında **açıkça yazılmalıdır**. `T-702`.

---

## İP-704 → `global-sourcing-kasifi`

**Bulgu:** Hedef merdivenin 600–1.000 TL bölgesinde gözlenen rakip seti
**neredeyse tamamen yerlidir** (65 yerli / 2 ithal, stokta,
`EV-2026-08-10-702`). Bu bölgede stok dışı olarak listelenen ithal markaların
menşe profili: İtalya, Fransa, Almanya, Şili, Yeni Zelanda, Gürcistan, Moldova.
**ABD ve Avustralya bu kanalda hiç yoktur** (TUR 1 B-8 / TUR 2 B-6 ile tutarlı).

**Neden önemli:** İki `OBSERVED_BENCHMARK` (ABD ve Avustralya) tam da bu kanalın
**hiç taşımadığı** menşelerdendir. Bu, benchmark'ların Metro'nun kendi
ithalatından geliyor olabileceği ihtimalini güçlendirir — **doğrulanmamıştır**
(`OQ-503`). Sourcing menşe kararında bu asimetri dikkate alınmalıdır.

---

## İP-705 → `yatirim-komitesi-baskani`

**Bulgu:** `TARGET_SHELF_PRICE` merdiveninin asıl karşılığı olan
`L8_CHAIN_RETAIL` katmanında projenin **sıfır gözlemi** vardır.

**Neden önemli:** Bu, `OQ-001`'in (benchmark hangi katman?) **hedef tarafındaki
aynasıdır** ve bugüne kadar adlandırılmamıştır. Ayrıntı ve talep: `T-701`.

---

## İP-706 → `seytanin-avukati`

**Bulgu (kendi aleyhime):** TUR 2.5'in ürettiği yoğunluk eğrisinin **tamamı**
tek bir online uzman perakendecinin **alt kuyruğundan** okunmuştur. TUR 2.5'te
tek kanal zaafını kırmak için **17 ek alan adı** denenmiş, **0 kullanılabilir
kanal** bulunmuştur (`EV-2026-08-10-701`) — TUR 1 ve TUR 2 ile birlikte
**üçüncü başarısız deneme**.

**Neden önemli:** Kırmızı takım bu belgeye saldıracaksa **en zayıf yer burasıdır**
ve bu ajan tarafından **kendisi** işaretlenmiştir. Saldırının hazır cephanesi:
`60-pazar/target-shelf-price-analysis.md` §5 ve §2.4.
