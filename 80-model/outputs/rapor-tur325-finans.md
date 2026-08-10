# AJAN RAPORU — `finans-fizibilite` · TUR 3.25 §12/§13

```yaml
ajan:             finans-fizibilite
tur:              "TUR 3.25 §12/§13 — QUOTE INGESTION SCHEMA + EVALUATION"
tarih:            2026-08-10
durum:            DRAFT               # APPROVED OLAMAZ — OQ-901/T-851 CRITICAL+OPEN
kapsam:           sema + degerlendirme motoru (TUR 3B karlilik modeli KOSULMADI)
yeni_arastirma:   YOK
yeni_evidence:    YOK                 # 10-evidence/ dokunulmadi
web_arama:        YOK
dis_iletisim:     NONE                # hicbir tedarikciye mesaj gonderilmedi
uretilen_teklif:  0                   # uydurulmus ornek teklif EKLENMEDI
uretilen_ret:     0                   # RET HUKMU YASAK
makro_yaml:       SADECE OKUNDU       # gumruk-vergi-uzmani'nin alani
ana_belge:        80-model/outputs/quote-evaluation-protokolu.md
testler:          34/34 (yeni) + 30/30 (TUR 3A, kirilmadi)
```

---

## 1. YÖNETİCİ ÖZETİ

1. **Teklif alım şeması kuruldu** (`quote-ingestion-schema.yaml`): iç içe
   (belge → beş kademe) yapı, 27 alan, ve **dokuz makine-okunur doğrulama
   kuralı** (`QV-1…QV-6`). Kurallar yorum satırı değil **veri**dir; motor
   onları çalıştırır — şemadan bir kural silindiğinde davranış değişir ve bu
   **davranışsal olarak test edilmiştir**.
2. **Değerlendirme motoru kuruldu** (`teklif_degerlendirme.py`): her kademe
   **dört FX ekseninde ayrı ayrı** ölçülür ve dört sonuçtan biri üretilir.
   **Tek kur ile tek sonuç üretilmez.**
3. **`REJECTED` üretilemez — dört kilitle.** Sonuç alfabesi dört elemanlıdır,
   yasak kelime listesi vardır, tek geçitten geçilir ve `retmek()` fonksiyonunun
   **gövdesi yoktur**. `Degerlendirme(sonuc="REJECTED")` **nesne olarak
   kurulamaz**.
4. **`fx` geldi** (`makro.yaml → fx.senaryolar`, TCMB 2026/147,
   `EV-2026-08-10-865/-866/-867/-868`). Üç turdur `UNKNOWN` olan **`MAX_FOB` /
   `MAX_EXW` kısmen açıldı**: dört eksende **üst sınır** hesaplandı
   (FX_0 · Grup P · Y: **≤ 5,2685 EUR** / **≤ 6,0889 USD** şişe başına).
   **Nokta değeri hâlâ `BLOCKED_INPUT`** — FOB→CIF köprüsü yok (`T-866`).
5. **En sert tek bulgu geometrik:** X→Y bandı (×1,4455) FX ekseninin
   açıklığından (×1,3333) **geniştir** → **kur hareketi tek başına bir teklifi
   `STRONG`'dan `ABOVE_CEILING`'e çeviremez.** Bu, kur riskinin senaryo
   riskinden küçük olduğu anlamına gelebilir — **ya da eksenin çok dar
   seçildiği** (`T-874`).

---

## 2. BULGULAR

### B-1: `MAX_FOB` / `MAX_EXW` — üç turluk `UNKNOWN` kısmen kapandı

```yaml
claim:          "fx geldigi icin MAX_FOB/MAX_EXW artik hesaplanabilir — ama NOKTA DEGERI olarak degil, UST SINIR olarak."
value:          "FX_0 · Grup P · TGT_799 · CHAIN · Y kosesi: MAX_FOB <= 5,2685 EUR/sise ; <= 6,0889 USD/sise"
unit:           "EUR veya USD / sise"
status:         DERIVED / UPPER_BOUND
tier:           "girdi: T2 (TCMB) — cikti: MODEL_DERIVED"
evidence_id:    "EV-2026-08-10-865, EV-2026-08-10-866 (kur) + country-buying-ceilings.csv (tavan)"
katman:         "L1 (FOB) ve L0 (EXW)"
```

**Türetme zinciri:**
```
MAX_CIF_TRY (Y kösesi, Grup P, TGT_799, CHAIN)   = 290,5134 TRY/sise   [CSV]
kur (FX_0, EUR/TRY, doviz_satis, 2026-08-10)     =  55,1414 TRY/EUR    [EV-...-865]
CIF = FOB + navlun + sigorta,  köprüler >= 0
  =>  MAX_FOB <= 290,5134 / 55,1414 = 5,2685 EUR/sise
  =>  MAX_EXW <= MAX_FOB           (EXW->FOB köprüsü de >= 0)
```

**⛔ Bu bir üst sınırın üst sınırının üst sınırıdır — üç kat:**
1. `MAX_CIF` zaten üst sınırdır (λ=1 çapası + **26 kalem `BLOCKED_INPUT`**),
2. köprü `0` alınmıştır (gerçekte `> 0`),
3. `Y` köşesi iyimser senaryodur (BASE + DOC_OK + 25.000).

**`lojistik.yaml → sise_basi_lojistik_maliyeti` bilerek KULLANILMADI:**
kapsamı `L1→L3`'tür (**CIF değil**) ve `_meta.dahil_degil` açıkça
**"sigorta"** diyor. CIF köprüsü olarak kullanmak **çift sayım** olurdu.

### B-2: Band genişliği > FX ekseni açıklığı — yapısal, girdisiz bulgu

```yaml
claim:          "Kur hareketi tek basina bir teklifi STRONG'dan ABOVE_CEILING'e ceviremez."
value:          "band = 290,5134/200,9780 = x1,4455  >  fx ekseni = 1,20/0,90 = x1,3333"
unit:           oran
status:         STRUCTURAL_FACT
tier:           MODEL_DERIVED
evidence_id:    "country-buying-ceilings.csv + makro.yaml/fx.senaryolar"
katman:         L2 (CIF)
```

**Gerekçe:** Bir teklifin `STRONG` (≤X) olması ile `ABOVE_CEILING` (>Y) olması
arasında **×1,4455**'lik bir mesafe vardır. FX ekseninin uçtan uca açıklığı
**×1,3333**'tür. Dolayısıyla `X`'in tam altındaki bir teklif, `FX_DOWN_10`'dan
`FX_UP_20`'ye giderken en fazla `Y`'ye kadar gelir, **onu aşamaz**.

Fixture ile doğrulandı: `TQV-7A` → `STRONG/STRONG/NEGOTIATE/NEGOTIATE`;
`TQV-7B` → `NEGOTIATE/NEGOTIATE/ABOVE_CEILING/ABOVE_CEILING`. **Hiçbir
tek teklif dört eksende üç sonucu birden gezmez.**

**Bu bulgu hiçbir `UNKNOWN`'a bağlı değildir** — `%11,765`'lik tercih kaybı
formülünden sonra modelin **ikinci girdisiz sayısıdır**.

### B-3: `V2 = 10.000` kademesinin tavanı YOK — interpolasyon yapılmadı

```yaml
claim:          "TUR 3.25'te eklenen V2 = 10.000 sise kademesi country-buying-ceilings.csv icinde YOK."
value:          "hacim_tavani_oku(...,10000) -> None + HACIM_KADEMESI_TAVANI_YOK(10000)"
status:         BLOCKED_INPUT
evidence_id:    "country-buying-ceilings.csv (VOLUME_BOTTLES ∈ {5.000, 25.000, 50.000, 100.000})"
katman:         L2
```

**Gerekçe:** 5.000 ile 25.000 arasında **düz çizgi çekilmedi**, çünkü hacim
eğrisi doğrusal değildir (`lojistik.yaml`: şişe başı lojistik maliyeti
5.000→100.000 arasında **3–4 kat** düşer). İnterpolasyon **sahte hassasiyet**
üretirdi. → **`T-865`** (çözümü yeni araştırma değil, ters modelin yeniden
koşulmasıdır).

### B-4: `FIRM_QUOTE` doğrulaması — gerçek e-posta yetmez

```yaml
claim:          "Gercek bir tedarikci e-postasi, gercek oldugu icin FIRM_QUOTE olmaz."
value:          "FIYAT + GECERLILIK + MIKTAR + INCOTERM(+yer) — DORDU AYNI KADEMEDE BIRLIKTE"
status:         SPEC_DECISION
```

Şemadaki makine-okunur hâli `QV-1` + `QV-1B`; destekleyici kilitler
`QV-1C` (belirsiz para birimi → `INCOMPLETE`), `QV-1D` (belirsiz Incoterm →
`INCOMPLETE`), `QV-2` (**sınıf yükseltme yasağı**: `etkin = min(beyan, hesaplanan)`).

Bu üç kilit **gerçek arızalardan** doğdu: Kart 1'de para birimi yalnızca `$`
(AUD mı USD mi **doğrulanmadı**, tek başına fiyatı ~1,5 kat değiştirir) ve
`C-461`'de **aynı sayı** hem `ex factory` hem `FOB` olarak sunulmuş.

### B-5: Tek yönlü karar — modelin kendi bilgisizliğinin yönünü bilmesi

```yaml
claim:          "Kopru eksikken YALNIZCA ABOVE_CEILING kararlastirilabilir; STRONG asla."
status:         STRUCTURAL_FACT
```

`gerçek_CIF ≥ teklif × kur` (köprüler `≥ 0`). Dolayısıyla:
`teklif × kur > Y` ⇒ `ABOVE_CEILING` **sağlamdır**;
`teklif × kur ≤ Y` ⇒ **hiçbir şey söylenemez** → `INCOMPLETE`.

Bu asimetri koda gömülüdür (`karar_yolu = TEK_YONLU_ALT_SINIR`) ve test
edilmiştir (`C::TEK_YONLU`). **Bugünkü pratik sonucu şudur: `T-866` kapanmadan
koşulan bir RFQ turunda, makul fiyatlı her teklif `INCOMPLETE` döner ve tur
bilgi üretmez.**

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | **FOB→CIF köprüsü** (navlun + **sigorta**, CIF kapsamlı, şişe başına) | `lojistik.yaml`'daki kalem `L1→L3` kapsamlı ve sigortasız | **HIGH** | `T-866` — `navlun-lojistik-uzmani` |
| 2 | **EXW→FOB köprüsü** (menşe içi nakliye + ihracat masrafı) | hiç toplanmadı; **tesise** bağlı, ülkeye değil | **HIGH** | `T-867` |
| 3 | `V2 = 10.000` tavanı | CSV'de o hacim satırı yok | **HIGH** | `T-865` — ters model yeniden koşulur |
| 4 | **Yatırımcı marj eşiği** | `OQ-901` açık | **CRITICAL** | `T-851` — bu yüzden ret hükmü yasak |
| 5 | `FULL_20FT_CONTAINER` şişe adedi | palet/koli konfigürasyonu tedarikçiye bağlı (paletsiz 11.800–13.700 / paletli 6.480–7.200) | MEDIUM | `T-869` |
| 6 | AUD / CLP / MDL kurları | `makro.yaml` yalnızca EUR/USD taşıyor | MEDIUM | AU ve MD tedarikçileri için gerekli olacak |
| 7 | Gümrükte uygulanacak kur (beyan kuru) | `fx.gumruk_kuru_kullanilir_mi` = `null` | HIGH | **`T-911` zaten AÇIK** — yeni ticket açılmadı |
| 8 | `quote_class` atama süreci sahibi | tanımlı değil | MEDIUM | `T-868` |

---

## 4. ÇELİŞKİLER

Bu turda **yeni çelişki bulunmadı.** `99-ops/celiskiler.md` **dokunulmadı**.

Kayda değer tek nokta: `makro.yaml`'da `fx.observed` ve düz `fx.usd_try`
blokları **kasıtlı kopyadır** (dosya bunu kendisi belirtiyor: *"biri
güncellenirse diğeri de güncellenir; yoksa CONFLICT doğar"*). Motor **`fx.senaryolar`
bloğunu** tercih eder ve eksen çarpanlarını **eksen adının tanımıyla
karşılaştırır**; uyuşmazlık olursa `CONFLICT` bayrağı basar
(test `F::FX_CARPAN` — bugün sapma **yok**).

---

## 5. ÜRETİLEN DOSYALAR

| Dosya | Ne |
|---|---|
| `80-model/inputs/quote-ingestion-schema.yaml` | şema — 27 alan, 5 kademe, **9 makine-okunur kural**, `teklifler: []` |
| `80-model/engine/teklif_degerlendirme.py` | ingestion + evaluation + `INTERNAL_ONLY` + ret yasağı |
| `80-model/engine/test_teklif_degerlendirme.py` | **34 test** |
| `80-model/inputs/TEST_FIXTURE-teklif-vektorleri.yaml` | 15 sentetik vektör (uydurma tedarikçi adları, sentetik kur, sentetik band) |
| `80-model/outputs/quote-evaluation-protokolu.md` | protokol |
| `80-model/outputs/INTERNAL_ONLY-teklif-degerlendirme.md` | motorun canlı çıktısı |
| `99-ops/tickets/T-865, T-866, T-867, T-868, T-869, T-874` | 6 ticket |

**Dokunulmayanlar:** `makro.yaml` (yalnızca **okundu**), `10-evidence/`,
`99-ops/{capraz-ipuclari,celiskiler,acik-sorular}.md`, `tickets/INDEX.md`,
`50-sourcing/`, `60-pazar/`, `70-kanal/`, `30-vergi-gumruk/`, `40-lojistik/`,
`country-buying-ceilings.csv` (yalnızca **okundu**).

### Test sonuçları

```
test_teklif_degerlendirme.py   34/34 gecti
test_model_butunlugu.py        30/30 gecti   (TUR 3A — KIRILMADI)
teklif_degerlendirme.py        0 teklif, 0 ret, 4/4 fx ekseni HAZIR
```

Kapsam: 10 sınıflandırma vektörü · 5 FX vektörü (her biri 4 eksen = 20 hücre) ·
tek-yönlü karar · katman ayrımı (`L0`≠`L1`) · ret yasağı (6 yasak kelime +
`retmek()` + nesne kurulumu) · `INTERNAL_ONLY` dosya kilidi · sızıntı taraması ·
fixture sızıntısı · kademe tekilliği · metadata damgası · **gerçek CSV bandı** ·
**gerçek `makro.yaml` dört ekseni** · çarpan tutarlılığı · `MAX_FOB` monotonluğu ·
kural-veri davranış testi · epistemik asimetri.

---

## Bu bulguyu ne çürütür?

### Hangi tek girdinin yanlış olması sonucu tersine çevirir?

**`MAX_CIF_TRY`'nin kendisi.** Bu turda kurulan her şey — dört sonuç değeri,
dört FX ekseni, `MAX_FOB` üst sınırı — **tek bir sayının üstünde duruyor**:
`290,5134` (ve `200,9780`). O sayı `reverse-price-model.md`'nin `DRAFT`
çıktısıdır ve **26 kalemi `BLOCKED_INPUT`**'tur.

Somut olarak: `m_retail = %25` yerine `%35` doğruysa `MAX_CIF` `272,83 → ~176`
(**−%35**) olur. O zaman **`MAX_FOB` üst sınırı `5,27 → ~3,2 EUR`'ya iner** ve
bugün `NEGOTIATE` görünecek her teklif `ABOVE_CEILING` olur. **Motorun cebri
değişmez, verdiği her cevap değişir.** Ve `m_retail`'in tek kanıtlı çapası
Migros'un **tüm kategori** %24,31'idir — **şarap değildir**.

Aynı şekilde `L8_CHAIN_RETAIL` katmanında Türkiye'de **sıfır gözlem** vardır
(`T-701`, `T-603`). Yani **pazarlık çapamızın dayandığı raf katmanı hiç
ölçülmemiştir.** Bu, bandın **hem X hem Y ucunu** aynı anda kaydırır — ve
band kayarsa B-2'deki geometrik bulgu (×1,4455 > ×1,3333) da **çöker**.

### Modelde çift sayım riski nerede?

| Yer | Risk |
|---|---|
| **`FOB_CIF` köprüsü ↔ `L5` kalemleri** | `lojistik.yaml`'ın `L1→L3` kapsamlı kalemi köprü olarak kullanılırsa, varış sonrası kalemler **hem köprüde hem `L5`'te** sayılır. Bu turda **kullanılmadı** — ama `T-866` cevaplanırken **kapsam sınırı açıkça yazılmazsa risk canlanır.** Bu, bu turun **en somut çift sayım tehlikesidir.** |
| **`EXW_FOB` ↔ `FOB_CIF`** | Menşe limanı terminal masrafı (THC) hangi bacakta? Incoterm'e göre değişir. İki ticket ayrı ajanlara değil **aynı ajana** açıldı (`T-866`+`T-867`) ki sınır **tek elden** çizilsin. |
| **`label_cost` ↔ `carton_cost` ↔ EXW fiyatı** | Kart 1'de "Dry Goods dahil" ama "etiket baskısı **dahil değil**"; Kart 3'te "tasarım ücretsiz" (**baskı değil**). Şema bu yüzden `label_cost` ve `label_cost_tek_seferlik`'i **ayrı alanlar** olarak taşıyor — ama **hangisinin EXW'nin içinde olduğunu tedarikçi söylemedikçe bilemeyiz.** `LEDGER_UNIQUENESS` bunu **yakalayamaz**, çünkü iki kalem farklı isimdedir. |
| **Kademeler arası** | İç içe yapı seçildiği için belge-seviyesi alanlar tek kaynaktadır → düz yapının ayrışma riski **ortadan kalktı**. `KademeCiftKayit` aynı kademenin iki kez yüklenmesini **engelliyor**. |

### Hangi ASSUMPTION'lar sonucu taşıyor — bunlar çökerse ne olur?

| ASSUMPTION | Çökerse |
|---|---|
| **X/Y köşe tanımı** (`HIGH`+`DOC_FAIL`+5.000 / `BASE`+`DOC_OK`+25.000) | Bu bir **seçimdir**, bir ölçüm değil. `rfq-negotiation-cards.md` §0.2'den devralındı. Köşeler değişirse **band genişliği değişir** ve B-2'deki geometrik bulgu geçersizleşir. |
| **`origin_document = UNKNOWN` ⇒ kötümser band (N)** | Muhafazakâr bir seçim. Ama Grup P'de gerçekten belge alınabiliyorsa, bugün `ABOVE_CEILING` denen bir teklif aslında `NEGOTIATE`'tir. Fark **tam `%11,765`**. |
| **FX ekseni ±%10/+%20** | `gumruk-vergi-uzmani`'nın tasarım kararı. Eksen dar seçildiyse "kur riski küçük" sonucu **eksenin yapaylığıdır**, bir bulgu değil → `T-874`. |
| **`doviz_satis` kur tipi** | İthalatçı dövizi satın alan taraftır → doğru seçim. Ama **gümrükte uygulanan kur farklı olabilir** (`T-911` **AÇIK**) ve o kur `MAX_CIF`'i **matrah üzerinden** etkiler — yani bu turda kullandığımız kur, verginin hesaplandığı kur **olmayabilir.** |
| **`ttl = 7d`** | Kur **2026-08-17**'de bayatlar. O tarihten sonra motor `FX_STALE` basar ama **hesap yapmaya devam eder**. Model hedef tarihi **2027**'dir — yani bugünün kuruyla 2027 tavanını karşılaştırmak **zaten yapısal olarak sorunludur** ve bunu FX eksenleri **çözmez**, yalnızca **gösterir**. |

### Bu turun kendi en zayıf noktası

**Sıfır teklifle kurulmuş bir teklif değerlendirme sistemi.**

34 testin tamamı **kendi yazdığım fixture'a** karşı koşuyor. Gerçek bir
tedarikçi e-postasının şemaya **sığacağını** hiçbir şey kanıtlamıyor. Gerçek
teklifler tipik olarak şemanın öngörmediği biçimlerde gelir: *"5–10 bin arası
€4,20–4,60"* (aralık, tek sayı değil), *"FOB Valencia veya EXW, sizin
tercihiniz"* (iki Incoterm bir arada), *"fiyat 2026 hasadına kadar geçerli"*
(tarih değil, olay).

Bu üçünün **hiçbiri** bugünkü şemaya sığmaz ve üçü de `INCOMPLETE` döner.
`INCOMPLETE` doğru cevaptır — ama **eğer gelen tekliflerin çoğu `INCOMPLETE`
dönerse, sistem disiplinli değil KULLANILAMAZ demektir**, ve bu ikisi
çıktıdan bakınca **aynı görünür.**

**`seytanin-avukati`'na öneri:** bu modüle saldırıya *"şu üç gerçekçi e-posta
metnini şemaya sok"* diye başlayın — cebirden değil, **kabul yüzeyinden**.
