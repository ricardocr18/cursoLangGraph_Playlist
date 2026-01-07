# Curso LangChain e LangGraph - Playlist

## 📖 Sobre o Projeto

Este repositório contém **implementações práticas** dos conceitos apresentados na playlist [**"LangChain e LangGraph"**](https://www.youtube.com/playlist?list=PLbIBj8vQhvm09IqqLYIwLF5dGrcbJzFZc), ministrada por **Otavio Miranda**.

A playlist aborda desde conceitos fundamentais até técnicas avançadas de construção de agentes de IA utilizando as bibliotecas **LangChain** e **LangGraph**.

### 🎯 Propósito

- 📝 Documentar o processo de aprendizado
- 💻 Fornecer código funcional e comentado
- 🔄 Facilitar a revisão de conceitos
- 🚀 Servir como referência para projetos futuros

### 👨‍🏫 Créditos

Todo o conteúdo educacional é baseado nos ensinamentos de **[Otavio Miranda](https://github.com/luizomf)**, criador da playlist original.

---

## 📚 Estrutura do Projeto

Cada branch representa um vídeo diferente da playlist:

| Branch | Descrição | Status |
|--------|-----------|--------|
| [`vide0001`](https://github.com/ricardocr18/cursoLangGraph_Playlist/tree/video001) | Primeiros passos com langchain | ✅ Completo |
| [`video002`](https://github.com/ricardocr18/cursoLangGraph_Playlist/tree/video002) | Utilizando Nodes, Edges e Graph | ✅ Completo |
| [`video003`](https://github.com/ricardocr18/cursoLangGraph_Playlist/tree/video003) | Criando Chat Bot com memória | ✅ Completo |
| [`video004`](https://github.com/ricardocr18/cursoLangGraph_Playlist/tree/video004) | Criando a primeira tool |🚧 Em construção |
| [`video005`]  |🚧 Em construção |

### Branches Disponíveis

- **`video001`** - Introdução ao LangChain: ChatBot básico com histórico de conversa
  - Implementação de um chatbot usando OpenAI
  - Gerenciamento de mensagens do sistema e do usuário
  - Loop de conversação interativo

- **`video002`** - Utilizando Nodes, edges e conditional edges e visualização do graph
    - Criação de grafos de estado com `StateGraph`
    - Nodes (A, B, C) e conditional edges
    - Funções de redução com `operator.add`
    - `TypedDict` vs `@dataclass`
    - Visualização com Mermaid

- **`video003`** - Integração LLM + LangGraph
    - Invocação de LLM dentro de nodes
    - `add_messages` para histórico
    - `HumanMessage` e `AIMessage`
    - Formatação com `rich`
    - Imutabilidade do estado

## 🚀 Como usar
Exemplo de como Clonar apenas o código do Vídeo 1    

1. Clone o repositório:
  ```bash
  # Exemplo: Clonar apenas o código do Vídeo 1
  git clone -b video001 --single-branch https://github.com/ricardocr18/cursoLangGraph_Playlist.git video001
  ```

2. Mude para a branch do vídeo que deseja estudar:
   ```bash
   git checkout video001
   ```

3. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Configure suas variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`
   - Adicione suas chaves de API

6. Execute o código:
   ```bash
   python main.py
   ```

## 📋 Requisitos

- Python 3.8+
- Conta OpenAI com API Key

## 🔗 Links Úteis

- [Documentação LangChain](https://docs.langchain.com/)
- [Documentação LangGraph](https://langchain-ai.github.io/langgraph/)

## 📝 Notas

- Cada branch é independente e contém o código completo do respectivo vídeo

## 👤 Autor

Ricardo - [@ricardocr18](https://github.com/ricardocr18)
