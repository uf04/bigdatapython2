pip install requests beautifulsoup4
import requests
from bs4 import BeautifulSoup

# 게임트릭스 메인 페이지 URL
url = "https://www.gametrics.com/"

# HTTP 요청 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.gametrics.com/"
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)
response.raise_for_status()  # 요청이 성공했는지 확인

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 게임 순위 테이블 찾기
table = soup.find("table", {"class": "table_list"})

# 게임 순위 데이터 추출
game_rankings = []
if table:
    rows = table.find_all("tr")[1:11]  # 상위 10개 항목 선택
    for idx, row in enumerate(rows, start=1):
        columns = row.find_all("td")
        if len(columns) >= 5:
            rank = idx
            title = columns[1].get_text(strip=True)
            company = columns[2].get_text(strip=True)
            percentage = columns[3].get_text(strip=True)
            game_rankings.append({"rank": rank, "title": title, "company": company, "percentage": percentage})

# 결과 출력
for game in game_rankings:
    print(f"{game['rank']}위: {game['title']} ({game['company']}) - 점유율: {game['percentage']}")
