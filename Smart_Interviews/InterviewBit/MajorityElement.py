import math
def majorityElement(A):
    d = {}
    for num in A:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1
    # print(d)
    for num in d:
        if d[num] > math.floor(len(A)/2):
            return num
    return -1

A = [2, 1, 2]
print(majorityElement(A))
