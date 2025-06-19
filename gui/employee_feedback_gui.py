import streamlit as st
from pathlib import Path
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Load the RAAO logo
st.image(str(Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "assets" / "branding" / "logo.png"), width=120)

st.title("💬 Employee Voice Panel")
st.caption("Please share your thoughts, concerns, or ideas. Your voice matters.")

# Load policy vector index
INDEX_PATH = Path.home() / "Dropbox" / "EI_Cloud" / "ABL_Rev2_6_1_25" / "data" / "policies" / "policy_faiss_index"
embedding = OpenAIEmbeddings()
vectorstore = FAISS.load_local(str(INDEX_PATH), embeddings=embedding, allow_dangerous_deserialization=True)
llm = ChatOpenAI(model="gpt-4", temperature=0)

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

# User Input
with st.form("voice_feedback"):
    st.subheader("🧠 How can we help you?")
    user_query = st.text_area("Enter your concern, feedback, or policy question here:")
    submit = st.form_submit_button("Ask Policy Assistant")

if submit and user_query:
    with st.spinner("Analyzing your feedback..."):
        response = qa_chain.run(user_query)
    st.success("✅ Policy Guidance")
    st.markdown(f"**Answer:** {response}")
