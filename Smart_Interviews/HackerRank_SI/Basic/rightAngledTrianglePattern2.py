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
n = int(input())
rightAngledTrianglePattern2(n)