from NetSalary import compute_net_salary

def main():
    name = input("Enter your name: ")
    hours_worked = int(input("Enter hours worked: "))
    loan = float(input("Enter loan amount: "))
    health_insurance = float(input("Enter health insurance amount: "))
    
    compute_net_salary(name, hours_worked, loan, health_insurance)

if __name__ == "__main__":
    main()
