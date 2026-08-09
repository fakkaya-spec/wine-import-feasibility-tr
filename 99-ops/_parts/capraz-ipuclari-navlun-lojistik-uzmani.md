# ÇAPRAZ İPUÇLARI — navlun-lojistik-uzmani (TUR 1)

> Bunlar **sonuç değildir, ipucudur.** Kendi alanım dışında rastladığım ama
> silmek istemediğim bulgular. İlgili ajan doğrulamadan hiçbiri kullanılamaz.

---

## → `mevzuat-ruhsat-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| M-1 | Bandrol/kodlu etiketin ya **yabancı üretim tesisinde** ya da Türkiye'de belirlenmiş **antrepolarda (İstanbul, İzmir, Mersin)** uygulandığı yönünde T5 bilgi bulundu (`EV-2026-08-09-380`). **Doğrulanmadı.** | Menşede bandrollenebiliyorsa antrepo bekleme süresi ve demurrage riski dramatik biçimde düşer. Lead time'ın en büyük belirsizliği burada. |
| M-2 | 2026 için "bandrol hizmet bedeli 1.000 adette 198,27 TL (baskı hariç)" şeklinde T5 bir haber görüldü (Bigpara/Hürriyet). **Ben bunu doğrulamadım ve kullanmadım** — bandrol ücreti senin alanın. | Şişe başı maliyete doğrudan girer. |
| M-3 | Alkollü içki ithalatında **iki ayrı beyanname** (antrepo + serbest dolaşıma giriş) gerekeceği varsayımıyla gümrük müşavirliği maliyeti hesapladım (`EV-2026-08-09-342`). Bu varsayımın mevzuat teyidi yok. | Yanlışsa müşavirlik maliyeti yarıya iner. |
| M-4 | Alkollü içki için **özel antrepo yetkisi / uygun depo şartı** olup olmadığını doğrulayamadım. Antrepo maliyeti bu şarta bağlı değişir. | Depo seçimi ve maliyeti. |
| M-5 | Terminal tarifelerinde IMO/tehlikeli yük konteynerine %20 surprim var (`EV-2026-08-09-340`). Şarap IMO sınıfına girmiyor olmalı (ABV düşük) ama yüksek alkollü ürünlerde girer. Şarap için teyit gerekli. | Yanlışsa terminal maliyetine +%20. |

---

## → `gumruk-vergi-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| G-1 | **Navlun ve sigorta gümrük kıymetine girer.** Ben sigorta primini %0,3–0,6 (CIF+%10 üzerinden) olarak ESTIMATE ettim (`EV-2026-08-09-360`) ve navlun bandını verdim — ama **gümrük kıymeti hesabı senin alanın, ben yapmadım.** Bkz. `T-303`. | Matrah tabanını doğrudan büyütür; ÖTV/KDV'ye kadar çarpan etkisi yapar. |
| G-2 | **Incoterm seçimi gümrük kıymetini değiştirir.** EXW alımda navlun+sigorta ithalatçının, CIF alımda satıcının faturasında olur. İkisinde de kıymete girer ama **belgelendirme ve ispat yükü farklıdır.** | Kıymet beyanı ve gözetim riski. |
| G-3 | 2026 Gümrük Müşavirliği Asgari Ücret Tarifesi'nde **ÖZ-4 kalemi (laboratuvar tahlili / ekspertiz / TSE-DTS işlemleri) 940 TL/işlem** olarak var (`EV-2026-08-09-342`). Alkollü içkide analiz zorunluysa bu kalem her partide çıkar. | Küçük ama unutulan kalem. |
| G-4 | Terminal tarifesinde **tam muayene** 20ft 2.322 TL / 40ft 3.249 TL (`EV-2026-08-09-341`). Alkollü içkide muayene/numune olasılığı yüksek — kırmızı hat oranı senin alanın. | Muayene olasılığı × maliyet = beklenen değer. |
| G-5 | **Antrepo rejiminin nakit akışı avantajı:** vergiler serbest dolaşıma girişte doğar, antrepoda beklerken doğmaz. Ürün antrepoda bandrollenirken vergi ödenmiyorsa `peak_cash_requirement` düşer. Bunu ben hesaplamadım. | Nakit akışı modelinin yapısını değiştirebilir. |

---

## → `global-sourcing-kasifi`

| # | İpucu | Neden önemli |
|---|---|---|
| S-1 | **Şişe/koli geometrisi konteyner kapasitesini %38'e kadar değiştiriyor.** Burgundy formu (geniş omuzlu) şişe, Bordeaux formuna göre şişe başı hacmi 0,00223 m³'ten 0,0036 m³'e çıkarıyor. RFQ'da **şişe formu, çapı, koli dış ölçüsü ve palet konfigürasyonu** mutlaka sorulmalı. Bkz. `T-302`. | Şişe başı navlunun tek en büyük belirleyicisi. |
| S-2 | **Hafif cam (300–420 g) sourcing kriteri olmalı.** Ağırlık 40HC'de bağlayıcı kısıt. Ağır cam (700 g) 40HC kapasitesini ~%15 düşürür. Fiyat/performans segmentinde hafif cam zaten yaygındır. | Hem navlun hem ambalaj maliyeti. |
| S-3 | **6'lı koli 12'liden hacimsel olarak ~%7 daha verimsiz.** AB tedarikçileri 6'lı, ABD tedarikçileri 12'li standardını kullanıyor (`EV-2026-08-09-308`). Private label'da koli formatı **müzakere edilebilir bir kalemdir**. | Konteyner başına şişe. |
| S-4 | **Akdeniz menşei lojistik olarak açık ara üstün:** transit 5–10 gün, haftalık sefer, düşük sıcaklık riski. California/Şili/G.Afrika 26–45 gün, seyrek sefer, yüksek sıcaklık riski. Benchmark ürünü California menşeili ama **lojistik olarak en kötü rota.** | Menşe seçiminde lojistik ağırlık taşımalı. |
| S-5 | **Incoterm sorusu:** EXW/FOB alırsak navlunu biz kontrol ederiz (rota, konsolidasyon, liner/reefer kararı bizde). CIF alırsak tedarikçinin forwarder'ına mahkûm oluruz ve **sigorta muhtemelen ICC (C) olur — ki kırılmayı kapsamaz.** Bkz. `T-305`. | Risk transferi ve maliyet kontrolü. |
| S-6 | Tedarikçiden **thermal liner / reefer** ile yükleme yapıp yapamayacağı, yaz aylarında yükleme politikası sorulmalı. | Bozulma riski. |

---

## → `finans-fizibilite`

| # | İpucu | Neden önemli |
|---|---|---|
| F-1 | **5.000 şişe/yıl senaryosu lojistik olarak verimsizdir.** LCL kırılma noktası ~5.000–7.000 şişe/sevkiyat. 5.000 şişe/yıl LCL demektir; LCL'de birim maliyet yüksek, kırılma riski fazla, varış sabit masrafları (200–500 USD) hacimden bağımsızdır. Ölçek eğrisi bu noktada **doğrusal değildir.** | Ölçek senaryolarının karşılaştırması. |
| F-2 | **Ruhsat/bandrol gecikmesi limanda yaşanırsa 20DV başına 60 günde ~8.000 USD** (`EV-2026-08-09-344`). Antrepoya çekilirse ~210 EUR. **Fark ~30 kat.** Modelde hangi senaryonun varsayıldığı açıkça yazılmalı. | Pilot maliyetini tek başına ikiye katlayabilir. |
| F-3 | **Toplam lead time UNKNOWN'dır.** Yalnız transit süresini (7–10 gün) lead time sanmak modeli sistematik olarak iyimser yapar. CCC ve `peak_cash_requirement` doğrudan etkilenir. | İşletme sermayesi. |
| F-4 | **2 × 20DV, 1 × 40HC'den %24–27 daha fazla şişe taşır** (ağırlık limiti araç başına). Ama konteyner başı sabit masraflar (THC 113 USD, müşavirlik ek konteyner 1.350 TL, iç nakliye, ardiye) az konteyner lehinedir. Bu bir **optimizasyon problemi**, sabit bir cevap yok. | Şişe başı lojistik maliyeti. |
| F-5 | Tüm navlun rakamları **spot**tur ve `ttl: 14d`'dir. Model bir navlun rakamına kilitlenirse 2026-08-23'ten sonra geçersizdir. Navlun **duyarlılık değişkeni** olarak modellenmelidir (ör. ±%100). | Model geçerliliği. |

---

## → `kanal-marj-uzmani`

| # | İpucu | Neden önemli |
|---|---|---|
| K-1 | Depodan kanala dağıtım maliyetini (şişe başı) hesaplayamadım — **UNKNOWN**. Ama alkollü içkide dağıtımın **yetki belgeli depo/araç** gerektirip gerektirmediği kanal maliyetini değiştirir. | Dağıtım modeli seçimi (kendi filo vs 3PL). |
| K-2 | Sevkiyat sıklığı düşükse (yılda 1–2 konteyner) **stok tek seferde gelir** → depoda uzun süre bekler → kanala parça parça dağıtılır. Bu, kanal vadesiyle birleşince nakit döngüsünü uzatır. | Vade ve stok politikası. |

---

## → `turkiye-pazar-kasifi`

| # | İpucu | Neden önemli |
|---|---|---|
| P-1 | Rafta gördüğün ithal şarapların **koli formatı (6'lı/12'li)** ve **cam ağırlığı** (şişeyi eline al) gözlemlenebilir. Bu, rakiplerin lojistik maliyet yapısı hakkında ipucu verir. | Rakip maliyet yapısı. |
| P-2 | Benchmark ürünü (Gold Country) **California menşeili** — yani en pahalı ve en riskli lojistik rotadan geliyor. Buna rağmen 599,90 TL'de raftaysa, ya çok ucuz alınıyor ya çok büyük hacimde geliyor. **Bu bir sinyal.** | Rakibin ölçeği hakkında ipucu. |
