# history_manager.py
class ChatHistoryManager:
    def __init__(self):
        self.messages = []

    def add_message(self, role, content):
        """대화 기록에 메시지를 추가"""
        self.messages.append({"role": role, "content": content})

    def get_history(self):
        """대화 기록을 반환"""
        return self.messages
