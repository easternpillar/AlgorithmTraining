# Reference: https://www.acmicpc.net/problem/17143
import sys

R, C, M = map(int, sys.stdin.readline().split())
big = [[0 for _ in range(C)] for _ in range(R)]
sharks = set()
for i in range(M):
    temp = tuple(map(int, sys.stdin.readline().split()))
    big[temp[0] - 1][temp[1] - 1] = (temp[0] - 1, temp[1] - 1, temp[2], temp[3], temp[4])
    sharks.add((temp[0] - 1, temp[1] - 1, temp[2], temp[3], temp[4]))

pos = -1
answer = 0
while pos < C - 1:
    pos += 1
    for i in range(R):
        if big[i][pos] != 0:
            answer += big[i][pos][-1]
            sharks.discard(big[i][pos])
            break
    temp_sharks = set()
    big = [[0 for _ in range(C)] for _ in range(R)]
    while sharks:
        r, c, s, d, z = sharks.pop()
        ss = s
        new_d = d

        if d == 1:
            while ss != 0:
                while r != 0:
                    new_d = 1
                    r -= 1
                    ss -= 1
                    if ss == 0:
                        break
                if ss == 0:
                    break
                while r != R - 1:
                    new_d = 2
                    r += 1
                    ss -= 1
                    if ss == 0:
                        break
        elif d == 2:
            while ss != 0:
                while r != R - 1:
                    new_d = 2
                    r += 1
                    ss -= 1
                    if ss == 0:
                        break
                if ss == 0:
                    break
                while r != 0:
                    new_d = 1
                    r -= 1
                    ss -= 1
                    if ss == 0:
                        break
        elif d == 3:
            while ss != 0:
                while c != C - 1:
                    new_d = 3
                    c += 1
                    ss -= 1
                    if ss == 0:
                        break
                if ss == 0:
                    break
                while c != 0:
                    new_d = 4
                    c -= 1
                    ss -= 1
                    if ss == 0:
                        break
        elif d == 4:
            while ss != 0:
                while c != 0:
                    new_d = 4
                    c -= 1
                    ss -= 1
                    if ss == 0:
                        break
                if ss == 0:
                    break
                while c != C - 1:
                    new_d = 3
                    c += 1
                    ss -= 1
                    if ss == 0:
                        break

        temp_sharks.add((r, c, s, new_d, z))
        if big[r][c] == 0:
            big[r][c] = (r, c, s, new_d, z)
        else:
            if big[r][c][-1] < z:
                temp_sharks.discard(big[r][c])
                big[r][c] = (r, c, s, new_d, z)
            else:
                temp_sharks.discard((r, c, s, new_d, z))

    sharks = temp_sharks
print(answer)
