# names = []
# phone_numbers = []
# num = 10
#
#
# for i in range(num):
#     name = input("Name: ")
#     phone_number = input("Phone Number: ")
#
#     names.append(name)
#     phone_numbers.append(phone_number)
#
# print("\nName\t\t\tPhone Number\n")
# search_term = input("\nEnter search term: ")
#
# print("Search result:")
#
# if search_term in names:
#     index = names.index(search_term)
#     phone_number = phone_numbers[index]
#     print("Name: {}, Phone Number: {}".format(search_term, phone_number))
#
# else:
#     print("Name Not Found")
record = {}


def add(a, b):
    record[a] = int(b)
    print("contact added!")


def delete(a):
    if a not in record:
        print("Record doesn't  exises!")
    else:
        del record[a]
        print("Deleted succesfully,updated record", record)


def search(a):
    if a not in record:
        print("Record doesn't  exists!")
    else:
        print("Details of ", a, ":", record[a])


def display():
    print("Current record book:")
    print(record)


f = 1
while (f):

    print("Choose:")
    print("0 to quit:")
    print("1 to add contact:")
    print("2 to delete contact:")
    print("3 to search:")
    print("4 to display all records:")
    f = int(input())
    if f == 1:
        a, b = map(str, input("Enter details (name,contact):").split(","))
        add(a, b)
    elif f == 2:
        a = input("Enter name of person whose record you want to delete:")
        delete(a)
    elif f == 3:
        a = input("Enter name of person whose record you want to search:")
        search(a)
    elif f == 4:
        display()