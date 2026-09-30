"""
RECORD CHECK  -  my version
===========================

Name  : Razvan
Lane  : Cyber
Date  : 30/09/2026

Run it:   python template.py
"""

# Keep track of how many checks came back OVER LIMIT.
over_limit_count = 0

while True:
    # Input section
    label = input("Enter a label (or 'quit' to finish): ")
    if label.lower() == "quit":
        break

    value = float(input("Enter a value: "))
    limit = float(input("Enter a limit: "))

    # Process section
    difference = limit - value
    percentage_used = (value / limit * 100) if limit != 0 else 0.0
    percentage_left = (difference / limit * 100) if limit != 0 else 0.0

    if percentage_used >= 100:
        status = "OVER LIMIT"
    elif percentage_used >= 90:
        status = "WARNING"
    else:
        status = "OK"

    if status == "OVER LIMIT":
        over_limit_count += 1

    # Output section
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Value        : {value:>10.2f}")
    print(f"  Limit        : {limit:>10.2f}")
    print(f"  Difference   : {difference:>10.2f}")
    print(f"  Used         : {percentage_used:>9.2f} %")
    print(f"  Left         : {percentage_left:>9.2f} %")
    print(f"  Status       : {status:>10}")
    print("=" * 34)

print(f"\nRecords over limit this session: {over_limit_count}")
