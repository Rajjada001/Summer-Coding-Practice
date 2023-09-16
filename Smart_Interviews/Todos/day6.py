def voting(a,m,n):
    count = [0]*(m+1)
    for i in range(n):
        count[a[i]]+=1
    print(count)
    winner = 0
    for i in range(1,m+1):
        if count[i]>count[winner]:
            winner = i

    return winner

a=[1,5,2,7,10,2,5,2,2,10,7,2,3,5,2]
print(voting(a,10,len(a)))