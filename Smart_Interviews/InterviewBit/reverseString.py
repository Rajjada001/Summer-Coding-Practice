def reverse(A):
    s = list(A.split())
    l,r = 0,len(s)-1
    while l<=r:
        s[l],s[r] = s[r],s[l]
        l+=1
        r-=1
    
    res = ""
    for i in range(len(s)-1):
        res += s[i] + ' '
    res += s[len(s)-1]
    return res

A = "the sky is blue"
print(reverse(A))