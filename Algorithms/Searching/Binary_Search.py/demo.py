def RecursiveContains(data, t):
    n = len(data)
    if n == 0:
        return False
    large,small = [],[]
    print("large=",large)
    print("small=",small)

    for i in range(1,n):
        if data[i] < data[0]:
            small.append(data[i])
        elif data[i]>data[0]:
            large.append(data[i])
    print("large=",large)
    print("small=",small)

    if data[0]==t:
        return True
    elif data[1]<t:
        return RecursiveContains(large, t)
    else:
        return RecursiveContains(small, t)


arr = [3,5, 6,8,12,32,48, 56]
t = 48

print(RecursiveContains(arr, t))