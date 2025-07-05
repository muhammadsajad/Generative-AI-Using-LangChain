from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv
import os

load_dotenv()  # Make sure HF_TOKEN is loaded from .env

model = ChatHuggingFace.from_model_id(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="conversational",
    model_kwargs={"max_new_tokens": 100, "temperature": 0.7}
)

result = model.invoke("What is the capital of Pakistan?")
print(result.content)
