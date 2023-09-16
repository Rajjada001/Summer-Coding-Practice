def rightAngledTriangle(n):
    for i in range(n):
        for j in range(i, n-1):
            print(" ", end="")
        for j in range(i+1):
            print("*", end="")
        print()

def rightAngledTrianglePattern2(n):
    num = 0
    for i in range(0,n):
        # print(i, end = " ")
        num = i + 1
        dec = n - 1
        for j in range(i+1):
            print(num, end=" ")
            num = num+dec
            dec = dec - 1
        print()

# t = int(input())
# for i in range(t):
#     n = int(input())
#     print("Case #{0}:".format(i+1))
#     rightAngledTriangle(n)
n = int(input())
rightAngledTrianglePattern2(n)