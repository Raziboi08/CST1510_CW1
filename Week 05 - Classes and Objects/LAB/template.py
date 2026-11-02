"""
RECORD CHECK  -  my version
===========================

Name  : Razvan Jipa
Lane  : cyber security 
Date  : 02/11/2026

Run it: python template.py
"""

# ====================================================================== CLASS
# 1. Define a class called Record.

class Record:
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Store the record's label, value and limit."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status based on the percentage used."""
        percent = (self.value / self.limit) * 100

        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
# 2. Create your records.

def load_records(path):
    """Read a file and return a list of Record objects."""
    records = []

    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))

    return records

from pathlib import Path
records = load_records(Path(__file__).parent / "records_sample.txt")


# ==================================================================== OUTPUT
# 3. Print a report for each record.

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    status = record.status()

    print(f"  GB used:  {record.value}")
    print(f"  GB total: {record.limit}")
    print(f"  Status:   {status}")

    if status == "OVER LIMIT":
        Record.over_limit_count += 1

    print("=" * 34)

print(f"\n{Record.over_limit_count} of {len(records)} records are OVER LIMIT")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers by hand
#    [ ] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself
#    [ ] Check every method and __init__ has a one-line docstring