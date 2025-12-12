#Дан список размера N, все элементы которого, кроме последнего, упорядочены по
#возрастанию. Сделать список упорядоченным, переместив последний элемент на
#новую позицию.
import random
n = input('n: ')

while type(n) != int:  # Обработка исключений
    try:
        n = int(n)
    except ValueError:
        print('Не правильно ввёл')
        n = input('n:')

c = []
for i in range(n):
    i += 1
    c.append(i)

c.append(random.randint(1,10))
c.sort()
print(c)