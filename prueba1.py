def comedor(A, B):
    contador = 0
    for i in range(len(B)):
        for j in range(len(B)):
            if A[j] == B[j]:
                contador = contador+1
                B.insert(0,B.pop())
    if len(B)**2 == contador:
        return -1
    else:
        return(contador)

print(comedor( [1,2,3,4,5,6,7,8,9],  [1,6,6,6,6,6,7,8,9]))

'''
8409214
9845018
8984501
1898450
'''


