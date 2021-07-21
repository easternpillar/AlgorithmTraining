# Problem:
# Reference: https://www.acmicpc.net/problem/10866

# My Solution:
import sys
from collections import deque

dq = deque([])
for _ in range(int(sys.stdin.readline().rstrip())):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_back':
        dq.append(cmd[1])
    elif cmd[0] == 'push_front':
        dq.appendleft(cmd[1])
    elif cmd[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)
    elif cmd[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
