# https://www.hackerrank.com/contests/smart-interviews/challenges/si-triple-trouble
def tripleTrouble(nums):
    ones = twos = 0
    for num in nums:
        twos = twos ^ (ones & num)
        
        ones = ones ^ num
        print("Before updating ones: {0} and twos:{1}".format(ones, twos))
        common_bit_mask = ~(ones & twos)
        
        ones = ones & common_bit_mask
        twos = twos & common_bit_mask
        print("After updating ones: {0} and twos:{1} and CBM: {2}".format(ones, twos, common_bit_mask))

    return ones

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(tripleTrouble(nums))