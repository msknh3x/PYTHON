balance = 10000

print("Welcome to ATM")
choice = int(input("Enter 1 for Withdraw, 2 for Deposit: "))

if choice == 1:
    amount = int(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful! New Balance: ", balance)
    else:
        print("Insufficient funds!")
elif choice == 2:
    amount = int(input("Enter amount to deposit:"))
    balance += amount
    print("'Deposit successful! New balance:", balance)
else:
    print("Invalid choice")

    