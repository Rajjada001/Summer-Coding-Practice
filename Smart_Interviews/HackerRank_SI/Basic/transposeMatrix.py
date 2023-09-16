def transpose(mat,m,n):
    for i in range(m):
        for j in range(i+1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    


def displayMatrix(mat, n,m):
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print()

# test cases
mat = []
n,m = map(int, input().split())
for j in range(n):
    row = list(map(int, input().split()))[:m]
    mat.append(row)
transpose(mat,m,n)
displayMatrix(mat, n, m)