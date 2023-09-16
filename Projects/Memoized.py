import sys

def get_min(a_val,b_val):
    if a_val<b_val:
        return a_val
    else:
        return b_val

def roboStack(memo, b, n, k, s):
    # Memoized condition
    if (b,s) in memo:
        return memo[b,s]
    # base case
    if(b==0):
        memo[b,s] = 1
        return memo[b,s]
    if(s == n):
        memo[b,s] = 0
        return memo[b,s]
    count = index = 0
    min_value = 0
    for index in range(get_min(b,k)+1):
        count += roboStack(memo, b-index, n, k, s+1) 

    memo[b,s] = count
    
    return memo[b,s] 

with open(sys.argv[1], 'r') as file:
    for line in file:
        b,n,k = line.split(' ')
        memo = {}
        rs = roboStack(memo, int(b),int(n),int(k), 0)
        print("({0},{1},{2}) = {3}".format(b,n,int(k), rs))