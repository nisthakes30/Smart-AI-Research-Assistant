import streamlit as st
from utils import extract_text_from_pdf
from summarizer import generate_summary
from qa import answer_question, highlight_answer
from quiz import generate_quiz

# Page config
st.set_page_config(page_title="Smart AI Research Assistant", page_icon="🧠", layout="wide")

# Styling
st.markdown("""
    <style>
    html, body {
        background-color: #f4f6ff;
        color: black;
    }
    .block-container { padding: 2rem 3rem; }
    h1 {
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
        color: #1a237e;
    }
    .stTabs [data-baseweb="tab-list"] {
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #ede7f6;
        color: #1a237e;
        padding: 12px 24px;
        margin: 0 4px;
        border-radius: 10px 10px 0 0;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(to right, #5c6bc0, #7986cb);
        color: white;
    }
    .result-box {
        background: #ffffff;
        color: black;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        margin-top: 16px;
        font-size: 16px;
        font-weight: 500;
    }
    mark {
        background-color: yellow;
        font-weight: bold;
    }
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("# 🧠 Smart AI Research Assistant")
st.markdown("Summarize, understand, and quiz your documents — beautifully and locally.")

# Upload document
with st.sidebar:
    st.markdown("### 📂 Upload Document")
    uploaded_file = st.file_uploader("Choose file", type=["pdf", "txt"], key="file_uploader_main")

# Initialize session state
if "uploaded_text" not in st.session_state:
    st.session_state.uploaded_text = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = []

# Load document
if uploaded_file:
    if uploaded_file.type == "application/pdf":
        st.session_state.uploaded_text = extract_text_from_pdf(uploaded_file)
    else:
        st.session_state.uploaded_text = uploaded_file.read().decode("utf-8")
    st.sidebar.success("✅ Document uploaded successfully!")

text = st.session_state.uploaded_text

# App interface tabs
if text:
    tab1, tab2, tab3 = st.tabs(["📑 Summary", "💬 Chat", "🧠 Challenge Me"])

    # Tab 1: Summary
    with tab1:
        st.markdown("### 📁 Document Summary")
        with st.spinner("Summarizing..."):
            summary = generate_summary(text)
            st.markdown(f"<div class='result-box'>{summary}</div>", unsafe_allow_html=True)

    # Tab 2: Chat
    with tab2:
        st.markdown("### 💬 Chat with Document")

        for msg in st.session_state.chat_history:
            if msg["role"] == "user":
                st.markdown(f"**👤 You:** {msg['content']}")
            elif msg["role"] == "assistant":
                st.markdown(f"<div class='result-box'><b>🤖 Assistant:</b> {msg['content']}</div>", unsafe_allow_html=True)
            elif msg["role"] == "context":
                st.markdown("🔍 <b>Source Snippet:</b>", unsafe_allow_html=True)
                st.markdown(msg["content"], unsafe_allow_html=True)

        question = st.text_input("Type your question here:", key="chat_input")

        if st.button("Clear Conversation"):
            st.session_state.chat_history = []
            st.rerun()

        if question:
            answer, source = answer_question(text, question)
            highlighted = highlight_answer(answer, source)

            st.session_state.chat_history.append({"role": "user", "content": question})
            st.session_state.chat_history.append({"role": "assistant", "content": answer})
            st.session_state.chat_history.append({"role": "context", "content": highlighted})
            st.rerun()

    # Tab 3: Quiz
    with tab3:
        st.markdown("### 🧠 Challenge Me: Logic-Based Quiz")

        if st.button("🎯 Generate New Quiz"):
            with st.spinner("Generating quiz questions..."):
                raw_quiz = generate_quiz(text)
                questions = [q.strip() for q in raw_quiz.split("Q: ") if q.strip()]
                quiz_data = []

                for q_block in questions:
                    parts = q_block.split("A:")
                    question = parts[0].strip()
                    answer_part = parts[1].split("Justification:")
                    ideal_answer = answer_part[0].strip()
                    justification = answer_part[1].strip() if len(answer_part) > 1 else "N/A"
                    quiz_data.append({
                        "question": question,
                        "ideal_answer": ideal_answer,
                        "justification": justification,
                        "user_answer": ""
                    })

                st.session_state.quiz_data = quiz_data

        score = 0
        if st.session_state.quiz_data:
            for i, q in enumerate(st.session_state.quiz_data):
                st.markdown(f"**Q{i+1}: {q['question']}**")
                user_input = st.text_input(f"Your Answer to Q{i+1}:", key=f"user_answer_{i}")
                q["user_answer"] = user_input

                if user_input:
                    if user_input.strip().lower() in q["ideal_answer"].lower():
                        st.success("✅ Correct!")
                        score += 1
                    else:
                        st.error("❌ Incorrect.")
                    st.markdown(f"**Ideal Answer:** {q['ideal_answer']}")
                    st.markdown(f"**Justification:** {q['justification']}")

            percent = round((score / len(st.session_state.quiz_data)) * 100)
            stars = "⭐️" * score + "✖️" * (len(st.session_state.quiz_data) - score)
            st.markdown(f"### 🏁 Your Score: **{score}/{len(st.session_state.quiz_data)}**")
            st.markdown(f"### 🎯 Accuracy: **{percent}%**")
            st.markdown(f"### ⭐️ Feedback: {stars}")

else:
    st.info("👈 Please upload a .pdf or .txt file to begin.")
