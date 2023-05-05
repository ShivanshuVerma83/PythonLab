record = []
def inp():
    a,b,c,d = input("enter name,id,mis and email:").split()
    s1,s2,s3 = input("Enter resut:").split()
    record.append({"Name":a,"id":b,"mis":c,"eamil":d,"result":{"s1":int(s1),"s2":int(s2),"s3":int(s3)}})

def update(x):
    for i in range(len(record)):
        if record[i]["name"]==x:
            a,b,c,d = input("enter new record:").split()
            s1,s2,s3 = input("Enter resut:").split()
            record[i]= {"Name":a,"id":b,"mis":c,"eamil":d,"result":{"s1":int(s1),"s2":int(s2),"s3":int(s3)}}
f=1
while(f):
    print("1 for insert,2 for  update,3 for view,4 to end:")
    n = int(input())
    if n==1:
        inp()
    elif n==2:
        a = input("name:")
        update(a)
    elif n==3:
        print(record)
    else:
        f=0