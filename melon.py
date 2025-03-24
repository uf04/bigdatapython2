import requests
from bs4 import BeautifulSoup

# 요청할 URL
url = "https://www.melon.com/chart/index.htm"

# 요청 헤더 (봇 감지를 피하기 위해 User-Agent 추가)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.melon.com/"
}

# 웹페이지 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 노래 제목과 아티스트 정보 추출
songs = soup.select("tr .wrap_song_info")

melon_chart = []
for song in songs:
    title_tag = song.select_one(".rank01 a")
    artist_tag = song.select_one(".rank02 a")
    
    if title_tag and artist_tag:
        title = title_tag.text.strip()
        artist = artist_tag.text.strip()
        melon_chart.append({"title": title, "artist": artist})

# 수집한 데이터 출력 (상위 100개)
for idx, song in enumerate(melon_chart[:100], start=1):
    print(f"{idx}. {song['title']} - {song['artist']}")
