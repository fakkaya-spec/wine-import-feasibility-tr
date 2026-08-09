# ÇAPRAZ İPUÇLARI

> **KURAL (CLAUDE.md §1.10–1.11):**
> Her ajan **yalnızca kendi görev alanında sonuç üretir.**
> Alan dışı bulgular **silinmez** — buraya bırakılır.
>
> Buraya yazılan şey **SONUÇ DEĞİLDİR, İPUCUDUR.**
> Hedef ajan bunu bir veri olarak değil, bir **araştırma yönlendirmesi**
> olarak kullanır ve kendi kaynaklarıyla doğrular.
>
> Buradaki bir ipucu **modele giremez.** Modele girmek için hedef ajan
> tarafından doğrulanıp kendi alanında kanıt kartına bağlanması gerekir.

---

## DURUM: BOŞ

Bu turda (TUR 0) araştırma yapılmadığı için henüz ipucu yoktur.

---

## KAYIT FORMATI

```yaml
ipucu_id:        IP-###
tarih:           YYYY-MM-DD
birakan_ajan:
hedef_ajan:
konu:
ipucu:           # Ne gordun (SONUC DEGIL)
nerede_gordun:   # URL / kaynak / baglam
neden_onemli:    # Hedef ajan icin neden anlamli
durum:           # NEW | SEEN | INVESTIGATED | DISMISSED
hedef_ajan_notu: # Hedef ajan inceledikten sonra doldurur
```

---

## ÖNCEDEN AÇILMIŞ İPUÇLARI (TUR 0 — KURULUM)

Bunlar araştırma bulgusu değil, **kurulum sırasında öngörülen** çapraz
bağımlılıklardır. Ajanlar TUR 1'e başlarken bunları bilerek başlasın.

```yaml
ipucu_id:        IP-001
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      gumruk-vergi-uzmani
konu:            Odeme sekli -> KKDF
ipucu: >
  tedarikci.yaml/odeme.odeme_sekli alani global-sourcing-kasifi tarafindan
  doldurulacak. Vadeli odeme / akreditif KKDF dogurabilir.
neden_onemli:    KKDF matrahi ve dogus kosulu odeme seklinden bagimsiz degildir.
durum:           NEW
```

```yaml
ipucu_id:        IP-002
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      gumruk-vergi-uzmani
konu:            Mense ispat belgesi -> tercihli tarife
ipucu: >
  tedarikci.yaml/belgeler.mense_ispat_belgesi alani global-sourcing-kasifi
  tarafindan doldurulacak (EUR.1 / fatura beyani / REX / yok).
neden_onemli: >
  Tedarikci belge veremiyorsa tercihli tarife kullanilamaz ve ulke secimi
  ekonomisi degisir.
durum:           NEW
```

```yaml
ipucu_id:        IP-003
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      navlun-lojistik-uzmani
konu:            Koli/palet olculeri -> konteyner hesabi
ipucu: >
  urun.yaml/ambalaj ve tedarikci teklifleri koli/palet olcu ve agirliklarini
  icerecek. Konteyner kapasitesi bu verilerden hesaplanir.
neden_onemli: >
  Sarapta genellikle AGIRLIK kisiti hacim kisitindan once baglayici olur —
  ama bu VARSAYILMAZ, hesaplanir.
durum:           NEW
```

```yaml
ipucu_id:        IP-004
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      navlun-lojistik-uzmani
konu:            Ruhsat/analiz gecikmesi -> demurrage
ipucu: >
  mevzuat-ruhsat-uzmani'nin T0 takvimi ve analiz sureleri, konteynerin
  limanda/antrepoda bekleme suresini belirler.
neden_onemli:    Free time asilirsa demurrage/detention maliyeti dogar.
durum:           NEW
```

```yaml
ipucu_id:        IP-005
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      finans-fizibilite
konu:            Antrepo kismi cekis -> peak cash
ipucu: >
  vergi.yaml/antrepo_rejimi.kismi_cekis_mumkun_mu alani gumruk-vergi-uzmani
  tarafindan doldurulacak.
neden_onemli: >
  Kismi cekis mumkunse vergiler parti parti odenir ve peak_cash_requirement
  DRAMATIK olcude duser. Bu tek alan pilot fizibilitesini degistirebilir.
durum:           NEW
```

```yaml
ipucu_id:        IP-006
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      kanal-marj-uzmani
konu:            Reklam yasagi -> marka insa maliyeti
ipucu: >
  ruhsat.yaml/satis_dagitim_reklam_kisitlari alanlari mevzuat-ruhsat-uzmani
  tarafindan doldurulacak.
neden_onemli: >
  Reklam yapilamiyorsa marka bilinirligi yalnizca raf ve kanal uzerinden
  kurulur. Bu, listeleme/gondol/kampanya maliyetlerini ve private label
  modelinin makuliyetini dogrudan etkiler.
durum:           NEW
```

```yaml
ipucu_id:        IP-007
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      gumruk-vergi-uzmani, mevzuat-ruhsat-uzmani, navlun-lojistik-uzmani
konu:            Bulk sarap hipotezi
ipucu: >
  50-sourcing/ulke-karsilastirma.md §4'te bir ARASTIRMA HIPOTEZI kayitli:
  dokme sarap ithal edip Turkiye'de siselemek.
neden_onemli: >
  Bu hipotez 00-charter/kapsam.md uyarinca KAPSAM DISIDIR ve BU PROJEDE
  COZULMEZ. Yalnizca ilerideki bir calisma icin isaretlenmistir.
  Ajanlar bu konuda arastirma YAPMAZ; yalnizca yolda tesadufen bir bilgi
  gorurlerse buraya not birakirlar.
durum:           NEW
```

```yaml
ipucu_id:        IP-008
tarih:           2026-08-09
birakan_ajan:    TUR 0 kurulum
hedef_ajan:      turkiye-pazar-kasifi
konu:            Etiket zorunluluklari -> raf gozleminde ipucu
ipucu: >
  Turkce arka etiketlerde ithalatci firma adi zorunlu olabilir.
neden_onemli: >
  Raf gozleminde etiket fotografi cekilirken ARKA etiket de cekilirse,
  hangi ithalatcinin hangi markayi getirdigi dogrudan tespit edilebilir.
  Bu, "mevcut ithalatci/distributorler" gorevini kanitli hale getirir.
durum:           NEW
```
