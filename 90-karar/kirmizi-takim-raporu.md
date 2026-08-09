# KIRMIZI TAKIM RAPORU

```yaml
ajan:    seytanin-avukati
tur:     TUR 4 (henuz calistirilmadi)
tarih:   -
durum:   BOS_ISKELET
```

---

## DURUM: BOŞ

Bu rapor **TUR 4**'te doldurulacaktır. TUR 0 kurulum turudur; kırmızı takım
henüz çalışmamıştır ve bu turda çalışmayacaktır.

Kırmızı takım ancak TUR 3'te (`/model-calistir`) model bir çıktı ürettikten
sonra anlamlıdır — saldıracak bir hedef olmadan saldırı yapılamaz.

---

## RAPOR YAPISI (DOLDURULDUĞUNDA)

### 1. YÖNETİCİ ÖZETİ
Projeyi öldürebilecek en güçlü **tek** argüman nedir?

### 2. SALDIRI SONUÇLARI

Her vektör için ayrı bölüm:

| # | Vektör | Bulgu var mı | En yüksek impact | Ticket |
|---|--------|--------------|------------------|--------|
| 1 | Gizli maliyet | | | |
| 2 | Regülasyon şoku | | | |
| 3 | Kur şoku | | | |
| 4 | MOQ tuzağı | | | |
| 5 | Yavaş stok | | | |
| 6 | Kanal gücü | | | |
| 7 | Supplier dependency | | | |
| 8 | Rekabet | | | |
| 9 | Nakit akışı | | | |
| 10 | İthalat riskleri | | | |
| 11 | Modelde çift sayım | | | |
| 12 | Unutulan maliyet | | | |
| 13 | **Yanlış benchmark** | | | |

### 3. HER CHALLENGE İÇİN

```
#### CH-##: <baslik>

**Iddia:**
**Kanit / gerekce:** (evidence_id)
**Etki:** model nerede ve NE KADAR kirilir
**Bu saldiriyi ne curutur:** (durust ol)
**Ticket:** T-###
**Impact:** CRITICAL | HIGH | MEDIUM | LOW
```

### 4. AÇILAN TICKET'LAR

| ticket_id | target_agent | claim | impact | status |
|-----------|--------------|-------|--------|--------|

### 5. PROJEYİ ÖLDÜREN SENARYO

Bulguları birleştirerek: projenin battığı en gerçekçi senaryo nedir?
Hangi üç şey aynı anda ters giderse iş yürümez?

### 6. BU BULGUYU NE ÇÜRÜTÜR?

Kendi saldırılarına karşı en güçlü savunma. Abartı güvenilirliği azaltır.

---

## HATIRLATMA — KIRMIZI TAKIM KURALLARI

- **Kanıtsız saldırı reddedilir.** "Bence riskli" yeterli değildir.
- **Her şeye `CRITICAL` verme.** Kaldıraç ucuzlar.
- **Kendi alternatif modelini kurma.** Sen yıkarsın; yeniden kurmak
  `finans-fizibilite`'nin işidir.
- **Nihai karar verme.** O `yatirim-komitesi-baskani`'nın işidir.
- **En kritik saldırı vektörü #13'tür** (yanlış benchmark) — çünkü
  OQ-001 hâlâ açıktır ve tüm fiyat merdiveni ona dayanır.
