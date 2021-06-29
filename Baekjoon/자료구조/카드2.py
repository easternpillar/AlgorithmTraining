# Problem:
# Reference: https://www.acmicpc.net/problem/2164

# My Solution:
import sys
from collections import deque

cards = [i for i in range(1,int(sys.stdin.readline().rstrip())+1)]
dq = deque(cards)
while True:
    if len(dq) == 1:
        print(dq[0])
        break
    dq.popleft()
    dq.append(dq.popleft())
