# ÇELİŞKİLER — global-sourcing-kasifi — TUR 2

> `99-ops/celiskiler.md` dosyasına **DOKUNULMAMIŞTIR** (başkan birleştirir).
> **Hiçbiri sessizce çözülmemiştir.**
> TUR 1'de açılan `C-401`, `C-402`, `C-403` bu turda da **OPEN** kalmıştır.

---

## C-461 — "FOB" terimi iki farklı katmana işaret ediyor

```yaml
conflict_id:      C-461
opened_by:        global-sourcing-kasifi
opened_date:      2026-08-10
impact:           HIGH
status:           OPEN
model_girdisi_etkisi: VAR — L0/L1 ayrımı
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **İddia** | "FOB" = Incoterms® 2020 FOB, **adı belirtilen yükleme limanı bordası** → **L1** | "FOB" = şarap ticaretinde üreticinin ithalatçıya verdiği **ex-cellar** fiyat → fiilen **L0** |
| **Kaynak** | Incoterms® 2020 (genel kabul) + Harland sayfasının kendi açıklaması ("...until your container is loaded onto the ship") | WineWiki (Wine with Seth) — "FOB — Free on Board" maddesi, `EV-2026-08-10-468` |
| **Tier/tarih** | T4 / 2026-08-10 | T4 / 2026-08-10 |

**Neden çelişiyor:** Aynı üç harf, maliyet merdiveninin **iki farklı basamağını**
adlandırıyor ve aralarında iç nakliye + liman + ihracat gümrüklemesi farkı var.

**Somut tetikleyici:** `EV-2026-08-10-451` — Harland aynı fiyatı ("$2.85+") tam
konteyner siparişinde **FOB**, MOQ siparişinde **ex factory** olarak tanımlıyor.
Yani **tek yayınlanmış sayı, sipariş büyüklüğüne göre L0 veya L1 oluyor.**

**Bu ajanın uyguladığı geçici kural:** Incoterm metinde açıkça tanımlanmadan
hiçbir fiyat L0 veya L1 diye etiketlenmez; `supplier-shortlist-v2.csv`'de
`price_layer` kolonu ayrı tutulur ve belirsizse belirsizliği yazar.

**Nasıl kapanır:** RFQ 3.1 (EXW + **yer**) ve 3.2 (FOB + **adı belirtilen liman**)
cevaplarıyla, tedarikçi bazında. Genel olarak kapanmaz — **her teklif için ayrı ayrı** kapanır.

**Kime taşınıyor:** `gumruk-vergi-uzmani` (gümrük kıymeti matrahı), `finans-fizibilite` (katman disiplini).

---

## C-462 — Doğrulanmış private label MOQ aralığı, pilot hacmini hem kapsıyor hem aşıyor

```yaml
conflict_id:      C-462
opened_by:        global-sourcing-kasifi
opened_date:      2026-08-10
impact:           HIGH
status:           OPEN
iliskili:         C-401 (TUR 1, OPEN — kapatılmadı)
model_girdisi_etkisi: VAR — pilot senaryosunun uygulanabilirliği
```

| | Kaynak A | Kaynak B | Kaynak C |
|---|---|---|---|
| **İddia** | MOQ **3.000–3.600** şişe | MOQ **6.000** şişe | MOQ **300–1.200** şişe |
| **Kaynak** | Interbrosa (ES) `EV-2026-08-09-408`; The Wine Factory (FR) `EV-2026-08-09-410`; Clark Estate (NZ) `EV-2026-08-10-455` | Cantina Danese (IT) `EV-2026-08-10-453`; Harland (AU) `EV-2026-08-10-452` | usetorg.com agregatörü `EV-2026-08-09-424` |
| **Tier** | T4 (üretici beyanı) | T4 (üretici beyanı) | T5 (agregatör) |

**Neden çelişiyor:** Üst uç ile alt uç arasında **20 kat** fark var. Daha kritiği:
**charter'ın 5.000 şişelik pilot hacmi tam bu aralığın ortasına düşüyor.**
Yani MOQ, pilotu ne kesin olarak mümkün ne kesin olarak imkânsız kılıyor —
**tedarikçiye göre değişiyor.**

**TUR 1'in ifadesinin nitelenmesi (`EV-2026-08-10-471`):**
TUR 1 raporu B-1'de *"3.000–3.600 şişe … charter'ın 5.000 şişelik pilot hacmiyle
UYUMLUDUR"* diyordu. Bu **hâlâ doğru ama artık eksiktir**: MOQ'su bilinen beş
üreticinin **üçüyle** pilot mümkün, **ikisiyle değil.**

**Bu bir CONFLICT'tir, ortalama alınamaz.** 3.000 ile 6.000'in ortalamasını
almak (4.500) hiçbir üreticinin gerçek MOQ'su değildir ve modele giremez.

**Nasıl kapanır:** RFQ 3.6a/3.6b + 4.2/4.3 ile, **tedarikçi bazında**.
Genel bir "sektör MOQ'su" yoktur — bu turun bulgusu tam olarak budur:
**MOQ ülke veya sektör özelliği değil, firma özelliğidir.**

**Kime taşınıyor:** `finans-fizibilite` (5.000 vs 10.000 şişe senaryolarının
tedarikçi havuzu farkı), `seytanin-avukati` (pilot mantığının kırılganlığı).

---

## TUR 1'DEN DEVREDEN VE HÂLÂ AÇIK OLANLAR

| conflict_id | Konu | TUR 2'de ne oldu |
|---|---|---|
| **C-401** | T5 agregatör MOQ 300–1.200 vs doğrulanmış üretici beyanları | **AÇIK.** TUR 2'de doğrulanmış üst sınır 3.600'den 6.000'e çıktı → makas **genişledi**. C-462 bu genişlemeyi kaydeder, C-401'i kapatmaz |
| **C-402** | Benchmark California menşeli ama ABD→TR ithalatı 18.298 l / ort. CIF 25,19 USD/l | **AÇIK.** TUR 2'de iki ABD private label sağlayıcısı daha bulundu (O'Neill, Bronco adayı) ama **hiçbiri Türkiye'ye ihracat kabiliyeti beyan etmedi** — çelişki derinleşti, çözülmedi |
| **C-403** | Benchmark ürünün California alt bölgesi: Sierra Foothills mı Central Valley mi | **AÇIK.** `EV-2026-08-10-463` (O'Neill ana tesisi Parlier/Central Valley) "Central Valley" ayağını **dolaylı** destekler ama iki T5 kaynağı arasındaki çelişkiyi **çözmez** |
