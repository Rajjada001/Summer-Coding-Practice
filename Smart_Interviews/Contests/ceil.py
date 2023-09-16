def sqrt(n):
    l,r = 1,n
    while l<=r:
        mid = (l+r)//2
        if mid*mid == n:
            return mid
        elif mid*mid < n:
            l = mid+1
        else:
            r = mid-1
    return r

def ceil_and_floor(left, right, target):
    l,r = 0,target
    res = [0,0]  #floor and ceil
    while l<r:
        mid = (l+r)//2
        if mid == target:
            res[0] = mid
            res[1] = mid
            break
        elif mid < target:
            res[0] = mid
            l = mid+1
        else:
            res[1] = mid
            r = mid-1
        
    return res


def countPerSq(A, B):
    sqrt_A = sqrt(A)
    sqrt_B = sqrt(B)
    print(sqrt_A, sqrt_B)
    # ceil = -(-sqrt_B//sqrt_A)
    # floor = (sqrt_B//sqrt_A)
    if sqrt_A == sqrt_B:
        return 0
    floor, dummy = ceil_and_floor(A, B, sqrt_B)
    dummy, ceil = ceil_and_floor(A, B, sqrt_A)

    # floor = 
    # print(floor, ceil)
    return floor-ceil+1

n = int(input())
for _ in range(n):
    A,B = map(int, input().split())
    print(countPerSq(A,B))