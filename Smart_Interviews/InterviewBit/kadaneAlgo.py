def maxSubArray(A):
        n = len(A)
        maxSum = -1e8
        currSum = 0
        for i in range(n):
            currSum = currSum+A[i]
            if currSum>maxSum:
                maxSum = currSum
            if currSum<0:
                currSum = 0
        return maxSum

A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(A))