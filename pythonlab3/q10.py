def sort(tup):

    n = len(tup)
    for i in range(0, n):

        for j in range(0, n - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


tup = [('joota', 500), ('chappal', 1000), ('kapde', 2800)]

print(sort(tup))