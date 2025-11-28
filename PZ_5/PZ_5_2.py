#Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг:
#значение A переходит в C, значение C — в B, значение B — в A (A, B, C —
#вещественные параметры, являющиеся одновременно входными и выходными). С
#помощью этой функции выполнить левый циклический сдвиг для двух данных
#наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).


def SL3(A, B, C):

    temp = A
    A = B
    B = C
    C = temp
    return A, B, C

# Первый набор чисел
A1, B1, C1 = input('Введите число A1: '), input('Введите число B1: '), input('Введите число C1: ')

while type(A1) != float:  # Обработка исключений
    try:
        A1 = float(A1)
    except ValueError:
        print('Не правильно ввёл')
        A1 = input('Введите первое число')

while type(B1) != float:  # Обработка исключений
    try:
        B1 = float(B1)
    except ValueError:
        print('Не правильно ввёл')
        B1 = input('Введите второе число')

while type(C1) != float:  # Обработка исключений
    try:
        C1 = float(C1)
    except ValueError:
        print('Не правильно ввёл')
        C1 = input('Введите третье число')
A1, B1, C1 = SL3(A1, B1, C1)
print(f"После сдвига: A1={A1}, B1={B1}, C1={C1}")

# Второй набор чисел
A2, B2, C2 = input('Введите число A2: '), input('Введите число B2: '), input('Введите число C2: ')

while type(A2) != float:  # Обработка исключений
    try:
        A2 = float(A1)
    except ValueError:
        print('Не правильно ввёл')
        A2 = input('Введите первое число')

while type(B2) != float:  # Обработка исключений
    try:
        B2 = float(B1)
    except ValueError:
        print('Не правильно ввёл')
        B2 = input('Введите второе число')

while type(C2) != float:  # Обработка исключений
    try:
        C2 = float(C2)
    except ValueError:
        print('Не правильно ввёл')
        C2 = input('Введите третье число')
A2, B2, C2 = SL3(A2, B2, C2)
print(f"После сдвига: A2={A2}, B2={B2}, C2={C2}")