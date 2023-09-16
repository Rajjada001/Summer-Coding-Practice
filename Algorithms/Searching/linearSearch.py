def linearSearch(a, k):
    for num in a:
        if num == k:
            return True
    return False


a = [1,2,3,4,5,6,7]
k = 1
print(linearSearch(a,k))   