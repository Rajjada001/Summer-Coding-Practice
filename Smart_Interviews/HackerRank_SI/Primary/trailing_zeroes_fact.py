def factorial_trailing_zeroes(n):
    count = 0
    while n>0:
        n = n//5
        count += n
    return count
t = int(input())
for _ in range(t):
    n = int(input())
    print(factorial_trailing_zeroes(n))