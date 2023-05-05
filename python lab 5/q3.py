a = [12 ,24 ,35 ,24 ,88 ,120 ,155 ,88 ,120 ,115]
a=list(set([x for x in a if a.count(x)%2 == 1]))
print(a)