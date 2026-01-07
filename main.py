from unittest import result
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import BaseTool
from pydantic_core import ValidationError
from rich import print

load_dotenv()

# Inicializar o modelo de linguagem
llm = ChatOpenAI(model_name="gpt-3.5-turbo",max_tokens = 150)


@tool
def multiply(a: float, b: float) -> float:
    """Multiply a * b and returns the result

    Args:
        a: float multiplicand
        b: float multiplier

    Returns:
        the resulting float of the equation a * b
    """
    return a * b

system_message = SystemMessage(
    "Você é um assistente prestativo. Você tem acesso a ferramentas. Quando o usuário pedir algo"
    " primeiro verifique se você tem uma ferramenta que resolve esse problema."
)

human_message = HumanMessage("Oi, sou Ricardo. Pode me falar quando é 3 vezes 4")
messages: list[BaseMessage] = [system_message, human_message]

tools: list[BaseTool] = [multiply]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)

llm_response = llm_with_tools.invoke(messages)
messages.append(llm_response)

if isinstance(llm_response, AIMessage) and getattr(llm_response, "tool_calls", None):  
    call = llm_response.tool_calls[-1]
    name, args, id_ = call["name"], call["args"], call["id"]

    try:
        content = tools_by_name[name].invoke(args)
        status = 'success'
    except (KeyError, IndexError, TypeError, ValidationError, ValueError) as error:
        content = f"Erro ao chamar a ferramenta {name} com os argumentos {args}: {error}"
        status = 'error'

    tool_message = ToolMessage(
        content=content,
        tool_call_id=id_,
        status=status
        )
    
    messages.append(tool_message)

    llm_response = llm_with_tools.invoke(messages)
    messages.append(llm_response)

    print(messages)

# result = multiply.invoke({"a": 2, "b":10})

