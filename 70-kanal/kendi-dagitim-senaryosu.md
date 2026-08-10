# SENARYO: IMPORTER + OWN DISTRIBUTION — VERİ YAPISI

```yaml
ajan:   kanal-marj-uzmani
tur:    TUR 2
tarih:  2026-08-10
durum:  DRAFT
amac:   "Ucuncu taraf distributor marjinin ortadan kalkmasina karsilik eklenen
         maliyetleri modelleyecek ALAN YAPISI. Kurucu bunu ileride GERCEK SIRKET
         VERISIYLE dolduracaktir."
uyari:  "BU BIR MALIYET TAHMINI DEGILDIR. Doldurulmus alanlarin cogu TABAN
         (floor) degeridir, BEKLENEN deger degildir. Bosluklar UYDURULMAMISTIR."
```

---

## 0. DOLULUK DURUMU

| Kategori | Toplam alan | Kanıtlı dolu | `null` + UNKNOWN |
|---|---|---|---|
| 1. Satış personeli | 9 | 3 | 6 |
| 2. Depo | 8 | 2 | 6 |
| 3. Araç ve filo | 8 | 0 | 8 |
| 4. Teslimat | 7 | 2 | 5 |
| 5. Tahsilat | 6 | 1 | 5 |
| 6. Fire / kırık / bozulma | 6 | 1 | 5 |
| 7. Operasyon / genel | 8 | 1 | 7 |
| 8. Karşı taraf: dış distribütör | 6 | 0 | 6 |
| **TOPLAM** | **58** | **10** | **48** |

> **%17 doluluk.** Bu bir eksiklik değil, bir **teşhistir**: kendi dağıtım modelinin
> maliyeti masabaşı araştırmayla **kurulamaz**; şirketin kendi verisi ve gerçek
> teklifler gerekir. Doldurulmuş 10 alanın **hepsi taban değeridir**.

---

## 1. SATIŞ PERSONELİ

| # | Alan | Birim | Değer | Statü | evidence | Not |
|---|---|---|---|---|---|---|
| 1.1 | `asgari_ucret_isveren_maliyeti_aylik` | TRY/ay/kişi | **40.214,03** | `FACT` | `EV-2026-08-10-621` | 2026, imalat **dışı** sektör (2 puan SGK indirimi). Ticaret/dağıtım bu gruptadır. |
| 1.2 | `asgari_ucret_brut_aylik` | TRY/ay | **33.030,00** | `FACT` | `EV-2026-08-10-621` | Referans |
| 1.3 | `satis_temsilcisi_ucret_carpani` | × asgari | `null` | `UNKNOWN` | — | Satış temsilcisi asgari ücretle çalışmaz. Çarpan **UNKNOWN**; şirket verisi gerekir. |
| 1.4 | `satis_temsilcisi_sayisi` | kişi | `null` | `UNKNOWN` | — | Kanal karmasına ve hedef nokta sayısına bağlıdır → bkz. §9 |
| 1.5 | `satis_primi_orani` | % ciro | `null` | `UNKNOWN` | — | Alkolde satış primi yapısı UNKNOWN |
| 1.6 | `arac_tahsisi_var_mi` | bool | `null` | `UNKNOWN` | — | Satış temsilcisi aracı, teslimat aracından **ayrı** kalemdir |
| 1.7 | `yol_yemek_telefon_aylik` | TRY/ay/kişi | `null` | `UNKNOWN` | — | Asgari ücret maliyetine **DAHİL DEĞİLDİR** |
| 1.8 | `satis_muduru_maliyeti_aylik` | TRY/ay | `null` | `UNKNOWN` | — | Yönetim katmanı; 1 kişilik ekipte gerekmeyebilir |
| 1.9 | `ziyaret_frekansi_nokta_ay` | ziyaret/ay | `null` | `UNKNOWN` | — | **Reklam yasağı nedeniyle kritik**: bilinirlik yalnızca sahada kurulur (`İP-2001`) |

> **`İP-2001` bağlantısı:** Marka bilinirliği ATL reklamla kurulamayacağı için, satış
> temsilcisinin ziyaret frekansı ve raf müdahalesi **bir pazarlama bütçesi işlevi
> görür**. Bu nedenle 1.9 satırı bir "operasyon detayı" değil, bir **pazarlama
> kaldıracıdır** ve model bunu öyle etiketlemelidir.

---

## 2. DEPO

| # | Alan | Birim | Değer | Statü | evidence | Not |
|---|---|---|---|---|---|---|
| 2.1 | `depo_tadab_sartlarini_saglamali_mi` | bool | **true** | `FACT` (mevzuat ajanı) | `EV-2026-08-09-204` (`L2`) | Sadece bu işe ayrılmış veya diğer gıdadan tefrik edilmiş, marka bazında sayım/etiket incelemesine imkân veren düzen, Kurumun yetki belgesi |
| 2.2 | `kendi_deposu_zorunlu_mu` | bool | **false** | `FACT` (mevzuat ajanı) | `EV-2026-08-09-204` (`L3`) | "Akde bağlanmış kullanıcı" olmak yeterli → **3PL yasal olarak açık** |
| 2.3 | `depo_basina_toptan_satis_belgesi_yillik` | TRY/yıl/depo | `null` → mevzuat ajanı | `UNKNOWN` (bu ajan için) | `EV-2026-08-09-210/-211` (`L4`) | Mevzuat ajanı 82.464 TL/yıl kaydetmiştir; **çok depolu ağ bu bedeli katlar**. Değer sahibi `ruhsat.yaml`'dır. |
| 2.4 | `depo_kirasi_aylik` | TRY/ay veya TRY/m²/ay | `null` | `UNKNOWN` | — | Lokasyona bağlı; teklif gerekir |
| 2.5 | `depo_personeli_sayisi` | kişi | `null` | `UNKNOWN` | — | Birim maliyet için 1.1 kullanılabilir |
| 2.6 | `3pl_birim_maliyeti` | TRY/palet/ay veya TRY/şişe | `null` | `UNKNOWN` | — | **A/B kararının en kritik alternatifi** — 3PL teklifi alınmadan kendi deposu savunulamaz |
| 2.7 | `sicaklik_kontrolu_gerekli_mi` | bool | `null` | `UNKNOWN` | — | `navlun-lojistik-uzmani` alanı ile kesişir (`M-1`, `L5`) |
| 2.8 | `ortalama_stok_gun` | gün | `null` | `UNKNOWN` | — | `finans-fizibilite` / `target_inventory_days` (`TBD`) |

---

## 3. ARAÇ VE FİLO

| # | Alan | Birim | Değer | Statü | Not |
|---|---|---|---|---|---|
| 3.1 | `arac_sayisi` | adet | `null` | `UNKNOWN` | Rota ve nokta sayısından türetilir |
| 3.2 | `arac_edinme_modeli` | SATIN_ALMA / KIRALAMA / TASERON | `null` | `UNKNOWN` | Sermaye yoğunluğunu doğrudan değiştirir |
| 3.3 | `arac_aylik_kira_veya_amortisman` | TRY/ay/araç | `null` | `UNKNOWN` | — |
| 3.4 | `yakit_maliyeti_aylik` | TRY/ay/araç | `null` | `UNKNOWN` | Rota km × tüketim × akaryakıt fiyatı |
| 3.5 | `sofor_maliyeti_aylik` | TRY/ay/araç | `null` (taban için 1.1) | `UNKNOWN` | Taban `EV-2026-08-10-621` |
| 3.6 | `sigorta_bakim_aylik` | TRY/ay/araç | `null` | `UNKNOWN` | — |
| 3.7 | `arac_teknik_sart_var_mi` | bool | `null` | `UNKNOWN` | Mevzuat ajanı `L5`: "ürünü dış şartlardan koruyacak" teknik özellik beklentisi |
| 3.8 | `arac_basina_gunluk_teslimat_noktasi` | nokta/gün | `null` | `UNKNOWN` | **Şişe başı dağıtım maliyetinin ana sürücüsü** |

---

## 4. TESLİMAT

| # | Alan | Birim | Değer | Statü | evidence | Not |
|---|---|---|---|---|---|---|
| 4.1 | `hedef_nokta_sayisi_GK` | adet | referans **48.956** | `FACT` (evren) | `EV-2026-08-10-613` | 2020, TADB. Bizim hedefimiz bunun bir **alt kümesidir**. |
| 4.2 | `hedef_nokta_sayisi_ASN` | adet | referans **29.218** | `FACT` (evren) | `EV-2026-08-10-613` | 2020, TADB |
| 4.3 | `hedef_nokta_sayisi_MK` | adet | `null` | `UNKNOWN` | `EV-613` | Modern kanal nokta sayısı bu kaynakta **yok** (merkezi alım nedeniyle dışarıda) |
| 4.4 | `teslimat_frekansi` | teslimat/ay/nokta | `null` | `UNKNOWN` | — | — |
| 4.5 | `ortalama_siparis_buyuklugu` | şişe/sipariş | `null` | `UNKNOWN` | — | Küçük sipariş = yüksek şişe başı maliyet |
| 4.6 | `minimum_siparis_miktari` | şişe | `null` | `UNKNOWN` | — | Bizim koyduğumuz eşik; kanal erişimini daraltır |
| 4.7 | `zincire_teslimat_merkezi_mi` | bool | `null` | `UNKNOWN` | `EV-613` dipnot | Zincirler **merkezi alım** yapar → zincir teslimatı mağaza değil **depo** teslimatıdır; bu, kendi dağıtımın zincir kanalında **avantajını azaltır** |

> **Yapısal not:** Kendi dağıtımın ekonomik değeri **kanala göre değişir**.
> Zincir market merkezi alım yaptığı için (`EV-613` dipnot 14), zincir kanalında
> "kendi dağıtım" ile "3PL/nakliyeci" arasında büyük fark yoktur. Kendi dağıtımın
> gerçek değeri **GK (48.956 nokta)** ve **ASN (29.218 nokta)** kanallarında ortaya
> çıkar — ve bu iki kanal charter'ın öncelik sıralamasında **2. ve 3.** sıradadır.
> Bu bir gerilimdir ve `finans-fizibilite`'ye açıkça taşınmalıdır.

---

## 5. TAHSİLAT

| # | Alan | Birim | Değer | Statü | evidence | Not |
|---|---|---|---|---|---|---|
| 5.1 | `zincir_vade_gun` | gün | bant: 45 / **60** / 90 / 120 | `ESTIMATE`+`ASSUMPTION` | `EV-602`, `EV-609`, `EV-617` | BASE = yasal tavan; STRESS = Migros vade tablosu |
| 5.2 | `gk_tekel_vade_gun` | gün | bant: 0 / **30** / 60 | `ASSUMPTION` | `EV-609` (türetme) | Geleneksel kanal organize kanaldan 23 gün kısa (süt, 2020) |
| 5.3 | `horeca_vade_gun` | gün | bant: 15 / **45** / 90 | `ASSUMPTION` | — | Kanıtsız; en riskli kanal |
| 5.4 | `supheli_alacak_orani` | % ciro | `null` | `UNKNOWN` | — | GK ve ASN'de **sıfır değildir**; şirket verisi gerekir |
| 5.5 | `tahsilat_personeli_maliyeti` | TRY/ay | `null` | `UNKNOWN` | — | Küçük noktada tahsilat = ayrı iş kolu |
| 5.6 | `cek_senet_kullanim_orani` | % | `null` | `UNKNOWN` | — | Perakende Yönetmelik m.5/4: çekle ödemede **geçerli ibrazın başladığı tarih**, vadeli araçlarda **vade tarihi** yasal süre içinde olmalıdır (`EV-2026-08-10-607` ile aynı madde) |

---

## 6. FİRE / KIRIK / BOZULMA

| # | Alan | Birim | Değer | Statü | evidence | Not |
|---|---|---|---|---|---|---|
| 6.1 | `kirik_urun_bedeli_sozlesmede_var_mi` | bool | **true** (zincir) | `FACT` | `EV-2026-08-10-612` | Alkollü içki zincir yıllık anlaşmasında **ismen** vardır |
| 6.2 | `kirik_urun_bedeli_tutari` | TRY veya % | `null` | `UNKNOWN` | `EV-612` | Kararda karartılmış |
| 6.3 | `dagitim_fire_orani` | % şişe | `null` | `UNKNOWN` | — | Cam şişe; iç dağıtımda kırılma |
| 6.4 | `iade_orani` | % şişe | `null` | `UNKNOWN` | `EV-2026-08-10-606` | **Şarapta iade için yasal sınır yok** → tamamen sözleşmesel |
| 6.5 | `fire_kdv_indirilemez_mi` | bool | **true** | `FACT` (vergi ajanı) | `EV-2026-08-10-103` / `Cİ-15.1` | KDVK md.30/c: zayi olan mala ait KDV indirilemez → fire maliyeti **mal + indirilemeyen KDV** |
| 6.6 | `skt_yaklasma_iade_kosulu` | metin | `null` | `UNKNOWN` | — | Şarapta SKT/tazelik yönetimi sözleşmeseldir |

> **Fire kaleminin gerçek formülü** (`Cİ-15.1`'den, vergi ajanının alanı):
> `fire_maliyeti = f × L4_per_şişe + f × KDV_per_şişe`. Kendi dağıtım modelinde
> `f` **bizim** kontrolümüzdedir; dış distribütörde **onun** kontrolündedir ama
> maliyeti sözleşmeye göre yine bize dönebilir.

---

## 7. OPERASYON / GENEL

| # | Alan | Birim | Değer | Statü | Not |
|---|---|---|---|---|---|
| 7.1 | `back_office_personel_maliyeti` | TRY/ay | `null` | `UNKNOWN` | Muhasebe, sipariş girişi, TADAB raporlama |
| 7.2 | `erp_sistem_maliyeti` | TRY/ay | `null` | `UNKNOWN` | — |
| 7.3 | `tadab_aylik_satis_raporlama_yuku` | saat/ay veya TRY/ay | `null` | `UNKNOWN` | Mevzuat ajanı `G6`: hizmet bedeli **satış** üzerinden, aylık satış raporu |
| 7.4 | `sevk_irsaliyesi_evrak_yuku` | TRY/ay | `null` | `UNKNOWN` | Mevzuat ajanı `L8`: en az 3 kopya, alıcı onaylı kopya iade, 2 yıl saklama |
| 7.5 | `ofis_kirasi_aylik` | TRY/ay | `null` | `UNKNOWN` | — |
| 7.6 | `sigorta_stok` | TRY/yıl | `null` | `UNKNOWN` | — |
| 7.7 | `finansman_orani_yillik` | % | referans **%38,6** | `ESTIMATE` (dış gözlem) | `EV-2026-08-10-617`: Migros ticari borçlarını 31.12.2025'te yıllık %38,6 ile iskonto ediyor → TL ticari kredinin **piyasa fiyatı göstergesi**. **Bu alan `makro.yaml`'a aittir**, bu ajanın değil. |
| 7.8 | `toplam_yillik_sabit_dagitim_maliyeti` | TRY/yıl | `null` | `UNKNOWN` | **Türev alan** — 1–7 doldurulunca hesaplanır |

---

## 8. KARŞI TARAF — DIŞ DİSTRİBÜTÖR (B modeli)

| # | Alan | Birim | Değer | Statü | Not |
|---|---|---|---|---|---|
| 8.1 | `distributor_marj_orani` | % | `null` | **`UNKNOWN`** | **Bu turda hiçbir kanıtlı değer bulunamamıştır.** Uydurulmamıştır. |
| 8.2 | `distributor_marj_tanimi` | margin/markup + KDV tabanı + katman | `null` | `UNKNOWN` | `M1` gereği tanımsız oran geçersizdir |
| 8.3 | `distributor_vade_bize` | gün | `null` | `UNKNOWN` | Distribütör kendi vadesini **bize** yansıtır |
| 8.4 | `distributor_kanal_erisimi` | nokta sayısı | `null` | `UNKNOWN` | Erişim iddiası **doğrulanmadan** kabul edilemez |
| 8.5 | `distributor_munhasirlik_talebi` | bool | `null` | `UNKNOWN` | Satış Yön. m.16 (mevzuat ajanı `K6`): münhasırlık ve bağlı satış **uygulanamaz** |
| 8.6 | `distributor_minimum_alim_taahhudu` | şişe/yıl | `null` | `UNKNOWN` | Stok riskini kime bıraktığını belirler |

---

## 9. KIRILMA NOKTASI — FORMÜL (hesabı `finans-fizibilite` yapar)

```
KENDİ DAĞITIM ekonomiktir  <=>

    Σ(1..7 sabit maliyetler)  <  hacim_şişe × L6 × distributor_marj_oranı
                                  ─────────────────────────────────────
                                  = distribütöre DEVREDİLEN marj

  Eşik hacim:
    hacim_kritik = yıllık_sabit_dağıtım_maliyeti / (L6 × distributor_marj_oranı)
```

**Bu formül şu anda ÇÖZÜLEMEZ**, çünkü sağ taraftaki `distributor_marj_oranı` (8.1)
ve sol taraftaki `yıllık_sabit_dağıtım_maliyeti` (7.8) **ikisi de UNKNOWN**'dır.

**Ama şu üç yapısal ifade kanıtlıdır ve model bunları kullanabilir:**

1. **Zincir kanalında kendi dağıtımın marjinal faydası düşüktür** — zincirler merkezi
   alım yapar (`EV-2026-08-10-613` dipnot 14), yani teslimat noktası sayısı azdır ve
   basit bir nakliyeci yeterlidir. Ayrıca zincir zaten **lojistik bedeli** almaktadır
   (`EV-2026-08-10-612`) — yani zincir kanalında dağıtım maliyetinin bir kısmı **zaten
   bize fatura edilmektedir**.
2. **Kendi dağıtımın gerçek değeri GK ve ASN'dedir** (48.956 + 29.218 nokta,
   `EV-613`) — ve bu kanallar reklam yasağı dünyasında bilinirliğin **tek** kanalıdır
   (`İP-2001`).
3. **Charter'ın kanal önceliği (1 zincir, 2 tekel, 3 HoReCa) ile kendi dağıtımın
   ekonomik mantığı ters yöndedir.** Öncelik 1'de kendi dağıtım gereksizdir; öncelik
   2 ve 3'te vazgeçilmezdir. **Kanal karması kararı, dağıtım modeli kararını belirler
   — tersi değil.** Bu, bu ajanın en önemli yapısal çıkarımıdır.

---

## 10. PİLOT HACİMDE UYARI (5.000 şişe/yıl)

5.000 şişe/yıl = **ayda ~417 şişe** = ayda ~35 koli (12'li). Bu hacim:

- **Tek bir satış temsilcisinin** aylık maliyetini (taban `40.214,03 TL`,
  `EV-2026-08-10-621`) bile karşılayamaz: şişe başına yalnız personel tabanı
  **96,5 TL/şişe** eder (40.214,03 / 417).
- Yani **5.000 şişe/yıl senaryosunda kendi dağıtım ekonomik olarak imkânsızdır**;
  tek seçenek dış distribütör veya doğrudan zincir satışıdır.

> Bu, bir hesap değil bir **büyüklük mertebesi kontrolüdür** ve tam da bu yüzden
> güçlüdür: 96,5 TL/şişe, benchmark bandının (`pazar.yaml`: 600–900 TL) **%11–16'sıdır**
> ve bu **yalnızca bir kişinin asgari ücret tabanıdır** — araç, depo, yakıt, prim,
> back-office hariç. `finans-fizibilite` bu kontrolü kendi rakamlarıyla tekrarlamalıdır.

---

## 11. BU YAPININ DOLDURULMASI İÇİN GEREKENLER

| Kim | Ne | Nasıl |
|---|---|---|
| Kurucu / şirket | 1.3, 1.7, 2.4, 2.5, 3.1–3.6, 5.5, 7.1–7.6 | Kendi bordro/kira/filo verisi |
| 3PL firmaları | 2.6 | Teklif (TUR 7) |
| Dış distribütör adayları | 8.1–8.6 | Görüşme (TUR 7, `T-604`) |
| Zincir kategori yöneticileri | 5.1, 6.2, 6.4 | Yıllık anlaşma müzakeresi (TUR 7) |
| `navlun-lojistik-uzmani` | 2.7, 6.3 | `K-1` ipucunun cevabı |
| `mevzuat-ruhsat-uzmani` | 2.1, 2.3, 7.3, 7.4 | `ruhsat.yaml` |
| `finans-fizibilite` | 7.7, 7.8, §9 | `makro.yaml` + model |
