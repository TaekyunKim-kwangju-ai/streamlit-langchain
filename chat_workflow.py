# chat_workflow.py
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.checkpoint.memory import MemorySaver

class ChatWorkflow:
    def __init__(self, model_caller):
        self.model_caller = model_caller
        self.workflow = StateGraph(state_schema=MessagesState)
        self.workflow.add_node('chat_model', self._call_model)
        self.workflow.add_edge(START, 'chat_model')
        self.memory = MemorySaver()
        self.app = self.workflow.compile(checkpointer=self.memory)
        self.config = {"configurable": {"thread_id": "1"}}

    def _call_model(self, state: MessagesState):
        messages = state["messages"]
        response = self.model_caller.call_model(messages)
        return {"messages": response}

    def stream_responses(self, input_text):
        """워크플로우를 통해 메시지를 스트리밍"""
        for msg, _ in self.app.stream({'messages': input_text}, config=self.config, stream_mode='messages'):
            yield msg.content
