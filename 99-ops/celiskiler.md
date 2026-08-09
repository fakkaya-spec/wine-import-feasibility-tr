# ÇELİŞKİLER

Format: `C-###`

> **KURAL (CLAUDE.md §1.13): Kaynaklar çelişirse SESSİZCE SEÇİM YAPILMAZ.**
> Çelişki buraya kaydedilir ve `yatirim-komitesi-baskani`'na taşınır.
> Başkan tier, yürürlük tarihi ve kanıt kalitesine bakarak çözer;
> çözemezse çelişki `CONFLICT` olarak karara taşınır.

---

## DURUM: BOŞ

Bu turda (TUR 0) araştırma yapılmadığı için henüz çelişki yoktur.

---

## ÇELİŞKİ KAYIT FORMATI

```yaml
conflict_id:        C-###
acilis_tarihi:      YYYY-MM-DD
acan_ajan:
konu:               # Neyle ilgili celiski

kaynak_a:
  evidence_id:
  iddia:
  value:
  tier:             # T1..T5
  publication_date:
  effective_date:
  source_name:

kaynak_b:
  evidence_id:
  iddia:
  value:
  tier:
  publication_date:
  effective_date:
  source_name:

celiski_turu:       # DEGER | TARIH | TANIM | KAPSAM | KATMAN
etki:               # Bu celiski cozulmezse model nerede kirilir
impact:             # CRITICAL | HIGH | MEDIUM | LOW
durum:              # OPEN | RESOLVED | UNRESOLVABLE
cozum:              # Baskanin gerekcesi
cozum_evidence_id:
cozen:              # yatirim-komitesi-baskani
cozum_tarihi:
```

---

## ÇÖZÜM HİYERARŞİSİ (BAŞKAN İÇİN)

Çelişki çözülürken şu sıra uygulanır:

1. **Tier** — T1 > T2 > T3 > T4 > T5.
   T1'e karşı T5 çelişkisinde T1 kazanır, ama bu **sessizce** değil,
   gerekçeli olarak kaydedilir.
2. **Yürürlük tarihi** — aynı tier'da daha güncel `effective_date` kazanır.
   Dikkat: `publication_date` değil, `effective_date`.
3. **Model hedef tarihi** — hangi değer modelin hedef tarihinde
   yürürlükte olacaksa o kullanılır.
4. **Kapsam uyumu** — kaynaklardan biri farklı bir GTİP/ürün/kanal için
   konuşuyor olabilir. Bu bir çelişki değil, **kapsam farkıdır** —
   `celiski_turu: KAPSAM` olarak işaretlenir.
5. **Katman uyumu** — iki sayı farklı maliyet katmanına (L0–L8) aitse
   bu da çelişki değil, **katman farkıdır** — `celiski_turu: KATMAN`.
   Bu, en sık yapılan sahte-çelişki türüdür; önce bunu ele.
6. Yukarıdakiler çözmezse → ilgili ajana ek doğrulama ticket'ı.
7. Hiçbiri çözmezse → `durum: UNRESOLVABLE`, değer `CONFLICT` statüsünde
   kalır ve modele **girmez**. Karara taşınır.

---

## BEKLENEN ÇELİŞKİ NOKTALARI (ÖNCEDEN İŞARETLENDİ)

Bu noktalarda çelişki çıkması muhtemeldir; ajanlar dikkatli olsun:

| Konu | Neden çelişir | İlgili ajan |
|------|---------------|-------------|
| Maktu ÖTV tutarı | Periyodik güncellenir; farklı tarihli kaynaklar dolaşır | `gumruk-vergi-uzmani` |
| Gümrük vergisi oranı | Ülke grubuna göre değişir; kaynak hangi grubu kastettiğini yazmayabilir | `gumruk-vergi-uzmani` |
| Tercihli tarifenin kapsamı | Gümrük vergisini mi, ÖTV'yi de mi etkiliyor | `gumruk-vergi-uzmani` |
| Navlun | Spot vs kontrat; all-in vs base | `navlun-lojistik-uzmani` |
| Konteyner şişe kapasitesi | Hacim kısıtı mı ağırlık kısıtı mı esas alınmış | `navlun-lojistik-uzmani` |
| Raf fiyatı | Online vs mağaza; promosyonlu vs normal; şehir farkı | `turkiye-pazar-kasifi` |
| Benchmark fiyat statüsü | KDV dahil/hariç, L7/L8 — bkz. OQ-001 | `turkiye-pazar-kasifi` |
| MOQ | Gösterge vs gerçek teklif | `global-sourcing-kasifi` |
| Kanal marjı | Brüt/net, KDV dahil/hariç, margin/markup | `kanal-marj-uzmani` |
| Ruhsat süreleri | Mevzuattaki yasal süre vs pratikte gerçekleşen süre | `mevzuat-ruhsat-uzmani` |
