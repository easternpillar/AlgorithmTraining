# Problem:
# Reference: https://www.acmicpc.net/problem/11508

# My Solution:
import sys

costs = []
for _ in range(int(sys.stdin.readline().rstrip())):
    costs.append(int(sys.stdin.readline().rstrip()))
costs.sort(reverse=True)

tot = 0
q, r = divmod(len(costs), 3)
for i in range(q):
    tot += costs[3 * i]
    tot += costs[3 * i + 1]

for i in range(len(costs) - 3 * q):
    tot += costs[3 * q + i]

print(tot)
