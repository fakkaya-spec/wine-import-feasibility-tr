# ÇELİŞKİLER — navlun-lojistik-uzmani, TUR 2

```yaml
ajan:  navlun-lojistik-uzmani
tur:   TUR 2
tarih: 2026-08-10
not:   "Bu dosya 99-ops/celiskiler.md'ye BASKAN tarafindan islenir. Ben ana dosyaya dokunmadim."
```

**Hiçbir çelişkide sessizce taraf seçilmemiştir.**

---

## C-311 — FCL base okyanus navlunu: yüzlerce USD mi, binlerce EUR mu?

```yaml
conflict_id:      C-311
konu:             "Ispanya/Avrupa -> Turkiye FCL base okyanus navlunu"
impact:           CRITICAL
status:           OPEN
model_girdisi_etkisi: VAR — bandin genisligi 4 kat
etkiledigi_alan:  lojistik.yaml -> tur2.fcl_navlun.ispanya_turkiye_20dv_base_ocean
```

### Kaynak A — marketplace "from" fiyatları (düşük)

| Değer | Rota | tier | tarih | evidence_id |
|---|---|---|---|---|
| **295 USD** | Rotterdam → İzmir (13 gün) | T4 | **YOK** | `EV-2026-08-10-322` |
| **350 USD** | London Gateway → Mersin (13 gün) | T4 | YOK | `EV-2026-08-10-322` |
| **500 USD** | İstanbul → Barcelona (14 gün) | T4 | YOK | `EV-2026-08-10-322` |
| **650 USD** | Aarhus → İstanbul (19 gün) | T4 | YOK | `EV-2026-08-10-322` |

### Kaynak B — blog/rehber bantları (yüksek)

| Değer | Rota | tier | tarih | evidence_id |
|---|---|---|---|---|
| **1.200–2.500 EUR** (20ft, ort. 1.800) | İspanya → Türkiye | **T5** | 2025 | `EV-2026-08-10-324` |
| **1.200–2.500 EUR** (20ft) | İspanya → Türkiye | **T5** | yok | `EV-2026-08-09-333` (TUR 1) |

### Kaynak C — yayınlanmış taşıyıcı tarifesi (orta-yüksek, ama yanlış yön ve yıl)

| Değer | Rota | tier | yürürlük | evidence_id |
|---|---|---|---|---|
| **785–1.030 EUR** (20') | Türkiye → Trieste (**ihracat**) | T4 | **2025-01-01** | `EV-2026-08-10-320` |

### Neden çelişiyor — üç olası açıklama, hiçbiri doğrulanmadı

| # | Hipotez | Lehine | Aleyhine |
|---|---|---|---|
| **H1** | Düşük rakamlar **yalnızca base ocean**, yüksek rakamlar **quasi-all-in** | TUR 2'de origin locals (349–554 EUR) ve destination locals (165–298 USD) ölçüldü; toplamları farkın **büyük kısmını açıklıyor** | Kaynak B "base rate" diyor ve üstüne %15–25 yakıt eklediğini yazıyor — yani kendisi de base olduğunu iddia ediyor |
| **H2** | Kaynak B **eski/geri dönüştürülmüş** veri | İki T5 kaynak **birebir aynı bandı** veriyor (1.200–2.500 EUR) → bağımsız değiller, biri diğerinden kopyalamış olabilir | Doğrulanamadı |
| **H3** | "from" fiyatları **gerçekleşmeyen taban fiyatlar** (pazarlama) | Marketplace'lerde yaygın pratik | Doğrulanamadı |

### Bu turda ne yaptım

- **Taraf seçmedim.** Bandı olduğu gibi taşıdım: **300–1.200 USD**,
  `status: ESTIMATE`, `confidence: LOW`, `ttl: 14d`.
- `lojistik.yaml`'a "**merkezî varsayım olarak KULLANILAMAZ**" notu düştüm.
- LCL/FCL kırılma noktası bandının (2.200–9.800 şişe) **genişliğinin
  tamamının** bu çelişkiden geldiğini açıkça yazdım.

### Nasıl çözülür

**Tek yolu var: bir forwarder'dan yazılı kotasyon** — kalem kalem
`included/excluded` listesiyle (`T-304`). Masabaşında çözülemez.

---

## C-312 — Terminal ardiye free time: 0 gün mü 5 gün mü?

```yaml
conflict_id:      C-312
konu:             "Turkiye ithalatinda terminal ardiye free time"
impact:           MEDIUM
status:           OPEN
model_girdisi_etkisi: VAR — 60 gunluk bekleme senaryosunda ~200 USD/konteyner
etkiledigi_alan:  lojistik.yaml -> tur2.terminal_tarifeleri.ardiye_free_time_gun
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **İddia** | Free time **0 gün** | Free time **5 gün** |
| **Metin** | "İthalat ardiye günleri **geminin yanaştığı günden itibaren** başlar" | "Ardiye 40–60 USD/gün, **6. günden itibaren**" |
| **Kaynak** | SafiPort 2026 konteyner ithalat tarifesi | Gümrük müşavirliği 2026 maliyet rehberi |
| **tier** | T4 (terminalin kendi tarifesi) | T4 (meslek uygulayıcısı) |
| **evidence_id** | `EV-2026-08-10-317` | `EV-2026-08-10-325` |

### Değerlendirme

Çözüm hiyerarşisinin hiçbir kuralı uygulanamıyor: **ikisi de T4, ikisi de
2026.** Ayrıca **ikisi de doğru olabilir** — free time terminale göre
değişebilir ve Kaynak B bir *ortalama uygulama* anlatıyor olabilir.

### Bu turda ne yaptım

Muhafazakâr olanı (**0 gün**) kullandım — TUR 1 ile aynı. **Bu bir seçim
değil, ihtiyattır** ve `lojistik.yaml`'da öyle etiketlendi.
Yön uyarısı: yanılıyorsam gecikme maliyeti tahminim **yüksektir**, yani hata
proje **lehine** değil aleyhine çalışıyor.

### Nasıl çözülür

Kumport / Marport / Mardaş tarife PDF'lerinin doğrudan okunması veya
terminale yazılı soru (`T-313`).

---

## C-313 — Taşıyıcı THD'si ile terminal kapı-çıkış ücreti aynı olayı mı fiyatlıyor?

```yaml
conflict_id:      C-313
konu:             "Varis terminal ellecleme ucreti cift sayiliyor mu"
impact:           MEDIUM
status:           OPEN
model_girdisi_etkisi: VAR — konteyner basina ~115 USD (0,008-0,010 USD/sise)
etkiledigi_alan:  lojistik.yaml -> tur2.destination_charges_turkiye.thd_limana_gore
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **Kalem** | THD (Terminal Handling Charge Destination) | Kapı çıkış / terminal elleçleme |
| **Değer** | **165–298 USD** (limana göre) | **113–116 USD** |
| **Kesen** | Armatör (Hapag-Lloyd) | Terminal (Beldeport / SafiPort) |
| **tier** | **T3** (taşıyıcının resmî tarifesi) | T4 (terminalin tarifesi) |
| **evidence_id** | `EV-2026-08-10-315` | `EV-2026-08-10-319`, `-317` |

### Neden bu bir çelişki

Fiziksel olay tektir: konteyner gemiden indirilir, sahada elleçlenir, kapıdan
çıkar. Ama **iki farklı taraf iki farklı tarife yayınlıyor.** Üç senaryo:

1. **Armatör terminale öder, importer'a THD olarak yansıtır** → tek kalem
   (165–298 USD), terminal tarifesi importer'ı ilgilendirmez.
2. **İkisi ayrı faturalanır** → toplam 278–414 USD.
3. **Merchant haulage / carrier haulage'a göre değişir** → duruma bağlı.

**TUR 1, Kaynak B'yi (113 USD) tek kalem olarak modele koymuştu.** Bu, Senaryo
1 doğruysa **%32–62 düşük** bir tahmindir.

### Bu turda ne yaptım

Muhafazakâr olarak **yalnızca taşıyıcı THD'sini** (165–298 USD) hesaba kattım
ve çift sayım yapmadım. Terminal tarifesini ayrı bir bilgi olarak kayda
geçirdim. **Sessiz seçim değildir**: gerekçesi budur — taşıyıcı tarifesi T3,
terminal tarifesi T4 ve ithalatçının faturasını genellikle taşıyıcı keser.

### Nasıl çözülür

Bir gerçek ithalat faturası örneği veya forwarder'ın kalem listesi (`T-304`
RFQ'suyla aynı temasta, `T-313`).

---

## TUR 1 ÇELİŞKİLERİNİN TUR 2 SONRASI DURUMU

### C-302 — Akdeniz transit süresi → **A LEHİNE KAPATILMASI ÖNERİLİR**

```yaml
conflict_id:      C-302
tur2_onerisi:     "A tarafi lehine RESOLVED"
karar_yetkisi:    yatirim-komitesi-baskani
oneri_sahibi:     navlun-lojistik-uzmani
```

**Yeni kanıt:** Flexport (T4, tarihli 2026-08-10, geçerlilik 2026-08-16)
Valencia/Barcelona → İstanbul için **4 gün** veriyor (`EV-2026-08-10-301`,
`-302`).

| Taraf | İddia | Kaynak sayısı | Durum |
|---|---|---|---|
| **A** | İspanya → İstanbul **4–10 gün** | **3** (JSV T4 + Maersk servis tarifesi T3 + **Flexport T4**) | ✅ güçlendi |
| **B** | Valencia → İstanbul **32–35 gün**; LA → İstanbul **15 gün** | 1 (BR Logistics T5) | ❌ tek başına |

**Ek olarak B'nin ikinci ayağı da yanlışlandı:** LA → İstanbul gerçek süre
**20 gün** (kara aktarmalı) veya **44 gün** (deniz aktarmalı)
(`EV-2026-08-10-309`). **15 gün hiçbir kaynakla doğrulanmadı.**

**Önerim:** `C-302` → `RESOLVED (A lehine)`; B kaynağının (BR Logistics)
tüm transit iddiaları `REJECTED` sayılsın. **Kapatma yetkisi bende değildir.**

### C-301 (palet sayısı) — **DEĞİŞMEDİ**, TUR 2'de yeni kanıt bulunamadı, `OPEN`.

### C-303 (20DV payload) — **DEĞİŞMEDİ**, düşük etkili, `OPEN`.

---

## TUR 1'İN BİR TAHMİNİNİN DÜZELTİLMESİ *(çelişki değil, hata)*

Bu bir çelişki değil, **kendi TUR 1 tahminimin yanlışlanmasıdır** ve kayda
geçirilmesi gerekir:

| | TUR 1 | **TUR 2 (doğru)** |
|---|---|---|
| G. Afrika → Türkiye transit | **~26 gün** | **49 gün** |
| Dayanak | Türkiye → Cape Town **ters yön** ölçümü | Cape Town → İstanbul doğrudan kotasyon, Hamburg aktarmalı |
| evidence_id | `EV-2026-08-09-327` | `EV-2026-08-10-307` |

**TUR 1 tahmini yaklaşık 2 kat iyimserdi.** Sebep: ters yön ölçümü, aktarma
yapısını yansıtmaz. Bu, **ters yön verisinin neden kullanılmaması gerektiğinin
somut örneğidir** ve `EV-2026-08-09-327`'nin `SUPERSEDED` sayılması önerilir.
