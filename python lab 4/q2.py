# n = 3
# d = dict(input("Enter key and value: ").split() for _ in range(n))
# print(d)
# my_dict = d
#
# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
#
#
#
# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])
input_list = list(map(str,input("enter the strings with space : ").split()))
dict ={}

for string in input_list:
	if string == string[::-1]:
		dict[string] = string[::-1]
print(dict)