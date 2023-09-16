# Assume if the twotothe(n) = 2^n
def twotothe(n):
    # Base Case
    if n == 0:
        return 1
    else:
        # 
        return 2 * twotothe(n-1)


print(twotothe(7))