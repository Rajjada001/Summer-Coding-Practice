def alternatingSubArr(nums):
    max_length = 0
    n = len(nums)
    for i in range(n - 1):
        current_length = 1

        while i < n - 1 and (nums[i] - nums[i + 1]) * (-1) ** i == 1:
            current_length += 1
            i += 1
        if current_length > max_length:
            max_length = current_length

    if max_length <= 1:
        return -1

    return max_length 

nums = list(map(int, input().split()))
print(alternatingSubArr(nums))