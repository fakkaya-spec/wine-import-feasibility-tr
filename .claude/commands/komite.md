---
description: TUR 6 — Yatırım komitesi, gate kontrolü ve nihai karar
---

# KOMİTE

Yürüten ajan: `yatirim-komitesi-baskani`

## ÖN KOŞUL

TUR 1–5 tamamlanmış olmalı. Kırmızı takım ticket'ları hedef ajanlara gitmiş
ve düzeltmeler yapılmış olmalı.

## BAŞKANIN KURALLARI

- **Araştırma yapmaz.** Eksik veri için ticket açar.
- **Kanıtsız sayıyı reddeder.**
- **Başka ajanın bulgusunu kendi tahminiyle değiştirmez.**
- Çelişkiyi sessizce çözmez.

## 1. KANIT KALİTESİ DENETİMİ

Her rapor için:
- Her önemli sayının `evidence_id`'si var mı?
- Vergi/mevzuat sonucu T1/T2'ye mi dayanıyor?
- `effective_date` yazılmış mı?
- `ttl` dolmuş kanıt kullanılıyor mu?
- Status etiketleri doğru mu (ASSUMPTION → FACT şişirmesi var mı)?
- **"Bu bulguyu ne çürütür?"** bölümü var mı ve dolu mu?
- Ajan alan dışı sonuç üretmiş mi?

Denetimi geçmeyen bulgu **kullanılmaz** ve gerekçeli olarak geri gönderilir.

## 2. GATE TABLOSU

| Gate | Soru | Durum |
|------|------|-------|
| **G0** | Yasal yol açık mı? (`mevzuat-ruhsat-uzmani` önerisi: PASS/BLOCKED/FAIL) | |
| **G1** | Vergi yükü kanıtlı ve satır satır hesaplanabilir mi? | |
| **G2** | Gerçek, ulaşılabilir tedarik kaynağı var mı? | |
| **G3** | Benchmark doğrulandı mı? (OPEN QUESTION #001 kapandı mı) | |
| **G4** | Model kanıtlı girdilerle pozitif contribution veriyor mu? | |
| **G5** | CRITICAL ticket'lar kapandı mı? | |

**Kurallar:**
- G0 önerisi `mevzuat-ruhsat-uzmani`'ndan gelir; **karar başkanındır.**
- OPEN QUESTION #001 kapanmadan **G3 geçilemez.**
- CRITICAL açık ticket varken model `APPROVED` olamaz → **G5 geçilemez.**
- **Kritik UNKNOWN kararı bloke edebilir.** "Yeterli veri yok" geçerli bir
  çıktıdır ve bundan kaçınmak için karar uydurulmaz.

## 3. ÇELİŞKİ ÇÖZÜMÜ

`99-ops/celiskiler.md` tek tek ele alınır:
- Tier karşılaştırması
- Yürürlük tarihi karşılaştırması
- Gerekirse ek doğrulama ticket'ı
- Çözüm gerekçesi `90-karar/karar-gunlugu.md`'ye yazılır
- Çözülemeyen çelişki `CONFLICT` olarak karara taşınır

## 4. KARAR

`KILL` · `HOLD` · `TEST` · `IMPORT PILOT` · `SCALE`

`00-charter/karar-esikleri.md` eşiklerine bakılır. Eşikler hâlâ `TBD` ise
bu durum kararda **açıkça** belirtilir — eşik uydurulmaz.

## 5. KARAR GÜNLÜĞÜ

`90-karar/karar-gunlugu.md` dosyasına yazılır:

- Karar ve tarih
- Dayandığı `evidence_id` listesi
- Kararı taşıyan **3 kritik varsayım**
- **Kararı tersine çevirecek bulgu** ("bunu görürsem fikrimi değiştiririm")
- Açık kalan CRITICAL UNKNOWN'lar
- Reddedilen bulgular ve red gerekçeleri
- Bir sonraki gözden geçirme tetikleyicisi

## 6. ZORUNLU SON BÖLÜM

`## Bu kararı ne çürütür?`

## SONRAKİ ADIM

Karar `TEST` veya `IMPORT PILOT` ise → TUR 7:
gerçek RFQ gönderimi, gerçek navlun teklifi, gerçek kanal doğrulaması.
