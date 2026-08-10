# MARGIN vs MARKUP ve KDV TABANI — NETLEŞTİRME

```yaml
ajan:   kanal-marj-uzmani
tur:    TUR 2
tarih:  2026-08-10
durum:  DRAFT
amac:   "Bu repoda 'marj' kelimesinin tek anlamli hale getirilmesi. Bu dosya bir
         SOZLESMEDIR: 70-kanal ve 80-model altindaki her marj sayisi bu tanimlara
         uymak zorundadir."
```

---

## 1. İKİ TANIM — BİRBİRİNİN YERİNE GEÇMEZ

```
gross margin on selling price   m = (satış − alış) / SATIŞ
markup on purchase price        k = (satış − alış) / ALIŞ
```

**Dönüşüm:**

```
k = m / (1 − m)          m = k / (1 + k)
```

### 1.1 Dönüşüm tablosu (ezberlenmesi gereken tablo)

| margin `m` | markup `k` | çarpan (satış/alış) |
|---|---|---|
| %10 | %11,11 | 1,111× |
| %12 | %13,64 | 1,136× |
| %15 | %17,65 | 1,176× |
| %18 | %21,95 | 1,220× |
| %20 | %25,00 | 1,250× |
| **%24,31** *(Migros 2025)* | **%32,12** | **1,321×** |
| %25 | %33,33 | 1,333× |
| %30 | %42,86 | 1,429× |
| %35 | %53,85 | 1,538× |
| %40 | %66,67 | 1,667× |
| %50 | %100,00 | 2,000× |
| %66,7 | %200,0 | **3,000×** *(HoReCa BASE)* |
| %80 | %400,0 | **5,000×** *(HoReCa HIGH)* |

### 1.2 Hatanın büyüklüğü — neden bu dosya var

> "Market %40 marj alır" cümlesi **iki farklı fiyat üretir**:
>
> - margin olarak okunursa: alış 100 → satış **166,67**
> - markup olarak okunursa: alış 100 → satış **140,00**
>
> Fark **%19,0**'dur. Bir fizibilitede %19'luk sistematik sapma, KILL ile
> IMPORT PILOT arasındaki farktır. Bu yüzden `M1` kuralı bağlayıcıdır.

**Karışıklığın yönü öngörülebilir:** Perakendeci "marjım %X" derken genellikle
**margin on selling price** kasteder (muhasebe brüt kâr marjı böyledir). Tedarikçi ve
distribütör "üstüne %X koyuyorum" derken **markup** kasteder. **İkisi aynı masada
farklı şey söylerler.** Görüşme notlarında hangisi olduğu **sorulmadan yazılmamalıdır**.

---

## 2. KDV TABANI — İKİNCİ EN SIK HATA

### 2.1 Üç ayrı taban vardır

| Taban | Nerede kullanılır | Bu projede |
|---|---|---|
| **KDV hariç (net)** | İthalatçı–perakendeci faturası, muhasebe brüt marjı, sözleşme müzakeresi | **MARJ HESABININ TEK GEÇERLİ TABANI** |
| **KDV dahil (brüt)** | Tüketici raf etiketi, HoReCa menü fiyatı | Yalnızca `L8` sunumunda |
| **ÖTV dahil / hariç** | İthalat maliyet zinciri | `gumruk-vergi-uzmani` alanı — bu dosyada **kullanılmaz** |

### 2.2 BAĞLAYICI KURAL

> **Bu repoda tüm kanal marjları KDV HARİÇ tabandan hesaplanır.**
> `L8` KDV dahil olarak gözlenmişse, marj hesabına girmeden önce
> `L8_haric = L8_dahil / (1 + t_kdv)` ile netleştirilir.
> `t_kdv` bu ajanın alanı değildir; `vergi.yaml`'dan alınır.

### 2.3 Neden KDV dahil marj hesaplamak yanlış sonuç vermez ama YANILTIR

Oransal olarak, alış ve satışın **ikisi de** aynı KDV oranıyla brütleştirilirse
`m` değişmez:

```
m_dahil = (S(1+t) − A(1+t)) / (S(1+t)) = (S−A)/S = m_haric      ✓
```

**AMA** üç durumda kırılır ve bu üç durum bu projede **hepsi mevcuttur**:

1. **Karışık taban.** Alış KDV hariç (fatura), satış KDV dahil (raf etiketi) okunursa
   marj **yapay olarak şişer**. Bu, raf fiyatından geriye marj türetirken yapılan
   klasik hatadır.
2. **Farklı KDV oranı.** Ürün KDV oranı ile HoReCa hizmet KDV oranı aynı olmayabilir.
   Aynı olup olmadığı `gumruk-vergi-uzmani` alanıdır; bu ajan **varsaymaz**.
3. **Mutlak tutarlar.** Listeleme bedeli, kırık ürün bedeli, lojistik bedeli **TL
   tutarlarıdır**; bunlar KDV'li mi KDV'siz mi faturalanıyor sorusu marjı oransal değil
   **mutlak** olarak kaydırır. `EV-2026-08-10-610`: bu bedeller **hizmet faturası** ile
   alınmaktadır → KDV'ye tabidir → **KDV'si indirilebilirse ekonomik maliyet değildir,
   ama nakit çıkışıdır** (CLAUDE.md §6 KDV iki perspektifi).

### 2.4 Metro'ya özel taban uyarısı — `İP-503` ve `İP-551`

- `İP-503`: Metro'nun **ticari dili KDV hariç**, **etiket dili KDV dahildir**
  → ithalatçı–Metro pazarlığındaki sayılar büyük olasılıkla **KDV hariç** konuşulur.
- `İP-551` (`EV-2026-08-10-503`): Metro'nun arşiv **şarap** kataloglarında fiyatlar
  **KDV hariç + KDV'li çiftli** basılmış; KDV hariç sayı ondalıklı (131,36), KDV'li sayı
  yuvarlak (155,00) → Metro şarapta **brüt (KDV'li) fiyattan geriye** çalışıyor olabilir.
- `C-551` bu nedenle **AÇIKTIR**: 599,90 TL'nin KDV dahil olduğu bir `ESTIMATE`'tir,
  `FACT` değildir.

> **Model kuralı:** 599,90 TL'nin KDV durumu belirsiz olduğu için, bu sayıdan geriye
> hesaplanan **her** marj/fiyat, `BM_A` (KDV dahil) ve `BM_B` (KDV hariç) senaryolarında
> **ayrı ayrı** çalıştırılmalıdır. Tek senaryo çalıştırmak `C-551`'i sessizce çözmek olur.

---

## 3. ÖRNEK HESAP — SEMBOLİK, GERÇEK FİYAT DEĞİLDİR

> **UYARI:** Aşağıdaki sayılar **illüstratiftir**. Girdi olarak alınan `L8` bir
> **hedef**tir, gözlenmiş bir fiyat değildir. `pazar.yaml → K5` gereği 599,90 TL
> hedef olarak kullanılamaz; burada da kullanılmamıştır. `t_kdv` sembolik olarak
> `%20` alınmıştır **yalnızca aritmetiği göstermek için** — gerçek oran
> `vergi.yaml`'dan gelir ve bu ajanın alanı değildir.

### 3.1 Ters hesap (chain retail, BASE senaryo)

```
GİRDİ (hedef, kanıt değil):
  L8_kdv_dahil        = 700,00 TL/şişe        ← İLLÜSTRATİF HEDEF
  t_kdv               = %20                   ← SEMBOLİK (vergi.yaml alanı)
  m_retail            = %25   margin on selling price, KDV hariç, L7→L8
  d                   = %8    fatura cirosu üzerinden geri akan bedeller
  f_per_bottle        = 6,00 TL/şişe          ← listeleme bedeli / yıllık hacim

ADIM 1  L8 netleştir
        L8_kdv_haric = 700,00 / 1,20                      = 583,33 TL

ADIM 2  Perakendeci marjını çıkar  (margin, markup DEĞİL)
        L7_effective = 583,33 × (1 − 0,25)                = 437,50 TL
        [markup ile yapılsaydı: 583,33 / 1,25 = 466,67 TL → +29,17 TL HATA]

ADIM 3  Sabit bedelleri geri ekle
        437,50 + 6,00                                     = 443,50 TL

ADIM 4  Oransal bedelleri brütleştir
        L6 (fatura fiyatı) = 443,50 / (1 − 0,08)          = 482,07 TL

ÇIKTI:  L6 = 482,07 TL/şişe (KDV hariç, fatura)
        L7_effective = 437,50 TL (perakendecinin FİİLİ maliyeti)
        L6 − L7_effective = 44,57 TL  ← kanalın bizden aldığı TOPLAM BEDEL (%9,2)
```

### 3.2 Aynı hedefte üç senaryonun ürettiği L6 (duyarlılık)

| Senaryo | `m_retail` | `d` | `f` | **L6 (TL, KDV hariç)** | BASE'e göre |
|---|---|---|---|---|---|
| LOW (bize iyi) | %18 | %3 | 0,00 | **493,13** | +2,3% |
| **BASE** | %25 | %8 | 6,00 | **482,07** | — |
| HIGH (bize kötü) | %35 | %18 | 15,00 | **480,69** | −0,3% |

> **Bu tablonun okunması gereken şey şudur:** Üç senaryo tesadüfen benzer `L6`
> üretmiştir çünkü etkiler **ters yönde birikmiştir** (yüksek `m_retail` `L7`'yi
> düşürür, yüksek `d` `L6`'yı yükseltir). **Bu bir güven işareti DEĞİLDİR.**
> Gerçek risk, üç parametrenin **aynı yönde** kötüleşmesidir. `finans-fizibilite`
> tek tek değil, **korelasyonlu** senaryo çalıştırmalıdır.
>
> Ayrıca: hedef `L8`'in kendisi **UNKNOWN**'dır (`pazar.yaml → l8_chain_retail`).
> `L8` ±%15 kayarsa `L6` da yaklaşık ±%15 kayar — yani **modeldeki en büyük
> belirsizlik marj değil, hedef raf fiyatıdır** (→ `T-603`).

### 3.3 HoReCa örneği — çarpan mantığı

```
GİRDİ:  L7_horeca = 450,00 TL (KDV hariç, ithalatçıdan HoReCa'ya fatura)
        k_horeca  = 3,0×  (BASE, ASSUMPTION, EV-2026-08-10-618)

Menü fiyatı (KDV hariç) = 450,00 × 3,0                  = 1.350,00 TL
Menü fiyatı (KDV dahil, t=%20 SEMBOLİK) = 1.350 × 1,20  = 1.620,00 TL
HoReCa'nın margin on selling price'ı = (1350−450)/1350   = %66,7
HoReCa'nın markup'ı                  = (1350−450)/450    = %200,0
```

> **DİKKAT:** `EV-618`'in kendisi çarpanı bir yerde *"perakende fiyatının 2 katı"*,
> başka bir yerde *"toptan fiyatının 2,5 katı"* olarak verir. Bunlar **farklı
> katmanlardır** (`L8` vs `L7`). Yukarıdaki hesap **`L7` üzerinden** yapılmıştır.
> Çarpan `L8` üzerinden uygulanırsa sonuç **tamamen farklıdır**. Her HoReCa
> çarpanı yazılırken **hangi katmanın katı** olduğu belirtilmek zorundadır.

---

## 4. "PERAKENDECİ MARJI" ≠ "TEDARİKÇİNİN TOPLAM YÜKÜ"

Rekabet Kurumu'nun brüt marj metodolojisi (`EV-2026-08-10-611`) satın alım maliyetinden
*ciro primi + aktivite primi + iade tutarı + ürün imha bedeli + iskonto faturaları*'nı
**düşer**. Yani yayımlanan zincir brüt marjı, tedarikçiden alınan bedelleri **zaten
içerir**.

```
tedarikçi_toplam_yükü  =  m_retail  +  d  +  f/L6
                          ────────     ───    ─────
                          fiyat marjı   oransal  sabit
                                        bedeller bedeller
```

> **ÇİFT SAYIM UYARISI (`İP 5.1`, global-sourcing-kasifi):** Üreticiden alınabilecek
> "marka/pazarlama katkısı" (RFQ 5.6) ile buradaki listeleme bedeli **aynı satırda
> netleştirilmelidir**. Aksi hâlde aynı para hem gelir hem gider olarak iki kez
> modele girer. `T-605` bu amaçla açılmıştır.

---

## 5. HER MARJ SATIRI İÇİN ZORUNLU ŞABLON

Bu repoda bir marj yazılacaksa **aşağıdaki altı alan eksiksiz** olmalıdır:

```yaml
deger:                 # sayı
katmanlar:             # ör. "L7 -> L8"   (ZORUNLU)
brut_mu_net_mi:        # BRUT | NET       (ZORUNLU)
kdv_dahil_mi:          # HARIC | DAHIL    (ZORUNLU)
margin_mi_markup_mi:   # MARGIN_ON_SELLING_PRICE | MARKUP_ON_PURCHASE_PRICE (ZORUNLU)
status:                # FACT | ESTIMATE | ASSUMPTION | UNKNOWN
evidence_id:           # yoksa modele giremez
```

**Bu altısı tam değilse sayı geçersizdir ve `finans-fizibilite` tarafından
reddedilmelidir.**
