# Wine Import Feasibility Turkey

Türkiye'ye **fiyat/performans segmentinde** şarap ithalatının gerçek ticari
fizibilitesini araştıran ve bunu bir yatırım kararına dönüştüren **çok ajanlı
araştırma sistemi.**

---

## ASIL SORU

> Metro rafında **599,90 TL**'ye satılan bir ithal şarabın karşısına
> çıkabilecek bir ürünü ithal edip kâr edebilir miyiz?
> Üreticiye en fazla kaç dolar/euro ödeyebiliriz?

**Benchmark:** Gold Country California Colombard-Chardonnay 2023, 750 ml —
Metro Türkiye, 09.08.2026 — **599,90 TL**
**Komşu benchmark:** Central Creek (Avustralya) — **649,90 TL**

> ⚠️ Bu fiyatların KDV dahil mi hariç mi, tüketici fiyatı mı cash & carry
> fiyatı mı olduğu **DOĞRULANMAMIŞTIR.**
> Bkz. `99-ops/acik-sorular.md` → **OPEN QUESTION #001**

---

## MEVCUT DURUM

```
TUR 0 — KURULUM TAMAMLANDI
```

Bu turda **bilinçli olarak** hiçbir araştırma yapılmamıştır.
Hiçbir vergi/navlun/fiyat verisi toplanmamış, model çalıştırılmamış,
karar verilmemiştir.

---

## BAŞLAMADAN ÖNCE — OKU

**`CLAUDE.md` bu repoda çalışan her ajan için BAĞLAYICIDIR.**

En kritik kurallar:

| # | Kural |
|---|-------|
| 1 | **Veri uydurmak yasaktır** |
| 2 | Doğrulanamayan veri `UNKNOWN`'dır — UNKNOWN yazmak başarısızlık değildir |
| 3 | Modele giren her önemli sayının `evidence_id`'si olmalıdır |
| 4 | Vergi/mevzuat sonucu T1/T2 resmî kaynağa dayanmalıdır — **T5 tek başına yetmez** |
| 5 | Vergi matrahları asla karıştırılmaz |
| 6 | EXW / FOB / CIF / landed cost / importer cost / wholesale / retail / shelf ayrı tutulur |
| 7 | Her ajan yalnızca kendi alanında sonuç üretir |
| 8 | Her raporun sonunda **"Bu bulguyu ne çürütür?"** bölümü zorunludur |
| 9 | Kaynaklar çelişirse sessizce seçim yapılmaz |
| 10 | **Kritik UNKNOWN nihai kararı bloke edebilir** |

---

## AJANLAR (9)

| # | Ajan | Rol |
|---|------|-----|
| 1 | `gumruk-vergi-uzmani` | GTİP, gümrük vergisi, ÖTV, KDV, KKDF, matrah sırası |
| 2 | `mevzuat-ruhsat-uzmani` | TADAB, ruhsat, etiket, bandrol, T0 takvimi |
| 3 | `navlun-lojistik-uzmani` | Konteyner, navlun, antrepo, iç lojistik |
| 4 | `global-sourcing-kasifi` | Ülke/tedarikçi keşfi, private label, RFQ şablonu |
| 5 | `turkiye-pazar-kasifi` | Raf fiyatları, rakipler, kanal yapısı |
| 6 | `kanal-marj-uzmani` | Kanal marjları, listeleme, vade, dağıtım modeli |
| 7 | `finans-fizibilite` | Model — **veri üretmez**, birleştirir |
| 8 | `seytanin-avukati` | Kırmızı takım — projeyi öldürmeye çalışır |
| 9 | `yatirim-komitesi-baskani` | Orkestrasyon, gate kontrolü, **nihai karar** |

`finans-fizibilite` ve `yatirim-komitesi-baskani` ajanlarının **web araçları
yoktur.** Bu kasıtlıdır — biri veri üretmesin, diğeri kendi araştırmasını
yapmasın diye.

---

## KOMUTLAR (7)

| Komut | Ne yapar |
|-------|----------|
| `/tur-1-kesif` | TUR 1 — 5 ajanı paralel başlatır |
| `/capraz-kontrol` | Çelişki, boşluk, kanıt kalitesi denetimi |
| `/model-calistir` | TUR 3 — finans modelini çalıştırır |
| `/kirmizi-takim` | TUR 4 — kırmızı takım saldırısı |
| `/komite` | TUR 6 — gate kontrolü ve nihai karar |
| `/tazelik-kontrol` | TTL dolmuş kanıtları bulur, yeniden doğrulatır |
| `/teklif-gir` | Gerçek tedarikçi teklifini kanıtlı olarak sisteme girer |

---

## AKIŞ

```
TUR 0  Kurulum                                              ✅ TAMAMLANDI
TUR 1  Paralel keşif (5 ajan)                               ⬜
TUR 2  Kanal-marj + çapraz kontroller                       ⬜
TUR 3  Finans modeli                                        ⬜
TUR 4  Şeytanın avukatı                                     ⬜
TUR 5  Düzeltmeler                                          ⬜
TUR 6  Yatırım komitesi — KARAR                             ⬜
TUR 7  Gerçek RFQ / navlun / kanal doğrulaması              ⬜
       (yalnızca karar TEST veya IMPORT PILOT ise)
```

---

## KLASÖR YAPISI

```
CLAUDE.md                     Bağlayıcı kurallar
README.md                     Bu dosya
_SABLON-ajan-raporu.md        Ajan rapor şablonu

.claude/agents/               9 ajan
.claude/commands/             7 komut

00-charter/                   benchmark · karar-esikleri · kapsam
10-evidence/                  Kanıt kartları (immutable) + index.csv
20-mevzuat/                   Ruhsat, TADAB, etiket, bandrol
30-vergi-gumruk/              matrah-sirasi.md + GTİP, oran, rejim
40-lojistik/                  Konteyner, navlun, antrepo
50-sourcing/                  ulke-karsilastirma · tedarikci-havuzu · rfq-template
60-pazar/                     raf-fiyat-gozlemleri.csv + segment analizi
70-kanal/                     Kanal marjları ve ticaret koşulları
80-model/                     inputs/ (8 YAML) · engine/ (3 py) · outputs/
90-karar/                     kirmizi-takim-raporu · karar-gunlugu
99-ops/                       acik-sorular · celiskiler · capraz-ipuclari
                              veri-tazeligi · CHANGELOG · tickets/
```

---

## MALİYET KATMANLARI

Bu katmanlar **asla karıştırılmaz:**

| Katman | Tanım |
|--------|-------|
| L0 | EXW — fabrika/mahzen çıkış |
| L1 | FOB — yükleme limanı bordası |
| L2 | CIF — varış limanı, navlun + sigorta dahil |
| L3 | PRE-TAX LANDED |
| L4 | POST-TAX LANDED |
| L5 | IMPORTER COST |
| L6 | IMPORTER SELLING PRICE |
| L7 | RETAILER PURCHASE PRICE |
| L8 | CONSUMER SHELF PRICE |

**KDV her zaman iki perspektifte gösterilir:**
(A) ekonomik maliyet / indirilebilirlik — (B) nakit akışında fiili ödeme zamanı
(`cash_tax_timing`). `peak_cash_requirement` mutlaka hesaplanır.

---

## KAYNAK OTORİTESİ

| Tier | Tanım |
|------|-------|
| T1 | Resmî Gazete / kanun / CBK / tebliğ |
| T2 | Kamu kurumunun resmî güncel sayfası |
| T3 | Resmî rehber / meslek örgütü / akredite kurum |
| T4 | Ticari teklif / sektör raporu / market gözlemi |
| T5 | Basın / blog / forum / LLM hafızası |

**Vergi ve mevzuat sonucu için T5 tek başına kullanılamaz.**

---

## MODELİ ÇALIŞTIRMA

```bash
cd 80-model/engine
python3 hesap.py
python3 duyarlilik.py
```

TUR 0'da model **kasıtlı olarak hesap yapmaz.** Katman iskeletini kurar,
eksik girdileri listeler ve `UNKNOWN` döner. Bu bir hata değildir —
uydurulmuş bir vergi hesabı, hiç hesap olmamasından daha tehlikelidir.

Gereksinim: Python 3.10+ · PyYAML (yoksa model yine çalışır, eksik girdi
bildirir — uydurma yapmaz).

---

## SONRAKİ ADIM

1. **Session'ı yeniden başlat** (9 ajanın registry'ye yüklenmesi için)
2. 9 ajanın registry'de **gerçekten** mevcut olduğunu doğrula
3. `/tur-1-kesif` çalıştır

> **Registry 9 ajanı tanımıyorsa:** `general-purpose` veya `Explore`
> kullanma, başka ajanı vekil atama, ajanların çalıştığını iddia etme.
> `SESSION RESTART REQUIRED` yaz ve dur. (CLAUDE.md §11)
