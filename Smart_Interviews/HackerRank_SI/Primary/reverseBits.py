def reverseBits(n):
    res = 0
    for i in range(32):
        res = res << 1
        print("After Left shift: ", res)
        res += n%2
        print("After Updating res: ", res)
        n = n//2
    return res

t = int(input())
for _ in range(t):
    n = int(input())
    print(reverseBits(n))
