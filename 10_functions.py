import math


# There are two type of functions 
# 1.Built-int functions
# 2.User defined functions
def avg():
    one = int(input("Enter Number one : "))
    two = int(input("Enter Number one : "))
    three = int(input("Enter Number one : "))
    avg = (one + two + three)/3
    dec_avg = math.trunc(avg) # conversion of floating into decimal
    print(dec_avg)
    

# Triggering/running function
avg()


# types of functions
# 1. functions without arguments 
# 2. functions with arguments
