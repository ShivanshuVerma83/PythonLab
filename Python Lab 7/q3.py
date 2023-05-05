
#3.	Write Simple  python program to Perform sum of all numbers input from user Anonymous Function
sum_of_digits = lambda n: sum(int(d) for d in str(n))
k=input('Enter the digits want to be added without space: ')
print(sum_of_digits(k))