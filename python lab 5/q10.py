questionSet = {("Which options are correct to create an empty set in Python?","()","{}","[]","set()",4),
               ("Which operator has higher precedence in the following list","//","+","%","**",4),
               ("which is best programming lang?","python","cpp","c","java",1),
               ("which library is used in data science?","numpy","tkinter","pil","none",1)}
for i in questionSet:
    print(i[0])
    for j in range(1,5):
        print(j,i[j])
    n = int(input("choose answer"))
    if n == i[-1]:
        print("Correct")
    else:
        print("Wrong")