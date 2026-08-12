# 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기

## 프로젝트 개요
Python 표준 라이브러리만으로 구현한 터미널 기반 퀴즈 게임.
메뉴 선택(퀴즈 풀기/추가/목록/최고 점수 확인/종료)으로 동작하며,
state.json에 데이터를 저장해 프로그램 재실행 후에도 퀴즈·최고 점수 유지.

## 퀴즈 주제 선정 이유
세금 상식(원천징수, 연말정산, 과세표준, 부가가치세, 소득공제·세액공제 차이 등)
— 실생활에 필요한 기초 세금 지식 학습 목적.

## 실행 방법
python3 main.py

## 기능 목록
- 퀴즈 풀기: 문제 출제, 정답/오답 판정, 결과(정답 수·100점 환산) 표시
- 퀴즈 추가: 문제/선택지 4개/정답 번호 입력 후 등록
- 퀴즈 목록: 등록된 퀴즈 확인 (없을 시 안내)
- 최고 점수 확인: 최고 점수 조회·갱신 (미풀이 시 안내)
- 종료: 저장 후 안전 종료
- 공통 입력 검증: 공백 제거, 숫자 변환 실패, 범위 밖, 빈 입력 처리
- Ctrl+C / EOF 발생 시 저장 후 안전 종료
- state.json 없음/손상 시 기본 퀴즈로 복구

## 파일 구조
E1_2/
├── main.py
├── state.json
├── .gitignore
├── README.md
└── logs/
    ├── step_1_git_setup_log.txt
    ├── step_2_menu_input_log.txt
    ├── step_3_quiz_class_log.txt
    ├── step_4_default_quiz_data_log.txt
    ├── step_5_play_quiz_branch_log.txt
    ├── step_6_add_quiz_log.txt
    ├── step_7_quizgame_class_log.txt
    ├── step_8_quiz_list_log.txt
    ├── step_8_quiz_list_supplement_log.txt
    ├── step_9_score_log.txt
    ├── step_10_file_io_log.txt
    ├── step_11_readme_log.txt
    └── step_12_clone_pull_log.txt

## 데이터 파일 설명 (state.json)
- quizzes: 퀴즈 목록 (question, choices, answer)
- best_score: 최고 점수
- has_played: 풀이 여부
- UTF-8 인코딩 저장/불러오기
- 파일 없음 → 기본 퀴즈 사용 / JSON 손상 → 기본 퀴즈로 복구(안내 메시지 출력)
> clone/pull 실습 기록 - 2026-08-12
