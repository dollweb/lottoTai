import streamlit as st
import openai

# OpenAI API 키 설정
openai.api_key = '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'  # 여기에 본인의 API 키를 입력하세요.

# 스트림릿 앱 설정
st.title("ChatGPT 챗봇")
st.write("ChatGPT와 대화해보세요!")

# 세션 상태 초기화
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# 사용자 입력 받기
user_input = st.text_input("당신의 질문을 입력하세요:")

def get_chatgpt_response(user_input):
    response = openai.ChatCompletion.create(  # 올바른 API 호출
        model="gpt-3.5-turbo",  # 사용할 모델
        messages=[
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']  # 응답 접근 방식

if st.button("전송"):
    if user_input:
        # 사용자 입력 저장
        st.session_state.chat_history.append(f"사용자: {user_input}")
        
        # ChatGPT 응답 생성
        bot_response = get_chatgpt_response(user_input)
        st.session_state.chat_history.append(f"챗봇: {bot_response}")

# 대화 기록 표시
if st.session_state.chat_history:
    st.write("대화 기록:")
    for chat in st.session_state.chat_history:
        st.write(chat)