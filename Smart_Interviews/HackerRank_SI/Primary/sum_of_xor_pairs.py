
# def sum_of_pairs(nums):
#     max_sum = 0
#     for num in nums:
#         current_sum = 0
#         for num1 in nums:
#             s= num^num1
#             current_sum += s
#         # print(current_sum)
#         max_sum += current_sum
#     return max_sum
def sum_of_pairs(nums):
    max_sum = 0
    for num in nums:
        max_sum ^= 2*num    
        # print(max_sum)
    return max_sum

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    print(sum_of_pairs(nums))