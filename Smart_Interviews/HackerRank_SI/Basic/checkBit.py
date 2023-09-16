def checkbit(n, i):
    # if i>=n:
    #     return False
    # binForm = []
    # while n>0:
    #     rem = n%2
    #     binForm.append(rem)
    #     n = n >> 1
    # if binForm[i]==1:
    #     print("true")
    # else:
    #     print("false")

    # Approach Two
    if n & (1<<i):
        print('true')
    else:
        print('false')

(n,i) = map(int, input().split())
checkbit(n,i)