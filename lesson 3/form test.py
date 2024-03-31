import tkinter as tk


class Human:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

def submit_form():
    name = name_entry.get()
    position = position_entry.get()
    salary = salary_entry.get()


    human = Human(name, position, salary)


    info_label.config(text=f"Ім'я: {human.name}\nПосада: {human.position}\nЗарпата: {human.salary}")
    year_salary = int(salary)*12
    salary_label.config(text=f"Зарплата за рік: {year_salary}")

    main_frame.pack_forget()
    info_frame.pack()



root = tk.Tk()
root.title("Форма для введення інформації")


main_frame = tk.Frame(root)
name_label = tk.Label(main_frame, text="Ім'я:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(main_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

position_label = tk.Label(main_frame, text="Посада:")
position_label.grid(row=1, column=0, padx=5, pady=5)
position_entry = tk.Entry(main_frame)
position_entry.grid(row=1, column=1, padx=5, pady=5)

salary_label = tk.Label(main_frame, text="Зарплата:")
salary_label.grid(row=2, column=0, padx=5, pady=5)
salary_entry = tk.Entry(main_frame)
salary_entry.grid(row=2, column=1, padx=5, pady=5)




submit_button = tk.Button(main_frame, text="Підтвердити", command=submit_form)
submit_button.grid(row=4, columnspan=2, padx=5, pady=5)

main_frame.pack()


info_frame = tk.Frame(root)
info_label = tk.Label(info_frame, text="")
info_label.pack(padx=10, pady=10)
salary_label = tk.Label(info_frame, text="Зарплата за рік:")
salary_label.pack()








root.mainloop()
