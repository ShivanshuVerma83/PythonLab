import re
inp = list(input().split(','))
ans = []
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,12}$"
pat = re.compile(reg)
for i in inp:
    if re.search(pat,i):
        print(i)