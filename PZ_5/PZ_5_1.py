#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится нуль?

def vych(num):

    def summa(num):
        f = 0
        num = str(num)
        for i in num:
            i = int(i)
            f += i
        return f

    g = 0

    while num != 0:
        num -= summa(num)
        g += 1

    return g

b = input('Введите число: ')

while type(b) != int: # Обработка исключений

    try:
        b = int(b)
    except ValueError:
        print('Не то ввёл')
        b = input('Введите число: ')

print(f'Через {vych(b)} действий получится 0')