# Problem:
# Given a change amount, print out the minimum number of coins.
# Condition(s):
# 1. Coins are only 2 and 5 units.

# My Solution:
import sys

changes = [0 for _ in range(100001)]
changes[2] = 1
changes[4] = 2
changes[5] = 1
target = int(sys.stdin.readline().rstrip())
for i in range(6, 100001):
    if changes[i - 5] != 0 and changes[i - 2] != 0:
        changes[i] = min(changes[i - 5] + 1, changes[i - 2] + 1)
    elif changes[i - 5] != 0:
        changes[i] = changes[i - 5] + 1
    elif changes[i - 2] != 0:
        changes[i] = changes[i - 2] + 1
if changes[target] == 0:
    print(-1)
else:
    print(changes[target])

# Other Solution:
import sys

changes = int(sys.stdin.readline().rstrip())
fives = 0
twos = 0
fives, changes = divmod(changes, 5)
flag = True
while changes % 2 != 0:
    fives -= 1
    changes += 5
    if fives < 0:
        flag = False
        break
if flag:
    twos = changes // 2
    print(fives + twos)
else:
    print(-1)
