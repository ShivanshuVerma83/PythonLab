class magic:
    def __init__(self,n):
        self.n = n

    def __sub__(self,copy):
        s1 = 0
        for i in copy:
            s1 += int(i)
        s2 = 1
        for i in self.n:
            s2 *= int(i)
        return s2-s1
n = input()
ob = magic(n)
print(ob-n)
