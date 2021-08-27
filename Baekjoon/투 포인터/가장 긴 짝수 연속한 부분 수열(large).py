# Problem:
# Reference: https://www.acmicpc.net/problem/22862

# My Solution:
import sys

N, K = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

left = 0
right = 0
odds = 0
evens = 0
answer = 0

while left <= right < N:
    if seq[right] % 2 == 0:
        evens += 1
        right += 1
        continue
    else:
        odds += 1
        right += 1
        if odds > K:
            answer = max(answer, evens)
            while seq[left] % 2 != 1:
                evens -= 1
                left += 1
            left += 1
            odds -= 1

answer = max(answer, evens)
print(answer)
