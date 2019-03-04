def dimension(A):
    return len(A),len(A[0])


X = [[2, 3, 4], [3, 5, 6]]
Y = [[2, 6], [2, 8], [4, 6]]

r1, c1 = dimension(X)
r2, c2 = dimension(Y)

result = [[[0]*2]*2]



if c1 == r2:

    # iterate through rows of X
    for i in range(r1):
        # iterate through columns of Y
        for j in range(c2):
            # iterate through rows of Y
            for k in range(c1):
                result[i][j] += X[i][k] * Y[k][j]


else:
    print(' dimension not valid for matrix multiplication ')

print(result)
