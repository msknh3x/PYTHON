current_savings = 50000.0
monthly_income = 3500.0
monthly_expenses = 20000.0
target_goal = 200000.0
inflation_rate = 0.003
months = 0

while current_savings < target_goal:
    monthly_expenses *= (1 + inflation_rate)
    net_savings = monthly_income - monthly_expenses
    current_savings += net_savings
    months += 1