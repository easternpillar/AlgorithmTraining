# Reference: https://www.acmicpc.net/problem/14891
import sys
from collections import deque
from copy import deepcopy

chains = [deque(list(map(int, list(sys.stdin.readline().rstrip())))) for _ in range(4)]
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().rstrip()))]
answer = 0


def rotate(chains, directions):
    for i in range(4):
        if directions[i] == 1:
            chains[i].appendleft(chains[i].pop())
        elif directions[i] == -1:
            chains[i].append(chains[i].popleft())
    return chains


for command in commands:
    directions = [0, 0, 0, 0]
    num_chain, direction = command
    directions[num_chain - 1] = direction

    for i in range(num_chain - 2, -1, -1):
        if chains[i][2] == chains[i + 1][6]:
            break
        else:
            directions[i] = -directions[i + 1]
    for i in range(num_chain, 4, 1):
        if chains[i][6] == chains[i - 1][2]:
            break
        else:
            directions[i] = -directions[i - 1]
    chains = rotate(chains, directions)

for i in range(4):
    if chains[i][0] == 1:
        answer += (2 ** i)
print(answer)
