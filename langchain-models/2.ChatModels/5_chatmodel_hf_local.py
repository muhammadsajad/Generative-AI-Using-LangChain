# Downloading and running a model on local Machine.
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME']='D:/huggingface_cache'

llm=HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temeprature=0.5,
        max_new_tokens=100
    )

)

model=ChatHuggingFace(llm=llm)

result=model.invoke("What is the capital of Pakistan")

print(result.content)