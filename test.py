from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-small",  # ✅ Change to a hosted model
    task="text-generation"
)

response = llm.invoke("What is the capital of Pakistan?")
print(response)
