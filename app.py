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
    <h1>🎮 케이트립 게임 앱</h1>
    <p>누구나 게임을 즐기는 경험을 해보세요!</p>
</div>
""", unsafe_allow_html=True)

# 피처 섹션
st.markdown("---")
st.markdown("### ✨ 게임 앱 특징")

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
    st.button("""
    <div class="game-title"><span class="icon">🎮</span> 숫자 게임</div>
    <div class="game-desc">숫자를 맞혀보세요! 숫자 맞추기 게임으로 당신의 실력을 시험해보세요.</div>
    """, unsafe_allow_html=True, key="number_game_card_btn"):
        st.switch_page("pages/1_Number Game.py")

# iframe 배너 추가
st.markdown("""
<div style='text-align: center; margin: 20px 0;'>
    <iframe src="https://coupa.ng/clptOA" width="100%" height="44" frameborder="0" scrolling="no" referrerpolicy="unsafe-url" browsingtopics></iframe>
</div>
""", unsafe_allow_html=True)

# 쿠팡 파트너스 안내 문구 추가
st.markdown("<p style='text-align: center; font-size: 0.8em;'>※ 쿠팡 파트너스 활동을 통해 일정액의 수수료를 제공받을 수 있습니다.</p>", unsafe_allow_html=True)