class Employee:
    a = 23
    @classmethod   # class method call class attribute nor the instance attribute
    def show(self):        # this is a function and in class now this is calle Method
        print(f"the class attributw of a is {self.a}")

e = Employee ()
e.a = 45

e.show()   #  out put = 23   because of class method