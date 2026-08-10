# ÇAPRAZ İPUÇLARI — global-sourcing-kasifi · TUR 2.5

```yaml
ajan:   global-sourcing-kasifi
tur:    TUR 2.5 — RFQ NEGOTIATION CARDS
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md bu turda DOKUNULMAZ listesindedir.
         Bulgular CLAUDE.md §11 geregi silinmemis, bu _parts dosyasina
         birakilmistir. Birlestirme karari baskanindir."
kaynak: 50-sourcing/rfq-negotiation-cards.md
```

> Bunlar **sonuç değildir, ipucudur.** Hiçbiri kendi alanımda üretilmiş bir
> karar değildir; kartlar yazılırken karşıma çıkan ve **başka ajanların
> alanına ait** gözlemlerdir.

| # | Hedef ajan | İpucu | Neden önemli | Ticket |
|---|---|---|---|---|
| **İP-871** | `gumruk-vergi-uzmani` | **OD-5 — koşullu fiyat düzeltme maddesi.** Menşe belgesi düşerse tarife farkının tedarikçiye rücu edilmesi sözleşmeye yazılabilir mi; sonradan ibraz / sonradan kontrol / geri ödeme yolları açık mı? | Açıksa OD-5 bir **nakit akışı** maddesine iner; kapalıysa pazarlıktaki **en değerli tek madde** olur (**32,10 TRY/şişe**) | `T-872` |
| **İP-872** | `gumruk-vergi-uzmani` | **Karışık menşeli tek konteyner.** Purcari grubu MD + RO + BG'yi tek sevkiyatta birleştirebilirse **tek konteynerde iki tarife oranı** doğar. Tek beyanname mi, iki mi? | Kart 10 soru #3'ün cevabı **ham hâliyle** iletilecek; ben yorumlamıyorum | `T-873` (yan) |
| **İP-873** | `gumruk-vergi-uzmani` | **Ödeme vadesi tedarikçiden tedarikçiye pazarlık konusudur.** 10 kartın 9'unda ödeme şartı `UNKNOWN`; tek gözlem (Harland) **%50+%50, tamamı sevkiyat öncesi**. Kartlar **hem peşin hem vadeli için ayrı fiyat** istiyor. | Modelin `KKDF = 0` varsayımı **n=1 gözleme** dayanıyor (`EV-2026-08-10-452`). Vadeli seçenek fiyat avantajı getirirse **KKDF matrahı devreye girer** | — |
| **İP-874** | `navlun-lojistik-uzmani` | **Purcari MD/RO/BG için ayrı navlun gerekiyor.** Moldova **denize kıyısı olmayan** bir menşedir; RO/BG rotası MD'den **32,10 TRY/şişe'den pahalıysa menşe değiştirme kazancı negatife döner.** | Havuzdaki **tek menşe değiştirme kaldıracının** net değeri buna bağlı | `T-873` |
| **İP-875** | `navlun-lojistik-uzmani` | **Şili — konsolidasyon tercihi düşürür.** Corta Hojas için LCL/konsolidasyon doğal rotası Rotterdam/Antwerp'tir; çıkış ülkesi Şili olmazsa **%50 → %70**. 5.000 şişelik pilotta ucuz görünen rota **20 puanlık tarifeyi yakabilir.** | `T-163` / `T-914` zaten açık — kart bunu **tedarikçi taahhüdüne** çevirdi (OD ŞİLİ EKİ) | `T-914` |
| **İP-876** | `navlun-lojistik-uzmani` | **Cantina Danese (Veneto) navlunu LCL ve FCL'de `UNKNOWN`.** Türkiye'nin **en güçlü ithalat hattı** (İtalya, 5,75 m lt/2025) üzerinde tek fiyat verisi yok. | Kart 2 en güçlü hat + bilinen MOQ birleşimi; navlun bacağı boş | `T-916` |
| **İP-877** | `kanal-marj-uzmani` | **Model A'da marka sahibi ithalatçıya yeniden satış fiyatı tavanı / markup sınırı dayatabilir.** Kart 6, 7, 8, 9'da bu doğrudan soruluyor. | Bu, kanal marjını **modelden değil, tedarikçi sözleşmesinden** kısıtlayan tek mekanizmadır — `dis_distributor.marj_pct` `null` iken (`T-604`) ikinci bir kısıt katmanı doğar | — |
| **İP-878** | `kanal-marj-uzmani` | **Model A'da pazarlama katkısı / listeleme desteği** tedarikçiden gelebilir. Kart 7 ve 8 bunu soruyor. | Gelirse `f` (listeleme bedeli, şu an `0` alınmış, `T-604`) **kısmen tedarikçiye kayar** ve tavan yukarı açılır | — |
| **İP-879** | `mevzuat-ruhsat-uzmani` | **Interbrosa'ya "Türkçe arka etiketi kendi tesisinizde uygulayabiliyor musunuz" soruluyor** (Kart 3, soru #3). Cevap "evet" ise Türkiye'deki etiketleme operasyonu **tamamen kalkar**. | `L5` içindeki bandrolleme/etiketleme operasyon maliyeti modelde **`0` alınmış** (`T-314`) — menşede etiketleme bunu **yapısal olarak** çözer | — |
| **İP-880** | `mevzuat-ruhsat-uzmani` | **Cantina Danese kendi gümrük antreposunu işletiyor** (`EV-2026-08-10-453`). Bandrol/ÜİS veya Türkçe etiketleme menşede yapılabiliyorsa, antrepo işleten tedarikçi bunu **operasyonel olarak kaldırabilir**. | TUR 2'de `İP-459` olarak bırakılmıştı; kartta **OD-3 riskiyle birlikte** yeniden doğdu — aynı antrepo **menşe karışması riski** de taşır | — |
| **İP-881** | `turkiye-pazar-kasifi` | **Danese'nin Türkiye'deki `Midas` ilişkisi canlı mı?** Ürün (`Danese Primitivo Puglia Black Label`, 1.419 TL) **stokta değil**. | Kart 2'nin münhasırlık riskinin **büyüklüğü** buna bağlı; "listelenmiş ama stokta yok" ile "aktif distribütör" **aynı şey değildir** | `T-565` |
| **İP-882** | `turkiye-pazar-kasifi` | **Porta 6 ve Mucho Más gibi küresel value markaların Türkiye'de bulunma ihtimali `presence UNKNOWN`'dır** — `T-464` cevabı tek kanaldan verilmiştir ve ajan bunu kendisi uyarmıştır. | Kart 8 (Vidigal) ve Model A tarafının tamamı bu statüye bağlı; **fiziksel mağaza turu** (`OQ-502`/`OQ-552`) yapılırsa bu 7 marka listeye eklenmeli | `T-464` |
| **İP-883** | `finans-fizibilite` | **`IMPLIED_BREAKEVEN_USDTRY` sıralaması AU/ZA/AR için kullanılamaz** (`TEMSİLİ DEĞİL`, hacim <100 bin lt). Kart 1 (Harland/AU) bu nedenle **sıralama değeri taşımıyor.** | Ülke sıralaması yalnızca **ES · MD · CL · PT · IT · FR** için okunabilir; kartlar bunu yazıyor | — |
| **İP-884** | `finans-fizibilite` | **RO/BG için gözlenen CIF birim değeri bu projede hiç kullanılmadı** → Purcari'nin RO/BG kolunda `IMPLIED_BREAKEVEN` **`UNKNOWN`**. | Menşe değiştirme kaldıracının (+32,10 TRY/şişe) **karşı tarafı ölçülemiyor**; bu turda **yeni araştırma yasak olduğu için açılmadı** | — |
