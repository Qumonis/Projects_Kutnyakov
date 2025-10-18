# Проверить истину высказывания: "Среди трёх данных чисел есть хотя бы одна пара совпадающих".

a, b, c = input('Введите первое число'), input('Введите второе число'), input('Введите третье число')

while type(a) != int:  # Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Не правильно ввёл')
        a = input('Введите первое число')

while type(b) != int:  # Обработка исключений
    try:
        b = int(b)
    except ValueError:
        print('Не правильно ввёл')
        b = input('Введите второе число')

while type(c) != int:  # Обработка исключений
    try:
        c = int(c)
    except ValueError:
        print('Не правильно ввёл')
        c = input('Введите третье число')

if a == b or a == c or b == c:
    print('Совпадают')
else:
    print('Ничего не совпадает')