# KARAR GÜNLÜĞÜ

Bu dosya `yatirim-komitesi-baskani`'nın verdiği tüm kararları ve
gerekçelerini kaydeder. Kararlar **silinmez**, üzerine yazılmaz — yeni karar
yeni kayıt olarak eklenir.

---

## KARAR TÜRLERİ

| Karar | Anlamı |
|-------|--------|
| `KILL` | Yapılmamalı |
| `HOLD` | Şu an değil |
| `TEST` | Karar için gerçek veri gerekiyor |
| `IMPORT PILOT` | Sınırlı hacimde gerçek ithalat |
| `SCALE` | Büyütme |

---

## KAYIT #0 — TUR 0 KURULUM

```yaml
tarih:            2026-08-09
tur:              TUR 0
karar:            KARAR VERILMEDI
karar_veren:      -
```

### Neden karar verilmedi

Bu tur **sadece kurulum turudur.** Kullanıcı talimatı açıktır:
web araştırması yapılmadı, vergi/navlun/fiyat verisi toplanmadı, model
çalıştırılmadı. **Karar verilecek hiçbir kanıt yoktur.**

Kanıtsız karar vermek `CLAUDE.md` §1'in doğrudan ihlalidir.

### Gate durumu

| Gate | Soru | Durum |
|------|------|-------|
| G0 | Yasal yol açık mı? | ⬜ **NOT STARTED** |
| G1 | Vergi yükü kanıtlı hesaplanabilir mi? | ⬜ **NOT STARTED** |
| G2 | Gerçek tedarik kaynağı var mı? | ⬜ **NOT STARTED** |
| G3 | Benchmark doğrulandı mı? | ⬜ **BLOCKED** — OQ-001 açık |
| G4 | Model pozitif contribution veriyor mu? | ⬜ **NOT STARTED** |
| G5 | CRITICAL ticket'lar kapandı mı? | ⬜ **NOT STARTED** |

### Kurulan sistem

- 9 ajan (`.claude/agents/`)
- 7 komut (`.claude/commands/`)
- Kanıt sistemi (immutable kanıt kartları, `EV-YYYY-MM-DD-###`)
- Ticket sistemi (`T-###`, CRITICAL gate kuralı)
- Maliyet katmanları L0–L8, KDV iki perspektif, `peak_cash_requirement`
- Model iskeleti — **hiçbir vergi oranı hard-code edilmemiş**

### Açık kalanlar

| # | Konu | Etki |
|---|------|------|
| OQ-001 | Metro 599,90 TL — KDV dahil/hariç, L7/L8 | **G3'ü bloke ediyor** |
| OQ-002 | Model hedef tarihi | Vergi verilerinin geçerlilik tarihi belirsiz |
| — | Karar eşikleri `TBD` | Nihai karar için eşik gerekli |
| — | 9 ajanın registry doğrulaması | TUR 1 başlayamaz |

### Sonraki adım

`SESSION RESTART` → 9 ajanın registry'de varlığını doğrula → `/tur-1-kesif`

---

## KARAR KAYIT FORMATI (SONRAKİ TURLAR)

```yaml
tarih:
tur:
karar:              # KILL | HOLD | TEST | IMPORT PILOT | SCALE
karar_veren:        yatirim-komitesi-baskani
```

### Karar gerekçesi

### Dayandığı kanıtlar

| evidence_id | claim | tier | status |
|-------------|-------|------|--------|

### Kararı taşıyan 3 kritik varsayım

1.
2.
3.

### Kararı tersine çevirecek bulgu

> "Şunu görürsem fikrimi değiştiririm: ..."

### Açık kalan CRITICAL UNKNOWN'lar

| # | UNKNOWN | Neden kapanmadı | Kararı nasıl etkiliyor |
|---|---------|-----------------|------------------------|

### Reddedilen bulgular

| Ajan | Bulgu | Red gerekçesi |
|------|-------|---------------|

### Çözülen çelişkiler

| conflict_id | Çözüm | Gerekçe |
|-------------|-------|---------|

### Bir sonraki gözden geçirme tetikleyicisi

Hangi olay gerçekleşirse bu karar yeniden ele alınır?

### Bu kararı ne çürütür?

---

## BAŞKANIN DEĞİŞMEZ KURALLARI

1. Araştırma yapmaz — eksik veri için ticket açar.
2. Kanıtsız sayıyı reddeder.
3. Başka ajanın bulgusunu kendi tahminiyle değiştirmez.
4. Çelişkiyi sessizce çözmez.
5. **"Yeterli veri yok" geçerli bir çıktıdır** — bundan kaçınmak için
   karar uydurmaz.
6. `impact: CRITICAL` açık ticket varken model `APPROVED` olamaz.
