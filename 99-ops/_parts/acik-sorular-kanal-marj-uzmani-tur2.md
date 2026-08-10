# AÇIK SORULAR — kanal-marj-uzmani, TUR 2

> Bu bir **parça dosyasıdır**. `99-ops/acik-sorular.md` ana dosyasına
> `yatirim-komitesi-baskani` tarafından birleştirilir. Bu ajan ana dosyaya
> **DOKUNMAMIŞTIR**.
>
> Ticket'a dönüşmeyen, ama kapanmadan modelin güvenilir olmayacağı sorular.

---

| # | Soru | Neden açık kaldı | Kritiklik | Nasıl kapanır |
|---|---|---|---|---|
| **OQ-601** | Türkiye'de zincir marketin **şarap kategorisi** brüt marjı nedir? | Rekabet Kurumu'nun beş büyük zincir analizi **"alkol ve tütün hariç"** tanımlıdır ve yayımlanan tüm marj oranları **ticari sır olarak karartılmıştır** (`EV-2026-08-10-611`) | **CRITICAL** | Yalnızca gerçek yıllık anlaşma müzakeresi (`T-604`) |
| **OQ-602** | Şarapta zincir **listeleme / giriş bedeli** tutarı nedir ve birimi nedir (SKU mu, mağaza mı, zincir mi)? | Güncel kamu kaynağı yok; tek iz 2004 tarihli T5 dergi haberi (`EV-2026-08-10-619`) | **CRITICAL** | `T-604` |
| **OQ-603** | HoReCa çarpanı hangi katmandan hesaplanır ve gerçek değeri nedir? | Tek kaynak 2012 tarihli köşe yazısı ve **kendi içinde iki farklı katman** verir (`EV-2026-08-10-618`, `C-602`) | HIGH | Gerçek restoran menü örneklemi (fiziksel) + HoReCa görüşmesi |
| **OQ-604** | Tekel bayii alış-satış farkı nedir? | Yalnızca çelişen T5 kaynaklar; hiçbiri margin/markup ve KDV tabanını belirtmiyor (`EV-2026-08-10-620`, `C-602`) | HIGH | Gerçek bayi görüşmesi / gerçek fiyat listesi |
| **OQ-605** | Dış distribütör marj oranı nedir? | **Hiçbir kanıt bulunamadı.** Ne T4 ne T5. | **CRITICAL** | Distribütör görüşmesi (`T-604`) — A/B dağıtım kararı bunsuz verilemez |
| **OQ-606** | Şarapta zincir **iade oranı** ve iade koşulları nedir? | Yasal düzenleme yok (`EV-2026-08-10-606`); tamamen sözleşmesel | HIGH | `T-604` |
| **OQ-607** | Kaç satış noktası, rakiplerin **5 yıllık şarap alım sözleşmeleri** ile bağlı? | Rekabet Kurulu kararındaki sözleşme sayısı tabloları **karartılmış** (`EV-2026-08-10-614`) | HIGH | Saha gözlemi / bayi görüşmesi. **Bu, listeleme bedelinden daha ölümcül bir erişim engeli olabilir.** |
| **OQ-608** | Zincirlerin şaraba ayırdığı **raf/SKU kotası** nedir? | Hiçbir kamu kaynağı yok. `EV-2026-08-10-624`: ithalat, iç piyasa şarap arzının **%4'ü** (2020, TADB) → ithal şaraba ayrılan raf da dar olmalı, ama **ölçülmedi** | MEDIUM | Fiziksel mağaza turu (`T-603` ile birlikte) |
| **OQ-609** | Zincir market **modern kanal** nokta sayısı (alkol satan) kaçtır? | TADB tablosunda modern kanal **kasten yoktur** (merkezi alım) (`EV-2026-08-10-613`) | MEDIUM | TADAB satış belgesi listeleri / zincirlerin kendi beyanı |
| **OQ-610** | Şarap, 6585 m.7/3 anlamında "tarım ve gıda ürünü" müdür? | Hukuki niteleme bu ajanın alanı değil | **CRITICAL** | `T-601` (`mevzuat-ruhsat-uzmani`) |
| **OQ-611** | 2015'teki "prim/bedele konu ürün sözleşme süresince rafta satışa sunulmalıdır" koruması 2024 metninde var mı? | Konsolide metinde görünmüyor ama **T1 doğrulaması yapılamadı** (`EV-2026-08-10-622`) | HIGH | `T-601` |
| **OQ-612** | Metro **mağaza fiyatı** ile **sevkiyat (Gastro Servis) fiyatı** arasındaki fark nedir? | `İP-501` / `T-506`; Metro fiyatları müşteri numarasına özel (`İP-505`) | HIGH | Metro müşteri kaydı + gerçek teklif (`T-604`) |
| **OQ-613** | HoReCa'da **tadım / eğitim etkinliği** kanal maliyeti olarak modellenebilir mi? | Kabul edilmiş iş kısıtının (`İP-2001`) kapsam belirsizliği; **bu ajan kısıtı yeniden araştırmamıştır** (kurucu kararı) | MEDIUM | Başkan kararı (`T-604` içinde soruldu) — modelleme kararıdır, hukuki soru değildir |
| **OQ-614** | Satış temsilcisi ücret çarpanı (× asgari ücret), araç maliyeti, 3PL birim fiyatı? | Şirket verisi ve gerçek teklif gerektirir | HIGH | Kurucu + 3PL teklifleri (`kendi-dagitim-senaryosu.md` §11) |
| **OQ-615** | Şarabın kanal bazında **ciro dağılımı** (zincir / tekel / HoReCa) nedir? | Kamuya açık veri bulunamadı; elde yalnızca **nokta sayısı** var ve nokta sayısı ciro payı değildir | **CRITICAL** | `T-603` — **ağırlıklı ortalama marj bu olmadan hesaplanamaz** |

---

## Bu turda BİLİNÇLİ OLARAK YAPILMAYANLAR

- 7584 s.K. / reklam kısıtının **kapsamı yeniden araştırılmadı** (kurucu kararı,
  `T-205`, `İP-2001`). Kısıt bir **veri** olarak kullanıldı.
- Hiçbir perakendeciye, distribütöre, HoReCa işletmesine **e-posta / form / mesaj
  gönderilmedi** (görev kısıtı).
- Vergi oranı, navlun tutarı, ruhsat prosedürü, tedarikçi fiyatı konularında
  **sonuç üretilmedi**.
- `599,90 TL`'den **geriye marj türetilmedi** (`pazar.yaml` K2/K4).
- `pazar.yaml`, `10-evidence/index.csv`, `99-ops/*.md` ana dosyaları,
  `99-ops/tickets/INDEX.md` ve diğer ajanların yaml dosyalarına **dokunulmadı**.
- `T-205`'in statüsü **değiştirilmedi**; yalnızca sonuna bir **kullanım kaydı** eklendi.
