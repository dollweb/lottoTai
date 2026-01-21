import streamlit as st

# --- 1. 퀴즈 데이터 ---
QUIZ_QUESTIONS = [
    {
        "question": "파이썬에서 리스트의 길이를 알아내는 함수는?",
        "options": ["size()", "count()", "len()", "length()"],
        "answer": "len()"
    },
    {
        "question": "다음 중 가장 오래된 프로그래밍 언어는?",
        "options": ["Python", "Java", "Fortran", "C++"],
        "answer": "Fortran"
    },
    {
        "question": "Streamlit 앱을 실행하는 명령은?",
        "options": ["python run", "streamlit start", "streamlit run", "st run"],
        "answer": "streamlit run"
    },
    {
        "question": "테트리스 게임의 블록을 부르는 이름은?",
        "options": ["Tetrak", "Tetromino", "Tetrapod", "Tetrix"],
        "answer": "Tetromino"
    },
    {
        "question": "지구는 태양 주위를 공전한다.",
        "options": ["O", "X"],
        "answer": "O"
    }
]

# --- 2. 게임 초기화 및 상태 관리 ---
def initialize_quiz():
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.feedback = ""
    st.session_state.answered = False
    st.session_state.game_over = False

if 'question_index' not in st.session_state:
    initialize_quiz()

# --- 3. 게임 로직 함수 ---
def submit_answer(question, selected_option):
    if st.session_state.answered: # 이미 답변했다면 무시
        return

    st.session_state.answered = True
    if selected_option == question["answer"]:
        st.session_state.score += 1
        st.session_state.feedback = "✅ 정답입니다!"
    else:
        st.session_state.feedback = f"❌ 오답입니다. 정답은 '{question['answer']}'였습니다."
    st.rerun()

def next_question():
    st.session_state.question_index += 1
    st.session_state.answered = False
    st.session_state.feedback = ""

    if st.session_state.question_index >= len(QUIZ_QUESTIONS):
        st.session_state.game_over = True
    st.rerun()

def reset_quiz():
    initialize_quiz()
    st.rerun()

# --- 4. 게임 화면 구성 ---
st.title("🧠 재미있는 퀴즈 게임!")

if st.session_state.game_over:
    st.balloons() # 게임 종료 시 축하 풍선
    st.success(f"퀴즈가 끝났습니다! 최종 점수: {st.session_state.score} / {len(QUIZ_QUESTIONS)}")
    if st.button("다시 시작"):
        reset_quiz()
else:
    current_question = QUIZ_QUESTIONS[st.session_state.question_index]

    st.subheader(f"문제 {st.session_state.question_index + 1}. {current_question['question']}")

    # 질문과 옵션 표시
    # st.radio는 여러 옵션 중 하나를 선택하게 합니다.
    selected_option = st.radio(
        "답변을 선택하세요:",
        options=current_question['options'],
        key=f"q_{st.session_state.question_index}_radio", # 각 라디오 버튼이 고유하도록 키 설정
        disabled=st.session_state.answered # 답변했으면 비활성화
    )

    # 답변 제출 버튼
    if not st.session_state.answered: # 아직 답변하지 않았을 때만 버튼 활성화
        if st.button("답변 제출", type="primary", use_container_width=True):
            submit_answer(current_question, selected_option)
    else: # 답변 후 피드백 및 다음 문제 버튼
        if st.session_state.feedback.startswith("✅"):
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

        if st.button("다음 문제", use_container_width=True):
            next_question()

st.sidebar.markdown(f"**현재 점수: {st.session_state.score} / {len(QUIZ_QUESTIONS)}**")
st.sidebar.markdown(f"**진행도: {st.session_state.question_index} / {len(QUIZ_QUESTIONS)}**")