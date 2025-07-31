# Generate sturcture output from llm using TypeDict
# we annotation to elaborate more to llms to generate type of output and guiding it
# Note: Its not gurranted that using this method llm will output our desired mention result according to our given instructions. Wiout being explicitly defined the data format of output their is till posibilty that it output difrent data format. So there is no data validation in this typedictonary method. this method is only for representation. If you want data validation their are others method like pydantic.
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated,Optional,Literal


load_dotenv()

model=ChatOpenAI()

# schema
class Review(TypedDict):

    key_themes=Annotated[list[str],"write down all the key themes discussed in the review in a list"]
    summary:Annotated[str,"A brief summary of the review"] 
    sentiment: Annotated[Literal["pos","neg","neu"]," Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]],"Write down all the pros inside the list"]
    cons:Annotated[Optional[list[str]], "Write down all the cons inside the list"]
    name:Annotated[Optional[str],"Write the name of the reviewer"]


structured_model=model.with_structured_output(Review)

result=structured_model.invoke("""After using the Samsung Galaxy S24 Ultra for a few weeks, I have mixed feelings. On one hand, it’s undeniably one of the most powerful smartphones on the market right now. The Snapdragon 8 Gen 3 processor handles everything I throw at it—whether it's gaming, heavy multitasking, or editing high-res photos—with impressive speed and responsiveness. The 5000mAh battery easily lasts a full day of use, and the 45W fast charging is genuinely convenient.

The display is gorgeous, and the S-Pen integration is a nice touch, especially for people who like to take notes or sketch. The 200MP camera is a standout feature, offering incredible zoom capabilities and stunning clarity, even in low-light conditions. Being able to zoom up to 100x is cool in theory, though practically speaking, image quality drops significantly beyond 30x.

That said, the phone has its drawbacks. It's bulky and quite heavy, which makes one-handed use difficult and uncomfortable. Samsung’s One UI still comes bloated with unnecessary pre-installed apps, many of which duplicate the functions already offered by Google. The price is another issue—at around $1,300, it’s not exactly a budget-friendly option, and I expected a more refined software experience at that cost.

Pros:
Extremely powerful processor – perfect for gaming, productivity, and multitasking

Stunning 200MP camera with impressive zoom and night mode performance

Long-lasting 5000mAh battery with fast charging

S-Pen support adds extra functionality for creative and professional users

Gorgeous display with vibrant colors and smooth refresh rate

Cons:
Bulky and heavy  not ideal for one-handed use

Still plagued by unnecessary bloatware in One UI

Very expensive compared to similar flagship options

Zoom quality drops significantly beyond 30x

Review by Muhammad Sajad
""")

print(result)

