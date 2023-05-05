

nterms=8
a,b = 0, 1
count = 0
if nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(a)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(a,end=" ")
       nth = a+b
       # update values
       a = b
       b = nth
       count += 1
