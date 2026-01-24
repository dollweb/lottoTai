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
    
    /* st.button을 카드처럼 보이도록 스타일링 */
    div.stButton > button {
        /* 김태립9784님의 .game-card 기본 스타일 적용 */
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 20px;
        padding: 30px;
        margin: 15px 0; /* 컬럼 배치 시 필요 */
        box-shadow: 0 10px 30px 0 rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        
        width: 100%; /* 컬럼 내에서 가득 차도록 */
        height: auto; /* 내용에 맞춰 높이 자동 조절 */
        border: none; /* Streamlit 기본 버튼 테두리 제거 */
        cursor: pointer;
        text-align: left; /* 내부 콘텐츠 왼쪽 정렬 */
        color: inherit; /* 폰트 색상을 내부 요소에서 상속 */
        white-space: pre-wrap; /* 줄 바꿈 및 공백 유지 */
        font-family: "NanumGothic", sans-serif; /* 나눔고딕 폰트 적용 */
        display: flex; /* 내부 텍스트 및 아이콘 정렬을 위해 */
        flex-direction: column; /* 세로로 배치 */
        align-items: flex-start; /* 좌측 정렬 */
    }
    
    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px 0 rgba(0, 0, 0, 0.3);
    }

    /* 버튼 내부에 텍스트가 있을 때의 스타일 (st.button은 직접 HTML 요소를 포함하지 않으므로, 이 부분이 중요) */
    /* st.button의 텍스트 레이블 자체는 Span 태그 안에 들어갑니다. */
    div.stButton > button > div > p { /* Streamlit이 버튼 텍스트를 감싸는 구조 */
        font-size: 1.8em; /* 제목 폰트 크기 */
        font-weight: bold; /* 제목 굵기 */
        color: #333; /* 제목 색상 */
        margin: 0 0 10px 0; /* 제목 아래 여백 */
        line-height: 1.2;
    }
    
    div.stButton > button > div > p:nth-of-type(2) { /* 두 번째 p 태그, 즉 설명 */
        font-size: 1em; /* 설명 폰트 크기 */
        font-weight: normal;
        color: #555; /* 설명 텍스트 색상 */
        margin-bottom: 0;
        line-height: 1.6;
    }

    /* 아이콘 스타일 - st.button 텍스트 안에 이모지를 직접 넣는 방식 */
    /* 이모지 자체는 span 태그로 감싸지지 않고 텍스트로 인식됩니다. */
    
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
        height: 100%; /* 일정한 높이 유지 */
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
st.markdown('<div class="category-header">🎲 게임 시작하기</div>', unsafe_allow_html=True)

col_game1, col_game2 = st.columns(2)

with col_game1:
    if st.button("🎮 숫자 게임\n\n숫자를 맞혀보세요! 숫자 맞추기 게임으로 당신의 실력을 시험해보세요.", 
                 key="number_game_card_btn", use_container_width=True):
        st.switch_page("pages/1_Number Game.py")

# iframe 배너 추가
st.markdown("""
<div style='text-align: center; margin: 20px 0;'>
    <iframe src="https://coupa.ng/clptOA" width="100%" height="44" frameborder="0" scrolling="no" referrerpolicy="unsafe-url" browsingtopics></iframe>
</div>
""", unsafe_allow_html=True)

# 쿠팡 파트너스 안내 문구 추가
st.markdown("<p style='text-align: center; font-size: 0.8em;'>※ 쿠팡 파트너스 활동을 통해 일정액의 수수료를 제공받을 수 있습니다.</p>", unsafe_allow_html=True)