import streamlit as st
import random
from datetime import datetime, timedelta

# 현재 날짜 가져오기
today = datetime.now()

# CSS 스타일 정의
st.markdown("""
<style>
.circle {
    display: inline-block;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    line-height: 30px;
    text-align: center;
    font-size: 15px;
    margin: 5px;
    color: white;
}
.dark-yellow { background-color: #FFD700; }
.blue { background-color: blue; }
.red { background-color: red; }
.gray { background-color: gray; }
.green { background-color: green; }

/* 버튼 스타일 */
.stButton > button {
    background-color: #f0f0f0; /* 밝은 회색 배경색 */
    color: black; /* 글자색을 검정으로 변경 */
    border: none; /* 테두리 없음 */
    padding: 15px 30px; /* 여백 */
    text-align: center; /* 텍스트 중앙 정렬 */
    text-decoration: none; /* 텍스트 장식 없음 */
    display: inline-block; /* 인라인 블록 요소 */
    font-size: 15px; /* 글자 크기 */
    margin: 4px 2px; /* 마진 */
    cursor: pointer; /* 커서 모양 */
    border-radius: 8px; /* 모서리 둥글기 */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08); /* 그림자 효과 */
    transition: background-color 0.3s, transform 0.2s; /* 효과 전환 */
}

.stButton > button:hover {
    background-color: #e0e0e0; /* 호버 시 밝은 회색으로 변화 */
    transform: translateY(-2px); /* 위로 이동 효과 */
}
</style>
""", unsafe_allow_html=True)

# 회차 및 날짜 설정
if today.weekday() == 6:  # 일요일
    # 다음 회차 및 날짜 계산
    current_round = 1134 + 1  # 다음 회차
    current_date = today + timedelta(days=1)  # 다음날 (월요일)
else:
    current_round = 1134
    current_date = today  # 현재 날짜 사용

# 제목
st.markdown("<h6 style='font-weight: bold;'>로또번호 인공지능 생성!! Lotto Tai_v0.1</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='font-size: 2.5em; font-weight: bold;'>로또 T아이</h6>", unsafe_allow_html=True)
st.markdown(f"<h6 style='font-weight: bold;'>{current_round}회차({current_date.strftime('%Y.%m.%d')})</h6>", unsafe_allow_html=True)

# 방문자 카운트 초기화
if 'total_visits' not in st.session_state:
    st.session_state.total_visits = 0
if 'daily_visits' not in st.session_state:
    st.session_state.daily_visits = 0

# 방문자 수 카운트
st.session_state.total_visits += 1
st.session_state.daily_visits += 1

# 방문자 수 표시
st.sidebar.write(f"오늘 방문자 수: {st.session_state.daily_visits}")
st.sidebar.write(f"전체 방문자 수: {st.session_state.total_visits}")

# 버튼 클릭 시 동작
button_text = "로또번호 5세트 생성 버튼"
if st.button(button_text):
    # 1부터 45까지의 숫자 생성
    numbers = list(range(1, 46))
    
    # 5개의 랜덤 번호 세트 생성
    all_numbers = []
    for _ in range(5):
        random_numbers = random.sample(numbers, 6)
        sorted_numbers = sorted(random_numbers)
        all_numbers.append(sorted_numbers)
    
    # 결과 출력
    st.write("로또번호 정보만 제공하고, 투자의 책임은 본인에게 있습니다.")
    number_sets_display = ""  # 모든 세트를 저장할 변수
    
    for idx, number_set in enumerate(all_numbers):
        number_display = ""
        for number in number_set:
            # 색상 설정
            if 1 <= number <= 10:
                color_class = "dark-yellow"
            elif 11 <= number <= 20:
                color_class = "blue"
            elif 21 <= number <= 30:
                color_class = "red"
            elif 31 <= number <= 40:
                color_class = "gray"
            else:
                color_class = "green"
            
            number_display += f'<div class="circle {color_class}">{number}</div>'
        
        # 각 세트를 한 줄에 표시
        number_sets_display += f"<div style='display: inline-block; margin-right: 10px;'>{idx + 1}세트: {number_display}</div>"

    # 모든 세트를 한 번에 출력
    st.markdown(number_sets_display, unsafe_allow_html=True)
    
# 배너 추가
st.markdown("""
<div style='text-align: center;'>
    <script src="https://ads-partners.coupang.com/g.js"></script>
    <script>
        new PartnersCoupang.G({
            "id":803207,
            "template":"carousel",
            "trackingCode":"AF1929818",
            "width":"500",
            "height":"100",
            "tsource":""
        });
    </script>
</div>
""", unsafe_allow_html=True)

# iframe 배너 추가
st.markdown("""
<div style='text-align: center;'>
    <iframe src="https://coupa.ng/cf3Jkx" width="100%" height="75" frameborder="0" scrolling="no" referrerpolicy="unsafe-url"></iframe>
</div>
""", unsafe_allow_html=True)