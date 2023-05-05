def combi(l1,l2,l3):
    for i in l1:
        for j in l2:
            for k in l3:
                print(i,j,k)
    return
l1 = list(map(str,input("Enter list 1:").split()))
l2 = list(map(str,input("Enter list 2:").split()))
l3 = list(map(str,input("Enter list 3:").split()))
combi(l1,l2,l3)