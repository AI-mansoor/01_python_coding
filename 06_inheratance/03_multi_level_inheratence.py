class country:
    a = "pakistan"

class province(country):
    b = "KPK"

class city(province):
    c = "Charsadda"


m = country
print(m.a)


m = province
print(m.a,m.b)


m = city
print(m.a,m.b,m.c)