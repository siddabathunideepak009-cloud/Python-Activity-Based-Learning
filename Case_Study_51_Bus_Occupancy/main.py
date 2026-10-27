capacity = int(input("Bus capacity: "))
stops = int(input("Number of stops: "))

if capacity <= 0 or stops < 0:
    print("Capacity must be positive and stops cannot be negative.")
else:
    passengers = 0
    maximum_occupancy = 0
    violations = 0

    for stop in range(1, stops + 1):
        print("\\nStop", stop)
        boarding = int(input("Passengers boarding: "))
        alighting = int(input("Passengers alighting: "))

        if boarding < 0 or alighting < 0:
            print("Invalid: passenger counts cannot be negative. Stop skipped.")
            continue
        if alighting > passengers:
            print("Invalid: more passengers cannot alight than are on the bus.")
            continue

        passengers = passengers - alighting + boarding
        maximum_occupancy = max(maximum_occupancy, passengers)
        print("Passengers on bus:", passengers)

        if passengers > capacity:
            print("CAPACITY VIOLATION!")
            violations += 1
        else:
            print("Occupancy within capacity.")

    print("\\n----- BUS SUMMARY -----")
    print("Final passengers:", passengers)
    print("Maximum occupancy:", maximum_occupancy)
    print("Capacity violations:", violations)
