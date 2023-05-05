from collections import Counter


# Python code to convert string to list


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1
    # li = list(string.split(" "))
    # return li
str=input("enter the input string : ")
list1=Convert(str)
counts = Counter(list1)
print(counts)
