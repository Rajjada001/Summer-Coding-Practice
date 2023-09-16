
def missingNumber(nums):
    xor2 = 0
    xor1 = 0
    for i in range(len(nums)):
        xor1 ^= nums[i]
        xor2 ^= i
    # print(xor1, xor2, xor1^xor2)
    return xor1^xor2

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    print(missingNumber(arr))