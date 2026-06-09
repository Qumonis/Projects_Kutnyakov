import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Регистрация")
root.geometry("600x550")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill="both", expand=True)

# Заголовок внутри формы
title_label = tk.Label(main_frame, text="Создание нового сайта", font=("Arial", 14, "bold"), fg="#0088cc")
title_label.grid(row=0, column=0, columnspan=2, pady=15, sticky="n")

# Email
tk.Label(main_frame, text="Email").grid(row=1, column=0, sticky="w", pady=5)
email_entry = tk.Entry(main_frame, width=30)
email_entry.grid(row=1, column=1, sticky="w", padx=10)

# Пароль
tk.Label(main_frame, text="Пароль").grid(row=2, column=0, sticky="w", pady=5)
pass_entry = tk.Entry(main_frame, width=30, show="*")
pass_entry.grid(row=2, column=1, sticky="w", padx=10)

# Имя
tk.Label(main_frame, text="Имя").grid(row=3, column=0, sticky="w", pady=5)
first_name_entry = tk.Entry(main_frame, width=30)
first_name_entry.grid(row=3, column=1, sticky="w", padx=10)

# Фамилия
tk.Label(main_frame, text="Фамилия").grid(row=4, column=0, sticky="w", pady=5)
last_name_entry = tk.Entry(main_frame, width=30)
last_name_entry.grid(row=4, column=1, sticky="w", padx=10)

# Никнейм
tk.Label(main_frame, text="Никнейм").grid(row=5, column=0, sticky="w", pady=5)
nickname_entry = tk.Entry(main_frame, width=30)
nickname_entry.grid(row=5, column=1, sticky="w", padx=10)

# Дата рождения
tk.Label(main_frame, text="Дата рождения").grid(row=6, column=0, sticky="w", pady=5)

dob_frame = tk.Frame(main_frame)
dob_frame.grid(row=6, column=1, sticky="w", padx=10)

day_var = tk.StringVar(value="День")
day_menu = ttk.Combobox(dob_frame, textvariable=day_var, values=[str(i) for i in range(1, 32)], width=5)
day_menu.pack(side="left", padx=2)

month_var = tk.StringVar(value="Месяц")
months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
month_menu = ttk.Combobox(dob_frame, textvariable=month_var, values=months, width=10)
month_menu.pack(side="left", padx=2)

year_var = tk.StringVar(value="Год")
year_menu = ttk.Combobox(dob_frame, textvariable=year_var, values=[str(i) for i in range(2026, 1900, -1)], width=6)
year_menu.pack(side="left", padx=2)

# Пол
tk.Label(main_frame, text="Пол").grid(row=7, column=0, sticky="nw", pady=5)
gender_var = tk.StringVar(value="Мужчина")

gender_frame = tk.Frame(main_frame)
gender_frame.grid(row=7, column=1, sticky="w", padx=10)

tk.Radiobutton(gender_frame, text="Мужчина", variable=gender_var, value="Мужчина").pack(side="left", padx=5)
tk.Radiobutton(gender_frame, text="Женщина", variable=gender_var, value="Женщина").pack(side="left", padx=5)

# Место проживания
tk.Label(main_frame, text="Место проживания").grid(row=8, column=0, sticky="w", pady=5)
location_var = tk.StringVar(value="Другой город...")
location_menu = ttk.Combobox(main_frame, textvariable=location_var, values=["Москва", "Санкт-Петербург", "Новосибирск", "Другой город..."], width=28)
location_menu.grid(row=8, column=1, sticky="w", padx=10)

# Код безопасности (Капча)
tk.Label(main_frame, text="Код безопасности").grid(row=9, column=0, sticky="w", pady=5)

captcha_frame = tk.Frame(main_frame)
captcha_frame.grid(row=9, column=1, sticky="w", padx=10)

captcha_entry = tk.Entry(captcha_frame, width=10)
captcha_entry.pack(side="left")

captcha_img_label = tk.Label(captcha_frame, text=" VPyJL ", font=("Courier", 14, "italic bold"), bg="#e0e0e0", fg="#333333", bd=1, relief="solid")
captcha_img_label.pack(side="left", padx=10)

# Чекбокс согласия
terms_var = tk.BooleanVar(value=True)
terms_check = tk.Checkbutton(main_frame, text="Подтверждаю условия использования uID сообщества", variable=terms_var)
terms_check.grid(row=10, column=0, columnspan=2, pady=15, sticky="w")

# Кнопки
button_frame = tk.Frame(root, pady=10)
button_frame.pack(fill="x", side="bottom")

register_btn = tk.Button(button_frame, text="Регистрация", width=15, bg="#0088cc", fg="white")
register_btn.pack(pady=5)

root.mainloop()