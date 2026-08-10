# TEDARİKÇİ ÖNCELİKLENDİRME — A / B / C

```yaml
sahibi:            global-sourcing-kasifi
tur:               TUR 2 — COMMERCIAL VALIDATION
tarih:             2026-08-10
girdi:             50-sourcing/supplier-shortlist-v2.csv (26 tedarikçi)
teklif_alindi_mi:  false
uretici_ile_iletisim: NONE — bu turda hiçbir üreticiye e-posta/form/mesaj gönderilmedi
```

> **UYARI:** Bu bir **tedarikçi seçimi değildir.** `A` etiketi "bu tedarikçi
> seçildi" demek değildir; **"gerçek RFQ göndermeye değer"** demektir.
> Hiçbir tedarikçiden fiyat alınmamıştır. Öncelik sırası **kanıt olgunluğuna**
> göredir, **ticari cazibeye** göre değildir — çünkü ticari cazibeyi ölçecek
> veri (fiyat) henüz yoktur.

---

## 1. KRİTERLER — ÖNCE TANIMLANDI, SONRA UYGULANDI

Beş boyut. Her boyut bağımsız olarak `POZİTİF` / `UNKNOWN` / `NEGATİF` alır.
Boyutların **ağırlığı yoktur** — çünkü ağırlık vermek, elimde olmayan fiyat
verisini örtük olarak varsaymak olurdu.

| # | Boyut | POZİTİF sayılma koşulu | NEGATİF sayılma koşulu |
|---|---|---|---|
| **K1** | **Ulaşılabilirlik** | Kurumsal kanal (site / fuar profili / dizin) okunabildi **ve** en az bir açık iletişim kanalı (e-posta, telefon veya form) var | Kurumsal kanal okunamadı **ve** iletişim kanalı bulunamadı |
| **K2** | **İş modeli beyanı** | Üretici **kendi kanalında** Model A veya Model B kabiliyetini açıkça beyan ediyor | Ne A ne B kabiliyeti hiçbir kanalda beyan edilmiyor |
| **K3** | **Ölçek uyumu** | MOQ **sayı olarak biliniyor** ve pilot bandıyla (5.000–10.000 şişe) uyumlu | MOQ konteyner bazlı veya bilinen değeri pilot bandının üstünde |
| **K4** | **Hat uyumu** | Menşe ülkenin Türkiye'ye 2025 şişelenmiş şarap ihracatı **> 300.000 litre** (`EV-2026-08-09-405`) | Aynı ihracat **< 100.000 litre** |
| **K5** | **Ürün uyumu** | 750 ml still beyaz + entry/value kademe **doğrulanmış** (çeşit veya kademe adıyla) | Üretici kendini açıkça premium konumlandırıyor veya bitmiş şişelenmiş ürün ana işi değil |

### Eşikler

| Öncelik | Koşul |
|---|---|
| **A — RFQ gönderilmeye değer** | K1 **ve** K2 `POZİTİF` **ve** K3/K4/K5'ten **en az ikisi** `POZİTİF` |
| **B — ikinci dalga RFQ** | K1 **ve** K2 `POZİTİF`, ancak K3/K4/K5'ten en fazla biri `POZİTİF` |
| **C — RFQ öncesi ek doğrulama gerekir** | K1 **veya** K2 `POZİTİF` değil, **veya** yapısal diskalifiye edici var (aracı/negociant katmanı, ülke charter kapsamı dışında, kurumsal kanal doğrulanamadı) |

> **`A` içinde de `NEGATİF` boyut olabilir.** Kriter "hiç negatif olmasın" demiyor;
> "en az iki pozitif olsun" diyor. Her `A` tedarikçinin negatif boyutu aşağıda
> **açıkça yazılmıştır** — gizlenmemiştir.

---

## 2. A ÖNCELİK — 7 TEDARİKÇİ

| # | Tedarikçi | Ülke | Model | K1 | K2 | K3 | K4 | K5 | Gerekçe (tek cümle) | Açık NEGATİF |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Harland Wine Company** | AU | B | ✅ | ✅ | ✅ | ❌ | ✅ | Havuzdaki **tek yayınlanmış şişe başı fiyat kademesi** + bilinen MOQ + bilinen ödeme şartı + bilinen konteyner doluluğu — tek bir RFQ ile en çok bilinmeyeni kapatır | Avustralya→Türkiye hattı fiilen yok (44.674 l/2025); **para birimi bilinmiyor** |
| 2 | **Cantina Danese** | IT | B | ✅ | ✅ | ✅ | ✅ | ⬜ | SKU bazlı MOQ (6.000) **ve** Türkiye'nin en güçlü ithalat hattı (İtalya, 5,75 m litre/2025) aynı tedarikçide buluşuyor | Beyaz portföy ve fiyat tamamen UNKNOWN |
| 3 | **Interbrosa Family Wines** | ES | B | ⬜ | ✅ | ✅ | ✅ | ⬜ | Doğrulanmış **en düşük MOQ** (3.000 şişe) + İspanya hattı (1,92 m litre/2025) + tasarım desteği beyanı | Site 2026-08-10'da **HTTP 503** — yalnızca e-posta/telefonla ulaşılabilir (`EV-2026-08-10-467`) |
| 4 | **The Wine Factory** | FR | B | ✅ | ✅ | ✅ | ✅ | ⬜ | MOQ (3.600) **ve** üretim süresi (28–42 gün) birlikte bilinen **tek** tedarikçi; Fransa hattı çalışıyor (2,85 m litre) | Fransa'nın L2 CIF birim değeri 6,27 USD/l — **segment üstü**; bu üreticinin altında olduğu doğrulanmadı |
| 5 | **Corta Hojas Export Wine** | CL | B | ✅ | ✅ | ⬜ | ✅ | ✅ | Beyaz çeşitleri (**Sauvignon Blanc, Chardonnay**) ürün tanımıyla birebir eşleşiyor + Şili hattı çalışıyor (946.350 l) + %100 ihracat odaklı | MOQ, fiyat, Incoterm, lead time — 2026-08-10 itibarıyla **hiçbiri yayınlanmamış** |
| 6 | **Bodegas San Valero** | ES | **A + B** | ✅ | ✅ | ⬜ | ✅ | ⬜ | Havuzdaki **tek doğrulanmış ikili aday**: tek bir RFQ, iki iş modelinin fiyat farkını **aynı maliyet tabanı üzerinde** ölçebilir | Private label beyanı **firmanın kendi kanalında değil**, üçüncü taraf yayında |
| 7 | **Casa Santos Lima** | PT | A | ✅ | ✅ | ⬜ | ✅ | ⬜ | Model A'nın **en olgun** adayı: ~50 ülke, üretimin ~%90'ı ihracat, Portekiz hattı çalışıyor (324.828 l) | Türkiye'de temsilcisi olup olmadığı UNKNOWN (**T-464**); private label kabiliyeti UNKNOWN |

**A grubunun model dağılımı: 5 × Model B · 1 × Model A · 1 × ikisi birden.**

> **Bu dağılım bir tercih değil, bir kanıt asimetrisidir** ve TUR 1'de itiraf edilen
> arama yanlılığının TUR 2'de **tam olarak kapatılamadığını** gösterir. Model A
> tarafında 7 aday bulundu (bkz. §3), ancak hiçbiri MOQ veya ölçek verisi
> yayınlamadığı için K3 boyutunda `UNKNOWN` kaldı ve `A`'ya çıkamadı.
> **Model A adaylarının `B`'de yoğunlaşması, modelin zayıf olduğunu değil,
> mevcut marka sahiplerinin ticari şartlarını web'de yayınlamadığını gösterir.**

---

## 3. B ÖNCELİK — 10 TEDARİKÇİ (ikinci dalga RFQ)

| # | Tedarikçi | Ülke | Model | Gerekçe | Neden A değil |
|---|---|---|---|---|---|
| 8 | **Viña Maria** | ES | B | Yıllık 15 m şişe kapasite; fiyat listesi talep edilebilir olarak ilan edilmiş | MOQ **konteyner bazlı** (1 × 20 ft karışık) → K3 `NEGATİF`; 5.000'lik pilotla uyumsuz olabilir |
| 9 | **Vinicola Vedovato Mario** | IT | B | **EXW/FOB/CIF/DAP dördünü de** görüşülebilir olarak listeleyen tek tedarikçi — RFQ 3.16'nın en iyi test adayı | MOQ, fiyat, ürün, kapasite tamamen UNKNOWN → yalnızca K4 pozitif |
| 10 | **Antawara Vineyards** | CL | B | Kendini **ithalatçı private label'ına tam odaklı** tanımlıyor; "Entry" kademesi segmentimize denk gelebilir | MOQ "convenient" denip **sayı verilmemiş**; ürün kademesi doğrulanmamış |
| 11 | **Origin Wine** | ZA | B | 100+ m litre/yıl; **çok menşeli** (ZA+AR+CH) → tek hasat riskini azaltır | ZA→TR hattı fiilen yok (18.026 l/2025) → K4 `NEGATİF`; MOQ UNKNOWN |
| 12 | **Zidela Worldwide Wines** | ZA | B | Kendini açıkça **"value for money private label"** diye konumlandıran tek tedarikçi — segment tanımıyla en doğrudan örtüşme | Kurumsal sitesi okunamadı (yaş duvarı); kanıt **üçüncü taraf dizininden**; ZA hattı yok |
| 13 | **Vidigal Wines** | PT | A | %90 ihracat oranı → **distribütör arayan profil**; Porta 6 uluslararası perakendede listelenmiş bir entry/orta marka | Beyaz portföy UNKNOWN; kurumsal site yaş duvarı arkasında; TR'de ithalatçısı UNKNOWN |
| 14 | **Parras Wines** | PT | A (+B?) | Grup içinde **kendi şişeleme tesisi** (Goanvi) → aynı firma iki modele de cevap verebilir | Private label **açıkça ilan edilmemiş** — bu bir çıkarımdır, kanıt değildir; ciro verisi 2020 |
| 15 | **Félix Solís Avantis** | ES | A | Viña Albali / Los Molinos **gıda perakendesi için tasarlanmış f/p markalar** — charter'ın 1. kanal önceliğiyle birebir | 115 ülkede bulunan bir markanın Türkiye'de boş olma ihtimali **düşük** → adaylığı zayıflatan gözlem |
| 16 | **Plaimont** | FR | A | **Ürün eşleşmesi havuzun en güçlüsü**: Côtes de Gascogne, Colombard-Chardonnay tarzının yapısal kaynağı (Colombelle) | Fransa L2 CIF 6,27 USD/l — segment üstü; Gascogne'un bunun altında olduğu **doğrulanmadı** |
| 17 | **Purcari Wineries Group** | MD (+RO/BG) | A | Moldova Türkiye'ye **en düşük L2 CIF** menşei (2,46 USD/l) ve hat çalışıyor; halka açık şirket = havuzun **en şeffaf** tedarikçisi | Grup kendini **"most premium"** diye konumlandırıyor → segmentimizle **ters sinyal** |

---

## 4. C ÖNCELİK — 9 TEDARİKÇİ (RFQ öncesi ek doğrulama gerekir)

| # | Tedarikçi | Ülke | Diskalifiye edici / eksik | Ne yapılırsa yukarı çıkar |
|---|---|---|---|---|
| 18 | **FMS Wine Marketing** | ZA | Üretici değil, **pazarlama/aracılık** firması → ek marj katmanı | Hangi üreticinin adına çalıştığı ve marjın nerede olduğu netleşirse |
| 19 | **Kingston Estate Wines** | AU | İş modeli **dökme ağırlıklı**; şişelenmiş bitmiş ürün kabiliyeti belirsiz | Şişelenmiş ürün için ayrı MOQ ve fiyat teyidi |
| 20 | **Scheid Family Wines** | US | ABD→TR hattı fiilen yok (18.298 l/2025); Monterey — Central Valley değil | ABD hattının açılabilirliği (`gumruk-vergi-uzmani` + `navlun-lojistik-uzmani`) |
| 21 | **Spanish Origin** | ES | **Üretici mi aracı mı UNKNOWN** ("exporter" diyor, "bodega" demiyor); site landing page seviyesinde | Kendi tesisi olduğu doğrulanırsa doğrudan B'ye çıkar (İspanya hattı güçlü) |
| 22 | **Clark Estate** | NZ | **Ülke charter kapsamında değil**; Marlborough SB yapısal olarak premium | Çıkmamalı — bu kayıt bir **MOQ referansıdır**, tedarikçi adayı değil |
| 23 | **O'Neill Vintners & Distillers** | US | İhracat kabiliyeti sitede doğrulanmadı; ABD→TR hattı yok | İhracat departmanı ve Türkiye'ye sevkiyat kabiliyeti doğrulanırsa |
| 24 | **Viña Luis Felipe Edwards** | CL | Kurumsal site **HTTP 404**; kanıt üçüncü taraf dizinlerinden; "premium" konumlandırma | Güncel kurumsal site ve entry markalar bulunursa → B (Şili hattı çalışıyor) |
| 25 | **Bronco Wine Company** | US | Private label kabiliyeti **kurumsal sitede kanıtlanamadı** (`EV-2026-08-10-466`) | broncowine-trade.com'da bir private label programı doğrulanırsa |
| 26 | **Geo Vino Wines** | US/çok menşeli | **Negociant**, üretici değil; iş modeli ABD iç pazarı (50 eyalet) | İhracat kabiliyeti ve menşe bazlı fiyat farkı beyanı gelirse |

---

## 5. DAĞILIM ÖZETİ

| Öncelik | Adet | Model B | Model A | İkisi | UNKNOWN |
|---|---|---|---|---|---|
| **A** | 7 | 5 | 1 | 1 | 0 |
| **B** | 10 | 5 | 5 | 0 | 0 |
| **C** | 9 | 7 | 1 | 0 | 1 |
| **Toplam** | **26** | **17** | **7** | **1** | **1** |

| Ülke | Adet | A | B | C |
|---|---|---|---|---|
| İspanya | 5 | 2 | 2 | 1 |
| ABD (California / çok menşeli) | 4 | 0 | 0 | 4 |
| Portekiz | 3 | 1 | 2 | 0 |
| Şili | 3 | 1 | 1 | 1 |
| Güney Afrika | 3 | 0 | 2 | 1 |
| İtalya | 2 | 1 | 1 | 0 |
| Fransa | 2 | 1 | 1 | 0 |
| Avustralya | 2 | 1 | 0 | 1 |
| Moldova | 1 | 0 | 1 | 0 |
| Yeni Zelanda | 1 | 0 | 0 | 1 |
| **Arjantin** | **0** | — | — | — |

**Arjantin bu turda da 0 tedarikçiyle kapandı** (`EV-2026-08-10-469`). Bu bir
eleme değil, bir **doğrulama başarısızlığıdır** ve öyle kaydedilmiştir.

---

## 6. DÜŞÜK MOQ ALTERNATİFLERİ — 5 ADET (doğrulanmış sayı ile)

| Tedarikçi | Ülke | MOQ | Yapı | Pilot (5.000 şişe) ile uyum |
|---|---|---|---|---|
| Interbrosa | ES | **3.000** | SKU bazlı | ✅ uyumlu |
| Clark Estate | NZ | **3.000** | çeşit + hasat yılı bazlı | ✅ uyumlu *(ülke kapsam dışı)* |
| The Wine Factory | FR | **3.600** | SKU bazlı | ✅ uyumlu |
| Cantina Danese | IT | **6.000** | referans (SKU) bazlı | ❌ pilot **üstünde** |
| Harland Wine Company | AU | **6.000** | şarap bazlı | ❌ pilot **üstünde** |

> **TUR 1'in "private label pilot ölçekte uygulanabilir" sonucu nitelenmiştir**
> (`EV-2026-08-10-471`, `C-462`): 5.000 şişelik pilot, MOQ'su bilinen **beş
> üreticinin üçüyle mümkün, ikisiyle değildir.** MOQ bir ülke veya sektör
> özelliği değil, **firma özelliğidir.**

---

## 7. BU SIRALAMAYI NE ÇÜRÜTÜR?

**Tek bir gerçek teklif.** Bu sıralamanın tamamı **kanıt olgunluğuna** göre
kurulmuştur çünkü **ticari cazibeyi ölçecek veri (fiyat) yoktur.** İlk beş
gerçek teklif geldiğinde sıralama büyük olasılıkla **tamamen yeniden kurulur** —
ve bu bir hata değil, bu turun tasarımının kabul edilmiş sonucudur.

Somut kırılma senaryoları:

1. **`A`'daki bir tedarikçi, fiyatı segment üstü olduğu için elenirse** —
   özellikle The Wine Factory (Fransa) ve Harland (para birimi USD çıkarsa)
   bu riski taşır. O durumda `A` grubu 7'den 5'e iner.
2. **Harland'ın para birimi USD çıkarsa**, havuzdaki tek yayınlanmış fiyat
   ~1,5 kat pahalılaşır ve **duyarlılık analizinin üst sınırı kayar.**
3. **`B`'deki Model A adaylarının Türkiye'de zaten ithalatçısı olduğu ortaya
   çıkarsa** (T-464), Model A tarafı 7 adaydan 1–2'ye düşer ve iki modelin
   "eşit öncelikli" değerlendirilmesi **fiilen imkânsız** hale gelir.
4. **MOQ'ların gerçekte 3× çıkması** (`C-462`): 3.000 → 9.000 ve 6.000 → 18.000
   olursa, düşük MOQ alternatifi sayısı **5'ten 0'a** iner ve pilot mantığı
   private label tarafında tamamen çöker.
