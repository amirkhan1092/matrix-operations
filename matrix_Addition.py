

def add(i):
    return i+2

A = ['2','3','4','54']
print(A)
d=map(int,A)

print(list(d))



# def print_digit():
#     print('this is digit function ')
#     print(0,1,2,3,4,5,6,7,8,9)
#
# print_digit()



#
#
#
#
# def matrix_create(A,r,c):
#     if len(A) == r*c:
#         mt = [[] for i in range(r)]
#         fg = 0
#         count = 0
#         for k in A:
#
#             mt[fg].append(k)
#             count +=1
#             if count == c:
#                 count=0
#                 fg += 1
#
#         return mt
#
#
#     else:
#         print('dimension not agree ')
#         return False
#
#
#
# H = [2,3,3,6,8,4,3,4,5,4]
#
# r,c =eval(input('enter the row and column tob configured r,c '))
# A=matrix_create(H,r,c)
# if A == False:
#     pass
# else:
#     for i in A:
#         for k in i:
#             print(k,end='\t')
#         print()




# from builtins import range, print
#
#
# def size(A):
#     return len(A),len(A[0])
#
# A = [[2,4],
#      [3,4,5],
#      [3,5]]
#
# B = [[2,4,5],
#      [4,0,6],
#      [4,7,8]]
#
# # if size(A) == size(B):
# #     result = [[0,0,0],
# #               [0,0,0],
# #               [0,0,0]]
# #     for r in range(len(A)):
# #         for c in range(len(A[0])):
# #             result[r][c]=A[r][c] + B[r][c]
# #
# # else:
# #     print('dimension not agree')
# #
# # print(result)
# #
# # for row in result:
# #     for col in row:
# #         print(col,end='\t')
# #     print()
# a=[]
#
# for j in range(5):
#     a.append(eval(input('enter the value')))
#
#
# print(a)
#
# print(a.index(max(a)))
# print(a.index(min(a)))
#
