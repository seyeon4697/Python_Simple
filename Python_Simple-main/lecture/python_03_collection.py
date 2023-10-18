# 컬렉션 타입
# - 변수 하나에 값을 여러개 저장
# - 실질적으로 변수에 컬렉션 1개가 저장
# - 리스트(List), 튜플(Tuple), 딕트(Dictionary), 세트(Set)

# 1. 리스트(List)  ex) 기차 생각하면된다
# - 시퀸스 자료형(연속된 값 저장)
# - index 사용( Slicing 가능)
# - [] 사용
# - 정렬 가능
# - mutable(생성 된 후 변경 가능)
# - packing 과 unpacking 가능
# - 멤버함수: append(), extend(), insert(), remove(), pop(), index(), sort() 등등
# * 2차원 리스트는 표(table)과 동일한 형태

list_a = [1, 2, 3]
list_b = []
list_c = ["chosun", 5, 3.14, [1, 2, 3]]

# packing and unpacking
list_d = ["A", "B", "C"]    # packing
a, b, c = ["A", "B", "C"]   # unpacking

# a = list_d[0]
# b = list_d[1]
# c = list_d[2] java나 C에서 사용하는

# append(값) : 리스트의 맨 마지막에 값을 추가
a = [1, 2, 3]
a.append(4)
print(a)
# insert(인덱스, 값) : 리스트의 원하는 인덱스에 값을 추가
b = [1, 2, 3]
b.insert(1, 9)
print(b)

#extend(리스트) : 리스트와 리스트를 병합
a = [1, 2, 3]
b = [3, 4, 5]
# a.extend(b)
# print(a)
c = a + b
print(c)    # 추천

# remove(값) : 리스트 내 원소를 값으로 삭제
# pop(인덱스) : 리스트 내 원소를 인덱스로 삭제
abc = [1, 2, 3, 4, 5]
abc.remove(3)   #3번이라는 값
print(abc)
e = abc.pop(0)  #0번 인덱스
print(abc)
print(e)

# index() : ()안의 값의 인덱스를 출력
a = ["A", "B"]
print(a.index("B"))

# sort() and sorted() : 리스트 안의 원소들을 정렬
# - sort() : 원본값 자체를 정렬(원본값 정렬)  # 사용금지
# - sorted() : 원본값을 복제해서 정렬(원본값 유지)
a = [95, 1, 3, 55, 27, 45]
b = sorted(a)   # 디폴트: 오름차순
c = sorted(a, reverse=True) # 내림 차순
print(b)
print(a)
print(c)

# 2.  튜플( Tuple) ex: 기차
# - List와 대부분 동일
# - 시퀀스 자료형
# - index 사용(Slicing 가능)
# - packing과 unpacking 가능
# - immutable(생성된 후 변경 불가)
# - 정렬 불가능
# - ()사용(생략 가능)
# * 여러분이 직접 Tuple 생성하는 경우(X)
#   -> python에서 결과값을 Tuple로 제공
print("="*50)
a = [1, 2, 3]   # List
b = (1, 2, 3)   # Tuple
c = 1, 2, 3     # Tuple

a[0] = 99
print(a)

# b[0] = 99     # Tuple 값 변경 불가
# print(b)

# 튜플 원소가 1개인 경우!
a = 1, 2, 3     # Tuple
b = 1, 2, 3     # Tuple
c = (1)         # Tuple
d = 1           # int
e = 1,          # Tuple
print(type(b))
print(type(d))
print(type(e))

a = 5
b = 8
# JAVA와 C에서의 Swap
# Java 와 C 에서의 교환
# temp = a
# a = b
# b = temp
a, b = b, a     # Tuple과 packing & iunpacking
print(a)    # 8
print(b)    # 5

# 3.세트(Set) ex: 복주머니
# - 수학의 집합 개념
# - 순서 없음(index 없음, 정렬불가)
# - 중복값 허용하지 않음(중요)
# - {} 사용
# - 멤버함수: union(), intersection(), difference() 등등

# * Set는 대부분 중복값 제거 활용

set_a = {1, 1, 1 , 2, 2, 3, 4, 5}
print(set_a)

# 중복값 제거 활용 방법
# - a List의 중복값 제거
a = ["A", "A", "B", "B", "C"]   # List type
# a = set(a) # ()안의 값을 set type으로 변경
# a = list(a) # ()안의 값을 list type으로 변경
# List -> Set(중복값 제거) -> List
print(list(set(a)))

# 4. 딕트(Dict) ex: 복주머니
# - 순서가 없음(인덱스 없음, 정렬 불가)
# - {key:value} -> key, value 1pair
# - key(중복 불가), value(중복 가능)
# - key를 통해서만 value접근 가능
# - 멤버 함수: update(), get(), keys(), values(), items()

# 사전(dict) type의 중요성!
# - 외부에서 데이터를 주고 받는 표준 규격: JSON
# {"id":"abc123", "pw":"@!123", "name":"bjw"}
# - Python의 dict == JSON

dict_a = {"Korea":"Seoul",
          "Canada":"Ottaws",
          "USA":"Washingthon D.C"}
print(dict_a)
import pprint
pprint.pprint(dict_a)

# update() : dict와 dict 병합
a = {"a": 1,
     "b": 2}
b = {"b": 3,
     "c": 5}
a.update(b)
print(a)    # 병합시 중복key는 입력값(b)이 우선

# pop(key) : dict 원소를 key를 통해 삭제
abc = {"a":1, "b":2, "c":3}
c = abc.pop("a")
print(abc)
print(c)

# in() : ()안의 key값이 존재 확인
print("c" in abc)
print("f" in abc)

# get() : 값 접근
# list, tuple, dict 접근
#  -> 컬레션[index or key]
#  -> ex: a[1], b["c"]
# print(abc["f"])  # key가 없으면 Error 발생
print(a.get("f"))  # key가 없으면 None 출력(Error X)

# keys(), values(), items()
print(a)
print(a.keys())     # key만 추출
print(a.values())   # value만 추출
print(a.items())    # (key, value) 추출

print(list(a.keys()))   # 활용 방법

# clear() : dict 초기화
print(abc)
abc.clear()
print(abc)

a = {}
print(type(a))

# 1. LIST [], 수정가능
# 2. Tuple (), 수정 불가능!
#     (1, 2, 3) => 1, 2, 3
#     (1) => 1,
#
# 3. DICT {key:value}
# 4. SET {}
#     -중복값 허용X
#
# List(), tuple(), set()
#
# DICT: JSON(데이터 전송 포맷)