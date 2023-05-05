dp = [[]]
def printSubsetsRec(arr, i, s, p):
    if (i == 0 and s != 0 and dp[0][s]):
        p.append(arr[i])
        print(*p)
        p = []
        return

    if (i == 0 and s == 0):
        display(p)
        p = []
        return

    if (dp[i - 1][s]):
        b = []
        b.extend(p)
        printSubsetsRec(arr, i - 1, s, b)

    if (s >= arr[i] and dp[i - 1][s - arr[i]]):
        p.append(arr[i])
        printSubsetsRec(arr, i - 1, s - arr[i], p)


def printAllSubsets(arr, n, s):
    if (n == 0 or s < 0):
        return

    global dp
    dp = [[False for i in range(s + 1)] for j in range(n)]

    for i in range(n):
        dp[i][0] = True

    if (arr[0] <= s):
        dp[0][arr[0]] = True

    for i in range(1, n):
        for j in range(0, s + 1):
            if (arr[i] <= j):
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - arr[i]])
            else:
                dp[i][j] = dp[i - 1][j]

    if (dp[n - 1][s] == False):
        print("There are no subsets with s ", s)
        return

    p = []
    printSubsetsRec(arr, n - 1, s, p)


l = [int(i) for i in input().split(",")]
printAllSubsets(l, len(l), 20)
