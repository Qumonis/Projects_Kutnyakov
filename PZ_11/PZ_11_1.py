#В последовательности на n целых элементов найти среднее арифметическое
#элементов первой трети.

from functools import reduce
import random

a = [random.randint(-5, 5) for x in range(random.randint(7, 15))]
print(a)

b = len(a) // 3
c = a[:b]
d = reduce(lambda x, y: x + y, c) / b
print(c)
print(d)
