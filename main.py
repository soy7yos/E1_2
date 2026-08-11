"""Tax Basic Quiz Game"""

MENU_MIN = 1
MENU_MAX = 5


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
        raw = input(prompt).strip()

        if raw == "":
            print("⚠️  입력값 없음 -> 다시 입력")
            continue

        try:
            value = int(raw)
        except ValueError:
            print("⚠️  숫자만 입력 가능 -> 다시 입력")
            continue

        if not (min_value <= value <= max_value):
            print(f"⚠️  {min_value}-{max_value} 사이 숫자만 입력 가능 -> 다시 입력")
            continue

        return value


class QuizGame:
    """게임 전체 관리"""

    def __init__(self, quizzes=None, best_score=0):
        self.quizzes = quizzes if quizzes is not None else []
        self.best_score = best_score

    def print_menu(self):
        print("*" * 25)
        print("   Tax Basic Quiz Game")
        print("*" * 25)
        print("1) Play Quiz")
        print("2) Add Quiz")
        print("3) Quiz List")
        print("4) High Scores")
        print("5) Exit\n")

    def play_quiz(self):
        if not self.quizzes:
            print("⚠️  등록된 퀴즈 없음\n")
            return

        total = len(self.quizzes)
        correct = 0

        print(f"\n 퀴즈 시작! (총 {total}문제)\n")

        for idx, quiz in enumerate(self.quizzes, start=1):
            print("-" * 40)
            print(f"[문제 {idx}]")
            quiz.display()

            user_answer = get_valid_input("\n정답 입력: ", 1, len(quiz.choices))

            if quiz.check_answer(user_answer):
                print("⭕️ 정답\n")
                correct += 1
            else:
                print(f"❌ 오답 (정답: {quiz.answer}번)\n")

        score = int(correct / total * 100)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답!\n")

        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다! 🎉\n")

    def add_quiz(self):
        print("\n📌 새로운 퀴즈 추가\n")

        question = input("문제 입력: ").strip()
        while question == "":
            print("⚠️  문제 입력")
            question = input("문제 입력: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            while choice == "":
                print("⚠️  선택지 입력")
                choice = input(f"선택지 {i}: ").strip()
            choices.append(choice)

        answer = get_valid_input("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        print("\n== 퀴즈 추가 완료 ==\n")

    def show_quiz_list(self):
        print("(추후 구현)")

    def show_high_scores(self):
        print("(추후 구현)")

    def save(self):
        pass  # state.json 저장 로직 (10단계에서 구현)

    def load(self):
        pass  # state.json 불러오기 로직 (10단계에서 구현)

    def save_and_exit(self):
        self.save()
        print("== 게임 종료 ==")

    def run(self):
        try:
            while True:
                self.print_menu()
                choice = get_valid_input("Enter your choice! (1-5): ", MENU_MIN, MENU_MAX)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_high_scores()
                elif choice == 5:
                    self.save_and_exit()
                    break
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️  게임 중단")
            self.save_and_exit()


def main():
    game = QuizGame(quizzes=list(DEFAULT_QUIZZES), best_score=0)
    game.run()


if __name__ == "__main__":
    main()