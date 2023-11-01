# 키오스크 기능들...

# 사용자 메뉴 선택
# - max_count: 메뉴별 갯수
# - menu_type: main or sub
def user_choice(max_count, menu_type=""):
    while True:
        choice = int(input(">> 번호: "))
        if choice == 99 and menu_type == "main":
            print("MSG: 조선별다방 키오스크를 종료합니다.")
            return choice
        if max_count >= choice >= 1:
            return choice
        else:
            print("MSG: 올바른 번호를 입력하세요.")