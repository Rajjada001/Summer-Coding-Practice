# https://www.hackerrank.com/contests/smart-interviews/challenges/si-x-and-y-set-bits/problem

def set_xy(x,y):
    return (1<<x | 1<<y)%1000000007

t = int(input())
for _ in range(t):
    x,y = map(int, input().split())
    print(set_xy(x,y))
