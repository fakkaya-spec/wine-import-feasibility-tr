# KANIT KARTI ŞABLONU

> Bu dosya **şablondur**. Kopyala, `10-evidence/raw/EV-YYYY-MM-DD-###.md`
> olarak kaydet, doldur. Bu şablonun kendisi doldurulmaz.
>
> **KANIT KARTLARI IMMUTABLE'DIR.** Bir kart oluşturulduktan sonra içeriği
> değiştirilmez. Veri değişirse **yeni kart** açılır, `supersedes` alanı ile
> eskiye bağlanır, eski kartın `status` alanı `SUPERSEDED` yapılır.
> (Bu, immutability'nin tek istisnasıdır ve yalnızca `status` alanına uygulanır.)

---

```yaml
evidence_id:        # EV-YYYY-MM-DD-###  (örn. EV-2026-08-09-001)
claim:              # Bu kanıt neyi iddia ediyor? Tek cümle.
value:              # Sayı veya metin. Orijinal birimde/para biriminde.
unit:               # TRY | USD | EUR | % | TL/litre | gün | ml | kg | adet ...
tier:               # T1 | T2 | T3 | T4 | T5
source_name:        # Kaynağın adı (Resmî Gazete, TADAB, forwarder adı, mağaza...)
url:                # Tam URL. Yoksa: OFFLINE / PHOTO / EMAIL
publication_date:   # Kaynağın yayın tarihi (YYYY-MM-DD)
effective_date:     # YÜRÜRLÜK tarihi — vergi/mevzuatta belirleyici olan budur
access_date:        # Erişim/gözlem tarihi (YYYY-MM-DD)
confidence:         # HIGH | MEDIUM | LOW
status:             # FACT | ESTIMATE | ASSUMPTION | UNKNOWN | CONFLICT | SUPERSEDED
ttl:                # Tazelik süresi (örn. 30d, 90d, 1y). Sonrası STALE.
snapshot_path:      # 10-evidence/raw/snapshots/... (sayfa kopyası, foto, PDF)
collecting_agent:   # Kanıtı toplayan ajanın adı
supersedes:         # Bu kartın geçersiz kıldığı evidence_id. Yoksa: -
conflict_id:        # Çelişki varsa C-### (99-ops/celiskiler.md). Yoksa: -
notes:              # Serbest not
```

---

## ALAN AÇIKLAMALARI

### `tier`
| Tier | Tanım |
|------|-------|
| T1 | Resmî Gazete / yürürlükteki kanun, CBK, tebliğ |
| T2 | İlgili kamu kurumunun resmî güncel sayfası |
| T3 | Resmî rehber / meslek örgütü / akredite kurum |
| T4 | Ticari teklif / sektör raporu / market gözlemi |
| T5 | Basın / blog / forum / LLM hafızası |

**Vergi ve mevzuat sonucu için T5 tek başına kullanılamaz.**

### Üç tarih neden ayrı
- `publication_date` — kaynak ne zaman yayınlandı
- `effective_date` — düzenleme ne zaman yürürlüğe girdi *(vergide belirleyici)*
- `access_date` — sen ne zaman baktın *(tazelik hesabı buradan)*

Bir tebliğ 2025'te yayınlanıp 2026'da yürürlüğe girebilir. Modelde
kullanılacak olan **model hedef tarihinde yürürlükte olan** değerdir.

### `status`
| Değer | Anlamı |
|-------|--------|
| `FACT` | Doğrulanmış |
| `ESTIMATE` | Gerçek verilerden türetilmiş (türetme zinciri `notes`'ta) |
| `ASSUMPTION` | Zorunlu tahmin (gerekçe `notes`'ta) |
| `UNKNOWN` | Doğrulanamadı |
| `CONFLICT` | Kaynaklar çelişiyor, `conflict_id` dolu |
| `SUPERSEDED` | Yeni kanıtla değiştirildi |

### `ttl` önerileri
| Veri türü | Önerilen TTL |
|-----------|--------------|
| ÖTV maktu tutarı | 30d |
| Gümrük vergisi oranı | 90d |
| Gözetim/referans kıymet | 30d |
| Navlun (spot) | 14d |
| Raf fiyatı gözlemi | 30d |
| FX kuru | 7d |
| Tedarikçi gösterge fiyatı | 90d |
| Tedarikçi firm offer | teklifin geçerlilik süresi |
| Ruhsat prosedürü | 180d |

---

## DOLDURULMUŞ ÖRNEK (SADECE FORMAT GÖSTERİMİ — GERÇEK VERİ DEĞİLDİR)

```yaml
evidence_id:        EV-2026-08-09-000
claim:              ÖRNEK KAYIT — format gösterimi. Gerçek veri değildir.
value:              null
unit:               -
tier:               T5
source_name:        SABLON
url:                -
publication_date:   -
effective_date:     -
access_date:        2026-08-09
confidence:         LOW
status:             UNKNOWN
ttl:                0d
snapshot_path:      -
collecting_agent:   -
supersedes:         -
conflict_id:        -
notes:              Bu satır index.csv'de yer almaz. Yalnızca alan sırasını gösterir.
```
