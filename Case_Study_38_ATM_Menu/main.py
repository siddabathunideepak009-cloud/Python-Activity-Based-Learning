try:
    balance = float(input("Opening balance (Rs.): "))
    if balance < 0:
        raise ValueError
except ValueError:
    print("Invalid opening balance. Enter a non-negative number.")
    exit()

deposit_total = 0.0
withdrawal_total = 0.0
deposit_count = 0
withdrawal_count = 0
withdrawal_limit = 10000

while True:
    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance inquiry")
    print("4. Transaction summary")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        try:
            amount = float(input("Deposit amount: Rs. "))
        except ValueError:
            print("Invalid amount. Enter a number.")
            continue

        if amount <= 0:
            print("Amount must be positive.")
        else:
            balance += amount
            deposit_total += amount
            deposit_count += 1
            print(f"Deposit successful. Balance: Rs. {balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Withdrawal amount: Rs. "))
        except ValueError:
            print("Invalid amount. Enter a number.")
            continue

        if amount <= 0:
            print("Amount must be positive.")
        elif amount > balance:
            print("Insufficient balance.")
        elif amount > withdrawal_limit:
            print("Per-transaction withdrawal limit exceeded.")
        else:
            balance -= amount
            withdrawal_total += amount
            withdrawal_count += 1
            print(f"Withdrawal successful. Balance: Rs. {balance:.2f}")

    elif choice == "3":
        print(f"Current balance: Rs. {balance:.2f}")

    elif choice == "4":
        print("\n----- TRANSACTION SUMMARY -----")
        print(f"Deposits: {deposit_count}, total Rs. {deposit_total:.2f}")
        print(f"Withdrawals: {withdrawal_count}, total Rs. {withdrawal_total:.2f}")
        print(f"Current balance: Rs. {balance:.2f}")

    elif choice == "5":
        print("Thank you for using the ATM simulation.")
        break

    else:
        print("Invalid menu option. Choose 1 to 5.")