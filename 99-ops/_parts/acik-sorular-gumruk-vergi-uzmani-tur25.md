# AÇIK SORULAR — `gumruk-vergi-uzmani` · TUR 2.5

> Bu tur **sınırlı bir model destek turudur**; yeni genel araştırma yapılmamıştır.
> Aşağıdakiler ters modelin vergi bacağı kurulurken **açık kalan** veya
> **yeni görünür hâle gelen** sorulardır. Devralınan açık sorular
> (`…-tur15.md`, `…-tur2.md`) burada tekrarlanmamıştır.

---

## OQ-G25-01 — `λ` (2027 ÖTV artış katsayısı) kim tarafından, nerede tanımlanacak?

**Kritiklik:** HIGH · **Bloke ettiği:** üç hedef tarih senaryosunun birbirinden
ayrışması

ÖTV, ÖTVK md.12/3 uyarınca Ocak ve Temmuz'da Yİ-ÜFE ile **kendiliğinden**
yeniden belirlenir (`EV-2026-08-09-114`). Üç hedef tarihin (2027-01-01 /
2027-04-01 / 2027-07-01) **üçü de** en az bir ayarlamanın ötesindedir.

`vergi.yaml → BASE_DATE_kurali` gelecek değer yazılmasını **yasaklar** ve bu
doğrudur. Ancak sonuç şudur: **üç senaryo da `λ=1` ile çalışacağı için ÖTV
açısından birbirinden ayrışmayacaktır.** Hedef tarih seçiminin ÖTV etkisi model
çıktısında **görünmeyecektir.**

**Kim cevaplamalı:** `yatirim-komitesi-baskani` (karar) + `finans-fizibilite`
(`makro.yaml`'da Yİ-ÜFE `ASSUMPTION`'ı, `senaryolar.yaml`'da duyarlılık ekseni).
**`gumruk-vergi-uzmani` bu sayıyı vermez ve veremez.**

---

## OQ-G25-02 — `g` (gümrük vergisi oranı) için neden ÖTV ile aynı titizlik uygulanmıyor?

**Kritiklik:** HIGH · **Tip:** metodolojik asimetri itirafı

`g = 0,50 / 0,70` değerleri **2026 İthalat Rejimi Kararı**'na aittir
(`effective_date: 2026-01-01`, `ttl: 90d`). Karar **her yıl 1 Ocak'ta
yenilenir.** Üç hedef tarihin üçü de **2027'dedir.**

Yani `g`, ÖTV ile **tamamen aynı yapısal durumdadır** ama:
- ÖTV için `otv_maktu_zaman_serisi` + `gelecek_deger_kurali` + `son_gozlem_gecerlilik_ufku` var,
- `g` için **hiçbiri yok** — model `0,50`'yi 2027'de de geçerli sayacak.

Bu bir çelişki değil, **kabul edilmiş bir tutarsızlıktır** ve gizlenmemiştir
(`ters-model-vergi-bacagi.md` §13.1, `rapor-tur25` §4).

**Neden bu turda kapatılmadı:** 2027 Kararı henüz **yayımlanmamıştır**
(2026 Aralık'ta beklenir). Yani `g` için doğrulanmış bir 2027 değeri **fiziksel
olarak mevcut değildir**. Yapılabilecek tek şey `g`'ye de bir
`gecerlilik_ufku: 2026-12-31` alanı eklemektir.

**Öneri (karar başkanındır):** `mense_tarife_eslemesi` bloğuna
`son_gozlem_gecerlilik_ufku: 2026-12-31` eklenmesi ve engine'in
`t > 2026-12-31` iken `g`'yi de `UPPER_BOUND`/`ANCHOR` etiketiyle raporlaması.
**Tarihsel yön ipucu yok:** oranların 2027'de artacağını da azalacağını da
gösteren bir kanıt bulunmamaktadır → yön bile `UNKNOWN`'dır.

---

## OQ-G25-03 — `X_pre` gerçekten sıfır mı? (damga vergisi ve md.21/c'nin idari yorumu)

**Kritiklik:** LOW (tutar) / MEDIUM (yöntem) · **Ticket:** `T-151`

Ters modelin R7 adımı `X_pre = 0` varsayar. Türetme: tescile kadarki tüm yurt
içi kalemler KDV'ye tabidir → md.21/c'nin "vergilendirilmeyenler" şartını
sağlamazlar (`EV-2026-08-10-108`).

**İki açık nokta:**
1. **Gümrük beyannamesi damga vergisi** md.21/b uyarınca KDV matrahına **girer**;
   tutarı `UNKNOWN`'dır (beyanname başına maktu → şişe başına ihmal edilebilir).
2. md.21/c'nin **idari yorumu (KDVGUT III/A)** okunmamıştır (`T-151`).

**En ucuz kapanış:** tek bir gerçekleşmiş gümrük beyannamesinde KDV matrahı
satırının `CIF + GV + ÖTV` toplamına **eşit** olup olmadığının gözlenmesi.
Bu, `master-commercial-input-table.md` §7'nin işaret ettiği yolla **aynı**dır.

---

## OQ-G25-04 — `T-911` (gümrük kuru) bu turda kapatılmadı

**Kritiklik:** HIGH · **Ticket:** `T-911` (OPEN, target: bu ajan)

Ters model `CIF_TRY_max` ve `FOB_TRY_max` üretebilir ama **döviz cinsinden
azami satın alma fiyatını üretemez.** Bunun için iki ayrı şey gerekir:
- `makro.yaml → fx` (`T-912`, `finans-fizibilite`/başkan),
- **gümrük beyanında hangi kurun, hangi tarihte esas alınacağı** (`T-911`, bu ajan).

`T-911` bu turda **bilinçli olarak kapsam dışı bırakılmıştır** (TUR 2.5 görev
tanımı: "yeni genel araştırma yapma"). **Bu, bir eksiklik olarak kayda geçmiştir**
ve ters modelin R11 adımını bloke eder.

> ⚠️ **T-911, ters modelin "segment matematiksel olarak mümkün mü" sorusunu
> cevaplamasının önündeki SON vergi engelidir.** `CIF_TRY_max` hesaplandıktan
> sonra onu gözlenen menşe CIF birim değerleriyle (USD/lt) karşılaştırmak
> için kur kuralı gerekir.

---

## OQ-G25-05 — ÖTV nispi oranının %0 olduğu tekrar doğrulanmalı mı?

**Kritiklik:** MEDIUM · **Tip:** tek nokta bağımlılığı

Ters formülün **tamamı** `nispi ÖTV = %0` üzerine kuruludur
(`EV-2026-08-09-110`, `effective_date: 2026-07-03`). Oran > 0 olsaydı denklem
parçalı-doğrusal olur ve tek bölmeyle çözülemezdi.

Bu tek kanıt, ters modelin **en yüksek kaldıraçlı tek girdisidir** — yanlışsa
sadece bir sayı değil, **formülün yapısı** yanlış olur.

**Öneri:** `EV-2026-08-09-110`'a `ttl: 30d` ve **yüksek öncelikli yeniden
doğrulama** etiketi. (Kanıt kartları immutable'dır; yeniden doğrulama yeni bir
kart ile yapılır.)

---

## OQ-G25-06 — Gözetim eşiği `null` iken ters modelin çıktısı ne kadar güvenilir?

**Kritiklik:** MEDIUM · **Ticket:** yok (TUR 1'den devir, `EV-2026-08-09-125`)

Ters model bir **üst sınır** üretir. Gözetim bir **alt sınır** dayatır. İkisi
kesişmezse proje **fiyat pazarlığıyla kurtarılamaz** (`ters-model-vergi-bacagi.md` §11).

Eşik `UNKNOWN` olduğu için ters modelin çıktısı **alt sınırla test
edilmemiştir.** Model bu uyarıyı basmak zorundadır, ama uyarı bir çözüm
değildir. **Bu, bir gümrük müşavirine sorulacak ilk üç sorudan biridir.**
