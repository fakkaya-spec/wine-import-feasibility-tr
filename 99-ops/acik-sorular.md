# AÇIK SORULAR

Format: `OQ-###` · Durum: `OPEN` | `ANSWERED` | `CLOSED` | `BLOCKED`

---

## OPEN QUESTION #001 — Metro benchmark fiyatının KDV ve kanal statüsü

```yaml
id:              OQ-001
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            TUR 0 kurulum
sorumlu_ajan:    turkiye-pazar-kasifi
oncelik:         1 (EN YUKSEK)
impact:          CRITICAL
bloke_ettigi:    G3 (Pazar gate'i), ters modelin hedef fiyati
```

### Soru

Metro Türkiye'de **09.08.2026** tarihinde görülen
**Gold Country California Colombard-Chardonnay 2023, 750 ml — 599,90 TL**
etiket fiyatı:

1. **KDV dahil mi, KDV hariç mi?**
2. **Tüketici satış fiyatı mı, profesyonel/cash & carry fiyatı mı?**
3. Hangi fiyat katmanına karşılık geliyor — **L7** (perakendeci alış) mi,
   **L8** (tüketici raf) mi?
4. Promosyonlu bir fiyat mıydı, normal fiyat mıydı?

Aynı sorular komşu benchmark için de geçerlidir:
**Central Creek (Avustralya) — 649,90 TL**

### Neden kritik

Metro bir **cash & carry** formatıdır. Bu formatta etikette KDV hariç
profesyonel fiyat ile KDV dahil fiyat birlikte gösterilebilir.

Bu doğrulanmazsa:
- Ters model (`target shelf price → max EXW/FOB`) **yanlış hedefle** çalışır.
- KDV oranı kadar bir sapma tüm fiyat merdivenini kaydırır.
- Sapma doğrudan **üreticiye ödeyebileceğimiz maksimum fiyata** yansır —
  yani projenin asıl çıktısını bozar.
- 599,90 TL bir L8 değil L7'ye yakın bir sayıysa, tüketici raf fiyatı
  belirgin biçimde daha yüksektir ve segment tanımı değişir.

### Kapanana kadar geçerli kural

`finans-fizibilite` bu benchmark'ı **tek bir sayı olarak kullanamaz.**
Model iki senaryoyu **ayrı ayrı** çalıştırır ve farkı raporlar:
- **BM_A:** 599,90 TL = KDV **dahil**
- **BM_B:** 599,90 TL = KDV **hariç**

(bkz. `80-model/inputs/senaryolar.yaml` → `benchmark_senaryolari`)

### Nasıl kapatılır

| # | Yöntem | Not |
|---|--------|-----|
| 1 | Mağazada etiketin tam fotoğrafı (küçük punto KDV satırı dahil) | En güçlü kanıt |
| 2 | Metro kasa fişi | Fiilen ödenen tutarı gösterir |
| 3 | Metro Türkiye online/kurumsal fiyat gösterim politikası | T2/T4 |
| 4 | Aynı SKU'nun zincir markette (Migros/CarrefourSA) tüketici fiyatı | Karşılaştırma sağlar |

### Kapanış kaydı

```yaml
cevap:              null
evidence_id:        null
kapanis_tarihi:     null
kapatan_ajan:       null
```

---

## OPEN QUESTION #002 — Model hedef tarihi

```yaml
id:              OQ-002
durum:           OPEN
acilis_tarihi:   2026-08-09
acan:            TUR 0 kurulum
sorumlu_ajan:    mevzuat-ruhsat-uzmani (T0 takvimi) -> yatirim-komitesi-baskani
impact:          HIGH
bloke_ettigi:    vergi.yaml/meta.model_hedef_tarihi
```

### Soru

İlk konteynerin gümrükten çekileceği tahmini tarih nedir?

### Neden önemli

Vergi ve mevzuat verileri **bugünkü** hâliyle değil, **model hedef
tarihinde yürürlükte olacak** hâliyle kullanılmalıdır. Özellikle maktu ÖTV
tutarları periyodik olarak güncellenir. Bugünkü tutarla yapılan hesap,
ithalat anında geçersiz olabilir.

Bu, `seytanin-avukati`'nın **regülasyon şoku** vektörünün doğrudan konusudur.

### Nasıl kapatılır

`mevzuat-ruhsat-uzmani`'nın T0 → ilk konteyner takviminden türetilir.

---

## KURAL

- Yeni açık soru bu dosyaya `OQ-###` ile eklenir.
- Kritik bir açık soru (`impact: CRITICAL`) ilgili gate'i bloke eder.
- **Kritik UNKNOWN nihai kararı bloke edebilir** — bu bir başarısızlık değil,
  tasarımın parçasıdır (CLAUDE.md §1.14).
- Bir soru **sessizce** kapatılmaz; kapanış `evidence_id` ile kanıtlanır.
