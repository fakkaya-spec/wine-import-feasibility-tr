# AJAN RAPORU — finans-fizibilite · TUR 2.5 REVERSE TARGET MODEL

```yaml
ajan:                   finans-fizibilite
tur:                    TUR 2.5 — REVERSE TARGET MODEL (SINIRLI GOREV)
tarih:                  2026-08-10
durum:                  SUBMITTED
cikti_statusu:          DRAFT            # APPROVED DEGIL — CLAUDE.md §5
web_aramasi_yapildi_mi: false            # bu ajanin araci YOKTUR — kasitlidir
yeni_evidence_uretildi_mi: false         # 10-evidence/ ACILMADI
inputs_yaml_yazildi_mi: false            # 80-model/inputs/* SALT OKUNDU
git_calistirildi_mi:    false
ileri_model_calistirildi_mi: false       # KAPSAM DISI
contribution_margin_uretildi_mi: false   # KAPSAM DISI
break_even_uretildi_mi: false            # KAPSAM DISI
roi_irr_uretildi_mi:    false            # KAPSAM DISI
tedarikci_onerisi_uretildi_mi: false     # KAPSAM DISI
yatirim_karari_verildi_mi: false         # KAPSAM DISI
```

---

## 1. YÖNETİCİ ÖZETİ

Hedef raf fiyatı merdiveninden (`599/699/799/899/999` TL, KDV dahil,
`INVESTOR_ASSUMPTION`) geriye doğru **azami ödenebilir CIF** hesaplandı.
Önce **`T-921` kapatıldı**: engine'e `otv_maktu_zaman_serisi` okuyucusu ve
**ufuk denetimi** eklendi — hedef tarih `2026-12-31` ufkunu aşıyorsa ve açık
bir senaryo bayrağı yoksa engine artık **`UNKNOWN` döner** (fiilen doğrulandı).
`gumruk-vergi-uzmani`'nın **10 birim test vektörünün 10'u da geçti**;
**R8 round-trip 2.700 satırın 2.700'ünde tuttu** (fark < 1e-24 TL).

**En kritik tek bulgu:** Başkanın *"en güçlü çürütücü"* hipotezi —
*"999 TL'de bile ödenebilir CIF negatif veya sıfıra yakın çıkar"* —
**ÇÜRÜTÜLMÜŞTÜR.** Zincir ve tekel kanallarında beş basamağın beşinde de
`MAX_CIF_TRY` **137–429 TL/şişe** bandındadır (799 TL / İspanya / DOC_OK /
BASE: **272,83 TL/şişe**). **Segment aritmetik olarak imkânsız değildir.**

**İkinci en kritik bulgu — kendi hatam:** Zincirin `R5` adımında (sahibi bu
ajandır) **kanal geri akan bedelleri (`d`) hiçbir yerde düşülmüyordu.**
Hata tespit edildi, düzeltildi ve **büyüklüğü ölçüldü: 799 TL'de +28,95
TL/şişe fazla tavan (%+10,6)** — yani `H1` (−17,82) ve `H3` (−22,22)
hatalarından **daha büyük** ve `ters-model-vergi-bacagi.md` §6'nın beş hata
listesinde **yok** (§2, B-2).

**Üçüncü:** `MAX_FOB` ve `MAX_EXW` — döviz cinsinden **veya TL cinsinden** —
**hesaplanamamıştır.** `makro.yaml → fx` `null`'dır (`T-912`) ve navlun USD,
menşe local charge EUR cinsindendir. **Modelin ülke ayrıştırma gücü bu tek
eksik yüzünden çalışmamaktadır:** `MAX_CIF_TRY` 9 ülkenin 9'unda yalnızca
**iki değer** alır (`g = 0,50` veya `0,70`).

---

## 2. BULGULAR

### B-1: `T-921` kapandı — engine ufuk denetimi kazandı

```yaml
claim:          "Engine artik otv_maktu_zaman_serisi'ni okuyor ve model hedef tarihi
                 son_gozlem_gecerlilik_ufku'nu astiginda ACIK BAYRAK yoksa UNKNOWN donuyor."
value:          "5 kabul kriterinin 5'i karsilandi"
status:         FACT     # kod calistirilarak dogrulandi
evidence_id:    —        # kanit karti ACILMADI (bu ajan kanit uretmez)
```

**Gerekçe:** `80-model/engine/otv_zaman_serisi.py` (YENİ) `engine_okuma_kurali`
adım 1–5'i birebir uygular. `python3 80-model/engine/hesap.py`:

```
- otv_maktu_zaman_serisi.gelecek_degerler = null. model_hedef_tarihi (2027-04-01)
  > son_gozlem_gecerlilik_ufku (2026-12-31) ve senaryolar.yaml'da SECILMIS bir
  OTV artis ASSUMPTION'i YOK -> engine UNKNOWN doner (O-5, T-921).
```

Açık bayrak `UPPER_BOUND_LAMBDA_1` verildiğinde hesaplar ve çıktıyı
**`UPPER_BOUND`** olarak, **O-2/O-3/O-5/O-6 etiketleriyle** üretir.
`engine_yasak` da koda geçti. **2027 ÖTV tutarı hiçbir yerde yazılmadı.**

---

### B-2: ⚠ **KENDİ BULDUĞUM HATA — `R5`'te EKSİK SAYIM (düzeltildi)**

```yaml
claim:          "Ilk uygulamada L5_max = L6 x (1 - mu) alinmisti. Bu YANLISTIR:
                 kanal geri akan bedelleri (d) ve listeleme bedeli (f) ITHALATCININ
                 odedigi bedellerdir; ithalatcinin fiili net hasilati L6 degil
                 L7_eff = L6(1-d) - f'dir. Dogru tanim: L5_max = L7_eff - mu x L6."
value:          "+28,95 TL/sise fazla tavan (799 TL, ES, CHAIN BASE, 5.000 sise)"
unit:           TRY/sise
status:         MODEL_DERIVED     # bir kod duzeltmesi
evidence_id:    EV-2026-08-10-612  # d kalemlerinin ITHALATCIDAN alindiginin kaniti
katman:         L5 / L6 / L7
```

**Gerekçe:** `EV-2026-08-10-612` (Rekabet Kurulu 21-51/708-351, para.82) —
alkollü içkide zincirlerle imzalanan yıllık satış anlaşmalarında CRM, B2B,
alan kullanımı, kırık ürün bedeli, lojistik bedeli, soğutucu enerji bedeli
**"müşteriye ödenecek bedeller"** olarak sayılmaktadır. **Bunları ödeyen
ithalatçıdır.**

**Büyüklük:**

| | `L5_max` | `MAX_CIF_TRY` |
|---|---|---|
| Naif (yanlış) | 542,7989 | **301,78** |
| **Düzeltilmiş** | **499,3750** | **272,83** |
| Fark | −43,42 | **−28,95 (−%9,6)** |

> **Bu hata `H1` (−17,82) ve `H3` (−22,22) hatalarından DAHA BÜYÜKTÜR** ve
> `ters-model-vergi-bacagi.md` §6'nın beş hata listesinde **yoktur** — çünkü
> o belge **vergi bacağını** kapsar, **kanal bacağını** değil.
> `R5`'in sahibi ise **bu ajandır**.
>
> **Yönü tehlikelidir:** hata **projenin lehine** çalışır (tavanı yükseltir),
> yani gözden kaçması **daha olasıdır** — `H1`'in ters yönde muhafazakâr
> görünmesinin aynası.

**Hatanın en görünür belirtisi:** düzeltmeden önce `CHAIN_RETAIL` ve
`INDEPENDENT_TEKEL` tavanları **neredeyse özdeşti (< %1 fark)**. Düzeltmeden
sonra **%11,4 ayrıştılar** (799 TL: 272,83 vs 303,90).

**İkincil etki:** kanal marjı ekseni tornadoda **−10,67/+14,31**'den
**−45,06/+32,00**'a çıktı. **Yani R5 hatası, kanal riskinin büyüklüğünü de
gizliyordu.**

---

### B-3: `MAX_CIF_TRY` hesaplanabilir ve POZİTİF — ama iki nedenle ÜST SINIR

```yaml
claim:          "799 TL hedef raf fiyati icin azami odenebilir CIF, Ispanya menseli
                 ve tercihli belge saglandiginda 272,83 TL/sise'dir."
value:          272.8306
unit:           TRY/sise
status:         MODEL_DERIVED / UPPER_BOUND    # FACT DEGIL, QUOTE DEGIL
evidence_id:    [EV-2026-08-09-103, EV-2026-08-09-111, EV-2026-08-09-118,
                 EV-2026-08-09-213, EV-2026-08-09-234, EV-2026-08-09-235,
                 EV-2026-08-10-329]
effective_date: "GV 2026-01-01 · KDV 2023-07-10 · OTV capasi 2026-07-03"
katman:         L2_CIF
```

**Türetme zinciri:** `reverse-price-model.md` §3.1 (katman katman, R8 doğrulamalı).

**Neden ÜST SINIR — iki bağımsız neden:**
1. **λ = 1** — ÖTV 2026-07-03 çapasıyla; λ ≥ 1 olduğu için gerçek değer daha düşük.
2. **13 maliyet kalemi 0 alındı** — USD/EUR local charges, listeleme bedeli `f`,
   `d` (tekel/HoReCa), fire, antrepo bekleme, KDV finansman maliyeti,
   bandrolleme operasyonu, distribütör marjı, ithalatçı katkı payı, gözetim
   eşiği, müşavirlik CIF kademesi. **13'ünün 13'ü de aynı yönde (yukarı) saptırır.**

---

### B-4: Ülkeler arası fark **tek bir bölene** iner

```yaml
claim:          "Ters modelde mense, MAX_CIF_TRY'yi YALNIZCA (1+g) boleni uzerinden
                 etkiler. 9 ulke icin 9 farkli sayi YOKTUR — 2 farkli sayi vardir."
value:          "MAX_CIF(g=0,70) / MAX_CIF(g=0,50) = 1,50/1,70 = 0,88235"
status:         FACT     # cebirsel ozdeslik, hicbir UNKNOWN'a bagli degil
tier:           T1
evidence_id:    [EV-2026-08-09-103, EV-2026-08-09-104, EV-2026-08-09-110]
katman:         L2_CIF
```

**Tercihli rejimi kaybetmek azami satın alma fiyatını TAM %11,765 düşürür —
hedef fiyattan, ÖTV'den, marjdan, hacimden ve navlundan BAĞIMSIZ olarak.**
799 TL hedefte TL karşılığı: **−32,10 TL/şişe**.
Koşullar `K3` (`T-161`) ve `K4` (`T-163`/`T-914`) alanlarındadır ve
**ikisi de `ASSUMPTION: true`'dur.**

---

### B-5: Ölçek eğrisi 25.000'den sonra **düzleşiyor** — sebebi navlun DEĞİL, RUHSAT

```yaml
claim:          "MAX_CIF'in hacme duyarliligi 5.000 -> 25.000 arasinda +17,68 TL,
                 25.000 -> 50.000 arasinda YALNIZCA +0,77 TL'dir."
value:          "5k:272,83 | 25k:290,51 | 50k:291,28 | 100k:293,03"
unit:           TRY/sise
status:         MODEL_DERIVED
evidence_id:    [EV-2026-08-09-234, EV-2026-08-10-329]
katman:         L2_CIF
```

**Türetme zinciri:** `ruhsat.yaml → toplam_ruhsat_sabit_maliyeti` **20.000
litre/yıl** eşiğinde kademe atlar: **150.839 → 253.372 TL**
(`EV-2026-08-09-234`). 20.000 lt = **26.667 şişe** (0,75 lt `ASSUMPTION`).
Şişe başı ruhsat 25k'da 6,03 TL iken 50k'da yalnızca 5,07 TL'ye iner.

**Ölçek ekonomisinin %87'si ilk sıçramada (5k→25k) gerçekleşir.**
`navlun-lojistik-uzmani`'nın TUR 2.5 düzeltmesiyle **tutarlıdır**:
*"3–4 kat düşer" iddiası YALNIZ FCL için doğrudur; LCL'de USD bacağı
%12–14 düşer.*

---

### B-6: `MAX_FOB` ve `MAX_EXW` — TL cinsinden **bile** hesaplanamıyor

```yaml
claim:          "fob_try_max ve exw_try_max UNKNOWN'dir; sadece doviz karsiliklari
                 degil, TL karsiliklari da hesaplanamaz."
value:          null
status:         UNKNOWN
katman:         L1_FOB / L0_EXW
```

`FOB = CIF − navlun − sigorta`. Navlun **USD**, menşe local charge **EUR**;
`makro.yaml → fx` **`null`** (`T-912`) ve gümrük beyan kuru kuralı
**`UNKNOWN`** (`T-911`).

> **`master-commercial-input-table.md` §5.3'ün *"fx olmadan ters model
> CIF_TRY'ye kadar çalışır"* hükmü KISMEN DOĞRUDUR** → **`C-852`**.
> Doğru hâli: *"fx olmadan ters model `CIF_TRY`'nin bir **ÜST SINIRINA**
> kadar çalışır"* — çünkü L2 ile L5 arasındaki **USD cinsli varış masrafları**
> düşülememiştir.

---

### B-7: HoReCa'da 599 TL menü fiyatı, 5× çarpanda **yapısal olarak ölü**

```yaml
claim:          "HoReCa 5,0x carpaninda MAX_CIF = 0 olan menu fiyati 546,77 TL'dir.
                 TGT_599 bu tabanin YALNIZCA 52 TL ustundedir."
value:          546.77
unit:           TRY (KDV dahil menu fiyati)
status:         MODEL_DERIVED
evidence_id:    [EV-2026-08-09-111, EV-2026-08-10-618]
katman:         L8
```

`TGT_599` HoReCa HIGH'da `MAX_CIF = 5,80 TL/şişe` — **ithalatçı katkısı sıfır
iken bile.** Herhangi bir ithalatçı marjı bu hücreyi **negatife** çevirir.
**Tüm taramada bulunan tek "kırılma noktasına yakın" hücredir.**

**Varsayım gerekçesi:** HoReCa çarpanı `ASSUMPTION`'dır; tek çapa
`EV-2026-08-10-618` **T5, 14 yıllık, `ttl: 0d` → ZATEN STALE** ve çarpanı
**iki farklı katmandan** verir. `kanal.yaml` çarpanı **KDV hariç L7** üzerine
uygular — **doğrulandı ve aynen uygulandı**.

---

### B-8: Tornado'nun en büyük iki ekseni **model dışındadır**

```yaml
claim:          "MAX_CIF belirsizliginin en buyuk iki kaynagi bir VERI eksikligi degil,
                 bir KARAR eksikligidir: ithalatci katki payi ve distributor marji."
value:          "her ikisi de -108,56 TL/sise (0 -> %30 araliginda)"
unit:           TRY/sise
status:         MODEL_DERIVED
```

Vergi eksenlerinin **tamamı tek yönlüdür ve hepsi aşağı bakar**: `g` yalnızca
%70'e çıkabilir, `λ` yalnızca ≥1 olabilir. **Vergi tarafında yukarı sürpriz
YOKTUR.**
**Hacim, tornadonun en küçük eksenidir** (+20,20 TL) ve tek kişilik bir
dağıtım ekibinin maliyetinden (−64,34 TL) **üç kat küçüktür.**

---

### B-9: Sweet-spot — `PRIMARY 799` · `SECONDARY 699` · `STRETCH 899`

```yaml
claim:          "Merdiveni tirmanmak vergi yukunden KACMAZ (%41,41 -> %39,84, yalnizca
                 1,57 puan); tirmanmanin gercek kazanci SABIT TL soklarina DAYANIKLILIKTIR."
value:          "PRIMARY 799 / SECONDARY 699 / STRETCH 899 / 599 FLOOR / 999 OUT OF MANDATE"
status:         MODEL_DERIVED / ONERI
confidence:     LOW-MEDIUM
```

**Gerekçe ve tam türetme:** `sweet-spot-analizi.md`.
**Talep hakkında hiçbir iddia yoktur.**

> ⚠ **Ekonomik gerekçem, `turkiye-pazar-kasifi`'nin bağımsız pazar
> gerekçesiyle AYNI sonuca varıyor — ama bu bir DOĞRULAMA DEĞİLDİR.**
> İkisi de kısmen aynı zayıf tabana dayanmaktadır.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | `fx` (USD/TRY, EUR/TRY, EUR/USD + kur tarihi) | Bu ajanın araştırma aracı **yoktur** (kasıtlı) | **CRITICAL** | Yatırımcı/başkan girdisi → `T-852` |
| 2 | Gümrük beyan kuru kuralı | `gumruk-vergi-uzmani` TUR 2.5'te kapatmadı | HIGH | `T-911` |
| 3 | `MAX_FOB_TRY` / `MAX_EXW_TRY` ve döviz karşılıkları | (1) ve (2)'ye bağlı | **CRITICAL** | `T-912`/`T-852` kapanınca **tek adımda** |
| 4 | Gerçek EXW/FOB tedarikçi fiyatı | 26/26 tedarikçiden teklif yok | **CRITICAL** | Gerçek RFQ — `T-466`, `T-467` |
| 5 | Yatırımcı minimum katkı payı / walk-away eşiği | Karar eşikleri `TBD` | **CRITICAL** | `OQ-901` → `T-851` |
| 6 | Dış distribütör marjı | Hiçbir kanıt bulunamadı | **CRITICAL** *(A/B kararı için)* | `T-604` |
| 7 | Listeleme bedeli `f` | Resmî raporda bile karartılmış | HIGH | `T-604` |
| 8 | `d` (tekel + HoReCa) | Yalnız zincir için bant var | HIGH | `T-856` |
| 9 | Varış local charge'ları (USD) — TL karşılığı | `fx` `null` | HIGH | `T-912` |
| 10 | Menşe local charge — 9 menşenin 8'inde **tutar da yok** | Yalnız İspanya bilinir | HIGH | `T-312` |
| 11 | Fire/zayi oranı ve `f × KDV_ithal` | — | MEDIUM | `T-314` |
| 12 | Antrepo bekleme süresi ve maliyeti | — | **CRITICAL** | `T-301` |
| 13 | Bandrolleme operasyon birim maliyeti | — | MEDIUM | `T-314` |
| 14 | Devreden KDV **finansman maliyeti** (RC4) | `makro.finansman.*` `null` | MEDIUM | Faiz oranı girdisi |
| 15 | Gözetim eşiği | Negatif arama sonucu | HIGH | `EV-2026-08-09-125` yeniden aranmalı |
| 16 | 2027 ÖTV tutarı (`λ`) | Gelecek Yİ-ÜFE bilinmez | **CRITICAL** | Bilinemez — yalnız duyarlılık; `T-104` |
| 17 | `l8_chain_retail` (gerçek zincir rafı) | Fiziksel mağaza turu yapılmadı | **CRITICAL** | `T-603`, `T-917` |
| 18 | Hedef merdivenin hangi **L8 alt katmanı** olduğu | — | HIGH | `T-701` → `T-859` |
| 19 | İtalya navlunu (LCL **ve** FCL) | 14 lane'in 14'ünde kotasyon yok | HIGH | `T-916` |
| 20 | FCL navlunu (İspanya dışı 8 rota) | — | **CRITICAL** *(ileri model)* | `T-304` |
| 21 | 10.000 şişe hacim senaryosu lojistiği | Lojistik tablosunda satır yok | MEDIUM | `T-855` |
| 22 | `peak_cash_requirement` **tutarı** | Gerçek CIF + antrepo süresi + fiili vade + fx yok | **CRITICAL** | TUR 3 |
| 23 | Ruhsat kademe eşiğinin tam tanımı (litre bazı) | `ruhsat.yaml` "<=20.000 litre/yil" — hangi litre? | HIGH | `T-858` |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A | Kaynak B | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-851** | `CLAUDE.md` §6: **L3** = CIF + **vergi öncesi yurt içi masraflar** | `ters-model-vergi-bacagi.md` §4.3 + R6: aynı masraflar **L5 kalemidir** | **Aynı kalem iki farklı katmana yerleştiriliyor** → çift sayım veya hiç saymama riski | **OPEN** |
| **C-852** | `master-commercial-input-table.md` §5.3: *"fx olmadan ters model **`CIF_TRY`'ye kadar** çalışır"* | L2↔L5 arasındaki **varış local charge'ları USD cinsindendir** ve düşülemez | Hüküm **kesin** ifade edilmiş; gerçekte yalnızca **ÜST SINIR** hesaplanabilir | **OPEN** |

Ayrıntı: `99-ops/_parts/celiskiler-finans-fizibilite-tur25.md`
*(`99-ops/celiskiler.md` bu ajan tarafından **değiştirilmemiştir**.)*

---

## 5. MODEL GİRDİLERİ

> **`80-model/inputs/*.yaml` dosyalarına HİÇBİR YAZMA YAPILMAMIŞTIR.**
> Aşağıdakiler **talep**tir, yapılmış değişiklik değildir.

| YAML | Alan | Talep | status | Ticket |
|---|---|---|---|---|
| `makro.yaml` | `fx.usd_try`, `fx.eur_try`, `fx.eur_usd` + `kur_tarihi` | tarihli tek kur + LOW/BASE/HIGH bandı | `UNKNOWN` | **`T-852`** |
| `makro.yaml` | `enflasyon.*` (Yİ-ÜFE varsayımı) | `λ` ekseni için `ASSUMPTION` | `UNKNOWN` | `T-104` 2. ayağı |
| `vergi.yaml` | `mense_tarife_eslemesi.ulkeler` | **`MD` satırı ekle** (`rate:70`, `preferential_regime:null`) | engine **DÜ FALLBACK**'e düşüyor | **`T-853`** |
| `kanal.yaml` | `duyarlilik_senaryolari.d_geri_akan_bedeller_pct` | tekel + HoReCa için **yapısal karar** | `UNKNOWN` | **`T-856`** |
| `ruhsat.yaml` | tarihe bağlı kalemler için `gecerlilik_ufku` yapısı | bandrol/TADAB/ruhsat 2027'de geçersiz | — | **`T-858`** |
| `senaryolar.yaml` | `duyarlilik_eksenleri[FX]`, `[FREIGHT]`, `[PRICE]` | min/base/max hâlâ `null` | `UNKNOWN` | `T-852` |
| `senaryolar.yaml` | `hedef_raf_fiyati_merdiveni.l8_alt_katmani` | **yeni alan** (değeri `UNKNOWN` bile olsa) | yok | **`T-859`** |
| `lojistik.yaml` | 10.000 şişe satırı | `V10K` çalıştırılamadı | yok | **`T-855`** |

**evidence_id'si olmayan satır modele giremez** — bu kural **ihlal edilmemiştir.**

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `mevzuat-ruhsat-uzmani` | **Bandrol (2,36073) her 1 Ocak'ta Yİ-ÜFE ile güncellenir** (`EV-2026-08-09-213`). Üç hedef tarihin **üçü de 2027'dedir** → hedef tarihte **yürürlükte olmayacaktır.** ÖTV için `T-921` ile **kod düzeyinde** uygulanan kural bandrol için **yoktur** | Model 2026 değerini kullanmak zorunda kaldı; **aynı tarih hatasını taşıyor.** Aynı risk `TADAB` ve `ruhsat sabit maliyeti` için de geçerli olabilir |
| `mevzuat-ruhsat-uzmani` | Ruhsat sabit maliyetinin **20.000 lt/yıl kademesi**, 25.000 → 50.000 şişe geçişinde ölçek kazancının **%96'sını yiyor** | Bir mevzuat kaleminin **ölçek stratejisini belirlediği** tek yer |
| `navlun-lojistik-uzmani` | Ters modelde **navlun senaryosu `MAX_CIF_TRY`'yi HİÇ değiştirmez** (navlun CIF'in içindedir). `C-311`'in ters model etkisi **SIFIRDIR** | `T-304`'ün aciliyeti **ileri model** ve **FOB pazarlığı** içindir; yeri netleşti |
| `navlun-lojistik-uzmani` | §4 tablolarının **TRY sütununun rota-bağımsız** olduğu varsayıldı | Doğru değilse 9 ülkenin 8'inde TR-içi bacak yanlıştır → `T-854` |
| `gumruk-vergi-uzmani` | `g`'nin 2027'de değişmeyeceği varsayımı ÖTV kuralıyla **asimetriktir** — ajan bunu kendisi itiraf etmiştir. `otv_zaman_serisi.py` deseni `gumruk_vergisi_oranlari_by_mense` için **aynen yeniden kullanılabilir** | `ttl: 90d` → **2026-11-08'den sonra STALE**; hedef tarih 2027 |
| `turkiye-pazar-kasifi` | Hedef merdivenin hangi **L8 alt katmanı** olduğu `UNKNOWN` (`T-701`). Ters model çıktısının **anlamı** buna bağlıdır | Metro cash & carry zincirden ucuzdur (`K3`) → aynı hedef, farklı katmanda **farklı zorluk** |
| `kanal-marj-uzmani` | R5 düzeltmesinden sonra **TEKEL tavanı zincirden %11,4 yüksek** çıkıyor ve **farkın tamamı** `d`'nin tekelde `0` alınmasından geliyor | İki kanal arasında ekonomik tercih **modelden okunamaz** → `T-856` |
| `seytanin-avukati` | **13 maliyet kaleminin 13'ü de `0`** alınmıştır ve **13'ü de aynı yönde saptırır.** Ayrıca **kendi bulduğum `R5` hatası da projenin lehineydi** | `MAX_CIF`'in "pozitif ve rahat" görünmesinin **yapısal nedeni** budur |

`99-ops/_parts/capraz-ipuclari-finans-fizibilite-tur25.md`'ye de yazıldı.

---

## 7. AÇILAN / KAPANAN TICKET'LAR

### 7.1 Cevaplanan

| ticket_id | target_agent | impact | yeni status | ne yapıldı |
|---|---|---|---|---|
| **`T-921`** | finans-fizibilite | **CRITICAL** | **`ANSWERED`** | 5 kabul kriterinin 5'i karşılandı; ufuk denetimi koda geçti |
| **`T-751`** | finans-fizibilite | **CRITICAL** | **`ANSWERED`** | 5 kabul kriterinin 5'i karşılandı; **TV-1…TV-10 = 10/10**; ayrıca **R5 eksik sayımı** bulundu ve düzeltildi |
| `T-922` | finans-fizibilite | HIGH | **`ANSWERED`** | KDV hariç merdiven türetildi; `L1`–`L7` kuralları uygulandı; çapraz çarpım koşuldu |
| `T-702` | finans-fizibilite | HIGH | **`ANSWERED`** | TARGET/OBSERVED ayrımı korundu; merdiven **bant** olarak koşuldu, 599 **downside** |
| `T-104` | finans-fizibilite | CRITICAL | **kısmen** — birinci ayak (`T-921`) kapandı | ikinci ayak (`makro.yaml` Yİ-ÜFE) **hâlâ açık** |
| `T-153` | finans-fizibilite | MEDIUM | **`ANSWERED`** (`T-921` kapsadı) | `model_hedef_tarihi_status != FACT` denetimi eklendi |

### 7.2 Açılan

| ticket_id | target_agent | claim (kısa) | impact | status |
|---|---|---|---|---|
| **`T-851`** | `yatirim-komitesi-baskani` | `TARGET`/`ACCEPTABLE`/`WALK-AWAY` **üretilemez** — `OQ-901` açık; yalnız `MAXIMUM STRUCTURAL BUY PRICE` üretildi | **CRITICAL** | OPEN |
| **`T-852`** | `yatirim-komitesi-baskani` | `fx` bir **yatırımcı girdisidir**, bu ajanın araştırabileceği bir şey değil; `MAX_FOB`/`MAX_EXW`'yi **tek adımda** açar | **CRITICAL** | OPEN |
| **`T-853`** | `gumruk-vergi-uzmani` | Moldova ülke listesinde **yok** → **DÜ FALLBACK**; sonuç tesadüfen doğru | MEDIUM | OPEN |
| **`T-854`** | `navlun-lojistik-uzmani` | TR-içi TRY bacağının **rota-bağımsızlığı** doğrulanmalı; Moldova karayolu | HIGH | OPEN |
| **`T-855`** | `navlun-lojistik-uzmani` | `V10K` için lojistik satırı **yok** → hacim senaryosu çalıştırılamadı | MEDIUM | OPEN |
| **`T-856`** | `kanal-marj-uzmani` | `d` tekel/HoReCa'da **`UNKNOWN` → 0**; tekel tavanı **%11,4 yapay olarak yüksek** | HIGH | OPEN |
| **`T-857`** | `yatirim-komitesi-baskani` | En dayanıklı basamak (999) **mandanın dışında**; 900 `ESTIMATE` tavanı teyit/revize edilmeli | HIGH | OPEN |
| **`T-858`** | `mevzuat-ruhsat-uzmani` | (a) ruhsat 20.000 lt kademesi ölçek eğrisini kesiyor (b) bandrol 2027'de **yürürlükte olmayacak** | HIGH | OPEN |
| **`T-859`** | `turkiye-pazar-kasifi` | Hedefin hangi **L8 alt katmanı** olduğu `UNKNOWN` → çıktının **anlamı** belirsiz | HIGH | OPEN |

### 7.3 Açılan çelişkiler

| conflict_id | Konu | Durum |
|---|---|---|
| **`C-851`** | L3 katman tanımı — CLAUDE.md §6 ↔ ters-model spesifikasyonu (**çift sayım riski**) | OPEN |
| **`C-852`** | *"fx olmadan `CIF_TRY`'ye kadar çalışır"* ↔ USD cinsli varış masrafları (**yalnız ÜST SINIR**) | OPEN |

---

## 8. TAZELİK

| evidence_id | ttl | STALE tarihi | Model etkisi |
|---|---|---|---|
| `EV-2026-08-10-301,-302,-303,-305,-306,-307,-308,-309,-310,-311` (**10** LCL kartı) | **6d** | **2026-08-17** | TR-içi lojistik TRY bacağı → `MAX_CIF`'te **±0,93 TL**. **Model 2026-08-10'da koşuldu → BUGÜN GEÇERLİ** (`P-3` sağlandı) |
| `EV-2026-08-10-304` (İtalya "kotasyon yok") | 14d | 2026-08-25 | LCL kotasyonu **DEĞİLDİR**. Sayım **11 değil 10** (`T-801`/`T-923`) |
| `EV-2026-08-10-329`, `-330` (türev) | 14d | 2026-08-25 | **Kaynak kartlar STALE olunca türev de STALE** → fiilen 2026-08-17 |
| `EV-2026-08-09-111` (ÖTV 71,2692) | 30d | **2026-09-08** | Modelin **çapası**; geçerliliği zaten **2026-12-31'de** biter |
| `EV-2026-08-09-103/-104/-105` (gümrük oranları) | 90d | **2026-11-08** | İthalat Rejimi Kararı **yıllıktır**; hedef tarih 2027 → **hiçbiri hedef tarihte doğrulanmış değil** |
| `EV-2026-08-09-213`, `-234`, `-235` (bandrol/ruhsat/TADAB) | — | **2027-01-01'de fiilen** | Yİ-ÜFE endeksli; **hedef tarihte geçersiz** → `T-858` |
| `EV-2026-08-10-616`, `-617`, `-621` | 1y | 2027-08-10 | Asgari ücret **fiilen 2026-12-31'de** eskir |
| `EV-2026-08-10-618`, `-619`, `-620` (T5) | **0d** | **ZATEN STALE** | Yalnız `ASSUMPTION` bandı olarak kullanıldı; **hiçbiri değer olarak modele girmedi** |
| `EV-2026-08-10-702` (yoğunluk eğrisi) | 30d | 2026-09-09 | Sweet-spot §2 alıntısı |

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

> ### **KDV indirim hakkının alkolde kısıtlanmış olması.**

Ters modelin **ekonomik dalının tamamı**, ithalatta ödenen KDV'nin
**indirilebilir** ve dolayısıyla **ekonomik maliyet olmadığı** sonucuna
dayanır (`EV-2026-08-10-101/-102/-103`). `gumruk-vergi-uzmani` kendisi
işaretlemiştir: **KDVK md.36 uyarınca çıkarılmış bir Cumhurbaşkanı Kararı
ARANMAMIŞTIR** (`T-151`, `OQ-G10`).

Böyle bir karar varsa: KDV ekonomik maliyet olur, `MAX_CIF_TRY` **~%22,7
düşer** (her iki menşede de aynı oran), 799/ES/CHAIN/BASE **272,83 → ~211
TL/şişe** iner, HoReCa sütununun **tamamı** negatife yaklaşır ve
**bu raporun tüm sayısal çıktısı yeniden hesaplanmalıdır.**

**Bu, saatler içinde ve ~sıfır maliyetle kapatılabilecek en yüksek getirili
kontroldür ve üç turdur yapılmamıştır.**

**İkinci en güçlü çürütücü:** **Gözetim tebliğinin var olduğunun tespiti.**
Ters modelde gözetim bir **ALT SINIR** dayatır; `eşik > MAX_CIF_TRY` olduğu
anda **çözüm kümesi boşalır** ve proje **fiyat pazarlığıyla kurtarılamaz**.

**Üçüncü:** **GTİP itirazı — köpüklü (2204.10).** ÖTV 53,4519 →
**361,1360 TL/şişe**. `MAX_CIF` `g=0,50`'de **−205,12 TL** düşer →
**599, 699 ve 799 basamaklarının üçü de negatife iner** (272,83 − 205,12 =
67,71 → 799 hariç hepsi ölür; 599 ve 699 kesinlikle negatif).

### 9.2 En kırılgan varsayımım hangisi ve neden?

> ### **13 maliyet kaleminin `0` alınması.**

Bu tek tercih `MAX_CIF_TRY`'yi *"pozitif ve rahat"* gösteren şeydir.
Yönü **muhafazakâr değil, iyimserdir** ve **13'ünün 13'ü de aynı yöne bakar.**

5.000 şişe / 799 TL / ES / CHAIN BASE, tavan **272,83 TL**:

| Eklenen kalem | Yeni tavan | Kayıp |
|---|---|---|
| Kendi dağıtım, **1 kişinin asgari ücret tabanı** | 208,49 | −64,34 |
| + ÖTV λ = 1,5625 (iki adım × %25) | 188,45 | −84,38 |
| + distribütör marjı %15 (grid noktası) | ~134 | −139 |
| + listeleme bedeli 10 TL/şişe | ~127 | −146 |

**Dört kalem, hepsi kanıtsız veya yatırımcı kararı, tavanı %53 siliyor.**
Hiçbirini modele koymadım çünkü hiçbirinin kanıtı yok — **ama koymamak da bir
seçimdir ve bu seçim projenin lehinedir.**

> **Bu turda kendi bulduğum `R5` hatası da tam olarak bu yöndeydi** (B-2):
> tavanı %10,6 fazla gösteriyordu. **İki bağımsız iyimserlik kaynağının aynı
> modelde bulunması bir desen olabilir.** `seytanin-avukati` buradan
> başlamalıdır.

**İkinci en kırılgan:** **`X_pre = 0`.** `ters-model-vergi-bacagi.md` §4.3
bunu **türetmiştir**, bir gümrük müşavirine **doğrulatmamıştır.**

**Üçüncü:** **TR-içi lojistik TRY bacağının rota-bağımsız olduğu varsayımı**
(`T-854`). Tablo İspanya→İstanbul için üretilmiştir; ben onu **9 ülkeye**
uyguladım.

### 9.3 Hangi kaynağıma en az güveniyorum?

| Sıra | Kaynak | Neden |
|---|---|---|
| **1** | **`EV-2026-08-10-618`** — HoReCa çarpanı | **T5**, **14 yıllık**, çarpanı **iki farklı katmandan** verir, `ttl: 0d` → **ZATEN STALE**. HoReCa sütununun tamamı bunun üzerinde |
| **2** | **`d` bandı (3/8/18%)** | `kanal-marj-uzmani`: *"BU BANDIN SEVİYE KANITI YOKTUR — tek dayanağı kalem sayısıdır"*. **R5 düzeltmesinden sonra bu band tornadonun 4. büyük eksenidir** — yani en zayıf girdi artık en etkili girdilerden biri |
| **3** | **`m_tekel` bandı (12/18/25%)** | *"BANDIN HİÇBİR NOKTASININ KANITI YOKTUR"* — `C-602` açık |
| **4** | **`EV-2026-08-09-405`** (gözlenen CIF birim değerleri) | `global-sourcing-kasifi` **iki turdur** Comtrade birim kodu yorumunu kapatmadığını itiraf ediyor. §10.3'ün tamamı buna dayanıyor |
| **5** | **`EV-2026-08-09-234`** (ruhsat sabit maliyeti) | `ESTIMATE`; `haric_tutulan_kalemler` **`UNKNOWN`** ve *"toplam sabit maliyeti YUKARI çekecektir"*. **Ölçek eğrisi bulgusunun (B-5) tek dayanağı** |

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

| Bulgu yanlışsa | Değişen karar |
|---|---|
| **`MAX_CIF` pozitif** yanlışsa (KDV indirilemezse / gözetim eşiği varsa / köpüklü GTİP) | **`KILL` ihtimali doğrudan masaya gelir.** Bu turun tek "iyi haber"i ortadan kalkar |
| **Ölçek eğrisi düzleşmesi** (B-5) yanlışsa | 25.000 üstü hacim hedefleri **yeniden değerlendirilir**. Şu an model *"25.000'in üstünde büyümek `MAX_CIF`'i neredeyse hiç değiştirmez"* diyor → **`SCALE` kararının ekonomik gerekçesini zayıflatıyor** |
| **`R5` düzeltmem** yanlışsa (yani `d` gerçekte ithalatçı maliyeti değilse) | Tavanlar **%10,6 yükselir**; sıralama değişmez ama **seviye ve tekel/zincir karşılaştırması** değişir |
| **Tercih kaybının %11,765'i** (B-4) yanlışsa | Menşe stratejisi değişir — ama bu **cebirsel bir özdeşliktir**; ancak `g` değerleri yanlışsa yanlış olur |
| **Sweet-spot 799** yanlışsa | Hedef fiyat seçimi değişir; bu bir **öneridir**, karar başkanındır |
| **HoReCa 599/5× ölü** (B-7) yanlışsa | Kanal karması kararı değişir — ama çarpanın kaynağı **zaten en güvenmediğim kaynaktır** |

### 9.5 Bunu doğrulamak için ne gerekir?

| # | Doğrulama | Kim | Nasıl | Süre | Maliyet |
|---|---|---|---|---|---|
| **1** | **KDVK md.36 CB kararı taraması** (§9.1) | `gumruk-vergi-uzmani` | Mevzuat taraması | **saatler** | ~0 |
| **2** | **`fx` — tarihli tek kur + bant** | **yatırımcı / başkan** | Tek kayıt | **dakikalar** | ~0 |
| **3** | **Gözetim tebliği yeniden taraması** | `gumruk-vergi-uzmani` | Tebliğ listesi | saatler | ~0 |
| **4** | **Yatırımcı minimum katkı eşiği** (`OQ-901`) | **yatırımcı** | Karar | dakikalar | 0 |
| **5** | **`l8_chain_retail` — fiziksel mağaza turu** | `turkiye-pazar-kasifi` | ≥2 şehir, ≥20 SKU, foto | **1–2 hafta** | ≈0 TL |
| **6** | **`R5` düzeltmesinin bağımsız denetimi** | `seytanin-avukati` | `EV-2026-08-10-612`'yi okuyup `d`'nin kimin maliyeti olduğunu teyit | saatler | 0 |
| **7** | **Gerçek RFQ (≥5 tedarikçi)** | `global-sourcing-kasifi` | Dış iletişim izni | 2–3 hafta | orta |
| **8** | **Tek gerçekleşmiş ithalat beyannamesi + fatura seti** | başkan / sektör teması | 4 ithalatçı grubu isimlendirilmiş | 1–2 hafta | düşük |

> ### KALDIRAÇ NOTU
> **1, 2, 3, 4 ve 6 numaralı doğrulamaların beşi de bir gün içinde ve
> ~sıfır maliyetle yapılabilir.** Birlikte:
> - `MAX_CIF`'in **%22,7 çökmesi riskini** kapatır (#1),
> - `MAX_FOB` / `MAX_EXW`'yi **açar** ve **ülke ayrıştırmasını çalıştırır** (#2),
> - tavanın bir **alt sınırla test edilmesini** sağlar (#3),
> - `TARGET`/`ACCEPTABLE`/`WALK-AWAY`'i **üretilebilir** kılar (#4),
> - modelin **kendi düzeltmesini bağımsız denetler** (#6).
>
> **Ters modelin bugünkü en büyük beş boşluğu, en ucuz beş adımla
> kapatılabilir durumdadır.** Bu asimetri TUR 6'ya taşınmalıdır.

---

## 10. BU TURDA YAPILMAYANLAR (SINIR BEYANI)

| Yapılmadı | Neden |
|---|---|
| İleri (forward) profitability modeli | Kapsam dışı — `exw`/`fob` `null` (`T-466`) |
| Contribution margin · break-even · ROI · IRR | **Kapsam dışı — açıkça yasaklandı** |
| Gerçek supplier profitability · tedarikçi tavsiyesi | Kapsam dışı; teklif yok |
| `peak_cash_requirement` **tutarı** | Gerçek CIF + antrepo süresi + fiili vade + fx yok. **Yalnız R9 nakit örtüsü** (tavanda) gösterildi |
| Yatırım kararı · gate açma/kapatma | **Başkanın alanı** |
| Web araması / yeni kanıt | **Bu ajanın araçları YOKTUR — kasıtlıdır** |
| `80-model/inputs/*.yaml` yazma | Girdiler diğer ajanların; **okundu, yazılmadı** |
| `10-evidence/`, `99-ops/{capraz-ipuclari,celiskiler,acik-sorular}.md`, `tickets/INDEX.md` | **DOKUNMA listesi** |
| `git` çalıştırma | Yasak |
