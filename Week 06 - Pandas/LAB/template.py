"""Record Check — Week 6
Name: Razvan-Stefan Jipa
Lane: Cyber Security
Date: 10 November 2026
Run: python template.py

"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

folder = Path(__file__).resolve().parent
df = pd.read_csv(folder / "cyber_records.csv")


df["percent"] = (df["failed_logins"] / df["total_attempts"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

print("All login records:")
print(df)
print("\nRecords that are not OK:")
print(df[df["status"] != "OK"])

status_counts = df.groupby("status").size()
print("\nCount per status:")
print(status_counts)
df.to_csv(folder / "cyber_report.csv", index=False)

status_counts.plot(kind="bar", color=["seagreen", "tomato", "orange"])
plt.title("Login records by status")
plt.xlabel("Status")
plt.ylabel("Number of records")
plt.xticks(rotation=0)
plt.yticks(range(int(status_counts.max()) + 1))
plt.tight_layout()
plt.savefig(folder / "cyber_status_counts.png")
plt.close()

