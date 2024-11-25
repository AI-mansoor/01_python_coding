class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class servant (Employee):         # employee is inherited in class servant
    company = "ICMS degree college"

a = Employee () 
b = servant ()       
print(a.company,b.company)