import streamlit as st
import random

# 제목
st.title("Lotto Tai_v0.1(로또 T아이)")

# 부제목 추가
st.markdown("<h4 style='font-weight: bold;'>인공지능 생성 로또 번호를 통한 새로운 기회!!</h2>", unsafe_allow_html=True)

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
if st.button("LOTTO 번호 5세트 생성하기"):
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