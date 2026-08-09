# CHANGELOG

Bu dosya reponun yapısal değişikliklerini kaydeder.
Araştırma bulguları buraya değil, ilgili klasörlere ve `10-evidence/`'a yazılır.

---

## [TUR 0] — 2026-08-09 — KURULUM

### Eklendi

**Kök**
- `CLAUDE.md` — bağlayıcı araştırma prensipleri, tier sistemi, maliyet
  katmanları, evidence/ticket kuralları, session restart kuralı
- `README.md`
- `_SABLON-ajan-raporu.md` — zorunlu "Bu bulguyu ne çürütür?" bölümü ile

**Ajanlar (`.claude/agents/`) — 9 adet**
- `gumruk-vergi-uzmani`
- `mevzuat-ruhsat-uzmani`
- `navlun-lojistik-uzmani`
- `global-sourcing-kasifi`
- `turkiye-pazar-kasifi`
- `kanal-marj-uzmani`
- `finans-fizibilite` (web araçları YOK — veri üretmez)
- `seytanin-avukati`
- `yatirim-komitesi-baskani` (web araçları YOK — araştırma yapmaz)

**Komutlar (`.claude/commands/`) — 7 adet**
- `tur-1-kesif.md`
- `capraz-kontrol.md`
- `model-calistir.md`
- `kirmizi-takim.md`
- `komite.md`
- `tazelik-kontrol.md`
- `teklif-gir.md`

**Charter (`00-charter/`)**
- `benchmark.md` — Gold Country 599,90 TL + Central Creek 649,90 TL,
  ikisi de `FACT_FROM_PHOTO`, KDV/katman durumu `UNKNOWN`
- `karar-esikleri.md` — finansal eşikler bilinçli olarak `TBD`;
  araştırma tercihleri belirlendi
- `kapsam.md` — kapsam içi/dışı, bulk hipotezi kapsam dışı olarak işaretlendi

**Kanıt sistemi (`10-evidence/`)**
- `_SABLON-kanit-karti.md` — 18 alanlı immutable kanıt kartı
- `index.csv` — başlık satırı (boş)
- `raw/` — boş

**Vergi (`30-vergi-gumruk/`)**
- `matrah-sirasi.md` — boş iskelet, tüm hücreler `UNKNOWN`

**Sourcing (`50-sourcing/`)**
- `ulke-karsilastirma.md` — 9 ülke iskeleti
- `tedarikci-havuzu.csv` — 44 kolonlu başlık
- `rfq-template.md` — v1.0, gönderime hazır İngilizce şablon

**Pazar (`60-pazar/`)**
- `raf-fiyat-gozlemleri.csv` — 32 kolonlu başlık + format açıklama satırı

**Model (`80-model/`)**
- `inputs/` — 8 YAML iskeleti, tüm değerler `null`/`UNKNOWN`
- `engine/matrah_sirasi.py` — boş iskelet, oran hard-code YOK
- `engine/hesap.py` — L0–L8 katman iskeleti, hesap yapmaz
- `engine/duyarlilik.py` — FX/FREIGHT/ÖTV/PRICE eksenleri, hesap yapmaz
- `outputs/` — boş

**Karar (`90-karar/`)**
- `kirmizi-takim-raporu.md` — iskelet
- `karar-gunlugu.md` — iskelet

**Ops (`99-ops/`)**
- `acik-sorular.md` — **OQ-001** (Metro benchmark KDV/kanal statüsü,
  `impact: CRITICAL`), **OQ-002** (model hedef tarihi)
- `celiskiler.md` — boş + çözüm hiyerarşisi + beklenen çelişki noktaları
- `capraz-ipuclari.md` — IP-001…IP-008 kurulum ipuçları
- `veri-tazeligi.md` — TTL referans tablosu
- `CHANGELOG.md`
- `tickets/_SABLON-ticket.md`

### Bilinçli olarak YAPILMADI

Bu tur **sadece kurulum turudur.** Kullanıcı talimatı gereği:

- ❌ Web araştırması yapılmadı
- ❌ Vergi / navlun / ÖTV / KDV oranı bulunmadı
- ❌ Fizibilite sonucu üretilmedi
- ❌ Yatırım kararı verilmedi
- ❌ Hiçbir sayı uydurulmadı
- ❌ Engine'de hiçbir vergi oranı hard-code edilmedi
- ❌ Karar eşiklerine değer atanmadı (`TBD` bırakıldı)

### Açık kalanlar

| # | Konu | Sorumlu |
|---|------|---------|
| OQ-001 | Metro 599,90 TL — KDV dahil/hariç, L7/L8 | `turkiye-pazar-kasifi` |
| OQ-002 | Model hedef tarihi | `mevzuat-ruhsat-uzmani` |
| — | Karar eşikleri `TBD` | Yatırımcı |
| — | 9 ajanın registry'de doğrulanması | Yeni session |

---

## KAYIT FORMATI (SONRAKİ TURLAR İÇİN)

```
## [TUR N] — YYYY-MM-DD — BAŞLIK

### Eklendi
### Değişti
### Kaldırıldı
### Açılan ticket'lar
### Kapanan açık sorular
### Model etkisi
```
