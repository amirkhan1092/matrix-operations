def matrix_size(A):
    return len(A),len(A[0])
A = [[1, 3, 4],
     [3, 5, 6],
     [3, 54, 8]]

B = [[2, 9, 0],
     [3, 6, 4],
     [3, 5, 9]]

# Add matrix B with Row of matrix A
C = A+B

print('Size of matrix A ', len(A),'x',len(A[0]))

#Addition
if matrix_size(A) == matrix_size(B):
    result = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]

else:
    print('dimension for Addition didnt match ')


for i in result:
    for k in i:
        print(k,end=' ')

    print()


