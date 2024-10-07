# ui.py
import streamlit as st
from chatbot import ChatBot
from history import ChatHistory

class ChatUI:
    def __init__(self, model_id):
        self.chat_history = ChatHistory()
        self.chatbot = ChatBot(model_id)

    def display_chat_history(self):
        """대화 기록을 화면에 표시"""
        for message in self.chat_history.get_history():
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def get_user_input(self):
        """사용자로부터 입력을 받아서 대화 기록에 추가하고, 화면에 표시"""
        prompt = st.chat_input("대화 내용을 입력하세요.")
        if prompt:
            # 사용자 메시지를 대화 기록에 추가
            self.chat_history.add_message("user", prompt)

            # 사용자 메시지를 UI에 표시
            with st.chat_message("user"):
                st.markdown(prompt)

            return prompt
        return None

    def generate_and_display_response(self, prompt):
        """챗봇 응답을 생성하고 화면에 표시"""
        with st.chat_message("assistant"):
            response = st.write_stream(self.chatbot.generate_response(prompt))

            # 챗봇 응답을 대화 기록에 추가
            self.chat_history.add_message("assistant", response)

