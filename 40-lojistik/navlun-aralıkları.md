# NAVLUN ARALIKLARI — ROTA BAZLI

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 1
tarih:  2026-08-09
durum:  DRAFT
```

> ## ⛔ BU DOSYAYI OKUMADAN ÖNCE
>
> 1. **Bu turda tek bir kesin navlun fiyatına kilitlenilmemiştir.** Her rakam
>    aralıktır, tarihlidir, kaynaklıdır ve confidence taşır.
> 2. **Bizim rotalarımız için (Akdeniz/ABD/Şili/G.Afrika → Türkiye) kamuya açık
>    bir navlun endeksi YOKTUR.** Drewry WCI ve Freightos FBX bizim rotalarımızı
>    ölçmez. Onlar burada yalnızca **piyasa seviyesi ve yönü** için referanstır.
> 3. Aşağıdaki "Türkiye'ye giriş" rakamlarının tamamı `ESTIMATE` veya `UNKNOWN`
>    statüsündedir. **Hiçbiri `FACT` değildir.**
> 4. **Spot ≠ kontrat.** Aşağıdaki her şey spot piyasa göstergesidir.
> 5. **All-in ≠ base.** Her satırda neyin dahil olduğu yazılıdır. Yazmıyorsa
>    o rakam modele giremez.
> 6. Spot navlun kanıt kartlarının `ttl` değeri **14 gündür** →
>    **2026-08-23 sonrası STALE.**

---

## 1. PİYASA SEVİYESİ ÇAPALARI (bizim rotamız DEĞİL)

| Endeks / kaynak | Değer | Birim | Tarih | tier | conf. | status | evidence_id |
|---|---|---|---|---|---|---|---|
| Drewry WCI — kompozit | **4.297** | USD/FEU | 2026-08-06 | T4 | HIGH | FACT | `EV-2026-08-09-330` |
| Drewry WCI — Shanghai→Genoa | 5.506 | USD/FEU | 2026-08-06 | T4 | HIGH | FACT | `EV-2026-08-09-330` |
| Drewry WCI — Shanghai→Rotterdam | 4.653 | USD/FEU | 2026-08-06 | T4 | HIGH | FACT | `EV-2026-08-09-330` |
| Drewry WCI — Shanghai→New York | 7.893 | USD/FEU | 2026-08-06 | T4 | HIGH | FACT | `EV-2026-08-09-330` |
| **Freightos FBX13 — Çin→Akdeniz** *(endeksin varış limanları arasında **Ambarlı** ve **İzmit** var)* | **6.066,80** | USD/FEU | erişim 2026-08-09 | T4 | MEDIUM | FACT | `EV-2026-08-09-331` |
| Freightos haftalık — Asya→Akdeniz | ~6.000 | USD/FEU | 2026-08-06 | T4 | MEDIUM | FACT | `EV-2026-08-09-332` |
| Freightos haftalık — Asya→K.Avrupa | ~5.000 | USD/FEU | 2026-08-06 | T4 | MEDIUM | FACT | `EV-2026-08-09-332` |

**Piyasa yönü (2026-08):** Drewry WCI 3 haftalık düşüşün ardından %1 toparlandı;
Freightos'a göre Asya-Akdeniz Temmuz zirvesinin **%16 altında**, Asya-K.Avrupa
%14 altında. **Yön: yumuşama.** Ancak bu Asya çıkışlıdır; Akdeniz-içi ve
Atlantik rotalarına birebir taşınamaz.

> **Neden bu endeksleri modele koymuyorum:** Şarap Çin'den gelmiyor. FBX13'ün
> varış limanları arasında Ambarlı olması cezbedicidir ama **menşe yanlıştır**.
> Bir Asya→Akdeniz rakamını İspanya→Türkiye yerine koymak, bu projenin
> yasakladığı türden bir uydurmadır.

---

## 2. BİZİM ROTALARIMIZ — NAVLUN

### 2.1 Tablo

| # | Rota | 20DV | 40HC | Neyi kapsıyor | Tarih | tier | conf. | status | evidence_id |
|---|---|---|---|---|---|---|---|---|---|
| R1 | **İspanya** (Valencia/Barcelona/Málaga) → Türkiye (Ambarlı/Mersin/İzmir) | 1.200 – 2.500 EUR | 2.000 – 4.600 EUR | **BELİRSİZ** — kaynak all-in mi base mi yazmıyor | 2026 | T5 | **LOW** | ESTIMATE | `EV-2026-08-09-333` |
| R2 | **İtalya** (Genova/La Spezia/Livorno) → Türkiye | **UNKNOWN** | **UNKNOWN** | — | — | — | — | UNKNOWN | — |
| R3 | **Fransa** (Marseille/Fos) → Türkiye | **UNKNOWN** | **UNKNOWN** | — | — | — | — | UNKNOWN | — |
| R4 | **ABD Doğu** (New York/Norfolk) → İstanbul | 2.550 USD | 4.600 USD | **BELİRSİZ** | 2026 | T5 | **LOW** | ESTIMATE | `EV-2026-08-09-333` |
| R5 | **ABD Batı / California** (Oakland/LA) → İstanbul | **UNKNOWN** | **UNKNOWN** | — | — | — | — | **UNKNOWN** ⚠ | `EV-2026-08-09-329` |
| R6 | **Şili** (San Antonio/Valparaíso) → Türkiye | **UNKNOWN** | **UNKNOWN** | — | — | — | — | UNKNOWN | `EV-2026-08-09-328` |
| R7 | **Güney Afrika** (Cape Town) → Türkiye | **UNKNOWN** | **UNKNOWN** | — | — | — | — | UNKNOWN | — |
| R8 | Türkiye'ye genel band (tüm menşeler) | 1.235 – 7.550 USD | 1.235 – 7.550 USD | **BELİRSİZ** | 2026 | T5 | **LOW** | ESTIMATE | `EV-2026-08-09-333` |

> ⚠ **R5 KRİTİKTİR.** Projenin benchmark ürünü (Gold Country, California) tam
> olarak bu rotadan gelir ve bu rotanın navlunu **UNKNOWN**'dır.
> Bkz. `T-304`.

### 2.2 R1 (İspanya→Türkiye) neden yine de zayıf bir sayıdır

Kaynak (`EV-2026-08-09-333`) bir forwarder pazarlama sayfasıdır (**T5**) ve:
- "1.200 – 4.600 EUR (20ft–40ft)" biçiminde, hangi ucun hangi konteynere ait
  olduğunu **açıkça yazmaz**;
- **all-in mi base mi belirtmez** (BAF/CAF/THC/ISPS dahil mi?);
- aynı sayfadaki transit süreleri T4 kaynaklarla **çelişir** (`C-302`);
- geçerlilik tarihi yoktur.

**Sonuç:** R1 rakamı model içinde **yalnızca duyarlılık bandı** olarak kullanılabilir,
merkezî varsayım olarak kullanılamaz.

---

## 3. SURCHARGE (EK MASRAF) YAPISI

Bir "navlun" rakamı verilirken **neyin dahil olduğu** yazılmazsa o rakam
kullanılamaz. Akdeniz→Türkiye rotasında karşılaşılacak kalemler:

| Kalem | Ne demek | Kim keser | Değer | status |
|---|---|---|---|---|
| **Ocean freight (base)** | Denizaşırı taşıma temel bedeli | armatör/forwarder | UNKNOWN | UNKNOWN |
| **BAF** (Bunker Adjustment Factor) | Yakıt fiyatı düzeltmesi | armatör | UNKNOWN | UNKNOWN |
| **CAF** (Currency Adjustment Factor) | Kur düzeltmesi | armatör | UNKNOWN | UNKNOWN |
| **PSS / PCS** (Peak Season / Port Congestion) | Sezon ve liman yığılma primi | armatör | UNKNOWN — İspanya-Türkiye rotasında uygulandığı teyitli (`EV-...-325`) | UNKNOWN |
| **THC origin** | Yükleme limanı elleçleme | mense terminal | UNKNOWN | UNKNOWN |
| **THC destination / gate-out** | Varış terminal elleçleme | Türk terminal | **113 USD** (20ft ve 40ft, standart) | FACT `EV-...-340` |
| **ISPS** | Güvenlik surcharge | armatör/terminal | UNKNOWN | UNKNOWN |
| **Doc fee / B/L** | Konşimento düzenleme | armatör acentesi | UNKNOWN | UNKNOWN |
| **Ordino (delivery order)** | Yük teslim talimatı | armatör acentesi | UNKNOWN | UNKNOWN |
| **Sigorta** | Kargo sigortası | sigortacı | %0,3 – 0,6 (CIF+%10 üzerinden) | ESTIMATE `EV-...-360` |

> Genel sektör kuralı: sursarjlar base navlunun üstüne **%10–20** ekleyebilir
> (T5, LOW). Bu sayı modele girmez, yalnızca "all-in ile base'i eşitleme"
> hatasının büyüklüğünü göstermek için buradadır.

---

## 4. TRANSİT SÜRELER (PORT-TO-PORT)

| Rota | Süre | Sefer sıklığı | tier | conf. | status | evidence_id |
|---|---|---|---|---|---|---|
| Valencia → **Ambarlı** | **7 – 10 gün** | haftalık/2 haftalık | T4 | MEDIUM | FACT | `EV-2026-08-09-325` |
| Valencia → **Mersin** | **5 – 8 gün** | — | T4 | MEDIUM | FACT | `EV-2026-08-09-325` |
| Valencia → **İzmir** | **6 – 9 gün** | — | T4 | MEDIUM | FACT | `EV-2026-08-09-325` |
| İspanya → Türkiye genel | 5 – 12 takvim günü | — | T4 | MEDIUM | FACT | `EV-2026-08-09-325` |
| Maersk SLR Marmara Sea A: Valencia→Barcelona→Piraeus→Ambarlı | **~10 gün** (3+5+2) | servis tarifesi | T3 | MEDIUM | FACT | `EV-2026-08-09-326` |
| İtalya → Türkiye | **UNKNOWN** (coğrafi olarak İspanya'dan kısa beklenir) | — | — | — | UNKNOWN | — |
| Fransa (Marseille/Fos) → Türkiye | **UNKNOWN** | — | — | — | UNKNOWN | — |
| ABD Doğu (NY) → İstanbul | 18 – 38 gün — **ÇELİŞKİLİ** | — | T5 | LOW | CONFLICT | `EV-2026-08-09-329` ⚠`C-302` |
| ABD Batı (Oakland/LA) → İstanbul | **UNKNOWN** (aktarmalı) | — | — | — | **UNKNOWN** ⚠ | `EV-2026-08-09-329` |
| Şili → Türkiye | **UNKNOWN** | — | — | — | UNKNOWN | `EV-2026-08-09-328` |
| Türkiye ↔ Cape Town | ~26 gün (**ters yön ölçümü**) | 1–2 haftada bir | T4 | LOW | ESTIMATE | `EV-2026-08-09-327` |

### 4.1 Sefer sıklığının stok etkisi

Güney Afrika ve Şili rotalarında sefer sıklığı düşüktür (1–2 haftada bir).
Bir sefer kaçırıldığında lead time doğrudan +7–14 gün artar. Akdeniz rotasında
bu risk düşüktür. **Bu, stok/işletme sermayesi hesabına girer — hesabı
`finans-fizibilite` yapar, süre burada verilmiştir.**

---

## 5. TOPLAM LEAD TIME (PO → SATIŞA HAZIR)

```
T_toplam = T_uretim/hazirlik + T_transit + T_liman/gumruk + T_antrepo/bandrol + T_ic_nakliye
```

| Bileşen | Süre | status | Sahibi |
|---|---|---|---|
| Üretim/hazırlık (PO → yükleme) | **UNKNOWN** | UNKNOWN | `global-sourcing-kasifi` |
| Transit (İspanya→Ambarlı) | **7 – 10 gün** | FACT | bu ajan `EV-...-325` |
| Transit (California→İstanbul) | **UNKNOWN** | UNKNOWN | bu ajan — RFQ gerekli |
| Liman + gümrükleme (antrepo beyannamesi) | **UNKNOWN** | UNKNOWN | bu ajan / `gumruk-vergi-uzmani` |
| Antrepoda bekleme (analiz + uygunluk + bandrol) | **UNKNOWN** | UNKNOWN | `mevzuat-ruhsat-uzmani` → **`T-301`** |
| Bandrolleme operasyonu (şişe/gün kapasite) | **UNKNOWN** | UNKNOWN | bu ajan — teklif gerekli |
| Serbest dolaşıma giriş + iç nakliye | **UNKNOWN** | UNKNOWN | bu ajan |
| **TOPLAM** | **UNKNOWN** | **UNKNOWN** | — |

> **Toplam lead time UNKNOWN'dır ve bu KRİTİKTİR.** İşletme sermayesi, CCC ve
> `peak_cash_requirement` doğrudan bu sayıya bağlıdır. Yalnız transit süresini
> lead time sanmak, modeli sistematik olarak **iyimser** yapar.

---

## 6. LİMAN / TERMİNAL / GÜMRÜK / ANTREPO MASRAF KALEMLERİ

*(Bir kalemin ne olduğu + kimin kestiği + varsa değer)*

### 6.1 Terminal (varış)

| Kalem | Ne | Kim keser | 20ft | 40ft | evidence |
|---|---|---|---|---|---|
| Kapı çıkış / terminal elleçleme (destination THC) | Gemiden tahliye → kapıdan çıkış | terminal | 113 USD | 113 USD | `EV-...-340` |
| Aynı, reefer | | terminal | 119 USD | 119 USD | `EV-...-340` |
| **Ardiye** (terminal storage) — kademeli | Konteynerin sahada beklemesi | terminal | 33–52 USD/gün | 58–90 USD/gün | `EV-...-340`,`EV-...-341` |
| Ardiye, **reefer** | | terminal | **135–165 USD/gün** | **165–205 USD/gün** | `EV-...-341` |
| İç boşaltım (devanning) | Konteynerin terminalde elden boşaltılması | terminal | 275 USD + KDV | 350 USD + KDV | `EV-...-341` |
| Tam muayene | Gümrük fiziki muayenesi için elleçleme | terminal | 2.322 TL + KDV | 3.249 TL + KDV | `EV-...-341` |
| Kısmi muayene | | terminal | 1.973 TL + KDV | 2.787 TL + KDV | `EV-...-341` |
| **Ardiye free time (gün)** | | terminal | **UNKNOWN** | **UNKNOWN** | — |
| Ordino | Yük teslim talimatı | armatör acentesi | **UNKNOWN** | **UNKNOWN** | — |

> Terminal tarifeleri Beldeport ve Asyaport'tan alınmıştır. **Ambarlı
> terminallerinin (Marport / Kumport / Mardaş) kendi tarifeleri alınamamıştır**
> — seviye göstergesi olarak kullanılmıştır, tam doğru değildir.

### 6.2 Demurrage & Detention

`EV-2026-08-09-343` (Maersk Türkiye **ithalat**, yürürlük 2025-09-15, **T3**):

| Gün aralığı | 20ft | 40ft |
|---|---|---|
| 1 – 7 (free time) | **0** | **0** |
| 8 – 12 | 60 USD/gün | 75 USD/gün |
| 13 – 17 | 80 USD/gün | 115 USD/gün |
| 18+ | 100 USD/gün | 150 USD/gün |

- **Free time: 7 takvim günü** (resmî tatiller dahil, USD, konteyner başına).
- Türkiye ithalatında **terminal ardiyesi (storage) armatör değil TERMİNAL
  tarafından ayrıca faturalanır** → gecikmede **iki sayaç birden** çalışır.
- Diğer hatların tarifesi farklı olabilir; sektör pratiği 7–14 gün.

### 6.3 Gümrük müşavirliği (2026 asgari tarife, `EV-2026-08-09-342`, **T3**)

| Kod | Hizmet | Ücret |
|---|---|---|
| **ANT-1** | Antrepo beyannamesi, CIF 0–15.000 USD | **1.350 TL** (+ 15.001–225.000 USD için aşan kısmın **%0,1**'i) |
| **ANT-3** | 2. ve sonraki her konteyner (antrepo) | 1.000 TL |
| **İTH-2** | **Deniz yoluyla gelip limanda yapılan ithalat** | **4.670 TL** |
| **İTH-13** | CIF kademesi | 0–15.000 USD tarife tutarı; 15.001–225.000 USD için aşan kısmın **%0,3**'ü; 225.001–2.000.000 USD için aşan kısmın %0,1'i |
| **İTH-14** | 2. ve sonraki her konteyner | 1.350 TL |
| **İTH-15** | 11. ve sonraki her kalem | 70 TL |
| **ÖZ-4** | Laboratuvar tahlili / ekspertiz / TSE-DTS işlemleri | 940 TL / işlem |

> **Alkollü içkide iki beyanname olur** (antrepo + serbest dolaşıma giriş) →
> `ANT-1 + İTH-2` birlikte hesaplanmalıdır. Bu, tek beyanname varsayan modelin
> gözden kaçırdığı bir kalemdir.

### 6.4 Antrepo ve iç lojistik

| Kalem | Değer | status | evidence |
|---|---|---|---|
| Antrepo paletli depolama | ~0,35 EUR/palet/gün | ESTIMATE (T5, LOW) | `EV-...-350` |
| Antrepo giriş/çıkış elleçleme | **UNKNOWN** | UNKNOWN | — |
| Alkole uygun antrepo gerekliliği | **UNKNOWN** | UNKNOWN | → `mevzuat-ruhsat-uzmani` |
| Limandan depoya konteyner çekme | **UNKNOWN** (band 3.000–30.000 TL çok geniş) | UNKNOWN | `EV-...-351` |
| Depodan kanala dağıtım (şişe başı) | **UNKNOWN** | UNKNOWN | — |
| Bandrolleme birim maliyeti (şişe başı) | **UNKNOWN** | UNKNOWN | — |
| Bandrolleme kapasitesi (şişe/gün) | **UNKNOWN** | UNKNOWN | — |
| Bandrolleme yeri | Yabancı üretim tesisi VEYA İstanbul/İzmir/Mersin antrepoları | **UNKNOWN** (T5) | `EV-...-380` → `T-301` |

---

## 7. GECİKME MALİYETİ — DEMURRAGE SENARYOSU

Alkollü içki ithalatında ruhsat / uygunluk / analiz / bandrol beklemesi gerçek
bir risktir. **Konteyner limanda beklerse:**

```
20DV, 21 GÜN LİMANDA BEKLEME
  D&D (Maersk, EV-...-343):
    gün 1–7   : 0
    gün 8–12  : 5 × 60  =   300 USD
    gün 13–17 : 5 × 80  =   400 USD
    gün 18–21 : 4 × 100 =   400 USD
                          ─────────
                            1.100 USD
  Ardiye (terminal, EV-...-340; free time UNKNOWN → 1. günden sayıldı, muhafazakâr):
    gün 1–5   : 5 × 37  =   185 USD
    gün 6–10  : 5 × 43  =   215 USD
    gün 11–21 : 11 × 52 =   572 USD
                          ─────────
                              972 USD
  TOPLAM ≈ 2.072 USD / 20DV  →  13.200 şişede  ≈ 0,157 USD/şişe

20DV, 60 GÜN LİMANDA BEKLEME
  D&D    ≈ 300 + 400 + (43 × 100) = 5.000 USD
  Ardiye ≈ 185 + 215 + (50 × 52)  = 3.000 USD
  TOPLAM ≈ 8.000 USD / 20DV  →  ≈ 0,61 USD/şişe
```
`EV-2026-08-09-344`

### 7.1 Karşı tedbir — ve bu raporun en pratik bulgusu

```
ALTERNATİF: konteyneri free time içinde ANTREPOYA çek, boşalt, boş konteyneri iade et.
  → detention DURUR, terminal ardiyesi DURUR
  → yerine antrepo depolama başlar: 10 palet × 60 gün × 0,35 EUR = 210 EUR
  → + antrepo beyannamesi 1.350 TL + elleçleme (UNKNOWN)

LİMANDA 60 GÜN  ≈ 8.000 USD
ANTREPODA 60 GÜN ≈   210 EUR + beyanname + elleçleme

FARK: yaklaşık 30–35 KAT
```

> **Operasyonel kural (ESTIMATE):** Bandrol/analiz beklemesi **limanda değil,
> antrepoda** yapılmalıdır. Bu zaten mevzuatın da doğal akışıdır (bandrol serbest
> dolaşıma girmeden önce uygulanır) ama **modelde bunun aksi varsayılırsa
> demurrage kalemi 30 kat şişer.**
>
> Bu bir tahmindir; antrepo elleçleme ve minimum süre ücretleri UNKNOWN olduğu
> için fark daraltabilir — ama büyüklük mertebesi değişmez.

---

## 8. SICAKLIK KONTROLLÜ TAŞIMA — GEREKLİ Mİ?

| | Kuru konteyner (dry) | Kuru + izolasyon liner | Reefer |
|---|---|---|---|
| Sıcaklık kontrolü | yok | pasif (artışı sınırlar) | aktif |
| Performans | — | iç sıcaklık artışı ort. 8–11 °C ile sınırlı (`EV-...-371`) | set point |
| Okyanus navlun primi | 0 | **UNKNOWN** | **%20–50** (T5, LOW) `EV-...-372` |
| Varış terminal gate-out | 113 USD | 113 USD | 119 USD `EV-...-340` |
| **Varış terminal ardiye** | 33 USD/gün (20ft) | 33 USD/gün | **135 USD/gün (20ft)** `EV-...-341` |
| Kapasite kaybı | 0 | liner kalınlığı kadar (UNKNOWN) | reefer iç hacmi daha küçük + palet sayısı 1 azalır (`EV-...-308`) |

**Şarap için sıcaklık gerçekleri (`EV-2026-08-09-370`, T5, LOW):**
- 20 °C üzerinde oksidasyon hızlanır, aroma kaybolur.
- Isı sıvıyı genleştirir → mantar itilir → **leakage (kaçırma)**.
- Kuru konteyner kullanan sevkiyatçılar tipik olarak **yaz sevkiyatından kaçınır**.

**Rota bazlı risk değerlendirmesi (ESTIMATE):**

| Rota | Transit | Yaz riski | Öneri (ESTIMATE) |
|---|---|---|---|
| İspanya/İtalya/Fransa → Türkiye | 5–10 gün | **düşük–orta** | Kuru konteyner yeterli olabilir; Temmuz–Ağustos yüklemesinde liner düşünülmeli |
| ABD Doğu → Türkiye | ~20–38 gün | **orta–yüksek** | Liner; yaz sevkiyatından kaçın |
| California → Türkiye | UNKNOWN (uzun, aktarmalı, Panama/Süveyş) | **yüksek** | Liner veya reefer; sevkiyat mevsimi planlanmalı |
| Şili / G.Afrika → Türkiye | 26–45 gün | **yüksek** — ayrıca ekvator geçişi | Liner/reefer değerlendirilmeli |

**Kritik uyarı:** Reefer seçilirse ve gümrükte/bandrolde beklenirse **terminal
ardiyesi kuru konteynerin ~4 katıdır** (135 vs 33 USD/gün). Yani reefer'ın
maliyeti navlun primiyle bitmez; **gecikme riskiyle çarpılır.** Alkollü içkide
gecikme olasılığı yüksek olduğu için reefer, göründüğünden pahalıdır.

**Beklenen fire/bozulma oranı: UNKNOWN.** Bu sayı olmadan liner/reefer kararı
finansal olarak verilemez → `T-304`.

---

## 9. SİGORTA

| Parametre | Değer | status | evidence |
|---|---|---|---|
| Prim oranı (genel) | %0,1 – 1,5 | ESTIMATE | `EV-...-360` |
| Prim oranı (tipik) | **%0,3 – 0,6** | ESTIMATE | `EV-...-360` |
| Şarap (kırılgan) | bandın üst ucu beklenir | ASSUMPTION | — |
| Teminat değeri esası | **CIF + %10** | ESTIMATE | `EV-...-360` |
| Gerekli klozlar | **ICC (A)** "all risks" + kırılma + termal şok / wine spoilage | ESTIMATE | `EV-...-360`, `EV-...-361` |
| Taşıyıcının sınırlı sorumluluğu | **3 USD/kg** → 1,26 kg'lık şişe için ~3,8 USD | FACT | `EV-2026-08-09-361` |
| Türk sigortacıdan gerçek kotasyon | **UNKNOWN** | UNKNOWN | → `T-304` |
| Muafiyet (deductible) | **UNKNOWN** | UNKNOWN | — |

> ⚠ **ICC (C) kırılmayı kapsamaz.** CIF Incoterms 2020'de satıcının asgari
> yükümlülüğü ICC (C)'dir. Yani CIF terimiyle alım yapıp "sigorta var" demek,
> şarapta **fiilen korumasız kalmak** anlamına gelebilir.
>
> ⚠ **Çift sayım uyarısı:** CIF terimiyle alım yapılırsa navlun ve sigorta
> tedarikçi fiyatının içindedir → ayrıca lojistik gideri olarak yazılamaz.
> (`80-model/inputs/lojistik.yaml` başındaki kural.)
>
> ℹ **Gümrük kıymeti bağlantısı:** Sigorta ve navlun gümrük kıymetine girer.
> Bu benim alanım değildir — hesabı `gumruk-vergi-uzmani` yapar. Bkz. `T-303`.

---

## 10. TAZELİK

| evidence_id | ttl | STALE tarihi |
|---|---|---|
| `EV-2026-08-09-330` (Drewry WCI) | 14d | **2026-08-23** |
| `EV-2026-08-09-331` (FBX13) | 14d | **2026-08-23** |
| `EV-2026-08-09-332` (Freightos haftalık) | 14d | **2026-08-23** |
| `EV-2026-08-09-333` (rota navlun bandı) | 14d | **2026-08-23** |
| `EV-2026-08-09-323` (LCL/FCL kırılma) | 14d | **2026-08-23** |
| `EV-2026-08-09-340`,`341`,`343`,`344`,`350`,`351`,`372` | 90d | **2026-11-07** |
| Diğer (fiziksel/mevzuat) | 180d – 1y | 2027-02-05 / 2027-08-09 |
