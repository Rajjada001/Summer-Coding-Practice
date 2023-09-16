# cook your dish here

def goodTurn(X, Y):
    s = X+Y
    if s>6:
        return True
    else:
        return False
    
    
t = int(input())
for i in range(t):
    (X,Y) = map(int, input().split(' '))
    isGood = goodTurn(X, Y)
    if isGood:
        print("YES")
    else:
        print("NO")