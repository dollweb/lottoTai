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
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # 또는 사용하고자 하는 모델 이름
    messages=[
        {"role": "user", "content": "안녕하세요!"},
    ]
)

# 응답 출력
st.write(response.choices[0].message['content'])