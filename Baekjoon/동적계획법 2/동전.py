# Problem:
# Given the units of coins to use and the amount to make, print the number of cases to make the amount.

# My Solution:
import sys

T = int(sys.stdin.readline().rstrip())
for i in range(T):
    N = int(sys.stdin.readline().rstrip())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().rstrip())
    amount = [0 for _ in range(M + 1)]
    amount[0] = 1
    for c in coins:
        for j in range(len(amount)):
            if j - c >= 0:
                amount[j] += amount[j - c]
    print(amount[M])
