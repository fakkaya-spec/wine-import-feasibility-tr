# MENŞE → UYGULANACAK TARİFE EŞLEMESİ

```yaml
belge:            mense-tarife-eslemesi
sahibi:           gumruk-vergi-uzmani
tur:              TUR 2
tarih:            2026-08-10
kapsam:           GTIP 2204.21 — 750 ml sişelenmiş, köpüksüz (durgun) taze üzüm şarabı
BASE_DATE:        2026-08-10
evidence_araligi: EV-2026-08-10-151 … EV-2026-08-10-164 (+ TUR 1: -103, -104, -105, -106)
```

---

## 0. UYARI — BU TABLO **MENŞE** SEVİYESİNDEDİR, **TEDARİKÇİ** SEVİYESİNDE DEĞİLDİR

Gümrük vergisi oranı **eşyanın menşe ülkesine** göre belirlenir; tedarikçi firmaya,
markaya, bölgeye (Rioja / Alentejo / Maule), üzüm çeşidine veya fiyat bandına göre
**değişmez**. Bir ülkedeki iki farklı tedarikçi **aynı** oranı öder.

**Bu nedenle bu belge 9 ülke satırından ibarettir ve tedarikçi bazında
kırılamaz.** Tedarikçi bazında bir tarife satırı yazmak **yanlış hassasiyet**
üretir. `50-sourcing/supplier-priority-ranking.md` tur sırasında yayımlandı ve
A-priority listesi §1.1'de eşlendi — ama yapılan iş **yeni bir tarife
araştırması değil**, mevcut 9 satırın **yeniden etiketlenmesidir**.

**İSTİSNA (kritik):** Tedarikçi seviyesinde değişen tek şey oran değil,
**belgenin fiilen düzenlenip düzenlenemediğidir.** Bu bir tarife sorusu değil,
bir **tedarikçi yeterlilik** sorusudur → §5 ve ticket **T-161**.

---

## 1. ANA TABLO — 9 ÜLKE × 5 ALAN

| # | `country` | `applicable_customs_rate` | `preferential_regime` | `required_origin_document` | `evidence_id` |
|---|---|---|---|---|---|
| **TIER A** ||||||
| 1 | **İspanya** (ES) | **%50** | **VAR** — Türkiye-AB Ortaklık Konseyi **1/98** sayılı Karar (tercihli **tarım ürünleri** ticareti). *Gümrük Birliği (1/95) DEĞİL.* | **EUR.1 Dolaşım Belgesi** (MBS 0302) **veya** **Fatura Beyanı** (MBS 0538). **A.TR GEÇERSİZDİR.** | EV-2026-08-09-103 (oran); EV-2026-08-10-155, -158 (belge); EV-2026-08-10-156, -159 (A.TR geçersiz) |
| 2 | **Şili** (CL) | **%50** | **VAR** — Türkiye-Şili STA. Şarabı **kapsar ama sıfırlamaz**: I sayılı Liste dipnot (2) ile DÜ %70 → **%50**. | **EUR.1 Dolaşım Belgesi** (0302) **veya** **Fatura Beyanı** (0538). **Çıkış ülkesi Şili olmak zorunda** (çapraz kümülasyon YOK). | EV-2026-08-09-105, EV-2026-08-10-164 (oran); EV-2026-08-10-160 (belge + çıkış ülkesi) |
| 3 | **Portekiz** (PT) | **%50** | **VAR** — 1/98 (AB tarım rejimi) | EUR.1 (0302) **veya** Fatura Beyanı (0538). A.TR geçersiz. | EV-2026-08-09-103; EV-2026-08-10-155, -158 |
| 4 | **İtalya** (IT) | **%50** | **VAR** — 1/98 (AB tarım rejimi) | EUR.1 (0302) **veya** Fatura Beyanı (0538). A.TR geçersiz. | EV-2026-08-09-103; EV-2026-08-10-155, -158 |
| 5 | **Güney Afrika** (ZA) | **%70** | **YOK** | Tercihli belge **yok** (düzenlenemez). Tercihsiz menşe için **menşe şahadetnamesi** — zorunluluğu koşullu, bkz. §4. | EV-2026-08-09-104 (oran); EV-2026-08-10-152, -161 (STA yok); EV-2026-08-10-162 (belge) |
| **TIER B** ||||||
| 6 | **Fransa** (FR) | **%50** | **VAR** — 1/98 (AB tarım rejimi) | EUR.1 (0302) **veya** Fatura Beyanı (0538). A.TR geçersiz. | EV-2026-08-09-103; EV-2026-08-10-155, -158 |
| 7 | **Arjantin** (AR) | **%70** | **YOK** (MERCOSUR STA'sı yürürlükte değil) | Tercihli belge **yok**. Tercihsiz menşe için menşe şahadetnamesi — koşullu. | EV-2026-08-09-104; EV-2026-08-10-152, -161, -162 |
| 8 | **ABD / Kaliforniya** (US) | **%70** | **YOK** | Tercihli belge **yok**. Tercihsiz menşe için menşe şahadetnamesi — koşullu. | EV-2026-08-09-104; EV-2026-08-10-152, -161, -162 |
| 9 | **Avustralya** (AU) | **%70** | **YOK** | Tercihli belge **yok**. Tercihsiz menşe için menşe şahadetnamesi — koşullu. | EV-2026-08-09-104; EV-2026-08-10-152, -161, -162 |

> **Tüm oranlar `status: FACT`, `tier: T1`, `effective_date: 2026-01-01`**
> (İthalat Rejimi Kararı 2026, I sayılı Liste — Tarım Ürünleri, 21–22. Fasıllar).
> Belge satırlarının tier'ı **T2/T3**'tür — bkz. §6 kaynak kalitesi notu.

---

## 1.1 A-PRIORITY TEDARİKÇİLERİN ÜLKE EŞLEMESİ

Kaynak: `50-sourcing/supplier-priority-ranking.md` §2 (yalnızca **okundu**;
tedarikçi değerlendirmesi hakkında sonuç üretmiyorum).

| # | Tedarikçi | Ülke | **Oran** | Tercihli rejim | Gerekli belge |
|---|---|---|---|---|---|
| 1 | Harland Wine Company | **AU** | **%70** | YOK | Tercihli belge yok |
| 2 | Cantina Danese | **IT** | **%50** | 1/98 (AB tarım) | EUR.1 **veya** fatura beyanı |
| 3 | Interbrosa Family Wines | **ES** | **%50** | 1/98 (AB tarım) | EUR.1 **veya** fatura beyanı |
| 4 | The Wine Factory | **FR** | **%50** | 1/98 (AB tarım) | EUR.1 **veya** fatura beyanı |
| 5 | Corta Hojas Export Wine | **CL** | **%50** | Türkiye-Şili STA | EUR.1 **veya** fatura beyanı · **çıkış ülkesi Şili olmak zorunda** |
| 6 | Bodegas San Valero | **ES** | **%50** | 1/98 (AB tarım) | EUR.1 **veya** fatura beyanı |
| 7 | Casa Santos Lima | **PT** | **%50** | 1/98 (AB tarım) | EUR.1 **veya** fatura beyanı |

**Dağılım: 6 tedarikçi %50 · 1 tedarikçi %70.**
Tek %70'lik aday **Harland (AU)**'dur ve `supplier-priority-ranking.md`'de
zaten `K4 ❌` (Avustralya→Türkiye hattı fiilen yok) ile işaretlenmiş.
**Bu iki bağımsız olumsuz sinyalin çakışması kayda değerdir — ama sourcing
kararı benim alanım değildir; yalnızca tarife tarafını bildiriyorum.**

### 1.1.1 B-priority'de kapsam dışı iki menşe — **uyarı**

| Tedarikçi | Ülke | Oran | Not |
|---|---|---|---|
| Origin Wine · Zidela | **ZA** | **%70** | Kapsamdaki 9 ülkeden biri; tabloda var |
| **Purcari Wineries Group** | **MD** (+RO/BG) | **Moldova %70** · **Romanya/Bulgaristan %50** | ⚠️ **Moldova 9 ülkelik kapsamın DIŞINDADIR ve bu belgede satırı yoktu** |

**Moldova bulgusu (`EV-2026-08-10-165`, T1):** Türkiye-Moldova STA'sı **VARDIR**
(GGM Menşe Kontrol Tablosu `MD` satırı, EUR.1/fatura beyanı) **ama 2204.21'i
KAPSAMAZ** — Moldova'nın I sayılı Liste 21–22. Fasıllar tablosunda ne sütunu
ne dipnotu vardır → **%70**. Bu, **EFTA ile birebir aynı yapısal durumdur** (§2).

Sourcing raporu Purcari'yi *"Moldova Türkiye'ye en düşük L2 CIF menşei
(2,46 USD/l)"* gerekçesiyle listelemiş. **O CIF avantajının bir kısmı %70
tarifeyle geri alınır.** Ayrıca aynı grubun **Romanya ve Bulgaristan**
varlıkları AB üyesidir ve **%50** öder — yani *aynı grubun hangi tesisinden
yüklendiği vergi sonucunu değiştirir.*

> Bu bir **sourcing sonucu değildir**, bir vergi tespitidir. Purcari'nin
> sıralamadaki yeri hakkında görüş bildirmiyorum; `global-sourcing-kasifi`'ye
> girdi olarak bırakıyorum.

---

## 2. TERCİHLİ REJİM ŞARABI **KAPSIYOR MU?** — ASIL SORU BU

> **Bir STA'nın varlığı, o üründe indirim olduğu anlamına GELMEZ.**
> Bunun kanıtı aynı tablonun içindedir.

| Ülke / grup | STA var mı | **2204.21'i kapsıyor mu** | Sonuç |
|---|---|---|---|
| **AB (ES/IT/PT/FR)** | Gümrük Birliği (1/95) **VAR** | ❌ **HAYIR** — 1/95 **tarım ürünlerini kapsamaz** | 1/95 yerine **1/98** devreye girer → **%50** (sıfır değil) |
| **AB (ES/IT/PT/FR)** | Tarım rejimi (1/98) **VAR** | ✅ **EVET, kapsıyor** | **%50** — kısmi taviz, sıfır **değil**; tarife kontenjanı **yok** (EV-2026-08-09-108) |
| **Şili** | STA **VAR** | ✅ **EVET, kapsıyor** | **%50** — dipnot (2). *2207 (etil alkol) için aynı anlaşma %0 veriyor; şarap için vermiyor* |
| **EFTA (İsviçre/Norveç/İzlanda/Lihtenştayn)** | Türkiye'nin **ilk** STA'sı (1992) **VAR** | ❌ **HAYIR** — 2204.21 için ne sütun ne dipnot var | **%70** (DÜ). *Tek istisna: İsviçre/Lihtenştayn 30.000 lt/yıl tarife kontenjanı @ %35 — EV-2026-08-09-109* |
| **ABD / Avustralya / Arjantin / G.Afrika** | STA **YOK** | — | **%70** (DÜ) |
| **GTS (Genelleştirilmiş Tercihler Sistemi)** | Tek taraflı taviz sistemi **VAR** | ❌ **HAYIR** | Şarapta **yapısal olarak imkânsız** — bkz. §2.1 |

### 2.1 GTS neden şarapta hiç uygulanamaz — üç bağımsız kanıt

| # | Kanıt | evidence_id |
|---|---|---|
| 1 | I sayılı Liste (Tarım Ürünleri) 21–22. Fasıllar tablosunda **GTS sütunu yoktur**. Sütunlar: AB,BK · GÜR · B-HER · G.KORE · MLZ · SNG · KOS · VNZ · BAE · TPS-OIC · D-8 · DÜ | EV-2026-08-10-151 |
| 2 | **2204 GTİP'i, GTS sütunu bulunan II sayılı Liste'de yer almaz.** O listede 22. fasıldan yalnızca 2201, 2202, 2203, 2205, 2207, 2208 vardır | EV-2026-08-10-154 |
| 3 | EK-1 GTS ülkeleri listesinde kapsamdaki **9 ülkenin hiçbiri** yoktur | EV-2026-08-10-153 |

> Bu, `EV-2026-08-09-125` (gözetim tebliği bulunamadı) tipi **zayıf bir negatif
> arama değildir.** Üç kanıtın üçü de **pozitif yapısal gözlemdir**: sütun yok,
> satır yok, ülke yok.

### 2.2 Gümrük Birliği'nin şarabı kapsamadığı **iki bağımsız yoldan** doğrulandı

| Yol | Kanıt | Bulgu |
|---|---|---|
| **Vergi oranı tarafı** (TUR 1) | EV-2026-08-09-103 | Şarap **I sayılı Liste (Tarım Ürünleri)** içindedir; AB sütunu %50'dir, %0 değil |
| **Belge/sistem tarafı** (TUR 2) | EV-2026-08-10-159 | GGM Menşe Kontrol Tablosu, `AT` (1/95) satırı: A.TR'nin GTİP kapsamı **"AKÇT ve tarım ürünleri HARİCİNDEKİ tüm ürünler"** — BİLGE sistemi 2204 için A.TR'yi zaten kabul etmez |
| Ek doğrulama (T2) | EV-2026-08-10-163 | *"Tarım ürünleri ve AKÇT ürünlerinin Türkiye ile AB arasındaki ticareti serbest dolaşım esasına değil, **menşe** esasına dayanmaktadır."* |

---

## 3. BELGE YOKSA NE OLUR — TARİFE **KOŞULLUDUR**

`applicable_customs_rate` sütunundaki **%50 değerleri koşulludur.**
Koşul sağlanmazsa **otomatik olarak %70** uygulanır.

> **T2 alıntı (EV-2026-08-10-157):** *"…menşe ispat veya dolaşım belgesi
> verilemediği zaman, ithalatçı firma vergi muafiyetinden veya indiriminden
> yararlanamayacak ve **daha yüksek ithalat vergisi ödemek zorunda kalacaktır**."*

### 3.1 Tercihli rejimden yararlanmanın **dört kümülatif koşulu** (EV-2026-08-10-163)

| # | Koşul | 2204.21'de anlamı | Risk sahibi |
|---|---|---|---|
| K1 | Eşya **anlaşma kapsamında** olmalı | AB → 1/98 tarım listesi; Şili → dipnot (2). **EFTA'da sağlanmaz.** | `gumruk-vergi-uzmani` — ✅ kapandı |
| K2 | Anlaşmanın **menşe kuralını** karşılamalı ve menşeli olmalı | Şarap tek ülkede üretilir; "tamamen elde edilmiş" kuralı normalde sorunsuz. **Ancak dökme ithal şarabın başka ülkede şişelenmesi menşei bozabilir** → §5 | `global-sourcing-kasifi` |
| K3 | **Geçerli menşe ispat belgesi** bulunmalı | EUR.1 **veya** fatura beyanı; ihracatçı düzenler, gümrükte vize edilir | **Tedarikçi** → T-161 |
| K4 | **Doğrudan nakledilmiş** olmalı | Çıkış ülkesi kontrolü — bkz. §3.2 | `navlun-lojistik-uzmani` → T-163 |

### 3.2 Çıkış ülkesi kontrolü — **rota seçimi bir vergi kararıdır**

BİLGE sistemi menşe ülke kontrolünün **yanı sıra** çıkış ülkesi kontrolü yapar
(EV-2026-08-10-158, -160):

| Rejim | Kabul edilen **çıkış ülkeleri** |
|---|---|
| **ATRM** (AB tarım, 1/98) | AB üyesi ülkeler + San Marino + EFTA + Faroe Adaları + Fas + Bosna-Hersek + Kosova + Karadağ + K.Makedonya + Filistin + Gürcistan + Sırbistan + Moldova + Mısır |
| **SIL** (Şili STA) | **Yalnızca Şili** |

> ⚠️ **İki somut arıza senaryosu:**
> 1. **Şili menşeli şarap Rotterdam/Antwerp'te konsolide edilip oradan
>    yüklenirse** → çıkış ülkesi Şili değildir → **%50 düşer, %70 uygulanır.**
> 2. **İspanyol şarabı bir Birleşik Krallık deposundan sevk edilirse** →
>    **BK, ATRM çıkış ülkesi listesinde YOKTUR** → tercih düşer.
>
> LCL/konsolidasyon avantajı ile 20 puanlık tarife farkı **doğrudan çelişebilir.**
> Bu bir navlun kararı gibi görünür ama **vergi sonucu doğurur.**
> Çapraz ipucu bırakıldı; sonuç `navlun-lojistik-uzmani` alanındadır (T-163).

### 3.3 Sayısal etki — belge riskinin büyüklüğü

CIF = 100 TL/şişe illüstrasyonu (`matrah-sirasi.md` §4 zinciriyle, peşin ödeme):

| Senaryo | GV | ÖTV matrahı | ÖTV | KDV matrahı | KDV | **L4** |
|---|---|---|---|---|---|---|
| AB/Şili + **belge TAM** (%50) | 50,0000 | 150,0000 | 53,4519 | 203,4519 | 40,6904 | **244,1423** |
| AB/Şili + **belge YOK/RED** (%70) | 70,0000 | 170,0000 | 53,4519 | 223,4519 | 44,6904 | **268,1423** |
| **Fark** | +20,00 | | 0,00 | | +4,00 | **+24,0000 TL/şişe** |

> **Kaldıraç: CIF'in her 100 TL'si için 24 TL.** Yani belge riski nominal
> 20 puanlık tarife farkından **%20 daha büyüktür**, çünkü gümrük vergisi
> KDV matrahına da girer (ÖTV maktu olduğu için ondan etkilenmez).
> *Bu tablo model çıktısı değildir; zinciri göstermek içindir.*

---

## 4. DÜ MENŞELİ (ABD / AVUSTRALYA / ARJANTİN / G.AFRİKA) İÇİN BELGE DURUMU

| Soru | Cevap | status |
|---|---|---|
| Tercihli menşe ispat belgesi düzenlenebilir mi? | **HAYIR** — anlaşma yok, BİLGE'de satır yok | FACT (EV-2026-08-10-161, -152) |
| Menşe şahadetnamesi (tercihsiz) gerekir mi? | **KOŞULLU** — Rehber, ibrazı **ticaret politikası önlemi** bağlamına bağlıyor | FACT (EV-2026-08-10-162) |
| 2204.21'de yürürlükte ticaret politikası önlemi var mı? | İGV **yok** (FACT); gözetim **tespit edilemedi** (UNKNOWN) | EV-2026-08-09-107, EV-2026-08-09-125 |
| O hâlde menşe şahadetnamesi **zorunlu mu**? | **UNKNOWN** | ⚠️ Gümrük Yönetmeliği md.205 T1 metnine bu oturumda erişilemedi (mevzuat.gov.tr kapalı) → **T-162** |

> **Model etkisi: YOK.** DÜ menşede oran zaten %70'tir; belgenin varlığı ya da
> yokluğu **oranı değiştirmez** — yalnızca beyan/uyum yükü sorunudur.
> Bu yüzden bu UNKNOWN **G1'i bloke etmez.**

---

## 5. TEDARİKÇİ SEVİYESİNDE DEĞİŞEN TEK ŞEY: **BELGENİN DÜZENLENEBİLİRLİĞİ**

Tarife menşe seviyesindedir. Ancak K3 (geçerli belge) ve K2 (menşe kuralı)
**tedarikçiye bağlıdır.** RFQ'da sorulması gereken, oran değil şunlardır:

| Soru | Neden |
|---|---|
| EUR.1 düzenleyebiliyor musunuz? Ek ücret var mı? | Belge yoksa %50 → %70 |
| Fatura beyanı yapabiliyor musunuz? "Onaylanmış ihracatçı" statünüz var mı? | Fatura beyanının değer eşiği/koşulu **UNKNOWN** (T-162) |
| Şarap **tamamen sizin ülkenizde mi** üretildi ve şişelendi? Dökme ithal bileşen var mı? | Dökme ithal şarabın başka ülkede şişelenmesi K2'yi bozabilir — private label'da **yüksek risk** |
| Sevkiyat hangi limandan **çıkacak**? | K4 / çıkış ülkesi kontrolü (§3.2) |

> Bunlar `global-sourcing-kasifi`'nin RFQ alanıdır; **sonuç üretmiyorum**,
> ticket **T-161** ile devrettim. `50-sourcing/rfq-template.md` bu alanları
> içeriyorsa T-161 doğrudan kapanabilir.

---

## 6. KAYNAK KALİTESİ — DÜRÜST NOT

| Katman | Tier | Kaynak | Not |
|---|---|---|---|
| **Oranlar** (%50 / %70) | **T1** | İthalat Rejimi Kararı 2026 ekli listeler (ticaret.gov.tr, TUR 1'de indirilmiş ZIP) | Sağlam. Yeniden doğrulanmadı, gerekmiyordu |
| **AB tarım rejiminin belgesi** | **T2** | Ticaret Bakanlığı **Gümrük Rehberi** (gumrukrehberi.gov.tr) | Bakanlığın kendi sitesi. **Sayfalarda yayın/yürürlük tarihi yok** → `effective_date: -`, `ttl: 180d` |
| **Şili + tam ülke listesi + çıkış ülkesi kontrolü** | **T3** | GGM **BİLGE Sistemi Menşe Kontrol Tablosu**, 14.04.2026, yürürlük 1/1/2026 | ⚠️ Belge **GGM'nin resmî yazısıdır (T2 niteliğinde)** ama bu oturumda **İGMD** (meslek örgütü) sitesinden alınmıştır → **T3**, `confidence: MEDIUM` |

**Ulaşılamayan resmî kaynaklar (bu oturum):**
`mevzuat.gov.tr`, `resmigazete.gov.tr`, `ticaret.gov.tr`, `ggm.ticaret.gov.tr` —
tamamı TLS/503 nedeniyle erişilemedi. Bu nedenle **Gümrük Yönetmeliği md.205**,
**Türkiye-Şili STA menşe protokolü** ve **1/98 sayılı OKK Protokol 3** metinleri
**birincil kaynaktan okunamadı.** Kanıt kartlarında bu açıkça yazılmıştır.

**Bunun sonucu:** Şili satırının **oranı T1**'dir (sağlam), **belgesi T3**'tür
(daha zayıf). AB satırının hem oranı hem belgesi T1/T2 ile desteklidir.

---

## 7. MODEL İÇİN — `vergi.yaml` KARŞILIĞI

`80-model/inputs/vergi.yaml` → `mense_tarife_eslemesi` bloğu.
Engine, ülke koduna göre bu bloktan okur; **kodda ülke/oran hard-code edilmez.**

```
gv(mense) = cif_try × mense_tarife_eslemesi[mense].applicable_customs_rate / 100

KOŞUL:  mense_tarife_eslemesi[mense].preferential_regime != null
        VE belge_ibraz_edildi == true
        VE cikis_ulkesi ∈ kabul_edilen_cikis_ulkeleri
DEĞİLSE: gv = cif_try × 70 / 100     (DÜ fallback)
```

`belge_ibraz_edildi` bir **senaryo değişkenidir**, bir vergi verisi değildir.
Varsayılanı `true` alınmalı **ama duyarlılık ekseni olarak `false` de
çalıştırılmalıdır** (§3.3: +24 TL/şişe @ CIF 100).

---

## 8. BU BULGUYU NE ÇÜRÜTÜR?

### Hangi mevzuat değişikliği bu eşlemeyi geçersiz kılar?

- **İthalat Rejimi Kararı'nın yıllık yenilenmesi (her yıl 1 Ocak).** Oranlar
  yıllık Karar ile belirlenir; 2027 listesi 2026 Aralık sonunda yayımlanacaktır.
  `ttl: 90d` bu yüzden konmuştur — **2026-11-08'den sonra tüm oran satırları
  STALE'dir.**
- **Yeni bir STA'nın yürürlüğe girmesi.** Örneğin Türkiye–MERCOSUR veya
  Türkiye–ABD bir anlaşma yürürlüğe koyarsa Arjantin/ABD satırları değişir.
  Ancak **dikkat**: EFTA örneği (§2) gösteriyor ki yeni bir STA'nın şarabı
  kapsayacağının **hiçbir garantisi yoktur**. Yeni STA haberi görüldüğünde
  yapılacak iş, I sayılı Liste'de **sütun veya dipnot açılıp açılmadığına**
  bakmaktır — anlaşmanın varlığına değil.
- **1/98 sayılı OKK'nın revize edilmesi.** AB ile tarım ticaretinin
  güncellenmesi uzun süredir gündemdedir; şarap tavizinin %50'den değişmesi
  tüm AB satırlarını etkiler.

### Hangi GTİP itirazı tüm yapıyı değiştirir?

- **Ürünün köpüklü (2204.10) sayılması:** Gümrük vergisi oranları **aynı
  kalır** (%50/%70) ama ÖTV 53,45 → 361,14 TL/şişe olur. Bu tablo hayatta
  kalır, proje kalmaz.
- **Ambalajın 2 litreyi aşması (2204.22 / bag-in-box):** oranlar yine aynıdır.
- ⚠️ **Asıl tehlike başka yerde:** Ürün **22.05'e (vermut/aromatize)** kayarsa,
  22.05 hem I sayılı hem **II sayılı Liste**'dedir; II sayılı listede
  **EFTA, F.ADA, G.KORE, MLZ, GTS** sütunları vardır. Yani **bu belgenin
  "GTS uygulanmaz" sonucu 22.05'te geçerli değildir.** Aromatize/tatlandırılmış
  bir SKU düşünülürse bu tablo yeniden kurulmalıdır.
- 12 haneli alt kod itirazı oranı **değiştirmez** (EV-2026-08-09-102) — 2204.21
  altındaki 113 satırın tamamında AB,BK=50 ve DÜ=70 aynıdır.

### Gözetim / kıymet itirazı senaryosunda ne olur?

- **Menşe ile kıymet ayrı eksenlerdir.** Bir kıymet itirazı `applicable_customs_rate`'i
  **değiştirmez**; matrahı (CIF) yukarı çeker. Etki oranla çarpımsaldır:
  aynı kıymet artışı **DÜ menşede %70, AB/Şili menşede %50** kadar ek gümrük
  vergisi doğurur → **kıymet riski DÜ menşede 1,4 kat daha ağırdır.**
- ÖTV maktu olduğu için kıymet itirazından **etkilenmez** (EV-2026-08-09-113).
- **Tersi yönde bir risk daha var:** Menşe **şüphesi** (kıymet değil) hâlinde
  gümrük idaresi ek kanıt isteyebilir ve tercihli oran **sonradan** geri
  alınabilir. Bu, ithalat anında ödenmemiş 20 puanın **sonradan cezalı olarak**
  istenmesi demektir. Bu senaryonun olasılığı ve usulü bu turda
  **araştırılmamıştır** → açık soru.

### Bu belgeyi geçersiz kılacak **tek** bulgu

**GGM Menşe Kontrol Tablosu'nun güncel olmadığının veya tabloda 2204 için
özel bir kısıt/istisna bulunduğunun tespiti.** Tablonun `ATRM` satırı GTİP
kapsamını *"yalnızca tarım ürünleri listesindeki tüm ürünler"* diye tanımlıyor;
o "tarım ürünleri listesi"nin **kendisini görmedim**. 2204.21'in o listede
olduğunu, İthalat Rejimi Kararı'nın AB sütununda %50 taviz bulunmasından
**türettim**. Eğer 1/98'in ürün listesi 2204.21'i içermiyorsa, %50 oranı
başka bir hukuki temele dayanıyor demektir ve belge satırı yanlış olur.
Bu, bu belgenin **en zayıf halkasıdır** ve bir gümrük müşavirine sorulacak
ilk sorudur.
