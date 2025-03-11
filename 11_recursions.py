def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter the number : "))
print(f'The factorial of number is {factorial(n)}')


# fac(5)
# 5 * fac(5-1)
# 5 * 4 * fac(4-1)
# 5 * 4 * 3 * fac(3-1)
# 5 * 4 * 3 * 2 * fac(2-1)
# 5 * 4 * 3 * 2 * 1 
