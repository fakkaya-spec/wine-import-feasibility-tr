# TOP 10 RFQ TARGETS

```yaml
sahibi:               global-sourcing-kasifi
tur:                  TUR 2 — COMMERCIAL VALIDATION
tarih:                2026-08-10
kaynak:               50-sourcing/supplier-shortlist-v2.csv + supplier-priority-ranking.md
gonderilecek_sablon:  50-sourcing/rfq-template.md (v2.1)
gonderildi_mi:        HAYIR — BU TURDA DIŞ İLETİŞİM YASAKTIR
model_dagilimi:       Model B: 5 · Model A: 4 · İkisi birden: 1
ulke_dagilimi:        ES 3 · PT 2 · IT 1 · FR 2 · CL 1 · AU 1 · MD 1  (11 kayıt = 1 tedarikçi iki model)
```

> **Bu liste bir gönderim listesidir, bir tedarikçi seçimi değildir.**
> Gönderim yalnızca karar `TEST` veya `IMPORT PILOT` ise ve `yatirim-komitesi-baskani`
> onayıyla, TUR 7'de yapılır.
>
> **Model dengesi bilinçlidir:** liste 5 Model B + 4 Model A + 1 ikili olacak
> şekilde kurulmuştur. Saf öncelik sırası uygulansaydı ilk 7'nin 5'i Model B
> olurdu; `00-charter/karar-esikleri.md` iki modeli **eşit öncelikli** tuttuğu
> için `B` grubundan **üç Model A adayı** listeye alınmıştır. Bu bir kanıt
> iddiası değil, bir **kaynak dağıtım kararıdır** ve burada açıkça yazılmıştır.

---

## 1 — HARLAND WINE COMPANY PTY LTD

1. **Şirket:** Harland Wine Company Pty Ltd
2. **Ülke:** Avustralya (South Eastern Australia / Langhorne Creek / Barossa / McLaren Vale)
3. **Neden seçildi:** Havuzdaki **tek üretici** ki MOQ, ödeme şartı, üretim süresi, Incoterm, konteyner doluluğu **ve** şişe başı fiyat kademesini aynı sayfada yayınlıyor. Tek bir RFQ ile en fazla bilinmeyeni kapatır; ayrıca elimizdeki tek "gösterge fiyat ↔ gerçek teklif" eşleştirmesini kurma imkânı sunar (TUR 1 §7.1'de ölçülemediği söylenen sapma).
4. **Model:** Private label (Model B)
5. **MOQ:** **6.000 şişe / şarap** (500×12×750 ml veya 1000×6×750 ml) — `EV-2026-08-10-452`
6. **Bilinen fiyat:** **`PUBLIC_INDICATIVE`** — "Entry Level $2.85+ per bottle" · Mid $5.00+ · Premium $8.50+. **Para birimi kaynakta yazılı DEĞİL.** Tam konteynerde **FOB (L1)**, MOQ siparişinde **ex factory (L0)** — yani aynı sayı iki farklı katmana işaret ediyor (`C-461`). Etiket baskısı fiyata **dahil değil**. — `EV-2026-08-10-451`
7. **İletişim kanalı:** hello@harlandwineco.com.au · https://www.harlandwineco.com.au/private-label
8. **Sorulması gereken kritik 3 soru:**
   1. **"$2.85 hangi para birimidir — AUD mi USD mi?"** (RFQ S11/3.1) Bu tek soru fiyatı ~1,5 kat değiştirir ve cevaplanmadan sayı modele giremez.
   2. **"6.000 şişelik MOQ siparişinde fiyat ex factory ise, aynı ürünün 6.000 şişe için FOB fiyatı ve adı belirtilen limanı nedir?"** (RFQ 3.2, 3.16, 2.10) — L0/L1 ayrımını kapatır.
   3. **"Etiket baskısı hariç deniyor; 6.000 şişelik bir baskı için tek seferlik (klişe/kalıp) ve şişe başı tekrarlayan maliyet nedir?"** (RFQ 4.13) — L0'ın gerçek kapsamını belirler.

---

## 2 — CANTINA DANESE S.R.L. UNIPERSONALE

1. **Şirket:** Cantina Danese s.r.l. Unipersonale
2. **Ülke:** İtalya — Roncà (VR), Veneto
3. **Neden seçildi:** SKU bazlı ve **sayı olarak bilinen** MOQ ile Türkiye'nin **en güçlü ithalat hattı** (İtalya: 5.749.972 litre / 2025, `EV-2026-08-09-405`) aynı tedarikçide buluşuyor. Ayrıca gümrük antreposu işlettiğini ve ihracat evrakını hazırladığını beyan ediyor — dokümantasyon riskini düşürür.
4. **Model:** Private label (Model B)
5. **MOQ:** **6.000 şişe / tek referans (SKU)** — `EV-2026-08-10-453`
6. **Bilinen fiyat:** **YOK.** `quote_class: NONE`. Sitede hiçbir fiyat yayınlanmamıştır. `UNKNOWN`.
7. **İletişim kanalı:** international@cantinadanese.com · +39 045 746 0060 · https://www.cantinadanese.com/private-label
8. **Sorulması gereken kritik 3 soru:**
   1. **"750 ml kuru beyaz için EXW (yer belirtilerek) ve FOB (liman belirtilerek) fiyatınız nedir; 5.000 / 10.000 / 25.000 şişe kademelerinde nasıl değişir?"** (RFQ 3.1, 3.2, 3.7)
   2. **"Portföyünüzde entry/value segmentte hangi beyaz çeşitler var (Trebbiano, Garganega, Pinot Grigio, Chardonnay) ve ABV kaçtır?"** (RFQ 1.2, 1.4) — ürün uyumu hâlâ doğrulanmadı.
   3. **"Türkiye için hangi menşe ispat belgesini düzenleyebiliyorsunuz — EUR.1, fatura beyanı, REX veya A.TR?"** (RFQ 6.1) — cevap ham hâliyle `gumruk-vergi-uzmani`'na iletilir.

---

## 3 — INTERBROSA FAMILY WINES

1. **Şirket:** Interbrosa Family Wines
2. **Ülke:** İspanya
3. **Neden seçildi:** Havuzda **doğrulanmış en düşük MOQ** (3.000 şişe) — 5.000 şişelik pilotu mümkün kılan iki üreticiden biri. İspanya, Türkiye'ye üçüncü en ucuz L2 CIF menşei (2,71 USD/l) ve hat çalışıyor (1.916.118 l/2025).
4. **Model:** Private label (Model B)
5. **MOQ:** **3.000 şişe** (şarap başına 4 palet) — `EV-2026-08-09-408`
6. **Bilinen fiyat:** **YOK.** Etiket/koli/kapsül/mantar **tasarımının** ek ücretsiz olduğu beyan ediliyor — bu bir **tasarım** beyanıdır, **baskı/klişe fiyatı değildir** ve fiyat teyidi sayılmaz.
7. **İletişim kanalı:** **info@interbrosa.es · +34 952 929 521** — ⚠️ **Web sitesi 2026-08-10'da HTTP 503 döndü** (`EV-2026-08-10-467`); bu tedarikçiye **siteden değil, doğrudan e-posta/telefonla** ulaşılmalıdır.
8. **Sorulması gereken kritik 3 soru:**
   1. **"3.000 şişelik MOQ hâlâ geçerli mi ve bu adette EXW/FOB şişe başı fiyat nedir?"** (RFQ 3.6, 3.1, 3.2) — TUR 1'in en kritik tek bulgusunun teyidi.
   2. **"Tasarım ücretsizse, klişe/kalıp/kesim bıçağı gibi tek seferlik baskı maliyetleri ayrıca fatura ediliyor mu?"** (RFQ 4.13a) — "ücretsiz" ile "maliyetsiz" arasındaki farkı kapatır.
   3. **"Türkçe arka etiketi kendi tesisinizde uygulayabiliyor musunuz?"** (RFQ 4.6) — evet ise Türkiye'deki etiketleme operasyonu tamamen kalkar (L5 kalemi).

---

## 4 — THE WINE FACTORY (SARL)

1. **Şirket:** The Wine Factory (SARL)
2. **Ülke:** Fransa — Bordeaux (Gornac) + Languedoc (Valros)
3. **Neden seçildi:** MOQ **ve** üretim süresi birlikte bilinen **tek** tedarikçi; `peak_cash_requirement` için gereken iki girdinin ikisi de elimizde. Fransa hattı çalışıyor (2.851.454 l/2025).
4. **Model:** Private label (Model B)
5. **MOQ:** **3.600 şişe** — `EV-2026-08-09-410`
6. **Bilinen fiyat:** **YOK.** `UNKNOWN`. Üretim süresi 4–6 hafta (ödeme sonrası) — bu ifade **peşin ödeme** ipucudur ama şart olarak doğrulanmamıştır.
7. **İletişim kanalı:** https://www.twf-wines.com/ · +33 5 56 61 91 12 (Bordeaux) · +33 4 67 76 50 24 (Languedoc)
8. **Sorulması gereken kritik 3 soru:**
   1. **"Languedoc tesisinizden entry segment beyaz için EXW ve FOB fiyatı nedir?"** — Bordeaux ile Languedoc **aynı fiyat noktası değildir**; RFQ 3.1 zaten "EXW `<yer>`" zorunlu tutuyor.
   2. **"'Ödeme sonrası üretim' ifadesi %100 peşin mi demek; ikinci siparişten itibaren vade mümkün mü?"** (RFQ 3.8, 3.9, 3.10) — KKDF ve CCC girdisi.
   3. **"Côtes de Gascogne veya benzeri IGP'de Colombard-Chardonnay tarzı bir blend üretebilir misiniz, minimum parti nedir?"** (RFQ 4.4) — ürün tanımıyla eşleşmeyi test eder.

---

## 5 — CORTA HOJAS EXPORT WINE

1. **Şirket:** Corta Hojas Export Wine
2. **Ülke:** Şili — Curicó, Maule
3. **Neden seçildi:** Beyaz portföyü (**Sauvignon Blanc, Chardonnay**) görev tanımındaki ürün listesiyle birebir eşleşen **tek doğrulanmış Şili üreticisi**; %100 ihracat odaklı; Şili hattı çalışıyor (946.350 l/2025, L2 CIF 2,89 USD/l).
4. **Model:** Private label (Model B)
5. **MOQ:** **UNKNOWN** — 2026-08-10'da yeniden okundu, hâlâ yayınlanmamış (`EV-2026-08-10-464`). Bu bir **negatif bulgudur**, eksik araştırma değildir.
6. **Bilinen fiyat:** **YOK.** `quote_class: NONE`. Fiyat, Incoterm ve lead time da yayınlanmamış.
7. **İletişim kanalı:** info@cortahojas.com · +56 75 2315 328 · https://www.cortahojas.com/private-labels-wines.php
8. **Sorulması gereken kritik 3 soru:**
   1. **"MOQ'nuzu iki birimde birden verir misiniz: (a) SKU başına minimum şişe, (b) sevkiyat başına minimum konteyner?"** (RFQ 3.6a/3.6b) — `C-401`'in doğrudan cevabı.
   2. **"Varietal kademesinde Sauvignon Blanc ve Chardonnay için EXW ve FOB (Valparaíso/San Antonio) fiyatınız nedir?"** (RFQ 3.1, 3.2, 2.10)
   3. **"Türkiye'ye daha önce ihracat yaptınız mı; yaptıysanız hangi ithalatçıya, hangi yıllarda, hangi hacimde?"** (RFQ 6.6) — ihracat bölgeleri listenizde Türkiye anılmıyor.

---

## 6 — BODEGAS SAN VALERO (GRUPO BSV)

1. **Şirket:** Bodegas San Valero (Grupo BSV)
2. **Ülke:** İspanya — DOP Cariñena, Aragón
3. **Neden seçildi:** Havuzdaki **tek doğrulanmış ikili aday** (hem kendi markaları hem perakendeci markası). Tek bir RFQ, iki iş modelinin fiyat farkını **aynı maliyet tabanı üzerinde** ölçebilir — charter'ın "iki model eşit öncelikli" kuralını **kanıtla** test etmenin en ucuz yoludur.
4. **Model:** **İKİSİ BİRDEN** — Model A (Particular vb. kendi markaları) + Model B (private label)
5. **MOQ:** **UNKNOWN** — `EV-2026-08-10-461`
6. **Bilinen fiyat:** **YOK.** `quote_class: NONE`. Ölçek bilgisi var (2,5 m koli/yıl, 40+ ülke, satışların %70'i ihracat) ama bunlar fiyat değildir.
7. **İletişim kanalı:** https://www.sanvalero.com/ · fuar profili: https://wineparis.com/exhibitor/bodega-san-valero
8. **Sorulması gereken kritik 3 soru:**
   1. **"Aynı beyaz şarap için (a) kendi markanızla, (b) bizim markamızla şişe başı EXW fiyatınız nedir?"** (RFQ 3.0, 3.1, 4.2) — **iki modelin fiyat farkını doğrudan ölçen tek soru.**
   2. **"Private label hizmeti sunduğunuz bir sektör yayınında belirtildi; bunu teyit eder misiniz ve private label MOQ'nuz standart MOQ'nuzdan farklı mı?"** (RFQ 4.1, 4.3)
   3. **"Türkiye'de hâlihazırda bir ithalatçınız var mı; bölge kapalı mı?"** (RFQ 5.2) — Model A adaylığının ön koşulu.

---

## 7 — CASA SANTOS LIMA

1. **Şirket:** Casa Santos Lima
2. **Ülke:** Portekiz — Alenquer (Lisboa) + 5 bölge
3. **Neden seçildi:** Model A'nın **en olgun** adayı: ~50 ülke, üretimin ~%90'ı ihracat, kendi markaları (Quinta da Espiga, Quinta das Setencostas, Palha-Canas) mevcut ve Portekiz hattı çalışıyor (324.828 l/2025, L2 CIF 3,20 USD/l).
4. **Model:** Existing brand distribution (Model A)
5. **MOQ:** **UNKNOWN** — `EV-2026-08-09-418`
6. **Bilinen fiyat:** **YOK.** `quote_class: NONE`.
7. **İletişim kanalı:** https://www.casasantoslima.com/en/contact/ (kurumsal iletişim formu)
8. **Sorulması gereken kritik 3 soru:**
   1. **"Türkiye'de bir ithalatçınız/distribütörünüz var mı ve bölge kapalı mı; bu markalar Türkiye'de daha önce satıldı mı, neden durdu?"** (RFQ 5.2, 5.3) — **Model A'nın varlık koşulu.**
   2. **"Türkiye için münhasırlık verir misiniz; hangi yıllık hacim taahhüdü karşılığında ve ithalatçıya bir markup/yeniden satış fiyatı tavanı uygular mısınız?"** (RFQ 5.4, 5.5, 5.7) — `kanal-marj-uzmani`'nın kanal marjı hesabını doğrudan kısıtlar.
   3. **"Value segmentte hangi beyaz SKU'lar Türkiye'ye uygundur ve bunlarda EXW/FOB şişe fiyatı nedir?"** (RFQ 5.1, 3.1, 3.2)

---

## 8 — VIDIGAL WINES S.A.

1. **Şirket:** Vidigal Wines S.A.
2. **Ülke:** Portekiz — Leiria bölgesi
3. **Neden seçildi:** İhracat oranı ~%90, 30+ ülke, 3 m+ şişe/yıl. Amiral markası **Porta 6** uluslararası perakendede listelenmiş bir **entry/orta segment** markadır — yani "raf için kurulmuş marka" arayışına yapısal olarak uyar ve distribütör arayan bir profil sergiler.
4. **Model:** Existing brand distribution (Model A)
5. **MOQ:** **UNKNOWN** — `EV-2026-08-10-456`
6. **Bilinen fiyat:** **YOK.** `quote_class: NONE`.
7. **İletişim kanalı:** Wine Paris katılımcı profili — https://wineparis.com/newfront/exhibitor/vidigal-wines-sa ⚠️ Kurumsal site (vidigalwines.com) 2026-08-10'da porta6.com'a yönlendiriyor ve yaş doğrulama duvarının arkasında; **fuar kanalı üzerinden ulaşılmalıdır.**
8. **Sorulması gereken kritik 3 soru:**
   1. **"Portföyünüzde 750 ml kuru BEYAZ value SKU var mı; hangi çeşitlerle ve hangi ABV'de?"** (RFQ 1.2, 1.4, 5.1) — beyaz portföy hâlâ tamamen UNKNOWN, ürün uyumunun ön koşulu.
   2. **"Porta 6 veya diğer markalarınız Türkiye'de hâlihazırda satılıyor mu; bölge açık mı?"** (RFQ 5.2, 5.3)
   3. **"Model A yanında bizim markamızla (private label) üretim yapar mısınız; MOQ farkı nedir?"** (RFQ 4.1, 4.3) — iki modeli aynı firmada test etme fırsatı.

---

## 9 — PLAIMONT (VIGNERONS EN GASCOGNE)

1. **Şirket:** Plaimont — Vignerons en Gascogne & Piémont Pyrénéen
2. **Ülke:** Fransa — Saint-Mont, Gaskonya (IGP Côtes de Gascogne)
3. **Neden seçildi:** **Havuzun en güçlü ürün eşleşmesi.** Görev tanımı örnek blend olarak açıkça "Colombard-Chardonnay" veriyor; Côtes de Gascogne bu stilin **yapısal kaynağıdır** ve Plaimont'un Colombelle markası apelasyonun amiral markasıdır. TUR 1'de Fransa "f/p için yapısal olarak zorlayıcı" diye Grup 4'e konmuştu — **Gascogne bu genellemenin sınanması gereken istisnasıdır.**
4. **Model:** Existing brand distribution (Model A) — private label kabiliyeti **UNKNOWN**
5. **MOQ:** **UNKNOWN** — `EV-2026-08-10-459`
6. **Bilinen fiyat:** **YOK.** `quote_class: NONE`. ⚠️ Karşı sinyal: Fransa'nın Türkiye'ye L2 CIF birim değeri **6,27 USD/l**'dir — segmentin **çok üstünde**. Gascogne'un bu ortalamanın altında olduğu **doğrulanmamıştır**; bu RFQ'nun cevaplayacağı asıl sorudur.
7. **İletişim kanalı:** https://www.plaimont.com/en/contact · +33 (0)5 62 69 62 87
8. **Sorulması gereken kritik 3 soru:**
   1. **"IGP Côtes de Gascogne Colombard / Colombard-Chardonnay için 25.000 şişe/yıl hacminde EXW ve FOB (adı belirtilen liman) fiyatınız nedir?"** (RFQ 3.1, 3.2, 3.7) — **Fransa'nın segment dışı olup olmadığını belirleyen tek soru.**
   2. **"Türkiye'de bir ithalatçınız var mı ve Colombelle markası için bölge açık mı?"** (RFQ 5.2)
   3. **"Kooperatif olarak müşteri markası (private label) üretiyor musunuz; MOQ ve ek lead time nedir?"** (RFQ 4.1, 4.2, 4.11)

---

## 10 — PURCARI WINERIES GROUP

1. **Şirket:** Purcari Wineries Group (Château Purcari · Bostavan · Crama Ceptura · Domeniile Cuza · Angels Estate)
2. **Ülke:** Moldova (+ Romanya, Bulgaristan) — üçü de Türkiye'ye fiilen ihracat yapan menşeler
3. **Neden seçildi:** Moldova, Türkiye'ye **en düşük L2 CIF birim değerine sahip menşedir** (2,46 USD/l) ve hat iki yıl üst üste çalışmıştır (2.038.906 l/2025, `EV-2026-08-09-405`). Ayrıca grup **Bükreş Borsası'nda işlem gören halka açık bir şirkettir** — denetlenmiş finansalları olan, tedarikçi sağlamlığı en şeffaf doğrulanabilir adaydır. Charter'ın 9 öncelikli ülkesinde değildir; ekleme gerekçesi budur.
4. **Model:** Existing brand distribution (Model A) — private label **UNKNOWN**
5. **MOQ:** **UNKNOWN** — `EV-2026-08-10-462`
6. **Bilinen fiyat:** **YOK.** `quote_class: NONE`. Grup geliri 437,2 m RON (2025) yayınlanmıştır ancak **hacim kırılımı olmadığı için şişe başı fiyat türetilemez** — türetmek uydurma olurdu. ⚠️ Karşı sinyal: grup kendini *"the most premium wines from Moldova and Romania"* diye konumlandırıyor.
7. **İletişim kanalı:** purcari@purcari.wine · +373 22 856 022 · https://purcariwineries.com/contacts/
8. **Sorulması gereken kritik 3 soru:**
   1. **"Grubunuzun value/entry segmentinde (Bostavan gibi) 750 ml kuru beyaz SKU'ları var mı ve EXW/FOB fiyatı nedir?"** (RFQ 5.1, 3.1, 3.2) — "premium" konumlandırmasının segmentimizi dışlayıp dışlamadığını doğrudan test eder.
   2. **"Türkiye'ye ihracat geçmişiniz var mı; hangi ithalatçı, hangi yıllar, hangi hacim?"** (RFQ 6.6) — Moldova hattı **ülke düzeyinde** çalışıyor; bu firmanın o hacimdeki payı bilinmiyor.
   3. **"Türkiye için hangi menşe ispat belgesini düzenleyebiliyorsunuz ve Moldova, Romanya, Bulgaristan menşeleri arasında belge tipi farkı var mı?"** (RFQ 6.1) — üç menşe **üç ayrı hukuki gruptadır**; cevap ham hâliyle `gumruk-vergi-uzmani`'na (T-401, T-462) iletilir.

---

## GÖNDERİM ÖNCESİ ZORUNLU KONTROLLER

| # | Kontrol | Sorumlu | Neden |
|---|---|---|---|
| 1 | `T-401` / `T-462` kapanmalı — hangi ülke hangi menşe belgesi grubunda | `gumruk-vergi-uzmani` | RFQ 6.1 ancak bu cevaptan sonra daraltılabilir; yoksa 10 üreticiye 10 farklı belirsiz soru gider |
| 2 | `T-464` cevaplanmalı — Model A adaylarının Türkiye'de ithalatçısı var mı | `turkiye-pazar-kasifi` | Cevap "var" ise 4 Model A hedefi listeden düşer ve yerlerine B grubundan yenileri gelir |
| 3 | `<VOLUME>` ve `<PILOT VOLUME>` doldurulmalı | `yatirim-komitesi-baskani` | RFQ şablonu bu alanlar boşken geçersizdir (rfq-template.md §0.9) |
| 4 | Tüm 10 hedefe **aynı metin** gitmeli | `global-sourcing-kasifi` | Metin değişirse teklifler karşılaştırılamaz (rfq-template.md §0.8) |
| 5 | Gönderim onayı | `yatirim-komitesi-baskani` | Karar `TEST` veya `IMPORT PILOT` değilse gönderim yapılmaz |
