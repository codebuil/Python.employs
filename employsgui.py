import tkinter as tk

def add_employee():
    employ_id = employ_id_entry.get()
    name = name_entry.get()
    reference = reference_entry.get()
    price = float(price_entry.get())
    time = float(time_entry.get())

    employees.append({'employ_id': employ_id, 'name': name, 'reference': reference, 'price': price, 'time': time})
    update_display()

def display_employees():
    employees_text.delete(1.0, tk.END)
    if not employees:
        employees_text.insert(tk.END, "No employee data available.")
    else:
        employees_text.insert(tk.END, "Employee ID\tName\tReference\tTotal Earnings\n")
        for employee in employees:
            total_earnings = employee['price'] * employee['time']
            employees_text.insert(tk.END, f"{employee['employ_id']}\t{employee['name']}\t{employee['reference']}\t{total_earnings}\n")

def save_and_exit():
    save_to_file()
    root.destroy()

def save_to_file():
    with open("employee_data.txt", 'w') as file:
        for employee in employees:
            file.write(f"{employee['employ_id']},{employee['name']},{employee['reference']},{employee['price']},{employee['time']}\n")

def load_from_file():
    employees = []
    try:
        with open("employee_data.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                employees.append({
                    'employ_id': data[0],
                    'name': data[1],
                    'reference': data[2],
                    'price': float(data[3]),
                    'time': float(data[4])
                })
    except FileNotFoundError:
        pass

    return employees

def update_display():
    display_employees()

employees = load_from_file()

root = tk.Tk()
root.title("Employee Management")
root.configure(bg="brown", width=800, height=600)  # Define a cor de 


employ_id_label = tk.Label(root, text="Employee ID:")
employ_id_label.grid(row=0, column=0)
employ_id_entry = tk.Entry(root)
employ_id_entry.grid(row=0, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

reference_label = tk.Label(root, text="Reference:")
reference_label.grid(row=2, column=0)
reference_entry = tk.Entry(root)
reference_entry.grid(row=2, column=1)

price_label = tk.Label(root, text="Price:")
price_label.grid(row=3, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=3, column=1)

time_label = tk.Label(root, text="Time:")
time_label.grid(row=4, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=4, column=1)

add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.grid(row=5, columnspan=2)

display_button = tk.Button(root, text="Display Employees", command=display_employees)
display_button.grid(row=6, columnspan=2)

employees_text = tk.Text(root, height=10, width=40)
employees_text.grid(row=7, columnspan=2)

exit_button = tk.Button(root, text="Save and Exit", command=save_and_exit)
exit_button.grid(row=8, columnspan=2)

root.mainloop()

