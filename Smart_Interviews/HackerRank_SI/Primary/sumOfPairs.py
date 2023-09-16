# approach: 
# Sort the array and use two pointer technique

# def merge(a,low,mid,high):
#     i,j = low,mid+1
#     k=0
#     temp = [0 for _ in range(high-low+1)]
#     print(temp)
#     while(i<=mid and j<=high):
#         if a[i] <= a[j]:
#             temp[k] = a[i]
#             i+=1
#         else:
#             temp[k] = a[j]
#             j += 1
#         k+=1
#     # remaining elements
#     while i<=mid:
#         temp[k] = a[i]
#         k+=1
#         i+=1
#     while j<=high:
#         temp[k] = a[j]
#         k+=1
#         j+=1
    

# def mergeSort(a,l,r):
#     if l!=r:
#         mid = l+(r-l)//2
#         # print(mid)
#         mergeSort(a,l,mid)
#         mergeSort(a,mid+1,r)
#         merge(a,l,mid,r)
#     return nums

def MergeSort(a):
    if len(a) > 1:
        mid = len(a)//2
        left = a[mid:]
        right = a[:mid]
        MergeSort(left)
        MergeSort(right)

        i=j=k=0
        # print("Before While")
        while i<len(left) and j < len(right):

            if left[i]<=right[j]:
                a[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                a[k] = right[j]
                j += 1

            k += 1

        # Remaining elements
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1

    return a

def sumOfPairs(nums, k):
    l,r = 0,len(nums)-1
    while l<r:
        s = nums[l]+nums[r]
        if s==k:
            return True
        elif s<k:
            l += 1
        else:
            r -= 1

    return False


t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    nums = list(map(int, input().split()))
#     sort the array
    MergeSort(nums)
#     Two Pointers
    print(sumOfPairs(nums, k))