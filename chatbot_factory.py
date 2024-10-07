# chatbot_factory.py
from chatbot_manager import ChatBotManager
from history_manager import ChatHistoryManager
from model_caller import ModelCaller
from chat_workflow import ChatWorkflow
from langchain_aws.chat_models import ChatBedrock

class ChatBotFactory:
    @staticmethod
    def create_chatbot(model_id):
        model = ChatBedrock(model_id=model_id)
        model_caller = ModelCaller(model)
        chatbot = ChatWorkflow(model_caller)
        chatbot_manager = ChatBotManager(chatbot)
        return chatbot_manager, ChatHistoryManager()
