# ÇAPRAZ İPUÇLARI — gumruk-vergi-uzmani (TUR 1.5, 2026-08-10)

> Alan dışı bulgular. **Sonuç üretilmemiştir** (CLAUDE.md §1.10, §1.11).
> `99-ops/capraz-ipuclari.md` ana dosyasına DOKUNULMAMIŞTIR.

---

## → `navlun-lojistik-uzmani`

### Cİ-15.1 — Kırılma/fire oranı artık bir VERGİ kalemidir (MEDIUM–HIGH)

KDVK **md.30/c** (T1, `EV-2026-08-10-103`): *"…**zayi olan mallara ait katma
değer vergisi**"* indirilemez.

Bu, fire oranını salt bir lojistik kaybı olmaktan çıkarır:

```
fire_maliyeti = f × (L4_per_sise)              ← malın kendisi
              + f × (KDV_per_sise)             ← İNDİRİLEMEYEN KDV  ← YENİ
```

Yani cam şişede **her %1 fire, KDV kanalından ayrıca ~%1 × 40–45 TL/şişe**
gerçek ekonomik maliyet yaratır (illüstratif CIF=100 TL'de). Bu, TUR 1'de
hiçbir yerde modellenmemiştir.

**İstenen:** `lojistik.yaml`'a `fire_orani` alanı (deniz taşıması + antrepo +
iç dağıtım kırılması). Kanıtlı bir bant yoksa `null` + `UNKNOWN`.
Vergi tarafı hazır: `vergi.yaml → kdv_perspektifleri.a_ekonomik_maliyet.
kdv_ekonomik_maliyete_donusme_kosullari[K2]` ve `hesap_sozlesmesi.turev_ciktilar
→ kdv_fire_maliyeti`.

### Cİ-15.2 — `lojistik.yaml → urun_fizik.sise_hacmi_ml = 750` aynı hijyen sorununu taşıyor (LOW)

`T-906(a)` `vergi.yaml`'daki `sise_hacmi_litre = 0.75` alanını
`FACT` + `evidence_id: null` → `ASSUMPTION` + `EV-2026-08-10-116` olarak
düzeltti. Başkanın denetimi (§3.2) **aynı sayının** `lojistik.yaml`'da da
`FACT` + `evidence_id: null` durduğunu tespit etmişti.

**Bu dosyaya DOKUNULMADI** (ajan izolasyonu). Aynı düzeltme orada da
yapılabilir; `EV-2026-08-10-116` kartı doğrudan referans alınabilir.

### Cİ-15.3 — Antrepo, ÖTV/GV'nin yanı sıra KDV nakit çıkışını da öteler (MEDIUM)

`EV-2026-08-10-106` (KDVK md.10/ı, T1): ithalatta vergiyi doğuran olay
**serbest dolaşıma giriş beyannamesinin tescilidir.** Bu yalnızca ÖTV ve gümrük
vergisi için değil, **KDV için de** geçerlidir.

Sonuç: `T-101` (antrepodan kısmi çekiş) sorusunun `peak_cash_requirement`
üzerindeki etkisi TUR 1'de sanılandan **daha büyüktür** — çünkü ertelenen tutar
sadece kalıcı vergiler değil, **devreden KDV havuzunun kendisidir.**
Kısmi çekiş mümkünse devreden KDV havuzu **hiç oluşmayabilir.**

**Karşı kalem (değişmedi):** ÖTV maktu tutarı Ocak/Temmuz'da artar
(`EV-2026-08-09-114`) → bekletme ÖTV artış riski taşır.

---

## → `finans-fizibilite`

### Cİ-15.4 — Devreden KDV'nin finansman maliyeti L5'te GERÇEK bir maliyettir

KDV ekonomik maliyet **değildir** (indirilebilir), ama **bedava da değildir.**
Devreden KDV nakden **iade edilmez** (KDVK md.29/2, `EV-2026-08-10-104`) ve
28–59 gün (ilk konteynerde satış hızı kadar) kilitli kalır.

```
kdv_finansman_maliyeti = ortalama_devreden_KDV × finansman_orani × sure_yil
```

`finansman_orani` `makro.yaml` alanıdır ve şu an `null`/`UNKNOWN`'dır.
Bu kalem **L5'te ayrı satır** olmalıdır (`vergi.yaml → engine_kurallari[C3]`).

### Cİ-15.5 — "Vergi yükü" tek satırda toplanamaz

`ekonomik_vergi_yuku = GV + İGV + KKDF + ÖTV` — **KDV DAHİL DEĞİL.**
`kdv_nakit_cikisi = KDV` — L5'e taşınmaz ama `peak_cash_requirement`'a
**tam tutarıyla** girer.

L4'e bakıp "şişe başına vergi yükü ~140 TL" demek **yanlıştır**.
Bkz. `vergi.yaml → hesap_sozlesmesi.turev_ciktilar` ve `engine_kurallari[C2, C4]`.

---

## → `mevzuat-ruhsat-uzmani` (bilgi notu — sonuç üretilmemiştir)

### Cİ-15.6 — Bandrol bedelinin katmanı, KDV matrahını da ilgilendiriyor

Başkanın denetimi (§2.5) bandrolün L5 değil **L3**'te doğabileceğini ve
vergilendirilebilir olabileceğini tespit etmişti (`T-203`).

TUR 1.5'te KDVK **md.21** tam metni okundu (`EV-2026-08-10-108`, T1):
matraha *"(c) gümrük beyannamesinin **tescil tarihine kadar** yapılan diğer
giderler ve ödemelerden **vergilendirilmeyenler**"* girer.

İki koşul birlikte aranır: **(1)** ödeme tescilden **önce** yapılmış olmalı,
**(2)** kendisi **vergilendirilmemiş** olmalı. Bandrol bedeli KDV'ye tabi bir
hizmet bedeli ise (2) sağlanmayabilir.

**Bu bir sonuç değildir** — bandrolün hukuki niteliği ve KDV'ye tabi olup
olmadığı `mevzuat-ruhsat-uzmani` alanıdır. Yalnızca `T-203`'ün doğru soruyu
sorabilmesi için madde metni buraya bırakılmıştır.

### Cİ-15.7 — KVK md.11/1-(ı): alkol reklam gideri KKEG (bilgi notu)

`EV-2026-08-10-113` (T1): alkollü içki **ilan/reklam giderlerinin %50'si**
kurum kazancının tespitinde indirilemez; KDVK md.30/d uyarınca o kısma ait
**KDV de indirilemez.**

**Bu bir vergi bulgusudur ve bu ajanın alanındadır.** Ancak alkolde reklamın
4250 / 7584 kapsamında **hukuken mümkün olup olmadığı** araştırılmamıştır
(bu tur kapsamı dışı ve `mevzuat-ruhsat-uzmani` alanı). Reklam hukuken
yapılamıyorsa bu hükmün pratik etkisi **sıfırdır** — dolayısıyla bu bir
"maliyet kalemi" olarak modele **girmemiştir.**
