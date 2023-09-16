# Link: https://www.hackerrank.com/contests/smart-interviews-b33-ic1/challenges/si-consecutive-set-bits

def setBits(n):
    count = 0
    while n>0:
        # print(n>>1)
        # print(n&(n>>1))
        n = n & (n>>1)
        count += 1
    return count


t = int(input())
for i in range(t):
    n = int(input())
    print(setBits(n))