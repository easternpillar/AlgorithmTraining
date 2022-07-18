# Reference: https://www.acmicpc.net/problem/13458
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())
cnt = 0
for num in nums:
    temp = num - B
    cnt += 1
    if temp < 0:
        continue
    if temp % C == 0:
        cnt += temp // C
    else:
        cnt += temp // C + 1

print(cnt)
