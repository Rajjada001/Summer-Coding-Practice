def uniqueEl(nums):
    
    for i in range(len(nums)):
        match = False
        for j in range(len(nums)):
            if nums[i]==nums[j] and i!=j:
                match = True
        if not match:
            print(nums[i], end=" ")

n = int(input())
nums = list(map(int, input().split()))[:n]
uniqueEl(nums)