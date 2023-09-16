# https://leetcode.com/problems/single-number-ii/
def singleNumber2(nums):
    res = 0
    for num in nums:
        res = (res ^ num)
    
    return res

arr = list(map(int, input().split()))
print(singleNumber2(arr))