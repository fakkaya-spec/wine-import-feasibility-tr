# ÇELİŞKİLER — `gumruk-vergi-uzmani` (TUR 2)

> CLAUDE.md §1.13: Kaynaklar çelişirse **sessizce seçim yapılmaz.**
> Çelişki kayda geçirilir ve başkana taşınır.

---

## C-161 — GTS menşe belgesi: **Form A** mı, **REX Menşe Beyanı** mı?

```yaml
conflict_id:        C-161
acan:               gumruk-vergi-uzmani
tarih:              2026-08-10
impact:             LOW
model_girdisi_etkisi: YOK
status:             OPEN
```

| | Kaynak A | Kaynak B |
|---|---|---|
| **Kaynak** | T.C. Ticaret Bakanlığı **Gümrük Rehberi** — "Menşe ispat ve dolaşım belgeleri nelerdir?" ve "Tercihli Ticaret Anlaşmaları" | GGM **BİLGE Sistemi Menşe Kontrol Tablosu**, `EAGZ` / `GYU` / `OTDU` satırları |
| **Tier** | T2 | T3 (belge GGM'nin, host İGMD) |
| **Tarih** | Yayın/yürürlük tarihi **yok** | 14.04.2026 · yürürlük **1/1/2026** |
| **İddia** | GTS kapsamındaki tavizden yararlanmak için **"Form A Menşe Belgesi"** ithalat sırasında gümrük idaresine sunulur | Aranacak belge **"1049 REX Menşe Beyanı"** |
| **evidence_id** | EV-2026-08-10-155 (aynı sayfa), EV-2026-08-10-163 | EV-2026-08-10-161 (aynı tablo) |

### Neden çelişiyor

Muhtemel açıklama: AB'nin GTS'de **Form A'dan REX sistemine geçişi**ne uyum
sağlanmış, Gümrük Rehberi metni **güncellenmemiş**. Ancak bu bir **yorumdur**,
kanıt değildir — bu yüzden çelişki olarak kaydediyorum.

### Neden **çözmüyorum**

Çözüm hiyerarşisinin tarih kuralı (B lehine: 1/1/2026 yürürlük) ile tier kuralı
(A lehine: T2 > T3) **zıt yönü** işaret ediyor. Kendi yorumumla kapatmam
CLAUDE.md §1.13 ihlali olur.

### Neden **modeli bloke etmiyor**

**GTS şarapta hiçbir koşulda uygulanmaz** — üç bağımsız kanıtla
(`EV-2026-08-10-151`, `-153`, `-154`). Dolayısıyla GTS'de hangi belgenin
arandığı sorusunun `mense_tarife_eslemesi` üzerinde **etkisi yoktur.**
`model_girdisi_etkisi: YOK`.

### Ne zaman maddi olur

Kapsam **22.05 (vermut/aromatize)** veya GTS sütunu bulunan başka bir
II sayılı Liste ürününe genişlerse. O durumda hem GTS uygulanabilir hâle gelir
hem bu çelişki maddileşir.

### Ayrıca kayda geçirilen ikincil gözlem

Gümrük Rehberi'nin **hiçbir sayfasında yayın veya güncelleme tarihi
yayımlanmıyor.** Bu, T2 kaynağın **tazeliğinin ölçülemez** olduğu anlamına
gelir. Bu turda Gümrük Rehberi'nden alınan **tüm** kanıtlara `ttl: 180d` ve
`effective_date: -` yazılmıştır. Bu, C-161'in ötesinde **yapısal bir kaynak
zayıflığıdır** ve TUR 1'de `EV-2026-08-09-126` için not edilen sorunun
(revizyon 2018, KDV %18 yazıyordu) aynısıdır.
