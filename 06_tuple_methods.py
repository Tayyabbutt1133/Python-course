# the main difference between tuple and lists is that tuple are immutable while lists are mutable, also tuple are more memory effecient

a = (1, 2, 3, 4)
print(a)

# methods 

tups = (1, 1, 12, 2, 3, 5)
count = tups.count(1) # it will give you a count of your required expected data in tuple
print(count)

# Returns the index of the first occurrence of the specified value
my_tuple = (1, 2, 3, 2, 2, 4)
print(my_tuple.index(3))  # Output: 2


# tuple unpacking--tuple allows you to assign it values to multiple variables for use
tupetest = (1,2,3)
d, e, f = tupetest
print("Value of d :",d)



# Extended tuple unpacking
my_tuple_extended = (1, 2, 3, 4, 5)
first, *middle, last = my_tuple_extended
print(first)   # Output: 1
print(middle)  # Output: [2, 3, 4]
print(last)    # Output: 5


# Slicing, Concatenation, and Multiplication:
tup1 = (1, 2, 3)
tup2 = (4, 5)
combined = tup1 + tup2  # Concatenation: (1, 2, 3, 4, 5)
repeated = tup1 * 2     # Multiplication: (1, 2, 3, 1, 2, 3)
slice_tup = tup1[1:]    # Slicing: (2, 3)


# finding index from tuple 
tupcheck = (1, 43, 23, 54)
index = tupcheck.index(43)
print("Index:",index)


# membership- check boolean condition in tuple to return if asked stuff is true or false, so that based on that we can do conditioning
tupbook = (2, 3, 12, 11)
print(2 in tupbook)



# checking length 
tupstups = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(tupstups))


# tuple() Constructor
list = [1, 2, 3, 4, 5, 6]
print(list)
tuple_conversion = tuple(list)
print(tuple_conversion)

# Nested Tuples – Tuples can contain other tuples.
tupling = ((1,2,3), (4,5,6),(7,8,9))
print(tupling[0])



# slicing : tuple supports slicing to create a new tuple from the subset of original
tuple_slice = (1, 3, 4, 5, 6)
sliced = tuple_slice[1:4]
print(sliced)



