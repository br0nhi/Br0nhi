---
name: youtube-monetization-analyzer
description: Analizira YouTube kanal (podrazumijevano @harlibee) u odnosu na YouTube politike monetizacije (YPP), s posebnim fokusom na "inauthentic content" politiku. Koristi kada korisnik traži provjeru kanala prije ponovne prijave za monetizaciju, procjenu rizika pojedinačnih videa, ili pitanja o autentičnosti sadržaja. Primjeri poziva - "analiziraj moj kanal", "provjeri monetizaciju", "da li je ovaj video inauthentic".
---

# YouTube Monetization Analyzer

Analiziraš YouTube kanal u odnosu na YouTube Partner Program (YPP) politike monetizacije,
s posebnim fokusom na **inauthentic content** politiku (na snazi od 15. jula 2025).

## Kontekst kanala (podrazumijevano)

- Kanal: **@harlibee** (https://www.youtube.com/@harlibee)
- Niša: **islamske historijske priče** (jedna niša, kanal revidiran nakon gubitka monetizacije)
- Historija: monetizacija ukinuta zbog "inauthentic content"; rok od 90 dana za ponovnu
  prijavu ističe **27. jula 2026**. Cilj analize je da kanal prođe ponovnu YPP reviziju.
- Ako korisnik navede drugi kanal ili video kao argument, analiziraj taj umjesto podrazumijevanog.

## Radni tok

### Korak 1: Učitaj referentne politike

Pročitaj `references/ypp-policies.md` i `references/inauthentic-content-checklist.md` iz
direktorija ovog skilla. Zatim pokušaj dohvatiti AŽURNE verzije zvaničnih politika
(politike se mijenjaju — bundlirane reference su rezerva, ne izvor istine):

1. `WebFetch` na https://support.google.com/youtube/answer/1311392 (YouTube channel monetization policies)
2. `WebFetch` na https://support.google.com/youtube/answer/97527 (reused/inauthentic content)
3. Ako zvanične stranice vrate 403/grešku, koristi `WebSearch` za najnovije izmjene
   ("YouTube inauthentic content policy update" + tekuća godina) i osloni se na bundlirane reference.

Ako ažurne politike odstupaju od bundliranih referenci, **ažurne imaju prednost** — i
napomeni korisniku šta se promijenilo.

### Korak 2: Prikupi podatke o kanalu

Pokušaj metode ovim redoslijedom (prva koja uspije):

1. **`youtube-connector-mcp` MCP alati** — ako je MCP server konfigurisan (vidi
   `.mcp.json` u korijenu repozitorija; zahtijeva env varijablu `YOUTUBE_API_KEY`),
   ovo je preferirana metoda jer daje strukturirane podatke bez pokretanja skripti:
   - `youtube_get_channel` za osnovne podatke o kanalu (pretplatnici, opis, ukupni pregledi)
   - `youtube_list_playlists` + `youtube_get_playlist` (uploads playlist) za listu videa
   - `youtube_get_video` za detalje pojedinačnog videa (trajanje, opis, statistika, tagovi)
   - `youtube_get_transcript` za tekst naracije (ključno za procjenu da li je skripta
     originalno autorsko djelo ili čitanje tuđeg teksta)
   - `youtube_get_comments` za signale autentičnosti (komentari o narativu, žalbe na sadržaj)
2. **YouTube Data API skripta** — ako MCP alati nisu dostupni, a postoji env varijabla
   `YOUTUBE_API_KEY`, pokreni:
   ```
   python3 scripts/fetch_channel.py @harlibee
   ```
   Skripta ispisuje JSON sa listom videa (naslov, opis, trajanje, datum objave, tagovi, broj pregleda).
3. **yt-dlp** — ako je instaliran: `yt-dlp --flat-playlist -J "https://www.youtube.com/@harlibee/videos"`
   (skripta iz tačke 2 automatski pokušava i ovaj fallback).
4. **WebFetch/WebSearch** — dohvati stranicu kanala i /videos tab; ako je blokirano,
   pretraži "site:youtube.com @harlibee" za listu videa.
5. Ako ništa ne uspije, zatraži od korisnika da nalijepi listu videa (naslov + kratak opis
   formata: narator, vrsta vizuala, dužina) i nastavi analizu na osnovu toga. NE izmišljaj
   videe koje nisi vidio.

Za svaki video prikupi što više od: naslov, opis, trajanje, datum objave, thumbnail stil,
te (ako je moguće, preko transkripta) prirodu naracije i vizuala.

### Korak 3: Analiza po videu

Za svaki video prođi kroz checklistu iz `references/inauthentic-content-checklist.md` i
dodijeli ocjenu rizika:

- 🔴 **VISOK** — vjerovatno bi bio označen kao inauthentic/reused content; ukloniti,
  prebaciti na "unlisted" ili suštinski preraditi PRIJE ponovne prijave
- 🟡 **SREDNJI** — granični slučaj; navedeni konkretni signali rizika i konkretna dorada koja ga spušta na nizak
- 🟢 **NIZAK** — u skladu s politikama

Ključna pitanja za nišu "islamske historijske priče" (tipično storytelling format):
- Da li videi djeluju šablonski (isti template, ista struktura, minimalna varijacija)?
- Da li je naracija TTS/AI glas bez ličnog autorskog doprinosa, ili stvarna autorska naracija?
- Da li su vizuali slideshow statičnih/stock/AI slika bez narativa, ili montiran sadržaj s dodanom vrijednošću?
- Da li je skripta originalno autorsko djelo (vlastito istraživanje, komentar, perspektiva)
  ili čitanje tuđeg teksta (Wikipedia, članci, tuđi videi)?
- Da li tempo objavljivanja sugeriše masovnu produkciju (mnogo videa u kratkom periodu)?
- Ima li preuzetog materijala (isječci iz filmova/dokumentaraca/tuđih videa) bez značajne transformacije?

VAŽNO: ako iz dostupnih podataka ne možeš utvrditi npr. vrstu naracije ili vizuala,
označi to kao "nepoznato — potrebna ručna provjera" umjesto da nagađaš, i postavi
korisniku ciljana pitanja.

### Korak 4: Analiza na nivou kanala

Pored pojedinačnih videa, ocijeni cjelinu:
- **Konzistentnost niše**: da li SVI preostali videi prate nišu islamskih historijskih priča?
  Ostaci starog (miješanog) sadržaja su rizik — YouTube pri ponovnoj prijavi gleda cijeli kanal.
- **Varijacija između videa**: da li se videi međusobno dovoljno razlikuju (struktura, vizuali,
  dužina) ili izgledaju kao serija iz istog kalupa?
- **Signali autentičnosti**: opis kanala, "About" sekcija, prisustvo autora (glas, lice,
  vodeni žig, community postovi), izvori navedeni u opisima.
- **Ostale YPP prepreke**: Community Guidelines strajkovi, copyright claimovi, advertiser-friendly
  smjernice, pragovi (1000 pretplatnika + 4000h gledanja / 10M Shorts pregleda), disclosure
  za AI/izmijenjeni sadržaj (Altered content oznaka).

### Korak 5: Izvještaj

Napiši izvještaj **na bosanskom jeziku** u ovoj strukturi:

1. **Presuda** — jedna rečenica: spreman za ponovnu prijavu / nije spreman + šta je blokator
2. **Tabela videa** — naslov | ocjena rizika | glavni razlog (najrizičniji prvi)
3. **Nalazi na nivou kanala**
4. **Plan akcije prije ponovne prijave** — konkretni, prioritizovani koraci s rokom
   (podsjeti na deadline 27. juli ako je relevantan)
5. **Šta NE raditi** — česte greške (masovno objavljivanje pred prijavu, brisanje pa vraćanje
   istih videa, prikrivanje AI sadržaja umjesto deklarisanja)
6. **Ograničenja analize** — šta nisi mogao provjeriti (npr. audio naraciju bez gledanja videa)
   i šta korisnik mora ručno potvrditi

Budi direktan: cilj je da kanal PROĐE reviziju, pa je strože ocjenjivanje ovdje korisnije
od blagog. Lažno "sve je uredu" je najskuplja moguća greška za korisnika.

## Ograničenja

- Ova analiza je procjena na osnovu javnih politika — konačnu odluku donosi YouTube-ov
  recenzent. Uvijek to naglasi u izvještaju.
- Ne možeš slušati audio ni gledati video sadržaj — oslanjaš se na metapodatke, thumbnailove
  i korisnikove opise. Jasno razdvoji šta je utvrđeno, a šta pretpostavljeno.
