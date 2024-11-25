class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class coder :
    language = "python"
    def printlanguages(self):
        print(f"out of all languages here is your language: {self.language}")
              


class programer (Employee,coder):         # employee is inherited in class servant
    company = "ICMS degree college"
    def showlanguage(self):
        print(f"The name is {self.company}and he is good with {self.language} language")



a = Employee () 
b = programer ()   
c = coder()    
print(a.company,b.language,c.language)
b.showlanguage()
c.printlanguages()
