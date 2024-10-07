# history.py
import streamlit as st

class ChatHistory:
    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def add_message(self, role, content):
        st.session_state.messages.append({"role": role, "content": content})

    def get_history(self):
        return st.session_state.messages
