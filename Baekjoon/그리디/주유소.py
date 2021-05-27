# Problem:
# Reference: https://www.acmicpc.net/problem/13305

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
roads = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

tot = 0
amount = roads[0]
cur_price = prices[0]
for i in range(1, len(roads)):
    if prices[i] < cur_price:
        tot += cur_price * amount
        cur_price = prices[i]
        amount = 0
    amount += roads[i]

if amount:
    tot += cur_price * amount

print(tot)
