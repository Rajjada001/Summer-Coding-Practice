import time

def roboStack(memo, b, n, k, s):
    
    # base case
    if(b==0):
        return 1
    if(s == n):
        return 0
    count = 0
    for i in range(min(b, k)+1):
        # print("i=", i)
        count += roboStack(memo, b-i, n, k, s+1) 
    # print(memo)
    
    return count

with open('/Users/rajjada/Coding/Projects/input.txt') as f:
    for line in f:
        b,n,k = line.split(' ')
        memo = {}
        start=time.time()
        rs = roboStack(memo, int(b),int(n),int(k), 0)
        end=time.time()
        print(((end-start))*1000000, "milli seconds with value of:", rs)
