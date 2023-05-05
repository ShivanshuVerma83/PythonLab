#sum and average
# 0 1 1 2


# Python program to find the sum
# and average of the list

L = [1,2,3,4,5]


sum = 0

for i in L:
    sum += i


avg = sum / len(L)

print("sum = ", sum)
print("average = ", avg)