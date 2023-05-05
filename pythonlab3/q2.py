#convert into hexadecimal and binary format
values = input("enter the  some comma seprated numbers : ")
list1 = values.split(",")

def get_number(values):
    total = 0
    for val in reversed(values):
        total = (total << 8) + val
    return total


print(get_number(list1))

