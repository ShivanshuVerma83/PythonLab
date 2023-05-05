alphabet,string=0,"shivanshu1234"
for i in string:
    if (i.isalpha()):
        alphabet+=1
print("Number of Digit is", len(string)-alphabet)
print("Number of Alphabets is", alphabet)