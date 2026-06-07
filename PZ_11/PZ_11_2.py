#Составить генератор (yield), который преобразует все буквенные символы в
#заглавные.

def upp(b):
    yield b.upper()

a = 'kalsjdhbn'
b = list(upp(a))
print(a)
print(b)