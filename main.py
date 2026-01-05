import json
from typing import Annotated, Literal, Sequence, TypedDict
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langgraph.graph import StateGraph, add_messages
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from rich import print
from rich.markdown import Markdown

load_dotenv()

# Inicializar o modelo de linguagem
llm = ChatOpenAI(model_name="gpt-3.5-turbo",max_tokens = 150)

# 1 - Defino o meu State
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]

# 2 - Defino os meus Nodes
def call_llm(state: AgentState) -> AgentState:
    llm_result = llm.invoke(state["messages"])
    return {"messages": [llm_result]}

# 3 - Criar o StateGraph
builder = StateGraph(
    AgentState,
    context_schem=None,
    input_schema=AgentState,
    output_schema=AgentState,
)

# 4 - Adicionar nodes ao grafico
builder.add_node("call_llm", call_llm)
builder.add_edge("__start__", "call_llm")
builder.add_edge("call_llm", "__end__")

# 5 - Copilar o grafo
graph = builder.compile()

if __name__ == "__main__":
    # 6 - Executar o grafo
    user_input = "Olá, meu nome é Raquel"
    human_message = HumanMessage(user_input)
    result = graph.invoke({"messages": [human_message]})

    print(result["messages"][1].content)
    print(Markdown("---"))

    # Converte cada mensagem para dicionário, modo debug com mais exclarecimentos
    # result_json = {
    #     "messages": [msg.model_dump() for msg in result["messages"]]
    # }
    # print(json.dumps(result_json, indent=2, ensure_ascii=False))



 


