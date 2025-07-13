import ollama

response = ollama.chat(model='mistral', messages=[
    {"role": "user", "content": "Summarize this: Chatbots are AI tools that interact with humans using language."}
])

print(response['message']['content'])