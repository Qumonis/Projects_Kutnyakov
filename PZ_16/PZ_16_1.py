# Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
# Добавьте методы для вычисления среднего балла и определения, является ли студент отличником.

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_excellent_student(self):
        return self.get_average_grade() >= 4.7


student1 = Student("Иван", "Иванов", [5, 5, 4, 5, 5])
student2 = Student("Петр", "Петров", [3, 4, 3, 5, 4])

print("Информация о студентах:")
print(f"Студент 1: {student1.first_name} {student1.last_name}")
print(f"Оценки: {student1.grades}")

print(f"\nСтудент 2: {student2.first_name} {student2.last_name}")
print(f"Оценки: {student2.grades}")

avg1 = student1.get_average_grade()
avg2 = student2.get_average_grade()

print("\nРезультат анализа успеваемости:")
print(f"Средний балл {student1.last_name}: {round(avg1, 2)}")
print(f"Является отличником: {'Да' if student1.is_excellent_student() else 'Нет'}")

print(f"\nСредний балл {student2.last_name}: {round(avg2, 2)}")
print(f"Является отличником: {'Да' if student2.is_excellent_student() else 'Нет'}")