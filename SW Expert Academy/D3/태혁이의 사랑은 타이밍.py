# Problem:
# Print the difference between 11:11 on the 11th and the given date.
# Condition(s):
# If the difference between the dates is negative, print -1.

# My Solution:
T = int(input())

for i in range(T):
    D, H, M = map(int, input().split())

    dd = D - 11
    hd = H - 11
    md = M - 11
    if md < 0:
        md += 60
        hd -= 1
    if hd < 0:
        dd -= 1
        hd += 24

    answer = dd * 60 * 24 + hd * 60 + md
    if answer >= 0:
        print("#{} {}".format(i + 1, answer))
    else:
        print("#{} {}".format(i + 1, -1))
