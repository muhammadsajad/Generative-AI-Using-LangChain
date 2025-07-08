## TO talk with Claude API which are the models of Anthropic Company
from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model='claude-3-5-sonnet-20241022')

result=model.invoke('What is the capital of Pakistan')

print(result.content)