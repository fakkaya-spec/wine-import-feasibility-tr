# ÇELİŞKİLER — finans-fizibilite · TUR 2.5

```yaml
ajan:   finans-fizibilite
tur:    TUR 2.5 — REVERSE TARGET MODEL
tarih:  2026-08-10
not:    "99-ops/celiskiler.md DOKUNMA listesindedir ve DEGISTIRILMEMISTIR.
         Bu dosya, baskanin merge edecegi PARCA kayittir."
```

---

## C-851 — `L3` KATMAN TANIMI: AYNI KALEM İKİ FARKLI KATMANDA

```yaml
conflict_id: C-851
acan:        finans-fizibilite
tarih:       2026-08-10
durum:       OPEN
impact:      HIGH        # cift sayim riski dogrudan MAX_CIF'i degistirir
```

| | **Kaynak A** | **Kaynak B** |
|---|---|---|
| Belge | **`CLAUDE.md` §6** (proje anayasası) | **`30-vergi-gumruk/ters-model-vergi-bacagi.md`** §4.3 + R6 + `vergi.yaml → ters_model_vergi_bacagi` |
| Tier | — (iç kural) | — (ajan spesifikasyonu, T1 kanıtlara dayalı) |
| Tarih | TUR 0 | 2026-08-10 |
| Der ki | **L3 PRE-TAX LANDED = CIF + vergi öncesi yurt içi masraflar** | Ordino · antrepo · elleçleme · iç nakliye · **müşavirlik**: hepsi **`L5` kalemidir**, vergi matrahına girmez; `L4_econ_max = L5_max − Σ(L5_kalemleri)` |

### Neden çelişiyor

**Aynı maliyet kalemleri iki farklı katmana yerleştiriliyor.**

- `CLAUDE.md` §6'ya göre bu kalemler **L2 ile L3 arasındadır.**
- Ters model spesifikasyonuna göre **L4 ile L5 arasındadır.**

Zincir tek yönlüdür (`L2 → L3 → L4 → L5`), dolayısıyla **iki tanım aynı anda
uygulanırsa kalem İKİ KEZ düşülür; hiçbiri uygulanmazsa HİÇ düşülmez.**

### Büyüklük

5.000 şişede TR-içi kalemler **3,99 TL/şişe** (LCL BASE) →
`MAX_CIF` üzerindeki etkisi **2,66 TL/şişe**. Çift sayım hâlinde
`MAX_CIF` **5,32 TL** eksik çıkar (799 TL hedefinde **%1,95**).
**Mertebe küçüktür ama yön belirsizdir ve kural düzeyinde bir boşluktur.**

> **Uyarı — mertebe yanıltıcı olabilir:** bu turda **kanal bacağında** benzer
> yapıda bir eksik sayım bulundu ve büyüklüğü **28,95 TL/şişe** çıktı
> (`reverse-price-model.md` §2.2). Katman sınırlarındaki belirsizlikler
> **küçük görünüp büyük çıkabilir**; `C-851` bu nedenle `HIGH` işaretlenmiştir.

### Bu turda ne yapıldı

**Sessiz seçim YAPILMADI.** Model, ters model spesifikasyonunu **esas aldı**
(kalemler `L5`'te bir kez düşüldü) ve `L3`'ü **yalnızca bilgi amaçlı** bir
türev alan olarak raporladı:

```python
l3_pre_tax_landed_max = cif_try_max + (TR_ ile baslayan TRY kalemlerin toplami)
# BU DEGER HICBIR CIKARMA ISLEMINDE KULLANILMAZ.
```

`reverse-price-model.md` §2.2'de **açıkça yazılmıştır.**

### Çözüm için gereken

Başkan kararı: `CLAUDE.md` §6'daki `L3` tanımına bir **niteleme** eklenmesi —
*"L3, vergi matrahına girmeyen yurt içi masrafları içerdiğinde bu kalemler
`L4 → L5` geçişinde İKİNCİ KEZ düşülemez"* — veya ters model
spesifikasyonunun `L3`'ü açıkça **atlayan** bir zincir tanımladığının kayda
geçirilmesi.

---

## C-852 — *"fx OLMADAN CIF_TRY'YE KADAR ÇALIŞIR"* HÜKMÜ FAZLA KESİN

```yaml
conflict_id: C-852
acan:        finans-fizibilite
tarih:       2026-08-10
durum:       OPEN
impact:      HIGH        # ciktinin STATUSUNU degistirir: sayi -> ust sinir
```

| | **Kaynak A** | **Kaynak B** |
|---|---|---|
| Belge | **`90-karar/master-commercial-input-table.md`** §5.3 (+ §7 "en kırılgan hüküm") | **Bu ters model çalıştırması** (TUR 2.5) + `40-lojistik/lojistik-senaryolari-tur25.md` §2.4 |
| Der ki | *"`fx` olmadan bile ters model **`CIF_TRY`'ye kadar** çalışır."* Gerekçe: L8 → KDV → L7 → L6 → L5 → L4 → ÖTV ve bandrol düşülür, geriye `CIF + GV` kalır | **L2 ile L5 arasında USD cinsli kalemler vardır** ve `fx` `null` iken düşülemezler: varış THD (165–298 USD/kont.), devanning (257–475 USD), CFS (30–80 USD/CBM), terminal ardiye (90–300 USD), drop-off (50 USD), LCL varış sabit masrafı (200–500 USD), dokümantasyon (50–100 USD), **müşavirlik CIF kademesi (%0,3)** |

### Neden çelişiyor

§5.3'ün türetmesi **eksiktir**: L5'ten L4'e geçerken düşülmesi gereken
kalemlerin **hepsinin TL cinsinden olduğunu** varsayar. Gerçekte
**varış tarafı masraflarının büyük kısmı USD cinsindendir**
(`EV-2026-08-10-315`…`-319`, `EV-2026-08-09-324`).

**Sonuç:** `fx` olmadan hesaplanabilen şey `CIF_TRY` **değil**,
`CIF_TRY`'nin bir **ÜST SINIRIDIR** — çünkü düşülemeyen tüm kalemler
**pozitiftir** ve sıfır alınmaları tavanı **yükseltir**.

### Büyüklük — `UNKNOWN`, ama alt sınırı verilebilir

5.000 şişelik İspanya LCL BASE senaryosunda USD bacağı **0,450 USD/şişe**
(`lojistik-senaryolari-tur25.md` §4.1) — bunun **bir kısmı** CIF içindedir
(okyanus navlunu), **bir kısmı** varış tarafındadır (CFS, varış sabit
masrafı, dokümantasyon). **Ayrıştırma bu belgede yapılmamıştır** ve
`fx` olmadan **TL karşılığı hesaplanamaz.**

> **Yani çelişkinin büyüklüğü de `fx`'e bağlıdır.** Bu, `T-852`'nin
> (CRITICAL) neden yalnızca bir "birim dönüşümü" olmadığını gösterir.

### Bu turda ne yapıldı

**Sessiz seçim YAPILMADI.** Model:
1. USD/EUR cinsli `L5` kalemlerini **ayrı satırlar** olarak taşıdı,
2. her birini **`0` aldı** ve bunu **her çalıştırmada uyarı olarak bastı**,
3. çıktı alanını **`cif_try_max_UPPER_BOUND`** olarak adlandırdı,
4. `reverse-price-model.md` §3.4'te **iki bağımsız üst-sınır nedenini**
   (λ=1 **ve** sıfır alınan kalemler) ayrı ayrı listeledi.

### Çözüm için gereken

`T-852` (fx) kapanması **yeterlidir** — kur geldiği anda USD kalemleri
düşülebilir ve `cif_try_max_UPPER_BOUND` gerçek bir `cif_try_max`'a döner.
`master-commercial-input-table.md` §5.3'ün hükmü ise **nitelenmeli**:
*"`fx` olmadan ters model `CIF_TRY`'nin bir **ÜST SINIRINA** kadar çalışır."*

---

## BU TURDA ÇÖZÜLMEYEN AMA DEĞİNİLEN MEVCUT ÇELİŞKİLER

| conflict_id | Sahibi | Ters modeldeki etkisi |
|---|---|---|
| `C-311` (FCL bandı 4 kat) | navlun-lojistik | **SIFIR** — navlun CIF'in içindedir, tavanı değiştirmez (`reverse-price-model.md` §8.3) |
| `C-501` (`available` filtresi) | türkiye-pazar | Sweet-spot §2 alıntısının tabanı; **modelin sayılarını değiştirmez** |
| `C-551` (Metro KDV sunumu) | türkiye-pazar | `OBSERVED_BENCHMARK` kullanılmadı → **etkisiz** |
| `C-561` (bantta ürün var, dönmüyor) | türkiye-pazar | `T-857`'nin ikinci bacağı |
| `C-601` (yasal vade 60 vs fiili 70–93 gün) | kanal-marj | `peak_cash` hesaplanmadığı için **bu turda etkisiz**; TUR 3'te belirleyici |
| `C-602` (tekel marjı) | kanal-marj | `T-856`'nın tabanı |
