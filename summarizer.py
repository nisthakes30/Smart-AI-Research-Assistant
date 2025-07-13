import ollama

def generate_summary(text, max_words=150):
    if not text or text.strip() == "":
        return "❌ No valid text extracted from the document."

    prompt = f"Summarize this document in under {max_words} words:\n\n{text[:1000]}"
    
    try:
        response = ollama.chat(model='mistral', messages=[
            {"role": "user", "content": prompt}
        ])
        return response['message']['content'].strip()
    except Exception as e:
        return f"❌ Error from LLM: {e}"