balance = float(input("Opening balance: "))
withdrawal_limit = float(input("Maximum withdrawal per transaction: "))
n = int(input("Number of transactions: "))
successful = 0
rejected = 0

for i in range(n):
    print("\\nTransaction", i + 1)
    kind = input("Type (D for deposit, W for withdrawal): ").strip().upper()
    amount = float(input("Amount: "))

    if amount <= 0:
        print("Rejected: amount must be positive.")
        rejected += 1
    elif kind == "D":
        balance += amount
        successful += 1
        print(f"Deposit successful. Balance: {balance:.2f}")
    elif kind == "W":
        if amount > balance:
            print("Rejected: insufficient balance.")
            rejected += 1
        elif amount > withdrawal_limit:
            print("Rejected: withdrawal limit exceeded.")
            rejected += 1
        else:
            balance -= amount
            successful += 1
            print(f"Withdrawal successful. Balance: {balance:.2f}")
    else:
        print("Rejected: invalid transaction type.")
        rejected += 1

print("\\n----- TRANSACTION SUMMARY -----")
print(f"Final balance: {balance:.2f}")
print(f"Successful transactions: {successful}")
print(f"Rejected transactions: {rejected}")

