#
import re

def f(text):
    patterns = '[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return 'Yes!'
    else:
        return ('Not matched')



def ff(text):
    patterns = '[z]+[o]'
    if re.search(patterns, text):
        return 'Yes!'
    else:
        return ('Not matched')









string = input("Enter the paragraph: ")

regex = re.compile(r"\d\(\d\+\)\d")
result = regex.findall(string)
print("Total no. of matches:", len(result))
print(f(string))
print(ff(string))



# print(result)