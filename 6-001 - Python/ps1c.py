total_cost = 1000000.0  #float(input("Cost of dream home"))
starting_salary = 150000.0  #float(input("Starting salary?"))
#portion_saved = .05  #float(input("Portion to save? (decimal)"))
semi_annual_raise = .07  #float(input("What is your semi-annual raise percentage? (decimal)"))
annual_return = .04
current_savings = 0
portion_down_payment = 0.25

epsilon = 0.01
steps = 0

x = total_cost
low = 0.0
high = max(1.0, x)

ans = (high + low) / 2.0

while abs(ans**2 - x) >= 100 and steps < 10000:
    steps += 1
    if steps > 9998:
        print("It is not possible.")
        break
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0

print(f'starting salary: {starting_salary}')
print(f'Best rate: {ans}')
print(f'Steps: {steps}')