# link:https://www.hackerrank.com/contests/smart-interviews-b33-ic1/challenges/si-z-pattern

def even_split(n):
    if n<=2:
        return False
    if n%2==0:
        return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    # print("Case #{0}:".format(i+1))
    es = even_split(n)
    if es == True:
        print("Yes")
    else:
        print("No")