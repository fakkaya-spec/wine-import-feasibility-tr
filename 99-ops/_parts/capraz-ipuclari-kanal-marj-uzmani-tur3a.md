# ÇAPRAZ İPUÇLARI — kanal-marj-uzmani · TUR 3A
<!-- 99-ops/capraz-ipuclari.md'ye BASKAN tarafindan birlestirilir. Bu dosya bir PART'tir. -->

> Bunlar **sonuç değildir, ipucudur.** Hepsi başka ajanların alanındadır ve
> bu ajan hiçbirinde sonuç üretmemiştir.

## İP-3A-1 → `gumruk-vergi-uzmani`

**Kanal bacağında KDV üç ayrı yerde vardır, model yalnızca birini
uyguluyor.** `kanal-katman-matrah-haritasi.md` §3.3:

| Görünüm | Matrah | Modelde |
|---|---|---|
| V1 raf/menü KDV'si | `L8_net` | ✅ `R1` |
| V2 mal faturası KDV'si | `L6` → `L6_gross` | ⚠ yok (alacak matrahı!) |
| V3 hizmet faturası KDV'si (`f`, `d`) | `d·L6 + f` | ❌ yok |

**Neden önemli:** V3'ün indirilebilirliği `f`+`d`'nin ekonomik maliyetini
**1,20 katına** çıkarabilir. V2 ise `peak_cash`'i **%20** etkiler.
→ `T-611`

---

## İP-3A-2 → `gumruk-vergi-uzmani`

**`vergi.yaml`'da HoReCa hizmet KDV oranı için AYRI BİR ALAN YOK.**
Model `R1`'i HoReCa menü fiyatına da ürün KDV oranıyla uyguluyor.
`marj-vs-markup.md` §2.3 bu riski TUR 2'de yazmıştı; model uyarıyı
**kullanmadı**. → `T-612`

---

## İP-3A-3 → `navlun-lojistik-uzmani`

**TR-içi lojistik rakamının TESLİM NOKTASI tanımı yazılı değil.**
Zincir **merkezi alım** yapar (`EV-2026-08-10-613` dipnot 14) ve ayrıca
bizden **lojistik bedeli** alır (`EV-2026-08-10-612`). Bu iki bacak
örtüşüyorsa **çift sayım**, örtüşmüyorsa mevcut model doğru — **ama
hangisi olduğu bilinmiyor.** → `T-618`

---

## İP-3A-4 → `finans-fizibilite` (ve `seytanin-avukati`)

**`reverse-price-model.md` §0.2'nin *"13 kalemin 13'ü de MAX_CIF'i yukarı
saptırır"* tespiti kanal bacağında da geçerlidir ve liste 7 kalem daha
uzuyor:** `f` ölçek asimetrisi · `d`'nin sabit bileşenleri · iade/fire ·
vade finansmanı · vade matrahı (`L6_gross`) · `f`+`d` KDV'si · tekel
kanalının üç sıfırı.

**Mertebe:** `K7` (38,00) + `K11` (19,38) + `K12` (27,55) ≈ **85 TL/şişe**
= `TGT_799 · CHAIN · BASE` tavanının (**272,83**) **%31'i.**
→ `70-kanal/kanal-bacagi-hata-listesi.md`

---

## İP-3A-5 → `turkiye-pazar-kasifi`

**Kanal karması modelin ölçülmemiş en büyük ekseni olabilir.**
`kanal_karmasi` üç alanın **üçü de `null`**. Üç kanalın tavanı
`TGT_799 · BASE`'te **272,83 / 303,90 / 87,88** — yani karma varsayımı
tek başına birleşik tavanı **3,5 kat** oynatabilir. Tornado'nun
**hiçbir ekseninde yok.**

**Uyarı:** nokta sayıları (GK 48.956 · ASN 29.218, `EV-2026-08-10-613`)
**ciro payı DEĞİLDİR** ve öyle kullanılamaz. Modern kanal nokta sayısı
zaten yoktur. → `T-603`

---

## İP-3A-6 → `yatirim-komitesi-baskani`

**`T-942`'nin önerdiği `R8-K` assertion'ı, birebir kodlanırsa `R5`
düzeltmesini geri alır.** `L5_max + μ·L6` ifadesi `L6`'ya değil `L7_eff`'e
eşittir; `L6` etiketiyle devam edilirse `d` ve `f` **iki kez** düşülür ve
test **tersine döner**: doğru formül reddedilir, naif formül kabul edilir.

**`T-942`'nin teşhisi doğrudur** — düzeltilmesi gereken tek şey `K1`
adımının etiketidir. Ama kabul kriteri olarak duruyor. → **`T-619`
(CRITICAL)**

---

## İP-3A-7 → `global-sourcing-kasifi`

**`T-605` (üreticiden alınan "marka/pazarlama katkısı" ↔ listeleme bedeli
çift sayımı) hâlâ açıktır** ve bu turda `K6c` olarak hata listesine
girmiştir. RFQ 5.6'daki katkı, `f` ile **aynı satırda netleştirilmelidir**;
aksi hâlde aynı para hem gelir hem gider olarak modele girer.
