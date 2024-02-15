employee_data = {}

while True:
    name = input("Enter the name of the employee: ")

    if name.lower() == "no":
        break

    salary = float(input("Enter the salary of the employee: "))

    employee_data[name] = salary

print("Employee data stored in the dictionary:")
for name, salary in employee_data.items():
    print(f"Name: {name}, Salary: {salary}")