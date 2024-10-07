# chatbot.py
from langchain_aws.chat_models import ChatBedrock
from langchain_core.output_parsers import StrOutputParser

class ChatBot:
    def __init__(self, model_id):
        self.model_id = model_id
        self.model = ChatBedrock(model_id=self.model_id)
        self.parser = StrOutputParser()

    def generate_response(self, input_text):
        chain = self.model | self.parser
        for chunk in chain.stream(input_text):
            yield chunk
