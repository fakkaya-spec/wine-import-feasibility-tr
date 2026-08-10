# ÇAPRAZ İPUÇLARI — `gumruk-vergi-uzmani` · TUR 2.5

> CLAUDE.md §1.11: alan dışı bulgular silinmez, buraya bırakılır.
> **Aşağıdakilerin hiçbiri bir sonuç değildir.** Ters modelin vergi bacağını
> kurarken görülen, başka ajanların alanına giren gözlemlerdir.
> Bu turda yeni dış kaynak taranmamıştır.

---

## İP-2501 → `mevzuat-ruhsat-uzmani` · **Bandrol da ÖTV ile aynı tarih hatasını taşıyor**

Bandrol birim bedeli **her yıl 1 Ocak'tan geçerli olmak üzere önceki yıl Yİ-ÜFE
oranında** güncellenir (`EV-2026-08-09-213`). Başkanın üç hedef tarihi
(**2027-01-01 / 2027-04-01 / 2027-07-01**) **üçü de 2027'dedir.**

Yani `ruhsat.yaml → bandrol_uis.bandrol_birim_bedeli = 2,36073` değeri, ÖTV'nin
`71,2692` değeriyle **birebir aynı yapısal durumdadır**: BASE_DATE'te geçerli,
hedef tarihte **geçerli olması beklenmez**.

ÖTV tarafında bu için `otv_maktu_zaman_serisi` + `gelecek_deger_kurali`
kurulmuştur (`T-104`). **Bandrol tarafında böyle bir yapı yoktur** ve model
`2,36073`'ü sabit okursa ters modelin `L4_econ_max` girdisi sessizce yanlış olur.

**Sonuç üretmiyorum.** Yalnız yapısal simetriyi işaret ediyorum: bandrol da bir
**zaman serisi** olarak modellenmeli veya en azından
`gecerlilik_ufku: 2026-12-31` ile etiketlenmelidir.

---

## İP-2502 → `navlun-lojistik-uzmani` · **Şili aktarması ters modelde İKİ senaryo zorunluluğu doğuruyor**

`master-commercial-input-table.md` §3.2.1 ve `T-914` zaten açık. Ters model
tarafındaki **sayısal sonucu** ekliyorum:

`SIL` rejiminde çıkış ülkesi kontrolü düşerse `g` 0,50 → 0,70 olur ve ters
modelde **azami satın alma fiyatı tam olarak %11,765 düşer** — L8'den,
marjdan, ÖTV'den ve navlundan **bağımsız** olarak.

Barcelona aktarmalı Şili rotasının navlun avantajı (0,432–0,454 vs 0,595–0,618
USD/şişe ≈ **0,16 USD/şişe**) ile karşılaştırılacak büyüklük budur. **Bu
karşılaştırmayı yapmıyorum** (navlun + kur benim alanım değil), ama ters model
`fx` olmadan bile `%11,765`'i üretebildiği için **karşılaştırma `fx`
gelmeden de kurulabilir**: yüzde cinsinden.

---

## İP-2503 → `global-sourcing-kasifi` · **Ters model, RFQ'daki tek bir sorunun fiyat karşılığını verebiliyor**

RFQ'daki *"EUR.1 düzenleyebiliyor musunuz?"* sorusunun cevabı `hayır` ise,
ters modelde o tedarikçiye ödenebilecek azami fiyat **%11,765 düşer**
(AB/Şili menşeli tedarikçiler için).

Yani bu soru bir uyum sorusu değil, **bir fiyat sorusudur** ve RFQ'da
şu biçimde sorulabilir: *"EUR.1 düzenleyemiyorsanız fiyatınızdan %11,8
indirim yapabilir misiniz?"* — çünkü ithalatçı için ikisi **matematiksel olarak
denktir**.

**Tedarikçi değerlendirmesi yapmıyorum**; yalnız `T-161`'in fiyat karşılığını
sayısallaştırdım.

---

## İP-2504 → `finans-fizibilite` · **`KDV_ithal = 0,20 × L4_econ` özdeşliği CIF bilinmeden çalışır**

Ters modelde bedava gelen bir sonuç: gümrükte nakden ödenecek KDV,
**CIF bilinmeden**, yalnız `L4_econ_max`'tan doğrudan hesaplanır
(`X_pre = 0` iken):

```
kdv_ithal = 0,20 × L4_econ_max          ← menşeden BAĞIMSIZ
L4_cash   = 1,20 × L4_econ_max
```

Yani hedef raf fiyatı bandı verildiği anda, **`fx` olmadan, tedarikçi fiyatı
olmadan, navlun olmadan** gümrükte ödenecek KDV tutarı hesaplanabilir.
`master-commercial-input-table.md` §5.3'ün 6. maddesi ("peak_cash yapısı
hesaplanabilir, tutarı hesaplanamaz") **kısmen aşılabilir**: KDV bileşeninin
**tutarı** hesaplanabilir. ÖTV bileşeni de zaten maktu ve TL'dir.

Geriye tutar olarak yalnız **GV** kalır ve o da `CIF_TRY_max`'a bağlıdır.
**Sonuç üretmiyorum**; modelleme kararı `finans-fizibilite`'nindir.
