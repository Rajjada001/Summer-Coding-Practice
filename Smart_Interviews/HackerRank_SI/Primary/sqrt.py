def sqrt(A):
    l,r = 0,A
    ans = -1
    while l<=r:
        mid = (l+r)>>1
        # print(mid*mid)
        if mid*mid <= A:
            ans = mid
            l = mid+1 
        # elif mid*mid < A:
        #     l = mid+1
        else:
            r = mid-1
    return ans


print(sqrt(9))