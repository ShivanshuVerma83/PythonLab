
input = [[5, 6], [4, 7, 10,17]]

print("The original list is : " + str(input))
ans = [(ele, " ") for sub in input for ele in sub]
print("The converted container : " + str(ans))

