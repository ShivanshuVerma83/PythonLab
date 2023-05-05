temp=""
for row in range(0,7):
    for column in range(0,7):
        if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column==6):
            temp+='*'
        else:
            temp+=' '
    temp=temp+"\n"
print(temp)



