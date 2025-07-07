'''
Creating a samll application in which we create embeddings of document
and then check the  cosinesimilarity between the query and the created document embeding 
'''
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents=[
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also know as the 'Sachine', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries,",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers"
]

query='Tell me about virat dhoni'

doc_embeddings=embedding.embed_documents(documents)
query_embedding=embedding.embed_query(query)

# Always send 2d list in cosine similarity function 
# that's why first convert query_embeding to 2d list and doc_embeddings is already a 2d list
# The result we get after running cosine_similarity is 2d list 
# But we want 1d list so we add 0 at the end
scores=cosine_similarity([query_embedding],doc_embeddings)[0]


#we are sorting it in ascending order based on the second element and retriveing the highest
# cosine similarity value along with its index
index,score=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("Similarity score is:",score)






