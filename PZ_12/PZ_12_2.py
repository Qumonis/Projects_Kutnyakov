#Перенести в новую матрицу Matr1 элементы, которые не находятся в первых и
#последних сроках и столбцах матрицы Matr2 произвольного размера.

import random

Matr2 = [[random.randint(-5, 5) for x in range(random.randint(3, 7))] for y in range(random.randint(3, 7))]

Matr1 = [x for x in Matr2[1:-1]]

print('Matr1:', Matr1)
print('Matr2:', Matr2)