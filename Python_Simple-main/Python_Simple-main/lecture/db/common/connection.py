# 데이터베이스(DB): 데이터를 효율적으로 저장하는 시스템
# FileSystem: 폴더를 사용한 저장

# 데이터베이스관리시스템(DBMS): DB이론을 실제로 구현!

# ** DBMS 종류
#  1) 관계형 데이터베이스(RDB): 전통적인(스키마: 명세서)
#   - ORACLE
#   - MySQL
#   - MariaDB

#  2) NoSQL: NEW
#   - MongoDB
#   - Redis

# ** DB 프로세스
#  - Do: ID와 PW 저장
#  Pycharm(Python)  ------------------ DB(MongoDB)
#   1) Pycharm과 DB가 Connection 맺기
#      - IP: 컴퓨터를 찾아갈 수 있는 주소!
#      - PORT: 컴퓨터 내에서 특정 프로그램의 위치
#      - ID and PW
#   2) SQL을 사용해서 DB에 CRUD작업 진행
#      - SQL(구조질의어): DB와 소통할 수 있는 언어(반드시)
#      - RDB(SQL)을 사용, NoSQL(SQL X)
#      Create(삽입)  -> INSERT
#      Read(조회)    -> SELECT
#      Update(수정)  -> UPDATE
#      Delete(삭제)  -> DELETE

# ** MongoDB 설정 방법
#  1.직접 설치(Local)
#  2.MongoDB에서 제공하는 웹 클라우드 사용(설치 x)
#    - MongoDB 회원가입 필수!
#    - IP와 PORT => URL 제공!

#  ** MongoDB 구조
#  설치: MongoDB(DBMS): 전체 시스템
#         ㄴ DB(카카오톡): 폴더
#            ㄴ collection(회원): 표
#            ㄴ collection(톡):
#            ㄴ collection(선물):
#            ㄴ collection(친구):
#         ㄴ DB(카카오뱅크)
#            ㄴ collection(회원):
#            ㄴ collection(계좌):
#            ㄴ collection(대출):
#         ㄴ DB(카카오페이)
#         ㄴ ...
# ※ 데이터를 CRUD -> collection


from pymongo import MongoClient

# Mongo DB Connection
def conn_mongodb():
    # ID, PORT, ID, PW
    DB_ID = ""  # 상수(전체 대문자로 변수명을 사용)
    DB_PW = ""  # ex) 은행권 => 금리(상수)
    client = MongoClient(f"mongodb+srv://{DB_ID}:{DB_PW}@atlascluster.1jknaiy.mongodb.net/")
    # DB설정 -> collection 설정
    db = client["daum"]
    collection = db.get_collection("news")
    return collection