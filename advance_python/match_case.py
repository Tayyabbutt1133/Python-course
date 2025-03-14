def check_number(n):
    match n:
        case 1:
            print("One")
        case 2:
            print("Two")
        case 3:
            print("Three")
        case _:
            print("Unknown number")

check_number(2)  # Output: Two
check_number(5)  # Output: Unknown number
