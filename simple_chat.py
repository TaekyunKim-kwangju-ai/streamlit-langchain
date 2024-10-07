import streamlit as st
from langchain_aws.chat_models import ChatBedrock
from langchain_core.output_parsers import StrOutputParser

st.title("🦜🔗 랭체인 챗봇 만들기")

CLAUDE_SONNET_ID = 'anthropic.claude-3-5-sonnet-20240620-v1:0'
CLAUDE_HAIKU_ID = 'anthropic.claude-3-haiku-20240307-v1:0'
TEXT_EMBEDDING_ID = 'amazon.titan-embed-text-v2:0'

def generate_response(input_text):
    model = ChatBedrock(model_id=CLAUDE_HAIKU_ID)
    chain = model | StrOutputParser()
    st.info(chain.invoke(input_text))

with st.form("my_form"):
    text = st.text_area(
        "사용자 입력:",
        "LangChain에 대해서 설명해주세요.",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        generate_response(text)