#Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна
#содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия
#водителя, даты отправки и прибытия, масса груза.

import sqlite3
from data import insert_initial_data

DB_NAME = "transport.db"


def print_table(title, rows):
    print(f"\nНазвание операции: {title} ")
    for row in rows:
        print(row)


try:
    # Создание таблицы
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS deliveries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                route TEXT NOT NULL,
                driver_lastname TEXT NOT NULL,
                departure_date TEXT NOT NULL,
                arrival_date TEXT NOT NULL,
                cargo_mass REAL NOT NULL
            )
        """)

    # Заполнение базы начальными данными (10 позиций)
    insert_initial_data()

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Вывод исходного состояния
        cursor.execute("SELECT * FROM deliveries")
        print_table("Исходное состояние базы данных", cursor.fetchall())

        # --- ЗАПРОСЫ НА ПОИСК ---
        # 1. Поиск рейсов определенного водителя
        cursor.execute("SELECT * FROM deliveries WHERE driver_lastname = 'Иванов'")
        print_table("Поиск рейсов водителя 'Иванов'", cursor.fetchall())

        # 2. Поиск рейсов с массой груза более 15 тонн
        cursor.execute("SELECT * FROM deliveries WHERE cargo_mass > 15.0")
        print_table("Поиск рейсов с массой груза > 15 тонн", cursor.fetchall())

        # 3. Поиск рейсов, отправленных по маршруту из Москвы
        cursor.execute("SELECT * FROM deliveries WHERE route LIKE 'Москва%'")
        print_table("Поиск рейсов, отправленных из Москвы", cursor.fetchall())

        # --- ЗАПРОСЫ НА РЕДАКТИРОВАНИЕ ---
        # 1. Изменение водителя для конкретного рейса по id
        cursor.execute("UPDATE deliveries SET driver_lastname = 'Петров' WHERE id = 1")

        # 2. Увеличение массы груза на 1.5 тонны для всех рейсов в Санкт-Петербург
        cursor.execute("""
            UPDATE deliveries 
            SET cargo_mass = cargo_mass + 1.5 
            WHERE route = 'Москва - Санкт-Петербург'
        """)

        # 3. Изменение даты прибытия для рейсов, отправленных 2026-06-02
        cursor.execute("""
            UPDATE deliveries 
            SET arrival_date = '2026-06-05' 
            WHERE departure_date = '2026-06-02'
        """)
        conn.commit()

        # Вывод после редактирования
        cursor.execute("SELECT * FROM deliveries")
        print_table("Состояние базы данных после операций редактирования", cursor.fetchall())

        # --- ЗАПРОСЫ НА УДАЛЕНИЕ ---
        # 1. Удаление конкретного рейса по id
        cursor.execute("DELETE FROM deliveries WHERE id = 5")

        # 2. Удаление рейсов с мелким грузом (меньше 4 тонн)
        cursor.execute("DELETE FROM deliveries WHERE cargo_mass < 4.0")

        # 3. Удаление рейсов водителя Новикова
        cursor.execute("DELETE FROM deliveries WHERE driver_lastname = 'Новиков'")
        conn.commit()

        # Вывод после удаления
        cursor.execute("SELECT * FROM deliveries")
        print_table("Состояние базы данных после операций удаления", cursor.fetchall())

except sqlite3.Error as error:
    print(f"Произошла ошибка при работе с SQLite: {error}")