#!/usr/bin/env python3
"""Dohvata listu videa YouTube kanala kao JSON (stdout).

Redoslijed metoda:
  1. YouTube Data API v3 (ako je postavljen YOUTUBE_API_KEY)
  2. yt-dlp fallback (ako je instaliran)

Upotreba:
  python3 fetch_channel.py @harlibee
  python3 fetch_channel.py @harlibee --max 100
"""
import json
import os
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request

API_BASE = "https://www.googleapis.com/youtube/v3"


def api_get(endpoint: str, params: dict) -> dict:
    url = f"{API_BASE}/{endpoint}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.load(resp)


def fetch_via_api(handle: str, api_key: str, max_videos: int) -> dict:
    ch = api_get("channels", {
        "part": "id,snippet,statistics,contentDetails",
        "forHandle": handle,
        "key": api_key,
    })
    if not ch.get("items"):
        raise RuntimeError(f"Kanal {handle} nije pronađen preko API-ja")
    channel = ch["items"][0]
    uploads = channel["contentDetails"]["relatedPlaylists"]["uploads"]

    video_ids, page_token = [], None
    while len(video_ids) < max_videos:
        params = {"part": "contentDetails", "playlistId": uploads,
                  "maxResults": 50, "key": api_key}
        if page_token:
            params["pageToken"] = page_token
        page = api_get("playlistItems", params)
        video_ids += [i["contentDetails"]["videoId"] for i in page.get("items", [])]
        page_token = page.get("nextPageToken")
        if not page_token:
            break
    video_ids = video_ids[:max_videos]

    videos = []
    for i in range(0, len(video_ids), 50):
        batch = api_get("videos", {
            "part": "snippet,contentDetails,statistics,status",
            "id": ",".join(video_ids[i:i + 50]),
            "key": api_key,
        })
        for v in batch.get("items", []):
            sn, st = v["snippet"], v.get("statistics", {})
            videos.append({
                "id": v["id"],
                "url": f"https://www.youtube.com/watch?v={v['id']}",
                "title": sn.get("title"),
                "description": sn.get("description"),
                "published_at": sn.get("publishedAt"),
                "duration": v.get("contentDetails", {}).get("duration"),
                "tags": sn.get("tags", []),
                "views": st.get("viewCount"),
                "likes": st.get("likeCount"),
                "comments": st.get("commentCount"),
                "privacy": v.get("status", {}).get("privacyStatus"),
                "made_for_kids": v.get("status", {}).get("madeForKids"),
            })

    return {
        "source": "youtube-data-api",
        "channel": {
            "id": channel["id"],
            "handle": handle,
            "title": channel["snippet"].get("title"),
            "description": channel["snippet"].get("description"),
            "subscribers": channel["statistics"].get("subscriberCount"),
            "total_views": channel["statistics"].get("viewCount"),
            "video_count": channel["statistics"].get("videoCount"),
        },
        "videos": videos,
    }


def fetch_via_ytdlp(handle: str, max_videos: int) -> dict:
    url = f"https://www.youtube.com/{handle}/videos"
    out = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--playlist-end", str(max_videos), "-J", url],
        capture_output=True, text=True, timeout=300, check=True,
    )
    data = json.loads(out.stdout)
    videos = [{
        "id": e.get("id"),
        "url": e.get("url") or f"https://www.youtube.com/watch?v={e.get('id')}",
        "title": e.get("title"),
        "description": e.get("description"),
        "duration": e.get("duration"),
        "views": e.get("view_count"),
    } for e in data.get("entries", [])]
    return {
        "source": "yt-dlp",
        "channel": {
            "handle": handle,
            "title": data.get("channel") or data.get("title"),
            "subscribers": data.get("channel_follower_count"),
        },
        "videos": videos,
    }


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    handle = args[0] if args else "@harlibee"
    if not handle.startswith("@"):
        handle = "@" + handle
    max_videos = 200
    if "--max" in sys.argv:
        max_videos = int(sys.argv[sys.argv.index("--max") + 1])

    errors = []
    api_key = os.environ.get("YOUTUBE_API_KEY")
    if api_key:
        try:
            print(json.dumps(fetch_via_api(handle, api_key, max_videos),
                             ensure_ascii=False, indent=2))
            return 0
        except Exception as e:
            errors.append(f"API: {e}")
    else:
        errors.append("API: YOUTUBE_API_KEY nije postavljen")

    if shutil.which("yt-dlp"):
        try:
            print(json.dumps(fetch_via_ytdlp(handle, max_videos),
                             ensure_ascii=False, indent=2))
            return 0
        except Exception as e:
            errors.append(f"yt-dlp: {e}")
    else:
        errors.append("yt-dlp: nije instaliran")

    print(json.dumps({"error": "Nijedna metoda nije uspjela", "details": errors},
                     ensure_ascii=False, indent=2), file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
