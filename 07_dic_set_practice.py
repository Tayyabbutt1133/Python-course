# Practice Problems

# Write a program to make dictionary of urdu words with values as their english translation, provide user with the option to look it up as well.
# dic_words = {
#     "madad" : "Help",
#     "Lehaz" : "Patience",
#     "Adab" : "Ethics"
# }
# user_input = input("Enter Urdu word to find it's translation : ")
# translated_word = dic_words[user_input]
# print("Translated word is :", translated_word)


# # Write a program to input eight numbers from the users and display all the unique numbers once
# num_set = set()

# n = input("Enter number one : ")
# num_set.add(int(n))
# n = input("Enter number two : ")
# num_set.add(int(n))
# n = input("Enter number three : ")
# num_set.add(int(n))
# n = input("Enter number four : ")
# num_set.add(int(n))
# n = input("Enter number five : ")
# num_set.add(int(n))

# print(num_set)


# Write a program to take input from user in list and then remove duplications using sets

num_list = []

i = int(input("Enter number of times you want to enter : "))

for x in range(i):
    user_num = int(input("Enter number : "))
    num_list.append(user_num)
print("Updated List :", num_list)


# so basically there are three ways to remove duplication from list
# ONE--using set
unique_number = sorted(set(num_list))
print("After removing duplication : ", unique_number)


# TWO--using Preserves Order
sorted_unique = sorted(dict.fromkeys(num_list))  # Keeps first occurrence
print(sorted_unique)  # Output: [1, 2, 4, 5, 7]




# THREE--Using loop
for num in num_list:
    if num not in num_list:  # Add only if not already in list
        num_list.append(num)
sorted_unique = sorted(num_list)  # Sort after filtering
print(sorted_unique)  # Output: [1, 2, 4, 5, 7]






