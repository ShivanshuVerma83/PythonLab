n = 1
d = dict(input("Enter name and value: ").split() for _ in range(n))
print(d)
dict1 = d
n = 1
e = dict(input("Enter mis no. and value: ").split() for _ in range(n))
print(e)
dict2 = e
n = 1
d = dict(input("Enter email and value: ").split() for _ in range(n))
print(d)
dict3 = d
people = {1: dict1,
          2: dict2,
          3: dict3}
print(people)
