#2.	Write Simple  python program to filter  all  positive numbers from user input  list

lst1 = []
lst1 = [int(item) for item in input("Enter the list items : ").split()]
print(lst1)
def myfunc(x):
    if x<0:
        return False
    else:
        return True
nlst1 = filter(myfunc,lst1)

for a in nlst1:
    print(a,end=" ")
