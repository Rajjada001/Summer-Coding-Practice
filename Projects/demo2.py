import time


def mysteryRecursion(n, m):
    if n==1 and m==1:
        return 1
    elif n==1:
        # print("Entered n")
        return m * mysteryRecursion(n, m//2)
    elif m==1:
        # print("Entered m")

        return n*mysteryRecursion(n//2, m)
    else:
        # print("for m:", m * mysteryRecursion(n, m//2))
        # print("for n:",n*mysteryRecursion(n//2, m))
        return  m * mysteryRecursion(n, m//2) + n*mysteryRecursion(n//2, m)
        # print(memo, memo_2)


start=time.time()
mr = mysteryRecursion(33324, 43532)
end=time.time()
print(int((end-start)*1000), "milli seconds with value of:", mr)
