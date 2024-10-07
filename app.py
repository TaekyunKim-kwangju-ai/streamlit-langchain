# app.py
import streamlit as st
from ui import ChatUI  # ChatUI 클래스 임포트
from constants import CHAT_MODEL_IDS
from chatbot_factory import ChatBotFactory

# Streamlit 앱 UI 설정
st.title("🦜🔗 랭체인 챗봇")

# 모델 선택 (현재는 고정된 모델을 사용)
model_name = 'haiku'
model_id = CHAT_MODEL_IDS[model_name]

# ChatBotManager와 ChatHistoryManager 인스턴스가 한 번만 초기화되도록 설정
if 'chat_ui' not in st.session_state:
    # 챗봇 및 기록 관리 매니저 초기화
    chatbot_manager, history_manager = ChatBotFactory.create_chatbot(model_id)

    # ChatUI 인스턴스 생성 후 세션 상태에 저장
    st.session_state.chat_ui = ChatUI(chatbot_manager, history_manager)

chat_ui = st.session_state.chat_ui  # 세션 상태에서 ChatUI 인스턴스 가져오기

# 대화 기록을 화면에 표시
chat_ui.display_chat_history()

# 사용자 입력을 받아 처리
if prompt := chat_ui.get_user_input():
    # 챗봇 응답 생성 및 화면에 표시
    chat_ui.generate_and_display_response(prompt)
