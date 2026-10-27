rates = {"USD": 83.0, "EUR": 90.0, "GBP": 105.0}
budget = float(input("Enter travel budget in INR: "))
fee_rate = float(input("Enter conversion fee percentage: "))
n = int(input("Number of expenses: "))
total = 0.0
category_totals = {}

for i in range(n):
    print("\\nExpense", i + 1)
    category = input("Category: ").strip().title()
    currency = input("Currency (USD/EUR/GBP): ").strip().upper()
    amount = float(input("Amount in foreign currency: "))

    if amount < 0 or currency not in rates:
        print("Invalid amount or unsupported currency; expense skipped.")
        continue

    converted = amount * rates[currency]
    fee = converted * fee_rate / 100
    cost = converted + fee
    total += cost
    category_totals[category] = category_totals.get(category, 0) + cost
    print(f"Converted: INR {converted:.2f}")
    print(f"Fee: INR {fee:.2f}")
    print(f"Expense total: INR {cost:.2f}")

print("\\n----- TRAVEL SUMMARY -----")
print(f"Total spending: INR {total:.2f}")
if total > budget:
    print(f"Over budget by: INR {total - budget:.2f}")
else:
    print(f"Budget remaining: INR {budget - total:.2f}")

if category_totals:
    largest = max(category_totals, key=category_totals.get)
    print(f"Largest expense category: {largest} (INR {category_totals[largest]:.2f})")
else:
    print("No valid expenses were entered.")