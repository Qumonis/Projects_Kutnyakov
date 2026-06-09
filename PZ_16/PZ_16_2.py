# Создание базового класса "Животное" и его наследование для создания классов "Собака" и "Кошка".
# В классе "Животное" будут общие методы, такие как "дышать" и "питаться",
# а классы-наследники будут иметь свои уникальные методы и свойства, такие как "гавкать" и "мурлыкать".

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f"{self.name} дышит кислородом"

    def eat(self):
        return f"{self.name} потребляет пищу"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def bark(self):
        return f"{self.name} гавкает"


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def purr(self):
        return f"{self.name} мурлычет"


dog = Dog(name="Шарик")
cat = Cat(name="Мурка")

print("Собака:")
print(f"Процесс жизнедеятельности: {dog.breathe()} и {dog.eat()}")
print(f"Издаваемый звук: {dog.bark()}")

print("\nКошка:")
print(f"Процесс жизнедеятельности: {cat.breathe()} и {cat.eat()}")
print(f"Издаваемый звук: {cat.purr()}")