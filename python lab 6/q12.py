from datetime import date

mon = int(input("Enter birth month in number: "))
dat = int(input("Enter birth date in number: "))
curr = list(map(int, input("Enter curr date (yyyy mm dd)").split()))
x = (date(curr[0], mon, dat) - date(curr[0], 1, 1)).days
y = (date(curr[0], curr[1], curr[2]) - date(curr[0], 1, 1)).days
if y <= x:
    print(x - y)
else:
    print(365 - y + x)