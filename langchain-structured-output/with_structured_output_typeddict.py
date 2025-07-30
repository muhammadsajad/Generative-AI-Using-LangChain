from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict 


load_dotenv()

model=ChatOpenAI()

# schema
class Review(TypedDict):

    summary: str 
    sentiment: str

structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""I bought this product hoping for quality, but it turned out to be a total letdown. It stopped working properly within a week, the build feels cheap, and the customer service was completely unhelpful. I regret this purchase and would not recommend it to anyone. Save your money and look elsewhere.

""")

print(result)
print(type(result))
print(result['summary'])
print(result['sentiment'])
