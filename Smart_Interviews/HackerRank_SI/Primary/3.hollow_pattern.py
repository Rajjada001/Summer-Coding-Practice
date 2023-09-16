def printDiamond(n):
   for row in range(n):
    for col in range(n):
        if (row + col == n//2) or (col == row + n//2) or (row==col+n//2) or (row+col == n-1+n//2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
    
n = int(input())
printDiamond(n)

#   0 1 2 3 4 5 6
# 0       *
# 1     *   *
# 2   *       *
# 3 *           *
# 4   *       *
# 5     *   *
# 6       *
# #  for upper left star pattern, if row + col == n//2 then print("*")
# #  for upper right pattern, if col==n//2 + row then print *
# # for bottom left star pattern, if row==n//2 + col then print *
# for bottom right pattern, if row+col = (n-1)+n//2 then print *
