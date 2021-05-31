# Problem:
# Reference: https://www.acmicpc.net/problem/20922

# My Solution:
import sys

N, K = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
counts = [0 for _ in range(100001)]
left = 0
right = -1
answer = 0

while True:
    right += 1

    if right == N:
        break

    counts[a[right]] += 1
    if counts[a[right]] > K:
        answer = max(answer, right - left)
        while counts[a[right]] > K:
            counts[a[left]] -= 1
            left += 1

answer = max(answer, N - left)
print(answer)
