# AÇIK SORULAR — global-sourcing-kasifi — TUR 1.5

```yaml
ajan:  global-sourcing-kasifi
tur:   TUR 1.5 — BLOCKER REMEDIATION (T-902)
tarih: 2026-08-10
```

> Parça dosyadır. `99-ops/acik-sorular.md` ana dosyasına başkan birleştirir.
> Bu ajan ana dosyaya dokunmadı.

---

## Yeni açık soru

| # | Ne bilinmiyor | Neden bu turda çözülmedi | Kritik mi | Nasıl bulunabilir |
|---|---|---|---|---|
| **OQ-451** | **OIV ihracat birim değeri serisinin gerçek katmanı nedir?** (`tedarikci.yaml → ihracat_ort_birim_degeri_EUR_per_litre`) TUR 1'de L1 (FOB) varsayılmıştı; T-902 ile bu iddia geri çekildi ve katman `UNKNOWN` yapıldı. | TUR 1.5 bir **düzeltme turudur**, araştırma turu değildir; yeni kaynak araması bu turda açıkça yasaklandı. | **MEDIUM** — modele fiyat girdisi olarak girmiyor (çit var), ama ülke sıralamasını kaba düzeyde etkiliyor | OIV'in "export value" tanımının birincil kaynaktan (OIV metodoloji notu) okunması. ~1 gün. |

**Neden CRITICAL değil:** bu seri `SENSITIVITY_BOUNDS_ONLY` çitinin arkasındadır ve
`kullanim_yasagi` bloğu onu L1 girdisi olarak kullanmayı açıkça yasaklar. Katmanı
bilinmese bile model yanlış bir sayı okumaz — sadece bu seriden çıkarım yapamaz.

**Neden LOW da değil:** eğer serinin gerçekten FOB olduğu doğrulanırsa, L1 > L2
tersliği bir etiket sorunu olmaktan çıkıp **veri sorununa** dönüşür ve o zaman ya
Comtrade birim yorumu (bkz. TUR 1 raporu §9.1) ya da OIV türetmesi hatalıdır.
Yani bu soru, iki farklı kaynağın güvenilirliğini test eden bir düğümdür.

---

## TUR 1'den devreden ve bu turda DEĞİŞMEYEN açık sorular

`OQ-401` … `OQ-415` (bkz. `99-ops/_parts/acik-sorular-global-sourcing-kasifi.md`)
**hiçbiri kapanmamıştır.** Özellikle:

- `OQ-401` (gerçek EXW/FOB — **CRITICAL**) — bu turda üreticiye temas yasaktı.
- `OQ-402` (gerçek MOQ yapısı — **CRITICAL**) — aynı.
- `OQ-403` (menşe ispat belgesi — **CRITICAL**) — `T-401`'e bağlı.

**T-902'nin kapanması bu üç kritik UNKNOWN'ı kapatmaz.** Katman etiketinin
düzeltilmesi bir kanıt kalitesi iyileştirmesidir, bir fiyat bulgusu değildir.

---

## Bu turda yeni ÇELİŞKİ (`C-4xx`) açılMAdı — gerekçe

L1 > L2 tersliği ilk bakışta bir `CONFLICT` gibi görünür, ama değildir:

- `CONFLICT` = **iki kaynak aynı iddia hakkında çelişiyor** (CLAUDE.md §1.13).
- Burada OIV ile Comtrade **aynı iddiada bulunmuyor**: biri ülkelerin dünyaya
  ihracatını, diğeri Türkiye'nin ithalatını ölçüyor. Çelişen kaynaklar değil,
  **bu ajanın iki seriye aynı ölçeği atfeden etiketiydi** — ve o etiket geri çekildi.

Terslik yine de kaydedilmiştir: `EV-2026-08-10-401` ve
`tedarikci.yaml → karsilastirilamazlik_kaniti`. Sessizce geçilmemiştir.

**Ne zaman gerçek bir çelişkiye dönüşür:** `OQ-451` cevaplanır ve OIV serisinin
gerçekten FOB olduğu doğrulanırsa. O noktada iki T3 kaynak aynı ölçekte çelişiyor
demektir ve bir `C-` numarası hak eder.
