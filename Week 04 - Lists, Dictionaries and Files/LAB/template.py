"""
RECORD CHECK  -  my version
===========================

Name  : Raz
Lane  : cyber security 
Date  : 2/11/26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

def check_record(value, limit):
    """Calculate the difference, percentage and status."""
    difference = value - limit
    percent = value / limit * 100
    status = "OVER LIMIT" if value > limit else "OK"
    return difference, percent, status


def print_report(label, difference=None, percent=None, status=None):
    """Print a record report or a message."""
    if difference is None:
        print(label)
    else:
        print(f"{label}: difference {difference}, {percent:.1f}%, {status}")


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

def load_records(path):
    """Load records from a comma-separated file."""
    records = []
    with open(path) as file:
        for line in file:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit)
            })
    return records


try:
    records = load_records("records_sample.txt")
except FileNotFoundError:
    records = []
    print_report("records_sample.txt not found")


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

over_limit_count = 0

with open("results.txt", "w") as results_file:
    for record in records:
        difference, percent, status = check_record(
            record["value"], record["limit"]
        )
        print_report(record["label"], difference, percent, status)
        results_file.write(f'{record["label"]},{status}\n')

        if status == "OVER LIMIT":
            over_limit_count += 1

print_report(f"OVER LIMIT count: {over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job