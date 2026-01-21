import streamlit as st
import random

# --- 1. 게임 초기화 및 상태 관리 ---
def initialize_tic_tac_toe():
    st.session_state.board = [" " for _ in range(9)] # 3x3 보드, 1차원 리스트로 관리
    st.session_state.current_player = "X" # 첫 턴은 항상 X
    st.session_state.game_over = False
    st.session_state.winner = None # 승자 ('X', 'O', 'Draw')
    st.session_state.game_message = "X의 차례입니다!"

if 'board' not in st.session_state:
    initialize_tic_tac_toe()

# --- 2. 게임 로직 함수 ---
def check_winner(board):
    win_conditions = [
        # 가로
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        # 세로
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        # 대각선
        [0, 4, 8], [2, 4, 6]
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] and board[cond[0]] != " ":
            return board[cond[0]] # 승자 반환
    if " " not in board:
        return "Draw" # 무승부
    return None # 아직 승자 없음

def handle_click(index):
    if st.session_state.board[index] == " " and not st.session_state.game_over:
        # 플레이어 턴
        st.session_state.board[index] = st.session_state.current_player
        winner = check_winner(st.session_state.board)

        if winner:
            st.session_state.winner = winner
            st.session_state.game_over = True
            if winner == "Draw":
                st.session_state.game_message = "무승부입니다!"
            else:
                st.session_state.game_message = f"🎉 {winner} 승리! 🎉"
        else:
            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
            st.session_state.game_message = f"{st.session_state.current_player}의 차례입니다!"

        st.rerun() # 상태 업데이트 후 화면 즉시 새로고침

def reset_tic_tac_toe_game():
    initialize_tic_tac_toe()
    st.rerun()

# --- 3. 게임 화면 구성 ---
st.title("⭕❌ O-X 게임")
st.header(st.session_state.game_message)

# 3x3 보드 그리기
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        idx = i * 3 + j
        with cols[j]:
            # 버튼 텍스트는 보드 상태에 따라 다르게 표시
            # 게임이 끝났거나 이미 채워진 칸은 비활성화
            if st.button(
                st.session_state.board[idx],
                key=f"cell_{idx}",
                use_container_width=True,
                disabled=st.session_state.board[idx] != " " or st.session_state.game_over
            ):
                handle_click(idx)

st.markdown("---")
if st.session_state.game_over:
    if st.button("새 게임 시작"):
        reset_tic_tac_toe_game()