import re

email = "john@google.com"
pattern = "^(\S+)(?=@)"

ans = re.findall(pattern,email)
print(ans)
emaill=input("Enter the email: ")
ans1 = re.findall(pattern,emaill)

print(ans1)

