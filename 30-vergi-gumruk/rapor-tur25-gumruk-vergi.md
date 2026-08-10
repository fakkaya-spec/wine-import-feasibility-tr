# AJAN RAPORU — TUR 2.5 · REVERSE MODEL VERGİ DESTEĞİ

```yaml
ajan:                 gumruk-vergi-uzmani
tur:                  TUR 2.5
tarih:                2026-08-10
durum:                SUBMITTED
gorev_tipi:           MODEL DESTEGI (yeni genel arastirma YAPILMADI)
yeni_evidence_karti:  0
yeni_dis_kaynak:      0
ana_cikti:            30-vergi-gumruk/ters-model-vergi-bacagi.md
```

---

## 1. YÖNETİCİ ÖZETİ

Bu turda yeni vergi araştırması yapılmadı; TUR 1/1.5/2'de kapatılmış bulguların
**ters (reverse) modelde cebirsel olarak doğru uygulanması** spesifikasyona
bağlandı. Ters modelin vergi bacağının tamamı tek bir satıra iner:
**`CIF_TRY_max = (L4_econ_max − ÖTV − KKDF − X_pre) / (1 + gv_oranı)`** ve bu
satırdaki **çıkarma işlemi bölmeden önce** yapılmak zorundadır — sıra ters
çevrilirse azami satın alma fiyatı menşeye göre **17,82–22,01 TL/şişe eksik**
çıkar (`EV-2026-08-09-111`, `-103`/`-104`).

En önemli tek sonuç: ters model, hiçbir `UNKNOWN` girdiye bağlı olmayan **kapalı
formlu** bir sayı üretiyor — **tercihli rejimi kaybetmek azami satın alma
fiyatını tam olarak %11,765 düşürür** (`1,50/1,70`), L8'den, ÖTV'den, marjdan ve
navlundan bağımsız olarak.

İkinci sonuç: başkanın üç hedef tarihinin (**2027-01-01 / 2027-04-01 /
2027-07-01**) **üçü de** ÖTV açısından `FUTURE_UNKNOWN` dönemine düşüyor. 2027
tutarları yazılmadı; ÖTV `λ` katsayısıyla parametrize edildi ve
`λ ≥ 1` olduğu için `λ=1` çalıştırmasının bir tahmin değil **ÜST SINIR** olduğu
kurala bağlandı (çıktı adı `cif_try_max_UPPER_BOUND`).

---

## 2. BULGULAR

### B-1: Ters model vergi bacağının kapalı formu

```yaml
claim:          Ters modelde vergi bacağı tek bölme + üç çıkarmadan ibarettir ve sıra bağlayıcıdır
value:          "CIF_TRY_max = (L4_econ_max − ÖTV − KKDF − X_pre) / (1 + gv_oranı)"
unit:           TRY/şişe
status:         FACT (türetme — girdilerin tamamı FACT)
tier:           T1
evidence_id:    EV-2026-08-09-103, -104, -105, -106, -110, -111, -115, -117; EV-2026-08-10-108
effective_date: 2026-01-01 (gv) · 2026-07-03 (ÖTV) · 2023-07-10 (KDV oranı)
katman:         L4_econ → L2
```

**Gerekçe:** İleri zincirde `L4_econ = C(1+g) + k + O`. `O` maktu ve `C`'den
bağımsız (nispi ÖTV %0, `EV-2026-08-09-110`); `g` yalnız `C` üzerinde oransal.
Denklem `C`'de birinci derecedendir ve tek adımda çözülür. **Bu sadelik tamamen
nispi ÖTV oranının %0 olmasına bağımlıdır** — oran > 0 olsaydı denklem
parçalı-doğrusal olur ve tek bölmeyle çözülemezdi.

**Türetme zinciri:** `ters-model-vergi-bacagi.md` §3 R7, adım (1)–(6).

---

### B-2: Tercihli rejim kaybının ters modeldeki **kapalı formlu** bedeli

```yaml
claim:          Tercihli tarifeyi kaybetmek azami satın alma fiyatını tam %11,765 düşürür
value:          0,88235   (= 1,50 / 1,70)
unit:           oran
status:         FACT (türetme)
tier:           T1
evidence_id:    EV-2026-08-09-103, EV-2026-08-09-104, EV-2026-08-10-157
effective_date: 2026-01-01
katman:         L2
```

**Gerekçe:** `CIF_max(g) = (A−O)/(1+g)` olduğundan iki menşenin oranı
`(1+0,50)/(1+0,70) = 0,88235`'tir ve `A`, `O` sadeleşir. **Bu, projedeki
`UNKNOWN` yoğunluğuna rağmen hesaplanabilen en dayanıklı sayıdır:** L8 hedef
fiyatı, marj, navlun, kur — hiçbiri bilinmeden geçerlidir.

**İleri yöndeki karşılığı** +24,00 TL/şişe @ CIF=100 idi
(`mense-tarife-eslemesi.md` §3.3). İkisi aynı olgunun iki yüzüdür; **işaretleri
zıttır** ve raporda karıştırılmamalıdır.

---

### B-3: ÖTV duyarlılığının ters yöndeki katsayısı

```yaml
claim:          Ters modelde ÖTV'nin azami CIF'e etkisi -1/(1+gv_oranı) katsayısıyla doğrusaldır
value:          "-0,6667 (gv %50) · -0,5882 (gv %70) TL azami CIF / +1 TL ÖTV"
unit:           TRY/TRY
status:         FACT (türetme)
tier:           T1
evidence_id:    EV-2026-08-09-110, EV-2026-08-09-111, EV-2026-08-09-113
effective_date: 2026-07-03
katman:         L2
```

**Karşı-sezgisel sonuç:** ÖTV artışı yüksek tarifeli menşede **TL olarak daha az**
azami CIF kaybettirir (0,3144 < 0,3563 TL/şişe per %1) çünkü kayıp `(1+g)` ile
bölünür. Bu bir avantaj değildir: o menşenin `CIF_max` seviyesi zaten %11,765
daha düşüktür, dolayısıyla **oransal** etki daha ağırdır.

---

### B-4: Bandrol ve TADAB hiçbir vergi matrahına girmez — **T-203 cevabı**

```yaml
claim:          Bandrol bedeli ve TADAB hizmet bedeli ÖTV/KDV matrahına ve gümrük kıymetine girmez
value:          "matrah dışı — L4→L5 geçişinde"
unit:           -
status:         ESTIMATE   (hukuki türetme; dayandığı iki kanıt T1)
tier:           T1
evidence_id:    EV-2026-08-10-108 (KDVK md.21/c) + EV-2026-08-09-213 (bandrol %20 KDV hariç)
                + EV-2026-08-09-120/-121 (GK md.27/28) + EV-2026-08-09-115 (ÖTV matrahı)
effective_date: 1985-01-01 (md.21) · 2026-01-01 (bandrol listesi)
```

**Türetme zinciri:** KDVK md.21/c yalnızca **"vergilendirilmeyen"** tescile-kadarki
gider/ödemeleri KDV matrahına alır. Bandrol bedeli Darphane listesinde
**"%20 KDV hariç"**tir → **vergilendirilendir** → md.21/c kapsamı dışındadır.
Satıcıya ödenen fiyatın parçası olmadığı için gümrük kıymetine de girmez.
ÖTV matrahı KDV matrahı unsurlarından oluştuğu için oraya da girmez.

**Neden bu `ESTIMATE` model için yeterli:** karşı senaryonun büyüklüğü
hesaplandı — bandrol KDV matrahına **girseydi** ek ÖTV **0,00** (maktu),
ek KDV **0,4721 TL/şişe**, ekonomik etki **0,00 TL** (KDV indirilebilir).
**T-203'ün `CIF_TRY_max` üzerindeki etkisi tam olarak sıfırdır** → ticket
ters modeli **bloke etmez**. (T-203 `ANSWERED` yapıldı.)

---

### B-5: Üç hedef tarihin üçü de ÖTV açısından `FUTURE_UNKNOWN`

```yaml
claim:          BASE/EARLY/LATE senaryolarının üçünde de 71,2692 TL/lt yürürlükte olmayacaktır
value:          null
unit:           TRY/litre
status:         FUTURE_UNKNOWN
tier:           T1 (mekanizma)
evidence_id:    EV-2026-08-09-114 (ÖTVK md.12/3), EV-2026-08-09-111, EV-2026-08-09-112
effective_date: -
```

**Gerekçe:** Her üç tarihten önce en az bir planlı md.12/3 ayarlaması vardır.
Gözlenen gerçek: "Ocak" ayarlaması 2025'te **31 Aralık**'ta, "Temmuz" ayarlaması
2026'da **3 Temmuz**'da yürürlüğe girdi. Buna göre **`LATE = 2027-07-01`, ikinci
adımın iki gün öncesindedir** → tescil tarihinin birkaç gün kayması ÖTV'yi bir
basamak yukarı taşır. Vergi tescilde doğduğu için (`EV-2026-08-09-122`) bu risk
`T-301` (antrepo bekleme süresi, CRITICAL) ile doğrudan bağlıdır.

**Taşıma kuralı:** `O = 53,4519 × λ`, `λ = FUTURE_UNKNOWN`, `λ ≥ 1`.
Üç senaryo da `λ=1` ile çalışır; çıktı **`UPPER_BOUND`** etiketiyle raporlanır.
`λ` için sayı seçmek bu ajanın alanı değildir (`makro.yaml` Yİ-ÜFE `ASSUMPTION`).

---

### B-6: Gözetim ters modelde **alt sınır** dayatır

```yaml
claim:          Ters model üst sınır üretir; gözetim alt sınır dayatır. Eşik > CIF_TRY_max ise çözüm kümesi boştur.
value:          null (eşik doğrulanamadı)
status:         UNKNOWN
evidence_id:    EV-2026-08-09-125
```

İleri modelde gözetim "maliyet arttı" gibi görünür ve pazarlıkla
kurtarılabilirmiş izlenimi verir. Ters modelde ise tedarikçi bedava verse bile
beyan eşiğin altına inemeyeceği için **kurtarılamayacağı hemen görülür.**
Model, eşik `null` iken *"`cif_try_max` bir alt sınırla TEST EDİLMEMİŞTİR"*
uyarısını basmak zorundadır. ÖTV maktu olduğu için gözetimden etkilenmez
(`EV-2026-08-09-113`).

---

## 3. UNKNOWN LİSTESİ (bu tura özgü — devralınanlar tekrarlanmadı)

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| U1 | `λ` — 2027 ÖTV artış katsayısı | Gelecek değer; tahmin yasak (BASE_DATE_kurali) | **HIGH** | `makro.yaml`'da Yİ-ÜFE `ASSUMPTION` + duyarlılık ekseni (başkan kararı) |
| U2 | 2027 İthalat Rejimi Kararı'nın `g` değerleri | 2026 Aralık'ta yayımlanacak | **HIGH** | 2026-12 sonrası yeniden doğrulama (`ttl: 90d`, STALE ≥ 2026-11-08) |
| U3 | `X_pre` — tescile kadarki KDV'siz gider (damga vergisi) | Tutar TUR 1'de doğrulanamadı | LOW | Gerçek bir gümrük beyannamesi / gümrük müşaviri |
| U4 | Gümrük beyanında kullanılacak **kur kuralı** | `T-911` bu turda **kapsam dışı** bırakıldı (sınırlı görev) | **HIGH** | `T-911` — sonraki turda bu ajan |
| U5 | KDVGUT III/C + KDVK md.36 CB kararı taraması | TUR 1.5'te erişilemedi | MEDIUM | `T-151` |
| U6 | 2027 bandrol birim bedeli | Alan dışı (`mevzuat-ruhsat-uzmani`) | MEDIUM | Çapraz ipucu bırakıldı |

---

## 4. ÇELİŞKİLER

**Bu turda yeni çelişki tespit edilmedi.** `C-751…C-769` bloğu kullanılmadı.

Bir **asimetri** tespit edildi ve gizlenmeden kayda geçirildi
(`ters-model-vergi-bacagi.md` §13.1): ÖTV için titizlikle uygulanan
"gelecek değer yazma" kuralı, **gümrük vergisi oranı `g` için uygulanmamaktadır.**
`g` de en az `O` kadar tarihe bağlıdır (İthalat Rejimi Kararı yıllıktır) ve üç
hedef tarihin üçü de 2027'dedir. Bu bir çelişki değil, **kabul edilmiş ve
etiketlenmiş bir tutarsızlıktır**; `seytanin-avukati` için meşru bir hedeftir.

---

## 5. TİCKET / ÇAPRAZ İPUCU

| ID | Yön | Konu |
|---|---|---|
| **T-751** (yeni) | → `finans-fizibilite` | Ters modelin vergi bacağı spesifikasyonu: bağlayıcı sıra, R8 round-trip assertion, 10 birim test vektörü |
| **T-203** | ← `mevzuat-ruhsat-uzmani` | **ANSWERED** — bandrol/TADAB matrah dışıdır; model etkisi ≤ 0,4721 TL/şişe, yalnız nakit |
| `T-911` | (bu ajana açık) | Gümrük kuru — bu turda **kapatılmadı**, sınırlı görev kapsamı dışında |
| `T-104`, `T-105`, `T-151`, `T-162` | açık | Devralındı, bu turda değişmedi |
| Çapraz ipuçları | → ruhsat / lojistik / sourcing | `99-ops/_parts/capraz-ipuclari-gumruk-vergi-uzmani-tur25.md` |

---

## 6. YAZILAN DOSYALAR

| Dosya | İçerik |
|---|---|
| `30-vergi-gumruk/ters-model-vergi-bacagi.md` | **Ana çıktı** — ters formül türetimi, 9 ülke tablosu, 6 hata + kural, ÖTV tarih senaryosu, KDV iki görünüm, 10 test vektörü |
| `30-vergi-gumruk/rapor-tur25-gumruk-vergi.md` | bu rapor |
| `80-model/inputs/vergi.yaml` → `ters_model_vergi_bacagi` | makine okunur karşılık (**yalnızca eklendi**; mevcut bloklar bozulmadı; YAML parse doğrulandı) |
| `99-ops/tickets/T-751.md` | spesifikasyon devri |
| `99-ops/tickets/T-203.md` | CEVAP bölümü dolduruldu → `ANSWERED` |
| `99-ops/_parts/capraz-ipuclari-gumruk-vergi-uzmani-tur25.md` | 3 alan dışı ipucu |
| `99-ops/_parts/acik-sorular-gumruk-vergi-uzmani-tur25.md` | 6 açık soru |

**Yeni kanıt kartı açılmadı** (yeni dış kaynak taranmadı). Tüm değerler mevcut
`evidence_id`'lere referans verir. `10-evidence/_index-parts/` altına dosya
eklenmedi.

---

## 7. BU BULGUYU NE ÇÜRÜTÜR?

### 7.1 Hangi mevzuat değişikliği bu hesabı geçersiz kılar?

- **ÖTV nispi oranının %0'dan farklı belirlenmesi.** Ters formülün **tamamı**
  `ÖTV = fiyattan bağımsız maktu sabit` varsayımına dayanır. Nispi oran > 0
  olursa `L4_econ = C(1+g) + max(r·C(1+g) ; O)` **parçalı-doğrusal** hâle gelir;
  tek bölmeyle çözülemez, iki dal ayrı çözülüp `max` koşulu doğrulanmalıdır.
  **Bu belgeyi tek başına çürütecek en temiz bulgudur.**
- **KDV indirim hakkının alkolde kısıtlanması** (KDVK md.36 uyarınca bir CB
  kararı — **aranmadı**, `T-151`). O hâlde ekonomik görünüm çöker, KDV maliyet
  olur ve `CIF_TRY_max` **~%22,7 düşer** (her iki menşede de aynı oranda).
  **Ters modelin en kırılgan tek dayanağı budur** ve
  `master-commercial-input-table.md` §7 de bağımsız olarak aynı noktayı
  işaret etmektedir.
- **2027 İthalat Rejimi Kararı.** `g = 0,50 / 0,70` değerleri **2026** yılına
  aittir; üç hedef tarihin üçü de 2027'dedir. §4'teki asimetri kaydı.
- **1/98 sayılı OKK'nın revizyonu** → tüm `1,50` bölenleri değişir.

### 7.2 Hangi GTİP itirazı tüm yapıyı değiştirir?

- **Köpüklü (2204.10) tespiti:** `O` 53,4519 → 361,1360 TL/şişe. Ters formül
  aynen çalışır ama `CIF_TRY_max`'tan `g=0,50`'de **205,1227 TL/şişe**,
  `g=0,70`'te **180,9906 TL/şişe** düşer. Fiyat/performans segmentinde
  `L4_econ_max` bu mertebeye ulaşmadığı için **`CIF_TRY_max` negatife düşer.**
  **Ters model bunu ileri modelden daha net gösterir:** negatif azami alım
  fiyatı tartışılamaz bir sonuçtur.
- **22.05 (aromatize/vermut):** `O` = 545,0441 TL/şişe → aynı mantık, daha kötü.
- **12 haneli alt kod itirazı** `g`'yi de `O`'yu da değiştirmez
  (`EV-2026-08-09-102`) → **ters formül etkilenmez.** Yapının en dayanıklı yeri.

### 7.3 Gözetim / kıymet itirazı senaryosunda ne olur?

Ters modelde gözetim bir **alt sınırdır** (B-6). `eşik > CIF_TRY_max` olduğu anda
çözüm kümesi boşalır ve **fiyat pazarlığıyla kurtarma imkânı yoktur.** ÖTV maktu
olduğu için gözetimden etkilenmez; itirazın etkisi yalnız `g` kanalıyladır ve
**DÜ menşede (%70) AB/Şili menşeye (%50) göre 1,4 kat ağırdır.** 2204.21 için
yürürlükte gözetim tebliği bulunamamıştır (`EV-2026-08-09-125`) — **ancak bu
negatif bir arama sonucudur, yokluğun kanıtı değildir.**

### 7.4 Bu raporun kendi en zayıf halkası

**`X_pre = 0` varsayımı ve bandrol türetmesi aynı hukuki bende dayanır**
(KDVK md.21/c "vergilendirilmeyenler"). O bendin **idari uygulaması (KDVGUT)
okunmamıştır** (`T-151`). Gerçek bir gümrük beyannamesinde KDV matrahı satırının
`CIF + GV + ÖTV` toplamından **büyük** çıkması, §4.2 ve §4.3'ü ve dolayısıyla R7
adımını aynı anda çürütür. **En ucuz çürütme yolu budur** ve
`master-commercial-input-table.md` §7'nin işaret ettiği tek gerçekleşmiş ithalat
beyannamesi bu testi zaten içermektedir.

### 7.5 Reddedilen kolaylığın bedeli (dürüstlük kaydı)

`λ` için bir sayı vermeyi reddettim. Bu **doğru** ama bedava değil: üç hedef
tarih senaryosu da aynı `λ=1` çapasıyla çalışacağı için **üç senaryo ÖTV
açısından birbirinden ayrışmayacaktır.** Yani hedef tarih seçiminin ÖTV etkisi
model çıktısında **görünmeyecek**, yalnızca §B-3'teki katsayı üzerinden
okunabilecektir. Bu bir eksikliktir; kapatılması `makro.yaml`'da açık bir
Yİ-ÜFE `ASSUMPTION`'ı ve başkan kararı gerektirir.
