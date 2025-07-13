from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains.question_answering import load_qa_chain

def create_faiss_index(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.create_documents([text])
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)
    return db

def highlight_answer(answer, source):
    import re

    stopwords = {"is", "the", "a", "an", "and", "or", "to", "on", "at", "with", "for", "by", "of", "in"}

    highlighted = source
    answer_words = [w for w in answer.split() if w.lower() not in stopwords and len(w) > 2]

    for word in set(answer_words):
        pattern = re.compile(rf'\b({re.escape(word)})\\b', re.IGNORECASE)
        highlighted = pattern.sub(r'<mark>\1</mark>', highlighted)

    return highlighted



def answer_question(text, question):
    faiss_index = create_faiss_index(text)
    relevant_docs = faiss_index.similarity_search(question, k=3)
    llm = Ollama(model="mistral")
    chain = load_qa_chain(llm, chain_type="stuff")
    answer = chain.run(input_documents=relevant_docs, question=question)
    source = relevant_docs[0].page_content if relevant_docs else ""
    highlighted = highlight_answer(answer, source)
    return answer.strip(), highlighted.strip()

