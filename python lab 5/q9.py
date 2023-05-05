s1 ={int(i) for i in input().split(",") if int(i)>=1}
print({bin(i)[2:] for i in s1})
print({hex(i) for i in s1})