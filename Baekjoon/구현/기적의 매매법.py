# Problem:
# Reference: https://www.acmicpc.net/problem/20546

# My Solution:
import sys


def bnp(cash):
    stocks = 0
    for i in range(14):
        if cash == 0:
            break
        add = cash // prices[i]
        stocks += add
        cash -= add * prices[i]

    return cash + stocks * prices[-1]


def timing(cash):
    stocks = 0
    for i in range(3, 14):
        up = 0
        down = 0
        for j in range(i - 2, i + 1):
            if prices[j] > prices[j - 1]:
                up += 1
            elif prices[j] < prices[j - 1]:
                down += 1
        if up == 3:
            cash += stocks * prices[i]
            stocks = 0

        elif down == 3:
            add = cash // prices[i]
            stocks += add
            cash -= add * prices[i]

    return cash + stocks * prices[-1]


cash1 = cash2 = int(sys.stdin.readline().rstrip())
prices = list(map(int, sys.stdin.readline().split()))
assets1 = bnp(cash1)
assets2 = timing(cash2)
if assets1 > assets2:
    print("BNP")
elif assets1 < assets2:
    print("TIMING")
else:
    print("SAMESAME")
