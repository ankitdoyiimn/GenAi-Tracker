from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

Documents = [
    "Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Kolkata is the cultural capital of India.",
    "Paris is the capital of France."
]

embedding_vector = embeddings.embed_documents(Documents)

print(embedding_vector)