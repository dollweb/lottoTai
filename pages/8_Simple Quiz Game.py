import streamlit as st
import random

QUIZ_QUESTIONS = [
    {"question": "대한민국의 수도는?", "options": ["부산", "대구", "서울", "대전"], "answer": "서울"},
    {"question": "2 + 2 = ?", "options": ["2", "3", "4", "5"], "answer": "4"},
    {"question": "개의 울음소리는?", "options": ["야옹", "멍멍", "꽥꽥", "짹짹"], "answer": "멍멍"},
    {"question": "1주일은 며칠인가?", "options": ["5일", "6일", "7일", "8일"], "answer": "7일"},
    {"question": "1년은 몇 개월인가?", "options": ["10개월", "11개월", "12개월", "13개월"], "answer": "12개월"},
    {"question": "신호등의 색깔은?", "options": ["1가지", "2가지", "3가지", "4가지"], "answer": "3가지"},
    {"question": "신호등의 파란색은 무엇을 의미하나?", "options": ["정지", "주의", "통행가능", "좌회전"], "answer": "통행가능"},
    {"question": "신호등의 빨간색은 무엇을 의미하나?", "options": ["통행가능", "주의", "정지", "좌회전"], "answer": "정지"},
    {"question": "신호등의 노란색은 무엇을 의미하나?", "options": ["통행가능", "주의", "정지", "좌회전"], "answer": "주의"},
    {"question": "고양이의 울음소리는?", "options": ["멍멍", "야옹", "꽥꽥", "짹짹"], "answer": "야옹"},
    {"question": "오리의 울음소리는?", "options": ["멍멍", "야옹", "꽥꽥", "짹짹"], "answer": "꽥꽥"},
    {"question": "새의 울음소리는?", "options": ["멍멍", "야옹", "꽥꽥", "짹짹"], "answer": "짹짹"},
    {"question": "무지개의 색 개수는?", "options": ["5가지", "6가지", "7가지", "8가지"], "answer": "7가지"},
    {"question": "무지개의 첫 번째 색은?", "options": ["주황색", "노란색", "빨간색", "파란색"], "answer": "빨간색"},
    {"question": "월요일 다음은?", "options": ["일요일", "화요일", "수요일", "목요일"], "answer": "화요일"},
    {"question": "1월 다음은?", "options": ["3월", "2월", "11월", "12월"], "answer": "2월"},
    {"question": "계절은 몇 가지인가?", "options": ["2가지", "3가지", "4가지", "5가지"], "answer": "4가지"},
    {"question": "봄 다음 계절은?", "options": ["겨울", "여름", "가을", "초여름"], "answer": "여름"},
    {"question": "손가락은 몇 개인가?", "options": ["8개", "9개", "10개", "12개"], "answer": "10개"},
    {"question": "발가락은 몇 개인가?", "options": ["8개", "9개", "10개", "12개"], "answer": "10개"},
    {"question": "얼굴에 눈은 몇 개인가?", "options": ["1개", "2개", "3개", "4개"], "answer": "2개"},
    {"question": "얼굴에 귀는 몇 개인가?", "options": ["1개", "2개", "3개", "4개"], "answer": "2개"},
    {"question": "얼굴에 코는 몇 개인가?", "options": ["1개", "2개", "3개", "4개"], "answer": "1개"},
    {"question": "얼굴에 입은 몇 개인가?", "options": ["1개", "2개", "3개", "4개"], "answer": "1개"},
    {"question": "치아는 대략 몇 개인가?", "options": ["20개", "28개", "32개", "40개"], "answer": "32개"},
    {"question": "우유는 어디서 나오나?", "options": ["닭", "돼지", "소", "양"], "answer": "소"},
    {"question": "계란은 누가 낳나?", "options": ["소", "돼지", "닭", "오리"], "answer": "닭"},
    {"question": "바나나의 색깔은?", "options": ["빨간색", "초록색", "노란색", "주황색"], "answer": "노란색"},
    {"question": "당근의 색깔은?", "options": ["빨간색", "초록색", "노란색", "주황색"], "answer": "주황색"},
    {"question": "상추의 색깔은?", "options": ["빨간색", "초록색", "노란색", "주황색"], "answer": "초록색"},
    {"question": "포도주의 색깔은?", "options": ["투명", "빨간색", "흰색", "분홍색"], "answer": "빨간색"},
    {"question": "우유의 색깔은?", "options": ["투명", "빨간색", "흰색", "노란색"], "answer": "흰색"},
    {"question": "피는 어떤 색인가?", "options": ["파란색", "빨간색", "검은색", "흰색"], "answer": "빨간색"},
    {"question": "숲의 색깔은?", "options": ["파란색", "노란색", "초록색", "검은색"], "answer": "초록색"},
    {"question": "하늘의 색깔은?", "options": ["초록색", "노란색", "파란색", "검은색"], "answer": "파란색"},
    {"question": "밤하늘의 색깔은?", "options": ["파란색", "노란색", "빨간색", "검은색"], "answer": "검은색"},
    {"question": "눈의 색깔은?", "options": ["빨간색", "흰색", "검은색", "주황색"], "answer": "흰색"},
    {"question": "불의 색깔은?", "options": ["파란색", "초록색", "빨간색", "흰색"], "answer": "빨간색"},
    {"question": "나뭇잎의 색깔은?", "options": ["노란색", "파란색", "초록색", "검은색"], "answer": "초록색"},
    {"question": "해는 어디서 뜨나?", "options": ["서쪽", "동쪽", "남쪽", "북쪽"], "answer": "동쪽"},
    {"question": "해는 어디로 질까?", "options": ["동쪽", "서쪽", "남쪽", "북쪽"], "answer": "서쪽"},
    {"question": "달은 언제 뜨나?", "options": ["아침", "낮", "저녁과 밤", "항상"], "answer": "저녁과 밤"},
    {"question": "별은 언제 보이나?", "options": ["아침", "낮", "저녁과 밤", "항상"], "answer": "저녁과 밤"},
    {"question": "물은 몇 도에서 끓나?", "options": ["50도", "75도", "100도", "150도"], "answer": "100도"},
    {"question": "물은 몇 도에서 언나?", "options": ["0도", "10도", "25도", "50도"], "answer": "0도"},
    {"question": "인간의 정상 체온은?", "options": ["35도", "36.5도", "37도", "38도"], "answer": "37도"},
    {"question": "산의 뜻은?", "options": ["평지", "높은 언덕", "골짜기", "들판"], "answer": "높은 언덕"},
    {"question": "바다의 반대는?", "options": ["산", "땅", "호수", "강"], "answer": "땅"},
    {"question": "강물이 흐르는 방향은?", "options": ["산 위로", "산 아래로", "바다로", "하늘로"], "answer": "바다로"},
    {"question": "세계에서 가장 긴 강은?", "options": ["아마존강", "황허강", "나일강", "양쯔강"], "answer": "나일강"},
    {"question": "세계에서 가장 높은 산은?", "options": ["에베레스트산", "K2", "칸첸중가", "로라이마산"], "answer": "에베레스트산"},
    {"question": "세계에서 가장 큰 사막은?", "options": ["칼라하리", "고비", "아라비아", "사하라"], "answer": "사하라"},
    {"question": "세계에서 가장 큰 섬은?", "options": ["스리랑카", "자바", "그린란드", "보르네오"], "answer": "그린란드"},
    {"question": "세계에서 가장 큰 호수는?", "options": ["카스피해", "바이칼호", "탕가니카호", "빅토리아호"], "answer": "카스피해"},
    {"question": "세계에서 가장 큰 나라는?", "options": ["캐나다", "중국", "미국", "러시아"], "answer": "러시아"},
    {"question": "세계에서 가장 인구가 많은 나라는?", "options": ["중국", "미국", "인도", "인도네시아"], "answer": "인도"},
    {"question": "세계에서 가장 작은 나라는?", "options": ["모나코", "산마리노", "바티칸", "룩셈부르크"], "answer": "바티칸"},
    {"question": "영국의 수도는?", "options": ["맨체스터", "런던", "리버풀", "버밍엄"], "answer": "런던"},
    {"question": "프랑스의 수도는?", "options": ["마르세유", "리옹", "파리", "니스"], "answer": "파리"},
    {"question": "이탈리아의 수도는?", "options": ["밀라노", "로마", "베네치아", "나폴리"], "answer": "로마"},
    {"question": "스페인의 수도는?", "options": ["바르셀로나", "마드리드", "발렌시아", "세비야"], "answer": "마드리드"},
    {"question": "독일의 수도는?", "options": ["뮌헨", "베를린", "함부르크", "쾰른"], "answer": "베를린"},
    {"question": "중국의 수도는?", "options": ["상하이", "베이징", "광저우", "충칭"], "answer": "베이징"},
    {"question": "일본의 수도는?", "options": ["오사카", "교토", "도쿄", "나고야"], "answer": "도쿄"},
    {"question": "태국의 수도는?", "options": ["치앙마이", "방콕", "푸켓", "파타야"], "answer": "방콕"},
    {"question": "이집트의 수도는?", "options": ["기자", "룩소르", "카이로", "알렉산드리아"], "answer": "카이로"},
    {"question": "그리스의 수도는?", "options": ["아테네", "스파르타", "테살로니키", "파트라스"], "answer": "아테네"},
    {"question": "러시아의 수도는?", "options": ["상트페테르부르크", "모스크바", "노보시비르스크", "예카테린부르크"], "answer": "모스크바"},
    {"question": "캐나다의 수도는?", "options": ["토론토", "밴쿠버", "오타와", "몬트리올"], "answer": "오타와"},
    {"question": "호주의 수도는?", "options": ["시드니", "멜버른", "캔버라", "브리즈번"], "answer": "캔버라"},
    {"question": "뉴질랜드의 수도는?", "options": ["오클랜드", "웰링턴", "크라이스트처치", "더니든"], "answer": "웰링턴"},
    {"question": "인도의 수도는?", "options": ["뭄바이", "콜카타", "델리", "벵갈루루"], "answer": "델리"},
    {"question": "브라질의 수도는?", "options": ["상파울루", "리우데자네이루", "브라질리아", "살바도르"], "answer": "브라질리아"},
    {"question": "멕시코의 수도는?", "options": ["칸쿤", "몬테레이", "멕시코시티", "푸에르토바야르타"], "answer": "멕시코시티"},
    {"question": "아르헨티나의 수도는?", "options": ["코르도바", "부에노스아이레스", "로사리오", "라플라타"], "answer": "부에노스아이레스"},
    {"question": "미국의 수도는?", "options": ["뉴욕", "로스앤젤레스", "워싱턴DC", "시카고"], "answer": "워싱턴DC"},
    {"question": "사과는 무엇인가?", "options": ["야채", "과일", "곡물", "고기"], "answer": "과일"},
    {"question": "당근은 무엇인가?", "options": ["과일", "고기", "야채", "곡물"], "answer": "야채"},
    {"question": "쌀은 무엇인가?", "options": ["과일", "고기", "야채", "곡물"], "answer": "곡물"},
    {"question": "소는 무엇인가?", "options": ["야채", "과일", "포유류", "곤충"], "answer": "포유류"},
    {"question": "개는 무엇인가?", "options": ["고양이", "물고기", "포유류", "파충류"], "answer": "포유류"},
    {"question": "전화기의 발명자는?", "options": ["에디슨", "갈릴레이", "알렉산더 벨", "라이트형제"], "answer": "알렉산더 벨"},
    {"question": "전기 불빛의 발명자는?", "options": ["알렉산더 벨", "에디슨", "갈릴레이", "라이트형제"], "answer": "에디슨"},
    {"question": "비행기의 발명자는?", "options": ["에디슨", "알렉산더 벨", "갈릴레이", "라이트형제"], "answer": "라이트형제"},
    {"question": "달에 처음 도착한 우주비행사는?", "options": ["버즈 올드린", "닐 암스트롱", "찰리 듀크", "피트 콘래드"], "answer": "닐 암스트롱"},
    {"question": "올림픽의 상징은?", "options": ["한 개의 고리", "다섯 개의 고리", "세 개의 고리", "열 개의 고리"], "answer": "다섯 개의 고리"},
    {"question": "FIFA 월드컵은 몇 년마다 열리는가?", "options": ["2년", "4년", "6년", "8년"], "answer": "4년"},
    {"question": "배구 팀은 몇 명으로 구성되나?", "options": ["5명", "6명", "7명", "8명"], "answer": "6명"},
    {"question": "농구 팀은 몇 명으로 구성되나?", "options": ["4명", "5명", "6명", "7명"], "answer": "5명"},
    {"question": "야구는 몇 이닝으로 진행되나?", "options": ["7이닝", "8이닝", "9이닝", "10이닝"], "answer": "9이닝"},
    {"question": "테니스에서 4판을 이겨야 하는 세트는?", "options": ["1세트", "2세트", "3세트", "4세트"], "answer": "3세트"},
    {"question": "수도권의 정의는?", "options": ["서울의 교외 지역", "서울과 주변 지역", "대도시 지역", "산업 지역"], "answer": "서울과 주변 지역"},
    {"question": "책은 무엇인가?", "options": ["음식", "의류", "정보 매체", "도구"], "answer": "정보 매체"},
    {"question": "연필의 짝은?", "options": ["펜", "지우개", "칠판", "분필"], "answer": "지우개"},
    {"question": "학교에서 배우는 것은?", "options": ["요리", "지식", "운동", "음악"], "answer": "지식"},
    {"question": "병원의 의사는?", "options": ["요리사", "환자", "의료인", "상점원"], "answer": "의료인"},
    {"question": "신발은 어디에 신나?", "options": ["손", "발", "머리", "목"], "answer": "발"},
    {"question": "모자는 어디에 쓰나?", "options": ["발", "손", "머리", "팔"], "answer": "머리"},
    {"question": "시계의 작은 바늘은?", "options": ["분", "초", "시간", "요일"], "answer": "시간"},
    {"question": "시계의 큰 바늘은?", "options": ["시간", "초", "분", "요일"], "answer": "분"},
]

# --- 2. 게임 초기화 및 상태 관리 ---
def initialize_quiz():
    """퀴즈 게임 초기화 - 100개 중 5개 랜덤 선택"""
    st.session_state.selected_questions = random.sample(QUIZ_QUESTIONS, 5)
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.feedback = ""
    st.session_state.user_answer = None
    st.session_state.quiz_started = True

def next_question():
    """다음 문제로 이동"""
    if st.session_state.question_index < len(st.session_state.selected_questions) - 1:
        st.session_state.question_index += 1
        st.session_state.feedback = ""
        st.session_state.user_answer = None
    else:
        st.session_state.quiz_completed = True

def submit_answer(answer):
    """답변 제출"""
    current_question = st.session_state.selected_questions[st.session_state.question_index]
    st.session_state.user_answer = answer
    
    if answer == current_question["answer"]:
        st.session_state.score += 1
        st.session_state.feedback = f"✅ 정답입니다! (답: {current_question['answer']})"
    else:
        st.session_state.feedback = f"❌ 틀렸습니다. (정답: {current_question['answer']})"

# --- 3. 초기화 ---
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = []
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False

# --- 4. UI 구성 ---
st.set_page_config(page_title="간단한 퀴즈 게임", layout="centered")
st.title("🎯 간단한 퀴즈 게임")

# 게임 완료 화면
if st.session_state.quiz_completed:
    st.balloons()
    st.markdown("---")
    st.success("🎉 모든 문제를 완료했습니다! 축하합니다! 🎉")
    
    # 최종 성적 표시
    score = st.session_state.score
    total = len(st.session_state.selected_questions)
    percentage = (score / total) * 100
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("최종 점수", f"{score}/{total}")
    with col2:
        st.metric("정답률", f"{percentage:.1f}%")
    with col3:
        if percentage == 100:
            st.metric("등급", "S (완벽!)")
        elif percentage >= 80:
            st.metric("등급", "A (우수!)")
        elif percentage >= 60:
            st.metric("등급", "B (좋음!)")
        else:
            st.metric("등급", "C (노력!)")
    
    st.markdown("---")
    st.write("### 다시 도전해보세요!")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 다시 시작", use_container_width=True):
            st.session_state.quiz_completed = False
            st.session_state.quiz_started = False
            st.rerun()
    with col2:
        if st.button("🏠 홈으로", use_container_width=True):
            st.session_state.quiz_completed = False
            st.session_state.quiz_started = False
            st.rerun()

elif not st.session_state.quiz_started:
    st.write("### 🎮 100가지 문제 중에서 랜덤으로 5가지 문제를 풀어보세요!")
    if st.button("퀴즈 시작하기", use_container_width=True, key="start_button"):
        initialize_quiz()
        st.rerun()
else:
    # 진행 상황 표시
    progress = st.session_state.question_index / len(st.session_state.selected_questions)
    st.progress(progress)
    
    # 현재 문제 표시
    current_question = st.session_state.selected_questions[st.session_state.question_index]
    st.write(f"### 문제 {st.session_state.question_index + 1}/{len(st.session_state.selected_questions)}")
    st.write(f"**{current_question['question']}**")
    
    # 답변 선택
    if st.session_state.user_answer is None:
        for option in current_question["options"]:
            if st.button(option, use_container_width=True, key=option):
                submit_answer(option)
                st.rerun()
    else: # 답변 후 피드백 및 다음 문제 버튼
        if st.session_state.feedback.startswith("✅"):
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

        if st.button("다음 문제", use_container_width=True):
            next_question()
            st.rerun()

st.sidebar.markdown(f"**현재 점수: {st.session_state.score} / {len(st.session_state.selected_questions) if st.session_state.selected_questions else 5}**")
st.sidebar.markdown(f"**진행도: {st.session_state.question_index} / {len(st.session_state.selected_questions) if st.session_state.selected_questions else 5}**")

# 배너 추가
st.markdown("""
<div style='text-align: center; margin: 20px 0;'>
    <a href="https://link.coupang.com/a/bPdnqr" target="_blank" referrerpolicy="unsafe-url"><img src="https://ads-partners.coupang.com/banners/803279?subId=&traceId=V0-301-879dd1202e5c73b2-I803279&w=728&h=90" alt=""></a>
</div>
""", unsafe_allow_html=True)

# 쿠팡 파트너스 안내 문구 추가
st.markdown("<p style='text-align: center; font-size: 0.8em;'>※ 쿠팡 파트너스 활동을 통해 일정액의 수수료를 제공받을 수 있습니다.</p>", unsafe_allow_html=True)
