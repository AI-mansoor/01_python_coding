class Employee:
    age = 26
    language = "py"        #    This is a class attributes
    salary = 12000

    def __init__(self,age,language,salary):     #  parameters             # constructor is also called  Dander function 
        self.age = age 
        self.language = language                 # when we write a function in classs then it is called a "Method"                  
        self.salary = salary
        print("i anm creating an oject")

    def getinfo(self):
        print(f"The language is {self.language} . The salary is {self.salary}")     #  Methods


    def greet(self):
        print("Good morning")                       #   Methods


harry = Employee("23","python","320000")   #    Arguments
harry.name="harry"                               #    Instance attributes
print(harry.name,harry.age,harry.language,harry.salary)
# harry.language = "javascript"

# harry.getinfo()
# harry.greet()
# Employee.getinfo(harry)

