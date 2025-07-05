import os
os.environ['OLLAMA_HOST'] = 'http://localhost:11434'

from ollama import chat

# Prompt and messages
prompt = "Give me 2 random facts about India. 1 fact per line"
messages = [{"role": "user", "content": prompt}]

# Query TinyLlama
response = chat(model="tinyllama", messages=messages)

# Output the response
print(response['message']['content'])
