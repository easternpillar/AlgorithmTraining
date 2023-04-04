# Reference: https://www.acmicpc.net/problem/17779
import math
import sys

answer = math.inf
regions = []
N = int(sys.stdin.readline().strip())
tot = 0
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    tot += sum(temp)
    regions.append(temp)


def fun(start):
    global answer
    for d1 in range(1, start[1] + 1):
        for d2 in range(1, N - start[1] + 1):
            if d1 + d2 > N - start[0]:
                continue
            ones = twos = threes = fours = fives = 0
            for i in range(0, d1, 1):
                r = start[0] + i
                if not (0 <= r < N):
                    continue
                for c in range(0, start[1] - i):
                    ones += regions[r][c]
            for i in range(0, d2 + 1, 1):
                r = start[0] + i
                if not (0 <= r < N):
                    continue
                for c in range(start[1] + 1 + i, N, 1):
                    twos += regions[r][c]
            for i in range(0, d2 + 1, 1):
                r = start[0] + d1 + i
                if not (0 <= r < N):
                    continue
                for c in range(0, start[1] - d1 + i, 1):
                    threes += regions[r][c]
            for i in range(0, d1, 1):
                r = start[0] + d2 + 1 + i
                if not (0 <= r < N):
                    continue
                for c in range(start[1] + d2 - i, N, 1):
                    fours += regions[r][c]

            for i in range(0, start[0]):
                for j in range(0, start[1] + 1):
                    ones += regions[i][j]
            for i in range(0, start[0]):
                for j in range(start[1] + 1, N):
                    twos += regions[i][j]
            for i in range(start[0] + d1 + d2 + 1, N):
                for j in range(0, start[1] - d1 + d2):
                    threes += regions[i][j]
            for i in range(start[0] + d1 + d2 + 1, N):
                for j in range(start[1] - d1 + d2, N):
                    fours += regions[i][j]

            fives = tot - ones - twos - threes - fours
            answer = min(answer, max(ones, twos, threes, fours, fives) - min(ones, twos, threes, fours, fives))


for i in range(N - 2):
    for j in range(1, N - 1):
        fun((i, j))

print(answer)
