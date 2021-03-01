# Problem:
# When January 1, 2016 is Friday, print the day of the week on a specific date in 2016.
# Condition(s):
# 1. It is a leap year.
# 2. Print from 0 to 6 from Monday to Sunday.

# My Solution:
T = int(input())
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(T):
    m, d = map(int, input().split())
    print("#{}".format(i + 1), end=" ")
    p = sum(days[:m + 1])
    p -= days[m] - d + 1
    p %= 7

    print((4 + p) % 7)
