def uniqueEl(nums):
    
    for i in range(len(nums)):
        match = 0
        for j in range(len(nums)):
            if nums[i]==nums[j] and i!=j:
                return nums[i]
    return -1

n = int(input())
nums = list(map(int, input().split()))[:n]
print(uniqueEl(nums))