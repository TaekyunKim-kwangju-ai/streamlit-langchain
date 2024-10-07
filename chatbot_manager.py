# chatbot_manager.py
class ChatBotManager:
    def __init__(self, chatbot):
        self.chatbot = chatbot

    def generate_response(self, input_text):
        """입력 텍스트에 대해 챗봇 응답을 생성"""
        for msg in self.chatbot.stream_responses(input_text):
            yield msg  # 스트리밍된 응답을 하나의 문자열로 결합
