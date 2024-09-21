import streamlit as st
import requests

# Rasa API 엔드포인트
RASA_API_URL = "http://localhost:8504/webhooks/rest/webhook"

st.title("Rasa 챗봇")

# 사용자 입력 받기
user_input = st.text_input("당신의 질문을 입력하세요:")

if st.button("전송"):
    if user_input:
        # Rasa에 메시지 전송
        response = requests.post(RASA_API_URL, json={"sender": "user", "message": user_input})
        
        # 응답 처리
        if response.status_code == 200:
            bot_responses = response.json()
            for message in bot_responses:
                if 'text' in message:
                    st.write(f"챗봇: {message['text']}")
                else:
                    st.write("챗봇: 응답 메시지가 없습니다.")
        else:
            st.error("Rasa 챗봇에 접근할 수 없습니다.")