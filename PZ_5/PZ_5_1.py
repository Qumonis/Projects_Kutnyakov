#Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
#результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
#получится нуль?

def kolvo_vichitaniy(n):

    def summa(num):
        #вычисление суммы цифр числа
        if num == 0:
            return 0
        return (num % 10) + summa(num // 10)

    def vichitanie(num, count):
        #подсчет количества вычитаний
        if num == 0:
            return count
        digit_sum = summa(num)
        return vichitanie(num - digit_sum, count + 1)

    return vichitanie(n, 0)

test_number = input('Введите число: ')

while type(test_number) != int: # обработка исключений
    try:
        test_number = int(test_number)
    except ValueError:
        print("Неправильно ввели!")

result = kolvo_vichitaniy(test_number)
print(f"Число {test_number}: получим 0 через {result} действий")