# Problem:
# Given a 2048 game case, return the maximum value of blocks.
# Condition(s):
# 1. 5 times can be moved at most.

# My Solution:
import copy
from _collections import deque


def up(block):
    b = copy.deepcopy(block)
    used = []
    for i in range(1, len(b)):
        for j in range(len(b)):
            if b[i][j] != 0:
                temp_i = i
                temp = b[i][j]
                b[i][j] = 0
                while temp_i > 0 and b[temp_i - 1][j] == 0:
                    temp_i -= 1
                b[temp_i][j] = temp

    for i in range(len(b) - 1):
        for j in range(len(b)):
            if b[i][j] == b[i + 1][j] and [i, j] not in used:
                b[i][j] *= 2
                b[i + 1][j] = 0
                used.append([i, j])

    for i in range(1, len(b)):
        for j in range(len(b)):
            if b[i][j] != 0:
                temp_i = i
                temp = b[i][j]
                b[i][j] = 0
                while temp_i > 0 and b[temp_i - 1][j] == 0:
                    temp_i -= 1
                b[temp_i][j] = temp

    m = 0
    for i in range(len(b)):
        if max(b[i]) > m:
            m = max(b[i])

    return b, m


def down(block):
    b = copy.deepcopy(block)
    used = []

    for i in range(len(b) - 2, -1, -1):
        for j in range(len(b)):
            if b[i][j] != 0:
                temp_i = i
                temp = b[i][j]
                b[i][j] = 0
                while temp_i < len(b) - 1 and b[temp_i + 1][j] == 0:
                    temp_i += 1
                b[temp_i][j] = temp

    for i in range(len(b) - 1, 0, -1):
        for j in range(len(b)):
            if b[i][j] == b[i - 1][j] and [i, j] not in used:
                b[i][j] *= 2
                b[i - 1][j] = 0
                used.append([i, j])

    for i in range(len(b) - 2, -1, -1):
        for j in range(len(b)):
            if b[i][j] != 0:
                temp_i = i
                temp = b[i][j]
                b[i][j] = 0
                while temp_i < len(b) - 1 and b[temp_i + 1][j] == 0:
                    temp_i += 1
                b[temp_i][j] = temp

    m = 0
    for i in range(len(b)):
        if max(b[i]) > m:
            m = max(b[i])

    return b, m


def left(block):
    b = copy.deepcopy(block)
    used = []
    for j in range(1, len(b)):
        for i in range(len(b)):
            if b[i][j] != 0:
                temp_j = j
                temp = b[i][j]
                b[i][j] = 0
                while temp_j > 0 and b[i][temp_j - 1] == 0:
                    temp_j -= 1
                b[i][temp_j] = temp

    for j in range(len(b) - 1):
        for i in range(len(b)):
            if b[i][j] == b[i][j + 1] and [i, j] not in used:
                b[i][j] *= 2
                b[i][j + 1] = 0
                used.append([i, j])

    for j in range(1, len(b)):
        for i in range(len(b)):
            if b[i][j] != 0:
                temp_j = j
                temp = b[i][j]
                b[i][j] = 0
                while temp_j > 0 and b[i][temp_j - 1] == 0:
                    temp_j -= 1
                b[i][temp_j] = temp

    m = 0
    for i in range(len(b)):
        if max(b[i]) > m:
            m = max(b[i])

    return b, m


def right(block):
    b = copy.deepcopy(block)
    used = []

    for j in range(len(b) - 2, -1, -1):
        for i in range(len(b)):
            if b[i][j] != 0:
                temp_j = j
                temp = b[i][j]
                b[i][j] = 0
                while temp_j < len(b) - 1 and b[i][temp_j + 1] == 0:
                    temp_j += 1
                b[i][temp_j] = temp

    for j in range(len(b) - 1, 0, -1):
        for i in range(len(b)):
            if b[i][j] == b[i][j - 1] and [i, j] not in used:
                b[i][j] *= 2
                b[i][j - 1] = 0
                used.append([i, j])

    for j in range(len(b) - 2, -1, -1):
        for i in range(len(b)):
            if b[i][j] != 0:
                temp_j = j
                temp = b[i][j]
                b[i][j] = 0
                while temp_j < len(b) - 1 and b[i][temp_j + 1] == 0:
                    temp_j += 1
                b[i][temp_j] = temp

    m = 0
    for i in range(len(b)):
        if max(b[i]) > m:
            m = max(b[i])

    return b, m


n = int(input())

li = []
for i in range(n):
    li.append(list(map(int, list(input().split()))))

q = deque([[li, 0]])
answer = set()

while q:
    temp = q.popleft()
    if temp[1] >= 5:
        break
    else:
        br, mr = up(copy.deepcopy(temp[0]))
        q.append([br, temp[1] + 1])
        answer.add(mr)
        br, mr = down(copy.deepcopy(temp[0]))
        q.append([br, temp[1] + 1])
        answer.add(mr)
        br, mr = left(copy.deepcopy(temp[0]))
        q.append([br, temp[1] + 1])
        answer.add(mr)
        br, mr = right(copy.deepcopy(temp[0]))
        q.append([br, temp[1] + 1])
        answer.add(mr)

if answer:
    print(max(answer))

# Learned:
# 1. copy.deepcopy(): makes complete copy of an object. general .copy() still refers the inner objects.
# 2. deque: deque is more efficient than stacks or queues made from a list.