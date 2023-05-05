def square(a,b):
    list=[]
    for i in range(a,b+1):
        list.append(i*i)
    return list
print(square(1,20))
print("The first 5 elements are: ")
print(square(1,5))