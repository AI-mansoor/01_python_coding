marks = {
    "Harry": 100,       # dictionary is unordered, mutable,can't duplicate
    "Mansoor":80,
    "Hassan": 70,
    0: "Harry"
}
print(id(marks))

print(marks, type( marks))
# print(marks["Harry"])  
print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry": 97}) 
print(id(marks))

print(marks.get("Harry"))