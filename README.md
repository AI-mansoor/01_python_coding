# 01_python_coding

1. What is Python? 🐍

Python is a high-level programming language.

It is easy to read, write, and understand because it uses simple English-like syntax.

It is used for many fields:

Web development 🌐

Data science 📊

Artificial intelligence 🤖

Automation ⚙️

Game development 🎮

Think of Python like a universal tool — just like a Swiss Army knife, you can use it for many different jobs.

2. Core Concepts of Python 🧩

Here are the building blocks you need to understand first:

Variables → Used to store data.

name = "Mansoor"
age = 18


Data Types → Different kinds of values.

int (numbers) → 5

float (decimal) → 3.14

str (text) → "Hello"

bool (true/false) → True, False

list, tuple, dict (collections of data)

Operators → Perform actions.

+ add, - subtract, * multiply, / divide

Control Flow → Decision making.

if age > 18:
    print("You are adult")
else:
    print("You are not adult")


Loops → Repeat tasks.

for i in range(5):
    print(i)


Functions → Reusable blocks of code.

def greet(name):
    return "Hello " + name
print(greet("Mansoor"))


Classes & Objects (OOP) → Blueprints for creating things.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

mycar = Car("Toyota", "Corolla")
print(mycar.brand)


Modules & Libraries → Pre-written code you can import and use.

import math
print(math.sqrt(16))


✅ So Python is all about:
Variables + Data + Logic + Reuse + Libraries = Powerful Programs
 




🟢 Definition of OOP

Object-Oriented Programming (OOP) is a way of writing programs using objects instead of just functions and logic.

An object is something that has data (attributes/variables) and behavior (methods/functions).

A class is like a blueprint to create objects.

👉 Example in real life:

Class = "Car" (blueprint)

Objects = Toyota Corolla, Honda Civic (actual cars made from the blueprint)

🟢 Four Main Pillars of OOP

Encapsulation → Binding data and methods together, and hiding the details.

Inheritance → One class can get properties/methods of another class.

Polymorphism → Same method name but different behavior in different classes.

Abstraction → Hiding unnecessary details, showing only the important features.

🟢 Very Simple Example in Python
# Class definition
class Car:
    def __init__(self, brand, model):   # Constructor
        self.brand = brand
        self.model = model

    def drive(self):   # Method
        print(f"{self.brand} {self.model} is driving...")

# Creating Objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Using Objects
car1.drive()
car2.drive()

Output:
Toyota Corolla is driving...
Honda Civic is driving...
