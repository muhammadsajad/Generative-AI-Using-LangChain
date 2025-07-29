# How to create a dictonry using Typedict
# this is like a definition of our dictonary so if two programers worked on same project so that they do not enter diffrent data type for keys in dictonary

from typing import TypedDict

# Define your own class and inherit from TypeDict
class Person(TypedDict):

    name:str
    age:int

# Create a dictonary name 'new_person'. it automatically sugest the key and also its type
# Note: it only give suggestions for type of data for key but not provide any kind of validation
new_person:Person={'name':'Sajad','age':32}

print(new_person)