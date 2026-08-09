# T0 → İLK KONTEYNER TAKVİMİ

> Sahibi: `mevzuat-ruhsat-uzmani` · TUR 1 · 2026-08-09
> **T0 = sıfırdan başlayan yatırımcı.** Şirket yok, belge yok, depo yok, SKU yok.
>
> **KURAL: Süre tahmini FACT değildir.** Aşağıda her adımın süresi
> `FACT` / `ESTIMATE` / `ASSUMPTION` / `UNKNOWN` olarak etiketlenmiştir.
> Yalnızca 4 adımın süresi mevzuatla sabittir; geri kalanı tahmindir.
>
> **Kapsam:** Bu takvim yalnızca **mevzuat/ruhsat** kaynaklı süreleri içerir.
> **Tedarikçi üretimi, şişeleme, navlun ve gümrük işlem süresi bu ajanın alanı
> DEĞİLDİR** ve toplam süreye ayrıca eklenmelidir
> (→ `global-sourcing-kasifi`, `navlun-lojistik-uzmani`).

---

## 1. MEVZUATLA SABİT SÜRELER (`FACT`)

| Süre | Ne | Kaynak | evidence_id |
|------|-----|--------|-------------|
| **15 iş günü** | TADAB ürün onayı karar süresi | TADAB duyurusu 11/4/2025 | `EV-2026-08-09-216` |
| +15 gün | Eksik belge tamamlama süresi (sonra yeniden 15 iş günü) | aynı | `EV-2026-08-09-216` |
| **15 gün** | Bandrol teslim süresi (onay + bedelin Darphane'ye yatırılmasından itibaren) | ÜİS Tebliği 3.5.1 | `EV-2026-08-09-214` |
| **15 gün** | Alkollü içki bildirimi belgelerinin dilekçe giriş kaydından sonra teslim süresi | Ticaret Yön. m.6 | `EV-2026-08-09-202` |
| **30 gün** | Dağıtım yetki belgesi yenileme başvurusu (süre bitiminden önce) | Ticaret Yön. m.12 | `EV-2026-08-09-203` |
| **2 yıl** | Dağıtım yetki belgesi geçerlilik süresi | Ticaret Yön. m.12 | `EV-2026-08-09-203` |

**Mevzuatta süresi TANIMSIZ olan en kritik adım:**
**Dağıtım yetki belgesi başvuru → belge** süresi. Ticaret Yön. m.12 yalnızca
"yerinde ve/veya kayıtlar üzerinde incelenerek" der; **süre yoktur**.
→ `EV-2026-08-09-228` (`UNKNOWN`), ticket `T-202`.

---

## 2. ADIM ADIM TAKVİM

Legend: **[KY]** = kritik yol üzerinde · `∥` = paralel yürütülebilir

| # | Adım | Ön koşul | Süre (gün) | Statü | Kaynak |
|---|------|----------|-----------|-------|--------|
| A1 **[KY]** | Şirket kuruluşu (ticaret sicili, ana sözleşmede alkollü içki ithalat/toptan ticaret faaliyet konusu) | — | 5–15 | `ASSUMPTION` | ticaret sicili pratiği |
| A2 `∥` | Adli sicil + vergi/prim borcu yoktur belgeleri | A1 | 3–10 | `ASSUMPTION` | `EV-...-205` (belge zorunlu: FACT) |
| A3 **[KY]** | Depo/3PL sözleşmesi + deponun TADAB şartlarına uygun hâle getirilmesi (tefrik, güvenlik, marka bazında sayım düzeni) | A1 | 30–90 | `ASSUMPTION` | `EV-...-204` (şart: FACT) |
| A4 `∥` | Antrepo/bandrol uygulama iş ortağı ile anlaşma | A1 | 15–45 | `ASSUMPTION` | `EV-...-212` (antrepo zorunluluğu: FACT) → lojistik |
| A5 `∥` **[KY]** | SKU seçimi, tedarikçi teyidi, marka çakışma taraması (TÜRKPATENT 33. sınıf) | A1 | 20–45 | `ASSUMPTION` | `EV-...-218` (çakışma engeli: FACT) |
| A6 **[KY]** | Türkçe etiket tasarımı + uyarı mesajı yerleşimi (≥18 cm²) + teknik spesifikasyon raporu + Türkçe üretim prosesi dosyası | A5 | 15–40 | `ASSUMPTION` | `EV-...-219`, `-220` (içerik: FACT) |
| A7 **[KY]** | **Alkollü içki bildirimi** dosyasının TADAB'a sunulması | A1,A2,A6 | dilekçeden sonra **15 gün** içinde belge teslimi | `FACT` | `EV-...-202` |
| A8 **[KY]** | **Dağıtım yetki belgesi** başvurusu → belge (bedelin 1/4'ü başvuruda, bakiye belge verilirken) | A3,A7 | **UNKNOWN** (planlama için 30–90) | `UNKNOWN` / `ASSUMPTION` | `EV-...-203`, `-228` · `T-202` |
| A9 `∥` | **Toptan satış belgesi** başvurusu (chain retail'e doğrudan satış için) | A3,A8 | 15–30 | `ASSUMPTION` | `EV-...-210`, `-211` |
| A10 **[KY]** | **GGBS** firma/üretici/ihracatçı tanımlama + Bitkisel Gıda ve Yemin **Ürün Bildirim Formu** onayı | A6 | 10–30 | `ASSUMPTION` | `EV-...-215` (adım: FACT) |
| A11 **[KY]** | **TADAB Ürün Onayı** (Portal, SKU bazında) | A8,A10 | **15 iş günü** (≈21 takvim günü); eksik varsa +15 gün +15 iş günü | `FACT` | `EV-...-216` |
| A12 | Sipariş → üretim → menşede etiketleme (seçilirse) → yükleme | A11 | **KAPSAM DIŞI** | — | → `global-sourcing-kasifi` |
| A13 | Deniz/kara navlun + varış | A12 | **KAPSAM DIŞI** | — | → `navlun-lojistik-uzmani` |
| A14 **[KY]** | **Bandrol talebi** → TADAB uygunluk onayı | A11 + vergi borcu yok belgesi | **UNKNOWN** (planlama için 5–15) | `UNKNOWN` / `ASSUMPTION` | `EV-...-214` |
| A15 **[KY]** | Bandrol bedelinin Darphane'ye yatırılması → **teslim 15 gün** | A14 | **15** | `FACT` | `EV-...-214` |
| A16 **[KY]** | Antrepoda **bandrol + Türkçe etiket uygulaması** (şişe başına) | A13,A15 | 5–15 | `ASSUMPTION` | `EV-...-212` (yer: FACT) → `T-204` |
| A17 | **GGBS Sevkiyat Bildirim Formu** + resmî kontrol (kontrol tarihi talep tarihinden en çok 3 gün içinde belirlenir) | A13 | 3–10 | `ASSUMPTION` | `EV-...-230` (T3) |
| A18 | Gümrük beyannamesi, vergi ödemesi, serbest dolaşıma giriş | A16,A17 | **KAPSAM DIŞI** | — | → `gumruk-vergi-uzmani` |
| A19 | Bandrollü/etiketli ürün fotoğraflarının portala yüklenmesi → **satış bildirimi** | A16 | 1–5 | `ASSUMPTION` | `EV-...-215` (zorunluluk: FACT) |

---

## 3. KRİTİK YOL (CRITICAL PATH)

```
A1 şirket
  └─> A3 depo/3PL ──────────────────────┐
  └─> A5 SKU/marka ─> A6 etiket+dosya ─> A7 bildirim ─┐
                                                      ├─> A8 DAĞITIM YETKİ BELGESİ  ◀── EN BÜYÜK BELİRSİZLİK
                                                      │      (süre UNKNOWN)
                              A10 GGBS ürün bildirimi ─┘
                                                      └─> A11 TADAB ÜRÜN ONAYI (15 iş günü, FACT)
                                                              └─> [A12 üretim + A13 navlun — KAPSAM DIŞI]
                                                              └─> A14 bandrol onayı (UNKNOWN)
                                                                    └─> A15 bandrol teslim (15 gün, FACT)
                                                                          └─> A16 antrepoda bandrol+etiket
                                                                                └─> A18 gümrük ─> SERBEST DOLAŞIM
```

### Hangi adım hangisini bloke eder

| Bloke eden | Bloke edilen | Hüküm |
|------------|--------------|-------|
| Depo (A3) | Dağıtım yetki belgesi (A8) | Ticaret Yön. m.10/b — depo/nakil aracı faaliyet dosyası zorunlu |
| Dağıtım yetki belgesi (A8) | **İthalatın tamamı** | m.12: *"Dağıtım yetki belgesi olmadan ... ithalat yapılamaz"* |
| Alkollü içki bildirimi (A7) | Dağıtım yetki belgesi (A8) | m.10/a — ithalatçılar için bildirim dosyası ön koşul |
| GGBS ürün bildirimi (A10) | TADAB ürün onayı (A11) | TADAB duyurusu: GGBS onayı **sonra** portal başvurusu |
| TADAB ürün onayı (A11) | **Bandrol talebi (A14)** | *"Onay alınmayan ürünler için bandrol başvurusunda bulunulamaz."* |
| Bandrol (A15/A16) | Serbest dolaşım / piyasaya arz | ÜİS dışında ithalat yapılamaz; bandrolsüz ürün arz edilemez |
| Vergi borcu | Bandrol talebi | ÜİS Tebliği 3.3.1(a) |
| Marka çakışması | Ürün onayı | TÜRKPATENT ≤34 Nice sınıfı tescili varsa onay verilmez |
| Toptan satış belgesi (A9) | **Chain retail'e doğrudan satış** | Satış Yön. m.7/1(a) — ithalatı bloke etmez, **kanalı** bloke eder |

> **Sıralama paradoksu (çözülmedi):** m.10/a dağıtım yetki belgesi için "alkollü
> içki bildirimi"ni ön koşul sayarken, m.12 "dağıtım yetki belgesi olmadan ithalat
> yapılamaz" der. Bildirim ile fiili ithalatın ayrıştığı varsayılmıştır
> (bildirim dosyası önce, fiili ithalat belge sonrası). **Doğrulanmadı** →
> çelişki `C-202`, ticket `T-202`.

---

## 4. TOPLAM SÜRE (`ESTIMATE` — `EV-2026-08-09-233`)

**Yalnızca mevzuat kaynaklı kritik yol** (üretim + navlun + gümrük hariç):

| Senaryo | Hesap | Toplam |
|---------|-------|--------|
| **İyimser** | A1(5) + A3(30) + A8(30) + A11(21) + A14(5) + A15(15) + A16(5) + A19(1) | **≈ 112 gün** |
| **Baz** | A1(10) + A3(60) + A8(60) + A11(21) + A14(10) + A15(15) + A16(10) + A19(3) | **≈ 189 gün** |
| **Kötümser** | A1(15) + A3(90) + A8(90) + A11(36) + A14(15) + A15(15) + A16(15) + A19(5) | **≈ 281 gün** |

**Model için önerilen aralık: 120 – 270 gün (≈ 4 – 9 ay).**
A5/A6/A10 kritik yola paralel yürütülebildiği varsayılmıştır; yürütülemezse
üst sınır **+40 güne kadar** artar.

> **Bu sayı FACT DEĞİLDİR.** İçinde **iki UNKNOWN** vardır (A8 ve A14) ve bunlar
> toplam sürenin **%30–50'sini** oluşturur. `A8` gerçekte 6 ayı aşarsa
> `IMPORT PILOT` kararının zamanlaması bozulur.

**Model hedef tarihi (`00-charter/kapsam.md` için):**
T0 = 2026-08-09 kabul edilirse, ilk konteynerin **izinler tarafından serbest
bırakıldığı** tarih **2026-12 → 2027-05** bandındadır. Üretim + navlun bu bandın
üzerine eklenir. **Vergi/mevzuat verileri 2027 yılına ait olabilir** — 2026
tebliğ bedelleri 1/1/2027'de yeniden belirlenecektir (Ticaret Yön. m.14: bedeller
her yıl yeniden belirlenir). Bu bir **regülasyon takvimi riskidir**.

---

## 5. TAKVİMİ KISALTAN / UZATAN FAKTÖRLER

**Kısaltan**
- Depo yerine **akde bağlanmış 3PL dağıtım ağı** kullanmak (m.10/b) → A3 kısalır
- SKU sayısını 1–2'de tutmak → A11 tekrarı azalır
- Vintage değişikliği yeni onay gerektirmediği için **2. yıl A11 tekrarlanmaz**
  (`EV-...-217`)
- Aynı dosya bilgisine sahip sonraki bildirimlerde bazı belgeler tekrar
  aranmaz (m.6 son fıkra)

**Uzatan**
- Eksik dosya → A11'e **+15 gün + 15 iş günü**
- Marka çakışması → SKU/marka değişimi, A5–A6–A11 baştan
- Vergi/prim borcu → bandrol talebi reddi (A14 bloke)
- Yeni kategori/alt kategori veya faaliyet hacmi artışı → belge güncelleme + ek bedel
- Yeni SKU eklemek → her SKU için A10+A11 tekrarı (15 iş günü/SKU)

---

## 6. AÇIK SORULAR (takvimi doğrudan etkileyen)

| Soru | Ticket | Etki |
|------|--------|------|
| Dağıtım yetki belgesi gerçek işlem süresi nedir? | `T-202` | Kritik yolun %25–35'i |
| Bandrol için TADAB uygunluk onayı ne kadar sürer? | `T-204` | 5–15 gün varsayımı |
| Antrepoda bandrol+etiket uygulaması gün/maliyet | `T-204` | demurrage riski |
| 4250 m.1/3 eşiği pilot ölçeği bloke eder mi? | `T-201` | G0 önerisini değiştirir |
| İthalatta zorunlu analiz var mı, parti başı mı? | `T-206` | +süre +maliyet |
