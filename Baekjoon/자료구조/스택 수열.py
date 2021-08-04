# Problem:
# Reference: https://www.acmicpc.net/problem/1874

# My Solution:
import sys


def solution():
    next = 1
    global answer
    for _ in range(n):
        num = int(sys.stdin.readline().rstrip())
        if not stack:
            stack.append(next)
            answer.append('+')
            next += 1
        while stack[-1] != num:
            stack.append(next)
            answer.append('+')
            next += 1
            if next > n+1:
                answer = ['NO']
                return
        stack.pop()
        answer.append('-')


stack = []
answer = []
n = int(sys.stdin.readline().rstrip())
solution()
for a in answer:
    print(a)
