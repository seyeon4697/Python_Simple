# DAO: Database Access Object
#  - 데이터 작업(CRUD)을 하는 객체
#  회원 => member_dao
#  로그인 => login_dao
#  뉴스 => news_dao
#  상품 => product_dao

# 뉴스(제목, 본문, 날짜, URL) 저장


from common.connection import conn_mongodb

def add_news():
    conn = conn_mongodb()  # 1.connection
    conn.insert_one(data)  # 2.DB에 저장