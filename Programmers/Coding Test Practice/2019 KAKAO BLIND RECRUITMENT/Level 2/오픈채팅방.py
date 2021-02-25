# Problem:
# Given a sequence of the Chatting room logs, return the print messages.
# Condition(s):
# 1. Messages of the same user should be changed if the user change the name.

# My Solution:
from collections import deque


def solution(record):
    answer = []
    result = []
    q = deque(record)
    d = {}
    while q:
        pop = q.popleft()
        pop = pop.split()
        if pop[0] == 'Enter':
            d[pop[1]] = pop[2]
            result.append((pop[1], 0))
        elif pop[0] == 'Leave':
            result.append((pop[1], 1))
        else:
            d[pop[1]] = pop[2]

    for r in result:
        if r[1] == 0:
            answer.append(d[r[0]] + '님이 들어왔습니다.')
        else:
            answer.append(d[r[0]] + '님이 나갔습니다.')
    return answer
