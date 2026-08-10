# AÇIK SORULAR — navlun-lojistik-uzmani · TUR 3.25

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 3.25 — FORWARDER RFQ PAKETI
tarih:  2026-08-10
not:    "99-ops/acik-sorular.md bu turda DOKUNMA listesindedir."
```

> Bu turda **yeni navlun araştırması yapılmadı**; yalnızca RFQ paketi
> hazırlandı. Aşağıdaki sorular **RFQ metnine gömülmüştür** — yani bu turun
> çıktısı soruların cevabı değil, **soruların doğru muhataba doğru formatta
> sorulabilir hâle getirilmesidir.**

| # | Soru | RFQ'da nerede soruluyor | Kritiklik | Bağlı kayıt |
|---|---|---|---|---|
| **OQ-3251** | FCL base ocean freight gerçekte 300 USD mü 1.200 USD mü? | §5.1 B1 + §5.3 (all-in reddi) | **CRITICAL** | `C-311`, `T-304` |
| **OQ-3252** | İtalya lane'i **gerçekten servis edilmiyor mu**, yoksa yalnızca kamuya açık fiyatı mı yok? | §4 Block A3 + *"not served yazın, boş bırakmayın"* | **HIGH** | `T-312`, `EV-2026-08-10-304` |
| **OQ-3253** | İspanya dışı 6 menşenin origin local charge'ları | §5.2 (yayımlanmış tarife talebi) | **HIGH** | `T-312` |
| **OQ-3254** | Çekici + şasi darası kaç kg? 44 t altında 40HC'ye ne konabilir? | §7 D1–D2 | **HIGH** | `karayolu_agirlik.cekici_sasi_darasi_kg` (ASSUMPTION) |
| **OQ-3255** | LCL fiyatı **loose case hacmi** üzerinden mi, **paletli footprint** üzerinden mi? (≈%5–10 fark) | §2 son paragraf + EK-1 A10 | MEDIUM | `OQ-2501` |
| **OQ-3256** | LCL fiyatına **CFS dahil mi**? | §5.1 B3/B8 + §6 EXCLUDED | **HIGH** | `OQ-2501` |
| **OQ-3257** | Konteyner başına **kaç palet** yükleniyor (9 mu 10 mu, 20 mi 21 mi)? | EK-1 A7 | MEDIUM | `C-301` |
| **OQ-3258** | Armatör THD'si ile terminal kapı-çıkış ücreti **aynı olayı iki kez** mi fiyatlıyor? | §5.1 B7 + B8 itemisation | **HIGH** | `C-313`, `T-313` |
| **OQ-3259** | Demurrage/detention free time armatöre göre değişiyor mu (Maersk 7 gün dışında)? | §5.1 B10–B12 | MEDIUM | `T-313` |
| **OQ-3260** | Terminal ardiye free time **0 gün mü 5 gün mü**? | §10.3 (berthing → pick-up) | MEDIUM | `C-312` |
| **OQ-3261** | Thermal liner birim maliyeti ve hangi rotalarda öneriliyor? | §9 E3 | **HIGH** | `sicaklik_riski.thermal_liner_ek_maliyet` |
| **OQ-3262** | Kırılma/termal teminatlı sigorta primi ve **istisnaları** (cam/şarap istisnası var mı?) | §9 E1 | **HIGH** | `sigorta.*`, `T-304` |
| **OQ-3263** | LCL'de **menşe konsolidasyon bekleme süresi** kaç gün? (lead time'a gizli ek) | §10.2 + EK-1 D4 | MEDIUM | `sure.toplam_lead_time_gun` |
| **OQ-3264** | 15/30/60 günlük ruhsat beklemesinde forwarder ne öneriyor, kaça mal olur? | §10.4 + EK-1 D6 | **HIGH** | `T-301` (süre başka ajanda), `demurrage_detention.*` |
| **OQ-3265** | Antrepo **alkollü içki için yetkili mi** — tesisin kendi beyanı | §9 E6 | MEDIUM | mevzuat tarafı `mevzuat-ruhsat-uzmani`'nda |
| **OQ-3266** | Teklif **spot mu kontrat mı**, kontratsa minimum hacim taahhüdü ne? | §5.1 B17 + §8 | MEDIUM | `navlun.navlun_tipi` |
| **OQ-3267** | BAF/ETS geçerlilik süresi **içinde** değişiyor mu? (değişiyorsa teklif aslında sabit değil) | §8 + EK-1 F1 | MEDIUM | `tur2.fcl_navlun.surcharge_*` |

---

## BU TURDA CEVAPLANAMAYAN VE RFQ'NUN DA ÇÖZMEDİĞİ SORULAR

| # | Soru | Neden RFQ çözmez |
|---|---|---|
| **OQ-3268** | Beklenen **kırılma / fire oranı (%)** | Forwarder kendi hasar istatistiğini paylaşmayabilir; paylaşsa bile kendi lehine yanlıdır. Gerçek cevap **sigortacının hasar geçmişi** veya pilot sevkiyattır |
| **OQ-3269** | **Bandrolleme** birim maliyeti ve kapasitesi (şişe/gün) | Forwarder'ın işi değil; antrepo işletmecisi / bandrol operatörü alanı → `T-314` |
| **OQ-3270** | Konteyner içi **ölçülmüş** sıcaklık (data logger) | Ancak gerçek sevkiyatta ölçülür; kotasyonla gelmez |
| **OQ-3271** | 5.000 şişelik pilotta **gerçek** LCL vs FCL kararı | Fiyat farkı gürültü seviyesinde (`lcl-vs-fcl-pilot.md` §3) — teklif gelse bile karar **non-finansal** kalabilir |
