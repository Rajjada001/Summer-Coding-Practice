def collecting_water(nums, n):
    # Not so optimal
    # ans = 0
    # L = [0 for i in range(n)]
    # R = [0 for i in range(n)]
    # L[0],R[n-1] = nums[0],nums[n-1]
    # # def maximum(nums, start, end):
    # #     return max(nums[start], nums[end])
    # for i in range(n):
    #     # lmax
    #     for j in range(1,n):
    #         L[j] = max(L[j-1], nums[j])
    #     # rmax
    #     for j in range(n-2, -1, -1):
    #         R[j] = max(R[j+1], nums[j])

    #     print(ans, L[i],R[i])
    #     ans = ans + min(L[i],R[i]) - nums[i]
        
    # return ans
    if n <= 2:
        return 0
    ans = 0
    l,r = 0,n-1
    lmax,rmax = nums[0],nums[-1]

    while l<=r:
        if nums[l] > lmax:
            lmax = nums[l]
        if nums[r] > rmax:
            rmax = nums[r]
        
        if lmax <= rmax:
            ans += lmax - nums[l]
            l += 1
        else:
            ans += rmax - nums[r]
            r -= 1
    
    return ans

res = []
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    print(collecting_water(nums, n))