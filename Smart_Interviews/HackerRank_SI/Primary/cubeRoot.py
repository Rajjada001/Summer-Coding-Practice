def cubeRoot(n):
    l = -abs(n) if n<0 else 0
    r = abs(n)
    print(l,r)
    temp = 0.000001
    # print(l,r)
    ans = -999999999999
    while l<=r:
        mid = (l+r)//2
        cube = mid*mid*mid
        if abs(cube-n)<temp:
            ans = mid
            return ans
        if cube < n:
            l = mid+1
        else:
            r = mid-1
    return ans

import math       
t = int(input())
for _ in range(t):
    n = int(input())
    print(int(cubeRoot(n)))