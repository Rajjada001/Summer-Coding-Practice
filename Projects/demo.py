'''
def factorial_memo(input_value):
    if input_value < 2: 
        return 1
    if input_value not in factorial_dict:
        factorial_dict[input_value] = input_value * factorial_memo(input_value-1)
    return factorial_dict[input_value]
'''
import time
import sys

memo = {}
def mysteryRecursion(n, m):
    if (n,m) in memo:
        return memo[(n,m)]
    if n==1 and m==1:
        memo[(n,m)] = 1
    elif n==1:
        # print("Entered n")
        # print("Memo in n", memo)

        memo[(n,m)] = m * mysteryRecursion(n, m//2)
        # return memo[(n,m)]

    elif m==1:
        # print("Entered m")
        # print("Memo in m", memo)
        memo[(n,m)] = n*mysteryRecursion(n//2, m)
        # return memo[(n,m)]
    
    else:
        # print("Else Memo")
        memo[(n,m)] = m * mysteryRecursion(n, m//2) + n*mysteryRecursion(n//2, m)

    # print("Final Memo")
    return memo[(n,m)]


start=time.time()
mr = mysteryRecursion(33324, 43532)
end=time.time()
print(((end-start)*1000), "milli seconds with value of:", mr)
