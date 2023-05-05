#valid password
# 1 small char 1 number and len max 12


l,d = 0,0
k = input("enter the password: ")
s = k.split(",")
if (len(s) >= 6):
    for i in s:


        if (i.islower()):
            l += 1


        if (i.isdigit()):
            d += 1
if (l >= 1 and d >= 1 ):
    print("Valid Password")
else:
    print("Invalid Password")