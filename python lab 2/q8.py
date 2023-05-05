
# word=input("enter the word: ")
# l=0
# h=len(word)
# while(l<=h):

def reverse(string):
    string = list(string)
    string.reverse()
    return "".join(string)


s=input('Enter the word: ')

print("reversed string is : ", reverse(s))
