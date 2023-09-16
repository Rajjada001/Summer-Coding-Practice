def findigFreq(nums):
    hm = {}
    for i in range(len(nums)):
        if nums[i] in hm:
            hm[nums[i]] += 1
        else:
            hm[nums[i]] = 1

    return hm

n = int(input())
nums = list(map(int, input().split()))[:n]
Q = int(input())
hm = findigFreq(nums)
for i in range(Q):
    q = int(input())
    try:
        print(hm[q])
    except:
        print(0)


            