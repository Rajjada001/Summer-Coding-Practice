def merge(nums1, m, nums2, n):
    i,j = m-1,n-1
    k = (m+n)-1
    while i>0 and j>0:
        if nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i-=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1
    
    while i>0:
        nums1[k]=nums1[i]
        i-=1
        k-=1
    while j>0:
        nums1[k]=nums2[j]
        j-=1
        k-=1
    return nums1

a1 = [1,2,3,0,0,0]
a2 = [2,5,6]
merge(a1, len(a1), a2, len(a2))