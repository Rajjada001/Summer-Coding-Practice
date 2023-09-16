
def rotateMatrix(mat):

        
    for i in range(len(mat)):
        for j in range(i):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
#     reverse the matrix
    for i in range(len(mat)):
        mat[i].reverse()
    return mat
            
def displayMatrix(ma):
    for i in range(len(mat)):
        for j in range(len(mat)):
            print(mat[i][j], end=" ")
        print()

    

# test cases
t = int(input())
for i in range(t):
    n = int(input())
    # declare mat
    mat = []
    for j in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    print("Test Case #:{0}".format(i+1))
    rotateMatrix(mat)
    displayMatrix(mat)