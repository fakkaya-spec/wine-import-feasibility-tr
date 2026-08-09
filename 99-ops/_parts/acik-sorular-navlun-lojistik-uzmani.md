# AÇIK SORULAR — navlun-lojistik-uzmani (TUR 1)

> **UNKNOWN yazmak başarısızlık değildir; uydurmak başarısızlıktır.**
> Aşağıdaki sorular TUR 1'de kapatılamadı.

---

## KRİTİK (nihai kararı bloke edebilir)

| # | Soru | Neden kritik | Kim / nasıl çözer | Ticket |
|---|---|---|---|---|
| **NL-Q1** | **Bizim rotalarımız için gerçek FCL navlunu kaç USD/EUR?** (İspanya/İtalya/Fransa/California/Şili/G.Afrika → Ambarlı/Mersin/İzmir; 20DV ve 40HC; all-in) | Hiçbir rotamız için doğrulanmış navlun yok. Bu, CIF'in ve dolayısıyla tüm vergi matrahının girdisidir. Navlun 2× olursa şişe başı maliyet ~0,10–0,20 USD artar. | 3 forwarder'dan yazılı kotasyon (geçerlilik tarihi ve dahil kalemler yazılı) | `T-304` |
| **NL-Q2** | **Ruhsat / analiz / uygunluk / bandrol beklemesi kaç gün sürer?** | Demurrage/detention (20DV'de 60 günde ~8.000 USD) ve toplam lead time bu sayıdan türer. Toplam lead time UNKNOWN olduğu sürece işletme sermayesi ve `peak_cash_requirement` hesaplanamaz. | `mevzuat-ruhsat-uzmani` T0 takvimi | `T-301` |
| **NL-Q3** | **Toplam lead time (PO → satışa hazır) kaç gün?** | CCC, stok gün sayısı, `peak_cash_requirement`. Yalnız transiti lead time sanmak modeli sistematik iyimser yapar. | NL-Q1 + NL-Q2 + sourcing üretim süresi birleşince türetilir | `T-301`, `T-304` |
| **NL-Q4** | **California → İstanbul transit süresi ve navlunu nedir?** | Benchmark ürünün (Gold Country) rotası tam budur ve tamamen UNKNOWN. Kaynaklar birbiriyle çelişiyor (`C-302`). | Armatör servis tarifesi + forwarder kotasyonu | `T-304` |

---

## YÜKSEK

| # | Soru | Neden önemli | Kim / nasıl çözer | Ticket |
|---|---|---|---|---|
| NL-Q5 | Tedarikçinin **gerçek şişe formu, çapı, koli dış ölçüsü, koli brüt ağırlığı, palet konfigürasyonu, cam ağırlığı** nedir? | Şişe başı hacim 0,00223 → 0,0036 m³'e çıkarsa **tüm konteyner kapasiteleri %38 düşer.** Bu, hesabın en kırılgan girdisidir. | `global-sourcing-kasifi` — RFQ'ya "case & pallet spec sheet" maddesi eklenmeli | `T-302` |
| NL-Q6 | **Çekici + şasi darası** kaç kg? | 40HC'de Türkiye karayolu kargo tavanını (24,1–27,1 t) doğrudan belirler. 17 t dara ise 5 katmanlı paletli 40HC yüklemesi imkânsız hale gelir. | Türk nakliyeciden ruhsat/tartı bilgisi | `T-304` |
| NL-Q7 | **Terminal ardiye free time** kaç gündür? | Demurrage senaryosunda 0 gün varsaydım (muhafazakâr). Gerçekte 3–7 gün olabilir → gecikme maliyeti düşer. | Ambarlı terminallerinden (Marport/Kumport/Mardaş) tarife | `T-304` |
| NL-Q8 | **Ambarlı terminallerinin** kendi tarifesi nedir? | Beldeport/Asyaport tarifelerini gösterge olarak kullandım. Ambarlı gerçek varış limanı olacaksa kendi tarifesi gerekir. | Terminal tarife sayfaları / acente | `T-304` |
| NL-Q9 | **Bandrolleme operasyonunun birim maliyeti (şişe başı) ve kapasitesi (şişe/gün)** nedir? | 100.000 şişe/yıl senaryosunda operasyonel darboğaz adayı. Birim maliyet doğrudan L5'e girer. | Antrepo işletmecisinden hizmet teklifi | `T-304` |
| NL-Q10 | **Sıcaklık kaynaklı beklenen fire/leakage oranı (%)** nedir? | Bu sayı olmadan liner/reefer kararı finansal olarak verilemez. | Sigortacı hasar istatistiği veya Hillebrand Gori benzeri uzman | `T-304` |
| NL-Q11 | **Thermal liner birim maliyeti** nedir? | Reefer'a alternatif olarak sunuluyor ama fiyatı hiçbir kaynakta yok. | Forwarder / liner tedarikçisi | `T-304` |

---

## ORTA

| # | Soru | Neden önemli | Ticket |
|---|---|---|---|
| NL-Q12 | Limandan depoya konteyner çekme ücreti (Ambarlı → İstanbul depo) | Bulunan band (3.000–30.000 TL) modele girecek kadar dar değil | `T-304` |
| NL-Q13 | Antrepo giriş/çıkış elleçleme ücreti ve minimum süre taahhüdü | Antrepo maliyetinin depolamadan büyük olabilecek kısmı | `T-304` |
| NL-Q14 | Türk sigortacıdan gerçek kargo sigortası kotasyonu (ICC A + kırılma + termal şok), muafiyet dahil | Prim bandı %0,1–1,5 çok geniş | `T-304` |
| NL-Q15 | Ordino, ISPS, doc fee, BAF/CAF tutarları | "All-in" ile "base" arasındaki farkın büyüklüğü | `T-304` |
| NL-Q16 | Paletsiz (floor loaded) yüklemede gerçek kırılma oranı ve antrepoda yeniden paletleme maliyeti | Paletli/paletsiz kararının net finansal farkı UNKNOWN kaldı | `T-304` |
| NL-Q17 | İtalya ve Fransa → Türkiye transit süreleri | Sourcing alternatiflerinin karşılaştırması eksik | `T-304` |
| NL-Q18 | Şili → Türkiye rota yapısı (direkt servis var mı, aktarma nerede) | Şili sourcing senaryosu değerlendirilemiyor | `T-304` |
| NL-Q19 | Diğer armatörlerin (MSC, CMA CGM, Arkas, Hapag-Lloyd) Türkiye ithalat D&D free time'ı | Yalnızca Maersk tarifesi elimde; 7 gün genelleştirilebilir mi bilinmiyor | `T-304` |

---

## DÜŞÜK

| # | Soru | Ticket |
|---|---|---|
| NL-Q20 | 40HC gerçek dara ağırlığı (ASSUMPTION 3.900 kg kullanıldı) | `T-304` |
| NL-Q21 | LCL konsolidasyon beklemesinin transit süreye kaç gün eklediği | `T-304` |
| NL-Q22 | Şarap konteynerinin IMO/tehlikeli yük sınıfına girip girmediği (terminal %20 surprim) | `T-301` (mevzuat) |
