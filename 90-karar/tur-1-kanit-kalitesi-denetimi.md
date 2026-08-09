# TUR 1 — KANIT KALİTESİ DENETİMİ

```yaml
belge:            tur-1-kanit-kalitesi-denetimi
denetleyen:       yatirim-komitesi-baskani
tarih:            2026-08-09
kapsam:           .claude/commands/tur-1-kesif.md §TUR SONU madde 4
karar_iceriyor_mu: false
```

> **BU BELGE BİR YATIRIM KARARI DEĞİLDİR.**
> `KILL` / `HOLD` / `TEST` / `IMPORT PILOT` / `SCALE` kararlarının hiçbiri bu
> belgede verilmemiştir ve verilemez. Nihai karar TUR 6'da,
> `90-karar/karar-gunlugu.md` dosyasında verilir. Bu belge yalnızca **kanıt
> kalitesi denetimi, çelişki çözümü ve gate durumu tespitidir.**

---

## 0. GENEL DEĞERLENDİRME

Beş ajanın TUR 1 çıktısı **kanıt disiplini açısından yüksek kalitelidir.**
142 kanıt kartının tamamının `10-evidence/raw/` altında karşılığı vardır
(eksik veya fazla kart **yoktur**); hiçbir ajan T5 kaynağı tek başına
vergi/mevzuat sonucu üretmek için kullanmamıştır; `80-model/engine/` altındaki
kodda hiçbir vergi oranı, ÖTV tutarı, KDV/KKDF oranı veya matrah tanımı
hard-code edilmemiştir (CLAUDE.md §12 **UYULMUŞTUR**); ve beş raporun beşinde de
zorunlu **"Bu bulguyu ne çürütür?"** bölümü mevcuttur.

Buna karşılık **beş yapısal ihlal/eksik** tespit edilmiştir; hiçbiri veri
uydurma niteliğinde değildir, tamamı **etiketleme, katman ve model girdisi
bütünlüğü** düzeyindedir. Bunlar §1–§3'te listelenmiş ve T-901…T-906 ile
ilgili ajanlara iade edilmiştir.

**Reddedilen bulgu sayısı: 0.** Hiçbir ajanın *bulgusu* reddedilmemiştir;
reddedilen şey **üç etiket** (bkz. §2.3, §2.4) ve **bir gate önerisinin
etiketi**dir (bkz. §5.1). Bulguların içeriğine dokunulmamıştır.

---

## 1. KANIT DİSİPLİNİ (CLAUDE.md §1, §2, §4)

### 1.1 "Bu bulguyu ne çürütür?" bölümü — TAM

| Rapor | Bölüm | Durum |
|---|---|---|
| `30-vergi-gumruk/rapor-tur1-gumruk-vergi.md` | §9 (9.1–9.5) | ✅ VAR |
| `20-mevzuat/rapor-tur1-mevzuat-ruhsat.md` | §9 (9.1–9.5) | ✅ VAR |
| `40-lojistik/rapor-tur1-navlun-lojistik.md` | §9 (9.1–9.5) | ✅ VAR |
| `50-sourcing/rapor-tur1-global-sourcing.md` | §9 (9.1–9.5) | ✅ VAR |
| `60-pazar/rapor-tur1-turkiye-pazar.md` | §9 (9.1–9.5) | ✅ VAR |
| `30-vergi-gumruk/matrah-sirasi.md` (ek) | §10 | ✅ VAR (zorunlu değildi) |

**Hiçbir rapor bu gerekçeyle geri gönderilmemiştir.**

Kalite notu: beş §9 bölümünün beşi de **gerçek** çürütme senaryosu üretmiştir,
tören amaçlı yazılmamıştır. Özellikle `global-sourcing-kasifi`'nin §9.2'de
**kendi arama yönteminin Model B lehine yanlı olduğunu** itiraf etmesi ve
`navlun-lojistik-uzmani`'nın "yön sağlam, büyüklük kırılgan" ayrımı, kırmızı
takıma hazır malzeme niteliğindedir.

### 1.2 T5'in tek başına vergi/mevzuat sonucu ürettiği yer — YOK

Programatik kontrol: `10-evidence/index.csv` içinde **`tier=T5` + `status=FACT`
olan hiçbir kart yoktur** (0 satır). `gumruk-vergi-uzmani` ve
`mevzuat-ruhsat-uzmani`'nın topladığı 61 kartın T3/T4/T5 olan **ikisi de**
(`EV-...-230`, `EV-...-231`) `status: UNKNOWN`'dır.

**CLAUDE.md §2 ihlali tespit edilmemiştir.**

İki yerde T1 belgeye erişilemediği için sonuç T2'den alınmış ve bu **açıkça
itiraf edilmiştir** — bu bir ihlal değil, doğru davranıştır:
- `EV-2026-08-09-118` (KDV %20): dayanak 7346 s. CBK'nın RG PDF'i taranmış
  görüntü; oran GİB konsolide metninden (T2) alınmış, rapor §9.3'te
  "T1 doğrulaması eksiktir" diye yazılmıştır.
- `EV-2026-08-09-111` (ÖTV 71,2692): T2 GİB listesi; dayanağı T1 ÖTVK md.12/3.
  Bkz. C-101 çözümü (§4.1).

### 1.3 `effective_date` eksikliği

38 kartta `effective_date` boş (`-` veya `UNKNOWN`). Bunların **büyük çoğunluğu
meşrudur**: ticari tarife, konteyner spesifikasyonu, tedarikçi site beyanı ve
türetme kartlarının yürürlük tarihi kavramı yoktur.

**Ancak bir gerçek ihlal vardır:**

| evidence_id | Sorun | Neden ihlal |
|---|---|---|
| `EV-2026-08-09-310` | **T2, `status: FACT`, mevzuat kanıtı** (Karayolları Trafik Yönetmeliği md.128, 44 ton) ama `effective_date: UNKNOWN` ve `publication_date: UNKNOWN` | CLAUDE.md §4: *"Vergi/mevzuatta **yürürlük tarihi (effective_date)** belirleyicidir."* Bu kart 40HC kapasite sonucunun **tek T2 dayanağıdır** ve `lojistik.yaml`'da `FACT (T2)` olarak durmaktadır. → **T-905** |

Ayrıca **iki tarih anomalisi**:

| evidence_id | Anomali |
|---|---|
| `EV-2026-08-09-509` | `publication_date: 2026-08-10` > `access_date: 2026-08-09` — **gelecek tarihli yayın** |
| `EV-2026-08-09-510` | Aynı |

Bu iki kart `EV-509`/`EV-510`, "400–800 TL bandında stokta ithal şarap yok"
bulgusunun **tek dayanağıdır** ve C-501'in de konusudur. Tarih tutarsızlığı
bulguyu çürütmez ama kaydın güvenilirliğini zayıflatır. → **T-903**

### 1.4 Hak edilmemiş `FACT` etiketleri

Üç kalem tespit edilmiştir. **Hiçbiri veri uydurma değildir; hepsi etiket
enflasyonudur.**

**(a) Türetme kartlarına T1 tier verilmesi — `mevzuat-ruhsat-uzmani`**

| evidence_id | tier | status | Kaynak alanının fiilî içeriği |
|---|---|---|---|
| `EV-2026-08-09-233` | **T1** | ESTIMATE | *"Türetme: EV-203/204/214/216 + **ASSUMPTION süreler**"* |
| `EV-2026-08-09-234` | **T1** | ESTIMATE | *"Türetme: EV-232 + EV-211"* |
| `EV-2026-08-09-235` | **T1** | ESTIMATE | *"Türetme: EV-213 (**T2**) + EV-209"* |

`EV-233` (T0 takvimi 120–270 gün) tier'ı **T1** olarak kayıtlıdır, oysa raporun
kendi ifadesiyle *"Bu sayının %30–50'si UNKNOWN'dan gelmektedir ve FACT
değildir."* Bir **ASSUMPTION karışımının tier'ı T1 olamaz.** `EV-235`'in
girdilerinden biri T2'dir; türetmenin tier'ı girdilerinin en zayıfından yüksek
olamaz.

**Etkisi sınırlıdır** çünkü `status` alanları doğru (`ESTIMATE`) ve
`confidence` alanları dürüst (`EV-233: LOW`). Yine de tier sütunu tek başına
okunduğunda yanıltıcıdır. → **T-904**

**(b) `tedarikci.yaml → ara_dogrulama` = 1.98 USD, `status: FACT`**

Kartın kendi notu: *"per: sise (750 ml **VARSAYILDI**)"*. Şişe hacmi
varsayılmışsa 750 ml başına değer bir `FACT` değil `ESTIMATE`'tir. → **T-902**

**(c) `vergi.yaml → urun_parametreleri.sise_hacmi_litre` = 0.75, `status: FACT`,
`evidence_id: null`**

Bu, **evidence_id'si olmayan tek dolu vergi girdisidir** ve ÖTV'yi doğrudan
çarpar (53,4519 = 0,75 × 71,2692). Kartın notu doğru bir şekilde "vergi kanıtı
değil, ürün tanımıdır" der — ama o zaman `status: FACT` değil, charter'a
dayanan bir tanım/`ASSUMPTION` olmalıdır. Bkz. §3.2. → **T-906**

### 1.5 `ESTIMATE` kartlarında türetme zinciri — UYULMUŞ

24 `ESTIMATE` kartının tamamında `source_name` alanı ya "Türetme: EV-…"
biçiminde girdi kartlarını gösteriyor ya da birincil kaynağı adlandırıyor.
Örnek kalite (kabul edilebilir üst sınır):
- `EV-2026-08-09-320` (20DV kapasitesi): türetme zinciri raporda **adım adım**
  yazılmış, çapraz kontrol yapılmış, bağlayıcı kısıt açıkça gösterilmiştir.
- `EV-2026-08-09-421` (FOB gösterge bandı): alt/üst sınırın **hangi kanıttan**
  geldiği ve **ne olmadığı** ayrı ayrı yazılmıştır.

### 1.6 `ASSUMPTION` kartlarında gerekçe — UYULMUŞ

`80-model/inputs/lojistik.yaml` içindeki iki `ASSUMPTION` alanının ikisinde de
gerekçe ve duyarlılık uyarısı vardır:
- `spec_40hc.dara_kg = 3900` → *"Kanıt BULUNAMADI… duyarlılık gerekli."*
- `karayolu_agirlik.cekici_sasi_darasi_kg = null` → *"KANIT YOK… KRİTİK
  duyarlılık (T-304)."*

`t0-takvimi.md`'de her adımın süresi `FACT`/`ESTIMATE`/`ASSUMPTION`/`UNKNOWN`
olarak ayrı ayrı etiketlenmiştir — bu, denetimde görülen **en iyi
etiketleme pratiğidir** ve diğer ajanlara örnek olarak gösterilir.

### 1.7 Alan dışı sonuç üretimi — TESPİT EDİLMEDİ

Beş ajanın hiçbiri başka bir ajanın alanında **sonuç** üretmemiştir. Aksine:
- `global-sourcing-kasifi` CIF'ten navlun düşüp FOB **hesaplamamıştır**
  ("alan dışı").
- `turkiye-pazar-kasifi` Metro 599,90 ile uzman perakende 875 TL arasındaki
  %46 farkı **hesaplamamış**, `kanal-marj-uzmani`'na bırakmıştır.
- `navlun-lojistik-uzmani` gümrük kıymeti hesabını **yapmamış**, T-303 ile
  devretmiştir.
- `mevzuat-ruhsat-uzmani` teminat konusunda *"negatif ispat yapılamaz"* diyerek
  FACT yazmamış, gümrük/antrepo teminatını alan dışı ilan etmiştir.

`mevzuat-ruhsat-uzmani`'nın **G0 önerisi** alan dışı değildir — CLAUDE.md ve
başkan görev tanımı G0 önerisini açıkça o ajana verir ve ajan *"Bu öneri bir
KARAR DEĞİLDİR"* notunu düşmüştür. Doğru davranış.

### 1.8 TTL / tazelik

Bugün (2026-08-09) itibarıyla **STALE kanıt yoktur.** Ancak takvim sıkıdır:

| Tarih | STALE olacak | Etki |
|---|---|---|
| **2026-08-23** | `EV-330`, `-331`, `-332`, `-333`, `-323` (navlun endeksleri, LCL/FCL kırılma) | Navlun bandının tamamı |
| **2026-09-08** | `EV-111` (**ÖTV 71,2692**), `-110`, `-125`, `-501`…`-504`, `-507`, `-509`…`-512` | **Projenin en kritik sayısı + tüm raf gözlemleri** |
| 2026-11-07 | `EV-223` (7584 s.K.), gümrük vergisi oranları, tedarikçi beyanları | Gate G0/G1 |

> **Başkan uyarısı:** TUR 3 (finans modeli) **2026-09-08'den sonra**
> çalıştırılacaksa `EV-2026-08-09-111` ve tüm raf gözlemleri
> `99-ops/veri-tazeligi.md` üzerinden yeniden doğrulanmadan model çıktısı
> `DRAFT`'tan yukarı çıkamaz.

---

## 2. KATMAN DİSİPLİNİ (CLAUDE.md §6)

### 2.1 Genel durum

Katman disiplini **genel olarak iyidir**. `tedarikci.yaml` dosyasının başında
*"EXW fiyatı L0, FOB fiyatı L1 katmanıdır. KARIŞTIRILMAZ"* kuralı yazılıdır;
`matrah-sirasi.md`'deki illüstratif tablo *"model çıktısı değildir"* uyarısıyla
çevrelenmiştir; `navlun-lojistik-uzmani` L1→L2 geçişinin bu turda **varsayımsal**
olduğunu açıkça ilan etmiştir.

### 2.2 `global-sourcing-kasifi` — Comtrade CIF birim değeri: **DOĞRU**

Soru: Comtrade birim değerleri L2 olarak mı kullanılmış?
**Cevap: EVET, doğru kullanılmıştır.**

- `tedarikci.yaml → katman_L2_turkiye_cif_USD_per_litre_2025` alanında uyarı:
  *"CIF (L2). FOB veya EXW YERİNE KULLANILAMAZ."*
- Rapor B-3'te: *"Bu **L2 (CIF)** katmanıdır… CIF'ten navlun ÇIKARILMAMIŞTIR
  çünkü navlun tutarı `navlun-lojistik-uzmani`'nın alanıdır."*
- Hacmi <100.000 litre olan menşeler (ZA/AU/AR/US) *"temsili değildir"* diye
  işaretlenmiş ve ülke elemesinde kullanılmamıştır.

Bu, denetimde görülen **en temiz katman uygulamasıdır.**

### 2.3 `global-sourcing-kasifi` — L1 etiketi: **REDDEDİLDİ (etiket)**

İki alanda L1 (FOB) etiketi **kanıtlanmamış bir katman iddiasıdır**:

**(a) `tedarikci.yaml → fob_gosterge_bandi.katman: L1`**

Bandın alt sınırı 0,56 EUR = OIV **dökme şarap sıvı maliyeti** — bu L1 değil,
L0'ın bile **altındadır** (kuru malzeme, şişeleme ve üretici marjı hariç).
Üst sınırı 1,85–2,40 USD = **L2 (CIF)**; alanın kendi içinde
`katman_uyarisi: "BU BIR L2 (CIF) SAYISIDIR"` yazmaktadır.

Yani `katman: L1` etiketi taşıyan bir bloğun **alt sınırı L0 altı, üst sınırı
L2**'dir. Üstelik alt sınır EUR, üst sınır USD'dir ve ajan (doğru olarak) ikisini
birleştirmemiştir — bu, bandın **aritmetik olarak da band olmadığı** anlamına gelir.

**(b) `tedarikci.yaml → katman_L1_ihracat_ort_EUR_per_litre`**

OIV ihracat birim değerlerine L1 (FOB) etiketi verilmiştir. **Bu etiket kendi
içindeki veriyle çelişmektedir:**

| Menşe | "L1" (EUR/litre) | L2 CIF (USD/litre) | Sonuç |
|---|---|---|---|
| İspanya | 2,87 | 2,71 | **L1 > L2** |
| Portekiz | 3,43 | 3,20 | **L1 > L2** |
| Fransa | 7,79 | 6,27 | **L1 > L2** |
| Şili | 2,68 | 2,89 | L1 ≈ L2 (navlun ≈ 0) |

**L1 tanım gereği L2'den küçüktür.** Üç menşede tersine dönmesi, iki serinin
aynı merdivenin basamakları **olmadığını** kanıtlar (farklı ürün karması,
farklı yıl, farklı para birimi, OIV tablosunda yuvarlama — ajan §9.3'te
`EV-404`'ün bu zaafını zaten itiraf etmiştir).

**BAŞKAN KARARI:** Her iki alanın `katman` etiketi **geçersizdir**. Bulguların
kendisi (sayılar, kaynaklar, uyarılar) **geçerlidir ve değiştirilmemiştir** —
reddedilen yalnızca katman etiketidir. `finans-fizibilite` bu iki alanı
**hiçbir koşulda L1/FOB girdisi olarak okuyamaz.** → **T-902**

Hafifletici not: `kullanim_kurali: SENSITIVITY_BOUNDS_ONLY` alanı ve
`exw_per_sise`/`fob_per_sise` alanlarının `null` bırakılması sayesinde bu etiket
hatası **modele fiyat olarak sızmamıştır.** İhlal potansiyeldir, gerçekleşmemiştir.

### 2.4 `turkiye-pazar-kasifi` — `L8_METRO_CASH_CARRY`: **MEŞRU, ONAYLANDI**

Soru: Bu ayrım meşru mu, yoksa L7/L8 karışıklığını mı gizliyor?
**Cevap: Meşrudur ve karışıklığı gizlemiyor — tam tersine, ifşa ediyor.**

Gerekçe:
1. Metro cash & carry'de **tek fiyat** vardır ve aynı rakam bireysel tüketici
   için L8, bakkal/HoReCa için fiilen bir satın alma maliyetidir. Bu ikiliği
   L7 veya L8'e **zorlamak** bilgi kaybı olurdu.
2. Ajan `L8_CHAIN_RETAIL` alanını **ayrı ve `UNKNOWN`** bırakmış, ikisinin
   eşitlenmemesini açıkça talep etmiştir (`oq-001-benchmark-dogrulama.md` §8).
3. Sapmanın **yönü** de yazılmıştır: cash & carry formatı yapısı gereği zincir
   perakendeden ucuzdur → gerçek zincir L8'i 599,90'ın **üstünde** olma
   eğilimindedir → hata **proje lehine değil, muhafazakâr yöndedir.**

**BAŞKAN KARARI — katman taksonomisi (bu benim yetkimdedir, CLAUDE.md §6):**

`L8_METRO_CASH_CARRY`, gözlenmiş ayrı bir katman olarak **onaylanmıştır**, şu
üç bağlayıcı kuralla:

| # | Kural |
|---|---|
| K1 | `L8_METRO_CASH_CARRY` **≠** `L8_CHAIN_RETAIL`. İkisi hiçbir hesapta birbirinin yerine geçemez. |
| K2 | `L8_METRO_CASH_CARRY` **L7 olarak da kullanılamaz.** Gerçek L7, ithalatçı→perakendeci pazarlığından doğar; Metro rafından okunan bir sayı L7 proxy'si olarak modele giremez. `kanal-marj-uzmani` L7'yi kendi kanıtıyla kuracaktır. |
| K3 | Ters model (`target shelf price → max EXW/FOB`) hedefini `L8_METRO_CASH_CARRY`'ye kurarsa, bunun **daha agresif** bir hedef olduğu çıktıda açıkça yazılır. |

### 2.5 `mevzuat-ruhsat-uzmani` — bandrol katmanı: **ÇÖZÜLMEMİŞ**

Rapor bandrolü (2,36073 TL/şişe) ve hizmet bedelini (0,1587 TL/şişe)
**L5 (importer cost)** olarak etiketlemiştir. Ancak:

- Bandrol, ithal üründe **zorunlu olarak ANTREPODA**, yani **serbest dolaşıma
  giriş beyannamesinin tescilinden ÖNCE** uygulanır (`EV-2026-08-09-212`).
- `matrah-sirasi.md` §4: ÖTV matrahı *"tescile kadar yapılan diğer gider ve
  ödemeler"i* içerir; KDV matrahı da öyle.

Yani bandrol bedeli **L3'te (pre-tax landed) doğuyor ve vergilendirilebilir**
olabilir; L5'te değil. Fark küçüktür (≈2,52 TL × 1,20 ≈ 0,50 TL/şişe ek yük)
ama **katman kuralı ihlalidir** ve `T-203` bu soruyu zaten sormaktadır.

Ayrıca `80-model/inputs/ruhsat.yaml` dosyasında **hiçbir maliyet kaleminde
`katman` alanı yoktur** — katman bilgisi yalnızca rapor metninde yaşamaktadır.
`lojistik.yaml`'da da masraf kalemlerinin katmanı etiketlenmemiştir.
→ **T-904**

### 2.6 Bir katmanın diğerinin yerine kullanıldığı yer — TESPİT EDİLMEDİ

`matrah-sirasi.md`'nin illüstratif CIF=100 TL tablosu, `konteyner-kapasitesi`
türetmeleri ve `oq-001` katman analizi dahil, **bir katmanın sayısını başka bir
katmanın yerine koyan bir hesap bulunamamıştır.** Tespit edilen sorunlar
(§2.3, §2.5) **etiket** düzeyindedir, ikame düzeyinde değildir.

---

## 3. MODEL GİRDİLERİ (CLAUDE.md §12)

### 3.1 Güvenlik kilidi — UYULMUŞ

`80-model/engine/*.py` (955 satır) programatik olarak tarandı:

| Aranan | Bulunan |
|---|---|
| Vergi oranı literal (`0.20`, `0.06`, `70`, `50`) | **YOK** |
| ÖTV tutarı (`71.2692`, `53.4519`) | **YOK** |
| GTİP (`2204`) | **YOK** |
| Matrah tanımı hard-code | **YOK** |

**CLAUDE.md §12 ihlali yoktur.** Kod girdileri YAML'dan okumaktadır.

### 3.2 evidence_id'si olmayan dolu sayı

Sekiz YAML dosyası programatik olarak tarandı (`value` dolu + `evidence_id`
boş/null olan yapraklar):

| Dosya | Alan | Değer | status | Değerlendirme |
|---|---|---|---|---|
| `vergi.yaml` | `urun_parametreleri.sise_hacmi_litre` | **0.75** | **FACT** | ⚠️ **İHLAL** — ÖTV'yi doğrudan çarpar; `FACT` + `evidence_id: null` olamaz → **T-906** |
| `lojistik.yaml` | `urun_fizik.sise_hacmi_ml` | 750 | FACT | ⚠️ Aynı sorun, aynı sayı (charter tanımı) → T-906 kapsamında |
| `lojistik.yaml` | `konteyner.spec_40hc.dara_kg` | 3900 | **ASSUMPTION** | ✅ Kabul — gerekçe + duyarlılık uyarısı mevcut (CLAUDE.md §1.3) |
| `tedarikci.yaml` | `fiyat.quote_type` | `NONE_YET` | FACT | ✅ Kabul — sayı değil, durum bildirimi |
| `tedarikci.yaml` | `risk.alternatif_tedarikci_sayisi` | **0** | FACT | ✅ Kabul — "hiç teklif alınmadı" ifadesinin sayısal karşılığı; kanıtı yokluğun kendisidir |
| `urun.yaml` | `urun.tip`, `urun.hacim_ml` | — | ASSUMPTION | ✅ Kabul — doğru etiketlenmiş |
| `makro.yaml`, `kanal.yaml`, `senaryolar.yaml` | — | — | — | ✅ Tamamen `null`/`UNKNOWN` |

**Sonuç: 1 gerçek ihlal (0,75 litre / 750 ml, iki dosyada aynı sayı).**
Kendim düzeltmedim; `gumruk-vergi-uzmani`'na T-906 ile iade edildi.

### 3.3 Eksik girdiler `null` + `UNKNOWN` mu?

**Evet.** Denetlenen kritik alanların tamamı doğru bırakılmıştır:

```
vergi.yaml     : meta.model_hedef_tarihi = null / UNKNOWN
                 matrah_sirasi[KKDF].matrah_tanimi = null
                 gozetim.uygulama_var_mi = null / UNKNOWN
                 tercihli_tarife.mense_ispat_belgesi = null / UNKNOWN
                 kdv_perspektifleri.a.ithalat_kdv_indirilebilir_mi = null / UNKNOWN
                 antrepo_rejimi.kismi_cekis_mumkun_mu = null / UNKNOWN
lojistik.yaml  : navlun.ocean_freight_per_konteyner = null / UNKNOWN
                 sure.toplam_lead_time_gun = null / UNKNOWN
tedarikci.yaml : fiyat.exw_per_sise = null / UNKNOWN
                 fiyat.fob_per_sise = null / UNKNOWN
ruhsat.yaml    : dagitim_yetki_belgesi.basvuru_suresi_gun = null / UNKNOWN
makro.yaml     : TÜM alanlar null / UNKNOWN
kanal.yaml     : TÜM alanlar null / UNKNOWN (TUR 2 bekliyor)
```

### 3.4 İki yapısal model girdisi sorunu

**(a) `80-model/inputs/pazar.yaml` DOSYASI YOKTUR.**

`turkiye-pazar-kasifi` raporunun §5 "Model Girdileri" tablosu 14 satırın
tamamını `pazar.yaml` dosyasına yazdığını beyan etmektedir (benchmark 599,90 TL,
`KDV_DAHIL`, `L8_METRO_CASH_CARRY`, segment 600–900 TL, 875 TL, 25 yerli SKU…).
**Bu dosya `80-model/inputs/` altında mevcut değildir.** Üç ticket (`T-501`,
`T-504`, `T-505`) da bu dosyaya atıf yapmaktadır.

Sonuç: **TUR 1'in tek gerçek pazar verisi hiçbir model girdi dosyasında
yaşamamaktadır.** `urun.yaml → segment.*` alanları hâlâ TUR 0 iskeleti olarak
`null`'dur. → **T-903**

**(b) `senaryolar.yaml` TUR 1 önerileriyle güncellenmemiştir.**

`turkiye-pazar-kasifi` BM_C (promosyon) ve BM_D (zincir L8 farkı) senaryolarının
eklenmesini **önermiştir**; `senaryolar.yaml` hâlâ yalnızca BM_A/BM_B
içermektedir ve ikisi de `status: ASSUMPTION` ile **eşit** ağırlıktadır.
Senaryo setini onaylamak başkana aittir; **bu denetim kapsamında
onaylanmamıştır** (karar niteliği taşır, TUR 2/3'e bırakılmıştır). Kayıt
altına alınmıştır ki unutulmasın.

**(c) `hesap_sozlesmesi` içinde sayı tekrarı — düşük öncelikli risk**

`vergi.yaml → hesap_sozlesmesi.adimlar` metin bloğu içinde `71.2692` ve `0.20`
literal olarak **tekrar** yazılmıştır. Bu metin bir sözleşme açıklamasıdır, kod
değildir ve §12'yi ihlal etmez; ancak ÖTV tutarı Ocak 2027'de değiştiğinde
**iki yerde** güncellenmesi gerekecektir → desenkronizasyon riski. → T-906

---

## 4. ÇELİŞKİLER — BAŞKAN ÇÖZÜMÜ

14 açık çelişkiden **8'i kapatıldı** (7 `RESOLVED`, 1 `UNRESOLVABLE`),
**6'sı `OPEN` kaldı.** Tam gerekçeler `99-ops/celiskiler.md` → *TUR 1 SONU —
BAŞKAN ÇÖZÜM KAYITLARI* bölümündedir.

### 4.1 C-101 — ÖTV 61,3914 vs 71,2692 TL/lt → **ÇÖZÜLDÜ: 71,2692 ONAYLANDI**

`gumruk-vergi-uzmani`'nın çözüm önerisi **onaylanmıştır.** Gerekçe (çözüm
hiyerarşisi sırasıyla):

1. **Tier (kural 1) tek başına yeterli değildir.** Naif okuma T1 (mevzuat.gov.tr,
   61,3914) lehinedir. Ancak çelişen şey iki *iddia* değil, aynı hükmün
   **iki farklı zamandaki hâlidir**. `celiski_turu: TARIH`.
2. **Yürürlük tarihi (kural 2) belirleyicidir.** ÖTVK md.12/3 (T1,
   `EV-...-114`) tutarların Ocak/Temmuz'da *"yeniden belirlenmiş sayılır"*
   demektedir — ayrı bir CBK gerekmez, dolayısıyla konsolide kanun metnine
   **işlenmez**. GİB listesi (T2) bu otomatik mekanizmanın **yayımıdır**,
   ayrı bir iddia değildir; başlığı yürürlüğü (3/7/2026) açıkça yazar.
3. Askıya alma kontrolü: CBK 10799 md.12/3'ü yalnız **2026 Ocak–Haziran**,
   CBK 11489 yalnız **(B) cetveli (tütün)** için askıya almıştır. Şarap
   ((III)/A) askı kapsamı **dışındadır**.
4. **Model hedef tarihi (kural 3):** `t0-takvimi.md`'ye göre ilk konteynerin
   izinlerinin tamamlanması **2026-12 → 2027-05** bandındadır — yani her hâlükârda
   3/7/2026'dan **sonrası**. 61,3914 hiçbir senaryoda geçerli değildir.

**Karar:** Model **71,2692 TL/litre** (`EV-2026-08-09-111`) kullanır.
`EV-2026-08-09-112` `SUPERSEDED` olarak kalır.

**İki bağlayıcı koşul:**
- **K1:** Bu değer modele **sabit sayı olarak giremez.** Model hedef tarihi
  2027-01-01 veya sonrasıysa ÖTV **Yİ-ÜFE'ye endeksli bir değişken** olarak
  modellenir. `T-104` (**CRITICAL**) bu nedenle **açık kalır**; C-101'in
  çözülmesi T-104'ü kapatmaz.
- **K2:** Çözümün en zayıf halkası — %16,09 artışın TÜİK Yİ-ÜFE'den
  **bağımsız doğrulanmamış** olması — **T-901** ile takip edilir. Bu kapanmadan
  `EV-111` "iki GİB listesi arasındaki oran" dayanağını aşamaz.

### 4.2 C-502 — Metro'nun KDV dili → **ÇÖZÜLDÜ: gerçek çelişki DEĞİL**

`turkiye-pazar-kasifi`'nın değerlendirmesine **katılıyorum.** Çözüm hiyerarşisi
kural 4 (kapsam uyumu) uygulanır: iki kaynak **aynı şey hakkında konuşmuyor.**
- Kaynak A (broşür, `KDV'li`) = **müşteriye ilan edilen raf fiyatı** → brüt.
- Kaynak B (kampanya koşulları, "alım hedeflerinize KDV dahil değildir") =
  **ciro/hedef muhasebesi** → net.

Aynı şirketin iki farklı matrahı iki farklı amaç için kullanması çelişki değil,
**kapsam farkıdır** (`celiski_turu: KAPSAM`). `durum: RESOLVED`.

**Bağlayıcı sınır:** Bu çözüm **OQ-001'i kapatmaz** ve G3'ü açmaz. C-502'nin
çözülmesi yalnızca "Metro kendi içinde tutarsız" itirazını ortadan kaldırır;
**şarap reyonundaki fiziksel etiketin** de `KDV'li` yazdığı hâlâ
**görülmemiştir** (`T-501`, `T-504` açık).

### 4.3 Çözülen diğer çelişkiler

| id | Karar | Gerekçe (özet) |
|---|---|---|
| **C-302** | **RESOLVED** | Kural 1: T3 (Maersk servis tarifesi) + T4 > T5. Kaynak B (`EV-333`) **kendi içinde tutarsızdır** (LA→İstanbul 15 gün fiziksel olarak imkânsız) → kaynak **bütünüyle diskalifiye**. Akdeniz 7–10 gün geçerli. Geriye kalan (California rotası) bir *çelişki değil*, `UNKNOWN`'dır → `T-304`. |
| **C-303** | **RESOLVED** | Kural 1: T3 (Maersk, 28.300 kg) > T4 (28.200) > T5 (26.000, kanıt kartı bile açılmamış). Etkisi sıfırdır: 20DV'de bağlayıcı kısıt zaten **hacimdir**. |
| **C-401** | **RESOLVED** | Kural 1: T5 agregatör iddiası (300–1.200 şişe, `EV-424`) CLAUDE.md §2 uyarınca **tek başına sonuç üretemez** → elenir. Geriye kalan 3.000 / 3.600 / 1 konteyner farkı **çelişki değil, tedarikçi sınıfı farkıdır** (kural 4, `KAPSAM`) ve zaten B-2'de FACT olarak kayıtlıdır. Gerçek boşluk `UNKNOWN`'dır (OQ-402), çelişki değil. **Model her iki MOQ yapısını ayrı senaryo olarak çalıştırır.** |
| **C-402** | **RESOLVED** | Kural 5 (katman) + kural 4 (kapsam): Kaynak A bir **L8 raf gözlemi/tek SKU**, Kaynak B bir **L2 yıllık ortalama/tüm ABD menşei**. Farklı katman + farklı popülasyon = **sahte çelişki**. 18.298 litrelik bir toplamda ortalama birkaç premium partiyle kolayca yukarı çekilir. **Bağlayıcı kural:** Comtrade ABD ortalaması benchmark ürünün maliyet proxy'si olarak **kullanılamaz**. Benchmark'ın gerçek menşe/rota sorusu `T-405` ile `UNKNOWN` olarak devam eder. |
| **C-503** | **RESOLVED** | Kural 1 + kural 2: Kaynak A T5, üç site aynı tabloyu kopyalamış, tarih Ocak 2026 (bayat). `EV-512` zaten `UNKNOWN` + "MODELE GİREMEZ" ile işaretlenmiştir. T5 bir kaynak T4 gözlemle çelişki oluşturamaz → kayıt kapanır. **Bu, `EV-510`'u doğrulamaz.** |
| **C-403** | **UNRESOLVABLE** | Her iki kaynak da **T5**. Kural 1–3 uygulanamaz; kural 7 devreye girer: değer `UNKNOWN` kalır, **modele girmez**, `T-405` ile takip edilir. impact LOW olduğu için karara taşınmaz. |

### 4.4 Açık kalan çelişkiler ve neden çözemediğim

| id | impact | Neden çözemedim |
|---|---|---|
| **C-201** | **CRITICAL** | T1 ↔ T1, aynı kanun, aynı tarih, ikisi de yürürlükte. Lafzî yorum ile kanunun sistematiği çatışıyor. Tier/tarih/kapsam/katman kurallarının **hiçbiri** uygulanamıyor. Bu bir **hukuki yorum** sorunudur; başkanın kendi yorumuyla çözmesi CLAUDE.md §1.16'nın ihlali olur. → `T-201` dış hukuki görüş/TADAB yazısı ile kapanır. **G0'ı doğrudan belirler.** |
| **C-202** | HIGH | T1 ↔ T1, aynı yönetmelik, iki madde. Sıralama sorunu; `celiski_turu` `TANIM` olarak yeniden sınıflandırıldı. `t0-takvimi.md` A7→A8 sırası **`ASSUMPTION` olarak açıkça etiketlenmiştir** — bu doğru davranıştır. → `T-202`. |
| **C-203** | **CRITICAL** | T1 ↔ T1, kanun **9 haftalıktır**, ikincil düzenleme yoktur. Çözmek için henüz var olmayan bir metni okumak gerekir. → `T-205`. **TUR 2'nin en büyük engeli.** |
| **C-204** | LOW | Mülga dayanaklı tebliğin yürürlük durumu bir **mevzuat yorumu**dur; `mevzuat-ruhsat-uzmani`'nın alanıdır. Kendi yorumumu koyamam. **Ticket açılmadı** (etki düşük); TUR 5'te `mevzuat-ruhsat-uzmani`'na havale edilmiştir. |
| **C-301** | MEDIUM | T4 ↔ T4, aynı firmanın iki yayını. Kural 2 (daha güncel) uygulanabilirdi (2025 > 2022) — **uygulamadım**, çünkü daha güncel olanı seçmek kapasite bandını %11 daraltır ve modeli **gerekçesiz iyimser** yapar. Farkın kaynağı büyük olasılıkla palet standardı tanımıdır (`TANIM`), değer hatası değil. **Başkan direktifi: 9–11 / 20–24 bandı korunur, tek değer seçilmesi YASAKTIR.** → `T-304` (stowage planı). |
| **C-501** | HIGH | T4 ↔ T4, **aynı feed**, aynı erişim tarihi. Tier/tarih ayrımı yok. Yalnızca fiziksel gözlemle kapanır (`OQ-502`). **G3'ü kısmen bloke eder** çünkü "400–800 TL'de ithal şarap yok" bulgusunun tek dayanağı `available: true` filtresidir. |

---

## 5. GATE DURUMU

### 5.0 Gate tanımları

`.claude/agents/yatirim-komitesi-baskani.md` G0–G5'i tanımlar. Lojistik/landed
cost için ayrı bir gate tanımlı **değildir**; bu denetim için **G2-L** alt
gate'ini açıkça tanımlıyorum. Kullanılan tanımlar:

| Gate | Soru | Sahibi |
|---|---|---|
| **G0** | Bu iş Türkiye'de yasal olarak kurulabilir mi? | `mevzuat-ruhsat-uzmani` önerir → **başkan karar verir** |
| **G1** | Vergi yükü kanıtlı ve satır satır hesaplanabilir mi? | `gumruk-vergi-uzmani` |
| **G2** | Gerçek, ulaşılabilir tedarik kaynağı ve fiyatı var mı? | `global-sourcing-kasifi` |
| **G2-L** *(bu denetimde tanımlandı)* | L1→L2→L3 geçişi kanıtla kurulabiliyor mu (navlun, lead time, landed cost)? | `navlun-lojistik-uzmani` |
| **G3** | Benchmark doğrulandı mı, segment gerçek mi? | `turkiye-pazar-kasifi` |
| **G4** | Model kanıtlı girdilerle pozitif contribution veriyor mu? | `finans-fizibilite` |
| **G5** | Kırmızı takımın CRITICAL ticket'ları kapandı mı? | `seytanin-avukati` |

**Gate kuralı:** Kapsamında `impact: CRITICAL` açık ticket veya çözülmemiş
CRITICAL çelişki bulunan bir gate `PASS` alamaz.

### 5.1 G0 — YASAL YOL: **BLOCKED (koşullu, kaldırılabilir)**

`mevzuat-ruhsat-uzmani` **`G0 PASS (koşullu)`** önermiştir.

**Bulguları kabul ediyorum, etiketi reddediyorum.**

Kabul edilen: (a) İncelenen T1/T2 mevzuatta şarap ithalatçısı olmayı yasaklayan
hüküm **yoktur**; (b) gerekli belgelerin tamamı tanımlıdır ve 2026 bedelleri
Resmî Gazete ile bilinmektedir; (c) depo zorunluluğu "akde bağlanmış dağıtım
ağı kullanıcısı" ile karşılanabilir; (d) `G0 FAIL` için dayanak yoktur.
Bu dört tespitin hiçbiri değiştirilmemiştir.

Reddedilen: **`PASS` etiketi.** Gerekçe:
- `T-201` (**CRITICAL, OPEN**) ve `C-201` (**CRITICAL, OPEN**) doğrudan G0'ın
  sorusunu hedefler: 4250 s.K. m.1/3'teki 1.000.000 litre/yıl eşiği durgun şarap
  ithalatına uygulanıyorsa, **projenin beş hacim senaryosunun tamamı**
  (3.750–75.000 litre) eşiğin çok altındadır. Ajanın kendi ifadesiyle bu durumda
  öneri *"`G0 PASS`'ten `G0 BLOCKED`'a döner"*.
- Kapsamında çözülmemiş **CRITICAL** bir çelişki bulunan gate `PASS` alamaz.
  "Koşullu PASS" downstream ajanlar tarafından yeşil ışık olarak okunur; bu
  nedenle etiket **BLOCKED** olmalıdır.

**Bu bir `FAIL` DEĞİLDİR ve kalıcı değildir.** G0, `T-201` olumsuz olmayan bir
cevapla kapandığı anda **`PASS`'e döner** — ek araştırma turu gerekmez.

| G0'ı açan koşul | Sahibi | Süre |
|---|---|---|
| `T-201` — TADAB yazılı görüşü veya alkol mevzuatında uzman hukuk bürosu mütalaası | Yatırımcı (dış temas) | 2–6 hafta |
| `T-202` — dağıtım yetki belgesi fiilî süresi <6 ay teyidi | Yatırımcı / danışman | 1–2 hafta |

> **En hızlı yol** `mevzuat-ruhsat-uzmani`'nın kendi önerisidir: sektörde faal
> **küçük ölçekli bir şarap ithalatçısıyla 1 saatlik görüşme** — T-201, T-202,
> T-204, T-206'nın dördünü birden aydınlatır. Böyle bir firmanın **varlığı**
> bile C-201'i pratikte çürütür.

### 5.2 G1 — VERGİ YAPISI: **BLOCKED (dar kapsamlı, PASS'e en yakın gate)**

**Kanıt kalitesi bu turun en yükseğidir.** Matrah zinciri T1 hükümleriyle
kurulmuş, sıra açık yazılmış, her adımın evidence_id'si vardır; ÖTV'nin fiilen
maktu olduğu ve fiyat/performans segmentini orantısız cezalandırdığı tespiti
projenin en değerli tek bulgusudur.

`PASS` verilmemesinin nedeni yapı değil, **üç CRITICAL boşluktur**:

| # | Boşluk | Etki |
|---|---|---|
| 1 | **İthalatta ödenen KDV indirilebilir mi?** (`UNKNOWN`) | Şişe başına ≈40–45 TL'nin ekonomik maliyet olup olmadığını belirler. Tek başına marj eşiğini kırabilir. |
| 2 | **Model hedef tarihinde geçerli ÖTV tutarı** (`T-104` CRITICAL, `OQ-002`) | `model_hedef_tarihi = null`. Takvim 2027'ye taşarsa bugünkü 71,2692 geçersizdir (+%16 mertebesinde). |
| 3 | **Gözetim / referans kıymet** (`UNKNOWN`, negatif arama) | Varsa düşük CIF beyanı stratejisi çöker. Ajan bunu doğru şekilde "yokluğun kanıtı değildir" diye bırakmıştır. |

Ayrıca `KKDF matrahı` (`T-105`) ve `menşe ispat belgesi türü` `UNKNOWN`'dır;
ikisi de **peşin ödeme + tek menşe** baz senaryosunda etkisizdir.

> **Not:** G1'in üç boşluğunun ikisi bir **YMM/gümrük müşaviri oturumuyla
> 1 haftada** kapanabilir. Bu gate mesafe olarak PASS'e en yakın olanıdır.

### 5.3 G2 — TEDARİK: **BLOCKED**

Bu gate'in sorusu "aday var mı?" değil, **"gerçek, ulaşılabilir tedarik kaynağı
ve fiyatı var mı?"**dır.

| Kanıt | Durum |
|---|---|
| Alınan teklif sayısı | **0** (`uretici_ile_iletisim: NONE`) |
| `exw_per_sise` / `fob_per_sise` | **null / UNKNOWN** |
| `alternatif_tedarikci_sayisi` | **0** |
| Doğrulanmış üretici (site erişimi düzeyinde) | 11 |

Ajanın kendi ifadesi bağlayıcıdır: *"11 aday ile 11 alternatif tedarikçi aynı
şey değildir."* Bu turda bunun aksi **iddia edilmemiştir** — bu doğru
davranıştır ve gate'in BLOCKED olması bir başarısızlık değil, tasarımın
sonucudur (bu tur bir **haritalama** turuydu).

Ek yapısal sorun: **iki iş modeli eşit derinlikte araştırılamamıştır**
(10 private label adayı / 1 Model A adayı). Ajan bunun bir kanıt farkı değil,
**arama yöntemi yanlılığı** olduğunu itiraf etmiştir. Kararın Model B'ye
**kanıtla değil yöntemle** kayması riski → **OQ-902** açıldı.

### 5.4 G2-L — LOJİSTİK / LANDED COST: **BLOCKED**

| Kanıt | Durum |
|---|---|
| Rota bazlı doğrulanmış FCL navlunu | **HİÇBİR ROTA İÇİN YOK** (`T-304` CRITICAL) |
| California → İstanbul (benchmark rotası) navlun + transit | **UNKNOWN** |
| `navlun.ocean_freight_per_konteyner` | **null** |
| `sure.toplam_lead_time_gun` | **null** |
| Tedarikçiden alınmış koli/palet spec | **YOK** (türetilmiş, `T-302`) |

**L1 → L2 geçişi bu turda kurulamamıştır.** Bu, ters modelin (target shelf
price → max FOB) çıktısını doğrudan belirsizleştirir.

Buna karşılık gate'in **BLOCKED olması bu ajanın kalitesizliğinden
kaynaklanmıyor**: konteyner kapasitesi ilk ilkelerden, her adım gösterilerek
türetilmiş; "20DV hacim kısıtlı / 40HC ağırlık kısıtlı" ve "bekleme limanda
değil antrepoda" bulguları **girdi hatalarına dayanıklı** (büyüklük mertebesi)
sonuçlardır. Eksik olan şey masabaşında üretilemeyecek olan **gerçek
kotasyondur**.

### 5.5 G3 — PAZAR / BENCHMARK: **BLOCKED**

Başkan kuralı açıktır: **OPEN QUESTION #001 kapanmadan G3 geçilemez.**
OQ-001 `PARTIALLY_RESOLVED`'dır.

| OQ-001 ayağı | Durum |
|---|---|
| KDV dahil mi? | ✅ **KAPANDI** — KDV DAHİL (yüksek güven, 4 kanıt) |
| Tüketiciye açık mı / cash&carry mi? | ✅ KAPANDI — ikisi de |
| Etikette çiftli KDV gösterimi var mı? | ✅ KAPANDI — **YOK**; ikinci sayı birim fiyattır (kurucu hipotez çürüdü) |
| **Promosyonlu mu, normal fiyat mı?** | ❌ **UNKNOWN** — `T-504` (**CRITICAL, OPEN**) |
| **Zincir market gerçek L8'i** | ❌ **UNKNOWN** — `OQ-502` |
| **Şarap reyonundaki fiziksel etiket** | ❌ **GÖRÜLMEDİ** — tüm KDV sonucu broşürden rafa yapılmış bir **çıkarımdır** |

Ek olarak `Türkiye şarap ithalat hacmi` **UNKNOWN**'dır (`EV-515`) — bu, pazar
büyüklüğü ve `SCALE` hedefinin doğrulanamaması demektir. C-501 (HIGH) da açıktır.

**Kaydedilmesi gereken olumlu bulgu:** OQ-001'in ilerlemesi gerçek ve
değerlidir; ayrıca "600–800 TL bandında rakip **ithal değil yerli**" bulgusu
projenin rekabet varsayımını değiştiren birinci sınıf bir tespittir.
Gate'in BLOCKED olması bunu geçersiz kılmaz.

### 5.6 G4 — EKONOMİ: **NOT_EVALUATED**

TUR 3 çalıştırılmamıştır ve **çalıştırılamaz**: fiyat girdisi (`exw/fob`)
`null`, navlun `null`, lead time `null`, `model_hedef_tarihi` `null`.
CLAUDE.md §1.15 uyarınca model bu girdilerle **`UNKNOWN` dönmek zorundadır**.

Ayrıca: **6 adet `impact: CRITICAL` açık ticket** vardır (T-104, T-201, T-205,
T-301, T-304, T-504). CLAUDE.md §5 uyarınca bunlar açıkken finans modeli çıktısı
`APPROVED` olamaz — en fazla `DRAFT`.

### 5.7 G5 — RİSK: **NOT_EVALUATED**

TUR 4 (`seytanin-avukati`) çalıştırılmamıştır.

### 5.8 Gate özeti

| Gate | Durum | Açan tek koşul |
|---|---|---|
| **G0** Yasal yol | **BLOCKED** (koşullu, kaldırılabilir) | `T-201` |
| **G1** Vergi yapısı | **BLOCKED** (dar kapsamlı) | KDV indirilebilirliği + `model_hedef_tarihi` + `T-104` |
| **G2** Tedarik | **BLOCKED** | Gerçek RFQ cevabı (≥5 tedarikçi) |
| **G2-L** Lojistik/landed | **BLOCKED** | 3 forwarder'dan yazılı kotasyon (`T-304`) |
| **G3** Pazar | **BLOCKED** | OQ-001'in promosyon ayağı (`T-504`) + fiziksel raf etiketi |
| **G4** Ekonomi | **NOT_EVALUATED** | G1+G2+G2-L+G3 |
| **G5** Risk | **NOT_EVALUATED** | TUR 4 |

**Hiçbir gate PASS almamıştır. Bu, TUR 1 sonunda beklenen ve sağlıklı bir
durumdur** — TUR 1 bir keşif turudur, doğrulama turu değildir. Kritik olan,
beş ajanın da **bunu gizlememiş** olmasıdır.

---

## 6. TUR 2'YE GEÇİŞ ENGELİ

**Karar: TUR 2 başlayabilir — ANCAK `kanal-marj-uzmani` için KAPSAM
KISITLAMASI ile.**

### 6.1 `kanal-marj-uzmani`'nın ihtiyaç duyduğu girdilerin durumu

| Girdi | Durum | Kaynak |
|---|---|---|
| Benchmark fiyatı ve KDV statüsü | ✅ **HAZIR** (599,90 TL, KDV dahil, yüksek güven) | `EV-503`…`-506` |
| Benchmark katmanı | ⚠️ **KISMEN** — `L8_METRO_CASH_CARRY` onaylandı; `L8_CHAIN_RETAIL` **UNKNOWN** | §2.4, `OQ-502` |
| Benchmark promosyon durumu | ❌ **UNKNOWN** | `T-504` CRITICAL |
| Reklam/promosyon/hediye yasağı çerçevesi | ✅ **HAZIR ve NET** — tam yasak, T1 | `EV-222` |
| **7584 s.K. raf/satış ünitesi kapsamı** | ❌ **UNKNOWN** | `T-205` CRITICAL, `C-203` |
| Metro mağaza ≠ sevkiyat fiyat rejimi | ✅ **HAZIR** (fark ölçülmemiş) | `EV-507`, `T-506` |
| Alkolün kampanya/çek mekanizmaları dışında olması | ✅ **HAZIR** | `EV-508` |
| İthalatçının ülke geneli yerinde teslim yükümlülüğü | ⚠️ **C-201'e bağlı** | `T-201` |
| **L5 / L6 (ithalatçı maliyeti ve satış fiyatı)** | ❌ **HESAPLANAMAZ** | fiyat, navlun, KDV indirilebilirliği hepsi `null` |
| Yılda 1–2 konteyner gelişinin stok/nakit etkisi | ✅ **HAZIR** (ipucu olarak) | navlun çapraz ipuçları |

### 6.2 Adıyla engeller

| # | Engel | Etkisi |
|---|---|---|
| **E1** | **`T-205` / `C-203`** — 7584 s.K. satış noktası marka/ambalaj görseli yasağının raf kapsamı **CRITICAL, OPEN** | Listeleme pazarlığında hangi kaldıraçların **var olduğunu** belirler. Geniş yorum doğruysa private label senaryosu elenir. Bu, `kanal-marj-uzmani`'nın **en büyük tek belirsizliğidir.** |
| **E2** | **L5/L6 yokluğu** — ithalatçı maliyeti hesaplanamıyor | Kanal marjı **yüzde olarak** araştırılabilir, **TL olarak** kapatılamaz. Fiyat merdiveni (L6→L7→L8) **kapatılamaz.** |
| **E3** | **`T-504`** — benchmark promosyonlu mu | Merdivenin **tepe noktası** belirsiz; ters model hedefi oynak. |
| **E4** | **`OQ-502`** — zincir market gerçek L8'i hiç gözlenmedi | Kanal önceliği #1 (chain retail) için **sıfır fiyat gözlemi** vardır. |
| **E5** | `80-model/inputs/pazar.yaml` yok | `kanal-marj-uzmani` benchmark girdilerini bir model dosyasından okuyamaz. → `T-903` (TUR 2'den **önce** kapanmalı) |

### 6.3 Başkan direktifi — TUR 2 kapsam kısıtlaması

`kanal-marj-uzmani` TUR 2'de **şunları yapar**: kanal bazında marj yapıları,
listeleme bedeli, ciro primi, vade, iade koşulları, kampanya maliyetleri —
her biri **min/base/max aralık** olarak, dört zorunlu nitelikle (hangi iki
katman arası / brüt-net / KDV dahil-hariç / margin-markup).

**Şunları YAPAMAZ:**
1. Hedef EXW/FOB **hesaplayamaz** (ters model `finans-fizibilite`'nindir).
2. Kapalı bir fiyat merdiveni (L5→L8) **kuramaz** — L5 yoktur.
3. `L8_METRO_CASH_CARRY`'yi **L7 veya `L8_CHAIN_RETAIL` yerine kullanamaz**
   (§2.4 K1–K2).
4. `T-205` kapanmadan 7584 s.K.'nın kanal etkisi hakkında **sonuç yazamaz** —
   yalnızca iki yorumu (dar/geniş) **ayrı senaryo** olarak modelleyebilir.

`T-903` TUR 2 başlamadan kapatılmalıdır; diğer engeller TUR 2'yi durdurmaz,
**kapsamını daraltır.**

---

## 7. KRİTİK UNKNOWN ENVANTERİ

Nihai kararı **bloke edebilecek** UNKNOWN'lar, beş rapordan tek listede
birleştirilip önceliklendirilmiştir. CLAUDE.md §1.14: *"Kritik UNKNOWN nihai
kararı bloke edebilir. Bu bir hata değil, tasarımdır."*

### P0 — Kararı doğrudan bloke eder

| # | UNKNOWN | Sahibi | Neyi bloke eder | Takip |
|---|---|---|---|---|
| **U1** | **4250 s.K. m.1/3 — 1.000.000 lt/yıl eşiği durgun şarap ithalatına uygulanıyor mu?** | mevzuat | **G0.** Uygulanıyorsa iş modelinin fiyatlandırma serbestisi yoktur → projenin çekirdek sorusu anlamsızlaşır | `T-201`, `C-201` |
| **U2** | **Gerçek EXW/FOB fiyatı — hiçbir üretici, hiçbir ülke için** | sourcing | **G2, G4.** İleri model çalışamaz; ters modelin çıktısı doğrulanamaz | `OQ-401` |
| **U3** | **Rota bazlı navlun (özellikle California) ve toplam lead time** | lojistik | **G2-L, G4.** L1→L2 geçişi + işletme sermayesi | `T-304` |
| **U4** | **İthalatta ödenen KDV indirilebilir mi?** | vergi | **G1, G4.** Şişe başına ≈40–45 TL'nin ekonomik maliyet olup olmadığı | vergi UNKNOWN #1 |
| **U5** | **Model hedef tarihinde geçerli ÖTV tutarı** (`model_hedef_tarihi = null`) | vergi + mevzuat | **G1, G4.** 2027'ye taşan takvimde +%16 mertebesinde sapma | `T-104`, `OQ-002`, `OQ-G08` |
| **U6** | **Benchmark 599,90 TL promosyonlu mu, normal mi?** | pazar | **G3.** Ters modelin hedefi | `T-504` |
| **U7** | **7584 s.K. raf/satış ünitesi kapsamı** | mevzuat | **G3, kanal modeli.** Geniş yorumda private label elenir | `T-205`, `C-203` |
| **U8** | **Karar eşiklerinin tamamı `TBD`** (`00-charter/karar-esikleri.md`) | **YATIRIMCI** | **TUR 6.** Eşiksiz nihai karar verilemez; araştırmayla kapanmaz | **`OQ-901`** |

### P1 — Kararın büyüklüğünü/biçimini değiştirir

| # | UNKNOWN | Sahibi | Etki | Takip |
|---|---|---|---|---|
| U9 | Zincir market gerçek L8'i (kanal önceliği #1'de sıfır gözlem) | pazar | Merdivenin tepesi; `L8_CHAIN_RETAIL` | `OQ-502` |
| U10 | Türkiye şarap ithalat hacmi / menşe kırılımı | pazar | 50–100 bin şişe ölçek hedefi doğrulanamaz → `SCALE` değerlendirilemez | `OQ-501`, `T-505` |
| U11 | Gerçek MOQ yapısı (SKU mu, konteyner mı) | sourcing | 5.000 şişelik pilotun mümkün olup olmadığı; `peak_cash_requirement` | `OQ-402`, C-401 |
| U12 | Dağıtım yetki belgesi fiilî süresi (mevzuatta **tanımsız**) | mevzuat | Kritik yolun %25–35'i; hangi yılın tarife setinin geçerli olacağı | `T-202` |
| U13 | Ruhsat/analiz/bandrol nedeniyle malın bekleme süresi | mevzuat + lojistik | Limanda mı antrepoda mı beklendiği **~30 kat** maliyet farkı | `T-301` |
| U14 | Antrepodan kısmi çekiş mümkün mü | lojistik | `peak_cash_requirement`'ı dramatik biçimde değiştirir | `T-101` |
| U15 | Gözetim / referans kıymet var mı (negatif arama) | vergi | Düşük CIF beyanına dayalı sourcing stratejisi | vergi UNKNOWN #2 |
| U16 | Bandrolleme birim maliyeti ve antrepo elleçlemesi | lojistik | Ruhsat değişken maliyeti 2,52 → 4,5+ TL/şişe olabilir | `T-204` |
| U17 | İki iş modelinin (A/B) eşit derinlikte araştırılamamış olması | sourcing + pazar | Karar **kanıtla değil arama yöntemiyle** Model B'ye kayabilir | **`OQ-902`** |
| U18 | Zorunlu laboratuvar analizi var mı, parti başı mı | mevzuat | 5.000 şişelik pilot ekonomisi | `T-206` |

### P2 — Modeli etkiler, kararı çevirmez

Menşe ispat belgesi türü · KKDF matrahı (peşin ödemede etkisiz) · 12 haneli
GTİP (vergiyi değiştirmiyor) · damga vergisi · çekici/şasi darası · palet adedi
(C-301 bandı) · terminal ardiye free time · fire/kırılma oranı · thermal liner
maliyeti · HoReCa fiyat çarpanı · benchmark ürünün California alt bölgesi
(C-403, `UNRESOLVABLE`).

### 7.1 Envanterin okunması

**18 P0/P1 UNKNOWN'ın 13'ü masabaşında kapanamaz** — gerçek RFQ, gerçek
kotasyon, fiziksel mağaza ziyareti veya kurum/danışman teması gerektirir.
Bu, TUR 1'in bir eksikliği değil, **doğal sınırıdır**; TUR 7'nin varlık
sebebidir.

**Tek bir eylem en çok UNKNOWN'ı kapatır:** sektörde faal küçük ölçekli bir
şarap ithalatçısı + bir gümrük müşaviri ile yapılacak iki oturum, U1, U4, U5,
U12, U13, U14, U15, U16 ve U18'i (9 kalem) aydınlatma potansiyeline sahiptir.

---

## 8. AÇILAN TICKET VE AÇIK SORULAR

| id | hedef | konu | impact |
|---|---|---|---|
| `T-901` | `gumruk-vergi-uzmani` | C-101 çözümünün zayıf halkası: %16,09 Yİ-ÜFE artışının bağımsız doğrulanması | HIGH |
| `T-902` | `global-sourcing-kasifi` | Katman etiketi ihlali: `fob_gosterge_bandi.katman: L1` ve `katman_L1_ihracat_ort_*` (L1 > L2 tersliği); `ara_dogrulama` FACT→ESTIMATE | HIGH |
| `T-903` | `turkiye-pazar-kasifi` | `80-model/inputs/pazar.yaml` mevcut değil; `EV-509`/`-510` gelecek tarihli `publication_date` | HIGH |
| `T-904` | `mevzuat-ruhsat-uzmani` | `ruhsat.yaml`'da katman etiketi yok; bandrolün L3 mü L5 mi olduğu (T-203 ile bağlantılı); türetme kartlarına T1 tier verilmesi | MEDIUM |
| `T-905` | `navlun-lojistik-uzmani` | `EV-2026-08-09-310` mevzuat kanıtı olmasına rağmen `effective_date: UNKNOWN` | MEDIUM |
| `T-906` | `gumruk-vergi-uzmani` | `sise_hacmi_litre = 0.75` `FACT` + `evidence_id: null`; `hesap_sozlesmesi` içinde oran/tutar tekrarı | MEDIUM |

| id | konu | impact |
|---|---|---|
| `OQ-901` | Karar eşiklerinin tamamı `TBD` — nihai karar eşiksiz verilemez (sahibi: **yatırımcı**) | **CRITICAL** |
| `OQ-902` | İki iş modeli eşit derinlikte araştırılmadı; karar arama yöntemi kaynaklı olarak Model B'ye kayabilir | HIGH |

---

## 9. BU KARARI NE ÇÜRÜTÜR?

*(Bu belge karar içermez; aşağıdaki soru bu **denetimin** hükümleri içindir.)*

### 9.1 Bu denetimi çürütecek en güçlü tek bulgu

**Şarap reyonundaki fiziksel raf etiketinin bir fotoğrafı — ve o fotoğrafta
`KDV'li` ibaresinin bulunmaması.**

Bu tek görüntü şu zinciri aynı anda kırar:
- OQ-001'in kapanan ayağı (KDV dahil) yeniden açılır → `BM_A`'nın base case
  konumu düşer;
- C-502'nin "kapsam farkı" çözümü (§4.2) geçersizleşir — çünkü o çözüm,
  "müşteriye ilan edilen fiyat brüttür" önermesine dayanıyordu;
- G3'ün "kısmen ilerledi" değerlendirmesi çöker;
- `turkiye-pazar-kasifi`'nın 15 kanıt kartının **dört tanesi** (`EV-503`…`-506`)
  aynı anda değer kaybeder.

**Nasıl ararız:** Tek bir insan, tek bir Metro ziyareti, ~15 dakika, ~0 TL.
`T-504` bunu zaten istemektedir. **Bu, projedeki en yüksek bilgi/maliyet
oranına sahip tek eylemdir** ve TUR 2'den önce yapılmalıdır.

### 9.2 Bu denetimin en kırılgan hükmü

**C-101'in `RESOLVED` sayılması (§4.1).**

Kırılgan çünkü çözüm, GİB'in (T2) yayımladığı listenin **hesabının doğru
olduğu** varsayımına dayanıyor ve %16,09'luk artış TÜİK'ten **bağımsız olarak
doğrulanmamıştır.** Ben bu doğrulamayı **yapamam** (CLAUDE.md §1.16 —
başkan araştırma yapmaz), bu yüzden çözümü `T-901` koşuluna bağladım.

3/7/2026 sonrasında şarap için md.12/3'ü askıya alan veya tutarı yeniden tespit
eden bir Cumhurbaşkanı Kararı çıkmışsa, **projenin en kritik tek sayısı
yanlıştır** ve C-101 yeniden açılır.

### 9.3 Bu denetimin en tartışmalı hükmü

**G0'ın `PASS (koşullu)` yerine `BLOCKED (koşullu)` etiketlenmesi (§5.1).**

Karşı argüman güçlüdür: 4250 s.K. m.1/3'ün yaptırım mercii (Tekel Genel
Müdürlüğü) **artık mevcut değildir** ve Türkiye'de fiilen faaliyet gösteren
çok sayıda küçük ölçekli şarap ithalatçısı olduğu bilinmektedir — yani hüküm
pratikte ölü olabilir. Bu doğruysa etiketim gereksiz yere muhafazakârdır ve
projeyi bir tur geciktirir.

**Yine de BLOCKED'da ısrar ediyorum**, çünkü "hüküm pratikte ölüdür" önermesi
şu anda **hiçbir kanıt kartına dayanmamaktadır** — yalnızca makul bir sezgidir.
Bu sezgiyi FACT gibi kullanmak, denetlediğim ihlalin ta kendisini işlemek olur.
`T-201`'in **Yetkili Dağıtım Firmaları Listesindeki küçük ithalatçıların
tespiti** ayağı bu etiketi bir hafta içinde `PASS`'e çevirebilir.

### 9.4 Bu denetimin yanlış olması durumunda ne değişir

| Yanlış çıkan hüküm | Değişen şey |
|---|---|
| C-101 çözümü (§4.1) | Projenin en kritik sayısı; tüm vergi yükü; G1 |
| G0 = BLOCKED (§5.1) | Bir tur gecikme (aşağı yönlü hata) veya G0'ın gerçekte FAIL olması (yukarı yönlü hata) |
| `L8_METRO_CASH_CARRY` onayı (§2.4) | Ters modelin hedef katmanı; `kanal-marj-uzmani`'nın merdiven tepesi |
| C-401/C-402'nin "sahte çelişki" sayılması (§4.3) | MOQ senaryo seti; benchmark maliyet proxy'si |
| "TUR 2 başlayabilir" (§6) | Kanal verisi eksik temel üzerine toplanır ve TUR 5'te yeniden yapılır |

### 9.5 Denetimin kendi kör noktası

Ben **kanıtların içeriğini bağımsız olarak doğrulamadım** — doğrulayamam
(CLAUDE.md §1.16). Kontrol ettiğim şey **iç tutarlılık, etiket doğruluğu,
katman disiplini ve kaynak otoritesi zinciridir.** Beş ajan da aynı sistematik
hatayı yapmış olsaydı (örneğin hepsi aynı erişilemeyen resmî kaynağın yerine
aynı ikincil kaynağı koysaydı), bu denetim onu **yakalayamazdı**.

Bunun panzehiri TUR 4'tür: `seytanin-avukati` bu denetimi değil, **bulguların
kendisini** hedef almalıdır.

---

## EK — ÜRETİLEN / GÜNCELLENEN DOSYALAR

- `90-karar/tur-1-kanit-kalitesi-denetimi.md` *(bu dosya)*
- `99-ops/celiskiler.md` — 8 çelişkinin `durum`/`cozum`/`cozen`/`cozum_tarihi`
  alanları güncellendi; **hiçbir çelişki metni silinmedi**
- `99-ops/tickets/T-901.md` … `T-906.md` + `99-ops/tickets/INDEX.md`
- `99-ops/acik-sorular.md` — `OQ-901`, `OQ-902` eklendi

**`90-karar/karar-gunlugu.md` dosyasına DOKUNULMAMIŞTIR.**
