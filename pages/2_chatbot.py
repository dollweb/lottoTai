import streamlit as st
import openai
import asyncio

st.title("lottoTai")
openai.api_key = st.secrets["OPENAI_API_KEY"]

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "무엇을 알려드릴까요?"}]

# 대화 내용 출력
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# 사용자 입력 처리
user_input = st.text_input("당신의 질문을 입력하세요:", key="user_input")

if user_input:
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": user_input})

    # OpenAI API 호출
    async def get_response():
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        return response.choices[0].message['content']

    # 비동기 함수 실행
    assistant_message = asyncio.run(get_response())
    
    # 응답 추가
    st.session_state.messages.append({"role": "assistant", "content": assistant_message})

    # 대화 내용 출력
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])