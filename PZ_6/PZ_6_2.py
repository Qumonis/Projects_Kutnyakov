#ан целочисленный список размера N. Найти количество различных элементов в
#данном списке.
import random
n = input('n: ')

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Не правильно ввёл')
        n = input('n:')

c = []
b = []
f = 0
for i in range(n):
    i += 1
    c.append(random.randint(0, 5))

for j in c:
    if j not in b:
        b.append(j)
        f += 1

print(f)
