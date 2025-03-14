# Example 1 without walrus
data = input("Enter something: ")
while data != "exit":
    print(f"You entered: {data}")
    data = input("Enter something: ")  # Redundant input call



# Example 1 after implementing walrus
while (data := input("Enter something: ")) != "exit":
    print(f"You entered: {data}")


# Example 2 without walrus
name = input("Enter your name: ")
if len(name) > 5:
    print(f"Your name '{name}' is long!")


if (name := input("Enter your name : ")) and len(name) > 5:
    print(f"Your name {name} is long!")