# AJAN RAPORU — `finans-fizibilite` · TUR 3A

```yaml
ajan:             finans-fizibilite
tur:              TUR 3A — MODEL AUDIT + ROUND-TRIP ASSERTIONS
tarih:            2026-08-10
kapsam:           model butunlugu (yeni karlilik modeli DEGIL)
durum:            DRAFT                # APPROVED OLAMAZ — acik CRITICAL ticket
yeni_arastirma:   YOK
yeni_evidence:    YOK
yeni_sayi:        YOK — hicbir tavan degismedi
ana_belge:        80-model/outputs/model-integrity-raporu.md
```

---

## 1. BU TURDA NE YAPILDI — ÜÇ CÜMLE

1. **`T-619` çözüldü.** `T-942`'nin önerdiği kanal round-trip assertion'ının
   **tersten çalıştığı** çalıştırılarak doğrulandı ve **doğru zincir**
   kuruldu; yanlış spesifikasyon **kalıcı bir negatif vektör** olarak
   kilitlendi.
2. **Sessiz atlama (silent omission) mimari olarak sonlandırıldı.**
   26 kalem artık `0` sayılmıyor; `BLOCKED_INPUT` damgasıyla **adıyla ve
   eksik alanıyla** çıktıya basılıyor.
3. **Hiçbir sayı değişmedi.** 2.700 satırın 22 sayısal sütununun tamamı
   TUR 2.5 ile **birebir aynıdır.**

---

## 2. GELEN ÜÇ SONUCUN MODELE İŞLENMESİ

### 2.1 KDV — `(A) CONFIRMED` (`T-171`)

| Kalem | Sonuç |
|---|---|
| `MAX_CIF_TRY` etkisi | **0,00 TL/şişe** — tavanlar **yeniden hesaplanmadı** |
| Gerekçe değişikliği | ~~"md.36 kararı YOK"~~ → **"md.36 kararı VAR (7846) ama bu ürüne DEĞMİYOR"** |
| Koşullu kilit | ✅ Engine'de **koşullu dal** olarak uygulandı (`md36_indirilemeyen_kdv_oku`) |
| Tetikleyici bugün | `G1 OR G2 OR G3 = false` → `kdv_ekonomik_maliyet = 0` |
| Tetiklenirse | **MAKTU kalem** olarak `(1+gv)` bölmesinden **ÖNCE** çıkarılır (`R7c`); `D` girdisi **yok** → model **`UNKNOWN`** döner, tahmin etmez |
| **`%22,7` düzeltmesi** | ✅ **YAPILDI** — üç çıktıda (`rapor-tur25-finans.md`, `sweet-spot-analizi.md`) tam-kısıt varsayımı olduğu ve 7846'nın **kısmi** kısıt getirdiği yazıldı |

> **Önemli epistemik nokta:** Bu, "risk yok" demek değildir. Bu, "risk
> **bugün** tetiklenmiyor" demektir. `ttl 30d` (`stale: 2026-09-09`) ve
> model hedef tarihi **2027**'dir. Bulgu **hedef tarihte doğrulanmış
> değildir** ve çıktı bunu her satırda yazar.

### 2.2 Gözetim — `NO APPLICABLE MEASURE`

`gozetim.birim_kiymet_esigi.status` artık `UNKNOWN` değil **`N/A`**.
Engine'in eski uyarı metni (*"cif_try_max BİR ALT SINIRLA TEST
EDİLMEMİŞTİR"*) **kaldırıldı**; yeni metin `vergi.yaml`'dan **okunur**,
koda gömülmez. `reverse-price-model.md` §11 `SUPERSEDED` işaretlendi.

**`CIF_TRY_max` üzerinde hukuki bir alt sınır YOKTUR.** Kalan kıymet
riski GK md.23–31 idari takdiridir ve **modellenmemiştir**.

### 2.3 `T-619` — `R8-K` tersten çalışıyordu

Ölçülen (`f = 6,00` tabanı):

| `L5_max` | `T-942` birebir | **DOĞRU `R8-K`** |
|---|---|---|
| **DOĞRU** `= L7_eff = 499,3750` | `725,48` → ⛔ **RED** | `799,0000` → ✅ **KABUL** |
| **NAİF** `= L6 = 549,3207` | `799,0000` → ✅ **KABUL** | `878,9130` → ⛔ **RED** |

Doğru zincir (`L6` **hiç kullanılmaz**):
```
K1'  L7_eff_geri = L5_max + mu_kesintisi + m_dist_kesintisi + iade_kaybi
K2'  L8_net_geri = L7_eff_geri / (1 - m)        [HORECA: * k]
K3'  L8_geri     = L8_net_geri * (1 + v)
```

---

## 3. GÖREV 3 — HANGİ YAPISAL DÜZELTME UYGULANDI, HANGİSİ GİRDİ BEKLİYOR

| Ticket | Yapısal değişiklik | Bu turda | Girdi durumu |
|---|---|---|---|
| **`T-619`** | doğru `R8-K` zinciri | ✅ **TAM UYGULANDI** | girdi gerekmiyor (cebir) |
| **`T-613`** | `d` → `d_var` + `D_fix` ayrımı | ⚠ **YAPI KURULDU**, `D_fix` alanı engine'de var ve test ediliyor | ⛔ `D_fix_total` **UNKNOWN** → `BLOCKED_INPUT`. Sepetin ayrışması TUR 7. |
| **`T-614`** | `L6_gross` + vade finansmanı | ⚠ **`L6_gross` HESAPLANIYOR ve TEST EDİLİYOR** (`651,3587` ≠ `L6 542,7989`) | ⛔ `makro.finansman_orani = null` → finansman satırı `BLOCKED_INPUT` + `VADE_MALIYETI_MODELLENMEDI` bayrağı |
| **`T-615`** | `Q_ithal ≠ Q_satilan` | ⚠ **AYRILDI**, `Q_satilan = Q_ithal·(1−r)` test edildi | ⛔ `r` **UNKNOWN** → `FIRE_SIFIR_VARSAYILDI` bayrağı; `geri_kazanilabilir_deger` **BLOCKED** |
| **`T-616`/`T-944`** | `μ` matrahı | ✅ **ÜÇ MATRAH KODLANDI ve TEST EDİLDİ**; `μ≠0` & matrah `null` → **`UNKNOWN`** | ⛔ **`INVESTOR_DECISION_REQUIRED`** (`OQ-620`/`D-03`) |
| **`T-617`** | MODEL A `A1`/`A2` | ✅ **KİLİT KURULDU** — `d_kimde` boşsa `UNKNOWN`; `A2`+`d>0` → `CIFT_SAYIM` | ⛔ `d_kimde` **BLOCKED** (`C-611`) |
| **`T-611`/`T-612`** | `f`/`d` KDV'si, HoReCa menü KDV'si | ⚠ **`BLOCKED_INPUT` olarak GÖRÜNÜR KILINDI** (HoReCa'da her koşuda basılıyor) | ⛔ `gumruk-vergi-uzmani` alanı |
| **`T-618`** | TR-içi lojistiğin teslim noktası | ⚠ Kalemin `not_` alanına **çift sayım riski yazıldı** | ⛔ `navlun-lojistik-uzmani` alanı |

> **Girdisi olmayan hiçbir kalem tahminle doldurulmadı.**
> Yapı kuruldu, alan açıldı, test yazıldı — **sayı üretilmedi.**

---

## 4. PRIMARY `799` HEDEFİ DEĞİŞTİ Mİ?

## **HAYIR.**

`799,90 TL` PRIMARY hedefi **değişmedi**. `TGT_799 · ES · CHAIN · BASE ·
5.000 şişe · DOC_OK` tavanı **272,83 TL/şişe** olarak **aynen durmaktadır.**

Değişen tek şey **tavanın taşıdığı damgadır**:

```
TUR 2.5 :  272,83  ·  STATUS = MODEL_DERIVED_UPPER_BOUND
TUR 3A  :  272,83  ·  STATUS = DRAFT_MODEL_DERIVED_UPPER_BOUND_BLOCKED_INPUT
                     ·  BLOCKED_INPUT_COUNT = 26
                     ·  R8K_ROUNDTRIP_OK = EVET
```

> `kanal-marj-uzmani`'nın ölçtüğü, bugün `0` alınan kanal kalemlerinin
> mertebesi (`K7` + `K11` + `K12` ≈ **85 TL/şişe**) bu 26 kalemin
> **içindedir** ve **hepsi tavanı aşağı çeker.** Yani `272,83` bir tahmin
> değil, **bir üst sınırın üst sınırıdır** — ve bu artık çıktının kendisinde
> yazılıdır.

---

## 5. SAYISAL ÖZET

| Ölçü | Değer |
|---|---|
| Kapsamdaki maliyet kalemi (CHAIN / TEKEL / HoReCa) | **35 / 38 / 40** |
| `OK` (düşülüyor) | **4** |
| `BLOCKED_INPUT` | **26 / 29 / 31** |
| `EXCLUDED_WITH_REASON` | **5** |
| Eklenen test | **30** |
| Geçen test | **30 / 30** |
| Eski test (`TV-1`…`TV-10`) | **10 / 10** |
| `R8` başarısız satır (2.700 üzerinde) | **0** |
| **`R8-K` başarısız satır (2.700 üzerinde)** | **0** |
| Ana round-trip farkı (5 yapılandırma) | **0,00000000 TL** |
| `MAX_CIF` değişimi | **0,00 TL/şişe** |

---

## Bu bulguyu ne çürütür?

### Hangi tek girdinin yanlış olması sonucu tersine çevirir?

**`kanal-katman-matrah-haritasi.md` §9'un kapalı formül setinin kendisi.**
Bu turda kurulan doğrulama mimarisi o spesifikasyonu **test etmez**,
**onunla test eder.** `R8-K`'nın kanıtladığı tek şey **iç tutarlılıktır**:
model kendi cebriyle çelişmiyor. Cebrin **gerçeğe** karşılık geldiğini
kanıtlamaz. `L7_eff = L6·(1−d) − f` ticari gerçekte böyle işlemiyorsa,
30/30 geçen paket **yanlış bir dünyayı tutarlı biçimde** tarif eder.

Bu, `T-942`'nin uyardığı tuzağın **bir üst katıdır**: o *"doğrulama yok"*
diyordu; buradaki risk **"doğrulama var ama yanlış şeyi doğruluyor"**dur —
ve bu ikincisi **daha tehlikelidir**, çünkü artık "test edilmiş" damgası
vardır.

**İkinci aday:** `d`'nin matrahının `L6` olduğu tespiti. `CRM/B2B`
kaleminin matrahı **kasa çıkışı cirosu**, yani `L8` olabilir (`B-8`).
Öyleyse `d·L6` **sistematik eksik sayımdır** — ve **`R8-K` bunu göremez**,
çünkü `R8-K` `d`'yi zaten `L6` matrahında varsayar.
**Bir round-trip kendi varsayımını test edemez.**

**Üçüncü aday:** `m_retail = %25`. Tek kanıtlı çapa Migros'un **tüm
kategori** %24,31'idir ve **şarap değildir**. `m = %35`'te `MAX_CIF`
`272,83 → ~176` (`−%35`) olur — bu turda düzeltilen her şeyden **büyük**
bir etki, ve **tek bir ASSUMPTION'dan** geliyor.

### Modelde çift sayım riski nerede?

| Yer | Neden `LEDGER_UNIQUENESS` yakalayamaz |
|---|---|
| **`K6a`** — `d` içindeki lojistik bedeli ↔ `L5`'teki TR-içi lojistik | İki kalemin **`kalem_kimligi` farklı**. Aynı ekonomik olay, **iki ad**. İsim denetimi bunu göremez; ancak `payer`+`receiver`+`layer` **çakışma denetimi** görebilirdi — ve o denetim **yazılmadı**, çünkü `BLOCKED` kalemlerin bu alanları zaten boş. **`T-618` AÇIK.** |
| **`K6d`** — `m_dist` ↔ `d + f` | ✅ Kilit kuruldu (`d_kimde` boşsa `UNKNOWN`), ama `A1`/`A2` **seçimi için kanıt yok** |
| **`K6b`** — `d` içindeki erken ödeme iskontosu ↔ vade finansman satırı | İkisi de bugün `BLOCKED_INPUT` → risk **uykuda**, ama biri doldurulduğu an **uyanır** |
| **`K6c`** — üreticiden alınan pazarlama katkısı ↔ `f` | Aynı para hem gelir hem gider; **`T-605` AÇIK** |
| `L3` ↔ `L5` | ✅ `EXCLUDED_WITH_REASON` ile kapatıldı |

### Hangi ASSUMPTION'lar sonucu taşıyor?

`m_retail = %25` · `d = %8` · `L8 = 799` · ÖTV `λ = 1` (2027) ·
KDV `(A) CONFIRMED` (`ttl 30d`, **2026-09-09'da bayatlıyor**).

**Ve bir tanesi bir ASSUMPTION bile değil — bir SUNUM KARARI:**
`BLOCKED` kalemlerin `0` sayılmaması **ama modele de girmemesi**.
Damga bu boşluğu **görünür** kılar; **doldurmaz.** Sayı hâlâ 26 kalem
eksik hesaplanıyor ve **eksikliğin yönü tek taraflı: aşağı.**
Bu 26 kalem kapandığında tavan **yalnızca düşebilir.**

### Bu turun kendi en zayıf noktası

**30/30 geçen bir test paketi, güven kaynağı olduğu kadar risk
kaynağıdır.** Yazılan 30 testin tamamı **tek bir ajanın** cebir anlayışına
dayanıyor ve beklenen değerlerin tamamı **tek bir kaynaktan**
(`kanal-marj-uzmani`'nın spesifikasyonu) geliyor. **Bağımsız ikinci bir
uygulama yoktur.**

Tek gerçek bağımsızlık `INV::L6_ZINCIRDE_YOK` testidir — çünkü bir sayıyı
değil bir **yapısal özelliği** sınar (`L5_max` sabitken `d` ve `f`
değişse de `L8_geri` sabit kalmalı) ve beklenen değerini
spesifikasyondan almaz.

**`seytanin-avukati`'na öneri: saldırıya bu test paketinden başlayın,
modelin sayılarından değil.**
