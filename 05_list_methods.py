# Different Methods that we can implement on list 
# 1. sort()
# 2. reverse()
# 3. append()
# 4. insert()
# 5. pop()
# 6. remove()



friends = ["khan", "tayyeb", "shahzad", "ubm", "ali", 12]

print(friends)

friends.append("new addition")

print(friends)


test = [12,1, 5, 2, 4, 3]
test.sort()
print(test)


l1 = [1, 2, 3, 4, 5, 7, 14, 90, 100]
value = l1.pop(1)
print("Pop out value is", value)
print(l1)
