1.	#Write aPython Program to Display Powers of 2 Using Anonymous Function
# x=lambda a,b:a**b
# k=int(input('Enter the number: '))
# print(x(k,2))

print("Enter Number of Terms: ")
k = int(input())

l = lambda x: 2 ** x
print()
for i in range(k):
    print("2 raised to the power ", i, " is ", l(i))