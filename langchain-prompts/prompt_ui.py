from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

model=ChatOpenAI()

st.header('Research Tool')

user_input=st.text_input('Enter Your Prompt')

if st.button('Summarize'):
    result=model.invoke(user_input)
    st.write(result.content)