#Дано трёхзначное число. В нём зачеркнули первую справа цифру и приписали ее слева. Вывести полученное число

import tkinter as tk
from tkinter import messagebox


def transform_number():
    try:
        input_val = entry_num.get()

        if not input_val.isdigit() or len(input_val) != 3:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректное трехзначное число!")
            return

        num = int(input_val)
        last_digit = num % 10
        remaining_part = num // 10

        result_num = last_digit * 100 + remaining_part

        label_res.config(text=f"Полученное число: {result_num}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введены некорректные данные!")


root = tk.Tk()
root.title("Преобразование числа")
root.geometry("400x250")

main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(main_frame, text="Введите трехзначное число:").grid(row=0, column=0, sticky="w", pady=10)
entry_num = tk.Entry(main_frame, width=15)
entry_num.grid(row=0, column=1, sticky="w", padx=10)

calc_btn = tk.Button(main_frame, text="Преобразовать", command=transform_number, width=15)
calc_btn.grid(row=1, column=0, columnspan=2, pady=20)

tk.Label(main_frame, text="Результат:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", pady=5)

label_res = tk.Label(main_frame, text="Полученное число: -", fg="blue", font=("Arial", 10))
label_res.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)

root.mainloop()