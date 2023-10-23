# https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    d = {}
    for i, el in enumerate(nums):
        temp = target -  el
        if temp in d:
            return [d[temp], i]
        else:
            d[el] = i

    return -1


# a = [2,7,11,15]
# target = 9
a = [3,3]
t = 6

print(twoSum(a, t))
