# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

import re


def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status
print(check(23.7, 20))