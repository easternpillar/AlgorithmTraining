# Problem:
# Reference: https://www.acmicpc.net/problem/21611

# My Solution: DENIED.
import sys


def makeSequence(b):
    seq = [0]
    length = 1
    r = c = len(b) // 2

    idx = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for i in range(0, len(b) - 1, 1):
        idx = idx % 4
        for j in range(0, length, 1):
            r += dx[idx]
            c += dy[idx]
            seq.append(b[r][c])
        idx += 1
        idx = idx % 4
        for j in range(0, length, 1):
            r += dx[idx]
            c += dy[idx]
            seq.append(b[r][c])
        idx += 1
        length += 1

    idx = idx % 4
    for j in range(0, length - 1, 1):
        r += dx[idx]
        c += dy[idx]
        seq.append(b[r][c])

    return seq


def ice(d, s):
    global sequence
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

    for i in range(len(seq) - 1, 0, -1):
        sequence.pop(seq[i])
        sequence.append(0)


def explosion():
    global sequence
    flag = True
    while flag:
        flag = False
        temp = []
        idx = 0
        prev = 0
        cnt = 1
        while idx < len(sequence) - 1:
            idx += 1
            if sequence[idx] == sequence[prev]:
                cnt += 1
            else:
                if cnt >= 4:
                    temp.append((prev, idx))
                prev = idx
                cnt = 1

        if temp:
            flag = True

            for i in range(len(temp) - 1, -1, -1):
                f, t = temp[i][0], temp[i][1]
                explosed[sequence[f]] += (t - f)
                sequence = sequence[:f] + sequence[t:]

            sequence.extend([0] * (N * N - len(sequence)))


def change():
    global sequence
    temp = [0]
    idx = 1
    prev = sequence[idx]
    cnt = 1
    while idx < len(sequence):
        idx += 1
        if sequence[idx] == 0:
            break

        if sequence[idx] == prev:
            cnt += 1
        else:
            temp.append(cnt)
            temp.append(prev)
            prev = sequence[idx]
            cnt = 1

    if len(temp) > len(sequence) ** 2:
        return temp[:len(sequence) ** 2]
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

for i in range(M):
    ice(directions[i], spaces[i])
    explosion()
    sequence = change()

answer = 0
for i in range(4):
    answer += explosed[i] * i

print(answer)
