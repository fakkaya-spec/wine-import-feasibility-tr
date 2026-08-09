# AÇIK SORULAR — turkiye-pazar-kasifi (TUR 1)

> Bu dosya ana `99-ops/acik-sorular.md`'ye başkan tarafından birleştirilecektir.

---

## OQ-001 — GÜNCEL DURUM

```yaml
id:              OQ-001
onceki_durum:    OPEN
YENI_DURUM:      PARTIALLY_RESOLVED
guncelleyen:     turkiye-pazar-kasifi
guncelleme_tar:  2026-08-09
```

### Kapanan kısımlar

| Alt soru | Cevap | Güven | evidence |
|---|---|---|---|
| KDV dahil mi, hariç mi? | **KDV DAHİL** | HIGH | `EV-2026-08-09-503`, `-504`, `-505`, `-506` |
| Tüketici satış fiyatı mı? | **EVET** (Metro TR bireysel müşteriye ücretsiz kartla açık) | HIGH | `EV-2026-08-09-505` |
| Profesyonel / cash & carry fiyatı mı? | **EVET, aynı anda** (Metro'da tek fiyat) | HIGH | `EV-505`, `EV-507`, `EV-508` |
| Metro etiketi nasıl okunur? | **KDV hariç/dahil ÇİFTLİ gösterim YOK.** İkinci sayı **birim fiyattır** (kg/L/adet). Büyük punto = güncel satış fiyatı + `KDV'li`. Promosyonda üstü çizili eski fiyat + "AVANTAJLI FİYAT" rozeti. | HIGH | `EV-503`, `EV-504` |

**OQ-001'in kurucu hipotezi kısmen ÇÜRÜMÜŞTÜR:** "Metro etiketinde KDV hariç
profesyonel fiyat ile KDV dahil fiyat birlikte gösterilebilir" varsayımı,
incelenen Metro Türkiye materyalinde **karşılığını bulmamıştır.**

### AÇIK KALAN kısımlar (bu yüzden `CLOSED` değil)

| # | Ne kapanmadı | Neden | Kritik mi |
|---|---|---|---|
| a | **Promosyon mu, normal fiyat mı?** | Tek gözlem var; etiketin promosyon rozeti/üstü çizili fiyat içerip içermediği bilinmiyor | **CRITICAL** — `T-504` |
| b | **Şarap reyonundaki fiziksel etiket** görüntülenmedi | Kanıt Metro'nun broşürlerinden; broşür ≠ raf etiketi | HIGH |
| c | **Zincir market tüketici fiyatı (gerçek L8)** | Alkol online satılamadığı için Migros/CarrefourSA'da fiyat yok | HIGH — `EV-511` |
| d | Metro'da üyelik tipine göre **özel fiyat** olup olmadığı | `guncelfiyatlar.metro-tr.com` "size özel fiyat" diyor ve giriş istiyor | MEDIUM |

### Model kuralı (güncellenmiş öneri — kararı başkan verir)

```yaml
BM_A (599,90 = KDV dahil):   BASE CASE      # kanitli
BM_B (599,90 = KDV haric):   SENSITIVITY    # kanitsiz, ama elenmedi
BM_C (599,90 = promosyonlu): YENI SENARYO   # OQ-001'in kapanmayan ayagi
BM_D (zincir L8 > Metro L8): YENI SENARYO   # katman ayrimi
```

**OQ-001 `CLOSED` yapılamaz.** Kapanması için `T-504` çözülmelidir.

---

## OQ-501 *(YENİ)* — Türkiye şarap ithalat hacmi ve pazar büyüklüğü

```yaml
id:              OQ-501
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            turkiye-pazar-kasifi
sorumlu_ajan:    mevzuat-ruhsat-uzmani (TADAB erisimi) -> yatirim-komitesi-baskani
oncelik:         2
impact:          HIGH
bloke_ettigi:    hacim senaryolarinin (5.000-100.000 sise) gercekcilik testi
ticket:          T-505
evidence:        EV-2026-08-09-515
```

**Soru:** Türkiye'ye yıllık kaç litre / kaç dolar şarap ithal ediliyor, menşe kırılımı
ve trend nedir?

**Neden kritik:** Pazar hacmi bilinmeden "100.000 şişe/yıl ölçeklenebilir mi" sorusu
cevaplanamaz. TADAB'ın *Resmî İstatistikler* sayfası **yalnızca yakıt biyoetanolü**
yayınlıyor; Ticaret Bakanlığı ve mevzuat.gov.tr bu turda HTTP 503 döndü.

---

## OQ-502 *(YENİ)* — Zincir market ve tekel bayii kanalında sıfır gözlem

```yaml
id:              OQ-502
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            turkiye-pazar-kasifi
sorumlu_ajan:    turkiye-pazar-kasifi (TUR 2/7'de fiziksel gozlem)
impact:          HIGH
bloke_ettigi:    segment bantlarinin kanal capraz dogrulamasi
evidence:        EV-2026-08-09-511, EV-2026-08-09-514
```

**Soru:** Migros / Macrocenter / CarrefourSA / tekel bayii raflarında fiyat/performans
segmentindeki şarap fiyatları nedir?

**Neden kritik:** Charter kanal önceliği `1) chain retail 2) independent/tekel`.
Bu turda ikisinde de **sıfır** gözlem alınabildi. Segment bantlarının %87'si
(45/52 gözlem) **tek bir online kanaldan** gelmektedir. Bu bir örnekleme yanlılığıdır.

**Nasıl kapanır:** Fiziksel mağaza turu (İstanbul'da 1 gün): Metro + Migros/Macrocenter
+ CarrefourSA + 2 tekel bayii, her birinde 600–1.200 TL bandındaki tüm şarap SKU'larının
etiket fotoğrafı.

---

## OQ-503 *(YENİ)* — Gold Country ve Central Creek'i kim ithal ediyor?

```yaml
id:              OQ-503
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            turkiye-pazar-kasifi
sorumlu_ajan:    turkiye-pazar-kasifi
impact:          MEDIUM
bloke_ettigi:    rakip maliyet yapisi anlayisi
```

**Soru:** Benchmark SKU'larının Türkiye ithalatçısı kim? Metro'nun kendi ithalatı
(private/exclusive import) mı, bağımsız bir ithalatçı mı?

**Neden önemli:** İncelenen online uzman perakende kanalında **ABD ve Avustralya
menşeli hiç şarap yok** (`EV-509`). Eğer Metro bu SKU'ları doğrudan ithal ediyorsa,
599,90 TL bir **ithalatçı marjı içermeyen** fiyattır ve bizim rekabet edeceğimiz
maliyet yapısı bir kademe daha alçaktır. Bu, projenin en kötü senaryosudur.

**Nasıl kapanır:** Şişenin arka etiketindeki "İthalatçı:" satırının fotoğrafı.
(Aynı mağaza ziyaretinde alınabilir — `T-504` ile birleştirilebilir.)
