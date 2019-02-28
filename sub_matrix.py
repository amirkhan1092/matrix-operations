
# matrix print and indexing
def matrix_create(A,r,c):
    mat=[[] for _ in range(r)]
    if len(A) >= r*c:
        fg=0
        count = 0
        for k in A:
            mat[fg].append(k)
            count += 1
            if count==c:
                count=0
                fg +=1

        return mat
    else:
        print('dimension not match ')
        return False


A=[2,4,6,5,4,4,6,8,9,4,3,5]
mat=matrix_create(A,4,3)
for row in mat:
    for col in row:
        print(col,end='\t')
    print()

# mat = [[1,3,6,7],[2,5,9,6], [2,43,4,5],[4,54,33,23]]
# for row in mat:
#     for col in row:
#         print(col,end='\t')
#     print()
#
#
# Sub Matrix
# print('\n')
# ro,ro1,co,co1= eval(input('enter sub matrix coordinate '))
# sub=mat[ro:ro1]
# tt=[[] for _ in  range(ro,ro1)]
# for ct,row in enumerate(sub):
#     for c,col in enumerate(row):
#         if c in range(co,co1):
#             print(col,end='\t')
#             tt[ct].append(col)
#         else:
#             pass
#     print()
# for row in tt:
#     for col in row:
#         print(col,end='\t')
#     print()