from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",dimensions=32
)

Documents = [
    "Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Kolkata is the cultural capital of India.",
    "Paris is the capital of France."]

embedding_vector = embeddings.embed_documents(Documents)

print(str(embedding_vector))