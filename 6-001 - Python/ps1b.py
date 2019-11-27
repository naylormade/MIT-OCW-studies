total_months = 0

total_cost = 500000.0  #float(input("Cost of dream home"))
annual_salary = 120000.0  #float(input("Starting annual salary?"))
portion_saved = .05  #float(input("Portion to save? (decimal)"))
semi_annual_raise = .03  #float(input("What is your semi-annual raise percentage? (decimal)"))
current_savings = 0
portion_down_payment = 0.25

#annual_savings = annual_salary * portion_saved
#annual_returns = current_savings * 0.04/12.0

down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    annual_returns = current_savings * 0.04/12.0
    current_savings += annual_returns + ((annual_salary / 12) * portion_saved)
    total_months += 1
    if total_months % 6 == 0:
        annual_salary *= (1 + semi_annual_raise)

print(f'Number of months: {total_months}')
