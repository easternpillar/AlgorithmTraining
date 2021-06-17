# Problem:
# Print 1 if it is a leap year, or 0 otherwise.

# My Solution:
import sys

year = int(sys.stdin.readline().rstrip())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)
