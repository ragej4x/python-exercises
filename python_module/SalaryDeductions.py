def compute_deductions(gross_salary, loan, health_insurance):
    #tax rate
    tax = gross_salary * 0.12 #
    total_deductions = tax + loan + health_insurance
    return tax, total_deductions
