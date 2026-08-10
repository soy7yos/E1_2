"""Tax Basic Quiz Game"""

menu_min = 1
menu_max = 5


def get_valid_input(prompt, min_value, max_value):
    """공백 제거, 숫자 변환 실패, 범위 밖 숫자, 빈 입력 처리"""
    while True:
        raw = input(prompt).strip()  # 공백 제거

        if raw == "":
            print("⚠️  입력값 없음 -> 다시 입력")
            continue

        try:
            value = int(raw)  # 숫자 변환 시도
        except ValueError:
            print("⚠️  숫자만 입력 가능 -> 다시 입력")
            continue

        if not (min_value <= value <= max_value):
            print(f"⚠️  {min_value}-{max_value} 사이 숫자만 입력 가능 -> 다시 입력")
            continue

        return value


def play_quiz():
    print("(추후 구현)")

def add_quiz():
    print("(추후 구현)")

def show_quiz_list():
    print("(추후 구현)")

def show_high_scores():
    print("(추후 구현)")


def print_menu():
    """메뉴 출력"""
    print("*" * 25)
    print("   Tax Basic Quiz Game")
    print("*" * 25)
    print("1) Play Quiz")
    print("2) Add Quiz")
    print("3) Quiz List")
    print("4) High Scores")
    print("5) Exit\n")


def save_and_exit():
    # 이후 QuizGame.save()로 대체 예정
    print("== 게임 종료 ==")


def main():
    try:
        while True:
            print_menu()
            choice = get_valid_input("Enter your choice! (1-5): ", menu_min, menu_max)

            if choice == 1:
                play_quiz()                
            elif choice == 2:
                add_quiz()
            elif choice == 3:
                show_quiz_list()
            elif choice == 4:
                show_high_scores()
            elif choice == 5:
                save_and_exit()
                break
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️  게임 중단") # 엔터 삽입 비교
        save_and_exit()


if __name__ == "__main__":
    main()