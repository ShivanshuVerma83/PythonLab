def even(x):
    return x % 2 == 0


a = [2, 5, 7, 8, 10, 13, 16]

result = filter(even, a)
print('Final List :', list(result))