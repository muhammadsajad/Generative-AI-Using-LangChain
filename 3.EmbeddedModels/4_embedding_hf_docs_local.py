# Creating embeddings of document using hugging face model on local machine
from langchain_huggingface import HuggingFaceEmbeddings
import os
os.environ['HF_Home']='D:/huggingface_cache'

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

document=[
    "Islamabad is the capital of Pakistan",
    "My name is Muhammad Sajad",
    "I am going to Germany"
]

vector=embedding.embed_documents(document)

print(str(vector))