# Problem:
# Reference: https://www.acmicpc.net/problem/11279

# My Solution:
import heapq
import sys

N = int(sys.stdin.readline().rstrip())
hq = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x > 0:
        heapq.heappush(hq, (-x, x))
    else:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
