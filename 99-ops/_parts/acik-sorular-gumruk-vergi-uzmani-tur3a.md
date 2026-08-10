# AÇIK SORULAR — gumruk-vergi-uzmani · TUR 3A (2026-08-10)

---

## KAPANAN AÇIK SORULAR

| Kod | Soru | Durum | Kanıt |
|---|---|---|---|
| **OQ-G10** | md.36'ya dayanan bir CB kararı var mı? | ✅ **KAPANDI** — **VAR** (7846 + 8000), ama önlem bazlı; 2204.21'de tetiklenmiyor | `EV-2026-08-10-852`, `-853`, `-856` |
| **U1** *(kdv-…-nakit.md §4)* | KDVGUT III/C tam metni taranmadı | ✅ **KAPANDI** — belgenin **tamamı** (397 s.) tarandı | `EV-2026-08-10-854`, `-855`, `-859` |
| **Gözetim** *(matrah-sirasi.md §2)* | 2204.21'de gözetim var mı? | ✅ **KAPANDI** — **YOK**, pozitif taramayla | `EV-2026-08-10-860` |
| — | Korunma önlemi / damping var mı? | ✅ **KAPANDI** — **YOK** | `EV-2026-08-10-861`, `-862` |
| — | Alkolde özel matrah şekli var mı? | ✅ **KAPANDI** — **YOK** (TEKEL'e özgüydü, fiilen kalktı) | `EV-2026-08-10-857` |

---

## YENİ / DEVAM EDEN AÇIK SORULAR

| # | Soru | Kritiklik | Neden kapanmadı | Nasıl kapanır | Ticket |
|---|---|---|---|---|---|
| **OQ-G20** | Yıllık pakete girmemiş, daha eski ve hâlâ yürürlükte bir gözetim tebliği var mı? | **MEDIUM** | Yöntem yalnız yıllık paketi görüyor; `mevzuat.gov.tr` erişilemedi | TARA ekranından tek GTİP sorgusu **veya** gümrük müşaviri | `T-172` |
| **OQ-G21** | Gözetim OLMAKSIZIN, GK md.23–31 kıymet araştırmasıyla artan matraha 7846 uygulanır mı? | **MEDIUM** | Karar ve KDVGUT metinlerinden çıkmıyor; iki okuma mümkün | YMM / gümrük müşaviri | `T-173` |
| **OQ-G22** | `mevzuat.gov.tr` ile ikinci bağımsız doğrulama | **LOW** | Site bu oturumda tamamen erişilemedi | erişim geri geldiğinde tekrar | `EV-…-864` (ttl 7d) |
| **OQ-G23** | GVK md.41 (şahıs işletmesi, KVK md.11/1-ı muadili) | **LOW** | `mevzuat.gov.tr` erişilemedi | ithalatçı sermaye şirketi ise **gereksiz** | `T-151` md.4 |
| **OQ-G24** | 7846 kapsamındaki YMM raporu / bildirim eşiği (46 Sıra No.lu SMMM-YMM Genel Tebliği md.3/1-a tutarı) | **LOW** | Baz senaryoda tetiklenmiyor | tetiklenirse aranır | — |
| **OQ-G02** *(devam)* | KKDF matrahının tam tanımı | MEDIUM | TUR 1'den beri açık; peşin ödemede etkisiz | gümrük müşaviri | `T-105` |
| **OQ-G03** *(devam)* | Gümrük beyannamesi damga vergisi 2026 tutarı | LOW | doğrulanmadı; şişe başına ihmal edilebilir | GİB tarifeleri | — |
| **OQ-G05** *(devam)* | Gümrük beyanında esas alınacak kur kuralı | HIGH | TUR 2.5'te kapatılamadı, TUR 3A kapsamı dışıydı | gümrük müşaviri | `T-911` |

---

## TAZELİK UYARISI — bu turda üretilen bulguların ömrü

| evidence_id | ttl | STALE tarihi | Neden kısa |
|---|---|---|---|
| `EV-2026-08-10-860` (gözetim) | **30d** | **2026-09-09** | Gözetim tebliği **yıl içinde de** çıkabilir |
| `EV-2026-08-10-861` (korunma) | 90d | 2026-11-08 | Soruşturmalar yıl içinde sonuçlanır |
| `EV-2026-08-10-862` (damping) | 90d | 2026-11-08 | Liste 13/07/2026 tarihli, düzenli güncelleniyor |
| `EV-2026-08-10-864` (erişim) | **7d** | **2026-08-17** | Site erişimi geri gelebilir |

> ⚠ **Model hedef tarihlerinin üçü de 2027'dedir.** Gözetim bulgusu — tıpkı ÖTV
> maktu tutarı ve gümrük vergisi oranı gibi — **hedef tarihte doğrulanmış
> değildir.** `ters-model-vergi-bacagi.md` §13.1'deki asimetri uyarısı
> **gözetim için de geçerlidir** ve bu turda o listeye eklenmiştir.
