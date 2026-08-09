# OQ-001 — METRO BENCHMARK FİYATININ DOĞRULANMASI

```yaml
oq_id:            OQ-001
sorumlu_ajan:     turkiye-pazar-kasifi
tur:              TUR 1
tarih:            2026-08-09
durum:            PARTIALLY_RESOLVED
```

> **ÖZET KARAR:**
> **KDV sorusu → CEVAPLANDI: KDV DAHİL (yüksek güven, ama etiketin ince yazısı fiziksel olarak okunmadı).**
> **Promosyon sorusu → UNKNOWN (kapanmadı).**
> **Katman sorusu → KISMEN: L8'dir ama "Metro cash & carry L8"idir; zincir market L8'i DEĞİLDİR.**
>
> Bu nedenle OQ-001 **tamamen kapatılmamıştır**. `finans-fizibilite` iki senaryolu
> çalıştırmaya devam etmelidir; ancak senaryo ağırlıkları artık simetrik değildir
> (bkz. §9).

---

## 0. NE ARANDI, NEYE ERİŞİLDİ, NEYE ERİŞİLEMEDİ

| Doğrulama yolu (acik-sorular.md'deki liste) | Sonuç |
|---|---|
| 1. Mağazada etiketin tam fotoğrafı (küçük punto KDV satırı dahil) | **ERİŞİLEMEDİ** — elimizde yalnızca fiyat rakamının okunduğu foto var |
| 2. Metro kasa fişi | **ERİŞİLEMEDİ** |
| 3. Metro Türkiye fiyat gösterim politikası | **ERİŞİLDİ** — Metro'nun kendi resmî broşürleri (EV-503, EV-504) + SSS (EV-505) + kampanya koşulları (EV-508) |
| 4. Aynı SKU'nun zincir markette tüketici fiyatı | **ERİŞİLEMEDİ** — alkol online satılamadığı için Migros/CarrefourSA online'da şarap fiyatı yok (EV-511) |
| (ek) Metro online fiyatı | **ERİŞİLEMEDİ** — `guncelfiyatlar.metro-tr.com` "Size özel fiyatları görmek için Giriş Yapın" diyor; fiyatlar üyeliğe/müşteri numarasına özel |
| (ek) Metro'nun aynı dönemdeki basılı fiyat iletişimi | **ERİŞİLDİ ve OKUNDU** — 3 farklı Metro broşürü, 58 sayfa görüntü olarak indirilip incelendi |

---

## 1. SORU 1 — Fiyat KDV **dahil** mi?

**CEVAP: EVET — KDV DAHİL. (confidence: HIGH, status: ESTIMATE→FACT'e yakın ama etiket bazında FACT değil)**

**Kanıt zinciri:**

| # | Kanıt | Ne gösteriyor | tier |
|---|---|---|---|
| 1 | `EV-2026-08-09-503` | Metro Türkiye'nin **kendi** haftalık broşüründe (5–11 Ağustos 2026 — benchmark gözlem tarihini kapsayan hafta) **her fiyatın yanında küçük puntoyla `KDV'li` yazıyor.** Örn. `1.099,90 TL KDV'li` | T4 (Metro'nun kendi künyeli yayını) |
| 2 | `EV-2026-08-09-504` | Metro "Temizlik/Kişisel Bakım" broşüründe hem üstü çizili normal fiyat hem indirimli fiyat `KDV'li` | T4 |
| 3 | `EV-2026-08-09-505` | Metro Türkiye SSS: *"Herkes! ... bireysel olarak alışveriş yapmak isteyen müşterilerimiz mağaza girişlerinden günlük kart çıkarttıktan sonra..."* → Metro TR saf B2B değil, **son tüketiciye açık** | T4 |
| 4 | `EV-2026-08-09-506` | Fiyat Etiketi Yönetmeliği: perakende satış fiyatı **tüm vergiler dahil** gösterilir; **"toptan ve perakende satışların birlikte yapıldığı yerlerde, perakende satışlar hakkında bu Yönetmelik hükümleri uygulanır"** | T1 (ikincil veritabanı üzerinden okundu — T-501 ile doğrulatılacak) |

**Karşı kanıt (dürüstlük gereği):**

- `EV-2026-08-09-508`: Metro'nun **kampanya koşulları** KDV **hariç** dille yazılmış
  (*"Alım hedeflerinize KDV dahil değildir"*, *"Kazanılacak çek tutarına KDV dahildir"*).
  Yani Metro'nun **ticari/muhasebe dili net (KDV hariç)**tir.
- `EV-2026-08-09-511`: Tüketici şikâyet platformunda Metro'da raf–kasa fiyat farkı
  şikâyetleri var; bazı kullanıcılar "etikette KDV'li tutar yazmıyor" diyor. (T5, LOW)

**Çelişki nasıl çözülüyor:** Bu ikisi çelişmez. Metro'nun **hedef/ciro dili** nettir
(B2B muhasebe), **müşteriye ilan ettiği raf/broşür fiyatı** brüttür (`KDV'li`).
Aynı şirket iki farklı yerde iki farklı matrah kullanır. Benchmark bir **raf etiketi**
gözlemidir → brüt taraf geçerlidir.

**Kalan risk:** Broşür ≠ raf etiketi. Broşürün `KDV'li` yazması rafın da öyle yazdığını
%100 kanıtlamaz. **Şarap reyonu özelinde etiket görülmedi.** (bkz. §9)

---

## 2. SORU 2 — Fiyat KDV **hariç** mi?

**CEVAP: HAYIR (olasılık düşük).**

Gerekçe: Metro Türkiye'nin yayınlanmış fiyat iletişiminde KDV hariç bir fiyat
**hiç görülmedi** — 58 sayfa broşürün tamamında tek bir `KDV hariç` ibaresi yok.
Ayrıca `599,90` / `649,90` biçimindeki **`,90` ile biten psikolojik fiyatlandırma**,
Metro'nun `KDV'li` fiyatlarının bitiş deseniyle birebir aynıdır
(`1.099,90` · `299,90` · `434,90` · `364,90` · `199,90` — hepsi `KDV'li`).
KDV hariç bir taban fiyattan türetilen brüt fiyat bu kadar düzenli `,90` ile bitmez.

Bu bir **ESTIMATE**'tir, kanıt değildir; ama yön gösterir.

---

## 3. SORU 3 — Son tüketici satış fiyatı mı?

**CEVAP: EVET, aynı zamanda.**

`EV-2026-08-09-505`: Metro Türkiye'ye bireysel müşteri girebilir, ücretsiz Metro Kart
alır, **belge gerekmez**, ve o fiyattan satın alır. Yani rafta gördüğümüz 599,90 TL
bir tüketicinin fiilen ödeyebileceği fiyattır.

**AMA:** Bu, "Türkiye'de bu şarabın tüketici raf fiyatı 599,90 TL'dir" demek DEĞİLDİR.
Bu, **Metro kanalındaki** tüketici fiyatıdır. Zincir markette (Migros/Macrocenter/
CarrefourSA) aynı ürünün fiyatı **bilinmiyor** ve büyük olasılıkla daha yüksektir —
ama bu **doğrulanmadı** (`EV-511`).

---

## 4. SORU 4 — Profesyonel / cash & carry fiyatı mı?

**CEVAP: EVET, aynı anda o da.**

Metro cash & carry'de **tek fiyat** vardır: aynı raf fiyatını hem bireysel tüketici
hem bakkal/restoran öder. Fark üyelik tipine bağlı **ek indirim/çek** mekanizmalarındadır
(`EV-508`) — ancak **alkol bu kampanyaların tamamının dışındadır** (`EV-508`).

Yani şarapta profesyonel müşterinin ekstra bir kanal indirimi **görünmüyor**.
(Kart bazlı özel fiyat olup olmadığı UNKNOWN — `guncelfiyatlar.metro-tr.com`
"size özel fiyat" ifadesi kullanıyor ve giriş istiyor.)

**Kritik ek bulgu (`EV-2026-08-09-507`):** Metro broşür künyesi:
*"Broşürdeki fiyatlar **sevkiyat hizmeti alan müşterilerimiz için geçerli değildir**."*
→ Metro'nun **mağaza (cash & carry) fiyatı** ile **teslimat/HoReCa dağıtım (Metro Gastro
Servis) fiyatı** FARKLIDIR. Benchmark mağaza fiyatıdır.

---

## 5. SORU 5 — Promosyon / indirim fiyatı mı?

**CEVAP: UNKNOWN. KAPANMADI.**

- Metro'nun promosyon etiket anatomisi bilinir hâle geldi (`EV-504`):
  promosyonda **üstü çizili eski fiyat + kırmızı "AVANTAJLI FİYAT" rozeti** bulunur.
- Benchmark fotoğrafına ilişkin kayıtta üstü çizili fiyat veya rozet **bildirilmemiştir**.
- Ancak fotoğrafın kendisi bu ajan tarafından incelenmedi; `00-charter/benchmark.md`
  promosyon durumunu `UNKNOWN` olarak kaydetmiştir.
- Ayrıca `EV-2026-08-09-514`: **alkollü içki Metro broşürlerinde hiç yer almıyor**
  (reklam/kampanya tanıtımı yasağı) → şarapta broşür promosyonu zaten yapılamaz,
  ama **mağaza içi fiyat indirimi** yapılabilir. Bu ihtimal elenemedi.

**Nasıl kapanır:** Aynı SKU'nun 2–4 hafta arayla ikinci bir mağaza gözlemi.
Fiyat aynıysa normal fiyattır.

---

## 6. SORU 6 — Normal fiyat mı?

**CEVAP: UNKNOWN** (5. sorunun aynası). Tek gözlemden normal/promosyon ayrımı yapılamaz.

---

## 7. SORU 7 — METRO FİYAT ETİKETİ NASIL YORUMLANMALI?

**CEVAP (belgelendi — `EV-503`, `EV-504`):**

Metro Türkiye'nin yayınlanmış fiyat gösterimi şu bileşenlerden oluşur:

```
┌───────────────────────────────────────┐
│  4̶3̶4̶,̶9̶0̶ ̶T̶L̶  ← üstü çizili ESKİ fiyat (KDV'li)  [yalnızca promosyonda]
│                                       │
│   434 , 90 TL      ← BÜYÜK PUNTO = güncel satış fiyatı
│            KDV'li  ← küçük punto: KDV DAHİL olduğunu söyler
│                                       │
│  adet fiyatı: 12,42 TL  ← küçük punto = BİRİM FİYAT (kg/L/adet)
└───────────────────────────────────────┘
```

**En kritik nokta — OQ-001'in temel hipotezi ÇÜRÜDÜ:**

> OQ-001 şu varsayımla açılmıştı: *"Metro cash & carry'de etikette KDV hariç
> profesyonel fiyat ile KDV dahil fiyat **birlikte** gösterilebilir."*

İncelenen Metro Türkiye materyallerinde **böyle bir çiftli gösterim YOKTUR.**
Etikette görülen **ikinci sayı KDV hariç fiyat değil, BİRİM FİYATTIR**
(`kg fiyatı: 599,80 TL`, `L fiyatı: 90,20 TL`, `adet fiyatı: 12,42 TL`).
Birim fiyat gösterimi zaten Fiyat Etiketi Yönetmeliği'nin bir zorunluluğudur.

Dolayısıyla "iki fiyat gördük, hangisini okuduk?" endişesi **Metro Türkiye için
büyük ölçüde yersizdir**. 750 ml'lik bir şişede birim fiyat satırı `L fiyatı: 799,87 TL`
gibi bir şey olurdu — 599,90 ile karıştırılamaz.

**UYARI:** Bu tespit **broşür** materyaline dayanır. Fiziksel raf etiketinin
(ESL / kâğıt etiket) tam mizanpajı bu turda görüntülenemedi.

---

## 8. SORU 8 — HANGİ KATMAN? L7 mi L8 mi?

**CEVAP: L8 — ama nitelikli olarak.**

| | |
|---|---|
| **Katman** | `L8` (CONSUMER SHELF PRICE) |
| **Ama hangi L8** | `L8_METRO_CASH_CARRY` — Metro kanalının tüketici raf fiyatı |
| **Zincir market L8'i mi?** | **HAYIR.** Zincir market tüketici fiyatı `UNKNOWN` ve muhtemelen daha yüksek. |
| **L7 midir?** | Hayır — ama **L7-proxy işlevi görür**: bir bakkal/tekel bayii/restoran Metro'dan bu fiyata alıp yeniden satarsa, 599,90 TL onun **satın alma maliyetidir**. |

**Neden bu ayrım kritik:**

Ters model (`target shelf price → max EXW/FOB`) 599,90 TL'yi **zincir market tüketici
raf fiyatı** sanırsa, kendi ürününü Metro'nun **cash & carry** fiyat seviyesine
konumlandırmış olur — yani gerçekte olduğundan **daha agresif** bir hedef koyar.
Cash & carry formatı yapısı gereği zincir perakendeden ucuzdur.

**Yön:** 599,90 TL, aynı ürünün zincir market tüketici fiyatının **altında** olma
eğilimindedir. Yani gerçek "zincir raf hedefi" 599,90'dan **yüksek** olabilir —
bu proje lehine bir sapmadır. Ancak **doğrulanmamıştır** (`EV-511`).

**Model için öneri:** `benchmark.katman = L8_METRO_CASH_CARRY`, ve `L8_CHAIN_RETAIL`
ayrı bir alan olarak `UNKNOWN` kalsın. İkisi eşitlenmesin.

---

## 9. SENARYO AĞIRLIKLARI — MODELE TALİMAT

`00-charter/benchmark.md` şu an iki senaryoyu **eşit** çalıştırmayı söylüyor:

- **BM_A:** 599,90 TL = KDV **dahil**
- **BM_B:** 599,90 TL = KDV **hariç**

**Bu ajanın önerisi (karar başkanındır):**

| Senaryo | Yeni durum | Gerekçe |
|---|---|---|
| **BM_A (KDV dahil)** | **BASE CASE** | EV-503, EV-504, EV-505, EV-506 |
| **BM_B (KDV hariç)** | **SENSITIVITY** olarak korunsun, base case olmaktan çıksın | Hiçbir doğrudan kanıtı yok; yalnızca EV-508'deki "Metro'nun hedef dili net" gözlemi besliyor |
| **BM_C (YENİ)** | **EKLENSİN**: "599,90 TL promosyonlu fiyattır, normal fiyat daha yüksektir" | Soru 5 kapanmadı; bu risk BM_B'den daha gerçekçidir |
| **BM_D (YENİ)** | **EKLENSİN**: "Zincir market L8'i Metro L8'inin üzerindedir" | Soru 8; kanal formatı farkı |

---

## 10. OQ-001 DURUM KAYDI

```yaml
durum:              PARTIALLY_RESOLVED
kapanan_kisimlar:
  - soru_1_2_KDV:   "KDV DAHIL"   # confidence HIGH, evidence EV-503/504/505/506
  - soru_3:         "EVET, son tuketiciye acik"   # EV-505
  - soru_4:         "EVET, ayni anda cash&carry"  # EV-505, EV-507, EV-508
  - soru_7:         "Metro etiketinde KDV haric/dahil CIFTLI gosterim YOK; ikinci sayi BIRIM FIYAT"  # EV-503/504
acik_kalan_kisimlar:
  - soru_5_6:       "Promosyon mu normal mi -> UNKNOWN"
  - soru_8_kismi:   "Zincir market L8'i -> UNKNOWN (EV-511)"
  - etiket_bazli_dogrulama: "Sarap reyonunda fiziksel etiket goruntusu YOK"
evidence_id:        EV-2026-08-09-503, EV-2026-08-09-504, EV-2026-08-09-505, EV-2026-08-09-506, EV-2026-08-09-507, EV-2026-08-09-508
kapanis_tarihi:     null
kapatan_ajan:       null
kalan_ticketlar:    T-501 (mevzuat dogrulamasi), T-503 (reklam yasagi), T-504 (ikinci gozlem)
```

---

## 11. OQ-001'İ TAM KAPATMAK İÇİN GEREKEN (tek cümle)

**Şarap reyonundaki etiketin, küçük puntolu satırı da okunabilecek şekilde çekilmiş
ikinci bir fotoğrafı + 2–4 hafta sonra aynı SKU'nun ikinci fiyat gözlemi.**
Bu ikisi olmadan OQ-001 `RESOLVED` yapılamaz.
