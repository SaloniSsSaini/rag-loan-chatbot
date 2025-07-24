from utils.embed_store import load_index_and_docs
from transformers import pipeline

index, docs, model = load_index_and_docs()
qa_model = pipeline("text2text-generation", model="google/flan-t5-small")

def get_answer(query, k=3):
    query_vec = model.encode([query])
    D, I = index.search(query_vec, k)
    context = "\n".join([docs[i] for i in I[0]])
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"
    result = qa_model(prompt, max_length=200, do_sample=False)
    return result[0]['generated_text']