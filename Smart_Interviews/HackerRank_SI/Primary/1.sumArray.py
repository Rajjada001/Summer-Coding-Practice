def arrSum(arr):
    aSum = 0
    for num in arr:
        aSum += num
    return aSum
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    print(arrSum(arr))