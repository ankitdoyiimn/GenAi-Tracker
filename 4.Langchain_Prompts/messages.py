from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant that provides information about research papers."),
    HumanMessage(content="Can you summarize Langchain for me?"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
