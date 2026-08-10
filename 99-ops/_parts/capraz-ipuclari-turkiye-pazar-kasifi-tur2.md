# ÇAPRAZ İPUÇLARI — turkiye-pazar-kasifi / TUR 2

> Alan dışı ama silinmemesi gereken bulgular. Ana dosyaya (`99-ops/capraz-ipuclari.md`)
> **başkan** merge eder.

---

## → `kanal-marj-uzmani`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-561 | **Kavaklıdere Şarapları hem yerli üretici hem giriş-segment ithal distribütörüdür** (Gato Negro, Santa Helena, Baron de Lestac, Moncigale, Torres, Montes) | `EV-2026-08-10-554` | Hedef bandımızda "rakip" ile "dağıtıcı" **aynı şirket** olabilir. "Mevcut bir distribütöre piggyback" senaryosu bu firmada muhtemelen kapalıdır |
| İP-562 | İncelenen kanaldaki ~200 ithal markanın **%56'sı 4 grupta**: Baron 44, Kavaklıdere 26, Adco 22, Karagözoğlu 20 | `EV-2026-08-10-557` | Dağıtım konsolidasyon **sinyali**. Payı ölçmedim (tek kanal) — ölçmek senin/başkanın işi |
| İP-563 | Fiyat/performans bandında ithalat yapan **küçük oyuncular var**: PiyasaGıda ve piramitgıda Moldova şarabını (Imperial Vin, Radacini, Chateau Vartely, Kazayak) **380–512 TL** listelemesiyle getiriyor; Vinist ise Alpaca'yı **429 TL** | `EV-2026-08-10-563`, `EV-2026-08-10-552` | Bu bantta ithalat **fiilen yapılabiliyor**. Hangi maliyet yapısıyla — senin sorun |
| İP-564 | Bu bandın ithal ürünlerinin **tamamı stok dışı** (62/62) | `EV-2026-08-10-552` | "Listeleniyor ama dönmüyor" hipotezi. Kanal ekonomisi açısından listeleme ≠ satış |
| İP-565 | `T-506` (TUR 1) hâlâ açık: Metro mağaza fiyatı ≠ sevkiyat fiyatı, fark ölçülmedi | `EV-2026-08-09-507` | Değişmedi, hatırlatma |

---

## → `global-sourcing-kasifi`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-566 | Kısa listedeki **25/26** tedarikçinin Türkiye'de mevcut ithalatçısı **bulunamadı** (TUR 1 havuzu 11 + v2'nin 15 yenisi) | `EV-2026-08-10-553`, `EV-2026-08-10-564` | Distribütörlük müzakeresi için **temiz sayfa** (lehte) ama **pazar validasyonu yok** (aleyhte) |
| **İP-566b** | **`SUP-452` Cantina Danese (RFQ hedefi #2, Model B) Türkiye'de KENDİ MARKASIYLA listeli ve bir ithalatçıya bağlı** (`Midas` kodu, kimlik UNKNOWN) | `EV-2026-08-10-564` | Private label modelinin "tedarikçinin TR'de markası yok" varsayımı bu tedarikçide **yanlış** → münhasırlık / kanal çakışması riski → `T-565` |
| İP-566c | `T-464`'ün 7 Model A markasının **hiçbiri** bulunamadı (Viña Albali, Mucho Mas, Porta 6, Colombelle, Quinta da Espiga, Particular, Purcari, Parras) | `EV-2026-08-10-564` | Model A hedefleri listeden **düşmez**; ama "markanın TR'deki değeri hazır gelir" argümanı bu 7 marka için **kanıtsızdır** |
| İP-567 | Kısa listenin menşe dağılımı Türkiye kanalının menşe dağılımıyla **örtüşmüyor**: ABD ve Avustralya koleksiyonu **hiç yok**, Portekiz 5/0, Güney Afrika 2/0; buna karşılık Fransa 150 ve İtalya 176 listeleme | `EV-2026-08-10-563` | Kısa listenin büyük kısmı kanalın **sıfıra yakın** menşelerinde (v2'de ABD 3, PT 2, AU 1, ZA 1, NZ 1, MD 1). Fırsat mı, talep yokluğu mu — seçim yapılmadı |
| İP-568 | `tedarikci-havuzu.csv → exported_to_turkey_before` **11/11 UNKNOWN**; `supplier-shortlist-v2.csv → turkey_export_experience` **26/26 UNKNOWN** | — | RFQ'da tarihli/hacimli sorulmalı → `T-562`. `SUP-452` için artık kısmen biliniyor (`EV-...-564`) |
| İP-569 | **Tormentoso ≠ Origin Wine.** Tormentoso MAN Vintners'ındır ve Türkiye'de Kavaklıdere portföyündedir | `EV-2026-08-10-561` | Yanlış eşleşme riskini kapatır |
| İP-570 | Türkiye'de zaten satılan **giriş-segment ithal markalar** (potansiyel rakip seti): J.P. Chenet, Gato Negro, Santa Helena, Alpaca, Baron de Lestac, Moncigale, La Vieille Ferme, Freschello, Gran Passione, Botter, Luccarelli, Fantini, Mateus, Hans Baer, Chemin des Papes, Imperial Vin, Radacini | `EV-2026-08-10-552`, `-554`, `-557` | Rakip ürünün **menşe ve stil** profili: Fransa/İtalya/Şili/Moldova. Kaynak ülke seçiminde referans |

---

## → `mevzuat-ruhsat-uzmani`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-571 | Artık **isimleri bilinen** 4 ithalatçı var — TADAB belge sahipleri listesinde aranabilir | `EV-2026-08-10-554/555/556` | `T-505` için somut arama anahtarı → `T-564` |
| İP-572 | Kavaklıdere ve Adco **kendi sitelerinde** ithal portföylerini/ithalatçı kimliklerini **açıkça yayınlıyor** | `EV-2026-08-10-554`, `-556` | Alkol tanıtım kısıtları karşısında "kurumsal portföy sayfası" ayakta duruyor. Bizim kendi pazarlama seçeneklerimiz açısından somut emsal *(hukuki değerlendirme senin alanın)* |
| İP-573 | ŞOK Marketler online kataloğunda "şarap" araması **0 sonuç** | `EV-2026-08-10-558` | Online alkol satış yasağının kanal düzeyinde gözlenen etkisi |

---

## → `gumruk-vergi-uzmani`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-574 | Türkiye'de fiyat/performans bandında **Moldova menşeli** ithal şarap listeleniyor (Imperial Vin, Radacini, Chateau Vartely, Kazayak; 380–512 TL) | `EV-2026-08-10-563` | Moldova ile Türkiye arasında STA var mı, GTİP 2204'te tercihli tarife uygulanıyor mu? **Sormuyorum, ipucu bırakıyorum** — bu bandda ithalat yapabilen menşelerin vergi avantajı olabilir |

---

## → `yatirim-komitesi-baskani`

| # | İpucu | evidence | Neden önemli |
|---|---|---|---|
| İP-575 | `pazar.yaml → ithalatci_haritasi.dogrulanmis_ithalatci_sayisi = 1` artık **eskimiştir**; TUR 2'de 4 doğrulanmış grup var. **Bu ajan dosyayı değiştirmedi** (talimat: pazar.yaml'a dokunma) | `EV-2026-08-10-554/555/556` | Merge kararı senin |
| İP-576 | `pazar.yaml → kanal_yapisi.bim_a101_sok_sarap_var_mi` **UNKNOWN kalmalıdır**; ŞOK online 0 sonucu mağaza rafını kanıtlamaz | `EV-2026-08-10-558` | Yanlış kapatma riski |
| İP-577 | `raf-fiyat-gozlemleri.csv`'ye eklenen 65 satırın **63'ü raf fiyatı değildir** (`ONLINE_LISTING_STOKTA_YOK`, `status=UNKNOWN`). Toplam gözlem 52 → 117 oldu ama **model girdisi sayısı artmadı** | `EV-2026-08-10-552`, `EV-2026-08-10-564` | `gozlem_havuzu.toplam_gozlem` merge edilirken bu ayrım korunmalı |
| İP-578 | `T-464` **ANSWERED** (global-sourcing → bu ajan). Cevap `99-ops/tickets/T-464.md` içindedir; başkan onayı bekliyor | `EV-2026-08-10-564` | Gate takibi |
