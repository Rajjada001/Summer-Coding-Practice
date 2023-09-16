def add(a,b):
    while b>0:
        carry = a&b
        print("carry: ",carry)
        a = a ^ b
        print("a^b: ",a)

        b = carry << 1
        print("b: ",b)
    return a

a,b = map(int, input().split())
print(add(a,b))