#6.	Write  Simple Python Program to create   calculator for multiple inputs .Take input from user,and  take operational input from user


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def div(x,y):
    return x//y
num1=int(input("enter the first number: "))
num2=int(input("enter the second number: "))
print(num1, "+", num2, "=", add(num1, num2))
print(num1, "-", num2, "=", sub(num1, num2))
print(num1, "*", num2, "=", multiply(num1, num2))
print(num1, "/", num2, "=", div(num1, num2))