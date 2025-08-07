from pydantic import BaseModel, EmailStr
from typing import Optional

class Student(BaseModel):

    name:str='Muhammad Sajad'
    age:Optional[int]=None
    email:EmailStr=None


new_student={'age':'34','email':'abc'}

student=Student(**new_student)

print(student)