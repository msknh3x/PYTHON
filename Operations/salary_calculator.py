basic_salary = 50000
bonus = 5000
tax_rate = 0.1 # 10%

gross_salary = basic_salary + bonus 
tax_amount = gross_salary * tax_rate
net_salary = gross_salary - tax_amount

if net_salary > 40000:
    status = "Good Salary"
else:
    status = "Needs Improvement"

eligible_for_loan = net_salary > 30000 and status == "Good Slaray"

print("Gross Salary:", gross_salary)
print("Tax Amount:", tax_amount)
print("Net Salary:", net_salary)
print("Status", status)
print("Eligible for loan?", eligible_for_loan)
