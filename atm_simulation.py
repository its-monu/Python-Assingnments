balance = 5000

print("===== ATM SIMULATION =====")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("Your balance is:", balance)

elif choice == "2":
    amount = float(input("Enter deposit amount: "))
    balance = balance + amount
    print("Amount deposited successfully.")
    print("New balance:", balance)

elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Please collect your cash.")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance.")

elif choice == "4":
    print("Thank you for using ATM.")

else:
    print("Invalid choice.")
