from datetime import datetime
from math import ceil

rates = {"BIKE": 20, "CAR": 50, "BUS": 100}
daily_caps = {"BIKE": 150, "CAR": 400, "BUS": 800}
penalty = 200

vehicle = input("Vehicle type (BIKE/CAR/BUS): ").strip().upper()
entry_text = input("Entry time (HH:MM): ").strip()
exit_text = input("Exit time (HH:MM): ").strip()

try:
    entry = datetime.strptime(entry_text, "%H:%M")
    exit_time = datetime.strptime(exit_text, "%H:%M")
    if vehicle not in rates:
        raise ValueError("Unknown vehicle type")

    start = entry.hour * 60 + entry.minute
    end = exit_time.hour * 60 + exit_time.minute
    if end < start:
        end += 24 * 60

    duration = end - start
    charged_hours = ceil(duration / 60)
    fee = min(charged_hours * rates[vehicle], daily_caps[vehicle])

    print("\\n----- PARKING RECEIPT -----")
    print("Vehicle:", vehicle)
    print(f"Duration: {duration // 60} hour(s) {duration % 60} minute(s)")
    print("Charged hours:", charged_hours)
    print(f"Parking fee: Rs. {fee:.2f}")
except ValueError:
    print("Invalid input. Use a supported vehicle and time in HH:MM format.")

