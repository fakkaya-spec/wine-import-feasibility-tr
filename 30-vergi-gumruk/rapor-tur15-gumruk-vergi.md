# AJAN RAPORU — gumruk-vergi-uzmani · TUR 1.5 (BLOCKER REMEDIATION)

```yaml
ajan:               gumruk-vergi-uzmani
tur:                TUR 1.5 — BLOCKER REMEDIATION
tarih:              2026-08-10
base_date:          2026-08-10
durum:              SUBMITTED
kapsam:             DAR — OQ-G01 (KDV) + BASE_DATE + T-906 + T-901
kapsam_disi:        7584/reklam/raf yasagi · GTIP · gumruk vergisi orani ·
                    tercihli tarife · gozetim · navlun · ruhsat · kanal marji
```

---

## 1. YÖNETİCİ ÖZETİ

**İthalatta ödenen KDV, şarap ithalatçısı için EKONOMİK MALİYET DEĞİLDİR.**
3065 s. KDV Kanunu **md.29/1-b** (T1, yürürlük 1985-01-01) ithal olunan mallar
dolayısıyla ödenen KDV'yi açıkça indirilebilir kılar; **md.34/1** belge şartını
gümrük makbuzu + defter kaydı olarak tanımlar; **md.30**'un (indirilemeyecek KDV)
**tam metni tarandı** ve alkollü içki ticaretine özgü **hiçbir hüküm bulunmadı**.
Bu, sıradan bir negatif arama değildir — md.30 **tahdidi** bir listedir, orada
yer almamak **hukmen** yer almamaktır. **OQ-G01 (CRITICAL) KAPANMIŞTIR**
(`EV-2026-08-10-101`, `-102`, `-103`).

**Ama KDV bedava değildir.** Gümrükte gümrük vergisiyle **aynı gün** nakden
ödenir (md.46/2, T1) ve mahsubu **28–59 gün** sonra mümkün olur; devreden KDV
**nakden iade EDİLMEZ** (md.29/2, T1) — yalnız gelecek dönem hesaplanan
KDV'sinden mahsup edilir. Yani KDV, `peak_cash_requirement`'a **tam tutarıyla**
girer ve geri kazanımı **satış hızına kilitlidir**. Bu, **ÖTV'nin tam
tersidir**: ÖTV de aynı gün ödenir ama **asla geri gelmez**.

**En kritik tek bulgu:** ÖTV, KDV matrahında olduğu için (md.21/b, T1) **CIF
sıfıra gitse bile** şişe başına **10,6904 TL** KDV doğar. 12.000 şişelik bir
konteynerde bu tek başına **128.285 TL** nakit demektir — **CIF'ten tamamen
bağımsız olarak**. Maktu ÖTV'nin ucuz şarabı cezalandırma etkisi, KDV kanalından
**%20 daha büyüktür**.

**Doğrulanamayan:** TÜİK Yİ-ÜFE Aralık 2025 → Haziran 2026 değişimi (`T-901`).
TÜİK veri portalı JS-render/WAF korumalı; endeks değerlerine erişilemedi.
**`UNKNOWN` yazdım, zorlamadım.**

---

## 2. BULGULAR

### B-1: İthalatta ödenen KDV indirilebilir

```yaml
claim:          Ithalatta odenen KDV, KDVK md.29/1-b uyarinca indirilebilir
value:          true
unit:           -
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-101
effective_date: 1985-01-01
katman:         -
```

**Gerekçe:** Madde metni birebir: *"Mükellefler, yaptıkları vergiye tabi işlemler
üzerinden hesaplanan katma değer vergisinden … indirebilirler: … **b) İthal olunan
mal ve hizmetler dolayısıyla ödenen katma değer vergisi**"*. Bent (b) Kanunun
aslî metnindedir (sonradan eklenmemiştir) → yürürlük md.62 uyarınca 1/1/1985.
*"Ödenen"* ifadesi bağlayıcıdır: gümrükte fiilen ödenmemiş KDV indirilemez.

---

### B-2: İndirimin belge ve zaman şartı

```yaml
claim:          Indirim, gumruk makbuzunda ayrica gosterim + kanuni deftere kayit
                sartiyla, kaydin yapildigi vergilendirme doneminde kullanilir;
                sure siniri VDO yilini takip eden takvim yili sonudur
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-102 (md.34/1) · EV-2026-08-10-105 (md.29/3)
effective_date: 1985-01-01 (md.34) · 2019-01-01 (md.29/3, 7104 s.K.)
```

**Gerekçe:** md.34/1 belge şartını, md.47 gümrük idaresinin makbuzda gösterme
**yükümlülüğünü** kurar → şart **yapısal olarak** sağlanır, ithalatçının ekstra
bir işlem yapmasına gerek yoktur. md.29/3: 2027-03 tescili → indirim en geç
**31/12/2028**'e kadar kullanılabilir.

---

### B-3: Alkollü içkiye özgü indirim kısıtlaması YOK — ama "aramadım" ile "yok" farkı yazıldı

```yaml
claim:          KDVK md.30 tam metninde alkollu ickiye ozgu indirim yasagi YOKTUR
value:          false
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-103
effective_date: 2019-01-01
```

**Gerekçe:** md.30 bentleri: (a) istisna/vergiye tabi olmayan teslimler,
(b) binek otomobil, (c) zayi olan mallar, (d) GVK/KVK'ya göre KKEG giderler,
(e) değersiz alacaklar. **Hiçbiri alkole değinmiyor.**

**Metodolojik ayrım (kritik):** Bu bulgu `EV-2026-08-09-125`'teki gözetim tebliği
aramasından **yapısal olarak farklıdır.** md.30 tahdidi (numerus clausus) bir
listedir — *"Aşağıdaki vergiler … indirilemez"*. Burada yer almamak, bir veri
tabanında bulunamamak değil, **hukmen yer almamaktır.**

**Ne YAPMADIĞIMI da yazıyorum:** KDV Genel Uygulama Tebliği III/C bölümü,
KDVK md.36'ya dayanan CB kararları ve GİB özelgeleri **taranmadı** (erişilemedi).
→ `EV-2026-08-10-114` (`status: UNKNOWN`), ticket **T-151**.

---

### B-4: Tek pozitif kısıtlama — KVK md.11/1-(ı), ama kapsamı dar

```yaml
claim:          Alkollu icki ILAN/REKLAM giderlerinin %50'si KKEG'dir; KDVK md.30/d
                uyarinca o kisma ait KDV de indirilemez
value:          50
unit:           %
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-113
effective_date: 2006-06-21
```

**Gerekçe:** Görev, alkollü içkiye özgü bir KDV kısıtlaması **aramamı** istedi.
Bulunan **tek** pozitif hüküm budur. **Ama malın kendisine ait ithalat KDV'sini
ETKİLEMEZ** — yalnız reklam giderlerini. Ayrıca CB'nin oranı değiştirmiş olma
ihtimali (`UNKNOWN`) ve alkolde reklamın hukuken mümkün olup olmadığı
(`mevzuat-ruhsat-uzmani` alanı, bu turda kapalı) nedeniyle **modele bir maliyet
kalemi olarak GİRMEMİŞTİR.**

---

### B-5: Devreden KDV iade EDİLMEZ

```yaml
claim:          KDVK md.29/2 — devreden KDV sonraki donemlere devrolunur ve IADE EDILMEZ;
                iade istisnasi yalnizca md.28 indirimli oran teslimleri icindir
value:          false
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-104
effective_date: 2004-01-01
```

**Gerekçe:** Şarabın yurt içi teslimi **genel oran %20**'dir
(`EV-2026-08-09-118`), indirimli oran listelerinde yer almaz → md.29/2'nin iade
istisnası **uygulanmaz.** md.32 kapsamında (ihracat vb.) iade hakkı doğuran işlem
de yoktur. **Sonuç: nakit iade yolu KAPALI; geri kazanım yalnızca mahsupladır.**

**Kuyruk riski (`EV-2026-08-10-112`, T1):** 7524 s.K. md.20, **1/1/2030**'dan
itibaren KDVK md.30'a *"(f) Beş takvim yılı süresince indirim yoluyla
giderilemeyen KDV"* bendini ekliyor. BASE_DATE'te **yürürlükte değildir**;
baz senaryo parametresi değil, **kuyruk riskidir.**

---

### B-6: Ödeme → ilk mahsup gecikmesi 28–59 gün

```yaml
claim:          Ithalat KDV'sinin gumrukte odenmesi ile ilk mahsup imkani arasindaki sure
value:          28-59 (ortalama ~44)
unit:           gun
status:         ESTIMATE
tier:           T1 (turetme — tum girdiler T1/T2)
evidence_id:    EV-2026-08-10-118
effective_date: 2026-08-10
```

**Türetme zinciri:**
```
t0 = tescil gunu D              [md.10/i — EV-...-106]
     KDV + GV + OTV ayni gun    [md.46/2 — EV-...-107]
t1 = gumruk makbuzunun deftere kaydi (ayni donem)  [md.34/1 — EV-...-102]
t2 = takip eden ayin 28'i (beyan + odeme)          [GIB, T2 — EV-...-109]
     kanuni sure 24/26          [md.41/1, md.46/1 — EV-...-110, T1]
gecikme = (N - D) + 28
   D=N (ay sonu tescil) -> 28 gun
   D=1, N=31            -> 58-59 gun
   ortalama             -> ~44 gun
```

**Neden ESTIMATE:** (a) 28. gün idari uzatmaya dayanır ve sirkülerin tarihi
doğrulanamadı; (b) aylık vergilendirme dönemi **ASSUMPTION**'dır (kanuni
varsayılan 3 aydır — `T-152`); (c) tescil günü bilinmiyor.
**3 aylık dönemde gecikme 28 → ~118 güne çıkar.**

---

### B-7: Kaldırılamaz KDV tabanı — 10,6904 TL/şişe

```yaml
claim:          OTV KDV matrahinda oldugu icin CIF sifira gitse bile sise basina
                10,6904 TL KDV dogar
value:          10.6904
unit:           TRY/sise
status:         ESTIMATE
tier:           T1 (turetme)
evidence_id:    EV-2026-08-10-119
effective_date: 2026-07-03 (OTV tutarina bagli)
katman:         L4 icinde
ttl:            30d
```

**Türetme:** md.21/b (ÖTV, KDV matrahında — `EV-2026-08-10-108`, T1) ×
71,2692 TL/lt × 0,75 lt × %20 = **10,6904 TL/şişe**.

**Genel formül (peşin ödeme, KKDF=0):**
```
KDV/sise = 0,20 x ( (1 + gv_oran) x CIF + 53,4519 )
  AB/BK/Sili (%50): 0,30 x CIF + 10,6904
  DU/ABD     (%70): 0,34 x CIF + 10,6904
```

**Bu, ekonomik maliyet DEĞİLDİR** (indirilebilir) ama **gümrükte nakden ödenir.**

---

### B-8: KDV matrahı zinciri T1 tam metinle TEYİT EDİLDİ

TUR 1'de kurulan zincir (`EV-2026-08-09-117`) KDVK **md.21 tam metniyle**
doğrulandı (`EV-2026-08-10-108`, T1): matrah = **(a)** GV tarhına esas kıymet +
**(b)** *"ithalat sırasında ödenen **her türlü vergi, resim, harç ve paylar**"*
(→ ÖTV buraya girer) + **(c)** tescile kadarki diğer gider ve ödemelerden
vergilendirilmeyenler.

**Yeni tespit:** 7555 s.K. ile md.21'e **(ç)** bendi eklenmiş — ÖTVK md.16/4
uyarınca **teminat karşılığı** ithal edilen malda teminata esas ÖTV tutarı da
matraha girer. **Baz senaryoda uygulanmaz** (şarapta ÖTV gümrükte fiilen ödenir,
teminata bağlanmaz). **Matrah zincirinde değişiklik gerektirmez.**

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| 1 | TÜİK Yİ-ÜFE Ara.2025→Haz.2026 değişimi (%16,09?) | TÜİK portalı JS-render SPA; `/api` HTTP 403; MEDAS oturum gerektiriyor | **HIGH** | JS'li tarayıcı / TCMB EVDS API anahtarı **veya** gümrük müşavirinden fiili beyanname teyidi (`T-901`) |
| 2 | Fiili vergilendirme dönemi (1 ay / 3 ay) | Bakanlık tespitini gösteren tebliğ bulunamadı; GİB sayfaları JS-render | **HIGH** | GİB mükellef grubu tebliği veya YMM teyidi (`T-152`) |
| 3 | KDVGUT III/C + md.36'ya dayanan CB kararları | GİB JS-render; mevzuat.gov.tr tebliğ uç noktası HTTP 302 | MEDIUM | JS'li ortam veya YMM/gümrük müşaviri (`T-151`) |
| 4 | 149 No.lu VUK Sirküleri'nin tarihi | GİB sirküler sayfası JS-render, PDF uç noktası bağlantı resetliyor | LOW | Aynı oturum |
| 5 | KVK md.11/1-(ı) %50 oranını değiştiren CB kararı | Aranmadı (alan sınırına yakın, etkisi ~0) | LOW | Aynı oturum |
| 6 | GVK md.41 muadili (şahıs işletmesi) | mevzuat.gov.tr 193 s.K. PDF HTTP 302 | LOW | Sermaye şirketi varsayımıyla etkisiz |
| 7 | Şişe kırılma/fire oranı `f` (md.30/c) | **ALAN DIŞI** | MEDIUM | `navlun-lojistik-uzmani` — çapraz ipucu Cİ-15.1 |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

**Bu turda yeni çelişki AÇILMAMIŞTIR.** Bir potansiyel çelişki incelendi ve
**çelişki olmadığı** tespit edildi:

| Görünürdeki çelişki | Çözüm | Neden çelişki değil |
|---|---|---|
| KDV beyan günü: **24** (KDVK md.41/1, T1) vs **28** (GİB, T2) | Çelişki **DEĞİL** — `KAPSAM` farkı | Biri **kanuni üst sınır**, diğeri VUK md.28 yetkisine dayanan **idari uzatma**. Model muhafazakâr olan 28'i kullanır. `EV-2026-08-10-109` / `-110` ayrı kartlarda tutulur |

`C-101` bu turda **yeniden açılmamıştır** — ayrıntı için `T-901` cevabına bakınız.
Bir çelişki bulunursa `C-151`…`C-199` bloğu kullanılacaktı; **kullanılmadı.**

---

## 5. MODEL GİRDİLERİ

`80-model/inputs/vergi.yaml` güncellendi:

| Blok | Değişiklik |
|---|---|
| `meta.BASE_DATE` | **YENİ** = `2026-08-10` + `BASE_DATE_kurali` + kapsam/kapsam-dışı listeleri |
| `meta.model_hedef_tarihi` | `TBD` olarak **KALDI** (`null` + `_durum: TBD` + `_status: UNKNOWN`) — gerekçe §6'da |
| `urun_parametreleri.sise_hacmi_litre` | `FACT`+`null` → **`ASSUMPTION`+`EV-2026-08-10-116`** + `duyarlilik` (T-906a) |
| `matrah_sirasi[4]` | `hesaplanan_otv_try_per_750ml: 53.4519` → `hesaplanan_otv_try_per_sise: {value: null, formul: …}` (T-906b genişletmesi) |
| `matrah_sirasi[5]` | KDV matrahı için T1 teyidi `EV-2026-08-10-108` eklendi |
| `kdv_perspektifleri.a_ekonomik_maliyet` | **9 alan** — indirilebilirlik `true`/FACT/T1, ekonomik maliyet `0.0`, K1–K4 risk koşulları |
| `kdv_perspektifleri.b_cash_tax_timing` | **13 alan** — VDO, ödeme anı (T2→**T1**), vergilendirme dönemi, beyanname günü, gecikme, devreden KDV, iade `N/A`, 2030 sınırı, KDV tabanı |
| `kdv_perspektifleri.b_cash_tax_timing.engine_kurallari` | **YENİ** — C1…C5 bağlayıcı kurallar |
| `kdv_perspektifleri.b_cash_tax_timing.peak_cash_requirement_sozlesmesi` | **YENİ** — tam formül |
| `hesap_sozlesmesi.adimlar` | **Tüm literaller** alan referansına çevrildi (5 satır) |
| `hesap_sozlesmesi.turev_ciktilar` | **YENİ** — `ekonomik_vergi_yuku` (KDV hariç) vs `kdv_nakit_cikisi` ayrımı |
| `hesap_sozlesmesi.tarih_kurali` | **YENİ** — BASE_DATE etiketleme zorunluluğu |

**CLAUDE.md §12 kontrolü:** `80-model/engine/` altındaki koda **DOKUNULMADI.**
`vergi.yaml` içindeki her oran/tutar artık **tek bir yerde** yaşar
(`matrah_sirasi[*]`); kalan sayısal geçişler yalnızca yorum/`notes` metinlerinde
ve hepsi *"İLLÜSTRATİFTİR, otorite formüldür"* ibaresi taşır.

---

## 6. BASE_DATE — NEDEN `TBD` LİTERALİ YAZILMADI

Görev, `model_hedef_tarihi`'nin **`TBD` olarak kalmasını** istedi. Literal
`"TBD"` string'i yazılsaydı `80-model/engine/matrah_sirasi.py:217`'deki

```python
if meta.get("model_hedef_tarihi") is None:
```

kontrolü **`False`** dönecek ve model eksik girdiyi **raporlamayacaktı** —
yani güvenlik kilidi **sessizce devre dışı kalacaktı.** CLAUDE.md §12 zaten
eksik girdinin `null` + `status: UNKNOWN` olarak durmasını emreder.

Bu nedenle **TBD durumu korunmuş ama güvenli biçimde temsil edilmiştir:**

```yaml
model_hedef_tarihi: null
model_hedef_tarihi_durum: TBD
model_hedef_tarihi_status: UNKNOWN
```

Engine kodu **değiştirilmedi** (ajan izolasyonu) → ticket **T-153**.

**BASE_DATE kuralı (yaml'da yorum satırlarıyla yazılı):** BASE_DATE senaryosunda
**yalnızca 2026-08-10'da yürürlükte olan doğrulanmış** vergi/mevzuat kullanılır.
**Gelecek ÖTV, kur veya mevzuat tahmini YAPILMAMIŞTIR.** ÖTV'nin Ocak/Temmuz'da
artacağı bilgisi bir **risk notudur** ve BASE_DATE bloğuna **değer olarak
yazılmamıştır**. 7524 s.K.'nın 2030 hükmü açıkça `BASE_DATE_disinda_kalan`
listesindedir.

---

## 7. TICKET DURUMLARI

| Ticket | Önce | Sonra | Sonuç |
|---|---|---|---|
| **T-906** | OPEN | **ANSWERED** | (a) `sise_hacmi_litre` → `ASSUMPTION` + `EV-2026-08-10-116` + duyarlılık; (b) **5 literal** alan referansına çevrildi + kapsam dışı 6. literal (`53.4519`) de temizlendi |
| **T-901** | OPEN | **ANSWERED** (`answer_result: DOGRULANAMADI_UNKNOWN`) | Yol A **başarısız** — 6 erişim yolu denendi, TÜİK verisine ulaşılamadı. `UNKNOWN`. **`RESOLVED` DEĞİLDİR**, kapanış kararı başkana ait |
| **T-151** | — | **OPEN** (yeni) | KDVGUT III/C + md.36 CB kararları taranmadı |
| **T-152** | — | **OPEN** (yeni) | Fiili vergilendirme dönemi 1 ay mı 3 ay mı (HIGH) |
| **T-153** | — | **OPEN** (yeni, → `finans-fizibilite`) | Engine `TBD`/`null` ayrımı + yeni `cash_tax_timing` bloğunu okumuyor |

**G1 gate'i üzerindeki etki:** Başkanın §5.2'de saydığı **üç CRITICAL boşluktan
BİRİ (KDV indirilebilirliği) KAPANDI.** Kalan ikisi (`model_hedef_tarihi` /
`T-104` ve gözetim) bu turun kapsamı dışındaydı ve **açık kalmıştır.**
**G1 hâlâ BLOCKED'dır** ve bu raporda aksi iddia edilmemektedir.

---

## 8. KANIT ÖZETİ

| | |
|---|---|
| Yeni kanıt kartı | **19** (`EV-2026-08-10-101` … `-119`) |
| T1 | 15 |
| T2 | 2 (`-109` GİB süreler, `-115` TÜİK — içeriğe erişilemedi) |
| T5 (tier dışı, proje içi doküman) | 1 (`-116`, `status: ASSUMPTION`) |
| `status: FACT` | 14 |
| `status: ESTIMATE` | 2 |
| `status: ASSUMPTION` | 1 |
| `status: UNKNOWN` | 2 (`-114`, `-115`) |
| Yeni snapshot | 6 dosya (KDVK tam PDF + madde alıntıları, KVK alıntısı, 7524 s.K., GİB süre tablosu, TÜİK erişim logu) |
| Index part | `10-evidence/_index-parts/gumruk-vergi-uzmani-tur15.csv` (19 satır, başlıksız) |

**Ana `10-evidence/index.csv` dosyasına DOKUNULMAMIŞTIR.**
`99-ops/capraz-ipuclari.md`, `99-ops/celiskiler.md`, `99-ops/acik-sorular.md`
dosyalarına **DOKUNULMAMIŞTIR.**

---

## 9. BU BULGUYU NE ÇÜRÜTÜR?

### 9.1 Hangi mevzuat değişikliği bu hesabı geçersiz kılar?

- **KDVK md.36 yetkisiyle** CB'nin alkollü içkilerde indirim hakkını
  kaldırması. Böyle bir kararın **yürürlükte olup olmadığı doğrulanmadı**
  (`EV-2026-08-10-114`, `T-151`). **Bu, raporun en zayıf halkasıdır.**
  Bulunursa şişe başına ~40–45 TL doğrudan maliyete döner ve
  fiyat/performans hipotezi ÖTV'den sonra **ikinci kez** vurulur.
- **md.30'a alkole ilişkin yeni bir bent eklenmesi.** 7524 s.K.'nın (f) bendini
  1/1/2030'da ekliyor olması, md.30'un **yaşayan bir liste** olduğunu kanıtlıyor.
- **KDV oranının değişmesi** tutarı değiştirir, **indirilebilirliği değiştirmez.**
- **Şarabın indirimli orana alınması** paradoksal biçimde **iade hakkı doğururdu**
  (md.29/2 istisnası) ve devreden KDV problemi ortadan kalkardı — yani
  *"vergi indirimi"* burada nakit akışı açısından **iyi haber** olurdu.

### 9.2 Hangi GTİP itirazı tüm yapıyı değiştirir?

GTİP itirazı **indirilebilirliği değiştirmez** (md.29/1-b tüm ithal mallar için).
Ama **KDV'nin tutarını** vurur: köpüklü (2204.10) tespiti ÖTV'yi
53,45 → 361,14 TL/şişe'ye çıkarır; ÖTV KDV matrahında olduğu için kaldırılamaz
KDV tabanı **10,69 → 72,23 TL/şişe** olur. 12.000 şişede yalnız bu taban
128 bin TL → **867 bin TL**. **GTİP itirazı ekonomik maliyeti değil,
`peak_cash_requirement`'ı öldürür.**

### 9.3 Gözetim / kıymet itirazı senaryosunda ne olur?

Kıymet yukarı çekilirse GV ve KDV matrahı büyür → **KDV nakit çıkışı artar**,
ama ekonomik maliyet **yine 0'dır**. ÖTV maktu olduğu için hiç etkilenmez.
**Kıymet itirazının KDV kanalındaki etkisi tamamen nakit akışıdır, kârlılık
değildir** — gümrük vergisi kanalı hariç. Bu, kıymet riskinin bu üründe
sanıldığından **daha az tehlikeli** olduğu anlamına gelir.

### 9.4 Bu raporun kendi kendini çürüttüğü nokta

**"KDV maliyet değildir" ifadesi, "satış gerçekleşir" varsayımına bağımlıdır.**

Devreden KDV **nakden iade edilmez** (md.29/2). Satış olmazsa KDV geri gelmez;
2030'dan sonra 5 yıl kuralına (md.30/f) takılır ve **ancak vergi incelemesi
sonucu gider** yazılabilir. Yani:

> KDV, **satış varsayımının bir türevidir.** Satış varsayımı çökerse
> KDV **de** maliyettir — üstelik ÖTV'nin üstüne biner.

Bu, `seytanin-avukati` için birinci sınıf bir saldırı yüzeyidir ve
**bilerek görünür bırakılmıştır.**

### 9.5 `T-901`'in çürütücü senaryosu

TÜİK Yİ-ÜFE değişimi **doğrulanamamıştır.** Eğer gerçek oran %16,09 değilse ve
**gerçek ÖTV tutarı 71,2692'den farklıysa**, bu raporun tüm türev sayıları
(53,4519 · 10,6904 · KDV formülleri) **kayar**. Türev sayılar `null` + formül
olarak saklandığı için model **kırılmaz** (T-906b düzeltmesi tam da bunu
sağlıyor) — ama basılı her sayı **yanlış olur**.

`EV-2026-08-09-111` **2026-09-08'de STALE** olacaktır. TUR 3 o tarihten sonra
çalıştırılırsa model çıktısı **`DRAFT`'tan yukarı çıkamaz.**

### 9.6 En ucuz çürütme testi

**Bir gümrük müşaviri / YMM ile 1 saatlik oturum**, üç ticket'ı birden kapatır:
`T-901` (fiili ÖTV tutarı), `T-151` (KDV indirim kısıtı var mı),
`T-152` (aylık mı üç aylık mı). Üçü de bu ortamdan kapatılamadı; üçü de
**bir telefon görüşmesi mesafesindedir.**
