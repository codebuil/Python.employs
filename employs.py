def add_employee_data(employees, employ_id, name, reference, price, time):
    employees.append({'employ_id': employ_id, 'name': name, 'reference': reference, 'price': price, 'time': time})

def display_employees(employees):
    if not employees:
        print("No employee data available.")
    else:
        print("Employee ID\tName\tReference\tTotal Earnings")
        for employee in employees:
            total_earnings = employee['price'] * employee['time']
            print(f"{employee['employ_id']}\t{employee['name']}\t{employee['reference']}\t{total_earnings}")

def save_to_file(employees, file_name):
    with open(file_name, 'w') as file:
        for employee in employees:
            file.write(f"{employee['employ_id']},{employee['name']},{employee['reference']},{employee['price']},{employee['time']}\n")

def load_from_file(file_name):
    employees = []
    if not file_name:
        return employees

    try:
        with open(file_name, 'r') as file:
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

def main():
    file_name = "employee_data.txt"

    employees = load_from_file(file_name)

    while True:
        print("\nEMPLOYEE MANAGEMENT MENU:")
        print("1. Add Employee Data")
        print("2. Display Employees")
        print("3. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            employ_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            reference = input("Enter Reference: ")
            price = float(input("Enter Price: "))
            time = float(input("Enter Time: "))
            add_employee_data(employees, employ_id, name, reference, price, time)
            print("Employee data added.")
        elif choice == '2':
            display_employees(employees)
        elif choice == '3':
            save_to_file(employees, file_name)
            print("Employee data saved to file.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    main()

