
def binarySearch(a,k):
    l,r = 0,len(a)-1
    while l<=r:
        mid = l + (r-l)//2
        # print(mid)
        if a[mid] == k:
            return mid
        
        elif a[mid] > k:
            r = mid-1
        else:
            l = mid + 1
        
    return -1


a = [1,2,3,4,5,6,7]
k = 1
print(binarySearch(a,k))   