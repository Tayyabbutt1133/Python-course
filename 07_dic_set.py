
# so basically we use dictionary to store data by assigning it to keys which are unique.
# Also, it is o(1) which is constant because it will just straight away get data through unique key so time is not dynamic based on data position/type


# The . popitem() method of a Python dictionary returns the last inserted key-value pair from a dictionary as a tuple and removes the entry.

marks = {
    "Tayyeb": 100,
    "Uzain": 100,
    "Faseeh": 100,
    "Umer": 100
}

print(marks["Tayyeb"])  # Use when you're sure the key exists
print(marks.get("Tayyeb")) #Use when you want to avoid errors

# Methods in dictionary

# 1. Get All Keys
person = {
    "name": "Alice",
    "age": 21,
}
print(person.keys())


# 2. To get all values
print(person.values())
# Output: dict_values(['Alice', 25, 'New York'])


# 3. Get All Key-Value Pairs
print(person.items())
# Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])


# 4. Safe Value Retrieval
print(person.get("name"))  # Output: Alice
print(person.get("gender", "Not Found"))  # Output: Not Found


# 5. Merge Dictionaries or Update Values
person.update({"age": 26, "gender": "Female"})
print(person)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'gender': 'Female'}


# 6.Remove and Return a Value
age = person.pop("age")
print(age)  # Output: 26
print(person)  # Output: {'name': 'Alice', 'city': 'New York', 'gender': 'Female'}

# Remove and Return Last Inserted Key-Value
last_item = person.popitem()
print(last_item)  # Output: ('gender', 'Female')
print(person)  # Output: {'name': 'Alice', 'city': 'New York'}


