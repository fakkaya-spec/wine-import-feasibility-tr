# ÇAPRAZ İPUÇLARI — global-sourcing-kasifi — TUR 1.5

```yaml
ajan:   global-sourcing-kasifi
tur:    TUR 1.5 — BLOCKER REMEDIATION (T-902)
tarih:  2026-08-10
kapsam: Yalnizca T-902 duzeltmesi + RFQ alan kontrolu. YENI ARASTIRMA YAPILMADI.
```

> Bu dosya bir **parça dosyasıdır**. `99-ops/capraz-ipuclari.md` ana dosyasına
> `yatirim-komitesi-baskani` tarafından birleştirilir. Bu ajan ana dosyaya dokunmadı.

---

## 1. `finans-fizibilite` — EN KRİTİK, MODELİ SESSİZCE BOZABİLİR

**`tedarikci.yaml`'daki iki seri artık L1 (FOB) etiketi taşımıyor. Aralarında çıkarma
işlemi yapmayın.**

TUR 1'de iki alan yanlışlıkla L1 (FOB) etiketiyle duruyordu. T-902 ile bu etiketler
geri çekildi. Somut risk şudur:

```
YANLIŞ:  navlun = L2_CIF_serisi − "L1"_serisi
SONUÇ:   İspanya, Portekiz ve Fransa için NEGATİF NAVLUN
```

Bu üç menşede "L1" serisi L2 serisinden **büyüktür**. Bu bir veri hatası değil, iki
serinin farklı şeyleri ölçtüğünün kanıtıdır (farklı ürün karması, farklı para birimi,
farklı raporlama bazı, farklı yıl kesiti — detay `tedarikci.yaml →
ulke_gosterge_birim_degerleri.karsilastirilamazlik_kaniti`).

Uyulması gereken üç kural YAML içine gömüldü:
- `duyarlilik_sinirlari_KARISIK_KATMAN.finans_fizibiliteye_uyari`
- `karsilastirilamazlik_kaniti.kullanim_yasagi` (4 madde)
- `kullanim_kurali: SENSITIVITY_BOUNDS_ONLY` (çit korundu)

**`fiyat.fob_per_sise` hâlâ `null`/`UNKNOWN`'dır ve bu turda da öyle kalmıştır.**
Gerçek FOB yalnızca RFQ ile alınacak `FIRM_OFFER`'dan gelir.

**Ek kural (T-902 sonrası):** duyarlılık çıktısı raporlanırken **hangi sınırın hangi
katmandan geldiği** yazılmak zorundadır. Alt sınır `L0_ALTI`, üst sınır `L2`'dir.

---

## 2. `navlun-lojistik-uzmani` — RFQ artık ağırlık verisini eksiksiz soruyor

`rfq-template.md` v2.1'de eklenen alanlar sizin konteyner/ağırlık hesabınız içindir:

| Yeni soru | Ne veriyor |
|---|---|
| 1.14 | Boş şişe ağırlığı (g) — koli brüt ağırlığının (2.2) bağımsız çapraz kontrolü |
| 1.15 | Dolu şişe brüt ağırlığı (g) — kapak, kapsül, etiket dahil |
| 1.16 | Hafif şişe alternatifi + şişe başına fiyat farkı — ağırlık/navlun ödünleşimi |
| 3.17d | Lead time'ın "gemi/kamyon bekleme" bileşeni ayrı soruluyor |

**Sizden bir talebim var:** v2.1'i bir kez okuyup Bölüm 2 (2.1–2.13) + 1.14/1.15 ile
konteyner doluluk hesabınızı **gerçekten kurabiliyor musunuz**, eksik bir alan var mı?
Varsa şablona eklerim — şablon TUR 7'de gönderildikten sonra eklemek geç olur.
(T-402 hâlâ OPEN.)

---

## 3. `gumruk-vergi-uzmani` — RFQ 3.18 ve 3.20 sizin matrahınızı ilgilendirebilir

Şablona eklenen 3.18, kuru malzeme kalemlerinin (etiket, karton, kapsül, palet)
**EXW fiyatının içinde mi dışında mı** olduğunu ayrı ayrı soruyor. 3.20 ise ihracat
evrak ücretlerini soruyor.

**Neden size ipucu bırakıyorum:** bu kalemlerin faturada ayrı satır olarak mı yoksa
mal bedeline dahil mi geldiği, gümrük kıymetinin oluşumunu etkiliyor olabilir.
**Bu benim alanım değil ve bir sonuç üretmedim.** Eğer fatura yapısı kıymet açısından
fark yaratıyorsa, RFQ'ya bu turdan sonra bir soru daha ekleyebilirim — söyleyin.

---

## 4. `yatirim-komitesi-baskani` — iki bakım işi

1. **`10-evidence/index.csv`:** `EV-2026-08-09-404`, `-419` ve `-421` kartlarının
   `status` alanı kart dosyalarında `SUPERSEDED` yapıldı, ancak `index.csv`
   satırlarında hâlâ eski değer duruyor. Bu ajan `index.csv`'ye dokunmakla
   yetkilendirilmedi. Yeni satırlar:
   `10-evidence/_index-parts/global-sourcing-kasifi-tur15.csv` (başlıksız, 3 satır).
2. **Terminoloji uyarısı:** `fob_gosterge_bandi` adı repoda **beş dosyada daha**
   geçiyor (denetim raporu, T-902, tickets/INDEX.md, `capraz-ipuclari.md` §607,
   TUR 1 raporu §5). Bunlar **tarihsel kayıttır ve değiştirilmemiştir** — geçmişi
   yeniden yazmak kanıt disiplinine aykırı olurdu. İzlenebilirlik için YAML'a
   `eski_adi` alanı eklendi. Arama yapan biri hem eski hem yeni adı bulur.

---

## 5. `seytanin-avukati` — size iki yeni saldırı vektörü bırakıyorum

1. **RFQ v2.1 uzadı.** 13 soru daha eklendi. Kendinizi bir üretici yerine koyup
   şablonu okuyun: kaç satırı **kaçamak cevapla** geçiştirebilirsiniz? Özellikle
   S19/S20 ("etiket ve karton EXW'nin içinde mi") ve 3.6 (MOQ) satırlarını hedef
   alın. Şablon "N/A veya TBC yazın" diyor — bu dürüstlüğü teşvik eder, ama aynı
   zamanda **cevaptan kaçmak için meşru bir kapı** açar.
2. **Katman düzeltmesi bir şeyi çözmedi, sadece dürüstçe etiketledi.** T-902 sonrası
   elimizde hâlâ **tek bir gerçek EXW veya FOB rakamı yok.** "Katman etiketi
   düzeltildi" cümlesi ilerleme gibi okunabilir; okunmamalı. Fiyat bilgisi açısından
   TUR 1.5, TUR 1'den bir milimetre ileride değildir.

---

## 6. BU TURDA YAPILMAYANLAR (kapsam dışı, bilinçli)

- Yeni tedarikçi, yeni ülke, yeni fiyat araştırması **yapılmadı**.
- Hiçbir üreticiye e-posta/mesaj **gönderilmedi**.
- OIV ihracat değer tanımının FOB olup olmadığı **araştırılmadı** (açık soru olarak
  kaydedildi — bkz. `acik-sorular-global-sourcing-kasifi-tur15.md`).
- Vergi, navlun tutarı, ruhsat ve kanal marjı konularında **sonuç üretilmedi**.
