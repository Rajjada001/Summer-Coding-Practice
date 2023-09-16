
# Problem link: https://www.hackerrank.com/contests/smart-interviews-b33-ic1/challenges/si-z-pattern

def pattern(n):
    for i in range(n):
        for j in range(n):
            if (i==0):
                print("*", end="")
            elif(i+j == n-1):
                print("*", end="")
            elif(i==n-1):
                print("*", end="")
            else:
                print(" ", end="")
        print()
t = int(input())
for i in range(t):
    n = int(input())
    print("Case #{0}:".format(i+1))
    pattern(n)
    