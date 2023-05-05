#  write a simple program which.... and students marks. calculate percentage and display grades best on following condition:
# if p>75 and %>75 print grade a+
# if p>70 and %<75 grade a
# p>60 and %<65 rade b no multiple if else
# age = 20
# age_group = "Minor" if age < 18 else "Adult"
# print(age_group)
# studentmarks=list(int("enter the marks : "))
# for i in range(len(studentmarks)):
#     percentage=studentmarks[i]
#     k="A+" if percentage>75  else "B"
#     i+=1
# print(k)

a=input("enter comma separated values:")
b=eval(a)
sum=0
for i in range(len(b)):
    sum+=b[i]
x=(sum/(len(b)*100))*100
print("percentage is: ",x)

if x>75:print("A+")
if 75>x>70:print("A")
if 65<x<70:print("B+")
if 60<x<65:print("B")








