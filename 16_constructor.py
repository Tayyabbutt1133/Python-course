# SELF Concept 
class Employee:
    language = "Python"
    salary = "120,0000"
    name = "tbs"
    
    def __init__(self, name, language, salary):   # dunder method in python that automatically runs without calling
        self.name = name
        self.language = language
        self.salary = salary
        
    
    def get_info(self):  # self is just a object name, we can name it anything like data etc
        print("Employee name is : ", self.name)
        print("Employee Salary is : ", self.salary)
        print("Employee language of work is : ", self.language)
        


data = Employee("Tayyeb", "Python & ReactJS", 120000)
print(data.name, data.salary, data.language)