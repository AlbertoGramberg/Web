import requests
from bs4 import BeautifulSoup

def buscar_videos_youtube(tema):
    url = f"https://www.youtube.com/results?search_query={tema}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    videos = []
    for vid in soup.find_all("a", class_="yt-uix-tile-link"):
        video = {
            "titulo": vid.text,
            "enlace": "https://www.youtube.com" + vid["href"]
        }
        videos.append(video)
    return videos