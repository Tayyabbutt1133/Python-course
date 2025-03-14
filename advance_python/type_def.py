# advance type hints
from typing import List, Dict, Set

numbers: List[int] = [1, 2, 3, 4, 5, 6]
set_data : Set(str, int) = ("Tayyeb", 21)
set_dict : Dict(str, int) = {"Name" : "Tayyeb", "Age" : 21}




# so it is somehow similar to interface in typescript, only difference is that we don't make interface of data 
# remember, unlike typescript Python implementing types does not enforce to check types at compile time and give errors if data type doesn't match the expected type




# a : int = 2
# my_name : str = "Tayyeb"


# for functions
def printing_data( a: int , b: int) -> int:
    c = a + b
    return c
     
     
a : int = 1
b : int = 7
result = printing_data(a, b)
print(result)