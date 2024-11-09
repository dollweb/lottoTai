import streamlit as st
import openai

# OpenAI API 키 설정 (환경 변수에서 불러오는 것이 좋음)
openai.api_key = "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"  # 여기에 API 키를 입력하세요.

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