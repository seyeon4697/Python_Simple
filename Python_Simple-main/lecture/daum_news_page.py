import requests     # 전체 소스코드 가져오기
from bs4 import BeautifulSoup   # 원하는 정보 SELECT
from service.service_news import get_news

count = 0   #전체 기사 수
page = 1    #시작 페이지 1로 고정

while True:
    url = f"https://news.daum.net/breakingnews/digital?page={page}"
    result = requests.get(url)

    if result.status_code == 200:
        print(result, "접속 성공 → 데이터를 수집합니다.")   #200(성공)뜨는지 확인
        doc = BeautifulSoup(result.text, "html.parser")
        url_list = doc.select("ul.list_news2 a.link_txt")

        # print(f"{page} 페이지의 기사 갯수: {len(url_list)}")

        if len(url_list) == 0:
            break;
        for url in url_list:
            count += 1
            print(f"{count}번", "="*100)
            # get_new(): 기사 제목, 본문, 날짜 수집
            get_news(url["href"])
            print(url["href"])          #url에 있는 주소만 가져오기

    else:
        print("URL경로가 잘못되었습니다.")

    page += 1