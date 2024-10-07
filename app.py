# app.py
import streamlit as st
from ui import ChatUI  # ChatUI 클래스 임포트
from constants import CHAT_MODEL_IDS

# Streamlit 앱 UI 설정
st.title("🦜🔗 랭체인 챗봇")

model_name = 'haiku'
model_id = CHAT_MODEL_IDS[model_name]

# ChatUI 인스턴스가 한 번만 초기화되도록 설정
if 'chat_ui' not in st.session_state:
    st.session_state.chat_ui = ChatUI(model_id)  # ChatUI 인스턴스 생성 후 세션 상태에 저장

chat_ui = st.session_state.chat_ui  # 세션 상태에서 ChatUI 인스턴스 가져오기

# 대화 기록을 화면에 표시
chat_ui.display_chat_history()

# 사용자 입력을 받아 처리
if prompt := chat_ui.get_user_input():
    # 챗봇 응답 생성 및 화면에 표시
    chat_ui.generate_and_display_response(prompt)
