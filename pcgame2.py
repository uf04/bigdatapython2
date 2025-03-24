import requests
import re

# 게임트릭스 URL
url = "https://www.gametrics.com/"

# 요청 헤더 설정 (차단 방지)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.gametrics.com/"
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)
response.raise_for_status()  # 요청이 실패하면 예외 발생

# HTML에서 게임 순위 부분 추출 (정규 표현식 사용)
pattern = re.compile(r'<td align="left"><a.*?>(.*?)</a></td>\s*<td align="center">(.*?)</td>\s*<td align="right">(.*?)%</td>', re.DOTALL)
matches = pattern.findall(response.text)

# 결과 출력 (상위 10개)
for idx, (title, company, percentage) in enumerate(matches[:10], start=1):
    print(f"{idx}위: {title} ({company}) - 점유율: {percentage}%")
