#Write aPython Program Python Program to Find HCF or GCD
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
l=int("Enter the first num: ")
m=int("Enter the second num: ")
print(gcd(l,m))