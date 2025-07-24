from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')
index_file = "embeddings/faiss_index.index"
doc_file = "embeddings/docs.pkl"

def build_faiss_index(docs):
    embeddings = model.encode(docs, show_progress_bar=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, index_file)
    with open(doc_file, "wb") as f:
        pickle.dump(docs, f)

def load_index_and_docs():
    index = faiss.read_index(index_file)
    with open(doc_file, "rb") as f:
        docs = pickle.load(f)
    return index, docs, model