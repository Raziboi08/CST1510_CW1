"""
RECORD CHECK - my version
===========================

Name : Razvan Jipa
Lane : Cyber
Date : 12/10/2026

Run it: python template.py
"""

# =================================================================== FUNCTIONS

def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage of failed logins."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a bordered report for one source IP."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {label}")
    print("=" * 34)
    print(f"  Failed logins : {value:>10.2f}")
    print(f"  Total attempts: {limit:>10.2f}")
    print(f"  Difference    : {difference:>10.2f}")
    print(f"  Percent       : {percent:>10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 34)


def print_summary(count):
    """Print the total number of records marked OVER LIMIT."""
    print(f"\nRecords OVER LIMIT: {count}")


# ==================================================================== INPUT

over_limit_count = 0

while True:
    label = input("Enter source IP (or quit to stop): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter failed logins: "))
    limit = float(input("Enter total attempts: "))

    # ================================================================ PROCESS

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # ================================================================= OUTPUT

    print_report(label, value, limit, difference, percent, status)

print_summary(over_limit_count)