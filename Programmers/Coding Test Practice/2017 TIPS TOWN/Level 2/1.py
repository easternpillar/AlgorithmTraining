# Problem:
# Given a string, return whether the pairing can be performed successfully.

# My Solution:
from collections import deque


def solution(s):
    answer = 0
    q = deque(s)
    tq = deque()
    while True:
        temp = len(q)
        while q:
            pop = q.popleft()
            if not tq:
                tq.append(pop)
                continue
            else:
                tpop = tq.pop()
                if pop == tpop:
                    continue
                else:
                    tq.append(tpop)
                    tq.append(pop)

        if not tq:
            return 1
        else:
            if temp == len(tq):
                return 0
            q, tq = tq, q
    return answer
