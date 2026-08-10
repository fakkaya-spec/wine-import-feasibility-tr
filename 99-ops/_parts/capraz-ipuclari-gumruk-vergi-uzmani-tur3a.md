# ÇAPRAZ İPUÇLARI — gumruk-vergi-uzmani · TUR 3A (2026-08-10)

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında gördüğüm bulgular.
> İlgili ajan doğrulamadan modele girmez.

---

## Cİ-3A-01 → `kanal-marj-uzmani` · **"HER ŞEY DAHİL" OTEL KANALI YAPISAL OLARAK %20 DAHA ZAYIF**

**Kaynak:** KDV Genel Uygulama Tebliği **III/B-2.5.2** (`EV-2026-08-10-858`, T1)

> *"Geceleme hizmetleri kapsamında sunulan alkollü içeceklere ait **yüklenilen KDV
> tutarları, konaklama tesisleri tarafından hesaplanan KDV tutarlarından
> indirilemez.**"*

**Ne demek:** "Her şey dahil" sistemle çalışan bir otel, aldığı şarabın
KDV'sini **indiremez** → şarabın KDV'si o otel için **gerçek maliyettir.**
Yani aynı fiyata alan bir market ile bir "her şey dahil" otelin **efektif
maliyeti farklıdır**: otelinki `fiyat × 1,20`, marketinki `fiyat`.

**Kaçış yolu var (ve bu bir satış argümanıdır):** tesis alkollü içecek
bedelini **faturada ayrıca gösterirse** genel oran uygular ve **KDV'yi
indirebilir**. Yani ithalatçı, HoReCa müşterisine *"bedeli ayrıştır"*
diyerek **%20'lik bir değer yaratabilir.**

**Neden önemli:** kanal marjı modelinde HoReCa'nın ödeme istekliliği,
"her şey dahil" mi "à la carte" mı olduğuna göre **yapısal olarak ayrışır.**
Bu bir pazarlık farkı değil, **vergi kaynaklı bir yapı farkıdır.**

> ⛔ **Bu benim alanım değildir. Kanal marjı sonucu ÜRETMİYORUM.**
> `EV-2026-08-10-858` mevcuttur; `kanal-marj-uzmani` isterse kullanır.

---

## Cİ-3A-02 → `finans-fizibilite` · **%22,7 RAKAMI FAZLA KÖTÜMSER (düzeltme gerekir)**

`rapor-tur25-finans.md` §9.1 ve `T-947`, KDV indirim hakkının kısıtlanması
hâlinde `MAX_CIF_TRY`'nin **%22,7** düşeceğini yazmıştı.

Bu rakam **tam kısıt** varsayımına dayanır. Bulunan gerçek düzenleme
(7846 s. CBK + KDVGUT III/C-2.6, `EV-2026-08-10-854`) **kısmi kısıt**
getirir: **yalnızca tevsik edilemeyen artış kısmına** isabet eden KDV
indirilemez; CIF ve ona isabet eden GV/İGV üzerinden ödenen KDV
**indirilebilir kalır.**

→ Ticket **`T-171`** ile resmen bildirildi.

---

## Cİ-3A-03 → `navlun-lojistik-uzmani` + `finans-fizibilite` · **YMM RAPORU: GÖRÜNMEZ BİR L5 KALEMİ**

KDVGUT **III/C-2.6.2** (`EV-2026-08-10-854`), 7846 kapsamında ithalat yapan
mükellefe **altışar aylık dönemler** itibarıyla ya **vergi dairesine bildirim**
ya da **Özel Amaçlı YMM Raporu** yükümlülüğü getirir (tam tasdik sözleşmesi
varsa rapor gerekmez).

**Baz senaryoda tetiklenmez** (gözetim yok). Ama gözetim gelirse:
`L5`'te **yeni bir gider satırı** doğar. Tutar **UNKNOWN** ve bu benim alanım
değildir. Ayrıca "tam tasdik sözleşmesi" bir **muhasebe/denetim** kararıdır ve
maliyeti vardır.

---

## Cİ-3A-04 → `global-sourcing-kasifi` · **GÖZETİM TAZE MEYVEYE UYGULANMIŞTIR**

Gözetim tebliği taramasında (`EV-2026-08-10-860`) 2019/6 sayılı tebliğe ilişkin
değişiklikte **`0810.10` (çilek)** ve **`0810.50` (kivi)** GTİP'leri görüldü.

**Anlamı:** *"Tarım/gıda ürününe gözetim gelmez"* varsayımı **yanlıştır.**
Şarapta gözetim bulunmaması bir **kategori bağışıklığı değil**, sadece
**fiilî listede olmama** durumudur.

→ Çok düşük FOB teklifleriyle çalışan bir sourcing stratejisi, gözetimin
**gelecekte** getirilebileceğini bir **senaryo riski** olarak taşımalıdır.
Sonuç üretmiyorum; ipucudur.

---

## Cİ-3A-05 → `yatirim-komitesi-baskani` (yöntem notu) · **RESMÎ PDF'LERDE "METİN VAR" ≠ "METİN OKUNUYOR"**

Gözetim tebliğlerinin taranmasında üç ayrı teknik gerekti:

| Sorun | Nerede görüldü |
|---|---|
| PDF metin katmanı **bozuk font kodlamasıyla** geliyor (harf harf şifrelenmiş gibi) | 2026/1, 2024/14 |
| GTİP tablosu **metin katmanında hiç yok**, ayrı bir **CCITT/JBIG2 görüntü** | 2026/2, 2026/4, 2026/5 ve diğerleri |
| Sayfa görüntüsü OCR'ı **tabloyu atlıyor** (psm 6 tablo bloğunu görmüyor) | çoğu tebliğ |

**Tek yöntemle yapılan bir tarama YANLIŞ NEGATİF üretirdi.**
Bu, projede **her "bulamadım" sonucunun yöntemini de sorgulamayı** gerektirir —
`EV-2026-08-09-125` tam olarak bu türden bir kayıttı.

**Genelleştirilebilir kural önerisi:** resmî bir listede bir GTİP'in
"olmadığı" iddiası, **listenin kaç kayıt içerdiği** (pozitif kontrol)
belirtilmeden kabul edilmemelidir.
