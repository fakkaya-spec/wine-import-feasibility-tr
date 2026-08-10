# AÇIK SORULAR — global-sourcing-kasifi — TUR 3A

```yaml
ajan:  global-sourcing-kasifi
tur:   TUR 3A — RFQ ZORUNLU TEKNIK ALANLAR
tarih: 2026-08-10
```

> Parça dosyadır. `99-ops/acik-sorular.md` ana dosyasına başkan birleştirir.
> Bu ajan ana dosyaya dokunmadı.

---

## Yeni açık sorular

| # | Ne bilinmiyor | Neden bu turda çözülmedi | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| **OQ-881** | **Zorunlu alan kuralı cevap oranını ne kadar düşürür?** RFQ v2.2 ile SUMMARY SHEET 25 → 27 satıra çıktı ve M5/M6 alt sorularıyla ~15 yeni cevap alanı eklendi. Zorunluluğun **cevap kalitesini artırıp toplam cevabı azaltma** takası ölçülmedi. | Ölçmek için **gerçek gönderim** gerekir; bu turda dış iletişim yasak (`T-467` açık). | **MEDIUM** — model çıktısını değiştirmez, ama TUR 7'nin verimini belirler | ≥8 üreticiye gönderim + **M-doluluk oranı** ölçümü (`rfq-zorunlu-alanlar.md` §4.4). %50'nin altındaysa M1/M5/M7/M8 ikinci aşamaya bırakılır. 2–4 hafta. |
| **OQ-882** | **M2/M3/M4 için kaç tedarikçi cevabı `paketli_sise_hacim_m3` bandını kapatmaya yeter?** Bugün bant üçüncü taraf palet spec sheet'inden geri hesap (0,00223 / 0,00239 / 0,00360). Tek bir tedarikçi cevabı **kendi ürünü için** kesin değer verir — ama **hangi ürünü alacağımız belli olmadan** bandın kapanıp kapanmadığı bir lojistik sorusudur. | `navlun-lojistik-uzmani`'nın alanı; `T-882` ile soruldu. | **MEDIUM** | `T-882` cevabı. |
| **OQ-883** | **Zorunlu alan baskısı yanlış rakam üretir mi?** Boş bırakılamayan alan, tedarikçiyi "bir şey yazmaya" iter. Çapraz tutarlılık kuralı (koli↔şişe↔palet) bunu kısmen yakalar, ama **tek bir tutarlı ama yanlış** paketleme setini yakalayamaz. | Ancak gerçek cevaplar + fiziksel numune/spec sheet karşılaştırmasıyla ölçülebilir. | **MEDIUM** | Numune sevkiyatında (RFQ 7.1–7.5) gelen şişenin **fiilen tartılması ve ölçülmesi**; beyanla karşılaştırma. TUR 7. |
| **OQ-884** | **M6 kabul kriteri fazla mı sıkı?** Bugünkü kural dört koşulu birden arıyor (belge adı + her sevkiyat taahhüdü + dökme bileşen yok + çıkış limanı menşe ülkesinde). Dördü birden gerekli mi, bilinmiyor. | `gumruk-vergi-uzmani`'nın alanı; `T-883` ile soruldu. | **MEDIUM** — fazla sıkıysa model **gereksiz yere aleyhimize** sapar (−%11,765'i hak etmeyen tedarikçilere de uygular) | `T-883` cevabı. |

---

## Bu turda KAPANMAYAN, önceki turlardan devreden ve RFQ'yu doğrudan etkileyen

| # | Soru | Sahibi | Neden RFQ'yu etkiliyor |
|---|---|---|---|
| `T-467` | RFQ gönderimi dış iletişim izni gerektiriyor | `yatirim-komitesi-baskani` | İzin yoksa v2.2 hiç test edilmez; zorunlu alan kuralı **kâğıt üzerinde** kalır |
| `T-871` | Pazarlık çapası hangi basamak / hangi kanal | `yatirim-komitesi-baskani` | `<VOLUME>` doldurulmadan RFQ **geçersizdir** (şablon §0.9) |
| `T-162` | Fatura beyanı değer eşiği `UNKNOWN` | `gumruk-vergi-uzmani` | RFQ 6.13(b) eşiği **rakamsız** soruyor; bağlayıcılığı düşük |
| `T-403` | Türkçe arka etiket menşede mi Türkiye'de mi | `mevzuat-ruhsat-uzmani` | M5'in **neden** sorulduğunun cevabı; kabul kriteri `T-881`'e bağlı |
| `T-206` | Şişelenmiş ithal şarapta zorunlu analiz var mı, parti başı mı | `mevzuat-ruhsat-uzmani` | M7'nin (sertifika seti) parametre listesinin **yeterli olup olmadığı** buna bağlı |
