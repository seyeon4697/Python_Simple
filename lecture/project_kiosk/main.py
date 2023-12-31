########################################
# "조선 별다방" 카페 키오스크 프로그램
# - 일자: 2023년 10월 13일
# - 작성자: luinsun
# - 내용 카페 음료를 주문 및 판매 하는 콘솔 프로그램

from service_kiosk import user_choice

# 메뉴와 가격표
# - Dict Type -> 데이터베이스 대체
main_name = {1: "커피(Coffee)", 2: "음료(Drink)", 3: "빵(Bakery)"}

coffee_name = {1: "아메리카노", 2: "카페라떼", 3: "콜드브루",4: "에스프레소"}
coffee_price = {1: 1500, 2: 3000, 3: 5000, 4: 1000}

drink_name = {1: "스무디", 2: "버블티", 3: "에이드", 4: "생과일주스", 5: "탄산"}
drink_price = {1: 2500, 2: 3000, 3: 2000, 4: 5000, 5:1000}

bakery_name = {1: "카스테라", 2: "케이크", 3: "허니브레드"}
bakery_price = {1: 4000, 2: 8000, 3: 6000}

#고객 주문 기록 저장
menu_save = [] # 고객 주문 메뉴 기록
price_save = [] # 고객 주문 가격 기록

# 1.메인 메뉴 출력
print("■"*50)
print("■■ == 조선 별다방 == ")
print("■■ == ver 1.2")
print("■■ 메인 메뉴")
for i,menu in enumerate(main_name.values()):
    print(f"■□ {i+1}.{menu}")

# 2.메인 메뉴 선택
choice = user_choice(len(main_name), "main")


# 3. 서브 메뉴 출력
if choice == 1:     # 커피
    print("●● 커피(Coffee)")
    for i in range(len(coffee_name)):
        print(f"●○ {i+1}.{coffee_name[i+1]}({coffee_price[i+1]}원)")
    choice = user_choice(len(coffee_name))
    menu_save.append(coffee_name[choice])
    price_save.append(coffee_price[choice])
elif choice == 2:     # 음료
    print("●● 음료(Drink)")
    for key, value in drink_name.items():
        print(f"●○ {key}.{value}({drink_price[key]}원)")
    choice = user_choice(len(drink_name))
    menu_save.append(drink_name[choice])
    price_save.append(drink_price[choice])
elif choice == 3:   #빵
    print("●● 빵(Bakery)")
    for i.value in enumerate(bakery_name.values()):
        print(f"●○ {i+1}.{value}({bakery_price[i+1]}원)")
    choice = user_choice(len(bakery_name))
    menu_save.append(bakery_name[choice])
    price_save.append(bakery_price[choice])
elif choice == 99:
    print("MSG: 조선별다방 키오스크를 종료합니다.")
    exit()

for menu in menu_save:
    print(menu)
for price in price_save:
    print(price)