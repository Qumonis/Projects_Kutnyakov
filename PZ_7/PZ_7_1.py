a = input('Введите что нибудь: ')

try:  # Обработка исключений
    a = int(a)
except ValueError:
    try:
        a = float(a)
    except ValueError:
        print(3)

if type(a) == int:
    print(1)
elif type(a) == float:
    print(2)