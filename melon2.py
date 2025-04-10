import requests
from bs4 import BeautifulSoup
import random

# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'  # 멜론의 최신 차트 URL로 확인 필요

# 헤더 설정 (멜론은 User-Agent 확인을 통해 봇 접근을 차단할 수 있으므로 설정이 필요할 수 있음)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목과 아티스트를 담을 리스트
songs = []

# 멜론 차트의 노래 제목과 아티스트를 찾습니다.
#lst50 #frm > div > table > tbody #lst50
for entry in soup.select('tr.lst50, tr.lst100'):  # 상위 50위 및 100위 목록
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))

# 수집한 데이터를 출력합니다.
for song in songs:
    print(f"{song[0]}. {song[1]} - {song[2]}")

# 1. 멜론 100곡 출력
# 2. 멜론 50곡 출력
# 3. 멜론 10곡 출력
# 4. AI 추천곡 출력
# 5. 가수 이름 검색
print("==================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("==================")
# 메뉴선택(숫자입력): 1
n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}")
# n = int(n) # 숫자로 변경(연산을 해야한다면)
# 만약에 1을 입력하면 
# 멜론 100 출력
if n == "1":
    print("멜론 100")
    # 수집한 데이터를 출력합니다.
    for i in range(100):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")
# else:
  #  print("1이 아닙니다.")
# 만약에 2를 입력하면
# 멜론 50 출력
elif n == "2":
    print("멜론 50")
    for i in range(50):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")
# ...
elif n == "3":
    print("멜론 10")
    for i in range(10):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")
elif n == "4":
    print("AI 추천 노래")
    ai_song = random.choice(songs)
    print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.") 
elif n == "5":
    print("가수 이름 검색")
    m = input("가수 이름 입력: ")
    print(f"당신이 찾는 가수의 곡은?: - {m}")
# 5를 입력하면 가수 이름 검색할 수 있게 입력창이 또 나와야함
# 이름을 입력하면 해당 가수 이름의 노래 리스트가 출력
else:
    print("1~5까지 입력하세요")