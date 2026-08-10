# AÇIK SORULAR — gumruk-vergi-uzmani (TUR 1.5, 2026-08-10)

> Bu dosya TUR 1'deki `acik-sorular-gumruk-vergi-uzmani.md` dosyasının
> **EKİDİR**, onun yerine geçmez. TUR 1 dosyasına DOKUNULMAMIŞTIR.

---

## KAPANAN SORU

### ✅ OQ-G01 — İthalatta ödenen KDV indirilebilir mi? — **KAPANDI**

**Cevap: EVET, indirilebilir.**
KDVK **md.29/1-b** (T1, yürürlük 1985-01-01) + **md.34/1** belge şartı +
**md.30** tahdidi yasak listesinde alkole ilişkin hüküm **yok**.

| evidence_id | tier | ne kanıtlıyor |
|---|---|---|
| `EV-2026-08-10-101` | T1 | md.29/1-b — ithalatta ödenen KDV indirilir |
| `EV-2026-08-10-102` | T1 | md.34/1 — gümrük makbuzu + defter kaydı şartı |
| `EV-2026-08-10-103` | T1 | md.30 tam metin — alkole özgü yasak YOK (tahdidi liste) |
| `EV-2026-08-10-104` | T1 | md.29/2 — devreden KDV **iade edilmez** |
| `EV-2026-08-10-105` | T1 | md.29/3 — indirim hakkı süresi (VDO yılı + 1 yıl) |

Tam analiz: `30-vergi-gumruk/kdv-ekonomik-maliyet-vs-nakit.md`

**Modele etkisi:** `A1/A2 iki senaryo` zorunluluğu **kalktı**. A1 baz senaryodur;
KDV'nin ekonomik maliyeti **0,00 TL/şişe**'dir.

---

## YENİ AÇILAN SORULAR

### OQ-G09 — Fiili KDV vergilendirme dönemi 1 ay mı 3 ay mı? (HIGH)

**Neden kritik:** KDVK md.39/1'in **kanuni varsayılanı 3 aydır**; 1 aylık dönem
bir Bakanlık tespitine dayanır. Model 1 ay varsayıyor (`ASSUMPTION`).
3 aylık dönemde ithalat KDV'sinin mahsup gecikmesi **28–59 gün → 28–~118 gün**'e
çıkar ve `peak_cash_requirement` ciddi biçimde büyür.
**Bu turda neden çözülemedi:** GİB'in mükellef gruplarını belirleyen tespiti/
tebliği bulunamadı; GİB sayfaları JS ile render ediliyor.
**evidence_id:** `EV-2026-08-10-111` (kanun metni, T1) · **Ticket:** `T-152`

---

### OQ-G10 — KDVGUT III/C ve md.36 CB kararları taranmadı (MEDIUM)

**Neden önemli:** KDVK **md.36** Cumhurbaşkanı'na indirim hakkını kısmen/tamamen
**kaldırma** yetkisi verir. Şarap için böyle bir karar olup olmadığı
**aranmamıştır.** Bulunursa OQ-G01'in cevabı tersine döner.
**Neden düşük olasılık:** md.30'un tahdidi listesiyle sistematik çelişki
yaratırdı ve sektörde bilinir olurdu. Ama bu bir **argüman**, kanıt değil.
**evidence_id:** `EV-2026-08-10-114` (`status: UNKNOWN`) · **Ticket:** `T-151`

---

### OQ-G11 — 149 No.lu VUK Sirküleri'nin tarihi (LOW)

GİB, KDV beyannamesi verme süresini kanuni 24. günden (KDVK md.41/1) **28. güne**
uzatmıştır. Bu uzatmanın `effective_date`'i doğrulanamadı → `EV-2026-08-10-109`
`effective_date: UNKNOWN`. Model **muhafazakâr** olan 28'i kullanır; 24/26
kullanılsaydı gecikme **2–4 gün kısalırdı** (yön lehte, büyüklük ihmal edilebilir).

---

### OQ-G12 — KVK md.11/1-(ı) %50 oranı yürürlükte değiştirilmiş mi? (LOW)

Alkollü içki **ilan/reklam** giderlerinin %50'si KKEG'dir (T1, `EV-2026-08-10-113`)
ve KDVK md.30/d uyarınca o kısma ait KDV indirilemez. Cumhurbaşkanı bu oranı
%0–%100 arası değiştirmeye yetkilidir; yürürlükte bir değiştirme kararı olup
olmadığı **doğrulanmadı.**
**Neden düşük:** malın kendisine ait KDV'yi etkilemez; ayrıca alkolde reklamın
hukuken mümkün olup olmadığı `mevzuat-ruhsat-uzmani` alanıdır ve bu turda
kapalıdır. Reklam yapılamıyorsa etki **sıfırdır.**

---

## DEVAM EDEN SORULAR (TUR 1'den)

`OQ-G02` (gözetim), `OQ-G03` (KKDF matrahı), `OQ-G04` (antrepo kısmi çekiş),
`OQ-G05` (menşe ispat belgesi), `OQ-G06` (12 haneli GTİP), `OQ-G07` (damga
vergisi), `OQ-G08` (model hedef tarihi ÖTV'si) **AÇIK KALMAKTADIR**.
Bu turun kapsamı dar olduğu için bunlara dokunulmamıştır.

`T-901` (TÜİK Yİ-ÜFE doğrulaması) **ANSWERED / DOĞRULANAMADI** olarak
kapatılmıştır — sonuç `UNKNOWN`'dır, `RESOLVED` değildir.
