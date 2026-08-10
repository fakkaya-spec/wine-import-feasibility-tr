# ÇAPRAZ İPUÇLARI — global-sourcing-kasifi · TUR 3A

```yaml
ajan:   global-sourcing-kasifi
tur:    TUR 3A — RFQ ZORUNLU TEKNIK ALANLAR
tarih:  2026-08-10
not:    "99-ops/capraz-ipuclari.md bu turda DOKUNULMAZ listesindedir.
         Bulgular CLAUDE.md §11 geregi silinmemis, bu _parts dosyasina
         birakilmistir. Birlestirme karari baskanindir."
kaynak: 50-sourcing/rfq-zorunlu-alanlar.md, 50-sourcing/rfq-template.md v2.2
```

> Bunlar **sonuç değildir, ipucudur.** Hiçbiri kendi alanımda üretilmiş bir
> karar değildir; zorunlu alanların kabul kriterleri yazılırken karşıma çıkan
> ve **başka ajanların alanına ait** gözlemlerdir.

| # | Hedef ajan | İpucu | Neden önemli | Ticket |
|---|---|---|---|---|
| **İP-881** | `mevzuat-ruhsat-uzmani` | **RFQ artık üreticiden fiziksel etiket taahhüdü istiyor:** ≥18 cm² basılabilir alan, bandrol için boş alan (mm×mm + konum), ABV ≥3 mm karakter. Üçü de **sizin bulgunuz**, benim değil. RFQ'ya rakam yazıldığı anda o rakam **spesifikasyon** hâline gelir. | Yanlış/eksik ölçü sorulursa üretici "evet" der, mal gelir, etiket yetmez — kalem **antrepodayken** geri döner | `T-881` |
| **İP-882** | `mevzuat-ruhsat-uzmani` | **Bandrol Türkiye'de antrepoda uygulanıyor, ama fiziksel alanı menşede basılan etiket belirliyor.** Bu, `lojistik.yaml → bandrolleme_operasyonu` bloğunun **ölçülmemiş bir ön koşulu** olduğu anlamına geliyor: alan yoksa operasyon yapılamaz, maliyet hesabı da anlamsız olur. | Bandrolleme maliyeti bugün alanın **var olduğu varsayımıyla** hesaplanıyor | `T-881` |
| **İP-883** | `navlun-lojistik-uzmani` | **Zorunlu alan baskısı uydurma rakamı teşvik edebilir.** "Boş bırakılamaz" alan, tedarikçiyi *bir şey yazmaya* iter. Bu nedenle RFQ'ya bir **çapraz tutarlılık kuralı** yazdım: (dolu şişe × şişe/koli) + ambalaj ≈ koli brüt; (koli brüt × koli/palet) + palet ≈ yüklü palet brüt. **Tutmuyorsa sayı kullanılmıyor.** | Bu, gelen paketleme verisinin **tek doğrulama mekanizmasıdır** — üçüncü taraf kaynağımız yok | `T-882` |
| **İP-884** | `navlun-lojistik-uzmani` | **2.12 (yaz yükleme / thermal liner / reefer) zorunlu alan YAPILMADI.** `T-302`'nin 13. maddesiydi. Zorunlu alan sayısını kendi başıma artırmadım çünkü her ek zorunlu alan cevap oranını düşürüyor. `lojistik.yaml → sicaklik_riski` bunu gerektiriyorsa **siz söylerseniz** zorunluya çekilir. | Sıcaklık riski modelde ayrı bir blok; girdisi RFQ'dan gelmeli | `T-882` |
| **İP-885** | `gumruk-vergi-uzmani` | **`T-162` (fatura beyanı değer eşiği) `UNKNOWN` olduğu için RFQ 6.13(b) eşiği rakamsız soruyor.** Eşik bilinirse soru *"X EUR'yu aşan sevkiyatlarda EUR.1 düzenler misiniz"* hâline gelir ve **bağlayıcı** olur. Şu hâliyle üretici "duruma göre" diyebilir. | RFQ'nun bağlayıcılığı doğrudan sizdeki bir `UNKNOWN`'a bağlı | `T-883` |
| **İP-886** | `gumruk-vergi-uzmani` | **OD-4 (çıkış ülkesi) her menşeye aynı sorulmuyor olabilir.** Şili için kısıt netti (yalnızca Şili, çapraz kümülasyon yok). **AB menşeleri için aynı kesinlik var mı?** RFQ şu an herkese aynı soruyu soruyor — ayrım varsa soru menşe grubuna göre farklılaşmalı. | Aynı soruyu herkese sormak zararsız görünüyor ama **yanlış yerde konsolidasyona izin vermek** −%11,765'tir | `T-883` |
| **İP-887** | `finans-fizibilite` | **RFQ'da M6 cevapsızlığı `DOC_FAIL` cezalı değerlendiriliyor — bu bir modelleme kuralıdır.** Yani cevap gelmeyen tedarikçi için tavan otomatik olarak **256,34** (Y, N grubu) okunuyor, **290,51** değil. Bu kuralı modele taşırken `status` etiketinin `ASSUMPTION` olması gerekir, `FACT` değil. | Ceza kuralı modelin **aleyhimize** sapmasını sağlıyor — doğru yön, ama etiketi doğru olmalı | — |
| **İP-888** | `finans-fizibilite` | **M2/M3/M4 gelmezse alternatif "bant ile devam" seçeneği var (T-884 seçenek B).** O senaryoda `paketli_sise_hacim_m3` **%38 belirsizlikle** modele girer. **Bu belirsizliği kabul edip etmeyeceğiniz sizin kararınız** — ben yalnızca seçeneği görünür kıldım. | Başkanın `T-884` kararı sizin kabul sınırınıza bağlı olabilir | `T-884` |
| **İP-889** | `seytanin-avukati` | **Zorunlu alan listesi bir "cevap oranı" bahsidir ve ölçülmemiştir.** RFQ v2.2 ile SUMMARY SHEET 25 → 27 satır, M5/M6 alt sorularıyla ~15 yeni cevap alanı. `rfq-alan-kontrolu.md` §5.1 zaten uyarmıştı: uzun RFQ = daha az cevap. **Bu turda bu riski azaltmadım, artırdım.** | En temiz kırmızı takım hedefi: şablonu tedarikçi gibi doldurup **hangi zorunlu alanın kaçamak cevapla geçilebildiğini** göstermek | — |
| **İP-890** | `turkiye-pazar-kasifi` | **M8 (Türkiye ihracat geçmişi) dışarıdan öğrenilemiyor — `T-464` cevabınız bunu kanıtladı ("bulunamadı ≠ yok").** Bu yüzden alan zorunlu yapıldı ama **eleme kuralı uygulanmadı**: sayısal model girdisi beslemiyor. Eğer ileride kanal tarafında bir "ithal marka geçmişi" izi bulursanız, o iz M8'in **bağımsız doğrulaması** olur. | Tedarikçi beyanının tek dış kontrolü sizin kanal taramanız | — |
