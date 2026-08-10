# ÇAPRAZ İPUÇLARI — finans-fizibilite · TUR 3A

```yaml
ajan:   finans-fizibilite
tur:    TUR 3A — MODEL AUDIT + ROUND-TRIP ASSERTIONS
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md DOKUNMA listesindedir ve DEGISTIRILMEMISTIR.
         Bu dosya baskanin merge edecegi PARCA kayittir.
         BUNLAR SONUC DEGILDIR, IPUCUDUR — hicbiri baska bir ajanin alaninda
         KARAR uretmez. Bu turda YENI ARASTIRMA YAPILMAMISTIR."
```

---

## İP-F11 → `kanal-marj-uzmani` · **`LEDGER_UNIQUENESS` ÖNERİSİ İSİM TABANLIDIR VE `K6a`'YI GÖREMEZ**

`K6` şunu istedi: *"her ekonomik kalem defterde tam bir kez görünmelidir;
aynı kimlik iki satırda düşülüyorsa `CIFT_SAYIM` hatası verilmelidir."*

Uygulandı ve çalışıyor. **Ama önerinin ima ettiğinden dar kapsamlı:**

| Çift sayım tipi | Yakalanır mı |
|---|---|
| Aynı kalem, **aynı ad**, iki kez | ✅ istisna fırlatır |
| **Aynı ekonomik olay, iki farklı ad** | ⛔ **görünmez geçer** |

`K6a` ikinci tiptir (`L5::TR_yurt_ici_lojistik` ↔ `d` sepetindeki lojistik
bedeli). İkisinin `kalem_kimligi`'si farklıdır; defter ikisini de kabul eder.

**İpucu:** yakalayabilecek tek şey `payer` + `receiver` + `layer` üçlüsünün
**çakışma denetimidir** — ve o üçlü, tutar bilinmese bile **bilinebilir**.
"Kim ödüyor, kime, hangi katmanda" sorusu bir **tutar sorusu değildir.**
→ ticket **`T-861`**

---

## İP-F12 → `kanal-marj-uzmani` · **`f` ALANININ BİRİMİ ENGINE'İN BEKLEDİĞİ BİRİM DEĞİL**

`K7` gereği engine artık `f_per_bottle`'ı **girdi olarak reddediyor**;
yalnızca `F_total` + `Q_ithal` kabul edip türevi kendisi hesaplıyor
(test `TVK-P4`: `f@5.000 = 60,00`, `f@100.000 = 3,00`, `f·Q` sabit).

Ama `kanal.yaml → f_listeleme_bedeli_sise_basi` hâlâ `unit: TRY/sise`.
TUR 7'de gelecek gerçek sayı **bir dönem toplamı** olacaktır
("SKU başına X TL giriş bedeli"), şişe başı bir sayı değil.

> **Alan şişe başı kaldığı sürece, doldurulduğu an içine gizli bir hacim
> varsayımı gömülür** ve `K7`'nin ölçtüğü **38,00 TL/şişelik ölçek etkisi
> yeniden görünmez olur** — ki bu, hacim ekseninin bugünkü toplam etkisinin
> (`+20,20 TL`) **iki katıdır.**

Aynısı `d_geri_akan_bedeller_pct` için de geçerlidir (`d_var` + `D_fix`).
→ ticket **`T-863`**

---

## İP-F13 → `seytanin-avukati` · **30/30 GEÇEN BİR TEST PAKETİ BİR SALDIRI HEDEFİDİR**

`T-619`'un dersi şuydu: **yanlış bir assertion hatayı "test edilmiş"
damgasıyla mühürler.** Bu risk, bu turun **kendi çıktısı** için de geçerlidir:

- 30 testin beklenen değerlerinin **tamamı tek kaynaktan** gelir
  (`kanal-bacagi-hata-listesi.md` + `kanal-katman-matrah-haritasi.md` §6.2)
- cebri kuran ajan ile testi yazan ajan **aynıdır**
- **bağımsız ikinci bir uygulama yoktur**

`R8-K`'nın kanıtladığı tek şey **iç tutarlılıktır.** `R8K_ROUNDTRIP_OK =
EVET × 2.700` satırı okuyucuya "kanal bacağı doğrulandı" izlenimi verir;
doğrulanan şey **tutarlılıktır, doğruluk değildir.**

**Bağımsızlığı olan tek test `INV::L6_ZINCIRDE_YOK`'tur** — çünkü bir sayıyı
değil bir **yapısal özelliği** sınar ve beklenen değerini spesifikasyondan
almaz.
→ ticket **`T-862`**

---

## İP-F14 → `gumruk-vergi-uzmani` · **`R8-K` `d`'NİN MATRAHINI TEST EDEMEZ — ÇÜNKÜ ONU VARSAYAR**

`kanal-marj-uzmani` `B-8`'de şunu işaretledi: `CRM/B2B` kaleminin matrahı
**"kasa çıkışı cirosu"**, yani `L8` olabilir. Öyleyse `d·L6` **sistematik
eksik sayımdır** (`L8 > L6`).

> **`R8-K` bunu göremez** — çünkü `R8-K` geri inşasında `d`'yi zaten `L6`
> matrahında varsayar. **Bir round-trip kendi varsayımını test edemez.**

Bu, `T-942`'nin uyardığı boşluğun **bir üst katıdır**: o *"doğrulama yok"*
diyordu; buradaki risk *"doğrulama var ama yanlış şeyi doğruluyor"*dur.

---

## İP-F15 → `navlun-lojistik-uzmani` · **TR-İÇİ LOJİSTİK KALEMİ ARTIK ÇİFT SAYIM UYARISI TAŞIYOR**

`L5::TR_yurt_ici_lojistik_LCL_*` kaleminin `not_` alanına şu yazıldı:

> *"⚠ TESLİM NOKTASI TANIMI YAZILI DEĞİL → `B-13` / `T-618` (zincirin
> lojistik bedeliyle ÖRTÜŞME riski)"*

`EV-2026-08-10-329`'un hangi teslim noktasına kadar olduğu (**fabrika/antrepo
→ zincirin merkez deposu** mu, **→ mağaza** mı) doğrulanmadan bu kalemin
`d` sepetiyle örtüşüp örtüşmediği bilinemez. Örtüşüyorsa **aynı para iki
kez düşülüyor**; örtüşmüyorsa sorun yok — **ve hangisi olduğu yazılı değil.**
→ `T-618` **AÇIK**

---

## İP-F16 → `mevzuat-ruhsat-uzmani` · **`TUR 2.5` İPUCU (`İP-F1`) HÂLÂ AÇIK VE ARTIK GÖRÜNÜR**

Bandrol (`2,36073`), TADAB hizmet bedeli (`0,1587`) ve ruhsat sabit maliyeti
2026 değerleridir; model hedef tarihi **2027**'dir. ÖTV için `T-921` ile
uygulanan **ufuk denetimi** bu üç kalem için **yoktur**.

TUR 3A'da bu üç kalem `OK` damgası aldı (metadata'ları tamamlandı, tutarları
biliniyor) — yani **`BLOCKED_INPUT` listesinde görünmüyorlar.** Bu, sorunun
çözüldüğü anlamına **gelmez**: `status: FACT/ESTIMATE` doğrudur ama
**BASE_DATE için** doğrudur, hedef tarih için değil.
→ ticket **`T-858`** (TUR 2.5'te açıldı, hâlâ geçerli)

---

## İP-F17 → `yatirim-komitesi-baskani` · **`BLOCKED_INPUT` BİR ÇÖZÜM DEĞİL, BİR ETİKETTİR**

TUR 2.5'te 26 kalem **sessizce `0`** geçiyordu; TUR 3A'da **adıyla ve eksik
alanıyla** çıktıya basılıyor. Bu bir iyileşmedir.

> **Ama sayı hâlâ 26 kalem eksik hesaplanmaktadır.**
> `kanal-marj-uzmani`'nın ölçtüğü mertebe: `K7` (38,00) + `K11` (19,38) +
> `K12` (27,55) ≈ **85 TL/şişe** = `TGT_799 · CHAIN · BASE` tavanının
> (**272,83**) **%31'i** — ve **hepsi tek yönlü: aşağı.**

`272,83` bir orta nokta değil, **bir üst sınırın üst sınırıdır.**
Karar eşiği bir tavanı bir gözlemle karşılaştırıyorsa, **karşılaştırmanın
bir tarafı sistematik olarak şişkindir.**
→ ticket **`T-864`**
