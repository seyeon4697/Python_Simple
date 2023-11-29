import requests
from bs4 import BeautifulSoup
from db.news_daaao


# 수집한 데이터 DB에 저장
# MongoDB -> JSON = Dict Type
data = {
    "title" :title,
    "content" :content,
    "date" :reg_date
}
add_news(data)