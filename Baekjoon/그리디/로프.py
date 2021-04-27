# Problem:
# Reference: https://www.acmicpc.net/problem/2217

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
weights = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
weights.sort(reverse=True)

maxi = 0
for i in range(len(weights)):
    maxi = max(maxi, weights[i] * (i + 1))

print(maxi)
