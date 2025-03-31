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
# response = requests.get(url)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

print(response)

for n in range(1,11):
    print(n)