def pyramid(n):
    for row in range(1, n+1):
        #   print spaces
        for i in range(1, n-row+1):
            print(" ", end="")
        for i in range(1, 2*row):
            print("*", end="")
        print()

n = int(input())
pyramid(n)