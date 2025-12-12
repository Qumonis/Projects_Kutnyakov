#Дан список размера N и целые числа K и L (1 < K < L < N). Найти сумму элементов
#списка с номерами от K до L включительно.
import random
k, l, n = input('k > 1: '), input('l > k: '), input('n > l: ')

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Не правильно ввёл')
        n = input('n:')

while type(k) != int:  # Обработка исключений
    try:
        k = int(k)
    except ValueError:
        print('Не правильно ввёл')
        k = input('k:')

while type(l) != int:  # Обработка исключений
    try:
        l = int(l)
    except ValueError:
        print('Не правильно ввёл')
        l = input('l:')

if 1 > k or k > l or l > n:
    print('Заного')
else:
    c = []
    f = 0
    for i in range(n):
        i += 1
        c.append(random.randint(0, 5))
    v = c[c.index(k):c.index(l) + 1]
    v = sum(v)
    print(v)