from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def gptOpenAI():
    # Inicializar o modelo de linguagem
    llm = ChatOpenAI(model_name="gpt-3.5-turbo",max_tokens = 150)
    return llm
