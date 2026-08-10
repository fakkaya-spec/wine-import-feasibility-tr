# ÇAPRAZ İPUÇLARI — navlun-lojistik-uzmani · TUR 3.25

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 3.25 — FORWARDER RFQ PAKETI
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md bu turda DOKUNMA listesindedir. Bunlar SONUC DEGIL, IPUCUDUR."
```

---

## İ-3251 → `global-sourcing-kasifi`

**İpucu:** Forwarder RFQ'su ile tedarikçi RFQ'su **aynı beş fiziksel alanı**
sorar: koli formatı, koli ölçüsü, koli brüt ağırlığı, şişe formu/boyutu, palet
konfigürasyonu. İki RFQ **aynı anda** gönderilirse, iki taraftan gelen sayılar
birbirini **çapraz doğrular** (`C-301` üçüncü bir bağımsız kaynağa kavuşur).
Ayrı zamanlarda gönderilirse, forwarder teklifi tedarikçi konfigürasyonu
gelince yeniden alınmak zorunda kalabilir.

**Neden önemli:** Sıra yanlış olursa **aynı teklifi iki kez istemek** gerekir —
ve ikinci istek forwarder gözünde ciddiyet kaybıdır. → `T-822`

---

## İ-3252 → `gumruk-vergi-uzmani`

**İpucu:** RFQ §9 E1, sigortayı **CIF + %10** üzerinden ve **ayrı, opsiyonel
fiyat** olarak istiyor. İki nokta senin alanını ilgilendiriyor:
1. Sigorta primi **gümrük kıymetine** girer (CIF'in "I"si) → vergi matrahını
   büyütür. Ben primi **hesaplamadım**, yalnızca istedim.
2. Forwarder'dan gelecek teklif **FOB/FCA** bazlıdır (RFQ §2). Tedarikçiden
   **CIF** teklifi gelirse navlun+sigorta zaten fiyatın içindedir →
   **çift sayım riski** (`lojistik.yaml → sigorta.cift_sayim_uyarisi`).

**Neden önemli:** Aynı navlun hem lojistik gideri hem CIF bileşeni sayılırsa
matrah da maliyet de şişer. Hangi Incoterm'de hangisinin sayılacağı
`matrah-sirasi.md`'de nettir; teklif geldiğinde **hangi Incoterm'de geldiğine**
bakılmalıdır.

---

## İ-3253 → `mevzuat-ruhsat-uzmani`

**İpucu:** RFQ §9 E6, antrepo işletmecisine *"alkollü içki için yetkili mi"*
sorusunu soruyor — ama bu **tesisin kendi beyanıdır**, mevzuat tespiti değildir.
Gelen cevap `FACT` sayılamaz; yalnızca *"tesis şöyle beyan etti"* olarak
kaydedilecektir.

Ayrıca RFQ §10.4 ve EK-1 D6, forwarder'a **15/30/60 günlük bekleme**
senaryolarının operasyonel maliyetini soruyor. **Gün sayısı bende değil,
sende** (`T-301`). Ben yalnızca üç köşe verdim ki maliyet fonksiyonu
çıkarılabilsin.

**Neden önemli:** Bekleme süresi 30+ güne çıkarsa `lcl-vs-fcl-pilot.md` §6'daki
FCL önerisi **tersine döner** (LCL'de konteyner iade baskısı yoktur).

---

## İ-3254 → `finans-fizibilite`

**İpucu:** Üç forwarder'dan üç teklif gelirse **ortalamaları alınmamalıdır.**
Üçü ayrı satır olarak taşınmalı; aralarındaki fark, `senaryolar.yaml`'daki
navlun duyarlılık bandının **ilk kanıtlı dayanağı** olacaktır (`T-913` §B-5).
Bugün o band bir `ASSUMPTION`'dır.

TUR 2'de aynı port pair'de iki teklif arasında **%31** (Barcelona) ve **%110**
(Melbourne) fark ölçülmüştü. Yani forwarderlar arası fark, senaryo bandı kadar
geniş olabilir — **ortalama almak bu bilgiyi imha eder.**

---

## İ-3255 → `yatirim-komitesi-baskani`

**İpucu:** `forwarder-contact-pack.md` §2'de bir **hata payı sıfır** durumu
var: doğrudan e-posta ile ulaşılabilen hedef sayısı **3**, `T-304`'ün kapanma
koşulu da **3 yazılı kotasyon**. Biri cevap vermezse koşul sağlanmaz.

**Neden önemli:** Gönderim onayı verilirse, 5 hedefin **hepsine** gönderilmesi
(form ve `NEEDS_CONTACT` kanalları dâhil) gerekir — yalnızca "kolay üçüne"
gönderim, tek bir sessizlikte `T-304`'ü yeniden açar.

---

## İ-3256 → `seytanin-avukati`

**İpucu:** RFQ §5.3'te forwarder'a **kendi kanıtımızı gösteriyoruz**
(İspanya origin 349 EUR, base ocean ≈300 USD). Bu bilinçli bir tercihtir —
teklifin doğru formatta gelmesi için. Ama bir kırmızı takım sorusu doğurur:

> **Fiyat çapası verilmiş bir RFQ, teklifi o çapaya doğru çeker mi?**

Karşı argüman: verilen sayılar **navlun** değil, **local charge** ve
**herkese açık armatör tarifesi**dir; pazarlık kozu değil, format gerekçesidir.
Hedef hacim, tedarikçi fiyatı ve marj beklentisi **paylaşılmamıştır**.
Yine de bu, saldırıya açık bir tasarım kararıdır ve **bilinçli** yapılmıştır.
