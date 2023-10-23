def spiral_traversl(nums, rows, cols):
    r,c = 0,0
    direction = 0 # 0:right, 1:down, 2:left, 3:up
    while r<rows and c<cols:
        if direction == 0:
            for i in range(c, cols):
                print(nums[r][i], end=" ")
            r += 1
        elif direction == 1:
            for i in range(r, rows):
                print(nums[i][cols-1], end=" ")
            cols -= 1
        elif direction == 2:
            for i in range(cols-1, c-1, -1):
                print(nums[rows-1][i], end=" ")
            rows -=1
        elif direction == 3:
            for i in range(rows-1, r-1, -1):
                print(nums[i][c], end=" ")
            c += 1
        direction = (direction+1)%4
    print()


m=n = int(input())
mat = []
for i in range(m):
    row = list(map(int, input().split()))[:m]
    mat.append(row)
spiral_traversl(mat,m,n)