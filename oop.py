# also one more thing which is that there are two types of attributes include : 
# 1. Class Attributes
# 2. Instance Attributes --> not belong to class

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance
        
    
    # Now we can define methods 
    def show_info(self):
        print(f"Account Holder : {self.account_holder}, Balance : {self.__balance}")
    
    def get_balance(self):
        return self.__balance
    

    def set_balance(self, new_balance):
        if new_balance > 0:
            self.__balance = new_balance
        else :
            print("Balance must be positive !")


bk = BankAccount("Tayyeb", 2500000)
print(bk.account_holder)

# so because our attribute is private/not accessible, 
print(bk.get_balance())

# also we can set age to a private attribute using method, can't do directly
bk.set_balance(500000000)
print(bk.get_balance())



    