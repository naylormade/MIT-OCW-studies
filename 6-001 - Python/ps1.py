total_months = 0

total_cost = 1000000.0  #float(input("Cost of dream home"))
annual_salary = 120000.0  #float(input("Starting annual salary?"))
portion_saved = .1  #float(input("Portion to save? (decimal)"))
current_savings = 0
portion_down_payment = 0.25

#annual_savings = annual_salary * portion_saved
#annual_returns = current_savings * 0.04/12.0

down_payment = total_cost * portion_down_payment

while current_savings < down_payment:
    annual_returns = current_savings * 0.04/12.0
    current_savings += annual_returns + ((annual_salary / 12) * portion_saved)
    total_months += 1

print(f'Number of months: {total_months}')
