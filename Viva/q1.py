#compress

def solve(x,ans):
      if x==l:
        return ans
      ans+=s[x]

      posi= x
      hm =s[x]
      val=0
      while 1:
        if posi>=l or s[posi]!=hm:
            break
        posi+=1
        val+=1
      ans+=str(val)
      x+=val
      ans=solve(x,ans)
      return ans

s=input()
l=len(s)
ans=''
res=solve(0,ans)
print(res)