# Smart AI Research Assistant

A GenAI-powered tool that reads and understands structured documents like research papers, resumes, technical manuals, or legal files. This assistant can summarize, answer context-based questions, generate logic-based quizzes, and provide accurate justifications using Retrieval-Augmented Generation (RAG) with local LLMs.

---

## 📌 Objective

To develop a document-aware AI assistant that:

* Understands uploaded documents in depth
* Answers natural language questions using the document
* Generates logic-based questions with ideal answers
* Provides source-based justification for every response
* Works completely offline using local models like Mistral (via Ollama)

---

## ✅ Features

* Upload `.pdf` or `.txt` documents
* Auto-generates summary (within 150 words)
* Ask anything about the document (chat interface with memory)
* Logic-based quiz generation and evaluation
* Source-based answer justification with highlights
* Supports follow-up questions via memory
* RAG (multi-chunk retrieval for better accuracy)
* Simple and clean Streamlit interface (fully local)

---

## 📁 Steps Included in the Project

1. Document uploader with PDF/TXT support
2. Summary generation using local LLM (Mistral)
3. Question Answering via LangChain + FAISS (RAG)
4. Quiz generator with logic-based questions and feedback
5. Memory handling for chat
6. Answer highlighting using `<mark>` HTML tag
7. Streamlit frontend styling and layout design

---

## ⚙️ Configuration & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-ai-assistant.git
cd smart-ai-assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/Scripts/activate   # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull local model using Ollama

```bash
ollama pull mistral
```

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📋 Prerequisites

* Python 3.10+
* Ollama installed locally with Mistral model
* Streamlit installed (`pip install streamlit`)
* PyMuPDF for PDF extraction
* LangChain and langchain-community
* FAISS for vector storage

---

## 📄 Sample Test File

Use the included `sample_ai_article.txt` file or upload your own `.pdf`/`.txt` file to test the app.

---

## 🔗 Demo Walkthrough

Watch the full demo here:
**\[YouTube Demo Video Link – INSERT HERE]**

---

## 🖼️ Screenshots

|

---

## 📂 Folder Structure

```
smart-ai-assistant/
├── app.py
├── qa.py
├── quiz.py
├── summarizer.py
├── utils.py
├── sample_ai_article.txt
├── requirements.txt
├── README.md
├── screenshots/
│   ├── summary.png
│   ├── chat.png
│   └── quiz.png
```

---

## 🙌 Credits

* Built by **Nistha Kesarwani**
* Internship Task: Smart GenAI Research Assistant
* Model: Mistral via Ollama
* Frameworks: Streamlit + LangChain + FAISS

---

## 🚀 Bonus Features Implemented

* [x] Contextual follow-up memory (chat history)
* [x] Answer highlighting using HTML `<mark>`
* [x] Logic-based quiz feedback with scoring
* [x] Multi-chunk RAG for improved accuracy





