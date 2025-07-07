# Now creating embedding using the hugging face model on our local machine

from langchain_huggingface import HuggingFaceEmbeddings
import os

# This will download the model in specific location
os.environ['HF_HOME']='D:/huggingface_cache'

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text="Islamabad is the capital of Pakistan"

vector=embedding.embed_query(text)

print(str(vector))