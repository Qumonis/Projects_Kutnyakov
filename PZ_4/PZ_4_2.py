# Дано целое число N (> 0). Найти сумму 1N + 2N-1 + ... + N1

N = input("Введите целое число N (> 0): ")

while type(N) != int:  #Обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Не то ввел")
        N = input("Введите целое число N (> 0): ")

if N <= 0:
    print("Ошибка: N должно быть больше 0!")
else:
  st = 0; t = 0
  while st < N:
    st += 1
    p = st ** st
    t += p

print(f'Сумма: {t}')
