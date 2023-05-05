d1 = dict()
d2 = dict()
d3 = dict()
for i in range(3):
    name = input("enter the name :")
    salary = int(input("enter the salary:"))
    design = input("enter the designation:")
    if (design == "technical officer"):
        d = dict()
        d["salary"] = salary
        d["designation"] = design
        d1[name] = d

    if (design == "manager"):
        d = dict()
        d["salary"] = salary
        d["designation"] = design
        d2[name] = d
    if (design == "software associate"):
        d = dict()
        d["salary"] = salary
        d["designation"] = design
        d3[name] = d
print(d1)
print(d2)
print(d3)