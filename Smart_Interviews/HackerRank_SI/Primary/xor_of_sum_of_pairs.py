# https://www.hackerrank.com/contests/smart-interviews/challenges/si-xor-of-sum-of-pairs
# def xor_sum_pairs(nums):
#     # arrays = []
#     max_sum = 0
#     for num in nums:
#         # helper = []
#         helper = 0
#         for nums1 in nums:
#             currSum = num + nums1
#             helper ^= currSum
#             # helper.append(currSum)
#         max_sum ^= helper
#     # print(arrays)
#     # for arr in arrays:
#     #     current_sum = 0
#     #     for a in arr:
#     #         current_sum ^= a
#     #     max_sum ^= current_sum
#     return max_sum

def xor_sum_pairs(nums):
    xor = 0
    for num in nums:
        xor ^= num
    return xor*2

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    print(xor_sum_pairs(arr))