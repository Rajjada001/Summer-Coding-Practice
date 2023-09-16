def sort(a):
    l,r = 0,len(a)-1
    while l<r:
        if a[l]>a[r]:
            a[l],a[r] = a[r],a[l]
        if a[l]==0:
            l+=1
        if a[r]==1:
            r-=1
    return a

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    sort(a)
    for num in a:
        print(num, end=" ")
    print()