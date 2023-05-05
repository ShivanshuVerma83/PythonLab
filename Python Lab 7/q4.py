fun = lambda x: int(((10*x)/3)**(1/2))
l = list(map(int,input().split(",")))
for i in l: print(fun(i))
