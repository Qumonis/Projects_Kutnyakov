#В матрице найти среднее арифметическое элементов последних двух столбцов.

import random
from functools import reduce

a = [[random.randint(-5, 5) for x in range(random.randint(3, 7))] for y in range(random.randint(3, 7))]

b = reduce(lambda x, y: x + y, a[-2]) // len(a[-2])
c = reduce(lambda x, y: x + y, a[-1]) // len(a[-1])

print(a)
print('Среднее арифметическое последних двух столбцов:', b, c)
