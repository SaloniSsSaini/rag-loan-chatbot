# System Architecture - Futuristic AI Voice Agent Dashboard

## 🔹 Overview
This project follows a modular client-server architecture integrating:
- **Frontend (Streamlit/React)** → UI for voice/text interaction
- **Backend (FastAPI)** → Handles requests, AI responses, sentiment analysis
- **External APIs** → OpenAI / Murf API for NLP + TTS
- **Database (Optional)** → User sessions and history

---

## 🔹 Flow Diagram
User Mic 🎙️ → SpeechRecognition → Backend (FastAPI) → OpenAI/MURF → Response → gTTS → Audio Output 🔊

---

## 🔹 Components
- **Frontend:** Streamlit/React UI with chat, mic input, dark mode
- **Backend:** FastAPI app for AI logic + TTS integration
- **APIs:** OpenAI, Murf, gTTS
- **Storage:** Optional (SQLite / Firebase)# rag-loan-chatbot
