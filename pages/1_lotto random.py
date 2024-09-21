import streamlit as st
import random
from datetime import datetime, timedelta

# 현재 날짜 가져오기
today = datetime.now()

# 로또 회차 계산
start_date = datetime(2024, 8, 24)  # 기준 날짜
round_duration = timedelta(weeks=1)  # 회차 간격 (1주)

# 현재 날짜와 기준 날짜의 차이 계산
weeks_difference = (today - start_date).days // 7
current_round = 1135 + weeks_difference  # 1134회차부터 시작

# 다음 토요일 날짜 계산
days_until_saturday = (5 - today.weekday()) % 7  # 5는 토요일
current_date = today + timedelta(days=days_until_saturday)

# 세션 상태 초기화
if 'show_lotto' not in st.session_state:
    st.session_state.show_lotto = True  # 기본적으로 로또 화면 표시

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
</style>
""", unsafe_allow_html=True)

# 로또 기능
if st.session_state.show_lotto:
    st.markdown("<h6 style='font-weight: bold;'>로또번호 인공지능 생성!! Lotto Tai_v0.1</h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='font-size: 2.5em; font-weight: bold;'>로또 T아이</h6>", unsafe_allow_html=True)
    st.markdown(f"<h6 style='font-weight: bold;'>{current_round}회차({current_date.strftime('%Y.%m.%d')})</h6>", unsafe_allow_html=True)

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
<div style='text-align: center; margin: 20px 0;'>
    <a href="https://link.coupang.com/a/bPdnqr" target="_blank" referrerpolicy="unsafe-url"><img src="https://ads-partners.coupang.com/banners/803279?subId=&traceId=V0-301-879dd1202e5c73b2-I803279&w=728&h=90" alt=""></a>
</div>
""", unsafe_allow_html=True)

# iframe 배너 추가
st.markdown("""
<div style='text-align: center; margin: 20px 0;'>
    <iframe src="https://coupa.ng/cf3Jkx" width="100%" height="75" frameborder="0" scrolling="no" referrerpolicy="unsafe-url"></iframe>
</div>
""", unsafe_allow_html=True)

# 쿠팡 파트너스 안내 문구 추가
st.markdown("<p style='text-align: center; font-size: 0.8em;'>※ 쿠팡 파트너스 활동을 통해 일정액의 수수료를 제공받을 수 있습니다.</p>", unsafe_allow_html=True)