x=set()
num = int(input("enter the no. between 10 to 50: "))

for j in range(1,num):
    if (num % j == 0):
        x.add(j)
print(x)
