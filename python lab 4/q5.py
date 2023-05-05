n = 3
d = dict(input("Enter key and value: ").split() for _ in range(n))
print(d)
dict1 = d
n = 3
e = dict(input("Enter key and value: ").split() for _ in range(n))
print(e)
dict2 = e
print(dict2 | dict1)