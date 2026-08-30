from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini")

chat_history = [
    SystemMessage(content="You are a helpful AI assistant."),
]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:", result.content)

    print("\nChat History:")
    for message in chat_history:
        if isinstance(message, SystemMessage):
            print("System:", message.content)
        elif isinstance(message, HumanMessage):
            print("User:", message.content)
        elif isinstance(message, AIMessage):
            print("AI:", message.content) 