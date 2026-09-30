"""
RECORD CHECK  -  my version
===========================

Name  : Razvan 
Lane  : Cyber
Date  : 28/09/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

source_ip = input("Enter the source IP: ")
failed_logins = float(input("Enter failed logins: "))
total_attempts = float(input("Enter total attempts: "))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.


successful_logins = total_attempts - failed_logins
failed_percentage = (failed_logins / total_attempts) * 100

# This helps compare successful and failed login activity.
successful_percentage = (successful_logins / total_attempts) * 100


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {source_ip}")
print("=" * 34)

# : your report lines go here

print(f"  Failed logins : {failed_logins:>10.2f}")
print(f"  Total attempts: {total_attempts:>10.2f}")
print(f"  Successful    : {successful_logins:>+10.2f}")
print(f"  Failed rate   : {failed_percentage:>10.2f} %")
print(f"  Success rate  : {successful_percentage:>10.2f} %")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
