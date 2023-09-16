def bitwise_operations(x,y):
    # &
    print("x & y = ", x&y)
    # or |
    print("x | y = ", x|y)
    # xor
    print("x ^ y = ", x^y)
    # negate x
    print("negation of x = ", ~x)
    # negation of y
    print("negation of y = ", ~y)

# (x,y) = map(int, input().split())
# bitwise_operations(x,y)
    
# n = int(input())
# count = 0
# while n!=0:
#     count += n&1
#     n = n>>1
# print(count)
# print(1<<31)

#brute force
def power(a,n):
    res = 1
    for _ in range(n):
        res *= a
    return res
print(power(2,3))