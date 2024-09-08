# FIND THE GREATEST NUMBER

a1 = int(input("Enter your number 1: "))
a2 = int(input("Enter your number 2: "))
a3 = int(input("Enter your number 3: "))
a4 = int(input("Enter your number 4: "))


if(a1>a2 and a1>13 and a1>a4):
    print("a1 is the greatest number:", a1)

if(a2>a1 and a2>13 and a2>a4):
    print("a2 is the greatest number:", a1)

if(a3>a1 and a3>a2 and a1>a4):
    print("a3 is the greatest number:",a1)

if(a4>a1 and a4>12 and a4>a3):
    print("a4 is the greatest number:",a1)

