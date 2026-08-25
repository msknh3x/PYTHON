def deposit(balance, amount):
    return balance + amount 

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount 
    else:
        print("Insufficient funds!")
        return balance

def check_balance(balance):
    print("Current Balance:", balance)

balance = 10000
balance = deposit(balance, 2000)
balance = withdraw(balance, 5000)
check_balance(balance)