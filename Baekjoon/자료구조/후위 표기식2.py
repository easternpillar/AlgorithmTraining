# Problem:
# Reference: https://www.acmicpc.net/problem/1935

# My Solution:
import sys
from collections import deque, defaultdict

n = int(sys.stdin.readline().rstrip())
temp = list(sys.stdin.readline().rstrip())
stack = []
alpha = defaultdict(int)
for i in range(n):
    alpha[chr(ord('A') + i)] = int(sys.stdin.readline().rstrip())

q = deque(temp)
while q:
    pop = q.popleft()
    if pop.isalpha():
        stack.append(alpha[pop])
        continue
    else:
        o1 = stack.pop()
        o2 = stack.pop()

        if pop == '+':
            stack.append(o1 + o2)
        elif pop == '-':
            stack.append(o2 - o1)
        elif pop == '*':
            stack.append(o1 * o2)
        elif pop == '/':
            stack.append(o2 / o1)

print("%.2f" % stack[0])
