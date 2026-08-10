# AJAN RAPORU — TUR 3A · gumruk-vergi-uzmani

```yaml
ajan:               gumruk-vergi-uzmani
tur:                TUR 3A — KDV CRITICAL CHECK + GÖZETİM/KIYMET
tarih:              2026-08-10
durum:              SUBMITTED
kapsam:             T-947 (CRITICAL) · T-151 (MEDIUM) · gözetim/referans kıymet
BASE_DATE:          2026-08-10
yeni_evidence:      14 (EV-2026-08-10-851 … -864)
acilan_ticket:      T-171, T-172, T-173
acilan_conflict:    YOK
```

---

## 1. YÖNETİCİ ÖZETİ

**Başkan bu turu "ters modelin tüm sayılarını çürütebilecek tek bulgu" olarak
işaretledi. Sonuç: sayılar ayakta, ama gerekçe değişti.**

1. **T-947 → (A) KDV İNDİRİMİ CONFIRMED.** `MAX_CIF_TRY` üzerindeki etki
   **0,00 TL/şişe**. `reverse-price-model.md`, `sweet-spot-analizi.md` ve
   `country-buying-ceilings.csv` **yeniden hesaplanmayacaktır.**
2. **Ama başkanın sorusu haklıydı ve benim TUR 1.5'teki "olasılık düşük"
   değerlendirmem YANLIŞTI:** KDVK md.36'ya dayanan, **yürürlükte bir
   Cumhurbaşkanı Kararı VARDIR** — **7846 sayılı Karar** (RG 24/11/2023-32379,
   `EV-2026-08-10-852`, T1). Karar **alkole özgü değil, ÖNLEME özgüdür**:
   gözetim / korunma önlemi / dampinge karşı vergi kapsamındaki matrah
   artışlarına ait KDV'nin indirim hakkını kaldırır.
3. **2204.21 bu üç önlemin hiçbirine tabi değildir** — üç ayrı resmî kaynakla
   pozitif olarak gösterildi (`EV-2026-08-10-860`, `-861`, `-862`).
   Yani cevap `A`'dır, ama dayanağı *"md.36 kararı yok"* değil,
   **"md.36 kararı VAR ama bu ürüne değmiyor."**
4. **Gözetim sorusu `UNKNOWN`'dan `FACT`'e çevrildi.** TUR 1'in "negatif arama"
   kaydı (`EV-2026-08-09-125`) yerine, **RG 31/12/2025-33124 (4. mükerrer)
   yıllık gözetim paketinin 47 tebliğinin tamamı** tarandı: **305 GTİP,
   22. fasıl hiç yok, 2204 sayısı 0** (`EV-2026-08-10-860`, T1).
   → `gozetim_esigi` artık `UNKNOWN` değil **`N/A`**; ters modelin
   `CIF_TRY_max`'ı üzerinde **hukuki bir alt sınır yoktur.**
5. **En önemli yapısal keşif:** gözetim ve KDV artık **aynı kırılma noktasını
   paylaşıyor.** 2204.21'e bir gün gözetim gelirse **üç etki birden** doğar:
   (a) beyan alt sınırı, (b) KDV'nin **kısmen** ekonomik maliyete dönmesi,
   (c) altışar aylık **YMM raporu** uyum yükü.

---

## 2. BULGULAR

### B-1: md.36 yetkisi ayakta ve fiilen kullanılmış

```yaml
claim:          KDVK md.36 Cumhurbaşkanı'na indirim hakkını mal bazında kaldırma yetkisi verir; AYM 22/7/2025 kararı yalnız "iade" ibaresini iptal etti (yürürlük 9/9/2026), "indirim" yetkisi ayaktadır
value:          "indirim yetkisi YÜRÜRLÜKTE"
unit:           -
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-851
effective_date: 2018-07-02
katman:         -
```

**Gerekçe:** Madde metni *"…indirim veya iade hakkını kısmen veya tamamen
kaldırmaya … ve bu şekilde indirim veya iade hakkı kısıtlanan **mal veya
hizmetleri belirlemeye** … yetkilidir."* Yani "şarap" diye bir karar
**hukuken mümkündür.** AYM iptali yalnız **iade** yetkisini kaldırır; şarapta
iade hakkı zaten yoktur (`EV-2026-08-10-104`) → iptalin bu projeye etkisi
**sıfırdır**, ama **indirim riski kapanmamıştır.**

---

### B-2: 7846 sayılı CB Kararı — md.36 yetkisi FİİLEN KULLANILMIŞ

```yaml
claim:          İthalatta gözetim/korunma önlemi/damping kaynaklı matrah artışlarına ait KDV'nin indirim hakkı kaldırılmıştır
value:          "7846 sayılı CBK (+ 8000 sayılı değişiklik)"
unit:           -
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-852
effective_date: 2023-11-24
katman:         -
```

**Gerekçe:** Resmî Gazete tam metni doğrudan okundu (OCR) ve **KDVGUT
III/C-2.6'daki resmî alıntıyla kelime kelime karşılaştırılarak** doğrulandı.
8000 sayılı Karar (`EV-2026-08-10-853`) yalnız bir geçici madde eklemiştir;
süresi **1/4/2024**'te dolmuştur, bugün etkisizdir.

**Kritik nitelik:** Karar **ürün bazlı değil, önlem bazlıdır.** Metinde
"alkol", "içki", "şarap" **geçmez.**

---

### B-3: Kısıt KISMİDİR — %22,7 fazla kötümser

```yaml
claim:          7846 kapsamında indirilemeyen KDV, yalnız tevsik edilemeyen artışa isabet eden kısımdır; CIF ve ona isabet eden GV/İGV üzerinden ödenen KDV indirilebilir kalır
value:          "indirilemeyen = kdv_oranı × (D + D·gv + D·igv)"
unit:           -
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-854
effective_date: 2026-01-31
katman:         -
```

**Gerekçe:** KDVGUT III/C-2.6'nın **sayısal örneği** birebir: CIF 4.000.000 TL,
gözetim bedeli 10.000.000 TL, GV %10, İGV %15, KDV %20 →
**indirilemeyecek KDV 1.500.000 TL**, **indirilecek KDV 1.000.000 TL.**
Yani KDV'nin **%40'ı** indirilebilir kalıyor — o örnekte.

**Model etkisi:** `finans-fizibilite`'nin `T-947`'de yazdığı **%22,7 düşüş**
**tam kısıt** varsayımıdır ve **fazla kötümserdir** → `T-171`.

---

### B-4: 32 CBK + 86 BKK TAM SAYIM — başka md.36 kısıtı yok

```yaml
claim:          KDVK'ya bağlı tüm Cumhurbaşkanı ve Bakanlar Kurulu kararları tarandı; md.36 dayanaklı indirim kısıtı yalnızca 7846 (+8000)
value:          32 CBK + 86 BKK
unit:           adet (tam sayım)
status:         FACT
tier:           T2
evidence_id:    EV-2026-08-10-856
effective_date: 2026-08-10
katman:         -
```

**Gerekçe:** GİB'in kanun bazlı mevzuat kaydından **totalElements=32 ve 86**
ile tam liste çekildi (örnekleme değil). Başlığında "36 ncı madde" geçen
3 BKK incelendi: **üçü de KDV ORANI kararıdır**, md.36 yalnızca md.28 ile
birlikte **usul dayanağı** olarak anılmıştır.

**Kırılganlık (dürüstlük):** GİB'in **kendi eşleştirmesine** dayanır.
`mevzuat.gov.tr` erişilemediği için ikinci bağımsız kaynakla çaprazlanamadı
(`EV-2026-08-10-864`) → `confidence: MEDIUM`.

---

### B-5: KDVGUT tam metin — ithalatçıya kısıt yok

```yaml
claim:          KDVGUT 397 sayfa tam metin tarandı; şarap ithalatçısının indirim hakkını sınırlayan tek bir hüküm yok
value:          19
unit:           eşleşen satır (tamamı kapsam dışı)
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-859
effective_date: 2026-01-31
katman:         -
```

Ayrıca **III/C-1** (`EV-2026-08-10-855`) ithalatta ödenen KDV'nin
indirilebilirliğini tebliğ düzeyinde teyit eder.

---

### B-6: Alkole özgü TEK kısıt — ve mükellefi ithalatçı değil

```yaml
claim:          KDVGUT III/B-2.5.2 — "her şey dahil" geceleme hizmetinde kullanılan alkollü içeceklere ait yüklenilen KDV KONAKLAMA TESİSİ tarafından indirilemez
value:          "mükellef: KONAKLAMA TESİSİ"
unit:           -
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-858
effective_date: 2014-05-01
katman:         -
```

**Vergi bacağına etkisi sıfır. Kanal marjına etkisi var** → çapraz ipucu
`kanal-marj-uzmani`'ye bırakıldı (Cİ-3A-01). Sonuç üretmedim.

---

### B-7: GİB özelgesi — idari görüş de aynı yönde

```yaml
claim:          "alkollü içki alımları nedeniyle yüklenilen KDV, Kanunun 29 uncu maddesi uyarınca indirim konusu yapılabilecektir"
value:          "indirilebilir"
unit:           -
status:         FACT
tier:           T2
evidence_id:    EV-2026-08-10-857
effective_date: 2011-08-20
katman:         -
```

**İkincil bulgu:** alkollü içkide **özel matrah şekli** TEKEL'e özgüydü ve
özelleştirme ile **fiilen kalkmıştır** → `matrah-sirasi.md` sıra 5 (KDV matrahı,
genel esaslar) **doğrulanmıştır.**

---

### B-8: GÖZETİM YOK — negatif aramadan pozitif taramaya

```yaml
claim:          RG 31/12/2025-33124 (4. mükerrer) yıllık gözetim paketinin 47 tebliğinin tamamı tarandı; 305 GTİP içinde 22. fasıl hiç yok
value:          0
unit:           2204/2205/2206 eşleşmesi (305 GTİP içinde)
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-860
effective_date: 2026-01-01
katman:         -
```

**Türetme zinciri (yöntem kritik):** üç bağımsız çıkarımın **birleşimi**
kullanıldı — (a) PDF metin katmanı, (b) sayfa görüntüsü OCR, (c) **gömülü
tablo görüntüsü** OCR. **Tek yöntem yanlış negatif üretirdi**: bazı tebliğlerde
GTİP tablosu metin katmanında **hiç yoktur**, ayrı bir CCITT/JBIG2 görüntüdür.
47 dosyanın 46'sından GTİP çıkarıldı; kalan 1'i (2024/14 değişikliği) ayrıca
tam OCR edildi — **GTİP tablosu içermiyor.**

**Destekleyen bulgular:** korunma önlemleri **11 adet, hepsi sanayi**
(`EV-2026-08-10-861`); damping listesi **1015 GTİP, 2204 sayısı 0**
(`EV-2026-08-10-862`); 2026 İthalat Tebliğleri **19 adet, şarap konulu yok**
(`EV-2026-08-10-863`).

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| U-1 | Yıllık pakete girmemiş, daha eski ve hâlâ yürürlükte bir gözetim tebliği var mı | Yöntem yalnız yıllık paketi görüyor; `mevzuat.gov.tr` erişilemedi | **MEDIUM** | TARA ekranından tek GTİP sorgusu (CAPTCHA → insan) **veya** gümrük müşaviri — `T-172` |
| U-2 | Gözetim OLMAKSIZIN GK md.23–31 kıymet artırımına 7846 uygulanır mı | Karar ve KDVGUT metinlerinden çıkmıyor | **MEDIUM** | YMM / gümrük müşaviri — `T-173` |
| U-3 | `mevzuat.gov.tr` ile ikinci bağımsız doğrulama | Site tamamen erişilemedi (5 deneme) | LOW | erişim geri geldiğinde — `EV-…-864`, ttl 7d |
| U-4 | GVK md.41 (şahıs işletmesi muadili) | `mevzuat.gov.tr` erişilemedi | LOW | ithalatçı A.Ş. ise **gereksiz** |
| U-5 | 7846 YMM raporu eşiği (46 Sıra No.lu SMMM-YMM Genel Tebliği tutarı) | Baz senaryoda tetiklenmiyor | LOW | tetiklenirse aranır |
| U-6 | Gözetim tetiklenirse YMM raporu ücreti (L5 kalemi) | Alan dışı | LOW | `finans-fizibilite` / muhasebe |
| U-7 *(devam)* | KKDF matrahının tam tanımı | TUR 1'den açık | MEDIUM | `T-105` |
| U-8 *(devam)* | Gümrük beyanında esas kur kuralı | TUR 2.5'te kapatılamadı, bu turun kapsamı dışıydı | **HIGH** | `T-911` |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

**Kaynaklar arası çelişki: YOK.** `C-171 … C-189` bloğundan hiçbir
`conflict_id` açılmamıştır.

| conflict_id | Kaynak A | Kaynak B | Neden | Durum |
|---|---|---|---|---|
| — | — | — | Taranan tüm T1/T2 kaynaklar tutarlı | — |

**Ancak üç PROJE İÇİ DÜZELTME kayda geçirildi**
(`99-ops/_parts/celiskiler-gumruk-vergi-uzmani-tur3a.md`):

| Kod | Düzeltme |
|---|---|
| **D-1** | TUR 1.5'in *"böyle bir karar olsa duyulurdu, olasılık düşük"* değerlendirmesi **yanlış çıktı** — karar var. |
| **D-2** | `finans-fizibilite`'nin **%22,7** rakamı **tam kısıt** varsayımıdır, **fazla kötümser** → `T-171` |
| **D-3** | Ters modelin *"alt sınırla test EDİLMEMİŞTİR"* uyarı metni **artık yanlış** → `vergi.yaml` güncellendi |

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|---|---|---|---|---|---|
| `vergi.yaml` | `gozetim.uygulama_var_mi` | **false** *(önceki: null/UNKNOWN)* | bool | **FACT** | EV-2026-08-10-860 |
| `vergi.yaml` | `gozetim.birim_kiymet_esigi.status` | **N/A** *(önceki: UNKNOWN)* | — | N/A | EV-2026-08-10-860 |
| `vergi.yaml` | `gozetim.tps_belge_kodu` | "TPS-0964 — Gözetim Belgesi Sanayi" | — | FACT | EV-2026-08-10-860 |
| `vergi.yaml` | `gozetim.tetiklenirse` *(YENİ, kullanımda değil)* | parametrik şema | — | — | EV-…-852/-854 |
| `vergi.yaml` | `korunma_onlemi.uygulama_var_mi` *(YENİ)* | **false** | bool | FACT | EV-2026-08-10-861 |
| `vergi.yaml` | `dampinge_karsi_vergi.var_mi` *(YENİ)* | **false** | bool | FACT | EV-2026-08-10-862 |
| `vergi.yaml` | `kiymet_arastirmasi_riski.idarenin_yetkisi_var_mi` *(YENİ)* | **true** | bool | FACT | EV-2026-08-09-121 |
| `vergi.yaml` | `kiymet_arastirmasi_riski.modellendi_mi` *(YENİ)* | **false** | bool | UNKNOWN | — |
| `vergi.yaml` | `kdv…md36_indirim_kisiti.yururlukteki_karar.var_mi` *(YENİ)* | **true** (7846) | bool | FACT | EV-2026-08-10-852 |
| `vergi.yaml` | `kdv…md36_indirim_kisiti.alkole_ozgu_mu` *(YENİ)* | **false** | bool | FACT | EV-2026-08-10-852 |
| `vergi.yaml` | `kdv…md36_indirim_kisiti.baz_senaryoda_tetiklenir_mi` *(YENİ)* | **false** | bool | FACT | EV-…-860/-861/-862 |
| `vergi.yaml` | `kdv…alkole_ozgu_indirim_kisiti_var_mi` | **false (DEĞİŞMEDİ)** | bool | FACT | EV-2026-08-10-103 *(+855, 857, 859)* |
| `vergi.yaml` | `kdv…ithalat_kdv_indirilebilir_mi` | **true (DEĞİŞMEDİ)** | bool | FACT | EV-2026-08-10-101 |
| `vergi.yaml` | `kdv…ekonomik_kdv_maliyeti_try_per_sise` | **0,0 (DEĞİŞMEDİ)** | TRY/şişe | FACT | EV-2026-08-10-117 |
| `vergi.yaml` | `ters_model…gozetim_ters_model_mantigi.cikti_kurali` | **YENİ METİN** | — | — | EV-…-860/-861/-862 |

**Hiçbir oran, tutar veya matrah tanımı değişmemiştir.**
**`MAX_CIF_TRY` üzerindeki net etki: 0,00 TL/şişe.**
YAML parse doğrulaması yapılmıştır (17 top-level anahtar, `matrah_sirasi` 6 satır,
ÖTV 71,2692 ve KDV %20 bozulmamış).

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `kanal-marj-uzmani` | **"Her şey dahil" otel şarabın KDV'sini indiremez** (KDVGUT III/B-2.5.2) → o kanalın efektif maliyeti `fiyat × 1,20`. **Kaçış yolu:** tesis bedeli faturada ayrıştırırsa indirebilir. | HoReCa'nın ödeme istekliliği **vergi kaynaklı olarak** yapısal biçimde ayrışıyor; bu bir pazarlık farkı değil |
| `finans-fizibilite` | **%22,7 rakamı fazla kötümser** — 7846 kısmi kısıttır | `T-171` ile resmen bildirildi |
| `finans-fizibilite` + `navlun-lojistik-uzmani` | Gözetim tetiklenirse **Özel Amaçlı YMM Raporu** L5'te yeni bir gider satırı doğurur | Şu an tetiklenmiyor; senaryoda görünmeli |
| `global-sourcing-kasifi` | **Gözetim taze meyveye uygulanmış** (0810.10 çilek, 0810.50 kivi) → *"tarım ürününe gözetim gelmez"* varsayımı **yanlıştır** | Çok düşük FOB stratejisi bu riski senaryo olarak taşımalı |
| `yatirim-komitesi-baskani` | **Yöntem notu:** resmî PDF'lerde "metin var" ≠ "metin okunuyor". Bir GTİP'in listede "olmadığı" iddiası, **listenin kaç kayıt içerdiği** (pozitif kontrol) yazılmadan kabul edilmemeli | `EV-2026-08-09-125` tam olarak bu türden bir kayıttı |

Tamamı: `99-ops/_parts/capraz-ipuclari-gumruk-vergi-uzmani-tur3a.md`

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (özet) | impact | status |
|---|---|---|---|---|
| **T-947** | gumruk-vergi-uzmani | md.36 dayanaklı alkol KDV kısıtı var mı | CRITICAL | **ANSWERED** — (A) CONFIRMED, karar var ama tetiklenmiyor |
| **T-151** | gumruk-vergi-uzmani | KDVGUT III/C + md.36 kararları taranmadı | MEDIUM | **ANSWERED** — 4 boşluktan 3'ü kapandı, 4.'sü LOW |
| **T-171** | **finans-fizibilite** | Yeni koşullu kilit `md36_indirim_kisiti` + gözetim uyarı metni değişti + %22,7 düzeltmesi | **HIGH** | **OPEN** |
| **T-172** | gumruk-vergi-uzmani | Yıllık pakete girmemiş eski gözetim tebliği riski | MEDIUM | **OPEN** |
| **T-173** | gumruk-vergi-uzmani | Gözetim olmadan kıymet araştırmasına 7846 uygulanır mı | MEDIUM | **OPEN** |

**Conflict:** açılmadı (`C-171…C-189` bloğu kullanılmadı).

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| EV-2026-08-10-860 (gözetim) | **30d** | **2026-09-09** |
| EV-2026-08-10-861 (korunma) | 90d | 2026-11-08 |
| EV-2026-08-10-862 (damping) | 90d | 2026-11-08 |
| EV-2026-08-10-863 (ithalat tebliğleri) | 90d | 2026-11-08 |
| EV-2026-08-10-864 (erişim sınırı) | **7d** | **2026-08-17** |
| EV-2026-08-10-851 / -852 / -853 (kanun + CBK) | 180d | 2027-02-06 |
| EV-2026-08-10-854 / -855 / -858 / -859 (KDVGUT) | 90d | 2026-11-08 |
| EV-2026-08-10-856 (CBK/BKK sayımı) | 90d | 2026-11-08 |
| EV-2026-08-10-857 (özelge) | 180d | 2027-02-06 |

> ⚠ **Model hedef tarihlerinin üçü de 2027'dedir. Gözetim bulgusu hedef tarihte
> doğrulanmış DEĞİLDİR** — tıpkı ÖTV maktu tutarı ve gümrük vergisi oranı gibi.
> `ters-model-vergi-bacagi.md` §13.1'deki asimetri uyarısı listesine
> **gözetim de eklenmiştir.**

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**2204 (veya 2204.21 alt satırlarından biri) için yürürlükte, benim taramamın
dışında kalmış bir gözetim tebliği.**

Bu tek bulgu **iki dosyayı birden** çürütür:
- `gozetim-kiymet-kontrolu.md`: alt sınır doğar, `CIF_TRY_max` bir tabanla
  çakışabilir;
- `kdv-indirim-hakki-dogrulama.md`: 7846 **kendiliğinden** devreye girer,
  KDV **kısmen** ekonomik maliyet olur, YMM uyum yükü doğar.

**Bu ikisinin artık tek bir kırılma noktasını paylaşması, bu turun en önemli
yapısal çıktısıdır** — ve aynı zamanda en büyük tekil risktir.
Kapatma maliyeti **~0 TL, dakikalar** (`T-172`).

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"31/12/2025 yıllık paketi, yürürlükteki gözetim evrenini yeterince temsil
eder."** Bu bir **ESTIMATE**'tir, kanıt değildir. Paketin 11 eski tebliği
aynı anda değiştirmiş olması idarenin eskileri elden geçirdiğine *işaret eder*
ama **kanıtlamaz.**

İkinci kırılgan nokta: **`EV-2026-08-10-856` GİB'in kendi kürasyonuna dayanır.**
Tam sayımdır ama tek kaynaklıdır (`confidence: MEDIUM`).

### 9.3 Hangi kaynağıma en az güveniyorum?

**Kendi OCR'ıma.** 47 PDF, 126 sayfa görüntüsü + 87 gömülü tablo görüntüsü
işledim. OCR bir GTİP'i yanlış okuyabilir (ör. `2204` → `2704`). Riski
azaltmak için **üç yöntemin birleşimi** alındı ve **hiçbirinde** 22. fasıl
görünmedi; ayrıca "şarap/wine" kelime araması da negatif çıktı. Yine de
**%100 değildir** ve `T-172` bunu da kapsar.

İkincil: **`EV-2026-08-10-857`** bir **özelgedir** — yalnız talep edene özgüdür
(VUK md.413), genel düzenleyici işlem değildir. Destekleyicidir, taşıyıcı
değildir.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Senaryo | Etki | Karar |
|---|---|---|
| Gözetim **varsa** ve eşik `CIF_TRY_max`'ın **altındaysa** | Ek GV + kısmi KDV maliyeti + YMM yükü | Marjlar daralır, **`TEST` mümkün olabilir** |
| Gözetim **varsa** ve eşik `CIF_TRY_max`'ın **üstündeyse** | **Çözüm kümesi boşalır** — tedarikçi bedava verse bile beyan eşiğin altına inemez | **`KILL` / `HOLD`** |
| md.36 ile alkole özgü yeni bir karar çıkarsa | KDV tam ekonomik maliyet olur | Tüm tavanlar yeniden hesaplanır |
| Hiçbiri olmazsa (mevcut durum) | — | **Karar bu bulguyla değişmez** |

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| Ne | Kim | Nasıl | Süre | Maliyet |
|---|---|---|---|---|
| Gözetim kesinleştirme (`T-172`) | **insan operatör** | `uygulama.gtb.gov.tr/Tara` → 2204.21 sorgusu (CAPTCHA var, otomatize edilemez) | **dakikalar** | 0 TL |
| Aynısı, ikinci yol | gümrük müşaviri | *"2204.21'de gözetim belgesi aranıyor mu?"* | aynı gün | 0 TL |
| 7846 ↔ kıymet araştırması ilişkisi (`T-173`) | YMM | tek soru | aynı oturum | 0 TL |
| md.36 kararlarının ikinci kaynağı | — | `mevzuat.gov.tr` erişimi geri geldiğinde | — | 0 TL |
| Nihai doğrulama | — | **tek gerçekleşmiş ithalat beyannamesi** — bu raporu, `matrah-sirasi.md` §4'ü ve `X_pre = 0` varsayımını **aynı anda** test eder | ilk konteyner | pilot maliyeti |

---

## 10. DÖNÜŞ DEĞERİ ÖZETİ (başkan için tek tablo)

| Soru | Cevap |
|---|---|
| **KDV sonucu** | **(A) CONFIRMED** — indirim hakkı var, baz senaryoda kısıt yok |
| **Gerekçe farkı** | *"md.36 kararı yok"* **değil** → **"7846 var ama tetiklenmiyor"** |
| **`MAX_CIF_TRY` etkisi** | **0,00 TL/şişe** — yeniden hesap **gerekmez** |
| **Gözetim sonucu** | **NO APPLICABLE MEASURE** — pozitif kanıtla (305 GTİP, 22. fasıl yok) |
| **Alt sınır** | **YOK** — `gozetim_esigi` artık `UNKNOWN` değil `N/A` |
| **T-947** | **ANSWERED** |
| **T-151** | **ANSWERED** |
| **Yeni ticket** | `T-171` (HIGH, finans-fizibilite) · `T-172` (MEDIUM) · `T-173` (MEDIUM) |
| **Çelişki** | **YOK** |
| **Yeni kanıt** | **14** (`EV-2026-08-10-851 … -864`) |
| **En büyük tekil risk** | Şaraba gözetim gelmesi — **tek olayla üç etki** doğurur |
