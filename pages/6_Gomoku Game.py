import streamlit as st
import random

# --- 1. 게임 초기화 및 상태 관리 ---
def initialize_omok():
    # 15x15 보드 초기화 (225개의 빈 칸)
    st.session_state.board = [[" " for _ in range(15)] for _ in range(15)]
    st.session_state.current_player = "●" # 첫 턴은 항상 검은 돌
    st.session_state.game_over = False
    st.session_state.winner = None # 승자 ('●', '○')
    st.session_state.game_message = "검은 돌(●)의 차례입니다!"

if 'board' not in st.session_state:
    initialize_omok()

# --- 2. 게임 로직 함수 ---
def check_winner_omok(board):
    # 오목 게임에서 승리 조건: 같은 색 돌 5개가 일직선으로 연결
    directions = [
        (0, 1),   # 가로
        (1, 0),   # 세로
        (1, 1),   # 대각선 \
        (1, -1)   # 대각선 /
    ]
    
    for row in range(15):
        for col in range(15):
            stone = board[row][col]
            if stone == " ":
                continue
            
            # 각 방향에서 같은 돌이 연결된 개수 확인
            for dr, dc in directions:
                count = 1
                
                # 정방향으로 확인
                r, c = row + dr, col + dc
                while 0 <= r < 15 and 0 <= c < 15 and board[r][c] == stone:
                    count += 1
                    r += dr
                    c += dc
                
                # 역방향으로 확인
                r, c = row - dr, col - dc
                while 0 <= r < 15 and 0 <= c < 15 and board[r][c] == stone:
                    count += 1
                    r -= dr
                    c -= dc
                
                if count >= 5:
                    return stone  # 승자 반환
    
    return None  # 아직 승자 없음

def handle_click_omok(row, col):
    if st.session_state.board[row][col] == " " and not st.session_state.game_over:
        # 플레이어 턴
        st.session_state.board[row][col] = st.session_state.current_player
        winner = check_winner_omok(st.session_state.board)

        if winner:
            st.session_state.winner = winner
            st.session_state.game_over = True
            winner_name = "검은 돌(●)" if winner == "●" else "흰 돌(○)"
            st.session_state.game_message = f"🎉 {winner_name} 승리! 🎉"
        else:
            st.session_state.current_player = "○" if st.session_state.current_player == "●" else "●"
            current_name = "검은 돌(●)" if st.session_state.current_player == "●" else "흰 돌(○)"
            st.session_state.game_message = f"{current_name}의 차례입니다!"

        st.rerun()  # 상태 업데이트 후 화면 즉시 새로고침

def reset_omok_game():
    initialize_omok()
    st.rerun()

# --- 3. 게임 화면 구성 ---
st.title("⚫⚪ 오목 게임")
st.header(st.session_state.game_message)

# 15x15 보드 그리기
for i in range(15):
    cols = st.columns(15)
    for j in range(15):
        with cols[j]:
            # 버튼 텍스트는 보드 상태에 따라 다르게 표시
            if st.button(
                st.session_state.board[i][j],
                key=f"cell_{i}_{j}",
                use_container_width=True,
                disabled=st.session_state.board[i][j] != " " or st.session_state.game_over
            ):
                handle_click_omok(i, j)

st.markdown("---")
if st.session_state.game_over:
    if st.button("새 게임 시작"):
        reset_omok_game()