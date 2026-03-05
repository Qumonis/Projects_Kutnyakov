#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Сумма элементов:
#Элементы до n-1 умножены на элемент n:

import random

s = ''

for i in range(random.randint(5, 11)):
    s += str(random.randint(-5, 5)) + ' '
l = [s]

f1 = open('data.txt', 'w')
f1.writelines(l)
f1.close()

f2 = open('data1.txt', 'w')
f2.write('Исходные данные: ')
f2.writelines(l)
f2.close()

f1 = open('data.txt')
k = len(f1.read().split())
f1.close()

f1 = open('data.txt')
v = 0
for i in f1.read().split():
    v += int(i)
f1.close()

f1 = open('data.txt')
c = f1.read().split()
g = []
for j in c[:-1]:
    g.append(int(j) * int(c[-1]))
f1.close()

f2 = open('data1.txt', 'a')
f2.write('\n')
f2.write('Количество элементов: ')
f2.writelines(str(k))
f2.write('\n')
f2.write('Сумма элементов: ')
f2.writelines(str(v))
f2.write('\n')
f2.write('Элементы до n-1 умножены на элемент n: ')
f2.writelines(str(g))
f2.close()

f2 = open('data1.txt')
print(f2.read())
f2.close()
