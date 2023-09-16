from math import comb

def combinations(n, b):
    factorial = comb(n,b)
    return factorial

def RobotStack(memo,b,n,k, s):
    count = 0

    if (n,k) in memo:
        return memo[n,k]
    if k == 1:
        # print("Entered k = 1 ")
        memo[n,k] = combinations(n,b)
        return memo[n,k]
    elif k == b:
        memo[n,k] = combinations(n+b-1, b)
        return memo[n,k]
    elif b == 0:
        memo[n,k] = 1
        return memo[n,k]
    elif s == n:
        memo[n,k] = 0
        return memo[n,k]
    else:
        for i in range(min(b, k)+1):
            count +=   RobotStack(memo, b-1,n, k-1, s+1) + combinations(n-b+k, b)
        memo[n,k] = count
    return memo[n,k]

with open('/Users/rajjada/Coding/Projects/input.txt') as f:
    for line in f:
        # print(line.strip())
        b,n,k = line.split(' ')
        memo = {}
        # print("",int(b),int(n),int(k),end= '')
        print(RobotStack(memo, int(b),int(n),int(k), 0))