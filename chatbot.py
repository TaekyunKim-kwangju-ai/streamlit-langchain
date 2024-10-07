# chatbot.py
from langchain_aws.chat_models import ChatBedrock
from langchain_core.output_parsers import StrOutputParser
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import SystemMessage


class ChatBot:
    def __init__(self, model_id):
        self.model_id = model_id
        self.model = ChatBedrock(model_id=self.model_id)
        self.parser = StrOutputParser()
        self.workflow = StateGraph(state_schema=MessagesState)
        self.workflow.add_node('chat_model', self.call_model)
        self.workflow.add_edge(START, 'chat_model')
        self.memory = MemorySaver()
        self.app = self.workflow.compile(checkpointer=self.memory)
        self.config = {"configurable": {"thread_id": "1"}}
    
    def call_model(self, state: MessagesState):
        system_prompt = (
            "You are a helpful assistant. "
            "Answer all questions to the best of your ability."
        )
        messages = [SystemMessage(content=system_prompt)] + state["messages"]
        chain = self.model | StrOutputParser()
        response = chain.invoke(messages)
        return {"messages": response}

    def generate_response(self, input_text):
        for msg, _ in self.app.stream({'messages': input_text}, config=self.config, stream_mode='messages'):
            yield msg.content