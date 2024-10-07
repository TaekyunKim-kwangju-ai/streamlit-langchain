# model_caller.py
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage

class ModelCaller:
    def __init__(self, model):
        self.model = model
        self.parser = StrOutputParser()

    def call_model(self, messages):
        """모델을 호출하여 메시지에 대한 응답을 생성"""
        system_prompt = (
            "You are a helpful assistant. "
            "Answer all questions to the best of your ability."
        )
        full_messages = [SystemMessage(content=system_prompt)] + messages
        chain = self.model | self.parser
        return chain.invoke(full_messages)
