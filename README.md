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
2. Prikuplja listu videa kanala (YouTube MCP konektor → YouTube Data API → yt-dlp → web fallback)
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

## Opciono: YouTube MCP konektor (preporučeno)

Repozitorij dolazi s projektnom MCP konfiguracijom (`.mcp.json`) koja registruje
[`youtube-connector-mcp`](https://github.com/ShellyDeng08/youtube-connector-mcp) — MCP
server koji izlaže alate poput `youtube_get_channel`, `youtube_get_video`,
`youtube_get_transcript`, `youtube_get_comments` i `youtube_list_playlists`. Skill ga
koristi kao prvi (najbogatiji) izvor podataka, prije skripte/yt-dlp fallbacka.

```bash
# instaliraj konektor
pipx install youtube-connector-mcp

# postavi YouTube API ključ (isti kao gore)
export YOUTUBE_API_KEY="tvoj-api-ključ"
```

Claude Code će pri pokretanju u ovom repozitoriju automatski pročitati `.mcp.json` i
ponuditi da odobriš `youtube-connector-mcp` server. Bez instaliranog konektora skill
i dalje radi preko postojećih fallback metoda (API skripta → yt-dlp → web).

## Struktura

```
.mcp.json                                       # registracija youtube-connector-mcp servera
.claude/skills/youtube-monetization-analyzer/
├── SKILL.md                                  # glavni tok analize
├── references/
│   ├── ypp-policies.md                       # YPP politike (snapshot juli 2026)
│   └── inauthentic-content-checklist.md      # checklist signala rizika + niša
└── scripts/
    └── fetch_channel.py                      # dohvat videa (API/yt-dlp fallback)
```

> Napomena: analiza je procjena na osnovu javnih politika — konačnu odluku o
> monetizaciji donosi YouTube-ov recenzent.
