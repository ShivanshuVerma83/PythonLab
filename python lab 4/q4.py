# dict1 = {'a': 12, 'for': 25, 'c': 9}
n = 3
d = dict(input("Enter key and value: ").split() for _ in range(n))
print(d)
dict1 = d
n = 3
e = dict(input("Enter key and value: ").split() for _ in range(n))
print(e)
dict2 = e


# dict2 = {'k': 100, 'l': 400, 'for': 100}
for key in dict2:
    if key in dict1:
        dict2[key] = int(dict2[key]) + int(dict1[key])
    else:
        pass

print(dict2 | dict1)
