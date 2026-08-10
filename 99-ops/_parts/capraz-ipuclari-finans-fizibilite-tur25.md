# ÇAPRAZ İPUÇLARI — finans-fizibilite · TUR 2.5

```yaml
ajan:   finans-fizibilite
tur:    TUR 2.5 — REVERSE TARGET MODEL
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md DOKUNMA listesindedir ve DEGISTIRILMEMISTIR.
         Bu dosya, baskanin merge edecegi PARCA kayittir.
         BUNLAR SONUC DEGILDIR, IPUCUDUR — hicbiri baska bir ajanin alaninda
         KARAR uretmez."
```

---

## İP-F1 → `mevzuat-ruhsat-uzmani` · **BANDROL 2027'DE YÜRÜRLÜKTE OLMAYACAK**

`ruhsat.yaml → bandrol_fiyat_endeksleme`: *"her yıl 1 Ocak'tan geçerli olmak
üzere önceki yıl Yİ-ÜFE oranı"* (`EV-2026-08-09-213`, **T1**).
`vergi.yaml → meta.tarih_senaryolari`: **üç hedef tarihin üçü de 2027'dedir.**

> **`2,36073 TL` hedef tarihte yürürlükte olmayacaktır.**
> ÖTV için `T-104`/`T-921` ile **kod düzeyinde** uygulanan "gelecek değer
> yazma / ufuk denetimi" kuralı **bandrol için yoktur** ve model 2026
> değerini kullanmak zorunda kalmıştır.

**Neden önemli:** Sayısal etkisi küçüktür (`MAX_CIF` üzerinde 1,57 TL taban,
%25 artışta −0,39 TL) — ama **aynı disiplin ihlali `TADAB hizmet bedeli`
(0,1587) ve `toplam_ruhsat_sabit_maliyeti` (150.839 / 253.372 TL) için de
geçerli olabilir** ve orada etki **çok daha büyüktür**.
→ ticket **`T-858`**

---

## İP-F2 → `mevzuat-ruhsat-uzmani` · **BİR MEVZUAT KADEMESİ ÖLÇEK STRATEJİSİNİ BELİRLİYOR**

`toplam_ruhsat_sabit_maliyeti` **20.000 litre/yıl** eşiğinde kademe atlıyor:
**150.839 → 253.372 TL** (`EV-2026-08-09-234`). 20.000 lt = **26.667 şişe**.

Ters modelde `MAX_CIF_TRY` (799 TL · İspanya · CHAIN BASE):

| Hacim | `MAX_CIF_TRY` | Geçiş | değişim |
|---|---|---|---|
| 5.000 | 272,83 | — | — |
| 25.000 | 290,51 | 5.000 → 25.000 | **+17,68 TL** |
| 50.000 | 291,28 | **25.000 → 50.000** | **+0,77 TL** |
| 100.000 | 293,03 | 50.000 → 100.000 | +1,75 TL |

> **Ölçek ekonomisinin %87'si ilk sıçramada gerçekleşiyor ve bunun sebebi
> navlun değil, bir RUHSAT KADEMESİ.** Bu, modeldeki başka hiçbir kalemin
> üretmediği bir etkidir ve **`SCALE` kararının ekonomik gerekçesini
> doğrudan zayıflatmaktadır.**

→ ticket **`T-858`** (a)

---

## İP-F3 → `navlun-lojistik-uzmani` · **`C-311` TERS MODELDE ETKİSİZDİR**

Okyanus navlunu ve sigorta **CIF'in İÇİNDEDİR** (GK md.27/1-e,
`EV-2026-08-09-120`). Ters model CIF **tavanını** üretir; navlun o tavanın
**nasıl bölüşüleceğini** belirler, tavanın **kendisini** değil.

> **FCL bandının 4 kat olması (`C-311`) `MAX_CIF_TRY`'yi SIFIR etkiler.**
> Navlunun ters modeldeki tek görünür etkisi **TR-içi TRY bacağıdır** ve o da
> 5.000 şişede tavanı yalnızca **±0,93 TL** oynatır.

**Sonuç:** `T-304` (CRITICAL) **ileri model** ve **FOB pazarlığı** için
blokerdir; **ters model için değildir.** Bu, `T-304`'ün aciliyetinin **nereye
ait olduğunu** netleştirir — aciliyeti düşürmez, **yerini değiştirir.**

---

## İP-F4 → `navlun-lojistik-uzmani` · **MOLDOVA'YA DENİZ MANTIĞI UYGULANDI**

Moldova havuzdaki **tek karayolu erişimli menşedir**. Ters modelde ona da
liman tabanlı TR-içi bacak (ardiye, devanning, THD içeren türev) uygulandı —
çünkü elimizde başka bir yapı yok.

**Bu muhtemelen yanlıştır** ve Moldova'nın gerçek TR-içi maliyeti farklı
kalemlerden oluşur (kara gümrük kapısı, TIR, ordino yapısı).
→ ticket **`T-854`** madde 2

---

## İP-F5 → `gumruk-vergi-uzmani` · **`g` İÇİN ASİMETRİ SÜRÜYOR**

Ajanın kendi itirafı (`ters-model-vergi-bacagi.md` §13.1):
*"ÖTV için titizlikle uygulanan 'gelecek değer yazma' kuralı, gümrük vergisi
oranı için de geçerlidir ve bu belge `g`'yi 2027'de değişmez varsayarak bir
ASİMETRİ taşımaktadır."*

**Model bu asimetriyi aynen taşımaktadır.** İthalat Rejimi Kararı **yıllıktır**;
`ttl: 90d` → **2026-11-08'den sonra STALE.** Üç hedef tarihin üçü de 2027'dedir
→ **§4'teki `g` değerlerinin hiçbiri hedef tarihte doğrulanmış değildir.**

**İpucu:** ÖTV için yazılan `otv_maktu_zaman_serisi` yapısının (gözlenen
değerler + `son_gozlem_gecerlilik_ufku` + `gelecek_deger_kurali` +
`engine_okuma_kurali`) **bire bir muadili `gumruk_vergisi_oranlari_by_mense`
için de kurulabilir** ve engine tarafı **hazırdır** (`otv_zaman_serisi.py`
deseni yeniden kullanılabilir).

---

## İP-F6 → `turkiye-pazar-kasifi` · **TERS MODEL ÇIKTISININ ANLAMI L8 ALT KATMANINA BAĞLI**

`MAX_CIF_TRY = 301,78 TL/şişe` sayısı, hedefin `L8_METRO_CASH_CARRY`'de mi
`L8_CHAIN_RETAIL`'de mi olduğuna göre **aynı sayı ama farklı anlam** taşır
(`K3`: cash & carry yapısı gereği zincirden ucuzdur).

Ayrıca model, kanal marj bandını (`m_retail` %18/25/35) **zincir perakende**
varsayımıyla uyguladı. Hedef aslında bir cash & carry fiyatı ise, uygulanması
gereken marj yapısı **farklıdır** — `kanal.yaml`'ın kendi gerekçesi cash &
carry formatını marjı **aşağı çeken** bir faktör olarak sayar.
→ ticket **`T-859`**

---

## İP-F7 → `kanal-marj-uzmani` · **TEKEL'İN %11 ÜSTÜNLÜĞÜ BİR ARTEFAKTTIR**

`MAX_CIF_TRY` (799 TL · ES · DOC_OK · 5.000 şişe · BASE):
**CHAIN 272,83** vs **TEKEL 303,90** → tekel **+%11,4**.

**Farkın TAMAMI**, `d` (geri akan bedeller) bandının **yalnız zincir için**
tanımlı olmasından ve tekelde **`UNKNOWN` → 0** alınmasından gelir.

> **Bu bir bulgu değildir. İki `ASSUMPTION` ile bir `UNKNOWN`'ın çarpımıdır.**
> Tekelde de bir tür geri akış (iskonto, ciro primi, vade farkı, teşhir
> desteği) varsa fark **kapanır veya tersine döner.**
> İki kanal arasında ekonomik tercih **modelden okunamaz.**

→ ticket **`T-856`**

---

## İP-F7b → `gumruk-vergi-uzmani` · **TERS MODELİN ALTINCI HATASI (kanal bacağında)**

`ters-model-vergi-bacagi.md` §6, ters modelde yapılması en muhtemel **beş**
hatayı listeler (`H1`…`H5` + `H6` ikincil). **Altıncısını bu turda kendim
yaptım, buldum ve düzelttim:**

```
H7 (onerilen ad) — "L5_max = L6" alinmasi
YANLIS:  L5_max = L6 x (1 - mu)
DOGRU:   L5_max = L7_eff - mu x L6      (L7_eff = L6(1-d) - f)
BUYUKLUK: 799 TL / ES / CHAIN BASE'te  -28,95 TL/sise  (H1: -17,82 ; H3: -22,22)
YONU:     PROJENIN LEHINE (tavani yukseltir) -> gozden kacmasi DAHA OLASI
```

**Neden sizin listenizde yok:** `H1`…`H6` **vergi bacağının** hatalarıdır;
bu hata **kanal bacağındadır** (R2–R5) ve o adımların sahibi
`kanal-marj-uzmani` + `finans-fizibilite`'dir.

**Öneri:** §6'ya, sınırın **kendi dışında** kalan bu hatayı işaret eden bir
satır eklenmesi — çünkü `R7`'nin girdisi olan `L4_econ_max`'ın doğruluğu
**tamamen R5'e bağlıdır** ve `R8` round-trip assertion'ı bu hatayı
**YAKALAYAMAZ** (round-trip yalnızca `L4_econ_max ↔ CIF` tutarlılığını test
eder, `L4_econ_max`'ın kendisinin doğru olup olmadığını değil).

> **`R8`'in kör noktası budur ve kayda geçirilmelidir.**

---

## İP-F8 → `seytanin-avukati` · **SALDIRILACAK EN VERİMLİ TEK NOKTA**

Modelde **13 maliyet kalemi `0` alınmıştır** ve **13'ünün 13'ü de aynı yönde
(yukarı) saptırır**:

varış local charge (USD) · menşe local charge (EUR) · müşavirlik CIF kademesi ·
listeleme bedeli `f` · `d` (tekel + HoReCa) · fire/zayi KDV'si ·
antrepo bekleme · bandrolleme operasyonu · devreden KDV finansman maliyeti ·
distribütör marjı · ithalatçı katkı payı · gözetim eşiği · ÖTV λ > 1

**Somut yıkım senaryosu** (5.000 şişe · 799 TL · İspanya · CHAIN BASE,
tavan **272,83 TL**):

| Eklenen | Yeni tavan | Kayıp |
|---|---|---|
| Kendi dağıtım, 1 kişinin **asgari ücret tabanı** | 208,49 | −64,34 |
| + ÖTV λ = 1,5625 | 188,45 | −84,38 |
| + distribütör marjı %15 | ~134 | −139 |
| + listeleme bedeli 10 TL/şişe | ~127 | −146 |

**Dört kalem tavanı %53 siliyor.** Hiçbirini modele koymadım çünkü hiçbirinin
kanıtı yok — **ama koymamak da bir seçimdir ve o seçim projenin lehinedir.**

> **DAHA DA ÖNEMLİSİ:** bu turda **kendi bulduğum `R5` hatası da tam olarak
> aynı yöndeydi** (tavanı %10,6 fazla gösteriyordu — İP-F7b).
> **İki bağımsız iyimserlik kaynağının aynı modelde bulunması bir DESEN
> olabilir.** Kırmızı takım bunu bir tesadüf saymamalıdır.

---

## İP-F9 → `gumruk-vergi-uzmani` + başkan · **EN UCUZ / EN YÜKSEK GETİRİLİ KONTROL**

**KDVK md.36 uyarınca çıkarılmış bir Cumhurbaşkanı Kararı ARANMAMIŞTIR**
(`T-151`, `OQ-G10`). Böyle bir karar varsa alkolde KDV indirim hakkı
kısıtlanmış olabilir ve:

- KDV **ekonomik maliyet** olur,
- `MAX_CIF_TRY` **~%22,7 düşer** (her iki menşede de aynı oran),
- 799/ES/CHAIN/BASE: **272,83 → ~211 TL/şişe**,
- HoReCa sütununun **tamamı** negatife yaklaşır,
- **Bu turun tüm sayısal çıktısı yeniden hesaplanır.**

> **Bu, saatler içinde ve ~sıfır maliyetle kapatılabilecek en yüksek getirili
> tek kontroldür ve üç turdur yapılmamıştır.**

---

## İP-F10 → başkan · **DÖRT UCUZ ADIM, DÖRT BÜYÜK BOŞLUK**

| # | Adım | Kim | Süre | Ne açar |
|---|---|---|---|---|
| 1 | KDVK md.36 CB kararı taraması | `gumruk-vergi-uzmani` | **saatler** | `MAX_CIF`'in %22,7 çökme riskini kapatır |
| 2 | **`fx` — tarihli tek kur + bant** | **yatırımcı/başkan** | **dakikalar** | `MAX_FOB` ve `MAX_EXW`'yi açar; **ülke ayrıştırmasını çalıştırır** |
| 3 | Gözetim tebliği yeniden taraması | `gumruk-vergi-uzmani` | saatler | Tavanın bir **alt sınırla** test edilmesini sağlar |
| 4 | **Minimum katkı eşiği** (`OQ-901`) | **yatırımcı** | dakikalar | `TARGET`/`ACCEPTABLE`/`WALK-AWAY` fiyatlarını **üretilebilir** kılar |

> **Ters modelin bugünkü en büyük dört boşluğu, en ucuz dört adımla
> kapatılabilir durumdadır.** Bu asimetri TUR 6'ya taşınmalıdır.
> `tur-25-preflight.md` §1.7 aynı asimetriyi **üçüncü kez** kaydetmişti.
