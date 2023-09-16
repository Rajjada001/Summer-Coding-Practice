def long_fact(n):
    a = {}
    if n in a:
        return a[n]
    elif n<=0:
        a[n] = 1
        return 1
    else:
        a[n] = n * long_fact(n-1)
    return a[n]

n = int(input())
print(long_fact(n))

