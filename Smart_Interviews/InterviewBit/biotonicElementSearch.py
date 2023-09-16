# Approach: Find peak element
# if the peak element is target: return the index
# else if the A[peak] < target element, return -1
# else(target > A[peak] element)
    # Search the Ascending part of the array(0 to peak-1)
    # if the target doesn't exist, then return -1
    # Search the Descending part of the array(peak to n-1)

def peakElement(A):
    l,r = 0,len(A)-1
    while l<r:
        mid = (l+r)>>1
        if A[mid]>A[mid+1]:
            r = mid
        else:
            l = mid+1
    return l

def ascendingBinarySearch(A, low, high, B):
    while low<=high:
        mid = (low+high)>>1
        if A[mid]==B:
            return mid
        elif A[mid]<B:
            low = mid+1
        else:
            high = mid-1
    return -1

def descendingBinarySearch(A, low, high, B):
    while low<=high:
        mid = (low+high)>>1
        if A[mid]==B:
            return mid
        elif A[mid]<B:
            high = mid-1
        else:
            low = mid+1
    return -1

def searchBiotonic(A, B):
    peak = peakElement(A)
    print(peak)
    if A[peak] == B:    
        return peak
    elif A[peak]<B:
        # print("Entered elif")
        return -1
    else:
        # print(peak)
        temp = ascendingBinarySearch(A, 0, peak-1, B)
        if temp != -1:
            return temp
        temp = descendingBinarySearch(A, peak+1, len(A)-1, B)
        if temp != -1:
            return temp
    
    return -1

A = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 ]
B = 12
print(searchBiotonic(A, B))