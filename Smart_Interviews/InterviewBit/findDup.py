# def findDup(nums):
#     x=y=0
#     for num in nums:
#         x = x^num
#     for i in range(len(nums)):
#         y ^= i
#     return y^x


def migratoryBirds(arr):
    # Write your code here
    freq = {}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    highestKey = highestVal = 0
    for key in freq:
        if freq[key]>highestVal:
            highestVal = freq[key]
            highestKey = key
    return highestKey
    # max_v = max(freq.values())
    # mul = []
    # res = [k for k, v in freq.items() if v==max_v]
    
    # return min(res)

nums = list(map(int, input().split()))
print(migratoryBirds(nums))
