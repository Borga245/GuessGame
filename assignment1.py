from datetime import datetime

def get_dates():
    """Input and return the from date and to date for hours worked."""
    from_date = input("Enter the from date (mm/dd/yyyy): ")
    to_date = input("Enter the to date (mm/dd/yyyy): ")
    return from_date, to_date

def calculate_payroll(from_date, to_date, employees):
    """Calculate income tax and net pay for each employee and return totals."""
    totals = {'total_employees': 0, 'total_hours': 0, 'total_tax': 0, 'total_net_pay': 0}
    
    for employee in employees:
        name, hours, rate, tax_rate = employee
        gross_pay = hours * rate
        income_tax = gross_pay * tax_rate
        net_pay = gross_pay - income_tax
        
        print(f"\nFrom Date: {from_date} | To Date: {to_date}")
        print(f"Employee: {name} | Hours Worked: {hours} | Hourly Rate: ${rate:.2f}")
        print(f"Gross Pay: ${gross_pay:.2f} | Income Tax Rate: {tax_rate:.2%}")
        print(f"Income Tax: ${income_tax:.2f} | Net Pay: ${net_pay:.2f}\n")
        
        totals['total_employees'] += 1
        totals['total_hours'] += hours
        totals['total_tax'] += income_tax
        totals['total_net_pay'] += net_pay
        
    return totals

def display_totals(totals):
    """Display the total number of employees, total hours, total tax, and total net pay."""
    print("Totals:")
    print(f"Total Employees: {totals['total_employees']}")
    print(f"Total Hours: {totals['total_hours']}")
    print(f"Total Income Tax: ${totals['total_tax']:.2f}")
    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")

def main():
    employees = []
    
    while True:
        from_date, to_date = get_dates()
        name = input("Enter employee name: ")
        hours = float(input("Enter total hours worked: "))
        rate = float(input("Enter hourly rate: "))
        tax_rate = float(input("Enter income tax rate (e.g., 0.20 for 20%): "))
        
        employees.append([name, hours, rate, tax_rate])
        
        more_employees = input("Do you want to add another employee? (yes/no): ")
        if more_employees.lower() != 'yes':
            break
    
    totals = calculate_payroll(from_date, to_date, employees)
    display_totals(totals)

if __name__ == "__main__":
    main()
