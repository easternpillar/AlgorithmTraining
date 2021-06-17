# Problem:
# Reference: https://www.acmicpc.net/problem/21921

# My Solution:
import sys

N, X = map(int, sys.stdin.readline().split())
visits = list(map(int, sys.stdin.readline().split()))
tot = sum(visits[:X])
cnt = 1
maxi = tot
l = 0
r = l + X - 1

while l <= r < len(visits) - 1:
    tot -= visits[l]
    l += 1
    r += 1
    tot += visits[r]

    if tot > maxi:
        maxi = tot
        cnt = 1
    elif tot == maxi:
        cnt += 1

if maxi == 0:
    print("SAD")
else:
    print(maxi)
    print(cnt)
