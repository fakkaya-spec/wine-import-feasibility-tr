# ÇELİŞKİLER — kanal-marj-uzmani, TUR 2

> Bu bir **parça dosyasıdır**. `99-ops/celiskiler.md` ana dosyasına
> `yatirim-komitesi-baskani` tarafından birleştirilir. Bu ajan ana dosyaya
> **DOKUNMAMIŞTIR**.
>
> CLAUDE.md §1.13: kaynaklar çelişirse **sessizce seçim yapılmaz.**
> Aşağıdaki iki çelişkide de **seçim yapılmamıştır.**

---

## C-601 — Zincir market ödeme vadesi: yasal tavan vs gözlenen pratik

```yaml
conflict_id:  C-601
acan_ajan:    kanal-marj-uzmani
tarih:        2026-08-10
durum:        OPEN
etki:         CRITICAL   # peak_cash_requirement'in en buyuk tek surucusu
```

| | Kaynak A | Kaynak B | Kaynak C |
|---|---|---|---|
| **İddia** | Ödeme süresi **60 günü geçemez** | Organize kanal ortalama vadesi **70 gün** | Migros ticari borçlarının **%34,4'ü 3–12 ay** vadeli; DPO **~93 gün** |
| **evidence** | `EV-2026-08-10-602` | `EV-2026-08-10-609` | `EV-2026-08-10-617` |
| **tier** | T3 (içerik T1) | T2 | T4 (denetimden geçmiş) |
| **tarih** | yürürlük **2024-01-01** | veri **2020** | veri **2025-12-31** |
| **kategori** | tarım-gıda ürünleri (şarap kapsamı **?**) | **süt ürünleri** | tüm kategoriler, tüm coğrafya |

### Neden çelişiyor

- **Zaman:** Kaynak B, 60 gün tavanının yürürlüğe girdiği 01.01.2024'ten **önceki**
  dönemi ölçer. Yani B, A'yı çürütmez — A'nın **niçin çıkarıldığını** açıklar.
- **Ama Kaynak C 2025 verisidir**, yani **tavan yürürlükteyken** alınmıştır ve
  borçların üçte biri 3–12 ay vadelidir. Bu, üç şeyden biri anlamına gelir:
  1. Şarap/gıda **tavan kapsamında değildir** (→ `T-601`),
  2. Kapsamdadır ama **ölçek testi** (küçük/orta alacaklı + orta/büyük borçlu)
     ya da **KOBİ Vasfı Belgesi değişimi** (`EV-2026-08-10-607`) yapılmadığı için
     tavan işlemiyordur,
  3. Migros'un ticari borçları büyük ölçüde **gıda dışı** ve **yurt dışı** kalemlerden
     oluşuyordur (bu ayrıştırma finansallarda **yoktur**).
- Ayrıca Kaynak B'nin **dipnot 69'u** bizzat şunu söyler: bildirilen süreler bazı
  firmalarda **sözleşmedeki standart sürelerdir** ve *"fiili süreler aslında
  sözleşmede yer alan sürelerden çok daha uzun olabilmektedir."*

### Bu ajanın YAPMADIĞI

Sessiz seçim yapılmamış, tek bir vade değeri **modele yazılmamıştır**.
`kanal.yaml → zincir_market.odeme_vadesi_gun = null / UNKNOWN`.
Bunun yerine **dört ayrı senaryo** tanımlanmıştır: 45 / **60** / 90 / **120** gün.

### Nasıl kapanır

`T-601` (şarap "tarım ve gıda ürünü" müdür?) + `T-604` (gerçek yıllık anlaşma
görüşmesi). İkisi de kapanmadan bu çelişki **çözülemez**.

---

## C-602 — Tekel bayii ve HoReCa marjı: kaynaklar hem çelişiyor hem tanımsız

```yaml
conflict_id:  C-602
acan_ajan:    kanal-marj-uzmani
tarih:        2026-08-10
durum:        OPEN
etki:         MEDIUM   # kanal 2 ve 3; charter oncelik sirasi 2 ve 3
```

### Tekel bayii

| İddia | Kaynak tipi | Sorun |
|---|---|---|
| "alkolde ~%17" | T5 içerik sitesi | margin mi markup mı **belirtilmemiş** |
| "rakı %8" | T5 içerik sitesi | ürün kategorisi farklı; taban belirtilmemiş |
| "brüt %10–15" | T5 forum | katman çifti belirtilmemiş |
| "ciro üzerinden %18–30" | T5 içerik sitesi | "ciro üzerinden" ifadesi **tanımsız** |

`evidence`: `EV-2026-08-10-620` (negatif kayıt)

### HoReCa

| İddia | Kaynak | Sorun |
|---|---|---|
| "perakende fiyatının **2 katı**" | Milliyet / Murat Bozok, 2012 | Çarpan **L8** üzerine |
| "toptan fiyatının **2,5 katı**" | **aynı yazı** | Çarpan **L7** üzerine |
| "market fiyatının **4–5 katı**" | **aynı yazı** | Yine **L8** üzerine, ve "gözlenen üst uç" |

`evidence`: `EV-2026-08-10-618`

### Neden bu bir "çelişki" olarak kaydedildi, "veri yok" olarak değil

Çünkü çelişki **kaynaklar arasında değil, kaynakların KENDİ İÇİNDEDİR.**
Tek bir yazı çarpanı **iki farklı katmandan** verir. Bu, sayının kendisinden
daha bilgilendirici bir bulgudur: **bu alanda konuşulan "marj" rakamları
tanımsız konuşulmaktadır** — ki `M1` kuralının varlık sebebi tam olarak budur.

### Bu ajanın YAPMADIĞI

Bu sayıların **hiçbiri** `kanal.yaml`'a `value` olarak yazılmamıştır.
`tekel_bayi.marj_pct` ve `horeca.fiyat_carpani` **UNKNOWN**'dır.
Duyarlılık bantları `ASSUMPTION` olarak ve **kanıtlı çapası olmadığı açıkça
yazılarak** ayrı blokta tutulmuştur.

### Nasıl kapanır

Yalnızca gerçek bayi/HoReCa görüşmesi veya gerçek bir fiyat listesi (`T-604`).
Masabaşı ile kapanmaz.
