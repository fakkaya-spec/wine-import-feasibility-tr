# AÇIK SORULAR — finans-fizibilite · TUR 3A
<!-- 99-ops/acik-sorular.md'ye BASKAN tarafindan birlestirilir. Bu dosya bir PART'tir. -->

```yaml
ajan:   finans-fizibilite
tur:    TUR 3A — MODEL AUDIT + ROUND-TRIP ASSERTIONS
tarih:  2026-08-10
not:    "99-ops/acik-sorular.md DOKUNMA listesindedir ve DEGISTIRILMEMISTIR.
         Bu dosya baskanin merge edecegi PARCA kayittir.
         Bu tur YENI ARASTIRMA yapmamistir; asagidaki sorular DENETIMIN
         ortaya cikardigi YAPISAL bosluklardir."
```

| # | Soru | Kime | Neden kritik | Ticket |
|---|---|---|---|---|
| **OQ-F31** | `L7_eff = L6·(1−d) − f` denklemi **ticari gerçekte** böyle mi işliyor? | `kanal-marj-uzmani` / TUR 7 | Bu turda kurulan **30 testin 30'u** bu denklemi test etmez, **onunla test eder**. Denklem yanlışsa testler yanlış bir dünyayı **tutarlı biçimde** doğrular. | `T-862` |
| **OQ-F32** | Aynı ekonomik olayın **iki farklı adla** iki satırda durması nasıl yakalanır? | `kanal-marj-uzmani` | `LEDGER_UNIQUENESS` **isim tabanlıdır**; `K6a` (`d` içindeki lojistik ↔ `L5` TR-içi lojistik) bu denetimden **görünmez geçer** | `T-861` |
| **OQ-F33** | `BLOCKED_INPUT_COUNT` kaç olduğunda çıktı `APPROVED` olabilir? | **başkan** | Bugün 26/29/31; kalemlerin **hepsi tavanı aşağı çeker**; eşik **tanımsız** | `T-864` |
| **OQ-F34** | `kanal.yaml`'daki `f_listeleme_bedeli_sise_basi` alanı **dönem toplamına** çevrilecek mi? | `kanal-marj-uzmani` | Engine artık `f_per_bottle`'ı **girdi olarak reddediyor**; alan doldurulsa bile **okunamaz** | `T-863` |
| **OQ-F35** | md.36 tetiklenirse `D` (tevsik edilemeyen tutar) **nasıl hesaplanır**? | `gumruk-vergi-uzmani` | Koşullu dal kodlandı ve `false`'ta duruyor; tetiklenirse `D` yok → model **`UNKNOWN`** dönecek, sayı **üretemeyecek** | `T-171` (`ANSWERED`) · `T-173` |
| **OQ-F36** | `makro.yaml → finansman_orani` ne zaman dolacak? | **yatırımcı** | `L6_gross` matrahı **kuruldu ve test edildi** (`651,3587` vs `L6 542,7989`) ama finansman satırı `BLOCKED_INPUT`. `K12`: 60 gün → **−27,55 TL/şişe** | `T-614` |
| **OQ-F37** | `μ` matrahı (`L6` / `L7_EFF` / `L5_MARKUP`) hangisi? | **yatırımcı** (`D-03`) | Üçü **kodlandı ve test edildi**; `μ≠0` & matrah `null` → engine **`UNKNOWN`** döner. `μ=%20`'de yayılım **16,89 TL**, `μ=%50`'de **69,96 TL** | `T-616` · `T-851` |
| **OQ-F38** | `peak_cash_requirement` hangi turda hesaplanacak? | **başkan** | Matrah (`L6_gross`) hazır, vade bandı (`kanal.yaml`) hazır, **finansman oranı yok** → sayı üretilmedi. Bu turda bilinçli olarak **yapılmadı**. | `T-614` · `OQ-F36` |

> ### BU TURUN AÇMADIĞI SORULAR (bilerek)
> Contribution margin, break-even, EBITDA, ROI, IRR ve tedarikçi tavsiyesi
> **sorulmadı ve üretilmedi.** Bu bir model bütünlüğü turuydu.
