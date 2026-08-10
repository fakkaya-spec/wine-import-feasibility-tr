# ÇAPRAZ İPUÇLARI — `turkiye-pazar-kasifi` / TUR 1.5

> `99-ops/capraz-ipuclari.md`'ye **merge edilmek üzere** hazırlanmıştır.
> Ana dosyaya bu ajan tarafından DOKUNULMAMIŞTIR.
> **Bunlar SONUÇ DEĞİL, İPUCUDUR.** Bu tur dar kapsamlıydı; liste kısadır.

| # | Hedef ajan | İpucu | evidence_id | Neden önemli |
|---|---|---|---|---|
| İP-551 | `kanal-marj-uzmani` | Metro'nun **2010 şarap kataloğunda** fiyatlar KDV hariç + KDV'li **çiftli** basılıydı ve KDV hariç sayı ondalıklı (131,36), KDV'li sayı yuvarlaktı (155,00) | `EV-2026-08-10-503` | Metro'nun şarap kategorisinde **brüt fiyattan geriye** çalıştığını (net değil) gösterir. Pazarlıkta hangi matrahtan konuşulduğu belirsizse marj hesabı kayar. |
| İP-552 | `kanal-marj-uzmani` | Metro'nun tarihsel şarap fiyatları **dönemseldir**: *"fiyatlar &lt;tarih aralığı&gt; arasında geçerlidir ve stoklarla sınırlıdır"* | `EV-2026-08-10-503` | Şarapta Metro'nun "kalıcı raf fiyatı" verip vermediği belirsiz. Listeleme/vade pazarlığında fiyat taahhüdünün süresi sorulmalı. |
| İP-553 | `mevzuat-ruhsat-uzmani` | Metro Türkiye 2013'e kadar **basılı şarap katalogu** yayınlıyordu; 2026'da hiçbir yayınında alkol yok | `EV-2026-08-10-503`, `EV-2026-08-09-514` | Reklam yasağının **fiili başlangıcını** ve kapsamının pratikte nereye oturduğunu gösteren somut bir "önce/sonra" karşılaştırması. *(Yasağın kapsamı bu turda YENİDEN ARAŞTIRILMAMIŞTIR — kabul edilmiş iş kısıtıdır.)* |
| İP-554 | `global-sourcing-kasifi` | Metro'nun 2008–2010 ithal şarap assortmanında **ABD ve Avustralya menşe zaten vardı** (Terra California Zinfandel, Sunset Creek California, Yellow Tail Shiraz, Huntington Chardonnay, Gallo) | `EV-2026-08-10-503` | Metro'nun bu iki menşede **15+ yıllık bir listeleme geçmişi** var. `EV-2026-08-09-509`'daki "uzman kanalda ABD/Avustralya YOK" bulgusuyla birlikte okunduğunda: bu menşeler Türkiye'de **uzman kanalın değil, cash&carry/market kanalının** menşeleridir. Kanal seçimi ile menşe seçimi bağımsız değildir. |
| İP-555 | `yatirim-komitesi-baskani` | `10-evidence/index.csv`'de `EV-2026-08-09-509` / `-510` satırlarının `status` alanı hâlâ `FACT`; raw kartlar `SUPERSEDED` yapıldı | — | Bu ajan `index.csv`'ye dokunmakla yetkili değil. Merge sırasında düzeltilmezse index ile kartlar desenkron kalır. |
| İP-556 | `finans-fizibilite` | `pazar.yaml` içindeki `katman_kurallari.K4`: bu dosyadan **marj türetilemez**; Metro 599,90 ile uzman perakende 875 TL farkı **kasten hesaplanmamıştır** | `pazar.yaml` | İki sayı farklı **kanal** ve farklı **katman** etiketlidir (`L8_METRO_CASH_CARRY` vs `L8_ONLINE_UZMAN_PERAKENDE`). Aradaki %46 fark bir marj **değil**, bilinmeyen bir karışımdır. |
