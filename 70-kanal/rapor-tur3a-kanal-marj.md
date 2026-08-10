# AJAN RAPORU — kanal-marj-uzmani · TUR 3A

```yaml
ajan:               kanal-marj-uzmani
tur:                TUR 3A — KANAL KATMAN DENETIMI (sinirli gorev)
tarih:              2026-08-10
durum:              SUBMITTED
tetikleyen:         T-942 · T-943 · T-944 (yatirim-komitesi-baskani denetimi)
yeni_arastirma:     YOK — WebSearch kullanilmadi, yeni dis kaynak taranmadi
yeni_evidence:      YOK — 10-evidence/ acilmadi, index.csv'ye dokunulmadi
yeni_marj_degeri:   YOK — bu tur SAYI uretmez, MATRAH tanimlar
```

---

## 1. YÖNETİCİ ÖZETİ

TUR 2.5'te `finans-fizibilite`'nin yakaladığı `R5` hatası (**−28,95 TL/şişe**)
bir aritmetik hatası değil, bir **matrah hatasıydı**: `L6` ile `L7_eff`'in
birbirinin yerine kullanılabileceği sanıldı. Bu tur, kanal bacağının
**matrah disiplinini** vergi bacağındaki `matrah-sirasi.md` seviyesine
çıkarmak için yapıldı. **Hiçbir yeni sayı üretilmedi; sadece her kalemin
hangi katmanda ve hangi tutarın üzerinden çalıştığı yazıldı.**

**Üç ana sonuç:**

1. **Aynı sınıftan 5 hata daha bulundu** ve hiçbiri modelde yok:
   `f`'nin hacme bağlı olması (`K7`, **38,00 TL**), `d`'nin homojen sanılması
   (`K8`), satılan≠ithal şişe (`K11`, **19,38 TL**), vadenin hem matrahının
   yanlış hem bedelinin sıfır olması (`K12`, **27,55 TL**), kanal karmasının
   hiç olmaması (`K9`). Bugün `0` alınan kanal kalemlerinin toplam mertebesi
   **≈85 TL/şişe** = `TGT_799 · CHAIN · BASE` tavanının (272,83) **%31'i.**

2. **`T-942`'nin önerdiği `R8-K` assertion'ı, birebir kodlanırsa `R5`
   düzeltmesini GERİ ALIR** ve hatayı "test edilmiş" damgasıyla mühürler.
   `L5_max + μ·L6` ifadesi `L6`'ya değil `L7_eff`'e eşittir. **Teşhis doğru,
   önerilen assertion ters çalışıyor** → **`T-619` (CRITICAL)**.

3. **`μ`'nün matrahı sorusunun (`T-944`) kanal tarafındaki cevabı: TEK
   CEVAP YOKTUR** — çünkü `μ` iki farklı ekonomik nesneyi (üçüncü tarafa
   **ödeme** vs bizim **artığımız**) aynı sembolde taşıyor. Üç aday matrahın
   ölçülen farkı `μ=%30`'da **31,73 TL/şişe (+%19,3)**. Mevcut seçim (`L6`)
   üçünün **en muhafazakârıdır** → hata bu kez **projenin aleyhine**.

---

## 2. BULGULAR

### B-1: Kalem × katman × matrah haritası tamamlandı — 3 kanal × 10 alan

```yaml
claim:          "Her ticari kosul kaleminin katmani ve matrahi tanimlanmis, tanimlanamayanlar BLOCKED isaretlenmistir."
value:          "9 kalem x 3 kanal; 15 kalem BLOCKED"
status:         SPESIFIKASYON
evidence_id:    "yeni evidence YOK — mevcut EV-2026-08-10-601..-621 kartlarina atif"
katman:         L5..L8
```

**Belge:** `70-kanal/kanal-katman-matrah-haritasi.md`

**Doğrulanan (modelde DOĞRU uygulanmış) üç kalem:**

| Kalem | Matrah | Denetim |
|---|---|---|
| `m_retail` | `L8_net` (margin on selling price) | ✅ `ters_model.py:277` — markup karışıklığı **yok** |
| `k_horeca` | `L7_eff` (çarpan) | ✅ `ters_model.py:267` — `kanal.yaml` tanımıyla birebir |
| `d` | `L6` (KDV hariç fatura cirosu) | ✅ **üç ayrı gerekçeyle** doğrulandı (`EV-610`, `EV-612`, `6585 m.6/2(c)`) |

### B-2: Repoya yeni bir sembol girdi — `L6_gross` (alacak tutarı)

```yaml
claim:          "Kanal alacaginin tutari L6 degil L6_gross = L6*(1+v)'dir; fatura toplami KDV'yi ICERIR."
value:          "651,3587 TL/sise (TGT_799 · CHAIN · BASE, v sembolik %20)"
status:         STRUCTURAL_FACT (aritmetik)
katman:         L6
```

**Gerekçe:** Perakendeci bize `L6 + KDV` öder; vade **o tutara** işler.
`peak_cash` alacak bacağı `L6` üzerinden kurulursa **%20 eksik** çıkar.
Bugüne kadar hiçbir belgede adı yoktu. → **`T-614`**

### B-3: `d` homojen değil — altı kalemin en az üçü SABİT tutarlı

```yaml
claim:          "EV-2026-08-10-612'nin ismen saydigi 6 kalemin en az 3'u sabit TL tutaridir, biri BASKA BIR HACME oranlidir, biri L8 matrahli olabilir."
status:         BLOCKED
evidence_id:    EV-2026-08-10-612
katman:         "L6 -> L7 koprusu"
```

**Türetme:** kalemlerin **adları** matrahlarını ele veriyor —
*"alan kullanımı"* (mağaza × dönem), *"soğutucu enerji bedeli"*
(soğutucu × dönem), *"kırık ürün bedeli"* (kırılan **adet**),
*"B2B **kasa çıkışı cirosu**"* (**`L8`** hacmi olabilir!).

**Etkisi:** hacim plandan **yarıya** düşerse gerçek yük 43,42 → **65,13
TL/şişe** olur; tek-`d` temsili bunu **tanım gereği göremez.**
→ **`T-613`**

### B-4: `T-942`'nin `R8-K` assertion'ı tersten çalışıyor

```yaml
claim:          "L5_max + mu*L6 ifadesi L6'ya DEGIL L7_eff'e esittir; L6 etiketiyle devam edilince d ve f IKI KEZ dusulur ve assertion tersine doner."
status:         FACT (aritmetik — repo ici dogrulama)
```

| Girilen `L5_max` | `L8_geri` | Sonuç |
|---|---|---|
| **DOĞRU** `= L7_eff = 499,3750` | **735,08** | ⛔ **REDDEDİLİR** |
| **NAİF** `= L6 = 542,7989` | **799,00** | ✅ **KABUL EDİLİR** |

**`T-942`'nin teşhisi doğrudur** (kanal bacağında doğrulama yok, `R5`
2.700/2.700 satırdan temiz geçti). Hatalı olan tek şey **`K1` adımının
etiketidir** — ama kabul kriteri olarak durduğu için birebir kodlanırsa
hatayı **mühürler.** → **`T-619` (CRITICAL)**

### B-5: `μ` iki farklı ekonomik nesneyi taşıyor — `T-944`'ün cevabı

```yaml
claim:          "mu'nun matrahi icin TEK BIR KANAL PRATIGI YOKTUR cunku mu, UCUNCU TARAFA ODEMEYI (distributor marji) ve BIZIM ARTIGIMIZI (ithalatci katki payi) ayni sembolde tasiyor."
status:         SPEC_DECISION + INVESTOR_DECISION_REQUIRED
```

| `μ` | (a) `L6` *(bugün)* | (b) `L7_EFF` | (c) `L5_MARKUP` | yayılım |
|---|---|---|---|---|
| %10 | **236,64** | 239,54 | 242,63 | 5,92 |
| %20 | **200,46** | 206,25 | 217,34 | **16,89** |
| %30 | **164,27** | 172,96 | 196,00 | **31,73** |
| %50 | **91,90** | 106,37 | 161,86 | **69,96** |

*(a) sütunu `reverse-price-model.md` §9.2 gridiyle **birebir aynıdır**.*

**Kanal tarafından verilen kısmi cevap:** distribütör marjı için matrah
**`L6` doğrudur** (ciro komisyonudur). İthalatçı katkı payı için matrah
**bir pazar olgusu değil, bir yatırımcı tanımıdır** →
`INVESTOR_DECISION_REQUIRED`. → **`T-616`**

### B-6: `T-856`'nın cevabı — bir sıfır değil, ÜÇ sıfır

```yaml
claim:          "Tekel kanalinin modeldeki %11,4 ustunlugu bir BULGU degil, UC AYRI SIFIRIN toplamidir; d icin bir sayi bulmak bu artefakti duzeltmez, yerini degistirir."
status:         SPEC_ANSWER
evidence_id:    [EV-2026-08-10-601, EV-2026-08-10-610, EV-2026-08-10-613]
```

Tekelde `d`'nin **hukuki karşılığı gerçekten yoktur** — yük üç başka
satıra düşer ve **üçü de modelde `0`'dır**: net fiyat iskontosu, kılcal
dağıtım maliyeti, şüpheli alacak. **Bu ajan tekel için `d` bandı
ÜRETMEMİŞTİR.** Önerilen çözüm bir sayı değil, bir **kontroldür**:
`ZERO_PARITY` (kanal başına `UNKNOWN→0` sayısı; eşit değilse
`KANALLAR_KARSILASTIRILAMAZ`).

### B-7: HoReCa sütunu doğrulanmamış bir KDV oranından geçiyor

```yaml
claim:          "R1 (L8/(1+v)) HoReCa MENU FIYATINA da URUN KDV oraniyla uygulaniyor; menu KDV'si yiyecek-icecek HIZMETI KDV'sidir ve ayni olup olmadigi DOGRULANMAMISTIR."
status:         BLOCKED
katman:         L8_HORECA
```

`marj-vs-markup.md` §2.3 bu riski **TUR 2'de yazmıştı**; model uyarıyı
**kullanmadı.** `reverse-price-model.md` §3.2'nin **15 HoReCa hücresinin
15'i** buradan geçiyor — *"HoReCa'da 599 TL menü fiyatı matematiksel
olarak ölüdür"* sonucu dâhil. → **`T-612`**

### B-8: MODEL A'da `d` + `m_dist` çift sayılıyor olabilir

```yaml
claim:          "reverse-price-model.md §7.1 distributor gridini CHAIN BASE (d=%8) uzerinde kosturuyor — yani ayni anda hem distributore hem zincire odedigimiz varsayiliyor. kanal-marj-yapisi.md §6 ise distributor marjinin 'L6 ile L7 ARASINA GIRDIGINI' soyler."
value:          "28,95 TL/sise (d*L6 = 43,42 / 1,50)"
status:         CONFLICT
conflict_id:    C-611
```

**`R5` hatasıyla aynı büyüklük, ters yön** — bu kez model **aşırı
kötümser** olabilir. Taraf **seçilmemiştir**; iki alt senaryo (`A1`/`A2`)
tanımlanmıştır. → **`C-611`**, **`T-617`**

---

## 3. UNKNOWN / BLOCKED LİSTESİ

**`BLOCKED` bu turda repoya girmiştir:** `UNKNOWN` bir **seviyenin**,
`BLOCKED` bir **denklemin şeklinin** bilinmemesidir. `UNKNOWN`
duyarlılıkla yönetilir; **`BLOCKED` yönetilemez.**

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunur |
|---|---|---|---|---|
| B-1 | `f`/`d` KDV'sinin indirilebilirliği | vergi alanı — bu ajan üretemez | **HIGH** | `T-611` |
| B-2 | HoReCa menü KDV oranı | vergi alanı | **HIGH** | `T-612` |
| B-3 | `d` sepetinin oransal/sabit ayrışması | oranlar `EV-610`'da **karartılmış** | **HIGH** | TUR 7 |
| B-4 | Ciro priminin kademeli olup olmadığı | **hiç sorulmamış** | MEDIUM | TUR 7 |
| B-5 | Lojistik bedelinin matrahı | karartılmış | MEDIUM | TUR 7 |
| B-6 | Alan kullanımı / teşhir birimi | karartılmış | MEDIUM | TUR 7 |
| B-7 | Kırık ürün bedelinin matrahı | karartılmış | MEDIUM | TUR 7 |
| B-8 | CRM/B2B matrahı (`L8` olabilir) | karartılmış | **HIGH** | TUR 7 |
| B-9 | `f`'nin birimi (SKU×zincir / SKU×mağaza) | karartılmış | **HIGH** | TUR 7 |
| B-10 | Tekel marj tipi | yalnız çelişen T5 (`C-602`) | MEDIUM | TUR 7 |
| B-11 | İade oranı + geri kazanılabilir değer | yasal düzenleme yok (`EV-606`) | **HIGH** | TUR 7 |
| B-12 | HoReCa desteğinin fixed/variable karması | `EV-615` ikisini de içeriyor | MEDIUM | TUR 7 |
| B-13 | TR-içi lojistiğin teslim noktası | başka ajanın kartı | MEDIUM | `T-618` |
| B-14 | `μ` matrahı | **bir yatırımcı kararı** — pazar olgusu değil | **HIGH** | `T-616`/`D-03` |
| B-15 | MODEL A'da `d`+`f`'i kim öder | sözleşmeye bağlı | **HIGH** | `C-611`/TUR 7 |

**15 `BLOCKED` kalemin 15'i de bugün modelde `0` veya bir varsayılan
davranışla geçmektedir. Hiçbiri için "yok" kanıtı yoktur.**

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A | Kaynak B | Neden çelişiyor | Durum |
|---|---|---|---|---|
| **C-611** | `kanal-marj-yapisi.md` §6: *"distribütör marjı `L6` ile `L7` **arasına girer**"* | `reverse-price-model.md` §7.1 + `ters_model.py:392`: `m_dist` ve `d` **aynı anda** ithalatçıda, *"toplanırlar"* | İki farklı **dünya**: A'da distribütör zincir bedellerini üstlenir, B'de biz de o da ödüyoruz | **OPEN** |
| `C-602` **(genişletildi)** | T5 kaynaklar (seviye çelişkisi) | **TUR 3A eklemesi: MATRAH çelişkisi de** — margin / iskonto / markup | `margin_mi_markup_mi` alanı `null`; model gerekçesiz `MARGIN` varsayıyor; fark **+12,19 TL/şişe** | **OPEN** |

`99-ops/_parts/celiskiler-kanal-marj-uzmani-tur3a.md`'ye yazıldı.
**`99-ops/celiskiler.md`'ye dokunulmadı** (başkan birleştirir).

---

## 5. MODEL GİRDİLERİ

**Bu turda `value` alanına HİÇBİR YENİ SAYI YAZILMAMIŞTIR.** Yazılan her
şey **metadata**'dır (matrah, katman, engine kuralı, assertion).

| YAML | Alan | Ne eklendi | status |
|---|---|---|---|
| `kanal.yaml` | `kullanim_kurallari.M7`, `M8` | 10-alan sözleşmesi; `L7` yasağı; `L6_gross` | BAĞLAYICI KURAL |
| `kanal.yaml` | `kalem_katman_matrah_haritasi` | **9 kalem × 10 alan** | SPESİFİKASYON |
| `kanal.yaml` | `merdiven_denklemi.tur3a_duzeltilmis_ileri` | `K1`–`K6` kapalı formül seti | SPESİFİKASYON |
| `kanal.yaml` | `merdiven_denklemi.tur3a_r8k_assertion` + `_uyarisi` | doğru `R8-K` + `T-619` uyarısı | **CRITICAL** |
| `kanal.yaml` | `dagitim_modeli.importer_katki_matrahi` | 3 seçenek + ölçülen fark tablosu | `INVESTOR_DECISION_REQUIRED` |
| `kanal.yaml` | `dagitim_modeli.mu_ile_distributor_marji_ayni_matrah_mi` | **`false`** | `SPEC_DECISION` |
| `kanal.yaml` | `dis_distributor.marj_matrahi` / `.d_kimde` | `L6` / `A1`–`A2` | `SPEC_DECISION` / `BLOCKED` |
| `kanal.yaml` | `tekel_bayi.t856_cevabi` + `.marj_tipi_matrahi` | üç sıfır + `ZERO_PARITY` | `SPEC_ANSWER` / `BLOCKED` |
| `kanal.yaml` | `kanal_karmasi.engine_kurali` | `KARMA_UNKNOWN` bayrağı | SPESİFİKASYON |
| `kanal.yaml` | `hacim_ayrimi` | `Q_ithal` ≠ `Q_satilan` | `UNKNOWN` (değer) |
| `kanal.yaml` | `kanal_bacagi_hata_listesi` | `K1`…`K12` özet | SPESİFİKASYON |
| `kanal.yaml` | `blocked_envanteri` | `B-1`…`B-15` | **BLOCKED** |

**Hiçbir satır `evidence_id`'siz bir DEĞER taşımıyor** — çünkü hiçbir
satır yeni bir değer taşımıyor.

---

## 6. ÇAPRAZ İPUÇLARI

| Hedef ajan | İpucu | Neden önemli |
|---|---|---|
| `gumruk-vergi-uzmani` | Kanal bacağında KDV **üç** ayrı yerde (`V1`/`V2`/`V3`), model **birini** uyguluyor | `V3` indirilemezse `f`+`d` **1,20 katı**; `V2` `peak_cash`'i **%20** etkiliyor |
| `gumruk-vergi-uzmani` | `vergi.yaml`'da HoReCa hizmet KDV oranı için **ayrı alan yok** | 15 HoReCa hücresinin 15'i etkileniyor |
| `navlun-lojistik-uzmani` | `EV-2026-08-10-329`'un **teslim noktası** yazılı değil | Zincirin lojistik bedeliyle çift/eksik sayım |
| `finans-fizibilite` | §0.2'nin *"13 kalemin 13'ü yukarı saptırır"* listesi kanal bacağında **7 kalem daha** uzuyor (≈85 TL/şişe) | Tavan **%31** düşebilir |
| `turkiye-pazar-kasifi` | Kanal karması modelin **ölçülmemiş en büyük ekseni** olabilir (3,5×) | Nokta sayısı ciro payı **değildir** |
| `yatirim-komitesi-baskani` | `T-942`'nin `R8-K`'sı birebir kodlanırsa `R5` düzeltmesini **geri alır** | **`T-619` CRITICAL** |
| `global-sourcing-kasifi` | `T-605` (üretici katkısı ↔ `f`) hâlâ açık; `K6c` olarak listeye girdi | Aynı para hem gelir hem gider |

`99-ops/_parts/capraz-ipuclari-kanal-marj-uzmani-tur3a.md`'ye yazıldı.

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim (özet) | impact | status |
|---|---|---|---|---|
| **T-611** | `gumruk-vergi-uzmani` | `f`/`d` hizmet faturası KDV'si indirilebilir mi? | HIGH | OPEN |
| **T-612** | `gumruk-vergi-uzmani` | HoReCa menü KDV oranı = ürün oranı mı? | HIGH | OPEN |
| **T-613** | `finans-fizibilite` | `d` → `d_var` + `D_fix` ayrıştırılsın | HIGH | OPEN |
| **T-614** | `finans-fizibilite` | Alacak matrahı `L6_gross`; vade finansmanı **yok** | HIGH | OPEN |
| **T-615** | `finans-fizibilite` | `Q_ithal` ≠ `Q_satilan`; iade bedeli `L6` | HIGH | OPEN |
| **T-616** | `yatirim-komitesi-baskani` | `μ` matrahı — `D-03` matrahla sorulsun | HIGH | OPEN |
| **T-617** | `finans-fizibilite` | `μ` ≢ `m_dist`; `A1`/`A2` ayrı koşulsun | HIGH | OPEN |
| **T-618** | `navlun-lojistik-uzmani` | TR-içi lojistiğin teslim noktası | MEDIUM | OPEN |
| **T-619** | `finans-fizibilite` | `T-942`'nin `R8-K`'sı **tersten çalışıyor** | **CRITICAL** | OPEN |

**Cevaplanan (kapanış kararı başkanındır):** `T-943` (bu iki belge),
`T-944` (→ `T-616`), `T-856` (→ `t856_cevabi`).

---

## 8. TAZELİK

**Bu turda hiçbir yeni kanıt kartı açılmamıştır.** Mevcut kartların
`ttl`'leri değişmemiştir (`kanal.yaml → tazelik`):

| Grup | `ttl` | STALE tarihi |
|---|---|---|
| Mevzuat kartları (`EV-601`…`-607`) | 180d | 2027-02-06 |
| Rekabet Kurumu kartları (`EV-609`…`-615`, `-624`) | 1y | 2027-08-10 |
| Migros finansalları (`EV-616`, `-617`) | 1y | 2027-08-10 |
| Asgari ücret (`EV-621`) | 1y | **fiilen 2026-12-31** |
| T5 kartları (`EV-618`, `-619`, `-620`, `-623`) | **0d** | **ZATEN STALE — modele giremez** |

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**Gerçek bir zincir yıllık anlaşmasının görülmesi.** Bu raporun tamamı,
`EV-2026-08-10-612`'nin **isim listesinden** matrah **çıkarımı** yapmaya
dayanıyor. Rekabet Kurulu kararı kalemleri **saymış**, tutarları
**karartmıştır** — matrahlarını ise **hiç yazmamıştır**.

Somut örnek: *"alan kullanımı bedeli"* kaleminin sabit TL değil, **ciroya
oranlı** olduğu ortaya çıkarsa `K8`'in tamamı düşer ve `d`'nin tek oranla
temsili **doğru** olur. Ben bu kalemin sabit olduğunu **kanıtlamadım** —
**adından çıkardım.** Bu bir `ESTIMATE`'tir ve rapor boyunca `BLOCKED`
etiketiyle işaretlenmiştir; ama **çıkarımın kendisi çürütülebilir.**

Aynı şey `CRM/B2B (kasa çıkışı cirosu)` için de geçerli: matrahının `L8`
olabileceğini **adından** okudum. "Kasa çıkışı cirosu" bir **raporlama
metriği** de olabilir, bir **matrah** değil.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**`d`'nin matrahının `L6` olduğu.** Üç gerekçe yazdım ve üçü de
**dolaylıdır**:
- `EV-610`'un *"tedarikçinin cirosuna oranlanır"* ifadesi FMCG genelidir,
  şarap değildir.
- `EV-612` kalemleri sayar, matrah **söylemez**.
- `6585 m.6/2(c)` argümanı bir **hukuki çıkarımdır** ve hukuk benim alanım
  **değildir**.

Eğer `d`'nin matrahı `L8` (perakendecinin satışı) çıkarsa, `L6 = (L7+f)/(1−d)`
denklemi **komple yanlıştır** ve ters modelin `R4` adımı yeniden yazılır.
Bu, `R5` hatasından **daha büyük** bir düzeltme olurdu.

**İkinci kırılgan nokta:** `C-611`'de distribütörün zincir bedellerini
üstlendiği yönündeki okumam. Bunun tek dayanağı **kendi TUR 2 belgemdeki
bir cümledir** (*"L6 ile L7 arasına girer"*) — yani **kendi yazdığımı
kanıt olarak kullanıyorum.** Bu döngüseldir ve `C-611` tam da bu yüzden
`OPEN` bırakılmıştır.

### 9.3 Hangi kaynağıma en az güveniyorum?

**Kendi aritmetiğime — spesifik olarak `K8` ve `K11`'in TL büyüklüklerine.**

- `K8`'in "%8'in yarısı sabit" varsayımı **tamamen keyfîdir**; kanıtı
  yoktur, yalnızca büyüklük mertebesi göstermek için seçilmiştir.
- `K11`'in `r` değerleri (%2/%5/%10) de **keyfîdir** — iade oranı
  `UNKNOWN`'dır ve öyle kalmıştır.
- `K12`'nin finansman oranı (%38,6) `EV-2026-08-10-617`'den alındı ama o
  **Migros'un kendi borçlarını iskonto ettiği orandır**, bizim borçlanma
  maliyetimiz **değildir** — ve `makro.finansman` `null`'dır.

**Bu üç sayı modele girmemelidir.** Görevleri yalnızca *"bu kalem
ihmal edilebilir mi?"* sorusuna *"hayır"* dedirtmektir.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

**Değişen karar: `T-619` düzeltilmezse `R8-K` yazıldığı anda kanal bacağı
"doğrulanmış" sayılır ve `P-4` kapısı SAHTE olarak açılır.** Bu, bu turun
**tek geri döndürülemez riskidir** — çünkü bir kez "test edildi" damgası
vurulduktan sonra kimse bir daha bakmaz.

**Ters yönde:** eğer `K7`+`K11`+`K12`'nin ≈85 TL/şişelik mertebesi doğruysa,
`TGT_799 · CHAIN · BASE` tavanı **272,83 → ~188 TL/şişe**'ye iner.
`reverse-price-model.md` §10.3'ün `IMPLIED_BREAKEVEN_USDTRY` sıralaması
**tamamen kayar** ve İspanya için 142,93 → **~101** olur. Yani **ülke
elemesi değişir.**

**Ama tersi de mümkün:** eğer `C-611`/`K6d` doğruysa (distribütör `d`'yi
üstleniyorsa) MODEL A tavanları **28,95 TL yukarı** gider ve dış distribütör
seçeneği bugün göründüğünden **daha iyidir.**

**Net etki bilinmiyor — ve bilinmediğini yazmak bu raporun işidir.**

### 9.5 Bunu doğrulamak için ne gerekir?

| Ne | Kim | Nasıl | Süre |
|---|---|---|---|
| `d` sepetinin matrah ayrışması, `f`'nin birimi, kademe yapısı | **bir zincirin ticaret müdürü** | gerçek yıllık anlaşma taslağı / SKU giriş formu | TUR 7, `T-604` — **başkan onayı gerekir** |
| `f`/`d` KDV işlemi, HoReCa menü KDV oranı | `gumruk-vergi-uzmani` | **masabaşı** — T1/T2 kaynak | **bu tur içinde kapatılabilir** (`T-611`, `T-612`) |
| TR-içi lojistiğin teslim noktası | `navlun-lojistik-uzmani` | **masabaşı** — kendi kartlarının kapsamı | **hemen** (`T-618`) |
| `R8-K`'nın doğru kodlanması | `finans-fizibilite` | `TVK-N1b` negatif vektörü | **hemen** (`T-619`) |
| `μ` matrahı | **yatırımcı** | `D-03` — matrah tablosuyla birlikte sorulmalı | `T-616`/`T-851` |
| İade oranı, geri kazanılabilir değer | TUR 7 | gerçek kanal görüşmesi | `T-615` |

> **Masabaşıyla kapanabilecek dört ticket (`T-611`, `T-612`, `T-618`,
> `T-619`) toplam etkisi bakımından TUR 7'yi beklemek zorunda değildir.
> `T-619` ise beklemek ZORUNDA DEĞİLDİR ÇÜNKÜ BEKLERSE ZARAR VERİR.**
