import re

inp = list(input().split(','))
ans = []
reg = "^(?=.*[a-z])|(?=.*[A-Z])|(?=.*[@$#])|[A-Za-z@$#]$"
pat = re.compile(reg)
for i in inp:
    if not re.search(pat, i):
        print(i)
