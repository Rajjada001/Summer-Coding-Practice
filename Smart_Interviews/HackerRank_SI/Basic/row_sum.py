(r,c) = map(int, input().split())
m1 = [[int(x) for x in input().split()] for _ in range(r)]
m2 = [[int(x) for x in input().split()] for _ in range(r)]
# row sum
# for i in range(r):
#     res = sum(arr[i])
#     print(res)
# col sum
# for col in range(c):
#     res = 0
#     for row in range(r):
#         res += arr[row][col]
#     print(res)
# matrix sum
mSum = 0
for row in range(r):
    for col in range(c):
        print(m1[row][col] + m2[row][col], end = " ")
    print()
