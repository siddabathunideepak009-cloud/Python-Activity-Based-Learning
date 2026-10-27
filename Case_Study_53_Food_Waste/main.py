try:
    days = int(input("Enter number of days: "))
    threshold = float(input("Enter acceptable wastage percentage: "))

    if days <= 0 or threshold < 0:
        raise ValueError

except ValueError:
    print("Enter a positive number of days and a non-negative threshold.")
    exit()

total_prepared = 0
total_served = 0
total_leftovers = 0

for day in range(1, days + 1):
    print(f"\n----- DAY {day} -----")

    try:
        prepared = int(input("Meals prepared: "))
        served = int(input("Meals served: "))

        if prepared <= 0 or served < 0 or served > prepared:
            raise ValueError

    except ValueError:
        print("Invalid input. Prepared meals must be positive, and served meals must be between 0 and prepared meals.")
        continue

    leftovers = prepared - served
    wastage_percentage = (leftovers / prepared) * 100

    total_prepared += prepared
    total_served += served
    total_leftovers += leftovers

    print("Meals prepared:", prepared)
    print("Meals served:", served)
    print("Leftover meals:", leftovers)
    print(f"Wastage percentage: {wastage_percentage:.2f}%")

    if wastage_percentage > threshold:
        print("Warning: Wastage exceeds the acceptable threshold.")
    else:
        print("Wastage is within the acceptable threshold.")

print("\n===== FOOD WASTE SUMMARY =====")
print("Total meals prepared:", total_prepared)
print("Total meals served:", total_served)
print("Total leftover meals:", total_leftovers)

if total_prepared > 0:
    overall_wastage = (total_leftovers / total_prepared) * 100
    print(f"Overall wastage percentage: {overall_wastage:.2f}%")
else:
    print("No valid days were recorded.")