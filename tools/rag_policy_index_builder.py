import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# Constants
SOURCE_DIR = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "RAAO_sources"
INDEX_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "policy_faiss_index"

# Load documents from PDFs and DOCX
all_docs = []
for file in SOURCE_DIR.iterdir():
    if file.suffix.lower() == ".pdf":
        loader = PyPDFLoader(str(file))
    elif file.suffix.lower() == ".docx":
        loader = Docx2txtLoader(str(file))
    else:
        continue

    docs = loader.load()
    print(f"📄 Loaded: {file.name} with {len(docs)} document(s)")
    all_docs.extend(docs)

# Split into chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs_chunked = splitter.split_documents(all_docs)

# Build vector index
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(docs_chunked, embeddings)

# Save index to disk
vectorstore.save_local(str(INDEX_PATH))
print(f"\n✅ Policy FAISS vector index written to: {INDEX_PATH}")
