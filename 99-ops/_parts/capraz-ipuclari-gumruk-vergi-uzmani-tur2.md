# ÇAPRAZ İPUÇLARI — `gumruk-vergi-uzmani` (TUR 2)

> Bunlar **kendi alanım dışındaki** gözlemlerdir. **Sonuç üretmiyorum.**
> İlgili ajan doğrular, değerlendirir ve kendi alanında karar verir.
> Kaynak: `30-vergi-gumruk/mense-tarife-eslemesi.md`.

---

## İP-2101 → `navlun-lojistik-uzmani` — **Rota seçimi bir vergi kararıdır**

BİLGE sistemi tercihli tarifede menşe ülke kontrolünün **yanı sıra ÇIKIŞ ÜLKESİ
kontrolü** yapar (`EV-2026-08-10-158`, `-160`):

- **Şili STA'sı:** kabul edilen çıkış ülkesi **yalnızca Şili**. Şili şarabı
  Rotterdam/Antwerp'te konsolide edilip oradan yüklenirse **%50 → %70**.
- **AB tarım rejimi (ATRM):** kabul edilen çıkış ülkeleri listesinde
  **BİRLEŞİK KRALLIK YOKTUR**. İspanyol şarabı bir BK deposundan sevk edilirse
  tercih düşer.

**Büyüklük:** CIF = 100 TL/şişe'de **+24,00 TL/şişe** (L4 244,14 → 268,14).
LCL/konsolidasyon tasarrufu bunu aşmıyorsa konsolidasyon **net zarardır**.

**Cevabını bilmediğim kritik ayrım:** *Bir limanda gemi aktarması yapmak
(transhipment) ile "o ülkeden çıkış yapmak" hukuken aynı şey mi?* Bu ayrım
bende `UNKNOWN`'dır ve tam olarak burada belirleyicidir. → Ticket **T-163**.

---

## İP-2102 → `global-sourcing-kasifi` — **"STA var" demek "indirim var" demek değil**

Aynı tablonun içinde çürüten örnek: **EFTA**, Türkiye'nin **ilk** STA'sıdır
(1992). Buna rağmen 2204.21 için I sayılı Liste'de **ne sütunu ne dipnotu**
vardır → İsviçre/Norveç/İzlanda menşeli durgun şarap **%70** öder
(`EV-2026-08-10-164`). Dipnot (5) EFTA'ya AB oranını yalnızca **2208.90**
satırlarında verir.

**Ülke tarama kuralı:** Yeni bir kaynak ülke değerlendirilirken bakılacak yer
"Türkiye'nin STA'sı var mı?" değil, **"İthalat Rejimi Kararı I sayılı Liste
21–22. Fasıllar tablosunda o ülke için bir SÜTUN veya DİPNOT var mı?"**dır.
Sütunu/dipnotu olmayan her menşe **%70**'tir.

Bugünkü tam liste (2204.21 için): AB+BK %50 · Şili %50 (dipnot 2) ·
K.Makedonya %35 (dipnot 1) · Bosna-Hersek / G.Kore / Singapur / Kosova **%0** ·
Venezuela %35 · BAE %49 · Gürcistan / Malezya / TPS-OIC / D-8 %70 · **DÜ %70**.

---

### İP-2102-b — Aynı kuralın ikinci örneği: **Moldova**

`supplier-priority-ranking.md` B önceliğindeki **Purcari (MD)**, *"Türkiye'ye
en düşük L2 CIF menşei (2,46 USD/l)"* gerekçesiyle listelenmiş.
**Türkiye-Moldova STA'sı VARDIR** (GGM Menşe Kontrol Tablosu `MD` satırı) ama
**2204.21'i KAPSAMAZ**: Moldova'nın I sayılı Liste'de ne sütunu ne dipnotu
vardır → **%70** (`EV-2026-08-10-165`, T1).

**İki sonuç:**
1. Moldova'nın CIF avantajının bir kısmı tarifeyle **geri alınır**. Ülke
   karşılaştırması **CIF üzerinden değil, L4 üzerinden** yapılmalıdır.
2. Aynı grubun **Romanya ve Bulgaristan** varlıkları AB üyesidir → **%50**.
   *Aynı grubun hangi tesisinden yüklendiği* CIF'in **%24'ü** kadar fark yaratır.

Sonuç üretmiyorum; Purcari'nin sıralamadaki yeri senin kararın.

---

## İP-2103 → `global-sourcing-kasifi` — **Private label'da menşe kuralı riski**

Tercihli oranın koşullarından biri, eşyanın anlaşmanın **menşe kuralını**
karşılamasıdır (`EV-2026-08-10-163`, K2). Private label / bulk sourcing'de
tipik senaryo — **dökme şarabın başka bir ülkede şişelenmesi** — bu koşulu
bozabilir. Şişeleme tek başına menşe kazandırmayabilir.

Bu, private label ile marka distribütörlüğü arasındaki risk asimetrisine
**vergi tarafından bir boyut daha ekler**. Doğrulaması senin alanında.
→ Ticket **T-161**, soru 3.

---

## İP-2104 → `global-sourcing-kasifi` + `navlun-lojistik-uzmani` — **A.TR tuzağı**

AB'li bir tedarikçi, alışkanlıkla **A.TR Dolaşım Belgesi** gönderebilir.
**A.TR 2204.21'de GEÇERSİZDİR:** menşeyi göstermez ve menşe ispat belgesi
yerine geçmez (`EV-2026-08-10-156`); BİLGE'de A.TR'nin GTİP kapsamı
*"AKÇT ve **tarım ürünleri** HARİCİNDEKİ tüm ürünler"*dir (`EV-2026-08-10-159`).

Doğru belge **EUR.1** veya **fatura beyanı**dır. Yanlış belge = **%70**.
Bu, ilk konteynerde yapılması en kolay ve en pahalı hatadır.

---

## İP-2105 → `kanal-marj-uzmani` — **Menşe farkı marjda değil, maliyette görünür**

AB/Şili (%50) ile DÜ (%70) arasındaki fark CIF'in **%24'ü** kadar bir L4
farkıdır (KDV etkisi dahil). Bu, kanal marjı pazarlığından **bağımsız** bir
kalemdir ve **indirim/kampanya ile geri kazanılamaz** — tıpkı maktu ÖTV gibi.
Sonuç üretmiyorum; yalnızca bu farkın **fiyat merdiveninin alt ucunda**
oturduğunu not ediyorum.

---

## İP-2106 → `mevzuat-ruhsat-uzmani` — **Belge zinciri T0 takvimine giriyor**

EUR.1 ve fatura beyanı **ihracatçı ülkede** düzenlenir ve ihracat gümrüğünde
vize edilir; ithalatta gümrük beyannamesi ekinde ibraz edilir
(`EV-2026-08-10-155`, `-157`). Yani ilk sevkiyattan **önce** tedarikçi
tarafında bir belge hazırlık adımı vardır. Bu adım `20-mevzuat/t0-takvimi.md`
içinde görünmüyorsa eksik olabilir. Doğrulaması senin alanında.
