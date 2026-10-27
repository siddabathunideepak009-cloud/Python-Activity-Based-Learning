try:
    product_count = int(input("Number of products: "))
    threshold = float(input("Overall change threshold (%): "))

    if product_count <= 0 or threshold < 0:
        raise ValueError

except ValueError:
    print("Enter a positive product count and a non-negative threshold.")
    exit()

results = []

for _ in range(product_count):
    print("\nProduct details")
    name = input("Product name: ").strip()
    prices_text = input("Historical prices separated by spaces: ").strip()

    try:
        prices = [float(value) for value in prices_text.split()]
    except ValueError:
        print("Invalid price list; product skipped.")
        continue

    if (
        len(prices) < 2
        or any(price < 0 for price in prices)
        or prices[0] == 0
    ):
        print("Need at least two non-negative prices and a non-zero first price.")
        continue

    overall_change = (prices[-1] - prices[0]) / prices[0] * 100
    consecutive_changes = []

    for i in range(1, len(prices)):
        previous_price = prices[i - 1]
        current_price = prices[i]

        if previous_price > 0:
            change = abs(
                (current_price - previous_price) / previous_price * 100
            )
            consecutive_changes.append(change)

    max_fluctuation = max(consecutive_changes) if consecutive_changes else 0
    flagged = abs(overall_change) > threshold

    print(f"Overall price change: {overall_change:.2f}%")
    print(f"Largest consecutive fluctuation: {max_fluctuation:.2f}%")
    print("Threshold exceeded:", "Yes" if flagged else "No")

    results.append((name, overall_change, max_fluctuation, flagged))

print("\n----- PRICE ANALYSIS SUMMARY -----")

if results:
    biggest = max(results, key=lambda item: abs(item[1]))
    print(
        f"Largest absolute overall change: "
        f"{biggest[0]} ({biggest[1]:.2f}%)"
    )

    print("Products exceeding threshold:")
    flagged_products = [item[0] for item in results if item[3]]

    if flagged_products:
        for product in flagged_products:
            print("-", product)
    else:
        print("None")
else:
    print("No valid products to analyze.")