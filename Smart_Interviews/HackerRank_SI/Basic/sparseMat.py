def sparseMatrix(mat):
    countZero = 0
    checkSparse = 0
    for row in range(len(mat[0])):
        col = 0
        if mat[row][col] == 0:
            countZero += 1
        col = 0
    if countZero > len(mat[0])//2:
        print("Yes")

r,c = map(int, input().split())
mat = [[int(n) for n in input().split()] for _ in range(r)]
sparseMatrix(mat)
    