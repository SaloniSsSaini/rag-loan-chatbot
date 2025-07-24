import streamlit as st
from utils.rag_pipeline import get_answer

st.set_page_config(page_title="RAG Q&A Chatbot", layout="wide")
st.title("📊 Loan Approval RAG Q&A Chatbot")

query = st.text_input("Ask a question about the loan dataset:")

if query:
    with st.spinner("Generating answer..."):
        answer = get_answer(query)
        st.markdown("### 🔍 Answer")
        st.write(answer)