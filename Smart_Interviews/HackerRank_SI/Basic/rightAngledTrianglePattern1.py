def rightAngledTrianglePattern1(n):
    num=0
    for i in range(n+1):
        for j in range(i):
            num= num+1
            print(num,end=" ")
        print()

n = int(input())
rightAngledTrianglePattern1(n)