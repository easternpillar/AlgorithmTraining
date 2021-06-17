# Problem:
# Reference: https://www.acmicpc.net/problem/18312

# My Solution:
import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0

for i in range(N + 1):
    for j in range(60):
        for k in range(60):
            if str(K) in str(i).rjust(2, '0') + str(j).rjust(2, '0') + str(k).rjust(2, '0'):
                cnt += 1

print(cnt)
