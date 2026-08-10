# AÇIK SORULAR — navlun-lojistik-uzmani · TUR 2.5

```yaml
ajan:   navlun-lojistik-uzmani
tur:    TUR 2.5
tarih:  2026-08-10
not:    "99-ops/acik-sorular.md bu turda DOKUNMA listesindedir."
```

> Bu turda **yeni araştırma yapılmadı**; aşağıdakiler TUR 2'nin açık
> sorularının **daralmış / keskinleşmiş** hâlidir. Yeni soru numaraları
> yalnızca bu dosya içindedir.

| # | Soru | Neden bu turda cevaplanamadı | Kritiklik | Bağlı ticket |
|---|---|---|---|---|
| **OQ-2501** | LCL kotasyonundaki fiyat **CFS'i içeriyor mu?** | Kotasyon metni "hariç" diyor ama tutar vermiyor; forwarder'a sorulmadan bilinemez (dış temas yasak) | **HIGH** — LCL BASE'imi ±%15 kaydırır | `T-304` |
| **OQ-2502** | FCL kotasyonu **hangi kanaldan** alınabilir? Marketplace'ler Türkiye varışını hiç fiyatlamıyor | 14 lane test edildi, 0 sonuç (`EV-2026-08-10-312`); yeni tarama bu turda yasaktı | **CRITICAL** | `T-304` |
| **OQ-2503** | LCL birim fiyatı 50+ CBM'de **kademeli olarak düşüyor mu?** | 5 CBM kotasyonu doğrusal uzatıldı; kademe yapısı bilinmiyor | HIGH — §5.1 üst sınır iddiasının dayanağı | `T-802` |
| **OQ-2504** | 25.000+ şişede LCL **iç nakliyesi** gerçekte kaça mal olur? | Senaryoda "küçük araç" (5.000–10.000 TL) varsayımı kullanıldı; büyük hacimde tam kamyona yakınsaması beklenir → **LCL TRY bacağım bu hacimlerde İYİMSER** | MEDIUM | `T-304` |
| **OQ-2505** | Bir sevkiyattaki çoklu konteyner **tek beyannamede** birleşiyor mu? | Tarifede İTH-14 ("ek konteyner") kalemi var, bu birleşmeyi ima ediyor ama teyit edilmedi | MEDIUM — 8 konteynerde 6.020×8 mi 6.020+7×1.350 mi (fark ~33.000 TL) | `T-304` |
| **OQ-2506** | 2026-08-16'dan sonra aynı kaynak **aynı fiyatları** verecek mi? | Yeniden doğrulama bu turda yapılmadı (görev tanımı gereği) | **HIGH** | `T-802` |
