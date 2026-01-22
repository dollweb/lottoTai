import streamlit as st
import random

# --- 1. 게임 초기화 및 상태 관리 ---
if 'dice_result' not in st.session_state:
    st.session_state.dice_result = [] # 주사위 결과 저장
    st.session_state.num_dice = 1     # 굴릴 주사위 개수
    st.session_state.roll_count = 0  # 굴린 횟수

# --- 2. 게임 로직 함수 ---
def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6)) # 1부터 6까지 무작위 숫자
    st.session_state.dice_result = results
    st.session_state.roll_count += 1
    st.rerun()

def reset_dice_roller():
    st.session_state.dice_result = []
    st.session_state.num_dice = 1
    st.session_state.roll_count = 0
    st.rerun()

# 주사위 그림 (유니코드 이모지)
dice_emojis = {
    1: "⚀", 2: "⚁", 3: "⚂",
    4: "⚃", 5: "⚄", 6: "⚅"
}

# --- 3. 게임 화면 구성 ---
st.title("🎲 주사위 굴리기 시뮬레이터")

st.subheader("설정")
# 주사위 개수 선택
num_dice_option = st.selectbox(
    "굴릴 주사위 개수를 선택하세요:",
    options=[1, 2, 3, 4, 5],
    index=st.session_state.num_dice - 1, # 초기값 설정
    key="num_dice_select"
)
if num_dice_option != st.session_state.num_dice:
    st.session_state.num_dice = num_dice_option
    st.session_state.dice_result = [] # 개수 변경 시 결과 초기화
    st.session_state.roll_count = 0

st.markdown("---")

# 주사위 굴리기 버튼
if st.button(f"{st.session_state.num_dice}개의 주사위 굴리기!", type="primary", use_container_width=True):
    roll_dice(st.session_state.num_dice)

if st.session_state.dice_result: # 결과가 있을 때만 표시
    st.subheader("결과")
    result_str = ""
    for r in st.session_state.dice_result:
        result_str += f"{dice_emojis.get(r, '?')} " # 주사위 이모지로 표시
    st.markdown(f"### {result_str}")
    st.markdown(f"총 합: **{sum(st.session_state.dice_result)}**")
    st.write(f"(_총 {st.session_state.roll_count}회 굴렸습니다_)")

st.markdown("---")

if st.session_state.roll_count > 0:
    if st.button("초기화"):
        reset_dice_roller()