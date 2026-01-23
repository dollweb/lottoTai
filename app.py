import streamlit as st
import random
from datetime import datetime, timedelta

# 페이지 설정
st.set_page_config(page_title="LottoAI - 게임 플랫폼", layout="wide", initial_sidebar_state="expanded")

# 커스텀 CSS 스타일
st.markdown("""
<style>
    /* 전체 배경 */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* 타이틀 스타일 */
    .title-container {
        text-align: center;
        padding: 40px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    .title-container h1 {
        color: white;
        font-size: 3.5em;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .title-container p {
        color: #e0e0ff;
        font-size: 1.2em;
        margin: 10px 0 0 0;
    }
    
    /* 게임 카드 스타일 */
    .game-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 20px;
        padding: 30px;
        margin: 15px 0;
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .game-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px 0 rgba(0, 0, 0, 0.3);
    }
    
    .game-title {
        font-size: 1.8em;
        font-weight: bold;
        color: #333;
        margin-bottom: 10px;
    }
    
    .game-desc {
        font-size: 1em;
        color: #555;
        margin-bottom: 15px;
        line-height: 1.6;
    }
    
    /* 버튼 스타일 */
    .game-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 25px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .game-button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* 카테고리 헤더 */
    .category-header {
        font-size: 2em;
        font-weight: bold;
        color: #667eea;
        margin-top: 40px;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 3px solid #667eea;
    }
    
    /* 피처 섹션 */
    .feature-box {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        text-align: center;
        flex: 1;
    }
    
    .feature-icon {
        font-size: 3em;
        margin-bottom: 10px;
    }
    
    .feature-title {
        font-weight: bold;
        color: #667eea;
        font-size: 1.2em;
        margin-bottom: 5px;
    }
    
    .feature-text {
        color: #666;
        font-size: 0.95em;
    }
</style>
""", unsafe_allow_html=True)

# 타이틀 섹션
st.markdown("""
<div class="title-container">
    <h1>🎮 LottoAI 게임 플랫폼</h1>
    <p>다양한 게임을 즐기고 재미있는 경험을 해보세요!</p>
</div>
""", unsafe_allow_html=True)

# 피처 섹션
st.markdown("---")
st.markdown("### ✨ 게임 플랫폼의 특징")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🎯</div>
        <div class="feature-title">다양한 게임</div>
        <div class="feature-text">숫자, 퀴즈, 오목 등 다양한 게임 즐기기</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🏆</div>
        <div class="feature-title">점수 기록</div>
        <div class="feature-text">각 게임의 성적을 기록하고 추적하기</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">빠른 플레이</div>
        <div class="feature-text">언제 어디서나 빠르게 게임 시작하기</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🎁</div>
        <div class="feature-title">재미있는 경험</div>
        <div class="feature-text">친구들과 함께 즐기는 게임 체험</div>
    </div>
    """, unsafe_allow_html=True)

# 게임 섹션
st.markdown("---")
st.markdown('<div class="category-header">🎲 숫자 게임</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="game-card">
        <div class="game-title">🎯 로또 번호 생성</div>
        <div class="game-desc">행운의 로또 번호를 생성해보세요! 매주 다른 번호로 행운을 시도할 수 있습니다.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🎯 로또 게임 시작 →", key="lotto_btn"):
        st.switch_page("pages/1_lotto random.py")

with col2:
    st.markdown("""
    <div class="game-card">
        <div class="game-title">🎮 숫자 게임</div>
        <div class="game-desc">숫자를 맞혀보세요! 스릴 있는 숫자 맞추기 게임으로 당신의 운을 시험해보세요.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🎮 숫자 게임 시작 →", key="number_btn"):
        st.switch_page("pages/4_Number Game.py")

# 퀴즈 섹션
st.markdown('<div class="category-header">🧠 지식 게임</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="game-card">
        <div class="game-title">📝 퀴즈 게임</div>
        <div class="game-desc">100개의 쉬운 상식 문제 중 랜덤으로 5개를 선택해서 풀어보세요! 당신의 지식을 테스트하는 즐거운 시간입니다.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📝 퀴즈 게임 시작 →", key="quiz_btn"):
        st.switch_page("pages/8_Simple Quiz Game.py")

with col2:
    st.markdown("""
    <div class="game-card">
        <div class="game-title">🤖 챗봇</div>
        <div class="game-desc">AI 챗봇과 대화해보세요! 다양한 주제로 흥미로운 대화를 나눌 수 있습니다.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🤖 챗봇 시작 →", key="chatbot_btn"):
        st.switch_page("pages/2_chatbot.py")

# 전략 게임 섹션
st.markdown('<div class="category-header">♟️ 전략 게임</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="game-card">
        <div class="game-title">⚫ 오목</div>
        <div class="game-desc">흑백 바둑돌을 놓아가며 5개를 만드세요! 전략적인 사고가 필요한 고전 게임입니다.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("⚫ 오목 게임 시작 →", key="gomoku_btn"):
        st.switch_page("pages/6_Gomoku Game.py")

with col2:
    st.markdown("""
    <div class="game-card">
        <div class="game-title">🗻 보 바위 보</div>
        <div class="game-desc">컴퓨터와 함께 보, 바위, 보 게임을 해보세요! 전 세계에서 가장 인기 있는 손가락 게임입니다.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🗻 보 바위 보 시작 →", key="rps_btn"):
        st.switch_page("pages/5_Rock Paper Scissors Game.py")

with col3:
    st.markdown("""
    <div class="game-card">
        <div class="game-title">🎲 주사위 게임</div>
        <div class="game-desc">주사위를 굴려보세요! 운이 좋으면 높은 점수를 얻을 수 있습니다.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🎲 주사위 게임 시작 →", key="dice_btn"):
        st.switch_page("pages/7_Dice Roller Game.py")

# 추가 게임 섹션
st.markdown('<div class="category-header">🌟 추가 게임</div>', unsafe_allow_html=True)

st.markdown("""
<div class="game-card">
    <div class="game-title">📍 지도 탐험</div>
    <div class="game-desc">Google Maps를 이용한 지도 탐험 게임! 세계의 다양한 장소를 발견해보세요.</div>
</div>
""", unsafe_allow_html=True)

if st.button("📍 지도 탐험 시작 →", key="map_btn"):
    st.switch_page("pages/3_google map.py")

# 구분선
st.markdown("---")

# 배너 추가
st.markdown("""
<div style='text-align: center; margin: 30px 0;'>
    <a href="https://link.coupang.com/a/bPdnqr" target="_blank" referrerpolicy="unsafe-url"><img src="https://ads-partners.coupang.com/banners/803279?subId=&traceId=V0-301-879dd1202e5c73b2-I803279&w=728&h=90" alt=""></a>
</div>
""", unsafe_allow_html=True)

# 쿠팡 파트너스 안내 문구 추가
st.markdown("<p style='text-align: center; font-size: 0.8em;'>※ 쿠팡 파트너스 활동을 통해 일정액의 수수료를 제공받을 수 있습니다.</p>", unsafe_allow_html=True)

# 하단 정보
st.markdown("""
<hr style='margin-top: 50px;'>
<div style='text-align: center; padding: 20px; color: #666; font-size: 0.9em;'>
    <p><strong>LottoAI Game Platform</strong></p>
    <p>재미있고 다양한 게임으로 즐거운 시간을 보내세요!</p>
    <p>© 2026 All Rights Reserved</p>
</div>
""", unsafe_allow_html=True)