# 1. for loop 
for i in range(5):  
    print(i)  

# 2. While loop
count = 0
while count < 5:
    print(count)
    count += 1


# Methods in Loops 

# range(start, stop, step)
for i in range(1, 10, 2):  
    print(i)  


# enumerate(iterable, start=0)
# enumerate function is a built-in function that allows you to iterate through a sequence and keep track of the index of each element
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names, start=1):
    print(index, name)
    


# break (Stops the loop)
for num in range(10):
    if num == 5:
        break
    print(num)


# continue (Skips current iteration)
for num in range(5):
    if num == 2:
        continue  # it will skip 2 for print as it will get back to loop before print line execution
    print(num)



# zip() (Looping over multiple iterables)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(name, "Scored", scores)
    
    
# reversed() (Looping in reverse)
for i in reversed(range(5)):
    print(i)


# sorted() (Looping in sorted order)
nums = [3, 1, 4, 2]
for num in sorted(nums):
    print(num)


