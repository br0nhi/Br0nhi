# Br0nhi — YouTube Monetization Analyzer skill

Claude Code skill za analizu YouTube kanala **@kanal** u odnosu na YouTube politike
monetizacije (YPP), s posebnim fokusom na **inauthentic content** politiku.

## Upotreba

U Claude Code sesiji unutar ovog repozitorija pokreni:

```
/youtube-monetization-analyzer
```

ili prirodnim jezikom: *"analiziraj moj kanal prije ponovne prijave za monetizaciju"*.

Za drugi kanal: `/youtube-monetization-analyzer @drugikanal`

## Šta skill radi

1. Dohvata ažurne YouTube politike monetizacije (uz bundlirane reference kao rezervu)
2. Prikuplja listu videa kanala (YouTube Data API → yt-dlp → web fallback)
3. Ocjenjuje svaki video rizikom 🔴/🟡/🟢 prema checklisti inauthentic content signala
4. Analizira kanal kao cjelinu (konzistentnost niše, varijacija, signali autentičnosti)
5. Generiše izvještaj na bosanskom s planom akcije prije ponovne YPP prijave

## Opciono: YouTube Data API

Za najpotpunije podatke postavi env varijablu prije pokretanja:

```
export YOUTUBE_API_KEY="tvoj-api-ključ"
```

Ključ se pravi besplatno na https://console.cloud.google.com (YouTube Data API v3).
Bez ključa skill koristi yt-dlp ili web pretragu.

## Struktura

```
.claude/skills/youtube-monetization-analyzer/
├── SKILL.md                                  # glavni tok analize
├── references/
│   ├── ypp-policies.md                       # YPP politike (snapshot juli 2026)
│   └── inauthentic-content-checklist.md      # checklist signala rizika + niša
└── scripts/
    └── fetch_channel.py                      # dohvat videa (API/yt-dlp)
```

> Napomena: analiza je procjena na osnovu javnih politika — konačnu odluku o
> monetizaciji donosi YouTube-ov recenzent.
