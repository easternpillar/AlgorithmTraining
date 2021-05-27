# Problem:
# Reference: https://www.acmicpc.net/problem/1110

# My Solution:
import sys

N = int(sys.stdin.readline().rstrip())
temp = N
cnt = 0
while True:
    a, b = divmod(temp, 10)
    temp = b * 10 + (a + b) % 10
    cnt += 1
    if temp == N:
        break
print(cnt)
