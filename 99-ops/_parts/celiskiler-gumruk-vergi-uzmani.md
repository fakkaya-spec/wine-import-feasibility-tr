# ÇELİŞKİLER — gumruk-vergi-uzmani (TUR 1, 2026-08-09)

> CLAUDE.md §1.13: Kaynaklar çelişirse **sessizce seçim yapılmaz.**
> Aşağıdaki çelişki başkana taşınmıştır.

---

## C-101 — Şarapta asgari maktu ÖTV tutarı: 61,3914 TL/lt mi, 71,2692 TL/lt mi?

| Alan | Değer |
|------|-------|
| conflict_id | **C-101** |
| Açan | `gumruk-vergi-uzmani` |
| Açılış | 2026-08-09 |
| Durum | **OPEN — çözüm önerisi sunuldu, başkan onayı bekleniyor** |
| Etkilenen model girdisi | `80-model/inputs/vergi.yaml` → `matrah_sirasi[OTV].asgari_maktu_tutar` |
| Etki | **CRITICAL** — projenin tek en kritik sayısı |

### Kaynak A
- **Kaynak:** T.C. Cumhurbaşkanlığı Mevzuat Bilgi Sistemi — 4760 sayılı ÖTV
  Kanunu **konsolide metin**, ekli (III) sayılı liste, 22.04 satırı
- **Tier:** T1
- **Erişim:** 2026-08-09 · `https://www.mevzuat.gov.tr/mevzuatmetin/1.5.4760.pdf`
- **Değer:** **61,3914 TL/litre**
- **Dipnot 58:** Tutar, 31/12/2025 tarihli ve 10799 sayılı Cumhurbaşkanı Kararı
  ile yayımı tarihinde yürürlüğe girmek üzere metne işlenmiştir; aynı Karar ile
  ÖTVK 12/3'ün **2026 Ocak–Haziran** dönemi için uygulanmayacağı hükme bağlanmıştır.
- **evidence_id:** EV-2026-08-09-112

### Kaynak B
- **Kaynak:** Gelir İdaresi Başkanlığı — "(III) SAYILI LİSTE — 4760 sayılı ÖTV
  Kanununun (12/3) maddesi uyarınca güncellenen liste — **Yürürlük: 3/7/2026**"
- **Tier:** T2 (dayanağı T1: ÖTVK md.12/3 otomatik yeniden belirleme)
- **Erişim:** 2026-08-09 · GİB CDN
- **Değer:** **71,2692 TL/litre**
- **evidence_id:** EV-2026-08-09-111

### Neden çelişiyor (görünüşte)
İki resmî kaynak aynı GTİP için farklı tutar gösteriyor. Naif bir okuyucu
mevzuat.gov.tr'yi (T1) esas alıp 61,3914 kullanır ve **şişe başına ~7,4 TL**
eksik ÖTV hesaplar.

### Önerilen çözüm (başkan onayına)
Çelişki **gerçek değil, mekanizma kaynaklıdır**:

1. ÖTVK md.12/3 (EV-2026-08-09-114) uyarınca (III) sayılı listedeki asgari maktu
   tutarlar Ocak ve Temmuz'da Yİ-ÜFE değişimi oranında **"yeniden belirlenmiş
   sayılır"** — yani ayrı bir Cumhurbaşkanı Kararı olmadan kendiliğinden değişir.
2. Kendiliğinden değişen tutarlar kanun metnine **işlenmez** (işlenecek bir
   düzenleme yoktur), bu yüzden mevzuat.gov.tr konsolide metni son CBK tutarını
   göstermeye devam eder.
3. CBK 10799'un 12/3'ü askıya alması yalnızca **2026 Ocak–Haziran** dönemi
   içindi. Temmuz 2026 için askıya alma yapılmamıştır — 3/7/2026 tarihli CBK
   11489 yalnızca **(III) sayılı listenin (B) cetveli** (tütün) mallarına ilişkin
   olup 12/3'ü **onlar için** Temmuz–Aralık 2026 döneminde askıya almıştır
   (kanun metni dipnot 60). Şarap (A cetveli) askı kapsamında **değildir**.
4. Dolayısıyla 3/7/2026 itibarıyla şarapta 12/3 otomatik güncellemesi işlemiş
   ve tutar 61,3914 → 71,2692 (+%16,09) olmuştur. GİB listesinin başlığı bunu
   açıkça yazmaktadır.

**Öneri:** Modelde **71,2692 TL/litre** (EV-2026-08-09-111) kullanılsın;
EV-2026-08-09-112 `SUPERSEDED` olarak kalsın.

### Bu çözümü ne çürütür
- 3/7/2026 sonrasında şarap için 12/3'ü askıya alan veya tutarı yeniden tespit
  eden bir Cumhurbaşkanı Kararı çıkmışsa (bu turda tespit edilmedi).
- GİB'in yayımladığı listenin hesaplama hatası içermesi (Yİ-ÜFE 6 aylık değişim
  oranının %16,09 olduğu **TÜİK kaynağından bağımsız olarak doğrulanmadı** —
  bu, çözümün en zayıf halkasıdır).

### Kapanış için gereken
- TÜİK Yİ-ÜFE Aralık 2025 → Haziran 2026 değişim oranının %16,09 civarında
  olduğunun doğrulanması, **veya**
- Bir gümrük müşaviri / GİB üzerinden güncel beyanname örneğinde uygulanan
  TL/lt tutarının teyidi.
