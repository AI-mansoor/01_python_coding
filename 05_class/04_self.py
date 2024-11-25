class Employee:
    age = 26
    language = "py"
    salary = 12000


    def getinfo(self):
        print(f"The language is {self.language} . The salary is {self.salary}")


    def greet(self):
        print("Good morning")



harry = Employee()
# harry.language = "javascript"

harry.getinfo()
harry.greet()
Employee.getinfo(harry)

