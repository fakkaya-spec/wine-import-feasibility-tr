# ÇELİŞKİLER — kanal-marj-uzmani · TUR 3A
<!-- 99-ops/celiskiler.md'ye BASKAN tarafindan birlestirilir. Bu dosya bir PART'tir. -->

## C-611 — DIŞ DİSTRİBÜTÖR MARJININ MODELDEKİ YERİ, KANAL BELGESİYLE ÇELİŞİYOR

```yaml
conflict_id:   C-611
acan:          kanal-marj-uzmani
tarih:         2026-08-10
durum:         OPEN
impact:        HIGH
```

| | **Kaynak A** | **Kaynak B** |
|---|---|---|
| Belge | `70-kanal/kanal-marj-yapisi.md` §6 (TUR 2, **bu ajan**) | `80-model/outputs/reverse-price-model.md` §7.1 + `ters_model.py:392` (TUR 2.5) |
| Tier | repo-içi spesifikasyon | repo-içi model uygulaması |
| İddia | *"distribütör marjı **`L6` ile `L7` arasına girer**"* — yani distribütör **bir katman olarak araya girer** ve zincir bedellerini **kendisi üstlenir** | Distribütör marjı, ithalatçının `L5` bütçesinden **`m_dist × L6`** olarak düşülür; **`d` ve `f` aynı anda ithalatçıda kalır** ve *"aynı anda ikisi birden uygulanırsa **TOPLANIRLAR**"* |

### Neden çelişiyor

İki okuma **aynı ekonomik dünyayı tarif etmiyor**:

- **A**: distribütör → perakendeci ilişkisini distribütör yönetir; zincirle
  yıllık anlaşmayı (`EV-2026-08-10-612`) o imzalar; ciro primini ve
  listeleme bedelini **o öder**. Bizim yükümüz `m_dist`'tir, `d` **değildir**.
- **B**: her iki yük de bizde. Yani zincire hem `d·L6 + f` ödüyoruz hem
  distribütöre `m_dist·L6` ödüyoruz.

**Bu bir hesap farkı değil, bir DÜNYA farkıdır.** Üstelik `B` altında
distribütörün ne sattığı belirsizdir: `L6` hem *bizim* fatura fiyatımız
hem *distribütörün* fatura fiyatı gibi kullanılmaktadır — **modelde
distribütör için ayrı bir katman YOKTUR.**

### Büyüklük

`TGT_799 · CHAIN BASE · d = %8`: `d·L6 = 43,4239 TL/şişe`
→ `MAX_CIF`'te **28,95 TL/şişe** (g=0,50).
**`R5` hatasıyla tam olarak aynı büyüklük, ters yön** — bu kez model
**aşırı kötümser** olabilir.

### Bu ajan sessizce seçim YAPMAMIŞTIR

Distribütörün zincir bedellerini üstlenip üstlenmediği **sözleşmeye
bağlıdır ve hiçbir kanıtımız yoktur** (`kanal.yaml`: *"TUR 2'DE HİÇBİR
KANITLI DEĞER BULUNAMAMIŞTIR"*). Bu ajan bir taraf **seçmemiş**, iki alt
senaryo tanımlamıştır:

```
A1 : d ve f BIZDE          + m_dist    (modelin bugunku davranisi)
A2 : d ve f DISTRIBUTORDE  + m_dist    (m_dist buyur, d ve f sifirlanir)
```

### Çözüm yolu

`T-617` (`finans-fizibilite`) — iki alt senaryonun **ayrı ayrı**
koşulması ve §7.1'deki *"özdeştir / toplanırlar"* ifadesinin
kaldırılması veya koşullandırılması. **Nihai çözüm ancak gerçek bir
distribütör görüşmesiyle gelir** (`T-604`, TUR 7).

---

## C-602'YE EKLEME — TEKEL BAYİ MARJININ **MATRAH** BOYUTU

```yaml
conflict_id:   C-602 (mevcut — kapatilmadi, GENISLETILDI)
ekleyen:       kanal-marj-uzmani
tarih:         2026-08-10
```

`C-602` bugüne kadar **seviye** çelişkisiydi (T5 kaynaklar birbiriyle
çelişiyor: *"alkolde ~%17"*, *"rakı %8"*, *"brüt %10–15"*,
*"ciro üzerinden %18–30"*).

**TUR 3A eklemesi — bu bir MATRAH çelişkisidir de:** bağımsız alkollü içki
noktasında ticari dil üç farklı olabilir ve **ikisi aynı, biri farklı sonuç
verir** (`L8_net = 665,83`, oran %18 illüstratif):

| Konuşma biçimi | Matrah | `L7_eff` |
|---|---|---|
| *"marjım %18"* (margin on selling price) | `L8_net` | **546,00** |
| *"tavsiye fiyattan %18 iskonto"* | `L8_net` | **546,00** *(aynı)* |
| *"maliyetin üstüne %18 koyarım"* (markup) | `L7_eff` | **564,27** *(+18,28)* |

`MAX_CIF` farkı **+12,19 TL/şişe** (g=0,50).

**Model bugün birinci okumayı kullanıyor ve bunu gerekçelendirmiyor.**
`kanal.yaml → tekel_bayi.marj_pct.margin_mi_markup_mi` alanı **`null`**'dır
— yani M1 kuralı gereği o sayı zaten geçersizdir.
→ `kanal-katman-matrah-haritasi.md` §4.1, `B-10`.

---

## C-551'E NOT — kapatılmadı, hatırlatılıyor

`C-551` (599,90 TL'nin KDV dahil olup olmadığı) **açıktır** ve bu turda
**ele alınmamıştır.** `kanal-katman-matrah-haritasi.md` bu sayıyı hiçbir
yerde kullanmamıştır (`M2`/`M3` gereği).
