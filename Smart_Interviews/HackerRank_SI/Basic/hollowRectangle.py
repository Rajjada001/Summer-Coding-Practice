def printHollowRect(b,l):
    for i in range(l):
        for j in range(b):
            if i==0 or j==0 or i==l-1 or j==b-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

l,b = map(int, input().split())
print(printHollowRect(l,b))