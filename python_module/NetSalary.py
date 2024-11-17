from GrossSalary import compute_gross_salary
from SalaryDeductions import compute_deductions

def compute_net_salary(name, hours_worked, loan, health_insurance):
    gross_salary = compute_gross_salary(hours_worked)
    
    tax, total_deductions = compute_deductions(gross_salary, loan, health_insurance)
    
    net_salary = gross_salary - total_deductions
    
    print(f"Name: {name}")
    print(f"Hour: {hours_worked}")
    print(f"Gross Salary: Php {gross_salary:.2f}")
    print(f"Tax: Php {tax:.2f}")
    print(f"Loan: Php {loan:.2f}")
    print(f"Insurance: Php {health_insurance:.2f}")
    print(f"Total Deductions: Php {total_deductions:.2f}")
    print(f"Net Salary: Php {net_salary:.2f}")
