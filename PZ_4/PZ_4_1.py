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

while type(X) != float:
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

    n = int(input("Введите n: "))
    stepen = 1
    i = 0

    while stepen <= N:
        # Вычисляем факториал для текущего нечётного числа
        factorial = 1
        temp = stepen
        i += 1
        print('bykva', i)
        while temp > 0:
            factorial *= temp
            temp -= 1

        # Переходим к следующему нечётному числу
        stepen += 2

        # Вычисляем член ряда: (-1)^i * x^(2i+1) / (2i+1)!
        t = ((-1) ** i) * (X ** stepen) / factorial
        result += t

    print(f"Приближенное значение sin({X}) = {result}")

