# ÇELİŞKİLER — `mevzuat-ruhsat-uzmani` / TUR 1.5

> Bu dosya `99-ops/celiskiler.md`'ye **konsolide edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu turda **DOKUNULMAMIŞTIR** (tur mandası).
> CLAUDE.md §1.13: kaynaklar çelişirse **sessiz seçim yapılmaz.**

---

## A) MEVCUT ÇELİŞKİNİN DURUMU — C-201

```yaml
conflict_id:      C-201
onceki_durum:     OPEN (CRITICAL)
onerilen_durum:   RESOLVED — NON_MATERIAL
oneren:           mevzuat-ruhsat-uzmani
oneri_tarihi:     2026-08-10
karar_yetkisi:    yatirim-komitesi-baskani   # bu ajan KAPATMAZ
```

C-201 üç ayak üzerinde duruyordu. **İkisi bu turda düştü:**

| Ayak | Durum | Kanıt |
|---|---|---|
| **(1)** "Eşik 1.000.000 litre/yıl'dır" | ✅ **DÜZELDİ.** Kademeli indirim 2006 sonunda **600.000**'de bitmiştir. Kanun metnindeki 1.000.000 bugün uygulanan rakam değildir. | `EV-2026-08-10-204` (T1), `EV-2026-08-10-205` (T1) |
| **(2)** "Yaptırım mercii Tekel GM artık yok, hüküm fiilen uygulanamaz" | ✅ **ÇÜRÜDÜ** (proje aleyhine). 4733 m.4/B(b) 4250'nin uygulanmasını açıkça Bakanlığa vermiştir; 4733 m.8 artık fıkrası belge iptali yolunu açık tutar. | `EV-2026-08-10-208` (T1), `EV-2026-08-10-210` (T1) |
| **(3)** "Muafiyet fıkrası ithal durgun şarabı kapsamıyor olabilir" | ⚠️ **AÇIK** — ama **maddi değil**. Yeniden numaralandırıldı: **C-252** | `EV-2026-08-10-202` (T1) |

**Neden `NON_MATERIAL` öneriliyor:** C-201'in G0'ı bloke etme gerekçesi
*"beş hacim senaryosunun hukuki geçerliliği"* idi. Eşiğin **türü** (fiyatlandırma
serbestisi koşulu) ve **büyüklüğü** (600.000 L) kesinleştikten sonra, beş
senaryonun beşi de eşiğin **8–160 katı altındadır** ve eşik senaryolar arasında
ayrım yaratmamaktadır. Ayrıca eşiğin bağlı olduğu mekanizma ikincil mevzuata
aktarılmamıştır (`EV-2026-08-10-206`, `-209`).

**Bu ajan C-201'i KAPATMAMIŞTIR.** Kapatma başkanın yetkisindedir.

---

## B) YENİ ÇELİŞKİ — C-251

```yaml
conflict_id:        C-251
acilis_tarihi:      2026-08-10
acan_ajan:          mevzuat-ruhsat-uzmani
konu:               "2007 yilindan itibaren uygulanacak olcu 600.000 mi, kanun metnindeki 1.000.000 mi"
celiski_turu:       TANIM
impact:             LOW
model_girdisi_etkisi: YOK
durum:              OPEN

kaynak_a:
  evidence_id:      EV-2026-08-10-205
  iddia:            "Kademeli takvim 2006 sonunda 600.000 litre ile biter; '2007 yilindan itibaren uygulanacak olcuyu sifira indirmeye Bakanlar Kurulu yetkilidir' ifadesi, 2007'den itibaren UYGULANAN olcunun 600.000 oldugunu varsayar"
  value:            600000
  tier:             T1
  effective_date:   2003-06-06
  source_name:      "Alkol ve Alkollu Ickilerin Ic ve Dis Ticaretine Iliskin Usul ve Esaslar Hakkinda Yonetmelik Gecici m.6"

kaynak_b:
  evidence_id:      EV-2026-08-10-201
  iddia:            "Gecici hukmun kademeli takvimi tuketilmistir; asil kanun hukmu (m.1/3) 1.000.000 litre/yil demeye devam eder ve gecici hukum sona erdiginde asil hukum canlanir"
  value:            1000000
  tier:             T1
  effective_date:   2001-01-20
  source_name:      "4250 s.K. m.1 ucuncu fikra"
```

**Neden çözülemedi:** T1 ↔ T1, aynı kanun ailesi, ikisi de yürürlükte. Geçici
hükmün *"altıncı yıldan itibaren uygulanacak olan bu ölçü"* ifadesindeki *"bu
ölçü"*nün 600.000'e mi yoksa asıl hükümdeki 1.000.000'e mi gönderme yaptığı
lafzen belirsizdir. Tier, tarih, kapsam ve katman kurallarının hiçbiri
uygulanamıyor. Bu bir **hukuki yorum** sorunudur.

**Neden acele edilmesine gerek yok:** Bu proje için **maddi değildir.** Beş
senaryonun en büyüğü 75.000 litre/yıl'dır; her iki ölçüde de eşiğin çok
altındadır (%7,5 / %12,5). `EV-2026-08-10-215`.

**Kapanış yolu:** TADAB yazılı görüşü. Öncelik: **DÜŞÜK.**

---

## C) YENİ ÇELİŞKİ — C-252 *(C-201'in kalan ayağı)*

```yaml
conflict_id:        C-252
acilis_tarihi:      2026-08-10
acan_ajan:          mevzuat-ruhsat-uzmani
konu:               "4250 m.1 son fikrasindaki muafiyet ITHAL durgun sarabin fiyatlandirilmasi/dagitilmasi/satilmasini da kapsiyor mu"
celiski_turu:       TANIM
impact:             LOW
model_girdisi_etkisi: YOK   # her iki okumada da bes senaryo esigin altinda
durum:              OPEN
onceki_kayit:       "C-201'in ucuncu ayagi; bu turda ayri kayda alindi"
```

Fıkra metni (`EV-2026-08-10-202`, T1, yürürlük 2001-01-20):

> *"Bira ve her türlü şarap ve meyve şaraplarının üretimi, fiyatlandırılması,
> dağıtılması ve satılması ile viski ve tabii köpüren şarapların ithali,
> fiyatlandırılması, dağıtılması ve satılması bu maddede öngörülen şartlar
> aranmaksızın, bu Kanun hükümlerine göre serbesttir."*

| | Okuma A | Okuma B |
|---|---|---|
| **İddia** | Muafiyet **ürüne** bağlıdır: *her türlü şarabın* fiyatlandırılması, dağıtılması ve satılması — ithal olsun olmasın — m.1 şartlarından muaftır. Listede olmayan tek şey *ithal etme eylemi*dir; m.1/3'ün yaptırımı ise tam olarak fiyatlandırma/satış/dağıtımdır → **ithal şaraba uygulanamaz.** | Muafiyet yalnızca **yurt içinde üretilen** şaraba ilişkindir; kanun koyucu ithal yönünden bilinçli olarak yalnızca **viski ve tabiî köpüren şarabı** saymıştır → durgun şarap ithalatı m.1/3'e tabidir. |
| **Lafzî dayanak** | Tamlayan **ürün gruplarıdır** ("her türlü şarap"), "üretilen şaraplar" denmemiştir | "ile" bağlacıyla gelen ikinci kolda *ithal* ayrıca ve **sınırlı** sayılmıştır |
| **tier** | T1 (metin) | T1 (metin) |

**Neden çözülemedi:** Aynı cümlenin iki lafzî okuması. Tier/tarih/kapsam/katman
kurallarının hiçbiri uygulanamıyor. TUR 1 raporum yalnızca **B**'yi görmüştü;
**A** bu turda tespit edilmiştir ve en az B kadar lafzîdir. **Sessiz seçim
yapılmamıştır.**

**Neden karar açısından kritik değil:** B okuması doğru olsa bile, (i) beş
senaryonun beşi de eşiğin altındadır ve eşik bir *yasak* değil, bir *serbestlik
kazanma çizgisi*dir; (ii) eşiği aşamayanlar için öngörülen mekanizmanın ikincil
mevzuatta karşılığı yoktur (`EV-2026-08-10-206`, `-209`); (iii) o mekanizmanın
bugünkü ticari muhatabı `UNKNOWN`'dır (`EV-2026-08-10-214`).

**G0'ı yeniden bloke etmesi için gereken:** C-252'nin **B lehine** kapanması
**VE** aynı anda "Tekel GM eliyle" işlev için bir halef merci belirlendiğinin
tespiti. **İkisi birden** gerekir; tek başına hiçbiri bloke etmez.

**Kapanış yolu:** TADAB yazılı görüşü / alkol mevzuatında uzman hukuk bürosu
mütalaası. Öncelik: **DÜŞÜK.**

---

## D) DEĞİŞMEYENLER

`C-202` (HIGH, sıralama döngüsü), `C-203` (**CRITICAL**, 7584 s.K. raf kapsamı)
ve `C-204` (LOW, mülga dayanaklı TGK Şarap Tebliği) bu turda **ele alınmamıştır**
— tur mandası dışıdır. Durumları **değişmemiştir.**
