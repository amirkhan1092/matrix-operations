def dimension(A):
    return len(A),len(A[0])


A = [[2,4,5],
     [3,7,9]]

B = [[2,6],
     [3,7],
     [2,4]]

r1,c1=dimension(A)
r2,c2=dimension(B)

if c1==r2:
    result =[[0,0],
             [0,0]]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] *B[k][j]

else:
    print('dimension not match ')


for i in result:
    print(i)


