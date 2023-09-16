from math import comb

def combinations(n, b):
    factorial = comb(n,b)
    return factorial

def roboStack(b, n, k, s):
    count = 0
    for i in range(n):
        for j in range(b):
            for z in range(k):
                continue

    return count

    

b,n,k = 3,4,2
print(roboStack(b,n,k, 0))
# with open('/Users/rajjada/Coding/Projects/input.txt') as f:
#     for line in f:
#         b,n,k = line.split(' ')
#         b = int(b)
#         n = int(n)
#         # memo = [[-1 for _ in range(n+1)] for _ in range(b+1)]
#         # print(memo)
#         start=time.time()
#         rs = roboStack(int(b),int(n),int(k), 0)
#         end=time.time()
#         print(((end-start))*1000000, "milli seconds with value of:", rs)

