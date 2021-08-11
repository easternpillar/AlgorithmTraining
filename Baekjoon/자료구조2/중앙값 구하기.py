# Problem:
# Reference: https://www.acmicpc.net/problem/2696

# My Solution:
import sys
import bisect
from collections import deque


for _ in range(int(sys.stdin.readline().rstrip())):
    M = int(sys.stdin.readline().rstrip())
    nums = []
    for i in range(M // 10 + 1):
        nums.extend(list(map(int, sys.stdin.readline().split())))
    q = deque(nums)
    seq = []
    cnt = 0
    answer = []
    while q:
        add = q.popleft()
        cnt += 1
        seq.insert(bisect.bisect_left(seq, add), add)
        if cnt % 2 == 1:
            answer.append(seq[len(seq) // 2])
    print(len(answer))
    for i in range(len(answer) // 10 + 1):
        print(*answer[i * 10:i * 10 + 10])
