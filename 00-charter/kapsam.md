# KAPSAM

## AMAÇ

Türkiye'ye **fiyat/performans segmentinde** şarap ithalatının gerçek ticari
fizibilitesini araştırmak ve bunu bir yatırım kararına dönüştürmek.

Cevaplanacak asıl soru:

> Metro rafında 599,90 TL'ye satılan bir ithal şarabın karşısına çıkabilecek
> bir ürünü ithal edip kâr edebilir miyiz? Üreticiye en fazla kaç dolar/euro
> ödeyebiliriz?

---

## KAPSAM İÇİ

### Ürün
- Şişelenmiş, bitmiş ürün (bottled finished product)
- 750 ml ana format
- Fiyat/performans segmenti (benchmark bandı çevresi)
- Beyaz şarap öncelikli (benchmark beyaz), ama segment analizi kırmızı ve
  roze SKU'ları da kapsar

### İş modelleri (eşit öncelikli)
- **A)** Mevcut marka distribütörlüğü
- **B)** Private label

### Coğrafya — tedarik
California, İspanya, İtalya, Fransa, Şili, Güney Afrika, Portekiz, Avustralya,
Arjantin + ekonomik olarak anlamlı diğer ülkeler.

### Coğrafya — satış
Türkiye.

### Kanallar (öncelik sırasıyla)
1. Chain retail (zincir market)
2. Independent retail / tekel bayi
3. HoReCa

### Hacim aralığı
5.000 · 10.000 · 25.000 · 50.000 · 100.000 şişe/yıl

### Analiz konuları
- GTİP, gümrük vergisi, tercihli tarife, ÖTV, KDV, KKDF, gümrük kıymeti,
  gözetim, antrepo rejimi
- TADAB ruhsatları, ürün uygunluğu, etiket, analiz, bandrol/ÜİS, teminat,
  satış/dağıtım/reklam kısıtları
- Konteyner, navlun, sigorta, liman, demurrage, antrepo, iç lojistik,
  depolama, sıcaklık riski, transit süre
- Tedarikçi keşfi, MOQ, Incoterm, ödeme vadesi, private label kapasitesi
- Türkiye raf fiyatları, rakipler, segmentler, ithalat hacmi, mevcut oyuncular
- Kanal marjları, listeleme, ciro primi, iade, vade, kampanya maliyetleri
- Tam finansal model: L0→L8, break-even, işletme sermayesi, CCC,
  peak cash requirement, duyarlılıklar

---

## KAPSAM DIŞI (BU PROJEDE ARAŞTIRILMAZ)

| Konu | Neden |
|------|-------|
| Türkiye'de **üretim / bağcılık** yatırımı | Bu bir ithalat fizibilitesidir |
| **Bulk şarap ithalatı + Türkiye'de şişeleme** | Yalnızca bir **araştırma hipotezi** olarak not edilir; bu turda çözülmez. Sourcing kâşifi hipotezi kaydeder, ilgili ajanlara `99-ops/capraz-ipuclari.md` üzerinden ipucu bırakır. |
| Diğer alkollü içkiler (bira, rakı, viski vb.) | Segment dışı. Yalnızca kanal/mevzuat karşılaştırması için referans alınabilir. |
| **İhracat** (Türkiye'den dışarı) | Ters yön |
| Türkiye dışına satış / re-export | Kapsam dışı |
| Duty free kanalı | Ayrı vergi rejimi, ayrı proje |
| Online D2C satış modeli | Alkolde regülasyon kısıtları nedeniyle ayrı inceleme gerektirir; `mevzuat-ruhsat-uzmani` yalnızca **kısıtın varlığını** not eder |
| Şirket kuruluşu / vergi yapılandırması / ortaklık yapısı | Finansal-hukuki danışmanlık alanı |
| Marka tescili detaylı süreci | Private label seçilirse ayrıca ele alınır |
| Personel / organizasyon tasarımı | Yalnızca maliyet kalemi olarak modele girer |

---

## KARAR KAPSAMI

Bu proje şu kararlardan **birini** üretir:

`KILL` · `HOLD` · `TEST` · `IMPORT PILOT` · `SCALE`

Kararı yalnızca `yatirim-komitesi-baskani` verir.

**"Yeterli veri yok" geçerli bir çıktıdır.** Kritik UNKNOWN nihai kararı
bloke edebilir ve bu bir başarısızlık değil, tasarımın parçasıdır.

---

## ZAMAN KAPSAMI

- Benchmark gözlem tarihi: **09.08.2026**
- Model hedef tarihi: TBD (ilk konteynerin gümrükten çıkacağı tahmini tarih;
  `mevzuat-ruhsat-uzmani`'nın T0 takviminden türetilir)
- Vergi/mevzuat verileri **model hedef tarihinde geçerli olacak** hâliyle
  kullanılmalıdır. Bugünkü oran ile ithalat anındaki oran farklı olabilir —
  bu bir risk kalemidir ve `seytanin-avukati`'nın regülasyon şoku
  vektöründe ele alınır.

---

## DİL VE PARA BİRİMİ

- Repo dili: Türkçe. Teknik terimler orijinal (EXW, FOB, CIF, contribution
  margin vb.) — çevrilmez.
- Para birimi: her sayı **kendi orijinal para biriminde** kaydedilir
  (USD/EUR/TRY). Dönüşüm yalnızca modelde, `makro.yaml`'daki kanıtlı kurla
  ve kur tarihi belirtilerek yapılır.
- **Kur dönüşümü yapılmış bir sayı, orijinal sayının yerine geçmez.**
