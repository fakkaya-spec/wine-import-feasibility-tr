# AJAN RAPORU — GÜMRÜK & VERGİ (TUR 2)

```yaml
ajan:               gumruk-vergi-uzmani
tur:                TUR 2 — COMMERCIAL VALIDATION (DESTEK MODU)
tarih:              2026-08-10
durum:              SUBMITTED
kapsam:             TEK GOREV — mense -> uygulanacak tarife eslemesi (9 ulke) + T-104
kapsam_disi:        Yeni genel vergi arastirmasi YAPILMADI (GTIP, OTV yapisi, KDV, KKDF, gozetim TUR 1/1.5'te bitti)
evidence_araligi:   EV-2026-08-10-151 … EV-2026-08-10-165 (15 kart)
```

---

## 1. YÖNETİCİ ÖZETİ

9 ülkenin tamamı için menşe → tarife eşlemesi kuruldu ve **hiçbiri `UNKNOWN`
kalmadı**: **İspanya, Şili, Portekiz, İtalya, Fransa %50** — **Güney Afrika,
Arjantin, ABD, Avustralya %70**. Menşe ispat belgesi sorusu, TUR 1'den beri
açık olan bir `UNKNOWN`'dı ve **kapandı**: hem AB tarım rejimi (1/98) hem Şili
STA'sı için **EUR.1 Dolaşım Belgesi (MBS 0302) veya Fatura Beyanı (MBS 0538)**
(`EV-2026-08-10-155`, `-158`, `-160`).

**Bu turun en önemli tek bulgusu bir orandan çok bir koşuldur: %50 oranı
KOŞULLUDUR.** Belge ibraz edilemezse ya da doğrudan nakliyat sağlanamazsa
**otomatik olarak %70** uygulanır (`EV-2026-08-10-157`). CIF = 100 TL/şişe'de
bu **+24,00 TL/şişe**'dir — nominal 20 puanlık farktan büyük, çünkü gümrük
vergisi KDV matrahına da girer. Model bu yüzden artık `applicable_customs_rate`'i
sabit değil, **iki senaryo değişkenine bağlı** okumak zorundadır.

İkinci bulgu: **BİLGE sistemi çıkış ülkesi kontrolü yapıyor.** Şili menşeli
şarapta çıkış ülkesi **yalnızca Şili** olabilir; AB tarım rejiminde kabul
edilen çıkış ülkeleri listesinde **Birleşik Krallık yoktur** (`EV-2026-08-10-158`,
`-160`). Yani **konsolidasyon rotası bir vergi kararıdır** — bu, navlun
tarafında hiç görünmeyen bir kaldıraçtır.

Üçüncü bulgu, "STA var = indirim var" varsayımını **aynı tablonun içinde**
çürütüyor: **EFTA**, Türkiye'nin ilk STA'sıdır (1992) ama 2204.21 için ne
sütunu ne dipnotu vardır → **%70** (`EV-2026-08-10-164`). Ülke tarama kuralı
"STA var mı?" değil, **"I sayılı Liste'de sütun/dipnot var mı?"** olmalıdır.

`50-sourcing/supplier-priority-ranking.md` tur sırasında yayımlandı ve
A-priority 7 tedarikçi eşlendi (`mense-tarife-eslemesi.md` §1.1):
**6 tedarikçi %50, 1 tedarikçi (Harland, AU) %70.** Ayrıca B-priority'de
kapsam dışı bir menşe çıktı ve ayrı kanıtla kapatıldı: **Moldova'nın STA'sı
vardır ama 2204.21'i kapsamaz → %70** (`EV-2026-08-10-165`) — Purcari'nin
"en düşük L2 CIF" avantajının bir kısmı tarifeyle geri alınır; aynı grubun
Romanya/Bulgaristan tesisleri ise **%50** öder.

**T-104** (CRITICAL) → **`ANSWERED`**. `vergi.yaml`'a `otv_maktu_zaman_serisi`
bloğu eklendi: gözlenen değerler + geçerlilik ufku (2026-12-31) + engine okuma
kuralı. `RESOLVED` **yapmadım** — hedef ajan `finans-fizibilite`'dir.

---

## 2. BULGULAR

### B-13: 9 ülkenin tamamı eşlendi — üç ülke grubu, iki oran

```yaml
claim:          2204.21'de Ispanya/Italya/Portekiz/Fransa (AB 1/98) ve Sili (STA) %50; G.Afrika/Arjantin/ABD/Avustralya (DU) %70
value:          "AB4 + CL: 50 | ZA, AR, US, AU: 70"
unit:           %
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-09-103, -104, -105 · EV-2026-08-10-152, -161, -164
effective_date: 2026-01-01
katman:         L2 -> L4
```

**Gerekçe:** Oranlar TUR 1'de İthalat Rejimi Kararı 2026 I sayılı Liste'den
alınmıştı; bu turda yeniden doğrulanmadı (gerekmiyordu). Yeni iş **negatif
tarafı kapatmaktı**: ABD, Avustralya, Arjantin ve Güney Afrika için tercihli
rejim **olmadığını** üç bağımsız yoldan gösterdim —
(a) İthalat Rejimi Kararı 2026 Kısaltmalar ekindeki **STA ülkeleri
enumerasyonu**nda yoklar (`EV-2026-08-10-152`, T1);
(b) GGM BİLGE **Menşe Kontrol Tablosu**'nun 37 anlaşma kodunun hiçbirinde
yoklar (`EV-2026-08-10-161`);
(c) EK-1 **GTS ülkeleri** listesinde yoklar (`EV-2026-08-10-153`, T1).

Bu, `EV-2026-08-09-125` (gözetim tebliği bulunamadı) tipi **zayıf bir negatif
arama değildir.** Her üç kaynak da **kapalı bir küme** tanımlar: listede olmamak
hükmen kapsam dışı olmaktır.

---

### B-14: Menşe ispat belgesi kapandı — EUR.1 **veya** fatura beyanı; A.TR **geçersiz**

```yaml
claim:          Hem AB tarim rejimi (1/98) hem Sili STA'si icin EUR.1 Dolasim Belgesi (0302) veya Fatura Beyani (0538) gecerlidir; A.TR menseyi ispat etmez ve sarapta kullanilamaz
value:          ["EUR.1", "Fatura Beyani"]
unit:           -
status:         FACT
tier:           T2 (AB) / T3 (Sili)
evidence_id:    EV-2026-08-10-155, -156, -158, -159, -160
effective_date: 2026-01-01
katman:         L2 -> L4 (kosul)
```

**Gerekçe (T2, Ticaret Bakanlığı Gümrük Rehberi):** *"Gümrük birliğinin kapsamı
dışında bırakılmış olan tarım ürünleri ve AKÇT ürünlerinin Türkiye ile Avrupa
Birliği arasındaki ticaretinin de tercihli ticaret anlaşmaları kapsamına
girdiğini hatırlatmak isteriz. Bu eşyanın … **EUR.1/EUR-MED Dolaşım Belgesi,
Fatura Beyanı / EUR-MED Fatura Beyanı** eşliğinde ticarete konu edilmesi
halinde ithalatçı ülkede tercihli rejimden faydalanması mümkündür."*

**A.TR tuzağı (T2 + T3):** *"A.TR Dolaşım Belgesi eşyanın menşeini göstermez
veya menşe ispat belgesi yerine geçmez."* (`EV-2026-08-10-156`). GGM Menşe
Kontrol Tablosu'nun `AT` satırı bunu sistem tarafında doğruluyor: A.TR'nin GTİP
kapsamı **"AKÇT ve tarım ürünleri HARİCİNDEKİ tüm ürünler"**dir
(`EV-2026-08-10-159`). AB'li bir tedarikçi alışkanlıkla A.TR gönderirse
**%50 düşer, %70 ödenir.**

**Yan sonuç:** Bu, TUR 1'in "Gümrük Birliği şarabı kapsamaz" bulgusunun
**ikinci bağımsız doğrulamasıdır.** TUR 1'de sonuç vergi oranından
türetilmişti; şimdi **belge/sistem tarafından** da doğrulandı.

---

### B-15: %50 oranı **KOŞULLUDUR** — dört kümülatif koşul, ikisi bizde değil

```yaml
claim:          Tercihli oran icin dort kosul birlikte gerekir: kapsam + mense kurali + gecerli belge + dogrudan nakliyat. Saglanmazsa DU orani (%70) uygulanir
value:          "K1 kapsam · K2 mense kurali · K3 belge · K4 dogrudan nakliyat"
unit:           -
status:         FACT
tier:           T2
evidence_id:    EV-2026-08-10-163 (kosullar), EV-2026-08-10-157 (yaptirim)
effective_date: -
katman:         L2 -> L4
```

**Gerekçe (T2):** *"…menşe ispat veya dolaşım belgesi verilemediği zaman,
ithalatçı firma vergi muafiyetinden veya indiriminden yararlanamayacak ve
**daha yüksek ithalat vergisi ödemek zorunda kalacaktır**."*

**Koşul sahipliği:**

| Koşul | Sahibi | Durum |
|---|---|---|
| K1 kapsam | `gumruk-vergi-uzmani` | ✅ kapandı |
| K2 menşe kuralı | `global-sourcing-kasifi` | ⏳ T-161 |
| K3 geçerli belge | `global-sourcing-kasifi` (tedarikçi) | ⏳ T-161 |
| K4 doğrudan nakliyat | `navlun-lojistik-uzmani` | ⏳ T-163 |

**Sayısal etki (CIF = 100 TL/şişe, peşin ödeme, illüstratif):**

| Kalem | Belge TAM (%50) | Belge YOK (%70) | Fark |
|---|---|---|---|
| Gümrük Vergisi | 50,0000 | 70,0000 | +20,0000 |
| ÖTV (maktu, değişmez) | 53,4519 | 53,4519 | 0,0000 |
| KDV %20 | 40,6904 | 44,6904 | +4,0000 |
| **L4 POST-TAX LANDED** | **244,1423** | **268,1423** | **+24,0000** |

Bu yüzden `vergi.yaml`'a iki **senaryo değişkeni** eklendi
(`tercihli_belge_ibraz_edildi`, `dogrudan_nakliyat_saglandi`), ikisi de
`ASSUMPTION` ve ikisi de `duyarlilik_zorunlu_mu: true`.

---

### B-16: BİLGE **çıkış ülkesi** kontrolü — rota seçimi bir vergi kararıdır

```yaml
claim:          Sili STA'sinda kabul edilen cikis ulkesi YALNIZCA Sili'dir; AB tarim rejiminde kabul edilen cikis ulkeleri listesinde BIRLESIK KRALLIK YOKTUR
value:          "SIL: {Sili} | ATRM: AB+SanMarino+EFTA+Faroe+Fas+B-Hersek+Kosova+Karadag+K.Makedonya+Filistin+Gurcistan+Sirbistan+Moldova+Misir"
unit:           -
status:         FACT
tier:           T3
evidence_id:    EV-2026-08-10-158, EV-2026-08-10-160
effective_date: 2026-01-01
katman:         L2 -> L4 (kosul)
```

**Gerekçe:** GGM BİLGE Menşe Kontrol Tablosu'nda her anlaşma satırı için
**"Menşe Ülke Kontrolü"** ve **"Çıkış Ülkesi Kontrolü"** ayrı sütunlardır.
`SIL` satırında çıkış ülkesi tek kelimedir: **"Şili"**.

**İki somut arıza:** (1) Şili şarabı Rotterdam/Antwerp konsolidasyonuyla
gelirse tercih düşer; (2) İspanyol şarabı BK deposundan sevk edilirse tercih
düşer. LCL tasarrufu 24 TL/şişe'yi aşmıyorsa **konsolidasyon net zarardır.**

**Cevabını bilmediğim ayrım:** gemi aktarması (transhipment) "çıkış ülkesi
değişimi" sayılır mı? → `OQ-G15`, ticket **T-163**. Bu ayrım Şili
senaryosunun tamamını değiştirebilir.

---

### B-17: **GTS şarapta yapısal olarak imkânsızdır** — üç bağımsız kanıt

```yaml
claim:          Genellestirilmis Tercihler Sistemi 2204.21'de hicbir kosulda uygulanamaz
value:          false
unit:           -
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-151, EV-2026-08-10-153, EV-2026-08-10-154
effective_date: 2026-01-01
katman:         -
```

| # | Kanıt |
|---|---|
| 1 | I sayılı Liste 21–22. Fasıllar tablosunda **GTS sütunu yoktur** (sütunlar: AB,BK · GÜR · B-HER · G.KORE · MLZ · SNG · KOS · VNZ · BAE · TPS-OIC · D-8 · DÜ) |
| 2 | **2204, GTS sütunu bulunan II sayılı Liste'de yer almaz.** O listede 22. fasıldan yalnızca 2201, 2202, 2203, **2205**, 2207, 2208 vardır |
| 3 | EK-1 GTS ülkeleri listesinde kapsamdaki **9 ülkenin hiçbiri** yoktur |

**Dikkat — kapsam uyarısı:** **22.05 (vermut/aromatize) II sayılı Liste'dedir**
ve orada **GTS sütunu VARDIR**. Yani bu bulgu 2204.21'e özgüdür; aromatize bir
SKU düşünülürse **bu tablo yeniden kurulmalıdır.**

---

### B-18: "STA var" ≠ "indirim var" — çürütücü örnek aynı tablonun içinde: **EFTA**

```yaml
claim:          Turkiye'nin ILK STA'si EFTA'dir (1992) ancak 2204.21 icin I sayili Liste'de ne sutunu ne dipnotu vardir -> %70
value:          70
unit:           %
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-164
effective_date: 2026-01-01
katman:         -
```

**Gerekçe:** I sayılı Liste 21–22. Fasıllar dipnotları: (1) K.Makedonya DÜ'nün
%50'si · (2) **Şili %50** · (3) Şili %0 *(yalnız 2207)* · (4) K.Makedonya %0 ·
(5) **Norveç ve İzlanda için AB sütunundaki oran** *(yalnız 2208.90.91/99)*.
2204.21 satırlarının dipnotu **"1.2"**dir — EFTA'nın ne sütunu ne dipnotu var.

**Türetilen tarama kuralı (`global-sourcing-kasifi`'ne bırakıldı, İP-2102):**
Yeni bir kaynak ülke değerlendirilirken sorulacak soru *"Türkiye'nin STA'sı var
mı?"* değil, ***"I sayılı Liste 21–22. Fasıllar tablosunda o ülke için SÜTUN
veya DİPNOT var mı?"***tır.

Aynı mantık Şili'de **ters yönde** de görünür: Şili STA'sı şarabı **kapsar ama
sıfırlamaz** (%70 → %50), buna karşılık **aynı anlaşma 2207 etil alkol için
%0 verir** (dipnot 3). Anlaşmaların tavizleri **ürün bazlıdır.**

---

### B-19: **Moldova'nın STA'sı şarabı kapsamıyor** — EFTA kuralının ikinci doğrulaması

```yaml
claim:          Turkiye-Moldova STA'si vardir ancak Moldova'nin I sayili Liste 21-22. Fasillar tablosunda ne sutunu ne dipnotu vardir -> Moldova mensei 2204.21 %70 oder; Romanya ve Bulgaristan (AB) %50 oder
value:          "MD: 70 | RO: 50 | BG: 50"
unit:           %
status:         FACT
tier:           T1
evidence_id:    EV-2026-08-10-165
effective_date: 2026-01-01
katman:         L2 -> L4
```

**Neden açtım:** `50-sourcing/supplier-priority-ranking.md` B önceliğinde
**Purcari Wineries Group (MD)** yer alıyor ve gerekçesi *"Moldova Türkiye'ye
en düşük L2 CIF menşei (2,46 USD/l)"*. Moldova, charter'daki 9 ülkelik kapsamın
**dışındadır** — bu yüzden ana tabloda satırı yoktu, ama sourcing tarafında
gündeme geldiği için kapatılması gerekiyordu.

**Bulgu:** GGM Menşe Kontrol Tablosu'nda `MD` satırı **vardır** (EUR.1/fatura
beyanı). Yani STA gerçektir. Ama I sayılı Liste 21–22. Fasıllar'da Moldova'nın
ne sütunu ne dipnotu var → **%70**. Bu, B-18'deki EFTA kuralının **ikinci
bağımsız örneğidir** ve İP-2102'deki tarama kuralını doğrular.

**Ek bulgu (aynı grup içinde tarife farkı):** Purcari'nin **Romanya ve
Bulgaristan** varlıkları AB üyesidir → **%50**. Yani *aynı grubun hangi
tesisinden yüklendiği* şişe başına CIF'in **%24'ü** kadar fark yaratır.
Sourcing kararı üretmiyorum; bu farkı `global-sourcing-kasifi`'ye girdi olarak
bırakıyorum.

---

### B-20: T-104 — ÖTV artık `vergi.yaml`'da zaman endeksli bir seridir

```yaml
claim:          OTV maktu tutari modelde sabit sayi olmaktan cikarildi; gozlenen_degerler + gecerlilik ufku + engine okuma kurali olarak tanimlandi
value:          "otv_maktu_zaman_serisi (2 gozlem, ufuk 2026-12-31)"
unit:           TRY/litre
status:         FACT (yapi) / UNKNOWN (gelecek deger)
tier:           T1 (mekanizma) / T2 (tutar)
evidence_id:    EV-2026-08-09-111, -112, -113, -114, -122
effective_date: 2026-07-03
katman:         L3 -> L4
```

Yapı: `gozlenen_degerler` (yalnız gerçekleşmiş, doğrulanmış tutarlar) ·
`son_gozlem_gecerlilik_ufku: 2026-12-31` · `gelecek_degerler: null / UNKNOWN` ·
`engine_okuma_kurali` (t > ufuk ve senaryo varsayımı yoksa **engine UNKNOWN
döner**) · `engine_yasak` (çakışmada seri esastır) · `antrepo_etkilesimi`
(antrepoda 1 Ocak/1 Temmuz'u geçirmek ÖTV'yi yükseltir).

`hesap_sozlesmesi` de güncellendi: `girdi`'ye `tarih_t` eklendi, ÖTV adımı
seriden okuyor.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden | Kritik mi | Nasıl bulunur |
|---|---|---|---|---|
| 1 | 1/98'in **ürün listesi** 2204.21'i içeriyor mu (`OQ-G12`) | Liste metnine erişilemedi; kapsam **%50 tavizden türetildi** | MEDIUM — **oranı değil, hukuki dayanağı** etkiler | 1/98 OKK eki; gümrük müşaviri |
| 2 | Transhipment "çıkış ülkesi değişimi" mi (`OQ-G15`) | Doğrudan nakliyat ile BİLGE çıkış kontrolü arasındaki ilişki belgelenmedi | **HIGH** — Şili senaryosunu değiştirir | T-163 → `navlun-lojistik-uzmani` |
| 3 | Fatura beyanının değer eşiği (`OQ-G13`) | Menşe protokollerine erişilemedi | LOW — EUR.1 alternatifi var | T-162 |
| 4 | DÜ menşede menşe şahadetnamesi zorunlu mu (`OQ-G14`) | Gümrük Yönetmeliği md.205 T1 metnine erişilemedi | LOW — **oranı değiştirmez** | T-162 |
| 5 | Tercihli oran sonradan geri alınabilir mi (`OQ-G16`) | Sonradan kontrol usulü incelenmedi | MEDIUM — kuyruk riski | Gümrük müşaviri |
| 6 | ~~A-priority tedarikçilerin ülkeleri~~ | ✅ **KAPANDI** — dosya tur sırasında yayımlandı, eşleme `mense-tarife-eslemesi.md` §1.1'de | — | — |

**TUR 1 ve TUR 1.5'in UNKNOWN'ları kapanmamıştır** ve kendi dosyalarında durur
(gözetim, KKDF matrahı, antrepo kısmi çekiş, damga vergisi, vergilendirme dönemi).

---

## 4. ÇELİŞKİLER

| conflict_id | Kaynak A | Kaynak B | Neden | Durum |
|---|---|---|---|---|
| **C-161** | Gümrük Rehberi (T2, tarihsiz): GTS için **Form A Menşe Belgesi** | GGM Menşe Kontrol Tablosu (T3, yürürlük 1/1/2026): **1049 REX Menşe Beyanı** | Muhtemelen Form A → REX geçişi; Rehber güncellenmemiş. Tarih kuralı B lehine, tier kuralı A lehine → **zıt yön** | **OPEN**, `impact: LOW`, `model_girdisi_etkisi: YOK` |

**Neden modeli bloke etmiyor:** GTS şarapta hiçbir koşulda uygulanmaz (B-17).
Ayrıntı: `99-ops/_parts/celiskiler-gumruk-vergi-uzmani-tur2.md`.

**Aynı kayıtta geçen yapısal uyarı:** Gümrük Rehberi'nin hiçbir sayfasında
yayın/güncelleme tarihi yoktur → tazeliği ölçülemez. Bu turda oradan alınan
**tüm** kanıtlara `effective_date: -` ve `ttl: 180d` yazılmıştır.

---

## 5. MODEL GİRDİLERİ

| YAML dosyası | Alan | Değer | status | evidence_id |
|---|---|---|---|---|
| vergi.yaml | `mense_tarife_eslemesi.ulkeler[9]` | ES/CL/PT/IT/FR = 50 · ZA/AR/US/AU = 70 | FACT | EV-2026-08-09-103/-104/-105 |
| vergi.yaml | `…ulkeler[*].preferential_regime` | ATRM (1/98) · SIL · null | FACT | EV-2026-08-10-152, -158, -160, -161 |
| vergi.yaml | `…ulkeler[*].required_origin_document` | ["EUR.1","Fatura Beyani"] / ["Menşe Şahadetnamesi (koşullu)"] | FACT | EV-2026-08-10-155, -160, -162 |
| vergi.yaml | `…tercihli_oran_kosullari[K1..K4]` | 4 kümülatif koşul + sahipleri | FACT | EV-2026-08-10-163 |
| vergi.yaml | `…engine_okuma_kurali` | koşullu oran + DÜ fallback | — | — |
| vergi.yaml | `…senaryo_degiskenleri.tercihli_belge_ibraz_edildi` | true (duyarlılık **zorunlu**) | **ASSUMPTION** | — |
| vergi.yaml | `…senaryo_degiskenleri.dogrudan_nakliyat_saglandi` | true (duyarlılık **zorunlu**) | **ASSUMPTION** | — |
| vergi.yaml | `…uygulanmayan_rejimler.gumruk_birligi_1_95` | false | FACT | EV-2026-08-10-159 |
| vergi.yaml | `…uygulanmayan_rejimler.gts` | false | FACT | EV-2026-08-10-151/-153/-154 |
| vergi.yaml | `…uygulanmayan_rejimler.efta_sta` | false | FACT | EV-2026-08-10-164 |
| vergi.yaml | `…uygulanmayan_rejimler.moldova_sta` | false (MD %70 · RO/BG %50) | FACT | EV-2026-08-10-165 |
| vergi.yaml | `tercihli_tarife.mense_ispat_belgesi` | **UNKNOWN → FACT** | FACT | EV-2026-08-10-155 |
| vergi.yaml | `tercihli_tarife.mense_ispat_belgesi_yoksa_uygulanan_oran` | 70 | FACT | EV-2026-08-10-157 |
| vergi.yaml | `tercihli_tarife.fatura_beyani_deger_esigi` | **null** | **UNKNOWN** | — |
| vergi.yaml | `otv_maktu_zaman_serisi.gozlenen_degerler` | 61,3914 (SUPERSEDED) · **71,2692** (FACT) | FACT | EV-2026-08-09-111, -112 |
| vergi.yaml | `otv_maktu_zaman_serisi.son_gozlem_gecerlilik_ufku` | 2026-12-31 | FACT | EV-2026-08-09-114 |
| vergi.yaml | `otv_maktu_zaman_serisi.gelecek_degerler` | **null** | **UNKNOWN** (bilinçli) | — |
| vergi.yaml | `hesap_sozlesmesi.girdi` | + `tarih_t`, `tercihli_belge_ibraz_edildi`, `dogrudan_nakliyat_saglandi` | — | — |

**BOZULMAYAN YAPILAR (doğrulandı):** `meta.BASE_DATE = 2026-08-10`,
`BASE_DATE_kurali`, `model_hedef_tarihi: null / TBD`, `kdv_perspektifleri`
(TUR 1.5), `matrah_sirasi[1..6]`, `engine_kurallari C1–C5`,
`peak_cash_requirement_sozlesmesi` — **hiçbirine dokunulmadı.**
YAML `yaml.safe_load` ile parse edilerek doğrulandı.

---

## 6. ÇAPRAZ İPUÇLARI

`99-ops/_parts/capraz-ipuclari-gumruk-vergi-uzmani-tur2.md`

| Kod | Hedef | İpucu |
|---|---|---|
| İP-2101 | `navlun-lojistik-uzmani` | Çıkış ülkesi kontrolü: Şili'de yalnız Şili, ATRM'de BK yok → konsolidasyon **+24 TL/şişe**'ye mal olabilir |
| İP-2102 | `global-sourcing-kasifi` | "STA var = indirim var" yanlış (EFTA örneği). Doğru tarama: **I sayılı Liste'de sütun/dipnot var mı?** |
| İP-2103 | `global-sourcing-kasifi` | Private label'da dökme şarabın başka ülkede şişelenmesi **menşe kuralını** bozabilir |
| İP-2104 | `global-sourcing-kasifi` + `navlun-lojistik-uzmani` | **A.TR tuzağı** — AB'li tedarikçi A.TR gönderirse %70 ödenir |
| İP-2105 | `kanal-marj-uzmani` | Menşe farkı (CIF'in %24'ü) kampanyayla geri kazanılamaz — maktu ÖTV gibi davranır |
| İP-2106 | `mevzuat-ruhsat-uzmani` | EUR.1 ihracatçı ülkede düzenlenir/vize edilir → T0 takviminde bir tedarikçi adımı var mı? |

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|---|---|---|---|---|
| **T-104** | `finans-fizibilite` | ÖTV zaman endeksli olmalı | **CRITICAL** | **OPEN → `ANSWERED`** *(veri yapısı kuruldu; engine + makro varsayım hâlâ hedef ajanda)* |
| T-161 | `global-sourcing-kasifi` | RFQ'da EUR.1/fatura beyanı + menşe + çıkış limanı sorulmalı | HIGH | OPEN |
| T-162 | `gumruk-vergi-uzmani` (kendime) | Fatura beyanı eşiği + md.205 menşe şahadetnamesi zorunluluğu | MEDIUM | OPEN |
| T-163 | `navlun-lojistik-uzmani` | Çıkış ülkesi kontrolü / transhipment ayrımı | HIGH | OPEN |

> **T-104 neden `RESOLVED` değil:** `target_agent` `finans-fizibilite`'dir.
> Ticket'ı açan ajan olarak tek taraflı kapatmam CLAUDE.md §5'i etrafından
> dolaşmak olurdu. Kapanış **başkana** aittir.

**G1 üzerindeki etki (bilgi — gate kararı bana ait değildir):**
`90-karar/tur-2-preflight-housekeeping.md` §D.4'teki üç boşluktan
**2 numaralı boşluğun "modelde sabit sayı olamaz" ayağı** yapısal olarak
karşılandı; ancak `model_hedef_tarihi` hâlâ `TBD` (`OQ-002`, yatırımcı girdisi)
ve **3 numaralı boşluk (gözetim/referans kıymet) aynen açıktır.**
Ayrıca T-104 `ANSWERED`'dır, `RESOLVED` değildir. **G1'i açmıyorum.**

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|---|---|---|
| EV-2026-08-10-151, -152, -153, -154, -164, -165 (İthalat Rejimi 2026 ekleri) | 90d | **2026-11-08** |
| EV-2026-08-10-155, -156, -157, -162, -163 (Gümrük Rehberi, T2) | 180d | 2027-02-06 |
| EV-2026-08-10-158, -159, -160, -161 (GGM Menşe Kontrol Tablosu, T3) | 180d | 2027-02-06 |

> ⚠️ **En kritik tazelik uyarısı bu turda değil, TUR 1'dedir:**
> `EV-2026-08-09-111` (ÖTV 71,2692 TL/lt) `ttl: 30d` ile **2026-09-08**'de
> STALE olur. `otv_maktu_zaman_serisi` o tarihte yeniden doğrulanmalıdır.
>
> ⚠️ **Oran satırlarının tamamı 2026-11-08'de STALE'dir** ve İthalat Rejimi
> Kararı **her yıl 1 Ocak'ta yenilenir.** Model 2027'ye uzanıyorsa oranlar
> yeniden okunmalıdır.

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU)*

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

**1/98 sayılı Karar'ın ekli ürün listesinde 2204.21'in bulunmadığının
tespiti.** GGM Menşe Kontrol Tablosu'nun `ATRM` satırı kapsamı *"yalnızca
tarım ürünleri listesindeki tüm ürünler"* diye tanımlıyor — **o listenin
kendisini görmedim.** 2204.21'in orada olduğunu, AB sütununda %50 taviz
bulunmasından **türettim.**

Eğer 2204.21 o listede değilse, %50 oranı başka bir hukuki temele dayanıyor
demektir ve **belge satırı (EUR.1/fatura beyanı) yanlış olur** — beş AB
ülkesinin (İspanya, İtalya, Portekiz, Fransa + Şili değil) belge sütunu çöker.
Oranlar (T1) ayakta kalır, **belgeler düşer.** `OQ-G12`.

**İkinci sıradaki geçersiz kılıcı:** GGM Menşe Kontrol Tablosu'nun 14.04.2026
sürümünün süpersede edilmiş olması. Tablo yılda birden fazla güncelleniyor
görünüyor; daha yeni bir sürüm çıkış ülkesi listelerini değiştirebilir.

### 9.2 En kırılgan varsayımım hangisi ve neden?

**"Şili'nin STA'sı 2204.21'i kapsıyor" varsayımı — ama beklenmedik bir
nedenden.** Oran (%50) I sayılı Liste dipnot (2) ile **T1**'dir, sağlamdır.
Kırılgan olan, o %50'nin **Türkiye-Şili STA'sından geldiği** çıkarımıdır.
Dipnot yalnızca *"Şili Cumhuriyeti için gümrük vergisi %50 olarak uygulanır"*
diyor — **anlaşmanın adını anmıyor.** Ben boşluğu STA ile doldurdum. Eğer bu
%50 otonom bir taviz olsaydı, **menşe ispat belgesi gerekmeyebilirdi** ve
tablonun Şili belge satırı yanlış olurdu. GGM tablosundaki `SIL` satırı bu
riski büyük ölçüde kapatıyor ama o satır **T3**'tür.

İkinci kırılgan varsayım: **belge senaryosunun varsayılanını `true` almam.**
`tercihli_belge_ibraz_edildi: true` bir kolaylıktır, bir bulgu değildir.
Bir tedarikçinin EUR.1 düzenleyeceğini **hiçbir kanıtla göstermedim.**
Bu yüzden `duyarlilik_zorunlu_mu: true` yazdım.

### 9.3 Hangi kaynağıma en az güveniyorum?

Sırayla:

1. **`EV-2026-08-10-158/-159/-160/-161` (GGM Menşe Kontrol Tablosu)** —
   Belgenin **kendisi** Ticaret Bakanlığı GGM'nin resmî yazısıdır ve içeriği
   son derece spesifiktir. Ama ben onu **bakanlığın sitesinden alamadım**;
   bir meslek örgütünün (İGMD) dosya sunucusundan indirdim. **T3**, `MEDIUM`.
   Bu turun **Şili ve çıkış ülkesi** bulgularının tamamı bu tek belgeye
   dayanıyor. Belge sahteyse ya da eskiyse, B-16'nın tamamı düşer.
2. **Gümrük Rehberi (T2) sayfaları** — Bakanlığın kendi sitesi, ama
   **hiçbir sayfada yayın veya güncelleme tarihi yok.** Yani "güncel resmî
   sayfa" tanımının **"güncel"** kısmını doğrulayamıyorum. TUR 1'de aynı
   ailenin bir sayfası (`EV-2026-08-09-126`) KDV'yi hâlâ %18 gösteriyordu.
   C-161 (Form A vs REX) tam da bu zayıflığın bir belirtisi olabilir.
3. **`EV-2026-08-10-152` (STA ülkeleri enumerasyonu)** — T1'dir ama bir
   **II sayılı Liste sütun tanımıdır**, "Türkiye'nin STA listesi" başlıklı bir
   belge değildir. Amacı dışında kullandığımı biliyorum; bu yüzden aynı
   sonucu `EV-2026-08-10-161` ile ikinci kez doğruladım.

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

- **Belge satırı yanlışsa (A.TR yeterliyse):** Operasyonel risk düşer, oranlar
  değişmez. Karar değişmez, sadece T-161 gereksizleşir.
- **Şili'nin %50'si kalkarsa (%70 olursa):** Şili, TIER A'dan fiilen düşer ve
  Yeni Dünya avantajı **tamamen** yok olur — kalan tüm %50'lik ülkeler AB'dir.
  `global-sourcing-kasifi`'nin coğrafi çeşitlendirme argümanı zayıflar.
- **Çıkış ülkesi kontrolü yanlışsa (transhipment sorun değilse):** Şili
  senaryosunun lojistiği **belirgin biçimde ucuzlar**; T-163 düşer.
- **Çıkış ülkesi kontrolü doğruysa ve doğrudan servis yoksa:** Şili fiilen
  **%70**'e döner. Bu, TIER A'nın beş ülkesinden birini eler.
- **Belge riski gerçekleşirse (+24 TL/şişe):** Bu, maktu ÖTV'nin (53,45 TL)
  **%45'i kadar** ek bir yüktür. Fiyat/performans segmentinde tek başına
  senaryo öldürebilir — ve **tamamen önlenebilir** bir maliyettir. Bu yüzden
  T-161 `HIGH`'dır.
- **Hiçbiri:** Bu tur **hiçbir gate'i açmaz veya kapatmaz.** G1 `BLOCKED`
  kalmaya devam eder (gözetim boşluğu + T-104 `ANSWERED` ≠ `RESOLVED`).

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)

| Ne | Kim | Nasıl | Süre |
|---|---|---|---|
| 1/98 ürün listesinde 2204.21 (`OQ-G12`) | Gümrük müşaviri | 1/98 OKK eki / BİLGE "tarım ürünleri listesi" ekranı | 1 gün |
| GGM Menşe Kontrol Tablosu'nun **resmî** kopyası ve son sürümü | Gümrük müşaviri | ticaret.gov.tr / GGM dağıtım yazısı | 1 gün |
| Transhipment ↔ çıkış ülkesi (`OQ-G15`) | `navlun-lojistik-uzmani` + gümrük müşaviri | T-163; forwarder'a doğrudan servis sorusu | 3–5 gün |
| Tedarikçinin EUR.1 düzenleyebilirliği | `global-sourcing-kasifi` | RFQ soru seti (T-161) | RFQ turuyla birlikte |
| Fatura beyanı eşiği + md.205 (`OQ-G13`, `OQ-G14`) | Gümrük müşaviri | Tek oturumda | 1 gün |
| Sonradan kontrol / tercih geri alınması (`OQ-G16`) | Gümrük müşaviri | Usul + emsal | 1–2 gün |

**Toplam:** TUR 1 raporundaki gümrük müşaviri oturumuna bu turdan **dört soru
daha** eklendi. Aynı tek oturum artık bu projedeki en yüksek bilgi/maliyet
oranına sahip **ikinci** eylemdir (birincisi hâlâ şarap rafının fotoğrafıdır).
