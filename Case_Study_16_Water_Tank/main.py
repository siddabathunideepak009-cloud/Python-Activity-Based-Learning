capacity = float(input("Tank capacity (litres): "))
level = float(input("Initial water level (litres): "))
threshold = float(input("Target threshold (litres): "))
n = int(input("Number of intervals: "))

if capacity <= 0 or not (0 <= level <= capacity) or not (0 <= threshold <= capacity) or n < 0:
    print("Invalid capacity, level, threshold, or interval count.")
else:
    first_threshold = None
    total_overflow = 0.0
    shortage_intervals = 0

    for i in range(1, n + 1):
        print("\\nInterval", i)
        inflow = float(input("Inflow (litres): "))
        outflow = float(input("Outflow (litres): "))

        if inflow < 0 or outflow < 0:
            print("Negative quantities are invalid; interval skipped.")
            continue

        level += inflow
        overflow = max(0, level - capacity)
        if overflow > 0:
            total_overflow += overflow
            level = capacity

        if outflow > level:
            shortage = outflow - level
            shortage_intervals += 1
            level = 0
        else:
            shortage = 0
            level -= outflow

        print(f"Overflow: {overflow:.2f} L")
        print(f"Shortage: {shortage:.2f} L")
        print(f"Water level: {level:.2f} L")

        if level >= threshold and first_threshold is None:
            first_threshold = i

    print("\\n----- TANK SUMMARY -----")
    print(f"Final water level: {level:.2f} L")
    print(f"Total overflow: {total_overflow:.2f} L")
    print(f"Intervals with shortage: {shortage_intervals}")
    if first_threshold is None:
        print("Threshold was not reached after an interval.")
    else:
        print(f"First interval reaching threshold: {first_threshold}")

