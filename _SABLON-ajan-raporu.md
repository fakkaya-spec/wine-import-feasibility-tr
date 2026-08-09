# AJAN RAPORU ŞABLONU

> Her ajan raporunu bu formatta yazar. **"Bu bulguyu ne çürütür?"** bölümü
> olmayan rapor eksiktir ve başkan tarafından geri gönderilir.

---

## BAŞLIK

```yaml
ajan:               # ajan adı
tur:                # TUR 1 | TUR 2 | ...
tarih:              # YYYY-MM-DD
durum:              # DRAFT | SUBMITTED | ACCEPTED | REJECTED | REVISION_REQUIRED
```

---

## 1. YÖNETİCİ ÖZETİ

3–5 cümle. Ne arandı, ne bulundu, en kritik tek bulgu ne.
Sayı verilecekse `evidence_id` ile birlikte.

---

## 2. BULGULAR

Her bulgu için ayrı blok:

### B-1: <bulgu başlığı>

```yaml
claim:          # Tek cümlelik iddia
value:          # Sayı/metin, orijinal birimde
unit:           #
status:         # FACT | ESTIMATE | ASSUMPTION | UNKNOWN | CONFLICT
tier:           # T1..T5
evidence_id:    # EV-YYYY-MM-DD-###
effective_date: # vergi/mevzuat ise ZORUNLU
katman:         # L0..L8 (fiyat/maliyet sayısıysa ZORUNLU)
```

**Gerekçe:** Neden bu sonuca vardın.
**Türetme zinciri:** (`ESTIMATE` ise zorunlu) Hangi sayıdan nasıl türettin.
**Varsayım gerekçesi:** (`ASSUMPTION` ise zorunlu) Neden bu varsayım, aralık ne.

---

## 3. UNKNOWN LİSTESİ

| # | Ne bilinmiyor | Neden bulunamadı | Kritik mi | Nasıl bulunabilir |
|---|---------------|------------------|-----------|-------------------|
| | | | CRITICAL/HIGH/MEDIUM/LOW | |

**UNKNOWN yazmak başarısızlık değildir. Uydurmak başarısızlıktır.**

---

## 4. ÇELİŞKİLER

Kaynaklar çelişiyorsa — **sessizce seçim yapma.**

| conflict_id | Kaynak A (tier/tarih) | Kaynak B (tier/tarih) | Neden çelişiyor | Durum |
|-------------|----------------------|----------------------|-----------------|-------|
| C-### | | | | OPEN |

`99-ops/celiskiler.md` dosyasına da yaz.

---

## 5. MODEL GİRDİLERİ

Bu rapordan `80-model/inputs/*.yaml` dosyalarına giden değerler:

| YAML dosyası | Alan | Değer | Birim | status | evidence_id |
|--------------|------|-------|-------|--------|-------------|

**evidence_id'si olmayan satır modele giremez.**

---

## 6. ÇAPRAZ İPUÇLARI

Kendi alanım dışında gördüğüm, başka ajanları ilgilendiren bulgular.
Bunlar **sonuç değildir**, ipucudur. `99-ops/capraz-ipuclari.md`'ye de yazıldı.

| Hedef ajan | İpucu | Neden önemli |
|------------|-------|--------------|

---

## 7. AÇILAN / KAPANAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|-----------|--------------|-------|--------|--------|

---

## 8. TAZELİK

| evidence_id | ttl | STALE olacağı tarih |
|-------------|-----|---------------------|

---

## 9. BU BULGUYU NE ÇÜRÜTÜR? *(ZORUNLU — bu bölüm olmadan rapor geçersizdir)*

Dürüst ol. Kendi işini savunmaya çalışma.

### 9.1 Bu raporu geçersiz kılacak tek bulgu nedir?

### 9.2 En kırılgan varsayımım hangisi ve neden?

### 9.3 Hangi kaynağıma en az güveniyorum?

### 9.4 Bu bulgunun yanlış olması durumunda projenin hangi kararı değişir?

### 9.5 Bunu doğrulamak için ne gerekir? (kim, nasıl, ne kadar sürede)
