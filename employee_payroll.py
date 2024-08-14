# Function to get employee name
def get_employee_name():
    return input("Enter the employee's name: ")

# Function to get total hours worked
def get_total_hours():
    while True:
        try:
            return float(input("Enter total hours worked: "))
        except ValueError:
            print("Please enter a valid number for total hours.")

# Function to get hourly rate
def get_hourly_rate():
    while True:
        try:
            return float(input("Enter hourly rate: "))
        except ValueError:
            print("Please enter a valid number for hourly rate.")

# Function to get income tax rate
def get_income_tax_rate():
    while True:
        try:
            return float(input("Enter income tax rate (as a percentage): ")) / 100
        except ValueError:
            print("Please enter a valid number for income tax rate.")

# Function to calculate gross pay, income tax, and net pay
def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = total_hours * hourly_rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

# Function to display individual employee information
def display_employee_info(name, total_hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay):
    print(f"\nEmployee Name: {name}")
    print(f"Total Hours: {total_hours}")
    print(f"Hourly Rate: ${hourly_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Income Tax Rate: {tax_rate * 100:.2f}%")
    print(f"Income Tax: ${income_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}\n")

# Function to display totals for all employees
def display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay):
    print(f"\nTotal Number of Employees: {total_employees}")
    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Gross Pay: ${total_gross_pay:.2f}")
    print(f"Total Income Tax: ${total_tax:.2f}")
    print(f"Total Net Pay: ${total_net_pay:.2f}")

# Main loop to process employees
def main():
    total_employees = 0
    total_hours = 0
    total_gross_pay = 0
    total_tax = 0
    total_net_pay = 0

    while True:
        name = get_employee_name()
        if name.lower() == "end":
            break
        total_hours_worked = get_total_hours()
        hourly_rate = get_hourly_rate()
        tax_rate = get_income_tax_rate()

        gross_pay, income_tax, net_pay = calculate_pay(total_hours_worked, hourly_rate, tax_rate)

        display_employee_info(name, total_hours_worked, hourly_rate, gross_pay, tax_rate, income_tax, net_pay)

        # Accumulate totals
        total_employees += 1
        total_hours += total_hours_worked
        total_gross_pay += gross_pay
        total_tax += income_tax
        total_net_pay += net_pay

    # Display totals after loop ends
    display_totals(total_employees, total_hours, total_gross_pay, total_tax, total_net_pay)

if __name__ == "__main__":
    main()
