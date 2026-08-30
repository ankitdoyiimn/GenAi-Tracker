from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.9,
    max_tokens=1000
)

result = llm.invoke("What is the capital of India?")
print(result.content)