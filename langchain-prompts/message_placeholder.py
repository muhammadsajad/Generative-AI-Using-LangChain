# This is used to load the previous chat so that llm remeber the prevoius conversation.
# Professionaly this is stored in database but here just for understanding we saved it in txt file and load it
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history=[]
# load chat history
# Professionaly this chat histroy is stored in database but here just for example we saved it in txt file
with open('langchain-prompts\chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt=chat_template.invoke({'chat_history':chat_history,'query':'Where is my refund'})


print(prompt)