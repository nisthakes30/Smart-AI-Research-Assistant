from dotenv import load_dotenv
import os
import ollama  # using local Mistral via Ollama

load_dotenv()

def generate_quiz(text, num_questions=3):
    prompt = f"""Generate {num_questions} logic-based or comprehension-focused questions from the following document. 
For each question, provide:
1. The question.
2. The ideal answer.
3. A brief justification using the document's content.

Return the output in this format exactly:
Q: <question>
A: <ideal answer>
Justification: <brief reference to where the answer comes from in the document>

Repeat for each question.
Document:
{text[:1000]}
"""

    try:
        response = ollama.chat(
            model='mistral',
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"
