# https://www.hackerrank.com/contests/smart-interviews-b33-ic1/challenges/si-number-of-divisors

def no_of_divisors(n):
    count = 0
    i = 1
    while i*i<= n:
    # for i in range(1, sqrt+1):
        if n%i==0:
            count += 2
        # in case of perfect square numbers
        if i*i == n:
            count -= 1
        i += 1
    return count

t = int(input())
for i in range(t):
    n = int(input())
    print(no_of_divisors(n))