import random
import time


def matrix_create(A, r, c):
    if len(A) == r * c:
        t = [[] for _ in range(r)]
        count = 1
        flg = 0
        for p in A:
            t[flg].append(p)
            if count == c:
                count = 0
                flg += 1

            count += 1
        return t
    else:
        print('invalid dimension with array ')


# # matrix creation
row, col = eval(input(' enter the dimension of matrix (Row X Column)'))
print('total number of data user to be entered ', row * col)

sel = input('would you like to enter row wise data press 1 and 2 for individual ')
mat = [[] for _ in range(row)]
if sel == '1':
    for rm in range(row):
        print('enter the {} row with comma separated '.format(rm + 1), end=' ')
        mat[rm].append(list(eval(input())))
elif sel == '2':
    matt = []
    for tt in range(row * col):
        print('enter the {} data '. format(tt),end='')
        matt.append(eval(input()))
        # ft = random.randint(0, 100)
        # print(ft, end=' ')
        # matt.append(ft)
        # time.sleep(.6)
    mat = matrix_create(matt, row, col)

# print(mat)
#
# a = [1, 2,3,43,4,5,4,6,767]
# mat = matrix_create(a,3,3)
for k in mat:
    for j in k:
        print(j, end='\t')
    print()
