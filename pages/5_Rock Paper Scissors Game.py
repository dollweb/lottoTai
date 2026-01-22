import streamlit as st
import random

# --- 1. 게임 초기화 및 상태 관리 ---
# Streamlit은 앱이 다시 로드될 때마다 코드를 처음부터 실행하므로,
# 게임 상태를 저장하기 위해 st.session_state를 사용합니다.
if 'player_score' not in st.session_state:
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_result = "게임을 시작해 보세요!"
    st.session_state.player_choice_display = ""
    st.session_state.computer_choice_display = ""

choices = {"가위": "✂️", "바위": "🪨", "보": "📄"}
choice_list = list(choices.keys()) # ['가위', '바위', '보']

# --- 2. 게임 로직 함수 ---
def play_round(player_choice):
    computer_choice = random.choice(choice_list)

    st.session_state.player_choice_display = f"플레이어: {choices[player_choice]}"
    st.session_state.computer_choice_display = f"컴퓨터: {choices[computer_choice]}"

    if player_choice == computer_choice:
        st.session_state.game_result = "무승부!"
    elif (player_choice == "바위" and computer_choice == "가위") or \
         (player_choice == "가위" and computer_choice == "보") or \
         (player_choice == "보" and computer_choice == "바위"):
        st.session_state.game_result = "플레이어 승리!"
        st.session_state.player_score += 1
    else:
        st.session_state.game_result = "컴퓨터 승리!"
        st.session_state.computer_score += 1
    
    st.rerun() # 상태 업데이트 후 화면 즉시 새로고침

def reset_game():
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.game_result = "게임을 시작해 보세요!"
    st.session_state.player_choice_display = ""
    st.session_state.computer_choice_display = ""
    st.rerun()

# --- 3. 게임 화면 구성 ---
st.title("✂️🪨📄 가위바위보 게임!")

# 현재 스코어 표시
st.sidebar.header("점수 현황")
st.sidebar.write(f"플레이어: {st.session_state.player_score}점")
st.sidebar.write(f"컴퓨터: {st.session_state.computer_score}점")
if st.sidebar.button("점수 초기화"):
    reset_game()

st.header(st.session_state.game_result) # 게임 결과 메시지

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 나의 선택")
    st.write(st.session_state.player_choice_display)

with col2:
    st.markdown("### 컴퓨터의 선택")
    st.write(st.session_state.computer_choice_display)

st.markdown("---") # 구분선

st.subheader("무엇을 내시겠습니까?")

# 선택 버튼들
buttons_col1, buttons_col2, buttons_col3 = st.columns(3)
with buttons_col1:
    if st.button("가위 ✂️", use_container_width=True):
        play_round("가위")
with buttons_col2:
    if st.button("바위 🪨", use_container_width=True):
        play_round("바위")
with buttons_col3:
    if st.button("보 📄", use_container_width=True):
        play_round("보")