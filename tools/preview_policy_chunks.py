from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from pathlib import Path

# Define index path
INDEX_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "policy_faiss_index"

# Load the vectorstore
embedding = OpenAIEmbeddings()
vectorstore = FAISS.load_local(str(INDEX_PATH), embeddings=embedding, allow_dangerous_deserialization=True)

# Preview all documents stored in vector index
print("\n📄 Indexed Policy Chunks:\n" + "-" * 60)
for i, doc in enumerate(vectorstore.docstore._dict.values()):
    print(f"\n🧩 Chunk {i+1}:\n{doc.page_content.strip()}")
