import chromadb
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(name="test_collection")

# Define text documents
documents=[
        {"id": "doc1", "text":"Hello, world!"},
        {"id": "doc2", "text":"How are you today"},
        {"id": "doc3", "text":"Goodbye, see you later!"},
]

for doc in documents:
    collection.upsert(ids=doc["id"], documents=[doc["text"]])
    

# Define a query text
query = "Hello, world!"

results = collection.query(
    query_texts=[query],
    n_results=3
)

print(results)