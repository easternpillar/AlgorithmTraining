# Problem:
# Reference: https://www.acmicpc.net/problem/1654

# My Solution:
import sys

K, N = map(int, sys.stdin.readline().split())
lans = [int(sys.stdin.readline().rstrip()) for _ in range(K)]

left, right = 1, max(lans)
answer = -1
flag = False
while True:
    mid = (left + right) // 2

    if left > right:
        print(mid)
        break

    temp = 0
    for lan in lans:
        temp += lan // mid

    if temp >= N:
        left = mid + 1
    else:
        right = mid - 1
