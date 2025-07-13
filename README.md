# Smart AI Research Assistant

A local, privacy-friendly GenAI-powered assistant that can read, summarize, reason, quiz, and answer questions about PDF or TXT documents — all running on your own machine.

## 🎯 Objective

To build a **document-aware AI assistant** capable of deep comprehension and logical reasoning over uploaded documents like research papers or technical reports.  
This project was built as part of EZ’s GenAI Internship Task.

---

## ✨ Features

- 📂 Upload PDF or TXT files
- 📑 Auto-summarization in under 150 words
- 💬 Ask Anything: Free-form Q&A grounded in the document
- 🧠 Challenge Me: Logic-based quizzes with feedback & scoring
- 🧠 RAG (Retrieval-Augmented Generation) with Ollama + Mistral
- 🔁 Follow-up memory handling (Chat history)
- 🔍 Source Highlighting: Snippet references in answers
- 💡 Attractive & responsive Streamlit UI (GPT-like)

---

## ⚙️ Prerequisites

- Python 3.10+
- Git
- [Ollama installed](https://ollama.com/download) locally (tested with Mistral model)
- Models: `mistral`, `all-MiniLM-L6-v2` (HuggingFace)
- Optional: VS Code for development

---

## 🛠 Installation & Setup

```bash
# Clone this repo
git clone https://github.com/your-username/Smart-AI-Research-Assistant.git
cd Smart-AI-Research-Assistant

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Pull model with Ollama (once)
ollama pull mistral

📁 Smart-AI-Research-Assistant
│
├── app.py                 # Streamlit interface
├── qa.py                  # Question Answering with RAG
├── quiz.py                # Quiz generator and evaluator
├── summarizer.py          # Summarization logic
├── utils.py               # PDF/TXT extraction utilities
├── requirements.txt       # All dependencies
├── .env                   # API key if using OpenAI (optional)
├── assets/                # Screenshots (optional)
└── README.md              # Project documentation

##🙏 Credits
Developed by Nistha Kesarwani
Part of EZ GenAI Internship 2025 🚀
Powered by Ollama, LangChain, HuggingFace, and Streamlit.

 ##🎬 Demo Walkthrough

##📺 Click to Watch YouTube Demo


## 📸 Screenshots

### 🧠 Smart AI Assistant – Summary Tab
![Summary Screenshot](assets/summary_ui.png)

### 💬 Chat Tab
![Chat Screenshot](assets/chat_ui.png)
