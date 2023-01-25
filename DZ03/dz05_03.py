import random

matrix = list(list(random.randint(0, 10) for i in range(6)) for j in range(6))
line = list(random.randint(0, 10) for i in range(6))
print('\n'.join('\t\t'.join(str(matrix[j][i]) for i in range(6)) for j in range(6)))
print(line, '\n')
newMatrix = sum(map(lambda x: [x[0]] + [x[1]], zip([line] * 3, matrix[1::2])), [])
print('\n'.join('\t\t'.join(str(newMatrix[j][i]) for i in range(6)) for j in range(6)))
