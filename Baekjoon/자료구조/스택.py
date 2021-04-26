# Problem:
# Reference: https://www.acmicpc.net/problem/10828

# My Solution:
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
stack = []

command = []
for _ in range(N):
    command.extend(sys.stdin.readline().split())

q = deque(command)
while q:
    c = q.popleft()
    if c == 'push':
        stack.append(q.popleft())
    elif c == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif c == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    elif c == 'size':
        print(len(stack))
    elif c == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
