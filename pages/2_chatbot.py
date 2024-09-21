import streamlit as st
from openai import OpenAI

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"assistant","content":"무엇을 알려드릴까요?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("질문을 입력하세요"):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response = completion.to_dict()["choices"][0]["message"]["content"]
    st.session_state.messages.append({"role":"assistant","content":response})
    with st.chat_message("assistant"):
        st.markdown(response)