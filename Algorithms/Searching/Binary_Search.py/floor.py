def ceil(a, t):

    l,r = 0,len(a)-1
    while l<=r:
        mid = l + (r-l)//2
        if a[mid] == t:
            return mid
        elif a[mid] > t:
            r = mid-1
        else:
            l = mid+1

    return r

a = [2,3,5,9,14,16,18]
t = 15

print(ceil(a,t))
