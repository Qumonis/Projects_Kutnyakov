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
    print("Вычисление ряда:")

    # Вычисляем степень: 1, 3, 5, 7, ...
    i = 1; stepen = 1
    while i <= N:
        i += 1
        stepen += 2

        # Вычисляем факториал для знаменателя
        factorial = 1
        while stepen:
            factorial *= stepen
        stepen -= 1

        # Вычисляем член ряда: (-1)^i * x^(2i+1) / (2i+1)!
        t = ((-1) ** i) * (X ** stepen) / factorial
        result += t

        # Вывод текущего члена ряда
        sign = "+" if ((-1) ** i) > 0 else "-"
        if i == 0:
            print(f"x", end="")
        else:
            print(f" {sign} x^{stepen}/{stepen}!", end="")

    print(f"\n\nПриближенное значение sin({X}) = {result}")

