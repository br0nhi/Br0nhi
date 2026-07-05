# YPP analiza kanala @harlibee — 5. juli 2026

> Analiza prema skillu `youtube-monetization-analyzer`. Rok za ponovnu YPP prijavu: **27. juli 2026**.
> Napomena: konačnu odluku donosi YouTube-ov ljudski recenzent — ovo je procjena na osnovu javnih politika.

## 1. Presuda

**Analiza po videima nije mogla biti završena** — okruženje u kojem je analiza rađena blokira
pristup youtube.com (yt-dlp, direktni fetch i statistički servisi svi vraćaju 403), pa lista
videa nije dostupna. Na osnovu onoga što JESTE utvrđeno: **kanal se još ne može proglasiti
spremnim za ponovnu prijavu**, i postoje dva konkretna signala rizika na nivou kanala koja
treba hitno provjeriti i sanirati (vidi tačku 3).

## 2. Status politika (provjereno 5. jula 2026)

- Politika **"inauthentic content"** (preimenovana iz "repetitious content", na snazi od
  15. jula 2025) i dalje je aktuelna i YouTube je pojačao njenu primjenu na AI-generisan
  masovni sadržaj. Bundlirane reference skilla su i dalje tačne — nema odstupanja koja bi
  mijenjala analizu.
- Fokus primjene u 2025/2026: šablonski videi s minimalnom varijacijom, AI skripte + TTS +
  stock/AI vizuali bez autorskog doprinosa, reciklirani klipovi, low-effort kompilacije.
  Politika se primjenjuje na **kanal kao cjelinu**, ne samo pojedinačne videe.
- Pragovi: za puni YPP (prihod od oglasa) i dalje važi 1.000 pretplatnika + 4.000 sati
  javnog gledanja (12 mj.) ili 10M Shorts pregleda (90 dana). Prošireni pristup (fan
  funding: članstva, Supers) dostupan je ranije s nižim pragom (500 pretplatnika).

## 3. Nalazi na nivou kanala (utvrđeno iz javnih izvora)

| # | Nalaz | Rizik | Šta uraditi |
|---|-------|-------|-------------|
| 1 | Google indeksira kanal (`UClXAOFnoNj5lPWU11vw2Rqw`) s opisom tipa *"entertainment and education content, varied topics"* | 🟡 | Ako About sekcija još govori o "raznovrsnom/zabavnom" sadržaju, to direktno protivrječi strategiji jedne niše. Prepisati About: islamske historijske priče, izvori, autor. Google snippet može biti i stari keš — provjeriti stvarnu About sekciju. |
| 2 | TikTok nalog `@harlibee` (isti handle) objavljuje bosanski komedija/meme sadržaj (Pixar meme klipovi, skečevi) | 🟡→🔴 | Ako su ti ili slični klipovi ikad postavljani na YouTube kanal (posebno kao Shorts) i još su javni, to je vjerovatno tip sadržaja zbog kojeg je monetizacija i ukinuta (repost/kompilacija bez transformacije). Sve takve ostatke ukloniti ili prebaciti na private PRIJE prijave. |
| 3 | Pojedinačni videi kanala nisu indeksirani u web pretrazi | ⚪ | Nije nužno problem (mali kanali se slabo indeksiraju), ali onemogućava vanjsku analizu po videima. |

## 4. Analiza po videima — BLOKIRANO, potrebni podaci od korisnika

Da bi se završila tabela rizika po videima, potrebna je lista **svih javnih videa** u formatu:

```
naslov | datum objave | trajanje | naracija (vlastiti glas / AI-TTS / bez) | vizuali (AI slike / stock / mape / montaža) | izvor skripte (vlastito istraživanje / prevod tuđeg teksta / Wikipedia)
```

Bez toga se ne dodjeljuju ocjene — videi se ne izmišljaju.

## 5. Plan akcije prije 27. jula (22 dana)

Prioritizovano, prema checklisti skilla:

1. **ODMAH — čišćenje ostataka (signal B5/A6):** proći kroz SVE javne videe i Shorts;
   sve što nije islamska historijska priča (stari zabavni/meme/repost sadržaj) obrisati
   ili prebaciti na private. Recenzent gleda kanal kakav je na dan prijave.
2. **ODMAH — About sekcija i branding:** opis kanala mora jasno reći nišu, autora i pristup
   (npr. "Autorske obrade islamske historije po izvorima: Ibn Kesir, Et-Taberi, Buharija…").
3. **Do 12. jula — audit preostalih videa** po checklisti: za svaki video potvrditi
   naraciju (vlastiti glas > AI glas s autorskom skriptom > TTS koji čita tuđi tekst),
   izvor skripte i varijaciju vizuala. Videe s 2+ signala grupe A ukloniti/preraditi.
4. **Do 18. jula — signali autentičnosti:** izvori u opisima svakog videa (unikatni opisi,
   ne copy-paste), community post ili dva, odgovaranje na komentare, po mogućnosti vodeni
   žig/intro s prisustvom autora.
5. **Do 18. jula — "Altered content" oznaka** na svim videima s realističnim AI vizualima
   historijskih događaja.
6. **20.–27. jula — prijava:** prijaviti se tek kad je sve gore završeno. Ako nešto nije
   spremno, bolje sačekati nego riskirati novo odbijanje (= novih ~90 dana).

## 6. Šta NE raditi

- Ne objavljivati masovno nove videe neposredno pred prijavu (pojačava utisak masovne produkcije).
- Ne brisati pa vraćati iste videe bez prerade.
- Ne prikrivati AI sadržaj — deklarisati ga (Altered content) i dodati autorski doprinos.
- Ne postavljati TikTok komedija klipove na YouTube kanal, ni kao Shorts.

## 7. Ograničenja analize

- **Nije pregledana lista videa** (mrežna blokada okruženja) — tabela rizika po videima čeka
  korisnikove podatke iz tačke 4.
- Nije moguće čuti naraciju ni vidjeti vizuale — i uz listu, korisnik mora potvrditi vrstu
  naracije, vizuala i porijeklo skripte.
- Google-ov opis kanala ("varied topics") može biti zastarjeli keš — provjeriti ručno.
- Ne mogu se provjeriti: strajkovi, copyright claimovi, watch-time pragovi — provjeriti u
  YouTube Studio (Monetization + Copyright tabovi).

## Izvori

- [Social Media Today — YouTube clarifies inauthentic content update](https://www.socialmediatoday.com/news/youtube-clarifies-monetization-update-inauthentic-repeated-content/752892/)
- [iMusician — YouTube targets inauthentic content](https://imusician.pro/en/resources/blog/youtube-updates-its-monetization-policies)
- [SubSub — YouTube inauthentic content policy](https://www.subsub.io/blog/youtube-inauthentic-content-policy-2025)
- [MilX — YouTube monetization requirements 2026](https://milx.app/en/trends/youtube-monetization-requirements-for-2026)
- [YouTube Help — channel monetization policies](https://support.google.com/youtube/answer/1311392?hl=en) (direktan pristup blokiran iz okruženja)
- Kanal: [Harlibee — YouTube](https://www.youtube.com/channel/UClXAOFnoNj5lPWU11vw2Rqw); TikTok: [@harlibee](https://www.tiktok.com/@harlibee)
