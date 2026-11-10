"""
RECORD CHECK - my version
Name: Razvan-Stefan Jipa
Lane: Cyber Security
Date: 10 November 2026
"""

from pathlib import Path


def parse_line(raw_line):
    """Clean a login record and return its source, attempts and result."""
    line = raw_line.strip().lower()
    fields = {}
    for piece in line.split(","):
        key, value = piece.split("=", 1)
        fields[key.strip()] = value.strip()
    return {
        "src": fields["src"],
        "attempts": int(fields["attempts"]),
        "result": fields["result"]
    }


def status_of(attempts, result):
    """Return FLAGGED for five or more failed attempts, otherwise OK."""
    if result == "failed" and attempts >= 5:
        return "FLAGGED"
    return "OK"


raw_records = []
with open(Path(__file__).with_name("cyber_records.txt"), "r") as file:
    for line in file:
        if line.strip():
            raw_records.append(line)


flagged_count = 0
for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["attempts"], record["result"])
    print(record, status)
    if status == "FLAGGED":
        flagged_count += 1

print(f"Records: {len(raw_records)}, flagged: {flagged_count}")
