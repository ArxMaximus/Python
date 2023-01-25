matrix1 = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]

matrix2 = [[1, 5, 9],
           [2, 6, 10],
           [3, 7, 11],
           [4, 8, 12]]


# def transposeMatrix(m):
#     return [sum(([elem[i]] for elem in m), []) for i in range(len(m[0]))]

def transposeMatrix(m):
    return [list(i) for i in zip(*m)]


print(transposeMatrix(matrix1))
print(transposeMatrix(matrix2))
