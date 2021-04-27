# Problem:
# Given 3 and 5 units, print the minimum usages to make N.

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
kgs = [-1 for _ in range(5001)]
kgs[3] = 1
kgs[5] = 1
for i in range(5, 5001, 1):
    if kgs[i - 3] != -1:
        kgs[i] = kgs[i - 3] + 1
    if kgs[i - 5] != -1:
        if kgs[i] == -1 or kgs[i - 5] + 1 < kgs[i]:
            kgs[i] = kgs[i - 5] + 1
print(kgs[N])
