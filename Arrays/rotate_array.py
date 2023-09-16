def reverse(a, l, r):
    
    while l<=r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
    return a


def rotateLeft(a, k):
    n = len(a)
    k = k % n

    reverse(a, 0, n-1) # [5 4 3 2 1]
    reverse(a, 0, k) 
    reverse(a, k+1, n-1)

    return a


def rotateRight(a, k):
    n = len(a)
    k = k % n
    
    reverse(a, 0, n-1)
    reverse(a, 0, k-1)
    reverse(a, k, n-1)

    return a

a = [1,2,3,4,5]
print(rotateRight(a, 2))
print(rotateLeft(a, 2))




def maxArr(arr):
    return max(arr)

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    print(maxArr(arr))