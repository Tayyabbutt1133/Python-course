# Write a program to store seven fruits in a list entered by user
import time

start_time = time.time()

fruits_list = []
# fruits_input = input("Enter name of Fruits:")
# fruits_list.append(fruits_input)
# fruits_input = input("Enter name of Fruits:")
# fruits_list.append(fruits_input)
# fruits_input = input("Enter name of Fruits:")
# fruits_list.append(fruits_input)
# fruits_input = input("Enter name of Fruits:")
# fruits_list.append(fruits_input)
# fruits_input = input("Enter name of Fruits:")
# fruits_list.append(fruits_input)
# fruits_input = input("Enter name of Fruits:")
# fruits_list.append(fruits_input)
# fruits_input = input("Enter name of Fruits:")
# fruits_list.append(fruits_input)



# now that is more structured/scalable/optimized way of writing cod 
number = int(input("Number of fruits that you want to enter ?"))
for _ in range(number):
    fruit_name = input("Enter name of fruit:")
    fruits_list.append(fruit_name)
print("fruit list is:",fruits_list)

end_time = time.time()
print(f"Execution Time: {end_time - start_time:.5f} seconds")



# write a program to accept marks of 6 students and sort them out 




