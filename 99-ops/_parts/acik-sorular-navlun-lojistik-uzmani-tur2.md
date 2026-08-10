# AÇIK SORULAR — navlun-lojistik-uzmani, TUR 2

```yaml
ajan:  navlun-lojistik-uzmani
tur:   TUR 2
tarih: 2026-08-10
not:   "Bu dosya 99-ops/acik-sorular.md'ye BASKAN tarafindan islenir. Ana dosyaya dokunmadim."
```

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 1. TUR 1'DEN KAPANANLAR *(şeffaflık için)*

| TUR 1 UNKNOWN # | Konu | **TUR 2 durumu** | evidence_id |
|---|---|---|---|
| 2 | California → İstanbul transit + navlun | ✅ **KAPANDI** (LCL): 20 gün, 0,505–0,574 USD/şişe | `EV-...-308`, `-309` |
| 7 | Terminal ardiye free time gün sayısı | ⚠ **KISMEN** — SafiPort 0 gün, ama `C-312` çelişkisi | `EV-...-317` |
| 8 | Ambarlı terminallerinin tarifesi | ⚠ **KISMEN** — Kumport ardiye bulundu ama `confidence: LOW` | `EV-...-318` |
| 12 | Origin THC, BAF/CAF, doc fee, ordino | ✅ **KAPANDI**: THO 287 EUR, B/L 62 EUR, ordino 2.000–5.000 TL, BAF %15–25 | `EV-...-313`, `-314`, `-325`, `-324` |
| 13 | Limandan depoya çekme ücreti | ✅ **DARALDI**: 10.000–15.000 TL (İstanbul içi, 20') | `EV-...-326` |
| 14 | Antrepo minimum süre | ✅ **KAPANDI**: 7 gün | `EV-...-327` |
| 17 | İtalya / Fransa → Türkiye transit | ⚠ **YARIM**: Fransa 12–15 gün ✅ / **İtalya UNKNOWN** ❌ | `EV-...-305`, `-304` |
| 18 | Şili → Türkiye rota yapısı | ✅ **KAPANDI**: 43–49 gün, Barcelona/Hamburg aktarmalı | `EV-...-306` |

**Ayrıca TUR 1'de sorulmamış ama TUR 2'de kapanan:**
40HC/20DV navlun oranı (**1,37–1,48**, `EV-...-328`) — TUR 1'in tek noktalı
1,54 eşiğini bir **banda** (1,39–1,82) çevirdi ve karşılaştırmayı mümkün kıldı.

---

## 2. HÂLÂ AÇIK — ÖNCELİK SIRASIYLA

| # | Soru | Neden bulunamadı | Kritik mi | Nasıl kapanır | Ticket |
|---|---|---|---|---|---|
| **U-1** | **Rota bazlı FCL navlunu (all-in kalem listesiyle)** | 14 Türkiye varışlı lane'in hiçbirinde kamuya açık FCL kotasyonu yok (`EV-...-312`); dolaylı çapalar 4–5 kat çelişiyor (`C-311`) | **CRITICAL** | 3 forwarder'dan yazılı RFQ | `T-304` |
| **U-2** | **İtalya → Türkiye navlunu (LCL ve FCL)** | Dört İtalyan limanında "0 offerings"; bulunan tek veri ters yön + 2025 | **HIGH** | Forwarder / armatör servis tarifesi | `T-312` |
| **U-3** | **İspanya dışı menşelerin origin local charge'ları** | Yalnızca Hapag-Lloyd İspanya tarifesi tarandı | **HIGH** | Menşe başına taşıyıcı local tarifesi | `T-312` |
| **U-4** | **Beklenen cam kırılma / fire oranı (%)** | Sektör hasar istatistiği kamuya açık değil | **HIGH** | Sigortacı + forwarder | `T-314` |
| **U-5** | **Bandrolleme birim maliyeti + kapasite (şişe/gün)** | Antrepo hizmet teklifi gerekiyor | **HIGH** | Antrepo işletmecisi teklifi | `T-314` |
| **U-6** | **Antrepo giriş/çıkış elleçleme (hammaliye)** | Antrepo siteleri fiyat yayınlamıyor (403) | **HIGH** | Aynı teklif | `T-314` |
| **U-7** | **Çekici + şasi darası (kg)** | Türk nakliyeci verisi kamuya açık değil; TUR 2'de de aranmadı/bulunamadı | **HIGH** | Nakliyeciden ruhsat bilgisi | `T-304` |
| **U-8** | **Terminal ardiye free time: 0 mı 5 mi** | İki T4 kaynak çelişiyor | MEDIUM | Terminal tarife PDF'i / yazılı soru | `T-313` / `C-312` |
| **U-9** | **THD ↔ terminal kapı-çıkış çift sayımı** | Taşıyıcı ve terminal ayrı tarife yayınlıyor | MEDIUM | Gerçek fatura örneği | `T-313` / `C-313` |
| **U-10** | **Kumport/Marport/Mardaş tarifelerinin doğrulanması** | PDF'lere doğrudan erişilemedi | MEDIUM | Terminal/acente | `T-313` |
| **U-11** | **Thermal liner birim maliyeti** | Hiçbir kaynakta fiyat yok (TUR 1'de de yoktu) | MEDIUM | Forwarder | `T-304` |
| **U-12** | **Türk sigortacıdan gerçek kotasyon + muafiyet** | Kotasyon gerekli | MEDIUM | Sigorta brokerı | `T-304` |
| **U-13** | **LCL konsolidasyon beklemesi (gün)** | Veri yok; lead time'a doğrudan giriyor | MEDIUM | Forwarder | `T-304` |
| **U-14** | **LCL per-CBM fiyatının 5 CBM'den 12 CBM'e doğrusal ölçeklenip ölçeklenmediği** | Flexport yalnızca 5 CBM için kotasyon veriyor | MEDIUM | Forwarder'dan 12 CBM kotasyonu | `T-304` |
| **U-15** | **Portekiz → İstanbul gerçek transit** | Kaynak "4 gün" diyor ama routing Barcelona aktarmalı → iç tutarsız | MEDIUM | Armatör servis tarifesi | `T-312` |
| **U-16** | **Şarap "Food Quality Container" (115 EUR) gerektirir mi** | Taşıyıcı tarifesinde kalem var, zorunluluğu belirsiz | LOW | Forwarder / tedarikçi | `T-312` |
| **U-17** | **Veteriner/fitosaniter kontrol (126 USD/BL) şarapta uygulanır mı** | Mevzuat alanı | LOW | `mevzuat-ruhsat-uzmani` (İP-2312) | — |
| **U-18** | **Depolama (serbest dolaşım sonrası) m²/palet maliyeti** | Teklif gerekiyor | MEDIUM | Depo işletmecisi | `T-314` |
| **U-19** | **Depodan kanala dağıtım (şişe başı)** | Kanal modeli belirsiz | MEDIUM | `kanal-marj-uzmani` ile birlikte | — |
| **U-20** | **FX kuru (USD/TRY, EUR/TRY) ve kur tarihi** | `makro.yaml` boş; benim alanım değil | **HIGH** | `finans-fizibilite` | `T-311` |
| **U-21** | **Ruhsat/bandrol bekleme süresi (gün)** | Mevzuat alanı | **CRITICAL** | `mevzuat-ruhsat-uzmani` | `T-301` |
| **U-22** | **Toplam lead time** | U-13 + U-21 + gümrükleme + üretim süresinden türetilir | **CRITICAL** | `T-301` + `T-304` + sourcing | — |
| **U-23** | Tedarikçinin gerçek koli/palet spec'i | Tedarikçi seçilmedi | HIGH | RFQ spec sheet | `T-302` |
| **U-24** | Paletsiz yüklemede yeniden paletleme maliyeti | Veri yok (TUR 1'de de yoktu) | MEDIUM | Antrepo teklifi | `T-314` |
| **U-25** | Diğer armatörlerin (MSC/CMA CGM/Arkas) D&D free time'ı | Sayfalar erişilemedi | MEDIUM | Armatör local info | `T-313` |

---

## 3. BU TURDA DENENİP BAŞARISIZ OLAN YOLLAR *(tekrar denenmesin diye)*

| # | Denenen | Sonuç |
|---|---|---|
| 1 | Flexport Rate Explorer — **FCL**, 14 farklı Türkiye lane'i | Hepsinde "0 offerings" |
| 2 | Flexport — İtalya (ITGOA, ITSPE, ITLIV, ITNAP) → İstanbul | Hepsinde "0 offerings", LCL dahil |
| 3 | Flexport — Valencia → **Mersin** | "0 offerings" (yalnızca İstanbul lane'leri kotasyonlanıyor) |
| 4 | Freightos route sayfaları | 302 redirect → `ship.freightos.com` (giriş gerekli) |
| 5 | SeaRates `/routes/` | 403 |
| 6 | Globy freight calculator (Türkiye ve Valencia→İstanbul) | 403 |
| 7 | Hapag-Lloyd Türkiye import charges **web formu** | 403 — **ama PDF tarifesi bulundu ve çalıştı** ✅ |
| 8 | Kumport tarife sayfası | Yalnızca başlıklar; PDF'lere erişilemedi |
| 9 | FixAntrepo 2026 fiyat sayfası | 403 — değerler yalnızca arama özetinden |
| 10 | Erciyes Lojistik 2026 konteyner fiyatları | 403 |
| 11 | Suaid Global 2026 navlun tabloları | Akdeniz / Türkiye rotaları **yok** |
| 12 | MoverDB konteyner fiyat tablosu | Veri **2023 sonu**, Türkiye satırı yok |
| 13 | Nakliyerehberim rota fiyatları (İspanya, Şili) | Yalnızca **Türkiye çıkışlı** (ihracat) satırlar |

> **Kalıp:** Türkiye **ithalat** yönü için kamuya açık FCL fiyatı sistematik
> olarak yayınlanmıyor. Türkiye **ihracat** yönü için yayınlanıyor. Bu bir
> arama başarısızlığı değil, **piyasa yapısı**dır: Türk forwarder'ları ihracat
> odaklı fiyat yayınlıyor; ithalat fiyatı yabancı taraftan geliyor ve
> kotasyona bağlı.

---

## 4. AÇIK SORULARIN GATE ETKİSİ

| Gate | Sahibi | Bu turdan sonra |
|---|---|---|
| **G2-L** — L1→L2→L3 geçişi kanıtla kurulabiliyor mu? | `navlun-lojistik-uzmani` | **BLOCKED — değişmedi.** Açan tek koşul (`T-304`: 3 forwarder kotasyonu) karşılanmadı. **Ama kapsamı daraldı:** L2→L3 geçişinin masraf kalemleri artık büyük ölçüde biliniyor; kilitli olan yalnızca **L1→L2 (ocean freight)**. |

**G2-L'nin bugünkü tam durumu:**

```
L1 (FOB)  →  L2 (CIF)   : ocean freight UNKNOWN (band 4 kat)  ❌  ← TEK KİLİT
                           origin locals BİLİNİYOR (İspanya)   ✅
                           sigorta ESTIMATE (%0,3–0,6)         ⚠
L2 (CIF)  →  L3 (pre-tax landed) : THD BİLİNİYOR              ✅
                                   ardiye BİLİNİYOR             ✅
                                   ordino BİLİNİYOR             ✅
                                   müşavirlik BİLİNİYOR         ✅
                                   iç nakliye DARALDI           ⚠
                                   antrepo bekleme UNKNOWN      ❌ (T-301)
                                   bandrolleme UNKNOWN          ❌ (T-314)
```
