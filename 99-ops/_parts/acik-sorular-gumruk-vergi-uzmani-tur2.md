# AÇIK SORULAR — `gumruk-vergi-uzmani` (TUR 2)

> Kapsam: menşe → tarife eşlemesi. TUR 1 ve TUR 1.5'in açık soruları
> `acik-sorular-gumruk-vergi-uzmani.md` ve `…-tur15.md` dosyalarında durmaktadır
> ve **kapanmamıştır**.

---

## OQ-G12 — 1/98 sayılı Karar'ın **ürün listesi** 2204.21'i gerçekten içeriyor mu?

```yaml
id:        OQ-G12
impact:    MEDIUM
blocks:    -            # G1'i bloke ETMEZ (oran T1 ile sabit)
sahibi:    gumruk-vergi-uzmani
```

GGM Menşe Kontrol Tablosu'nun `ATRM` satırı, GTİP kapsamını *"**3 — Yalnızca
Tarım ürünleri listesindeki** tüm ürünler esas alınacaktır"* diye tanımlıyor
(`EV-2026-08-10-158`). **O "tarım ürünleri listesi"nin kendisini görmedim.**

2204.21'in o listede olduğunu, İthalat Rejimi Kararı'nın AB sütununda **%50
taviz bulunmasından türettim**. Türetme mantıklıdır (taviz varsa dayanağı
1/98'dir) ama **doğrudan gözlem değildir.**

**Neden G1'i bloke etmiyor:** `applicable_customs_rate = 50` değeri
`EV-2026-08-09-103` (T1, İthalat Rejimi Kararı) ile **doğrudan** sabittir.
Bu soru oranı değil, **oranın hukuki dayanağının adını** ve dolayısıyla
belge satırının doğruluğunu ilgilendirir.

**Nasıl kapanır:** 1/98 sayılı OKK'nın ekli ürün listesi (mevzuat.gov.tr /
ticaret.gov.tr — bu oturumda erişilemedi) veya gümrük müşaviri teyidi.
Bu, `mense-tarife-eslemesi.md`'nin **en zayıf halkasıdır.**

---

## OQ-G13 — Fatura beyanının değer eşiği ve "onaylanmış ihracatçı" koşulu

```yaml
id:        OQ-G13
impact:    LOW
blocks:    -
sahibi:    gumruk-vergi-uzmani
ticket:    T-162
```

Fatura beyanının belirli bir değer eşiği altında **her** ihracatçıya, üstünde
ise yalnızca **"onaylanmış ihracatçı"**ya açık olup olmadığı T1/T2 ile
doğrulanamadı. **Model etkisi yok:** EUR.1 her hâlükârda düzenlenebilir; bu
yalnızca tedarikçinin hangi belgeyi tercih edeceğini etkiler.

---

## OQ-G14 — DÜ menşede menşe şahadetnamesi **zorunlu** mu?

```yaml
id:        OQ-G14
impact:    LOW
blocks:    -
sahibi:    gumruk-vergi-uzmani
ticket:    T-162
```

Gümrük Rehberi (T2), menşe şahadetnamesinin ibrazını **ticaret politikası
önlemi** bağlamına bağlıyor (`EV-2026-08-10-162`). 2204.21'de yürürlükte bir
önlem tespit edilemedi (İGV yok — `EV-2026-08-09-107`; gözetim `UNKNOWN` —
`EV-2026-08-09-125`). Gümrük Yönetmeliği **md.205** T1 metnine erişilemedi.

**Model etkisi yok:** DÜ'de oran zaten %70; belge oranı değiştirmez.

---

## OQ-G15 — Transhipment ≠ çıkış ülkesi değişimi mi?

```yaml
id:        OQ-G15
impact:    HIGH
blocks:    -            # G1 degil, G2-L / G4 tarafinda
sahibi:    navlun-lojistik-uzmani
ticket:    T-163
```

BİLGE çıkış ülkesi kontrolü (`EV-2026-08-10-158`, `-160`) ile "doğrudan
nakliyat" koşulu (`EV-2026-08-10-163`) arasındaki tam ilişki bende
`UNKNOWN`'dır: **bir limanda gemi aktarması yapmak, o ülkeden "çıkış yapmak"
sayılır mı?**

**Neden HIGH:** Sayılıyorsa, Şili rotasında herhangi bir aktarma tercihli oranı
düşürür ve şişe başına **+24 TL** getirir. Sayılmıyorsa etki yoktur.
İki cevap arasındaki fark, tüm Şili senaryosunun ekonomisini değiştirir.

---

## OQ-G16 — Tercihli oran **sonradan geri alınabilir mi**?

```yaml
id:        OQ-G16
impact:    MEDIUM
blocks:    -
sahibi:    gumruk-vergi-uzmani
```

Gümrük Rehberi, menşe şahadetnamesinde *"ciddi bir şüphe durumunda gümrük
idareleri ek kanıtlar istemeye yetkilidir"* diyor. **Tercihli** belgelerde de
sonradan kontrol (subsequent verification) mekanizması olduğu biliniyor
(Rehber'de "Menşe ve dolaşım belgeleri üzerinde yapılan kontroller" başlığı
var) ancak **usulü ve sonucu bu turda incelenmedi.**

**Neden önemli:** İthalat anında ödenmeyen 20 puanın, aylar sonra **cezalı**
olarak istenmesi senaryosudur. Bu, bir maliyet kalemi değil bir **kuyruk
riskidir** ve `seytanin-avukati` için hedeftir.

---

## Ulaşılamayan resmî kaynaklar (2026-08-10 — dürüst kayıt)

| Host | Sonuç | Etkilenen soru |
|---|---|---|
| `mevzuat.gov.tr` | TLS handshake / connection reset | Gümrük Yönetmeliği md.205, Türkiye-Şili menşe yönetmeliği (No 14805), 1/98 OKK |
| `resmigazete.gov.tr` | Aynı | Aynı |
| `ticaret.gov.tr`, `ggm.ticaret.gov.tr`, `ab.ticaret.gov.tr` | Sunucu ara sertifika göndermiyor → TLS zinciri kurulamıyor; WebFetch 503 | STA listesi, Menşe Kontrol Tablosu'nun **resmî** kopyası |
| `gumrukrehberi.gov.tr` | ✅ Erişildi | T2 kanıtların kaynağı |
| `files.igmd.org.tr` | ✅ Erişildi | GGM Menşe Kontrol Tablosu PDF'i (T3 host) |

Bu, TUR 1'deki "TGTC taranmış görüntü" ve TUR 1.5'teki "TÜİK erişilemedi"
kayıtlarıyla aynı türden bir sınırlamadır ve **gizlenmemiştir.**
