# ÇAPRAZ İPUÇLARI — gumruk-vergi-uzmani (TUR 1, 2026-08-09)

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında gördüğüm ama
> ilgili ajanı ilgilendiren bulgular. Hedef ajan doğrulamadan modele girmez.

---

## → `global-sourcing-kasifi`

### Cİ-1 — Menşe seçimi gümrük vergisinde 70 puanlık bir kaldıraç barındırıyor
2204.21 (750 ml köpüksüz şarap) gümrük vergisi oranları (EV-2026-08-09-103…106):

| Menşe | Gümrük vergisi |
|-------|----------------|
| **Bosna-Hersek** | **%0** |
| **Kosova** | **%0** |
| Güney Kore, Singapur | %0 |
| Kuzey Makedonya | %35 |
| Venezuela | %35 |
| BAE | %49 |
| AB (İspanya/İtalya/Fransa/Portekiz), Birleşik Krallık, **Şili** | %50 |
| Gürcistan, Malezya, TPS-OIC, D-8 | %70 |
| **ABD, Güney Afrika, Avustralya, Arjantin** (DÜ) | **%70** |

**Neden önemli:** Kapsam listesindeki 9 ülkenin hiçbiri %0 grubunda değil.
Buna karşılık **Bosna-Hersek, Kosova ve Kuzey Makedonya** üzüm/şarap üreten
ülkeler ve Türkiye'ye coğrafi olarak yakın. Bunlar sourcing kapsamında hiç
yoktu. Fiyat/performans segmentinde %70 → %0 gümrük vergisi farkı, navlun
avantajıyla birlikte, kapsam genişletmeyi haklı çıkarabilir.

**Not:** Şili'nin STA'sı şarapta sıfır getirmiyor, sadece %70 → %50 indiriyor
(dipnot 2). Şili'yi "STA var, vergi düşük" varsayımıyla öne almayın.

### Cİ-2 — İsviçre/Lihtenştayn kontenjanı var ama pratik değeri düşük
2204.21 için yılda **30.000 litre** (≈40.000 şişe) tarife kontenjanı,
kontenjan içi vergi %35 (EV-2026-08-09-109). Tüm ithalatçılar için toplam
miktardır ve İsviçre şarabı fiyat/performans segmentinde değildir.
Yine de "kontenjan var mı" sorusunun cevabı olarak kayda geçirildi.

### Cİ-3 — Köpüklü şarap ürün genişletmesi vergiden ölür
2204.10 köpüklü şarapta ÖTV **481,5146 TL/litre** = 750 ml'de **361,14 TL/şişe**
(EV-2026-08-09-110). Köpüksüzde bu 53,45 TL. Portföye köpüklü SKU eklenmesi
düşünülüyorsa bu tek başına eleyici olabilir.

---

## → `navlun-lojistik-uzmani`

### Cİ-4 — Navlun ve sigorta gümrük kıymetine giriyor, yani vergilendiriliyor
Gümrük Kanunu md.27/1-e: Türkiye'deki giriş liman/yerine kadar navlun + sigorta
+ yükleme/elleçleme gümrük kıymetine **dahildir** (EV-2026-08-09-120).
Sonuç: navlunun her 1 TL'si DÜ menşede **~1 TL × (1+0,70) × 1,20 = 2,04 TL**
landed maliyet yaratıyor (gümrük vergisi + KDV kaskadı). Yani **navlun optimizasyonunun
vergi çarpanı vardır.** LCL/FCL kararında bu çarpan hesaba katılmalı.

### Cİ-5 — Giriş yerinden sonraki nakliye/sigorta kıymete girmiyor, ama ayırt edilebilir olmalı
GK md.28/a: giriş yerine varıştan sonraki nakliye ve sigorta hariç — **fiyattan
ayırt edilebilmesi koşuluyla** (EV-2026-08-09-121). Faturada tek kalem
"door-to-door" fiyat verilirse tamamı gümrük kıymetine girer ve vergilenir.
Forwarder'dan **liman-sonrası masrafların ayrı fatura/ayrı satır** olarak
alınması ciddi bir tasarruf kalemidir.

### Cİ-6 — Antrepoda bekletmenin gizli vergi riski
Vergi, serbest dolaşıma giriş beyannamesinin tescil tarihinde doğar
(EV-2026-08-09-122) ve ÖTV maktu tutarı **Ocak ve Temmuz'da otomatik artar**
(EV-2026-08-09-114, son artış +%16,09). Antrepoda 1 Temmuz'u geçirmek şişe başı
ÖTV'yi ~%16 artırabilir. Antrepo nakit akışı avantajı hesaplanırken bu risk
karşı kaleme yazılmalı.

---

## → `mevzuat-ruhsat-uzmani`

### Cİ-7 — Ürün Güvenliği ve Denetimi tebliği radarda
Mevzuat aramasında "**TÜTÜN, TÜTÜN MAMULLERİ, ALKOL VE ALKOLLÜ İÇKİLERİN
İTHALAT DENETİMİ TEBLİĞİ (ÜRÜN GÜVENLİĞİ VE DENETİMİ: 2026/…)**", RG 31.12.2025,
22.04'ü kapsayacak şekilde çıktı. İthalatta gümrük öncesi uygunluk denetimi
anlamına geliyor olabilir — takvim ve maliyet etkisi sizin alanınızda.

### Cİ-8 — ÖTV bandrol usulü kanunda açıkça yetkilendirilmiş
ÖTV Kanunu md.14/5: Maliye Bakanlığı "(III) sayılı listedeki mallara ait
verginin **bandrol usulü ile tahsiline**" ilişkin usulleri belirlemeye yetkilidir.
Bandrol/ÜİS maliyeti ve süreci sizin alanınız; ancak bunun bir **vergi tahsil
yöntemi** olduğunu ve dolayısıyla ÖTV ödeme anını etkileyebileceğini not düşüyorum.

### Cİ-9 — TAPDK/Tarım tebliğlerinde 2204.21 açıkça geçiyor
"ALKOL VE ALKOLLÜ İÇKİLERİN İÇ VE DIŞ TİCARETİNE İLİŞKİN USUL VE ESASLAR
HAKKINDA YÖNETMELİĞİN 14 ÜNCÜ … MADDESİ" tebliğlerinin her yılki versiyonunda
2204.21 GTİP'i geçiyor (2018–2025 serisi, her yıl aralık sonunda yenileniyor).
Bu yıllık yenilenen tebliğ serisi sizin takviminize girmeli.

---

## → `turkiye-pazar-kasifi`

### Cİ-10 — Benchmark ürün en yüksek gümrük vergisi grubunda
Benchmark (Gold Country California Colombard-Chardonnay, **ABD menşeli**)
DÜ sütunundadır → gümrük vergisi **%70** (EV-2026-08-09-104). Yani 599,90 TL'lik
rafın arkasında ithalatçı en pahalı gümrük rejimini ödüyor. Bu, raf fiyatının
gerçekten agresif bir fiyat mı yoksa bir hata mı olduğunu değerlendirirken
önemli bir sinyal — rakip analizinde menşe kırılımı toplanmalı.

---

## → `kanal-marj-uzmani`

### Cİ-11 — Vergi tabanı fiyat-esnek değil
ÖTV şişe başına sabit **53,4519 TL**'dir ve CIF'ten bağımsızdır
(EV-2026-08-09-111). Yani **indirim/kampanya yapıldığında ödenen ÖTV düşmez.**
Kampanya maliyeti tamamen marjdan karşılanır. Kanal kampanya ekonomisi
modellenirken bu, sabit maliyet gibi davranır.

---

## Genel not
Bu ipuçlarının hiçbiri benim alanımda **sonuç** değildir. Yalnızca vergi
verisinden düşen sinyallerdir. İlgili ajan kendi T1/T2 kanıtını kurmadan
modele girmemelidir.
