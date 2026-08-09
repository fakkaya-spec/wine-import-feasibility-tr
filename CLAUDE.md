# CLAUDE.md — Wine Import Feasibility Turkey

Bu dosya bu repoda çalışan **her ajan** ve **her session** için BAĞLAYICIDIR.
Kurallar tavsiye değildir. İhlal edilirse üretilen çıktı geçersizdir.

---

## 0. PROJENİN AMACI

Türkiye'ye **fiyat/performans segmentinde** şarap ithalatının gerçek ticari
fizibilitesini araştırmak ve bunu bir yatırım kararına dönüştürmek.

İlk benchmark ve komşu benchmark için bkz. `00-charter/benchmark.md`.
Kapsam için bkz. `00-charter/kapsam.md`.
Karar eşikleri için bkz. `00-charter/karar-esikleri.md`.

---

## 1. TEMEL ARAŞTIRMA PRENSİPLERİ (BAĞLAYICI)

1. **Veri uydurmak yasaktır.** Hatırlamak, tahmin etmek veya "genelde şu kadardır"
   demek veri değildir.
2. **Doğrulanamayan veri `UNKNOWN`'dır.** UNKNOWN yazmak başarısızlık değildir;
   uydurmak başarısızlıktır.
3. Modelleme için zorunlu tahmin `ASSUMPTION` olarak etiketlenir ve gerekçesi yazılır.
4. Gerçek verilerden türetilmiş yaklaşık değer `ESTIMATE` olarak etiketlenir ve
   türetildiği kanıtlar (evidence_id) listelenir.
5. Doğrulanmış bilgi `FACT` olarak etiketlenir ve kaynağı gösterilir.
6. **Modele giren her önemli sayının `evidence_id`'si olmalıdır.** evidence_id'si
   olmayan sayı modele giremez.
7. Vergi ve mevzuat sonuçları mümkün olduğunca **T1/T2 resmî kaynaklara** dayanmalıdır.
8. **Vergi matrahları asla karıştırılmamalıdır.** Hangi verginin hangi matrah
   üzerinden ve hangi sırayla hesaplandığı `30-vergi-gumruk/matrah-sirasi.md`
   dosyasında açıkça tanımlı olmalıdır.
9. Şu kavramlar **ayrı tutulur, birbirinin yerine kullanılamaz**:
   `EXW`, `FOB`, `CIF`, `landed cost`, `importer cost`, `wholesale price`,
   `retail purchase price`, `consumer shelf price`.
10. **Her ajan yalnızca kendi görev alanında sonuç üretir.** Kapsam dışı konuda
    sonuç/karar üretmek yasaktır.
11. Alan dışı bulgular **silinmez**, `99-ops/capraz-ipuclari.md` dosyasına bırakılır.
12. **Her ajan raporunun sonunda "Bu bulguyu ne çürütür?" bölümü zorunludur.**
13. Kaynaklar çelişirse **sessizce seçim yapılmaz**. Çelişki
    `99-ops/celiskiler.md` dosyasına kaydedilir ve başkana taşınır.
14. **Kritik UNKNOWN nihai kararı bloke edebilir.** Bu bir hata değil, tasarımdır.
15. **Finans modeli kanıtsız sayı üretmez.** Girdi yoksa çıktı `UNKNOWN` döner.
16. **Başkan kendi araştırmasını yapmaz.** Başkan yalnızca orkestre eder, kanıt
    kalitesini denetler, çelişkileri çözer ve karar verir.
17. **Şeytanın avukatı projeyi doğrulamaya değil, yanlışlamaya çalışır.**

---

## 2. KAYNAK OTORİTESİ (TIER)

| Tier | Tanım |
|------|-------|
| **T1** | Resmî Gazete / yürürlükteki kanun, Cumhurbaşkanlığı Kararı (CBK), tebliğ |
| **T2** | İlgili kamu kurumunun resmî ve güncel sayfası |
| **T3** | Resmî rehber / meslek örgütü / akredite kurum |
| **T4** | Ticari teklif / sektör raporu / market gözlemi |
| **T5** | Basın / blog / forum / LLM hafızası |

**KURAL: Vergi ve mevzuat sonucu için T5 tek başına kullanılamaz.**
T5 yalnızca "nereye bakılacağını" gösteren bir ipucu olarak kullanılabilir ve
sonuç T1/T2 ile doğrulanmadan FACT sayılamaz.

T4 (market gözlemi, ticari teklif) pazar ve sourcing verisi için meşrudur, ancak
tier'ı kanıt kartında açıkça yazılır.

---

## 3. VERİ STATÜ ETİKETLERİ

| Etiket | Anlamı |
|--------|--------|
| `FACT` | Doğrulanmış, kaynaklı bilgi |
| `ESTIMATE` | Gerçek verilerden türetilmiş yaklaşık değer (türetme zinciri gösterilir) |
| `ASSUMPTION` | Modelleme için zorunlu tahmin (gerekçe + duyarlılık zorunlu) |
| `UNKNOWN` | Doğrulanamadı |
| `CONFLICT` | Kaynaklar çelişiyor, çözülmedi |
| `SUPERSEDED` | Yeni kanıtla değiştirildi (kanıt silinmez, bağlanır) |

---

## 4. KANIT SİSTEMİ

Her önemli veri için `10-evidence/raw/` altına bir **kanıt kartı** açılır.
Şablon: `10-evidence/_SABLON-kanit-karti.md`
Dizin: `10-evidence/index.csv`

**Evidence ID formatı:** `EV-YYYY-MM-DD-###` (örn. `EV-2026-08-09-001`)

Zorunlu alanlar:
`evidence_id, claim, value, unit, tier, source_name, url, publication_date,
effective_date, access_date, confidence, status, ttl, snapshot_path,
collecting_agent, supersedes, conflict_id, notes`

**KURALLAR:**
- Kanıt kartları **immutable**'dır. İçeriği değiştirilmez.
- Yeni veri eski kanıtı **overwrite etmez**. Yeni kart açılır, `supersedes`
  alanı ile eskiye bağlanır; eski kartın `status` alanı `SUPERSEDED` olur.
- `snapshot_path` mümkün olduğunca doldurulur (sayfa kopyası / ekran görüntüsü).
- `ttl` (tazelik süresi) dolan kanıtlar `99-ops/veri-tazeligi.md` üzerinden
  yeniden doğrulanır.
- `publication_date` ≠ `effective_date` ≠ `access_date`. Vergi/mevzuatta
  **yürürlük tarihi (effective_date)** belirleyicidir.

---

## 5. TICKET SİSTEMİ

Şablon: `99-ops/tickets/_SABLON-ticket.md`

Alanlar: `ticket_id, opened_by, target_agent, claim, impact, status, resolution_evidence`

**ID formatı:** `T-###`
**Status:** `OPEN` → `ANSWERED` → `RESOLVED` / `REJECTED`

**KURAL: Kritik (`impact: CRITICAL`) açık ticket varken finans modeli
`APPROVED` olamaz.**

---

## 6. MALİYET KATMANLARI (KARIŞTIRILAMAZ)

| Katman | Tanım |
|--------|-------|
| **L0** | EXW — fabrika/mahzen çıkış |
| **L1** | FOB — yükleme limanı bordası |
| **L2** | CIF — varış limanı, navlun + sigorta dahil |
| **L3** | PRE-TAX LANDED — CIF + vergi öncesi yurt içi masraflar |
| **L4** | POST-TAX LANDED — tüm ithalat vergileri dahil |
| **L5** | IMPORTER COST — ithalatçının tam maliyeti (bandrol, depo, iç nakliye, finansman vb.) |
| **L6** | IMPORTER SELLING PRICE — ithalatçı satış fiyatı |
| **L7** | RETAILER PURCHASE PRICE — perakendecinin alış fiyatı |
| **L8** | CONSUMER SHELF PRICE — tüketici raf fiyatı |

Bir katmanın sayısı başka bir katmanın yerine kullanılamaz.
Bir katmandan diğerine geçiş **açıkça gösterilir** (hangi kalem eklendi/çıktı).

### KDV — iki ayrı perspektif
KDV her zaman **iki ayrı** şekilde gösterilir:
- **A) Ekonomik maliyet / indirilebilirlik**: KDV indirilebiliyorsa ekonomik
  maliyet değildir; indirilemiyorsa maliyettir.
- **B) Nakit akışındaki fiili ödeme zamanı**: gümrükte ne zaman ödenir,
  ne zaman mahsup/iade edilir.

Bu ayrım `cash_tax_timing` mantığı ile modellenir.
`peak_cash_requirement` mutlaka hesaplanır.

---

## 7. AJANLAR

`.claude/agents/` altında 9 ajan tanımlıdır:

| # | Ajan | Rol |
|---|------|-----|
| 1 | `gumruk-vergi-uzmani` | GTİP, gümrük vergisi, ÖTV, KDV, KKDF, matrah sırası |
| 2 | `mevzuat-ruhsat-uzmani` | TADAB, ruhsat, etiket, bandrol, izin takvimi |
| 3 | `navlun-lojistik-uzmani` | Konteyner, navlun, sigorta, antrepo, iç lojistik |
| 4 | `global-sourcing-kasifi` | Ülke/tedarikçi keşfi, private label, RFQ şablonu |
| 5 | `turkiye-pazar-kasifi` | Raf fiyatları, rakipler, kanal yapısı, pazar hacmi |
| 6 | `kanal-marj-uzmani` | Kanal marjları, listeleme, vade, dağıtım modeli |
| 7 | `finans-fizibilite` | Model — veri ÜRETMEZ, birleştirir |
| 8 | `seytanin-avukati` | Kırmızı takım — projeyi öldürmeye çalışır |
| 9 | `yatirim-komitesi-baskani` | Orkestrasyon, gate kontrolü, nihai karar |

**Ajan izolasyonu:** Bir ajan başka bir ajanın alanında sonuç üretemez.
Şüpheli/ilginç ama alan dışı bulgu → `99-ops/capraz-ipuclari.md`.

---

## 8. ARAŞTIRMA AKIŞI (TURLAR)

| Tur | İçerik |
|-----|--------|
| **TUR 0** | Kurulum (bu tur) |
| **TUR 1** | Paralel keşif: gümrük-vergi, mevzuat-ruhsat, navlun-lojistik, global-sourcing, türkiye-pazar |
| **TUR 2** | kanal-marj-uzmani + çapraz kontroller |
| **TUR 3** | finans-fizibilite |
| **TUR 4** | seytanin-avukati |
| **TUR 5** | İlgili ajanların düzeltmeleri |
| **TUR 6** | yatirim-komitesi-baskani — karar |
| **TUR 7** | Karar TEST veya IMPORT PILOT ise: gerçek RFQ / gerçek navlun / gerçek kanal doğrulaması |

---

## 9. KARARLAR

Nihai karar yalnızca `yatirim-komitesi-baskani` tarafından verilir:

`KILL` · `HOLD` · `TEST` · `IMPORT PILOT` · `SCALE`

Başkan:
- Kanıtsız sayıyı reddeder.
- Başka ajanın bulgusunu kendi tahminiyle değiştirmez.
- Karar gerekçesini `90-karar/karar-gunlugu.md` dosyasına yazar.

---

## 10. RAPOR FORMATI

Her ajan raporu kökteki `_SABLON-ajan-raporu.md` şablonunu kullanır.
Zorunlu son bölüm: **"Bu bulguyu ne çürütür?"**

---

## 11. SESSION / AGENT REGISTRY KURALI (KRİTİK)

9 ajan dosyası oluşturulduktan sonra, mevcut Claude Code session'ının agent
registry'si bu ajanları tanımıyorsa:

- `general-purpose` **kullanılmaz**
- `Explore` **kullanılmaz**
- başka ajan **vekil atanmaz**
- görev başka agent type'a **taşınmaz**
- ajanların çalıştığı **iddia edilmez**

Bunun yerine tam olarak şu yazılır ve DURULUR:

```
SESSION RESTART REQUIRED
```

Yeni session açıldıktan sonra 9 ajanın registry'de **gerçekten** mevcut olduğu
doğrulanmadan TUR 1 başlamaz.

---

## 12. FİNANS MODELİ — GÜVENLİK KİLİDİ

`80-model/engine/` altındaki kod, A1 seviyesinde resmî mevzuatla doğrulanmadan:
- vergi oranı
- ÖTV tutarı / oranı
- KDV oranı
- KKDF oranı
- matrah tanımı

**hard-code etmez.** Bu değerler `80-model/inputs/vergi.yaml` içinde `null` +
`status: UNKNOWN` olarak durur ve evidence_id ile doldurulur.

Model, eksik girdi ile çalıştırıldığında **uydurmaz** — `UNKNOWN` döndürür ve
hangi girdinin eksik olduğunu raporlar.

---

## 13. DİL

Repo dili Türkçe'dir. Teknik terimler (EXW, FOB, CIF, landed cost, contribution
margin vb.) İngilizce orijinal haliyle kullanılır ve çevrilmez.
