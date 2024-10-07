# ui.py
import streamlit as st

class ChatUI:
    def __init__(self, chatbot_manager, history_manager):
        self.chatbot_manager = chatbot_manager
        self.history_manager = history_manager

    def display_chat_history(self):
        """대화 기록을 화면에 표시"""
        for message in self.history_manager.get_history():
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def get_user_input(self):
        """사용자로부터 입력을 받아서 대화 기록에 추가하고, 화면에 표시"""
        prompt = st.chat_input("대화 내용을 입력하세요.")
        if prompt:
            # 사용자 메시지를 대화 기록에 추가
            self.history_manager.add_message("user", prompt)

            # 사용자 메시지를 UI에 표시
            with st.chat_message("user"):
                st.markdown(prompt)

            return prompt
        return None

    def generate_and_display_response(self, prompt):
        """챗봇 응답을 생성하고 화면에 표시"""
        with st.chat_message("assistant"):
            response = st.write_stream(self.chatbot_manager.generate_response(prompt))

            # 챗봇 응답을 대화 기록에 추가
            self.history_manager.add_message("assistant", response)