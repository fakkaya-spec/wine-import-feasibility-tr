# ÇELİŞKİLER — gumruk-vergi-uzmani · TUR 3A (2026-08-10)

---

## KAYNAKLAR ARASI ÇELİŞKİ: **YOK**

Bu turda taranan tüm T1/T2 kaynaklar **birbiriyle tutarlıdır**:

| Kaynak A | Kaynak B | Sonuç |
|---|---|---|
| RG 24/11/2023-32379, 7846 s. CBK tam metni (OCR) | KDVGUT III/C-2.6'daki resmî alıntı | **KELİME KELİME AYNI** — çapraz doğrulama sağlandı |
| KDVK md.29/1-b (kanun) | KDVGUT III/C-1 (tebliğ) | Aynı sonuç |
| KDVK md.30 tahdidi liste | GİB özelgesi 20/08/2011 | Aynı sonuç |
| TUR 1 gözetim araması (`EV-2026-08-09-125`, mevzuat.gov.tr) | TUR 3A gözetim taraması (`EV-2026-08-10-860`, RG) | **Farklı yöntem, aynı sonuç** |

Bu nedenle `C-171 … C-189` bloğundan **hiçbir conflict_id açılmamıştır.**

---

## PROJE İÇİ TUTARSIZLIK (çelişki değil, **düzeltme**) — kayda geçirilir

### D-1 · TUR 1.5'in olasılık değerlendirmesi YANLIŞ ÇIKTI

`EV-2026-08-10-114` ve `T-151` şunu yazıyordu:

> *"Olasılık **DÜŞÜK** değerlendirilmiştir — böyle bir kısıtlama sektörde
> bilinir olurdu ve md.30'un tahdidi listesiyle sistematik olarak çelişirdi."*

**Gerçek:** md.36'ya dayanan bir Cumhurbaşkanı Kararı **vardır** (7846 s.,
yürürlük 2023-11-24) ve md.30'un tahdidi listesiyle **hiç çelişmez** —
çünkü md.30 değil, **md.36 ayrı bir yetki hükmüdür.**

**Ders (yöntemsel):** *"böyle bir şey olsa duyulurdu"* bir kanıt değildir ve
bu projede bir kez daha yanlış çıkmıştır. `EV-2026-08-10-114`'ün `status`
alanı `UNKNOWN` kalır (kanıt kartları immutable'dır) ancak artık
`EV-2026-08-10-852` ile **cevaplanmıştır.**

### D-2 · `finans-fizibilite`'nin %22,7 rakamı FAZLA KÖTÜMSER

`rapor-tur25-finans.md` §9.1 ve `T-947`, kısıt hâlinde `MAX_CIF_TRY`'nin
**%22,7** düşeceğini yazmıştı. Bu **tam kısıt** varsayımıdır.

7846 **kısmi kısıt** getirir (`EV-2026-08-10-854`): yalnız tevsik edilemeyen
artış kısmına isabet eden KDV indirilemez.

**Bu bir çelişki değil, bir varsayım düzeltmesidir** → `T-171` ile
`finans-fizibilite`'ye bildirildi. Rakamın kendisi **onun alanıdır**;
ben yeni bir tavan hesaplamadım.

### D-3 · Ters modelin gözetim uyarı metni ARTIK YANLIŞ

`ters-model-vergi-bacagi.md` §11 ve `vergi.yaml`'daki eski `cikti_kurali`:

> *"gözetim eşiği doğrulanmamıştır; `CIF_TRY_max` bir alt sınırla test
> EDİLMEMİŞTİR"*

**Artık test edilmiştir ve alt sınır YOKTUR.** `vergi.yaml` güncellendi;
`ters-model-vergi-bacagi.md` §11 metni bu turda **değiştirilmemiştir**
(TUR 2.5 belgesidir, tarihsel kayıt olarak durur) — güncel otorite
`vergi.yaml` ve `gozetim-kiymet-kontrolu.md`'dir. Bu ayrım `T-171`'de
açıkça yazılmıştır.
