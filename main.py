"""Tax Basic Quiz Game"""

menu_min = 1
menu_max = 5


class Quiz:
    """개별 퀴즈"""

    def __init__(self, question, choices, answer):
        self.question = question      # 문제
        self.choices = choices        # 선택지 4개 (list)
        self.answer = answer          # 정답 번호 1~4

    def display(self):
        """퀴즈 출력"""
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def check_answer(self, user_answer):
        """정답 확인 -> bool 반환"""
        return user_answer == self.answer


DEFAULT_QUIZZES = [
    Quiz(
        "월급을 받을 때 소득세의 일부가 미리 빠져나가는 것을 무엇이라고 할까요?",
        ["세액공제", "원천징수", "소득공제", "세금환급"],
        2
    ),
    Quiz(
        "연말정산의 가장 정확한 설명은 무엇일까요?",
        [
            "연말에 회사가 보너스를 지급하는 절차",
            "1년 동안 낸 세금을 모두 면제받는 절차",
            "미리 낸 세금과 실제 부담할 세금을 정산하는 절차",
            "다음 해에 낼 세금을 미리 납부하는 절차"
        ],
        3
    ),
    Quiz(
        "세율을 곱하기 전의 기초가 되는 금액으로, 총수입에서 관련 비용과 소득공제액 등을 반영한 금액을 무엇이라 할까요?",
        ["결정세액", "총급여액", "산출세액", "과세표준"],
        4
    ),
    Quiz(
        "한국의 부가가치세(VAT) 기본 세율은 몇 %일까요?",
        ["5%", "8%", "10%", "15%"],
        3
    ),
    Quiz(
        "소득공제와 세액공제의 차이를 가장 잘 설명한 것은?",
        [
            "소득공제는 내야 할 세금에서 직접 빼고, 세액공제는 소득에서 뺀다.",
            "소득공제는 과세 대상이 되는 소득을 줄이고, 세액공제는 계산된 세금에서 직접 뺀다.",
            "소득공제와 세액공제는 이름만 다를 뿐 같은 제도다.",
            "소득공제는 직장인만, 세액공제는 사업자만 받을 수 있다."
        ],
        2
    ),
]


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
    # QuizGame.save()로 대체 예정
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
        print("\n\n⚠️  게임 중단")
        save_and_exit()


if __name__ == "__main__":
    main()