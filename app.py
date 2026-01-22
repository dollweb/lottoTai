import streamlit as st
import random
from datetime import datetime, timedelta

st.title("메인 페이지")
st.write("여기는 메인 페이지입니다.")

# iframe 배너 추가
st.markdown("""
<div style='text-align: center; margin: 20px 0;'>
    <iframe src="https://coupa.ng/cf3Jkx" width="100%" height="75" frameborder="0" scrolling="no" referrerpolicy="unsafe-url"></iframe>
</div>
""", unsafe_allow_html=True)

# 쿠팡 파트너스 안내 문구 추가
st.markdown("<p style='text-align: center; font-size: 0.8em;'>※ 쿠팡 파트너스 활동을 통해 일정액의 수수료를 제공받을 수 있습니다.</p>", unsafe_allow_html=True)