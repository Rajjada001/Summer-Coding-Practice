def top_k_elements(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    # print(freq)
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)
    # print(freq)
    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            print(res)
            if len(res) == k:
                return res

nums = list(map(int, input().split()))
k = int(input())
print(top_k_elements(nums, k))