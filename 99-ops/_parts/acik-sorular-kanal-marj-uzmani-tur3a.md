# AÇIK SORULAR — kanal-marj-uzmani · TUR 3A
<!-- 99-ops/acik-sorular.md'ye BASKAN tarafindan birlestirilir. Bu dosya bir PART'tir. -->

> TUR 3A **sınırlı bir denetim turudur** — yeni araştırma yapılmamıştır.
> Aşağıdaki sorular yeni bulgular değil, **denetimin ortaya çıkardığı
> yapısal boşluklardır.**

| # | Soru | Kime | Neden kritik | Ticket |
|---|---|---|---|---|
| **OQ-611** | `f` ve `d` hizmet faturalarındaki KDV **indirilebilir mi**? Ciro primi KDV'de iskonto mu hizmet mi? | `gumruk-vergi-uzmani` | İndirilemezse `f`+`d`'nin ekonomik maliyeti **1,20 katı** | `T-611` |
| **OQ-612** | HoReCa **menü fiyatındaki** KDV oranı, ürün KDV oranıyla aynı mı? | `gumruk-vergi-uzmani` | `reverse-price-model.md` §3.2'nin **15 HoReCa hücresinin 15'i** bu doğrulanmamış orandan geçiyor | `T-612` |
| **OQ-613** | `d` sepetinin kaç puanı gerçekten **oransal**, kaç puanı **sabit TL**? | TUR 7 (kanal görüşmesi) | Hacim plandan saparsa tek-`d` temsili gerçek yükü **göremiyor** | `T-613` |
| **OQ-614** | Ciro primi **kademeli (tiered)** mi? | TUR 7 | Kademeliyse `d` hacme bağlıdır, sabit oran olarak taşınamaz | `T-613` |
| **OQ-615** | `f`'nin birimi **SKU × zincir** mi, **SKU × mağaza** mı? | TUR 7 | Mağaza bazlıysa `f_per_bottle` bir mertebe büyür (`B-9`) | `T-604` |
| **OQ-616** | **CRM/B2B "kasa çıkışı cirosu"** kaleminin matrahı `L6` mı `L8` mi? | TUR 7 | `L8 > L6` → `L6` matrahıyla yazmak **sistematik eksik sayım** | `T-613` |
| **OQ-617** | İade edilen şişenin **geri kazanılabilir değeri** nedir (0 mı, `L5` mi)? | TUR 7 | İadenin bedeli `L6 − geri_kazanım`; şu an `0` alınıyor | `T-615` |
| **OQ-618** | `EV-2026-08-10-329`'un TR-içi lojistiği **hangi teslim noktasına** kadar? | `navlun-lojistik-uzmani` | Zincirin lojistik bedeliyle **çift/eksik sayım** riski | `T-618` |
| **OQ-619** | Dış distribütör, zincir bedellerini (`d`, `f`) **üstlenir mi**? | TUR 7 / **başkan** | `A1` mi `A2` mi — 28,95 TL/şişe fark | `T-617` · `C-611` |
| **OQ-620** | Yatırımcı `μ`'yü **hangi matrahtan** tanımlıyor? | **yatırımcı** (`D-03`) | Matrahsız `μ` yüzdesi **anlamsızdır**; fark `μ=%30`'da 31,73 TL | `T-616` |
| **OQ-621** | Tekel bayii marjı **margin / iskonto / markup** hangisi olarak konuşuluyor? | TUR 7 | `C-602`'nin matrah boyutu; +12,19 TL fark | `C-602` |
| **OQ-622** | **Kanal karması** (zincir / tekel / HoReCa ciro payları) nedir? | `turkiye-pazar-kasifi` / TUR 7 | Üç alan da `null`; birleşik tavan **hesaplanamaz**; tavan 3,5 kat oynayabilir | `T-603` · `K9c` |
