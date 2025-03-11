

# Write a program to find the greatest of three numbers using functions
def greatest_num():
    numbers_arr = []
    highest_num = set()
    user_enter = int(input("Enter number of times you want to enter : "))
    for x in range(user_enter):
        value_enter = int(input("Enter Number : "))
        numbers_arr.append(value_enter)
    numbers_arr.sort()
    # sorting using sets
    highest_num = max(numbers_arr)
    print("Array that we have is : ", numbers_arr)
    print("Highest number is : ", highest_num)

# calling function
greatest_num()
    
    