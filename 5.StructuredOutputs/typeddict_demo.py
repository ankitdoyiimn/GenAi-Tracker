from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    "name": "John Doe",
    "age": 30
}

#noe changing the age of the person to string datatype
new_person['age'] = "thirty"  # This will not raise an error at runtime, but it will violate the type hinting of the TypedDict

print(new_person)