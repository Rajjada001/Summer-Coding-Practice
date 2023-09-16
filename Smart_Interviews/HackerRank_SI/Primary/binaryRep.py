def binrep(n):
    res = []
    while n>0:
        rem = n%2
        res.append(rem)
        n = n//2
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    res = binrep(n)
    for i in range(len(res)-1, -1, -1):
        print(res[i], end="")
