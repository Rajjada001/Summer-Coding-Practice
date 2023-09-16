def multiplication(n):
    for i in range(1,11):
        print("{0} * {1} = {2}".format(n, i, n*i))

n = int(input())
multiplication(n)