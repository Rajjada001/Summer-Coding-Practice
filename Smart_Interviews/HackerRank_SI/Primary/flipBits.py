def flipBits(A,B):
    x = A^B
    count  = 0
    while x:
        count += x&1
        x= x>>1
    return count

t = int(input())
for _ in range(t):
    A,B = map(int, input().split())
    print(flipBits(A,B))
