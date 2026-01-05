from typing import Annotated, Literal, TypedDict
from langgraph.graph import StateGraph, add_messages
import operator
from dataclasses import dataclass

# Define o meu estado, que será passado entre os nodes
@dataclass
class State:
    nodes_path: Annotated[list[str], operator.add]
    current_number: int = 0  

# Definir os nodes
def node_a(state: State) -> State: 
    output_state: State = State(nodes_path=["Bom dia"], current_number=state.current_number)
    print("> node_a", f"{state=}", f"{output_state=}")
    return output_state

def node_b(state: State) -> State:
    output_state: State = State(nodes_path=["sim, tudo bem"], current_number=state.current_number)
    print("> node_b", f"{state=}", f"{output_state=}")
    return output_state

def node_c(state: State) -> State:
    output_state: State = State(nodes_path=["Não, não é um bom dia"], current_number=state.current_number)
    print("> node_c", f"{state=}", f"{output_state=}")
    return output_state

# Função condicional para escolher o caminho
def the_conditional(state: State) -> Literal["goes_to_B", "goes_to_C"]:
    if state.current_number >= 50:
        return "goes_to_C"
    else:
        return "goes_to_B"

# Definir o builder do grafo "os nomes dos nodes"
builder = StateGraph(State)
builder.add_node("A", node_a)
builder.add_node("B", node_b)
builder.add_node("C", node_c)

# Conectar as edges (ou arestas)
builder.add_edge("__start__", "A")
builder.add_conditional_edges("A", the_conditional, {"goes_to_B": "B", "goes_to_C": "C"})
builder.add_edge("B", "__end__")
builder.add_edge("C", "__end__")

graph = builder.compile()

# resultado de todo o Graph, com duas respostas
print()
response = graph.invoke(State(nodes_path=[]))
print(f"{response=}")
print()

print()
response = graph.invoke(State(nodes_path=[], current_number=60))
print(f"{response=}")
print()

# aqui vou gerar o graph para ser aberto no site mermaid
# print(graph.get_graph().draw_mermaid())

