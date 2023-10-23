# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

def mergeSortedArrays(a, m, b, n):
    res = []
    l,m = len(a),len(b)
    i,j,k = 0,0,0
    while i<l and j<m:
        if a[i]<b[j]:
            if len(res)==0 or res[-1]!=a[i]:
                res.append(a[i])
            i+=1
        else:
            if len(res)==0 or res[-1]!=b[j]:
                res.append(b[j])
            j+=1
    while i<l:
        if res[-1]!=a[i]:
            res.append(a[i])
        i+=1
    while j<m:
        if res[-1]!=b[j]:
            res.append(b[j])
        j+=1
    return res

print(mergeSortedArrays([1,2,3,4,6], 5, [2,3,5], 3))

