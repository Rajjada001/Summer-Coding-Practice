def moveZeroes(a):
    j = 0
    for i in range(len(A)):
        num = 0
        if A[i]>0:
            A[j] = A[i]
            j += 1
    # print(A, j)
    # remainingEl = len(A)-k
    # print(remainingEl)
    for i in range(j, len(A)):
        A[i]= 0
        
    return A

A = [0]
print(moveZeroes(A))