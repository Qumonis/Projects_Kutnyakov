# Дано вещественное число X и целое число N (> 0). Найти значение выражения X -
# X3/(3!) + X5/(5!) - ... + (-1)N-X2-N+1/((2-N+1)!) (N! = 12 ...N). Полученное число
# является приближенным значением функции sin в точке X

X = input("Введите действительное число X: ")
N = input("Введите целое число N (> 0): ")

while type(N) != int:  #Обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Не то ввел")
        N = input("Введите целое число N (> 0): ")

while type(X) != float:  #Обработка исключений
    try:
        X = float(X)
    except ValueError:
        print("Не то ввел")
        X = input("Введите действительное число X: ")

if N <= 0:
    print("Ошибка: N должно быть больше 0!")
else:
    # Вычисление приближенного значения sin(x)
    result = 0
    stepen = 1
    i = 1

    while i <= N:
        # Вычисляем факториал для текущего нечётного числа
        factorial = 1
        temp = stepen
        i += 1

        while temp > 0:
            factorial *= temp
            temp -= 1
        # Переходим к следующему нечётному числу
        t = ((-1) ** i) * (X ** stepen) / factorial
        result += t
        stepen += 2

    print(f"Приближенное значение sin({X}) = {result}")

