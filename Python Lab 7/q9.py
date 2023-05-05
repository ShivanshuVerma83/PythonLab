#Python Program to Find Factorial of Number Using Recursion
def rec(x):
    if x==1:
        return 1
    else:
        return x*rec(x-1)

num = int(input("Enter a number: "))


result = rec(num)
print("The factorial of", num, "is", result)