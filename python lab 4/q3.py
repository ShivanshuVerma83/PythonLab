n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    if x%3==0 or x%5==0:
        d[x]=x

print(d)