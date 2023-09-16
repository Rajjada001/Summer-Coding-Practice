def power_of_2(n):
    # return int((1<<n)%1e9)
    res = 0
    if n&1 == 1:
        return False
    else:
        while n>0:
            res = n%2
            if (res & 1) and n!=1:
                # print(n)
                return False
            n = n//2
    return True


print(power_of_2(int(input())))