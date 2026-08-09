# AÇIK SORULAR — gumruk-vergi-uzmani (TUR 1, 2026-08-09)

> Bu turda cevaplanamayan, cevabı modeli veya kararı etkileyen sorular.
> Kritiklik sırasına göre.

---

## OQ-G01 — İthalatta ödenen KDV indirilebilir mi? (CRITICAL)
**Neden kritik:** CLAUDE.md §6 KDV'yi iki perspektifle göstermeyi zorunlu kılıyor.
İndirilebiliyorsa KDV L5'e taşınmaz ve yalnız nakit akışını etkiler; indirilemiyorsa
şişe başına ~40–45 TL doğrudan ekonomik maliyettir. Bu, tüm marj hesabını değiştirir.
**Bu turda neden çözülemedi:** KDV Kanunu md.29 vd. genel indirim mekanizması
mevcut, ancak alkollü içki ticaretine özgü bir sınırlama olup olmadığı
T1/T2 ile doğrulanamadı.
**Nasıl bulunur:** 3065 sayılı Kanun md.29–34 ve KDV Genel Uygulama Tebliği'nin
indirim bölümü; GİB özelgeleri.
**Sorumlu:** `gumruk-vergi-uzmani` (TUR 5).
**Geçici çözüm:** Model iki senaryo (A1 indirilebilir / A2 indirilemez) ile çalıştırılır.

---

## OQ-G02 — Şarapta ithalatta gözetim uygulaması gerçekten yok mu? (CRITICAL)
**Neden kritik:** Gözetim varsa birim kıymet eşiğinin altında beyan fiilen
kullanılamaz ve ucuz sourcing stratejisi çöker (`matrah-sirasi.md` §2).
**Bu turda ne yapıldı:** Mevzuat Bilgi Sistemi tebliğ veri tabanında
"2204.21", "2204.29", "22.04" tam metin araması yapıldı — hiçbir gözetim tebliği
eşleşmedi. Yöntem, bilinen bir gözetim GTİP'i (8536.20.10.00.11) ile kontrol
edildi ve ilgili tebliğ (2008/11) doğru bulundu.
**Neden yeterli değil:** Negatif arama sonucu yokluğun kanıtı değildir; veri
tabanı kapsamı ve mülga/geçici tebliğler doğrulanmadı.
**Nasıl kapanır:** Ticaret Bakanlığı İthalat Genel Müdürlüğü'nün yürürlükteki
gözetim tebliğleri listesi veya bir gümrük müşavirinden GTİP bazlı teyit.
**evidence_id:** EV-2026-08-09-125

---

## OQ-G03 — KKDF matrahı tam olarak nedir? (HIGH — vadeli senaryoda CRITICAL)
**Neden önemli:** 2011/2304 sayılı Karar md.4 yalnızca **oranı** (%6) ve
tetikleyici ödeme şekillerini tanımlıyor; matrahın mal bedeli mi, CIF mi,
yoksa vadeli ödenen kısım mı olduğu Karar metninde yok.
**Baz senaryoya etkisi:** Peşin ödemede KKDF = 0 olduğu için **etkisiz**.
Vadeli ödeme senaryosunda CIF üzerinden %6, şişe başı maliyeti anlamlı ölçüde
değiştirir.
**Nasıl bulunur:** Gümrükler Genel Müdürlüğü KKDF genelgeleri; Hazine ve Maliye
Bakanlığı KKDF tebliğleri.
**Ticket:** T-105

---

## OQ-G04 — Antrepodan kısmi çekiş (partial release) mümkün mü ve maliyeti nedir? (HIGH)
**Neden önemli:** Mümkünse `peak_cash_requirement` dramatik biçimde düşer.
Bir konteyner (≈10.000–13.000 şişe) tek seferde vergilendirilirse şişe başı
~150–200 TL vergi × 12.000 şişe = 2 milyon TL mertebesinde peşin nakit gerekir.
**Bu turda ne bulundu:** Gümrük Kanunu md.101/1 antrepoda sınırsız kalış süresi
tanıyor; md.181/1-a vergiyi serbest dolaşıma giriş beyannamesinin tesciline
bağlıyor. Kısmi çekişe dair açık bir T1 hüküm bu turda bulunamadı.
**Ticket:** T-101 → `navlun-lojistik-uzmani` (antrepo onun alanında)

---

## OQ-G05 — Menşe ispat belgesi türü nedir? (MEDIUM)
**Neden önemli:** AB/BK/Şili için %50 indirimli oranın kullanılabilmesi belge
şartına bağlıdır. Belge alınamazsa DÜ %70 uygulanır — 20 puanlık fark.
**Bu turda çözülemedi:** EUR.1 / fatura beyanı / REX / A.TR ayrımı anlaşma
bazında doğrulanamadı. Şarap tarım ürünü olduğu için A.TR'nin (serbest dolaşım
belgesi) tek başına yeterli olmayacağı, menşe ispatı gerekeceği yapısal olarak
beklenir ancak **belgelenmedi**.
**Nasıl bulunur:** Türkiye-AB 1/98 sayılı Ortaklık Konseyi Kararı menşe
protokolü; Gümrük Yönetmeliği tercihli menşe hükümleri.

---

## OQ-G06 — 12 haneli GTİP alt kırılımı hangisi? (LOW — vergiyi değiştirmiyor)
**Neden düşük öncelikli:** 2204.21/22/29 altındaki 113 GTİP satırının tamamında
AB=%50, DÜ=%70 aynı; ÖTV 22.04 pozisyon seviyesinde. Alt kod **vergi yükünü
değiştirmiyor** (EV-2026-08-09-102).
**Neden yine de gerekli:** Gümrük beyannamesi 12 haneli kod ister.
**Bu turda neden çözülemedi:** 2026 Türk Gümrük Tarife Cetveli (CBK 10781,
RG 30/12/2025) PDF'i **taranmış görüntü** olarak yayımlanmış, metin katmanı yok;
TARA tarife arama motoru CAPTCHA korumalı.
**Nasıl bulunur:** Gümrük müşaviri, TARA (manuel), veya AB Kombine Nomenklatürü
2026 (8 hane için) + TGTC (son 4 hane için).

---

## OQ-G07 — Gümrük beyannamesi damga vergisi 2026 tutarı? (LOW)
Maktu ve küçük bir kalem, ancak `UNKNOWN` bırakıldı. Beyanname başına düşer,
şişe başına etkisi ihmal edilebilir düzeyde olması beklenir — ancak
**varsayılmadı**.

---

## OQ-G08 — Model hedef tarihinde hangi ÖTV tutarı geçerli olacak? (CRITICAL — zamanlama)
`00-charter/kapsam.md` model hedef tarihini TBD bırakmış. ÖTV maktu tutarı
**Ocak ve Temmuz'da otomatik artıyor** (EV-2026-08-09-114). İlk konteynerin
gümrükten çıkış tarihi 2027 Ocak'ı geçerse, bugünkü 71,2692 TL/lt **geçersizdir**.
**Bağımlılık:** `mevzuat-ruhsat-uzmani`'nın T0 takvimi.
**Ticket:** T-104 → `finans-fizibilite`
