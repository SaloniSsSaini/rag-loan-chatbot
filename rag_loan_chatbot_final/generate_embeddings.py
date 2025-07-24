from utils.data_preprocess import load_and_prepare_data
from utils.embed_store import build_faiss_index

docs = load_and_prepare_data("data/Training Dataset.csv")
build_faiss_index(docs)
print("✅ Embeddings and FAISS index created successfully.")