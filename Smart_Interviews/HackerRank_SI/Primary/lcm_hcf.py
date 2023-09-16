# logic: a*b = lcm * hcf


def hcf(x,y):
    if y==0:
        return x
    else:
        return hcf(y,x%y)

def lcm(x,y):
    return (x*y)//hcf(x,y)

t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    print(lcm(x,y),hcf(x,y), sep=" ")

    