# Problem:
# Reference: https://www.acmicpc.net/problem/21611

# My Solution:
import sys


def makeSequence(b):
    seq = [0]
    length = 1
    r = c = len(b) // 2

    idx = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for i in range(len(b) - 1):
        idx = idx % 4
        for j in range(length):
            r += dx[idx]
            c += dy[idx]
            seq.append(b[r][c])
        idx += 1
        idx = idx % 4
        for j in range(length):
            r += dx[idx]
            c += dy[idx]
            seq.append(b[r][c])
        idx += 1
        length += 1

    idx = idx % 4
    for j in range(length - 1):
        r += dx[idx]
        c += dy[idx]
        seq.append(b[r][c])

    return seq


def ice(d, s):
    idx = 0
    seq = [0]
    if d == 1:
        while idx < s:
            seq.append(seq[idx] + 8 * idx + 7)
            idx += 1
    elif d == 2:
        while idx < s:
            seq.append(seq[idx] + 8 * idx + 3)
            idx += 1
    elif d == 3:
        while idx < s:
            seq.append(seq[idx] + 8 * idx + 1)
            idx += 1
    else:
        while idx < s:
            seq.append(seq[idx] + 8 * idx + 5)
            idx += 1

    return seq


def explosion(s):
    flag = True
    while flag:
        flag = False
        temp = []
        idx = 0
        prev = 0
        cnt = 1
        while idx < len(s) - 1:
            idx += 1
            if s[idx] == s[prev]:
                cnt += 1
            else:
                if cnt >= 4:
                    temp.append((prev, idx))
                prev = idx
                cnt = 1

        if temp:
            flag = True

        for f, t in list(reversed(temp)):
            explosed[s[f]] += (t - f)
            del s[f:t]

        if len(s) < N * N:
            s.extend([0] * (N * N - len(s)))


def change(s):
    temp = [0]
    idx = 1
    prev = s[idx]
    cnt = 1
    while idx < len(s):
        idx += 1
        if s[idx] == 0:
            break

        if s[idx] == prev:
            cnt += 1
        else:
            temp.append(cnt)
            temp.append(prev)
            prev = s[idx]
            cnt = 1

    if len(temp) > len(s) ** 2:
        return temp[:len(s) ** 2]
    else:
        add = N * N - len(temp)
        temp.extend([0] * add)
        return temp


explosed = [0 for _ in range(4)]
N, M = map(int, sys.stdin.readline().split())
board = []

for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

directions = []
spaces = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    directions.append(a)
    spaces.append(b)

sequence = makeSequence(board)
# print("시퀀스:", sequence)

for i in range(M):
    temp = ice(directions[i], spaces[i])
    temp.pop(0)
    for idx in sorted(temp, reverse=True):
        sequence.pop(idx)
        sequence.append(0)
    # print("얼음파편:", sequence)

    explosion(sequence)
    # print("폭발:", sequence)
    sequence = change(sequence)[:]
    # print("변화:", sequence)

answer = 0
for i in range(4):
    answer += explosed[i] * i

print(answer)
