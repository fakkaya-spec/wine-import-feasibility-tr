# TICKET ŞABLONU

> Bu dosya **şablondur**. Kopyala, `99-ops/tickets/T-###.md` olarak kaydet,
> doldur. Bu şablonun kendisi doldurulmaz ve bir ticket sayılmaz.

---

```yaml
ticket_id:            # T-###
opened_by:            # ticketi acan ajan
target_agent:         # cozecek ajan
opened_date:          # YYYY-MM-DD
claim:                # Tek cumlelik iddia / soru
impact:               # CRITICAL | HIGH | MEDIUM | LOW
status:               # OPEN | ANSWERED | RESOLVED | REJECTED
resolution_evidence:  # Cozumu kanitlayan evidence_id(ler)
```

---

## AÇIKLAMA

### Ne iddia ediliyor / ne soruluyor

### Neden önemli — model nerede kırılır

### Hangi model girdisini etkiler

| YAML dosyası | Alan |
|--------------|------|
| | |

---

## CEVAP *(target_agent doldurur)*

### Bulgu

### Kanıt

| evidence_id | tier | claim | effective_date |
|-------------|------|-------|----------------|
| | | | |

### Sonuç

`status` → `ANSWERED`

---

## KAPANIŞ *(yatirim-komitesi-baskani doldurur)*

### Karar

`RESOLVED` (kabul edildi) veya `REJECTED` (reddedildi)

### Gerekçe

### Kapanış tarihi

---

# ALAN TANIMLARI

## `impact`

| Değer | Anlamı | Sonucu |
|-------|--------|--------|
| `CRITICAL` | Doğruysa proje kararını değiştirir | **Açıkken finans modeli `APPROVED` olamaz** |
| `HIGH` | Model çıktısını anlamlı ölçüde değiştirir | Karar öncesi kapanmalı |
| `MEDIUM` | Bir senaryoyu etkiler | Kapanması tercih edilir |
| `LOW` | İyileştirme / netleştirme | Bloke etmez |

> **Uyarı:** Her şeye `CRITICAL` verilirse hiçbir şey CRITICAL olmaz.
> `seytanin-avukati` bu kaldıracı ucuzlatmamalıdır.

## `status`

| Değer | Anlamı |
|-------|--------|
| `OPEN` | Açıldı, henüz cevaplanmadı |
| `ANSWERED` | `target_agent` cevapladı, başkan onayı bekliyor |
| `RESOLVED` | Başkan cevabı kabul etti, kapandı |
| `REJECTED` | Başkan iddiayı/cevabı reddetti (gerekçeli) |

## Gate kuralı

**`impact: CRITICAL` ve `status: OPEN` olan tek bir ticket bile varken
finans modeli çıktısı `APPROVED` olamaz — en fazla `DRAFT` olabilir.**
(bkz. `CLAUDE.md` §5, `80-model/inputs/senaryolar.yaml` → `cikti_kapisi`)

---

# TICKET İNDEKSİ

Açılan tüm ticket'lar burada listelenir.

| ticket_id | opened_by | target_agent | impact | status | claim (kısa) |
|-----------|-----------|--------------|--------|--------|--------------|
| *(boş — TUR 0'da ticket açılmadı)* | | | | | |
