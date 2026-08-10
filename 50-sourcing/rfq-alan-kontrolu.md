# RFQ ŞABLONU — ALAN KONTROLÜ (TUR 1.5)

```yaml
ajan:            global-sourcing-kasifi
tur:             TUR 1.5 — BLOCKER REMEDIATION
tarih:           2026-08-10
kontrol_edilen:  50-sourcing/rfq-template.md
girdi_surumu:    v2.0 (TUR 1, 2026-08-09)
cikti_surumu:    v2.1 (TUR 1.5, 2026-08-10)
zorunlu_alan:    25
sonuc:           VARDI 20 / KISMEN VARDI (genisletildi) 4 / EKLENDI 1
```

Bu dosya, sonraki **gerçek teklif turu** (TUR 7) öncesinde RFQ şablonunun 25 zorunlu
alanı sorup sormadığının alan alan denetimidir. Bu turda **hiçbir üreticiye temas
edilmemiştir**; denetim tamamen şablon metni üzerinde yapılmıştır.

---

## 1. KONTROL TABLOSU

| # | Zorunlu alan | Sonuç | v2.0'da nerede | v2.1'de nerede | Not |
|---|---|---|---|---|---|
| 1 | winery / supplier | **VARDI** | 8.1, 8.7 | S1, 8.1, 8.7 | Yasal unvan + sicil + adres + hesap sorumlusu zaten sorulmuş. Özet tabloya S1 olarak taşındı. |
| 2 | product | **VARDI** | 1.1 | S2, 1.1 | Ürün adı / iç referans. |
| 3 | grape / blend | **VARDI** | 1.2 | S3, 1.2 | Çeşit **yüzdesi** ile isteniyor — "Colombard-Chardonnay benzeri blend" hedefi için yeterli. |
| 4 | vintage | **VARDI** | 1.3 | S4, 1.3 | Mevcut hasat yılları + yıl başına yaklaşık stok. |
| 5 | ABV | **VARDI** | 1.4 | S5, 1.4 | "Etikette görünecek kesin rakam" olarak soruluyor. |
| 6 | bottle size | **VARDI** | 1.7 | S6, 1.7 | 750 ml talebi + teyit. |
| 7 | **bottle weight** | **KISMEN VARDI (genişletildi)** | 1.8 içinde, şişe tipi ve cam rengiyle **aynı hücrede** | 1.8 (tip/renk), **1.14 (boş şişe ağırlığı, g)**, **1.15 (dolu şişe brüt ağırlığı, g)**, **1.16 (hafif şişe alternatifi + fiyat farkı)**, S7 | v2.0'da tek hücrede üç şey soruluyordu; tedarikçi tipik olarak ilk ikisini yazıp ağırlığı atlar. Ayrıldı. Ayrıca dolu şişe ağırlığı hiç sorulmuyordu — koli brüt ağırlığının (2.2) çapraz kontrolü bu olmadan yapılamaz. |
| 8 | case configuration | **VARDI** | 2.1, 2.2, 2.3, 2.4 | S8 + aynı sorular | Şişe/koli, brüt+net kg, dış ölçü L×W×H, katman düzeni. |
| 9 | pallet configuration | **VARDI** | 2.5, 2.6, 2.7 | S9 + aynı sorular | Koli/palet, palet tipi (EUR/endüstriyel), ISPM-15, brüt kg, toplam yükseklik. |
| 10 | MOQ | **VARDI** | 3.6 (a şişe / b konteyner), 4.2, 4.3 | S10 + aynı sorular | İki birimde birden sorulması C-401'in doğrudan cevabıdır — korundu. |
| 11 | EXW | **VARDI** | 3.1 | S11, 3.1 | Teslim **yeri** zorunlu tutuluyor ("EXW Bordeaux ≠ EXW Languedoc"). |
| 12 | FOB | **VARDI** | 3.2 | S12, 3.2 | **Named port** zorunlu tutuluyor. |
| 13 | Incoterm | **KISMEN VARDI (genişletildi)** | Yalnızca **dolaylı**: 3.1/3.2/3.3 belirli Incoterm'lerde fiyat istiyor; "hangi Incoterm'lerle çalışabiliyorsun" sorusu **yoktu** | **3.16** (Incoterms® 2020 listesi + tedarikçinin standardı + Türkiye önerisi), S13 | `tedarikci-havuzu.csv → incoterm` ve `tedarikci.yaml → fiyat.incoterm` kolonlarının doğrudan karşılığı yoktu. TUR 1'de SUP-403'ün dört Incoterm'i birden listelemesi (EV-2026-08-09-417) bunun **müzakere edilebilir** olduğunu gösteriyordu; artık açıkça soruluyor. |
| 14 | port | **VARDI** | 2.10, 2.11, 3.2 | S14 + aynı sorular | En yakın/olağan yükleme limanı + mesafe (km) + FOB'un named port'u. |
| 15 | lead time | **VARDI** | 3.11 | S15, 3.11 | PO onayı → yüklemeye hazır, takvim günü. |
| 16 | production time | **KISMEN VARDI (genişletildi)** | 3.11 **toplam** lead time'ı soruyordu; üretim süresi ayrı alan değildi | **3.17** (a üretim/şişeleme, b etiket basım+uygulama, c ihracat evrakı, d gemi/kamyon bekleme), S16 | Bu ayrım kritiktir: `tedarikci.yaml → arastirma_bulgulari.uretim_lead_time_gun` (28–42 gün) **yalnızca üretim** süresidir ve navlun hariçtir. Toplam lead time ile karıştırılırsa `peak_cash_requirement` yanlış hesaplanır. |
| 17 | payment terms | **VARDI** | 3.8 (ilk sipariş), 3.9 (sonraki), 3.10 (vade günü + sürşarj) | S17 + aynı sorular | İlk sipariş / sonraki sipariş ayrımı korundu; KKDF ipucu `gumruk-vergi-uzmani`'na T-404 ile zaten bırakılmış. |
| 18 | private label availability | **VARDI** | 4.1 (+ 4.2–4.12 tüm blok) | S18 + aynı sorular | Model A/B eşitliği için Bölüm 5 de korundu. |
| 19 | **label cost** | **KISMEN VARDI (genişletildi)** | 4.7 yalnızca "one-off artwork or plate/cliché charge" diyordu; **birim etiket maliyeti ve EXW'ye dahil olup olmadığı sorulmuyordu** | **3.18(d)** (etiket seti birim maliyeti + EXW'ye dahil mi), **4.13** (a: tek seferlik — artwork, klişe, kesim bıçağı, renk provası; b: şişe/1.000 başına tekrarlayan; + kapsül/kapak baskısı ayrı), **4.15** (klişe sonrası iptal ücreti), S19; 4.7 revizyon **sayısı ve süresine** odaklandı | `tedarikci.yaml → private_label.etiket_tasarim_maliyeti` alanı doldurulamıyordu. TUR 1'de SUP-401 tasarımı "ek ücretsiz" beyan etmişti (EV-2026-08-09-408) — ama bu **tasarım**tır, **baskı ve klişe** değildir. Şablon artık ikisini ayırıyor. |
| 20 | **carton cost** | **EKLENDİ** | **YOKTU.** 3.14 yalnızca "EXW'ye dahil olmayan kalemler nelerdir" diye açık uçlu soruyordu; karton hiç geçmiyordu | **3.18(e)** (karton/koli birim maliyeti + EXW'ye dahil mi), **3.18(f/g)** (ara bölme, palet + streç + paletleme işçiliği), **3.19** (koli konfigürasyonu değişikliğinin şişe başına etkisi), **4.14** (markalı karton ile düz karton farkı + minimum baskı adedi), S20 | Şablondaki **tek gerçek boşluktu.** Karton maliyeti L0'ın kapsamını belirler: karton hariç verilmiş bir EXW ile dahil verilmiş bir EXW karşılaştırılamaz. |
| 21 | sample policy | **VARDI** | 7.1–7.5 | S21 + aynı sorular | Gönderim, adet, maliyet, süre, **aynı parti mi** temsili parti mi, analiz sertifikası ile birlikte mi. |
| 22 | annual capacity | **VARDI** | 3.12 (bize ayrılabilir hacim), 8.3 (toplam kapasite), 8.4 (şişeleme hattı) | S22 + aynı sorular | İki soru bilinçli olarak ayrı: **toplam kapasite** ile **bize ayrılabilir kapasite** aynı şey değildir. Kontrol listesine çapraz tutarlılık maddesi eklendi. |
| 23 | certificate availability | **VARDI** | 6.1 (menşe ispatı: EUR.1 / fatura beyanı / REX / A.TR), 6.2 (menşe şahadetnamesi), 6.3–6.4 (analiz + akreditasyon), 6.5 (sağlık/serbest satış), 6.10 (BRCGS/IFS/ISO 22000/HACCP) | S23 + aynı sorular | 6.1 "evet" cevabını kabul etmiyor, **belge adı** istiyor — korundu. Tarife yorumu yapılmıyor (alan dışı, `gumruk-vergi-uzmani`). |
| 24 | Turkey export experience | **VARDI** | 6.6 (hangi ithalatçı, hangi yıllar, hangi hacim), 5.2/5.3 (Model A: mevcut temsilci, geçmiş marka) | S24 + aynı sorular | `risk.turkiyeye_ihracat_gecmisi` alanının doğrudan karşılığı. |
| 25 | **validity date of quote** | **VARDI** | 3.5 (geçerlilik tarihi), 3.4 (INDICATIVE / FIRM_OFFER) | S25 (ikisi tek satırda), 3.4, 3.5 | Bu ikisi **birlikte** sorulmalıdır: geçerlilik tarihi olmayan bir FIRM_OFFER firm değildir. S25'te birleştirildi; 3.5 cevabı kanıt kartının `ttl`'i olur. |

---

## 2. ÖZET

| Sonuç | Adet | Alanlar |
|---|---|---|
| **VARDI** | 20 | 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 15, 17, 18, 21, 22, 23, 24, 25 |
| **KISMEN VARDI (genişletildi)** | 4 | 7 (bottle weight), 13 (Incoterm), 16 (production time), 19 (label cost) |
| **EKLENDİ** | 1 | 20 (carton cost) |

**Şablon gerçek teklif turuna hazır mı: EVET** — 25 alanın tamamı v2.1'de soruluyor.

---

## 3. YAPISAL CEVAP TOPLAMA — NE DEĞİŞTİ

v2.0 doğru soruları soruyordu ama cevabı **8 ayrı bölüme dağıtıyordu**. Bir üretici
tipik olarak e-postaya serbest metin ve bir PDF fiyat listesi ile cevap verir; o
cevabı 45 satırlık bir CSV'ye elle oturtmak hem yavaştır hem hata üretir.

v2.1'de eklenen **SUMMARY SHEET (S1–S25)**, e-posta gövdesinin en başında, doldurulacak
tek sayfalık bir tablodur ve satırları CSV/YAML alanlarıyla birebir eşleşir. Detay
soruları (Bölüm 1–8) korunmuştur; özet tablo onların yerine geçmez, **giriş noktasıdır**.

Ayrıca:
- Soru → CSV eşleme tablosuna **`tedarikci.yaml` alanı** üçüncü sütun olarak eklendi.
  Böylece hangi cevabın hangi model girdisine gittiği denetlenebilir.
- Katman disiplini eşleme tablosuna yazıldı: 3.1 → **L0**, 3.2 → **L1**, 3.3 → **L2**.
  CIF cevabı (3.3) CSV'de ayrı satıra yazılır, EXW/FOB ile aynı hücreye **girmez**.
- Cevap değerlendirme kontrol listesine 6 yeni madde eklendi (özet tablo doluluğu,
  özet-detay çelişkisi, boş şişe ağırlığı, etiket dahil/hariç, karton dahil/hariç,
  üretim süresi ayrımı).

### Teklif geldiğinde `tedarikci-havuzu.csv`'ye eklenecek yeni kolonlar

`empty_bottle_weight_g`, `filled_bottle_weight_g`, `loading_port`,
`production_time_days`, `carton_cost_per_bottle`, `label_cost_per_bottle`

Bu kolonlar **bu turda eklenmedi**: teklif alınmadığı için 11 satırın tamamı
`UNKNOWN` olurdu ve bu, dosyaya bilgi değil gürültü eklerdi.

---

## 4. BU KONTROLÜN SINIRI

Bu denetim şablonun **sorduğu soruları** doğrular. Doğrulamadığı üç şey vardır:

1. **Tedarikçinin cevaplayacağını** doğrulamaz. 25 alanın hepsini soran bir RFQ'ya
   üreticinin 25 alanı da doldurarak cevap vermesi beklenemez; TUR 1 raporunun
   §9.3'te yazdığı gibi bu beyanlar tedarikçinin pazarlama metnidir ve teklifte de
   seçici olabilir. Doluluk oranı ancak gerçek cevaplar geldiğinde ölçülebilir.
2. **Cevapların doğruluğunu** doğrulamaz. Şablon `INDICATIVE`/`FIRM_OFFER` ayrımını
   zorlar ama bir FIRM_OFFER'ın da tutulacağını garanti etmez.
3. **Soru sayısının cevap oranını düşürüp düşürmediğini** ölçmez. v2.1 ile soru
   sayısı arttı (13 yeni satır). Bu bir risktir ve §5'te işlenmiştir.

---

## 5. BU BULGUYU NE ÇÜRÜTÜR?

### 5.1 "Şablon hazır" sonucunu ne çürütür?

**Cevap oranının çökmesi.** v2.1 ile şablon 13 soru daha uzadı ve toplam 90 satırın
üzerine çıktı. Uzun RFQ'nun tipik sonucu daha eksiksiz cevap değil, **daha az cevap**
olabilir: üretici formu doldurmak yerine kendi standart fiyat listesini PDF olarak
gönderir ve bizim yapılandırılmış tablomuz boş döner. Bu gerçekleşirse "alan kontrolü
tamam" sonucu kâğıt üzerinde doğru, pratikte anlamsız olur.

**Erken uyarı göstergesi:** ilk 8 gönderimde Summary Sheet doldurma oranı %50'nin
altındaysa şablon **kısaltılmalıdır** — S1–S25 tek başına gönderilip Bölüm 1–8 ikinci
aşamaya bırakılabilir. Bu, TUR 7'de ölçülmesi gereken bir metriktir.

### 5.2 Hangi eklenen alan gereksiz çıkabilir?

**3.19 (koli konfigürasyonu değişikliğinin maliyet etkisi)** ve **1.16 (hafif şişe
alternatifi)** spekülatif alanlardır: ikisi de biz henüz koli/şişe tercihi
yapmadığımız için soruluyor. Eğer 12×750 ml standart ve ağır şişe tercih edilmiyorsa
bu iki soru cevap oranını düşüren ölü ağırlıktır.

Buna karşılık **karton (20) ve etiket (19) maliyetinin EXW'ye dahil olup olmadığı
sorusu gereksiz çıkamaz** — bu, L0'ın kapsamını tanımlayan sorudur ve cevapsız
kalırsa iki tedarikçinin EXW'si aritmetik olarak karşılaştırılamaz.

### 5.3 Bu kontrolün en zayıf noktası

Ben bu denetimi **kendi yazdığım şablon üzerinde** yaptım. "VARDI" kararlarının
20'sini kendi TUR 1 çalışmama vererek verdim; bu bir öz-değerlendirmedir ve
sistematik olarak cömert olma eğilimi taşır. Özellikle 14 (port), 22 (annual
capacity) ve 23 (certificate availability) alanlarında "soru var" ile "soru
**yeterince kısıtlayıcı**" arasındaki farkı kendi lehime yorumlamış olabilirim.

Bağımsız kontrol: `seytanin-avukati` şablonu bir tedarikçi gibi okuyup **kaçamak
cevap verilebilecek** satırları işaretlerse bu denetim gerçek anlamda doğrulanmış olur.

### 5.4 Kim, nasıl, ne kadar sürede doğrular?

| # | Ne | Kim | Nasıl | Süre |
|---|---|---|---|---|
| 1 | Şablonun kaçamak cevaba açık satırları | `seytanin-avukati` | Tedarikçi rolüyle şablonu doldurup boşlukları göstermek | 1 gün |
| 2 | Ambalaj bloğunun navlun hesabına yeterliliği | `navlun-lojistik-uzmani` | 2.1–2.13 + 1.14/1.15 ile konteyner doluluk hesabı kurulabiliyor mu (T-402) | 1 gün |
| 3 | Menşe belgesi sorusunun (6.1) doğru belgeleri listeleyip listelemediği | `gumruk-vergi-uzmani` | T-401 kapandıktan sonra 6.1'in daraltılması | T-401 sonrası |
| 4 | Gerçek doluluk oranı | `global-sourcing-kasifi` | ≥8 üreticiye gönderim, Summary Sheet doluluk oranının ölçülmesi | 2–4 hafta (TUR 7) |
