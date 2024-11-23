import streamlit as st
import openai
from openai import OpenAI

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
if prompt := st.chat_input("질문을 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 전체 대화 내용 포함하여 API 호출
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.messages
    )

    response = completion.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)